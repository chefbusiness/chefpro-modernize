#!/usr/bin/env python3
"""
mapas.py — HACCP Food Safety Kit Pro (EN) · mapas ES→EN del Pack Plantillas APPCC v2.0.

SPEC: `scripts/productos-digitales/haccp-kit/SPEC.md` (D1-Dn). Sesión Claude Code, 3-oct-2026.
Copia adaptada de `restaurant-inventory-kit/mapas.py`. Importable SIN efectos (solo constantes y
funciones). Ejecutado como script corre el autotest (pestañas ≤ 31 caracteres y sin caracteres
prohibidos, listas de DV ≤ 255 caracteres y sin comas dentro de un ítem, tokens de CF sin colisiones
dentro de un mismo rango, conversiones °C→°F coherentes con los límites) y, si existe `censo_es.json`
al lado, comprueba que TODAS las pestañas, listas de DV, literales de fórmula y de CF, patrones de
fórmula con cifras de mercado y DV numéricas del censo tienen su EN.

    python3 mapas.py

Contenido:
  · PRODUCTO / SLUG / URL_PRODUCTO / VERSION_ES / PIE_ES / PIE_EN       (D1, D2, D21)
  · FICHEROS, TITULOS                                   nombres de fichero y título interior (D5)
  · HOJAS, HOJAS_ES_POR_LIBRO                           pestañas ES→EN (D6)
  · CLAVES                                              ítems de DV, literales de fórmula y de CF y
                                                        valores de celda iguales a un ítem (D7)
  · DV_LISTAS_ESPECIALES                                listas que cambian de nº de ítems (D13)
  · LIMITES_02                                          tabla «Limits» del 02 (D10)
  · TEMP_COLUMNAS / C_A_F / EJEMPLOS_NUM                °C→°F de los ejemplos y overrides (D9, D20)
  · DV_NUM                                              DV numéricas en °C → °F (D9)
  · FORMULAS_EN                                         patrones de fórmula con cifras de mercado (D10-D17)
  · PARAMETROS / ALTITUD_19                             celdas-parámetro de la fila 3 (D15-D17)
  · PATRONES_SIN_CAMBIO                                 fórmulas con comparación numérica que no cambian
  · CONSERVAR_ES / CONSERVAR_EN                         línea de conservación de los 21 libros (D19)
  · SIN_LETRAS                                          celdas sin letras que cambian (horas, AM/PM, 911)
  · SEVERIDAD_15                                        gravedad de los 25 puntos del 15 (D12)
  · LIMITES_F                                           límites US de las fórmulas con su fuente (SPEC §3)
  · POR_CELDA                                           textos EN fijados por celda (02 familias, 17 col. I y K)
"""
import json
import math
import os
import re
from collections import OrderedDict

AQUI = os.path.dirname(os.path.abspath(__file__))

# ==========================================================================
# 0. Producto (D1, D2, D21)
# ==========================================================================
PRODUCTO = 'HACCP Food Safety Kit Pro'
SLUG = 'haccp-templates'
URL_PRODUCTO = 'aichef.pro/en/digital-products/' + SLUG
VERSION_ES = '2.0'
PIE_ES = '— Pack de Plantillas APPCC · AI Chef Pro · aichef.pro'
PIE_EN = '— HACCP Food Safety Kit Pro · AI Chef Pro · aichef.pro'
FOOTER_EN = 'AI Chef Pro · aichef.pro · Page &P of &N'

# ==========================================================================
# 1. Ficheros y títulos (D5: intención de búsqueda US/UK, no traducción literal)
# ==========================================================================
FICHEROS = OrderedDict([
    ('01-registro-temperaturas-diario.xlsx', '01-food-temperature-log.xlsx'),
    ('02-registro-temperaturas-recepcion.xlsx', '02-receiving-temperature-log.xlsx'),
    ('03-plan-limpieza-desinfeccion.xlsx', '03-cleaning-sanitizing-schedule.xlsx'),
    ('04-registro-limpieza-diaria.xlsx', '04-daily-cleaning-checklist.xlsx'),
    ('05-checklist-recepcion-mercancias.xlsx', '05-receiving-checklist.xlsx'),
    ('06-registro-trazabilidad.xlsx', '06-traceability-log.xlsx'),
    ('07-control-plagas-ddd.xlsx', '07-pest-control-log.xlsx'),
    ('08-matriz-alergenos.xlsx', '08-allergen-matrix.xlsx'),
    ('09-control-aceite-fritura.xlsx', '09-fryer-oil-log.xlsx'),
    ('10-control-agua-potable.xlsx', '10-water-quality-log.xlsx'),
    ('11-registro-acciones-correctivas.xlsx', '11-corrective-action-log.xlsx'),
    ('12-analisis-peligros-haccp.xlsx', '12-haccp-plan-hazard-analysis.xlsx'),
    ('13-checklist-higiene-personal.xlsx', '13-employee-hygiene-health-checklist.xlsx'),
    ('14-fichas-14-alergenos.xlsx', '14-allergen-chart-reaction-protocol.xlsx'),
    ('15-guia-inspeccion-sanidad.xlsx', '15-health-inspection-checklist.xlsx'),
    ('16-registro-coccion-regeneracion.xlsx', '16-cooking-reheating-log.xlsx'),
    ('17-registro-enfriamiento-descongelacion.xlsx', '17-cooling-thawing-log.xlsx'),
    ('18-registro-congelacion-anisakis.xlsx', '18-parasite-destruction-log.xlsx'),
    ('19-verificacion-termometros.xlsx', '19-thermometer-calibration-log.xlsx'),
    ('BONUS-01-registro-formacion.xlsx', 'BONUS-01-food-safety-training-log.xlsx'),
    ('BONUS-02-protocolo-alerta-alimentaria.xlsx', 'BONUS-02-food-recall-response-plan.xlsx'),
])
LIBROS_ES = list(FICHEROS)

