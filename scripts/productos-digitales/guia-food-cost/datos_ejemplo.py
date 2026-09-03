#!/usr/bin/env python3
"""
datos_ejemplo.py — JUEGO DE DATOS ÚNICO del producto «Guía Food Cost + Ingeniería
de Menú» (SPEC: scripts/productos-digitales/guia-food-cost-SPEC.md, §2.2).

Los 8 libros de Excel, el guion de la guía (`guion_guia_food_cost_ingenieria_menu.py`)
y el caso integral del capítulo 19 usan ESTA carta, ESTA ficha y ESTAS referencias.
Regla de la familia (§7-bis.7 de guias-v2-SPEC.md): una sola fuente de cifras.
Si un número cambia, cambia aquí y se regeneran los libros.

Todo importe va SIN IVA salvo que el nombre diga lo contrario. Las cifras de
referencia del sector llevan su fuente; las que no la tienen NO existen aquí
(lista negra en la SPEC, D10).
"""

# --------------------------------------------------------------------------
# El restaurante modelado (caso MODELADO, no cliente real — SPEC §4 cap. 19)
# --------------------------------------------------------------------------
RESTAURANTE = {
    'nombre': 'Restaurante de ejemplo «La Encina»',
    'formato': 'restaurante de carta, servicio en mesa, 70 plazas, ciudad media española',
    'servicios_mes': 52,          # comidas + cenas abiertas en un mes tipo
    'cubiertos_mes': 3900,        # ≈ 75 cubiertos por servicio
    'food_cost_objetivo': 0.30,   # objetivo de la casa (CaixaBankLab/elBulli: media del sector ~30 %)
    'iva_sala': 0.10,
}

# --------------------------------------------------------------------------
# La carta: 20 platos (nombre, familia, coste/ración sin IVA, PVP sin IVA, uds/mes)
# Los 12 primeros ids (E1-E4, P1-P5, D1-D3) son «los 12 platos de ejemplo» que
# cita el capítulo 19; el resto completa las familias para que la matriz tenga
# masa crítica. El coste de P1 se DERIVA de la ficha (más abajo).
# --------------------------------------------------------------------------
PLATOS = [
    # id, nombre, familia, coste, pvp_sin_iva, uds_mes
    ('E1', 'Croquetas de jamón ibérico (6 ud)',            'Entrantes',   2.10,  8.60, 420),
    ('E2', 'Ensalada de tomate rosa, ventresca y cebolleta', 'Entrantes', 3.60, 11.80, 310),
    ('E3', 'Gambas al ajillo',                              'Entrantes',   6.90, 15.50, 260),
    ('E4', 'Huevos rotos con patatas y chistorra',          'Entrantes',   2.40,  9.80, 380),
    ('E5', 'Tabla de quesos de la zona',                    'Entrantes',   5.20, 13.60,  90),
    ('E6', 'Alcachofas confitadas con jamón',               'Entrantes',   3.10, 10.90, 120),
    ('E7', 'Sopa de tomate asado con albahaca',             'Entrantes',   1.20,  7.20, 150),
    ('P1', 'Solomillo de cerdo ibérico con puré de boniato', 'Principales', None, 17.30, 340),  # coste = ficha
    ('P2', 'Bacalao confitado al pil-pil',                  'Principales', 7.40, 19.10, 190),
    ('P3', 'Hamburguesa de vaca madurada con patatas',      'Principales', 4.30, 13.60, 460),
    ('P4', 'Arroz meloso de secreto ibérico y setas',       'Principales', 6.20, 16.40, 270),
    ('P5', 'Chuletón de vaca madurada (500 g)',             'Principales', 14.80, 32.70, 110),
    ('P6', 'Lubina a la sal',                               'Principales', 8.90, 21.80,  80),
    ('P7', 'Pollo de corral asado con patatas',             'Principales', 3.70, 12.70, 300),
    ('P8', 'Lasaña de verduras de temporada',               'Principales', 2.60, 11.40, 140),
    ('P9', 'Tataki de atún rojo con sésamo',                'Principales', 9.60, 22.40, 130),
    ('D1', 'Tarta de queso cremosa',                        'Postres',     1.30,  5.90, 520),
    ('D2', 'Torrija caramelizada con helado',               'Postres',     1.10,  5.50, 210),
    ('D3', 'Coulant de chocolate',                          'Postres',     1.60,  6.20, 330),
    ('D4', 'Fruta de temporada preparada',                  'Postres',     1.40,  4.50,  60),
]

