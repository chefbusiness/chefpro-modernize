# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_japones/a.py — el CONTENIDO del grupo A (§2 de
`guias-v2-SPEC.md`) para la guía «Cómo Montar un Restaurante Japonés» (60
plazas, 65 EUR, hermano T6 del representante gastronómico).

`grupo_a.py` pone la lógica de familia (detección de variante, localización de
filas por etiqueta); aquí van las filas, los textos, los importes y los
parámetros **propios de esta guía**. Japonés es la variante «hermanos» (§2
cabecera de la SPEC), igual que casual/mexicano/peruano/nikkei: ticket en
columna única, `pl-mensual-escenarios` en TRES hojas ya tecleadas, escandallo
modelo E2 (merma como recargo, a corregir por el motor) y `calculadora-capex`
variante «desglosado». La mecánica de cada pieza NO se repite aquí: vive en
`grupo_a.py` y ya está verificada contra el representante, casual, mexicano y
peruano (T6 previos, mismo mecanismo).

FUENTE DE CADA CIFRA:
  · «fichero original» → ya estaba en el `.xlsx` de esta guía (v1.1) y se
    conserva o se convierte en fórmula (§1.2), nunca se inventa.
  · «docx §N»           → `guia-restaurante-japones.docx`, párrafo citado.
  · «parametrizado»     → NO sale de ningún fichero de esta guía ni de la
    SPEC. Va en celda verde con nota, declarado como ejemplo editable.

──────────────────────────────────────────────────────────────────────────
UNA SOLA FUENTE POR MAGNITUD (§7-bis.7) — lo medido en el censo propio
──────────────────────────────────────────────────────────────────────────
`pl-mensual-escenarios.xlsx` (escenario Realista: Ventas sala 45.000 + Barra
sake/whisky 15.000 + Delivery 10.000 + Bebidas 8.000 = 78.000 EUR/mes) y el
`'P&L Mensual'` de `plan-financiero-3-anos.xlsx` YA comparten exactamente las
mismas cuatro líneas de ingreso, mes a mes, y los mismos 11 conceptos de coste
fijo (Alquiler 6.500 · Personal cocina 22.000 · Personal sala 13.000 ·
Suministros 3.500 · Seguros 500 · Gestoría 500 · Marketing 1.200 · Tecnología
450 · Mantenimiento 400 · Reposición sake/whisky 1.800 · Varios 700 =
50.550 EUR/mes) — verificado abriendo los dos ficheros, coincide al céntimo en
las 14 líneas y en los dos TOTALES. No hace falta `PLAN['pl_mensual']`: la
precarga ya la trae v1.1 (a diferencia del representante, que sí la necesita).

⚠️ **§7-bis.14 — JAPONÉS es el caso que motivó la propia decisión de la SPEC**
(«el de japonés entrega un EBITDA de −12.055 €/mes… se recalibra con el
módulo de contenido y queda etiquetado como valor de ejemplo»). Verificado a
mano: Pesimista (v1.1) = Ventas 33.750 + Barra 11.250 + Delivery 7.500 +
Bebidas 6.000 = 58.500 TOTAL INGRESOS (75 % del Realista); Food cost 33 % de
58.500 = 19.305 + Packaging 700 = 20.005 TOTAL COSTES VARIABLES; Costes fijos
50.550 (idénticos en las tres hojas, fichero original); EBITDA =
58.500-20.005-50.550 = **-12.055**, que cuadra exacto con el `B31` cacheado
(-144.660 EUR/año, -20,6 % de margen sobre 702.000 EUR/año de facturación).
Aritméticamente CORRECTO, pero es el ejemplo que la propia SPEC cita como «no
prudencia, error de calibración que invalida la herramienta» — a diferencia de
peruano y mexicano (RD-PERU-01/RD-MEX-04, documentados sin recalibrar), aquí
SÍ toca recalibrar.

