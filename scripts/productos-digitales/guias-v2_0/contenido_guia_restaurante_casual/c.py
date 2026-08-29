# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_casual/c.py — contenido del **grupo C** (cocina,
carta y sala, `guias-v2-SPEC.md` §4) para «Cómo Montar un Restaurante Casual»
(80 plazas, 65 EUR).

Casual usa el modelo **E2** de escandallo (los 5 hermanos), el modelo **M2**
de menu engineering (Matrix, YA con 10 platos reales) y el modelo **T2** de
cuadrante (rejilla YA rellena de P/T/M, sin columna «Horas/Semana»). No lleva
`budget-bodega.xlsx` (sólo el representante): por eso este módulo no expone
`BODEGA`.

FUENTE DE CADA CIFRA:
  · `fichero original`  — ya estaba en el `.xlsx` de esta guía (v1.1).
  · `docx capN`          — `guia-restaurante-casual.docx`, capítulo citado.
  · `ejemplo editable`   — sin fuente en ningún fichero de esta guía; celda
                           verde, anunciada como ejemplo.

Lo que **no** está aquí, y por qué:
  · **El food cost y el IVA del escandallo.** `escandallo-maestro.xlsx!
    Escandallo!G16='=G15/0.30'` y `G17='=G16*1.10'` ya traen el 30 % y el
    10 % dentro de la fórmula: `grupo_c._escandallo_e2()` los EXTRAE del
    propio texto de la fórmula (no hace falta declararlos aquí; el valor de
    `ESCANDALLO['food_cost_objetivo']` de abajo es sólo la red por si esa
    extracción fallara).
  · **Los 10 platos del menu engineering.** `menu-engineering-matrix.xlsx!
    Matrix!B5:F14` YA trae 10 platos reales con PVP, Food Cost y Uds
    Vendidas/Mes (fichero original): `grupo_c._menu()` sólo precarga
    `MENU['platos']` cuando el modelo es M1 (representante) y la hoja está
    vacía; en M2 con datos ya presentes no se toca ni una celda de la carta.
  · **Los ingredientes del escandallo.** Ya vienen precargados (8 líneas:
    pan brioche, carne madurada, cheddar, bacon, verduras, salsa, patatas,
    aceite) — fichero original de v1.1; no se sustituyen.
