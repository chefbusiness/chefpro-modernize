#!/usr/bin/env python3
"""
mapas_catering.py — Catering Checklists Kit Pro (EN) · DELTA del Kit de Tareas para Catering (`kit-tareas-catering`,
11 xlsx v2.0) sobre `mapas.py` (Restaurant Checklists Kit Pro). SPEC: `catering/SPEC.md` (solo el delta). Tercer
hermano vertical, hecho como el bar y la cafetería. Sesión Claude Code, 18-oct-2026.

Se usa con `--kit catering` (kit.py). Importa `mapas.py` y SOLO añade o sobrescribe: producto, ficheros, títulos,
pestañas (36: el catering tiene otra estructura de libros), glosario de catering (zonas, roles, «D-15»…), el 09 como
LIBRO PROPIO (cobros por evento, no caja: liquidación con sales tax, registro de eventos y la tabla opcional de efectivo
de la barra en dólares), el calendario del BONUS-02 (otra estructura: A nº · B fecha · C tipo · D tareas · E
antelación · F notas), POR_CELDA, VALORES_EN (tipo de sales tax), CLAVES (estados del cobro y «Tarea»), ADAPTAR y
REGLAS_US (comida fuera del local, chafing, permisos, alcohol, service charge). La hora de 12 h y el resto se
heredan. Las funciones del base que leen constantes (titulo_interior, autotest, cruzar_censo) se re-enlazan a ESTE
módulo. Ejecutado como script: autotest + cruce con catering/censo_es.json.

    python3 catering/mapas_catering.py
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
AQUI = os.path.dirname(os.path.abspath(__file__))              # catering/ (el import * trae el AQUI del base)

ORIGEN_ES = 'kit-tareas-catering'
PRODUCTO = 'Catering Checklists Kit Pro'
TITULO_SEO = 'Catering Checklists Kit Pro: Catering Event Checklist Templates for Excel'
SLUG = 'catering-checklist-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
ENV_STRIPE = 'VITE_STRIPE_PAYMENT_LINK_CATERING_CHECKLISTS_KIT'
JWT = SLUG + '-jwt'
MARCA_ES = '— Kit de Tareas Recurrentes · Catering / Eventos · AI Chef Pro · aichef.pro'
MARCA_EN = '— ' + PRODUCTO + ' · AI Chef Pro · aichef.pro'
VARIANTES_ES = ('Catering / Eventos',)
# heredar.py: memoria con VARIAS fuentes, en orden de preferencia (base, bar, cafetería; la primera que acierta gana)
_SUF = lambda v: [(' — Catering / Eventos', ' — ' + v), (' · Catering / Eventos', ' · ' + v)]  # noqa: E731
MEMORIA = [('base', '', _SUF('Restaurante Casual')), ('bar', 'bar', _SUF('Bar / Cocktails')),
           ('cafe', 'cafe', _SUF('Cafetería / Brunch'))]
# heredar.py: EN heredado que en un catering no vale tal cual → pendientes (motivo «contexto»). «venue» entra porque
# en el bar es el propio local y en el catering es el recinto del cliente.
RX_CONTEXTO_PENDIENTE = (r'(?i)\b(?:restaurants?(?! consultant)|dining room|host stand|head chef|sous chef|'
                         r'line cooks?|prep cooks?|shift managers?|FOH managers?|coffee shops?|cafes?|baristas?|'
                         r'tip jar|venues?|line-up|patio season)\b')
# gates_en.py G2: términos de otros kits que NINGUNA celda EN del catering puede llevar (la firma de autor, «restaurant
# consultant», queda fuera por el lookahead; «Head Chef» sí vale: el chef de evento). Lo que inyecta el autotest:
TERMINOS_PROHIBIDOS = (r'(?i:\b(?:restaurants?(?! consultant)|host stands?|sous chefs?|FOH managers?|shift managers?|'
                       r'coffee shops?|cafes?|baristas?|tip jars?|line-up)\b)')
TERMINO_PROHIBIDO_EJEMPLO = 'Ask the shift manager.'
REFERENCIAS_TRADUCTOR = ['catering/SPEC.md', 'SPEC.md §0-§3 y §7.2 (brief)', 'textos_en/glosario.json (glosario de '
                         'la prosa del kit base)', 'catering/textos_en/heredado.json (cómo se dijo ya cada cosa: '
                         'base, bar y cafetería)', 'catering/mapas_catering.py: GLOSARIO, HOJAS, FICHEROS, TITULOS, '
                         'POR_CELDA, REGLAS_US', '../GLOSARIO-JERGA-ES-EN.md']
DOCPROPS_EN = OrderedDict([
    ('subject', PRODUCTO + ' · v2.0'),
    ('keywords', 'catering checklist, catering event checklist, catering checklist template, off-site catering, '
                 'catering setup checklist, BEO, AI Chef Pro'),
    ('description', URL_PRODUCTO),
    ('category', 'AI Chef Pro · Digital products'),
])

# ==========================================================================
# Ficheros (D5: intención US — catering checklist 90 · catering event checklist 50 · catering checklist template 50)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-apertura-cierre.xlsx', '01-catering-prep-production-checklist.xlsx'),
    ('02-partidas-cocina.xlsx', '02-catering-transport-delivery-checklist.xlsx'),
    ('03-tareas-manager.xlsx', '03-catering-event-manager-checklist.xlsx'),
    ('04-tareas-perfiles.xlsx', '04-catering-staff-checklists-by-role.xlsx'),
    ('05-tareas-semanales-mensuales.xlsx', '05-catering-event-setup-breakdown-checklist.xlsx'),
    ('06-eventos-festivos.xlsx', '06-catering-event-checklists-by-type.xlsx'),
    ('07-plantilla-personalizable.xlsx', '07-catering-checklist-template.xlsx'),
    ('08-apertura-cierre-negocio.xlsx', '08-catering-commissary-opening-closing-checklist.xlsx'),
    ('09-cobros-facturacion-eventos.xlsx', '09-catering-deposits-invoicing-payments.xlsx'),
    ('BONUS-01-briefing-servicio.xlsx', 'BONUS-01-catering-pre-event-briefing-template.xlsx'),
    ('BONUS-02-calendario-anual-tareas.xlsx', 'BONUS-02-catering-events-calendar.xlsx'),
])
LIBROS_ES = list(FICHEROS)
TITULOS = OrderedDict([
    ('01-catering-prep-production-checklist.xlsx', 'Catering Prep & Production Checklist (Off-Site Catering)'),
    ('02-catering-transport-delivery-checklist.xlsx',
     'Catering Transport & Delivery Checklist: Loading, Holding Temps & Load-In'),
    ('03-catering-event-manager-checklist.xlsx', 'Catering Event Manager Checklist + Quarterly & Annual Compliance'),
    ('04-catering-staff-checklists-by-role.xlsx',
     'Catering Staff Checklists by Role (Event Chef, Banquet Captain, Server, Bartender)'),
    ('05-catering-event-setup-breakdown-checklist.xlsx', 'Catering Event Setup & Breakdown Checklist (Load-In / Load-Out)'),
    ('06-catering-event-checklists-by-type.xlsx',
     'Catering Event Checklists: Weddings, Corporate, Cocktail Receptions & Outdoor'),
    ('07-catering-checklist-template.xlsx', 'Catering Checklist Template (Blank & Editable)'),
    ('08-catering-commissary-opening-closing-checklist.xlsx', 'Catering Commissary Opening & Closing Checklist'),
    ('09-catering-deposits-invoicing-payments.xlsx',
     'Catering Deposits, Invoicing & Payments: Event Settlement & Billing Log'),
    ('BONUS-01-catering-pre-event-briefing-template.xlsx', 'BONUS: Catering Pre-Event Briefing Template (Team Huddle)'),
    ('BONUS-02-catering-events-calendar.xlsx', 'BONUS: Catering Busy Season & Events Calendar (US)'),
])
NOMBRES_CITA = OrderedDict((es, en) for es, en in FICHEROS.items())

HOJAS = OrderedDict(_base.HOJAS)
HOJAS.update([
    ('Producción', 'Production'), ('Transporte', 'Transport & Delivery'), ('Event Manager', 'Event Manager'),
    ('Chef de Evento', 'Event Chef'), ('Maître - Jefe Sala', 'Banquet Captain'),
    ('Montaje', 'Setup & Load-In'), ('Desmontaje', 'Breakdown & Load-Out'),
    ('Bodas', 'Weddings'), ('Corporativo', 'Corporate'), ('Cocktail Standing', 'Cocktail Reception'),
    ('Outdoor - Exterior', 'Outdoor Events'),
    ('Por Fase', 'By Event Phase'), ('Por Zona', 'By Area'),
    ('Apertura del Negocio', 'Commissary Opening'), ('Cierre del Negocio', 'Commissary Closing'),
    ('Antes del Evento', 'Before the Event'), ('Después del Evento', 'After the Event'),
    ('Liquidación del Evento', 'Event Settlement'), ('Registro de Eventos', 'Event Billing Log'),
    ('Briefing', 'Pre-Event Briefing'), ('Calendario', 'Events Calendar'),
])
HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Producción']),
    ('02', ['Instrucciones', 'Transporte']),
    ('03', ['Instrucciones', 'Event Manager', 'Trimestral y Anual']),
    ('04', ['Instrucciones', 'Chef de Evento', 'Maître - Jefe Sala', 'Camarero', 'Barman']),
    ('05', ['Instrucciones', 'Montaje', 'Desmontaje']),
    ('06', ['Instrucciones', 'Bodas', 'Corporativo', 'Cocktail Standing', 'Outdoor - Exterior']),
    ('07', ['Instrucciones', 'Por Fase', 'Por Zona', 'Por Perfil']),
    ('08', ['Instrucciones', 'Apertura del Negocio', 'Cierre del Negocio']),
    ('09', ['Instrucciones', 'Antes del Evento', 'Después del Evento', 'Liquidación del Evento',
            'Registro de Eventos']),
    ('B01', ['Instrucciones', 'Briefing']),
    ('B02', ['Instrucciones', 'Calendario']),
])
H_LIQ, H_REG = 'Liquidación del Evento', 'Registro de Eventos'

# ==========================================================================
# GLOSARIO: el base entero (opcional) + celdas cortas del catering. Jerga US de catering: commissary, load-in /
# load-out, BEO, banquet captain, guaranteed count; «D-15» → «15 days out».
# ==========================================================================
GLOSARIO = OrderedDict(_base.GLOSARIO)
CLAVES_ESTADO = OrderedDict([('Cobrado', 'Paid'), ('Pendiente', 'Pending'), ('VENCIDO', 'OVERDUE')])
_GLOSARIO_CATERING = OrderedDict([
    # subtítulo de marca (A2) de las checklists: el producto EN, igual en todo el kit
    ('AI Chef Pro · aichef.pro — Kit de Tareas: Catering / Eventos', 'AI Chef Pro · aichef.pro — ' + PRODUCTO),
    ('AI Chef Pro · aichef.pro — Escribe tus propias tareas', 'AI Chef Pro · aichef.pro — Write your own tasks'),
    # «Pendiente» citado entre comillas es el ESTADO (Paid / Pending / OVERDUE, CLAVES), no la columna de importe
    # (H5 del registro = «Balance due» por POR_CELDA, que manda en esa celda): así lo cita c0645 (Liquidación D24)
    ('Pendiente', CLAVES_ESTADO['Pendiente']),
    ('Hora', 'Time'), ('Zona/Fase', 'Area / phase'), ('Evento / Cliente', 'Event / client'), ('Fórmula.', 'Formula.'),
    # zonas (columna C)
    ('Producción', 'Production'), ('Transporte', 'Transport'), ('Montaje', 'Setup'), ('Desmontaje', 'Breakdown'),
    ('Logística', 'Logistics'), ('Oficina', 'Office'), ('Almacén', 'Storage'), ('Recepción', 'Front desk'),
    ('Caja', 'POS'),
    # roles (columna D del 08, columna C del 09)
    ('Encargado', 'Ops manager'), ('Comercial', 'Sales'), ('Administración', 'Accounting'),
    ('Event Manager', 'Event manager'), ('Dirección', 'Owner / GM'),
    # secciones de los perfiles (04)
    ('Pre-servicio', 'Before service'), ('Durante el servicio', 'During service'),
    ('Post-servicio', 'After service'), ('Durante el evento', 'During the event'),
    # cuándo (09) y cadencia (03)
    ('D-15', 'By 15 days out'), ('D-7', 'By 7 days out'), ('D-3', 'By 3 days out'), ('D-1', 'Day before'),
    ('D+0', 'Event day'), ('D+1', 'Day after'), ('D+7', '7 days after'), ('D+30', '30 days after'),
    ('Semestral', 'Semiannual'),
    # vida útil en congelación (01) y antelación (BONUS-02)
    ('6-12 meses', '6–12 months'), ('3-6 meses', '3–6 months'), ('1-2 meses', '1–2 months'), ('1 mes', '1 month'),
    ('No congelar', 'Do not freeze'), ('3-4 meses', '3–4 months'), ('2 meses', '2 months'),
    ('3 semanas', '3 weeks'), ('4 semanas', '4 weeks'), ('4-6 semanas', '4–6 weeks'), ('3-6 semanas', '3–6 weeks'),
    ('24-48h', '24–48 h'),
])
GLOSARIO.update(_GLOSARIO_CATERING)
GLOSARIO_OPCIONAL = frozenset(_base.GLOSARIO)
PUESTOS_ES = frozenset(_base.PUESTOS_ES | {'Producción', 'Transporte', 'Montaje', 'Desmontaje', 'Logística',
                                           'Oficina', 'Almacén', 'Recepción', 'Caja', 'Encargado', 'Comercial',
                                           'Administración', 'Event Manager', 'Dirección'})

# ==========================================================================
# CLAVES: «Tarea» (los contadores del 01-07 restan la fila de cabecera) y los estados del cobro (09)
# ==========================================================================
CLAVES = OrderedDict(_base.CLAVES)
CLAVES.update([
    ('Tarea', 'Task'),
    *CLAVES_ESTADO.items(),
    ('OK: las dos bases suman presupuesto + extras', 'OK: the two subtotals add up to quote + extras'),
    ('REVISA: las dos bases no suman presupuesto + extras', 'CHECK: the two subtotals do not add up to quote + extras'),
])

# ==========================================================================
# CF_POR_CELDA (ronda 1 M5, desviación DECLARADA respecto del ES; SPEC §1 D-CF): en las hojas con varias tablas, las
# cabeceras internas llevan «✓» en la columna E y la CF de «hecho» las pintaba de verde (texto blanco ilegible). La EN
# excluye las filas cuyo B es la cabecera «Task»; los contadores ya las restan. aplicar_en y G1 la admiten SOLO aquí.
# (libro, hoja ES, sqref) → (fórmula ES, fórmula EN)
# ==========================================================================
_CF_HOJAS = [('01', 'Producción', 'A6:G51'), ('02', 'Transporte', 'A6:G38'), ('03', 'Event Manager', 'A6:G47'),
             ('03', 'Trimestral y Anual', 'A6:G34'), ('04', 'Chef de Evento', 'A6:G27'),
             ('04', 'Maître - Jefe Sala', 'A6:G27'), ('04', 'Camarero', 'A6:G27'), ('04', 'Barman', 'A6:G27'),
             ('05', 'Montaje', 'A6:G41'), ('05', 'Desmontaje', 'A6:G28'), ('06', 'Bodas', 'A6:G21'),
             ('06', 'Corporativo', 'A6:G18'), ('06', 'Cocktail Standing', 'A6:G20'),
             ('06', 'Outdoor - Exterior', 'A6:G20'), ('B01', 'Briefing', 'A6:G34')]
CF_POR_CELDA = OrderedDict(((c, h, sq), ('$E6="✓"', 'AND($E6="✓",$B6<>"%s")' % CLAVES['Tarea']))
                           for c, h, sq in _CF_HOJAS)

# ==========================================================================
# 09 = LIBRO PROPIO (cobros por evento). Mismas celdas, fórmulas y protección que el ES; cambian por celda:
#   · la tabla opcional de efectivo de la barra (Liquidación A30:C45): billetes y monedas de EE. UU., como el base;
#   · el IVA (10 % / 21 %) → sales tax: base gravable + base exenta; el sales tax = base gravable × el tipo del
#     «Event Billing Log» C3 (parámetro, 0 por defecto); la línea del 21 % pasa a «tax on the non-taxable subtotal»
#     (siempre 0: la estructura del ES no se toca).
# ==========================================================================
HOJA_CAJA = ('09', H_LIQ)
DENOMINACIONES = [
    (30, '500 €', 500, '$100', 100), (31, '200 €', 200, '$50', 50), (32, '100 €', 100, '$20', 20),
    (33, '50 €', 50, '$10', 10), (34, '20 €', 20, '$5', 5), (35, '10 €', 10, '$2', 2), (36, '5 €', 5, '$1', 1),
    (38, '2 €', 2, '$1 coin', 1), (39, '1 €', 1, '50¢', 0.5), (40, '0,50 €', 0.5, '25¢', 0.25),
    (41, '0,20 €', 0.2, '10¢', 0.1), (42, '0,10 €', 0.1, '5¢', 0.05), (43, '0,05 €', 0.05, '1¢', 0.01),
    (44, '0,02 €', 0.02, '25¢ roll', 10), (45, '0,01 €', 0.01, '10¢ roll', 5),
]
VALORES_DENOMINACION_EN = sorted({d[4] for d in DENOMINACIONES})
_REF_TASA = "'%s'!$C$3" % 'Event Billing Log'
FORMULAS_POR_CELDA = OrderedDict(
    ((HOJA_CAJA[0], HOJA_CAJA[1], 'C%d' % f), ('=IFERROR(B%d*%s,0)' % (f, _num(xes)), '=IFERROR(B%d*%s,0)' % (f, _num(xen))))
    for f, _es, xes, _en, xen in DENOMINACIONES)
FORMULAS_POR_CELDA.update([
    (('09', H_LIQ, 'C15'), ('=IFERROR(ROUND(C12*0.1,2),0)', '=IFERROR(ROUND(C12*%s,2),0)' % _REF_TASA)),
    (('09', H_LIQ, 'C16'), ('=IFERROR(ROUND(C13*0.21,2),0)', '=IFERROR(ROUND(C13*0,2),0)')),
])
# G1: fórmulas con referencia a otra hoja que el EN añade (C15 lee el tipo del «Event Billing Log»)
FORMULAS_CON_HOJA_EXTRA = {('09', H_LIQ): 1}
# Las comparaciones numéricas del 09 (≤ 0,01 de tolerancia, total ≤ 0) no cambian en el EN
PATRONES_SIN_CAMBIO = {('09', H_LIQ, 'C14'), ('09', H_LIQ, 'C24'), ('09', H_REG, 'K6')}
# VALORES_EN: el tipo de sales tax del registro (el ES trae el 10 % del IVA): 0, para que cada uno ponga el suyo
VALORES_EN = OrderedDict([(('09', H_REG, 'C3'), (0.1, 0))])
FORMATOS_EN = OrderedDict(_base.FORMATOS_EN)
FORMATOS_EN.update([('0 %', '0.00%'),                          # 8.25 %, 7.375 %…: dos decimales y sin espacio
                    ('DD/MM/YYYY', 'MM/DD/YYYY')])              # fechas del 09 (evento, vencimiento, registro)
# G3: libros cuyo ES no trae la línea de marca D19 (solo el 08 y el 09 la llevan; los demás, el subtítulo A2)
LIBROS_SIN_MARCA = ('01', '02', '03', '04', '05', '06', '07', 'B01', 'B02')

# ==========================================================================
# BONUS-02 «Events Calendar»: otra estructura (A nº · B fecha/evento · C tipo · D tareas · E antelación · F notas;
# filas 5-26). B y C fijados; E por GLOSARIO; D = traductor, con ADAPTAR donde el evento cambia.
# fila → (fecha / evento EN, tipo EN, ADAPTAR de D o None)
# ==========================================================================
HOJA_CAL = ('B02', 'Calendario')
FILAS_CALENDARIO = range(5, 27)
CALENDARIO = OrderedDict([
    (5, ('Feb — Super Bowl Sunday (2nd Sunday)', 'Celebration',
         'Sustituye a Reyes / roscón. Tareas: bandejas para ver el partido y catering de entrega (drop-off): wings, '
         'sliders, dips; pedidos cerrados la semana anterior')),
    (6, ("Feb 14 — Valentine's Day", 'Holiday', None)),
    # ronda 1 M10: orden cronológico (el ES pone las Comuniones antes del 19-mar); D y E de 7-9 van por POR_CELDA
    (7, ("Mar 17 — St. Patrick's Day", 'Holiday', None)),
    (8, ('Mar–Apr — Easter & Passover (dates vary)', 'Holiday', None)),
    (9, ('April — First Communions (season starts), quinceaneras & bar/bat mitzvahs', 'Celebration', None)),
    (10, ('May — Wedding season starts', 'Wedding', None)),
    (11, ("May — First Communions & quinceaneras (peak) + Mother's Day (2nd Sunday)", 'Celebration',
          "Mismas tareas del ES (máxima demanda: 2-3 eventos a la vez); añade los brunch de Mother's Day por "
          'encargo')),
    (12, ('May–June — Weddings + graduation parties', 'Mixed', None)),
    (13, ('June — Corporate summer picnics & team building', 'Corporate', None)),
    (14, ('July–August — Summer weddings & July 4 cookouts', 'Mixed',
          'Mismas tareas del ES (calor, menús frescos, más personal) + barbacoas del 4 de julio (cookouts)')),
    (15, ('September — Back to business (after Labor Day)', 'Corporate', None)),
    (16, ('Sep–Oct — Fall wedding season (peak)', 'Wedding',
          'Menús de otoño US (calabaza, manzana, setas); sin caza')),
    (17, ('Oct 31 — Halloween', 'Holiday', 'Eventos temáticos y decoración; «cocktails especiales» → bebidas '
          'temáticas (con alcohol solo con licencia)')),
    (18, ('October — Holiday party bookings open', 'Corporate', None)),
    (19, ('November — Thanksgiving (4th Thursday)', 'Holiday',
          'Sustituye al Black Friday gastro. Tareas: cenas de Thanksgiving para llevar y Friendsgivings de empresa '
          '(pavo, guarniciones y pies por encargo); cerrar los pedidos el fin de semana anterior')),
    (20, ('Early Dec — Holiday party peak weekends', 'Mixed',
          'Sustituye al puente de la Constitución. Los primeros fines de semana de diciembre: fiestas de empresa, '
          'bodas de invierno y reuniones familiares; cerrar personal extra y stock ANTES')),
    (21, ('December — Corporate holiday parties', 'Corporate', None)),
    (22, ('December — Hanukkah, Christmas Eve & Christmas dinners', 'Celebration',
          'Menús de fiestas US: prime rib, jamón, marisco, postres de temporada (sin cordero ni turrones)')),
    (23, ("Dec 31 — New Year's Eve", 'Holiday',
          'Sin uvas ni cotillón: menú premium, party favors, barra libre (open bar) según tu licencia (21+ con ID) y '
          'brindis con champán a medianoche')),
    (24, ('Year-round — Baptisms, baby & bridal showers', 'Celebration', None)),
    (25, ('Year-round — Funeral receptions & celebrations of life', 'Celebration', None)),
    (26, ('Year-round — Product launches', 'Corporate', None)),
])

# ==========================================================================
# POR_CELDA: rótulos del 09 (libro propio), servicios contratados del 03 y calendario
# ==========================================================================
_TA = ('03', 'Trimestral y Anual')
POR_CELDA = OrderedDict([
    # 09 · Liquidación del Evento
    (('09', H_LIQ, 'A4'), 'Item'), (('09', H_LIQ, 'C4'), 'Amount ($)'), (('09', H_LIQ, 'D4'), 'What to enter'),
    (('09', H_LIQ, 'A6'), 'Event date'), (('09', H_LIQ, 'A7'), 'Guaranteed count'),
    (('09', H_LIQ, 'A8'), 'Actual count'),
    (('09', H_LIQ, 'A9'), '🧾 Subtotals & sales tax'),
    (('09', H_LIQ, 'A10'), 'Accepted quote (before tax)'), (('09', H_LIQ, 'A11'), 'Extras (before tax)'),
    (('09', H_LIQ, 'A12'), 'Taxable subtotal'), (('09', H_LIQ, 'A13'), 'Non-taxable subtotal'),
    (('09', H_LIQ, 'A14'), 'Check: the two subtotals must add up to quote + extras'),
    (('09', H_LIQ, 'A15'), 'Sales tax (rate set in Event Billing Log C3)'),
    (('09', H_LIQ, 'D15'), 'Formula: taxable subtotal × the rate in Event Billing Log C3. It stays at $0 until you '
                           'enter your rate there.'),
    (('09', H_LIQ, 'A16'), 'Non-taxable subtotal: no sales tax'),
    (('09', H_LIQ, 'D16'), 'Always $0: exempt items and tax-exempt clients carry no sales tax. Nothing to enter.'),
    (('09', H_LIQ, 'A17'), 'INVOICE TOTAL'),
    (('09', H_LIQ, 'A18'), '💰 Deposit, balance & payment'),
    (('09', H_LIQ, 'A19'), 'Deposit received (−)'), (('09', H_LIQ, 'A20'), 'Balance after deposit'),
    (('09', H_LIQ, 'A21'), 'Paid after the event'), (('09', H_LIQ, 'A22'), 'BALANCE DUE'),
    (('09', H_LIQ, 'A23'), 'Balance due date'), (('09', H_LIQ, 'A24'), 'STATUS'),
    (('09', H_LIQ, 'A26'), '💰 Only if there was a CASH bar'),
    (('09', H_LIQ, 'A28'), 'Denomination'), (('09', H_LIQ, 'B28'), 'Quantity'),
    (('09', H_LIQ, 'C28'), 'Subtotal ($)'),
    (('09', H_LIQ, 'A29'), 'BILLS'), (('09', H_LIQ, 'A37'), 'COINS'), (('09', H_LIQ, 'A46'), 'TOTAL CASH'),
    (('09', H_LIQ, 'A47'), 'Cash bar starting bank (−)'), (('09', H_LIQ, 'A48'), 'Net cash from the event'),
    # 09 · Registro de Eventos
    (('09', H_REG, 'A3'), 'Sales tax rate (state + local) — set it first'),
    (('09', H_REG, 'A5'), 'Date'), (('09', H_REG, 'C5'), 'Guests'), (('09', H_REG, 'D5'), 'Pre-tax (quote + extras)'),
    (('09', H_REG, 'E5'), 'Invoice total'), (('09', H_REG, 'F5'), 'Deposit'), (('09', H_REG, 'G5'), 'Paid'),
    (('09', H_REG, 'H5'), 'Balance due'), (('09', H_REG, 'I5'), 'Payment method'), (('09', H_REG, 'J5'), 'Due date'),
    (('09', H_REG, 'K5'), 'Status'), (('09', H_REG, 'A31'), 'TOTALS'),
    (('09', H_REG, 'A33'), 'Events with a balance PENDING'), (('09', H_REG, 'A34'), 'OVERDUE events'),
    # 03 · Trimestral y Anual: servicios contratados US de un catering (commissary + vehículos)
    (_TA + ('B6',), 'Pest control of the commissary by a licensed operator: service visit and signed service report '
                    'on file'),
    (_TA + ('F6',), 'Monthly'),
    (_TA + ('B7',), 'Hood and duct cleaning by a certified contractor (NFPA 96: quarterly if high volume or '
                    'charbroil, semiannual if moderate)'),
    (_TA + ('F7',), 'Semiannual'),
    (_TA + ('B15',), "Vehicle registration and commercial auto insurance renewed; the health department's catering "
                     'vehicle permit or inspection, if your county requires one'),
    (_TA + ('B16',), 'Vehicle refrigeration unit serviced by a qualified tech: refrigerant, door seals and '
                     'temperature recorder'),
    (_TA + ('B23',), 'Gas lines and appliance connections checked by a licensed pro if the kitchen has gas (as '
                     'often as your local code requires)'),
    (_TA + ('F23',), 'Annual'),
    (_TA + ('B24',), 'Refrigeration service by an EPA 608-certified tech (walk-ins, reach-ins, blast chiller); '
                     "ovens serviced per the manufacturer's schedule"),
    (_TA + ('B25',), 'Annual extinguisher maintenance by a licensed fire protection company: new tag and record '
                     '(OSHA 1910.157); hood fire suppression inspected every 6 months (NFPA 96)'),
    (_TA + ('B26',), 'Used cooking oil pickup by a licensed recycler: file the pickup receipts'),
    (_TA + ('B32',), 'Invoicing and POS software check: sales tax rates and settings, user permissions, updates'),
    # BONUS-02 · cabecera
    (('B02', 'Calendario', 'B4'), 'Date / period'), (('B02', 'Calendario', 'C4'), 'Type'),
    (('B02', 'Calendario', 'D4'), 'Key tasks'),
])
for _f, _es, _xes, _en, _xen in DENOMINACIONES:
    POR_CELDA[(HOJA_CAJA[0], HOJA_CAJA[1], 'A%d' % _f)] = _en
# 08 · Cierre (ronda 1 M7; errata del ES): toda la secuencia, mismas 15 filas y mismos contadores (E = «Close»):
# primero lo que vuelve del evento (comida a enfriar o a la basura), luego el commissary, y la alarma y la llave al final
_CN = ('08', 'Cierre del Negocio')
_CIERRE = [
    ('Unload and clean the delivery vehicles: returned food that still qualifies goes straight to the blast chiller or '
     'walk-in to finish cooling (FDA Food Code 3-501.14); the rest is discarded', 'Logistics', 'Ops manager'),
    ('Check in the portable equipment that came back', 'Storage', 'Ops manager'),
    ('Collect and store the outdoor equipment that came back (tents, umbrellas and patio heaters)', 'Outside',
     'Ops manager'),
    ('Clear and hose down the loading dock: no carts, no pallets and no trash', 'Outside', 'Ops manager'),
    ('Empty trash cans in common areas and restrooms', 'Restrooms', 'Ops manager'),
    ("Turn off the commissary equipment that shouldn't run overnight (ovens, fryer, hood) and leave the walk-ins and "
     'blast chiller on', 'General', 'Ops manager'),
    ('Turn off the card terminal (or leave it on standby)', 'POS', 'Ops manager'),
    ('Final safety check (gas, water, outlets)', 'General', 'Ops manager'),
    ('Check that windows are closed', 'General', 'Ops manager'),
    ('Turn off HVAC', 'General', 'Ops manager'),
    ('Check that no staff or visitors are left in the commissary before closing', 'General', 'Ops manager'),
    ('Turn off lights (leave security lighting)', 'General', 'Ops manager'),
    ('Set the alarm', 'Entrance', 'Ops manager'),
    ('Close security gate and doors', 'Entrance', 'Last one out'),
    ('Lock up and verify it is locked', 'Entrance', 'Last one out'),
]
for _fila, (_b, _c, _d) in enumerate(_CIERRE, 5):
    for _col, _v in (('B', _b), ('C', _c), ('D', _d)):
        POR_CELDA[_CN + ('%s%d' % (_col, _fila),)] = _v
# 08 · Apertura (ronda 1 M6, m8, M8): revisar y preenfriar el vehículo ANTES de cargar; la carga, a las 7:30 AM tras
# el briefing (D y E se quedan con su fila); sin «front door» ni «POS» de restaurante; el guaranteed count ya cerrado
_AN = ('08', 'Apertura del Negocio')
for _celda, _v in (
        ('B8', 'Raise the security gate and unlock the doors'),
        ('B9', 'Check the transport vehicles: clean, fueled and the refrigeration on, pre-chilled to 41 °F or below '
               'before anything is loaded'), ('C9', 'Logistics'),
        ('B10', 'Turn on the card terminal and the invoicing software (deposits and balances paid by card)'),
        ('C13', 'Office'),
        ('B20', 'Check the portable equipment'), ('C20', 'Storage'),
        ('B21', "Review the day's order of events"), ('C21', 'Office'),
        ('B22', 'Load the insulated carriers for the events leaving first and log the departure temperature (hot '
                '135 °F or above, cold 41 °F or below) — log reading: ____ °F (loading details go in the Transport & '
                'Delivery sheet of 02-catering-transport-delivery-checklist.xlsx)'), ('C22', 'Outside')):
    POR_CELDA[_AN + (_celda,)] = _v
POR_CELDA[('08', 'Instrucciones', 'B16')] = ('▸ Everything filled in daily is GREEN: Assigned to, Due by (When, at '
                                             'closing), ✓ Done, Initials and Notes.')   # m12
# 03 · Event Manager (m11): rótulos de sección como los demás del libro
POR_CELDA[('03', 'Event Manager', 'A27')] = 'During the Event'
POR_CELDA[('03', 'Event Manager', 'A38')] = 'After the Event'
# BONUS-02 (M10 + M11): D y E de las filas 7-9 siguen a su evento
for _celda, _v in (
        ('D7', 'Corporate parties and family gatherings with a themed menu; alcohol only under the license your state '
               "requires (yours or the venue's), 21+ with ID"), ('E7', '3 weeks'),
        ('D8', 'Easter brunch and family dinners (ham, lamb, seasonal desserts); Passover seder if your clients ask '
               '(kosher only with a certified kitchen and supervision)'), ('E8', '3 weeks'),
        ('D9', "Kids' + adult menus, themed decor"), ('E9', '2–3 months')):
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], _celda)] = _v
for _fila, (_evento, _tipo, _dir) in CALENDARIO.items():
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'B%d' % _fila)] = _evento
    POR_CELDA[(HOJA_CAL[0], HOJA_CAL[1], 'C%d' % _fila)] = _tipo

# ==========================================================================
# ADAPTAR (en español, con el dato US; las cifras y normas salen de REGLAS_US)
# ==========================================================================
_A = _base.ADAPTAR
_TEMP_FRIO = ('°F: refrigeración 41 °F o menos, congelación 0 °F o menos (FDA Food Code 3-501.16); coletilla «— log '
              'reading: ____ °F»; °C solo entre paréntesis si cabe')
_HACCP_KIT = ('«Pack APPCC» → «HACCP Food Safety Kit Pro» (nuestro kit EN: aichef.pro/en/digital-products/'
              'haccp-templates)')
_CARGA = ('°F: lo caliente a 135 °F o más y lo frío a 41 °F o menos (FDA Food Code 3-501.16), al cargar, en el '
          'trayecto y al descargar; coletilla «— log reading: ____ °F»; ' + _HACCP_KIT)
_PARASITOS = ('Destrucción de parásitos US (FDA Food Code 3-402.11): congelado a −4 °F o menos 7 días, o a −31 °F o '
              'menos hasta sólido + 15 h; registro del proveedor guardado 90 días. Sin «≥24 h a −20 °C» ni la '
              'palabra «anisakis» como norma (dilo «parasite destruction»)')
_DATE = ('Date marking US: etiqueta con producto y fecha; lo preparado y listo para comer, 7 días como máximo a '
         '41 °F contando el día de preparación (FDA Food Code 3-501.17); alérgenos: los 9 principales de EE. UU.')
_ALERGENOS = ('Alérgenos US: los 9 principales (FALCPA + FASTER Act: leche, huevo, pescado, crustáceos (crustacean '
              'shellfish; los moluscos no), frutos de '
              'cáscara, cacahuete, trigo, soja y sésamo); en UK, los 14')
_TPHC = ('Time as a public health control (FDA Food Code 3-501.19): marca la hora en que sale del control de '
         'temperatura y sirve DENTRO de las 4 h; lo que quede a las 4 h se descarta y no puede volver al caliente ni '
         'al frío para reiniciar el reloj; lo frío puede llegar a 6 h solo si sale a 41 °F o menos y vigilas que no '
         'pase de 70 °F: se descarta en cuanto pasa, y a las 6 h; necesita procedimiento escrito y, según tu condado, '
         'aviso al departamento de salud')
_BARRA = ('Barra libre = open bar: horario pactado; ID a quien parezca menor de 30 (21+); no servir a quien esté '
          'visiblemente ebrio; el alcohol, con la licencia que pida tu estado (la del catering o la del venue) y '
          'bartenders con la formación de servicio responsable que exija el estado (TIPS, ServSafe Alcohol)')
_LAVAMANOS = ('Agua potable y una estación de lavado de manos (handwashing station) junto a la cocina y al servicio '
              'si el sitio no tiene lavamanos: agua caliente, jabón, papel y cubo de recogida, como pida tu '
              'departamento de salud')
_FICHAJES = _base.POR_CELDA[('03', 'Mensual Manager', 'B16')]
ADAPTAR = OrderedDict([
    # 01 · producción
    (('01', 'Instrucciones', 'B16'), _PARASITOS),
    (('01', 'Producción', 'B6'), '«Ficha técnica del evento» → BEO (banquet event order)'),
    (('01', 'Producción', 'B18'), _A[('01', 'Apertura Cocina', 'B7')]),
    (('01', 'Producción', 'B20'), _A[('01', 'Apertura Cocina', 'B9')]),
    (('01', 'Producción', 'B21'), _A[('01', 'Apertura Cocina', 'B10')]),
    (('01', 'Producción', 'B23'), _A[('01', 'Apertura Cocina', 'B14')]),
    (('01', 'Producción', 'B28'), _TEMP_FRIO + '; ' + _DATE),
    (('01', 'Producción', 'B34'), _PARASITOS),
    (('01', 'Producción', 'B35'), _A[('02', 'Fríos', 'B6')]),
    (('01', 'Producción', 'B36'), _DATE),
    (('01', 'Producción', 'B41'), _TEMP_FRIO),
    (('01', 'Producción', 'B47'), 'GN → hotel pans; contenedores isotérmicos → insulated food carriers (los «cambros» '
     'de la jerga US)'),
    (('01', 'Producción', 'B48'), _CARGA),
    (('01', 'Producción', 'D59'), 'La destrucción de parásitos (−4 °F 7 días, FDA Food Code 3-402.11) no sustituye a '
     'esta vida útil: se cuentan por separado'),
    # 02 · transporte
    (('02', 'Instrucciones', 'B7'), 'Mantiene la comida a temperatura segura en el trayecto (41 °F o menos / 135 °F '
     'o más, FDA Food Code 3-501.16); sin «cumple la normativa»'),
    (('02', 'Transporte', 'B8'), _TEMP_FRIO),
    (('02', 'Transporte', 'B9'), 'Sin ATP (no existe en EE. UU.): combustible, registro, seguro comercial del vehículo '
     '(commercial auto) y, si tu condado lo exige, el permiso o la inspección del vehículo de catering del '
     'departamento de salud'),
    (('02', 'Transporte', 'B15'), _CARGA),
    (('02', 'Transporte', 'B25'), _CARGA),
    (('02', 'Transporte', 'B26'), 'Ronda 1 M1: las 4 h cuentan desde que sale de 41 / 135 °F (puede ser al emplatar) e '
     'incluyen el trayecto Y el servicio en el venue; a las 4 h se descarta; procedimiento escrito. '
     'Sin el «máx. 2 h» español: lo frío a 41 °F o menos y lo caliente a 135 °F o más '
     'todo el trayecto; si algo viaja sin control de temperatura, va con time as a public health control (FDA Food '
     'Code 3-501.19): 4 h como máximo con la hora de salida marcada'),
    (('02', 'Transporte', 'B35'), _CARGA),
    # 03 · event manager y revisiones
    (('03', 'Instrucciones', 'B14'), 'Describe la lista US de «Quarterly & Annual»: control de plagas del commissary, '
     'campana y conductos (NFPA 96), extintores y extinción de la campana, gas, vehículos (registro, seguro y permiso '
     'del condado si lo pide), calibración de termómetros, aceite usado, permisos sanitarios, food handler cards y '
     'Certified Food Protection Manager, seguros y facturación / sales tax. Sin DDD, ATP, RGSEAA, carnés de '
     'manipulador, BIE ni Verifactu'),
    (('03', 'Instrucciones', 'B16'), 'Fichajes US: ' + _FICHAJES + '; montaje y desmontaje también son horas '
     'trabajadas'),
    (('03', 'Event Manager', 'B7'), 'Bartenders con la formación de servicio responsable que exija tu estado (TIPS, '
     'ServSafe Alcohol)'),
    (('03', 'Event Manager', 'B13'), 'Timing sheet minuto a minuto → run sheet (event timeline)'),
    (('03', 'Event Manager', 'B18'), 'Acceso (loading dock), electricidad, agua potable, baños, punto frío y '
     'estación de lavado de manos'),
    (('03', 'Event Manager', 'B46'), 'Fichajes US: ' + _FICHAJES + '; con los del montaje, el servicio y el '
     'desmontaje (sin «4 años»)'),
    (('03', 'Trimestral y Anual', 'B8'), 'En EE. UU. no es obligatorio: opcional, para verificar el plan de limpieza '
     '(environmental swabs o análisis de producto en un laboratorio)'),
    (('03', 'Trimestral y Anual', 'B9'), 'Revisar el plan HACCP (food safety plan) y las fichas de proveedor; ' + _HACCP_KIT),
    (('03', 'Trimestral y Anual', 'B10'), 'Food handler cards donde tu estado o condado las pida y al menos un '
     'Certified Food Protection Manager (p. ej. ServSafe Manager) en plantilla (FDA Food Code 2-102.12); renovar y '
     'archivar'),
    (('03', 'Trimestral y Anual', 'B11'), 'Permiso sanitario del commissary (health permit / food service license) '
     'que cubra el catering, renovado según tu condado'),
    (('03', 'Trimestral y Anual', 'B17'), _A[('05', 'Trimestral y Anual', 'B23')]),
    (('03', 'Trimestral y Anual', 'B18'), 'Sin ITV: la inspección estatal del vehículo si tu estado la pide y el '
     'extintor de a bordo revisado'),
    (('03', 'Trimestral y Anual', 'B30'), 'Seguros: general liability (con los límites que suelen pedir los venues), '
     "liquor liability si sirves alcohol, commercial auto y workers' comp; tener el COI (certificate of insurance) "
     'listo, con el venue como additional insured si lo pide'),
    (('03', 'Trimestral y Anual', 'B31'), 'Altas del trimestre: Form I-9 y W-4 de cada empleado nuevo de eventos, y '
     'los fichajes archivados'),
    # 04 · perfiles
    (('04', 'Chef de Evento', 'B17'), '°F: caliente a 135 °F o más, frío a 41 °F o menos (FDA Food Code 3-501.16)'),
    (('04', 'Maître - Jefe Sala', 'B11'), '«Office» = estación de servicio (service station / pantry), no la oficina'),
    (('04', 'Maître - Jefe Sala', 'B26'), 'Propinas (gratuities) según la política de la casa y las normas de tu '
     'estado; un service charge obligatorio NO es propina: lo que se paga de él al personal es salario para el IRS '
     '(Rev. Rul. 2012-18); managers y supervisores no pueden quedarse parte de las propinas del equipo (FLSA)'),
    (('04', 'Camarero', 'B11'), 'Zona de fumadores solo si el venue tiene una (muchos estados prohíben fumar en '
     'interiores)'),
    (('04', 'Barman', 'B7'), 'Si el cliente aporta el alcohol (client-supplied / BYOB), solo si tu estado y el venue lo '
     'permiten'),
    (('04', 'Barman', 'B8'), 'El hielo es un alimento (FDA Food Code): pala (ice scoop), nunca el vaso'),
    (('04', 'Barman', 'B11'), 'Batches en recipientes propios etiquetados; nunca rellenar una botella de licor'),
    (('04', 'Barman', 'B15'), 'Cava → espumoso (sparkling wine); bienvenida solo a mayores de 21'),
    (('04', 'Barman', 'B17'), _BARRA),
    # 05 · montaje y desmontaje
    (('05', 'Montaje', 'B6'), 'Cocina temporal: si cocinas en el sitio en un evento público, comprueba si tu condado o '
     'tu ciudad piden un permiso de temporary food establishment'),
    (('05', 'Montaje', 'B8'), 'Infernillos → butane burners; calentadores → food warmers; llama abierta solo si el '
     'venue y el fire marshal lo permiten'),
    (('05', 'Montaje', 'B9'), _LAVAMANOS),
    (('05', 'Montaje', 'B11'), 'A 41 °F o menos (FDA Food Code 3-501.16)'),
    (('05', 'Montaje', 'B29'), 'Chafing dishes y combustible (chafing fuel): mantienen, no recalientan (lo que llega '
     'frío se recalienta a 165 °F antes, FDA Food Code 3-403.11) y a 135 °F o más; latas lejos de manteles y '
     'decoración, nunca recargar ni mover un chafer encendido, extintor a mano y las normas de llama abierta del '
     'venue y del fire marshal'),
    (('05', 'Montaje', 'B31'), 'Refrigeración a 41 °F o menos para lo que lleve crema, nata o lácteos'),
    (('05', 'Montaje', 'B32'), 'Señal de cada plato con su nombre y los 9 alérgenos principales de EE. UU. que lleva '
     '(UK: los 14)'),
    (('05', 'Montaje', 'B38'), '°F: 68–72 °F (20–22 °C)'),
    (('05', 'Montaje', 'B40'), 'Salidas de emergencia despejadas y señales de salida (exit signs) visibles'),
    (('05', 'Desmontaje', 'B15'), 'Apagar el combustible de los chafing con su tapa o apagador y dejarlo enfriar '
     'antes de recoger'),
    (('05', 'Desmontaje', 'B18'), 'Sobrantes US: lo que se mantuvo a 41 °F o menos (o a 135 °F o más) y no salió a '
     'sala: enfriar lo caliente (de 135 °F a 70 °F en 2 h y a 41 °F en 4 h más, FDA Food Code 3-501.14) y lo frío, '
     'directo a 41 °F o menos; etiquetar y fechar; '
     'lo que estuvo expuesto en el buffet o bajo time as a public health control: se descarta (no vuelve a la '
     'cámara)'),
    (('05', 'Desmontaje', 'B28'), 'Temperatura en °F: 41 °F o menos para lo que vuelva en frío'),
    # 06 · tipos de evento
    (('06', 'Bodas', 'B10'), 'Barra libre → open bar'),
    (('06', 'Bodas', 'B19'), _BARRA),
    (('06', 'Cocktail Standing', 'B9'), _PARASITOS + '; aviso al consumidor (consumer advisory) de crudo o poco '
     'hecho en el cartel de la estación o la carta (FDA Food Code 3-603.11)'),
    (('06', 'Cocktail Standing', 'B10'), _ALERGENOS),
    (('06', 'Cocktail Standing', 'B11'), 'Barra de cocktails solo con la licencia de alcohol que pida tu estado (o la '
     'del venue); 21+ con ID'),
    (('06', 'Outdoor - Exterior', 'B10'), _LAVAMANOS),
    (('06', 'Outdoor - Exterior', 'B11'), 'Carpa (tent): las grandes suelen necesitar permiso del fire marshal y lona '
     'ignífuga (flame-resistant); pregunta a tu ciudad'),
    (('06', 'Outdoor - Exterior', 'B16'), 'Al aire libre: lo caliente a 135 °F o más y lo frío a 41 °F o menos; ' +
     _TPHC + '. Sin la regla española de «1 h con más de 30 °C»: con calor, reponer más a menudo y en menos cantidad'),
    # 08 · commissary
    (('08', 'Apertura del Negocio', 'B12'), 'Órdenes de servicio → BEOs (banquet event orders)'),
    (('08', 'Apertura del Negocio', 'B17'), 'Estufas → patio heaters (propano: según el fire code local)'),
    # 09 · cobros (libro propio)
    (('09', 'Instrucciones', 'B7'), 'En EE. UU. el catering cobra por evento, casi siempre con cheque, ACH (bank '
     'transfer) o tarjeta: sin mostrador ni turno de POS'),
    (('09', 'Instrucciones', 'B19'), 'Celdas verdes US: presupuesto y extras ANTES del sales tax, cómo se reparte esa '
     'base entre «Taxable subtotal» y «Non-taxable subtotal», el anticipo (deposit), lo cobrado después y la fecha '
     'de vencimiento; el sales tax sale del tipo de la celda C3 del «Event Billing Log»'),
    (('09', 'Instrucciones', 'B20'), 'Qué lleva sales tax lo decide tu estado (consúltalo con tu CPA o el department '
     'of revenue): en muchos la comida, la bebida, los alquileres y el service charge obligatorio. Un service charge '
     'obligatorio NO es propina: es ingreso del negocio y lo que se paga de él al personal es salario para el IRS '
     '(Rev. Rul. 2012-18); en algunos estados (NY, MA) un service charge sin aviso claro se presume del personal: la '
     'política, en el contrato; la propina (gratuity) la decide el '
     'cliente, va aparte y es del equipo. Un cliente exento (tax-exempt) necesita su certificado de exención en el '
     'expediente'),
    (('09', 'Instrucciones', 'B22'), 'La tabla de efectivo trae billetes y monedas de EE. UU. ($100 … 1¢; un «25¢ '
     'roll» cuenta $10 y un «10¢ roll» $5); en UK, Canadá o Australia, desprotege la hoja (sin contraseña) y cambia el '
     'rótulo de cada fila y el multiplicador de su fórmula de Subtotal'),
    (('09', 'Antes del Evento', 'B6'), 'Comensales confirmados → guaranteed count (final headcount), con la fecha '
     'límite de cambios por escrito'),
    (('09', 'Antes del Evento', 'B7'), 'Anticipo → deposit (retainer) del 30-50 % según tu contrato'),
    (('09', 'Antes del Evento', 'B9'), 'Datos de facturación US: nombre legal (legal name), dirección y email de '
     'facturación y, si el cliente está exento de sales tax, su certificado de exención (sin CIF / NIF)'),
    (('09', 'Antes del Evento', 'B14'), 'COI (certificate of insurance) de general liability (y liquor liability si '
     'sirves alcohol) en vigor, con el venue como additional insured si lo pide'),
    (('09', 'Después del Evento', 'B5'), 'Recuento real (actual count) frente al guaranteed count; se factura lo que '
     'diga tu contrato (lo normal: el mayor de los dos)'),
    (('09', 'Después del Evento', 'B9'), 'Factura (invoice) con el sales tax de lo que tu estado grave y, en líneas '
     'aparte, el service charge y la propina (gratuity) si la hay; sin IVA ni tipos españoles'),
    (('09', H_LIQ, 'D10'), 'El importe aceptado ANTES del sales tax'),
    (('09', H_LIQ, 'D11'), 'Horas extra del personal, bebidas de más, suplementos y roturas; antes del sales tax'),
    (('09', H_LIQ, 'D12'), 'Lo que tu estado grava: en muchos, comida, bebida, alquileres y el service charge '
     'obligatorio (pregunta a tu CPA o al department of revenue)'),
    (('09', H_LIQ, 'D13'), 'Lo exento en tu estado, o todo si el cliente es tax-exempt con su certificado; 0 si todo '
     'lleva sales tax. La propina (gratuity) no va aquí'),
    (('09', H_LIQ, 'D17'), 'Las dos bases más el sales tax: lo que dice la factura'),
    (('09', H_LIQ, 'D19'), 'Lo cobrado al firmar (deposit, el 30-50 % habitual); se resta del total'),
    (('09', H_LIQ, 'A27'), 'Cuenta el efectivo en dólares y, si quieres, suma tú el «Net cash from the event» a «Paid '
     'after the event»; no se enlaza solo (la mayoría de los eventos no llevan barra con cobro en efectivo)'),
    (('09', H_REG, 'D3'), 'Ronda 1 M9: empieza por «0 = no sales tax until you enter your combined rate». '
     'Tu tipo combinado (estatal + local), p. ej. 0.0825 para el 8.25 %. «Event Settlement» lo '
     'aplica a la base gravable; aquí se aplica a toda la base, así que «Invoice total» es una estimación si parte '
     'del evento está exenta: la cifra exacta, en «Event Settlement»'),
    # BONUS-01
    (('B01', 'Briefing', 'B8'), 'Comensales confirmados → guaranteed count'),
    (('B01', 'Briefing', 'B17'), 'Cava → espumoso o champán (sparkling wine / champagne)'),
    # BONUS-02
    (('B02', 'Instrucciones', 'B10'), 'Fechas locales US: ferias del estado (state fairs), festivales y fiestas de tu '
     'ciudad; añade la nota UK: bank holidays y Boxing Day en las filas libres'),
])
for _fila, (_evento, _tipo, _dir) in CALENDARIO.items():
    if _dir:
        ADAPTAR[(HOJA_CAL[0], HOJA_CAL[1], 'D%d' % _fila)] = 'Evento EN: «%s». %s' % (_evento, _dir)
CELSIUS_SIN_F = frozenset()

# ==========================================================================
# REGLAS_US: las del base + las del catering (fuente única de las cifras y normas que el kit puede afirmar)
# ==========================================================================
REGLAS_US = OrderedDict(_base.REGLAS_US)
REGLAS_US.update([
    ('tphc', ('time as a public health control: servir o descartar DENTRO de las 4 h (lo que quede a las 4 h se '
              'descarta y no vuelve al control de temperatura); frío hasta 6 h si sale a 41 °F o menos, vigilando que no '
              'pase de 70 °F (se descarta si pasa); procedimiento escrito y hora marcada', 'FDA Food Code 2022 §3-501.19')),
    ('transporte', ('frío 41 °F o menos y caliente 135 °F o más también en el transporte y el buffet',
                    'FDA Food Code 2022 §3-501.16')),
    ('chafing', ('chafing: mantener a 135 °F, no recalentar en él; no recargar ni mover el combustible encendido; '
                 'normas de llama abierta', '[local] fire code y normas del venue; [fabricante] etiqueta del combustible')),
    ('permiso_temporal', ('permiso de temporary food establishment para cocinar en un evento público, según el condado',
                          '[local] departamento de salud del condado o la ciudad')),
    ('lavamanos_portatil', ('estación de lavado de manos con agua caliente, jabón y papel si no hay lavamanos',
                            '[local] departamento de salud (eventos temporales)')),
    ('vehiculo', ('permiso o inspección del vehículo de catering si el condado lo pide; sin ATP',
                  '[local] departamento de salud; [estatal] registro e inspección del vehículo')),
    ('cfpm', ('al menos un Certified Food Protection Manager', 'FDA Food Code 2022 §2-102.12')),
    ('food_handler', ('food handler cards donde el estado o el condado las pidan', '[estatal] / [local] food handler card')),
    ('edad_alcohol', ('21 años para comprar o consumir alcohol, en todos los estados',
                      'National Minimum Drinking Age Act of 1984 (23 U.S.C. 158)')),
    ('licencia_eventos', ('alcohol en eventos con la licencia que pida el estado (la del catering o la del venue)',
                          '[estatal] ABC / liquor authority')),
    ('servicio_responsable', ('formación de servicio responsable (TIPS, ServSafe Alcohol u otro aprobado), obligatoria '
                              'en algunos estados', '[estatal] p. ej. California RBS (AB 1221); Illinois BASSET')),
    ('alcohol_cliente', ('alcohol que aporta el cliente: según el estado y la política del venue',
                         '[estatal] ABC / liquor authority; [local] normas del venue')),
    ('hielo', ('el hielo es un alimento: pala, nunca el vaso', 'FDA Food Code 2022, «food» incluye el hielo')),
    ('rellenado', ('no rellenar botellas de licor; batches en recipientes propios etiquetados',
                   '26 U.S.C. 5301(c); 27 CFR 31.201')),
    ('service_charge', ('el service charge obligatorio no es propina: es ingreso del negocio, y lo que se paga de él al '
                        'personal es salario en nómina, no propina', 'IRS Rev. Rul. 2012-18')),
    ('service_charge_aviso', ('en algunos estados (NY, MA) un service charge que no se anuncia claramente como «no es '
                              'propina» se presume del personal: la política, en el contrato',
                              '[estatal] 12 NYCRR 146-2.19; M.G.L. c. 149 §152A')),
    ('propinas_supervisores', ('managers y supervisores no pueden quedarse ninguna parte de las propinas del equipo',
                               'FLSA, 29 U.S.C. 203(m)(2)(B)')),
    ('sales_tax', ('qué lleva sales tax (incluido el service charge obligatorio) y el tipo estatal + local, según el '
                   'estado; tipo como parámetro (0 por defecto)', '[estatal] department of revenue')),
    ('exencion', ('cliente exento con su certificado de exención', '[estatal] department of revenue')),
    ('coi', ('COI de general liability (y liquor liability si hay alcohol), con el venue como additional insured',
             '[criterio del kit] práctica de contratos con venues')),
    ('guaranteed_count', ('se factura según el contrato; lo habitual, el mayor entre guaranteed y actual count',
                          '[criterio del kit] práctica de banquetes US')),
    ('i9', ('Form I-9 de cada empleado nuevo, completado antes del 3.er día hábil', 'USCIS Form I-9 (8 U.S.C. 1324a; '
            '8 CFR 274a.2(b)(1)(ii))')),
    ('carpas', ('las carpas grandes suelen necesitar permiso del fire marshal y lona ignífuga',
                '[local] fire code (International Fire Code, cap. 31)')),
    ('sala', ('20-22 °C = 68-72 °F', '[criterio del kit] cifras del ES convertidas')),
    ('super_bowl', ('Super Bowl el 2.º domingo de febrero', '[criterio del kit] calendario de la NFL desde 2022')),
    ('comuniones', ('primeras comuniones sobre todo de abril a mayo; quinceañeras y bar/bat mitzvahs, todo el año',
                    '[criterio del kit] calendario parroquial US')),
])
# °F que el kit puede afirmar (G7): las del base + 68-72 °F (sala)
GRADOS_F_SPEC = {-31, -4, 0, 32, 41, 68, 70, 72, 100, 135, 165}

# ==========================================================================
# Pistas y dependencias del catering (extraer_textos.py)
# ==========================================================================
PISTAS_CAMBIO = {
    r'Kit de Tareas': 'D2: «Catering Checklists Kit Pro»',
    r'[Cc]amarer|[Cc]ociner|[Jj]efe|[Jj]efa|[Aa]uxiliar|[Ee]ncargad|[Bb]arman|[Pp]artida|[Pp]astel':
        'Roles de catering US (mapas.GLOSARIO): camarero → server; chef de evento → event chef; maître / jefe de sala '
        '→ banquet captain; barman → bartender; encargado → ops manager; cocineros → cooks; partida / estación → '
        'station; runner se queda',
    r'Responsable( de turno| general)?:': 'Formularios: «Responsable de turno:» → «Manager on duty:»; «Responsable:» → '
                                          '«Manager:»',
    r'[Ss]ala\b|SALA|[Cc]omedor': 'sala (del evento) → the room / dining room del venue; equipo de sala → service '
                                  'team; plano de sala → floor plan',
    r'[Bb]riefing': 'briefing → pre-event briefing (team huddle)',
}
PISTAS_FUERA = (r'Restaurante Casual', r'[Tt]erraza|TERRAZA')
PISTAS_EXTRA = [
    (r'Catering / Eventos', 'D2: la EN no lleva el sufijo de variante: quita «— Catering / Eventos»'),
    (r'[Ff]icha técnica del evento|[Óó]rden(es)? de servicio|BEO', 'ficha técnica del evento / orden de servicio → '
                                                                  'BEO (banquet event order)'),
    (r'[Cc]omensales', 'comensales → guests; nº confirmado / contratado → guaranteed count; reales → actual count'),
    (r'[Dd]escarga|[Cc]arga\b|[Cc]argar', 'carga y descarga en el venue → load-in / load-out; muelle → loading dock'),
    (r'[Mm]ontaje|[Dd]esmontaje', 'montaje → setup (load-in); desmontaje → breakdown / teardown (load-out)'),
    (r'[Tt]iming|[Tt]imeline|minuto a minuto', 'timing sheet / timeline minuto a minuto → run sheet'),
    (r'\bGN\b|[Ii]sot[eé]rm|[Ii]sotermo', 'GN → hotel pans; contenedor isotérmico / isotermo → insulated food carrier '
                                          '(«cambro»); furgoneta isoterma → insulated / refrigerated van'),
    (r'[Cc]hafing|[Cc]alientaplatos|[Ii]nfernillo|[Cc]ombustible', 'chafing dishes; combustible → chafing fuel; '
                                                                    'infernillo → butane burner'),
    (r'[Oo]brador|[Cc]ocina central', 'obrador / cocina central → commissary (kitchen)'),
    (r'[Mm]aître', 'maître → banquet captain'),
    (r'[Bb]arra libre', 'barra libre → open bar (21+ con ID)'),
    (r'\b[Cc]ava\b', 'cava → sparkling wine'),
    (r'[Mm]antel|[Mm]enaje|[Cc]ristaler|[Cc]ubert|[Vv]ajilla', 'mantelería → linens; menaje → smallwares / rentals; '
                                                               'cristalería → glassware; cubertería → flatware; '
                                                               'vajilla → china'),
    (r'[Cc]arpa|[Ff]inca|[Tt]oldo', 'carpa → tent; finca → estate / ranch venue; toldo → canopy'),
    (r'[Ee]scandallo', 'escandallo → costing (cost per guest)'),
    (r'[Pp]resupuesto|[Aa]nticipo|[Ss]aldo|[Ff]actur|IVA|[Tt]ransferencia',
     'presupuesto → quote / proposal; anticipo → deposit; saldo → balance; factura → invoice; IVA → sales tax; '
     'transferencia → ACH / bank transfer'),
    (r'\bD[-+]\d+', 'D-15 → «15 days out», D-7 → «7 days out», D-3 → «3 days out», D-1 → «Day before», D+0 → «Event '
                    'day», D+1 → «Day after», D+7 → «7 days after», D+30 → «30 days after» (rótulos de «When»)'),
    (r'[Rr]egistro de jornada', 'registro de jornada → time records (time-clock punches)'),
    (r'[Pp]ropinas?', 'propinas → tips / gratuities; service charge ≠ gratuity'),
    (r'[Aa]lmacenamiento temporal|[Aa]copio', 'almacenamiento temporal / zona de acopio → staging area'),
    (r'[Ee]stufas', 'estufas de exterior → patio heaters (propano)'),
    (r'[Tt]anatorio|[Ff]unerales', 'funerales / tanatorio → funeral receptions, celebrations of life'),
    (r'[Bb]autizos', 'bautizos → baptisms / christenings'),
    (r'RRSS|redes', 'RRSS → social media'),
    (r'Antes del Evento|Después del Evento|Liquidación del Evento|Registro de Eventos',
     'pestañas del 09 (aunque no vayan entre comillas): Antes del Evento → «Before the Event»; Después del Evento → '
     '«After the Event»; Liquidación del Evento → «Event Settlement»; Registro de Eventos → «Event Billing Log»'),
    (r'PENDIENTE DE COBRO|ESTADO|VENCIDO|Cobrado|Pendiente|Efectivo neto|TOTAL FACTURA|[Ff]ondo de (la )?barra',
     'rótulos y estados EN del 09 (mapas.POR_CELDA y CLAVES): PENDIENTE DE COBRO → BALANCE DUE; ESTADO → STATUS; '
     'TOTAL FACTURA → INVOICE TOTAL; «Cobrado» → "Paid"; «Pendiente» → "Pending"; «VENCIDO» → "OVERDUE"; «Efectivo '
     'neto del evento» → "Net cash from the event"; fondo de la barra → cash bar starting bank'),
]
DEPENDENCIAS_EXTRA = OrderedDict([
    ('variante', ('Sufijo de variante «Catering / Eventos»', r'Catering / Eventos', 'D2: la EN no lleva sufijo')),
    ('cobros', ('IVA, anticipo, factura y medios de pago españoles', r'IVA|CIF|NIF|[Aa]nticipo|[Ff]actura|'
                r'[Tt]ransferencia', 'D-CAT cobros: sales tax (tipo como parámetro), deposit, invoice, service charge ≠ '
                'gratuity')),
    ('fuera', ('Comida fuera del local: transporte, buffet, exterior', r'[Tt]ransporte|[Bb]uffet|[Oo]utdoor|'
               r'[Ee]xterior|[Cc]hafing', 'D-CAT: 135 °F / 41 °F, time as a public health control, 165 °F al recalentar')),
    ('alcohol', ('Alcohol en eventos', r'[Bb]arra libre|[Cc]ava\b|[Cc]ocktail|[Bb]arman', 'D-CAT: licencia según el '
                 'estado, 21+ con ID, servicio responsable')),
])


def _rebind(f):
    return types.FunctionType(f.__code__, globals(), f.__name__, f.__defaults__, f.__closure__)


titulo_interior = _rebind(_base.titulo_interior)
_autotest_base = _rebind(_base.autotest)
_cruzar_censo_base = _rebind(_base.cruzar_censo)


def autotest():
    err = _autotest_base()                       # pestañas, ficheros, glosario, POR_CELDA, billetes, calendario…
    if _REF_TASA.split('!')[0].strip("'") != HOJAS[H_REG]:
        err.append('C15 cita una hoja que no es la EN del registro: %s' % _REF_TASA)
    for k, (es, en) in VALORES_EN.items():
        if not isinstance(en, (int, float)) or isinstance(en, bool) or en < 0:
            err.append('VALORES_EN: el EN de %r debe ser un número ≥ 0: %r' % (k, en))
        if k in POR_CELDA or k in ADAPTAR:
            err.append('VALORES_EN y POR_CELDA/ADAPTAR sobre la misma celda: %r' % (k,))
    if CLAVES['Tarea'] != GLOSARIO['Tarea']:
        err.append('CLAVES["Tarea"] debe ser el EN de la cabecera (GLOSARIO): los contadores la restan')
    estados = {CLAVES[k] for k in ('Cobrado', 'Pendiente', 'VENCIDO')}
    for caso in CASOS_G5:
        for (h, coord) in list(caso['entradas']) + list(caso['esperado']):
            if h not in HOJAS_ES_POR_LIBRO['09']:
                err.append('CASOS_G5 %s: hoja %r fuera del 09' % (caso['nombre'], h))
        for k, v in caso['esperado'].items():
            if isinstance(v, str) and v not in estados and v not in CLAVES.values():
                err.append('CASOS_G5 %s: texto esperado %r que no es una CLAVE EN' % (caso['nombre'], v))
    import re
    rx = re.compile(TERMINOS_PROHIBIDOS)
    if not rx.search(TERMINO_PROHIBIDO_EJEMPLO):
        err.append('TERMINO_PROHIBIDO_EJEMPLO no lo caza TERMINOS_PROHIBIDOS')
    for k, v in list(_GLOSARIO_CATERING.items()) + list(POR_CELDA.items()) + list(CLAVES.items()):
        if rx.search(v):
            err.append('término prohibido en un texto EN fijado: %r → %r' % (k, v))
    if CITA_AUTOTEST.strip('()').split()[-1] in ' '.join(f for _v, f in REGLAS_US.values()):
        err.append('CITA_AUTOTEST está en REGLAS_US: G7 no la cazaría')
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
    for (c, h, coord) in VALORES_EN:
        if (c, h, coord) in tx:
            err.append('VALORES_EN: %r es texto en el ES (se esperaba el número)' % ((c, h, coord),))
    for fila in FILAS_CALENDARIO:
        for col in 'BCE':
            if (HOJA_CAL[0], HOJA_CAL[1], '%s%d' % (col, fila)) not in tx:
                err.append('calendario: %s%d sin texto en el ES' % (col, fila))
        e = tx.get((HOJA_CAL[0], HOJA_CAL[1], 'E%d' % fila))
        if e and e not in GLOSARIO:
            err.append('calendario: la antelación %r (E%d) no está en el GLOSARIO' % (e, fila))
    return err


# ==========================================================================
# G5 (gates_en.py): casos del 09 calculados en una copia. (hoja ES, celda) → valor; los textos esperados en EN.
# ==========================================================================
_CAJA = {(H_LIQ, 'B%d' % f): 1 for f, _es, _x, _en, _xen in DENOMINACIONES}
CASOS_G5 = [
    {'nombre': 'efectivo 1 de cada', 'entradas': dict(list(_CAJA.items()) + [((H_LIQ, 'C47'), 4.91)]),
     'esperado': {(H_LIQ, 'C46'): 204.91, (H_LIQ, 'C48'): 200}},
    {'nombre': 'liquidación con saldo', 'entradas': {
        (H_REG, 'C3'): 0.0825, (H_LIQ, 'C10'): 10000, (H_LIQ, 'C11'): 500, (H_LIQ, 'C12'): 10000,
        (H_LIQ, 'C13'): 500, (H_LIQ, 'C19'): 4000, (H_LIQ, 'C21'): 0,
        (H_REG, 'D6'): 10500, (H_REG, 'F6'): 4000, (H_REG, 'G6'): 6000},
     'esperado': {(H_LIQ, 'C14'): CLAVES['OK: las dos bases suman presupuesto + extras'], (H_LIQ, 'C15'): 825,
                  (H_LIQ, 'C16'): 0, (H_LIQ, 'C17'): 11325, (H_LIQ, 'C20'): 7325, (H_LIQ, 'C22'): 7325,
                  (H_LIQ, 'C24'): 'Pending', (H_REG, 'E6'): 11366.25, (H_REG, 'H6'): 1366.25,
                  (H_REG, 'K6'): 'Pending', (H_REG, 'D33'): 1, (H_REG, 'D34'): 0}},
    {'nombre': 'liquidación cobrada y bases que no cuadran', 'entradas': {
        (H_REG, 'C3'): 0.0825, (H_LIQ, 'C10'): 10000, (H_LIQ, 'C11'): 500, (H_LIQ, 'C12'): 10000,
        (H_LIQ, 'C13'): 0, (H_LIQ, 'C19'): 4000, (H_LIQ, 'C21'): 6825},
     'esperado': {(H_LIQ, 'C14'): CLAVES['REVISA: las dos bases no suman presupuesto + extras'],
                  (H_LIQ, 'C17'): 10825, (H_LIQ, 'C22'): 0, (H_LIQ, 'C24'): 'Paid'}},
    {'nombre': 'registro vencido', 'entradas': {
        (H_REG, 'C3'): 0, (H_REG, 'D6'): 1000, (H_REG, 'F6'): 300, (H_REG, 'J6'): 'FECHA_PASADA'},
     'esperado': {(H_REG, 'E6'): 1000, (H_REG, 'H6'): 700, (H_REG, 'K6'): 'OVERDUE', (H_REG, 'D34'): 1}},
]
CELDA_CACHE_MAL = 'C12'                                          # autotest G6: una entrada del 09 que mueve el total
HOJA_HORAS = ('08', 'Apertura del Negocio')                    # autotest G2/G4: la hoja con horas de celda
HOJA_VERDE = ('08', 'Apertura del Negocio')                    # autotest G1: una hoja protegida con verdes desbloqueadas
CITA_AUTOTEST = '(FDA Food Code 3-501.18)'                     # autotest G7: una cita que NO está en REGLAS_US


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas_catering.py: {} ficheros · {} pestañas · {} glosario · {} por celda · {} valores · {} adaptar · '
          '{} fórmulas por celda · {} reglas · {} errores'.format(
              len(FICHEROS), len(HOJAS), len(GLOSARIO), len(POR_CELDA), len(VALORES_EN), len(ADAPTAR),
              len(FORMULAS_POR_CELDA), len(REGLAS_US), len(e)))
    raise SystemExit(1 if e else 0)
