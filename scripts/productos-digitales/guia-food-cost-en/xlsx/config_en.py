"""Configuración de la capa EN de los 8 xlsx de la guía Food Cost (SPEC §2, D6-D8, DECISIONES-TANDAS).

Conversión EXACTA y sin redondear (D8): las cantidades y los precios por unidad se guardan con todos los
decimales para que todo importe calculado sea idéntico al ES (cantidad_lb × precio_lb = cantidad_kg × precio_kg).
"""
KG_PER_LB = 0.45359237                 # definición legal
LB_PER_KG = 1 / KG_PER_LB              # 2.2046226218…
ML_PER_FLOZ = 29.5735295625            # US fluid ounce
CL_TO_FLOZ = 10 / ML_PER_FLOZ
ML_TO_FLOZ = 1 / ML_PER_FLOZ

# Factores de unidad válidos en el gate (EN/ES de una celda derivada de una magnitud convertida)
FACTORES_UNIDAD = {'lb/kg': LB_PER_KG, 'kg/lb (por lb)': KG_PER_LB, 'ml/cl': 10.0, 'fl oz/cl': CL_TO_FLOZ}

DV_DECIMAL_TASA = {'type': 'decimal', 'operator': 'between', 'formula1': '0', 'formula2': '0.21'}

LIBROS = {
    'ficha-escandallo-base.xlsx': {
        'out': 'recipe-cost-card.xlsx',
        'titulo': 'Recipe Cost Card',
        'hojas': {'Instrucciones': 'Instructions', 'Ficha': 'Cost Card',
                  'Albarán e IVA soportado': 'Invoice & Tax Check'},
        # (hoja ES, rango, operación)
        'num': [
            ('Ficha', 'D10:D13', ('mul', LB_PER_KG)), ('Ficha', 'E10:E13', ('mul', KG_PER_LB)),
            ('Ficha', 'D15', ('mul', LB_PER_KG)), ('Ficha', 'E15', ('mul', KG_PER_LB)),
            ('Ficha', 'D19:D20', ('mul', LB_PER_KG)), ('Ficha', 'E19:E20', ('mul', KG_PER_LB)),
            ('Ficha', 'G10:G20', ('set', 0)),
            ('Ficha', 'E35', ('set', 0)),
            ('Albarán e IVA soportado', 'C11:C12', ('mul', LB_PER_KG)),
            ('Albarán e IVA soportado', 'E11:E12', ('mul', KG_PER_LB)),
            ('Albarán e IVA soportado', 'C14', ('mul', LB_PER_KG)),
            ('Albarán e IVA soportado', 'E14', ('mul', KG_PER_LB)),
            ('Albarán e IVA soportado', 'G11:G17', ('set', 0)),
            ('Albarán e IVA soportado', 'A5', ('set', 1)),
            ('Albarán e IVA soportado', 'A6', ('set', 2)),
            ('Albarán e IVA soportado', 'A7', ('set', 3)),
        ],
        'estilo': [('Albarán e IVA soportado', 'A5:A7', 'A11')],   # la tabla por país numera 1-3 (antes 4/10/21 %)
        'texto': {('Albarán e IVA soportado', 'D17'): 'case',
                  ('Albarán e IVA soportado', 'E10'): 'Unit price pre-tax'},
        'dv': {
            ('Ficha', 'C10'): {'formula1': '"lb,oz,kg,g,L,ml,cl,fl oz,qt,gal,each,dozen,portion"'},
            ('Ficha', 'G10'): DV_DECIMAL_TASA,
            ('Albarán e IVA soportado', 'G11'): DV_DECIMAL_TASA,
            ('Albarán e IVA soportado', 'A5'): None,      # se elimina: A5:A7 ya no son tipos de IVA
        },
        # celdas de tipo de impuesto puestas a 0 (para el gate: ES con estas celdas a 0 = referencia)
        'impuesto0': [('Ficha', 'G10:G20'), ('Ficha', 'E35'), ('Albarán e IVA soportado', 'G11:G17')],
    },
    'rendimiento-mermas-producto.xlsx': {
        'out': 'yield-and-trim-loss.xlsx',
        'titulo': 'Yield, Trim Loss and Net Product Cost',
        'hojas': {'Instrucciones': 'Instructions', 'Test de Rendimiento': 'Yield Test',
                  'Merma de Cocción': 'Cooking Loss Test', 'Mi Tabla de Mermas': 'My Trim Loss Table'},
        'num': [
            ('Test de Rendimiento', 'C6:C15', ('mul', LB_PER_KG)),
            ('Test de Rendimiento', 'E6:F15', ('mul', LB_PER_KG)),
            ('Test de Rendimiento', 'D6:D15', ('mul', KG_PER_LB)),
            ('Test de Rendimiento', 'G6:G15', ('mul', KG_PER_LB)),
            ('Merma de Cocción', 'D6:E10', ('mul', LB_PER_KG)),
            ('Merma de Cocción', 'I6:I10', ('mul', KG_PER_LB)),
        ],
        'impuesto0': [],
    },
    'precio-objetivo-multi-metodo.xlsx': {
        'out': 'menu-pricing-calculator.xlsx',
        'titulo': 'Menu Pricing Calculator',
        'hojas': {'Instrucciones': 'Instructions', 'Por Plato': 'By Dish'},
        'num': [('Por Plato', 'E6', ('set', 0))],
        'impuesto0': [('Por Plato', 'E6')],
    },
    'matriz-multimetodo-carta.xlsx': {
        'out': 'menu-engineering-matrix.xlsx',
        'titulo': 'Multi-Method Menu Engineering Matrix',
        'hojas': {'Instrucciones': 'Instructions', 'Datos': 'Data', 'Kasavana-Smith': 'Kasavana-Smith',
                  'Miller': 'Miller', 'Pavesic': 'Pavesic', 'Goal Value': 'Goal Value',
                  'Comparativa': 'Comparison', 'Menú Precio Fijo': 'Prix Fixe Menu'},
        # El menú del día ES guarda el precio CON IVA (14,50 € al 10 %): el EN guarda el neto exacto
        # (14,50 / 1,10 = 13,18…) con el impuesto a 0 %, así que el neto y todo lo que cuelga de él es idéntico.
        'num': [('Datos', 'D34', ('set', 0)),
                ('Menú Precio Fijo', 'C20', ('set', 0)),
                ('Menú Precio Fijo', 'C19', ('set', 14.5 / 1.1))],
        'impuesto0': [('Datos', 'D34'), ('Menú Precio Fijo', 'C20'), ('Menú Precio Fijo', 'C19', 14.5 / 1.1)],
    },
    'cuadro-de-mando-prime-cost.xlsx': {
        'out': 'prime-cost-dashboard.xlsx',
        'titulo': 'Prime Cost Dashboard',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Inputs', 'Mensual': 'Monthly'},
        'num': [],
        'impuesto0': [],
    },
    'carta-de-bebidas-beverage-cost.xlsx': {
        'out': 'beverage-cost-menu.xlsx',
        'titulo': 'Beverage Menu and Beverage Cost',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Inputs', 'Vinos': 'Wines',
                  'Cervezas y Refrescos': 'Beer & Soft Drinks', 'Destilados y Cócteles': 'Spirits & Cocktails',
                  'Resumen Bodega': 'Beverage Summary'},
        'num': [
            ('Parámetros', 'B6:D8', ('set', 0)),
            ('Vinos', 'E5:F12', ('mul', 10.0)),                         # botella y copa: cl -> ml
            ('Cervezas y Refrescos', 'G5:H10', ('mul', CL_TO_FLOZ)),     # barril, tercio, lata, agua: cl -> fl oz
            ('Cervezas y Refrescos', 'G11', ('mul', KG_PER_LB * ML_TO_FLOZ)),   # ml de zumo por kg -> fl oz por lb
            ('Cervezas y Refrescos', 'H11', ('mul', ML_TO_FLOZ)),               # 250 ml -> 8.45 fl oz
            ('Cervezas y Refrescos', 'F11', ('mul', KG_PER_LB)),                # precio por kg -> por lb
            ('Destilados y Cócteles', 'E5:F9', ('mul', 10.0)),           # botella y servicio: cl -> ml
        ],
        'texto': {('Cervezas y Refrescos', 'B5'): 'Draft beer, 30 L keg (8.45 fl oz pours)',
                  ('Cervezas y Refrescos', 'B6'): 'Draft beer, 30 L keg (16.91 fl oz pours)'},
        'dv': {('Cervezas y Refrescos', 'E5'): {'formula1': '"fl oz,ml,cl,oz,g"'}},
        'impuesto0': [('Parámetros', 'B6:D8')],
    },
    'simulador-repricing-multicanal.xlsx': {
        'out': 'multichannel-repricing-simulator.xlsx',
        'titulo': 'Multichannel Repricing Simulator',
        'hojas': {'Instrucciones': 'Instructions', 'Parámetros': 'Inputs', 'Carta': 'Menu', 'Resumen': 'Summary'},
        'num': [('Parámetros', 'B6:D8', ('set', 0))],
        'impuesto0': [('Parámetros', 'B6:D8')],
    },
    'plan-accion-90-dias.xlsx': {
        'out': '90-day-action-plan.xlsx',
        'titulo': '90-Day Action Plan',
        'hojas': {'Instrucciones': 'Instructions', 'Decisiones': 'Decisions', 'Calendario 90 Días': '90-Day Calendar',
                  'KPI de Seguimiento': 'Tracking KPIs'},
        'num': [],
        'impuesto0': [],
    },
}

# Pies y cabeceras (sustitución literal dentro del texto con los códigos &C&8…)
HF = [('Página &P de &N', 'Page &P of &N')]

# Formatos numéricos (D6, piloto D5): sin símbolo de moneda; fechas US
FORMATOS = {'#,##0.00 €': '#,##0.00', 'dd/mm/yyyy': 'mm/dd/yyyy', 'yyyy-mm-dd': 'mm/dd/yyyy'}

ASUNTO = 'Food Cost + Menu Engineering Guide · Version 1.0 · October 2026'
AUTOR = 'AI Chef Pro'
FECHA_MOD = '2026-10-15T08:00:00Z'
PAPEL_LETTER = '1'
