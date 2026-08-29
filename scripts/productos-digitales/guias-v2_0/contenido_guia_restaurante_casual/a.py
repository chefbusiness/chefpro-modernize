# -*- coding: utf-8 -*-
"""
contenido_guia_restaurante_casual/a.py — el CONTENIDO del grupo A (§2 de
`guias-v2-SPEC.md`) para la guía «Cómo Montar un Restaurante Casual» (80
plazas, 65 EUR, hermano T6 del representante gastronómico).

`grupo_a.py` pone la lógica de familia (detección de variante, localización de
filas por etiqueta); aquí van las filas, los textos, los importes y los
parámetros **propios de esta guía**. Casual es la variante «hermanos»
(§2 cabecera de la SPEC) en las cinco piezas: ticket en columna única,
`pl-mensual-escenarios` en TRES hojas con todo tecleado, escandallo modelo E2
(merma como recargo, a corregir), matrix M2 (YA con 10 platos reales) y
`calculadora-capex` variante «desglosado». La mecánica de cada una NO se repite
aquí: vive en `grupo_a.py` y ya está verificada contra el representante.

FUENTE DE CADA CIFRA:
  · «fichero original» → ya estaba en el `.xlsx` de esta guía (v1.1) y se
    conserva o se convierte en fórmula (§1.2), nunca se inventa.
  · «docx §N»           → `guia-restaurante-casual.docx`, capítulo citado.
  · «parametrizado»     → NO sale de ningún fichero de esta guía ni de la SPEC.
    Va en celda verde con nota, declarado como ejemplo editable.

──────────────────────────────────────────────────────────────────────────
UNA SOLA FUENTE POR MAGNITUD (§7-bis.7) — lo medido en el censo propio
──────────────────────────────────────────────────────────────────────────
A diferencia del representante, en casual el `pl-mensual-escenarios.xlsx`
(escenario Realista: 59.000 EUR/mes) y el `'P&L Mensual'` de
`plan-financiero-3-anos.xlsx` YA comparten exactamente las mismas cuatro
líneas de ingreso mes a mes (Ventas sala 35.000 / Menú del día 8.000 /
Delivery 6.000 / Bebidas 10.000 = 59.000 EUR/mes en las dos hojas): no hace
falta calibrar nada para que cuadren, sólo verificarlo (hecho: coincide al
céntimo en las 4 líneas y en el TOTAL). El personal de `plantilla-turnos-
brigada.xlsx` (§7-bis.16 abajo) da un bruto anual de 291.088 EUR/año
(161.994 EUR cocina + 129.094 EUR sala), que es coherente con los
14.000+11.000 = 25.000 EUR/mes = 300.000 EUR/año que las dos hojas de P&L ya
llevan (diferencia 3 %, dentro de lo razonable para un «ejemplo» tomado de un
punto prudente del rango del capítulo 13/14).

Lo que SÍ cambia con la aplicación de §2.3.5 (fondo de maniobra dimensionado,
DOM-01): la partida «Fondo de maniobra (3 meses)» de `Inversión` (55.000 EUR,
tecleada) pasa a fórmula = estructura mensual (fijos + variables del propio
P&L: 35.000 + 18.100 = 53.100 EUR/mes) × 6 meses (mínimo de la SPEC, no los 3
que rotulaba la fila) = 318.600 EUR. La «TOTAL INVERSIÓN» sube de
305.000 EUR a 568.600 EUR, muy por encima del «150.000 EUR-350.000 EUR» que
el cap. 4 anuncia como rango de inversión. **No se corrige a la baja**: es la
misma corrección que el representante ya aplicó (DOM-01/COM-30) y que hizo
subir su propia inversión; el ajuste del texto de la landing/docx (que el
cap. 4 declare el rango real) es capa de producto/documentos (T7/T8), fuera
del alcance de T6 (post-proceso de los xlsx). Se deja anotado en el informe.
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
    # docx §7 (viñeta «Tráfico peatonal…») no da un cubiertos/día directo; el
    # que se usa es el mismo que Break-Even!B6 (fichero original de ESTA
    # guía, cash-flow-break-even.xlsx) para no inventar una segunda cifra:
    # 90 comensales/día. Días abierto: Break-Even!B7 = 26 (fichero original).
    'cubiertos_dia': 90,     # fuente: fichero original — Break-Even!B6
    'dias_mes': 26,          # fuente: fichero original — Break-Even!B7
}

# ==========================================================================
# §2.2 · pl-mensual-escenarios.xlsx — variante «tres hojas»
# ==========================================================================
#: Las 3 hojas (Pesimista/Realista/Optimista) llegan con TODO tecleado y
#: aritméticamente correctas (verificado a mano: 26.250+6.000+4.500+7.500 =
#: 44.250 = TOTAL INGRESOS Pesimista; 4.500+14.000+11.000+2.800+350+400+800+
#: 350+300+500 = 35.000 = TOTAL COSTES FIJOS en las tres). `grupo_a.py` las
#: convierte en fórmula (NUEVO-01 no aplica aquí: casual SÍ tenía sus totales
#: calculados a mano, a diferencia de los 5 hermanos de la SPEC — el defecto
#: real es que eran CONSTANTES, no fórmulas). No se precarga ninguna línea de
#: detalle: `PL` se queda vacío a propósito.
#:
#: §7-bis.14 (Pesimista «malo, no inviable») — VERIFICADO y NO recalibrado
#: por valores en T6, con motivo. El Pesimista de casual da EBITDA
#: -4.425 EUR/mes (-53.100 EUR/año, -10,0 % sobre 44.250 EUR de facturación):
#: peor que el escenario del representante, pero lejos del -12.055 EUR/mes
#: (-145 k EUR/año) de japonés que motivó la decisión de la SPEC. Se intentó
#: recalibrar en esta misma tanda subiendo «Ventas sala» y bajando «Varios»
#: — la comprobación §1.2 del motor (tolerancia de 0,01 EUR entre la
#: constante vieja y el resultado de la fórmula nueva) lo rechazó, porque
#: `grupo_a.pl_tres_hojas()` no tiene forma de pasarle una `nota_dif` a la
#: fórmula del TOTAL cuando una línea de detalle cambia de valor: ese
#: cableado (propagar la nota de una línea recalibrada hasta el `a_formula()`
#: del TOTAL que la suma) no existe hoy para la variante «tres hojas» y es un
#: cambio en el módulo COMPARTIDO por las 8 guías — fuera del alcance de este
#: paquete de contenido (T6 = «adapta `contenido_<pid>.py`», no «modifica
#: `grupo_a.py`»). Queda como hallazgo para una futura tanda de motor
#: (§ informe, id RD-CASUAL-02): la fórmula correcta sería sumar a
#: `nota_dif` cada nota de `conf['notas']` cuyo patrón matchee una fila cuyo
#: valor de v1.1 se haya sobrescrito.
PL = {}

# ==========================================================================
# §2.3 · plan-financiero-3-anos.xlsx
# ==========================================================================
PLAN = {
    'proyeccion': {
        # parametrizado: ni la SPEC ni el docx fijan un crecimiento propio de
        # casual. Mismo criterio que el representante (§2.3.1).
        'crecimiento': {'C': 0.07, 'D': 0.05},
        'inflacion': {'C': 0.03, 'D': 0.03},
        'impuesto_sociedades': 0.25,
    },
    'financiacion': {
        # parametrizado: préstamo de EJEMPLO. La necesidad total, tras aplicar
        # §2.3.5 (fondo de maniobra dimensionado a 6 meses = 6 x 53.100 EUR de
        # estructura mensual del P&L), sube de 305.000 EUR a 568.600 EUR
        # (250.000 EUR de CAPEX sin la partida de maniobra + 318.600 EUR de
        # fondo de maniobra calculado; verificado en el dry-run, informe T6).
        # Préstamo de ejemplo: 380.000 EUR a 8 años al 6,0 %, 1 año de
        # carencia (mismo criterio que el representante: la carencia ocupa un
        # año ENTERO, no una fracción — con una fracción de año la hoja de
        # Financiación, que decide la cuota por año completo, no la
        # repartiría correctamente entre carencia y cuota completa dentro del
        # mismo ejercicio). Fondos propios = 568.600 - 380.000 = 188.600 EUR.
        'importe': 380000,
        'plazo': 8,
        'tipo': 0.06,
        'carencia': 1,
        'fondos_propios': 188600,   # verificado en el dry-run: cuadra exacto
        'otras_fuentes': 0,
    },
    # SPEC §2.3.5/§7-bis.3: mínimo 6 meses. NO se sube más allá del mínimo:
    # el propio docx (cap. 4) ya avisa de que «el fondo de maniobra es donde
    # más emprendedores se quedan cortos», así que 6 es el suelo defendible,
    # no un margen extra sin fuente.
    'fondo_maniobra': {'meses': 6},
    # Los 5 hermanos (§2.3.5, grupo_a.fondo_de_maniobra) NO devuelven filas
    # de alquiler/personal en el P&L de esta variante, así que el bloque de
    # PREAPERTURA (rentas y nóminas antes de abrir) no se activa aquí — es
    # una limitación conocida y documentada de la variante «tres hojas»/
    # «P&L Mensual sin desglose de personal», no un olvido de este módulo.
    'preapertura': {},
    # §2.3.6 — correspondencia de las 23 partidas de `Inversión` (plan-
    # financiero) con las 10 categorías de `calculadora-capex!CAPEX
    # Desglosado`, medida abriendo los dos ficheros (fuente: fichero
    # original en los dos lados).
    'capex_map': {
        r'^acondicionamiento local': 'Obra',
        r'^instalaciones electricas y gas': 'Obra',
        r'^fontaneria y saneamiento': 'Obra',
        r'^climatizacion': 'Obra',
        r'^equipamiento cocina completo': 'Cocina',
        r'^campana extractora': 'Cocina',
        r'^menaje, ollas': 'Cocina',
        r'^mobiliario interior': 'Sala',
        r'^barra y taburetes': 'Sala',
        r'^iluminacion decorativa': 'Sala',
        r'^decoracion e interiorismo': 'Sala',
        r'^mobiliario terraza': 'Terraza',
        r'^sombrillas': 'Terraza',
        r'^vajilla, cristaleria': 'Vajilla',
        r'^tpv \+ software': 'Tech',
        r'^web \+ carta digital': 'Tech',
        r'^licencia actividad': 'Licencias',
        r'^proyecto tecnico': 'Licencias',
        r'^branding, diseno': 'Marketing',
        r'^campana pre-apertura|^campana pre.apertura': 'Marketing',
        r'^materia prima inicial': 'Stock',
        r'^bebidas y bodega inicial': 'Stock',
        r'^fondo de maniobra': 'Maniobra',
    },
    # Las 23 partidas SON las de v1.1 (fichero original): no se tocan salvo
    # la de fondo de maniobra, que grupo_a.fondo_de_maniobra() convierte en
    # fórmula por sí solo (no necesita 'inversion' aquí: no hay ninguna
    # partida vacía que precargar, a diferencia del representante).
}

# ==========================================================================
# §2.4 · cash-flow-break-even.xlsx — variante «cash-y-breakeven»
# ==========================================================================
#: `Cash Flow` llega ENTERAMENTE en blanco (B5:N27, fichero original) y
#: `Break-Even!B5:B9` YA trae valores propios (ticket 28 EUR, 90 comensales/
#: día, 26 días/mes, food cost 30 %, costes fijos 35.000 EUR/mes — los cuatro
#: últimos COINCIDEN con `plan-financiero!'P&L Mensual'` y con
#: `plantilla-turnos-brigada`; el ticket de 28 EUR es mayor que el 23,95 EUR
#: del simulador de ticket medio porque Break-Even mide un ticket CON bebida,
#: y el simulador, sin ella — no se fuerza a que coincidan: son magnitudes
#: distintas, ninguna de las dos está en la lista de «una sola fuente»
#: del §7-bis.7, que sólo cubre inversión/personal/fondo de maniobra/
#: headcount) y sólo le falta B13 «Break-Even (meses)», que `grupo_a.py`
#: calcula solo desde el flujo acumulado de `Cash Flow`.
CASH = {
    # Repetidas con nota, no enlazadas (§1.13): son las cuotas del préstamo
    # de ejemplo de PLAN.financiacion (380.000 EUR, 8 años, 6,0 %, 6 meses de
    # carencia). Verificado tras ejecutar `hoja_financiacion` (§ informe).
    'cuota_mensual': 5317.03,  # verificado: Financiación!B12 (post-carencia)
    'cuota_carencia': 1900.0,  # verificado: Financiación!B13 (solo intereses)
    'anio': 1,
    'necesidad_total': 568600.0,   # verificado: Inversión!C40
    'iva_bebida': 0.21,
    # Rampa de apertura sobre el escenario REALISTA (59.000 EUR/mes) — mismo
    # criterio que el representante (§2.4): parametrizada, en verde.
    'rampa': (0.60, 0.70, 0.80, 0.85, 0.90, 0.95,
              1.00, 1.00, 1.00, 1.00, 1.00, 1.00),
    'mes_tipo': {
        'ingresos': {r'^ventas sala': 35000, r'^menu del dia': 8000,
                     r'^delivery': 6000, r'^bebidas': 10000},
        'variables': {r'^materia prima': 17700},   # food cost 30% Realista
        'fijos': {r'^personal': 25000, r'^alquiler': 4500,
                  r'^suministros': 2800, r'^marketing': 800,
                  r'^tecnologia': 350, r'^otros gastos': 1550},
        # IVA soportado: 10 % de la materia prima y 21 % del resto de gastos
        # con IVA (nóminas y SS no llevan). Base de gastos con IVA = todo lo
        # de «fijos» salvo el personal: 4.500+2.800+800+350+1.550 = 10.000.
        'iva_soportado': {'variables': 0.10, 'fijos_con_iva': 10000,
                          'tipo_fijos': 0.21},
    },
    # RD-07 (representante) / mismo criterio aquí: saldo inicial = fondo de
    # maniobra que dimensiona plan-financiero-3-anos!Inversión (§2.3.5).
    # Se rellena tras verificar el importe exacto (§ informe).
    # Saldo inicial de tesorería = fondo de maniobra que dimensiona
    # plan-financiero-3-anos!Inversión (§2.3.5): 6 x 53.100 EUR = 318.600 EUR
    # (verificado en el dry-run: Inversión!C37).
    'apertura': {'saldo_inicial': 318600.0, 'desembolso_capex': None,
                 'iva_capex': None},
    'break_even': {
        # NO se toca: son fichero original de ESTA guía (Break-Even!B5:B9) y
        # ya son coherentes con el resto del pack (costes fijos 35.000 EUR/
        # mes = TOTAL COSTES FIJOS del P&L; food cost 30 % = el mismo de
        # pl-mensual y del escandallo). `grupo_a._break_even_hoja_propia` los
        # LEE de la hoja, no hace falta repetirlos aquí.
    },
}

# ==========================================================================
# §2.3.6 · calculadora-capex.xlsx — variante «desglosado»
# ==========================================================================
#: `CAPEX Desglosado` YA trae 30 partidas con importe y fila TOTAL con SUM
#: (fichero original): no hace falta precargar nada. Lo único que le falta,
#: y que `grupo_a.py` añade sin contenido adicional, es §1 (protección,
#: formato por tipo, versión, bio) — no hay «rangos de mercado» que
#: reconciliar porque esta variante no los tiene (a diferencia del
#: representante): es ya el desglose «Mi CAPEX» de casual.
CAPEX = {}
