#!/usr/bin/env python3
"""
guion_guia_restaurante_gastronomico.py — GUION del representante de la familia
«Guías Cómo Montar» v2.0 (§5.2 y §5.4 de `guias-v2-SPEC.md`).

Un capítulo no se le pide a `bridge.py` con un título: se le pide con un guion
CERRADO. Por capítulo van (a) el objetivo, (b) 4-6 epígrafes con lo que debe
contener, (c) las **cifras del propio producto** citadas por
`fichero.xlsx!Hoja!Celda` —que `documentos.py` resuelve con openpyxl
`data_only` antes de escribir el prompt, así que el modelo recibe el NÚMERO, no
el fichero—, (d) los **datos del sector** por `id` de
`auditorias/guias-v2-research-sector.json` (§7-bis.21: la cifra sin fuente NO
entra), (e) las tablas exigidas —que las construye el maquetador desde el
xlsx, no el modelo—, (f) el presupuesto de palabras (§5.1) y (g) lo que NO
debe decir (§5.4).

FUENTE ÚNICA DE CIFRAS (§7-bis.7): inversión, coste de personal, fondo de
maniobra y headcount salen de `plan-financiero-3-anos.xlsx` (con el personal
desde `plantilla-turnos-brigada.xlsx`). Los 18 xlsx de
`astro-site/public/dl/guia-restaurante-gastronomico/` se LEEN; no se tocan.

Presupuesto (§5.1): 22 capítulos, 80+ páginas prometidas, ~37.000 palabras
objetivo, 1.600-1.750 palabras por capítulo (los cinco que el R1 señala como
más delgados —9, 13, 14, 19 y 21— llevan más). Calibración medida el
2026-08-29 con la maqueta real: 37.295 palabras + 33 tablas = 73 páginas sin
saltos y **90 con PageBreak por capítulo**, portada e índice.
"""

PID = 'guia-restaurante-gastronomico'

# --------------------------------------------------------------------------
# Cabecera del documento
# --------------------------------------------------------------------------
BIO = (
    'John Guerrero es CEO de AI Chef Pro y fundador de ChefBusiness Group. En '
    'cocina desde los 17 años y consultor gastronómico desde 2010, ha asesorado '
    'la apertura de más de 200 establecimientos, incluidos restaurantes con '
    'Estrella MICHELIN y Soles Repsol en España y Europa. Más sobre su trabajo '
    'en johnguerrero.es.')

LEGAL = (
    '*Esta guía es un documento de trabajo profesional, no un dictamen jurídico, '
    'fiscal ni laboral. Las cifras de inversión, costes y resultados son valores '
    'de ejemplo tomados de las plantillas Excel que acompañan a este pack y '
    'sirven para que las sustituyas por las tuyas: ninguna es una previsión de '
    'tus resultados. La nomenclatura de licencias y buena parte de los plazos '
    'son autonómicos y municipales, y el convenio provincial de hostelería '
    'prevalece sobre los mínimos estatales cuando fija condiciones superiores. '
    'Antes de firmar un arrendamiento, un contrato de trabajo o un préstamo, '
    'contrasta con tu asesoría, con tu ayuntamiento y con la autoridad sanitaria '
    'de tu comunidad autónoma.*')

GUIA = {
    'pid': PID,
    'titulo': 'Cómo Montar un Restaurante Gastronómico',
    'subtitulo': '65 plazas · Guía completa España 2026 · MICHELIN y Soles Repsol',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Cómo Montar un Restaurante Gastronomico',
    'fecha': 'agosto de 2026',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        '22 capítulos, 18 plantillas y checklists en Excel y dos documentos de '
        'trabajo en Word para abrir un restaurante gastronómico de 65 plazas en '
        'España. Todas las cifras de esta guía salen de las plantillas que '
        'vienen en el mismo pack: el texto y las hojas de cálculo dicen lo '
        'mismo, y cuando cambies un dato en el Excel, la lógica que explica '
        'este documento sigue siendo la tuya.'),
    'gates': {
        'paginas_prometidas': 80,
        'palabras_objetivo': 37000,
        'min_palabras_cap': 900,
        # Derivadas por aritmética de celdas del propio libro, documentadas:
        #  · 734.020,40 € = C27 (1.668.340,88) - C26 (934.320,48) → CAPEX sin
        #    el fondo de maniobra, que es como se presenta en el capítulo 4.
        #  · 1.155.923,84 € = calculadora-capex!F18 (total de la columna verde).
        'cifras_extra': ('734.020,40', '734.020', '1.155.923,84'),
        'cifras_ignorar': (),
        # Única formulación de mortalidad admitida: la del INE, con fuente.
        'mortalidad_permitida': ['41,9', '41.9', 'INE', '11.183'],
    },
}

X_PLAN = 'plan-financiero-3-anos.xlsx'
X_TURNOS = 'plantilla-turnos-brigada.xlsx'
X_CASH = 'cash-flow-break-even.xlsx'
X_PL = 'pl-mensual-escenarios.xlsx'
X_TICKET = 'calculadora-ticket-medio.xlsx'
X_CAPEX = 'calculadora-capex.xlsx'
X_ESC = 'escandallo-maestro.xlsx'
X_MENU = 'menu-engineering-matrix.xlsx'
X_BODEGA = 'budget-bodega.xlsx'
X_GANTT = 'cronograma-apertura-gantt.xlsx'
CK_LEGAL = 'checklist-legal.xlsx'
CK_APPCC = 'checklist-appcc.xlsx'
CK_EQUIP = 'checklist-equipamiento-cocina.xlsx'
CK_SALA = 'checklist-diseno-sala.xlsx'
CK_VAJ = 'checklist-vajilla-cristaleria.xlsx'
CK_MKT = 'checklist-marketing-preapertura.xlsx'
CK_CONTRA = 'checklist-contratacion.xlsx'
CK_INSP = 'checklist-inspeccion-michelin-repsol.xlsx'

# Prohibiciones transversales (§5.4): van en TODOS los capítulos.
NO_COMUN = [
    'No escribas ninguna cifra de inversión distinta de las que te doy: en la '
    'edición anterior convivían «500.000-900.000 €» en el texto con otras tres '
    'cifras en las plantillas, y eso es un defecto, no un matiz.',
    'No digas que un porcentaje de restaurantes cierra, fracasa o no sobrevive '
    'salvo que te haya dado esa cifra con su fuente.',
    'No cites años anteriores a 2026 junto a precios ni a tendencias.',
    'No escribas «IVA incluido» sin decir el tipo: en restauración es el 10 % y '
    'en bebida alcohólica el 21 %.',
]