TITULOS = OrderedDict([
    ('01-food-temperature-log.xlsx', 'Food Temperature Log: Coolers, Freezers & Hot Holding'),
    ('02-receiving-temperature-log.xlsx', 'Receiving Temperature Log'),
    ('03-cleaning-sanitizing-schedule.xlsx', 'Master Cleaning & Sanitizing Schedule'),
    ('04-daily-cleaning-checklist.xlsx', 'Daily Cleaning Checklist (AM/PM)'),
    ('05-receiving-checklist.xlsx', 'Receiving Checklist for Deliveries'),
    ('06-traceability-log.xlsx', 'Food Traceability Log (Lots In & Out)'),
    ('07-pest-control-log.xlsx', 'Pest Control Log & Bait Station Map'),
    ('08-allergen-matrix.xlsx', 'Menu Allergen Matrix (US Big 9 & UK 14)'),
    ('09-fryer-oil-log.xlsx', 'Fryer Oil Log (TPM Tests & Disposal)'),
    ('10-water-quality-log.xlsx', 'Water Quality Log (Chlorine & Private Supply)'),
    ('11-corrective-action-log.xlsx', 'Corrective Action Log'),
    ('12-haccp-plan-hazard-analysis.xlsx', 'HACCP Plan Template: Hazard Analysis & CCPs'),
    ('13-employee-hygiene-health-checklist.xlsx', 'Employee Hygiene & Health Checklist'),
    ('14-allergen-chart-reaction-protocol.xlsx', 'Allergen Chart & Allergic Reaction Protocol'),
    ('15-health-inspection-checklist.xlsx', 'Health Inspection Self-Checklist'),
    ('16-cooking-reheating-log.xlsx', 'Cooking & Reheating Temperature Log'),
    ('17-cooling-thawing-log.xlsx', 'Cooling & Thawing Log (2-Stage Cooling)'),
    ('18-parasite-destruction-log.xlsx', 'Parasite Destruction Log (Fish Served Raw)'),
    ('19-thermometer-calibration-log.xlsx', 'Thermometer Calibration Log'),
    ('BONUS-01-food-safety-training-log.xlsx', 'BONUS: Food Safety Training Log'),
    ('BONUS-02-food-recall-response-plan.xlsx', 'BONUS: Food Recall & Foodborne Illness Response Plan'),
])

# ==========================================================================
# 2. Pestañas (D6) — nombres ≤ 31 caracteres, sin []:*?/\
# ==========================================================================
HOJAS = OrderedDict([
    ('Instrucciones', 'Instructions'),
    ('Registro Semanal', 'Weekly Log'),
    ('Recepción Temperaturas', 'Receiving Temps'),
    ('Límites', 'Limits'),
    ('Plan Maestro L+D', 'Master Cleaning Plan'),
    ('Productos químicos', 'Chemicals'),
    ('Limpieza Diaria', 'Daily Cleaning'),
    ('Recepción Mercancías', 'Receiving Checklist'),
    ('Trazabilidad', 'Traceability In'),
    ('Salida y uso interno', 'Traceability Out'),
    ('Control Plagas DDD', 'Pest Control Log'),
    ('Plano de cebos', 'Bait Station Map'),
    ('Matriz Alérgenos', 'Allergen Matrix'),
    ('Control Aceite', 'Oil Tests'),
    ('Retirada de aceite usado', 'Used Oil Pickups'),
    ('Control Agua', 'Water Checks'),
    ('Acciones Correctivas', 'Corrective Actions'),
    ('Análisis Peligros', 'Hazard Analysis'),
    ('Higiene Personal', 'Hygiene Checklist'),
    ('14 Alérgenos', 'Allergen Chart'),
    ('25 Puntos Inspección', '25-Point Self-Inspection'),
    ('Cocción y Regeneración', 'Cooking & Reheating'),
    ('Enfriamiento', 'Cooling'),
    ('Descongelación', 'Thawing'),
    ('Congelación Anisakis', 'Parasite Destruction'),
    ('Verificación Termómetros', 'Calibration Log'),
    ('Formación Personal', 'Training Log'),
    ('Protocolo Alerta', 'Response Plan'),
])

HOJAS_ES_POR_LIBRO = OrderedDict([
    ('01', ['Instrucciones', 'Registro Semanal']),
    ('02', ['Instrucciones', 'Recepción Temperaturas', 'Límites']),
    ('03', ['Instrucciones', 'Plan Maestro L+D', 'Productos químicos']),
    ('04', ['Instrucciones', 'Limpieza Diaria']),
    ('05', ['Instrucciones', 'Recepción Mercancías']),
    ('06', ['Instrucciones', 'Trazabilidad', 'Salida y uso interno']),
    ('07', ['Instrucciones', 'Control Plagas DDD', 'Plano de cebos']),
    ('08', ['Instrucciones', 'Matriz Alérgenos']),
    ('09', ['Instrucciones', 'Control Aceite', 'Retirada de aceite usado']),
    ('10', ['Instrucciones', 'Control Agua']),
    ('11', ['Instrucciones', 'Acciones Correctivas']),
    ('12', ['Instrucciones', 'Análisis Peligros']),
    ('13', ['Instrucciones', 'Higiene Personal']),
    ('14', ['Instrucciones', '14 Alérgenos']),
    ('15', ['Instrucciones', '25 Puntos Inspección']),
    ('16', ['Instrucciones', 'Cocción y Regeneración']),
    ('17', ['Instrucciones', 'Enfriamiento', 'Descongelación']),
    ('18', ['Instrucciones', 'Congelación Anisakis']),
    ('19', ['Instrucciones', 'Verificación Termómetros']),
    ('B01', ['Instrucciones', 'Formación Personal']),
    ('B02', ['Instrucciones', 'Protocolo Alerta']),
])

HOJA_PROHIBIDOS = set('[]:*?/\\')

# ==========================================================================
# 3. Claves (D7): un solo diccionario ES→EN para ítems de DV, literales de fórmula, tokens de CF
#    (todas las CF del pack son de igualdad exacta, no SEARCH) y celdas cuyo valor ES un ítem.
# ==========================================================================
# Semáforo universal del pack: las 3 reglas de CF de cada rango repiten estas listas (rojo/ámbar/verde)
SEMAFORO_ROJO = OrderedDict([('ALERTA', 'ALERT'), ('RECHAZAR', 'REJECT'), ('CAMBIAR', 'CHANGE'),
                             ('REVISAR', 'INVESTIGATE'), ('✗', '✗'), ('CADUCADO', 'EXPIRED'),
                             ('EXCESO', 'EXCESS')])
