#!/usr/bin/env python3
"""
mapas_cafe.py — Coffee Shop Checklists Kit Pro (EN) · DELTA del Kit de Tareas para Cafetería (`kit-tareas-cafeteria`,
11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `cafe/SPEC.md` (solo el delta). Segundo hermano
vertical, hecho como el bar (`bar/mapas_bar.py`). Sesión Claude Code, 18-oct-2026.

Se usa con `--kit cafe` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas, glosario de cafetería (puestos, unidades del inventario), calendario (misma estructura que el base: filas
5-26; cambian los eventos y las tareas de una coffee shop), POR_CELDA (caja 09, plagas 05 y fichajes heredados TAL
CUAL tras comprobar el texto ES; el resto, de la cafetería), VALORES_EN (mínimos del inventario en lb/oz y como
número), ADAPTAR, CLAVES (+ «⚠️ PEDIR») y REGLAS_US (+ espresso, leche, vitrina, hielo, mimosas). La hora de 12 h,
la caja en dólares y el resto se heredan. Las funciones del base que leen constantes (titulo_interior, autotest,
cruzar_censo) se re-enlazan a ESTE módulo. Ejecutado como script: autotest + cruce con cafe/censo_es.json + cruce con
el base (lo heredado por celda tiene en la cafetería el mismo texto ES que en el kit base).

    python3 cafe/mapas_cafe.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # cafe/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-cafeteria'
PRODUCTO = 'Coffee Shop Checklists Kit Pro'
TITULO_SEO = 'Coffee Shop Checklists Kit Pro: Coffee Shop Opening & Closing Checklist Templates for Excel'
SLUG = 'coffee-shop-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_COFFEE_SHOP_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Cafetería / Brunch · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Cafetería / Brunch',)
# heredar.py: memoria de traducción con VARIAS fuentes, en orden de preferencia (la primera que acierta gana).
# (nombre, carpeta junto a los scripts, sufijos de variante: cafetería → fuente; el EN de la fuente ya no lo lleva)
MEMORIA = [
    ('base', '', [(' — Cafetería / Brunch', ' — Restaurante Casual'), (' · Cafetería / Brunch', ' · Restaurante Casual')]),
    ('bar', 'bar', [(' — Cafetería / Brunch', ' — Bar / Cocktails'), (' · Cafetería / Brunch', ' · Bar / Cocktails')]),
]
# heredar.py: EN heredado que en una coffee shop no vale tal cual → pendientes (motivo «contexto»)
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|dining room|host stand|head chef|sous chef|'
                         r'prep cooks?|shift managers?|FOH managers?|bartenders?|barbacks?|cocktails?|draft|kegs?|'
                         r'liquor|beer|wine|21\+|venue|speed rail|ice well)\b')
# heredar.py: cadenas idénticas a una fuente cuyo EN se corrigió en la revisión de la cafetería (→ pendientes → G1.json)
NO_HEREDAR = {
    'Limpiar y desinfectar superficie de barra': 'ronda 1 M2: + tira de sanitizante',
    'Responsable general: _________________________': 'ronda 1 M5: «General manager» → «Manager»',
    'Desmontar mesas: recoger manteles, cubiertos, vasos': 'ronda 1 m11: placemats/napkins, como la apertura',
}
# gates_en.py G2 (ronda 1 M5): términos de restaurante que NINGUNA celda EN de la cafetería puede llevar (la firma de
# autor, «restaurant consultant», queda fuera por el lookahead). TERMINO_PROHIBIDO_EJEMPLO: lo que inyecta el autotest.
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:restaurants?(?! consultant)|dining rooms?|host stands?|head chefs?|sous chefs?|'
                       r'FOH managers?|general managers?|shift managers?|venues?|bartenders?|barbacks?)\b)|'
                       r'\b(?:GM|MOD)\b')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the host stand.'
REFERENCIAS_TRADUCTOR = ['cafe/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de la '
                         'prosa del kit base)', 'cafe/textos_en/heredado.json (cómo se dijo ya cada cosa: base y bar)',
                         'cafe/mapas_cafe.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, REGLAS_US',
                         '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'coffee shop checklist, cafe checklist, coffee shop opening checklist, coffee shop closing '
                 'checklist, barista checklist, cafe cleaning checklist, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-coffee-shop-opening-closing-checklists.xlsx'),
    ('02-partidas-cocina.xlsx', '02-cafe-kitchen-pastry-case-checklists.xlsx'),
    ('03-tareas-manager.xlsx', '03-coffee-shop-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-barista-checklist-duties-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-cafe-cleaning-checklist-inventory-maintenance.xlsx'),
    ('06-eventos-festivos.xlsx', '06-coffee-shop-event-checklists.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-blank-coffee-shop-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-cafe-opening-closing-checklist.xlsx'),
    ('09-apertura-cierre-caja.xlsx', '09-cash-drawer-opening-closing.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-coffee-shop-pre-shift-meeting-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-coffee-shop-holiday-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-coffee-shop-opening-closing-checklists.xlsx',
     'Coffee Shop Opening & Closing Checklists: Espresso Bar, Kitchen & FOH'),
    ('02-cafe-kitchen-pastry-case-checklists.xlsx', 'Cafe Kitchen Checklists: Hot Line, Cold Station & Pastry Case'),
    ('03-coffee-shop-manager-checklist.xlsx', 'Coffee Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover'),
    ('04-barista-checklist-duties-by-role.xlsx',
     'Barista Checklist & Daily Duties by Role (Shift Lead, Barista, Baker, Server, Busser)'),
    ('05-cafe-cleaning-checklist-inventory-maintenance.xlsx', 'Cafe Cleaning Checklist, Inventory & Maintenance Schedule'),
    ('06-coffee-shop-event-checklists.xlsx',
     "Coffee Shop Event Checklists: Sunday Brunch, Valentine's Day, Holiday Season & Patio"),
    ('07-blank-coffee-shop-checklist-template.xlsx', 'Blank Coffee Shop Checklist Template (Editable)'),
    ('08-cafe-opening-closing-checklist.xlsx', 'Cafe Opening & Closing Checklist (Whole Shop)'),
    ('09-cash-drawer-opening-closing.xlsx', 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log'),
    ('BONUS-01-coffee-shop-pre-shift-meeting-template.xlsx', 'BONUS: Coffee Shop Pre-Shift Meeting Template (Huddle Notes)'),
    ('BONUS-02-coffee-shop-holiday-calendar.xlsx', 'BONUS: Coffee Shop Holiday & Events Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Apertura Barra Café', 'Espresso Bar Opening'), ('Cierre Barra Café', 'Espresso Bar Closing'),
    ('Pastelería Vitrina', 'Pastry Case'),
    ('Encargado', 'Shift Lead'), ('Barista', 'Barista'), ('Pastelero', 'Baker'), ('Auxiliar', 'Busser & Runner'),
    ('Inventario Diario', 'Daily Inventory'), ('Inventario Semanal', 'Weekly Inventory'),
    ('Brunch Dominical', 'Sunday Brunch'), ('Navidad', 'Holiday Season'),
    ('Apertura del Negocio', 'Cafe Opening'), ('Cierre del Negocio', 'Cafe Closing'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Apertura Cocina', 'Apertura Sala', 'Apertura Barra Café', 'Cierre Cocina', 'Cierre Sala',
            'Cierre Barra Café']),
    ('02', ['Instrucciones', 'Calientes', 'Fríos', 'Pastelería Vitrina']),
    ('03', ['Instrucciones', 'Diario Manager', 'Semanal Manager', 'Mensual Manager', 'Handover Turno']),
    ('04', ['Instrucciones', 'Encargado', 'Barista', 'Pastelero', 'Camarero', 'Auxiliar']),
    ('05', ['Instrucciones', 'Inventario Diario', 'Inventario Semanal', 'Limpieza Semanal', 'FIFO Semanal',
            'Mantenimiento Mensual', 'Trimestral y Anual']),
    ('06', ['Instrucciones', 'Brunch Dominical', 'San Valentín', 'Navidad', 'Temporada Terraza']),
    ('07', ['Instrucciones', 'Por Franja Horaria', 'Por Área', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Apertura de Caja', 'Cierre de Caja', 'Registro Mensual']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario Anual']),
])

# ==========================================================================
# GLOSARIO: el base entero (opcional en la cafetería) + celdas cortas de la cafetería. Jerga de coffee shop US:
# shift lead (no shift manager), barista, baker, busser; unidades del inventario en lb / oz / qt (VALORES_EN).
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
_GLOSARIO_CAFE = OrderedDict([
    ('Encargado', 'Shift lead'), ('Encargado/a', 'Shift lead'), ('Barista', 'Barista'),
    # ronda 1 M5: roles y zonas del base que en una coffee shop no existen (07 «By Role», 08, 09)
    ('Jefe de Cocina', 'Kitchen lead'), ('Jefe de Sala', 'Shift lead'), ('Gerente', 'Manager'),
    ('Recepción', 'Front counter'), ('Responsable de caja', 'Cashier / shift lead'),
    ('Pastelero/a', 'Baker'), ('Camarero/a', 'Server'), ('Auxiliar', 'Busser / runner'),
    ('Camarero/a apertura', 'Opening server'), ('Camarero/a cierre', 'Closing server'),
    ('Cocinero calientes', 'Hot line cook'), ('Cocinero fríos', 'Cold station cook'),
    ('Turno saliente', 'Outgoing shift'),
    ('Técnico SAT', 'Espresso tech'), ('Técnico/Barista', 'Tech / barista'),
    ('Office', 'Office'), ('Almacén', 'Storage'), ('Cámara', 'Walk-in'),
    ('Primavera', 'Spring'), ('Otoño', 'Fall'),
    ('Dic 1', 'Dec 1'), ('20 Dic', 'Dec 20'), ('23 Dic', 'Dec 23'), ('7 Ene', 'Jan 7'),
    # inventario (05): unidades US; los mínimos de kg y g cambian de cifra (VALORES_EN), los de L y uds no (1 qt ≈ 1 L)
    ('kg', 'lb'), ('g', 'oz'), ('L', 'qt'), ('uds', 'ea'), ('doc', 'doz'), ('Unidad', 'Unit'),
])
GLOSARIO.update(_GLOSARIO_CAFE)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Encargado/a', 'Barista', 'Pastelero/a', 'Camarero/a', 'Camarero/a apertura',
                                           'Camarero/a cierre', 'Cocinero calientes', 'Cocinero fríos',
                                           'Turno saliente', 'Técnico SAT', 'Técnico/Barista',
                                           'Office', 'Almacén', 'Cámara'})

# ==========================================================================
# CLAVES: el inventario diario avisa con «⚠️ PEDIR» / «OK» (literales de fórmula)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([('⚠️ PEDIR', '⚠️ REORDER'), ('OK', 'OK')])

# ==========================================================================
# BONUS-02 «Holiday Calendar»: misma estructura que el base (filas 5-26: A mes · B fecha/evento · C tareas ·
# D antelación). A, B y D fijados; C = traductor, con ADAPTAR donde la tarea de cafetería cambia.
# fila → (mes, evento, antelación, ADAPTAR de C o None). Lo que no cambia, del base.
# ==========================================================================
CALENDARIO = OrderedDict(_base.CALENDARIO)
CALENDARIO.update([
    (7, ('February', "Feb 14 — Valentine's Day", '2 weeks',
         'Cafetería: menú para parejas de desayuno / brunch (no «date night»), decoración romántica, turnos extra')),
    (6, ('January', 'Jan 6 — King cake season begins', '1 week',
         'Sustituye a Reyes: el roscón → King cake (del 6 de enero, Epiphany, al Mardi Gras; sobre todo en Luisiana y '
         'la costa del Golfo). Tareas: King cake por encargo y en la vitrina si encaja con tu zona, menú familiar')),
    (9, ('March', "Mar 17 — St. Patrick's Day", '2 weeks',
         'Sustituye al Día del Padre (en EE. UU. va en junio, fila 16). Tareas de cafetería: bebidas y bollería '
         'temáticas (sin alcohol), decoración')),
    (10, ('March–April', 'Easter Sunday (varies)', '2 weeks',
          'Sustituye a Semana Santa (sin bacalao, potaje ni torrijas). Tareas: brunch de Pascua, bollería de temporada '
          '(hot cross buns), reservas ampliadas')),
    (12, ('May–June', 'Graduation season', '1 month',
          'Mismas tareas del ES (menú de grupo cerrado, depósito y precio por persona, tartas por encargo → custom cake '
          'orders); en EE. UU. son graduaciones y baby/bridal showers')),
    (13, ('May', 'Teacher Appreciation Week (1st full week of May)', '1 week',
          'Sustituye al 1 de mayo. Tareas: promoción para profesores y colegios (pedidos de café para llevar en termo y '
          'bandejas de bollería), turnos especiales')),
    (15, ('May', 'Memorial Day (last Monday)', '1 month',
          'Sustituye a «Inicio temporada alta». Tareas: reforzar plantilla, stock de verano (bebidas frías, cold brew '
          'si lo sirves, hielo), patio a pleno')),
    (16, ('June', "3rd Sunday — Father's Day", '2 weeks',
          'Sustituye a San Juan. Tareas = las del Día del Padre del ES (fila 9): desayuno / brunch familiar, reservas '
          'ampliadas, detalle para el padre')),
    (17, ('July', 'Jul 4 — Independence Day', '1 week',
          'Sustituye a la fila de temporada alta (sus tareas pasan a la fila 18). Tareas: decidir el horario (abrir '
          'solo por la mañana o cerrar), patio a pleno rendimiento, refuerzo de bebidas frías y hielo')),
    (19, ('September', 'Back to school + Sep 29 — National Coffee Day', '2 weeks',
          'Sustituye a «Vuelta al cole / rutina». Tareas: carta de otoño (fall drinks) y desayuno reforzado para la '
          'vuelta a la rutina; el 29 de septiembre es el National Coffee Day: bebida o promoción del día y aviso en '
          'redes')),
    (20, ('October', 'Oct 31 — Halloween', '1 week', 'Decoración temática; bebidas y bollería especiales (sin cócteles)')),
    (21, ('November', 'Thanksgiving (4th Thursday)', '1 month',
          'Sustituye a Todos los Santos (la bollería de temporada → pedidos de tartas de Thanksgiving: pumpkin y pecan '
          'pie). Tareas: decidir si se abre el jueves, pedidos de tartas y bollería para llevar, turnos del miércoles')),
    (23, ('Nov–Dec', 'Holiday gift card season', '2 weeks',
          'Sustituye al puente de la Constitución. Del Black Friday a Nochebuena. Tareas: promoción de tarjetas regalo, '
          'expositor junto a la caja (register), venta online')),
    (24, ('December', 'Holiday catering (office orders)', '1 month',
          'Sustituye a las cenas de empresa. Tareas: pedidos de empresa (café para llevar en termo y bandejas de '
          'bollería), reservas de grupo, turnos extra')),
    (26, ('December', "Dec 31 — New Year's Eve", '2 weeks',
          'Sin uvas, cava ni cotillón español. Tareas: decidir el horario (cerrar pronto o abrir de noche); si '
          'abres de noche, party favors y brindis a medianoche sin alcohol (o con champán solo si tu licencia lo '
          'permite; 21+ con ID), turnos')),
])

# ==========================================================================
# POR_CELDA: lo heredado del base (mismo texto ES en la misma celda o en la fila equivalente; lo comprueba
# cruzar_base) + lo de la cafetería
# ==========================================================================
_HEREDA_POR_CELDA = [k for k in _base.POR_CELDA if k[0] == '09'] + [
    ('05', 'Trimestral y Anual', 'B6'), ('05', 'Trimestral y Anual', 'D6'), ('05', 'Trimestral y Anual', 'E6')]
POR_CELDA = OrderedDict((k, _base.POR_CELDA[k]) for k in _HEREDA_POR_CELDA)
_T = ('05', 'Trimestral y Anual')
POR_CELDA.update([
    # 03 · conservación de fichajes (B16 en el base; mismo texto EN)
    (('03', 'Mensual Manager', 'B15'), _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]),
    # 02 · pescado ahumado o crudo: destrucción de parásitos (D10, FDA Food Code 3-402.11)
    # (errata de texto del 18-oct-2026: las TRES opciones de 3-402.11 con la temperatura de cada tramo; registro 3-402.12)
    (('02', 'Calientes', 'B9'),
     'Smoked salmon and fish served raw — parasite destruction (FDA Food Code 3-402.11): get the supplier\'s freezing '
     'record (frozen at −4 °F or below for 7 days; or at −31 °F or below until solid, then 15 h at −31 °F or below or '
     '24 h at −4 °F or below) or freeze it yourself; log the lot and keep the record 90 days (FDA Food Code '
     '3-402.12)'),
    # 05 · Inventario: la línea de marca va con otro formato en el ES (dos puntos y raya final) → la del kit con su
    # raya final (no es la línea D19: G3 cuenta las MARCA_EN contra las MARCA_ES del ES)
    (('05', 'Inventario Diario', 'A48'), MARCA_EN + ' —'), (('05', 'Inventario Semanal', 'A58'), MARCA_EN + ' —'),
    # 05 · Trimestral y Anual: servicios contratados US de una coffee shop
    (_T + ('B7',), 'Hood and duct cleaning by a certified contractor if the cafe cooks under a hood (NFPA 96: '
                   'semiannual if moderate volume, quarterly if high volume, annual only for low-volume operations); '
                   'hood fire suppression inspected every 6 months'),
    (_T + ('D7',), 'Hood cleaning co.'), (_T + ('E7',), 'Semiannual'),
    (_T + ('B8',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record '
                   '(OSHA 1910.157); hydrostatic tests per the label'),
    (_T + ('D8',), 'Fire safety co.'),
    (_T + ('B9',), 'Legionella: if you have a cooling tower or at-risk hot water, keep a water management program as '
                   'your local health code requires'),
    (_T + ('D9',), 'Water treatment co.'),
    (_T + ('B11',), 'Gas lines and appliance connections checked by a licensed pro if the cafe has gas (as often as '
                    'your local code requires)'),
    (_T + ('D11',), 'Licensed plumber'), (_T + ('E11',), 'Annual'),
    (_T + ('B12',), 'Refrigeration service by an EPA 608-certified tech: walk-in, reach-ins and refrigerated pastry '
                    'case — coils, gaskets and refrigerant leak check'),
    (_T + ('D12',), 'Refrigeration tech'),
    (_T + ('B13',), 'Used cooking oil pickup by a licensed recycler if you have a fryer: file the pickup receipts'),
    (_T + ('D13',), 'Oil recycler'),
    (_T + ('B21',), "Review insurance (general liability, property, workers' comp; liquor liability if you serve "
                    'alcohol) and renewal dates'),
    (_T + ('B22',), 'POS check: software updates, sales tax rates and settings, user permissions'),
    # ronda 1 m1: la apertura del local va a la hora de la primera tarea (la pastelería hornea a las 6:30 AM; errata ES)
    (('08', 'Apertura del Negocio', 'E5'), '6:30 AM'), (('08', 'Apertura del Negocio', 'E6'), '6:30 AM'),
    (('08', 'Apertura del Negocio', 'E7'), '6:30 AM'), (('08', 'Apertura del Negocio', 'E8'), '6:30 AM'),
    (('04', 'Encargado', 'E6'), '6:30 AM'),
    # ronda 1 m14: el 05 no promete hojas protegidas que no lo están (los inventarios van sin proteger; errata ES)
    (('05', 'Instrucciones', 'B23'), '▸ Checklist sheets with formulas are protected WITHOUT a password: the input cells '
                                     '(the green ones) are unlocked. The two inventory sheets are left unprotected so '
                                     "you can add products: don't type over the Status or Total value columns."),
    # ronda 1 m15: «15 días antes» bajo «PREPARACIÓN (2 SEMANAS ANTES)»
    (('06', 'Navidad', 'E6'), '2 weeks out'), (('06', 'Navidad', 'E8'), '2 weeks out'),
    # ronda 1 m12: el bacon se compra por libras
    (('05', 'Inventario Diario', 'C34'), 'lb'),
])
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'A%d' % _fila)] = _mes
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = _antel

# ==========================================================================
# VALORES_EN: (libro, hoja ES, celda) → (valor ES tal cual, valor EN). Los mínimos del «Inventario Diario» vienen
# como TEXTO en el ES («2»): la fórmula «B<D» compara un número con un texto y pide SIEMPRE (errata ES). La EN los
# escribe como NÚMERO; los de kg y g, convertidos a lb y oz (×2,2 y ÷28,35, redondeado a una cifra de pedido).
# ==========================================================================
_MINIMOS = [  # fila, ES, EN
    (6, '2', 4), (7, '1', 2), (8, '0.5', 1), (10, '5', 5), (11, '3', 3), (12, '3', 3), (13, '2', 2), (14, '2', 2),
    (15, '1', 1), (17, '0.5', 1), (18, '100', 4), (19, '0.5', 0.5), (20, '0.5', 0.5), (21, '20', 20), (22, '3', 3),
    (24, '10', 10), (25, '8', 8), (26, '6', 6), (27, '12', 12), (28, '10', 10), (29, '8', 8), (31, '30', 30),
    (32, '6', 6), (33, '300', 10), (34, '500', 1), (35, '250', 8), (36, '250', 8), (37, '2', 4), (38, '0.5', 1),
    (40, '50', 50), (41, '30', 30), (42, '80', 80), (43, '30', 30), (44, '100', 100),
]
VALORES_EN = OrderedDict((('05', 'Inventario Diario', 'D%d' % f), (es, en)) for f, es, en in _MINIMOS)

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_TEMP_FRIO = _A[('01', 'Cierre Cocina', 'B12')]
_VITRINA_FRIA = ('°F: vitrina refrigerada (refrigerated pastry case) a 41 °F o menos para lo TCS: tartas de crema, '
                 'cheesecake, rellenos lácteos (FDA Food Code 3-501.16); coletilla «— log reading: ____ °F»; °C solo '
                 'entre paréntesis si cabe')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act): en bollería sobre todo trigo, huevo, leche, '
              'soja, frutos de cáscara (tree nuts), cacahuete y sésamo; en UK, los 14')
_SIN_MANO = ('FDA Food Code 3-301.11: sin mano desnuda en lo listo para consumir: pinzas, papel de pastelería (bakery '
             'tissue) o guantes')
_DATE_BOLLERIA = ('Date marking US: etiqueta con la fecha; lo TCS (cremas, cheesecake, rellenos lácteos) a 41 °F o '
                  'menos y 7 días como máximo contando el día de preparación (FDA Food Code 3-501.17)')
_LAVAVAJILLAS = ('Lavavajillas = dish machine: filtros y rinse aid; la sal, solo si la máquina lleva descalcificador '
                 '(water softener)')
_DESCALE = ('Descalcificar = «descale … per the manufacturer\'s instructions» (en muchas máquinas comerciales lo hace '
            'el técnico); sin cifras ni productos que no diga el fabricante')
_HEREDA_ADAPTAR = [('08', 'Apertura del Negocio', 'B8'), ('09', 'Cierre de Caja', 'B10'),
                   ('09', 'Registro Mensual', 'A37'),
                   ('B02', 'Instrucciones', 'B8')] + [k for k in _A if k[:2] == ('09', 'Instrucciones')]
ADAPTAR = OrderedDict((k, _A[k]) for k in _HEREDA_ADAPTAR)
ADAPTAR.update([
    # 01 · cocina y sala (mismas instrucciones que el base en las filas equivalentes)
    (('01', 'Apertura Cocina', 'B7'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Apertura Cocina', 'B9'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Apertura Cocina', 'B10'), _A[('01', 'Apertura Cocina', 'B10')]),
    (('01', 'Apertura Cocina', 'B13'), _A[('01', 'Apertura Cocina', 'B14')]),
    (('01', 'Apertura Cocina', 'B16'), 'Baño maría = steam table / bain-marie: lo que se mantiene en caliente, a 135 °F '
     'o más (FDA Food Code 3-501.16)'),
    (('01', 'Apertura Cocina', 'B17'), _A[('01', 'Apertura Cocina', 'B18')]),
    (('01', 'Apertura Sala', 'B18'), _A[('01', 'Apertura Sala', 'B19')]),
    (('01', 'Cierre Cocina', 'B6'), _A[('01', 'Cierre Cocina', 'B6')]),
    (('01', 'Cierre Cocina', 'B16'), _A[('02', 'Calientes', 'B27')]),
    (('01', 'Cierre Cocina', 'B21'), _TEMP_FRIO),
    (('01', 'Cierre Sala', 'B15'), _A[('01', 'Apertura Sala', 'B19')]),
    (('01', 'Cierre Sala', 'B24'), 'Cuadrar las propinas del día (tip jar y propinas de tarjeta) y repartirlas según la '
     'política de la casa (tip pool); sin más afirmaciones legales'),
    # 01 · barra de café (espresso bar)
    (('01', 'Apertura Barra Café', 'B8'), 'Dial in: deja «25–30 s» y «25–30 ml» (así habla un barista US) y añade '
     '«(about 1 fl oz)» tras los ml'),
    (('01', 'Apertura Barra Café', 'B14'), 'Leches: whole, skim (nonfat), oat, soy y almond. Alérgenos US entre los 9: '
     'milk, soy y tree nuts (almendra); la avena no lo es'),
    (('01', 'Apertura Barra Café', 'B22'), 'Jarras de leche (milk pitchers) frías: la leche sale de la nevera a 41 °F '
     'o menos y vuelve a ella; una jarra por tipo de leche (la de vaca, la de soja y la de almendra son alérgenos)'),
    (('01', 'Apertura Barra Café', 'B23'), 'FDA Food Code: el hielo es un alimento. Cubitera = ice bin, limpia; pala '
     '(ice scoop) fuera del hielo o con el mango hacia fuera; nunca el vaso'),
    (('01', 'Apertura Barra Café', 'B31'), _ALERGENOS),
    (('01', 'Apertura Barra Café', 'B32'), _VITRINA_FRIA),
    (('01', 'Apertura Barra Café', 'B33'), _SIN_MANO),
    (('01', 'Cierre Barra Café', 'B6'), 'Backflush diario con detergente para espresso (tabletas o polvo), grupo a '
     'grupo, según las instrucciones del fabricante de la máquina'),
    (('01', 'Cierre Barra Café', 'B10'), 'Cajón de borra → knock box (vaciar los posos)'),
    (('01', 'Cierre Barra Café', 'B18'), _DATE_BOLLERIA + '; la bollería seca, con la fecha del día'),
    (('01', 'Cierre Barra Café', 'B20'), 'Leche abierta (y el cold brew, si lo sirves) a la nevera a 41 °F o menos, '
     'tapada y con date marking: 7 días como máximo contando el día de apertura, sin pasar del use-by del fabricante '
     '(FDA Food Code 3-501.17(B))'),
    (('01', 'Cierre Barra Café', 'B16'), 'Ronda 1 M3: + si sirves cold brew, arrancar el lote de mañana en un recipiente '
     'limpio y tapado, en frío salvo que tu departamento de salud permita el reposo a temperatura ambiente'),
    (('01', 'Cierre Barra Café', 'B24'), 'Ronda 1 M2: + comprobar el sanitizante con una tira (rango de su etiqueta)'),
    (('01', 'Apertura Barra Café', 'B25'), 'Ronda 1 M3: + si sirves cold brew, filtrar el lote que terminó el reposo y '
     'guardarlo tapado a 41 °F o menos, con date marking (7 días como máximo contando el día de preparación)'),
    (('01', 'Apertura Cocina', 'B24'), 'Ronda 1 M4: hollandaise con huevo pasteurizado; a 135 °F o más, o con la hora '
     'marcada y a la basura a las 4 h (FDA Food Code 3-501.19)'),
    (('01', 'Apertura Cocina', 'B35'), 'Ronda 1 M2: sanitizante aprobado a la concentración de la etiqueta, medida con '
     'tira'),
    (('01', 'Cierre Cocina', 'B14'), 'Ronda 1 M2: + comprobar el sanitizante con una tira (rango de su etiqueta)'),
    (('02', 'Calientes', 'B16'), 'Ronda 1 M4: la yema líquida pide el aviso al consumidor en la carta salvo huevo '
     'pasteurizado (FDA Food Code 3-603.11)'),
    (('04', 'Barista', 'B11'), 'Ronda 1 M3: + filtrar el cold brew, si lo sirves'),
    # 02
    (('02', 'Fríos', 'B6'), _A[('02', 'Fríos', 'B6')]),
    (('02', 'Fríos', 'B17'), _TEMP_FRIO),
    (('02', 'Pastelería Vitrina', 'B12'), _SIN_MANO),
    (('02', 'Pastelería Vitrina', 'B13'), _ALERGENOS),
    (('02', 'Pastelería Vitrina', 'B14'), _VITRINA_FRIA),
    (('02', 'Pastelería Vitrina', 'B24'), _DATE_BOLLERIA),
    # 03
    (('03', 'Semanal Manager', 'B8'), _A[('03', 'Diario Manager', 'B29')]),
    (('03', 'Mensual Manager', 'B10'), 'Plataformas US: DoorDash, Uber Eats y Grubhub'),
    (('03', 'Mensual Manager', 'B17'), _DESCALE),
    (('03', 'Mensual Manager', 'B20'), _LAVAVAJILLAS),
    # 04
    (('04', 'Barista', 'B21'), 'Backflush con detergente para espresso, según las instrucciones del fabricante'),
    (('04', 'Pastelero', 'B12'), _ALERGENOS),
    (('04', 'Pastelero', 'B18'), _DATE_BOLLERIA),
    (('04', 'Auxiliar', 'B17'), '«Office» aquí es la zona de friegue (dish pit), no la oficina: friegue final de toda '
     'la vajilla pendiente'),
    # 05
    (('05', 'Instrucciones', 'B6'), 'Describe la lista US de la hoja «Quarterly & Annual»: control de plagas, campana '
     '(si se cocina bajo campana), extintores, legionela, gas, frío, aceite usado, filtro de agua y servicio técnico '
     'de la máquina de espresso, muelas del molinillo, termómetros, seguros y POS / sales tax. Sin DDD, BIE, '
     'Verifactu ni facturación española'),
    (('05', 'Inventario Semanal', 'A6'), 'Unidad US: lb; «bolsas 1kg» → «2 lb bags» (1 kg ≈ 2.2 lb)'),
    (('05', 'Limpieza Semanal', 'B10'), 'Sanitizar con un sanitizante aprobado a la concentración de la etiqueta, medida '
     'con tiras (test strips) (FDA Food Code 4-501.114); sin «lejía» a ojo'),
    (('05', 'FIFO Semanal', 'B9'), _TEMP_FRIO),
    (('05', 'FIFO Semanal', 'B11'), 'Leche abierta: fuera a los 7 días contando el de apertura o en el use-by de la '
     'etiqueta, lo que llegue antes (FDA Food Code 3-501.17(B)); a 41 °F o menos'),
    (('05', 'Mantenimiento Mensual', 'B6'), _DESCALE),
    (('05', 'Mantenimiento Mensual', 'B16'), _LAVAVAJILLAS),
    (('05', 'Mantenimiento Mensual', 'B21'), _A[('05', 'Mantenimiento Mensual', 'B21')]),
    (('05', 'Trimestral y Anual', 'B18'), 'Peso US: planas 880–1,320 lb (400–600 kg), cónicas 1,760–2,650 lb '
     '(800–1,200 kg); orientativo, manda el fabricante del molinillo'),
    (('05', 'Trimestral y Anual', 'B19'), _A[('05', 'Trimestral y Anual', 'B23')]),
    # 06
    (('06', 'Brunch Dominical', 'B23'), 'Mimosa / bellini solo si tu licencia de alcohol lo permite (beer & wine '
     'license) y a mayores de 21 con ID'),
    (('06', 'San Valentín', 'B7'), 'Champán (champagne) solo si tu licencia de alcohol lo permite'),
    (('06', 'San Valentín', 'B10'), 'Alérgenos US: los 9 principales; ejemplos: trigo (gluten), frutos de cáscara '
     '(tree nuts) y cacahuete, leche, huevo'),
    (('06', 'San Valentín', 'B16'), 'Bebida de bienvenida para parejas: sin alcohol, o una mimosa solo donde tu '
     'licencia y tu estado permiten regalar alcohol (21+ con ID)'),
    (('06', 'Temporada Terraza', 'B6'), _A[('06', 'Temporada Terraza', 'B6')] + ': comprobar que está vigente y '
     'renovarlo si caduca esta temporada'),
    (('06', 'Navidad', 'B7'), 'Sin turrón ni cava: panettone, galletas de temporada (holiday cookies) y chocolate para '
     'el hot chocolate especial'),
    (('06', 'Navidad', 'B17'), 'Sin roscón: panettone, stollen y galletas de temporada (holiday cookies)'),
    (('06', 'Navidad', 'B18'), 'Sin turrón ni polvorón: una galleta de temporada (p. ej. gingerbread) con el café'),
    (('06', 'Navidad', 'B23'), 'Retirar la decoración navideña la primera semana de enero (sin Reyes)'),
    # BONUS-01
    (('B01', 'Briefing', 'B2'), 'Turnos de cafetería: ☐ AM ☐ PM (sin comida / cena); «Encargado» → «Shift lead»'),
])
for _fila, (_mes, _evento, _antel, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)
# Celdas ES con °C cuya EN NO lleva cifra en °F (el filtrado del aceite sigue al fabricante, como en el base)
CELSIUS_SIN_F = frozenset({('01', 'Cierre Cocina', 'B16')})

# ==========================================================================
# REGLAS_US: las del base + las de la cafetería (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('leche', ('leche y alternativas abiertas a 41 °F o menos; 7 días desde la apertura (día 1), sin pasar el use-by '
               'del fabricante', 'FDA Food Code 2022 §3-501.16 y §3-501.17(B)')),
    ('cold_brew', ('a 41 °F o menos, tapado y con fecha, 7 días; el reposo, donde lo permita el departamento de salud',
                   'FDA Food Code 2022 §3-501.16 y §3-501.17; [local] departamento de salud')),
    ('tphc', ('4 h sin control de temperatura con la hora marcada; después, a la basura', 'FDA Food Code 2022 §3-501.19(B)')),
    ('alergenos_leches', ('milk, soy y tree nuts están entre los 9; la avena no', 'FALCPA 2004 + FASTER Act 2021')),
    ('vitrina', ('vitrina refrigerada a 41 °F o menos para lo TCS; date marking 7 días',
                 'FDA Food Code 2022 §3-501.16 y §3-501.17')),
    ('mano_desnuda', ('sin mano desnuda en alimentos listos para consumir', 'FDA Food Code 2022 §3-301.11')),
    ('hielo', ('el hielo es un alimento: pala, nunca el vaso', 'FDA Food Code 2022, «food» incluye el hielo')),
    ('backflush', ('backflush diario con detergente; descalcificación según el fabricante',
                   '[fabricante] manual de la máquina de espresso')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol, en todos los estados',
                      'National Minimum Drinking Age Act of 1984 (23 U.S.C. 158)')),
    ('alcohol_gratis', ('regalar alcohol está restringido en algunos estados', '[estatal] ABC / liquor authority')),
    ('muelas', ('planas 400-600 kg = 880-1.320 lb · cónicas 800-1.200 kg = 1.760-2.650 lb',
                '[criterio del kit] cifras del ES convertidas')),
    ('inventario', ('mínimos de kg → lb (×2,2) y de g → oz (÷28,35); L → qt (1 qt ≈ 0,95 L)',
                    '[criterio del kit] conversión')),
    ('national_coffee_day', ('National Coffee Day el 29 de septiembre', '[criterio del kit] fecha comercial US')),
    ('teacher_week', ('Teacher Appreciation Week, la primera semana completa de mayo', '[criterio del kit] National PTA')),
])
# °F que el kit puede afirmar (G7): las del base
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 70, 100, 135, 165}

# ==========================================================================
# Pistas y dependencias de la cafetería (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {r'Kit de Tareas': 'D2: «Coffee Shop Checklists Kit Pro»'}
PISTAS_FUERA = (r'Restaurante Casual',)
PISTAS_EXTRA = [
    (r'Cafetería / Brunch', 'D2: la EN no lleva el sufijo de variante: quita «— Cafetería / Brunch»'),
    (r'[Cc]afeter[ií]a', 'cafetería → coffee shop o cafe (SIN tilde: nunca «café» con tilde en inglés)'),
    (r'[Mm]áquina de espresso|[Gg]rupos?\b|[Pp]ortafiltro', 'Espresso US: máquina de espresso → espresso machine; '
                                                           'grupo → group head; portafiltro → portafilter'),
    (r'[Ll]an[cz]a? de vapor|[Ll]ance', 'lanza / lance de vapor → steam wand; purgar → purge'),
    (r'[Mm]olinillo|[Mm]olienda|[Mm]uelas|[Tt]olva', 'molinillo → grinder; calibrar la molienda → dial in; muelas → '
                                                     'burrs; tolva → hopper'),
    (r'[Jj]arrit|[Jj]arra', 'jarritas de leche → milk pitchers'),
    (r'[Bb]orra|[Pp]osos', 'cajón de borra → knock box; posos → grounds'),
    (r'[Bb]atch brew|[Cc]afé filtro|[Tt]ermos?', 'café filtro → drip / batch brew; termo → airpot'),
    (r'[Vv]itrina', 'vitrina → pastry case (refrigerada: refrigerated pastry case)'),
    (r'[Bb]oller[ií]a', 'bollería → pastries / baked goods'),
    (r'[Tt]ake-away|[Pp]ara llevar', 'take-away → to-go'),
    (r'[Pp]izarra', 'pizarra → menu board / chalkboard'),
    (r'[Ll]eches?|[Nn]ata', 'leche entera → whole milk; desnatada → skim (nonfat); avena / soja / almendra → oat / soy '
                            '/ almond milk; nata para montar → heavy whipping cream'),
    (r'[Ss]irope', 'sirope → syrup'),
    (r'[Zz]umo', 'zumo → juice'),
    (r'[Tt]ortitas', 'tortitas → pancakes'),
    (r'[Cc]ubitera', 'cubitera → ice bin; pala → ice scoop'),
    (r'[Pp]ropinas?', 'bote de propinas → tip jar'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'Glovo', 'Glovo → DoorDash (plataformas US: DoorDash, Uber Eats, Grubhub)'),
    (r'SAT\b', 'SAT → espresso tech / service tech'),
    (r'[Ee]ncargad|[Rr]esponsable (de )?turno', 'encargado/a / responsable de turno → shift lead (no «shift manager»)'),
    (r'[Jj]efe de [Ss]ala', 'en la cafetería no hay FOH manager: shift lead o manager'),
    (r'\bMínimo\b', 'Mínimo (de stock) → Par (par level)'),
    (r'[Bb]riks?', 'brik → carton (half-gallon / gallon)'),
    (r'[Aa]utoservicio', 'barra de autoservicio → self-serve station / condiment bar'),
    (r'[Ll]ocal\b', 'el local → the cafe / the shop (nunca «restaurant» ni «venue»)'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Cafetería / Brunch»', r'Cafetería / Brunch', 'D2: la EN no lleva sufijo')),
    ('espresso', ('Máquina de espresso: backflush, descalcificación, técnico', r'[Bb]ackflush|[Dd]escalcific|SAT\b',
                  'D-CAFE: backflush diario con detergente y descale según el fabricante')),
    ('leche', ('Leches y alternativas vegetales', r'[Ll]eches?\b', 'D-CAFE: 41 °F, fecha de la etiqueta, alérgenos '
               '(milk, soy, tree nuts)')),
    ('alcohol', ('Alcohol en el brunch', r'[Mm]imosa|[Bb]ellini|[Cc]ava\b', 'D-CAFE: solo con licencia, 21+ con ID; '
                 'regalarlo, según el estado')),
])

# aplicar_en.capa_ajuste (gancho de la ghost kitchen; errata de texto del 18-oct-2026): 02 «Hot Line» B9 va sin ajuste en el ES y
# ya salía cortada en la EN; con las TRES opciones de 3-402.11 se alarga más: se activa el ajuste (la fila es automática
# y crece). Sin la constante, el resto del kit no cambia
AJUSTE_FORZADO = frozenset({('02', 'Calientes', 'B9')})


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)


def autotest():
    err = _autotest_base()
    for k, (es, en) in VALORES_EN.items():
        if not isinstance(en, (int, float)) or isinstance(en, bool) or en <= 0:
            err.append('VALORES_EN: el EN de %r debe ser un número > 0: %r' % (k, en))
        if k in POR_CELDA or k in ADAPTAR:
            err.append('VALORES_EN y POR_CELDA/ADAPTAR sobre la misma celda: %r' % (k,))
    import re
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for k, v in list(GLOSARIO.items()) + list(POR_CELDA.items()):
        if k not in _base.GLOSARIO or k in _GLOSARIO_CAFE:
            if rx.search(v):
                err.append('texto EN fijado con un término prohibido: %r → %r' % (k, v))
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
    for k, (es, en) in VALORES_EN.items():
        if tx.get(k) != es:
            err.append('VALORES_EN: %r no trae en el ES %r (trae %r)' % (k, es, tx.get(k)))
    factor = {('kg', 'lb'): 2.2046, ('g', 'oz'): 1 / 28.35, ('g', 'lb'): 1 / 453.6, ('L', 'qt'): 1, ('uds', 'ea'): 1}
    for f, es, en in _MINIMOS:
        c = ('05', 'Inventario Diario', 'C%d' % f)
        u_es = tx.get(c)
        u_en = POR_CELDA.get(c) or GLOSARIO.get(u_es)
        x = factor.get((u_es, u_en))
        if x is None:
            err.append('VALORES_EN: unidad %s → %s sin factor en la fila %d' % (u_es, u_en, f))
        elif x == 1 and float(es) != en:
            err.append('VALORES_EN: fila %d en %s no cambia de cifra (%s → %s)' % (f, u_es, es, en))
        elif x != 1 and not (0.5 <= en / (float(es) * x) <= 1.5):
            err.append('VALORES_EN: fila %d, %s %s → %s %s fuera de la conversión' % (f, es, u_es, en, u_en))
    return err


def cruzar_base(p_cafe, p_base):
    """Lo heredado POR CELDA del base (POR_CELDA y ADAPTAR) tiene en la cafetería el mismo texto ES que en el base;
    las filas equivalentes (otra celda, mismo contenido) se comparan por su texto."""
    import json
    err = []

    def textos(p):
        d = {}
        for info in json.load(open(p, encoding='utf-8'))['libros'].values():
            for h, hd in info['hojas_detalle'].items():
                for coord, t in hd.get('textos', {}).items():
                    d[(info['corto'], h, coord)] = t
        return d
    tb, tr = textos(p_base), textos(p_cafe)
    for nombre, claves in (('POR_CELDA', _HEREDA_POR_CELDA), ('ADAPTAR', _HEREDA_ADAPTAR)):
        for k in claves:
            if tr.get(k) != tb.get(k):
                err.append('%s heredado %r: el texto ES de la cafetería %r ≠ base %r' % (nombre, k, tr.get(k),
                                                                                         tb.get(k)))
    equivalentes = [(('03', 'Mensual Manager', 'B15'), ('03', 'Mensual Manager', 'B16'))]
    for kc, kb in equivalentes:
        if tr.get(kc, '').split(' (')[0] != tb.get(kb, '').split(' (')[0]:
            err.append('%r de la cafetería no es la fila del base %r: %r ≠ %r' % (kc, kb, tr.get(kc), tb.get(kb)))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
        e += cruzar_base(pc, os.path.join(os.path.dirname(AQUI), 'censo_es.json'))
    for x in e:
        print('ERROR', x)
    print('mapas_cafe.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} valores · {} adaptar · '
          '{} reglas · {} errores'.format(len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(VALORES_EN),
                                          len(ADAPTAR), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