def C(etiqueta, ref, fmt='eur2'):
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Los 22 capítulos
# --------------------------------------------------------------------------
CAPITULOS = [
    {
        'n': 1, 'titulo': 'Qué es un Restaurante Gastronómico',
        'resumen_indice': 'definición, categorías y en qué se diferencia de la restauración convencional.',
        'palabras': 1550, 'bloques': 2,
        'objetivo': 'Dejar claro qué compra el lector cuando decide abrir un '
                    'gastronómico y no otra cosa: una estructura de costes '
                    'distinta, un ritmo de servicio distinto y una plantilla '
                    'que no se parece a la de un restaurante de menú.',
        'epigrafes': [
            'Qué hace diferente al fine dining',
            'Las cuatro categorías: fine dining, casual fine, menú degustación y barra de autor',
            'Lo que cambia en la cuenta de resultados cuando subes de categoría',
            'Perfil del promotor: qué hace falta antes de firmar nada',
        ],
        'puntos': [
            'Explicar el ratio de personal por comensal como el rasgo que define '
            'la categoría: 24 personas para 65 plazas y 70 cubiertos al día.',
            'Explicar que el food cost bajo no significa margen alto: el peso lo '
            'lleva el personal, no la materia prima.',
            'Advertir de que la categoría se decide en el proyecto, no después: '
            'la cocina, los aseos y la instalación eléctrica se dimensionan una vez.',
        ],
        'cifras': [
            C('Facturación mensual del escenario realista', f'{X_PL}!Escenarios!C17'),
            C('Ticket medio ponderado realista', f'{X_TICKET}!Ticket Medio!C16'),
            C('Ticket medio que ve el comensal, con IVA', f'{X_TICKET}!Ticket Medio!C24'),
            C('Cubiertos al día del escenario realista', f'{X_TICKET}!Ticket Medio!C17', 'num'),
            C('Personas en el cuadrante de la brigada', f'{X_TURNOS}!Turnos Semana!A30', 'num'),
            C('Coste anual de la brigada con Seguridad Social', f'{X_TURNOS}!Turnos Semana!O33'),
            C('Coste de materia prima sobre ventas (escenario realista)', f'{X_PL}!Escenarios!C11', 'pct0'),
            C('EBITDA mensual del escenario realista', f'{X_PL}!Escenarios!C21'),
        ],
        'sector': ['SECT-01', 'SECT-02', 'SECT-03', 'TICK-01'],
        'tablas': [{
            'titulo': 'Los tres escenarios del pack, comparados (pl-mensual-escenarios.xlsx, hoja «Escenarios»)',
            'src': (X_PL, 'Escenarios'),
            'cols': [('Concepto', 'A', 'txt'), ('Pesimista', 'B', 'eur2'),
                     ('Realista', 'C', 'eur2'), ('Optimista', 'D', 'eur2')],
            'filas': (17, 24),
            'nota': 'Los tres escenarios están calculados sobre los mismos cubiertos y los '
                    'mismos días de apertura; lo que cambia es el ticket, el food cost y el '
                    'coste de personal. Las filas de cubiertos y ticket están en las filas 6 a 10 '
                    'del mismo libro.',
        }],
        'prohibido': NO_COMUN + [
            'No definas el fine dining por los manteles ni por la decoración: se '
            'define por el producto, la técnica y el número de manos por plato.',
        ],
    },
    {
        'n': 2, 'titulo': 'El Mercado de la Alta Cocina en España 2026',
        'resumen_indice': 'tamaño del sector, turismo gastronómico y dónde está la demanda, con fuente por dato.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Dar al lector el tamaño real del mercado con datos citables '
                    'y fechados, y desmontar la idea de que el reconocimiento '
                    'llega solo por cocinar bien.',
        'epigrafes': [
            'El tamaño del sector y qué parte es restauración de mantel',
            'El turismo gastronómico: cuánto gasta y qué parte viene por la comida',
            'Cuántos restaurantes distinguidos hay en España y qué significa esa cifra',
            'Supervivencia empresarial: lo que dicen los datos y lo que no dicen',
            'Dónde está la demanda: ciudades, temporada y mercado local frente a visitante',
        ],
        'puntos': [
            'Cada cifra de este capítulo va con su fuente y su año entre paréntesis '
            'dentro del propio párrafo.',
            'Explicar la diferencia entre turistas que hacen actividades '
            'enogastronómicas y turistas cuyo motivo principal es la gastronomía: '
            'son dos órdenes de magnitud distintos y confundirlos infla el mercado.',
            'Con el dato de supervivencia del INE, explicar que es de TODOS los '
            'sectores y que no es una tasa de fracaso de restaurantes.',
        ],
        'cifras': [
            C('Ticket medio del pack, con IVA', f'{X_TICKET}!Ticket Medio!C24'),
            C('Facturación anual del año 1 del plan financiero', f'{X_PLAN}!Proyección 3 Años!B13'),
        ],
        'sector': ['SECT-01', 'SECT-02', 'SECT-03', 'SECT-04', 'SECT-05', 'SECT-06',
                   'SECT-07', 'SECT-08', 'SECT-09', 'TURG-01', 'TURG-02', 'TURG-03',
                   'TURG-05', 'TICK-01', 'TICK-03', 'MICH-04', 'MICH-10', 'REPS-01'],
        'tablas': [{
            'titulo': 'El sector en cifras, con fuente y fecha',
            'cabecera': ['Dato', 'Cifra', 'Fuente', 'Fecha'],
            'filas': [
                ['Establecimientos de hostelería en España', 'más de 300.000', 'Restauración News (Hostelería de España)', '2026-01'],
                ['Producción del sector hostelería', '166.211 M€', 'Restauración News (Hostelería de España)', '2026-01'],
                ['Facturación del subsector restaurantes', '31.000 M€ aprox.', 'Profesional Horeca (DBK)', '2026'],
                ['Empresas de restaurantes (censo DBK)', '70.997', 'Profesional Horeca (DBK)', '2026'],
                ['Empleo en hostelería (media anual)', '1.890.000 trabajadores', 'Diario de Gastronomía', '2026'],
                ['Gasto de turistas internacionales con actividades enogastronómicas', '37.261 M€', 'Agent Travel', '2026'],
                ['Turistas internacionales con actividades enogastronómicas', '24,8 millones', 'FOS Consulting', '2026-07'],
                ['Turistas cuyo MOTIVO PRINCIPAL fue la gastronomía', '445.000', 'Agent Travel', '2026'],
                ['Supervivencia empresarial a 5 años (todos los sectores)', '41,9 %', 'INE, Demografía Armonizada de Empresas', '2023'],
            ],
            'nota': 'Ninguna cifra de esta tabla procede de la memoria del autor: todas se '
                    'verificaron con su fuente el 29 de agosto de 2026 y se citan con la fecha de '
                    'publicación del medio. Cuando una cifra no tuvo fuente comprobable, no se '
                    'ha escrito.',
        }],
        'prohibido': NO_COMUN + [
            'España NO es el tercer país del mundo por restaurantes con estrella: '
            'usa exactamente la posición que te da el research y cita la fuente.',
            'No escribas ninguna cifra de mercado que no esté en la lista de datos '
            'del sector que te doy.',
        ],
    },
    {
        'n': 3, 'titulo': 'Modelos de Negocio',
        'resumen_indice': 'menú degustación, carta premium, barra de autor y chef\'s table, con sus márgenes.',
        'palabras': 1650, 'bloques': 2,
        'objetivo': 'Que el lector elija modelo con la calculadora delante: cada '
                    'formato mueve el ticket, el food cost, el número de manos '
                    'y la previsibilidad de la compra.',
        'epigrafes': [
            'Modelo 1: solo menú degustación',
            'Modelo 2: carta premium con menú corto',
            'Modelo 3: barra de autor y counter',
            "Modelo 4: chef's table y comedor privado como línea complementaria",
            'Cómo se elige: previsibilidad de compra, merma y rotación de mesa',
        ],
        'puntos': [
            'El food cost objetivo del pack es el 28 % en la ficha de escandallo '
            'y el 30 % en el escenario realista del P&L: explicar por qué el '
            'segundo es mayor (bebida, merma y pases de cortesía).',
            'Explicar la rotación: 65 plazas y 70 cubiertos al día no es una '
            'rotación de una mesa; es comida más cena con ocupaciones distintas.',
            'Cada modelo con su implicación en compras: el menú único permite '
            'comprar por encargo; la carta obliga a stock y sube la merma.',
        ],
        'cifras': [
            C('Food cost objetivo de la ficha de escandallo', f'{X_ESC}!Ficha (plantilla)!H4', 'pct0'),
            C('Food cost del escenario pesimista', f'{X_PL}!Escenarios!B11', 'pct0'),
            C('Food cost del escenario realista', f'{X_PL}!Escenarios!C11', 'pct0'),
            C('Food cost del escenario optimista', f'{X_PL}!Escenarios!D11', 'pct0'),
            C('Precio del menú degustación largo (escenario realista)', f'{X_TICKET}!Ticket Medio!C6'),
            C('Precio del menú degustación corto (escenario realista)', f'{X_TICKET}!Ticket Medio!C8'),
            C('Ticket medio de carta (escenario realista)', f'{X_TICKET}!Ticket Medio!C10'),
            C('Precio del maridaje (escenario realista)', f'{X_TICKET}!Ticket Medio!C12'),
            C('Margen bruto mensual del escenario realista', f'{X_PL}!Escenarios!C19'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Mix de oferta y ticket ponderado por escenario (calculadora-ticket-medio.xlsx, hoja «Ticket Medio»)',
            'src': (X_TICKET, 'Ticket Medio'),
            'cols': [('Concepto', 'A', 'txt'), ('Pesimista', 'B', 'num2'),
                     ('Realista', 'C', 'num2'), ('Optimista', 'D', 'num2')],
            'filas': (5, 20),
            'nota': 'Los porcentajes de comensales de las filas 5, 7 y 9 reparten el 100 % de la '
                    'sala; el maridaje y la copa son consumo adicional sobre el mismo comensal, '
                    'por eso pueden sumar más de 100 %.',
        }],
        'prohibido': NO_COMUN + [
            'No presentes el menú degustación como el modelo más rentable por '
            'definición: es el que más manos consume por comensal.',
        ],
    },
    {
        'n': 4, 'titulo': 'Estudio de Viabilidad y Plan Financiero',
        'resumen_indice': 'CAPEX, preapertura, fondo de maniobra, IVA, financiación, P&L y proyección a tres años.',
        'palabras': 2100, 'bloques': 3,
        'objetivo': 'Es el capítulo que decide si el proyecto existe. Tiene que '
                    'dejar UNA sola cifra de inversión, explicar de dónde sale '
                    'cada bloque y enseñar a leer el punto de equilibrio con la '
                    'cuota del banco dentro.',
        'epigrafes': [
            'Las tres necesidades de dinero: CAPEX, preapertura y fondo de maniobra',
            'El IVA de la inversión es tesorería, no coste',
            'Fuentes de financiación y servicio de la deuda',
            'La cuenta de resultados mensual, línea a línea',
            'Punto de equilibrio: en euros, en cubiertos y en meses',
            'La proyección a tres años y la rampa de arranque',
        ],
        'puntos': [
            'Dejar explícito que la cifra de inversión de esta guía es la del '
            'plan financiero y que las plantillas de checklist tasan las '
            'partidas una a una: si suman más que tu presupuesto, manda el '
            'presupuesto tasado.',
            'Explicar que el EBITDA no resta la amortización y que el EBIT sí; '
            'un EBITDA con la amortización dentro es un EBIT con otro nombre.',
            'Explicar el fondo de maniobra como meses de estructura completa, no '
            'como un colchón redondeado a ojo.',
            'Explicar la carencia del préstamo: durante la carencia se pagan solo '
            'intereses y el capital pendiente no baja.',
            'Explicar el IVA del CAPEX: se soporta al pagar la obra y el equipo, '
            'se recupera por el modelo 303 con su plazo, y mientras tanto hay que '
            'tenerlo en caja.',
        ],
        'cifras': [
            C('CAPEX total del plan, con el fondo de maniobra dentro', f'{X_PLAN}!Inversión!C27'),
            C('Fondo de maniobra dimensionado (6 meses)', f'{X_PLAN}!Inversión!C26'),
            C('Coste mensual de estructura', f'{X_PLAN}!Inversión!C32'),
            C('Alquiler mensual', f'{X_PLAN}!Inversión!C33'),
            C('Coste mensual de la brigada', f'{X_PLAN}!Inversión!C34'),
            C('Rentas y suministros de preapertura', f'{X_PLAN}!Inversión!C37'),
            C('Nóminas de preapertura', f'{X_PLAN}!Inversión!C38'),
            C('Total de costes de preapertura', f'{X_PLAN}!Inversión!C39'),
            C('NECESIDAD TOTAL DE FINANCIACIÓN', f'{X_PLAN}!Inversión!C46'),
            C('Importe del préstamo del ejemplo', f'{X_PLAN}!Financiación!B5'),
            C('Plazo del préstamo (años)', f'{X_PLAN}!Financiación!B6', 'num'),
            C('Tipo de interés nominal anual', f'{X_PLAN}!Financiación!B7', 'pct1'),
            C('Cuota mensual tras la carencia', f'{X_PLAN}!Financiación!B12'),
            C('Cuota mensual durante la carencia (solo intereses)', f'{X_PLAN}!Financiación!B13'),
            C('Fondos propios necesarios en el ejemplo', f'{X_PLAN}!Financiación!B31'),
            C('Total ingresos del mes tipo', f'{X_PLAN}!P&L Mensual!B10'),
            C('Total costes variables del mes tipo', f'{X_PLAN}!P&L Mensual!B15'),
            C('Total costes fijos sin amortización', f'{X_PLAN}!P&L Mensual!B32'),
            C('EBITDA del mes tipo', f'{X_PLAN}!P&L Mensual!B34'),
            C('EBIT del mes tipo', f'{X_PLAN}!P&L Mensual!B37'),
            C('Umbral de ventas mensual solo explotación', f'{X_CASH}!Cash Flow 12 Meses!B48'),
            C('Umbral de ventas mensual con el servicio de la deuda', f'{X_CASH}!Cash Flow 12 Meses!B50'),
            C('Cubiertos al día necesarios para el equilibrio', f'{X_CASH}!Cash Flow 12 Meses!B53', 'num1'),
            C('Mes de break-even de caja', f'{X_CASH}!Cash Flow 12 Meses!B54', 'num'),
            C('Ingresos del año 1 de la proyección', f'{X_PLAN}!Proyección 3 Años!B13'),
            C('Ingresos del año 3 de la proyección', f'{X_PLAN}!Proyección 3 Años!D13'),
            C('EBITDA del año 1', f'{X_PLAN}!Proyección 3 Años!B17'),
            C('EBITDA del año 3', f'{X_PLAN}!Proyección 3 Años!D17'),
            C('Resultado neto del año 1', f'{X_PLAN}!Proyección 3 Años!B23'),
            C('Meses de rampa hasta el ritmo de crucero', f'{X_PLAN}!Proyección 3 Años!B9', 'num'),
            C('Porcentaje del crucero que se factura el primer mes', f'{X_PLAN}!Proyección 3 Años!B10', 'pct0'),
            C('Tipo de IVA de restauración', f'{X_CASH}!Cash Flow 12 Meses!B25', 'pct0'),
            C('Tipo de IVA de la bebida alcohólica', f'{X_CASH}!Cash Flow 12 Meses!B26', 'pct0'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'CAPEX del proyecto, concepto a concepto (plan-financiero-3-anos.xlsx, hoja «Inversión»)',
                'src': (X_PLAN, 'Inversión'),
                'cols': [('#', 'A', 'num'), ('Concepto', 'B', 'txt'),
                         ('Presupuesto (€)', 'C', 'eur'),
                         ('Categoría de referencia', 'F', 'txt')],
                'filas': (5, 27),
                'nota': 'La columna «Real (€)» de la hoja se entrega vacía a propósito: es donde '
                        'anotas lo que pagas de verdad, y su desviación se enciende sola en cuanto '
                        'escribes la primera cifra.',
            },
            {
                'titulo': 'Preapertura y fondo de maniobra: las dos partidas que hunden a quien abre',
                'src': (X_PLAN, 'Inversión'),
                'cols': [('Concepto', 'A', 'txt'), ('Importe', 'C', 'eur2')],
                'filas': (32, 46),
                'nota': 'El cronograma de este mismo pack firma el arrendamiento en el mes 3 y '
                        'contrata la brigada en el 12 para abrir en el 18: hay renta y hay nóminas '
                        'antes de facturar un euro.',
            },
            {
                'titulo': 'Rangos de mercado por categoría (calculadora-capex.xlsx, hoja «CAPEX»)',
                'src': (X_CAPEX, 'CAPEX'),
                'cols': [('Categoría', 'B', 'txt'), ('Bajo (€)', 'C', 'eur'),
                         ('Medio (€)', 'D', 'eur'), ('Alto (€)', 'E', 'eur')],
                'filas': (5, 18),
            },
            {
                'titulo': 'Cuenta de resultados del mes tipo (plan-financiero-3-anos.xlsx, hoja «P&L Mensual»)',
                'src': (X_PLAN, 'P&L Mensual'),
                'cols': [('Concepto', 'A', 'txt'), ('Importe (€)', 'B', 'eur2'),
                         ('% s/ventas', 'C', 'pct1')],
                'filas': (5, 37),
            },
            {
                'titulo': 'Proyección a tres años (plan-financiero-3-anos.xlsx, hoja «Proyección 3 Años»)',
                'src': (X_PLAN, 'Proyección 3 Años'),
                'cols': [('Concepto', 'A', 'txt'), ('Año 1', 'B', 'eur'),
                         ('Año 2', 'C', 'eur'), ('Año 3', 'D', 'eur')],
                'filas': (13, 24),
            },
            {
                'titulo': 'Cuadro de amortización del préstamo (plan-financiero-3-anos.xlsx, hoja «Financiación»)',
                'src': (X_PLAN, 'Financiación'),
                'cols': [('Año', 'A', 'num'), ('Capital inicial (€)', 'B', 'eur'),
                         ('Cuota del año (€)', 'C', 'eur'), ('Intereses (€)', 'D', 'eur'),
                         ('Amortización (€)', 'E', 'eur'), ('Pendiente (€)', 'F', 'eur')],
                'filas': (18, 27),
            },
            {
                'titulo': 'Los doce meses del primer año, con IVA y con la cuota del banco (cash-flow-break-even.xlsx)',
                'src': (X_CASH, 'Cash Flow 12 Meses'),
                'cols': [('Concepto', 'A', 'txt'), ('Mes 1', 'B', 'eur'),
                         ('Mes 3', 'D', 'eur'), ('Mes 6', 'G', 'eur'),
                         ('Mes 9', 'J', 'eur'), ('Mes 12', 'M', 'eur'),
                         ('Año (€)', 'N', 'eur')],
                'filas': (10, 42),
            },
        ],
        'prohibido': NO_COMUN + [
            'No repitas «500.000-900.000 €»: esa cifra estaba en la edición '
            'anterior y la desmienten las plantillas del propio pack.',
            'No llames EBITDA a un resultado que ya ha restado la amortización.',
            'No hables del punto de equilibrio sin incluir la cuota del préstamo.',
            'No digas que el fondo de maniobra son «3 a 6 meses» y luego «6 meses»: '
            'es un rótulo único y una cifra calculada.',
        ],
    },
    {
        'n': 5, 'titulo': 'Requisitos Legales en España',
        'resumen_indice': 'sociedad, licencias, registro sanitario, seguros, protección de datos y el coste real de los trámites.',
        'palabras': 1750, 'bloques': 2,
        'objetivo': 'Que el lector sepa qué papel pide quién, en qué orden y con '
                    'qué plazo, sabiendo que la nomenclatura es autonómica y '
                    'municipal y que la licencia condiciona el calendario entero.',
        'epigrafes': [
            'Forma jurídica, constitución y altas previas a cualquier gasto',
            'Licencias de obra y de actividad: por tipo genérico, no por nombre',
            'Registro sanitario y comunicación previa a la autoridad autonómica',
            'Seguros obligatorios y recomendables, y protección de datos',
            'Terraza, música, horarios y venta de alcohol',
        ],
        'puntos': [
            'Decir explícitamente que el nombre de cada licencia cambia por '
            'comunidad autónoma y por ordenanza municipal, y que hay que '
            'preguntarlo en el propio ayuntamiento antes de firmar el alquiler.',
            'Explicar por qué el arrendamiento se negocia con carencia: la '
            'licencia tarda meses y la renta corre desde la firma.',
            'No mencionar el libro de visitas: está derogado.',
            'Explicar que el registro de jornada es obligatorio y que se conserva '
            'cuatro años.',
        ],
        'cifras': [
            C('Coste tasado del checklist legal', f'{CK_LEGAL}!Legal!G56'),
            C('Partidas del checklist legal aún sin presupuestar', f'{CK_LEGAL}!Legal!G57', 'num'),
            C('Proyecto técnico y licencias en el plan financiero', f'{X_PLAN}!Inversión!C22'),
            C('Seguros del primer año en el plan financiero', f'{X_PLAN}!Inversión!C23'),
            C('Meses de renta antes de abrir previstos en el plan', f'{X_PLAN}!Inversión!C35', 'num'),
        ],
        'sector': ['JORN-01', 'JORN-02', 'JORN-04'],
        'tablas': [{
            'titulo': 'Trámites legales del checklist, con responsable y coste tasado (checklist-legal.xlsx)',
            'src': (CK_LEGAL, 'Legal'),
            'cols': [('#', 'A', 'num'), ('Categoría', 'B', 'txt'), ('Trámite', 'C', 'txt'),
                     ('Responsable', 'D', 'txt'), ('Coste est. (€)', 'G', 'eur')],
            'filas': (5, 53),
            'nota': 'El total es un suelo: no incluye las partidas que llegan sin importe, que '
                    'dependen de tasas municipales y de honorarios que solo conoces al pedir '
                    'presupuesto.',
        }],
        'prohibido': NO_COMUN + [
            'No menciones el libro de visitas: está derogado.',
            'No des el nombre de una licencia como si fuera estatal: di el tipo '
            'genérico y advierte de que la nomenclatura es autonómica o municipal.',
            'No afirmes que existe un reglamento de registro horario digital: a la '
            'fecha de esta guía no está publicado en el BOE.',
        ],
    },
    {
        'n': 6, 'titulo': 'APPCC y Seguridad Alimentaria',
        'resumen_indice': 'los siete principios, los catorce alérgenos, anisakis, baja temperatura y vacío, y trazabilidad.',
        'palabras': 1800, 'bloques': 2,
        'objetivo': 'Convertir el APPCC en un sistema que se pueda auditar en un '
                    'restaurante que hace crudos, marinados y cocciones a baja '
                    'temperatura, que es exactamente donde está el riesgo.',
        'epigrafes': [
            'Los siete principios aplicados a una cocina de menú degustación',
            'Los catorce alérgenos de declaración obligatoria y cómo se gestionan en sala',
            'Anisakis: la congelación preventiva y su binomio legal',
            'Cocción a baja temperatura y envasado al vacío: validación documental',
            'Trazabilidad, etiquetado y registros que hay que poder enseñar',
        ],
        'puntos': [
            'Los catorce alérgenos son los del Anexo II del Reglamento (UE) '
            '1169/2011, con el RD 126/2015 para la información no envasada.',
            'La congelación preventiva es obligatoria para pescado destinado a '
            'consumo en crudo, marinado, escabechado o en salazón.',
            'Advertir de que los «cinco días» que circulan son la recomendación '
            'de AESAN para congeladores domésticos, no el requisito legal.',
            'Explicar que la responsabilidad de alérgenos en sala la asume el '
            'maître y que tiene que estar por escrito.',
        ],
        'cifras': [
            C('Coste tasado del checklist APPCC', f'{CK_APPCC}!APPCC!G62'),
            C('Partidas del APPCC sin importe tasado', f'{CK_APPCC}!APPCC!G63', 'num'),
        ],
        'sector': ['ANIS-01', 'ANIS-02', 'ANIS-03', 'ANIS-04', 'ANIS-05', 'ANIS-06'],
        'tablas': [
            {
                'titulo': 'Los catorce alérgenos de declaración obligatoria (Anexo II del Reglamento (UE) 1169/2011)',
                'cabecera': ['#', 'Alérgeno', 'Dónde aparece en una cocina de alta gama'],
                'filas': [
                    ['1', 'Cereales con gluten', 'Panes propios, masas, salsas ligadas con harina, cerveza, sémolas'],
                    ['2', 'Crustáceos', 'Fondos y jugos, gamba roja, cigala, bogavante, aceites infusionados'],
                    ['3', 'Huevos', 'Yemas curadas, merengues, helados, mahonesas, glaseados'],
                    ['4', 'Pescado', 'Fumets, garum de anchoa, colas de pescado en gelatinas, salsas Worcester'],
                    ['5', 'Cacahuetes', 'Pralinés, aceites, crujientes de repostería'],
                    ['6', 'Soja', 'Salsa de soja, miso propio, lecitina en emulsiones y aireados'],
                    ['7', 'Leche (incluida lactosa)', 'Mantequillas, beurre blanc, helados, quesos, sueros'],
                    ['8', 'Frutos de cáscara', 'Avellana, almendra, nuez y pistacho en pralinés y guarniciones'],
                    ['9', 'Apio', 'Fondos de verdura, mirepoix, jugos y consomés'],
                    ['10', 'Mostaza', 'Vinagretas, mostaza antigua, encurtidos'],
                    ['11', 'Granos de sésamo', 'Panes, crujientes, aceites y tahini'],
                    ['12', 'Dióxido de azufre y sulfitos (>10 mg/kg o mg/l)', 'Vinos, vinagres, frutas desecadas, algunos crustáceos'],
                    ['13', 'Altramuces', 'Harinas sin gluten, encurtidos'],
                    ['14', 'Moluscos', 'Ostra, navaja, almeja, calamar, pulpo y sus jugos'],
                ],
                'nota': 'La lista es la del Anexo II del Reglamento (UE) 1169/2011; la información '
                        'de alimentos no envasados se rige además por el Real Decreto 126/2015. '
                        'En un menú degustación la ficha de alérgenos se hace POR PASE, no por carta.',
            },
            {
                'titulo': 'Puntos de control del APPCC de este pack (checklist-appcc.xlsx)',
                'src': (CK_APPCC, 'APPCC'),
                'cols': [('#', 'A', 'num'), ('Bloque', 'B', 'txt'), ('Control', 'C', 'txt'),
                         ('Responsable', 'D', 'txt')],
                'filas': (5, 60),
            },
        ],
        'prohibido': NO_COMUN + [
            'No digas que la congelación anti-anisakis son cinco días: ese es el '
            'consejo de AESAN para congeladores domésticos.',
            'No conviertas la lista de alérgenos en trece ni en quince elementos: '
            'son catorce.',
        ],
    },
    {
        'n': 7, 'titulo': 'Ubicación y Local',
        'resumen_indice': 'metros necesarios de verdad, zonas, verificaciones antes de firmar y el contrato con carencia.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Evitar el error que más dinero cuesta: firmar un local que '
                    'no admite la cocina, la extracción o los vestuarios que el '
                    'proyecto necesita.',
        'epigrafes': [
            'Cuántos metros hacen falta de verdad para 65 plazas',
            'Las verificaciones técnicas antes de firmar: potencia, evacuación de humos, acometidas',
            'Zona, entorno competitivo y accesibilidad',
            'El contrato de arrendamiento: carencia, obras, duración y salida',
        ],
        'puntos': [
            'La superficie total de trabajo de esta guía es de 280 a 340 m², no '
            'de 250: por debajo no caben los vestuarios y aseos de personal que '
            'exige el Real Decreto 486/1997 para 24 personas.',
            'Repartir la superficie: sala, cocina, cámaras y almacén, aseos de '
            'clientes con aseo adaptado, vestuarios y aseos de personal, oficina '
            'y zona de recepción de mercancía.',
            'Explicar por qué la cocina no baja del 25 % de la superficie total.',
            'Explicar la carencia de obra en el arrendamiento con el alquiler '
            'mensual del plan financiero como referencia.',
        ],
        'cifras': [
            C('Alquiler mensual del plan financiero', f'{X_PLAN}!Inversión!C33'),
            C('Peso del alquiler sobre ventas en el mes tipo', f'{X_PLAN}!P&L Mensual!C22', 'pct1'),
            C('Meses de renta antes de abrir', f'{X_PLAN}!Inversión!C35', 'num'),
            C('Rentas y suministros de preapertura', f'{X_PLAN}!Inversión!C37'),
            C('Obra civil y reforma integral en el plan', f'{X_PLAN}!Inversión!C5'),
            C('Instalaciones (electricidad, fontanería, gas, ventilación)', f'{X_PLAN}!Inversión!C6'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Reparto de superficie para 65 plazas y una brigada de 24 personas',
            'cabecera': ['Zona', 'Superficie orientativa (m²)', 'Por qué'],
            'filas': [
                ['Sala de comensales', '120 a 160', '1,8 a 2,4 m² por plaza en fine dining, con paso de gueridón'],
                ['Cocina de producción y pase', '70 a 90', 'No menos del 25 % del total: partidas, pase, plonge y office'],
                ['Cámaras, almacén y bodega de servicio', '25 a 35', 'Cámaras separadas por familia y bodega climatizada'],
                ['Aseos de clientes, con aseo adaptado', '15 a 20', 'Accesibilidad conforme al CTE DB-SUA'],
                ['Vestuarios y aseos de personal', '18 a 25', 'Real Decreto 486/1997: separados de los de clientes, para 24 personas'],
                ['Recepción de mercancía y residuos', '10 a 15', 'Entrada independiente y zona de residuos refrigerada'],
                ['Oficina y despacho', '8 a 12', 'Documentación del APPCC, registro de jornada y caja'],
                ['TOTAL', '280 a 340', 'Superficie de trabajo de esta guía'],
            ],
        }],
        'prohibido': NO_COMUN + [
            'No escribas «250 m² totales»: con 120 a 160 de sala y 70 a 90 de '
            'cocina no quedan metros para aseos, vestuarios, almacén y oficina.',
            'No olvides los vestuarios y aseos de personal: son obligatorios y en '
            'la edición anterior no aparecían en ningún fichero.',
        ],
    },
    {
        'n': 8, 'titulo': 'Diseño de Cocina Profesional',
        'resumen_indice': 'flujo de trabajo, partidas, el pase, frío y extracción para un menú de 8 a 12 pases.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Dibujar una cocina que sostenga 70 cubiertos con ocho a doce '
                    'pases sin cruces de circulación ni contaminación cruzada.',
        'epigrafes': [
            'El flujo: recepción, almacenamiento, mise en place, producción, pase y lavado',
            'Las partidas y quién ocupa cada una',
            'El pase: dimensión, altura, iluminación y tiempos',
            'Frío, abatimiento y cuarto frío para crudos y marinados',
            'Extracción, climatización, ruido y consumo eléctrico',
        ],
        'puntos': [
            'Explicar la marcha adelante: el producto no vuelve hacia atrás y el '
            'sucio no cruza el limpio.',
            'Ligar el cuarto frío con el capítulo de APPCC: los crudos y los '
            'marinados obligan a congelación preventiva y a separación física.',
            'Explicar el dimensionado eléctrico y de extracción como partida que '
            'se decide en el proyecto, no en la compra del equipo.',
        ],
        'cifras': [
            C('Equipamiento de cocina caliente en el plan', f'{X_PLAN}!Inversión!C7'),
            C('Equipamiento de cocina fría en el plan', f'{X_PLAN}!Inversión!C8'),
            C('Pastelería y obrador en el plan', f'{X_PLAN}!Inversión!C9'),
            C('Zona de pase y expedición en el plan', f'{X_PLAN}!Inversión!C10'),
            C('Plonge y lavado en el plan', f'{X_PLAN}!Inversión!C11'),
            C('Almacenamiento y cámaras en el plan', f'{X_PLAN}!Inversión!C12'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Las seis zonas de la cocina y su presupuesto en el plan financiero',
            'src': (X_PLAN, 'Inversión'),
            'cols': [('Zona', 'B', 'txt'), ('Presupuesto (€)', 'C', 'eur2')],
            'filas': (7, 12),
            'nota': 'Cada zona se tasa una a una en checklist-equipamiento-cocina.xlsx, que es '
                    'la lista de la compra con responsable, estado y coste por línea.',
        }],
        'prohibido': NO_COMUN,
    },
    {
        'n': 9, 'titulo': 'Equipamiento de Cocina',
        'resumen_indice': 'la lista de la compra completa, con precio tasado, alternativas y lo que hay que pedir presupuesto.',
        'palabras': 1900, 'bloques': 2,
        'objetivo': 'Sustituir la lista de marcas por una lista de decisiones: '
                    'qué equipo, para qué técnica, con qué alternativa y con qué '
                    'coste tasado en el propio pack.',
        'epigrafes': [
            'Cocción: bloque modular, horno mixto, brasa y baja temperatura',
            'Frío: abatidor, cámaras, maduración y hielo',
            'Cuarto frío y técnicas: robot térmico, deshidratadora, sifones, envasado al vacío',
            'Pastelería y obrador: fermentación controlada, helados y chocolate',
            'Pase, plonge y almacenamiento',
            'Cómo se decide entre dos escalones de gama sin romper el presupuesto',
        ],
        'puntos': [
            'Nombrar de forma explícita el robot térmico tipo Thermomix y el '
            'Pacojet, que la landing anuncia y que en la edición anterior no '
            'aparecían en ningún fichero del pack.',
            'Explicar el conflicto de escalones: un bloque de seis fuegos de '
            'precio de hostelería estándar no convive con un horno de brasa de '
            'gama alta sin decidir cuál es el nivel del proyecto.',
            'Explicar el lavado: si el proyecto pide túnel de lavado, el '
            'presupuesto de un lavavajillas de capota no lo cubre.',
            'Advertir de que las líneas sin importe tasado del checklist se piden '
            'a proveedor y el total del libro se recalcula solo.',
        ],
        'cifras': [
            C('Coste tasado del checklist de equipamiento de cocina', f'{CK_EQUIP}!Equipamiento Cocina!G98'),
            C('Líneas del checklist aún sin importe', f'{CK_EQUIP}!Equipamiento Cocina!G99', 'num'),
            C('Rango bajo de equipamiento de cocina profesional', f'{X_CAPEX}!CAPEX!C6'),
            C('Rango medio de equipamiento de cocina profesional', f'{X_CAPEX}!CAPEX!D6'),
            C('Rango alto de equipamiento de cocina profesional', f'{X_CAPEX}!CAPEX!E6'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Lista de equipamiento de cocina con coste tasado (checklist-equipamiento-cocina.xlsx)',
            'src': (CK_EQUIP, 'Equipamiento Cocina'),
            'cols': [('#', 'A', 'num'), ('Zona', 'B', 'txt'), ('Equipo', 'C', 'txt'),
                     ('Responsable', 'D', 'txt'), ('Coste est. (€)', 'G', 'eur')],
            'filas': (5, 95),
            'nota': 'El total es un suelo. Las líneas sin importe son las que hay que pedir a '
                    'proveedor: la celda es editable y el total del libro se recalcula.',
        }],
        'prohibido': NO_COMUN + [
            'No des un rango de doscientos euros de amplitud para un bloque de '
            'cocción: o das el precio tasado del checklist o dices que se pide '
            'presupuesto.',
            'No recomiendes túnel de lavado y presupuestes un lavavajillas de '
            'capota en el mismo párrafo sin decir la diferencia de precio.',
        ],
    },
    {
        'n': 10, 'titulo': 'Diseño de Sala para 65 Plazas',
        'resumen_indice': 'distribución, mobiliario, iluminación, acústica y las partidas que condicionan la licencia.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Diseñar una sala que sostenga un servicio largo: distancias, '
                    'luz, ruido y una mesa que no obligue a mover al comensal.',
        'epigrafes': [
            'Distribución de las 65 plazas y distancias de servicio',
            'Mobiliario, mesas y confort para un servicio de tres horas',
            'Iluminación: temperatura de color, niveles y escenas de servicio',
            'Acústica: por qué condiciona la licencia y cómo se resuelve',
            'Accesibilidad, aseos y evacuación',
        ],
        'puntos': [
            'Ligar el confort con la duración del menú: una silla que aguanta '
            'cuarenta minutos no aguanta tres horas.',
            'Explicar el limitador-registrador acústico y el estudio de impacto '
            'acústico como condicionantes de licencia, no como un extra.',
            'Recordar que los aseos de personal son distintos de los de clientes.',
        ],
        'cifras': [
            C('Coste tasado del checklist de diseño de sala', f'{CK_SALA}!Diseño de Sala (FOH)!G42'),
            C('Partidas del checklist de sala sin importe', f'{CK_SALA}!Diseño de Sala (FOH)!G43', 'num'),
            C('Mobiliario de sala en el plan financiero', f'{X_PLAN}!Inversión!C13'),
            C('Iluminación y decoración en el plan financiero', f'{X_PLAN}!Inversión!C14'),
            C('Rango bajo de mobiliario de sala', f'{X_CAPEX}!CAPEX!C7'),
            C('Rango alto de mobiliario de sala', f'{X_CAPEX}!CAPEX!E7'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Checklist de diseño de sala, con coste tasado (checklist-diseno-sala.xlsx)',
            'src': (CK_SALA, 'Diseño de Sala (FOH)'),
            'cols': [('#', 'A', 'num'), ('Bloque', 'B', 'txt'), ('Elemento', 'C', 'txt'),
                     ('Responsable', 'D', 'txt'), ('Coste est. (€)', 'G', 'eur')],
            'filas': (5, 39),
        }],
        'prohibido': NO_COMUN,
    },
    {
        'n': 11, 'titulo': 'Vajilla, Cristalería y Cubertería Premium',
        'resumen_indice': 'cuánto material hace falta por plaza, criterios de compra, roturas y reposición anual.',
        'palabras': 1550, 'bloques': 2,
        'objetivo': 'Convertir la vajilla en una partida gestionada: dotación por '
                    'plaza, coeficiente de reposición y coste anual, no una lista '
                    'de marcas.',
        'epigrafes': [
            'Cuántas piezas por plaza hacen falta en un menú de ocho a doce pases',
            'Criterios de compra: reposición garantizada, apilado, lavado y peso',
            'Cristalería: copas por tipo de vino y por servicio',
            'Roturas y reposición anual: cómo se presupuesta',
        ],
        'puntos': [
            'Explicar la dotación en «vueltas»: cada pase necesita su pieza y el '
            'lavado no da tiempo a devolverla al servicio siguiente.',
            'Explicar que la reposición se presupuesta como porcentaje anual del '
            'valor del parque, no como imprevisto.',
        ],
        'cifras': [
            C('Coste tasado del checklist de vajilla y cristalería', f'{CK_VAJ}!Vajilla, Cristalería!G57'),
            C('Partidas de vajilla sin importe', f'{CK_VAJ}!Vajilla, Cristalería!G58', 'num'),
            C('Vajilla, cristalería y cubertería en el plan financiero', f'{X_PLAN}!Inversión!C15'),
            C('Mantelería y textil en el plan financiero', f'{X_PLAN}!Inversión!C16'),
            C('Rango bajo de vajilla en la calculadora de CAPEX', f'{X_CAPEX}!CAPEX!C8'),
            C('Rango alto de vajilla en la calculadora de CAPEX', f'{X_CAPEX}!CAPEX!E8'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Dotación de vajilla, cristalería y cubertería (checklist-vajilla-cristaleria.xlsx)',
            'src': (CK_VAJ, 'Vajilla, Cristalería'),
            'cols': [('#', 'A', 'num'), ('Familia', 'B', 'txt'), ('Elemento', 'C', 'txt'),
                     ('Coste est. (€)', 'G', 'eur')],
            'filas': (5, 54),
        }],
        'prohibido': NO_COMUN,
    },
    {
        'n': 12, 'titulo': 'Bodega y Servicio de Vinos',
        'resumen_indice': 'cómo se construye la carta, cuánto inmoviliza, márgenes reales con IVA y rotación.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Que la bodega deje de ser un capricho y pase a ser un activo '
                    'con rotación, margen medido sobre precio sin IVA y una '
                    'inversión que cuadra con el plan financiero.',
        'epigrafes': [
            'Cómo se construye una carta de vinos que se venda',
            'El margen de verdad: por qué se calcula sobre el precio sin IVA',
            'Rotación, inmovilizado y reposición',
            'Maridaje, copa y su peso en el ticket',
            'Conservación, servicio y formación del equipo',
        ],
        'puntos': [
            'El precio de carta en España se anuncia CON IVA y la bebida '
            'alcohólica va al 21 %: cruzar un coste sin IVA con un precio con IVA '
            'deja el food cost de bebida unos siete puntos por debajo del real.',
            'Explicar el multiplicador frente al margen sobre PVP: son dos '
            'lecturas distintas del mismo número.',
            'Ligar el valor del stock a coste con la partida de bodega inicial del '
            'plan financiero.',
        ],
        'cifras': [
            C('Valor del stock de bodega a coste', f'{X_BODEGA}!Bodega!N56'),
            C('Valor del stock de bodega a PVP', f'{X_BODEGA}!Bodega!O56'),
            C('Margen medio sobre PVP de la bodega', f'{X_BODEGA}!Bodega!L56', 'pct1'),
            C('Food cost medio de bebida', f'{X_BODEGA}!Bodega!M56', 'pct1'),
            C('Botellas en stock', f'{X_BODEGA}!Bodega!I56', 'num'),
            C('IVA de la bebida alcohólica', f'{X_BODEGA}!Bodega!C59', 'pct0'),
            C('Bodega inicial en el plan financiero', f'{X_PLAN}!Inversión!C17'),
            C('Vitrina climatizada en el plan financiero', f'{X_PLAN}!Inversión!C18'),
            C('Ingresos mensuales de vinos y bebidas', f'{X_PLAN}!P&L Mensual!B8'),
            C('Coste mensual de bodega', f'{X_PLAN}!P&L Mensual!B14'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Referencias de bodega con margen y rotación (budget-bodega.xlsx)',
            'src': (X_BODEGA, 'Bodega'),
            'cols': [('Referencia', 'B', 'txt'), ('Tipo', 'C', 'txt'), ('D.O.', 'D', 'txt'),
                     ('Coste (€)', 'E', 'eur2'), ('PVP carta con IVA (€)', 'F', 'eur2'),
                     ('Margen s/PVP', 'L', 'pct1'), ('Rotación/mes', 'J', 'num2')],
            'filas': (5, 14),
        }],
        'prohibido': NO_COMUN + [
            'No calcules el margen de una botella dividiendo el coste entre el '
            'precio de carta con IVA: hay que pasar el precio a sin IVA primero.',
        ],
    },
    {
        'n': 13, 'titulo': 'Brigada de Cocina',
        'resumen_indice': 'organigrama, salarios de convenio, coste con Seguridad Social, turnos y registro de jornada.',
        'palabras': 1900, 'bloques': 2,
        'objetivo': 'Dar el coste REAL del equipo de cocina, con la Seguridad '
                    'Social dentro, sin ningún puesto por debajo del mínimo legal '
                    'y con el cuadrante que lo sostiene.',
        'epigrafes': [
            'El organigrama de cocina para 70 cubiertos y ocho a doce pases',
            'Qué cobra cada puesto y por qué el convenio manda sobre el mínimo estatal',
            'Del bruto al coste de empresa: la Seguridad Social a cargo del empleador',
            'Turnos, jornada anual y descanso entre jornadas',
            'Registro de jornada: qué es obligatorio y qué no lo cumple',
            'Formación, rotación y retención en un equipo joven',
        ],
        'puntos': [
            'Decir explícitamente que el coste de personal del pack es el coste '
            'CON Seguridad Social, y que el porcentaje está en una celda del '
            'libro, no escrito a mano en el texto.',
            'Ningún puesto puede quedar por debajo del salario mínimo vigente: '
            'los suelos de la tabla son el mínimo, y el convenio provincial de '
            'hostelería prevalece si fija más.',
            'Explicar que un cuadrante con letras M, T, P y L no cumple el '
            'registro de jornada: hace falta hora de entrada y de salida por '
            'trabajador y día.',
            'Explicar el descanso mínimo de doce horas entre jornadas y qué '
            'significa en un servicio partido.',
        ],
        'cifras': [
            C('Personas en el cuadrante completo', f'{X_TURNOS}!Turnos Semana!A30', 'num'),
            C('Bruto anual sumado de toda la brigada', f'{X_TURNOS}!Turnos Semana!L33'),
            C('Coste anual con Seguridad Social', f'{X_TURNOS}!Turnos Semana!O33'),
            C('Horas semanales programadas en el cuadrante', f'{X_TURNOS}!Turnos Semana!K33', 'num'),
            C('Seguridad Social a cargo de la empresa', f'{X_TURNOS}!Turnos Semana!C41', 'pct0'),
            C('Salario mínimo vigente en cómputo anual (14 pagas)', f'{X_TURNOS}!Turnos Semana!C42', 'eur'),
            C('Jornada anual de referencia', f'{X_TURNOS}!Turnos Semana!C50', 'num'),
            C('Jornada máxima semanal', f'{X_TURNOS}!Turnos Semana!C44', 'num'),
            C('Coste mensual de personal de cocina en el P&L', f'{X_PLAN}!P&L Mensual!B20'),
            C('Peso del personal de cocina sobre ventas', f'{X_PLAN}!P&L Mensual!C20', 'pct1'),
            C('Coste mensual total de la brigada', f'{X_PLAN}!Inversión!C34'),
        ],
        'sector': ['JORN-01', 'JORN-02', 'JORN-03', 'JORN-04'],
        'tablas': [{
            'titulo': 'Brigada de cocina: puestos, bruto anual y coste por hora (plantilla-turnos-brigada.xlsx)',
            'src': (X_TURNOS, 'Turnos Semana'),
            'cols': [('#', 'A', 'num'), ('Puesto', 'C', 'txt'), ('Horas/semana', 'K', 'num'),
                     ('Bruto anual (€)', 'L', 'eur'), ('Pagas', 'M', 'num'),
                     ('Coste/hora (€)', 'O', 'eur2')],
            'filas': (6, 20),
            'nota': 'El coste por hora ya lleva la Seguridad Social a cargo de la empresa y '
                    'divide por la jornada anual aplicada del propio libro. Si escribes la jornada '
                    'de tu convenio, manda la tuya.',
        }],
        'prohibido': NO_COMUN + [
            'No escribas ningún salario por debajo del salario mínimo vigente que '
            'te doy en las cifras.',
            'No digas «incluyendo Seguridad Social» sobre una suma que sea el '
            'bruto: si la cifra es bruta, dilo, y da aparte la del coste.',
            'No des un porcentaje de Seguridad Social «aproximado» escrito a mano: '
            'usa el de la celda del libro.',
        ],
    },
    {
        'n': 14, 'titulo': 'Equipo de Sala',
        'resumen_indice': 'maître, sumiller, rangos y runners: perfiles, coste con Seguridad Social y ratios de servicio.',
        'palabras': 1900, 'bloques': 2,
        'objetivo': 'Dimensionar la sala de un menú largo, con el mismo rigor de '
                    'coste que la cocina y con el ratio de comensales por '
                    'profesional que el formato exige.',
        'epigrafes': [
            'El organigrama de sala y el ratio de comensales por profesional',
            'Perfiles: maître, sumiller, jefe de rango, camarero, runner y hostess',
            'Coste de sala con Seguridad Social y peso sobre ventas',
            'Turnos de sala, briefing y solape con cocina',
            'Carrera profesional: cómo se retiene a un sumiller y a un maître',
        ],
        'puntos': [
            'Explicar el ratio de servicio de un menú degustación frente al de '
            'carta: el número de intervenciones por comensal es lo que fija la '
            'plantilla, no el número de mesas.',
            'Dar el coste de sala con la Seguridad Social dentro y su peso sobre '
            'ventas, tomados del P&L del pack.',
            'Explicar por qué el sumiller es una posición de ingreso y no un gasto: '
            'ligarlo con el margen de bodega del capítulo 12.',
        ],
        'cifras': [
            C('Coste mensual de personal de sala en el P&L', f'{X_PLAN}!P&L Mensual!B21'),
            C('Peso del personal de sala sobre ventas', f'{X_PLAN}!P&L Mensual!C21', 'pct1'),
            C('Seguridad Social a cargo de la empresa', f'{X_TURNOS}!Turnos Semana!C41', 'pct0'),
            C('Salario mínimo vigente en cómputo anual (14 pagas)', f'{X_TURNOS}!Turnos Semana!C42', 'eur'),
            C('Coste anual de toda la plantilla con Seguridad Social', f'{X_TURNOS}!Turnos Semana!O33'),
            C('Coste tasado del checklist de contratación', f'{CK_CONTRA}!Contratación Equipo!G37'),
            C('Cubiertos al día del escenario realista', f'{X_TICKET}!Ticket Medio!C17', 'num'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'Equipo de sala: puestos, bruto anual y coste por hora (plantilla-turnos-brigada.xlsx)',
                'src': (X_TURNOS, 'Turnos Semana'),
                'cols': [('#', 'A', 'num'), ('Puesto', 'C', 'txt'), ('Horas/semana', 'K', 'num'),
                         ('Bruto anual (€)', 'L', 'eur'), ('Pagas', 'M', 'num'),
                         ('Coste/hora (€)', 'O', 'eur2')],
                'filas': (22, 30),
            },
            {
                'titulo': 'Trámites y costes de contratación (checklist-contratacion.xlsx)',
                'src': (CK_CONTRA, 'Contratación Equipo'),
                'cols': [('#', 'A', 'num'), ('Bloque', 'B', 'txt'), ('Trámite', 'C', 'txt'),
                         ('Coste est. (€)', 'G', 'eur')],
                'filas': (5, 34),
            },
        ],
        'prohibido': NO_COMUN + [
            'No escribas ningún salario por debajo del salario mínimo vigente.',
            'No presentes al sumiller como un lujo prescindible.',
        ],
    },
    {
        'n': 15, 'titulo': 'Menú Engineering para Fine Dining',
        'resumen_indice': 'escandallo con merma, food cost objetivo, PVP con IVA y la matriz de Kasavana y Smith por familia.',
        'palabras': 1750, 'bloques': 2,
        'objetivo': 'Enseñar a poner precio con la ficha técnica delante y a '
                    'clasificar la carta con la matriz aplicada DENTRO de cada '
                    'familia, que es la única forma de que un menú de 130 € y un '
                    'postre de 15 € convivan en la misma tabla.',
        'epigrafes': [
            'La ficha técnica: cantidad neta, merma y cantidad bruta a comprar',
            'Del coste por ración al PVP: food cost objetivo en celda, no en la fórmula',
            'El precio de carta lleva IVA: qué le pasa al food cost si lo olvidas',
            'La matriz de Kasavana y Smith, familia por familia',
            'Qué se hace con cada cuadrante: mantener, subir precio, promocionar o retirar',
        ],
        'puntos': [
            'La merma entra dividiendo, no multiplicando: la cantidad que compras '
            'es la neta dividida por uno menos la merma.',
            'Explicar el umbral de popularidad como el 70 % del mix medio, con el '
            'factor en celda por si la carta es corta.',
            'Explicar que la clasificación se hace comparando cada plato con el '
            'margen medio y el umbral de SU familia.',
        ],
        'cifras': [
            C('Food cost objetivo de la ficha', f'{X_ESC}!Ficha (plantilla)!H4', 'pct0'),
            C('IVA de restauración en la ficha', f'{X_ESC}!Ficha (plantilla)!H31', 'pct0'),
            C('Unidades vendidas en el ejemplo de la matriz', f'{X_MENU}!Menu Engineering!D31', 'num'),
            C('Margen medio ponderado de la carta de ejemplo', f'{X_MENU}!Menu Engineering!G31', 'eur2'),
            C('Factor del umbral de popularidad', f'{X_MENU}!Menu Engineering!I32', 'pct0'),
            C('Food cost del escenario realista', f'{X_PL}!Escenarios!C11', 'pct0'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'La carta de ejemplo clasificada por familia (menu-engineering-matrix.xlsx)',
            'src': (X_MENU, 'Menu Engineering'),
            'cols': [('Plato', 'B', 'txt'), ('Familia', 'C', 'txt'), ('Uds', 'D', 'num'),
                     ('Coste (€)', 'E', 'eur2'), ('PVP sin IVA (€)', 'F', 'eur2'),
                     ('Margen (€)', 'G', 'eur2'), ('Mix', 'H', 'pct1'),
                     ('Clasificación', 'I', 'txt'), ('Acción', 'J', 'txt')],
            'filas': (5, 16),
            'nota': 'La columna «Coste (€)» es el coste por ración de la ficha correspondiente de '
                    'escandallo-maestro.xlsx, que ya incluye la merma: no se vuelve a añadir aquí.',
        }],
        'prohibido': NO_COMUN + [
            'No multipliques por uno más la merma: un 20 % de merma es dividir '
            'entre 0,80, no multiplicar por 1,20.',
            'No dejes el food cost objetivo dentro de la fórmula como número fijo.',
        ],
    },
    {
        'n': 16, 'titulo': 'Proveedores Km0 y Producto de Temporada',
        'resumen_indice': 'cómo se construye la red de proveedores, la trazabilidad y el calendario de temporada.',
        'palabras': 1550, 'bloques': 2,
        'objetivo': 'Que el discurso de producto tenga detrás un sistema de '
                    'compras: quién sirve, con qué frecuencia, con qué documento '
                    'y con qué plan B.',
        'epigrafes': [
            'Cómo se selecciona y se homologa a un proveedor',
            'Lonja, huerta y pequeño productor: logística y mínimos de pedido',
            'Trazabilidad documental y recepción de mercancía',
            'Calendario de temporada y su efecto en la carta y en el escandallo',
        ],
        'puntos': [
            'Explicar la homologación de proveedor como parte del APPCC: '
            'documentación, condiciones de transporte y control en recepción.',
            'Explicar el efecto del producto de temporada sobre el escandallo: el '
            'coste por ración cambia y hay que rehacer la ficha.',
            'Explicar el plan B: qué se hace cuando la lonja no trae el pescado '
            'del pase principal.',
        ],
        'cifras': [
            C('Stock inicial de materias primas en el plan', f'{X_PLAN}!Inversión!C24'),
            C('Coste mensual de materia prima en el mes tipo', f'{X_PLAN}!P&L Mensual!B13'),
            C('Peso de la materia prima sobre ventas', f'{X_PLAN}!P&L Mensual!C13', 'pct1'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Ficha de homologación de proveedor: qué se pide y para qué',
            'cabecera': ['Documento o control', 'Quién lo pide', 'Para qué sirve'],
            'filas': [
                ['Registro sanitario del proveedor', 'Responsable de compras', 'Acredita que el operador está autorizado'],
                ['Ficha técnica del producto', 'Chef', 'Origen, formato, conservación y alérgenos declarados'],
                ['Albarán con lote y fecha', 'Recepción', 'Es la base de la trazabilidad hacia atrás'],
                ['Control de temperatura en recepción', 'Responsable APPCC', 'Cadena de frío verificada y registrada'],
                ['Condiciones de entrega y ventana horaria', 'Sous chef', 'Que la mercancía no llegue en pleno servicio'],
                ['Plan B por familia de producto', 'Chef', 'Un segundo proveedor homologado por cada pase crítico'],
                ['Acuerdo de precio y revisión', 'Compras', 'Que el escandallo no se rompa a mitad de temporada'],
            ],
        }],
        'prohibido': NO_COMUN,
    },
    {
        'n': 17, 'titulo': 'Cómo Aspirar a una Estrella MICHELIN',
        'resumen_indice': 'qué evalúa la guía de verdad, cuántos restaurantes distinguidos hay y qué hacer en los dos primeros años.',
        'palabras': 1750, 'bloques': 2,
        'objetivo': 'Dar una lectura honesta del reconocimiento: qué se evalúa, '
                    'qué no, cuántos hay y qué se puede trabajar desde el primer '
                    'servicio, con cada cifra citada con su fuente.',
        'epigrafes': [
            'Qué evalúa la guía y qué no evalúa',
            'Cuántos restaurantes distinguidos hay en España y cómo se reparte la selección',
            'La Estrella Verde: sostenibilidad como categoría propia',
            'Qué se puede trabajar desde el primer año: constancia, producto y equipo',
            'Preparación de una visita: el checklist de este pack, punto por punto',
        ],
        'puntos': [
            'Cada cifra de la selección va con la fuente y la edición, no como '
            'dato flotante.',
            'Matizar bien el «qué no evalúan»: el reconocimiento se otorga por lo '
            'que hay en el plato, y el nivel de confort se refleja aparte en la '
            'clasificación de la guía; eso no autoriza a descuidar el servicio ni '
            'la vajilla, que sí sostienen la experiencia y el precio.',
            'Explicar la Estrella Verde con su cifra y su fuente.',
        ],
        'cifras': [
            C('Coste tasado del checklist de preparación de inspección', f'{CK_INSP}!Preparación Inspección!G52'),
            C('Ítems del checklist de inspección', f'{CK_INSP}!Preparación Inspección!A49', 'num'),
        ],
        'sector': ['MICH-01', 'MICH-02', 'MICH-03', 'MICH-04', 'MICH-05', 'MICH-06',
                   'MICH-07', 'MICH-08', 'MICH-09', 'MICH-10'],
        'tablas': [
            {
                'titulo': 'La selección MICHELIN España y Andorra 2026, con su fuente',
                'cabecera': ['Categoría', 'Restaurantes', 'Fuente', 'Fecha'],
                'filas': [
                    ['Tres Estrellas', '16', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                    ['Dos Estrellas', '37', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                    ['Una Estrella', '254', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                    ['Total con Estrella', '307', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                    ['Estrellas Verdes (sostenibilidad)', '59', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                    ['Bib Gourmand', '204', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                    ['Total de la selección', '1.295', 'Espacio de Prensa MICHELIN España', '25-11-2025'],
                ],
                'nota': 'Datos de la nota de prensa oficial de la edición España y Andorra 2026, '
                        'presentada el 25 de noviembre de 2025. Ninguna cifra de este capítulo '
                        'procede de la memoria del autor.',
            },
            {
                'titulo': 'Checklist de preparación de una visita (checklist-inspeccion-michelin-repsol.xlsx)',
                'src': (CK_INSP, 'Preparación Inspección'),
                'cols': [('#', 'A', 'num'), ('Bloque', 'B', 'txt'), ('Punto de control', 'C', 'txt'),
                         ('Responsable', 'D', 'txt')],
                'filas': (5, 49),
            },
        ],
        'prohibido': NO_COMUN + [
            'No escribas que España es el tercer país del mundo por número de '
            'restaurantes con estrella: usa la posición del research con su fuente.',
            'No des ninguna cifra de inspectores: no hay fuente para eso en este '
            'trabajo, así que se formula sin número.',
            'No digas que la guía «no evalúa el servicio, la vajilla ni la '
            'decoración» sin el matiz de que el confort se refleja aparte.',
        ],
    },
    {
        'n': 18, 'titulo': 'Cómo Aspirar a un Sol Repsol',
        'resumen_indice': 'en qué se diferencia de MICHELIN, cuántos Soles hay y cómo se prepara la visita.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Explicar la otra guía de referencia en España sin repetir el '
                    'capítulo anterior: criterio, universo y estrategia.',
        'epigrafes': [
            'Qué es la Guía Repsol y en qué se diferencia de MICHELIN',
            'El universo de Soles: cuántos hay por categoría',
            'Cómo se prepara una visita y qué peso tiene el producto local',
            'Estrategia de posicionamiento para un restaurante que abre',
        ],
        'puntos': [
            'Cada cifra con su fuente y su edición.',
            'Explicar que las dos guías no son excluyentes y que el trabajo de '
            'base es el mismo: constancia, producto y equipo.',
        ],
        'cifras': [
            C('Coste tasado del checklist de preparación de inspección', f'{CK_INSP}!Preparación Inspección!G52'),
        ],
        'sector': ['REPS-01', 'REPS-02', 'REPS-03', 'REPS-04', 'REPS-05', 'REPS-06', 'REPS-07'],
        'tablas': [{
            'titulo': 'El universo de Soles Repsol en la edición 2026, con su fuente',
            'cabecera': ['Categoría', 'Restaurantes', 'Fuente', 'Fiabilidad'],
            'filas': [
                ['Tres Soles', '46', 'Gastroeconomy (Guía Repsol 2026)', 'media'],
                ['Dos Soles', '173', 'Gastroeconomy (Guía Repsol 2026)', 'media'],
                ['Un Sol', '589', 'Gastroeconomy (Guía Repsol 2026)', 'media'],
                ['Total con Sol', '808', 'Gastroeconomy (Guía Repsol 2026)', 'media'],
                ['Recomendados sin Sol', '1.605', 'Gastroeconomy (Guía Repsol 2026)', 'media'],
            ],
            'nota': 'Cifras tomadas de un medio especializado que recoge la presentación de la '
                    'edición 2026; se citan con esa procedencia y no como dato oficial de la guía.',
        }],
        'prohibido': NO_COMUN + [
            'No des cifras de inspectores ni de plazos de visita: no hay fuente.',
        ],
    },
    {
        'n': 19, 'titulo': "The World's 50 Best Restaurants",
        'resumen_indice': 'cómo funciona el ranking, qué se puede y qué no se puede trabajar, y qué hacer con el mercado internacional.',
        'palabras': 1900, 'bloques': 2,
        'objetivo': 'Explicar un ranking de votación sin inventar cifras: en qué '
                    'se diferencia de una guía de inspectores, qué construye '
                    'visibilidad internacional y qué es humo.',
        'epigrafes': [
            'Un ranking de votación no es una guía de inspectores',
            'Qué construye visibilidad internacional de verdad',
            'Prensa, congresos y colaboraciones: qué aporta cada canal',
            'El coste de la proyección internacional y cómo se presupuesta',
            'Qué NO hay que hacer: por qué perseguir un ranking desenfoca el negocio',
        ],
        'puntos': [
            'No dar ninguna cifra de votantes, de regiones ni de composición del '
            'panel: no hay fuente verificada en este trabajo, así que el capítulo '
            'se escribe en cualitativo.',
            'Explicar la diferencia estructural: un inspector visita y evalúa; un '
            'panel de votación recuerda y vota lo que ha visitado.',
            'Ligar el presupuesto de proyección con la partida de marketing del '
            'plan financiero y con el checklist de preapertura.',
            'Advertir de que el reconocimiento internacional cambia el mix de '
            'clientes y con él la previsión de reservas y de no-show.',
        ],
        'cifras': [
            C('Marketing de lanzamiento en el plan financiero', f'{X_PLAN}!Inversión!C21'),
            C('Web, branding y diseño gráfico en el plan financiero', f'{X_PLAN}!Inversión!C20'),
            C('Marketing mensual en el P&L', f'{X_PLAN}!P&L Mensual!B25'),
            C('Peso del marketing sobre ventas', f'{X_PLAN}!P&L Mensual!C25', 'pct1'),
            C('Coste tasado del checklist de marketing de preapertura', f'{CK_MKT}!Marketing Pre-Apertura!G42'),
        ],
        'sector': [],
        'tablas': [{
            'titulo': 'Tres formas distintas de reconocimiento y qué implica cada una',
            'cabecera': ['Reconocimiento', 'Cómo se decide', 'Qué premia', 'Qué puedes controlar'],
            'filas': [
                ['Guía de inspectores anónimos', 'Visitas anónimas y repetidas de inspectores', 'Lo que hay en el plato, con constancia', 'La cocina, el producto y la regularidad'],
                ['Guía de guías nacionales', 'Visitas de un equipo propio y criterio editorial', 'Producto local, cocina y experiencia global', 'La coherencia del proyecto con su territorio'],
                ['Ranking por votación de un panel', 'Votos de profesionales que han visitado el restaurante', 'La memoria y la conversación del sector', 'Estar donde el sector mira, sin poder forzar el voto'],
            ],
            'nota': 'Esta tabla es cualitativa a propósito: en este trabajo no se ha podido '
                    'verificar con fuente ninguna cifra sobre la composición del panel de un '
                    'ranking por votación, y una cifra sin fuente no entra en esta guía.',
        }],
        'prohibido': NO_COMUN + [
            'No escribas ninguna cifra de votantes, de expertos ni de regiones del '
            'panel: no hay fuente y no entra.',
            'No prometas que un plan de comunicación mete a nadie en un ranking.',
        ],
    },
    {
        'n': 20, 'titulo': 'Marketing, PR y Lanzamiento',
        'resumen_indice': 'plan de preapertura, prensa, reservas, evento inaugural y los primeros noventa días.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Llenar la sala desde el primer mes sin quemar el presupuesto: '
                    'la rampa de arranque del plan financiero es una previsión, y '
                    'esto es lo que hay que hacer para cumplirla.',
        'epigrafes': [
            'El calendario de preapertura: qué se hace en cada uno de los últimos seis meses',
            'Prensa gastronómica y creadores: cómo se trabaja y qué no funciona',
            'El evento inaugural y los servicios de prueba',
            'Reservas, depósito y política de no-show',
            'Los primeros noventa días: qué se mide y cuándo se ajusta',
        ],
        'puntos': [
            'Describir el evento inaugural con detalle operativo: invitados, '
            'formato, coste y qué se pretende conseguir.',
            'Explicar los servicios de prueba como parte del plan, con el equipo '
            'ya contratado y cobrando.',
            'Ligar la rampa de arranque del plan financiero con el esfuerzo de '
            'captación: si la previsión dice que el primer mes se factura una '
            'parte del crucero, el marketing tiene que sostener esa curva.',
        ],
        'cifras': [
            C('Coste tasado del checklist de marketing de preapertura', f'{CK_MKT}!Marketing Pre-Apertura!G42'),
            C('Partidas de marketing sin importe', f'{CK_MKT}!Marketing Pre-Apertura!G43', 'num'),
            C('Marketing de lanzamiento en el plan financiero', f'{X_PLAN}!Inversión!C21'),
            C('Marketing mensual en el P&L', f'{X_PLAN}!P&L Mensual!B25'),
            C('Meses de rampa hasta el ritmo de crucero', f'{X_PLAN}!Proyección 3 Años!B9', 'num'),
            C('Porcentaje del crucero que se factura el primer mes', f'{X_PLAN}!Proyección 3 Años!B10', 'pct0'),
            C('Facturación del mes 1 del cash flow', f'{X_CASH}!Cash Flow 12 Meses!B10'),
            C('Facturación del mes 12 del cash flow', f'{X_CASH}!Cash Flow 12 Meses!M10'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'Checklist de marketing de preapertura (checklist-marketing-preapertura.xlsx)',
                'src': (CK_MKT, 'Marketing Pre-Apertura'),
                'cols': [('#', 'A', 'num'), ('Bloque', 'B', 'txt'), ('Acción', 'C', 'txt'),
                         ('Responsable', 'D', 'txt'), ('Coste est. (€)', 'G', 'eur')],
                'filas': (5, 39),
            },
            {
                'titulo': 'El cronograma de apertura a 18 meses (cronograma-apertura-gantt.xlsx)',
                'src': (X_GANTT, 'Gantt'),
                'cols': [('Fase / Tarea', 'A', 'txt'), ('Responsable', 'B', 'txt'),
                         ('Mes de inicio', 'X', 'num'), ('Duración (meses)', 'Y', 'num'),
                         ('Depende de', 'Z', 'txt')],
                'filas': (5, 39),
                'saltar_vacias': False,
            },
        ],
        'prohibido': NO_COMUN + [
            'No des cifras de audiencia, seguidores o retorno de una campaña: no '
            'hay fuente para eso en este trabajo.',
        ],
    },
    {
        'n': 21, 'titulo': 'Tecnología para Fine Dining',
        'resumen_indice': 'TPV, reservas, CRM de comensales, gestión de alérgenos y digitalización discreta.',
        'palabras': 1900, 'bloques': 2,
        'objetivo': 'Elegir el sistema con criterio de operación y de dato, no de '
                    'catálogo: qué tiene que resolver cada pieza y cómo se '
                    'conecta con el APPCC, con el escandallo y con la sala.',
        'epigrafes': [
            'TPV y comandas: qué debe resolver en un menú de ocho a doce pases',
            'Reservas: motor propio, plataformas y política de depósito',
            'CRM de comensales: qué se guarda, para qué y con qué base legal',
            'Gestión de alérgenos y de preferencias en la ficha del comensal',
            'Inventario, escandallo y contabilidad: integración y traspaso de datos',
            'Digitalización discreta: la tecnología que el comensal no ve',
        ],
        'puntos': [
            'Desarrollar el CRM de comensales y la gestión de alérgenos, que la '
            'landing anuncia y que en la edición anterior no aparecían.',
            'Explicar la base legal del tratamiento de datos del comensal y la '
            'información mínima que hay que dar; los datos de salud, como una '
            'alergia, exigen especial cuidado.',
            'Explicar el depósito de reserva como herramienta contra el no-show y '
            'su implicación en cobro y devolución.',
            'Ligar el TPV con el escandallo: sin ventas por plato no hay ingeniería '
            'de menú posible.',
            'Escribir las plataformas de reserva que operan en España; no '
            'mencionar plataformas que no operen aquí.',
        ],
        'cifras': [
            C('TPV, software y tablets en el plan financiero', f'{X_PLAN}!Inversión!C19'),
            C('Tecnología y software mensual en el P&L', f'{X_PLAN}!P&L Mensual!B26'),
            C('Peso de tecnología sobre ventas', f'{X_PLAN}!P&L Mensual!C26', 'pct1'),
            C('Rango bajo de tecnología en la calculadora de CAPEX', f'{X_CAPEX}!CAPEX!C12'),
            C('Rango medio de tecnología en la calculadora de CAPEX', f'{X_CAPEX}!CAPEX!D12'),
            C('Rango alto de tecnología en la calculadora de CAPEX', f'{X_CAPEX}!CAPEX!E12'),
            C('Unidades vendidas del ejemplo de ingeniería de menú', f'{X_MENU}!Menu Engineering!D31', 'num'),
        ],
        'sector': ['JORN-02'],
        'tablas': [{
            'titulo': 'Qué tiene que resolver cada pieza del sistema y con qué se conecta',
            'cabecera': ['Pieza', 'Qué resuelve', 'Con qué se conecta', 'Riesgo si falta'],
            'filas': [
                ['TPV y comandas', 'Comanda por pase, tiempos y ventas por plato', 'Ingeniería de menú y escandallo', 'Sin ventas por plato no hay matriz de carta'],
                ['Motor de reservas propio', 'Reserva directa, depósito y datos del comensal', 'CRM y política de no-show', 'Toda la demanda pasa por un intermediario'],
                ['Plataformas de reserva', 'Visibilidad y captación de público nuevo', 'Motor propio y agenda de sala', 'Sala vacía en los primeros meses'],
                ['CRM de comensales', 'Historial, preferencias, alergias y ocasiones', 'Reservas y briefing de sala', 'El equipo repite preguntas al cliente habitual'],
                ['Ficha de alérgenos', 'Trazabilidad de la información por pase', 'APPCC y cocina', 'Riesgo sanitario y legal directo'],
                ['Inventario y escandallo', 'Coste por ración real y control de merma', 'Compras y P&L', 'El food cost se descubre a fin de mes'],
                ['Registro de jornada', 'Entrada y salida por trabajador y día', 'Nóminas y cuadrante', 'Incumplimiento laboral con sanción'],
                ['Contabilidad y facturación', 'Cierre diario y conciliación', 'TPV y banco', 'Descuadres que se detectan tarde'],
            ],
        }],
        'prohibido': NO_COMUN + [
            'No menciones plataformas de reserva que no operen en España.',
            'No des precios de licencias de software en dólares ni en ninguna '
            'moneda que no sea el euro.',
        ],
    },
    {
        'n': 22, 'titulo': 'Tendencias 2026-2027',
        'resumen_indice': 'sostenibilidad, fermentación, cocina vegetal, experiencia y lo que ya no funciona.',
        'palabras': 1700, 'bloques': 2,
        'objetivo': 'Cerrar con lo que va a mover la alta cocina española en los '
                    'dos próximos ejercicios, ligado a decisiones concretas de '
                    'carta, de compra y de equipo.',
        'epigrafes': [
            'Sostenibilidad medida, no declarada',
            'Fermentación y despensa propia: qué aporta al coste y al discurso',
            'Cocina vegetal en el centro del menú',
            'Experiencia, formato y duración del servicio',
            'Lo que ya no funciona y conviene abandonar',
        ],
        'puntos': [
            'Ligar la sostenibilidad con la categoría propia que ya reconoce la '
            'guía de inspectores, citando su cifra con fuente.',
            'Explicar la fermentación y la despensa propia por su efecto en el '
            'escandallo y en la carga de trabajo de la brigada, no como moda.',
            'Advertir de que cada tendencia que se adopta cambia el escandallo y '
            'el cuadrante: si no se recalculan, la tendencia sale cara.',
        ],
        'cifras': [
            C('Food cost objetivo de la ficha', f'{X_ESC}!Ficha (plantilla)!H4', 'pct0'),
            C('Coste mensual de materia prima', f'{X_PLAN}!P&L Mensual!B13'),
            C('EBITDA del mes tipo', f'{X_PLAN}!P&L Mensual!B34'),
        ],
        'sector': ['MICH-05', 'TURG-02', 'SECT-07'],
        'tablas': [{
            'titulo': 'Cinco decisiones de tendencia y su efecto medible en el negocio',
            'cabecera': ['Decisión', 'Efecto en el escandallo', 'Efecto en la brigada', 'Qué hay que medir'],
            'filas': [
                ['Despensa propia de fermentados', 'Baja el coste por ración de salsas y jugos', 'Suma horas de mise en place y control', 'Horas dedicadas frente a ahorro por ración'],
                ['Producto vegetal como pase principal', 'Baja el coste de materia prima por pase', 'Sube el número de manipulaciones', 'Margen por pase y aceptación en sala'],
                ['Aprovechamiento integral del producto', 'Reduce la merma que entra en la ficha', 'Exige formación y disciplina de despiece', 'Merma real por familia de producto'],
                ['Menú más corto y servicio más ágil', 'Menos pases, menos coste por comensal', 'Permite el mismo servicio con menos manos', 'Duración media del servicio y rotación'],
                ['Sostenibilidad verificable', 'Puede subir el coste de compra', 'Exige documentación y proveedor homologado', 'Coste por ración frente a valor percibido'],
            ],
        }],
        'prohibido': NO_COMUN + [
            'El título del capítulo es «Tendencias 2026-2027»: no escribas ni una '
            'sola vez «2025» ni «2025-2026».',
            'No presentes la inteligencia artificial como sustituto del criterio '
            'de cocina.',
        ],
    },
]


# --------------------------------------------------------------------------
# Los dos bonus (§5.5) — dejan de ser un índice
# --------------------------------------------------------------------------
BONUS = [
    {
        'nombre': 'business-plan-modelo',
        'guia': {
            'titulo': 'Plan de Negocio Modelo — Restaurante Gastronómico de 65 Plazas',
            'subtitulo': 'Documento completo para banco e inversores · Bonus del pack «Cómo Montar un Restaurante Gastronómico»',
            'cabecera': 'AI Chef Pro · Plan de Negocio Modelo',
            'portada_texto': (
                'Este no es un formulario con huecos: es un plan de negocio '
                'RELLENO, con el caso completo de un restaurante gastronómico de '
                '65 plazas y con todas sus cifras tomadas de las plantillas Excel '
                'de este mismo pack. Sustituye los datos por los tuyos y la '
                'estructura sigue en pie. Los pocos huecos que quedan están '
                'marcados entre corchetes porque solo tú puedes rellenarlos.'),
        },
        'gates': {
            'paginas_prometidas': 12,
            'palabras_objetivo': 3000,
            'min_palabras_cap': 250,
            'cifras_extra': ('734.020,40', '734.020', '1.155.923,84'),
            'mortalidad_permitida': ['41,9', '41.9', 'INE', '11.183'],
            'meta': {'title': 'Plan de Negocio Modelo — Restaurante Gastronómico 65 Plazas',
                     'subject': 'Bonus 1 del pack Cómo Montar un Restaurante Gastronómico · Versión 2.0 · agosto 2026'},
        },
        'capitulos': [
            {
                'n': 1, 'titulo': 'Resumen Ejecutivo',
                'resumen_indice': 'el proyecto en una página, con la cifra de inversión, la previsión y la petición al banco.',
                'palabras': 420, 'bloques': 1,
                'objetivo': 'La página que decide si el resto se lee. Proyecto, '
                            'mercado, equipo, inversión, retorno y petición.',
                'epigrafes': ['El proyecto en una página', 'Qué se pide y para qué'],
                'puntos': [
                    'Escribir el resumen COMO SI FUERA REAL, con las cifras del '
                    'plan financiero, no con enunciados de lo que el lector debe '
                    'escribir.',
                    'Dejar entre corchetes solo lo que depende del promotor: '
                    'nombre comercial, ciudad y fecha prevista de apertura.',
                ],
                'cifras': [
                    C('Necesidad total de financiación', f'{X_PLAN}!Inversión!C46'),
                    C('Préstamo solicitado', f'{X_PLAN}!Financiación!B5'),
                    C('Fondos propios aportados', f'{X_PLAN}!Financiación!B31'),
                    C('Ingresos previstos del año 1', f'{X_PLAN}!Proyección 3 Años!B13'),
                    C('Ingresos previstos del año 3', f'{X_PLAN}!Proyección 3 Años!D13'),
                    C('EBITDA previsto del año 1', f'{X_PLAN}!Proyección 3 Años!B17'),
                    C('Resultado neto previsto del año 1', f'{X_PLAN}!Proyección 3 Años!B23'),
                    C('Mes de break-even de caja', f'{X_CASH}!Cash Flow 12 Meses!B54', 'num'),
                ],
                'sector': ['SECT-03', 'TURG-01'],
                'tablas': [{
                    'titulo': 'Cuadro de mando del proyecto',
                    'src': (X_PLAN, 'Proyección 3 Años'),
                    'cols': [('Concepto', 'A', 'txt'), ('Año 1', 'B', 'eur'),
                             ('Año 2', 'C', 'eur'), ('Año 3', 'D', 'eur')],
                    'filas': (13, 24),
                }],
                'prohibido': NO_COMUN + ['No escribas «[Tu resumen ejecutivo aquí]»: el resumen va escrito.'],
            },
            {
                'n': 2, 'titulo': 'Concepto y Propuesta de Valor',
                'resumen_indice': 'qué restaurante es, para quién y por qué lo elegirán.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Definir el concepto con precisión operativa: formato, '
                            'menú, ticket y experiencia.',
                'epigrafes': ['El concepto', 'A quién se dirige y por qué lo elegirá'],
                'puntos': ['Ligar el concepto con el ticket y el mix de oferta del pack.'],
                'cifras': [
                    C('Ticket medio ponderado', f'{X_TICKET}!Ticket Medio!C16'),
                    C('Ticket medio con IVA que ve el comensal', f'{X_TICKET}!Ticket Medio!C24'),
                    C('Precio del menú largo', f'{X_TICKET}!Ticket Medio!C6'),
                    C('Precio del menú corto', f'{X_TICKET}!Ticket Medio!C8'),
                    C('Cubiertos al día previstos', f'{X_TICKET}!Ticket Medio!C17', 'num'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Mix de oferta previsto',
                    'src': (X_TICKET, 'Ticket Medio'),
                    'cols': [('Concepto', 'A', 'txt'), ('Realista', 'C', 'num2')],
                    'filas': (5, 20),
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 3, 'titulo': 'Análisis de Mercado',
                'resumen_indice': 'tamaño del sector, turismo gastronómico y competencia, con fuente por dato.',
                'palabras': 480, 'bloques': 1,
                'objetivo': 'Un análisis de mercado escrito, con cifras citadas, '
                            'no un enunciado de lo que habría que analizar.',
                'epigrafes': ['El mercado en cifras', 'Competencia y posicionamiento'],
                'puntos': ['Cada cifra con su fuente entre paréntesis.'],
                'cifras': [],
                'sector': ['SECT-01', 'SECT-02', 'SECT-03', 'SECT-04', 'SECT-06',
                           'SECT-08', 'SECT-09', 'TURG-01', 'TURG-02', 'TURG-03',
                           'MICH-04', 'REPS-01'],
                'tablas': [{
                    'titulo': 'El mercado, con fuente y fecha',
                    'cabecera': ['Dato', 'Cifra', 'Fuente'],
                    'filas': [
                        ['Producción del sector hostelería', '166.211 M€', 'Restauración News (Hostelería de España), 2026'],
                        ['Facturación del subsector restaurantes', '31.000 M€ aprox.', 'Profesional Horeca (DBK), 2026'],
                        ['Empresas de restaurantes', '70.997', 'Profesional Horeca (DBK), 2026'],
                        ['Gasto de turistas con actividades enogastronómicas', '37.261 M€', 'Agent Travel, 2026'],
                        ['Turistas con motivo principal gastronómico', '445.000', 'Agent Travel, 2026'],
                        ['Restaurantes con Estrella MICHELIN en España y Andorra', '307', 'Espacio de Prensa MICHELIN España, 25-11-2025'],
                        ['Restaurantes con Sol Repsol', '808', 'Gastroeconomy, 2026'],
                        ['Supervivencia empresarial a 5 años', '41,9 %', 'INE, Demografía Armonizada de Empresas'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 4, 'titulo': 'Ubicación, Local e Inversión',
                'resumen_indice': 'metros, obra, equipamiento y el desglose completo del CAPEX.',
                'palabras': 420, 'bloques': 1,
                'objetivo': 'Justificar la inversión partida a partida, con la '
                            'tabla del plan financiero delante.',
                'epigrafes': ['El local y su reparto de superficie', 'Desglose de la inversión'],
                'puntos': ['Distinguir CAPEX, preapertura y fondo de maniobra.'],
                'cifras': [
                    C('CAPEX total con fondo de maniobra', f'{X_PLAN}!Inversión!C27'),
                    C('Fondo de maniobra', f'{X_PLAN}!Inversión!C26'),
                    C('Total de preapertura', f'{X_PLAN}!Inversión!C39'),
                    C('Necesidad total de financiación', f'{X_PLAN}!Inversión!C46'),
                    C('Alquiler mensual', f'{X_PLAN}!Inversión!C33'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Desglose del CAPEX (plan-financiero-3-anos.xlsx, hoja «Inversión»)',
                    'src': (X_PLAN, 'Inversión'),
                    'cols': [('#', 'A', 'num'), ('Concepto', 'B', 'txt'), ('Presupuesto (€)', 'C', 'eur')],
                    'filas': (5, 27),
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 5, 'titulo': 'Plan de Operaciones',
                'resumen_indice': 'cocina, sala, compras, APPCC y el cronograma de apertura.',
                'palabras': 420, 'bloques': 1,
                'objetivo': 'Demostrar que el proyecto sabe cómo va a funcionar el '
                            'día a día, no solo cuánto cuesta.',
                'epigrafes': ['Operación diaria', 'Cronograma de apertura'],
                'puntos': ['Citar el cronograma a 18 meses y sus dependencias.'],
                'cifras': [
                    C('Cubiertos al día previstos', f'{X_TICKET}!Ticket Medio!C17', 'num'),
                    C('Días de apertura al mes', f'{X_TICKET}!Ticket Medio!C19', 'num'),
                    C('Personas en plantilla', f'{X_TURNOS}!Turnos Semana!A30', 'num'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Cronograma de apertura a 18 meses (cronograma-apertura-gantt.xlsx)',
                    'src': (X_GANTT, 'Gantt'),
                    'cols': [('Fase / Tarea', 'A', 'txt'), ('Mes de inicio', 'X', 'num'),
                             ('Duración (meses)', 'Y', 'num'), ('Depende de', 'Z', 'txt')],
                    'filas': (5, 39),
                    'saltar_vacias': False,
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 6, 'titulo': 'Equipo y Organización',
                'resumen_indice': 'organigrama, coste de personal con Seguridad Social y política laboral.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Enseñar al banco que la plantilla está dimensionada y '
                            'costeada, no estimada.',
                'epigrafes': ['Organigrama y dimensionado', 'Coste de personal y marco laboral'],
                'puntos': ['El coste va con la Seguridad Social dentro, y el porcentaje sale de una celda.'],
                'cifras': [
                    C('Bruto anual de toda la plantilla', f'{X_TURNOS}!Turnos Semana!L33'),
                    C('Coste anual con Seguridad Social', f'{X_TURNOS}!Turnos Semana!O33'),
                    C('Seguridad Social a cargo de la empresa', f'{X_TURNOS}!Turnos Semana!C41', 'pct0'),
                    C('Salario mínimo vigente anual', f'{X_TURNOS}!Turnos Semana!C42', 'eur'),
                ],
                'sector': ['JORN-02'],
                'tablas': [{
                    'titulo': 'Plantilla completa con bruto anual y coste por hora',
                    'src': (X_TURNOS, 'Turnos Semana'),
                    'cols': [('#', 'A', 'num'), ('Puesto', 'C', 'txt'),
                             ('Bruto anual (€)', 'L', 'eur'), ('Coste/hora (€)', 'O', 'eur2')],
                    'filas': (6, 30),
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 7, 'titulo': 'Plan de Marketing y Ventas',
                'resumen_indice': 'captación, rampa de arranque y presupuesto.',
                'palabras': 380, 'bloques': 1,
                'objetivo': 'Explicar cómo se llena la sala y con qué presupuesto.',
                'epigrafes': ['Captación y canales', 'Presupuesto y rampa de arranque'],
                'puntos': ['Ligar la rampa del plan financiero con el esfuerzo de captación.'],
                'cifras': [
                    C('Marketing de lanzamiento', f'{X_PLAN}!Inversión!C21'),
                    C('Marketing mensual', f'{X_PLAN}!P&L Mensual!B25'),
                    C('Meses de rampa', f'{X_PLAN}!Proyección 3 Años!B9', 'num'),
                    C('Porcentaje del crucero el primer mes', f'{X_PLAN}!Proyección 3 Años!B10', 'pct0'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Facturación mes a mes del primer año (cash-flow-break-even.xlsx)',
                    'src': (X_CASH, 'Cash Flow 12 Meses'),
                    'cols': [('Concepto', 'A', 'txt'), ('Mes 1', 'B', 'eur'), ('Mes 4', 'E', 'eur'),
                             ('Mes 8', 'I', 'eur'), ('Mes 12', 'M', 'eur'), ('Año', 'N', 'eur')],
                    'filas': (6, 10),
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 8, 'titulo': 'Plan Financiero',
                'resumen_indice': 'P&L, cash flow, break-even, proyección a tres años y cuadro de amortización.',
                'palabras': 520, 'bloques': 1,
                'objetivo': 'El bloque que el banco lee dos veces: cifras, '
                            'hipótesis y sensibilidad.',
                'epigrafes': ['Hipótesis y cuenta de resultados', 'Tesorería, break-even y servicio de la deuda'],
                'puntos': [
                    'Explicar que el EBITDA no resta amortización.',
                    'Dar el punto de equilibrio con la cuota del préstamo dentro.',
                ],
                'cifras': [
                    C('Total ingresos del mes tipo', f'{X_PLAN}!P&L Mensual!B10'),
                    C('EBITDA del mes tipo', f'{X_PLAN}!P&L Mensual!B34'),
                    C('EBIT del mes tipo', f'{X_PLAN}!P&L Mensual!B37'),
                    C('Umbral de ventas con servicio de deuda', f'{X_CASH}!Cash Flow 12 Meses!B50'),
                    C('Cubiertos al día para el equilibrio', f'{X_CASH}!Cash Flow 12 Meses!B53', 'num1'),
                    C('Mes de break-even de caja', f'{X_CASH}!Cash Flow 12 Meses!B54', 'num'),
                    C('Cuota mensual tras la carencia', f'{X_PLAN}!Financiación!B12'),
                    C('Cuota durante la carencia', f'{X_PLAN}!Financiación!B13'),
                ],
                'sector': [],
                'tablas': [
                    {
                        'titulo': 'Cuenta de resultados del mes tipo',
                        'src': (X_PLAN, 'P&L Mensual'),
                        'cols': [('Concepto', 'A', 'txt'), ('Importe (€)', 'B', 'eur2'),
                                 ('% s/ventas', 'C', 'pct1')],
                        'filas': (5, 37),
                    },
                    {
                        'titulo': 'Cuadro de amortización del préstamo',
                        'src': (X_PLAN, 'Financiación'),
                        'cols': [('Año', 'A', 'num'), ('Cuota del año (€)', 'C', 'eur'),
                                 ('Intereses (€)', 'D', 'eur'), ('Principal (€)', 'E', 'eur'),
                                 ('Pendiente (€)', 'F', 'eur')],
                        'filas': (18, 27),
                    },
                ],
                'prohibido': NO_COMUN,
            },
            {
                'n': 9, 'titulo': 'Análisis de Riesgos y Escenarios',
                'resumen_indice': 'los tres escenarios, los riesgos principales y su plan de mitigación.',
                'palabras': 420, 'bloques': 1,
                'objetivo': 'Enseñar que el promotor ha pensado en lo que puede '
                            'salir mal y tiene respuesta.',
                'epigrafes': ['Los tres escenarios', 'Riesgos y mitigación'],
                'puntos': ['Explicar qué pasa en el escenario pesimista y qué palancas se accionan.'],
                'cifras': [
                    C('Facturación mensual pesimista', f'{X_PL}!Escenarios!B17'),
                    C('EBITDA mensual pesimista', f'{X_PL}!Escenarios!B21'),
                    C('EBIT mensual pesimista', f'{X_PL}!Escenarios!B24'),
                    C('Facturación mensual optimista', f'{X_PL}!Escenarios!D17'),
                    C('EBITDA mensual optimista', f'{X_PL}!Escenarios!D21'),
                ],
                'sector': ['SECT-07', 'SECT-08'],
                'tablas': [{
                    'titulo': 'Los tres escenarios del plan',
                    'src': (X_PL, 'Escenarios'),
                    'cols': [('Concepto', 'A', 'txt'), ('Pesimista', 'B', 'eur2'),
                             ('Realista', 'C', 'eur2'), ('Optimista', 'D', 'eur2')],
                    'filas': (17, 24),
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 10, 'titulo': 'Petición, Garantías y Calendario de Ejecución',
                'resumen_indice': 'qué se pide al banco, con qué garantías y en qué plazos.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Cerrar con la petición concreta y el calendario de '
                            'disposición del dinero.',
                'epigrafes': ['La petición y sus condiciones', 'Calendario de disposición y de devolución'],
                'puntos': ['Dejar entre corchetes solo las garantías, que dependen del promotor.'],
                'cifras': [
                    C('Necesidad total de financiación', f'{X_PLAN}!Inversión!C46'),
                    C('Préstamo solicitado', f'{X_PLAN}!Financiación!B5'),
                    C('Plazo en años', f'{X_PLAN}!Financiación!B6', 'num'),
                    C('Tipo de interés nominal', f'{X_PLAN}!Financiación!B7', 'pct1'),
                    C('Carencia en años', f'{X_PLAN}!Financiación!B8', 'num'),
                    C('Fondos propios', f'{X_PLAN}!Financiación!B31'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Condiciones de la operación solicitada',
                    'src': (X_PLAN, 'Financiación'),
                    'cols': [('Concepto', 'A', 'txt'), ('Valor', 'B', 'num2')],
                    'filas': (5, 14),
                }],
                'prohibido': NO_COMUN,
            },
        ],
    },
    {
        'nombre': 'manual-servicio-sala',
        'guia': {
            'titulo': 'Manual de Servicio de Sala — Fine Dining',
            'subtitulo': 'Protocolo, guiones y fichas de formación · Bonus del pack «Cómo Montar un Restaurante Gastronómico»',
            'cabecera': 'AI Chef Pro · Manual de Servicio de Sala',
            'portada_texto': (
                'Un manual para formar al equipo, no un índice de buenas '
                'intenciones: mise en place de sala, secuencia del menú pase a '
                'pase, tiempos objetivo, temperaturas de servicio, briefing '
                'previo, guiones literales para la casuística difícil y fichas de '
                'formación con criterios de evaluación. Empieza por el protocolo '
                'de alérgenos, que es el único apartado de este documento cuya '
                'omisión tiene consecuencias legales y sanitarias.'),
        },
        'gates': {
            'paginas_prometidas': 12,
            'palabras_objetivo': 3000,
            'min_palabras_cap': 250,
            'cifras_extra': ('734.020,40', '1.155.923,84'),
            'mortalidad_permitida': ['41,9', 'INE'],
            'meta': {'title': 'Manual de Servicio de Sala — Fine Dining',
                     'subject': 'Bonus 2 del pack Cómo Montar un Restaurante Gastronómico · Versión 2.0 · agosto 2026'},
        },
        'capitulos': [
            {
                'n': 1, 'titulo': 'Protocolo de Alérgenos en Sala',
                'resumen_indice': 'los catorce alérgenos, quién responde, qué se pregunta y qué se registra.',
                'palabras': 480, 'bloques': 1,
                'objetivo': 'El apartado que abre el manual porque es el único '
                            'cuya omisión tiene consecuencias legales y sanitarias.',
                'epigrafes': ['Quién responde y qué se pregunta al reservar y al sentar',
                              'Qué se comunica a cocina y qué queda registrado'],
                'puntos': [
                    'La lista es la del Anexo II del Reglamento (UE) 1169/2011 y '
                    'la información de alimentos no envasados se rige por el Real '
                    'Decreto 126/2015.',
                    'El checklist de APPCC de este pack asigna la responsabilidad '
                    'al maître: escribirlo así.',
                    'En un menú degustación la ficha de alérgenos se hace por pase.',
                    'Un dato de alergia es un dato de salud: se trata con especial '
                    'cuidado y solo se guarda si hay base para ello.',
                ],
                'cifras': [],
                'sector': [],
                'tablas': [{
                    'titulo': 'Los catorce alérgenos de declaración obligatoria y su guion en sala',
                    'cabecera': ['#', 'Alérgeno', 'Qué se pregunta y qué se responde en sala'],
                    'filas': [
                        ['1', 'Cereales con gluten', 'Confirmar si es celiaquía o intolerancia; el pan propio y las masas se sustituyen, no se retiran del plato'],
                        ['2', 'Crustáceos', 'Revisar fondos y jugos: la traza más frecuente no está en el pase, está en la salsa'],
                        ['3', 'Huevos', 'Afecta a yemas curadas, helados, merengues y emulsiones'],
                        ['4', 'Pescado', 'Revisar fumets, garum y gelatinas'],
                        ['5', 'Cacahuetes', 'Revisar pralinés y aceites de repostería'],
                        ['6', 'Soja', 'Revisar salsa de soja, miso propio y lecitina de las emulsiones'],
                        ['7', 'Leche y lactosa', 'Distinguir alergia a la proteína de intolerancia a la lactosa: no es el mismo cambio'],
                        ['8', 'Frutos de cáscara', 'Preguntar por cuál en concreto y anotarlo en la comanda'],
                        ['9', 'Apio', 'Está en casi todos los fondos de verdura'],
                        ['10', 'Mostaza', 'Vinagretas y encurtidos'],
                        ['11', 'Sésamo', 'Panes, crujientes y aceites'],
                        ['12', 'Sulfitos', 'Vinos y vinagres: afecta también al maridaje'],
                        ['13', 'Altramuces', 'Harinas sin gluten y encurtidos'],
                        ['14', 'Moluscos', 'Ostra, navaja, almeja y sus jugos'],
                    ],
                    'nota': 'La comanda con alérgeno se canta en voz alta en el pase y se confirma '
                            'de vuelta. El plato modificado sale marcado y lo lleva siempre la misma '
                            'persona hasta la mesa.',
                }],
                'prohibido': NO_COMUN + ['No reduzcas la lista a menos de catorce alérgenos.'],
            },
            {
                'n': 2, 'titulo': 'Mise en Place de Sala y Briefing Previo',
                'resumen_indice': 'qué se monta, quién lo revisa y qué se dice en el briefing.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Dejar la sala lista y al equipo informado antes del '
                            'primer comensal.',
                'epigrafes': ['Mise en place de sala, paso a paso', 'El briefing pre-servicio: guion y duración'],
                'puntos': [
                    'Dar el guion del briefing con sus puntos fijos: pases del día, '
                    'roturas de stock, alérgenos de las reservas, VIP y cumpleaños, '
                    'y reparto de rangos.',
                    'Dar tiempos concretos de montaje.',
                ],
                'cifras': [
                    C('Plazas de la sala', f'{X_TURNOS}!Turnos Semana!A30', 'num'),
                    C('Cubiertos al día previstos', f'{X_TICKET}!Ticket Medio!C17', 'num'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Mise en place de sala con responsable y hora límite',
                    'cabecera': ['Tarea', 'Responsable', 'Hora límite', 'Cómo se verifica'],
                    'filas': [
                        ['Repaso de cristalería a contraluz', 'Camarero de rango', 'T menos 90 min', 'Muestreo de 10 copas por rango'],
                        ['Montaje de mesas y alineación', 'Jefe de rango', 'T menos 75 min', 'Revisión visual del maître'],
                        ['Repaso de cubertería y reposición', 'Runner', 'T menos 75 min', 'Cajón de repaso completo'],
                        ['Puesta a punto del gueridón y carros', 'Jefe de rango', 'T menos 60 min', 'Material completo y limpio'],
                        ['Comprobación de temperaturas de vinos', 'Sumiller', 'T menos 60 min', 'Termómetro y registro'],
                        ['Lectura de reservas, alergias y notas', 'Maître', 'T menos 45 min', 'Impreso de sala firmado'],
                        ['Briefing con cocina', 'Maître y chef', 'T menos 30 min', 'Todo el equipo presente'],
                        ['Prueba de iluminación y música', 'Maître', 'T menos 15 min', 'Escena de servicio activada'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 3, 'titulo': 'Recepción, Acomodo y Toma de Comanda',
                'resumen_indice': 'los primeros cinco minutos, que deciden el resto del servicio.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Estandarizar la llegada: quién recibe, en cuánto '
                            'tiempo, qué se dice y qué se anota.',
                'epigrafes': ['Recepción y acomodo', 'Toma de comanda y venta sugerida'],
                'puntos': [
                    'Dar guiones literales entrecomillados para la bienvenida, la '
                    'explicación del menú y la pregunta de alérgenos.',
                    'Dar tiempos objetivo en minutos.',
                ],
                'cifras': [
                    C('Precio del menú largo', f'{X_TICKET}!Ticket Medio!C6'),
                    C('Precio del menú corto', f'{X_TICKET}!Ticket Medio!C8'),
                    C('Precio del maridaje', f'{X_TICKET}!Ticket Medio!C12'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Tiempos objetivo de los primeros minutos',
                    'cabecera': ['Momento', 'Tiempo objetivo', 'Quién', 'Señal de que algo va mal'],
                    'filas': [
                        ['Saludo desde que se abre la puerta', 'menos de 15 segundos', 'Hostess', 'El comensal busca con la mirada'],
                        ['Acomodo en mesa', 'menos de 2 minutos', 'Hostess o maître', 'Espera de pie en la entrada'],
                        ['Ofrecimiento de agua y aperitivo', 'menos de 3 minutos', 'Jefe de rango', 'Mesa sin nada sobre el mantel'],
                        ['Explicación del menú', 'menos de 5 minutos', 'Jefe de rango', 'El comensal pregunta antes de que se le explique'],
                        ['Toma de comanda cerrada', 'menos de 8 minutos', 'Jefe de rango', 'Cocina sin comanda a los 10 minutos'],
                        ['Primer pase en mesa', 'menos de 15 minutos', 'Runner', 'Silencio prolongado en la mesa'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 4, 'titulo': 'Secuencia del Menú Degustación, Pase a Pase',
                'resumen_indice': 'marcaje, cambio de cubierto y de copa, tiempos entre pases y coordinación con el pase de cocina.',
                'palabras': 480, 'bloques': 1,
                'objetivo': 'El corazón del manual: cómo se sirve un menú de ocho '
                            'a doce pases sin que la mesa espere ni se atropelle.',
                'epigrafes': ['Marcaje, servicio y retirada', 'Tiempos entre pases y coordinación con cocina'],
                'puntos': [
                    'En plato emplatado se sirve y se retira POR LA DERECHA; la '
                    'izquierda es para el servicio en fuente. Escribirlo así, '
                    'explícitamente, porque la edición anterior lo enseñaba al revés.',
                    'El orden de servicio es en sentido horario desde el invitado '
                    'de honor y termina por el anfitrión, que es quien cata. No se '
                    'sirve «empezando por las señoras».',
                    'Dar los tiempos objetivo entre pases y qué hacer si se '
                    'desajustan.',
                ],
                'cifras': [],
                'sector': [],
                'tablas': [{
                    'titulo': 'Secuencia de un menú de diez pases con tiempos objetivo',
                    'cabecera': ['Momento del servicio', 'Acción de sala', 'Tiempo objetivo', 'Quién'],
                    'filas': [
                        ['Aperitivos', 'Marcaje sin cubierto, servicio a la mano', '0 a 10 min', 'Jefe de rango'],
                        ['Pase 1 a 3 (fríos)', 'Marcaje previo, servicio por la derecha, retirada por la derecha', '8 a 12 min entre pases', 'Runner y jefe de rango'],
                        ['Cambio a pases calientes', 'Cambio completo de cubertería y repaso de mesa', 'menos de 3 min', 'Jefe de rango'],
                        ['Pase 4 a 7 (principales)', 'Servicio por la derecha, salsa en mesa si procede', '10 a 14 min entre pases', 'Jefe de rango'],
                        ['Cambio de copa por maridaje', 'Copa nueva por vino, retirada de la anterior', 'antes del pase', 'Sumiller'],
                        ['Prepostre y postres', 'Repaso de mesa completo y cambio de cubertería', '8 a 10 min entre pases', 'Jefe de rango'],
                        ['Petit fours y café', 'Servicio en mesa o en zona de sobremesa', '5 a 8 min', 'Jefe de rango'],
                        ['Cuenta', 'Se presenta solo cuando se pide', 'menos de 4 min desde la petición', 'Maître'],
                    ],
                }],
                'prohibido': NO_COMUN + [
                    'No escribas «servir por la izquierda y retirar por la derecha»: '
                    'en plato emplatado se sirve y se retira por la derecha.',
                    'No escribas «empezando por las señoras».',
                ],
            },
            {
                'n': 5, 'titulo': 'Servicio de Vinos: Temperaturas, Decantación y Maridaje',
                'resumen_indice': 'cómo se presenta, se abre, se sirve y se repone cada tipo de vino.',
                'palabras': 420, 'bloques': 1,
                'objetivo': 'Un protocolo de vinos que cualquiera del equipo pueda '
                            'ejecutar, no solo el sumiller.',
                'epigrafes': ['Presentación, apertura y cata del anfitrión', 'Temperaturas, decantación y reposición'],
                'puntos': [
                    'La cata la hace quien pide el vino, y el orden de servicio '
                    'termina en esa persona.',
                    'Dar temperaturas concretas por tipo de vino.',
                    'Ligar el margen de bodega del pack con la venta sugerida sin '
                    'convertir al sumiller en vendedor.',
                ],
                'cifras': [
                    C('Margen medio sobre PVP de la bodega', f'{X_BODEGA}!Bodega!L56', 'pct1'),
                    C('Food cost medio de bebida', f'{X_BODEGA}!Bodega!M56', 'pct1'),
                    C('Precio del maridaje', f'{X_TICKET}!Ticket Medio!C12'),
                    C('Precio de la copa media', f'{X_TICKET}!Ticket Medio!C14'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Temperaturas y protocolo por tipo de vino',
                    'cabecera': ['Tipo', 'Temperatura de servicio', 'Copa', 'Decantación'],
                    'filas': [
                        ['Espumoso', '6 a 8 °C', 'Copa de vino blanco de tiro alto', 'No'],
                        ['Blanco joven', '8 a 10 °C', 'Copa de blanco', 'No'],
                        ['Blanco con crianza', '10 a 12 °C', 'Copa de blanco amplia', 'Ocasional, para abrir'],
                        ['Rosado', '8 a 10 °C', 'Copa de blanco', 'No'],
                        ['Tinto joven', '13 a 15 °C', 'Copa de tinto', 'Ocasional'],
                        ['Tinto con crianza', '15 a 17 °C', 'Copa de tinto amplia', 'Sí, para airear'],
                        ['Tinto de guarda', '16 a 18 °C', 'Copa de tinto amplia', 'Sí, con cuidado del poso'],
                        ['Generoso seco', '7 a 9 °C', 'Copa de catavinos', 'No'],
                        ['Dulce', '8 a 10 °C', 'Copa pequeña', 'No'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 6, 'titulo': 'Gestión de Quejas y Casuística Difícil',
                'resumen_indice': 'guiones literales para lo que sale mal, con quién decide y hasta dónde.',
                'palabras': 460, 'bloques': 1,
                'objetivo': 'Sustituir las veintiséis palabras del apartado '
                            'anterior por guiones que el equipo pueda usar tal cual.',
                'epigrafes': ['El método: escuchar, reconocer, resolver y registrar',
                              'Casuística con guion literal y límite de decisión'],
                'puntos': [
                    'Cada caso con la frase literal entrecomillada, quién la dice y '
                    'qué puede ofrecer sin consultar.',
                    'Dejar claro qué decisiones son del jefe de rango, cuáles del '
                    'maître y cuáles de dirección.',
                    'Explicar el registro de la incidencia y su revisión semanal.',
                ],
                'cifras': [],
                'sector': [],
                'tablas': [{
                    'titulo': 'Casuística, guion y límite de decisión',
                    'cabecera': ['Situación', 'Qué se dice', 'Quién decide', 'Hasta dónde se puede llegar'],
                    'filas': [
                        ['Plato fuera de punto', '«Lo retiro ahora mismo y le traigo otro recién hecho; disculpe la espera.»', 'Jefe de rango', 'Rehacer el pase sin consultar'],
                        ['Espera larga entre pases', '«Se ha retrasado el pase; le traigo algo mientras y lo compenso al final.»', 'Jefe de rango', 'Ofrecer un aperitivo de cortesía'],
                        ['Vino en mal estado', '«Tiene usted razón, esta botella no está bien; abrimos otra.»', 'Sumiller', 'Cambiar la botella sin discutir'],
                        ['Reserva no encontrada', '«Vamos a resolverlo ahora mismo; deme un momento y le acomodo.»', 'Maître', 'Acomodar aunque descuadre el rango'],
                        ['Alergia comunicada tarde', '«Gracias por decírnoslo; paro el pase y lo revisamos con cocina.»', 'Maître', 'Detener el servicio de esa mesa'],
                        ['Queja por la cuenta', '«Se lo reviso línea a línea con usted ahora mismo.»', 'Maître', 'Corregir el error en el momento'],
                        ['Comensal molesto por el ruido', '«Le cambio de mesa si le parece; tengo una más tranquila.»', 'Maître', 'Reubicar aunque suponga mover el rango'],
                        ['Queja en reseña posterior', 'Respuesta escrita, sin discutir y con invitación a volver', 'Dirección', 'Ofrecer una segunda visita'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 7, 'titulo': 'Reservas, No-Show, Prepago y Gestión de la Cuenta',
                'resumen_indice': 'la política que protege la caja sin espantar al cliente.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Escribir la política de reservas y de cobro que el '
                            'equipo aplica sin improvisar.',
                'epigrafes': ['Política de reserva, depósito y cancelación', 'Cierre de mesa y gestión de la cuenta'],
                'puntos': [
                    'Explicar el depósito y su devolución con claridad, y qué se '
                    'comunica al reservar.',
                    'Explicar el efecto del no-show en un restaurante de 65 plazas '
                    'con el ticket del pack.',
                    'El precio de carta se anuncia con IVA y la bebida alcohólica '
                    'tributa distinto.',
                ],
                'cifras': [
                    C('Ticket medio con IVA', f'{X_TICKET}!Ticket Medio!C24'),
                    C('Ticket medio sin IVA', f'{X_TICKET}!Ticket Medio!C16'),
                    C('Cubiertos al día previstos', f'{X_TICKET}!Ticket Medio!C17', 'num'),
                    C('Facturación diaria prevista', f'{X_TICKET}!Ticket Medio!C18'),
                    C('IVA de restauración', f'{X_TICKET}!Ticket Medio!B23', 'pct0'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Política de reservas: qué se aplica en cada caso',
                    'cabecera': ['Caso', 'Qué se aplica', 'Qué se comunica al reservar'],
                    'filas': [
                        ['Reserva de 1 a 4 comensales', 'Tarjeta en garantía, sin cargo previo', 'Cargo por no presentarse, indicado al confirmar'],
                        ['Reserva de 5 o más', 'Depósito por comensal a cuenta del menú', 'Importe, plazo de cancelación y devolución'],
                        ['Cancelación con más de 48 h', 'Devolución íntegra', 'Se confirma por escrito'],
                        ['Cancelación con menos de 24 h', 'Retención del depósito', 'Se avisa al reservar y se recuerda la víspera'],
                        ['No presentarse', 'Cargo del importe comunicado', 'Se avisa al reservar y se recuerda la víspera'],
                        ['Reducción de comensales el mismo día', 'Se mantiene el depósito de las plazas retiradas', 'Se avisa al reservar'],
                        ['Comedor privado o evento', 'Contrato con calendario de pagos', 'Condiciones firmadas por las dos partes'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 8, 'titulo': 'Fichas de Formación y Evaluación del Equipo',
                'resumen_indice': 'qué tiene que saber cada puesto, cómo se enseña y cómo se comprueba.',
                'palabras': 460, 'bloques': 1,
                'objetivo': 'Convertir el manual en un plan de formación con '
                            'criterios de evaluación medibles.',
                'epigrafes': ['El plan de formación por puesto y por semana',
                              'Cómo se evalúa: criterios observables, no impresiones'],
                'puntos': [
                    'Dar el plan de las primeras cuatro semanas de un incorporado.',
                    'Los criterios de evaluación tienen que ser observables en un '
                    'servicio, no opiniones.',
                ],
                'cifras': [
                    C('Personas en plantilla', f'{X_TURNOS}!Turnos Semana!A30', 'num'),
                    C('Coste tasado del checklist de contratación', f'{CK_CONTRA}!Contratación Equipo!G37'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Ficha de formación por puesto de sala',
                    'cabecera': ['Puesto', 'Qué debe dominar al final del mes 1', 'Cómo se comprueba', 'Quién evalúa'],
                    'filas': [
                        ['Hostess', 'Recepción, agenda, alergias en la reserva y acomodo', 'Observación de 3 servicios completos', 'Maître'],
                        ['Runner', 'Marcaje, servicio por la derecha y rutas de sala', 'Servicio de 2 rangos sin corrección', 'Jefe de rango'],
                        ['Camarero de rango', 'Secuencia completa del menú y repaso de mesa', 'Servicio de un rango completo solo', 'Jefe de rango'],
                        ['Jefe de rango', 'Explicación del menú, comanda, tiempos y quejas de nivel 1', 'Dos servicios llenos con evaluación escrita', 'Maître'],
                        ['Sumiller', 'Carta completa, temperaturas, maridaje y venta sugerida', 'Cata a ciegas de la carta por copas', 'Maître y dirección'],
                        ['Maître', 'Sala completa, incidencias, cuenta y coordinación con cocina', 'Un mes de servicios con revisión semanal', 'Dirección'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
            {
                'n': 9, 'titulo': 'Protocolo VIP, Ocasiones Especiales y Cierre del Servicio',
                'resumen_indice': 'qué se hace distinto, qué se registra y cómo se cierra la sala.',
                'palabras': 400, 'bloques': 1,
                'objetivo': 'Cerrar el manual con lo que diferencia a un equipo '
                            'que recuerda de uno que solo atiende.',
                'epigrafes': ['Comensal habitual, VIP y ocasiones especiales', 'Cierre de servicio y traspaso de información'],
                'puntos': [
                    'Explicar qué se guarda en la ficha del comensal y con qué '
                    'límite: una preferencia no es lo mismo que un dato de salud.',
                    'Dar el guion del cierre: qué se registra, quién lo escribe y '
                    'quién lo lee al día siguiente.',
                ],
                'cifras': [],
                'sector': [],
                'tablas': [{
                    'titulo': 'Cierre de servicio: qué se registra y quién lo lee',
                    'cabecera': ['Registro', 'Quién lo escribe', 'Quién lo lee', 'Para qué'],
                    'filas': [
                        ['Incidencias de sala', 'Maître', 'Dirección y chef', 'Corregir antes del siguiente servicio'],
                        ['Notas de comensales habituales', 'Jefe de rango', 'Maître', 'Reconocer al cliente en la siguiente visita'],
                        ['Alergias atendidas', 'Maître', 'Chef y responsable de APPCC', 'Trazabilidad y mejora de las fichas por pase'],
                        ['Roturas de material', 'Jefe de rango', 'Dirección', 'Presupuesto de reposición'],
                        ['Ventas por plato y por vino', 'TPV', 'Chef y sumiller', 'Ingeniería de menú y de carta de vinos'],
                        ['No-show y cancelaciones', 'Hostess', 'Dirección', 'Ajuste de la política de depósito'],
                    ],
                }],
                'prohibido': NO_COMUN,
            },
        ],
    },
]