# --------------------------------------------------------------------------
# La ficha de escandallo del plato P1 (1 ración). Cantidades NETAS por ración,
# precio de compra sin IVA por unidad de compra, merma en tanto por uno.
# cantidad bruta = neta / (1 - merma); coste = bruta × precio.
# --------------------------------------------------------------------------
FICHA = {
    'plato': 'Solomillo de cerdo ibérico con puré de boniato',
    'familia': 'Principales',
    'raciones': 1,
    'food_cost_objetivo': 0.30,
    'pvp_actual_sin_iva': 17.30,
    'lineas': [
        # ingrediente, unidad, cantidad neta/ración, precio/ud sin IVA, merma, iva_compra
        ('Solomillo de cerdo ibérico',        'kg', 0.220, 15.80, 0.12, 0.10),
        ('Panceta ibérica (crujiente)',       'kg', 0.030, 11.50, 0.05, 0.10),
        ('Boniato',                           'kg', 0.180,  1.60, 0.18, 0.04),
        ('Mantequilla',                       'kg', 0.015,  8.90, 0.00, 0.10),
        ('Nata 35 % M.G.',                    'L',  0.030,  3.40, 0.00, 0.10),
        ('Cebolla',                           'kg', 0.040,  0.95, 0.12, 0.04),
        ('Vino Pedro Ximénez (para la salsa)', 'L', 0.030,  9.80, 0.00, 0.21),
        ('Caldo de carne',                    'L',  0.060,  2.20, 0.00, 0.10),
        ('Aceite de oliva virgen extra',      'L',  0.015,  7.20, 0.00, 0.04),
        ('Brotes de rúcula',                  'kg', 0.010, 12.00, 0.10, 0.04),
        ('Sal, pimienta, tomillo y pimentón (prorrateo)', 'kg', 0.010, 6.00, 0.00, 0.10),
    ],
}


def coste_ficha(ficha=FICHA):
    """Coste por ración de la ficha con la convención D/(1-F). Redondeo a céntimos."""
    total = 0.0
    for _, _, neta, precio, merma, _ in ficha['lineas']:
        bruta = neta / (1 - merma)
        total += bruta * precio
    return round(total / ficha['raciones'], 2)


# El coste de P1 en TODOS los libros es el de la ficha (coherencia §7-bis.7).
PLATOS = [(i, n, f, (coste_ficha() if c is None else c), p, u) for i, n, f, c, p, u in PLATOS]
LOS_12 = [p for p in PLATOS if p[0] in ('E1', 'E2', 'E3', 'E4', 'P1', 'P2', 'P3', 'P4', 'P5', 'D1', 'D2', 'D3')]

# --------------------------------------------------------------------------
# Menú de precio fijo (capítulo 14): el margen lo decide el MIX de elecciones.
# Precio del menú 14,50 € con IVA en sala (10 %). Coste por opción sin IVA y
# mix de elección estimado.
# --------------------------------------------------------------------------
MENU_PRECIO_FIJO = {
    'nombre': 'Menú del mediodía',
    'pvp_con_iva': 14.50,
    'iva': 0.10,
    'fijos_por_menu': 0.55,   # pan, agua/copa de vino de la casa, prorrateados
    'cursos': [
        ('Primeros', [('Ensalada de la huerta', 1.10, 0.40), ('Crema de calabaza', 1.05, 0.25), ('Pasta al pesto', 1.60, 0.35)]),
        ('Segundos', [('Pollo asado con patatas', 2.80, 0.45), ('Merluza a la romana', 3.90, 0.30), ('Albóndigas de ternera', 3.20, 0.25)]),
        ('Postres',  [('Flan casero', 0.50, 0.55), ('Fruta del tiempo', 0.70, 0.45)]),
    ],
}