SEMAFORO_AMBAR = OrderedDict([('VIGILAR', 'WATCH'), ('⚠', '⚠'), ('INCOMPLETO', 'INCOMPLETE'),
                              ('CADUCA PRONTO', 'EXPIRES SOON'), ('RENOVAR', 'RENEW'),
                              ('FALTA CLORO', 'CHLORINE MISSING'), ('FALTA TEST', 'TEST MISSING')])
SEMAFORO_VERDE = OrderedDict([('OK', 'OK'), ('✓', '✓'), ('Cumple', 'Compliant'), ('VIGENTE', 'CURRENT'),
                              ('Completo', 'Complete'), ('APTO', 'PASS')])

CLAVES = OrderedDict()
for _d in (SEMAFORO_ROJO, SEMAFORO_AMBAR, SEMAFORO_VERDE):
    CLAVES.update(_d)
CLAVES.update([
    # respuestas cortas (03, 05, 08, 10, 02)
    ('S', 'Y'), ('N', 'N'), ('N/A', 'N/A'), ('SÍ', 'YES'), ('NO', 'NO'), ('T', 'T'),
    # 03 frecuencias
    ('Cada uso', 'After each use'), ('Cada servicio', 'Each service'), ('2 veces/día', 'Twice a day'),
    ('Diaria', 'Daily'), ('Semanal', 'Weekly'), ('Quincenal', 'Every 2 weeks'), ('Mensual', 'Monthly'),
    ('Trimestral', 'Quarterly'), ('Semestral', 'Twice a year'), ('Anual', 'Yearly'),
    # 07 plagas
    ('Desinsectación', 'Insect treatment'), ('Desratización', 'Rodent treatment'),
    ('Desinfección', 'Disinfection'), ('Revisión de cebos', 'Bait station check'),
    ('Inspección visual', 'Visual inspection'), ('Otro', 'Other'),
    ('Cebadero de roedores', 'Rodent bait station'), ('Trampa de captura', 'Mechanical trap'),
    ('Lámpara insectocutora', 'Insect light trap'), ('Trampa de feromonas', 'Pheromone trap'),
    ('Sin consumo', 'No activity'), ('Consumo parcial', 'Partial bait taken'),
    ('Consumo total', 'All bait taken'), ('Captura', 'Catch'), ('Dañado', 'Damaged'), ('Ausente', 'Missing'),
    # 08 alérgenos
    ('Entrantes', 'Appetizers'), ('Primeros', 'First courses'), ('Segundos', 'Entrées'),
    ('Postres', 'Desserts'), ('Bebidas', 'Drinks'), ('Tapas', 'Small plates'), ('Desayunos', 'Breakfast'),
    ('Infantil', 'Kids'), ('Otros', 'Other'),
    ('⚠ SIN VERIFICAR', '⚠ NOT VERIFIED'), ('⚠ FALTA ESPECIE', '⚠ SPECIFY TYPE'),
    # 09 aceite
    ('Tiras reactivas', 'Test strips'), ('Medidor digital', 'Digital TPM meter'), ('Visual', 'Visual'),
    # 10 agua
    ('Normal', 'Normal'), ('Turbio', 'Cloudy'), ('Olor extraño', 'Odd smell'), ('Color anormal', 'Abnormal color'),
    # 11 acciones correctivas
    ('Temperatura', 'Temperature'), ('Producto rechazado', 'Rejected product'), ('Limpieza', 'Cleaning'),
    ('Plagas', 'Pests'), ('Reclamación de cliente', 'Customer complaint'), ('Alérgeno', 'Allergen'),
    ('Contaminación', 'Contamination'), ('Caducidad', 'Expired / date mark'), ('Trazabilidad', 'Traceability'),
    ('Formación', 'Training'),
    ('01 Temperaturas diario', '01 Food temperatures'), ('02 Recepción temperaturas', '02 Receiving temps'),
    ('04 Limpieza diaria', '04 Daily cleaning'), ('05 Recepción mercancías', '05 Receiving checklist'),
    ('06 Trazabilidad', '06 Traceability'), ('07 Plagas', '07 Pest control'), ('08 Alérgenos', '08 Allergens'),
    ('09 Aceite', '09 Fryer oil'), ('10 Agua', '10 Water'), ('16 Cocción', '16 Cooking & reheating'),
    ('17 Enfriamiento', '17 Cooling & thawing'), ('18 Anisakis', '18 Parasite destruction'),
    ('19 Termómetros', '19 Thermometers'),
    ('Desechado', 'Discarded'), ('Devuelto al proveedor', 'Returned to vendor'), ('Reprocesado', 'Reworked'),
    ('Liberado tras evaluación', 'Released after evaluation'), ('Pendiente de decisión', 'Pending decision'),
    ('No aplica', 'Not applicable'),
    ('Pendiente', 'Pending'), ('Verificado OK', 'Verified OK'), ('Requiere seguimiento', 'Follow-up needed'),
    # 12 análisis de peligros
    ('B (Biológico)', 'B (Biological)'), ('Q (Químico)', 'C (Chemical)'), ('F (Físico)', 'P (Physical)'),
    ('Alta', 'High'), ('Media', 'Medium'), ('Baja', 'Low'),
    ('Crítico', 'Critical'), ('Alto', 'High'), ('Medio', 'Medium'), ('Bajo', 'Low'),
    ('PCC', 'CCP'), ('PPRo', 'OPRP'),
    # 15 inspección (D12: gravedad Ley 17/2011 → categorías del FDA Food Code)
    ('✓ Cumple', '✓ Compliant'), ('⚠ Mejorar', '⚠ Needs work'), ('✗ No cumple', '✗ Not compliant'),
    ('Muy grave', 'Priority'), ('Grave', 'Priority foundation'), ('Leve', 'Core'),
    # 16 cocción
    ('REPETIR', 'REPEAT'),
    # 19 termómetros
    ('Hielo fundente (0 °C)', 'Ice point (32 °F)'), ('Agua en ebullición (100 °C)', 'Boiling point (212 °F)'),
    ('NO APTO', 'FAIL'),
    # BONUS-01 formación (D18)
    ('Higiene alimentaria (manipulación de alimentos)', 'Food handler training'),
    ('APPCC básico', 'Certified Food Protection Manager (CFPM)'), ('APPCC avanzado', 'HACCP training'),
    ('Alérgenos e información al consumidor', 'Food allergen awareness'),
    ('Limpieza y desinfección', 'Cleaning & sanitizing'), ('Primeros auxilios', 'First aid & CPR'),
    ('Prevención de riesgos laborales', 'Workplace safety (OSHA / HSE)'), ('Otra', 'Other'),
])

