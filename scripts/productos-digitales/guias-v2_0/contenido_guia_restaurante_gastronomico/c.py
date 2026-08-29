# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_gastronomico/c.py — contenido del **grupo C**
(cocina, carta y sala, `guias-v2-SPEC.md` §4) para la guía **Cómo Montar un
Restaurante Gastronómico (65 plazas, 85 EUR)**.

Aquí sólo hay datos: las filas, los textos, los importes y los parámetros
PROPIOS de esta guía. La mecánica (detección de modelo, merma que entra en el
coste, Kasavana & Smith, valoración de la bodega, horas y coste de la brigada,
registro de jornada) vive en `grupo_c.py` y vale para las 8.

FUENTE DE CADA CIFRA — es la regla dura de este paquete
------------------------------------------------------
Cada valor lleva su `fuente`, y sólo hay cuatro:

  · `SPEC §x`            — está escrito en `guias-v2-SPEC.md`.
  · `fichero original`   — ya estaba en el `.xlsx` o en el `.docx` de la guía y
                           no se inventa: se conserva o se convierte.
  · `guía cap. N`        — sale del texto de `guia-restaurante-gastronomico.docx`
                           (los rangos de precio de carta, el multiplicador de
                           bodega), citando el capítulo.
  · `ejemplo editable`   — dato de EJEMPLO para que la herramienta funcione al
                           abrirla, en celda verde y anunciado como ejemplo en
                           la propia hoja. No es un dato del sector y no se
                           publica como tal en ningún sitio.

Lo que **no** está aquí, y por qué:

  · **Salarios de la brigada.** El cap. 13 los tiene, pero dos de sus puestos
    («Ayudante de cocina 16.000-19.000 EUR», «Plonge 15.000-17.000 EUR») quedan
    por debajo del SMI vigente (17.094 EUR/año, RD 126/2026), y §7-bis.5 y
    §7-bis.16 prohíben publicar un rango por debajo del mínimo legal. Subirlos
    «a ojo» sería inventar la tabla del convenio provincial, que es quien
    manda. Así que la columna «Bruto anual» se entrega VACÍA y verde, con el
    SMI en celda y un semáforo rojo que se enciende solo. [DOM-13]
  · **Ingredientes del escandallo.** El libro se entrega con 20 líneas en
    blanco y así se queda: una ficha técnica es del chef, y precargar 20
    ingredientes con precio sería inventar una lista de la compra. Lo que
    cambia es que ahora la hoja CALCULA (merma, raciones, food cost, IVA) y que
    con el libro en blanco devuelve `""` en vez de 0,00 EUR.
  · **Las 50 referencias de la bodega.** Igual: la carta de vinos es del
    sommelier. Lo que se añade es el desplegable de tipo, las columnas que
    faltaban y la fila TOTAL que valora el inventario.

