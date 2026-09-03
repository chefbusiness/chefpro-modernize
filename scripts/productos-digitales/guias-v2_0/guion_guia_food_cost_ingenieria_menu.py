#!/usr/bin/env python3
"""
guion_guia_food_cost_ingenieria_menu.py — GUION de la «Guía Food Cost +
Ingeniería de Menú» v1.0 (SPEC `guia-food-cost-SPEC.md`, §4 y §4.2).

Mismo esquema que el representante de la familia
(`guion_guia_restaurante_gastronomico.py`): un capítulo no se le pide a
`bridge.py` con un título, se le pide con un guion CERRADO. Por capítulo van
(a) el objetivo, (b) 4-6 epígrafes, (c) las **cifras del propio producto**
citadas por `fichero.xlsx!Hoja!Celda` —que `documentos.py` resuelve con
openpyxl `data_only` antes de escribir el prompt, así que el modelo recibe el
NÚMERO, no el fichero—, (d) los datos del sector por `id` de
`auditorias/guias-v2-research-sector.json` (la cifra sin fuente NO entra; los
ids sin `cifra`, sin `url` o de fiabilidad baja llegan al prompt como HUECO y
el capítulo se escribe sin número), (e) las tablas exigidas —que las construye
el maquetador desde el xlsx, no el modelo—, (f) el presupuesto de palabras y
(g) lo que NO debe decir.

FUENTE ÚNICA DE CIFRAS (SPEC §7-bis.7 de la familia): los OCHO libros de
`astro-site/public/dl/guia-food-cost-ingenieria-menu/`, que se LEEN y no se
tocan. Mientras el producto no esté copiado a producción viven en
`scripts/productos-digitales/guia-food-cost/build/`, y sus mapas de celdas
(`mapa-*.json`) son el contrato: toda coordenada de este guion sale de ahí o
está verificada abriendo el libro con `data_only`.

Presupuesto (SPEC §4): 20 capítulos, 60 páginas prometidas, ~30.000 palabras
objetivo, 1.400-1.600 palabras por capítulo (el 19 lleva 2.200 por ser el caso
integral; los 03, 11 y 15 llevan 1.700 porque cargan la matriz fiscal, la
matriz de Kasavana & Smith y el multicanal). Bonus: 12 ejercicios resueltos de
550-700 palabras, ~7.500 palabras y ~17 páginas.

DECISIONES QUE ESTE GUION MATERIALIZA (no se reabren aquí): D4 (matriz de IVA
3x3 verificada contra el BOE), D5 (prime cost 65 %/55 %), D6 (matriz
multi-método honesta: se enseña dónde discrepan), D8 (señuelo primero, Wansink
con salvedad), D9 (bonus de 12 ejercicios), D10 (lista negra: ninguna cifra de
inflación, de mortalidad ni de tarifario «oficial»), D12 (vocabulario
ES/LATAM), D14 (hotel, buffet, banquete y catering dentro del cap. 14), D16
(cap. 20: criterio frente a automatización).

Via: Claude Code
"""

PID = 'guia-food-cost-ingenieria-menu'

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
    '*Esta guía es un documento de trabajo profesional, no un dictamen fiscal, '
    'jurídico ni contable. Los tipos de IVA que se citan son los vigentes en '
    'España al cierre de esta edición y están recogidos en celdas editables de '
    'las hojas de cálculo precisamente porque cambian: si cambia el tipo, se '
    'cambia la celda y todo el libro se recalcula. Los costes, precios de '
    'venta, márgenes y porcentajes son valores de ejemplo tomados de las ocho '
    'plantillas Excel que acompañan a este pack y sirven para que los '
    'sustituyas por los tuyos: ninguno es una previsión de tus resultados ni '
    'una recomendación de precio. La calificación fiscal de una operación '
    'concreta —qué es servicio de hostelería y qué es entrega de bienes, qué '
    'tipo lleva un producto determinado— depende de los hechos de esa '
    'operación. Antes de cambiar la carta, el precio de un plato o el tipo con '
    'el que facturas, contrasta con tu asesoría.*')

GUIA = {
    'pid': PID,
    'titulo': 'Guía Food Cost + Ingeniería de Menú',
    'subtitulo': 'Escandallo, precios y rentabilidad de tu carta · España 2026',
    'autor_linea': 'John Guerrero · AI Chef Pro · aichef.pro',
    'cabecera': 'AI Chef Pro · Guía Food Cost + Ingeniería de Menú',
    'fecha': 'septiembre de 2026',
    'version': '1.0',
    'bio': BIO,
    'legal': LEGAL,
    'portada_texto': (
        '20 capítulos, 8 herramientas en Excel con fórmulas vivas y un bonus '
        'de 12 ejercicios resueltos para escandallar tu carta, ponerle precio '
        'y saber qué plato te da de comer y cuál te lo quita. No es una guía '
        'de apertura: está escrita para quien ya sirve todos los días. Todas '
        'las cifras que leerás salen de los libros de este mismo pack, así que '
        'el texto y las hojas de cálculo dicen lo mismo; cuando cambies un '
        'dato en el Excel, la lógica que explica este documento sigue siendo '
        'la tuya.'),
    'gates': {
        'paginas_prometidas': 60,
        'palabras_objetivo': 30000,
        'min_palabras_cap': 900,
        # Cifras con separador de miles que el texto puede escribir y que NO
        # están en ninguna celda de los ocho libros ni en el research. Se
        # admiten UNA A UNA y por SIGNIFICADO (lección RD-21 del representante:
        # que las celdas existan no basta para dar por buena una derivada).
        #  · 1.100 € = coste anual de referencia, por local y sin IVA, de un
        #    software de gestión de escandallos y de carta. Es la cifra de la
        #    decisión D16 de la SPEC, que fija la frase del capítulo 20
        #    («esta guía te da el criterio; el software te da la
        #    automatización»). No sale de ninguna celda porque no es un dato
        #    del pack: es el precio de mercado del que se contrasta.
        'cifras_extra': ('1.100', '1.100,00'),
        'cifras_ignorar': (),
        # Ninguna. En esta guía NO se escribe ni una cifra de cierre, quiebra o
        # mortalidad de restaurantes (D10), así que cualquier coincidencia del
        # patrón es un defecto que hay que corregir, no una excepción.
        'mortalidad_permitida': [],
    },
}

# --------------------------------------------------------------------------
# Los ocho libros del pack. Se referencian por NOMBRE de fichero: documentos.py
# los busca en astro-site/public/dl/<pid>/.
# --------------------------------------------------------------------------
X_FICHA = 'ficha-escandallo-base.xlsx'
X_MERMA = 'rendimiento-mermas-producto.xlsx'
X_PRECIO = 'precio-objetivo-multi-metodo.xlsx'
X_MATRIZ = 'matriz-multimetodo-carta.xlsx'
X_MULTI = 'simulador-repricing-multicanal.xlsx'
X_BEBIDAS = 'carta-de-bebidas-beverage-cost.xlsx'
X_PRIME = 'cuadro-de-mando-prime-cost.xlsx'
X_PLAN90 = 'plan-accion-90-dias.xlsx'

# --------------------------------------------------------------------------
# Prohibiciones transversales: van en TODOS los capítulos.
# Las siete primeras son la LISTA NEGRA de la decisión D10 de la SPEC; las
# siguientes fijan el vocabulario de la D12 y el ámbito del producto.
# --------------------------------------------------------------------------
NO_COMUN = [
    # ---- Lista negra D10 -------------------------------------------------
    'PROHIBIDO escribir cualquier porcentaje de food cost atribuido a un tipo '
    'de negocio concreto que no esté en los datos del sector que te doy. En '
    'particular, NO escribas que una marisquería trabaja con un 40-42 % ni '
    'ninguna variante de esa frase: esa cifra no tiene fuente y no existe.',
    'PROHIBIDO escribir ninguna cifra de inflación, de IPC ni de subida de '
    'precios de la materia prima: ni un porcentaje, ni un dato mensual, ni una '
    'variación interanual, ni siquiera «aproximadamente». Lo que se enseña es '
    'DÓNDE mirarlo (la nota de prensa del IPC del INE y el sistema de precios '
    'origen-mayorista del Ministerio de Agricultura), no cuánto vale hoy.',
    'PROHIBIDO escribir que un porcentaje de los restaurantes «no conoce su '
    'food cost», «no escandalla», «no aplica escandallos» o similar. No hay '
    'fuente para eso. Si quieres decir que es una práctica poco extendida, '
    'dilo sin número.',
    'PROHIBIDO usar ningún porcentaje como efecto de un anclaje de precio '
    '(«subir el precio ancla eleva el ticket un tanto por ciento»): de la '
    'psicología de precios sólo puedes escribir las cifras que te llegan en '
    'los datos del sector, con su fuente y con su salvedad.',
    'PROHIBIDO citar a Gregg Rapp, «el ingeniero de menús», o cualquier caso '
    'de consultor con resultados atribuidos: no está verificado.',
    'PROHIBIDO presentar ningún porcentaje de comisión de plataforma de '
    'reparto como «tarifa oficial», «tarifario» o dato cerrado. Las comisiones '
    'se escriben como ORDEN DE MAGNITUD, con la horquilla y con la fuente, y '
    'diciendo que dependen de la zona, del plan contratado y de quién reparte.',
    'PROHIBIDO escribir ninguna cifra de cierre, quiebra, fracaso o '
    'supervivencia de restaurantes, NI SIQUIERA PARA NEGARLA O DESMENTIRLA. '
    'Tampoco escribas frases del tipo «con ese margen el X % del beneficio '
    'desaparece»: el porcentaje pegado a un verbo de desaparición se lee como '
    'un dato de mortalidad. Reformula sin número.',
    # ---- Ámbito del producto --------------------------------------------
    'NO expliques qué es un escandallo desde cero, ni definas «food cost» como '
    'si el lector no lo hubiera oído nunca. Esta guía es para quien ya opera: '
    'la primera frase de cada bloque asume que sabe lo que es una ficha '
    'técnica y un porcentaje sobre ventas. Lo que aporta el capítulo es el '
    'criterio, el caso límite y la decisión, no la definición.',
    'NO conviertas esta guía en una guía de apertura: aquí no se habla de '
    'licencias, de obra, de inversión inicial, de plan de negocio ni de '
    'financiación. El lector ya tiene el local abierto y el problema es la '
    'carta.',
    'NO repitas las siete tácticas de negociación con proveedores del bono del '
    'Kit de Escandallos. Cuando toque negociar, se explica cuándo y con qué '
    'dato se va a la mesa, y se remite al material que ya tiene el lector.',
    'NO escribas ningún precio de venta, coste, margen ni porcentaje que no '
    'esté en la lista de cifras que te doy o en los datos del sector. Ni '
    '«ronda los», ni «suele estar en», ni un ejemplo inventado para ilustrar. '
    'Si necesitas un número, es uno de los que tienes; si no lo tienes, la '
    'frase se escribe sin número.',
    'NO hagas cuentas nuevas con las cifras que te doy: no sumes, no restes y '
    'no proyectes a doce meses para escribir un total que no te he dado. Los '
    'totales ya están calculados en los libros.',
    # ---- Vocabulario D12 -------------------------------------------------
    'VOCABULARIO OBLIGATORIO (español de España, con la equivalencia de '
    'Hispanoamérica sólo la primera vez que aparezca el término en el '
    'capítulo): «escandallo (costeo de recetas)», «coste (costo)», «precio de '
    'venta», «plato», «carta (menú)». Después de esa primera mención se usa '
    'siempre la forma española, sin repetir el paréntesis. No escribas '
    '«costeo» ni «costo» a secas, ni llames «menú» a la carta salvo cuando '
    'hables del menú de precio fijo, que sí es un menú.',
    'NO uses anglicismos que tengan término español asentado en el oficio: se '
    'escribe «margen de contribución», no «contribution margin». Sí se usan '
    'tal cual, porque son los del oficio, «food cost», «prime cost», «labor '
    'cost», «beverage cost», «delivery», «take away» y «packaging».',
    # ---- Higiene de redacción -------------------------------------------
    'No cites años anteriores a 2026 junto a precios ni a tendencias. Un año '
    'pasado sólo aparece si va con su fuente (una norma, un estudio académico '
    'o un informe fechado).',
    'No escribas «IVA incluido» sin decir el tipo, y no digas nunca que la '
    'restauración «va al 21 %»: en sala todo el consumo va al tipo reducido, '
    'bebida alcohólica incluida, y el 21 % aparece fuera de la sala y en '
    'productos concretos.',
    'No menciones el proceso de edición ni palabras como «maquetador», '
    '«prompt», «instrucciones», «guion» o «capítulo anterior del guion»: el '
    'lector compra un libro, no ve el taller. Tampoco escribas tu propio '
    'razonamiento.',
]


def C(etiqueta, ref, fmt='eur2'):
    return (etiqueta, ref, fmt)