# Línea de conservación (D19): se escribe igual en los 21 libros; las variantes con prefijo se traducen
CONSERVAR_ES = ('Conservar al menos 2 años (trazabilidad y proveedores: 5); el Reg. (CE) 178/2002 exige '
                'trazabilidad pero no fija plazo — consulta la guía de prácticas correctas de higiene de tu '
                'comunidad autónoma.')
CONSERVAR_EN = ('Keep these records for at least 2 years (house rule of this kit). FDA Food Code minimum: '
                '90 days for shellstock tags and parasite-destruction records (§3-203.12, §3-402.12); '
                'follow your health department if it asks for longer.')

# Fórmulas con comparaciones numéricas que NO cambian en EN (puntuación de riesgo 1-9 y días de aviso),
# por (libro, hoja, primera celda del patrón). Solo cambian sus literales (CLAVES).
PATRONES_SIN_CAMBIO = {('12', 'Análisis Peligros', 'G5'), ('B01', 'Formación Personal', 'J5')}

# Listas que cambian de forma (D13): la del 16 pasa de 2 procesos a 5 con su límite en °F entre paréntesis
PROCESOS_16 = ['Cook: poultry & stuffed foods (165 °F)', 'Cook: ground meat & eggs hot-held (155 °F)',
               'Cook: steaks/fish/eggs to order (145 °F)', 'Cook: veg for hot holding (135 °F)',
               'Reheat for hot holding (165 °F)']
DV_LISTAS_ESPECIALES = OrderedDict([
    (('16', 'Cocción y Regeneración', 'C5:C44'), ('"Cocción,Regeneración"', '"' + ','.join(PROCESOS_16) + '"')),
])

# ==========================================================================
# 4. Temperaturas (D9-D10). °F primero; °C entre paréntesis SOLO en texto.
# ==========================================================================
def c_a_f(c, dec=0):
    """°C→°F redondeando HALF-UP (no el redondeo bancario de round())."""
    f = c * 9.0 / 5.0 + 32.0
    k = 10 ** dec
    v = math.floor(f * k + 0.5) / k
    return int(v) if dec == 0 else v


# Columnas con temperaturas numéricas de ejemplo en °C, por hoja (se convierten con c_a_f)
TEMP_COLUMNAS = OrderedDict([
    (('01', 'Registro Semanal'), ('BG', 0)),
    (('02', 'Recepción Temperaturas'), ('D', 0)),
    (('05', 'Recepción Mercancías'), ('D', 0)),
    (('09', 'Control Aceite'), ('E', 0)),
    (('16', 'Cocción y Regeneración'), ('E', 0)),
    (('17', 'Enfriamiento'), ('DF', 0)),
    (('17', 'Descongelación'), ('F', 0)),
    (('18', 'Congelación Anisakis'), ('F', 0)),
    (('19', 'Verificación Termómetros'), ('E', 1)),
])

# Overrides de ejemplo (D20): mandan sobre la conversión cuando el límite US cambiaría el veredicto
# o cuando la regla US necesita otro dato. Cadena = fórmula/valor literal EN; número = valor EN.
EJEMPLOS_NUM = OrderedDict([
    (('02', 'Recepción Temperaturas', 'D6'), 38),      # 5,5 °C = 42 °F rechazaría (límite US 41 °F)
    (('05', 'Recepción Mercancías', 'D6'), 38),        # misma entrega que 02!D6
    (('17', 'Enfriamiento', 'F7'), 78),                # 14 °C = 57 °F pasaría el 1.er tramo (≤ 70 °F): INC-005
    (('17', 'Enfriamiento', 'I5'), 38),                # D14: 2.º tramo (≤ 41 °F a las 6 h)
    (('17', 'Enfriamiento', 'I6'), 39),
    (('17', 'Enfriamiento', 'I7'), None),              # desechado: sin lectura a las 6 h
    (('18', 'Congelación Anisakis', 'E5'), '+169h'),   # D15: 168 h a −4 °F → salida = entrada + 169 h
    (('18', 'Congelación Anisakis', 'F6'), -33),       # D15: vía −31 °F / 15 h
    (('18', 'Congelación Anisakis', 'E6'), '+16h'),
    (('16', 'Cocción y Regeneración', 'C5'), PROCESOS_16[1]),
    (('16', 'Cocción y Regeneración', 'C6'), PROCESOS_16[4]),
    (('16', 'Cocción y Regeneración', 'C7'), PROCESOS_16[4]),
])

# DV numéricas en °C → °F (mismo sqref; mensajes EN en °F)
DV_NUM = OrderedDict([
    (('01', 'Registro Semanal'), (('-40', '130'), ('-40', '266'))),
    (('02', 'Recepción Temperaturas'), (('-40', '60'), ('-40', '140'))),
    (('09', 'Control Aceite', 'E'), (('0', '250'), ('32', '482'))),
    (('16', 'Cocción y Regeneración', 'E'), (('0', '250'), ('32', '482'))),
    (('17', 'Enfriamiento'), (('-30', '130'), ('-22', '266'))),
    (('17', 'Descongelación'), (('-5', '20'), ('23', '68'))),
    (('18', 'Congelación Anisakis'), (('-60', '0'), ('-76', '32'))),
    (('19', 'Verificación Termómetros'), (('-60', '150'), ('-76', '302'))),
])

