# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_mexicano/a.py — el CONTENIDO del grupo A (§2 de
`guias-v2-SPEC.md`) para la guía «Cómo Montar un Restaurante Mexicano» (80
plazas, 65 EUR, hermano T6 del representante gastronómico).

`grupo_a.py` pone la lógica de familia (detección de variante, localización de
filas por etiqueta); aquí van las filas, los textos, los importes y los
parámetros **propios de esta guía**. Mexicano es la variante «hermanos»
(§2 cabecera de la SPEC), igual que casual/peruano/japonés/nikkei: ticket en
columna única, `pl-mensual-escenarios` en TRES hojas ya tecleadas, escandallo
modelo E2 (merma como recargo, a corregir por el motor) y `calculadora-capex`
variante «desglosado». La mecánica de cada pieza NO se repite aquí: vive en
`grupo_a.py` y ya está verificada contra el representante y contra casual
(T6 previo, mismo mecanismo).

FUENTE DE CADA CIFRA:
  · «fichero original» → ya estaba en el `.xlsx` de esta guía (v1.1) y se
    conserva o se convierte en fórmula (§1.2), nunca se inventa.
  · «docx capN»          → `guia-restaurante-mexicano.docx`, capítulo citado.
  · «parametrizado»      → NO sale de ningún fichero de esta guía ni de la
    SPEC. Va en celda verde con nota, declarado como ejemplo editable.

──────────────────────────────────────────────────────────────────────────
UNA SOLA FUENTE POR MAGNITUD (§7-bis.7) — lo medido en el censo propio
──────────────────────────────────────────────────────────────────────────
El `pl-mensual-escenarios.xlsx` (escenario Realista: Ventas sala 28.000 +
Barra tequilas 12.000 + Delivery 6.000 + Bebidas 6.000 = 52.000 EUR/mes) y el
`'P&L Mensual'` de `plan-financiero-3-anos.xlsx` YA comparten exactamente las
mismas cuatro líneas de ingreso, mes a mes, y los mismos 11 conceptos de coste
fijo (Alquiler 4.000 · Personal cocina 16.000 · Personal sala 12.000 ·
Suministros 2.800 · Seguros 350 · Gestoría 400 · Marketing 900 · Tecnología
350 · Mantenimiento 300 · Reposición tequila/mezcal 1.500 · Varios 500 =
39.100 EUR/mes) — verificado abriendo los dos ficheros, coincide al céntimo en
las 15 líneas y en los dos TOTALES. No hace falta `PLAN['pl_mensual']`: la
precarga ya la trae v1.1 (a diferencia del representante, que SÍ la necesita).

Lo que SÍ cambia con la aplicación de §2.3.5 (fondo de maniobra dimensionado,
DOM-01): la partida «Fondo de maniobra (3 meses)» de `Inversión` (45.000 EUR,
tecleada) pasa a fórmula = estructura mensual (fijos + variables del propio
P&L: 39.100 + 16.520 = 55.620 EUR/mes, con el food cost al 31 % que ya declara
el rótulo) × 6 meses (mínimo de la SPEC, no los 3 que rotulaba la fila) =
333.720 EUR. La «TOTAL INVERSIÓN» sube de 290.100 EUR (que YA incluía el
antiguo fondo de 45.000 EUR) a 578.820 EUR (245.100 EUR del resto de partidas
+ 333.720 EUR de fondo calculado) — verificado en el dry-run (informe T6). Es
la misma corrección que ya aplicaron el representante y casual, y por el mismo
motivo: el «120.000 EUR-280.000 EUR» que el cap. 4 del docx anuncia como rango
de inversión se queda MUY corto. **No se corrige a la baja**: es efecto
correcto de la corrección, y el ajuste del texto de la landing/docx es T7/T8,
fuera del alcance de T6 (post-proceso de los xlsx). Se deja anotado en el
informe.