# --------------------------------------------------------------------------
# Test de rendimiento (capítulo 05): 10 productos medidos con báscula.
# peso bruto (kg), precio/kg bruto sin IVA, peso limpio (kg), subproductos
# aprovechables (kg) y su valor de uso (€/kg: lo que costaría comprarlos).
# --------------------------------------------------------------------------
TESTS_RENDIMIENTO = [
    ('Lubina entera (1,2 kg)',           1.20, 14.90, 0.62, 0.30, 2.50),   # espinas y cabeza → fumet
    ('Merluza entera',                   2.40, 11.80, 1.30, 0.55, 2.50),
    ('Solomillo de vacuno (pieza)',      2.10, 26.50, 1.85, 0.12, 6.00),   # recortes → tartar/ragú
    ('Pollo de corral entero',           2.20,  5.40, 1.50, 0.45, 1.80),   # carcasa → caldo
    ('Cordero (paletilla)',              1.60, 13.20, 1.35, 0.00, 0.00),
    ('Tomate rosa',                      5.00,  3.80, 4.40, 0.00, 0.00),
    ('Alcachofa',                        5.00,  2.90, 1.90, 0.00, 0.00),
    ('Boniato',                          5.00,  1.60, 4.10, 0.00, 0.00),
    ('Mejillón (con concha)',            5.00,  2.60, 1.00, 0.00, 0.00),
    ('Gamba blanca (entera)',            2.00, 24.00, 1.05, 0.50, 3.00),   # cabezas y cáscaras → fondo
]

# Pruebas de merma de cocción (peso crudo → peso cocinado), medidas por el usuario.
TESTS_COCCION = [
    ('Solomillo de cerdo a la plancha', 'Plancha', 0.250, 0.195),
    ('Pollo de corral al horno',         'Horno',   1.500, 1.080),
    ('Bacalao confitado',                'Confitado', 0.200, 0.176),
    ('Secreto ibérico a la brasa',       'Brasa',   0.300, 0.222),
    ('Verduras asadas',                  'Horno',   1.000, 0.690),
]

# Rangos de merma de REFERENCIA (orientativos, de uso profesional; L3 §8.1-8.2,
# fiabilidad media; se presentan como «ajusta con tu test», nunca como tabla oficial).
MERMAS_REFERENCIA = [
    # categoría, merma mín, merma máx, nota
    ('Carnes (piezas con hueso/grasa)',   0.15, 0.30, 'Rendimiento 70-85 %'),
    ('Solomillo de vacuno (limpieza)',    0.10, 0.15, ''),
    ('Pescado entero',                    0.45, 0.55, 'Cabeza y espinas aprovechables en fumet'),
    ('Pescado en lomos/filetes',          0.05, 0.12, 'Piel y recortes'),
    ('Verduras de hoja',                  0.10, 0.15, ''),
    ('Verduras y hortalizas (general)',   0.10, 0.25, 'Rendimiento 75-90 %'),
    ('Alcachofa',                         0.55, 0.65, 'Se queda el corazón'),
    ('Mejillones, caracoles, callos',     0.80, 0.85, 'Rendimiento 15-20 %'),
    ('Marisco entero (gamba, cigala)',    0.45, 0.55, 'Cabezas y cáscaras aprovechables en fondo'),
    ('Fruta',                             0.15, 0.30, 'Piel, hueso, corazón'),
    ('Aves enteras',                      0.28, 0.35, 'Carcasa aprovechable en caldo'),
    ('Quesos, embutidos (corteza/piel)',  0.03, 0.08, ''),
]
FUENTE_MERMAS = ('Tabla orientativa de uso profesional (agregado de tablas de mermas de cocina '
                 'profesional y del post «Qué son las mermas en cocina» de aichef.pro/blog). '
                 'No es una tabla oficial: mide la tuya con el test de rendimiento.')