# --------------------------------------------------------------------------
# Los 20 capítulos (SPEC §4)
# --------------------------------------------------------------------------
CAPITULOS = [
    {
        'n': 1, 'titulo': 'Para Quién es Esta Guía (y Qué no Vas a Encontrar Aquí)',
        'resumen_indice': 'nivel de partida, mapa de problema a capítulo y a herramienta, y el glosario de arranque.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Que el lector sepa en cinco minutos si esta guía le sirve, '
                    'por dónde entrar según su problema real y con qué libro '
                    'del pack se resuelve cada cosa. Y que sepa lo que NO hay '
                    'aquí, para que no lo busque.',
        'epigrafes': [
            'Qué damos por sabido y qué no',
            'Tu problema, su capítulo y su herramienta',
            'Qué hace esta guía y qué hace el Kit de Escandallos',
            'Cómo llamamos aquí a cada cosa',
        ],
        'puntos': [
            'Dejar claro que esta guía no es de apertura: no hay inversión, ni '
            'licencias, ni plan de negocio. El punto de partida es una carta '
            'que ya se está sirviendo.',
            'Explicar la división del trabajo: el Kit de Escandallos aporta las '
            'plantillas por formato de negocio y el control diario; esta guía '
            'aporta el criterio de decisión y las ocho herramientas de análisis '
            'de carta. Quien tenga los dos no duplica nada.',
            'Presentar la carta de ejemplo del pack —la misma en los ocho '
            'libros— como el hilo que recorre todo el documento, y decir '
            'expresamente que es un caso modelado, no un cliente real.',
            'Anunciar el glosario mínimo con la equivalencia de Hispanoamérica: '
            'escandallo (costeo de recetas), coste (costo), carta (menú).',
        ],
        'cifras': [
            C('Platos dados de alta en la carta de ejemplo', f'{X_MATRIZ}!Datos!D36', 'num'),
            C('Unidades vendidas al mes por la carta de ejemplo', f'{X_MATRIZ}!Datos!D32', 'num'),
            C('Ventas netas del mes de la carta de ejemplo', f'{X_MATRIZ}!Datos!I32', 'eur'),
            C('Food cost medio ponderado de la carta de ejemplo', f'{X_MATRIZ}!Datos!H32', 'pct1'),
            C('Food cost objetivo con el que trabaja el pack', f'{X_FICHA}!Ficha!D7', 'pct0'),
            C('Objetivo de prime cost en vigor en el cuadro de mando', f'{X_PRIME}!Parámetros!B11', 'pct0'),
        ],
        'sector': ['FC-BENCH-01', 'FC-PRIME-04'],
        'tablas': [{
            'titulo': 'Tu problema, el capítulo que lo trata y la herramienta que lo resuelve',
            'cabecera': ['Si tu problema es…', 'Capítulo', 'Herramienta del pack'],
            'filas': [
                ['No sé si mi food cost está bien calculado', '3 y 4', 'ficha-escandallo-base.xlsx'],
                ['Compro mucho y no sé cuánto llega al plato', '5', 'rendimiento-mermas-producto.xlsx'],
                ['Tengo que rehacer la ficha de un plato', '6', 'ficha-escandallo-base.xlsx'],
                ['Mi food cost real no cuadra con el teórico', '7', 'cuadro-de-mando-prime-cost.xlsx'],
                ['Vendo mucho y no gano', '8', 'cuadro-de-mando-prime-cost.xlsx'],
                ['No sé qué precio ponerle a un plato nuevo', '9 y 10', 'precio-objetivo-multi-metodo.xlsx'],
                ['No sé qué plato quitar de la carta', '11, 12 y 13', 'matriz-multimetodo-carta.xlsx'],
                ['Quiero montar un menú de precio fijo', '14', 'matriz-multimetodo-carta.xlsx'],
                ['El delivery me deja menos de lo que parece', '15', 'simulador-repricing-multicanal.xlsx'],
                ['La bodega no sé si gana o pierde', '16', 'carta-de-bebidas-beverage-cost.xlsx'],
                ['Me han subido el proveedor y no sé qué tocar', '18', 'precio-objetivo-multi-metodo.xlsx'],
                ['Tengo el diagnóstico y no lo aplico', '19 y 20', 'plan-accion-90-dias.xlsx'],
            ],
            'nota': 'Los ocho libros comparten la misma carta de ejemplo, así que puedes '
                    'saltar al capítulo que te interese sin perder el hilo de las cifras.',
        }],
        'prohibido': NO_COMUN + [
            'No prometas resultados («con esta guía bajarás X puntos de food '
            'cost»): la guía da método y herramientas, y el resultado depende '
            'de los datos del lector.',
            'No presentes el pack como sustituto de un asesor fiscal ni de un '
            'software de gestión.',
        ],
    },
    {
        'n': 2, 'titulo': 'Las Cuatro Cifras que Gobiernan tu Carta',
        'resumen_indice': 'food cost, margen de contribución, prime cost y ticket medio: cuál manda en cada decisión.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Que el lector deje de mirar una sola cifra. Enseñar las '
                    'cuatro que se contradicen entre sí, en qué decisión manda '
                    'cada una y por qué un food cost bajo no significa nada por '
                    'sí solo.',
        'epigrafes': [
            'Food cost porcentual: qué mide y qué no mide',
            'Margen de contribución: los euros que caen en la caja',
            'Prime cost: producto y personal en la misma línea',
            'Ticket medio y margen por cubierto',
            'Cuál manda en cada decisión',
        ],
        'puntos': [
            'La tesis del capítulo: el porcentaje ordena, el euro paga. Un plato '
            'con food cost del 20 % que deja pocos euros por unidad puede ser '
            'peor negocio que uno con food cost alto que deja muchos.',
            'Explicar que el margen de contribución medio ponderado de la carta '
            'de ejemplo y su food cost medio ponderado se calculan sobre las '
            'unidades REALMENTE vendidas, no sobre la media simple de los '
            'platos: la media simple da un número que no existe.',
            'Introducir el prime cost como la cifra que impide engañarse: se '
            'puede bajar el food cost subiendo el trabajo de cocina, y el '
            'ahorro reaparece en la nómina.',
            'Cerrar con la regla de uso: para retirar o mantener un plato manda '
            'el margen de contribución; para negociar compras manda el food '
            'cost; para saber si el negocio aguanta manda el prime cost.',
        ],
        'cifras': [
            C('Food cost medio ponderado de la carta de ejemplo', f'{X_MATRIZ}!Datos!H32', 'pct1'),
            C('Margen de contribución medio ponderado de la carta', f'{X_MATRIZ}!Datos!G32'),
            C('Unidades vendidas al mes por la carta', f'{X_MATRIZ}!Datos!D32', 'num'),
            C('Ventas netas del mes de la carta', f'{X_MATRIZ}!Datos!I32', 'eur'),
            C('Ventas netas anuales del cuadro de mando', f'{X_PRIME}!Mensual!D17', 'eur'),
            C('Coste de materia prima sobre ventas del año', f'{X_PRIME}!Mensual!I17', 'pct1'),
            C('Labor cost del año', f'{X_PRIME}!Mensual!M17', 'pct1'),
            C('Prime cost del año', f'{X_PRIME}!Mensual!N17', 'pct1'),
            C('Margen tras prime cost del año', f'{X_PRIME}!Mensual!P17', 'eur'),
            C('Ticket medio sin IVA en el mes 0 del plan de 90 días', f'{X_PLAN90}!KPI de Seguimiento!B7', 'num1'),
            C('Margen de contribución por cubierto en el mes 0', f'{X_PLAN90}!KPI de Seguimiento!B8', 'num1'),
        ],
        'sector': ['FC-BENCH-01', 'FC-BENCH-03', 'FC-PRIME-04'],
        'tablas': [
            {
                'titulo': 'El cuadro de mando mensual: food cost, labor cost y prime cost (cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»)',
                'src': (X_PRIME, 'Mensual'),
                'cols': [('Mes', 'A', 'txt'), ('Ventas netas (€)', 'D', 'eur'),
                         ('Food cost (%)', 'I', 'pct1'), ('Labor cost (%)', 'M', 'pct1'),
                         ('Prime cost (%)', 'N', 'pct1'), ('Objetivo (%)', 'O', 'pct1'),
                         ('Lectura', 'R', 'txt')],
                'filas': (5, 17),
                'nota': 'La última fila es el total del año y sus porcentajes son ponderados, '
                        'no la media de los doce meses: un mes flojo pesa lo que factura, no '
                        'una doceava parte.',
            },
            {
                'titulo': 'Las tres familias de la carta de ejemplo (matriz-multimetodo-carta.xlsx, hoja «Datos»)',
                'src': (X_MATRIZ, 'Datos'),
                'cols': [('Familia', 'B', 'txt'), ('Platos', 'C', 'num'),
                         ('Uds vendidas', 'E', 'num'), ('Mix sobre la carta (%)', 'F', 'pct1'),
                         ('MC medio ponderado (€)', 'G', 'eur2'),
                         ('Food cost medio ponderado (%)', 'H', 'pct1'),
                         ('Ventas netas del mes (€)', 'I', 'eur')],
                'filas': (40, 42),
            },
        ],
        'prohibido': NO_COMUN + [
            'No digas que el food cost «debe ser» un número concreto: da el '
            'rango con su fuente y explica de qué depende.',
            'No confundas margen de contribución con beneficio: el margen de '
            'contribución no ha pagado todavía ni el personal ni el alquiler, y '
            'hay que decirlo expresamente.',
        ],
    },
    {
        'n': 3, 'titulo': 'IVA, Base Imponible y el Error que Invalida tu Food Cost',
        'resumen_indice': 'la matriz de IVA por canal y tipo de producto, y por qué el porcentaje se calcula sobre la venta neta.',
        'palabras': 1700, 'bloques': 3,
        'objetivo': 'Cerrar de una vez el error más caro y más común: calcular '
                    'el food cost sobre el precio que ve el cliente. Y dejar la '
                    'matriz fiscal completa, con los tres canales y los tres '
                    'tipos de producto, para que el lector sepa qué tipo aplica '
                    'a cada línea de su ticket.',
        'epigrafes': [
            'Sobre qué número se calcula el food cost',
            'La matriz de IVA repercutido: tres canales por tres tipos de producto',
            'En sala va todo al tipo reducido, bebida alcohólica incluida',
            'Sin servicio hay entrega de bienes: qué se va al tipo general',
            'El mismo plato con IVA y sin IVA: cuántos puntos de food cost te inventas',
            'Por qué el tipo vive en una celda y no dentro de la fórmula',
        ],
        'puntos': [
            'La tesis: el food cost se calcula sobre la BASE IMPONIBLE, no sobre '
            'el precio de carta. Dividir el coste entre el precio con IVA infla '
            'artificialmente el numerador respecto del denominador y da un food '
            'cost más bajo del real, que es la peor dirección posible del error.',
            'Explicar el fundamento de la matriz: en sala hay un SERVICIO de '
            'hostelería y por eso todo el consumo va al tipo reducido, incluida '
            'la bebida alcohólica; sin servicio hay una ENTREGA DE BIENES y '
            'entonces sí juegan las exclusiones del alcohol y de las bebidas '
            'con azúcares o edulcorantes añadidos.',
            'Advertir de que el mismo botellín de cerveza lleva un tipo en la '
            'barra y otro si el cliente se lo lleva: no es una rareza, es la '
            'consecuencia de que en un caso se presta un servicio y en el otro '
            'se entrega un bien.',
            'Explicar la consecuencia operativa: si la carta de delivery es la '
            'misma que la de sala, el margen por canal no es el mismo, y eso se '
            'trabaja en el capítulo del multicanal.',
            'Cerrar con la razón de ingeniería: los tipos están en celdas '
            'editables con nota, y las fórmulas los leen con INDEX y MATCH. Si '
            'mañana cambia un tipo, se cambia la celda y el libro entero se '
            'recalcula, sin tocar una sola fórmula.',
        ],
        'cifras': [
            C('IVA repercutido en sala, comida', f'{X_MULTI}!Parámetros!B6', 'pct0'),
            C('IVA repercutido en sala, bebida alcohólica', f'{X_MULTI}!Parámetros!D6', 'pct0'),
            C('IVA repercutido en delivery, comida', f'{X_MULTI}!Parámetros!B8', 'pct0'),
            C('IVA repercutido en delivery, refresco azucarado', f'{X_MULTI}!Parámetros!C8', 'pct0'),
            C('IVA repercutido en delivery, bebida alcohólica', f'{X_MULTI}!Parámetros!D8', 'pct0'),
            C('Coste por ración del plato de la ficha, sin IVA', f'{X_FICHA}!Ficha!E33'),
            C('PVP actual en carta del plato, sin IVA', f'{X_FICHA}!Ficha!E37'),
            C('PVP actual del plato con IVA', f'{X_FICHA}!Ficha!E38'),
            C('Food cost real del plato con el PVP actual', f'{X_FICHA}!Ficha!E39', 'pct1'),
            C('Food cost si contases el IVA soportado como coste', f'{X_FICHA}!Ficha!E47', 'pct1'),
            C('IVA soportado total de la ficha', f'{X_FICHA}!Ficha!E45'),
            C('Coste de la ficha con el IVA soportado dentro', f'{X_FICHA}!Ficha!E46'),
            C('Margen de contribución del plato con el PVP actual', f'{X_FICHA}!Ficha!E40'),
        ],
        'sector': ['FC-IVA-01', 'FC-IVA-02', 'FC-IVA-03', 'FC-IVA-04', 'FC-IVA-07', 'FC-IVA-08'],
        'tablas': [
            {
                'titulo': 'La matriz de IVA repercutido: canal por tipo de producto (simulador-repricing-multicanal.xlsx, hoja «Parámetros»)',
                'src': (X_MULTI, 'Parámetros'),
                'cols': [('Canal', 'A', 'txt'), ('Comida', 'B', 'pct0'),
                         ('Refresco o bebida azucarada', 'C', 'pct0'),
                         ('Bebida alcohólica', 'D', 'pct0')],
                'filas': (6, 8),
                'nota': 'Las nueve casillas son editables y llevan su nota con el artículo que '
                        'las sostiene. Si trabajas fuera de España, cambias las nueve y el resto '
                        'del libro se recalcula solo.',
            },
            {
                'titulo': 'El IVA soportado no es coste: qué pasa si lo metes dentro (ficha-escandallo-base.xlsx, hoja «Ficha»)',
                'src': (X_FICHA, 'Ficha'),
                'cols': [('Concepto', 'B', 'txt'), ('Valor', 'E', 'eur2')],
                'filas': (45, 47),
                'nota': 'El IVA de las compras se deduce en la declaración: es tesorería, no '
                        'coste. Meterlo en el escandallo sube el food cost sin que nadie haya '
                        'gastado un euro de más.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO escribas que la restauración tributa al tipo general: en sala '
            'todo el consumo va al tipo reducido y el general aparece fuera de '
            'la sala. Escribir lo contrario es el error que este capítulo viene '
            'a corregir.',
            'NO digas que el alcohol lleva siempre el tipo general: en sala no. '
            'La frase correcta distingue el canal.',
            'NO des consejo fiscal ni digas «puedes facturar al tipo X»: se '
            'explica la regla y se remite a la asesoría para el caso concreto.',
            'NO cites un número de artículo que no esté en los datos del sector '
            'que te doy, y cita siempre la norma con su nombre completo la '
            'primera vez.',
        ],
    },
    {
        'n': 4, 'titulo': 'El Coste Real de Compra: 4 %, 10 % y 21 % en el Mismo Albarán',
        'resumen_indice': 'los tres tipos de IVA soportado, qué producto lleva cada uno y por qué el IVA de compra no es coste.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Que el lector sepa leer un albarán con los tres tipos '
                    'dentro, entienda que el IVA soportado se deduce y no entra '
                    'en el escandallo, y sepa qué productos concretos bajan al '
                    'tipo superreducido.',
        'epigrafes': [
            'Los tres tipos que conviven en la misma caja de la compra',
            'La lista cerrada del tipo superreducido',
            'Un albarán de ejemplo, línea a línea',
            'El IVA soportado es tesorería: dónde entra y dónde no',
        ],
        'puntos': [
            'La lista del tipo superreducido es CERRADA: lo que no está en ella '
            'y no está excluido va al tipo reducido ordinario. Enumerarla '
            'entera y señalar la incorporación del aceite de oliva con su norma '
            'y su fecha de efectos.',
            'Explicar el caso del packaging: la caja del delivery no es un '
            'alimento y por eso lleva el tipo general, aunque el plato que va '
            'dentro lleve el reducido.',
            'Dejar clara la regla del escandallo: se cuesta con el precio SIN '
            'IVA. El IVA de compra se deduce, así que meterlo en la ficha es '
            'contar dos veces.',
            'Explicar cuándo esto deja de ser cierto: si el negocio no puede '
            'deducirse el IVA soportado, ese IVA sí es coste. Decir que es un '
            'caso a consultar con la asesoría, sin entrar en el régimen.',
        ],
        'cifras': [
            C('Tipo de IVA soportado superreducido', f'{X_FICHA}!Albarán e IVA soportado!A5', 'pct0'),
            C('Tipo de IVA soportado reducido', f'{X_FICHA}!Albarán e IVA soportado!A6', 'pct0'),
            C('Tipo de IVA soportado general', f'{X_FICHA}!Albarán e IVA soportado!A7', 'pct0'),
            C('Base imponible total del albarán de ejemplo', f'{X_FICHA}!Albarán e IVA soportado!F18'),
            C('Cuota de IVA total del albarán de ejemplo', f'{X_FICHA}!Albarán e IVA soportado!H18'),
            C('Total con IVA del albarán de ejemplo', f'{X_FICHA}!Albarán e IVA soportado!I18'),
            C('IVA soportado total de la ficha de escandallo', f'{X_FICHA}!Ficha!E45'),
            C('Coste por ración sin IVA', f'{X_FICHA}!Ficha!E33'),
            C('Coste por ración con el IVA soportado dentro', f'{X_FICHA}!Ficha!E46'),
            C('Food cost correcto del plato', f'{X_FICHA}!Ficha!E39', 'pct1'),
            C('Food cost erróneo contando el IVA como coste', f'{X_FICHA}!Ficha!E47', 'pct1'),
        ],
        'sector': ['FC-IVA-05', 'FC-IVA-06', 'FC-IVA-07'],
        'tablas': [
            {
                'titulo': 'Qué compra lleva cada tipo de IVA soportado (ficha-escandallo-base.xlsx, hoja «Albarán e IVA soportado»)',
                'src': (X_FICHA, 'Albarán e IVA soportado'),
                'cols': [('Tipo', 'A', 'pct0'), ('Qué compra lleva este tipo', 'B', 'txt')],
                'filas': (5, 7),
            },
            {
                'titulo': 'Un albarán con los tres tipos dentro, línea a línea (ficha-escandallo-base.xlsx, hoja «Albarán e IVA soportado»)',
                'src': (X_FICHA, 'Albarán e IVA soportado'),
                'cols': [('#', 'A', 'num'), ('Producto', 'B', 'txt'),
                         ('Cantidad', 'C', 'num1'), ('Unidad', 'D', 'txt'),
                         ('Precio/ud sin IVA (€)', 'E', 'eur2'),
                         ('Base imponible (€)', 'F', 'eur2'),
                         ('Tipo (%)', 'G', 'pct0'), ('Cuota de IVA (€)', 'H', 'eur2'),
                         ('Total con IVA (€)', 'I', 'eur2')],
                'filas': (11, 18),
                'nota': 'La columna que entra en el escandallo es la base imponible. La cuota de '
                        'IVA de este albarán se deduce en la declaración del trimestre.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO digas que el aceite de oliva está en la letra f) de la lista: es '
            'la g). La f) son frutas, verduras, hortalizas, legumbres, '
            'tubérculos y cereales.',
            'NO amplíes la lista del tipo superreducido con productos que no '
            'estén en ella (aceite de girasol, carne, pescado, conservas): esos '
            'van al reducido ordinario.',
            'NO expliques cómo se rellena el modelo 303 ni des instrucciones de '
            'liquidación: eso es de la asesoría.',
        ],
    },
    {
        'n': 5, 'titulo': 'Del Bruto al Neto: Merma, Rendimiento y el Test que Sustituye a la Tabla',
        'resumen_indice': 'despiece, cocción y subproductos: cómo medir tu propia merma y cuánto cuesta de verdad el kilo limpio.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Sustituir la tabla de mermas copiada de internet por una '
                    'medición propia, y enseñar a calcular el coste del kilo '
                    'limpio contando lo que se aprovecha del recorte.',
        'epigrafes': [
            'Las tres mermas que no son la misma: despiece, cocción y desperdicio',
            'El protocolo del test de rendimiento, paso a paso',
            'Qué pasa con el subproducto: cabezas, espinas y recortes',
            'El coste del kilo limpio y el factor de corrección',
            'Tu tabla de mermas: cuándo puedes dejar de usar la referencia',
        ],
        'puntos': [
            'La tesis: la merma no es un porcentaje del sector, es un dato de tu '
            'proveedor, de tu calibre y de tu manera de limpiar. Dos cocinas con '
            'el mismo pescado tienen rendimientos distintos.',
            'Explicar el protocolo con la báscula: se pesa el bruto, se limpia, '
            'se pesa el limpio y se pesa el aprovechable por separado. Tres '
            'medidas de la misma pieza, el mismo día.',
            'Explicar el factor de corrección como el número que se lleva a la '
            'ficha: es el inverso del rendimiento y es lo que convierte la '
            'cantidad neta de la receta en la cantidad que hay que comprar.',
            'Explicar la decisión económica del subproducto: aprovechar la cabeza '
            'o la espina sólo compensa si el valor de uso que le asignas es '
            'real, es decir, si ese fondo sustituye a algo que ibas a comprar.',
            'La merma de cocción es una merma DISTINTA y se aplica encima de la '
            'del despiece: quien sólo aplica una de las dos está costeando de '
            'menos.',
        ],
        'cifras': [
            C('Productos medidos en el test de rendimiento', f'{X_MERMA}!Test de Rendimiento!E23', 'num'),
            C('Peso bruto total comprado en los tests', f'{X_MERMA}!Test de Rendimiento!E24', 'num2'),
            C('Peso limpio total obtenido', f'{X_MERMA}!Test de Rendimiento!E25', 'num2'),
            C('Rendimiento medio ponderado de los tests', f'{X_MERMA}!Test de Rendimiento!E26', 'pct1'),
            C('Merma media ponderada de los tests', f'{X_MERMA}!Test de Rendimiento!E27', 'pct1'),
            C('Coste total de compra de los tests', f'{X_MERMA}!Test de Rendimiento!E28'),
            C('Valor de uso de los subproductos', f'{X_MERMA}!Test de Rendimiento!E29'),
            C('Rendimiento de la lubina entera', f'{X_MERMA}!Test de Rendimiento!H6', 'pct1'),
            C('Coste neto por kilo limpio de la lubina, sin aprovechar', f'{X_MERMA}!Test de Rendimiento!M6'),
            C('Coste neto por kilo limpio de la lubina, aprovechando', f'{X_MERMA}!Test de Rendimiento!N6'),
            C('Sobrecoste de la lubina sobre el precio del kilo bruto', f'{X_MERMA}!Test de Rendimiento!P6'),
            C('Rendimiento de la alcachofa', f'{X_MERMA}!Test de Rendimiento!H12', 'pct1'),
            C('Rendimiento del mejillón con concha', f'{X_MERMA}!Test de Rendimiento!H14', 'pct1'),
            C('Ahorro por aprovechar las cabezas de la gamba', f'{X_MERMA}!Test de Rendimiento!O15'),
            C('Pérdida por cocción del pollo de corral al horno', f'{X_MERMA}!Merma de Cocción!G7', 'pct1'),
            C('Pérdida media por cocción de las pruebas registradas', f'{X_MERMA}!Merma de Cocción!E19', 'pct1'),
            C('Categorías con medición propia en tu tabla de mermas', f'{X_MERMA}!Mi Tabla de Mermas!E26', 'num'),
            C('Categorías que aún usan la referencia', f'{X_MERMA}!Mi Tabla de Mermas!E27', 'num'),
        ],
        'sector': ['FC-MERMA-01', 'FC-MERMA-02'],
        'tablas': [
            {
                'titulo': 'Diez tests de rendimiento con su coste del kilo limpio (rendimiento-mermas-producto.xlsx, hoja «Test de Rendimiento»)',
                'src': (X_MERMA, 'Test de Rendimiento'),
                'cols': [('Producto', 'B', 'txt'), ('Peso bruto (kg)', 'C', 'num2'),
                         ('Precio/kg bruto (€)', 'D', 'eur2'), ('Peso limpio (kg)', 'E', 'num2'),
                         ('Rendimiento (%)', 'H', 'pct1'), ('Merma (%)', 'I', 'pct1'),
                         ('Factor de corrección', 'J', 'num2'),
                         ('Coste neto sin aprovechar (€/kg)', 'M', 'eur2'),
                         ('Coste neto aprovechando (€/kg)', 'N', 'eur2')],
                'filas': (6, 20),
            },
            {
                'titulo': 'Tu tabla de mermas: referencia orientativa y medición propia (rendimiento-mermas-producto.xlsx, hoja «Mi Tabla de Mermas»)',
                'src': (X_MERMA, 'Mi Tabla de Mermas'),
                'cols': [('Categoría', 'B', 'txt'), ('Referencia mínima (%)', 'C', 'pct1'),
                         ('Referencia máxima (%)', 'D', 'pct1'),
                         ('Tu merma medida (%)', 'F', 'pct1'),
                         ('Merma que usas (%)', 'G', 'pct1'),
                         ('De dónde sale el dato', 'H', 'txt')],
                'filas': (6, 23),
                'nota': 'La columna «Merma que usas» toma tu medición en cuanto la escribes y, '
                        'mientras no la tengas, se queda con la referencia. La última columna te '
                        'dice siempre de dónde viene el número que está costeando tus platos.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO des una tabla de mermas por categoría con porcentajes concretos '
            'atribuidos a una autoridad: los rangos que tienes en los datos del '
            'sector están marcados como orientativos y SIN fuente citable, así '
            'que se presentan como punto de partida provisional y se dice '
            'expresamente que el número bueno es el que mida el lector.',
            'NO escribas ningún porcentaje de merma por producto que no esté en '
            'la lista de cifras o en la tabla que acompaña al capítulo.',
            'NO mezcles merma de despiece con merma de cocción en el mismo '
            'porcentaje: son dos números y se aplican uno detrás de otro.',
        ],
    },
    {
        'n': 6, 'titulo': 'La Ficha de Escandallo que Aguanta una Auditoría',
        'resumen_indice': 'cantidad neta, merma, cantidad bruta, coste por ración y precio objetivo, línea a línea.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Dejar una ficha que cualquiera pueda auditar: cada línea '
                    'con su cantidad neta, su merma y su precio sin IVA, y un '
                    'resumen que enlaza el coste por ración con el precio de '
                    'venta objetivo y con el que hay hoy en la carta.',
        'epigrafes': [
            'Qué tiene que llevar una línea de escandallo para ser auditable',
            'La merma entra dividiendo, no multiplicando',
            'Del coste por ración al precio de venta objetivo',
            'Comparar el precio objetivo con el que hay hoy en la carta',
            'Errores que invalidan una ficha',
        ],
        'puntos': [
            'La regla de la cantidad bruta: es la cantidad neta dividida entre '
            'uno menos la merma. Multiplicar por el porcentaje de merma es el '
            'error clásico y siempre se queda corto.',
            'Explicar por qué se guarda el precio SIN IVA en la línea y el tipo '
            'de IVA de compra en su propia columna: así la ficha sirve para '
            'costear y para conciliar el albarán.',
            'Explicar el campo «raciones que salen de esta ficha»: costear una '
            'elaboración entera y dividir es lo que evita el redondeo de '
            'costear a ojo la ración.',
            'La comparación entre el precio de venta objetivo y el actual es la '
            'que produce la decisión: la ficha no dice sólo cuánto cuesta, dice '
            'cuánto habría que subir.',
            'Cross-sell explícito y honesto: si el lector necesita las plantillas '
            'por formato de negocio, están en el Kit de Escandallos; esta ficha '
            'es la base y es suficiente para trabajar el criterio de esta guía.',
        ],
        'cifras': [
            C('Plato de la ficha de ejemplo', f'{X_FICHA}!Ficha!D4', 'txt'),
            C('Raciones que salen de la ficha', f'{X_FICHA}!Ficha!D6', 'num'),
            C('Food cost objetivo de la ficha', f'{X_FICHA}!Ficha!D7', 'pct0'),
            C('Cantidad neta por ración de la primera línea', f'{X_FICHA}!Ficha!D10', 'num2'),
            C('Merma de la primera línea', f'{X_FICHA}!Ficha!F10', 'pct1'),
            C('Cantidad bruta a comprar de la primera línea', f'{X_FICHA}!Ficha!H10', 'num2'),
            C('Coste sin IVA de la primera línea', f'{X_FICHA}!Ficha!I10'),
            C('Cantidad bruta del boniato', f'{X_FICHA}!Ficha!H12', 'num2'),
            C('Coste total de la ficha, sin IVA', f'{X_FICHA}!Ficha!E32'),
            C('Coste por ración, sin IVA', f'{X_FICHA}!Ficha!E33'),
            C('PVP objetivo sin IVA', f'{X_FICHA}!Ficha!E34'),
            C('PVP objetivo con IVA', f'{X_FICHA}!Ficha!E36'),
            C('PVP actual en carta, sin IVA', f'{X_FICHA}!Ficha!E37'),
            C('Food cost real con el PVP actual', f'{X_FICHA}!Ficha!E39', 'pct1'),
            C('Margen de contribución con el PVP actual', f'{X_FICHA}!Ficha!E40'),
            C('Diferencia entre el PVP objetivo y el actual', f'{X_FICHA}!Ficha!E41'),
            C('Subida necesaria sobre el PVP actual', f'{X_FICHA}!Ficha!E42', 'pct1'),
        ],
        'sector': [],
        'tablas': [
            {
                'titulo': 'Las líneas de la ficha, con la merma dentro (ficha-escandallo-base.xlsx, hoja «Ficha»)',
                'src': (X_FICHA, 'Ficha'),
                'cols': [('#', 'A', 'num'), ('Ingrediente', 'B', 'txt'),
                         ('Unidad', 'C', 'txt'), ('Cantidad neta/ración', 'D', 'num2'),
                         ('Precio/ud sin IVA (€)', 'E', 'eur2'), ('Merma (%)', 'F', 'pct1'),
                         ('Cantidad bruta a comprar', 'H', 'num2'),
                         ('Coste sin IVA (€)', 'I', 'eur2')],
                'filas': (10, 29),
            },
            {
                'titulo': 'El resumen de la ficha: del coste por ración al precio de carta (ficha-escandallo-base.xlsx, hoja «Ficha»)',
                'src': (X_FICHA, 'Ficha'),
                'cols': [('Concepto', 'B', 'txt'), ('Valor', 'E', 'eur2')],
                'filas': (32, 42),
                'nota': 'Las filas marcadas con «(%)» son porcentajes; el resto, euros. El precio '
                        'objetivo sale de dividir el coste por ración entre el food cost '
                        'objetivo, que es una celda editable y no un número dentro de la fórmula.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO escribas la fórmula de la cantidad bruta como una multiplicación '
            'por el porcentaje de merma: es una división entre uno menos la '
            'merma, y el capítulo existe para corregir precisamente eso.',
            'NO des el precio de ningún ingrediente que no esté en la tabla o en '
            'la lista de cifras.',
            'NO presentes el Kit de Escandallos como imprescindible para usar '
            'esta guía: es complementario y hay que decirlo así.',
        ],
    },
    {
        'n': 7, 'titulo': 'Food Cost Teórico vs Real: Dónde se Escapa el Dinero',
        'resumen_indice': 'el consumo real con stock inicial, compras y stock final, y las cuatro causas de la desviación.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Enseñar a calcular el food cost REAL del periodo y a leer '
                    'la diferencia con el teórico como un diagnóstico, no como '
                    'un error de la hoja de cálculo.',
        'epigrafes': [
            'Los dos food cost y por qué nunca coinciden del todo',
            'El consumo real: stock inicial, compras y stock final',
            'Las cuatro causas de la desviación',
            'El protocolo semanal que la mantiene bajo control',
        ],
        'puntos': [
            'La fórmula del consumo real: stock inicial más compras menos stock '
            'final. Sin inventario no hay food cost real; hay food cost de '
            'compras, que es otra cosa y engaña cuando el almacén sube o baja.',
            'Las cuatro causas ordenadas por frecuencia: porciones que no se '
            'ajustan a la ficha, merma y caducidad, invitaciones y personal, y '
            'precios de compra que se movieron sin que nadie reescandallara.',
            'Explicar que una desviación estable no es un problema urgente y una '
            'desviación que crece sí: lo que se vigila es la tendencia, no el '
            'valor absoluto de un mes.',
            'Protocolo semanal realista: inventario corto de las diez '
            'referencias que más pesan, no inventario completo. Y remitir al '
            'dashboard del Kit de Escandallos para quien quiera el seguimiento '
            'diario.',
        ],
        'cifras': [
            C('Compras del año en el cuadro de mando', f'{X_PRIME}!Mensual!F17', 'eur'),
            C('Consumo real de materia prima del año', f'{X_PRIME}!Mensual!H17', 'eur'),
            C('Ventas netas totales del año', f'{X_PRIME}!Mensual!D17', 'eur'),
            C('Coste de materia prima sobre ventas del año', f'{X_PRIME}!Mensual!I17', 'pct1'),
            C('Food cost objetivo del cuadro de mando', f'{X_PRIME}!Parámetros!B21', 'pct0'),
            C('Food cost real de enero', f'{X_PRIME}!Mensual!I5', 'pct1'),
            C('Ventas netas totales de enero', f'{X_PRIME}!Mensual!D5', 'eur'),
            C('Food cost teórico de la carta de ejemplo', f'{X_MATRIZ}!Datos!H32', 'pct1'),
            C('Food cost objetivo de la ficha de escandallo', f'{X_FICHA}!Ficha!D7', 'pct0'),
        ],
        'sector': ['FC-BENCH-01'],
        'tablas': [{
            'titulo': 'Del stock al consumo: el food cost real mes a mes (cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»)',
            'src': (X_PRIME, 'Mensual'),
            'cols': [('Mes', 'A', 'txt'), ('Ventas netas (€)', 'D', 'eur'),
                     ('Stock inicial (€)', 'E', 'eur'), ('Compras (€)', 'F', 'eur'),
                     ('Stock final (€)', 'G', 'eur'), ('Consumo (€)', 'H', 'eur'),
                     ('Food cost (%)', 'I', 'pct1')],
            'filas': (5, 17),
            'nota': 'Compárense las columnas de compras y de consumo: cuando difieren, lo que '
                    'ha cambiado es el almacén, y usar las compras como si fueran el consumo '
                    'habría dado un food cost falso ese mes.',
        }],
        'prohibido': NO_COMUN + [
            'NO des un porcentaje de desviación «aceptable» entre teórico y real: '
            'no hay fuente para eso. Se explica cómo se lee la tendencia.',
            'NO desarrolles aquí la plantilla de control semanal: el capítulo '
            'explica el método y remite al Kit de Escandallos, que ya la trae.',
            'NO atribuyas la desviación al robo como causa principal: las cuatro '
            'causas que se explican son las de la lista y en ese orden.',
        ],
    },
]

CAPITULOS += [
    {
        'n': 8, 'titulo': 'Prime Cost: la Métrica que Mide la Salud del Negocio',
        'resumen_indice': 'producto más personal en una sola cifra, con el umbral español del 65 % y el del 55 % en barra.',
        'palabras': 1600, 'bloques': 2,
        'objetivo': 'Sacar al lector del food cost como métrica única. Enseñar '
                    'el prime cost con el umbral que aplica a su formato y '
                    'mostrar el caso que más engaña: food cost impecable con '
                    'coste de personal desbocado.',
        'epigrafes': [
            'Qué suma el prime cost y por qué se miran juntos',
            'El umbral español: 30 % de producto y 30-35 % de personal',
            'Servicio en mesa o barra: dos objetivos distintos',
            'El coste de personal es el bruto más la Seguridad Social',
            'Leer el cuadro de mando: el mes bueno, el mes malo y el año',
        ],
        'puntos': [
            'La tesis del capítulo: el food cost y el coste de personal son '
            'vasos comunicantes. Elaborar más en casa baja el food cost y sube '
            'las horas; comprar elaborado hace lo contrario. Sólo el prime cost '
            've las dos cosas a la vez.',
            'Explicar la estructura española de referencia —en torno al 30 % de '
            'producto más un 30-35 % de personal con servicio integrado en '
            'mesa— y de ahí el objetivo del pack, que está en celda editable y '
            'no dentro de la fórmula.',
            'Explicar por qué el formato de barra o autoservicio tolera un '
            'umbral más bajo: su coste de personal es estructuralmente menor, '
            'así que el mismo prime cost significa cosas distintas.',
            'Insistir en que el coste de personal que entra aquí lleva la '
            'Seguridad Social a cargo de la empresa: comparar un labor cost '
            'calculado sobre brutos con un objetivo pensado para coste total es '
            'compararse con una vara que no es la suya.',
            'Contrastar el umbral español con la referencia estadounidense del '
            '60 %, citándola como lo que es: una referencia de otro mercado, '
            'con otra estructura de personal.',
            'Cerrar con el cross-sell honesto: quien vea el labor cost fuera de '
            'sitio tiene el Kit de Gestión de Personal para trabajar cuadrantes '
            'y horas; esta guía se queda en el diagnóstico.',
        ],
        'cifras': [
            C('Tipo de negocio elegido en el cuadro de mando', f'{X_PRIME}!Parámetros!B5', 'txt'),
            C('Objetivo de prime cost con servicio en mesa', f'{X_PRIME}!Parámetros!B8', 'pct0'),
            C('Objetivo de prime cost en barra o autoservicio', f'{X_PRIME}!Parámetros!B9', 'pct0'),
            C('Objetivo de prime cost en vigor', f'{X_PRIME}!Parámetros!B11', 'pct0'),
            C('Seguridad Social a cargo de la empresa', f'{X_PRIME}!Parámetros!B20', 'pct0'),
            C('Salarios brutos del año', f'{X_PRIME}!Mensual!J17', 'eur'),
            C('Otros costes de personal del año', f'{X_PRIME}!Mensual!K17', 'eur'),
            C('Coste de personal con Seguridad Social del año', f'{X_PRIME}!Mensual!L17', 'eur'),
            C('Coste de materia prima sobre ventas del año', f'{X_PRIME}!Mensual!I17', 'pct1'),
            C('Labor cost del año', f'{X_PRIME}!Mensual!M17', 'pct1'),
            C('Prime cost del año', f'{X_PRIME}!Mensual!N17', 'pct1'),
            C('Margen tras prime cost del año', f'{X_PRIME}!Mensual!P17', 'eur'),
            C('Margen tras prime cost del año sobre ventas', f'{X_PRIME}!Mensual!Q17', 'pct1'),
            C('Prime cost del mejor mes (abril)', f'{X_PRIME}!Mensual!N8', 'pct1'),
            C('Prime cost del peor mes (agosto)', f'{X_PRIME}!Mensual!N12', 'pct1'),
            C('Lectura del prime cost de agosto', f'{X_PRIME}!Mensual!R12', 'txt'),
        ],
        'sector': ['FC-PRIME-01', 'FC-PRIME-02', 'FC-PRIME-03', 'FC-PRIME-04'],
        'tablas': [
            {
                'titulo': 'El objetivo de prime cost por tipo de negocio (cuadro-de-mando-prime-cost.xlsx, hoja «Parámetros»)',
                'src': (X_PRIME, 'Parámetros'),
                'cols': [('Tipo de negocio', 'A', 'txt'),
                         ('Objetivo de prime cost (%)', 'B', 'pct0')],
                'filas': (8, 9),
                'nota': 'Las dos casillas son editables: si tu convenio, tu mix o tu formato '
                        'piden otro umbral, se escribe ahí y el semáforo de los doce meses se '
                        'recalcula contra el tuyo.',
            },
            {
                'titulo': 'Producto y personal en la misma tabla, mes a mes (cuadro-de-mando-prime-cost.xlsx, hoja «Mensual»)',
                'src': (X_PRIME, 'Mensual'),
                'cols': [('Mes', 'A', 'txt'),
                         ('Coste de personal con SS (€)', 'L', 'eur'),
                         ('Food cost (%)', 'I', 'pct1'), ('Labor cost (%)', 'M', 'pct1'),
                         ('Prime cost (%)', 'N', 'pct1'), ('Objetivo (%)', 'O', 'pct1'),
                         ('Margen tras prime cost (€)', 'P', 'eur')],
                'filas': (5, 17),
            },
        ],
        'prohibido': NO_COMUN + [
            'NO presentes el 60 % como el umbral español: es la referencia '
            'estadounidense y hay que decirlo dentro de la misma frase.',
            'NO afirmes que un prime cost por encima del objetivo significa que '
            'el negocio pierde dinero: significa que le queda menos margen para '
            'pagar alquiler, suministros y estructura. Esa es la frase.',
            'NO des ningún porcentaje de alquiler, suministros o gastos '
            'generales que no esté en los datos del sector.',
        ],
    },
    {
        'n': 9, 'titulo': 'Cuatro Formas de Poner Precio a un Plato',
        'resumen_indice': 'factor sobre el coste, margen objetivo en euros, precio de mercado y valor percibido.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Quitarle al lector la idea de que hay una fórmula. Enseñar '
                    'los cuatro métodos, el food cost que resulta de cada uno y '
                    'el criterio para elegir método plato a plato.',
        'epigrafes': [
            'Método A: factor sobre el coste, y dónde se rompe',
            'Método B: margen objetivo en euros',
            'Método C: precio de mercado de tu zona',
            'Método D: valor percibido',
            'Qué método le toca a cada plato',
        ],
        'puntos': [
            'La tesis: el factor sobre el coste arruina los platos de coste alto. '
            'Aplicado al chuletón de la carta de ejemplo, el precio que sale es '
            'inservible, y ese es el argumento del capítulo, no una anécdota.',
            'Explicar el método del margen en euros como el remedio del anterior: '
            'en los platos de producto caro se fija cuánto se quiere ganar por '
            'ración y el porcentaje sale de ahí, aunque quede feo.',
            'Explicar que los métodos C y D no calculan el precio, lo IMPONEN '
            'desde fuera, y que lo que devuelve la hoja en esos casos es el food '
            'cost que te queda al aceptar ese precio: la pregunta cambia de '
            '«cuánto cobro» a «puedo permitírmelo».',
            'Enseñar a leer el reparto de métodos de la carta de ejemplo: no hay '
            'un método ganador, hay una cartera de métodos.',
            'Señalar el caso de las croquetas —el precio actual está por encima '
            'del que sale por factor— para explicar que un plato puede estar '
            'bien cobrado y que el método sólo confirma el suelo.',
        ],
        'cifras': [
            C('Food cost objetivo global de la hoja de precios', f'{X_PRECIO}!Por Plato!E5', 'pct0'),
            C('Tipo de IVA de restauración en sala', f'{X_PRECIO}!Por Plato!E6', 'pct0'),
            C('PVP del chuletón por el método del factor', f'{X_PRECIO}!Por Plato!K20'),
            C('PVP del chuletón por margen objetivo', f'{X_PRECIO}!Por Plato!L20'),
            C('PVP elegido para el chuletón', f'{X_PRECIO}!Por Plato!Q20'),
            C('Food cost final del chuletón', f'{X_PRECIO}!Por Plato!T20', 'pct1'),
            C('PVP actual del chuletón en carta', f'{X_PRECIO}!Por Plato!V20'),
            C('PVP de las croquetas por el método del factor', f'{X_PRECIO}!Por Plato!K9'),
            C('PVP actual de las croquetas en carta', f'{X_PRECIO}!Por Plato!V9'),
            C('Diferencia de las croquetas con su PVP actual', f'{X_PRECIO}!Por Plato!W9'),
            C('Platos con precio calculado', f'{X_PRECIO}!Por Plato!E36', 'num'),
            C('Platos dentro del objetivo', f'{X_PRECIO}!Por Plato!E37', 'num'),
            C('Platos por encima del objetivo', f'{X_PRECIO}!Por Plato!E38', 'num'),
            C('Food cost del conjunto de la carta con los precios elegidos', f'{X_PRECIO}!Por Plato!E39', 'pct1'),
            C('Margen de contribución medio por plato', f'{X_PRECIO}!Por Plato!E40'),
            C('Platos que usan el método A', f'{X_PRECIO}!Por Plato!E52', 'num'),
            C('Platos que usan el método B', f'{X_PRECIO}!Por Plato!E53', 'num'),
            C('Platos que usan el método C', f'{X_PRECIO}!Por Plato!E54', 'num'),
            C('Platos que usan el método D', f'{X_PRECIO}!Por Plato!E55', 'num'),
        ],
        'sector': ['FC-BENCH-01', 'FC-BENCH-03'],
        'tablas': [{
            'titulo': 'Los cuatro métodos aplicados a la misma carta (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)',
            'src': (X_PRECIO, 'Por Plato'),
            'cols': [('Plato', 'B', 'txt'), ('Coste/ración (€)', 'D', 'eur2'),
                     ('Método elegido', 'F', 'txt'),
                     ('A · PVP por factor (€)', 'K', 'eur2'),
                     ('B · PVP por margen (€)', 'L', 'eur2'),
                     ('PVP elegido sin IVA (€)', 'Q', 'eur2'),
                     ('Food cost final (%)', 'T', 'pct1'),
                     ('Semáforo', 'U', 'txt')],
            'filas': (9, 33),
            'nota': 'Las columnas A y B calculan siempre, aunque el plato use otro método: '
                    'están ahí para que veas qué precio habría salido y decidas con las cuatro '
                    'respuestas delante.',
        }],
        'prohibido': NO_COMUN + [
            'NO presentes el factor sobre el coste como «el método correcto» ni '
            'como el estándar del sector: es uno de cuatro y tiene un punto de '
            'rotura conocido.',
            'NO recomiendes un food cost objetivo concreto para el lector: el '
            'objetivo es una celda y depende de su estructura de costes.',
            'NO escribas precios de venta de platos que no estén en la tabla o '
            'en la lista de cifras.',
        ],
    },
    {
        'n': 10, 'titulo': 'Psicología de Precios: lo Demostrado y lo que es Leyenda',
        'resumen_indice': 'efecto señuelo, nombres descriptivos y formato del precio, cada uno con su estudio y su salvedad.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Separar lo que tiene estudio detrás de lo que circula por '
                    'blogs, y enseñar a aplicar lo demostrado sin convertir la '
                    'carta en un truco.',
        'epigrafes': [
            'El efecto señuelo: la opción que no quieres vender',
            'Nombres descriptivos: el estudio y su letra pequeña',
            'El formato del precio: qué se midió y en qué moneda',
            'Lo que circula sin estudio detrás',
            'Cómo se aplica esto a una carta de verdad',
        ],
        'puntos': [
            'Abrir con el efecto señuelo, que es lo mejor sostenido: una tercera '
            'opción claramente peor que una de las dos reales, pero no peor que '
            'la otra, empuja la elección hacia la opción que quieres vender. '
            'Citar el trabajo revisado por pares con su publicación.',
            'Al citar el estudio de los nombres descriptivos, escribir la '
            'salvedad DENTRO del mismo párrafo: su autor principal fue objeto de '
            'una investigación por mala praxis estadística y no se ha localizado '
            'una replicación independiente de este trabajo en concreto. El dato '
            'se usa como indicio, no como ley.',
            'Al citar el estudio del formato del precio, decir que se hizo en '
            'dólares y con comensales estadounidenses, y que lo que se midió no '
            'es el símbolo sino la ausencia de referencia monetaria.',
            'Ser explícito con lo que no tiene respaldo: los precios acabados en '
            'nueve, la posición del plato en la esquina superior derecha y las '
            'reglas de recorrido de la vista se repiten mucho y no se han '
            'sostenido con un estudio citable. Se dicen sin número y sin '
            'atribución.',
            'Cerrar con la aplicación práctica: el método D de la hoja de precios '
            'es exactamente esto —un precio que se impone desde la percepción— y '
            'la hoja te devuelve el food cost que te queda al hacerlo.',
            'CITAS OBLIGATORIAS, con este nombre exacto: el trabajo del efecto '
            'señuelo se cita como publicado en International Hospitality Review '
            '(editorial Emerald); el de los nombres descriptivos, como Wansink, '
            'Painter y van Ittersum (2001) en la Cornell Hotel and Restaurant '
            'Administration Quarterly; el del formato del precio, como Yang, '
            'Kimes y Sessarego (2009) en el Cornell Hospitality Report.',
        ],
        'cifras': [
            C('Tipo de IVA de restauración en sala', f'{X_PRECIO}!Por Plato!E6', 'pct0'),
            C('Platos que usan el método del precio de mercado', f'{X_PRECIO}!Por Plato!E54', 'num'),
            C('Platos que usan el método del valor percibido', f'{X_PRECIO}!Por Plato!E55', 'num'),
            C('Precio de la carta entera si todo fuese a valor percibido', f'{X_PRECIO}!Por Plato!E48'),
            C('Precio de la carta entera con los PVP actuales', f'{X_PRECIO}!Por Plato!E49'),
            C('Food cost del conjunto de la carta con los precios elegidos', f'{X_PRECIO}!Por Plato!E39', 'pct1'),
            C('PVP elegido de las croquetas, sin IVA', f'{X_PRECIO}!Por Plato!Q9'),
            C('PVP elegido del chuletón, sin IVA', f'{X_PRECIO}!Por Plato!Q20'),
        ],
        'sector': ['FC-PSICO-03', 'FC-PSICO-01', 'FC-PSICO-02'],
        'tablas': [{
            'titulo': 'Cuando el precio viene de fuera: mercado y valor percibido (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)',
            'src': (X_PRECIO, 'Por Plato'),
            'cols': [('Plato', 'B', 'txt'), ('Coste/ración (€)', 'D', 'eur2'),
                     ('Precio de mercado de la zona (€)', 'H', 'eur2'),
                     ('Precio de valor percibido (€)', 'I', 'eur2'),
                     ('PVP elegido sin IVA (€)', 'Q', 'eur2'),
                     ('PVP elegido con IVA (€)', 'R', 'eur2')],
            'filas': (9, 33),
            'nota': 'El precio con IVA de la última columna es el que se imprime en la carta y '
                    'el único que ve el cliente: es ahí donde operan los efectos de este '
                    'capítulo, no en la base imponible con la que tú trabajas.',
        }],
        'prohibido': NO_COMUN + [
            'PROHIBIDO citar el estudio de los nombres descriptivos sin la '
            'salvedad sobre su autor y sobre la falta de replicación: la '
            'salvedad va en la misma frase o en la siguiente, nunca en una nota '
            'al final.',
            'PROHIBIDO trasladar al euro la cifra del estudio del formato del '
            'precio: se midió en dólares y con comensales de Estados Unidos.',
            'NO escribas ninguna cifra sobre el efecto señuelo: el trabajo que '
            'lo sostiene se cita por su resultado cualitativo, sin porcentaje.',
            'NO recomiendes quitar el símbolo de moneda de la carta como '
            'receta: se explica qué se midió y se deja la decisión al lector, '
            'que además tiene que cumplir con la información de precios al '
            'consumidor.',
        ],
    },
    {
        'n': 11, 'titulo': 'Ingeniería de Menú I: Kasavana & Smith Bien Hecho',
        'resumen_indice': 'popularidad por margen, el umbral del 70 % dividido por familia y qué se hace con cada cuadrante.',
        'palabras': 1700, 'bloques': 3,
        'objetivo': 'Enseñar la matriz clásica sin los dos errores que la '
                    'inutilizan: aplicarla a la carta entera en vez de por '
                    'familia, y comparar el margen con una media simple en vez '
                    'de con la ponderada.',
        'epigrafes': [
            'Qué mide la matriz y qué deja fuera',
            'El umbral de popularidad: por qué es el 70 % dividido entre los platos de la familia',
            'Por familia, siempre: un postre no compite con un principal',
            'Los cuatro cuadrantes y lo que significan de verdad',
            'Qué se hace con cada uno, en orden de riesgo',
        ],
        'puntos': [
            'Explicar la construcción: dos ejes, popularidad y margen de '
            'contribución en euros, cada plato comparado con el umbral y con la '
            'media ponderada de SU familia.',
            'Explicar de dónde sale el umbral: si una familia tiene N platos, un '
            'reparto plano daría a cada uno una N-ésima parte de las unidades; '
            'el umbral es el 70 % de esa parte, y el factor está en celda para '
            'quien quiera ser más exigente.',
            'Insistir en el error de aplicarla a la carta entera: un principal '
            'caro y un postre barato nunca competirán en margen, así que el '
            'postre saldría siempre mal clasificado por una razón que no tiene '
            'que ver con su rentabilidad.',
            'Explicar el orden de intervención por riesgo: primero se sube el '
            'precio de un caballo de batalla con cuidado, después se rediseña un '
            'puzle, y retirar es lo último porque un plato puede sostener a '
            'otros del ticket.',
            'Advertir de la limitación reconocida por la propia literatura: la '
            'matriz usa promedios, así que un cambio pequeño en la carta puede '
            'mover un plato de cuadrante. No es una etiqueta permanente.',
            'CITA OBLIGATORIA, con este nombre exacto: el modelo se atribuye a '
            'Kasavana y Smith (1982), «Menu Engineering: A Practical Guide to '
            'Menu Analysis». Se cita una vez, al presentarlo.',
        ],
        'cifras': [
            C('Factor del umbral de popularidad', f'{X_MATRIZ}!Datos!D33', 'pct0'),
            C('Platos con ventas en la carta', f'{X_MATRIZ}!Datos!D35', 'num'),
            C('Unidades vendidas al mes por la carta', f'{X_MATRIZ}!Datos!D32', 'num'),
            C('Margen de contribución medio ponderado de la carta', f'{X_MATRIZ}!Datos!G32'),
            C('MC medio ponderado de los entrantes', f'{X_MATRIZ}!Datos!G40'),
            C('MC medio ponderado de los principales', f'{X_MATRIZ}!Datos!G41'),
            C('MC medio ponderado de los postres', f'{X_MATRIZ}!Datos!G42'),
            C('Platos clasificados como Star', f'{X_MATRIZ}!Kasavana-Smith!C33', 'num'),
            C('Unidades vendidas por los Star', f'{X_MATRIZ}!Kasavana-Smith!D33', 'num'),
            C('Porcentaje de las unidades de la carta que son Star', f'{X_MATRIZ}!Kasavana-Smith!E33', 'pct1'),
            C('MC total aportado por los Star', f'{X_MATRIZ}!Kasavana-Smith!F33', 'eur'),
            C('Platos clasificados como Plowhorse', f'{X_MATRIZ}!Kasavana-Smith!C34', 'num'),
            C('MC total aportado por los Plowhorse', f'{X_MATRIZ}!Kasavana-Smith!F34', 'eur'),
            C('Platos clasificados como Puzzle', f'{X_MATRIZ}!Kasavana-Smith!C35', 'num'),
            C('MC total aportado por los Puzzle', f'{X_MATRIZ}!Kasavana-Smith!F35', 'eur'),
            C('Platos clasificados como Dog', f'{X_MATRIZ}!Kasavana-Smith!C36', 'num'),
            C('Unidades vendidas por los Dog', f'{X_MATRIZ}!Kasavana-Smith!D36', 'num'),
            C('MC total aportado por los Dog', f'{X_MATRIZ}!Kasavana-Smith!F36', 'eur'),
        ],
        'sector': ['FC-METODO-01'],
        'tablas': [
            {
                'titulo': 'La carta clasificada plato a plato, dentro de su familia (matriz-multimetodo-carta.xlsx, hoja «Kasavana-Smith»)',
                'src': (X_MATRIZ, 'Kasavana-Smith'),
                'cols': [('Plato', 'B', 'txt'), ('Familia', 'C', 'txt'),
                         ('Uds', 'D', 'num'), ('Mix en su familia (%)', 'E', 'pct1'),
                         ('Umbral (%)', 'F', 'pct1'), ('Popularidad', 'G', 'txt'),
                         ('MC del plato (€)', 'H', 'eur2'),
                         ('MC medio de su familia (€)', 'I', 'eur2'),
                         ('Clasificación', 'K', 'txt')],
                'filas': (5, 29),
            },
            {
                'titulo': 'Cuánto pesa cada cuadrante (matriz-multimetodo-carta.xlsx, hoja «Kasavana-Smith»)',
                'src': (X_MATRIZ, 'Kasavana-Smith'),
                'cols': [('Clasificación', 'B', 'txt'), ('Platos', 'C', 'num'),
                         ('Uds vendidas', 'D', 'num'), ('% de las uds de la carta', 'E', 'pct1'),
                         ('MC total aportado (€)', 'F', 'eur')],
                'filas': (33, 36),
                'nota': 'Mírese la última columna antes de tocar nada: hay cuadrantes con pocos '
                        'platos que sostienen una parte grande del margen del mes.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO traduzcas los nombres de los cuadrantes a un vocabulario propio: '
            'se usan los originales (Star, Plowhorse, Puzzle, Dog) con su '
            'explicación en español al lado, porque son los que el lector va a '
            'encontrar en la hoja y en cualquier otro material.',
            'NO digas que un Dog se retira sin más: se explica el orden de '
            'intervención y las razones para conservar uno.',
            'NO uses la media simple del margen de la carta como referencia: la '
            'comparación es siempre contra la media ponderada de la familia.',
        ],
    },
    {
        'n': 12, 'titulo': 'Ingeniería de Menú II: lo que la Matriz Clásica no Ve',
        'resumen_indice': 'Miller, Pavesic, Goal Value y LeBruto: tres variables y ningún método que las mida todas.',
        'palabras': 1600, 'bloques': 3,
        'objetivo': 'Enseñar los tres modelos que corrigen a la matriz clásica y '
                    'dejar clara la razón por la que existen: cada uno mide dos '
                    'de las tres variables que importan.',
        'epigrafes': [
            'Miller: popularidad contra food cost porcentual',
            'Pavesic: food cost porcentual contra margen ponderado por unidades',
            'Goal Value: un índice por plato en lugar de cuadrantes',
            'LeBruto: qué pasa cuando entra el coste de mano de obra',
            'Las tres variables y por qué ningún método las mide todas',
        ],
        'puntos': [
            'La tesis del capítulo: popularidad, food cost porcentual y margen '
            'en euros son tres variables, y cada modelo elige dos. Por eso '
            'discrepan, y por eso la discrepancia es información.',
            'Explicar Miller como el modelo del que compra bien: premia el food '
            'cost bajo con volumen, y por eso puede señalar como ganador un '
            'plato que deja pocos euros.',
            'Explicar Pavesic como el corrector de Miller: pondera el margen por '
            'las unidades vendidas, así que un plato de margen alto que casi no '
            'se vende deja de parecer estupendo.',
            'Explicar Goal Value como una alternativa NO matricial: un único '
            'índice por plato que combina food cost, precio, popularidad y '
            'costes variables, con la crítica de sus autores al enfoque de '
            'cuadrantes, que se apoya en promedios.',
            'Explicar LeBruto como lectura y no como hoja: mete el coste de mano '
            'de obra y parte los cuatro cuadrantes en ocho. Su frase clave —los '
            'operadores ingresan dinero, no porcentajes— es la que ordena todo '
            'el capítulo.',
            'Advertir de que el Goal Value es un índice sin unidades: sólo sirve '
            'comparado con el objetivo de su propia familia, nunca en absoluto '
            'ni entre familias.',
            'CITAS OBLIGATORIAS, con estos nombres exactos y una sola vez cada '
            'una, al presentar su modelo: Miller (1980); Pavesic (1983); Hayes '
            'y Huffman (1985), «Menu Analysis: A Better Way», en la Cornell '
            'Hotel and Restaurant Administration Quarterly; LeBruto, Quain y '
            'Ashley (1995), «Menu Engineering: A Model Including Labor», en la '
            'FIU Hospitality Review.',
        ],
        'cifras': [
            C('Platos clasificados como Winner por Miller', f'{X_MATRIZ}!Miller!C33', 'num'),
            C('Unidades vendidas por los Winner', f'{X_MATRIZ}!Miller!D33', 'num'),
            C('Porcentaje de las unidades que son Winner', f'{X_MATRIZ}!Miller!E33', 'pct1'),
            C('Food cost medio ponderado de los Winner', f'{X_MATRIZ}!Miller!F33', 'pct1'),
            C('Platos clasificados como Marginal', f'{X_MATRIZ}!Miller!C34', 'num'),
            C('Platos clasificados como Loser', f'{X_MATRIZ}!Miller!C35', 'num'),
            C('Food cost medio ponderado de los Loser', f'{X_MATRIZ}!Miller!F35', 'pct1'),
            C('Platos clasificados como Prime por Pavesic', f'{X_MATRIZ}!Pavesic!C33', 'num'),
            C('MC ponderado total de los Prime', f'{X_MATRIZ}!Pavesic!F33', 'eur'),
            C('Platos clasificados como Standard', f'{X_MATRIZ}!Pavesic!C34', 'num'),
            C('Platos clasificados como Sleeper', f'{X_MATRIZ}!Pavesic!C35', 'num'),
            C('Platos clasificados como Problem', f'{X_MATRIZ}!Pavesic!C36', 'num'),
            C('MC ponderado total de los Problem', f'{X_MATRIZ}!Pavesic!F36', 'eur'),
            C('Coste de personal sobre ventas usado en el Goal Value', f'{X_MATRIZ}!Goal Value!D33', 'pct0'),
            C('Otros costes variables sobre ventas usados en el Goal Value', f'{X_MATRIZ}!Goal Value!D34', 'pct0'),
            C('Platos por encima del Goal Value objetivo de su familia', f'{X_MATRIZ}!Goal Value!D36', 'num'),
            C('Platos por debajo del Goal Value objetivo de su familia', f'{X_MATRIZ}!Goal Value!D37', 'num'),
            C('Food cost medio ponderado de la carta', f'{X_MATRIZ}!Datos!H32', 'pct1'),
        ],
        'sector': ['FC-METODO-02', 'FC-METODO-03', 'FC-METODO-04', 'FC-METODO-05'],
        'tablas': [
            {
                'titulo': 'Miller: cuánto pesa cada grupo (matriz-multimetodo-carta.xlsx, hoja «Miller»)',
                'src': (X_MATRIZ, 'Miller'),
                'cols': [('Clasificación', 'B', 'txt'), ('Platos', 'C', 'num'),
                         ('Uds vendidas', 'D', 'num'), ('% de las uds de la carta', 'E', 'pct1'),
                         ('Food cost medio ponderado del grupo (%)', 'F', 'pct1')],
                'filas': (33, 35),
            },
            {
                'titulo': 'Pavesic: cuánto margen ponderado aporta cada grupo (matriz-multimetodo-carta.xlsx, hoja «Pavesic»)',
                'src': (X_MATRIZ, 'Pavesic'),
                'cols': [('Clasificación', 'B', 'txt'), ('Platos', 'C', 'num'),
                         ('Uds vendidas', 'D', 'num'), ('% de las uds de la carta', 'E', 'pct1'),
                         ('MC ponderado total del grupo (€)', 'F', 'eur')],
                'filas': (33, 36),
            },
            {
                'titulo': 'Goal Value plato a plato, contra el objetivo de su familia (matriz-multimetodo-carta.xlsx, hoja «Goal Value»)',
                'src': (X_MATRIZ, 'Goal Value'),
                'cols': [('Plato', 'B', 'txt'), ('PVP sin IVA (€)', 'F', 'eur2'),
                         ('Food cost (%)', 'E', 'pct1'),
                         ('Goal Value del plato', 'G', 'num2'),
                         ('Goal Value objetivo de su familia', 'K', 'num2'),
                         ('Lectura', 'L', 'txt')],
                'filas': (5, 29),
                'nota': 'El Goal Value es un ÍNDICE, no un importe: sólo tiene sentido comparado '
                        'con el objetivo de su propia familia, que es la columna de al lado.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO digas que uno de los métodos es «el bueno» o que sustituye a los '
            'demás: el capítulo existe para explicar qué mide cada uno.',
            'NO escribas el Goal Value con símbolo de euro ni lo llames importe: '
            'es un índice.',
            'NO reproduzcas la fórmula del Goal Value con constantes inventadas: '
            'los porcentajes de coste de personal y de otros costes variables '
            'son los que te doy, y viven en celdas editables.',
        ],
    },
    {
        'n': 13, 'titulo': 'Cuando los Métodos Discrepan: el Protocolo de Decisión',
        'resumen_indice': 'leer las cuatro lecturas a la vez, entender la discrepancia y decidir entre reformular, resubir, rediseñar o retirar.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Convertir la discrepancia entre métodos en un protocolo de '
                    'decisión. Que el lector sepa qué hacer cuando dos modelos '
                    'dicen cosas contrarias sobre el mismo plato.',
        'epigrafes': [
            'Coincidencia no es confianza: qué significa que los cuatro coincidan',
            'Los patrones de discrepancia más frecuentes',
            'Las cuatro erres: reformular, resubir, rediseñar, retirar',
            'El orden de intervención y cuántos platos se tocan a la vez',
        ],
        'puntos': [
            'La tesis: que los cuatro métodos coincidan no valida el '
            'diagnóstico, porque comparten datos de entrada. Lo que aporta '
            'información es DÓNDE discrepan, y el capítulo enseña a leer eso.',
            'Patrón uno: margen alto con food cost porcentual pobre. Es un plato '
            'de producto caro que deja dinero; se revisa el precio o la ración, '
            'no se retira.',
            'Patrón dos: food cost porcentual excelente con margen bajo. Vende '
            'mucho y deja poco; el sitio de ese plato es el ticket, no la '
            'cuenta de resultados, y se decide si se mantiene como gancho.',
            'Patrón tres: popularidad baja en todos los modelos. Antes de '
            'retirar, se comprueba si el problema es el plato o su descripción y '
            'su sitio en la carta.',
            'Regla operativa: no se tocan más de dos o tres platos a la vez, '
            'porque cada cambio mueve el mix y con él los umbrales de todos los '
            'demás. Después de cada tanda se vuelve a medir.',
            'Al nombrar los modelos se usan los apellidos de sus autores: '
            'Kasavana y Smith, Miller, Pavesic, y Hayes y Huffman para el Goal '
            'Value. Sin año y sin repetir la referencia completa, que ya se dio '
            'al presentarlos.',
        ],
        'cifras': [
            C('Platos con las cuatro lecturas en la mejor categoría', f'{X_MATRIZ}!Comparativa!C39', 'num'),
            C('Platos con tres o cuatro lecturas fuera', f'{X_MATRIZ}!Comparativa!C40', 'num'),
            C('Platos con ninguna lectura fuera', f'{X_MATRIZ}!Comparativa!C33', 'num'),
            C('Porcentaje de la carta sin ninguna lectura fuera', f'{X_MATRIZ}!Comparativa!D33', 'pct1'),
            C('Platos con una lectura fuera', f'{X_MATRIZ}!Comparativa!C34', 'num'),
            C('Platos con dos lecturas fuera', f'{X_MATRIZ}!Comparativa!C35', 'num'),
            C('Porcentaje de la carta con dos lecturas fuera', f'{X_MATRIZ}!Comparativa!D35', 'pct1'),
            C('Platos con tres lecturas fuera', f'{X_MATRIZ}!Comparativa!C36', 'num'),
            C('Platos con las cuatro lecturas fuera', f'{X_MATRIZ}!Comparativa!C37', 'num'),
            C('Platos con ventas en la carta', f'{X_MATRIZ}!Datos!D35', 'num'),
            C('Margen de contribución medio ponderado de la carta', f'{X_MATRIZ}!Datos!G32'),
        ],
        'sector': ['FC-METODO-01', 'FC-METODO-04', 'FC-METODO-05'],
        'tablas': [
            {
                'titulo': 'Las cuatro lecturas del mismo plato, una al lado de otra (matriz-multimetodo-carta.xlsx, hoja «Comparativa»)',
                'src': (X_MATRIZ, 'Comparativa'),
                'cols': [('Plato', 'B', 'txt'), ('Familia', 'C', 'txt'),
                         ('Kasavana & Smith', 'D', 'txt'), ('Miller', 'E', 'txt'),
                         ('Pavesic', 'F', 'txt'), ('Goal Value', 'G', 'txt'),
                         ('Lecturas fuera', 'H', 'num'),
                         ('Decisión sugerida', 'J', 'txt')],
                'filas': (5, 29),
            },
            {
                'titulo': 'Cuántos platos discrepan, y cuánto (matriz-multimetodo-carta.xlsx, hoja «Comparativa»)',
                'src': (X_MATRIZ, 'Comparativa'),
                'cols': [('Lecturas fuera de la mejor categoría', 'B', 'num'),
                         ('Platos', 'C', 'num'), ('% de la carta', 'D', 'pct1')],
                'filas': (33, 37),
                'nota': 'La columna de la izquierda no es una nota: es el número de modelos que '
                        'sacan al plato de su mejor categoría. Cuanto más arriba, más de acuerdo '
                        'están los cuatro en que ahí hay algo que revisar.',
            },
        ],
        'prohibido': NO_COMUN + [
            'NO presentes la coincidencia de los cuatro métodos como prueba de '
            'nada: comparten datos de entrada y hay que decirlo.',
            'NO conviertas las cuatro erres en un algoritmo cerrado: son un '
            'orden de intervención, y la decisión final la toma quien conoce a '
            'su cliente.',
            'NO recomiendes cambiar la carta entera de golpe.',
        ],
    },
    {
        'n': 14, 'titulo': 'Carta Corta, Menú de Precio Fijo, Buffet y Banquete',
        'resumen_indice': 'cuando el precio ya está puesto y el margen lo decide el mix: menú del día, buffet, hotel y catering.',
        'palabras': 1500, 'bloques': 3,
        'objetivo': 'Trabajar los formatos en los que el cliente no elige precio '
                    'sino contenido. Aquí no se pone precio plato a plato: se '
                    'gestiona el reparto de lo que la gente escoge.',
        'epigrafes': [
            'Tamaño de carta: qué se gana al podar y qué se pierde',
            'Menú de precio fijo: el margen lo decide el mix',
            'Los dos escenarios de mix y qué hacer con ellos',
            'Buffet, banquete y hotel: el mismo problema con otra escala',
            'Catering y eventos: el mix se pacta antes',
        ],
        'puntos': [
            'La tesis del capítulo: en un menú de precio fijo el ingreso está '
            'cerrado, así que el resultado depende ENTERAMENTE de qué opción '
            'elija la gente. Gestionar ese menú es gestionar el mix.',
            'Enseñar la mecánica de los dos escenarios: el mismo menú, el mismo '
            'precio y el mismo número de comensales dan márgenes distintos sólo '
            'porque cambia lo que se pide.',
            'Explicar la palanca real: si el plato más caro del menú es el más '
            'pedido, no se sube el precio del menú, se cambia el sitio de ese '
            'plato en la pizarra o se mejora la alternativa.',
            'Explicar los costes fijos por menú —pan, café, bebida incluida— que '
            'muchos escandallos de menú del día olvidan y que en un ticket bajo '
            'pesan mucho.',
            'Buffet, banquete y hotel: se cuesta por comensal servido y no por '
            'ración emplatada, y el dato que gobierna es el consumo medido por '
            'cabeza, que hay que medir en la propia casa.',
            'Catering y eventos: el mix se pacta en la propuesta, así que el '
            'trabajo de ingeniería se hace ANTES de firmar, no después de '
            'servir.',
        ],
        'cifras': [
            C('PVP del menú de precio fijo, con IVA', f'{X_MATRIZ}!Menú Precio Fijo!C19'),
            C('Tipo de IVA de restauración en sala', f'{X_MATRIZ}!Menú Precio Fijo!C20', 'pct0'),
            C('PVP del menú sin IVA', f'{X_MATRIZ}!Menú Precio Fijo!C21'),
            C('Costes fijos por menú', f'{X_MATRIZ}!Menú Precio Fijo!C22'),
            C('Food cost objetivo del menú', f'{X_MATRIZ}!Menú Precio Fijo!C23', 'pct0'),
            C('Menús servidos al mes', f'{X_MATRIZ}!Menú Precio Fijo!C24', 'num'),
            C('Coste medio total del menú con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B38'),
            C('Coste medio total del menú en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C38'),
            C('Coste medio total del menú en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D38'),
            C('Food cost del menú con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B39', 'pct1'),
            C('Food cost del menú en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C39', 'pct1'),
            C('Food cost del menú en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D39', 'pct1'),
            C('Margen de contribución por menú con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B40'),
            C('Margen de contribución por menú en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C40'),
            C('Margen de contribución por menú en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D40'),
            C('Margen del mes con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B41'),
            C('Margen del mes en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C41'),
            C('Margen del mes en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D41'),
            C('Platos dados de alta en la carta de ejemplo', f'{X_MATRIZ}!Datos!D36', 'num'),
        ],
        'sector': ['FC-BENCH-05', 'FC-BENCH-03'],
        'tablas': [
            {
                'titulo': 'Las opciones del menú y los tres repartos de mix (matriz-multimetodo-carta.xlsx, hoja «Menú Precio Fijo»)',
                'src': (X_MATRIZ, 'Menú Precio Fijo'),
                'cols': [('Curso', 'A', 'txt'), ('Opción', 'B', 'txt'),
                         ('Coste por ración (€)', 'C', 'eur2'),
                         ('Mix base (%)', 'D', 'pct0'),
                         ('Mix escenario A (%)', 'E', 'pct0'),
                         ('Mix escenario B (%)', 'F', 'pct0')],
                'filas': (5, 15),
                'nota': 'Los tres repartos suman el 100 % dentro de cada curso; lo único que '
                        'cambia entre escenarios es qué opción se lleva la gente.',
            },
            {
                'titulo': 'El coste medio de cada curso según el mix (matriz-multimetodo-carta.xlsx, hoja «Menú Precio Fijo»)',
                'src': (X_MATRIZ, 'Menú Precio Fijo'),
                'cols': [('Curso', 'A', 'txt'), ('Coste medio base (€)', 'C', 'eur2'),
                         ('Coste medio A (€)', 'E', 'eur2'),
                         ('Coste medio B (€)', 'G', 'eur2')],
                'filas': (27, 29),
            },
            {
                'titulo': 'El mismo menú, el mismo precio, tres resultados (matriz-multimetodo-carta.xlsx, hoja «Menú Precio Fijo»)',
                'src': (X_MATRIZ, 'Menú Precio Fijo'),
                'cols': [('Concepto', 'A', 'txt'), ('Mix base', 'B', 'eur2'),
                         ('Escenario A', 'C', 'eur2'), ('Escenario B', 'D', 'eur2')],
                'filas': (34, 41),
            },
        ],
        'prohibido': NO_COMUN + [
            'NO des un número máximo de platos «correcto» para una carta: se '
            'explican las consecuencias de podar (menos merma, menos stock, más '
            'rotación) y las de no hacerlo, sin inventar un óptimo.',
            'NO escribas ningún precio de menú, de buffet, de banquete ni de '
            'cubierto de catering que no esté en la lista de cifras.',
            'NO des ratios de consumo por comensal en buffet: no hay fuente y '
            'ese dato se mide en cada casa.',
        ],
    },
]

CAPITULOS += [
    {
        'n': 15, 'titulo': 'Multicanal: Sala, Take Away y Delivery',
        'resumen_indice': 'comisión, packaging, IVA por canal y precio techo: cuánto subir en cada canal y qué plato excluir.',
        'palabras': 1700, 'bloques': 3,
        'objetivo': 'Que el lector deje de servir la misma carta al mismo precio '
                    'en tres canales que tienen estructuras de coste distintas, '
                    'y que sepa qué platos no deben estar en la aplicación de '
                    'reparto.',
        'epigrafes': [
            'Tres canales, tres cuentas de resultados',
            'La comisión no es el único coste: packaging y platos por pedido',
            'El IVA cambia con el canal y con el producto',
            'El precio techo: hasta dónde te deja subir la aplicación',
            'Qué platos no deberían estar en delivery',
            'Vender fuera de España: qué casillas se cambian',
        ],
        'puntos': [
            'La tesis: la comisión no se resta del margen, se aplica sobre el '
            'precio, así que un mismo plato con el mismo precio tiene un food '
            'cost efectivo distinto en cada canal. Ese es el número que hay que '
            'mirar, no el de la sala.',
            'Explicar el packaging por PLATO y no por pedido: el envase se paga '
            'por pedido, así que su coste por plato depende de cuántos platos '
            'lleve el pedido medio, y ese dato es una celda.',
            'Explicar el precio techo: la aplicación tiene su propio mercado y '
            'un precio por encima del de la competencia no se vende aunque los '
            'números cuadren. Por eso la hoja no da un precio, da un precio '
            'necesario y lo compara con el techo.',
            'Explicar la decisión de excluir: un plato que no llega al food cost '
            'objetivo del canal sin pasarse del techo no se sube de precio, se '
            'saca de la carta de esa aplicación o se reformula en un formato '
            'que viaje mejor.',
            'Las comisiones se presentan como orden de magnitud con su fuente y '
            'con la advertencia de que dependen de la zona, del plan y de quién '
            'reparte; además hay costes que no están en el porcentaje nominal.',
            'Nota para Hispanoamérica: las nueve casillas de la matriz fiscal y '
            'las comisiones son editables; los operadores citados como ejemplo '
            'en esos mercados son Rappi y DiDi en México y PedidosYa en '
            'Argentina, Uruguay y Panamá.',
        ],
        'cifras': [
            C('Comisión de la plataforma en delivery', f'{X_MULTI}!Parámetros!B18', 'pct0'),
            C('Packaging por pedido en take away', f'{X_MULTI}!Parámetros!C17'),
            C('Packaging por pedido en delivery', f'{X_MULTI}!Parámetros!C18'),
            C('Platos por pedido en delivery', f'{X_MULTI}!Parámetros!D18', 'num1'),
            C('Packaging por plato en delivery', f'{X_MULTI}!Parámetros!F18'),
            C('Food cost objetivo en sala', f'{X_MULTI}!Parámetros!E16', 'pct0'),
            C('Food cost objetivo en take away', f'{X_MULTI}!Parámetros!E17', 'pct0'),
            C('Food cost objetivo en delivery', f'{X_MULTI}!Parámetros!E18', 'pct0'),
            C('Food cost efectivo medio en sala', f'{X_MULTI}!Resumen!D5', 'pct1'),
            C('Food cost efectivo medio en take away', f'{X_MULTI}!Resumen!D6', 'pct1'),
            C('Food cost efectivo medio en delivery', f'{X_MULTI}!Resumen!D7', 'pct1'),
            C('Platos viables en sala', f'{X_MULTI}!Resumen!B5', 'num'),
            C('Platos viables en delivery', f'{X_MULTI}!Resumen!B7', 'num'),
            C('Platos a excluir o reformular en delivery', f'{X_MULTI}!Resumen!C7', 'num'),
            C('Margen mensual total en sala', f'{X_MULTI}!Resumen!G5', 'eur'),
            C('Margen mensual total en delivery', f'{X_MULTI}!Resumen!G7', 'eur'),
            C('Diferencia de margen del delivery frente a la sala', f'{X_MULTI}!Resumen!I7', 'eur'),
            C('Food cost en sala de las croquetas', f'{X_MULTI}!Carta!H5', 'pct1'),
            C('Food cost en delivery de las croquetas', f'{X_MULTI}!Carta!V5', 'pct1'),
            C('PVP sin IVA que necesitan las croquetas en delivery', f'{X_MULTI}!Carta!W5'),
            C('Precio techo de las croquetas en la aplicación', f'{X_MULTI}!Carta!F5'),
        ],
        'sector': ['FC-DELIV-01', 'FC-DELIV-02', 'FC-DELIV-03', 'FC-BENCH-04',
                   'FC-IVA-02', 'FC-IVA-03', 'FC-IVA-04', 'FC-IVA-08'],
        'tablas': [
            {
                'titulo': 'Los parámetros de cada canal (simulador-repricing-multicanal.xlsx, hoja «Parámetros»)',
                'src': (X_MULTI, 'Parámetros'),
                'cols': [('Canal', 'A', 'txt'), ('Packaging (€/pedido)', 'C', 'eur2'),
                         ('Platos por pedido', 'D', 'num1'),
                         ('Comisión de la plataforma (%)', 'B', 'pct0'),
                         ('Food cost objetivo (%)', 'E', 'pct0'),
                         ('Packaging por plato (€)', 'F', 'eur2')],
                'filas': (16, 18),
                'nota': 'Las seis columnas son editables: son el contrato que hayas firmado tú, '
                        'no un estándar del sector.',
            },
            {
                'titulo': 'Comisiones de las plataformas: orden de magnitud, no tarifario (simulador-repricing-multicanal.xlsx, hoja «Parámetros»)',
                'src': (X_MULTI, 'Parámetros'),
                'cols': [('Plataforma', 'A', 'txt'),
                         ('Comisión y cuotas de referencia', 'B', 'txt')],
                'filas': (24, 27),
                'nota': 'Estas horquillas son de referencia sectorial y cambian por zona, por '
                        'plan contratado y según quién haga el reparto. El número que hay que '
                        'escribir en la casilla es el de tu contrato.',
            },
            {
                'titulo': 'Los tres canales, comparados (simulador-repricing-multicanal.xlsx, hoja «Resumen»)',
                'src': (X_MULTI, 'Resumen'),
                'cols': [('Canal', 'A', 'txt'), ('Platos viables', 'B', 'num'),
                         ('Platos a excluir o reformular', 'C', 'num'),
                         ('Food cost efectivo medio (%)', 'D', 'pct1'),
                         ('Food cost objetivo (%)', 'E', 'pct1'),
                         ('PVP medio necesario (€)', 'F', 'eur2'),
                         ('Margen mensual total (€)', 'G', 'eur')],
                'filas': (5, 7),
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO presentar ninguna comisión como tarifa oficial o cerrada: '
            'siempre horquilla, siempre con la fuente y siempre diciendo de qué '
            'depende.',
            'NO restes la comisión del margen como si fuese un coste fijo por '
            'plato: se aplica sobre el precio de venta y por eso escala con él.',
            'NO digas que el delivery «no es rentable»: se explica en qué '
            'condiciones deja margen y qué platos no deberían estar ahí.',
            'NO olvides que en delivery la comida sigue en el tipo reducido: lo '
            'que cambia de tipo es el alcohol y las bebidas con azúcares o '
            'edulcorantes añadidos.',
        ],
    },
    {
        'n': 16, 'titulo': 'Beverage Cost: la Bodega Como Cuenta de Resultados Propia',
        'resumen_indice': 'copa contra botella, barril, cócteles y el IVA por canal: la bodega tiene sus propios objetivos.',
        'palabras': 1600, 'bloques': 3,
        'objetivo': 'Sacar la bebida del food cost general y gestionarla con sus '
                    'propios objetivos por categoría, que no son los de la '
                    'comida ni son iguales entre sí.',
        'epigrafes': [
            'Por qué la bebida no se mide con la vara de la comida',
            'Vino: la copa cambia la ecuación de la botella',
            'Cerveza de barril y refrescos: el coste por servicio',
            'Destilados y cócteles: cuando el coste está en la mezcla',
            'El resumen de la bodega y el margen que estás dejando en la mesa',
        ],
        'puntos': [
            'Abrir con el dato que rompe el tópico: en el informe español de '
            'referencia la bebida pesa proporcionalmente MÁS sobre sus propios '
            'ingresos que la comida sobre los suyos. Explicarlo como matiz, no '
            'como regla universal: depende del mix de bodega.',
            'Explicar la decisión copa contra botella: la copa mejora el '
            'porcentaje y el número de copas por botella es el dato que la '
            'sostiene; si se sirven de más, el beverage cost real se dispara y '
            'nadie lo ve.',
            'Explicar el coste por servicio del barril: se compra en litros y se '
            'vende en centilitros, y la merma de espuma y de limpieza de líneas '
            'es la que separa el cálculo de la realidad.',
            'Explicar el cóctel como una ficha de escandallo en miniatura: se '
            'cuesta ingrediente a ingrediente y la mezcla suele pesar más de lo '
            'que se cree.',
            'Cerrar con la lectura del resumen: cada categoría tiene su objetivo '
            'editable y el libro calcula el margen que se recuperaría si cada '
            'una llegase al suyo. Ese número es el orden de prioridades.',
            'El IVA por canal también afecta a la bodega: la misma botella lleva '
            'un tipo en sala y otro si el cliente se la lleva, y las columnas de '
            'precio con IVA de la hoja lo resuelven solas.',
        ],
        'cifras': [
            C('Objetivo de beverage cost de los vinos', f'{X_BEBIDAS}!Parámetros!B17', 'pct0'),
            C('Objetivo de beverage cost de cervezas y refrescos', f'{X_BEBIDAS}!Parámetros!B18', 'pct0'),
            C('Objetivo de beverage cost de destilados y cócteles', f'{X_BEBIDAS}!Parámetros!B19', 'pct0'),
            C('Ventas totales de bodega del mes', f'{X_BEBIDAS}!Resumen Bodega!B8', 'eur'),
            C('Coste total de bodega del mes', f'{X_BEBIDAS}!Resumen Bodega!C8'),
            C('Beverage cost ponderado de toda la bodega', f'{X_BEBIDAS}!Resumen Bodega!D8', 'pct1'),
            C('Margen de contribución total de la bodega', f'{X_BEBIDAS}!Resumen Bodega!F8'),
            C('Margen total a recuperar si cada categoría llegase a su objetivo', f'{X_BEBIDAS}!Resumen Bodega!H8'),
            C('Beverage cost ponderado de los vinos', f'{X_BEBIDAS}!Resumen Bodega!D5', 'pct1'),
            C('Beverage cost ponderado de cervezas y refrescos', f'{X_BEBIDAS}!Resumen Bodega!D6', 'pct1'),
            C('Beverage cost ponderado de destilados y cócteles', f'{X_BEBIDAS}!Resumen Bodega!D7', 'pct1'),
            C('Peso de los vinos sobre las ventas de bodega', f'{X_BEBIDAS}!Resumen Bodega!G5', 'pct1'),
            C('Peso de cervezas y refrescos sobre las ventas de bodega', f'{X_BEBIDAS}!Resumen Bodega!G6', 'pct1'),
            C('Botellas de vino vendidas al mes', f'{X_BEBIDAS}!Vinos!J35', 'num'),
            C('Copas de vino vendidas al mes', f'{X_BEBIDAS}!Vinos!K35', 'num'),
            C('Coste por copa del tinto de la casa', f'{X_BEBIDAS}!Vinos!L5'),
            C('Margen por copa del tinto de la casa', f'{X_BEBIDAS}!Vinos!N5'),
            C('Beverage cost de la botella del tinto de la casa', f'{X_BEBIDAS}!Vinos!O5', 'pct1'),
            C('Beverage cost de la copa del tinto de la casa', f'{X_BEBIDAS}!Vinos!P5', 'pct1'),
            C('Servicios de cerveza y refrescos vendidos al mes', f'{X_BEBIDAS}!Cervezas y Refrescos!J20', 'num'),
            C('Beverage cost ponderado de los combinados', f'{X_BEBIDAS}!Destilados y Cócteles!N17', 'pct1'),
            C('Beverage cost ponderado de los cócteles', f'{X_BEBIDAS}!Destilados y Cócteles!I64', 'pct1'),
        ],
        'sector': ['FC-BENCH-02', 'FC-BEV-01', 'FC-BEV-02', 'FC-IVA-01', 'FC-IVA-03'],
        'tablas': [
            {
                'titulo': 'La bodega por categorías, con su objetivo al lado (carta-de-bebidas-beverage-cost.xlsx, hoja «Resumen Bodega»)',
                'src': (X_BEBIDAS, 'Resumen Bodega'),
                'cols': [('Categoría', 'A', 'txt'), ('Ventas del mes (€)', 'B', 'eur'),
                         ('Coste del mes (€)', 'C', 'eur2'),
                         ('Beverage cost ponderado (%)', 'D', 'pct1'),
                         ('Objetivo (%)', 'E', 'pct1'),
                         ('Margen de contribución (€)', 'F', 'eur2'),
                         ('Peso sobre las ventas de bodega (%)', 'G', 'pct1')],
                'filas': (5, 8),
                'nota': 'Los objetivos por categoría son celdas editables sembradas con las '
                        'referencias del sector: no son un estándar, son un punto de partida '
                        'para que escribas el tuyo.',
            },
            {
                'titulo': 'Vinos: la misma botella por botella y por copa (carta-de-bebidas-beverage-cost.xlsx, hoja «Vinos»)',
                'src': (X_BEBIDAS, 'Vinos'),
                'cols': [('Vino', 'B', 'txt'),
                         ('Compra de la botella sin IVA (€)', 'D', 'eur2'),
                         ('Copas por botella', 'G', 'num1'),
                         ('PVP botella sin IVA (€)', 'H', 'eur2'),
                         ('PVP copa sin IVA (€)', 'I', 'eur2'),
                         ('Coste por copa (€)', 'L', 'eur2'),
                         ('Beverage cost botella (%)', 'O', 'pct1'),
                         ('Beverage cost copa (%)', 'P', 'pct1')],
                'filas': (5, 34),
            },
            {
                'titulo': 'Cervezas y refrescos: del formato de compra al servicio (carta-de-bebidas-beverage-cost.xlsx, hoja «Cervezas y Refrescos»)',
                'src': (X_BEBIDAS, 'Cervezas y Refrescos'),
                'cols': [('Referencia', 'B', 'txt'), ('Formato de compra', 'C', 'txt'),
                         ('Precio de compra sin IVA (€)', 'F', 'eur2'),
                         ('Servicios por unidad', 'K', 'num1'),
                         ('Coste por servicio (€)', 'L', 'eur2'),
                         ('PVP en sala sin IVA (€)', 'I', 'eur2'),
                         ('Beverage cost (%)', 'N', 'pct1')],
                'filas': (5, 19),
            },
        ],
        'prohibido': NO_COMUN + [
            'NO afirmes como regla general que la bebida deja más margen que la '
            'comida: el dato del que dispones dice lo contrario en su fuente y '
            'hay que presentarlo como matiz, con el mix de bodega detrás.',
            'NO des objetivos de beverage cost como si fueran estándar del '
            'sector: los rangos que tienes llevan fuente de fiabilidad media y '
            'las casillas del libro son editables.',
            'NO escribas precios de vinos, cervezas ni destilados que no estén '
            'en las tablas o en la lista de cifras.',
        ],
    },
    {
        'n': 17, 'titulo': 'Costeo por Lote en Obrador y Pastelería',
        'resumen_indice': 'rendimiento de tanda, mano de obra por hora, packaging y escalado: por qué la ración no es la unidad.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Adaptar todo lo anterior a un negocio que no produce '
                    'raciones sino tandas, en el que la mano de obra y el '
                    'envase pesan tanto como la harina.',
        'epigrafes': [
            'La unidad de costeo es la tanda, no la pieza',
            'Mano de obra por hora dentro del coste del lote',
            'Packaging y etiquetado: el coste que no está en la receta',
            'Escalar una fórmula sin escalar el error',
        ],
        'puntos': [
            'La tesis: en obrador se cuesta la tanda entera y se divide entre las '
            'piezas BUENAS que salen, no entre las teóricas. El rendimiento de '
            'tanda es el equivalente al rendimiento de despiece del capítulo 5.',
            'Explicar por qué aquí sí entra la mano de obra en el coste unitario: '
            'una pieza de bollería puede llevar más euros de manos que de '
            'materia prima, y un escandallo que sólo mira el ingrediente da un '
            'precio ruinoso.',
            'Explicar la merma de cocción y de fermentación como parte del '
            'rendimiento de tanda, con las pruebas medidas que trae el libro de '
            'rendimiento.',
            'Explicar el packaging y el etiquetado como coste por pieza, no por '
            'pedido, en cuanto el producto se vende envasado.',
            'Explicar el escalado: doblar la fórmula no dobla el tiempo ni la '
            'merma, así que el coste por pieza baja con el tamaño de tanda hasta '
            'que el horno o la cámara ponen el límite.',
            'Para el negocio que quiera la plantilla de costeo por lote lista, '
            'está en el Kit de Escandallos; aquí se da el método y se usa el '
            'método del margen objetivo, que es el que encaja con este formato.',
        ],
        'cifras': [
            C('Pruebas de cocción registradas', f'{X_MERMA}!Merma de Cocción!E20', 'num'),
            C('Rendimiento medio de cocción ponderado', f'{X_MERMA}!Merma de Cocción!E18', 'pct1'),
            C('Pérdida media por cocción', f'{X_MERMA}!Merma de Cocción!E19', 'pct1'),
            C('Pérdida de cocción del solomillo a la plancha', f'{X_MERMA}!Merma de Cocción!G6', 'pct1'),
            C('Pérdida de cocción del pollo de corral al horno', f'{X_MERMA}!Merma de Cocción!G7', 'pct1'),
            C('Coste por kilo del pollo ya cocinado', f'{X_MERMA}!Merma de Cocción!J7'),
            C('Pérdida de cocción de las verduras asadas', f'{X_MERMA}!Merma de Cocción!G10', 'pct1'),
            C('Platos que usan el método del margen objetivo', f'{X_PRECIO}!Por Plato!E53', 'num'),
            C('Margen de contribución medio por plato', f'{X_PRECIO}!Por Plato!E40'),
            C('Food cost del conjunto de la carta', f'{X_PRECIO}!Por Plato!E39', 'pct1'),
        ],
        'sector': ['FC-PRIME-03'],
        'tablas': [
            {
                'titulo': 'Lo que pierde el producto en el horno y en la plancha (rendimiento-mermas-producto.xlsx, hoja «Merma de Cocción»)',
                'src': (X_MERMA, 'Merma de Cocción'),
                'cols': [('Elaboración', 'B', 'txt'), ('Técnica', 'C', 'txt'),
                         ('Peso crudo (kg)', 'D', 'num2'), ('Peso cocinado (kg)', 'E', 'num2'),
                         ('Pérdida por cocción (%)', 'G', 'pct1'),
                         ('Factor de cocción', 'H', 'num2'),
                         ('Coste/kg crudo (€)', 'I', 'eur2'),
                         ('Coste/kg cocinado (€)', 'J', 'eur2')],
                'filas': (6, 15),
                'nota': 'El factor de cocción se multiplica por el coste del producto crudo: es '
                        'lo que convierte el precio del albarán en el coste de lo que sale del '
                        'horno.',
            },
            {
                'titulo': 'Poner precio por margen objetivo, que es el método del obrador (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)',
                'src': (X_PRECIO, 'Por Plato'),
                'cols': [('Plato', 'B', 'txt'), ('Coste/ración (€)', 'D', 'eur2'),
                         ('Margen objetivo (€)', 'G', 'eur2'),
                         ('B · PVP por margen (€)', 'L', 'eur2'),
                         ('FC resultante con B (%)', 'N', 'pct1')],
                'filas': (9, 33),
            },
        ],
        'prohibido': NO_COMUN + [
            'NO des un coste por hora de mano de obra ni un precio de packaging: '
            'no están en las cifras. Se explica cómo se calcula y de dónde sale '
            'el dato en el propio negocio.',
            'NO desarrolles la plantilla de costeo por lote: se explica el método '
            'y se remite al Kit de Escandallos, que ya la trae.',
            'NO extrapoles los datos de cocción de la tabla a la pastelería como '
            'si fueran suyos: son pruebas de cocina y sirven de ejemplo del '
            'método, no de tabla de referencia de obrador.',
        ],
    },
    {
        'n': 18, 'titulo': 'Cuando Sube el Proveedor: Protocolo de Re-escandallado',
        'resumen_indice': 'disparadores, calendario, dónde mirar los precios y cómo subir sin perder al cliente.',
        'palabras': 1500, 'bloques': 2,
        'objetivo': 'Dar un protocolo que no dependa de la memoria: cuándo se '
                    'vuelve a escandallar, qué se revisa primero y cómo se '
                    'traslada la subida a la carta.',
        'epigrafes': [
            'Los cuatro disparadores de un re-escandallado',
            'El calendario: qué se revisa cada mes y qué cada trimestre',
            'Dónde mirar el precio de la materia prima',
            'Cómo se sube un precio sin que se note en la caja',
        ],
        'puntos': [
            'Los cuatro disparadores: una subida de proveedor por encima del '
            'umbral que fijes, un cambio de formato o de calibre, un cambio de '
            'receta, y el vencimiento del calendario aunque no haya pasado nada.',
            'Explicar la regla del 80/20 en el re-escandallado: no se revisa la '
            'carta entera, se revisan las referencias que más pesan en el '
            'consumo del mes y los platos más vendidos.',
            'Enseñar DÓNDE mirar sin dar ninguna cifra: la nota de prensa del '
            'IPC del Instituto Nacional de Estadística para el comportamiento '
            'general de los alimentos, y el sistema de precios origen-mayorista '
            'del Ministerio de Agricultura para el fresco. Se explica cómo se '
            'consultan y qué preguntan, no cuánto valen hoy.',
            'Cómo se sube: no todos los platos a la vez ni el mismo porcentaje. '
            'Se sube donde el mercado deja, se aprovecha un cambio de carta o de '
            'temporada, y se revisan primero los platos cuya subida es pequeña '
            'en euros aunque sea grande en porcentaje.',
            'Advertir del efecto sobre la matriz: cambiar precios mueve el mix, '
            'así que después de una subida hay que volver a medir antes de '
            'sacar conclusiones sobre ningún plato.',
        ],
        'cifras': [
            C('Platos con precio calculado', f'{X_PRECIO}!Por Plato!E36', 'num'),
            C('Platos dentro del objetivo', f'{X_PRECIO}!Por Plato!E37', 'num'),
            C('Platos por encima del objetivo', f'{X_PRECIO}!Por Plato!E38', 'num'),
            C('Diferencia total con los PVP actuales', f'{X_PRECIO}!Por Plato!E41'),
            C('Subida media sobre el PVP actual', f'{X_PRECIO}!Por Plato!E42', 'pct1'),
            C('Diferencia de las croquetas con su PVP actual', f'{X_PRECIO}!Por Plato!W9'),
            C('Subida necesaria del plato de la ficha', f'{X_FICHA}!Ficha!E42', 'pct1'),
            C('Diferencia entre el PVP objetivo y el actual del plato de la ficha', f'{X_FICHA}!Ficha!E41'),
            C('Impacto total estimado de las decisiones del plan', f'{X_PLAN90}!Decisiones!D31', 'eur'),
            C('Decisiones de negociación registradas en el plan', f'{X_PLAN90}!Decisiones!C43', 'num'),
            C('Impacto estimado de las decisiones de negociación', f'{X_PLAN90}!Decisiones!D43', 'eur'),
        ],
        'sector': ['FC-FUENTES-01', 'FC-FUENTES-02', 'FC-FUENTES-03'],
        'tablas': [
            {
                'titulo': 'Qué plato hay que tocar y cuánto (precio-objetivo-multi-metodo.xlsx, hoja «Por Plato»)',
                'src': (X_PRECIO, 'Por Plato'),
                'cols': [('Plato', 'B', 'txt'), ('Coste/ración (€)', 'D', 'eur2'),
                         ('PVP actual sin IVA (€)', 'V', 'eur2'),
                         ('PVP elegido sin IVA (€)', 'Q', 'eur2'),
                         ('Diferencia (€)', 'W', 'eur2'),
                         ('Semáforo vs objetivo', 'U', 'txt')],
                'filas': (9, 33),
                'nota': 'La columna de la diferencia es la que ordena el trabajo: se empieza por '
                        'los platos cuya corrección es mayor en euros y se vende mucho, no por '
                        'los que tienen el porcentaje más feo.',
            },
            {
                'titulo': 'Las decisiones del plan, por tipo (plan-accion-90-dias.xlsx, hoja «Decisiones»)',
                'src': (X_PLAN90, 'Decisiones'),
                'cols': [('Decisión', 'B', 'txt'), ('Decisiones', 'C', 'num'),
                         ('Impacto estimado (€/mes)', 'D', 'eur2'),
                         ('Impacto conseguido (€/mes)', 'E', 'eur2')],
                'filas': (39, 44),
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO escribir cualquier cifra de inflación, de IPC o de subida '
            'de precios de un producto concreto. Este capítulo enseña dónde se '
            'consulta el dato, no cuál es.',
            'NO repitas las siete tácticas de negociación con proveedores del '
            'bono del Kit de Escandallos: aquí se explica con qué dato se va a '
            'la negociación y se remite a ese material.',
            'NO recomiendes una periodicidad de re-escandallado como si fuera '
            'una norma del sector: se explica qué se revisa en cada plazo y por '
            'qué.',
        ],
    },
    {
        'n': 19, 'titulo': 'Caso Integral: una Carta Entera, de Principio a Fin',
        'resumen_indice': 'la carta de ejemplo recorrida entera: ficha, matriz, precio, multicanal y plan de 90 días.',
        'palabras': 2200, 'bloques': 3,
        'objetivo': 'Recorrer la carta del pack de punta a punta con las ocho '
                    'herramientas encadenadas, para que el lector vea el flujo '
                    'completo antes de hacerlo con la suya.',
        'epigrafes': [
            'El punto de partida: qué había sobre la mesa',
            'Paso 1: escandallar y medir la merma',
            'Paso 2: clasificar la carta con los cuatro métodos',
            'Paso 3: poner precio plato a plato',
            'Paso 4: revisar el delivery y decidir exclusiones',
            'Paso 5: convertir el diagnóstico en decisiones con fecha',
            'Qué salió de todo esto',
        ],
        'puntos': [
            'Encabezar el capítulo diciendo con todas las letras que es un CASO '
            'MODELADO construido sobre las plantillas del pack, no un cliente '
            'real ni un negocio identificable.',
            'Paso a paso, y en cada paso: qué se miró, qué dijo la herramienta y '
            'qué se decidió. La decisión es lo que hay que enseñar, porque los '
            'números ya están en las tablas.',
            'En el paso de la clasificación, señalar los platos donde los cuatro '
            'métodos discrepan y explicar la decisión concreta que se tomó con '
            'cada uno de esos.',
            'En el paso del delivery, explicar por qué algunos platos salen de la '
            'aplicación y otros suben de precio, con el food cost efectivo y el '
            'precio techo delante.',
            'En el último paso, mostrar cómo cada decisión queda con '
            'responsable, semana e impacto estimado, y advertir de que el '
            'impacto es una ESTIMACIÓN a la fecha del plan, no un resultado.',
            'Cerrar con la lectura de los indicadores del trimestre y con la '
            'advertencia de que los del mes 3 del libro son un objetivo de '
            'ejemplo, no lo que le va a pasar al lector.',
        ],
        'cifras': [
            C('Platos dados de alta en la carta', f'{X_MATRIZ}!Datos!D36', 'num'),
            C('Unidades vendidas al mes', f'{X_MATRIZ}!Datos!D32', 'num'),
            C('Ventas netas del mes de la carta', f'{X_MATRIZ}!Datos!I32', 'eur'),
            C('Food cost medio ponderado de la carta', f'{X_MATRIZ}!Datos!H32', 'pct1'),
            C('Margen de contribución medio ponderado de la carta', f'{X_MATRIZ}!Datos!G32'),
            C('Coste por ración del plato de la ficha', f'{X_FICHA}!Ficha!E33'),
            C('PVP objetivo del plato de la ficha, sin IVA', f'{X_FICHA}!Ficha!E34'),
            C('Rendimiento medio ponderado de los tests', f'{X_MERMA}!Test de Rendimiento!E26', 'pct1'),
            C('Platos con las cuatro lecturas en la mejor categoría', f'{X_MATRIZ}!Comparativa!C39', 'num'),
            C('Platos con tres o cuatro lecturas fuera', f'{X_MATRIZ}!Comparativa!C40', 'num'),
            C('Platos Star', f'{X_MATRIZ}!Kasavana-Smith!C33', 'num'),
            C('Platos Dog', f'{X_MATRIZ}!Kasavana-Smith!C36', 'num'),
            C('Platos dentro del objetivo tras poner precio', f'{X_PRECIO}!Por Plato!E37', 'num'),
            C('Food cost del conjunto de la carta con los precios elegidos', f'{X_PRECIO}!Por Plato!E39', 'pct1'),
            C('Diferencia total con los PVP actuales', f'{X_PRECIO}!Por Plato!E41'),
            C('Platos viables en delivery', f'{X_MULTI}!Resumen!B7', 'num'),
            C('Platos a excluir o reformular en delivery', f'{X_MULTI}!Resumen!C7', 'num'),
            C('Food cost efectivo medio en delivery', f'{X_MULTI}!Resumen!D7', 'pct1'),
            C('Margen mensual total en sala', f'{X_MULTI}!Resumen!G5', 'eur'),
            C('Diferencia de margen del delivery frente a la sala', f'{X_MULTI}!Resumen!I7', 'eur'),
            C('Beverage cost ponderado de toda la bodega', f'{X_BEBIDAS}!Resumen Bodega!D8', 'pct1'),
            C('Margen de contribución total de la bodega', f'{X_BEBIDAS}!Resumen Bodega!F8'),
            C('Prime cost del año', f'{X_PRIME}!Mensual!N17', 'pct1'),
            C('Objetivo de prime cost en vigor', f'{X_PRIME}!Parámetros!B11', 'pct0'),
            C('Decisiones registradas en el plan', f'{X_PLAN90}!Decisiones!D27', 'num'),
            C('Impacto total estimado de las decisiones', f'{X_PLAN90}!Decisiones!D31', 'eur'),
            C('Impacto total estimado a doce meses', f'{X_PLAN90}!Decisiones!D34', 'eur'),
            C('Food cost del mes 0 en los indicadores', f'{X_PLAN90}!KPI de Seguimiento!B5', 'pct1'),
            C('Food cost del mes 3 en los indicadores', f'{X_PLAN90}!KPI de Seguimiento!E5', 'pct1'),
            C('Prime cost del mes 0 en los indicadores', f'{X_PLAN90}!KPI de Seguimiento!B6', 'pct1'),
            C('Prime cost del mes 3 en los indicadores', f'{X_PLAN90}!KPI de Seguimiento!E6', 'pct1'),
            C('Platos en carta en el mes 0', f'{X_PLAN90}!KPI de Seguimiento!B9', 'num'),
            C('Platos en carta en el mes 3', f'{X_PLAN90}!KPI de Seguimiento!E9', 'num'),
        ],
        'sector': ['FC-BENCH-01', 'FC-PRIME-04'],
        'tablas': [
            {
                'titulo': 'La carta de ejemplo entera, plato a plato (matriz-multimetodo-carta.xlsx, hoja «Datos»)',
                'src': (X_MATRIZ, 'Datos'),
                'cols': [('Plato', 'B', 'txt'), ('Familia', 'C', 'txt'),
                         ('Uds vendidas', 'D', 'num'), ('Coste por ración (€)', 'E', 'eur2'),
                         ('PVP sin IVA (€)', 'F', 'eur2'), ('MC (€)', 'G', 'eur2'),
                         ('Food cost (%)', 'H', 'pct1'),
                         ('PVP con IVA en sala (€)', 'I', 'eur2')],
                'filas': (5, 29),
                'nota': 'Es la misma carta que aparece en la ficha, en la matriz, en la hoja de '
                        'precios y en el simulador multicanal: todo lo que se lee en esta guía '
                        'sale de estas líneas.',
            },
            {
                'titulo': 'La misma carta en el canal de reparto (simulador-repricing-multicanal.xlsx, hoja «Carta»)',
                'src': (X_MULTI, 'Carta'),
                'cols': [('Plato', 'B', 'txt'), ('Coste por ración (€)', 'C', 'eur2'),
                         ('PVP en sala sin IVA (€)', 'D', 'eur2'),
                         ('Food cost en delivery (%)', 'V', 'pct1'),
                         ('PVP necesario en delivery (€)', 'W', 'eur2'),
                         ('Precio techo (€)', 'F', 'eur2'),
                         ('¿Viable?', 'Y', 'txt')],
                'filas': (5, 29),
            },
            {
                'titulo': 'Las decisiones, con responsable y fecha (plan-accion-90-dias.xlsx, hoja «Decisiones»)',
                'src': (X_PLAN90, 'Decisiones'),
                'cols': [('Plato o área', 'B', 'txt'), ('Herramienta de origen', 'C', 'txt'),
                         ('Decisión', 'D', 'txt'), ('Semana', 'F', 'num'),
                         ('Estado', 'H', 'txt'),
                         ('Impacto estimado (€/mes)', 'I', 'eur2')],
                'filas': (5, 24),
            },
            {
                'titulo': 'Los indicadores del trimestre (plan-accion-90-dias.xlsx, hoja «KPI de Seguimiento»)',
                'src': (X_PLAN90, 'KPI de Seguimiento'),
                'cols': [('KPI', 'A', 'txt'), ('Mes 0', 'B', 'num1'), ('Mes 3', 'E', 'num1'),
                         ('Variación mes 3 vs mes 0', 'H', 'num1'),
                         ('Lectura', 'J', 'txt')],
                'filas': (5, 12),
                'nota': 'Las cifras del mes 3 son el objetivo con el que se sembró el libro para '
                        'que veas cómo se lee la tabla, no una previsión de resultados.',
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO presentar el caso como un cliente real, un restaurante '
            'concreto o un proyecto identificable: es un caso modelado y hay que '
            'escribirlo así en el primer párrafo.',
            'PROHIBIDO presentar el impacto estimado del plan como un resultado '
            'conseguido: es una estimación, y las columnas de «conseguido» del '
            'libro están a cero a propósito, porque el trabajo aún no se ha '
            'hecho.',
            'NO sumes ni proyectes cifras nuevas: los totales del caso están '
            'calculados en los libros y son los que te doy.',
        ],
    },
    {
        'n': 20, 'titulo': 'Cuándo tu Excel se Queda Corto',
        'resumen_indice': 'el criterio para saltar de la hoja de cálculo al software y a los agentes de IA, con la cuenta delante.',
        'palabras': 1400, 'bloques': 2,
        'objetivo': 'Cerrar con honestidad: decir dónde acaba la hoja de cálculo, '
                    'qué resuelve un software y qué resuelve un agente de IA, '
                    'sin vender la guía como sustituto de nada ni al revés.',
        'epigrafes': [
            'Las cuatro señales de que la hoja se te ha quedado pequeña',
            'Qué te da un software que la hoja no te da',
            'Qué te da un agente de inteligencia artificial',
            'La cuenta: cuánto cuesta cada salto',
            'El orden correcto: criterio primero, automatización después',
        ],
        'puntos': [
            'Las cuatro señales: más de un local, precios de proveedor que '
            'cambian a diario, inventario que no se puede llevar a mano, y más '
            'de una persona tocando la misma hoja.',
            'Lo que da un software: precios que entran solos desde el albarán, '
            'escandallos que se recalculan sin abrir nada y trazabilidad de '
            'quién cambió qué.',
            'Lo que da un agente de inteligencia artificial: redacción de fichas, '
            'propuestas de reformulación y lectura de la carta en lenguaje '
            'natural. No sustituye al criterio de este libro: lo aplica más '
            'rápido.',
            'La frase que ordena el capítulo: esta guía te da el criterio; el '
            'software te da la automatización. Un software de gestión de '
            'escandallos y carta cuesta del orden de 1.100 € al año por local, '
            'IVA aparte, así que el salto se hace cuando el tiempo que ahorra '
            'vale más que eso.',
            'Explicar que el mantenimiento tiene coste aunque se quede en Excel: '
            'el plan de 90 días del pack tiene hitos y responsables, y si nadie '
            'los cierra la herramienta no vale nada.',
            'Cierre honesto con la plataforma de AI Chef Pro: se dice qué hace y '
            'para quién, sin prometer resultados y sin presentarla como '
            'obligatoria para aprovechar la guía.',
        ],
        'cifras': [
            C('Hitos registrados en el calendario de 90 días', f'{X_PLAN90}!Calendario 90 Días!D33', 'num'),
            C('Hitos pendientes', f'{X_PLAN90}!Calendario 90 Días!D35', 'num'),
            C('Avance del calendario', f'{X_PLAN90}!Calendario 90 Días!D36', 'pct0'),
            C('Decisiones registradas', f'{X_PLAN90}!Decisiones!D27', 'num'),
            C('Objetivo de cierre a 90 días', f'{X_PLAN90}!Decisiones!D35', 'pct0'),
            C('Impacto total estimado de las decisiones', f'{X_PLAN90}!Decisiones!D31', 'eur'),
            C('Impacto total estimado a doce meses', f'{X_PLAN90}!Decisiones!D34', 'eur'),
            C('Decisiones que salen de la matriz multi-método', f'{X_PLAN90}!Decisiones!C51', 'num'),
            C('Impacto estimado de las decisiones de la matriz', f'{X_PLAN90}!Decisiones!D51', 'eur'),
            C('Decisiones que salen del simulador multicanal', f'{X_PLAN90}!Decisiones!C52', 'num'),
            C('Platos dados de alta en la carta de ejemplo', f'{X_MATRIZ}!Datos!D36', 'num'),
        ],
        'sector': ['FC-FUENTES-03'],
        'tablas': [
            {
                'titulo': 'El avance del plan por bloque de trabajo (plan-accion-90-dias.xlsx, hoja «Calendario 90 Días»)',
                'src': (X_PLAN90, 'Calendario 90 Días'),
                'cols': [('Bloque', 'C', 'txt'), ('Hitos', 'D', 'num'),
                         ('Hechos', 'E', 'num'), ('Avance (%)', 'F', 'pct0')],
                'filas': (40, 44),
                'nota': 'El libro se entrega con todo a cero: el avance lo escribe quien hace el '
                        'trabajo, y eso es exactamente lo que ningún software hace por ti.',
            },
            {
                'titulo': 'De qué herramienta sale cada decisión (plan-accion-90-dias.xlsx, hoja «Decisiones»)',
                'src': (X_PLAN90, 'Decisiones'),
                'cols': [('Herramienta de origen', 'B', 'txt'), ('Decisiones', 'C', 'num'),
                         ('Impacto estimado (€/mes)', 'D', 'eur2'),
                         ('Impacto conseguido (€/mes)', 'E', 'eur2')],
                'filas': (48, 54),
            },
        ],
        'prohibido': NO_COMUN + [
            'PROHIBIDO presentar esta guía como sustituto funcional de un '
            'software de gestión, y prohibido presentar el software como '
            'sustituto del criterio: la frase del capítulo distingue las dos '
            'cosas y no se puede difuminar.',
            'NO des precios de ningún producto de AI Chef Pro ni de ninguna '
            'plataforma concreta de la competencia: la única cifra de coste que '
            'puedes escribir en este capítulo es la del orden de magnitud anual '
            'del software por local que te doy en los puntos.',
            'NO prometas ahorro de tiempo ni retorno de la inversión con '
            'números: se explica el criterio de decisión y se deja la cuenta al '
            'lector.',
            'NO termines con un cierre de venta agresivo: el capítulo acaba con '
            'el criterio, no con una llamada a comprar.',
        ],
    },
]


# --------------------------------------------------------------------------
# El bonus: 12 ejercicios resueltos (SPEC §4.2 y decisión D9)
#
# D9: doce ejercicios de 550-700 palabras con tabla, NO veinte de 300. Cada uno
# es un «capítulo» del pipeline con tres epígrafes fijos —enunciado, resolución
# y lectura del resultado— y una tabla construida desde uno de los ocho libros,
# con las MISMAS cifras y los MISMOS platos que la guía: el lector resuelve
# sobre el material que ya tiene abierto.
# --------------------------------------------------------------------------
EPI_EJ = ['El enunciado y los datos',
          'La resolución, paso a paso',
          'Cómo se lee el resultado']

NO_COMUN_BONUS = NO_COMUN + [
    'Escribe el ejercicio como un ejercicio: enunciado con los datos, '
    'resolución con las operaciones escritas una a una y lectura del resultado. '
    'No lo conviertas en un capítulo teórico.',
    'Escribe las operaciones con los números que te doy y con el mismo formato '
    'con el que te los doy. No inventes datos de partida ni redondees a un '
    'número más bonito.',
    'No remitas al lector a «el capítulo correspondiente de la guía» por su '
    'número: puedes decir de qué trata, pero este documento se lee suelto.',
]

BONUS = [
    {
        'nombre': 'BONUS-ejercicios-resueltos',
        'guia': {
            'titulo': '12 Ejercicios Resueltos de Food Cost e Ingeniería de Menú',
            'subtitulo': 'Bonus del pack «Guía Food Cost + Ingeniería de Menú» · con los datos de las ocho herramientas Excel',
            'cabecera': 'AI Chef Pro · 12 Ejercicios Resueltos',
            'portada_texto': (
                'Doce ejercicios con enunciado, resolución paso a paso y tabla, '
                'resueltos sobre la misma carta de ejemplo que usan las ocho '
                'herramientas Excel de este pack. No hay ninguna cifra '
                'inventada: cada número sale de una celda que puedes abrir y '
                'comprobar. Haz el ejercicio con tus datos al lado y en dos '
                'tardes tendrás tu carta escandallada, clasificada y con '
                'precio.'),
        },
        'gates': {
            'paginas_prometidas': 17,
            'palabras_objetivo': 7500,
            'min_palabras_cap': 450,
            'cifras_extra': (),
            'cifras_ignorar': (),
            'mortalidad_permitida': [],
            'meta': {'title': '12 Ejercicios Resueltos de Food Cost e Ingeniería de Menú',
                     'subject': 'Bonus del pack Guía Food Cost + Ingeniería de Menú · '
                                'Versión 1.0 · septiembre 2026'},
        },
        'capitulos': [
            {
                'n': 1, 'titulo': 'Cantidad Bruta y Coste con Merma',
                'resumen_indice': 'de la cantidad neta de la receta a la cantidad que hay que comprar, y de ahí al coste de la línea.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Fijar la operación que más se hace mal: la merma '
                            'entra dividiendo, y el coste de la línea se calcula '
                            'sobre la cantidad bruta.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: una línea de la ficha con su cantidad neta por '
                    'ración, su merma y su precio por unidad sin IVA. Se pide la '
                    'cantidad bruta a comprar y el coste de la línea.',
                    'Resolución: cantidad bruta igual a cantidad neta dividida '
                    'entre uno menos la merma; coste igual a cantidad bruta por '
                    'precio unitario.',
                    'Mostrar el error de multiplicar por la merma y cuánto se '
                    'queda corto respecto del resultado correcto, sin escribir '
                    'ninguna cifra que no esté en la lista.',
                ],
                'cifras': [
                    C('Cantidad neta por ración de la línea de solomillo', f'{X_FICHA}!Ficha!D10', 'num2'),
                    C('Merma de la línea de solomillo', f'{X_FICHA}!Ficha!F10', 'pct1'),
                    C('Precio por unidad sin IVA del solomillo', f'{X_FICHA}!Ficha!E10'),
                    C('Cantidad bruta a comprar de solomillo', f'{X_FICHA}!Ficha!H10', 'num2'),
                    C('Coste sin IVA de la línea de solomillo', f'{X_FICHA}!Ficha!I10'),
                    C('Cantidad bruta del boniato, con merma del 18 %', f'{X_FICHA}!Ficha!H12', 'num2'),
                    C('Coste total de la ficha, sin IVA', f'{X_FICHA}!Ficha!E32'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Las líneas de la ficha, con la cantidad bruta calculada',
                    'src': (X_FICHA, 'Ficha'),
                    'cols': [('Ingrediente', 'B', 'txt'), ('Cantidad neta/ración', 'D', 'num2'),
                             ('Merma (%)', 'F', 'pct1'),
                             ('Cantidad bruta a comprar', 'H', 'num2'),
                             ('Precio/ud sin IVA (€)', 'E', 'eur2'),
                             ('Coste sin IVA (€)', 'I', 'eur2')],
                    'filas': (10, 29),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 2, 'titulo': 'Test de Rendimiento con Subproductos',
                'resumen_indice': 'cuánto cuesta el kilo limpio cuando el recorte se aprovecha y cuánto cuando no.',
                'palabras': 640, 'bloques': 1,
                'objetivo': 'Calcular el coste del kilo limpio de una pieza '
                            'entera y decidir si compensa aprovechar el '
                            'subproducto.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: una lubina entera con su peso bruto, su precio '
                    'por kilo, el peso limpio que ha dado y los kilos de '
                    'subproducto aprovechable con su valor de uso.',
                    'Resolución: rendimiento igual a peso limpio entre peso '
                    'bruto; coste de compra igual a peso bruto por precio; coste '
                    'neto por kilo limpio igual a coste de compra menos el valor '
                    'de los subproductos, dividido entre el peso limpio.',
                    'Lectura: comparar el coste neto por kilo limpio con el '
                    'precio por kilo bruto y explicar que la diferencia es lo '
                    'que se paga por lo que va a la basura.',
                ],
                'cifras': [
                    C('Rendimiento de la lubina entera', f'{X_MERMA}!Test de Rendimiento!H6', 'pct1'),
                    C('Coste neto por kilo limpio sin aprovechar el subproducto', f'{X_MERMA}!Test de Rendimiento!M6'),
                    C('Coste neto por kilo limpio aprovechando el subproducto', f'{X_MERMA}!Test de Rendimiento!N6'),
                    C('Sobrecoste de la lubina sobre el precio del kilo bruto', f'{X_MERMA}!Test de Rendimiento!P6'),
                    C('Ahorro por aprovechar las cabezas de la gamba', f'{X_MERMA}!Test de Rendimiento!O15'),
                    C('Rendimiento medio ponderado de los tests', f'{X_MERMA}!Test de Rendimiento!E26', 'pct1'),
                    C('Valor de uso total de los subproductos', f'{X_MERMA}!Test de Rendimiento!E29'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Diez tests con su coste del kilo limpio, con y sin aprovechar el recorte',
                    'src': (X_MERMA, 'Test de Rendimiento'),
                    'cols': [('Producto', 'B', 'txt'), ('Peso bruto (kg)', 'C', 'num2'),
                             ('Peso limpio (kg)', 'E', 'num2'),
                             ('Subproductos (kg)', 'F', 'num2'),
                             ('Valor de uso (€/kg)', 'G', 'eur2'),
                             ('Coste neto sin aprovechar (€/kg)', 'M', 'eur2'),
                             ('Coste neto aprovechando (€/kg)', 'N', 'eur2'),
                             ('Ahorro (€/kg)', 'O', 'eur2')],
                    'filas': (6, 20),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 3, 'titulo': 'Food Cost Real de un Mes',
                'resumen_indice': 'stock inicial más compras menos stock final, y el porcentaje sobre la venta neta.',
                'palabras': 610, 'bloques': 1,
                'objetivo': 'Calcular el consumo real del periodo y su '
                            'porcentaje sobre ventas, y ver la diferencia con '
                            'usar las compras como si fueran el consumo.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: un mes con su stock inicial, sus compras, su '
                    'stock final y sus ventas netas.',
                    'Resolución: consumo igual a stock inicial más compras menos '
                    'stock final; food cost igual a consumo entre ventas netas.',
                    'Lectura: comparar el resultado con el que habría salido '
                    'usando las compras, y explicar en qué dirección engaña cada '
                    'vez que el almacén sube o baja.',
                ],
                'cifras': [
                    C('Ventas netas totales de enero', f'{X_PRIME}!Mensual!D5', 'eur'),
                    C('Consumo de materia prima de enero', f'{X_PRIME}!Mensual!H5', 'eur'),
                    C('Food cost de enero', f'{X_PRIME}!Mensual!I5', 'pct1'),
                    C('Compras del año', f'{X_PRIME}!Mensual!F17', 'eur'),
                    C('Consumo real del año', f'{X_PRIME}!Mensual!H17', 'eur'),
                    C('Ventas netas totales del año', f'{X_PRIME}!Mensual!D17', 'eur'),
                    C('Food cost del año', f'{X_PRIME}!Mensual!I17', 'pct1'),
                    C('Food cost objetivo del cuadro de mando', f'{X_PRIME}!Parámetros!B21', 'pct0'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Del stock al consumo, mes a mes',
                    'src': (X_PRIME, 'Mensual'),
                    'cols': [('Mes', 'A', 'txt'), ('Stock inicial (€)', 'E', 'eur'),
                             ('Compras (€)', 'F', 'eur'), ('Stock final (€)', 'G', 'eur'),
                             ('Consumo (€)', 'H', 'eur'),
                             ('Ventas netas (€)', 'D', 'eur'),
                             ('Food cost (%)', 'I', 'pct1')],
                    'filas': (5, 17),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 4, 'titulo': 'El Mismo Plato por los Cuatro Métodos',
                'resumen_indice': 'factor, margen objetivo, mercado y valor percibido aplicados al mismo coste por ración.',
                'palabras': 660, 'bloques': 1,
                'objetivo': 'Ver los cuatro precios que salen del mismo plato y '
                            'entender por qué el factor se rompe en los platos '
                            'de coste alto.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: un plato de coste alto —el chuletón— con su '
                    'coste por ración, el food cost objetivo, el margen objetivo '
                    'en euros y los precios de mercado y de valor percibido.',
                    'Resolución: precio por factor igual a coste entre food cost '
                    'objetivo; precio por margen igual a coste más margen '
                    'objetivo; con los precios de mercado y de valor percibido lo '
                    'que se calcula es el food cost resultante.',
                    'Lectura: el precio por factor es inservible en este plato, y '
                    'el capítulo del ejercicio explica por qué eso no es un fallo '
                    'de la hoja sino del método.',
                ],
                'cifras': [
                    C('Food cost objetivo global', f'{X_PRECIO}!Por Plato!E5', 'pct0'),
                    C('PVP del chuletón por factor', f'{X_PRECIO}!Por Plato!K20'),
                    C('PVP del chuletón por margen objetivo', f'{X_PRECIO}!Por Plato!L20'),
                    C('PVP elegido para el chuletón', f'{X_PRECIO}!Por Plato!Q20'),
                    C('Food cost final del chuletón', f'{X_PRECIO}!Por Plato!T20', 'pct1'),
                    C('PVP actual del chuletón en carta', f'{X_PRECIO}!Por Plato!V20'),
                    C('PVP de las croquetas por factor', f'{X_PRECIO}!Por Plato!K9'),
                    C('PVP actual de las croquetas', f'{X_PRECIO}!Por Plato!V9'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'Los cuatro métodos sobre la misma carta',
                    'src': (X_PRECIO, 'Por Plato'),
                    'cols': [('Plato', 'B', 'txt'), ('Coste/ración (€)', 'D', 'eur2'),
                             ('A · PVP por factor (€)', 'K', 'eur2'),
                             ('B · PVP por margen (€)', 'L', 'eur2'),
                             ('FC con el precio de mercado (%)', 'O', 'pct1'),
                             ('FC con el valor percibido (%)', 'P', 'pct1'),
                             ('PVP elegido sin IVA (€)', 'Q', 'eur2')],
                    'filas': (9, 33),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 5, 'titulo': 'El IVA de una Bebida, Canal por Canal',
                'resumen_indice': 'la misma botella en sala y para llevar: dos tipos y dos precios al cliente.',
                'palabras': 600, 'bloques': 1,
                'objetivo': 'Aplicar la matriz fiscal a un caso concreto y ver '
                            'que el precio que ve el cliente cambia sin que '
                            'cambie ni el coste ni el margen.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: una botella de vino con su precio de venta sin '
                    'IVA en sala. Se pide el precio con IVA en sala y el precio '
                    'con IVA si el cliente se la lleva.',
                    'Resolución: en sala hay servicio de hostelería y se aplica '
                    'el tipo reducido; sin servicio hay entrega de bienes y la '
                    'bebida alcohólica queda excluida del reducido, así que va al '
                    'general.',
                    'Lectura: si mantienes el mismo precio al público en los dos '
                    'canales, la base imponible que te queda para llevar es menor '
                    'y el margen baja sin que nadie haya subido un coste.',
                ],
                'cifras': [
                    C('IVA repercutido en sala, bebida alcohólica', f'{X_BEBIDAS}!Parámetros!D6', 'pct0'),
                    C('IVA repercutido para llevar, bebida alcohólica', f'{X_BEBIDAS}!Parámetros!D7', 'pct0'),
                    C('IVA repercutido para llevar, refresco azucarado', f'{X_BEBIDAS}!Parámetros!C7', 'pct0'),
                    C('IVA repercutido para llevar, comida', f'{X_BEBIDAS}!Parámetros!B7', 'pct0'),
                    C('PVP de la botella del tinto de la casa en sala, sin IVA', f'{X_BEBIDAS}!Vinos!H5'),
                    C('PVP de esa botella con IVA en sala', f'{X_BEBIDAS}!Vinos!V5'),
                    C('PVP de esa botella con IVA para llevar', f'{X_BEBIDAS}!Vinos!Y5'),
                    C('Coste de compra de esa botella, sin IVA', f'{X_BEBIDAS}!Vinos!D5'),
                ],
                'sector': ['FC-IVA-01', 'FC-IVA-03', 'FC-IVA-04'],
                'tablas': [{
                    'titulo': 'La misma botella, dos canales y dos tipos de IVA',
                    'src': (X_BEBIDAS, 'Vinos'),
                    'cols': [('Vino', 'B', 'txt'),
                             ('PVP botella sin IVA (€)', 'H', 'eur2'),
                             ('IVA en sala (%)', 'U', 'pct0'),
                             ('PVP con IVA en sala (€)', 'V', 'eur2'),
                             ('IVA para llevar (%)', 'X', 'pct0'),
                             ('PVP con IVA para llevar (€)', 'Y', 'eur2')],
                    'filas': (5, 34),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 6, 'titulo': 'Clasificar una Familia con Kasavana & Smith',
                'resumen_indice': 'umbral de popularidad, margen medio ponderado y los cuatro cuadrantes, dentro de una familia.',
                'palabras': 650, 'bloques': 1,
                'objetivo': 'Hacer la clasificación a mano en una familia para '
                            'entender de dónde sale cada etiqueta.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: la familia de entrantes con sus platos, sus '
                    'unidades vendidas y su margen de contribución por unidad.',
                    'Resolución: mix de cada plato dentro de su familia; umbral '
                    'igual al factor por uno entre el número de platos de la '
                    'familia; margen medio ponderado de la familia; y la etiqueta '
                    'que sale de cruzar las dos comparaciones.',
                    'Lectura: explicar que la etiqueta depende del conjunto, así '
                    'que quitar un plato recoloca a los demás.',
                    'Cita el modelo una sola vez y con este nombre exacto: '
                    'Kasavana y Smith (1982).',
                ],
                'cifras': [
                    C('Factor del umbral de popularidad', f'{X_MATRIZ}!Datos!D33', 'pct0'),
                    C('Platos de la familia de entrantes', f'{X_MATRIZ}!Datos!C40', 'num'),
                    C('Unidades vendidas por los entrantes', f'{X_MATRIZ}!Datos!E40', 'num'),
                    C('MC medio ponderado de los entrantes', f'{X_MATRIZ}!Datos!G40'),
                    C('Platos Star de la carta', f'{X_MATRIZ}!Kasavana-Smith!C33', 'num'),
                    C('Platos Plowhorse de la carta', f'{X_MATRIZ}!Kasavana-Smith!C34', 'num'),
                    C('Platos Puzzle de la carta', f'{X_MATRIZ}!Kasavana-Smith!C35', 'num'),
                    C('Platos Dog de la carta', f'{X_MATRIZ}!Kasavana-Smith!C36', 'num'),
                ],
                'sector': ['FC-METODO-01'],
                'tablas': [{
                    'titulo': 'La clasificación plato a plato, con el umbral de su familia al lado',
                    'src': (X_MATRIZ, 'Kasavana-Smith'),
                    'cols': [('Plato', 'B', 'txt'), ('Familia', 'C', 'txt'),
                             ('Uds', 'D', 'num'), ('Mix en su familia (%)', 'E', 'pct1'),
                             ('Umbral (%)', 'F', 'pct1'), ('MC (€)', 'H', 'eur2'),
                             ('Clasificación', 'K', 'txt')],
                    'filas': (5, 29),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 7, 'titulo': 'El Mismo Grupo en Miller y en Pavesic',
                'resumen_indice': 'por qué dos modelos que miran los mismos platos llegan a conclusiones distintas.',
                'palabras': 660, 'bloques': 1,
                'objetivo': 'Ver la discrepancia en acción y saber qué hacer con '
                            'ella.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: un grupo de platos con su food cost porcentual, '
                    'su margen por unidad y sus unidades vendidas.',
                    'Resolución: Miller cruza popularidad con food cost '
                    'porcentual; Pavesic cruza food cost porcentual con el margen '
                    'PONDERADO por unidades. Escribir las dos comparaciones y '
                    'señalar en qué platos cambia la etiqueta.',
                    'Lectura: la discrepancia no es un error, es el aviso de que '
                    'ese plato tiene un porcentaje que no se corresponde con los '
                    'euros que deja.',
                    'Cita los dos modelos una sola vez y con estos nombres '
                    'exactos: Miller (1980) y Pavesic (1983).',
                ],
                'cifras': [
                    C('Platos Winner en Miller', f'{X_MATRIZ}!Miller!C33', 'num'),
                    C('Platos Loser en Miller', f'{X_MATRIZ}!Miller!C35', 'num'),
                    C('Food cost medio ponderado de los Winner', f'{X_MATRIZ}!Miller!F33', 'pct1'),
                    C('Platos Prime en Pavesic', f'{X_MATRIZ}!Pavesic!C33', 'num'),
                    C('Platos Problem en Pavesic', f'{X_MATRIZ}!Pavesic!C36', 'num'),
                    C('MC ponderado total de los Prime', f'{X_MATRIZ}!Pavesic!F33', 'eur'),
                    C('Platos con las cuatro lecturas en la mejor categoría', f'{X_MATRIZ}!Comparativa!C39', 'num'),
                    C('Platos con tres o cuatro lecturas fuera', f'{X_MATRIZ}!Comparativa!C40', 'num'),
                ],
                'sector': ['FC-METODO-02', 'FC-METODO-03'],
                'tablas': [{
                    'titulo': 'Miller y Pavesic sobre el mismo plato, uno al lado del otro',
                    'src': (X_MATRIZ, 'Comparativa'),
                    'cols': [('Plato', 'B', 'txt'), ('Familia', 'C', 'txt'),
                             ('Miller', 'E', 'txt'), ('Pavesic', 'F', 'txt'),
                             ('Lecturas fuera', 'H', 'num'),
                             ('Diagnóstico', 'I', 'txt')],
                    'filas': (5, 29),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 8, 'titulo': 'Goal Value de Dos Platos',
                'resumen_indice': 'un índice por plato frente al objetivo de su familia, sin cuadrantes.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Calcular el índice y entender que sólo dice algo '
                            'comparado con el objetivo de su propia familia.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: dos platos con su food cost porcentual, su precio '
                    'sin IVA y sus unidades vendidas, más los porcentajes de '
                    'coste de personal y de otros costes variables.',
                    'Resolución: escribir el cálculo del índice de cada plato y '
                    'el del objetivo de su familia, que usa las medias '
                    'ponderadas de esa familia.',
                    'Lectura: el índice no tiene unidades y no se compara entre '
                    'familias; lo único que dice es si el plato está por encima '
                    'o por debajo del objetivo de los suyos.',
                    'Cita el modelo una sola vez y con este nombre exacto: '
                    'Hayes y Huffman (1985).',
                ],
                'cifras': [
                    C('Coste de personal sobre ventas usado en el índice', f'{X_MATRIZ}!Goal Value!D33', 'pct0'),
                    C('Otros costes variables sobre ventas usados en el índice', f'{X_MATRIZ}!Goal Value!D34', 'pct0'),
                    C('Platos por encima del objetivo de su familia', f'{X_MATRIZ}!Goal Value!D36', 'num'),
                    C('Platos por debajo del objetivo de su familia', f'{X_MATRIZ}!Goal Value!D37', 'num'),
                    C('Food cost medio ponderado de la carta', f'{X_MATRIZ}!Datos!H32', 'pct1'),
                ],
                'sector': ['FC-METODO-04'],
                'tablas': [{
                    'titulo': 'El índice de cada plato frente al objetivo de su familia',
                    'src': (X_MATRIZ, 'Goal Value'),
                    'cols': [('Plato', 'B', 'txt'), ('PVP sin IVA (€)', 'F', 'eur2'),
                             ('Food cost (%)', 'E', 'pct1'),
                             ('Goal Value del plato', 'G', 'num2'),
                             ('Goal Value objetivo de su familia', 'K', 'num2'),
                             ('Lectura', 'L', 'txt')],
                    'filas': (5, 29),
                    'nota': 'El Goal Value es un índice sin unidades: no es un importe, aunque '
                            'la hoja lo muestre con dos decimales.',
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 9, 'titulo': 'Repricing en Delivery con Packaging y Techo',
                'resumen_indice': 'comisión sobre el precio, envase por plato y el precio máximo que aguanta la aplicación.',
                'palabras': 670, 'bloques': 1,
                'objetivo': 'Calcular el precio que hace falta en el canal de '
                            'reparto y decidir si el plato se queda o se sale.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: un plato con su coste por ración, su precio de '
                    'sala sin IVA, la comisión del canal, el envase por pedido, '
                    'los platos por pedido y el precio techo de la aplicación.',
                    'Resolución: coste efectivo igual a coste por ración más '
                    'envase por plato; food cost efectivo igual a ese coste entre '
                    'el precio por uno menos la comisión; precio necesario igual '
                    'al coste efectivo entre el producto del food cost objetivo '
                    'por uno menos la comisión.',
                    'Lectura: comparar el precio necesario con el techo y decidir. '
                    'Si no cabe, la respuesta no es subir igual, es sacar el '
                    'plato o reformularlo.',
                ],
                'cifras': [
                    C('Comisión de la plataforma en delivery', f'{X_MULTI}!Parámetros!B18', 'pct0'),
                    C('Packaging por pedido en delivery', f'{X_MULTI}!Parámetros!C18'),
                    C('Platos por pedido en delivery', f'{X_MULTI}!Parámetros!D18', 'num1'),
                    C('Packaging por plato en delivery', f'{X_MULTI}!Parámetros!F18'),
                    C('Food cost objetivo en delivery', f'{X_MULTI}!Parámetros!E18', 'pct0'),
                    C('Coste por ración de las croquetas', f'{X_MULTI}!Carta!C5'),
                    C('PVP en sala de las croquetas, sin IVA', f'{X_MULTI}!Carta!D5'),
                    C('Food cost en delivery de las croquetas', f'{X_MULTI}!Carta!V5', 'pct1'),
                    C('PVP necesario en delivery de las croquetas', f'{X_MULTI}!Carta!W5'),
                    C('Precio techo de las croquetas', f'{X_MULTI}!Carta!F5'),
                    C('Platos viables en delivery', f'{X_MULTI}!Resumen!B7', 'num'),
                    C('Platos a excluir o reformular en delivery', f'{X_MULTI}!Resumen!C7', 'num'),
                ],
                'sector': ['FC-DELIV-01', 'FC-DELIV-03'],
                'tablas': [{
                    'titulo': 'La carta en el canal de reparto: precio necesario contra precio techo',
                    'src': (X_MULTI, 'Carta'),
                    'cols': [('Plato', 'B', 'txt'), ('Coste por ración (€)', 'C', 'eur2'),
                             ('PVP en sala sin IVA (€)', 'D', 'eur2'),
                             ('Food cost en delivery (%)', 'V', 'pct1'),
                             ('PVP necesario (€)', 'W', 'eur2'),
                             ('Precio techo (€)', 'F', 'eur2'),
                             ('¿Viable?', 'Y', 'txt')],
                    'filas': (5, 29),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 10, 'titulo': 'Copa o Botella',
                'resumen_indice': 'el mismo vino servido de dos formas: qué cambia en el porcentaje y qué cambia en los euros.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Decidir con números si conviene abrir por copas, y '
                            'ver qué pasa cuando se sirven copas de más.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: una botella con su precio de compra sin IVA, su '
                    'formato, el servicio de copa y los precios de venta de '
                    'botella y de copa.',
                    'Resolución: copas por botella; coste por copa igual al '
                    'precio de compra entre las copas; margen y beverage cost de '
                    'la botella y de la copa.',
                    'Lectura: el porcentaje mejora con la copa, pero el margen en '
                    'euros por botella abierta depende de que se sirvan todas. '
                    'Servir de más se come la diferencia sin que aparezca en '
                    'ninguna hoja.',
                ],
                'cifras': [
                    C('Precio de compra de la botella del tinto de la casa', f'{X_BEBIDAS}!Vinos!D5'),
                    C('Copas por botella', f'{X_BEBIDAS}!Vinos!G5', 'num1'),
                    C('Coste por copa', f'{X_BEBIDAS}!Vinos!L5'),
                    C('Margen por botella', f'{X_BEBIDAS}!Vinos!M5'),
                    C('Margen por copa', f'{X_BEBIDAS}!Vinos!N5'),
                    C('Beverage cost de la botella', f'{X_BEBIDAS}!Vinos!O5', 'pct1'),
                    C('Beverage cost de la copa', f'{X_BEBIDAS}!Vinos!P5', 'pct1'),
                    C('Beverage cost ponderado de los vinos', f'{X_BEBIDAS}!Vinos!T35', 'pct1'),
                    C('Objetivo de beverage cost de los vinos', f'{X_BEBIDAS}!Parámetros!B17', 'pct0'),
                ],
                'sector': ['FC-BEV-01'],
                'tablas': [{
                    'titulo': 'Botella y copa del mismo vino, con su margen y su porcentaje',
                    'src': (X_BEBIDAS, 'Vinos'),
                    'cols': [('Vino', 'B', 'txt'), ('PVP botella sin IVA (€)', 'H', 'eur2'),
                             ('PVP copa sin IVA (€)', 'I', 'eur2'),
                             ('Copas por botella', 'G', 'num1'),
                             ('Coste por copa (€)', 'L', 'eur2'),
                             ('Margen por botella (€)', 'M', 'eur2'),
                             ('Margen por copa (€)', 'N', 'eur2'),
                             ('BC botella (%)', 'O', 'pct1'),
                             ('BC copa (%)', 'P', 'pct1')],
                    'filas': (5, 34),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 11, 'titulo': 'Prime Cost de un Mes y su Semáforo',
                'resumen_indice': 'sumar producto y personal con la Seguridad Social dentro, y compararlo con el objetivo del formato.',
                'palabras': 620, 'bloques': 1,
                'objetivo': 'Calcular el prime cost de un mes concreto y leer el '
                            'semáforo con el objetivo correcto.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: un mes con sus ventas netas, su consumo de '
                    'materia prima, sus salarios brutos y sus otros costes de '
                    'personal, más el porcentaje de Seguridad Social a cargo de '
                    'la empresa y el objetivo del formato.',
                    'Resolución: coste de personal igual a los brutos por uno más '
                    'la Seguridad Social, más los otros costes; food cost y labor '
                    'cost sobre ventas netas; prime cost igual a la suma de los '
                    'dos porcentajes.',
                    'Lectura: comparar con el objetivo del formato y explicar por '
                    'qué el mismo prime cost significa cosas distintas en sala y '
                    'en barra.',
                ],
                'cifras': [
                    C('Seguridad Social a cargo de la empresa', f'{X_PRIME}!Parámetros!B20', 'pct0'),
                    C('Objetivo de prime cost con servicio en mesa', f'{X_PRIME}!Parámetros!B8', 'pct0'),
                    C('Objetivo de prime cost en barra o autoservicio', f'{X_PRIME}!Parámetros!B9', 'pct0'),
                    C('Ventas netas totales de agosto', f'{X_PRIME}!Mensual!D12', 'eur'),
                    C('Coste de personal con Seguridad Social de agosto', f'{X_PRIME}!Mensual!L12', 'eur'),
                    C('Food cost de agosto', f'{X_PRIME}!Mensual!I12', 'pct1'),
                    C('Labor cost de agosto', f'{X_PRIME}!Mensual!M12', 'pct1'),
                    C('Prime cost de agosto', f'{X_PRIME}!Mensual!N12', 'pct1'),
                    C('Lectura del prime cost de agosto', f'{X_PRIME}!Mensual!R12', 'txt'),
                    C('Prime cost del año', f'{X_PRIME}!Mensual!N17', 'pct1'),
                ],
                'sector': ['FC-PRIME-02', 'FC-PRIME-03'],
                'tablas': [{
                    'titulo': 'Los doce meses con su prime cost y su lectura',
                    'src': (X_PRIME, 'Mensual'),
                    'cols': [('Mes', 'A', 'txt'),
                             ('Coste de personal con SS (€)', 'L', 'eur'),
                             ('Food cost (%)', 'I', 'pct1'),
                             ('Labor cost (%)', 'M', 'pct1'),
                             ('Prime cost (%)', 'N', 'pct1'),
                             ('Objetivo (%)', 'O', 'pct1'),
                             ('Lectura', 'R', 'txt')],
                    'filas': (5, 17),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
            {
                'n': 12, 'titulo': 'Menú de Precio Fijo: el Margen lo Decide el Mix',
                'resumen_indice': 'el mismo menú al mismo precio con tres repartos de elección distintos.',
                'palabras': 640, 'bloques': 1,
                'objetivo': 'Comprobar que en un menú cerrado el resultado '
                            'depende de lo que elija la gente, no del precio.',
                'epigrafes': EPI_EJ,
                'puntos': [
                    'Enunciado: un menú con su precio con IVA, sus costes fijos '
                    'por menú, sus opciones por curso con el coste de cada una y '
                    'tres repartos de mix.',
                    'Resolución: base imponible del menú; coste medio de cada '
                    'curso como suma del coste de cada opción por su mix; coste '
                    'total del menú sumando los cursos y los costes fijos; food '
                    'cost y margen por menú, y margen del mes por el número de '
                    'menús servidos.',
                    'Lectura: los tres escenarios dan tres márgenes distintos con '
                    'el mismo precio, y eso señala exactamente dónde hay que '
                    'trabajar: en qué se pide, no en cuánto se cobra.',
                ],
                'cifras': [
                    C('PVP del menú con IVA', f'{X_MATRIZ}!Menú Precio Fijo!C19'),
                    C('Tipo de IVA de restauración en sala', f'{X_MATRIZ}!Menú Precio Fijo!C20', 'pct0'),
                    C('PVP del menú sin IVA', f'{X_MATRIZ}!Menú Precio Fijo!C21'),
                    C('Costes fijos por menú', f'{X_MATRIZ}!Menú Precio Fijo!C22'),
                    C('Menús servidos al mes', f'{X_MATRIZ}!Menú Precio Fijo!C24', 'num'),
                    C('Coste medio total del menú con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B38'),
                    C('Coste medio total del menú en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C38'),
                    C('Coste medio total del menú en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D38'),
                    C('Food cost del menú con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B39', 'pct1'),
                    C('Food cost del menú en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C39', 'pct1'),
                    C('Food cost del menú en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D39', 'pct1'),
                    C('Margen por menú con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B40'),
                    C('Margen del mes con el mix base', f'{X_MATRIZ}!Menú Precio Fijo!B41'),
                    C('Margen del mes en el escenario A', f'{X_MATRIZ}!Menú Precio Fijo!C41'),
                    C('Margen del mes en el escenario B', f'{X_MATRIZ}!Menú Precio Fijo!D41'),
                ],
                'sector': [],
                'tablas': [{
                    'titulo': 'El mismo menú y el mismo precio, tres resultados según el mix',
                    'src': (X_MATRIZ, 'Menú Precio Fijo'),
                    'cols': [('Concepto', 'A', 'txt'), ('Mix base', 'B', 'eur2'),
                             ('Escenario A', 'C', 'eur2'), ('Escenario B', 'D', 'eur2')],
                    'filas': (34, 41),
                }],
                'prohibido': NO_COMUN_BONUS,
            },
        ],
    },
]


# --------------------------------------------------------------------------
# Erratas que el gate ortográfico marca y NO lo son: nombres propios, términos
# del oficio y extranjerismos que no están en el léxico del blog. El gate
# normaliza los acentos antes de buscar, así que también propone «reparar»
# palabras bien escritas con tilde que el corpus nunca usó.
# --------------------------------------------------------------------------
_ERRATAS_OK = (
    # Autores y modelos de ingeniería de menú
    'Kasavana', 'Smith', 'Miller', 'Pavesic', 'Hayes', 'Huffman', 'LeBruto',
    'Quain', 'Ashley', 'Wansink', 'Painter', 'Ittersum', 'Kimes', 'Sessarego',
    'Cornell', 'Emerald', 'Plowhorse', 'Plowhorses', 'Puzzle', 'Puzzles',
    'Sleeper', 'Sleepers', 'Winner', 'Winners', 'Marginal', 'Loser', 'Losers',
    # Vocabulario del oficio y del canal
    'beverage', 'delivery', 'packaging', 'away', 'takeaway', 'catering',
    'buffet', 'escandallo', 'escandallos', 'escandallar', 'reescandallado',
    'escandallado', 'costeo', 'roner', 'Horeca', 'Hostelería', 'sommelier',
    'ponderado', 'ponderada', 'repricing',
    # Plataformas, marcas y fuentes citadas
    'Glovo', 'Deliveroo', 'Rappi', 'PedidosYa', 'Mercasa', 'CaixaBankLab',
    'CaixaBank', 'elBulli', 'Toast', 'Cucinovo', 'qamarero',
    # Producto y familia
    'Repsol', 'Michelin', 'Tempranillo', 'Rioja', 'boniato', 'ventresca',
    'cebolleta', 'alcachofa', 'lubina', 'merluza', 'albóndigas', 'calabaza',
    # Palabras correctas que el léxico del blog no contiene o que el gate
    # propone «reparar» por la normalización de acentos
    'reformular', 'reformularlo', 'resubir', 'rediseñar', 'retirar',
    'superreducido', 'repercutido', 'soportado', 'deducible', 'vinculante',
    'consolidado', 'edulcorantes', 'gaseosas', 'panificables', 'tubérculos',
    'auditable', 'trazabilidad', 'emplatada', 'disparadores', 'señuelo',
    'replicación', 'retractados',
)
GUIA['gates']['erratas_permitidas'] = _ERRATAS_OK
for _b in BONUS:
    _b['gates']['erratas_permitidas'] = _ERRATAS_OK