# Tabla «Limits» del 02 (D10): filas A5:C14, máx. en °F. Base = FDA Food Code 2022 §3-202.11 salvo nota.
# (familia EN, máx °F o 'N/A', base EN que se escribe en C)
LIMITES_02 = [
    ('Fresh fish (packed on ice)', 41, 'FDA Food Code 2022 §3-202.11(A)'),
    ('Raw meat: beef, pork, lamb & ground', 41, 'FDA Food Code 2022 §3-202.11(A)'),
    ('Raw poultry', 41, 'FDA Food Code 2022 §3-202.11(A)'),
    ('Live shellfish (shellstock)', 45, '§3-202.11(B) and NSSP: air temperature; cool to 41 °F after receipt'),
    ('Shucked shellfish', 45, '§3-202.11(B) and NSSP: cool to 41 °F within 4 hours'),
    ('Milk & fluid dairy', 45, '§3-202.11(B) and the PMO: cool to 41 °F within 4 hours'),
    ('Shell eggs', 45, '§3-202.11(C): ambient air temperature of the truck'),
    ('Other refrigerated TCS food (deli, cheese, cut produce)', 41, 'FDA Food Code 2022 §3-202.11(A)'),
    ('Frozen food', 0, '§3-202.11(E) says «received frozen»; 0 °F (−18 °C) is the usual spec'),
    ('Ambient / shelf-stable', 'N/A', '§3-202.15: intact package, label and use-by date'),
]

# Celdas de TEXTO con EN fijado por la SPEC (aplicar_en las escribe tras los textos traducidos):
# familias de los ejemplos del 02 (= filas de LIMITES_02: si no, el VLOOKUP no las encuentra), cabecera
# de la columna I del 17 (D14) y destino de los ejemplos 1-2 del 17, que pasa a «Notes» (D14).
POR_CELDA = OrderedDict([
    (('02', 'Recepción Temperaturas', 'E5'), LIMITES_02[0][0]),
    (('02', 'Recepción Temperaturas', 'E6'), LIMITES_02[1][0]),
    (('02', 'Recepción Temperaturas', 'E7'), LIMITES_02[8][0]),
    (('17', 'Enfriamiento', 'I4'), 'Temp at 6 h (°F)'),
    (('17', 'Enfriamiento', 'K5'), 'Walk-in 1, for next-day service (sample)'),
    (('17', 'Enfriamiento', 'K6'), 'Walk-in 2 (sample)'),
])

# Límites de las fórmulas (D10-D17), con su fuente. Lista cerrada: el gate G6 la recorre.
LIMITES_F = OrderedDict([
    ('frio', (32, 41, 'FDA Food Code 2022 §3-501.16(A)(2): ≤ 41 °F; 32 °F = suelo de calidad del ES [estimado]')),
    ('congelado', (0, None, '0 °F (−18 °C) [estimado: práctica; el Food Code no fija cifra de almacenamiento]')),
    ('caliente', (135, None, 'FDA Food Code 2022 §3-501.16(A)(1): ≥ 135 °F')),
    ('enfriar_2h', (70, None, 'FDA Food Code 2022 §3-501.14(A)(1): 135 → 70 °F en ≤ 2 h')),
    ('enfriar_6h', (41, None, 'FDA Food Code 2022 §3-501.14(A)(2): → 41 °F en ≤ 6 h en total')),
    ('recalentar', (165, 120, 'FDA Food Code 2022 §3-403.11(A),(E): 165 °F en ≤ 2 h')),
    ('parasitos', (-4, 168, 'FDA Food Code 2022 §3-402.11(A)(1): −4 °F durante 168 h (UK/UE: 24 h, parámetro B3)')),
    ('parasitos_rapido', (-31, 15, 'FDA Food Code 2022 §3-402.11(A)(2): −31 °F hasta sólido y 15 h')),
    ('termometro', (2, 32, 'FDA Food Code 2022 §4-203.11(A): ±2 °F (±1 °C); hielo fundente 32 °F')),
    ('ebullicion', (212, 550, '212 °F a nivel del mar, −1 °F cada 550 ft [estimado: ≡ 1 °C cada 300 m del ES]')),
    ('descongelar', (41, 24, 'FDA Food Code 2022 §3-501.13(A) (≤ 41 °F); 24 h = criterio del kit (parámetro B3)')),
    ('cloro', (0.2, 4.0, '40 CFR 141.72 (0,2 mg/L mínimo de entrada) y 141.65 (MRDL 4,0 mg/L)')),
    ('aceite', (375, None, '375 °F (190 °C) [estimado: rango comercial de fritura 350-375 °F]')),
])