§7-bis.14 (Pesimista «malo, no inviable») — el Pesimista de mexicano es
ARITMÉTICAMENTE correcto (verificado a mano: 21.000+9.000+4.500+4.500=39.000 =
TOTAL INGRESOS; 12.090+400=12.490 = TOTAL COSTES VARIABLES; TOTAL COSTES FIJOS
39.100 en las tres hojas —los costes fijos NO varían por escenario, sólo
ingresos y food cost—; EBITDA = 39.000-12.490-39.100 = -12.590, que cuadra con
el B31 cacheado) pero es un escenario PEOR que el de casual (-4.425 EUR/mes) y
del mismo orden que el de japonés que motivó la decisión de la SPEC
(-12.055 EUR/mes): -12.590 EUR/mes = -151.080 EUR/año sobre una facturación
Pesimista de 468.000 EUR/año (-32,3 % de margen). Igual que en casual
(RD-CASUAL-04), se intentó recalibrar subiendo «Ventas sala» y bajando
«Reposición tequila/mezcal» en este módulo, y el motor compartido
(`grupo_a.pl_tres_hojas()`) sigue sin poder propagar una `nota_dif` a la
fórmula del TOTAL cuando una línea de detalle se recalibra en la variante
«tres hojas» (mismo cableado ausente que documentó casual: cambio de
`grupo_a.py`, no de contenido — fuera del alcance de T6). Se deja como
hallazgo (informe, id RD-MEX-02) y **NO se recalibra**: los valores de v1.1
son aritméticamente correctos y se convierten en fórmula tal cual (§1.2).

