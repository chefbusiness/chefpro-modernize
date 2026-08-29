# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_peruano/a.py — el CONTENIDO del grupo A (§2 de
`guias-v2-SPEC.md`) para la guía «Cómo Montar un Restaurante Peruano» (80
plazas, 65 EUR, hermano T6 del representante gastronómico).

`grupo_a.py` pone la lógica de familia (detección de variante, localización de
filas por etiqueta); aquí van las filas, los textos, los importes y los
parámetros **propios de esta guía**. Peruano es la variante «hermanos» (§2
cabecera de la SPEC), igual que casual/mexicano/japonés/nikkei: ticket en
columna única, `pl-mensual-escenarios` en TRES hojas ya tecleadas, escandallo
modelo E2 (merma como recargo, a corregir por el motor) y `calculadora-capex`
variante «desglosado». La mecánica de cada pieza NO se repite aquí: vive en
`grupo_a.py` y ya está verificada contra el representante, casual y mexicano
(T6 previos, mismo mecanismo).

FUENTE DE CADA CIFRA:
  · «fichero original» → ya estaba en el `.xlsx` de esta guía (v1.1) y se
    conserva o se convierte en fórmula (§1.2), nunca se inventa.
  · «docx §N»           → `guia-restaurante-peruano.docx`, párrafo citado.
  · «parametrizado»     → NO sale de ningún fichero de esta guía ni de la
    SPEC. Va en celda verde con nota, declarado como ejemplo editable.

──────────────────────────────────────────────────────────────────────────
UNA SOLA FUENTE POR MAGNITUD (§7-bis.7) — lo medido en el censo propio
──────────────────────────────────────────────────────────────────────────
El `pl-mensual-escenarios.xlsx` (escenario Realista: Ventas sala 30.000 +
Barra piscos y coctelería 10.000 + Delivery 8.000 + Bebidas 7.000 =
55.000 EUR/mes) y el `'P&L Mensual'` de `plan-financiero-3-anos.xlsx` YA
comparten exactamente las mismas cuatro líneas de ingreso, mes a mes, y los
mismos 11 conceptos de coste fijo (Alquiler 4.500 · Personal cocina 17.000 ·
Personal sala 12.000 · Suministros 2.800 · Seguros 350 · Gestoría 400 ·
Marketing 900 · Tecnología 350 · Mantenimiento 300 · Reposición pisco 1.200 ·
Varios 500 = 40.300 EUR/mes) — verificado abriendo los dos ficheros, coincide
al céntimo en las 15 líneas y en los dos TOTALES. No hace falta
`PLAN['pl_mensual']`: la precarga ya la trae v1.1 (a diferencia del
representante, que sí la necesita).

Lo que SÍ cambia con la aplicación de §2.3.5 (fondo de maniobra dimensionado,
DOM-01): la partida «Fondo de maniobra (3 meses)» de `Inversión` (50.000 EUR,
tecleada) pasa a fórmula = estructura mensual (fijos + variables del propio
P&L: 40.300 + 17.000 = 57.300 EUR/mes, con el food cost al 30 % que ya declara
el rótulo) × 6 meses (mínimo de la SPEC, no los 3 que rotulaba la fila) =
343.800 EUR. La «TOTAL INVERSIÓN» sube de 300.400 EUR (que YA incluía el
antiguo fondo de 50.000 EUR) a 594.200 EUR (250.400 EUR del resto de 43
partidas + 343.800 EUR de fondo calculado) — verificado en el dry-run
(informe T6). Es la misma corrección que ya aplicaron el representante, casual
y mexicano, y por el mismo motivo: el «130.000 EUR-300.000 EUR» que el docx
(párrafo 53) anuncia como rango de inversión, y el propio título de
`calculadora-capex.xlsx` («Inversión 130K-300K€»), se quedan MUY cortos frente
al coste real de abrir con un fondo de maniobra que cumpla el mínimo legal
defendible. **No se corrige a la baja**: es efecto correcto de la corrección,
y el ajuste del texto de la landing/docx es T7/T8, fuera del alcance de T6
(post-proceso de los xlsx). Se deja anotado en el informe.