# Patrones de fórmula con cifras de mercado (D10-D17). Clave = patrón ES normalizado (filas → {r},
# ver `patron()`), valor = patrón EN ya con hojas y literales EN. Lo que NO esté aquí tiene que salir
# idéntico tras aplicar HOJAS y CLAVES (gate G1).
FORMULAS_EN = OrderedDict([
    # 01: refrigeración y exposición fría 0-4 / 0-8 °C → 32-41 °F; congelación ≤ −18 → ≤ 0; caliente ≥ 65 → ≥ 135
    ('=IF($B{r}="","",IF(AND($B{r}>=0,$B{r}<=4),"OK","ALERTA"))',
     '=IF($B{r}="","",IF(AND($B{r}>=32,$B{r}<=41),"OK","ALERT"))'),
    ('=IF($G{r}="","",IF(AND($G{r}>=0,$G{r}<=4),"OK","ALERTA"))',
     '=IF($G{r}="","",IF(AND($G{r}>=32,$G{r}<=41),"OK","ALERT"))'),
    ('=IF($B{r}="","",IF(AND($B{r}>=0,$B{r}<=8),"OK","ALERTA"))',
     '=IF($B{r}="","",IF(AND($B{r}>=32,$B{r}<=41),"OK","ALERT"))'),
    ('=IF($G{r}="","",IF(AND($G{r}>=0,$G{r}<=8),"OK","ALERTA"))',
     '=IF($G{r}="","",IF(AND($G{r}>=32,$G{r}<=41),"OK","ALERT"))'),
    ('=IF($B{r}="","",IF($B{r}<=-18,"OK","ALERTA"))', '=IF($B{r}="","",IF($B{r}<=0,"OK","ALERT"))'),
    ('=IF($G{r}="","",IF($G{r}<=-18,"OK","ALERTA"))', '=IF($G{r}="","",IF($G{r}<=0,"OK","ALERT"))'),
    ('=IF($B{r}="","",IF($B{r}>=65,"OK","ALERTA"))', '=IF($B{r}="","",IF($B{r}>=135,"OK","ALERT"))'),
    ('=IF($G{r}="","",IF($G{r}>=65,"OK","ALERTA"))', '=IF($G{r}="","",IF($G{r}>=135,"OK","ALERT"))'),
    # 09: temperatura máxima de fritura 180 °C → 375 °F (D11); % de compuestos polares sin cambio
    ('=IF(AND($D{r}="",$E{r}=""),"",IF(IF($E{r}="",0,$E{r})>180,"CAMBIAR",IF($D{r}="","FALTA TEST",'
     'IF($D{r}>=25,"CAMBIAR",IF($D{r}>=20,"VIGILAR","OK")))))',
     '=IF(AND($D{r}="",$E{r}=""),"",IF(IF($E{r}="",0,$E{r})>375,"CHANGE",IF($D{r}="","TEST MISSING",'
     'IF($D{r}>=25,"CHANGE",IF($D{r}>=20,"WATCH","OK")))))'),
    # 10: cloro libre 0,2-1,0 mg/L (RD 3/2023) → 0,2-4,0 mg/L (EPA)
    ('=IF(AND($C{r}="",$D{r}=""),"",IF(AND($D{r}<>"",$D{r}<>"Normal"),"REVISAR",IF($C{r}="","FALTA CLORO",'
     'IF($D{r}="","INCOMPLETO",IF(AND($C{r}>=0.2,$C{r}<=1),"OK","REVISAR")))))',
     '=IF(AND($C{r}="",$D{r}=""),"",IF(AND($D{r}<>"",$D{r}<>"Normal"),"INVESTIGATE",IF($C{r}="","CHLORINE MISSING",'
     'IF($D{r}="","INCOMPLETE",IF(AND($C{r}>=0.2,$C{r}<=4),"OK","INVESTIGATE")))))'),
    # 08: la especie se exige también en crustáceos (E) y pescado (G): FALCPA (D8)
    ('=IF($B{r}="","",IF(COUNTIF($D{r}:$Q{r},"S")+COUNTIF($D{r}:$Q{r},"T")+COUNTIF($D{r}:$Q{r},"N")<14,'
     '"⚠ SIN VERIFICAR",IF(AND(OR($D{r}="S",$D{r}="T",$K{r}="S",$K{r}="T"),$R{r}=""),"⚠ FALTA ESPECIE","Completo")))',
     '=IF($B{r}="","",IF(COUNTIF($D{r}:$Q{r},"Y")+COUNTIF($D{r}:$Q{r},"T")+COUNTIF($D{r}:$Q{r},"N")<14,'
     '"⚠ NOT VERIFIED",IF(AND(OR($D{r}="Y",$D{r}="T",$E{r}="Y",$E{r}="T",$G{r}="Y",$G{r}="T",$K{r}="Y",$K{r}="T"),'
     '$R{r}=""),"⚠ SPECIFY TYPE","Complete")))'),
    # 16: límite por proceso = la cifra entre paréntesis del desplegable; recalentado en ≤ 120 min (D13)
    ('=IF($E{r}="","",IF($E{r}<75,"REPETIR",IF(AND($C{r}="Regeneración",$F{r}<>"",$F{r}>60),"REPETIR","OK")))',
     '=IF($E{r}="","",IF($E{r}<IFERROR(VALUE(MID($C{r},FIND("(",$C{r})+1,3)),165),"REPEAT",'
     'IF(AND(LEFT($C{r},6)="Reheat",$F{r}<>"",$F{r}>120),"REPEAT","OK")))'),
    # 17 Cooling: dos tramos 135→70 °F en 2 h y →41 °F en 6 h; la columna I pasa a «Temp at 6 h» (D14)
    ('=IF(OR($F{r}="",$G{r}=""),"",IF($D{r}="","INCOMPLETO",IF(AND($D{r}>=60,$F{r}<=10,$G{r}>0,$G{r}<=2),"OK","ALERTA")))',
     '=IF(OR($F{r}="",$G{r}=""),"",IF($D{r}="","INCOMPLETE",IF(AND($D{r}>=135,$F{r}<=70,$G{r}>0,$G{r}<=2),'
     'IF($I{r}="","INCOMPLETE",IF($I{r}<=41,"OK","ALERT")),"ALERT")))'),
    # 17 Thawing: cámara ≤ 41 °F y tiempo máximo = parámetro B3 (24 h por defecto, D16)
    ('=IF(OR($F{r}="",$G{r}=""),"",IF(AND($F{r}<=4,$G{r}<=24),"OK","ALERTA"))',
     '=IF(OR($F{r}="",$G{r}=""),"",IF(AND($F{r}<=41,$G{r}<=IF($B$3="",24,$B$3)),"OK","ALERT"))'),
    # 18: −4 °F durante B3 horas (168 por defecto; UK/UE 24) o −31 °F durante 15 h (D15)
    ('=IF(OR($F{r}="",$G{r}=""),"",IF(OR(AND($F{r}<=-20,$G{r}>=24),AND($F{r}<=-35,$G{r}>=15)),"OK","ALERTA"))',
     '=IF(OR($F{r}="",$G{r}=""),"",IF(OR(AND($F{r}<=-4,$G{r}>=IF($B$3="",168,$B$3)),AND($F{r}<=-31,$G{r}>=15)),"OK","ALERT"))'),
    # 19: hielo 32 °F; ebullición 212 °F − altitud en pies / 550 (≡ 1 °C cada 300 m del ES); tolerancia ±2 °F (D17)
    ('=IF($C{r}="","",IF($C{r}="Hielo fundente (0 °C)",0,IF($C{r}="Agua en ebullición (100 °C)",100-IF($B$3="",0,$B$3)/300,"")))',
     '=IF($C{r}="","",IF($C{r}="Ice point (32 °F)",32,IF($C{r}="Boiling point (212 °F)",212-IF($B$3="",0,$B$3)/550,"")))'),
    ('=IF($F{r}="","",IF(ABS($E{r}-$D{r})<=1,"APTO","NO APTO"))',
     '=IF($F{r}="","",IF(ABS($E{r}-$D{r})<=2,"PASS","FAIL"))'),
])

