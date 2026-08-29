# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_peruano/c.py — contenido del **grupo C** (cocina,
carta y sala, `guias-v2-SPEC.md` §4) para «Cómo Montar un Restaurante
Peruano» (80 plazas, 65 EUR).

Peruano usa el modelo **E2** de escandallo (los 5 hermanos: merma como
recargo `G=E*(1+F)`, a corregir por `grupo_c._escandallo_e2()` a
`/(1-merma)`), el modelo **M2** de menu engineering (Matrix, YA con 15 platos
reales) y el modelo **T2** de cuadrante (rejilla YA rellena de P/T/M, sin
columna «Horas/Semana»). No lleva `budget-bodega.xlsx` (sólo el
representante): por eso este módulo no expone `BODEGA`.

FUENTE DE CADA CIFRA:
  · `fichero original`  — ya estaba en el `.xlsx` de esta guía (v1.1).
  · `docx §N`            — `guia-restaurante-peruano.docx`, párrafo citado.
  · `ejemplo editable`   — sin fuente en ningún fichero de esta guía; celda
                           verde, anunciada como ejemplo.

Lo que **no** está aquí, y por qué:
  · **El food cost y el IVA del escandallo.** `escandallo-maestro-peruano.
    xlsx!Escandallo!G18='=G17/0.30'` y `G19='=G18*1.10'` ya traen el 30 % y
    el 10 % dentro de la fórmula: `grupo_c._escandallo_e2()` los EXTRAE del
    propio texto de la fórmula (no hace falta declararlos aquí; el valor de
    `ESCANDALLO['food_cost_objetivo']` de abajo es sólo la red por si esa
    extracción fallara).
  · **Los 15 platos del menu engineering.** `menu-engineering-matrix.xlsx!
    Matrix!B5:F19` YA trae 15 platos reales con PVP, Food Cost y Uds
    Vendidas/Mes (fichero original, coherente con la carta descrita en el
    docx: ceviche, lomo saltado, causa, ají de gallina, anticuchos,
    tiradito, arroz con mariscos, huancaína, pisco sour, chicharrón, tacu
    tacu, chaufa, suspiro limeño, picarones, pollo a la brasa):
    `grupo_c._menu()` sólo precarga `MENU['platos']` cuando el modelo es M1
    (representante) y la hoja está vacía; en M2 con datos ya presentes no se
    toca ni una celda de la carta.
  · **Los ingredientes del escandallo.** Ya vienen precargados (10 líneas:
    corvina fresca, zumo de limón, cebolla morada, ají limo, cilantro, ají
    amarillo en pasta, sal/pimienta, camote cocido, choclo desgranado,
    lechuga — «Ceviche Clásico de Corvina», la ficha ejemplo del propio
    fichero) — fichero original de v1.1; no se sustituyen.