⚠️ ESPACIO FINO (U+202F) y GUION NO SEPARABLE (U+2011): se referencian por
escape (`N`, `G`), nunca escribiendo el carácter. Al pasar por un heredoc del
shell degeneran en espacio y guion normales y ninguna sustitución encuentra su
patrón (CLAUDE.md).
"""

N = '\u202f'      # espacio fino (U+202F), SIEMPRE por escape
G = '\u2011'      # guion no separable (U+2011), SIEMPRE por escape


# ==========================================================================
# escandallo-maestro.xlsx (modelo E1) — §4.1
# ==========================================================================
#: El único parámetro propio de esta guía: el food cost objetivo, que el
#: fichero ya traía en `Escandallo!H4` como la CADENA `'28%'` (por eso ninguna
#: fórmula podía leerlo). `grupo_c.py` la convierte a número 0,28 leyéndola del
#: propio fichero; este valor es sólo la red por si un hermano llegara sin ella.
#: Coherente con el cap. 3, «Modelo 2: carta + menú degustación, food cost
#: 28-32 %», y con el cap. 15, «menú degustación, food cost objetivo 25-28 %».
ESCANDALLO = {
    'food_cost_objetivo': 0.28,        # fuente: fichero original (H4 = '28%')
    'fuente': 'fichero original: escandallo-maestro.xlsx!Escandallo!H4',
}


# ==========================================================================
# menu-engineering-matrix.xlsx (modelo M1) — §4.2
# ==========================================================================
#: §4.2 pide precargar 12-15 platos de ejemplo «coherentes con la carta que
#: describe el cap. 15», porque la hoja se entrega con **25 filas vacías y ni
#: una fórmula que clasificar**: sin datos no hay matriz que enseñar y el BONUS
#: 5 de la landing («matrix automática… recomendaciones al instante») seguiría
#: sin existir al abrirlo.
#:
#: De dónde sale cada número:
#:   · **PVP** — de las bandas del **cap. 15** de la guía: «Carta: entrantes
#:     18-28 EUR, principales 32-48 EUR, postres 14-22 EUR», «Menú degustación
#:     largo (8-12 pases): 90-180 EUR», «corto (5-7 pases): 55-90 EUR».
#:     Ninguno se sale de su banda.
#:   · **Coste** — el food cost objetivo del propio producto aplicado al PVP:
#:     cap. 3 «Modelo 2 … food cost 28-32 %» para la carta y cap. 15 «food cost
#:     objetivo 25-28 %» para los menús degustación. Los dos menús van al 27 %.
#:   · **Uds vendidas/mes** — EJEMPLO. No hay ninguna fuente de mix de ventas
#:     para un restaurante que aún no ha abierto, y no se finge que la haya:
#:     son cifras redondas, en celda verde, y la hoja dice que se sustituyan.
#:
#: Los platos son de EJEMPLO y así se anuncia en la hoja. Están escritos con el
#: vocabulario del cap. 16 (Km0, temporada, fermentaciones propias: miso,
#: garum, kimchi) para que el comprador reconozca su propio recetario.
MENU = {
    'categorias': ['Entrante', 'Principal', 'Postre', 'Menú degustación',
                   'Maridaje'],
    'platos': [
        # --- Entrantes: banda 18-28 EUR (cap. 15) ------------------------
        {'plato': 'Tartar de vaca madurada, yema curada y mostaza antigua',
         'categoria': 'Entrante', 'pvp': 24.0, 'coste': 7.20, 'uds': 90,
         'fuente_pvp': 'guía cap. 15 (entrantes 18-28 EUR)',
         'fuente_coste': 'food cost 30 % sobre PVP (cap. 3, modelo 2: 28-32 %)',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Gamba roja, su jugo y aceite de cebollino',
         'categoria': 'Entrante', 'pvp': 28.0, 'coste': 9.80, 'uds': 75,
         'fuente_pvp': 'guía cap. 15 (entrantes 18-28 EUR)',
         'fuente_coste': 'food cost 35 % — producto caro de temporada, el que '
                         'tira del food cost medio hacia arriba',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Alcachofa a la brasa, garum de anchoa y avellana',
         'categoria': 'Entrante', 'pvp': 19.0, 'coste': 5.20, 'uds': 110,
         'fuente_pvp': 'guía cap. 15 (entrantes 18-28 EUR)',
         'fuente_coste': 'food cost 27 % (garum de elaboración propia, cap. 16)',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Ostra, encurtido de manzana y agua de pepino',
         'categoria': 'Entrante', 'pvp': 22.0, 'coste': 7.50, 'uds': 60,
         'fuente_pvp': 'guía cap. 15 (entrantes 18-28 EUR)',
         'fuente_coste': 'food cost 34 %',
         'fuente_uds': 'ejemplo editable'},
        # --- Principales: banda 32-48 EUR (cap. 15) -----------------------
        {'plato': 'Merluza de pincho, pil' + G + 'pil ligero y algas',
         'categoria': 'Principal', 'pvp': 36.0, 'coste': 11.90, 'uds': 95,
         'fuente_pvp': 'guía cap. 15 (principales 32-48 EUR)',
         'fuente_coste': 'food cost 33 %',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Pichón asado, remolacha y su jugo',
         'categoria': 'Principal', 'pvp': 44.0, 'coste': 14.50, 'uds': 55,
         'fuente_pvp': 'guía cap. 15 (principales 32-48 EUR)',
         'fuente_coste': 'food cost 33 %',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Cochinillo confitado, manzana y miso propio',
         'categoria': 'Principal', 'pvp': 38.0, 'coste': 10.30, 'uds': 80,
         'fuente_pvp': 'guía cap. 15 (principales 32-48 EUR)',
         'fuente_coste': 'food cost 27 % (miso de elaboración propia, cap. 16)',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Rodaballo salvaje a la brasa, beurre blanc de kimchi',
         'categoria': 'Principal', 'pvp': 46.0, 'coste': 16.10, 'uds': 40,
         'fuente_pvp': 'guía cap. 15 (principales 32-48 EUR)',
         'fuente_coste': 'food cost 35 % — pescado salvaje de lonja',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Arroz de verduras de temporada y kombu',
         'categoria': 'Principal', 'pvp': 32.0, 'coste': 7.80, 'uds': 70,
         'fuente_pvp': 'guía cap. 15 (principales 32-48 EUR)',
         'fuente_coste': 'food cost 24 % — plato de huerta, el más rentable',
         'fuente_uds': 'ejemplo editable'},
        # --- Postres: banda 14-22 EUR (cap. 15) ---------------------------
        {'plato': 'Torrija de brioche y helado de leche de oveja',
         'categoria': 'Postre', 'pvp': 15.0, 'coste': 3.90, 'uds': 120,
         'fuente_pvp': 'guía cap. 15 (postres 14-22 EUR)',
         'fuente_coste': 'food cost 26 %',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Chocolate, café y cardamomo',
         'categoria': 'Postre', 'pvp': 18.0, 'coste': 5.00, 'uds': 85,
         'fuente_pvp': 'guía cap. 15 (postres 14-22 EUR)',
         'fuente_coste': 'food cost 28 %',
         'fuente_uds': 'ejemplo editable'},
        {'plato': 'Cítricos, hinojo y sorbete de yuzu',
         'categoria': 'Postre', 'pvp': 16.0, 'coste': 4.80, 'uds': 50,
         'fuente_pvp': 'guía cap. 15 (postres 14-22 EUR)',
         'fuente_coste': 'food cost 30 %',
         'fuente_uds': 'ejemplo editable'},
        # --- Los dos menús degustación NO se precargan, y es de oficio ----
        # Kasavana & Smith se aplica DENTRO de una familia de carta, no
        # mezclando un menú degustación de 145 EUR con un postre de 15 EUR: el
        # margen de contribución medio ponderado lo arrastra el menú y casi
        # todo lo demás cae a «Plowhorse» o «Dog». Medido con estas mismas 14
        # filas: con los dos menús dentro salían 2 Stars, 9 Plowhorses, 3 Dogs
        # y NINGÚN Puzzle (MC medio 34,63 EUR); sin ellos, 4 Stars, 6
        # Plowhorses, 1 Puzzle y 1 Dog (MC medio 18,58 EUR), que es una matriz
        # que se puede enseñar. La categoría «Menú degustación» sigue en el
        # desplegable para quien quiera analizarlos aparte, y las
        # Instrucciones lo advierten.
    ],
}


# ==========================================================================
# budget-bodega.xlsx — §4.3
# ==========================================================================
#: Desplegable de la columna «Tipo». No es una cifra: es la taxonomía con la
#: que un sommelier ordena una carta de 300-500 referencias (cap. 12). Poner el
#: tipo en lista y no en texto libre es lo que permite después filtrar y sumar
#: por familia sin pelearse con «tinto» / «Tinto» / «TINTO».
BODEGA = {
    'tipos': ['Tinto', 'Blanco', 'Rosado', 'Espumoso', 'Generoso',
              'Dulce', 'Sake', 'Otros'],
    'fuente': 'guía cap. 12 (carta de 300-500 referencias; multiplicador '
              'x2,5-x3,5 sobre coste; food cost de vino 28-40 %)',
}


# ==========================================================================
# plantilla-turnos-brigada.xlsx (modelo T1) — §4.4
# ==========================================================================
#: NO hay salarios aquí, y es una decisión, no un olvido: ver la cabecera del
#: módulo [DOM-13].
#:
#: El headcount tampoco se teclea: `grupo_c.py` cuenta los puestos del cuadrante
#: al abrirlo (§9, gate de recuento) y con esa cifra corrige el título del libro,
#: que decía «(25 personas)» sobre 24 puestos reales — 15 de cocina (C6:C20) y
#: 9 de sala (C22:C30). Las otras tres cifras del mismo producto (el «22-30» del
#: cap. 14, el 21-29 que suman las tablas 2 y 3 del docx y el «25 personas» de
#: la tarjeta del dashboard) son de T7 y T8 [TEC-13 · COM-21 · §7-bis.7].
TURNOS = {
    'salarios': None,       # deliberado: ver DOM-13 en la cabecera
    'headcount': 'medido en tiempo de ejecución (§9)',
}