# Celdas-parámetro nuevas (D15, D16): copian el patrón de 19!A3:C3 (etiqueta · celda verde · nota)
PARAMETROS = OrderedDict([
    (('17', 'Descongelación'), ('Max. thawing time (hours):', 24,
                                'House limit for portions. Large items need longer: allow about 24 h per 4-5 lb '
                                '(USDA FSIS) and raise this number.')),
    (('18', 'Congelación Anisakis'), ('Minimum hours at -4 °F or below:', 168,
                                      'US Food Code §3-402.11: 168 h (7 days). UK and EU rule: 24 h at -20 °C '
                                      '(-4 °F): type 24 if you operate in the UK.')),
])
# Celdas SIN letras que cambian en EN (el extractor las excluye de textos_es.json): horas de 12 h, turnos
# mañana/tarde del 04 y el teléfono de emergencias del BONUS-02 (D7, D21, D23)
SIN_LETRAS = OrderedDict([
    (('01', 'Registro Semanal', 'D7'), '8:15 AM'), (('01', 'Registro Semanal', 'I7'), '7:40 PM'),
    (('01', 'Registro Semanal', 'D8'), '8:10 AM'), (('01', 'Registro Semanal', 'I8'), '7:35 PM'),
    (('01', 'Registro Semanal', 'D9'), '8:20 AM'), (('01', 'Registro Semanal', 'I9'), '7:45 PM'),
    (('B02', 'Protocolo Alerta', 'C29'), '911 (UK: 999)'),
])
for _i, _col in enumerate('BCDEFGHIJKLMNO'):
    SIN_LETRAS[('04', 'Limpieza Diaria', _col + '5')] = ('AM', 'PM')[_i % 2]

# 15: gravedad por punto (D12) = categoría del FDA Food Code 2022 de la sección que lo regula.
# Las marcas P / Pf / C se comprueban UNA vez en F2 contra el PDF del Food Code (revisión adversarial).
SEVERIDAD_15 = OrderedDict([
    (6, ('Priority foundation', '§8-201.13-.14 HACCP plan')), (7, ('Priority foundation', '§8-201.14(D) records')),
    (8, ('Priority foundation', '§2-102.11-.12 PIC knowledge, CFPM')),
    (9, ('Priority foundation', '§3-602.12 allergen notice')), (10, ('Priority foundation', '§6-501.111 pests')),
    (12, ('Priority', '§3-501.16(A)(2) cold holding')), (13, ('Priority foundation', '§4-301.11 equipment')),
    (14, ('Priority', '§3-501.16(A)(1) hot holding')), (15, ('Priority foundation', '§4-302.12 thermometer')),
    (16, ('Priority foundation', '§4-502.11 calibration')), (18, ('Core', '§6-501.12 cleaning')),
    (19, ('Core', '§4-101.11 materials')), (20, ('Priority foundation', '§5-205.11 handwashing sink')),
    (21, ('Priority', '§3-302.11 separation')), (22, ('Core', '§6-305.11 dressing areas')),
    (24, ('Priority', '§3-501.18 discard past date')), (25, ('Priority', '§3-302.11(A) raw below RTE')),
    (26, ('Priority foundation', '§3-501.17 date marking')), (27, ('Core', '§3-305.11 off the floor')),
    (28, ('Priority', '§7-201.11 chemicals')), (30, ('Core', '§2-302/2-303/2-402 hygiene')),
    (31, ('Core', 'kit criterion, no Food Code item')), (32, ('Priority foundation', '§3-501.13 thawing')),
    (33, ('Priority', '§3-402.11 parasite destruction')), (34, ('Priority foundation', '§2-103.11(N) allergens')),
])

# 19!A3: la altitud pasa a pies (D17)
ALTITUD_19 = ('Elevation of your kitchen (feet above sea level):',
              'Corrects the boiling-point reference. Leave 0 at sea level.')


def patron(formula):
    """Normaliza las filas de las referencias de celda a {r} (las referencias absolutas $X$n se respetan)."""
    return re.sub(r'(?<![A-Za-z_$])(\$?[A-Z]{1,3})(?<!\$)(\d+)(?![\d(])',
                  lambda m: m.group(1) + '{r}', formula)


def todas_las_claves():
    return OrderedDict((k, ('clave', v)) for k, v in CLAVES.items())


def dv_lista(items):
    return '"' + ','.join(items) + '"'


# ==========================================================================
# 5. Autotest y cruce con el censo
# ==========================================================================
RX_LIT = re.compile(r'"((?:[^"]|"")*)"')


def autotest():
    err = []
    for es, en in HOJAS.items():
        if len(en) > 31 or set(en) & HOJA_PROHIBIDOS or en.startswith("'"):
            err.append('pestaña inválida: ' + en)
    for f, hs in HOJAS_ES_POR_LIBRO.items():
        ens = [HOJAS[h] for h in hs]
        if len(set(ens)) != len(ens):
            err.append('pestañas EN duplicadas en ' + f)
    if len(FICHEROS) != 21 or len(set(FICHEROS.values())) != 21:
        err.append('FICHEROS debe tener 21 nombres EN distintos')
    for es, en in FICHEROS.items():
        if en not in TITULOS:
            err.append('fichero sin título: ' + en)
        if es[:2] != en[:2] or not re.fullmatch(r'(BONUS-)?\d{2}-[a-z0-9-]+\.xlsx', en):
            err.append('fichero EN mal formado: ' + en)
    for k, v in CLAVES.items():
        if ',' in v:
            err.append('coma dentro de una clave EN: %r' % v)
    if any(',' in p for p in PROCESOS_16) or len(dv_lista(PROCESOS_16)) > 255:
        err.append('PROCESOS_16 no cabe en una DV de lista')
    for p in PROCESOS_16:
        m = re.search(r'\((\d{3}) °F\)$', p)
        if not m:
            err.append('proceso sin límite «(nnn °F)» al final: ' + p)
    if len(SEVERIDAD_15) != 25 or {v[0] for v in SEVERIDAD_15.values()} - {'Priority', 'Priority foundation', 'Core'}:
        err.append('SEVERIDAD_15: 25 puntos con Priority / Priority foundation / Core')
    if len(SIN_LETRAS) != 21:
        err.append('SIN_LETRAS debe tener 21 celdas (6 horas + 14 turnos + 1 teléfono)')
    for k, v in POR_CELDA.items():
        if re.search(r'[áéíóúñ¿¡]|\bde\b|\by\b', v):
            err('POR_CELDA con español: %r' % (k,))
    if len(LIMITES_02) != 10:
        err.append('LIMITES_02 debe tener 10 filas (A5:A14)')
    # el semáforo universal tiene que ser inyectivo
    sem = list(SEMAFORO_ROJO.values()) + list(SEMAFORO_AMBAR.values()) + list(SEMAFORO_VERDE.values())
    if len(set(sem)) != len(sem):
        err.append('semáforo EN con tokens repetidos')
    # conversiones: los ejemplos convertidos conservan el veredicto (lo comprueba G6 en F2); aquí, sanidad
    if c_a_f(4) != 39 or c_a_f(-18) != 0 or c_a_f(65) != 149 or c_a_f(-1.8, 1) != 28.8:
        err.append('c_a_f no redondea half-up')
    for es, en in FORMULAS_EN.items():
        for lit in RX_LIT.findall(en):
            if lit and lit not in CLAVES.values() and lit not in ('Normal', 'Ice point (32 °F)', 'Boiling point (212 °F)',
                                                                   '(', 'Reheat', 'Y', 'T', 'N'):
                err.append('literal EN no previsto en FORMULAS_EN: %r' % lit)
        if re.search(r'[áéíóúñÁÉÍÓÚÑ¿¡]', en):
            err.append('español en FORMULAS_EN: ' + en[:60])
    return err