"""

# ==========================================================================
# escandallo-maestro.xlsx (modelo E2) — §4.1
# ==========================================================================
#: `Escandallo!G16='=G15/0.30'` (30 %, food cost objetivo) y
#: `G17='=G16*1.10'` (10 %, IVA de restauración) ya están en la fórmula:
#: `grupo_c._escandallo_e2()` los extrae con regex y los baja a celda verde.
#: Coherente con `pl-mensual-escenarios` (food cost 30 % en las tres hojas) y
#: con `cash-flow-break-even!Break-Even!B8` (30 %): la MISMA cifra en los
#: tres libros.
ESCANDALLO = {
    'food_cost_objetivo': 0.30,   # fuente: fichero original (G16 = G15/0.30)
    'fuente': 'fichero original: escandallo-maestro.xlsx!Escandallo!G16',
}

# ==========================================================================
# menu-engineering-matrix.xlsx (modelo M2) — §4.2
# ==========================================================================
#: Vacío a propósito: la carta de 10 platos (croquetas, ensalada César,
#: hamburguesa gourmet, risotto, pollo al horno, tartar de atún, pasta
#: carbonara, tarta de queso, brownie, nachos) ya está en el fichero (fichero
#: original) y cubre exactamente la «Estructura de carta casual» del
#: docx cap. 15 (entrantes/para compartir, principales, postres —
#: 18-26 platos totales; estos 10 son la muestra que trae el libro).
#: `grupo_c.py` sólo añade mix %, umbral 70 %/N, margen medio y clasificación
#: por fórmula: no hace falta ningún dato de este módulo para eso.
MENU = {}

# ==========================================================================
# plantilla-turnos-brigada.xlsx (modelo T2) — §4.4
# ==========================================================================
#: El cuadrante YA trae 13 puestos con la rejilla P/T/M rellena de lunes a
#: domingo (fichero original, docx cap. 13 «Brigada de Cocina 6-10 personas»
#: → 7 puestos de cocina aquí; docx cap. 14 «Equipo de Sala 6-8 personas» →
#: 6 puestos de sala aquí, dentro de los dos rangos). NO hay columna «Horas/
#: Semana» ni «Bruto anual»: `grupo_c.py` las añade y usa `brutos` para
#: precargar un ejemplo por puesto — el cuadrante en sí (`cuadrante` de abajo,
#: vacío) NO hace falta rellenarlo: las celdas D:J ya están escritas y
#: `grupo_c._headcount`/`_precargar` sólo escriben donde la celda está VACÍA.
#:
#: Fuente de cada bruto: docx caps. 13-14 («Organigrama tipo», rangos
#: EUR brutos/mes), convertidos a bruto ANUAL con 14 pagas (la que el propio
#: producto declara «habitual en hostelería» y que es el valor por defecto de
#: la columna «Nº de pagas» del cuadrante), tomando el tercio bajo del rango
#: — mismo criterio prudente que usó el representante — y ELEVANDO al SMI
#: vigente (17.094 EUR/año, RD 126/2026) los dos puestos que quedaban por
#: debajo [DOM-13 · §7-bis.16].
#:
#: §7-bis.7 — el total de esta tabla (291.088 EUR/año: 161.994 EUR cocina +
#: 129.094 EUR sala) es la fuente del coste de personal de TODO el producto y
#: es coherente (±3 %, dentro de lo razonable para cifras de EJEMPLO) con los
#: 300.000 EUR/año (14.000+11.000 EUR/mes) que `pl-mensual-escenarios` y
#: `plan-financiero-3-anos!'P&L Mensual'` YA llevan precargados en las dos
#: — no hace falta forzar el cuadre exacto: los tres libros describen la
#: misma magnitud dentro de un margen defendible para cifras de ejemplo.
TURNOS = {
    'headcount': 'medido en tiempo de ejecución (§9)',
    'brutos': {
        # --- cocina (docx cap. 13, 2.200-2.800 / 1.800-2.200 / 1.500-1.800 /
        #     1.200-1.500 EUR brutos/mes) ------------------------------------
        'jefe de cocina': 33600,          # 2.400 EUR/mes x14 (punto prudente)
        'segundo de cocina': 26600,       # 1.900 EUR/mes x14
        'cocinero 1': 22400,              # 1.600 EUR/mes x14
        'cocinero 2': 22400,
        'cocinero 3': 22400,
        'ayudante cocina': 17500,         # 1.250 EUR/mes x14 — ya sobre SMI
        'office': 17094,                  # 1.200 EUR/mes x14 = 16.800 < SMI
                                          # → SUELO SMI (17.094 EUR/año)
        # --- sala (docx cap. 14, 2.000-2.500 / 1.400-1.700 / 1.200-1.400 /
        #     1.500-1.900 EUR brutos/mes) --------------------------------
        'encargado sala': 29400,          # 2.100 EUR/mes x14
        'camarero 1': 20300,              # 1.450 EUR/mes x14
        'camarero 2': 20300,
        'camarero 3': 20300,
        'runner': 17094,                  # 1.200 EUR/mes x14 = 16.800 < SMI
                                          # → SUELO SMI (17.094 EUR/año)
        'barra / coctelería': 21700,      # 1.550 EUR/mes x14
    },
    # El cuadrante YA está relleno de P/T/M en el fichero original: no hay
    # nada que precargar aquí (a diferencia del representante, cuya rejilla
    # llegaba en blanco).
    'cuadrante': {},
}
