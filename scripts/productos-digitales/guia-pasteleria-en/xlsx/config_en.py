"""Configuración de la capa EN (US) de los 8 xlsx de «How to Open a Pastry Shop» (SPEC §2, D6-D8, D12, D13, D15).

Solo la parte NUMÉRICA y ESTRUCTURAL: pestañas, títulos, entradas numéricas, formatos, pies, validaciones y textos de
celda puntuales que acompañan a un cambio numérico. La traducción de textos va aparte (textos_en/<libro>.json).
Detalle, razones y pendientes: CONFIG-NOTAS.md (al lado).

Reglas:
  - D7: todo tipo de IVA tecleado -> 0; todo «PVP con IVA» tecleado -> el PVP sin IVA del ES con todos los decimales
    (misma expresión que la fórmula ES: valor / (1 + tipo)), así todo lo derivado «sin IVA» queda idéntico.
  - D8: m² -> sq ft (× 10.7639…), €/m² -> $/sq ft (÷), m³/h -> CFM (÷ 1.6990…); gramos y €/kg se quedan.
  - D12: pagas 15 -> 12 y bruto mensual × 15/12 (anual idéntico); SMI -> mínimo federal/Texas anual 7.25 × 2,080.
  - D13: el pico 3 (Mother's Day) pasa del mes 3 al 5.
  - D15: techos de temperatura de la hoja «Egg & TCS Decision» -> 41 °F (FDA Food Code 3-501.16), no la conversión
    exacta de 4 °C / 8 °C.

`impuesto0` = las entradas de la REFERENCIA del gate (ES con estos valores puestos). Además de los impuestos lleva los
ajustes que no son un factor de unidad (sueldos, pagas, SMI, meses, temperaturas, recursos propios): así G3 compara el EN
contra un ES con los mismos supuestos. Las conversiones de unidad NO van aquí: el gate las reconoce por FACTORES_UNIDAD.
"""

# ------------------------------------------------------------------------------------------- constantes exactas
SQFT_PER_M2 = 1 / 0.09290304              # 1 sq ft = 0.09290304 m² (definición) -> 10.763910416709722
M3H_PER_CFM = 0.028316846592 * 60         # 1 ft³ = 0.028316846592 m³ (definición) -> 1.69901079552 m³/h por CFM
SUELDO_15_12 = 15 / 12                    # bruto mensual de 15 pagas -> 12 pagas con el mismo anual (= 1.25)
PAGAS_EN = 12
SMI_ANUAL_EN = 7.25 * 2080                # salario mínimo federal = Texas, jornada completa: 15,080 $/año (D12)
TECHO_TCS_F = 41                          # FDA Food Code 2022, 3-501.16(A)(2): TCS en frío ≤ 41 °F (D15)
MES_PICO3_EN = 5                          # D13: Mother's Day / Día de las Madres en mayo
RECURSOS_PROPIOS_EN = 167915.61           # D7: necesidad de caja EN (227,915.60182…, sin IVA adelantado) − préstamo
                                          # 60,000, redondeado al céntimo hacia arriba como el ES (201,826.48)

# Texto EN de las opciones de las listas que se fijan junto con un cambio numérico. DEBEN coincidir con la traducción
# que dé textos_en/<libro>.json a la misma cadena ES (si no, la celda queda fuera de su desplegable).
EN_NO = 'No'                              # ES «No» (listas ¿Lleva IVA? / ¿El precio lleva IVA?)
EN_SIN_IVA = 'pre-tax'                    # ES «sin IVA» (lista «Base del precio», Equipamiento!E61)

# Factores de unidad válidos en el gate (EN/ES de una celda derivada de una magnitud convertida)
FACTORES_UNIDAD = {
    'sq ft/m²': SQFT_PER_M2,
    'por sq ft (÷ sq ft/m²)': 1 / SQFT_PER_M2,
    'CFM/(m³/h)': 1 / M3H_PER_CFM,
    'ft/m': 3.280839895013123,
    'cu ft/m³': 35.31466672148859,
    'por cu ft': 1 / 35.31466672148859,
}


def neto(v, tipo):
    """PVP sin IVA con la misma expresión que la fórmula ES (L/(1+M)): bit a bit igual que el valor ES."""
    return v / (1 + tipo)


