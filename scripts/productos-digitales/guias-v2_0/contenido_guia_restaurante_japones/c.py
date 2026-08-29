# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_japones/c.py — contenido del **grupo C** (cocina,
carta y sala, `guias-v2-SPEC.md` §4) para «Cómo Montar un Restaurante
Japonés» (60 plazas, 65 EUR).

Japonés usa el modelo **E2** de escandallo (los 5 hermanos: merma como
recargo `G=E*(1+F)`, a corregir por `grupo_c._escandallo_e2()` a
`/(1-merma)`), el modelo **M2** de menu engineering (Matrix, YA con 15 platos
reales) y el modelo **T2** de cuadrante (rejilla YA rellena de P/T/M, sin
columna «Horas/Semana»). No lleva `budget-bodega.xlsx` (sólo el
representante): por eso este módulo no expone `BODEGA`.

FUENTE DE CADA CIFRA:
  · `fichero original`  — ya estaba en el `.xlsx` de esta guía (v1.1).
  · `docx §N`            — `guia-restaurante-japones.docx`, párrafo citado.
  · `ejemplo editable`   — sin fuente en ningún fichero de esta guía; celda
                           verde, anunciada como ejemplo.

Lo que **no** está aquí, y por qué:
  · **El food cost y el IVA del escandallo.** `escandallo-maestro-japones.
    xlsx!Escandallo!G19='=G18/0.33'` y `G20='=G19*1.10'` ya traen el 33 % y
    el 10 % dentro de la fórmula: `grupo_c._escandallo_e2()` los EXTRAE del
    propio texto de la fórmula (no hace falta declararlos aquí; el valor de
    `ESCANDALLO['food_cost_objetivo']` de abajo es sólo la red por si esa
    extracción fallara).
  · **Los 15 platos del menu engineering.** `menu-engineering-matrix.xlsx!
    Matrix!B5:F19` YA trae 15 platos reales con PVP, Food Cost y Uds
    Vendidas/Mes (fichero original, coherente con la carta descrita en el
    docx: sashimi moriawase, nigiri salmón, nigiri toro, uramaki spicy tuna,
    ramen tonkotsu, ramen shoyu chashu, gyoza, karaage, tempura moriawase,
    yakitori pollo, yakitori wagyu, katsu, chirashi bowl, highball whisky,
    sake daiginjo): `grupo_c._menu()` sólo precarga `MENU['platos']` cuando
    el modelo es M1 (representante) y la hoja está vacía; en M2 con datos ya
    presentes no se toca ni una celda de la carta.
  · **Los ingredientes del escandallo.** Ya vienen precargados (11 líneas:
    salmón sashimi-grade, atún rojo sashimi-grade, hamachi, lubina, vieira,
    pulpo cocido, rábano daikon, shiso, wasabi, jengibre encurtido, salsa de
    soja — «Sashimi Moriawase 12 piezas», la ficha ejemplo del propio
    fichero) — fichero original de v1.1; no se sustituyen. Nótese que las
    tres primeras líneas ya citan «previamente congelado -20°C/24h», lo que
    confirma que v1.1 SÍ sabía de la obligación de anisakis en el escandallo
    mismo, aunque la citara sin base normativa en el checklist (§3.2, b.py).