§7-bis.14 (Pesimista «malo, no inviable») — el Pesimista de peruano es
ARITMÉTICAMENTE correcto (verificado a mano: 22.500+7.500+6.000+5.250=41.250 =
TOTAL INGRESOS; 12.375+500=12.875 = TOTAL COSTES VARIABLES —food cost 30 % de
41.250 = 12.375—; TOTAL COSTES FIJOS 40.300 en las tres hojas —los costes
fijos NO varían por escenario, sólo ingresos y food cost—; EBITDA =
41.250-12.875-40.300 = -11.925, que cuadra con el B31 cacheado) y es un
escenario del mismo orden que el de japonés que motivó la decisión de la SPEC
(-12.055 EUR/mes): -11.925 EUR/mes = -143.100 EUR/año sobre una facturación
Pesimista de 495.000 EUR/año (-28,9 % de margen).

⚠️ **RD-PERU-01 (alta, no sólo el Pesimista) — verificado en el dry-run tras
escribir el motor.** El escenario REALISTA (55.000 EUR/mes de facturación,
40.300 EUR/mes de costes fijos, food cost 30 %) YA daba EBITDA negativo en
v1.1: `Realista!B31 = -2.300` (-27.600 EUR/año), y es aritméticamente correcto
(verificado por pycel: `recalculado=-2300.0, coincide=true`). Es el MISMO
número, con la MISMA fuente, que el `'P&L Mensual'` de `plan-financiero-
3-anos.xlsx` (Ingresos 55.000 - Food cost 16.500 - Packaging 500 - Fijos
40.300 = -2.300 EUR/mes), así que NUEVO-01 (§2.5) al encadenarse en
`Proyección 3 Años` arrastra el mismo problema de fondo: el Año 1 nace de un
mes base con EBITDA negativo. Igual que RD-MEX-04/RD-CASUAL-04: no se
recalibra en esta tanda (el cableado para propagar una recalibración al TOTAL
de la variante «tres hojas» no existe en `grupo_a.py`, y tocar
Realista!B6:B9/Break-Even!B5:B9 sin fuente sería inventar cifras del negocio,
prohibido por §7-bis). Se documenta con severidad ALTA en el informe de T6
para que el orquestador decida en T7/T8/§7.3 si el concepto necesita un ticket
medio más alto, más cubiertos/día o menos coste fijo antes de publicarse como
«viable» en la landing — el defecto es del NEGOCIO descrito por v1.1, no de
este post-proceso, que se limita a calcularlo con exactitud. El propio
`Break-Even!B5:B9` (fichero original: ticket 27 EUR, 80 comensales/día,
26 días/mes, food cost 30 %, costes fijos 40.300 EUR/mes) confirma el mismo
diagnóstico por su propio camino: margen de contribución mensual
`80×26×27×(1-0,30) = 39.312 EUR`, que se queda 988 EUR POR DEBAJO de los
40.300 EUR de costes fijos — verificado en pycel tras el dry-run,
`Break-Even!B13` devuelve `"No alcanzado"`, no un mes concreto. Es la MISMA
conclusión que el Realista del P&L (EBITDA negativo) llegando por una vía de
cálculo distinta (ticket plano de 27 EUR frente al ticket ponderado del
simulador de §2.1): dos calculadoras con parámetros de entrada propios —
ninguna de las dos es la «una sola fuente» que exige §7-bis.7 (que sólo cubre
inversión/personal/fondo de maniobra/headcount)— y las dos, independientemente,
dicen que el negocio tal como lo describe v1.1 no cubre sus costes fijos al
ritmo Realista. Verificado también en `cash-flow-break-even!'Cash Flow'!M27`
(saldo acumulado a 12 meses): con el fondo de maniobra de 343.800 EUR como
colchón inicial, el saldo acumulado a fin de año 1 es -67.800 EUR — negativo
pese al colchón de 6 meses.
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
    # docx no da un cubiertos/día directo para el simulador; el que se usa es
    # el mismo que Break-Even!B6 (fichero original de ESTA guía,
    # cash-flow-break-even.xlsx) para no inventar una segunda cifra: 80
    # comensales/día. Días abierto: Break-Even!B7 = 26 (fichero original).
    'cubiertos_dia': 80,     # fuente: fichero original — Break-Even!B6
    'dias_mes': 26,          # fuente: fichero original — Break-Even!B7
}

# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx — variante «tres hojas»
# ==========================================================================
#: Las 3 hojas (Pesimista/Realista/Optimista) llegan con TODO tecleado y
#: aritméticamente correctas (verificado a mano, ver cabecera del módulo).
#: `grupo_a.py` las convierte en fórmula (NUEVO-01 no aplica aquí: peruano SÍ
#: tenía sus totales calculados a mano, a diferencia de los 5 hermanos que
#: describe la SPEC — el defecto real es que eran CONSTANTES, no fórmulas).
#: No se precarga ninguna línea de detalle: `PL` se queda vacío a propósito.
#: §7-bis.14 — NO recalibrado en esta tanda, con motivo (ver cabecera del
#: módulo, id RD-PERU-01): el motor compartido no tiene el cableado para
#: propagar una nota de recalibración al TOTAL en la variante «tres hojas».
PL = {}

# ==========================================================================
# §2.3 · plan-financiero-3-anos.xlsx
# ==========================================================================
PLAN = {
    'proyeccion': {
        # parametrizado: ni la SPEC ni el docx fijan un crecimiento propio de
        # peruano. Mismo criterio que el representante, casual y mexicano
        # (§2.3.1): un concepto de restauración temática recién llegado a un
        # barrio crece más rápido el año 2 que el 3, cuando ya ha madurado.
        'crecimiento': {'C': 0.08, 'D': 0.05},
        'inflacion': {'C': 0.03, 'D': 0.03},
        'impuesto_sociedades': 0.25,
    },
    'financiacion': {
        # parametrizado: préstamo de EJEMPLO. La necesidad total, tras
        # aplicar §2.3.5 (fondo de maniobra a 6 meses = 6 x 57.300 EUR de
        # estructura mensual del P&L), sube de 300.400 EUR (con el fondo
        # viejo de 50.000 EUR ya dentro) a 594.200 EUR (250.400 EUR del resto
        # de las 43 partidas + 343.800 EUR de fondo calculado; verificado en
        # el dry-run, informe T6). Préstamo de ejemplo: 420.000 EUR a 8 años
        # al 6,0 %, 1 año de carencia (mismo criterio que representante,
        # casual y mexicano: la carencia ocupa un año ENTERO, no una fracción
        # — con una fracción de año la hoja de Financiación, que decide la
        # cuota por año completo, no la repartiría correctamente entre
        # carencia y cuota completa dentro del mismo ejercicio). Fondos
        # propios = 594.200 - 420.000 = 174.200 EUR.
        'importe': 420000,
        'plazo': 8,
        'tipo': 0.06,
        'carencia': 1,
        'fondos_propios': 174200,   # verificado en el dry-run: cuadra exacto
        'otras_fuentes': 0,
    },
    # SPEC §2.3.5/§7-bis.3: mínimo 6 meses. NO se sube más allá del mínimo:
    # el propio docx (párrafo 62) ya da un rango de fondo de maniobra a 3
    # meses (25.000-65.000 EUR) que confirma que 3 meses es la práctica de
    # v1.1, no un margen de sobra; 6 es el suelo defendible de la SPEC, no un
    # extra sin fuente.
    'fondo_maniobra': {'meses': 6},
    # Los 5 hermanos (§2.3.5, grupo_a.fondo_de_maniobra) NO devuelven filas
    # de alquiler/personal en el P&L de la variante «tres hojas» (pl-mensual-
    # escenarios.xlsx), así que el bloque de PREAPERTURA (rentas y nóminas
    # antes de abrir) no se activa aquí — es una limitación conocida y
    # documentada de esa variante (verificada ya en casual y mexicano), no un
    # olvido de este módulo.
    'preapertura': {},
    # §2.3.6 — correspondencia de las 44 partidas de `Inversión` (plan-
    # financiero) con las 12 categorías de `calculadora-capex!CAPEX
    # Desglosado`, medida abriendo los dos ficheros (fuente: fichero
    # original en los dos lados; las 44 partidas de Inversión y las 35 de
    # CAPEX Desglosado se agrupan en las MISMAS 12 categorías).
    'capex_map': {
        r'^acondicionamiento local': 'Obra',
        r'^instalaciones electricas y gas': 'Obra',
        r'^fontaneria y saneamiento': 'Obra',
        r'^climatizacion': 'Obra',
        r'^extraccion reforzada': 'Obra',
        r'^wok profesional': 'Cocina PE',
        r'^mesa refrigerada estacion ceviche': 'Cocina PE',
        r'^parrilla anticuchos': 'Cocina PE',
        r'^horno pollo a la brasa': 'Cocina PE',
        r'^licuadoras industriales': 'Cocina PE',
        r'^exprimidor citricos': 'Cocina PE',
        r'^tablas corte extra grandes cevichero': 'Cocina PE',
        r'^horno mixto': 'Cocina',
        r'^cocina gas 6 fuegos': 'Cocina',
        r'^freidora doble': 'Cocina',
        r'^camaras frigorificas': 'Cocina',
        r'^congelador': 'Cocina',
        r'^tren de lavado': 'Cocina',
        r'^campana extractora': 'Cocina',
        r'^menaje y utensilios': 'Cocina',
        r'^vitrina iluminada botellas pisco': 'Barra',
        r'^utensilios cocteleria peruana': 'Barra',
        r'^stock inicial pisco': 'Barra',
        r'^maquina de hielo': 'Barra',
        r'^mobiliario interior': 'Sala',
        r'^barra \+ taburetes': 'Sala',
        r'^textiles andinos': 'Decoración',
        r'^ceramica precolombina': 'Decoración',
        r'^revestimientos madera natural': 'Decoración',
        r'^iluminacion calida': 'Decoración',
        r'^vajilla ceramica artesanal': 'Decoración',
        r'^plantas tropicales': 'Decoración',
        r'^mobiliario exterior': 'Terraza',
        r'^sombrillas': 'Terraza',
        r'^tpv \+ pantallas': 'Tech',
        r'^web \+ carta qr': 'Tech',
        r'^licencia actividad \+ terraza': 'Licencias',
        r'^proyecto tecnico': 'Licencias',
        r'^registro eori': 'Licencias',
        r'^branding peruano': 'Marketing',
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
#: `Break-Even!B5:B9` YA trae valores propios (ticket 27 EUR, 80 comensales/
#: día, 26 días/mes, food cost 30 %, costes fijos 40.300 EUR/mes — los tres
#: últimos COINCIDEN con `plan-financiero!'P&L Mensual'`; el ticket de 27 EUR
#: es distinto del ticket ponderado del simulador porque Break-Even mide un
#: ticket MEDIO de sala, y el simulador calcula el ticket completo con barra
#: de piscos y postre por separado — no se fuerza a que coincidan: son
#: magnitudes distintas, ninguna de las dos está en la lista de «una sola
#: fuente» del §7-bis.7) y sólo le falta B13 «Break-Even (meses)», que
#: `grupo_a.py` calcula solo desde el flujo acumulado de `Cash Flow`.
CASH = {
    # Repetidas con nota, no enlazadas (§1.13): son las cuotas del préstamo
    # de ejemplo de PLAN.financiacion (420.000 EUR, 8 años, 6,0 %, 1 año de
    # carencia). Verificado tras ejecutar `hoja_financiacion` (§ informe) con
    # pycel sobre el fichero YA escrito: la amortización corre sobre los 7
    # años POSTERIORES a la carencia (84 meses, no los 96 del plazo total) →
    # cuota mensual post-carencia = 6.135,59 EUR/mes (idéntica a la de
    # mexicano, que usa el mismo importe/tipo/plazo/carencia); cuota durante
    # la carencia (solo intereses) = 420.000 x 0,005 = 2.100,00 EUR/mes.
    'cuota_mensual': 6135.59,   # verificado: Financiación!B12 (post-carencia)
    'cuota_carencia': 2100.0,   # verificado: Financiación!B13 (solo intereses)
    # 'anio': 1 → durante el AÑO 1 (dentro de la carencia) sólo se usa
    # `cuota_carencia`; `cuota_mensual` queda documentado para cuando el
    # cliente copie el cash flow al año 2+ (nota de la propia hoja).
    'anio': 1,
    'necesidad_total': 594200.0,   # verificado: Inversión!C50
    'iva_bebida': 0.21,
    # Rampa de apertura sobre el escenario REALISTA (55.000 EUR/mes) — mismo
    # criterio que el representante, casual y mexicano (§2.4): parametrizada,
    # en verde.
    'rampa': (0.60, 0.70, 0.80, 0.85, 0.90, 0.95,
              1.00, 1.00, 1.00, 1.00, 1.00, 1.00),
    'mes_tipo': {
        'ingresos': {r'^ventas sala': 30000, r'^barra piscos': 10000,
                     r'^delivery': 8000, r'^bebidas': 7000},
        # food cost 30 % de 55.000 EUR (Realista) = 16.500 EUR. El Cash Flow
        # de esta guía no tiene línea de «packaging delivery» propia (a
        # diferencia del P&L, que sí la separa): se queda dentro de «Materia
        # prima + ajíes + pescado fresco», que es como lo rotula el fichero
        # original.
        'variables': {r'^materia prima': 16500},
        # A diferencia de casual (una sola línea «Personal»), el Cash Flow de
        # peruano trae DOS líneas separadas — «Personal cocina» y «Personal
        # sala» — igual que el P&L: se respetan por separado (fichero
        # original).
        'fijos': {r'^personal cocina': 17000, r'^personal sala': 12000,
                  r'^alquiler': 4500, r'^suministros': 2800,
                  r'^marketing': 900,
                  r'^reposicion stock pisco': 1200,
                  r'^tecnologia': 350,
                  # «Otros gastos» del Cash Flow agrega lo que el P&L separa
                  # en Seguros(350) + Gestoría(400) + Mantenimiento(300) +
                  # Varios(500) = 1.550 EUR: no hay una línea de Cash Flow
                  # para cada una por separado (fichero original, 9 salidas
                  # frente a las 11 del P&L; mismo recuento que mexicano).
                  r'^otros gastos': 1550},
        # IVA soportado: 10 % de la materia prima (alimentación) y 21 % del
        # resto de gastos con IVA (nóminas y SS no llevan). Base de gastos
        # con IVA = alquiler + suministros + marketing + reposición pisco +
        # tecnología + otros = 4.500+2.800+900+1.200+350+1.550 = 11.300 EUR.
        'iva_soportado': {'variables': 0.10, 'fijos_con_iva': 11300,
                          'tipo_fijos': 0.21},
    },
    # Saldo inicial de tesorería = fondo de maniobra que dimensiona
    # plan-financiero-3-anos!Inversión (§2.3.5): 6 x 57.300 EUR = 343.800 EUR
    # (verificado en el dry-run: Inversión!fila del fondo calculado).
    'apertura': {'saldo_inicial': 343800.0, 'desembolso_capex': None,
                 'iva_capex': None},
    'break_even': {
        # NO se toca: son fichero original de ESTA guía (Break-Even!B5:B9) y
        # ya son coherentes con el resto del pack (costes fijos 40.300 EUR/
        # mes = TOTAL COSTES FIJOS del P&L; food cost 30 % = el mismo de
        # pl-mensual y del escandallo). `grupo_a._break_even_hoja_propia` los
        # LEE de la hoja, no hace falta repetirlos aquí.
    },
}

# ==========================================================================
# §2.3.6 · calculadora-capex.xlsx — variante «desglosado»
# ==========================================================================
#: `CAPEX Desglosado` YA trae 35 partidas con importe y fila TOTAL con SUM
#: (fichero original): no hace falta precargar nada. Lo único que le falta,
#: y que `grupo_a.py` añade sin contenido adicional, es §1 (protección,
#: formato por tipo, versión, bio) — no hay «rangos de mercado» que
#: reconciliar porque esta variante no los tiene (a diferencia del
#: representante): es ya el desglose «Mi CAPEX» de peruano.
CAPEX = {}