# --------------------------------------------------------------------------
# Fiscalidad (SPEC §3). IVA repercutido por canal y tipo de producto, y tipos de
# IVA soportado en compras. Ley 37/1992 (consolidada, BOE-A-1992-28740).
# --------------------------------------------------------------------------
IVA_REPERCUTIDO = {
    # canal: {tipo de producto: tipo}
    'Sala':      {'Comida': 0.10, 'Refresco/azucarada': 0.10, 'Bebida alcohólica': 0.10},
    'Take away': {'Comida': 0.10, 'Refresco/azucarada': 0.21, 'Bebida alcohólica': 0.21},
    'Delivery':  {'Comida': 0.10, 'Refresco/azucarada': 0.21, 'Bebida alcohólica': 0.21},
}
NOTAS_IVA = {
    'Sala': ('10 % para todo el consumo en el local, alcohol incluido: art. 91.Uno.2.2.º de la Ley '
             'del IVA (servicios de hostelería y suministro de comidas y bebidas para consumir en el acto).'),
    'Take away': ('Sin servicio es entrega de bienes y manda el tipo del producto: comida elaborada 10 % '
                  '(art. 91.Uno.1.1.º); bebidas alcohólicas y refrescos, zumos y gaseosas con azúcares o '
                  'edulcorantes añadidos, 21 % (excluidos del tipo reducido desde el 1-ene-2021).'),
    'Delivery': 'Misma regla que el take away: es entrega de bienes, no servicio de hostelería.',
}
IVA_SOPORTADO = [
    (0.04, 'Pan común, harinas panificables, leche, quesos, huevos, frutas, verduras, hortalizas, '
           'legumbres, tubérculos, cereales y aceites de oliva (art. 91.Dos.1.1.º; el aceite de oliva '
           'desde el 1-ene-2025 por el RDL 4/2024).'),
    (0.10, 'Resto de alimentos y bebidas no alcohólicas sin azúcares añadidos: carnes, pescados, '
           'conservas, aceites de semillas, agua (art. 91.Uno.1.1.º).'),
    (0.21, 'Bebidas alcohólicas; refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos; '
           'y todo lo no alimentario: packaging, menaje, productos de limpieza (art. 90).'),
]
FUENTE_IVA = 'Ley 37/1992 del IVA, texto consolidado: https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740'

# Albarán de ejemplo del capítulo 04 (importes sin IVA y tipo por línea)
ALBARAN_EJEMPLO = [
    ('Solomillo de cerdo ibérico', 12.0, 'kg', 15.80, 0.10),
    ('Tomate rosa',                 20.0, 'kg',  3.80, 0.04),
    ('Aceite de oliva virgen extra', 25.0, 'L',  7.20, 0.04),
    ('Queso curado de oveja',        4.0, 'kg', 18.50, 0.04),
    ('Vino tinto crianza (botella)', 24.0, 'ud',  6.10, 0.21),
    ('Refresco de cola (lata)',      48.0, 'ud',  0.55, 0.21),
    ('Envases para llevar (caja)',    2.0, 'ud', 38.00, 0.21),
]

# --------------------------------------------------------------------------
# Delivery (capítulo 15): órdenes de magnitud 2025-2026, NO tarifario oficial
# (fuente única especializada: qamarero.com, consultado 2026-09-03; las
# plataformas no publican tarifas).
# --------------------------------------------------------------------------
COMISIONES_REFERENCIA = [
    ('Glovo',     '15-35 % + IVA según zona y si la plataforma reparte; cuota mensual aprox. 39 €'),
    ('Uber Eats', '30 % / 25 % / 15-20 % + IVA según plan'),
    ('Just Eat',  '13 % + IVA solo marketing (reparto propio) · 25-35 % + IVA servicio completo · 0,30 €/pedido'),
    ('Deliveroo', '30 % + IVA estándar · 25 % + IVA a partir de 500 pedidos/mes · cuota tecnológica 50 €/mes'),
]
FUENTE_COMISIONES = ('Orden de magnitud de mercado 2025-2026 según qamarero.com (consultado el '
                     '2026-09-03). Las plataformas no publican tarifario: usa el porcentaje de TU contrato.')