"""

# ==========================================================================
# escandallo-maestro-japones.xlsx (modelo E2) — §4.1
# ==========================================================================
#: `Escandallo!G19='=G18/0.33'` (33 %, food cost objetivo) y
#: `G20='=G19*1.10'` (10 %, IVA de restauración) ya están en la fórmula:
#: `grupo_c._escandallo_e2()` los extrae con regex y los baja a celda verde.
#: Coherente con `pl-mensual-escenarios` (food cost 33 % en las tres hojas,
#: el mismo objetivo, sin desviación) y con
#: `cash-flow-break-even!Break-Even!B8` (33 %): las tres cifras son la MISMA
#: magnitud, sin necesidad de calibrar nada — igual que peruano (que cuadraba
#: 30/30/30 exacto en los tres libros) y a diferencia de mexicano (30 %
#: objetivo del plato vs 31 % real de la carta).
ESCANDALLO = {
    'food_cost_objetivo': 0.33,   # fuente: fichero original (G19 = G18/0.33)
    'fuente': 'fichero original: escandallo-maestro-japones.xlsx!Escandallo!G19',
}

# ==========================================================================
# menu-engineering-matrix.xlsx (modelo M2) — §4.2
# ==========================================================================
#: Vacío a propósito: la carta de 15 platos (sashimi moriawase, nigiri
#: salmón, nigiri toro, uramaki spicy tuna, ramen tonkotsu, ramen shoyu
#: chashu, gyoza cerdo, karaage de pollo, tempura moriawase, yakitori pollo
#: tare, yakitori wagyu, katsu cerdo + arroz, chirashi bowl, highball whisky
#: japonés, sake daiginjo) ya está en el fichero (fichero original) y cubre
#: exactamente los platos que describe el docx a lo largo de sus capítulos de
#: carta y escandallo. `grupo_c.py` sólo añade mix %, umbral 70 %/N, margen
#: medio y clasificación por fórmula: no hace falta ningún dato de este
#: módulo para eso.
MENU = {}

# ==========================================================================
# plantilla-turnos-brigada.xlsx (modelo T2) — §4.4
# ==========================================================================
#: El cuadrante YA trae 14 puestos con la rejilla P/T/M rellena de lunes a
#: domingo (fichero original, docx §12 «Organigrama tipo — Cocina, 8-10
#: personas» → 9 puestos de cocina aquí; docx §13 «Equipo de Sala, 5-8
#: personas» → 5 puestos de sala aquí, dentro de los dos rangos). NO hay
#: columna «Horas/Semana» ni «Bruto anual»: `grupo_c.py` las añade y usa
#: `brutos` para precargar un ejemplo por puesto. El cuadrante en sí SÍ hace
#: falta tocarlo, y no para rellenar huecos: v1.1 tenía los 14 puestos a 7
#: días de un único turno (11 en «P», 2 en «T», 1 en «M») SIN NINGÚN «L», es
#: decir, 70 h/semana en 11 puestos y 56 h/semana en 3 puestos con cero días
#: de libranza en los 14 — verificado en el dry-run del gate «brigada ≤ 40 h/
#: puesto» de T6 (§ informe). Es el MISMO defecto exacto, con el MISMO
#: reparto (11+2+1), que ya cazaron casual (RD-CASUAL-02), mexicano
#: (RD-MEX-03) y peruano (RD-PERU-02) en sus propios v1.1: aquí RD-JP-03.
#: `cuadrante` de abajo trae el patrón CORREGIDO y `forzar_cuadrante=True`
#: para que se escriba encima del que ya había.
#:
#: Fuente de cada bruto: docx §§12-13 («Organigrama tipo», rangos EUR
#: brutos/mes), convertidos a bruto ANUAL con 14 pagas (la que el propio
#: producto declara como opción por defecto del desplegable «Nº de pagas»
#: del cuadrante), tomando el TERCIO BAJO del rango —mismo criterio prudente
#: que representante, casual, mexicano y peruano— sin necesidad de elevar
#: ningún puesto al SMI: **verificado, los 14 puestos de esta guía quedan ya
#: por encima del SMI vigente (17.094 EUR/año, RD 126/2026) tomando el
#: tercio bajo del rango del docx** — a diferencia de peruano, donde el
#: Runner necesitaba el suelo del SMI. El puesto más bajo aquí (Runner,
#: 1.400 EUR/mes) queda un 15 % por encima del SMI mensual (1.221 EUR/mes).
#:
#: §7-bis.7 — el total de esta tabla (373.800 EUR/año: 253.400 EUR cocina +
#: 120.400 EUR sala) es la fuente del coste de personal de TODO el producto y
#: es coherente (89,0 %, dentro de lo razonable para cifras de EJEMPLO) con
#: los 420.000 EUR/año (22.000+13.000 EUR/mes) que `pl-mensual-escenarios` y
#: `plan-financiero-3-anos!'P&L Mensual'` YA llevan precargados en las dos —
#: no hace falta forzar el cuadre exacto: los tres libros describen la misma
#: magnitud dentro de un margen defendible para cifras de ejemplo (la brigada
#: de 14 puestos con bruto medido da un coste ligeramente MENOR que la línea
#: agregada del P&L, que es justo lo esperable: el P&L incluye margen de
#: contingencia sobre la nómina real, y el itamae —el puesto más caro de toda
#: la familia de guías— puede negociarse por encima del tercio bajo sin
#: romper el presupuesto). Verificación por partida: cocina (21.117 EUR/mes
#: bruto x1,33 SS = 28.085 EUR/mes) está justo en el techo de «Coste total
#: cocina: 17.000-28.000 EUR/mes (incluye SS empresa)» (docx §218) — esperable
#: en la guía más cara de personal de cocina de la familia, «el itamae es
#: caro» (docx §61); sala (10.033 EUR/mes bruto x1,33 SS = 13.344 EUR/mes)
#: cae dentro de «Coste total sala: 9.000-15.000 EUR/mes (incluye SS
#: empresa)» (docx §229). Los dos rangos del docx, igual que en el
#: representante, casual, mexicano y peruano, YA incluyen la SS dentro del
#: bruto — el mismo defecto de fondo que documenta DOM-02: el capítulo suma
#: brutos y llama al resultado «incluye SS empresa» sin haberla sumado. El
#: cuadrante de esta guía, con la columna «Coste/hora» de §4.4, deja esa
#: cuenta hecha correctamente por primera vez.
TURNOS = {
    'headcount': 'medido en tiempo de ejecución (§9)',
    'brutos': {
        # --- cocina (docx §210-217: 3.000-4.500 (itamae) / 2.200-2.800
        #     (sushi chef) / 1.900-2.400 (ramen cook, robata cook) /
        #     1.800-2.200 (tempura/hot kitchen) / 1.600-2.000 (cocineros) /
        #     1.500-1.800 (preparación pescado) / 1.300-1.600 (ayudante/
        #     office) EUR brutos/mes) -----------------------------------
        'itamae / jefe de cocina': 49000,       # 3.500 EUR/mes x14 — el
                                                 # puesto MÁS caro de la
                                                 # familia: «la decisión más
                                                 # importante» (docx §219)
        'sushi chef (segundo)': 33600,          # 2.400 EUR/mes x14
        'ramen cook': 28700,                    # 2.050 EUR/mes x14
        'robata / yakitori cook': 28700,        # 2.050 EUR/mes x14 — mismo
                                                 # rango que ramen cook
        'tempura / hot kitchen cook': 27300,    # 1.950 EUR/mes x14
        'cocinero 1 (izakaya)': 24500,          # 1.750 EUR/mes x14
        'preparacion pescado': 22400,           # 1.600 EUR/mes x14
        'ayudante cocina / office': 19600,      # 1.400 EUR/mes x14
        'office': 19600,                        # 1.400 EUR/mes x14 — mismo
                                                 # rango que ayudante (docx
                                                 # los agrupa en una línea:
                                                 # «Ayudante/office: 1-2
                                                 # personas»)
        # --- sala (docx §225-228: 2.200-2.800 (encargado, sommelier — «a
        #     veces el mismo») / 1.500-1.800 (camareros) / 1.300-1.500
        #     (runner) EUR brutos/mes) -----------------------------------
        'encargado sala / sommelier sake': 33600,  # 2.400 EUR/mes x14 —
                                                    # combina las dos
                                                    # funciones en un único
                                                    # puesto del cuadrante,
                                                    # como permite el propio
                                                    # docx §226
        'camarero 1': 22400,               # 1.600 EUR/mes x14
        'camarero 2': 22400,
        'camarero 3': 22400,
        'runner': 19600,                   # 1.400 EUR/mes x14 = 15% por
                                            # encima del SMI (17.094)
        # ⚠️ Las claves van SIN tilde y SIN mayúscula inicial: son el
        # resultado de `grupo_a._norm()` (quita acentos y minuscula) sobre el
        # texto LITERAL de la columna C, no una paráfrasis. Mismo gotcha que
        # cazaron casual («barra / coctelería»), mexicano («salsero / '
        # cocinero frío») y peruano («wokero (chifa/nikkei)») en T6.
    },
    # RT-08-ter (T6, mismo mecanismo que casual, mexicano y peruano) — el
    # cuadrante NO se deja «tal cual»: medido en el fichero original, 11 de
    # los 14 puestos estaban a 7 días de «P» (Partido, 10 h) = 70 h/semana, 2
    # a «T» x7 (56 h) y 1 a «M» x7 (56 h) — los 14 puestos, CERO días de
    # libranza («L») en toda la semana. Incumple el art. 34.1 ET (jornada) y
    # el 37.1 ET (descanso semanal) a la vez. Se recalibra con el mismo
    # criterio que el representante, casual, mexicano y peruano: los turnos
    # PARTIDOS bajan a 4 «P» (40 h) y los de un único turno corrido bajan a 5
    # «M»/«T» (40 h), los dos con libranza REAL, y `forzar_cuadrante=True`
    # para que `grupo_c.py` sobrescriba el patrón viejo (no sólo huecos: aquí
    # no hay huecos que rellenar, hay que corregir lo que ya estaba escrito).
    # Ningún puesto queda por debajo de 2 días de libranza; los partidos, con
    # 3 — y se ESCALONAN para que no todo el mundo libre el mismo día.
    'forzar_cuadrante': True,
    #: Original v1.1 (medido) → recalibrado (40 h, con libranza):
    #:   los 11 puestos en «P»: «PPPPPPP» (70 h) → 4 «P» + 3 «L» (40 h),
    #:   rotados para que el descanso no coincida en los 11.
    #:   preparación pescado: «MMMMMMM» (56 h) → 5 «M» + 2 «L» (40 h).
    #:   robata cook / camarero 3: «TTTTTTT» (56 h) → 5 «T» + 2 «L» (40 h).
    'cuadrante': {
        'itamae / jefe de cocina':          'PPPPLLL',
        'sushi chef (segundo)':             'PPPLLLP',
        'ramen cook':                       'PPLLLPP',
        'tempura / hot kitchen cook':       'PLLLPPP',
        'cocinero 1 (izakaya)':             'LLLPPPP',
        'ayudante cocina / office':         'LLPPPPL',
        'office':                           'LPPPPLL',
        'encargado sala / sommelier sake':  'PPPPLLL',
        'camarero 1':                       'PPPLLLP',
        'camarero 2':                       'PPLLLPP',
        'runner':                           'PLLLPPP',
        'preparacion pescado':               'MMMMMLL',
        'robata / yakitori cook':            'TTTTTLL',
        'camarero 3':                        'TTTTTLL',
    },
}
