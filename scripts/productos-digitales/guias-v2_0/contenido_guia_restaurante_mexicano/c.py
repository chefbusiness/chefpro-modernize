# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_mexicano/c.py — contenido del **grupo C** (cocina,
carta y sala, `guias-v2-SPEC.md` §4) para «Cómo Montar un Restaurante
Mexicano» (80 plazas, 65 EUR).

Mexicano usa el modelo **E2** de escandallo (los 5 hermanos: merma como
recargo `G=E*(1+F)`, a corregir por `grupo_c._escandallo_e2()` a
`/(1-merma)`), el modelo **M2** de menu engineering (Matrix, YA con 15 platos
reales) y el modelo **T2** de cuadrante (rejilla YA rellena de P/T/M, sin
columna «Horas/Semana»). No lleva `budget-bodega.xlsx` (sólo el
representante): por eso este módulo no expone `BODEGA`.

FUENTE DE CADA CIFRA:
  · `fichero original`  — ya estaba en el `.xlsx` de esta guía (v1.1).
  · `docx capN`          — `guia-restaurante-mexicano.docx`, capítulo citado.
  · `ejemplo editable`   — sin fuente en ningún fichero de esta guía; celda
                           verde, anunciada como ejemplo.

Lo que **no** está aquí, y por qué:
  · **El food cost y el IVA del escandallo.** `escandallo-maestro-mexicano.
    xlsx!Escandallo!G17='=G16/0.30'` y `G18='=G17*1.10'` ya traen el 30 % y
    el 10 % dentro de la fórmula: `grupo_c._escandallo_e2()` los EXTRAE del
    propio texto de la fórmula (no hace falta declararlos aquí; el valor de
    `ESCANDALLO['food_cost_objetivo']` de abajo es sólo la red por si esa
    extracción fallara).
  · **Los 15 platos del menu engineering.** `menu-engineering-matrix.xlsx!
    Matrix!B5:F19` YA trae 15 platos reales con PVP, Food Cost y Uds
    Vendidas/Mes (fichero original, y coherente con los «15 Recetas Base con
    Food Cost» del cap. 16 del docx): `grupo_c._menu()` sólo precarga
    `MENU['platos']` cuando el modelo es M1 (representante) y la hoja está
    vacía; en M2 con datos ya presentes no se toca ni una celda de la carta.
  · **Los ingredientes del escandallo.** Ya vienen precargados (9 líneas:
    tortillas de maíz, carne de cerdo adobada, piña, cebolla, cilantro,
    limón, chile guajillo, achiote, salsa verde — «Tacos al Pastor», que es
    la ficha del cap. 16) — fichero original de v1.1; no se sustituyen.