PACKAGING_REFERENCIA = (1.35, 2.15)   # €/pedido, misma fuente
SIMULADOR_DEFECTO = {
    'comision_delivery': 0.30,
    'comision_take_away': 0.00,       # pedido por teléfono/web propia
    'packaging_por_pedido': 1.75,
    'platos_por_pedido': 2.5,
    'fc_objetivo_sala': 0.30,
    'fc_objetivo_take_away': 0.30,
    'fc_objetivo_delivery': 0.30,
}
# Precio techo en la app por plato (sin IVA): lo que el mercado local acepta; ejemplo.
PRECIO_TECHO_APP = {
    'E1': 10.50, 'E2': 12.90, 'E3': 17.50, 'E4': 11.50, 'E5': 14.50, 'E6': 12.00, 'E7': 8.20,
    'P1': 19.90, 'P2': 21.50, 'P3': 15.90, 'P4': 18.50, 'P5': 34.90, 'P6': 23.90, 'P7': 14.50,
    'P8': 12.90, 'P9': 24.90, 'D1': 6.90, 'D2': 6.20, 'D3': 6.90, 'D4': 4.90,
}
TIPO_PRODUCTO_PLATO = 'Comida'   # los 20 platos son comida; las bebidas van en su libro

# --------------------------------------------------------------------------
# Bodega (capítulo 16). Compra sin IVA, PVP sin IVA en sala.
# --------------------------------------------------------------------------
VINOS = [
    # nombre, compra botella, formato cl, pvp botella, pvp copa, copas por botella, uds botella/mes, copas/mes
    ('Tinto de la casa (Tempranillo joven)',   3.90, 75, 13.60, 3.00, 5, 120, 780),
    ('Crianza Rioja',                          6.10, 75, 19.10, 4.10, 5,  95, 320),
    ('Ribera del Duero roble',                 7.40, 75, 21.80, 4.50, 5,  70, 210),
    ('Verdejo Rueda',                          4.20, 75, 14.50, 3.20, 5, 110, 640),
    ('Albariño Rías Baixas',                   7.90, 75, 22.70, 4.80, 5,  55, 150),
    ('Cava brut nature',                       5.60, 75, 18.20, 3.90, 5,  40, 180),
    ('Rosado Navarra',                         3.70, 75, 12.70, 2.90, 5,  30, 140),
    ('Vino dulce Pedro Ximénez',              11.50, 50, 27.30, 4.00, 8,  10, 120),
]
CERVEZAS_REFRESCOS = [
    # nombre, formato, compra por unidad de compra, contenido (cl), cl por servicio, pvp servicio, uds/mes
    ('Cerveza de barril (30 L)',  'barril', 78.00, 3000, 25, 2.30, 2900),   # caña
    ('Cerveza de barril (30 L)',  'barril', 78.00, 3000, 50, 4.10,  620),   # jarra/doble
    ('Cerveza tercio (33 cl)',    'botella', 0.62,   33, 33, 2.50,  540),
    ('Cerveza sin alcohol (33 cl)', 'botella', 0.58, 33, 33, 2.40,  180),
    ('Refresco de cola (lata 33 cl)', 'lata', 0.55,  33, 33, 2.30,  760),
    ('Agua mineral (50 cl)',      'botella', 0.28,   50, 50, 1.80, 1100),
    ('Zumo de naranja natural',   'kg naranjas', 1.40, 1000, 250, 3.20, 260),
]
DESTILADOS = [
    # nombre, compra botella 70 cl, cl por copa, coste mezcla (tónica/refresco), pvp combinado, uds/mes
    ('Ginebra premium',        16.90, 5, 0.60, 8.20, 310),
    ('Ron añejo',              14.20, 5, 0.55, 7.50, 140),
    ('Whisky escocés 12 años', 22.40, 5, 0.55, 8.60,  95),
    ('Vodka',                  11.80, 5, 0.55, 7.20,  80),
    ('Vermut de grifo (1 L)',   7.90, 8, 0.10, 3.60, 420),
]
COCTELES = [
    # nombre, [(ingrediente, cantidad cl, precio por litro)], pvp, uds/mes
    ('Gin tonic de la casa', [('Ginebra premium', 5, 24.14), ('Tónica premium', 20, 3.00), ('Lima y botánicos', 1, 12.00)], 8.20, 310),
    ('Mojito',               [('Ron blanco', 5, 17.00), ('Lima', 3, 4.00), ('Azúcar y hierbabuena', 2, 6.00), ('Soda', 10, 1.20)], 7.90, 160),
    ('Aperol spritz',        [('Aperol', 6, 18.50), ('Cava brut', 9, 7.47), ('Soda', 3, 1.20)], 7.50, 210),
    ('Negroni',              [('Ginebra', 3, 24.14), ('Vermut rojo', 3, 7.90), ('Bitter', 3, 18.00)], 8.80, 70),
]
BEVERAGE_COST_REFERENCIA = [
    # categoría, objetivo sembrado, nota con fuente
    ('Vinos',                0.30, 'Media española de bebida 34,5 % sobre ingresos de bebida (CaixaBankLab × elBulliFoundation); objetivo de la casa 30 %'),
    ('Cervezas y refrescos', 0.22, 'Referencia España 15-25 % en bebidas estándar (qamarero.com); barril 20-26 % y botella 24-28 % (referencias EE. UU., purimax.com)'),
    ('Destilados y cócteles', 0.20, 'Referencia EE. UU. 15-22 % (purimax.com); pour cost objetivo del sector 18-24 %'),
]
FUENTE_BEVERAGE = ('CaixaBankLab × elBulliFoundation (https://www.caixabanklab.com/elbullifoundation/es/consumos-beneficios-restaurante/), '
                   'qamarero.com y purimax.com, consultados el 2026-09-03.')