def _celdas(hoja, valores, fn):
    """[(hoja, celda, ('set', fn(v)))] y [(hoja, celda, fn(v))] desde {celda: valor ES}."""
    num = [(hoja, ref, ('set', fn(v))) for ref, v in valores.items()]
    ref0 = [(hoja, ref, fn(v)) for ref, v in valores.items()]
    return num, ref0


def _sueldos(hoja, valores):
    """Bruto mensual × 15/12: op 'mul' (como pide D12) y valor explícito para la referencia del gate."""
    num = [(hoja, ref, ('mul', SUELDO_15_12)) for ref in valores]
    ref0 = [(hoja, ref, v * SUELDO_15_12) for ref, v in valores.items()]
    return num, ref0


# ------------------------------------------------------------------------------------------- valores ES de partida
# (verificados contra los xlsx ES por el dry-check; si el ES cambia, el dry-check falla)
PVP_CARTA = {  # 'Coste Hora y Mano de Obra'!L (PVP con IVA) y M (tipo): 26 al 10 %, panes PA1-PA4 al 4 %
    6: (1.6, 0.1), 7: (1.85, 0.1), 8: (1.85, 0.1), 9: (1.7, 0.1), 10: (1.85, 0.1), 11: (1.95, 0.1),
    12: (3.6, 0.1), 13: (3.2, 0.1), 14: (2.1, 0.1), 15: (3.8, 0.1), 16: (2.3, 0.1), 17: (4.5, 0.1),
    18: (3.6, 0.1), 19: (3.4, 0.1), 20: (3.2, 0.1), 21: (3.3, 0.1), 22: (3.8, 0.1), 23: (3.5, 0.1),
    24: (1.2, 0.04), 25: (1.6, 0.04), 26: (3.9, 0.04), 27: (3.2, 0.04),
    28: (16.5, 0.1), 29: (2.4, 0.1), 30: (1.6, 0.1), 31: (1.9, 0.1), 32: (1.85, 0.1), 33: (1.2, 0.1),
    34: (10.5, 0.1), 35: (13.5, 0.1)}
PVP_PICOS = {6: (16.5, 0.1), 7: (2.1, 0.1), 8: (3.6, 0.1), 9: (2.4, 0.1), 10: (3.5, 0.1), 11: (1.6, 0.1)}
IVA_PLAN = 0.201276 * 0.04 + (1 - 0.201276) * 0.1   # '0. Supuestos'!B20 = B19·B16 + (1−B19)·B15 (0.08792344)
TABLA_6_GRUPOS = (1733.88, 1427.89, 1376.91, 1249.42, 1192.42, 1192.42)

# CAPEX: UNOX y SMEG con «¿El precio lleva IVA?» = Sí (precio de ficha CON IVA al 21 %)
_capex_unox, _capex_unox0 = _celdas('CAPEX por Bloque', {'H7': 3354.12, 'I7': 3354.12, 'J7': 3354.12,
                                                         'H8': 2513.41, 'I8': 2513.41, 'J8': 2513.41},
                                    lambda v: neto(v, 0.21))