"""

# ==========================================================================
# escandallo-maestro-peruano.xlsx (modelo E2) — §4.1
# ==========================================================================
#: `Escandallo!G18='=G17/0.30'` (30 %, food cost objetivo) y
#: `G19='=G18*1.10'` (10 %, IVA de restauración) ya están en la fórmula:
#: `grupo_c._escandallo_e2()` los extrae con regex y los baja a celda verde.
#: Coherente con `pl-mensual-escenarios` (food cost 30 % en las tres hojas,
#: el mismo objetivo, sin desviación) y con
#: `cash-flow-break-even!Break-Even!B8` (30 %): las tres cifras son la MISMA
#: magnitud, sin necesidad de calibrar nada — a diferencia de mexicano
#: (30 % objetivo del plato vs 31 % real de la carta), peruano ya cuadra
#: exacto en los tres libros.
ESCANDALLO = {
    'food_cost_objetivo': 0.30,   # fuente: fichero original (G18 = G17/0.30)
    'fuente': 'fichero original: escandallo-maestro-peruano.xlsx!Escandallo!G18',
}

# ==========================================================================
# menu-engineering-matrix.xlsx (modelo M2) — §4.2
# ==========================================================================
#: Vacío a propósito: la carta de 15 platos (ceviche clásico de corvina, lomo
#: saltado, causa limeña de atún, ají de gallina, anticuchos de corazón,
#: tiradito de lubina, arroz con mariscos, papa a la huancaína, pisco sour,
#: chicharrón con mote, tacu tacu con lomo, arroz chaufa de pollo, suspiro
#: limeño, picarones, pollo a la brasa) ya está en el fichero (fichero
#: original) y cubre exactamente los platos que describe el docx a lo largo
#: de sus capítulos de carta y escandallo. `grupo_c.py` sólo añade mix %,
#: umbral 70 %/N, margen medio y clasificación por fórmula: no hace falta
#: ningún dato de este módulo para eso.
MENU = {}

# ==========================================================================
# plantilla-turnos-brigada.xlsx (modelo T2) — §4.4
# ==========================================================================
#: El cuadrante YA trae 14 puestos con la rejilla P/T/M rellena de lunes a
#: domingo (fichero original, docx §12 «Brigada de Cocina 6-10 personas» → 8
#: puestos de cocina aquí; docx §13 «Equipo de Sala 6-8 personas» → 6 puestos
#: de sala aquí, dentro de los dos rangos). NO hay columna «Horas/Semana» ni
#: «Bruto anual»: `grupo_c.py` las añade y usa `brutos` para precargar un
#: ejemplo por puesto. El cuadrante en sí SÍ hace falta tocarlo, y no para
#: rellenar huecos: v1.1 tenía los 14 puestos a 7 días de un único turno (11
#: en «P», 1 en «M», 2 en «T») SIN NINGÚN «L», es decir, 70 h/semana en 11
#: puestos y 56 h/semana en 3 puestos con cero días de libranza en los 14 —
#: verificado en el dry-run del gate «brigada ≤ 40 h/puesto» de T6
#: (§ informe). Es el MISMO defecto exacto, con el MISMO reparto (11+1+2),
#: que ya cazaron casual (RD-CASUAL-02) y mexicano (RD-MEX-03) en sus propios
#: v1.1: aquí RD-PERU-02. `cuadrante` de abajo trae el patrón CORREGIDO y
#: `forzar_cuadrante=True` para que se escriba encima del que ya había.
#:
#: Fuente de cada bruto: docx §§12-13 («Organigrama tipo», rangos EUR
#: brutos/mes), convertidos a bruto ANUAL con 14 pagas (la que el propio
#: producto declara «habitual en hostelería» y que es el valor por defecto de
#: la columna «Nº de pagas» del cuadrante), tomando el TERCIO BAJO del rango
#: —mismo criterio prudente que representante, casual y mexicano— con un
#: pequeño ajuste al alza en los puestos especializados que el propio docx
#: describe como críticos (cevichero: «el alma del restaurante peruano»,
#: §212; wokero y parrillero: puestos «específicos que no existen en una
#: cocina europea convencional», §203; barman de piscos: coctelería
#: especializada, §217), ELEVANDO al SMI vigente (17.094 EUR/año, RD
#: 126/2026) el único puesto que quedaba por debajo [DOM-13 · §7-bis.16]:
#: Runner (1.200 EUR/mes x14 = 16.800 EUR/año < SMI).
#:
#: §7-bis.7 — el total de esta tabla (328.594 EUR/año: 194.600 EUR cocina +
#: 133.994 EUR sala) es la fuente del coste de personal de TODO el producto y
#: es coherente (94,4 %, dentro de lo razonable para cifras de EJEMPLO) con
#: los 348.000 EUR/año (17.000+12.000 EUR/mes) que `pl-mensual-escenarios` y
#: `plan-financiero-3-anos!'P&L Mensual'` YA llevan precargados en las dos —
#: no hace falta forzar el cuadre exacto: los tres libros describen la misma
#: magnitud dentro de un margen defendible para cifras de ejemplo (la brigada
#: de 14 puestos con bruto medido da un coste ligeramente MENOR que la línea
#: agregada del P&L, que es justo lo esperable: el P&L incluye margen de
#: contingencia sobre la nómina real). Verificación por partida: cocina
#: (13.900 EUR/mes bruto x1,33 SS = 18.487 EUR/mes) cae dentro de «Coste
#: total cocina: 13.000-22.000 EUR/mes (incluye SS empresa)» (docx §211); sala
#: (9.571 EUR/mes bruto x1,33 SS = 12.729 EUR/mes) cae dentro de «Coste total
#: sala: 9.000-15.000 EUR/mes (incluye SS empresa)» (docx §223).
TURNOS = {
    'headcount': 'medido en tiempo de ejecución (§9)',
    'brutos': {
        # --- cocina (docx §205-211: 2.200-2.800 (jefe) / 1.800-2.200
        #     (cevichero, wokero, parrillero) / 1.500-1.800 (cocineros) /
        #     1.200-1.500 (ayudante/office) EUR brutos/mes) ------------------
        'jefe de cocina': 33600,          # 2.400 EUR/mes x14 (punto prudente)
        'cevichero': 26600,               # 1.900 EUR/mes x14 — puesto
                                          # especializado, «el alma del
                                          # restaurante peruano» (docx §213)
        'wokero (chifa/nikkei)': 26600,   # 1.900 EUR/mes x14 — puesto
                                          # específico sin equivalente en
                                          # cocina europea (docx §203)
        'parrillero (anticuchos)': 26600, # 1.900 EUR/mes x14 — ídem
        'cocinero 1 (criollos)': 22400,   # 1.600 EUR/mes x14
        'cocinero 2': 22400,              # 1.600 EUR/mes x14
        'ayudante cocina': 18200,         # 1.300 EUR/mes x14 — ya sobre SMI
        'office': 18200,                  # 1.300 EUR/mes x14 — ya sobre SMI
        # --- sala (docx §219-222: 2.000-2.500 (encargado) / 1.800-2.200
        #     (barman) / 1.400-1.700 (camareros) / 1.200-1.400 (runner)
        #     EUR brutos/mes) -----------------------------------------------
        'encargado sala': 29400,          # 2.100 EUR/mes x14
        'barman piscos': 26600,           # 1.900 EUR/mes x14 — especializado
                                          # (coctelería peruana, docx §217)
        'camarero 1': 20300,              # 1.450 EUR/mes x14
        'camarero 2': 20300,
        'camarero 3': 20300,
        'runner': 17094,                  # 1.200 EUR/mes x14 = 16.800 < SMI
                                          # → SUELO SMI (17.094 EUR/año)
        # ⚠️ Las claves van SIN tilde y SIN mayúscula inicial: son el
        # resultado de `grupo_c._norm()` (quita acentos y minuscula), no el
        # texto que se ve en la celda C (p. ej. «Wokero (chifa/Nikkei)»).
        # Mismo gotcha que cazaron casual («barra / coctelería») y mexicano
        # («salsero / cocinero frío») en T6.
    },
    # RT-08-ter (T6, mismo mecanismo que casual y mexicano) — el cuadrante NO
    # se deja «tal cual»: medido en el fichero original, 11 de los 14 puestos
    # estaban a 7 días de «P» (Partido, 10 h) = 70 h/semana, 1 a «M» x7
    # (56 h) y 2 a «T» x7 (56 h) — los 14 puestos, CERO días de libranza
    # («L») en toda la semana. Incumple el art. 34.1 ET (jornada) y el 37.1
    # ET (descanso semanal) a la vez. Se recalibra con el mismo criterio que
    # el representante, casual y mexicano: los turnos PARTIDOS bajan a 4 «P»
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
    #:   barman piscos / camarero 3: «TTTTTTT» (56 h) → 5 «T» + 2 «L» (40 h).
    'cuadrante': {
        'jefe de cocina':           'PPPPLLL',
        'cevichero':                'PPPLLLP',
        'wokero (chifa/nikkei)':    'PPLLLPP',
        'parrillero (anticuchos)':  'PLLLPPP',
        'cocinero 1 (criollos)':    'LLLPPPP',
        'ayudante cocina':          'LLPPPPL',
        'office':                   'LPPPPLL',
        'encargado sala':           'PPPPLLL',
        'camarero 1':               'PPPLLLP',
        'camarero 2':               'PPLLLPP',
        'runner':                   'PLLLPPP',
        'cocinero 2':                'MMMMMLL',
        'barman piscos':             'TTTTTLL',
        'camarero 3':                'TTTTTLL',
    },
}