# --------------------------------------------------------------------------
# Prime cost (capítulo 08). Estructura española: producto ~30 % + personal
# 30-35 % con servicio en mesa (15-25 % en barra/autoservicio) → objetivo de
# prime cost 65 % / 55 %. Fuente: CaixaBankLab × elBulliFoundation. El 60 % de
# Toast (EE. UU.) se cita solo como contraste.
# --------------------------------------------------------------------------
PRIME_COST_OBJETIVO = {'Servicio en mesa': 0.65, 'Barra / autoservicio': 0.55}
SS_EMPRESA = 0.33
MESES = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto',
         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
# ventas netas comida, ventas netas bebida, stock inicial, compras, stock final, salarios brutos, otros costes de personal
CUADRO_MENSUAL = [
    (44800, 19200, 6900, 20100, 6700, 15400, 900),
    (42100, 18000, 6700, 19300, 6500, 15400, 850),
    (47600, 20400, 6500, 21900, 6800, 15900, 900),
    (50200, 21500, 6800, 22400, 6600, 16100, 950),
    (53900, 23100, 6600, 24800, 6900, 16600, 1000),
    (55400, 23700, 6900, 26900, 6400, 17300, 1050),
    (58100, 24900, 6400, 27200, 6700, 17800, 1100),
    (49800, 21300, 6700, 24600, 6200, 17800, 1000),
    (52700, 22600, 6200, 23300, 6800, 16400, 950),
    (51300, 22000, 6800, 22700, 6600, 16100, 950),
    (48900, 21000, 6600, 21800, 6900, 15900, 900),
    (61200, 26200, 6900, 27900, 7400, 17600, 1200),
]