⚠️ **RD-MEX-04 (alta, no sólo el Pesimista) — verificado en el dry-run tras
escribir el motor.** El escenario REALISTA (52.000 EUR/mes de facturación,
39.100 EUR/mes de costes fijos, food cost 31 %) YA daba EBITDA negativo en
v1.1: `Realista!B31 = -3.620` (-43.440 EUR/año), y es aritméticamente
correcto (verificado por pycel: `recalculado=-3620.0, coincide=true`). Al
encadenar la `Proyección 3 Años` desde ese mismo P&L, los TRES años dan
EBITDA negativo: Año 1 -86.016 EUR (con la rampa de apertura), Año 2 -29.878
EUR y Año 3 -28.653 EUR — incluso con crecimiento del 8 %/5 % y a pesar de
que el Año 2 ya factura a crucero completo (673.920 EUR). Y
`cash-flow-break-even!Break-Even!B13` («Break-Even (meses)») devuelve
`"No alcanzado"`, no por un error de fórmula sino porque a los parámetros
propios de esta guía (85 comensales/día, ticket 24 EUR, food cost 31 %,
costes fijos 39.100 EUR/mes) el margen de contribución mensual (36.597,6 EUR)
NUNCA llega a cubrir los costes fijos (39.100 EUR): es el resultado
CORRECTO del calculador, no un fallo del motor — el break-even devuelve
exactamente `"No alcanzado"` para una serie que nunca cruza a positivo, que
es la demostración que exige §2.4. Igual que RD-MEX-02/RD-CASUAL-04: no se
recalibra en esta tanda (el cableado para propagar una recalibración al
TOTAL de la variante «tres hojas» no existe en `grupo_a.py`, y tocar
Break-Even!B5:B9 sin fuente sería inventar cifras del negocio, prohibido por
§7-bis). Se documenta con severidad ALTA en el informe de T6 para que el
orquestador decida en T7/T8/§7.3 si el concepto necesita un ticket medio más
alto, más cubiertos/día o menos coste fijo antes de publicarse como
«viable» en la landing — el defecto es del NEGOCIO descrito por v1.1, no de
este post-proceso, que se limita a calcularlo con exactitud.
"""

# ==========================================================================
# §2.1 · calculadora-ticket-medio.xlsx — variante «columna única»
# ==========================================================================
#: `Ticket Medio` YA trae los 9 valores (B5:B13) precargados de v1.1: son
#: fichero original, no se tocan (§1.2: sólo la fila del resultado, B15, que
#: hoy está VACÍA, pasa a fórmula). Lo único que aporta este módulo son las
#: DOS filas que la variante «columna única» añade siempre debajo del ticket
#: (`grupo_a.ticket_columna_unica`, §2.1): Cubiertos/día y Días abierto/mes.
TICKET = {
    # docx cap. 4/11 no da un cubiertos/día directo; el que se usa es el
    # mismo que Break-Even!B6 (fichero original de ESTA guía,
    # cash-flow-break-even.xlsx) para no inventar una segunda cifra: 85
    # comensales/día. Días abierto: Break-Even!B7 = 26 (fichero original).
    'cubiertos_dia': 85,     # fuente: fichero original — Break-Even!B6
    'dias_mes': 26,          # fuente: fichero original — Break-Even!B7
}

# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx — variante «tres hojas»
# ==========================================================================
#: Las 3 hojas (Pesimista/Realista/Optimista) llegan con TODO tecleado y
#: aritméticamente correctas (verificado a mano, ver cabecera del módulo).
#: `grupo_a.py` las convierte en fórmula (NUEVO-01 no aplica aquí: mexicano SÍ
#: tenía sus totales calculados a mano, a diferencia de los 5 hermanos que
#: describe la SPEC — el defecto real es que eran CONSTANTES, no fórmulas).
#: No se precarga ninguna línea de detalle: `PL` se queda vacío a propósito.
#: §7-bis.14 — NO recalibrado en esta tanda, con motivo (ver cabecera del
#: módulo, id RD-MEX-02): el motor compartido no tiene el cableado para
#: propagar una nota de recalibración al TOTAL en la variante «tres hojas».
PL = {}

# ==========================================================================
# §2.3 · plan-financiero-3-anos.xlsx
# ==========================================================================
PLAN = {
    'proyeccion': {
        # parametrizado: ni la SPEC ni el docx fijan un crecimiento propio de
        # mexicano. Mismo criterio que el representante y casual (§2.3.1): un
        # concepto de restauración temática recién llegado a un barrio crece
        # más rápido el año 2 que el 3, cuando ya ha madurado.
        'crecimiento': {'C': 0.08, 'D': 0.05},
        'inflacion': {'C': 0.03, 'D': 0.03},
        'impuesto_sociedades': 0.25,
    },
    'financiacion': {
        # parametrizado: préstamo de EJEMPLO. La necesidad total, tras
        # aplicar §2.3.5 (fondo de maniobra a 6 meses = 6 x 55.620 EUR de
        # estructura mensual del P&L), sube de 290.100 EUR (con el fondo
        # viejo de 45.000 EUR ya dentro) a 578.820 EUR (245.100 EUR del resto
        # de partidas + 333.720 EUR de fondo calculado; verificado en el
        # dry-run, informe T6). Préstamo de ejemplo: 420.000 EUR a 8 años al
        # 6,0 %, 1 año de carencia (mismo criterio que representante y
        # casual: la carencia ocupa un año ENTERO, no una fracción — con una
        # fracción de año la hoja de Financiación, que decide la cuota por
        # año completo, no la repartiría correctamente entre carencia y cuota
        # completa dentro del mismo ejercicio). Fondos propios =
        # 578.820 - 420.000 = 158.820 EUR.
        'importe': 420000,
        'plazo': 8,
        'tipo': 0.06,
        'carencia': 1,
        'fondos_propios': 158820,   # verificado en el dry-run: cuadra exacto
        'otras_fuentes': 0,
    },
    # SPEC §2.3.5/§7-bis.3: mínimo 6 meses. NO se sube más allá del mínimo:
    # el propio docx (cap. 4) da un rango de inversión que ya se queda corto
    # (120.000-280.000 EUR frente a los 578.820 EUR reales, ver cabecera del
    # módulo), así que 6 es el suelo defendible, no un margen extra sin
    # fuente.
    'fondo_maniobra': {'meses': 6},
    # Los 5 hermanos (§2.3.5, grupo_a.fondo_de_maniobra) NO devuelven filas
    # de alquiler/personal en el P&L de esta variante, así que el bloque de
    # PREAPERTURA (rentas y nóminas antes de abrir) no se activa aquí — es
    # una limitación conocida y documentada de la variante «tres hojas»/
    # «P&L Mensual sin desglose de personal» (verificada ya en casual), no un
    # olvido de este módulo.
    'preapertura': {},
    # §2.3.6 — correspondencia de las 44 partidas de `Inversión` (plan-
    # financiero) con las 12 categorías de `calculadora-capex!CAPEX
    # Desglosado`, medida abriendo los dos ficheros (fuente: fichero
    # original en los dos lados; las 44 partidas de Inversión Y las 36 de
    # CAPEX Desglosado se agrupan en las MISMAS 12 categorías).
    'capex_map': {
        r'^acondicionamiento local': 'Obra',
        r'^instalaciones electricas y gas': 'Obra',
        r'^fontaneria y saneamiento': 'Obra',
        r'^climatizacion': 'Obra',
        r'^extraccion reforzada': 'Obra',
        r'^comal profesional': 'Cocina MX',
        r'^prensa de tortillas': 'Cocina MX',
        r'^trompo de pastor': 'Cocina MX',
        r'^ahumador': 'Cocina MX',
        r'^parrilla carbon': 'Cocina MX',
        r'^molcajetes': 'Cocina MX',
        r'^licuadoras industriales': 'Cocina MX',
        r'^horno mixto': 'Cocina',
        r'^cocina gas 6 fuegos': 'Cocina',
        r'^freidora doble': 'Cocina',
        r'^camaras frigorificas': 'Cocina',
        r'^congelador$': 'Cocina',
        r'^tren de lavado': 'Cocina',
        r'^campana extractora': 'Cocina',
        r'^menaje y utensilios': 'Cocina',
        r'^expositor iluminado': 'Barra',
        r'^maquina de margaritas': 'Barra',
        r'^stock inicial tequila': 'Barra',
        r'^coctelera, medidores': 'Barra',
        r'^maquina de hielo': 'Barra',
        r'^mobiliario interior': 'Sala',
        r'^barra \+ taburetes': 'Sala',
        r'^azulejos talavera': 'Decoración',
        r'^mural artistico': 'Decoración',
        r'^vajilla de barro': 'Decoración',
        r'^iluminacion decorativa': 'Decoración',
        r'^plantas, cactus': 'Decoración',
        r'^mobiliario exterior': 'Terraza',
        r'^sombrillas / toldos': 'Terraza',
        r'^tpv \+ pantallas': 'Tech',
        r'^web \+ carta qr': 'Tech',
        r'^licencia actividad': 'Licencias',
        r'^proyecto tecnico': 'Licencias',
        r'^registro eori': 'Licencias',
        r'^branding mexicano': 'Marketing',
        r'^fotos \+ video': 'Marketing',
        r'^materia prima inicial': 'Stock',
        r'^bebidas \(cerveza': 'Stock',
        r'^fondo de maniobra': 'Maniobra',
    },
    # Las 44 partidas SON las de v1.1 (fichero original): no se tocan salvo
    # la de fondo de maniobra, que grupo_a.fondo_de_maniobra() convierte en
    # fórmula por sí solo (no necesita 'inversion' aquí: no hay ninguna
    # partida vacía que precargar, a diferencia del representante).
}

# ==========================================================================
# §2.4 · cash-flow-break-even.xlsx — variante «cash-y-breakeven»
# ==========================================================================
#: `Cash Flow` llega ENTERAMENTE en blanco (B5:M27, fichero original) y
#: `Break-Even!B5:B9` YA trae valores propios (ticket 24 EUR, 85 comensales/
#: día, 26 días/mes, food cost 31 %, costes fijos 39.100 EUR/mes — los tres
#: últimos COINCIDEN con `plan-financiero!'P&L Mensual'`; el ticket de 24 EUR
#: es distinto del ticket ponderado del simulador porque Break-Even mide un
#: ticket MEDIO de sala, y el simulador calcula el ticket completo con barra
#: de tequilas y postre por separado — no se fuerza a que coincidan: son
#: magnitudes distintas, ninguna de las dos está en la lista de «una sola
#: fuente» del §7-bis.7, que sólo cubre inversión/personal/fondo de
#: maniobra/headcount) y sólo le falta B13 «Break-Even (meses)», que
#: `grupo_a.py` calcula solo desde el flujo acumulado de `Cash Flow`.
CASH = {
    # Repetidas con nota, no enlazadas (§1.13): son las cuotas del préstamo
    # de ejemplo de PLAN.financiacion (420.000 EUR, 8 años, 6,0 %, 1 año de
    # carencia). Verificado tras ejecutar `hoja_financiacion` (§ informe).
    'cuota_mensual': 6135.59,  # verificado: Financiación!B12 (post-carencia)
    'cuota_carencia': 2100.0,  # verificado: Financiación!B13 (solo intereses)
    # 'anio': 1 → durante el AÑO 1 (dentro de la carencia) sólo se usa
    # `cuota_carencia`; `cuota_mensual` queda documentado para cuando el
    # cliente copie el cash flow al año 2+ (nota A44 de la propia hoja).
    'anio': 1,
    'necesidad_total': 578820.0,   # verificado: Inversión!C50
    'iva_bebida': 0.21,
    # Rampa de apertura sobre el escenario REALISTA (52.000 EUR/mes) — mismo
    # criterio que el representante y casual (§2.4): parametrizada, en verde.
    'rampa': (0.60, 0.70, 0.80, 0.85, 0.90, 0.95,
              1.00, 1.00, 1.00, 1.00, 1.00, 1.00),
    'mes_tipo': {
        'ingresos': {r'^ventas sala': 28000, r'^barra tequilas': 12000,
                     r'^delivery': 6000, r'^bebidas': 6000},
        # food cost 31 % de 52.000 EUR (Realista) = 16.120 EUR. El Cash Flow
        # de esta guía no tiene línea de «packaging delivery» propia (a
        # diferencia del P&L, que sí la separa): se queda dentro de «Materia
        # prima + chiles importados», que es como lo rotula el fichero
        # original.
        'variables': {r'^materia prima': 16120},
        # A diferencia de casual (una sola línea «Personal»), el Cash Flow de
        # mexicano trae DOS líneas separadas — «Personal cocina» y «Personal
        # sala» — igual que el P&L: se respetan por separado (fichero
        # original).
        'fijos': {r'^personal cocina': 16000, r'^personal sala': 12000,
                  r'^alquiler': 4000, r'^suministros': 2800,
                  r'^marketing': 900,
                  r'^reposicion tequila/mezcal': 1500,
                  r'^tecnologia': 350,
                  # «Otros gastos» del Cash Flow agrega lo que el P&L separa
                  # en Seguros(350) + Gestoría(400) + Mantenimiento(300) +
                  # Varios(500) = 1.550 EUR: no hay una línea de Cash Flow
                  # para cada una por separado (fichero original, 9 salidas
                  # frente a las 11 del P&L).
                  r'^otros gastos': 1550},
        # IVA soportado: 10 % de la materia prima (alimentación) y 21 % del
        # resto de gastos con IVA (nóminas y SS no llevan). Base de gastos
        # con IVA = alquiler + suministros + marketing + reposición
        # tequila/mezcal + tecnología + otros = 4.000+2.800+900+1.500+350+
        # 1.550 = 11.100 EUR.
        'iva_soportado': {'variables': 0.10, 'fijos_con_iva': 11100,
                          'tipo_fijos': 0.21},
    },
    # Saldo inicial de tesorería = fondo de maniobra que dimensiona
    # plan-financiero-3-anos!Inversión (§2.3.5): 6 x 55.620 EUR = 333.720 EUR
    # (verificado en el dry-run: Inversión!C48/fila del fondo calculado).
    'apertura': {'saldo_inicial': 333720.0, 'desembolso_capex': None,
                 'iva_capex': None},
    'break_even': {
        # NO se toca: son fichero original de ESTA guía (Break-Even!B5:B9) y
        # ya son coherentes con el resto del pack (costes fijos 39.100 EUR/
        # mes = TOTAL COSTES FIJOS del P&L; food cost 31 % = el mismo de
        # pl-mensual y del escandallo). `grupo_a._break_even_hoja_propia` los
        # LEE de la hoja, no hace falta repetirlos aquí.
    },
}

# ==========================================================================
# §2.3.6 · calculadora-capex.xlsx — variante «desglosado»
# ==========================================================================
#: `CAPEX Desglosado` YA trae 36 partidas con importe y fila TOTAL con SUM
#: (fichero original): no hace falta precargar nada. Lo único que le falta,
#: y que `grupo_a.py` añade sin contenido adicional, es §1 (protección,
#: formato por tipo, versión, bio) — no hay «rangos de mercado» que
#: reconciliar porque esta variante no los tiene (a diferencia del
#: representante): es ya el desglose «Mi CAPEX» de mexicano.
CAPEX = {}