# «Variante del Formato» K:L = horquilla publicada. PENDIENTES-XLSX (T01): rangos US de Zenind 2026 en las tres filas que
# los tienen (fila 15 caso base = small retail, 16 casera = home-based, 17 obrador a puerta cerrada = production). Las
# filas 18-22 deberían quedar VACÍAS y aplicar_en.py no sabe vaciar una celda (ver CONFIG-NOTAS §5).
RANGOS_US = {'K15': 50000, 'L15': 100000, 'K16': 15000, 'L16': 25000, 'K17': 75000, 'L17': 150000}
_fmt_us = [('Variante del Formato', ref, ('set', v)) for ref, v in RANGOS_US.items()]
_fmt_us0 = [('Variante del Formato', ref, v) for ref, v in RANGOS_US.items()]
# Filas 18-22 sin horquilla US publicada (T01): se VACÍAN (op 'vaciar' de aplicar_en.py; la referencia del gate también)
_fmt_us += [('Variante del Formato', 'K18:L22', ('vaciar', None))]
_fmt_us0 += [('Variante del Formato', 'K18:L22', None)]
# «Traspaso vs Obra Nueva» filas 27-40: 14 traspasos reales de España → filas VACÍAS para los anuncios de tu zona (T04;
# FILAS_LIBRES de split_md.py). La fila 26 (el traspaso del caso) se queda.
_traspasos = [('Traspaso vs Obra Nueva', 'A27:E40', ('vaciar', None)), ('Traspaso vs Obra Nueva', 'H27:H40', ('vaciar', None))]
_traspasos0 = [('Traspaso vs Obra Nueva', 'C27:E40', None)]
_eq_unox, _eq_unox0 =_celdas('Equipamiento', {'I16': 3354.12, 'I17': 2513.41}, lambda v: neto(v, 0.21))
_carta_pvp =[('Coste Hora y Mano de Obra', 'L%d' % r, ('set', neto(v, t))) for r, (v, t) in PVP_CARTA.items()]
_carta_pvp0 = [('Coste Hora y Mano de Obra', 'L%d' % r, neto(v, t)) for r, (v, t) in PVP_CARTA.items()]
_picos_pvp = [('Calendario de 6 Picos', 'H%d' % r, ('set', neto(v, t))) for r, (v, t) in PVP_PICOS.items()]
_picos_pvp0 = [('Calendario de 6 Picos', 'H%d' % r, neto(v, t)) for r, (v, t) in PVP_PICOS.items()]
_carta_sueldo, _carta_sueldo0 = _sueldos('Parámetros', {'D6': 1427.89, 'D7': 1376.91, 'D8': 1192.42})
_picos_sueldo, _picos_sueldo0 = _sueldos('Parámetros', {'B17': 1192.42})
_turnos_sueldo, _turnos_sueldo0 = _sueldos('Parámetros', {'C%d' % (8 + i): v for i, v in enumerate(TABLA_6_GRUPOS)})
_plan_sueldo, _plan_sueldo0 = _sueldos('Personal', {'E%d' % (15 + i): v for i, v in enumerate(TABLA_6_GRUPOS)})


def _r0(lista):
    """(hoja, celda, valor) -> entrada de impuesto0 (hoja, rango, valor)."""
    return [(h, ref, v) for h, ref, v in lista]