# --------------------------------------------------------------------------
# Plan de acción 90 días (capítulo 19 y libro 8): decisiones que SALEN de las
# otras herramientas sobre la carta de ejemplo.
# --------------------------------------------------------------------------
DECISIONES_EJEMPLO = [
    # plato/área, herramienta de origen, decisión, responsable, semana, impacto €/mes estimado
    ('Gambas al ajillo (E3)',           'Matriz multi-método', 'Resubir',    'Gerente',        2,  310.0),
    ('Chuletón de vaca madurada (P5)',  'Matriz multi-método', 'Mantener',   'Jefe de cocina', 1,    0.0),
    ('Tabla de quesos (E5)',            'Matriz multi-método', 'Retirar',    'Gerente',        4,  120.0),
    ('Lasaña de verduras (P8)',         'Matriz multi-método', 'Reformular', 'Jefe de cocina', 3,  180.0),
    ('Fruta de temporada (D4)',         'Matriz multi-método', 'Rediseñar',  'Jefe de cocina', 3,   60.0),
    ('Lubina a la sal (P6) en delivery', 'Simulador multicanal', 'Retirar',  'Gerente',        2,   90.0),
    ('Chuletón (P5) en delivery',       'Simulador multicanal', 'Retirar',   'Gerente',        2,  140.0),
    ('Pescado entero: cambiar a lomos', 'Test de rendimiento', 'Negociar',   'Jefe de compras', 5, 260.0),
    ('Copa de crianza: PVP',            'Carta de bebidas',    'Resubir',    'Jefe de sala',   2,  210.0),
    ('Cuadrante de sala en meses bajos', 'Cuadro de mando prime cost', 'Reformular', 'Gerente', 6, 900.0),
]
KPI_SEGUIMIENTO = {
    # kpi: (mes 0, mes 1, mes 2, mes 3) — ejemplo editable; mes 0 es la foto de salida
    'Food cost (%)':                 (0.331, 0.322, 0.311, 0.298),
    'Prime cost (%)':                (0.668, 0.661, 0.652, 0.638),
    'Ticket medio sin IVA (€)':      (27.40, 27.90, 28.60, 29.10),
    'Margen de contribución por cubierto (€)': (18.10, 18.60, 19.40, 20.20),
    'Platos en carta (n.º)':         (20, 20, 19, 18),
}

# --------------------------------------------------------------------------
# Benchmarks de food cost por formato (capítulo 02/09), SOLO los que tienen fuente.
# --------------------------------------------------------------------------
BENCHMARKS_FOOD_COST = [
    ('Media del sector, España',           '25-35 % (media ~30 %)', 'CaixaBankLab × elBulliFoundation', 'alta'),
    ('Comida / bebida, España',            'comida 28 % · bebida 34,5 % (mix de ingresos 70/30)', 'CaixaBankLab × elBulliFoundation', 'alta'),
    ('Restaurante gastronómico',           '20-25 %', 'qamarero.com', 'media'),
    ('Restaurante tradicional de carta',   '28-32 %', 'qamarero.com', 'media'),
    ('Bar de tapas',                       '28-35 %', 'qamarero.com', 'media'),
    ('Pizzería',                           '25-30 %', 'qamarero.com', 'media'),
    ('Cafetería',                          '20-28 %', 'qamarero.com', 'media'),
    ('Delivery / dark kitchen (packaging dentro)', '28-32 % objetivo; 30-38 % típico', 'foodshot.ai, kitchennmbrs.app (LATAM/EE. UU.)', 'media'),
    ('Pastelería / obrador artesanal',     '28-34 %', 'agregado LATAM (GASDA, Roomlab)', 'media'),
    ('Hotel F&B / buffet',                 '28-40 %', 'cucinovo.com (EE. UU.)', 'media'),
]

if __name__ == '__main__':
    print('coste ficha P1 =', coste_ficha())
    for p in PLATOS:
        i, n, f, c, pvp, u = p
        print(f'{i} {n[:42]:42s} {f:12s} coste {c:6.2f}  pvp {pvp:6.2f}  fc {c/pvp:5.1%}  mc {pvp-c:6.2f}  uds {u}')