def cruzar_censo(p):
    censo = json.load(open(p, encoding='utf-8'))
    err = []
    for f, info in censo['libros'].items():
        if f not in FICHEROS:
            err.append('libro sin nombre EN: ' + f)
        c = info['corto']
        if HOJAS_ES_POR_LIBRO.get(c) != info['hojas']:
            err.append('HOJAS_ES_POR_LIBRO no coincide con el censo en ' + c)
        for h in info['hojas']:
            if h not in HOJAS:
                err.append('pestaña sin EN: %s / %s' % (f, h))
        for h, hd in info['hojas_detalle'].items():
            for dv in hd['dv']:
                f1 = dv['formula1'] or ''
                esp = DV_LISTAS_ESPECIALES.get((c, h, dv['sqref']))
                if esp:
                    if esp[0] != f1:
                        err.append('DV especial cambiada en el ES: %s / %s / %s' % (c, h, dv['sqref']))
                    continue
                if f1.startswith('"'):
                    for it in f1.strip('"').split(','):
                        if it not in CLAVES:
                            err.append('ítem de DV sin EN: %s / %s / %r' % (c, h, it))
                elif dv['type'] in ('decimal', 'whole') and dv['cita_temp']:
                    claves = [k for k in DV_NUM if k[:2] == (c, h)]
                    ok = any(DV_NUM[k][0] == (dv['formula1'], dv['formula2']) and
                             (len(k) == 2 or dv['sqref'].startswith(k[2])) for k in claves)
                    if not ok:
                        err.append('DV de temperatura sin EN: %s / %s / %s %s-%s' % (
                            c, h, dv['sqref'], dv['formula1'], dv['formula2']))
            for lit in list(hd['literales']) + list(hd['literales_cf']):
                if lit not in CLAVES and lit not in ('', 'Regeneración') and lit not in (
                        'Hielo fundente (0 °C)', 'Agua en ebullición (100 °C)'):
                    err.append('literal sin EN: %s / %s / %r' % (c, h, lit))
            for pat in hd['patrones_formula']:
                clave = (c, h, pat['celdas'].split('..')[0])
                if pat['cifras'] and pat['patron'] not in FORMULAS_EN and clave not in PATRONES_SIN_CAMBIO:
                    err.append('fórmula con comparación numérica sin decidir: %s / %s / %s' % (c, h, pat['patron'][:110]))
            # tokens de CF: dentro de un mismo rango, dos tokens ES distintos no pueden dar el mismo EN
            por_rango = {}
            for cf in hd['cf']:
                for f_ in cf['formula']:
                    for lit in RX_LIT.findall(f_):
                        por_rango.setdefault(cf['sqref'], set()).add(lit)
            for rng, toks in por_rango.items():
                ens = {}
                for t in toks:
                    en = CLAVES.get(t, t)
                    if en in ens and ens[en] != t:
                        err.append('colisión de CF en %s / %s / %s: %r y %r → %r' % (c, h, rng, ens[en], t, en))
                    ens[en] = t
    # cada patrón de FORMULAS_EN tiene que existir en el censo (si el ES cambia, se nota aquí)
    todos = {pat['patron'] for info in censo['libros'].values() for hd in info['hojas_detalle'].values()
             for pat in hd['patrones_formula']}
    primeras = {(info['corto'], h, pat['celdas'].split('..')[0]) for info in censo['libros'].values()
                for h, hd in info['hojas_detalle'].items() for pat in hd['patrones_formula']}
    for es in FORMULAS_EN:
        if es not in todos:
            err.append('patrón de mapas.py que no está en el censo: ' + es[:110])
    for k in PATRONES_SIN_CAMBIO - primeras:
        err.append('PATRONES_SIN_CAMBIO cita un patrón que no está en el censo: %r' % (k,))
    usados = {(c, h) for (c, h, _x) in EJEMPLOS_NUM}
    for (c, h) in usados:
        if not any(info['corto'] == c and h in info['hojas'] for info in censo['libros'].values()):
            err.append('EJEMPLOS_NUM cita una hoja inexistente: %s / %s' % (c, h))
    return err


if __name__ == '__main__':
    e = autotest()
    pc = os.path.join(AQUI, 'censo_es.json')
    if os.path.exists(pc):
        e += cruzar_censo(pc)
    for x in e:
        print('ERROR', x)
    print('mapas.py: {} ficheros · {} pestañas · {} claves · {} patrones de fórmula EN · {} errores'.format(
        len(FICHEROS), len(HOJAS), len(CLAVES), len(FORMULAS_EN), len(e)))
    raise SystemExit(1 if e else 0)