LIBROS = {
    # ===================================================================================================== CAPEX
    'calculadora-capex-pasteleria.xlsx': {
        'out': 'startup-cost-calculator.xlsx',
        'titulo': 'Startup Cost Calculator (CAPEX)',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Settings',
                  'CAPEX por Bloque': 'Startup Costs by Block', 'Variante del Formato': 'Format Variant',
                  'Traspaso vs Obra Nueva': 'Takeover vs New Build', 'IVA y Tesorería': 'VAT-GST & Cash',
                  'Resumen': 'Summary'},
        'num': [
            ('Parámetros', 'B6', ('mul', SQFT_PER_M2)),            # 90 m² -> 968.75 sq ft (D8)
            ('Parámetros', 'B7:B9', ('mul', 1 / SQFT_PER_M2)),     # 600/900/1,200 €/m² -> $/sq ft (D8)
            ('Parámetros', 'B13:B15', ('set', 0)),                 # IVA general 21 % · pastelería 10 % · tasas 0 % (D7)
            ('Traspaso vs Obra Nueva', 'C26:C30', ('mul', SQFT_PER_M2)),   # m² de los 5 traspasos con superficie (D8)
        ] + _capex_unox + _fmt_us + _traspasos,                                 # UNOX/SMEG con IVA -> ÷ 1.21 (D7) · rangos US (T01)
        'texto': {('CAPEX por Bloque', 'F7'): EN_NO, ('CAPEX por Bloque', 'F8'): EN_NO},   # «¿Lleva IVA?» Sí -> No
        'dv': {},
        'impuesto0': [('Parámetros', 'B13:B15')] + _r0(_capex_unox0) + _r0(_fmt_us0) + _r0(_traspasos0),
    },
    # ===================================================================================================== capacidad
    'capacidad-obrador-y-local.xlsx': {
        'out': 'kitchen-capacity-and-site.xlsx',
        'titulo': 'Production Kitchen Capacity and Site Visit Checklist',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Settings', 'Zonas y m2': 'Zones and Square Feet',
                  'Capacidad por Equipo': 'Capacity by Equipment', 'Cuello de Botella': 'Bottleneck',
                  'Ficha de Visita a Local': 'Site Visit Checklist'},
        'num': [
            ('Parámetros', 'B14', ('mul', SQFT_PER_M2)),               # superficie del local 90 m² (D8)
            ('Parámetros', 'B19:B20', ('mul', 1 / M3H_PER_CFM)),       # 40/50 m³/h por kW -> CFM por kW (D8)
            ('Zonas y m2', 'D6:D12', ('mul', SQFT_PER_M2)),            # 7 zonas, 90 m² (D8)
            ('Capacidad por Equipo', 'E14', ('mul', SQFT_PER_M2)),     # vitrina 0,93 m² de exposición (D8)
            ('Capacidad por Equipo', 'G14', ('mul', 1 / SQFT_PER_M2)),  # 130 piezas por m² -> por sq ft (D8)
            ('Ficha de Visita a Local', 'F8', ('mul', 1 / M3H_PER_CFM)),   # caudal medido 1,400 m³/h (D8)
            ('Ficha de Visita a Local', 'F13', ('mul', SQFT_PER_M2)),      # superficie útil medida 92 m² (D8)
            ('Parámetros', 'B22', ('mul', 3.280839895013123)),         # altura libre mínima 3 m -> ft (D8 ampliado)
            ('Ficha de Visita a Local', 'F12', ('mul', 3.280839895013123)),  # altura medida 3,2 m -> ft
            ('Capacidad por Equipo', 'E13', ('mul', 35.31466672148859)),      # cámara 8 m³ -> cu ft
            ('Capacidad por Equipo', 'G13', ('mul', 1 / 35.31466672148859)),  # piezas por m³ -> por cu ft
        ],
        'dv': {},
        'impuesto0': [],
    },
    # ===================================================================================================== carta
    'carta-de-apertura-y-escandallo.xlsx': {
        'out': 'opening-menu-and-recipe-costing.xlsx',
        'titulo': 'Opening Menu and Batch Recipe Costing',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Settings', 'Escandallo por Tanda': 'Batch Costing',
                  'Coste Hora y Mano de Obra': 'Labor Cost per Hour',
                  'Decisión de Huevo y Temperatura': 'Egg & TCS Decision',
                  'Mix y Ticket Medio': 'Mix and Average Ticket', 'Decisión de Surtido': 'Menu Decision'},
        'num': [
            ('Parámetros', 'B11', ('set', PAGAS_EN)),                  # pagas 15 -> 12 (D12)
            ('Parámetros', 'B19:B21', ('set', 0)),                     # IVA 10 % / pan 4 % / degustación 10 % (D7)
            ('Parámetros', 'B28:B29', ('set', TECHO_TCS_F)),           # techos 4 °C y 8 °C -> 41 °F Food Code (D15)
            ('Coste Hora y Mano de Obra', 'M6:M35', ('set', 0)),       # IVA por referencia (D7)
        ] + _carta_sueldo + _carta_pvp,                                # brutos × 15/12 (D12) · PVP con IVA -> neto (D7)
        'dv': {},
        'impuesto0': [('Parámetros', 'B19:B21'), ('Coste Hora y Mano de Obra', 'M6:M35'),
                      ('Parámetros', 'B11', PAGAS_EN), ('Parámetros', 'B28:B29', TECHO_TCS_F)]
                     + _r0(_carta_sueldo0) + _r0(_carta_pvp0),
    },
    # ===================================================================================================== equipamiento
    'checklist-equipamiento-y-proveedores.xlsx': {
        'out': 'equipment-and-suppliers-checklist.xlsx',
        'titulo': 'Equipment and Suppliers Checklist',
        'hojas': {'Instrucciones': 'Instructions', 'Equipamiento': 'Equipment', 'Variante del Formato': 'Format Variant',
                  'Proveedores': 'Suppliers', 'Contador': 'Counter'},
        'num': [('Equipamiento', 'C7', ('set', 0)), ('Equipamiento', 'D24:E24', ('vaciar', None))] + _eq_unox,   # horno de pisos: marca y modelo ES fuera (T05)       # IVA general 21 % (D7) · UNOX/SMEG ÷ 1.21
        'texto': {('Equipamiento', 'J16'): EN_SIN_IVA, ('Equipamiento', 'J17'): EN_SIN_IVA,
                  ('Equipamiento', 'J22'): EN_SIN_IVA},   # batidora «no declarada» -> pre-tax (NUM, textos X2)   # «con IVA» -> pre-tax
        'dv': {},
        'impuesto0': [('Equipamiento', 'C7')] + _r0(_eq_unox0),
    },
    # ===================================================================================================== licencias
    'checklist-legal-y-licencias.xlsx': {
        'out': 'permits-and-licenses-checklist.xlsx',
        'titulo': 'Permits, Licenses and Opening Timeline Checklist',
        'hojas': {'Instrucciones': 'Instructions', 'Checklist Legal (F1-F6)': 'Permits Checklist (P1-P6)',
                  'Árbol de Registro Sanitario': 'Which Permit Do I Need',
                  'Suministro a Otros Minoristas': 'Selling Wholesale', 'Ruta Doméstica': 'Cottage Food Route',
                  'Registro de Formación': 'Training Log', 'Cronograma y Ruta Crítica': 'Timeline and Critical Path'},
        'num': [
            ('Ruta Doméstica', 'B6', ('mul', SQFT_PER_M2)),            # 12 m² útiles (D8)
            ('Ruta Doméstica', 'B15', ('mul', 1 / SQFT_PER_M2)),       # 8 kg por m² y semana -> por sq ft (D8)
            ('Cronograma y Ruta Crítica', 'C49', ('set', MES_PICO3_EN)),   # mes del pico 3: 3 -> 5 (D13; lo lee C42)
        ],
        'dv': {},
        'impuesto0': [('Cronograma y Ruta Crítica', 'C49', MES_PICO3_EN)],
    },
    # ===================================================================================================== picos
    'estacionalidad-y-picos.xlsx': {
        'out': 'seasonal-peaks-planner.xlsx',
        'titulo': 'Seasonality and Holiday Peaks Planner',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Settings', 'Calendario de 6 Picos': '6-Peak Calendar',
                  'Peso sobre el Año': 'Share of the Year', 'Capacidad vs Demanda del Pico': 'Peak Capacity vs Demand',
                  'Refuerzo y Tesorería': 'Extra Staff and Cash'},
        'num': [
            ('Parámetros', 'B18', ('set', PAGAS_EN)),                  # pagas 15 -> 12 (D12)
            ('Parámetros', 'B25:B26', ('set', 0)),                     # IVA 10 % / pan 4 % (D7)
            ('Calendario de 6 Picos', 'G6:G11', ('set', 0)),           # IVA de cada campaña (D7)
            ('Calendario de 6 Picos', 'D8', ('set', MES_PICO3_EN)),    # mes del pico 3: 3 -> 5 (D13; no lo lee nadie)
        ] + _picos_sueldo + _picos_pvp,                                # bruto grupo 5 × 15/12 · PVP con IVA -> neto
        'dv': {},
        'impuesto0': [('Parámetros', 'B25:B26'), ('Calendario de 6 Picos', 'G6:G11'),
                      ('Parámetros', 'B18', PAGAS_EN), ('Calendario de 6 Picos', 'D8', MES_PICO3_EN)]
                     + _r0(_picos_sueldo0) + _r0(_picos_pvp0),
    },
    # ===================================================================================================== plan financiero
    'plan-financiero-3-anos-pasteleria.xlsx': {
        'out': '3-year-financial-plan.xlsx',
        'titulo': '3-Year Financial Plan',
        'hojas': {'Instrucciones': 'Instructions', '0. Supuestos': '0. Assumptions',
                  'Inversión Inicial': 'Startup Investment', 'PyG 3 Años': '3-Year P&L',
                  'Punto de Equilibrio': 'Break-Even', 'Escenarios': 'Scenarios', 'Personal': 'Staff',
                  'Tesorería 12 meses': '12-Month Cash Flow', 'Financiación': 'Financing',
                  'Canales y Punto Muerto': 'Channels and Break-Even'},
        'num': [
            ('0. Supuestos', 'B8', ('set', neto(2.4557, IVA_PLAN))),   # PVP medio CON IVA -> neto con el IVA medio (D7)
            ('0. Supuestos', 'B15:B18', ('set', 0)),                   # IVA 10 % / pan 4 % / general 21 % / compras 10 %
            ('0. Supuestos', 'B26', ('set', PAGAS_EN)),                # pagas 15 -> 12 (D12)
            ('0. Supuestos', 'B27', ('set', SMI_ANUAL_EN)),            # SMI 17,094 €/año -> 15,080 $/año (D12)
            ('0. Supuestos', 'B36', ('set', RECURSOS_PROPIOS_EN)),     # recursos propios = necesidad − préstamo (D7)
            ('0. Supuestos', 'B54:B56', ('set', 0)),                   # meses de paga extra 7/12/3 -> ninguno (D12)
            ('Inversión Inicial', 'E6:E16', ('set', 0)),               # tipo de IVA de cada línea (D7)
            ('PyG 3 Años', 'F23:F30', ('set', 0)),                     # tipo de IVA de los fijos tecleados (D7)
        ] + _plan_sueldo,                                              # tabla de 6 sueldos × 15/12 (D12)
        # «¿Lleva IVA?» Sí -> No: con el tipo a 0 la comprobación B23 (Sí con tipo 0) saldría en rojo
        'texto': {('Inversión Inicial', 'D%d' % r): EN_NO for r in (6, 7, 8, 9, 10, 14, 15)},
        'dv': {},
        'impuesto0': [('0. Supuestos', 'B15:B18'), ('Inversión Inicial', 'E6:E16'), ('PyG 3 Años', 'F23:F30'),
                      ('0. Supuestos', 'B8', neto(2.4557, IVA_PLAN)),
                      ('0. Supuestos', 'B26', PAGAS_EN), ('0. Supuestos', 'B27', SMI_ANUAL_EN),
                      ('0. Supuestos', 'B36', RECURSOS_PROPIOS_EN), ('0. Supuestos', 'B54:B56', 0)]
                     + _r0(_plan_sueldo0),
    },
    # ===================================================================================================== plantilla
    'plantilla-turnos-y-coste-personal.xlsx': {
        'out': 'staff-schedule-and-labor-cost.xlsx',
        'titulo': 'Staffing, Schedules and Labor Cost',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Settings', 'Turnos Semanales': 'Weekly Schedule',
                  'Horas y Coste': 'Hours and Cost', 'Plan de Contratación': 'Hiring Plan'},
        'num': [
            ('Parámetros', 'C15', ('set', PAGAS_EN)),                  # pagas 15 -> 12 (D12)
            ('Parámetros', 'C17', ('set', SMI_ANUAL_EN)),              # SMI anual 17,094 -> 15,080 (D12)
            ('Plan de Contratación', 'D18', ('set', MES_PICO3_EN)),    # mes del pico 3: 3 -> 5 (D13; no lo lee nadie)
        ] + _turnos_sueldo,                                            # tabla de 6 sueldos × 15/12 (D12)
        'dv': {},
        'impuesto0': [('Parámetros', 'C15', PAGAS_EN), ('Parámetros', 'C17', SMI_ANUAL_EN),
                      ('Plan de Contratación', 'D18', MES_PICO3_EN)] + _r0(_turnos_sueldo0),
    },
}

# Pies y cabeceras (sustitución literal dentro del texto con los códigos &C&8…): el único patrón de los 53 pies ES es
# «&C&8 AI Chef Pro · aichef.pro · Página &P de &N»; no hay cabeceras.
HF = [('Página &P de &N', 'Page &P of &N')]

# Formatos numéricos presentes en los styles.xml ES: sin símbolo de moneda (D6); fechas US.
# Sin cambio: '#,##0.0', '#,##0.000', '0.0%', '0.0000%', '[=999]"";0.0' (centinela del cronograma).
FORMATOS = {'#,##0.00 €': '#,##0.00', 'dd/mm/yyyy': 'mm/dd/yyyy', 'yyyy-mm-dd': 'mm/dd/yyyy'}

ASUNTO = 'How to Open a Pastry Shop · Version 1.0 · October 2026'
AUTOR = 'AI Chef Pro'
FECHA_MOD = '2026-10-17T08:00:00Z'
PAPEL_LETTER = '1'