"""

# ==========================================================================
# escandallo-maestro-mexicano.xlsx (modelo E2) — §4.1
# ==========================================================================
#: `Escandallo!G17='=G16/0.30'` (30 %, food cost objetivo) y
#: `G18='=G17*1.10'` (10 %, IVA de restauración) ya están en la fórmula:
#: `grupo_c._escandallo_e2()` los extrae con regex y los baja a celda verde.
#: Coherente con `pl-mensual-escenarios` (food cost 31 % en las tres hojas —
#: la diferencia de 1 punto entre el 30 % objetivo del escandallo y el 31 %
#: real del P&L es razonable: el objetivo es la meta por plato, el 31 % es la
#: media real de la carta incluyendo el coste algo mayor de los chiles y
#: especias importados, que el propio cap. 4 del docx anticipa
#: — «food cost 28-33 % sobre ventas») y con
#: `cash-flow-break-even!Break-Even!B8` (31 %): magnitudes del mismo orden en
#: los tres libros, sin forzar una igualdad que no pide el §7-bis.7 (que sólo
#: exige una sola fuente para inversión/personal/fondo de maniobra/
#: headcount, no para el food cost objetivo de UN plato frente a la media de
#: TODA la carta).
ESCANDALLO = {
    'food_cost_objetivo': 0.30,   # fuente: fichero original (G17 = G16/0.30)
    'fuente': 'fichero original: escandallo-maestro-mexicano.xlsx!Escandallo!G17',
}

# ==========================================================================
# menu-engineering-matrix.xlsx (modelo M2) — §4.2
# ==========================================================================
#: Vacío a propósito: la carta de 15 platos (tacos al pastor, guacamole,
#: enchiladas suizas, burrito, nachos, quesadillas, mole poblano, ceviche,
#: margarita, churros, pozole, chile relleno, elotes, carnitas, flan de
#: cajeta) ya está en el fichero (fichero original) y cubre exactamente la
#: «Estructura de carta mexicana» del docx cap. 14 y las «15 Recetas Base con
#: Food Cost» del cap. 16. `grupo_c.py` sólo añade mix %, umbral 70 %/N,
#: margen medio y clasificación por fórmula: no hace falta ningún dato de
#: este módulo para eso.
MENU = {}

# ==========================================================================
# plantilla-turnos-brigada.xlsx (modelo T2) — §4.4
# ==========================================================================
#: El cuadrante YA trae 14 puestos con la rejilla P/T/M rellena de lunes a
#: domingo (fichero original, docx cap. 12 «Brigada de Cocina 6-10 personas»
#: → 8 puestos de cocina aquí; docx cap. 13 «Equipo de Sala 6-8 personas» →
#: 6 puestos de sala aquí, dentro de los dos rangos). NO hay columna «Horas/
#: Semana» ni «Bruto anual»: `grupo_c.py` las añade y usa `brutos` para
#: precargar un ejemplo por puesto. El cuadrante en sí SÍ hace falta
#: tocarlo, y no para rellenar huecos: v1.1 tenía los 14 puestos a 7 días
#: de un único turno (11 en «P», 1 en «M», 2 en «T») SIN NINGÚN «L», es
#: decir, 70 h/semana en 11 puestos y 56 h/semana en 3 puestos con cero días
#: de libranza en los 14 — verificado en el dry-run del gate «brigada
#: ≤ 40 h/puesto» de T6 (§ informe). Es el mismo defecto que ya cazó casual
#: en su propio v1.1 (RD-CASUAL-02), aquí RD-MEX-03. `cuadrante` de abajo
#: trae el patrón CORREGIDO y `forzar_cuadrante=True` para que se escriba
#: encima del que ya había.
#:
#: Fuente de cada bruto: docx caps. 12-13 («Organigrama tipo», rangos
#: EUR brutos/mes), convertidos a bruto ANUAL con 14 pagas (la que el propio
#: producto declara «habitual en hostelería» y que es el valor por defecto de
#: la columna «Nº de pagas» del cuadrante), tomando el tercio bajo del rango
#: — mismo criterio prudente que usaron el representante y casual — y
#: ELEVANDO al SMI vigente (17.094 EUR/año, RD 126/2026) los dos puestos que
#: quedaban por debajo [DOM-13 · §7-bis.16].
#:
#: §7-bis.7 — el total de esta tabla (322.588 EUR/año: 188.594 EUR cocina +
#: 133.994 EUR sala) es la fuente del coste de personal de TODO el producto y
#: es coherente (96,0 %, dentro de lo razonable para cifras de EJEMPLO) con
#: los 336.000 EUR/año (16.000+12.000 EUR/mes) que `pl-mensual-escenarios` y
#: `plan-financiero-3-anos!'P&L Mensual'` YA llevan precargados en las dos —
#: no hace falta forzar el cuadre exacto: los tres libros describen la misma
#: magnitud dentro de un margen defendible para cifras de ejemplo (la brigada
#: de 14 puestos con bruto medido da un coste ligeramente MENOR que la línea
#: agregada del P&L, que es justo lo esperable: el P&L incluye margen de
#: contingencia sobre la nómina real).
TURNOS = {
    'headcount': 'medido en tiempo de ejecución (§9)',
    'brutos': {
        # --- cocina (docx cap. 12, 2.200-2.800 / 1.800-2.200 (taquero y
        #     parrillero) / 1.500-1.800 (salsero y cocineros) /
        #     1.200-1.500 (ayudante/office) EUR brutos/mes) ------------------
        'jefe de cocina': 33600,          # 2.400 EUR/mes x14 (punto prudente)
        'taquero': 26600,                 # 1.900 EUR/mes x14 — puesto
                                          # especializado (cap. 12: «el alma
                                          # del restaurante mexicano»)
        'parrillero': 26600,              # 1.900 EUR/mes x14
        'salsero / cocinero frio': 22400, # 1.600 EUR/mes x14
        'cocinero 1': 22400,              # 1.600 EUR/mes x14
        'cocinero 2': 22400,              # 1.600 EUR/mes x14
        'ayudante cocina': 17500,         # 1.250 EUR/mes x14 — ya sobre SMI
        'office': 17094,                  # 1.200 EUR/mes x14 = 16.800 < SMI
                                          # → SUELO SMI (17.094 EUR/año)
        # --- sala (docx cap. 13, 2.000-2.500 / 1.800-2.200 (barman) /
        #     1.400-1.700 / 1.200-1.400 (runner) EUR brutos/mes) ------------
        'encargado sala': 29400,          # 2.100 EUR/mes x14
        'barman tequilas': 26600,         # 1.900 EUR/mes x14 — especializado
                                          # (cap. 13: «vende el triple»)
        'camarero 1': 20300,              # 1.450 EUR/mes x14
        'camarero 2': 20300,
        'camarero 3': 20300,
        'runner': 17094,                  # 1.200 EUR/mes x14 = 16.800 < SMI
                                          # → SUELO SMI (17.094 EUR/año)
        # ⚠️ La clave va SIN tilde en la í: es el resultado de
        # `grupo_c._norm()` (quita acentos), no el texto que se ve en la
        # celda C8 («Salsero / cocinero frío»). Con la tilde, la clave no
        # matchearía nunca y esta fila se quedaría sin bruto ni cuadrante —
        # mismo gotcha que cazó casual en su «barra / coctelería» (T6).
    },
    # RT-08-ter (T6, mismo mecanismo que casual) — el cuadrante NO se deja
    # «tal cual»: medido en el fichero original, 11 de los 14 puestos
    # estaban a 7 días de «P» (Partido, 10 h) = 70 h/semana, 1 a «M» x7
    # (56 h) y 2 a «T» x7 (56 h) — los 14 puestos, CERO días de libranza
    # («L») en toda la semana. Incumple el art. 34.1 ET (jornada) y el
    # 37.1 ET (descanso semanal) a la vez. Se recalibra con el mismo criterio
    # que el representante y casual: los turnos PARTIDOS bajan a 4 «P»
    # (40 h) y los de un único turno corrido bajan a 5 «M»/«T» (40 h), los
    # dos con libranza REAL, y `forzar_cuadrante=True` para que `grupo_c.py`
    # sobrescriba el patrón viejo (no sólo huecos: aquí no hay huecos que
    # rellenar, hay que corregir lo que ya estaba escrito). Ningún puesto
    # queda por debajo de 2 días de libranza; los partidos, con 3.
    'forzar_cuadrante': True,
    #: Original v1.1 (medido) → recalibrado (40 h, con libranza):
    #:   los 11 puestos en «P»: «PPPPPPP» (70 h) → 4 «P» + 3 «L» (40 h),
    #:   escalonados para que no todo el mundo libre el mismo día.
    #:   cocinero 2: «MMMMMMM» (56 h) → 5 «M» + 2 «L» (40 h).
    #:   barman tequilas / camarero 3: «TTTTTTT» (56 h) → 5 «T» + 2 «L»
    #:   (40 h).
    'cuadrante': {
        'jefe de cocina':           'PPPPLLL',
        'taquero':                  'PPPLLLP',
        'parrillero':               'PPLLLPP',
        'salsero / cocinero frio':  'PLLLPPP',
        'cocinero 1':               'LLLPPPP',
        'cocinero 2':               'MMMMMLL',
        'ayudante cocina':          'LLPPPPL',
        'office':                   'LPPPPLL',
        'encargado sala':           'PPPPLLL',
        'barman tequilas':          'TTTTTLL',
        'camarero 1':               'PPPLLLP',
        'camarero 2':               'PPLLLPP',
        'camarero 3':               'TTTTTLL',
        'runner':                   'PLLLPPP',
    },
}