**Recalibración aplicada** (vía `PL['escenarios']['Pesimista']`, §1.2: el
valor viejo queda anotado como diferencia justificada por un defecto
corregido): Pesimista pasa del 75 % al **90 %** del Realista —sigue siendo el
peor de los tres escenarios y sigue por debajo del punto de equilibrio, «malo»
de verdad, pero deja de ser un año que por sí solo fulminaría el fondo de
maniobra en menos de 12 meses—: Ventas sala 40.500 (45.000×0,90) + Barra
13.500 (15.000×0,90) + Delivery 9.000 (10.000×0,90) + Bebidas 7.200
(8.000×0,90) = **70.200 TOTAL INGRESOS**; Food cost 33 % = 23.166 + Packaging
700 = 23.866 TOTAL COSTES VARIABLES; Costes fijos 50.550 (sin tocar: los fija
`Instrucciones!A7`, «son iguales en los 3 escenarios», y no hay fuente para
inventar un fijo distinto por escenario); **EBITDA = 70.200-23.866-50.550 =
-4.216 EUR/mes** (-50.592 EUR/año, -6,0 % de margen). Sigue en rojo —no se
maquilla a positivo, que sería falsear el escenario pesimista en la otra
dirección— pero un restaurante que cierra el año con un -6 % de margen en su
escenario MALO es una herramienta de planificación útil; uno que dice -20,6 %
en el mismo escenario no lo es. El % de recorte (90 % en vez de 75 %) es el
mismo criterio que ya fijó la propia hoja para el Optimista (125 % del
Realista, fichero original: 97.500/78.000=1,25): un pesimista simétrico al
optimista respecto del Realista (-10 % / +25 %, no siempre simétrico en % pero
sí en que ninguno de los dos convierte el negocio en un caso extremo)."""

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
    # cash-flow-break-even.xlsx) para no inventar una segunda cifra: 65
    # comensales/día. Días abierto: Break-Even!B7 = 26 (fichero original).
    'cubiertos_dia': 65,     # fuente: fichero original — Break-Even!B6
    'dias_mes': 26,          # fuente: fichero original — Break-Even!B7
}

# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx — variante «tres hojas»
# ==========================================================================
#: Las 3 hojas (Pesimista/Realista/Optimista) llegan con TODO tecleado.
#: Realista y Optimista son aritméticamente correctas (verificado a mano) y
#: NO se tocan (NUEVO-01 no aplica aquí igual que en peruano: japonés SÍ tenía
#: sus totales calculados a mano; el defecto real es que eran CONSTANTES, no
#: fórmulas — `grupo_a.py` las convierte). El Pesimista SÍ se recalibra
#: (§7-bis.14, ver cabecera del módulo): es el caso que la propia SPEC cita
#: por su nombre.
PL = {
    'escenarios': {
        'Pesimista': {
            r'^ventas sala': 40500,
            r'^barra sake': 13500,
            r'^delivery': 9000,
            r'^bebidas': 7200,
        },
    },
    'notas': {
        r'^ebitda': ('Recalibrado (§7-bis.14): el original de v1.1 daba '
                     '-12.055 EUR/mes (-144.660 EUR/año, -20,6% de margen) '
                     'tecleado a mano y aritméticamente correcto pero es el '
                     'caso que la propia SPEC cita como "no prudencia, error '
                     'de calibración". Ahora el Pesimista es el 90% del '
                     'Realista (antes 75%) en las cuatro líneas de ingreso, '
                     'con el mismo food cost (33%) y los mismos costes fijos '
                     '(50.550 EUR/mes, iguales en las tres hojas por diseño '
                     'de v1.1): EBITDA -4.216 EUR/mes (-6,0% de margen). '
                     'Sigue siendo el peor escenario y sigue en pérdidas: no '
                     'se maquilla a positivo.'),
    },
}

# ==========================================================================
# §2.3 · plan-financiero-3-anos.xlsx
# ==========================================================================
PLAN = {
    'proyeccion': {
        # parametrizado: ni la SPEC ni el docx fijan un crecimiento propio de
        # japonés. Mismo criterio que el representante, casual, mexicano y
        # peruano (§2.3.1): un concepto de restauración temática recién
        # llegado crece más rápido el año 2 que el 3, cuando ya ha madurado.
        'crecimiento': {'C': 0.08, 'D': 0.05},
        'inflacion': {'C': 0.03, 'D': 0.03},
        'impuesto_sociedades': 0.25,
    },
    'financiacion': {
        # parametrizado: préstamo de EJEMPLO. La necesidad total, tras
        # aplicar §2.3.5 (fondo de maniobra a 6 meses = 6 x estructura
        # mensual del P&L: 50.550 fijos + 26.440 variables del Realista =
        # 76.990 EUR/mes x6 = 461.940 EUR), sube de 436.400 EUR (con el fondo
        # viejo de 70.000 EUR ya dentro) a 828.340 EUR (366.400 EUR del resto
        # de las 45 partidas + 461.940 EUR de fondo calculado; a verificar en
        # el dry-run, informe T6, y a repatchear aquí si el cómputo real del
        # motor difiere de este cálculo manual). Préstamo de ejemplo: 580.000
        # EUR a 8 años al 6,0 %, 1 año de carencia (mismo criterio que
        # representante, casual, mexicano y peruano: la carencia ocupa un año
        # ENTERO, no una fracción). Fondos propios = 828.340 - 580.000 =
        # 248.340 EUR (~70 % de deuda, mismo orden que peruano 70,7 %).
        'importe': 580000,
        'plazo': 8,
        'tipo': 0.06,
        'carencia': 1,
        'fondos_propios': 248340,   # a verificar en el dry-run
        'otras_fuentes': 0,
    },
    # SPEC §2.3.5/§7-bis.3: mínimo 6 meses. NO se sube más allá del mínimo:
    # el propio docx (párrafo 57) ya da un rango de fondo de maniobra a 3
    # meses (45.000-95.000 EUR) que confirma que 3 meses es la práctica de
    # v1.1, no un margen de sobra; 6 es el suelo defendible de la SPEC.
    'fondo_maniobra': {'meses': 6},
    # Los 5 hermanos (§2.3.5, grupo_a.fondo_de_maniobra) NO devuelven filas
    # de alquiler/personal en el P&L de la variante «tres hojas» (pl-mensual-
    # escenarios.xlsx), así que el bloque de PREAPERTURA (rentas y nóminas
    # antes de abrir) no se activa aquí — es una limitación conocida y
    # documentada de esa variante (verificada ya en casual, mexicano y
    # peruano), no un olvido de este módulo.
    'preapertura': {},
    # §2.3.6 — correspondencia de las 46 partidas de `Inversión` (plan-
    # financiero) con las 13 categorías de `calculadora-capex!CAPEX
    # Desglosado`, medida abriendo los dos ficheros (fuente: fichero
    # original en los dos lados; las 46 partidas de Inversión y las 35 de
    # CAPEX Desglosado se agrupan en las MISMAS 13 categorías — japonés tiene
    # una categoría más que peruano, «Barra Sushi», separada de «Barra Sake»
    # porque los dos libros ya las distinguen).
    'capex_map': {
        r'^acondicionamiento local': 'Obra',
        r'^instalaciones electricas y gas': 'Obra',
        r'^fontaneria y saneamiento': 'Obra',
        r'^climatizacion': 'Obra',
        r'^extraccion reforzada': 'Obra',
        r'^suihanki': 'Cocina JP',
        r'^vitrina refrigerada de sashimi': 'Cocina JP',
        r'^ramen cooker': 'Cocina JP',
        r'^ollas de caldo': 'Cocina JP',
        r'^parrilla robata': 'Cocina JP',
        r'^plancha teppanyaki': 'Cocina JP',
        r'^cuchillos japoneses': 'Cocina JP',
        r'^ohitsu': 'Cocina JP',
        r'^maquina sake caliente': 'Cocina JP',
        r'^horno mixto': 'Cocina',
        r'^cocina gas 6 fuegos': 'Cocina',
        r'^wok profesional': 'Cocina',
        r'^freidora doble': 'Cocina',
        r'^camaras frigorificas': 'Cocina',
        r'^congelador certificado': 'Cocina',
        r'^tren de lavado': 'Cocina',
        r'^campana extractora reforzada': 'Cocina',
        r'^menaje y utensilios japoneses': 'Cocina',
        r'^barra de sushi profesional': 'Barra Sushi',
        r'^vitrina refrigerada sake': 'Barra Sake',
        r'^utensilios cocteleria japonesa': 'Barra Sake',
        r'^stock inicial sake': 'Barra Sake',
        r'^maquina de hielo': 'Barra Sake',
        r'^mobiliario interior mesas': 'Sala',
        r'^barra sushi taburetes': 'Sala',
        r'^madera natural en paredes': 'Decoracion',
        r'^noren': 'Decoracion',
        r'^lamparas washi': 'Decoracion',
        r'^jardin zen': 'Decoracion',
        r'^vajilla ceramica japonesa': 'Decoracion',
        r'^carbonilla': 'Decoracion',
        r'^mobiliario exterior': 'Terraza',
        r'^tpv \+ pantallas': 'Tech',
        r'^web \+ carta qr': 'Tech',
        r'^licencia actividad \+ terraza': 'Licencias',
        r'^registro eori': 'Licencias',
        r'^branding japones': 'Marketing',
        r'^fotos \+ video': 'Marketing',
        r'^materia prima inicial': 'Stock',
        r'^bebidas \(cerveza japonesa': 'Stock',
        r'^fondo de maniobra': 'Maniobra',
    },
    # Las 46 partidas SON las de v1.1 (fichero original): no se tocan salvo
    # la de fondo de maniobra, que grupo_a.fondo_de_maniobra() convierte en
    # fórmula por sí solo (no necesita 'inversion' aquí: no hay ninguna
    # partida vacía que precargar, a diferencia del representante).
}

# ==========================================================================
# §2.4 · cash-flow-break-even.xlsx — variante «cash-y-breakeven»
# ==========================================================================
#: `Cash Flow` llega ENTERAMENTE en blanco (B5:M27, fichero original) y
#: `Break-Even!B5:B9` YA trae valores propios (ticket 45 EUR, 65 comensales/
#: día, 26 días/mes, food cost 33%, costes fijos 50.550 EUR/mes — los tres
#: últimos COINCIDEN con `plan-financiero!'P&L Mensual'`; el ticket de 45 EUR
#: es distinto del ticket ponderado del simulador porque Break-Even mide un
#: ticket MEDIO de sala, y el simulador calcula el ticket completo con barra
#: de sake/whisky y postre por separado — no se fuerza a que coincidan: son
#: magnitudes distintas, ninguna de las dos está en la lista de «una sola
#: fuente» del §7-bis.7) y sólo le falta B13 «Break-Even (meses)», que
#: `grupo_a.py` calcula solo desde el flujo acumulado de `Cash Flow`.
CASH = {
    # Repetidas con nota, no enlazadas (§1.13): son las cuotas del préstamo
    # de ejemplo de PLAN.financiacion (580.000 EUR, 8 años, 6,0 %, 1 año de
    # carencia). Verificado tras ejecutar `hoja_financiacion` (§ informe) con
    # pycel sobre el fichero YA escrito: la amortización corre sobre los 7
    # años POSTERIORES a la carencia (84 meses, no los 96 del plazo total).
    # cuota mensual post-carencia calculada con la anualidad algebraica
    # (importe x i) / (1-(1+i)^-n): 580.000 x 0,005 / (1-1,005^-84)
    # ≈ 8.472,98 EUR/mes (mismo factor por euro que peruano: 6.135,59/420.000
    # = 8.472,98/580.000 = 0,0146086 EUR de cuota por EUR de principal).
    'cuota_mensual': 8472.98,   # a verificar: Financiación!B12 (post-carencia)
    'cuota_carencia': 2900.0,   # 580.000 x 0,06/12 (solo intereses)
    # 'anio': 1 → durante el AÑO 1 (dentro de la carencia) sólo se usa
    # `cuota_carencia`; `cuota_mensual` queda documentado para cuando el
    # cliente copie el cash flow al año 2+ (nota de la propia hoja).
    'anio': 1,
    'necesidad_total': 828340.0,   # a verificar: Inversión!C52
    'iva_bebida': 0.21,
    # Rampa de apertura sobre el escenario REALISTA (78.000 EUR/mes) — mismo
    # criterio que el representante, casual, mexicano y peruano (§2.4):
    # parametrizada, en verde.
    'rampa': (0.60, 0.70, 0.80, 0.85, 0.90, 0.95,
              1.00, 1.00, 1.00, 1.00, 1.00, 1.00),
    'mes_tipo': {
        'ingresos': {r'^ventas sala': 45000, r'^barra sake': 15000,
                     r'^delivery': 10000, r'^bebidas': 8000},
        # food cost 33% de 78.000 EUR (Realista) = 25.740 EUR + packaging
        # 700 EUR = 26.440 EUR. El Cash Flow de esta guía no tiene línea de
        # «packaging delivery» propia (a diferencia del P&L, que sí la
        # separa): se queda dentro de «Pescado sashimi-grade + arroz +
        # importados», que es como lo rotula el fichero original.
        'variables': {r'^pescado sashimi': 26440},
        # A diferencia de casual (una sola línea «Personal»), el Cash Flow de
        # japonés trae DOS líneas separadas — «Personal cocina (itamae)» y
        # «Personal sala» — igual que el P&L: se respetan por separado
        # (fichero original).
        'fijos': {r'^personal cocina': 22000, r'^personal sala': 13000,
                  r'^alquiler': 6500, r'^suministros': 3500,
                  r'^marketing': 1200,
                  r'^reposicion stock sake': 1800,
                  r'^tecnologia': 450,
                  # «Otros gastos» del Cash Flow agrega lo que el P&L separa
                  # en Seguros(500) + Gestoría(500) + Mantenimiento(400) +
                  # Varios(700) = 2.100 EUR: no hay una línea de Cash Flow
                  # para cada una por separado (fichero original, 9 salidas
                  # frente a las 11 del P&L; mismo recuento que peruano).
                  r'^otros gastos': 2100},
        # IVA soportado: 10 % de la materia prima (alimentación) y 21 % del
        # resto de gastos con IVA (nóminas y SS no llevan). Base de gastos
        # con IVA = alquiler + suministros + marketing + reposición sake +
        # tecnología + otros = 6.500+3.500+1.200+1.800+450+2.100 = 15.550 EUR.
        'iva_soportado': {'variables': 0.10, 'fijos_con_iva': 15550,
                          'tipo_fijos': 0.21},
    },
    # Saldo inicial de tesorería = fondo de maniobra que dimensiona
    # plan-financiero-3-anos!Inversión (§2.3.5): 6 x 76.990 EUR = 461.940 EUR
    # (a verificar en el dry-run: Inversión!fila del fondo calculado).
    'apertura': {'saldo_inicial': 461940.0, 'desembolso_capex': None,
                 'iva_capex': None},
    'break_even': {
        # NO se toca: son fichero original de ESTA guía (Break-Even!B5:B9) y
        # ya son coherentes con el resto del pack (costes fijos 50.550 EUR/
        # mes = TOTAL COSTES FIJOS del P&L; food cost 33% = el mismo de
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
#: representante): es ya el desglose «Mi CAPEX» de japonés.
CAPEX = {}
