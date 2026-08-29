#!/usr/bin/env python3
"""
Contenido de `plan-negocio-tapas-bar` para el grupo A (§2 de la SPEC, T7).

Molde **A-β** (idéntico patrón que `plan-negocio-cafeteria`, ya construido
como hermano de referencia de esta misma tanda): hojas SIN numerar
(`'Inversión Inicial'`, `'PyG 3 Años'`, `'Punto Equilibrio'`, `'Escenarios'`,
`'Personal'`, `'Instrucciones'`) y **sin ningún input de ticket ni de
cubiertos en el P&L** en el fichero original — viven repartidos entre
`Escenarios` y `Punto Equilibrio`, con DOS calendarios distintos (`NUEVO-03`:
`Escenarios!B7/C7` = 310 días/año frente al calendario IMPLÍCITO de
`'PyG 3 Años'!B10` = 270.000 € = 50 cubiertos × 18 € × **300** días).
`grupo_a.py` reconstruye el P&L con el MISMO driver `cubiertos × ticket ×
días` que usan A-α y los otros tres A-β, y reparte el total entre DOS líneas
de venta (comida/bebida) por su peso (§2.3.2) — el patrón «2 líneas,
mix_en_supuestos=True» que ya usa `plan-negocio-cafeteria`, no el de 4 líneas
tecleadas: con más de 2 líneas el libro EN BLANCO deja `pct_bebida` en 0 %
(defecto de MOTOR anotado por el hermano de cafetería, no de este contenido).

Aquí NO hay lógica: sólo los datos propios de este plan —supuestos,
plantilla, partidas, umbrales y textos legales del checklist— con **la fuente
de cada cifra**. La mecánica es de `grupo_a.py`.

DE DÓNDE SALE CADA NÚMERO — tres orígenes, siempre declarados (mismo criterio
que `contenido_plan_negocio_bar_restaurante/a.py` y
`contenido_plan_negocio_cafeteria/a.py`):

  * «fichero v1.1» — estaba ya en `plan-financiero-tapas-bar.xlsx` o en
    `checklist-apertura-tapas-bar.xlsx` y se conserva (o se reconcilia entre
    las dos hojas que se contradecían).
  * «SPEC/R1» — lo fija `planes-v2-SPEC.md` o un hallazgo del R1 del
    representante que también mide esta familia (columna «ámbito» del mapa
    §8, FAMILIA).
  * «parametrizado» — no está en la SPEC ni en el fichero: celda VERDE
    editable con nota. Ninguna cifra del sector se teclea sin marcarla como
    parámetro (regla dura 6 del encargo T7).

RECONCILIACIÓN DEL CALENDARIO (NUEVO-03, medido el 2026-08-29)
------------------------------------------------------------------------
El fichero v1.1 trae DOS calendarios que no coinciden:

  * `Escenarios!B7:D7` declara 310-320 días/año.
  * `'PyG 3 Años'!B10` = 270.000 € es EXACTAMENTE 50 cubiertos × 18 € ×
    **300** días (comprobado: 50*18*300 = 270.000), el mismo dato que repite
    la portada del docx («facturación de 270.000 euros») y
    `'Punto Equilibrio'!B12` («Facturación mensual objetivo: 270.000 EUR /
    12 meses»). Es la cifra que el cliente ya conoce de memoria.

Se reconcilia a **300 días/año, un único calendario**, porque es el que hace
CIERTA la cifra más repetida del paquete (portada del docx, punto de
equilibrio y el propio total del P&L) sin inventar ningún dato nuevo: sólo
elige, de los dos que ya estaban, el que no contradice al resto del fichero.

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01, medido en el censo de
familia del 2026-08-29)
------------------------------------------------------------------------
El defecto que hunde los cinco planes de línea A es el mismo en los cinco: el
P&L imputa un coste de personal que NO es el de su propia hoja `Personal`.
Medido en `plan-financiero-tapas-bar.xlsx` v1.1: `'PyG 3 Años'!B23`
(«Salarios brutos incl. SS 33,4 %») = **96.000 €** mientras `Personal!E12`
(«TOTAL PERSONAL», columna «COSTE/AÑO») suma **209.174 €** — una diferencia de
**113.174 €**, la segunda peor de los cinco hermanos (censo de familia,
`planes-v2-SPEC.md` línea del censo: «tapas-bar 96.000 frente a 209.174
(−113.174)»). Con la cifra real de personal, el coste laboral es el **77,5 %**
de las ventas (270.000 €), muy por encima del techo 32-38 % que publica
`Instrucciones!B9` del mismo libro. El plan es inviable con sus propios datos,
igual que sus cuatro hermanos — y RT-03 (`planes-v2-correccion.json`) mide el
mismo síntoma en el `--dry-run` de partida: «semáforo de personal 74,7 %»
antes de que este módulo exista.

Lo que se ha hecho, y por qué se puede defender ante un banco:

1. **La plantilla estaba sobredimensionada para lo que paga el negocio.** El
   fichero v1.1 tenía 7 puestos a jornada prácticamente completa (incluido un
   «Gerente / Propietario» a 2.400 €/mes) sumando 209.174 €/año sobre una
   facturación de 270.000 €. Se redimensiona a **7 puestos por horas de
   servicio**, con el propietario trabajando en sala/barra (no como gerente
   puro) y el resto del equipo escalado por franja horaria: turno fuerte de
   tarde-noche (afterwork + cena), tarde floja, y refuerzo de fin de semana,
   que es el propio patrón que describe `Instrucciones!B15`
   («Ocupación media semana: 50-65 %») y `B16` («Ocupación fin de semana:
   80-95 %», con el propio docx citando el afterwork como «entre el 25 y 30
   por ciento» de la facturación — párrafo 58).
2. **Cubiertos, ticket y días se mantienen en los valores que el propio
   fichero ya declaraba como objetivo** (50 cubiertos/día, 18 € SIN IVA,
   300 días/año): no hace falta inflar ingresos para cuadrar el plan, con
   sólo redimensionar la plantilla el caso base pasa su propio semáforo.
3. **El ticket pasa a declararse SIN IVA** (TEC-11, DOM-30, igual que en el
   representante y en cafetería): 18 € SIN IVA es justo el valor que ya
   multiplicaba `50 × 18 × 300` para dar los 270.000 € que publica el
   fichero, así que no hay ningún salto de cifra, sólo se declara qué es lo
   que esa cifra ya era.
4. **Aparecen los costes fijos que el checklist obliga a contratar y que el
   plan no tenía** (TEC-18, igual que en los otros cuatro hermanos): gestión
   de residuos (crítico aquí: plancha y freidora generan aceite usado y grasa
   de forma continua, así que el volumen es MAYOR que en una cafetería), DDD,
   derechos de autor por música ambiental (distinto de la licencia municipal
   de música que el checklist YA tenía en `F2!B10`) y PRL. Todos en celda
   verde con nota de «pide presupuesto en tu zona».

Resultado del caso base (verificado con `data_only` tras `inject_cache.py`,
ver informe de la tanda): coste de personal ~33 % (techo elegido 36 % dentro
del rango 32-38 % de `Instrucciones!B9`), alquiler ~11,1 % (techo 12 % —
`Instrucciones!B10`), coste de mercancía ~27,8 % (dentro de 22-32 % según la
línea — `Instrucciones!B6-B8`, y coincide con el 28,1 % que el propio fichero
v1.1 ya declaraba en `'PyG 3 Años'!E17`), margen bruto ~69 % (suelo 68 % —
`Instrucciones!B17`) y resultado neto positivo. **El plan no se suspende a sí
mismo.**
"""

CONCEPTO = 'Tapas Bar / Gastrobar'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato = se queda el que trae `grupo_a`.
# pct_comida/pct_bebida NO se declaran aquí: con dos líneas de venta
# comida/bebida (`LINEAS_INGRESO`, abajo) `grupo_a.supuestos_calculadas()`
# las escribe SOLAS desde el peso de esas líneas (RD-23/RC-06/RT-13) — es el
# mismo patrón que ya usa el hermano de cafetería, no el de bar-restaurante
# (que también las deja fuera, pero por tener UNA sola línea).
# ==========================================================================
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 50, None,
        'Clientes servidos al día de media del año, tapeo de barra y '
        'raciones de mesa incluidos. Es el «Clientes/día objetivo (Año 1)» '
        'que ya declaraba el fichero v1.1',
        "fichero v1.1 ('Punto Equilibrio'!B11)"),
    'ticket_medio': (
        None, None, 18.00, None,
        'SIN IVA. Es el mismo 18 € que el fichero v1.1 ya usaba para derivar '
        'los 270.000 € de ingresos (50 × 18 × 300): declarar que es SIN IVA '
        'no cambia ningún número, sólo aclara qué era. Dentro del rango '
        '15-22 € «Ticket medio tapas bar» de Instrucciones!B11',
        "fichero v1.1 ('Punto Equilibrio'!B9, TEC-11/DOM-30)"),
    'dias_apertura': (
        None, None, 300, None,
        'El MISMO dato lo usan el P&L, el punto de equilibrio y los '
        'escenarios: el fichero v1.1 tenía DOS calendarios distintos '
        "(Escenarios!B7:D7: 310-320 días/año; 'PyG 3 Años'!B10 = 270.000 € "
        'está calculado con 300 días). Se elige 300 porque es el que hace '
        'CIERTA la cifra que repiten la portada del docx y el propio punto '
        'de equilibrio (270.000 €), no un dato nuevo',
        "fichero v1.1 (implícito en 'PyG 3 Años'!B10) — fija NUEVO-03"),
    'crec_a2': (
        None, None, 0.15,
        None, 'El fichero v1.1 proyectaba 320.000 € en el año 2 sobre '
        '270.000 € (+18,5 %): se redondea a la baja para no depender de la '
        'consolidación de la clientela afterwork en el primer año',
        'fichero v1.1 (redondeado a la baja, conservador)'),
    'crec_a3': (
        None, None, 0.10, None,
        'El fichero v1.1 proyectaba 370.000 € sobre 320.000 € (+15,6 %): '
        'igual, redondeado a la baja',
        'fichero v1.1 (redondeado a la baja, conservador)'),
    'coste_comida': (
        None, None, 0.30, None,
        'Food cost de tapas y raciones: dentro del 28-32 % que declara '
        'Instrucciones!B6 de este mismo libro. Coincide con el 43.500/'
        '145.000 = 30 % que ya tenía la v1.1',
        "fichero v1.1 ('PyG 3 Años'!B13/B6, Instrucciones!B6)"),
    'coste_bebida': (
        None, None, 0.25, None,
        'Coste de cerveza, vino, vermut y cócteles sobre sus propias '
        'ventas: media ponderada entre el 22-28 % de cerveza/vino '
        '(Instrucciones!B7) y el 18-25 % de cócteles (Instrucciones!B8). '
        'Coincide con (23.750+6.250)/(95.000+25.000) = 25 % de la v1.1',
        'fichero v1.1 (Instrucciones!B7 y B8)'),
    'pct_consumibles': (
        None, None, 0.01, None,
        'Vajilla desechable de take-away, servilletas y papel de barra',
        "parametrizado (v1.1: 'Packaging y desechables' 2.500 €/270.000 = "
        '0,93 %, redondeado)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: el checklist de este plan lo marca como tarea '
        'del mes 2-3 («Evaluar delivery si el margen lo permite»), no del '
        'día 1. Súbelo al peso real del canal cuando lo actives',
        'TEC-23/DOM-34 (mismo criterio que el representante)'),
    'comision_delivery': (
        None, None, 0.30, None,
        'El propio checklist v1.1 ya cita el rango: «Solo si margen lo '
        'permite (comisiones 25-35%)» — se toma el punto medio',
        "fichero v1.1 (checklist 'F6 - 90 Dias'!E12)"),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado; un tapas bar con barra '
        'prominente cobra en tarjeta la mayoría de las consumiciones',
        'parametrizado (el plan v1.1 no lo contemplaba)'),
    'alquiler_mes': (
        None, None, 2500, None,
        'Local de tapas bar/gastrobar de 60-80 m² con barra prominente + '
        'terraza. 11,1 % de las ventas del caso base, dentro del techo de '
        '12 % que fija Instrucciones!B10 de este mismo libro',
        "fichero v1.1 ('PyG 3 Años'!B22 = 30.000 €/año ÷ 12)"),
    'fianza_meses': (None, None, 3, None,
                     'Tres meses de renta, como en el contrato tipo de local '
                     'de negocio', 'parametrizado (v1.1 no lo declaraba '
                     'como fila propia)'),
    'suministros_mes': (
        None, None, 800, None,
        'Luz, agua y gas de cocina con plancha, freidora y horno + barra de '
        'grifos de cerveza (enfriador): pide el histórico del local antes '
        'de firmar',
        "fichero v1.1 ('PyG 3 Años'!B24 = 9.600 €/año ÷ 12)"),
    'seguros_ano': (None, None, 2400, None,
                    'Responsabilidad civil (mínimo 300.000 € — checklist '
                    "F2!E11) + multirriesgo del local",
                    "fichero v1.1 ('PyG 3 Años'!B25)"),
    'pct_varios': (
        None, None, 0.01, None,
        'Colchón de gasto corriente no presupuestado. Es un coste VARIABLE '
        '(sube y baja con la facturación, no puede vivir en los fijos: '
        'RT-04/RT-05), sustituye a la fila fija que traía la v1.1',
        "fichero v1.1 ('PyG 3 Años'!B31 = 2.500 €/270.000 = 0,93 %, "
        'redondeado)'),
    'recursos_propios': (
        None, None, 45000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja de este plan',
        'parametrizado'),
    'prestamo': (
        None, None, 140000, None,
        'Principal solicitado. La hoja de Financiación comprueba que origen '
        'y usos cuadran con la necesidad de caja calculada en la hoja 1',
        'parametrizado (recursos propios + préstamo = 185.000 €; ajustado '
        'de un primer intento de 150.000 € porque la hoja de Financiación '
        'marcaba un déficit de 34.412,45 € frente a la necesidad de caja '
        'real del caso base — mismo gotcha que el hermano de cafetería. '
        'Muy por encima de los 115.500 € que sumaba la v1.1 porque el fondo '
        'de maniobra real es mayor que el que dotaba el fichero original '
        '— NUEVO-01, la IVA soportado sobre la inversión y los imprevistos '
        'de obra por fórmula suman a la necesidad de caja)'),
    'tipo_prestamo': (None, None, 0.06, None,
                      'Tipo nominal anual; pide oferta a dos entidades y a '
                      'una línea ICO antes de fijarlo', 'parametrizado'),
    'plazo_prestamo': (None, None, 7, None, 'Años totales, carencia incluida',
                       'parametrizado'),
    'carencia_prestamo': (None, None, 1, None,
                          'Primer año sólo intereses, que es cuando la caja '
                          'está más tensa (obra + primeras semanas de '
                          'rodaje)', 'parametrizado'),
    'meses_fondo': (
        None, None, 3, None,
        'Mínimo que exige este mismo libro (Instrucciones): un colchón por '
        'debajo de 3 meses no cubre un bache de temporada baja',
        'SPEC §2.2 / TEC-07 (v1.1 dotaba 12.000 €, que eran 0,93 meses de '
        'sus propios costes fijos de entonces: NUEVO-01, la segunda peor '
        'proporción de los cinco hermanos)'),
    'vida_obra': (None, None, 10, None,
                  'Obra, instalaciones, extracción y decoración de un tapas '
                  'bar con cocina clasificada. Coincide con los «10 años» '
                  'que ya citaba la v1.1. Coeficientes de la tabla del art. '
                  '12.1 LIS: confírmalo con tu asesor',
                  "fichero v1.1 ('PyG 3 Años'!A35 «Amortización (10 años)»)"),
    'vida_maquinaria': (
        None, None, 8, None,
        'Plancha, freidora, horno, cámaras, grifos de cerveza y mobiliario '
        'de barra. Coeficiente lineal máximo del art. 12.1 LIS: 12 % '
        'maquinaria, 10 % mobiliario — por debajo de 8-10 años el exceso no '
        'es deducible. Confírmalo con tu asesor',
        'parametrizado (v1.1: 10 años planos para todo el inmovilizado, sin '
        'distinguir obra de maquinaria — NUEVO-02, mismo criterio que '
        'cafetería y panadería)'),
    'pct_bebida_alc': (
        None, None, 0.85, None,
        'Bebida ALCOHÓLICA sobre el total de bebida: la línea de bebida de '
        'este plan es cerveza, vino, vermut y cócteles/destilados — un '
        'tapas bar con «barra prominente» (docx, concepto) vende sobre todo '
        'alcohol. El resto —refrescos, agua, algún café— va al IVA reducido '
        'de hostelería',
        'parametrizado (composición de la línea de bebida de este plan: '
        "'PyG 3 Años'!A7 «cerveza, vino, vermut» + A8 «cocteles y "
        'destilados»)'),
    'aforo': (
        None, None, 45, None,
        'Plazas interiores (40-50, docx párrafo 89) + terraza (10-12 mesas, '
        "'Inversión Inicial'!C17). De aquí sale la rotación implícita: "
        'cubiertos/día ÷ aforo. Cuéntalo sobre el plano de tu local, no lo '
        'copies',
        'fichero v1.1 (docx: «capacidad para cuarenta a cincuenta plazas '
        'interiores más terraza»)'),
    'salario_convenio': (
        None, None, 0, None,
        'El convenio PROVINCIAL de hostelería, no el SMI, es el suelo real '
        'del sector: cópialo de la tabla salarial de tu provincia. Con 0 el '
        'semáforo compara sólo contra el SMI',
        'SPEC §2.6/DOM-24 (mismo criterio que el representante y '
        'cafetería)'),
}

# ==========================================================================
# §2.3.2 — líneas de venta. DOS líneas (comida/bebida), el patrón
# `mix_en_supuestos` que ya usa cafetería: con más de dos, `grupo_a.pyg()`
# deja `pct_bebida` en 0 % con el libro en blanco (defecto de MOTOR, no de
# este contenido — anotado por el hermano de cafetería en su propio módulo).
# El desglose tapas/raciones · cerveza/vino/vermut · cócteles que traía v1.1
# se conserva como NOTA de cada línea (transparencia), aunque el cálculo
# agregue en dos.
# (rótulo, peso, grupo 'comida'|'bebida', nota, fuente)
# ==========================================================================
LINEAS_INGRESO = (
    ('Ventas de comida (tapas, raciones y otros)', 0.5556, 'comida',
     'Tapas y raciones de barra y mesa, más eventos, catering mini y '
     'take-away (la línea "Otros" de la v1.1)',
     'fichero v1.1: suma de «Ventas tapas y raciones» + «Otros» '
     '((145.000+5.000)/270.000 = 55,6 %)'),
    ('Ventas de bebida (cerveza, vino, vermut y cócteles)', 0.4444, 'bebida',
     'Grifos de cerveza, vino y vermut de barra, más cócteles y destilados '
     '(coste más alto por elaboración, Instrucciones!B8)',
     'fichero v1.1: suma de «Ventas bebidas» + «Ventas cocteles y '
     'destilados» ((95.000+25.000)/270.000 = 44,4 %)'),
)

# ==========================================================================
# §2.6 — plantilla redimensionada por horas de servicio (§7-bis.17)
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
# ==========================================================================
PLANTILLA = (
    ('Propietario/a y encargado/a de sala', 1, 1150,
     'Gestiona compras, caja, proveedores y RRSS, y cubre barra/sala en el '
     'turno fuerte de tarde-noche',
     'recalibrado §7-bis.17 (v1.1: «Gerente / Propietario» 2.400 €, coste/'
     'año 44.828 €, jornada completa sin ninguna referencia de horas)',
     1.0),
    ('Jefe de cocina', 1, 1350,
     'Diseña la carta de tapas, coordina la línea de cocina y controla el '
     'food cost semanal (checklist F6!B6)',
     'recalibrado (v1.1: «Jefe de cocina / Cocinero principal» 2.000 €)',
     1.0),
    ('Camarero/a de barra (turno fuerte)', 1, 1050,
     'Tiraje de cerveza, vermut y cócteles: el afterwork representa el '
     '25-30 % de la facturación de un gastrobar (docx párrafo 58)',
     'recalibrado (v1.1: «Camarero/a principal (barra)» 1.550 €)', 1.0),
    ('Camarero/a de sala y terraza', 1, 550,
     'Cubre el servicio de mesa y terraza, más floja fuera del turno '
     'afterwork (Instrucciones!B15: «ocupación media semana 50-65 %»)',
     'recalibrado (v1.1: «Camarero/a sala» 1.450 € a jornada completa)',
     0.45),
    ('Ayudante de cocina', 1, 400,
     'Mise en place, limpieza y apoyo en plancha/freidora en el turno '
     'fuerte',
     'recalibrado (v1.1: «Ayudante cocina» 1.400 € a jornada completa)',
     0.28),
    ('Extra de fin de semana (barra y sala)', 1, 200,
     'Refuerzo de los picos de viernes-sábado, cuando la ocupación sube al '
     '80-95 % (Instrucciones!B16)',
     'recalibrado (v1.1: «Extra fines de semana» 800 € a 20 h/semana)',
     0.15),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que el convenio
    # provincial sí impone: siete puestos con 30 días naturales de
    # vacaciones (art. 38 ET) son días de servicio que alguien tiene que
    # cubrir.
    ('Suplencias de vacaciones y descansos', 1, 90,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso '
     'semanal del equipo',
     'parametrizado (RC-19, mismo criterio que el representante y '
     'cafetería)', 0.08),
)

# ==========================================================================
# §2.2 — partidas de la inversión
# ==========================================================================
#: Reglas por rótulo NORMALIZADO (después de que `_limpiar_rotulo` quite el
#: paréntesis con el parámetro, §7-bis.11): `('suprimir', motivo)` o
#: `(importe, nota)`.
#: Terraza (A17) y stock inicial (A23) YA existen como partida propia en
#: `Inversión Inicial` del fichero v1.1 (a diferencia del representante, que
#: sólo los tenía en el Word): DOM-19 «no aplica» aquí, igual que en
#: cafetería.
INVERSION = {
    'imprevistos': (
        'suprimir',
        'RD-02 (mismo patrón que el representante y cafetería): el 8 % '
        'tecleado a mano se sustituye por la fila «Imprevistos de obra y '
        'acondicionamiento», que `grupo_a` calcula por fórmula sobre las '
        'partidas de obra de este mismo bloque (§2.2)'),
    # §1.7 — «gestion» sin tilde NO está cubierto por `motor.TILDES`: el
    # diccionario lleva «gestoria»→«gestoría» pero no la palabra suelta
    # «gestión» (no es -ción/-sión: termina en «-tion», y la regla
    # generativa RX_CION sólo cubre «-cion»/«-sion»). Medido el 2026-08-29 en
    # el gate de esta misma tanda; no está en el R1 del representante, que no
    # tiene esta partida con esa grafía.
    'tpv + software gestion + comandero': (
        'suprimir',
        '§1.7: «gestion» sin tilde no lo cubre el diccionario del motor '
        '(no es -ción/-sión); se re-da de alta como «TPV + software '
        'gestión + comandero» en INVERSION_EXTRA, mismo importe (2.000 €) y '
        'nota'),
    # La NOTA (no el rótulo) de «Rotulacion + imagen exterior» decía «Rotulo
    # + pizarra tapas + vinilo», con «Rotulo» sin tilde: el rótulo de la fila
    # SÍ lo corrige el motor (RX_CION: rotulacion→rotulación), la nota no,
    # porque es una palabra distinta («rótulo», no «rotulación»). Se usa la
    # vía del importe (idéntico, 2.000 €) para reescribir sólo la nota.
    'rotulacion + imagen exterior': (
        2000,
        'Rótulo, pizarra de tapas y vinilo de escaparate'),
    # §1.7 — la NOTA de «Stock inicial (producto, vinos, cervezas)» decía
    # «Genero perecedero, bodega vinos, barrileria cerveza», con «Genero» y
    # «barrileria» sin tilde. El rótulo no lleva parámetro entre paréntesis
    # (RX_PARENTESIS_NUM sólo quita paréntesis con número/%/años), así que
    # no pasa por `_limpiar_rotulo`, y la nota no la toca ningún gancho del
    # motor porque la partida se PRESERVA tal cual del fichero original. Se
    # usa la vía del importe (idéntico, 4.000 €) para reescribir sólo la
    # nota. Medido el 2026-08-29 en el gate de esta misma tanda.
    'stock inicial (producto, vinos, cervezas)': (
        4000,
        'Género perecedero, bodega de vinos y barrilería de cerveza'),
    # §1.7 — misma trampa: la nota de «Grifos cerveza + instalacion» decía
    # «4-6 grifos, enfriador, barrileria, CO2», con «barrileria» sin tilde,
    # y «barrileria» no está en `motor.TILDES` como palabra suelta (sólo
    # aparece dentro de compuestos ya listados). Medido el 2026-08-29.
    'grifos cerveza + instalacion': (
        3000,
        '4-6 grifos, enfriador, barrilería, CO2'),
}

#: Las dos únicas partidas nuevas son el re-alta de §1.7 de arriba (mismo
#: importe y bloque, sólo corrige la ortografía del rótulo).
INVERSION_EXTRA = (
    (None, 'TPV + software gestión + comandero', 2000,
     'TPV táctil de barra + comandero inalámbrico + software de gestión',
     'fichero v1.1 (rótulo corregido, §1.7 — antes «…gestion…»)'),
)

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (TEC-18, FAMILIA(5): el mismo defecto que en los otros cuatro hermanos)
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Gestión de residuos (orgánico, cartón y aceite usado)', 900,
     'Gestor autorizado; el checklist lo pide antes de abrir. Con plancha y '
     'freidora en marcha, un tapas bar genera MÁS aceite usado que una '
     'cafetería — pide presupuesto en tu zona',
     'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 700,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC que el '
     "checklist ya exige ('F4 - Personal'!B14: «Formación alérgenos + "
     'APPCC»)', 'parametrizado (TEC-18)'),
    ('Derechos de autor por música ambiental (SGAE/AGEDI-AIE)', 700,
     'Es una licencia DISTINTA de la municipal de música ambiente que el '
     "checklist ya tiene ('F2 - Local'!B10): esa es administrativa, ésta es "
     'de propiedad intelectual. Se pagan las dos si hay hilo musical o DJ',
     'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 500,
     'El plan de prevención es obligatorio; el proveedor externo, no (art. '
     "30.5 de la Ley 31/1995) — el checklist 'F4 - Personal' lo corrige",
     'parametrizado (DOM-26)'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Las CINCO ratios que exige el gate de la tanda (dry-run: «caso base que
# pasa sus 5 ratios»). Los rótulos los pone `grupo_a`; aquí van el valor y el
# comentario, con la cita literal de `Instrucciones` de ESTE producto.
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.68,
     'Suelo del propio libro: «Instrucciones!B17 — Margen bruto objetivo: '
     '>68%»'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.30,
     'Blend de los tres food cost que publica este producto (comida '
     '28-32 %, cerveza/vino 22-28 %, cócteles 18-25 % — Instrucciones!'
     'B6-B8): 30 % coincide con el 28,1 % que la propia v1.1 ya declaraba '
     "en 'PyG 3 Años'!E17, con margen"),
    ('r_personal', 'Coste de personal / Ventas', 0.36,
     'Dentro del rango 32-38 % que publica Instrucciones!B9 de este mismo '
     'libro: cerca del extremo estricto, pero dejando margen realista para '
     'retribuir un jefe de cocina cualificado a jornada completa'),
    ('r_alquiler', 'Alquiler / Ventas', 0.12,
     'Techo del propio libro: «Instrucciones!B10 — Alquiler / ventas: '
     '8-12%, no superar 12% para ser viable»'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Derivado del suelo de EBITDA que declara este producto para el año 2 '
     '(«Instrucciones!B18 — EBITDA objetivo: 15-22%»): descontando '
     'amortización, intereses e Impuesto de Sociedades, un EBITDA en la '
     'franja baja del rango deja un resultado neto en torno al 5 % ya en el '
     'año 1'),
)

# ==========================================================================
# §2.5 — escenarios extremos (cubiertos/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# El fichero v1.1 usaba días DISTINTOS por columna (310/310/320): se unifica
# a los 300 de Supuestos (NUEVO-03), conservando cubiertos y ticket.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (35, 16.00, 300),
    'optimista': (65, 21.00, 300),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma 1)
# ==========================================================================
#: Estacionalidad de un tapas bar/gastrobar urbano con terraza y afterwork:
#: verano fuerte (terraza + turismo, docx párrafo 56: «España recibió más de
#: 85 millones de turistas»), diciembre fuerte por cenas y vermuts de
#: Navidad, enero flojo por la cuesta de enero. PARÁMETRO editable: si el
#: local no tiene terraza, el pico de verano se modera.
ESTACIONALIDAD = (0.065, 0.070, 0.080, 0.082, 0.088, 0.095,
                  0.100, 0.095, 0.085, 0.082, 0.078, 0.100)

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    'uso': [
        '7. La hoja «Tesorería 12 meses» responde la pregunta que decide una '
        'operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '8. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota) — se conservan las referencias del
    # sector que ya traía este fichero (mismo criterio que el representante
    # y cafetería: no se borran, se citan con su fuente).
    'referencias': [
        ('Food cost comida (tapas/raciones)', '28-32 %', 'Fichero v1.1',
         'Las tapas permiten aprovechar recortes y género de menor coste'),
        ('Food cost bebidas (cerveza/vino)', '22-28 %', 'Fichero v1.1',
         'La cerveza de grifo tiene mejor margen que la de botella'),
        ('Food cost cócteles', '18-25 %', 'Fichero v1.1',
         'Margen alto si se estandarizan recetas'),
        ('Coste de personal sobre ventas', '32-38 %', 'Fichero v1.1',
         'Incluye los extras de fin de semana en el cálculo'),
        ('Alquiler sobre ventas', '8-12 %', 'Fichero v1.1',
         'No superar el 12 % para ser viable'),
        ('Ticket medio tapas bar', '15-22 €', 'Fichero v1.1',
         '2-3 tapas + 2 bebidas por persona'),
        ('Ticket medio gastrobar', '22-30 €', 'Fichero v1.1',
         'Raciones + maridaje de vino o vermut'),
        ('Consumiciones de barra sobre ventas', '35-45 %', 'Fichero v1.1',
         'La barra es clave en un tapas bar, con alto margen'),
        ('Ocupación media semana', '50-65 %', 'Fichero v1.1',
         'El afterwork de jueves-viernes es muy fuerte'),
        ('Ocupación fin de semana', '80-95 %', 'Fichero v1.1',
         'Vermut de sábado + cenas de fin de semana'),
        ('Margen bruto objetivo', '> 68 %', 'Fichero v1.1',
         'Un tapas bar tiene margen superior al de un restaurante casual'),
        ('EBITDA objetivo (año 2)', '15-22 %', 'Fichero v1.1',
         'Más rentable que un restaurante por el ticket rápido de barra'),
        ('Retorno de la inversión', '18-30 meses', 'Fichero v1.1',
         'Más rápido que un restaurante por el menor desperdicio'),
        ('Merma media', '3-5 %', 'Fichero v1.1',
         'Las tapas permiten aprovechar recortes: menor merma que en un '
         'restaurante de carta'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería',
         'DOM-24 / checklist F4',
         'No existe una tabla salarial estatal única: copia la tabla de tu '
         'provincia en la celda de Supuestos'),
    ],
}

# ==========================================================================
# §2.10 — checklist de apertura: legal vigente y sin inventos (molde C2, seis
# hojas `F1..F6`). El primer campo de cada alta es la REGEX contra el título
# de la hoja que decide dónde se añade (`grupo_a.checklist`, `destino = […]
# re.search(a[0], ws.title...)` cuando el libro tiene más de dos hojas).
# ==========================================================================
CHECKLIST = {
    # ⚠️ `grupo_a.checklist()` corre DESPUÉS del §1 transversal del motor
    # (tildes + `EUR`→`€`), así que los patrones de abajo NO anclan con
    # `^…$` de forma rígida contra el texto CRUDO de v1.1: buscan la
    # SUBCADENA estable —el número, la cifra en euros o una palabra que no
    # cambia— con acentos opcionales, mismo criterio que el hermano de
    # cafetería (que perdió 3 reemplazos en su primera pasada por anclar
    # contra el texto de ANTES del §1 transversal).
    'reemplazos': [
        # DOM-08 / COM-11 (FAMILIA) — el carnet de manipulador está
        # DEROGADO (RD 109/2010); la responsabilidad es de la EMPRESA.
        # Tapas-bar lo escribe SIN «de» entre «Carnet» y «manipulador»
        # (distinto del representante y de cafetería: «Carnet manipulador
        # alimentos», no «Carnet de manipulador de alimentos»).
        (r'^Carnet manipulador alimentos$',
         'Formación en higiene alimentaria de todo el equipo'),
        (r'^Todos$', 'Titular'),
        (r'^Obligatorio todo personal, curso online valido$',
         'El «carnet de manipulador» está derogado (RD 109/2010): la '
         'formación la acredita la EMPRESA y se documenta en el plan '
         'APPCC'),
        # DOM-09 (FAMILIA) — el registro sanitario que corresponde es el
        # AUTONÓMICO, no el RGSEAA estatal (RD 191/2011 art. 2.2).
        (r'^Registro sanitario RGSEAA$',
         'Inscripción en el Registro Sanitario de tu Comunidad Autónoma '
         '(declaración responsable de inicio de actividad alimentaria)'),
        (r'^Obligatorio por elaboraci[oó]n de alimentos$',
         'El Registro General Sanitario estatal NO aplica al minorista que '
         'sirve al consumidor final (art. 2.2 del RD 191/2011): el que te '
         'toca es el autonómico'),
        # DOM-25 (FAMILIA) — cuota de autónomo parametrizada, con nota de
        # año. Tapas-bar no lleva «primer año» en el texto (a diferencia del
        # representante): «Tarifa plana autonomos 80 EUR/mes» a secas.
        # Medido tras el §1 transversal: «autónomos» y «€» ya puestos por el
        # motor.
        (r'Tarifa plana aut[oó]nomos? 80\s*(EUR|€)/mes',
         'Cuota según la base mínima del tramo que te corresponda. '
         'Consulta el importe del ejercicio en curso y verifica con tu '
         'gestoría si te aplica la cuota reducida de inicio de actividad'),
        # DOM-26 (FAMILIA) — el PRL obligatorio es el PLAN, no el proveedor.
        (r'^SPA$', 'Titular o servicio ajeno'),
        (r'Servicio de Prevenci[oó]n Ajeno obligatorio',
         'El plan de prevención es obligatorio; el proveedor externo, no: '
         'con menos de 25 trabajadores y un solo centro el titular puede '
         'asumir la actividad preventiva (art. 30.5 de la Ley 31/1995 y '
         'art. 11 del RD 39/1997)'),
        # §1.7 — «musica» sin tilde en la licencia municipal: es la ÚNICA
        # celda de esta familia de errata que sobrevive al §1 transversal
        # porque «musica» no está en `motor.TILDES` (sólo cubre el
        # sustantivo dentro de compuestos ya listados, no esta fila suelta).
        # Medido el 2026-08-29 en el gate de esta misma tanda.
        (r'^Licencia de musica ambiente$',
         'Licencia de música ambiente'),
        # DOM-33 (REPRESENTANTE, extendido a esta hermana) — el epígrafe de
        # IAE, con opciones y la nota de que la elección la valida el
        # gestor. `673.2 (otros cafés y bares)` YA coincide con la
        # definición que fija esta SPEC (§2.10), pero un tapas bar con
        # cocina clasificada («Licencia de actividad clasificada»,
        # 'Inversión Inicial'!C7) puede caer también en el grupo de
        # restaurantes según el peso de la barra frente al servicio de
        # mesa: se da la misma horquilla que usa el representante.
        (r'Epigrafe IAE: 673\.2 \(otros caf[eé]s y bares\)',
         'Epígrafe IAE: 671.5 (restaurantes de un tenedor) o 673.2 (otros '
         'cafés y bares), según el peso de la barra frente al servicio de '
         'mesa — la elección la valida tu gestor: condiciona inspecciones '
         'y licencia'),
    ],
    'suprimir': [],
    'fases': {},
    # TEC-18 (FAMILIA) + RGPD: trámites que faltan y cuestan dinero o multa.
    # Repartidos por hoja (F1 Constitución, F2 Local, F3 Equipamiento,
    # F4 Personal, F5 Marketing, F6 primeros 90 días) — molde C2 (6 hojas),
    # igual que cafetería, distinto del monolítico C1 del representante.
    'altas': [
        ('F1', 'RGPD',
         'Registro de actividades de tratamiento de datos personales',
         'Titular', 'Antes de abrir',
         'Art. 30 del RGPD y art. 31 de la LOPDGDD: lo pide la AEPD en la '
         'primera inspección. Incluye clientes, personal y proveedores'),
        ('F1', 'Fiscal',
         'Adaptar el TPV y la facturación al sistema Veri*factu / factura '
         'electrónica', 'Gestor', 'Antes de abrir',
         'El RD 1007/2023 y su calendario escalonado obligan a que el '
         'software de facturación sea verificable. Consulta la fecha que te '
         'aplica antes de comprar el TPV + comandero que presupuesta la '
         'hoja de Inversión'),
        ('F2', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador',
         'Titular', '1 día',
         'El modelo y el texto del cartel los aprueba tu Comunidad '
         'Autónoma'),
        ('F2', 'Legal',
         'Contrato con gestor autorizado de residuos', 'Titular',
         '2 semanas',
         'Se comprueba en la inspección. Cartón, orgánico y el aceite '
         'usado de plancha y freidora, que no puede ir al desagüe'),
        ('F2', 'APPCC',
         'Contrato de desinsectación, desratización y desinfección (DDD)',
         'Titular', '1 semana',
         'Empresa inscrita en el ROESB; el certificado forma parte del plan '
         'APPCC'),
        ('F2', 'RGPD',
         'Cartel y contrato de videovigilancia con la empresa de '
         'seguridad', 'Titular', 'Con la obra',
         'Cartel homologado en zona visible, contrato de encargado de '
         'tratamiento y plazo máximo de conservación de 30 días'),
        ('F4', 'Laboral',
         'Registro horario diario de la jornada de todo el equipo',
         'Gestor', 'Desde el primer contrato',
         'Art. 34.9 del Estatuto de los Trabajadores; se conserva cuatro '
         'años'),
        ('F4', 'RGPD',
         'Informar al equipo del registro horario y del tratamiento de sus '
         'datos', 'Gestor', 'Desde el primer contrato',
         'La cláusula informativa se entrega con el contrato; el fichaje es '
         'un tratamiento de datos, no sólo una obligación laboral'),
        ('F5', 'Legal',
         'Licencia de derechos de autor por la música ambiental (SGAE/'
         'AGEDI-AIE)',
         'Titular', '2 semanas',
         'Distinta de la licencia municipal de música que ya tiene este '
         'checklist: ésta es de propiedad intelectual y se paga aunque el '
         'ayuntamiento ya haya autorizado el hilo musical o el DJ'),
        ('F5', 'RGPD',
         'Cláusula informativa y consentimiento en TheFork y en la lista de '
         'correo', 'Titular', 'Antes de abrir',
         'TheFork, WhatsApp y newsletter tratan datos: cada canal necesita '
         'su información previa'),
    ],
}

# ==========================================================================
# Registro de lo que cambia de valor respecto de la v1.1 (§1.3: «la
# diferencia entre el valor viejo y el nuevo queda anotada por fichero»)
# ==========================================================================
RECALIBRADO = (
    ('Coste de personal imputado al P&L', '96.000 €',
     'Sale de la hoja Personal, por fórmula',
     "TEC-01/DOM-01 (FAMILIA): el P&L usaba una cifra tecleada distinta de "
     "su propia hoja Personal (209.174 €), una diferencia de 113.174 € — la "
     "segunda peor de los cinco hermanos"),
    ('Plantilla', '7 puestos / 209.174 €',
     '7 puestos (tres a jornada parcial y suplencias) / ~93.000 €',
     '§7-bis.17: dimensionada por horas de servicio; con la plantilla '
     'anterior el coste laboral era el 77,5 % de las ventas'),
    ('Calendario', 'Escenarios: 310-320 días/año · PyG (implícito): 300 '
     'días/año (dos calendarios distintos)', '300 días/año, un único dato '
     'en Supuestos', 'NUEVO-03 (defecto propio de los cuatro hermanos '
     'A-β, no visto por el R1 del representante A-α)'),
    ('Ticket medio', '18 € (sin declarar IVA)', '18 € SIN IVA (mismo '
     'número)', 'TEC-11/DOM-30: se declara qué era el número, no se '
     'cambia el número'),
    ('Fondo de maniobra', '12.000 € etiquetados «3 meses»',
     '3 × costes fijos de caja mensuales, por fórmula',
     'TEC-07/DOM-12/NUEVO-01: los 12.000 € cubrían 0,93 meses de los '
     '12.925 €/mes de costes fijos de la v1.1'),
    ('Amortización', '11.550 €/año a 10 años planos sobre TODO el '
     'inmovilizado', 'Base amortizable real (sólo obra y maquinaria) / '
     'vida útil por fórmula, con obra (10 años) y maquinaria (8 años) '
     'separadas',
     'NUEVO-02: la base plana no distinguía obra de maquinaria'),
    ('Imprevistos de obra', '8.500 € (8 % tecleado a mano sobre el total)',
     'Por fórmula sobre las partidas de obra del bloque, con el '
     'porcentaje en Supuestos',
     '§7-bis.11: ningún número vive dentro de una fórmula ni de un rótulo'),
    ('Impuesto de Sociedades', '25 % en los tres años, sin compensar '
     'bases negativas', '15 % los dos primeros ejercicios con base '
     'positiva y compensación de bases negativas',
     'TEC-06/DOM-15 (FAMILIA): arts. 26 y 29.1 LIS'),
    ('Plan de financiación', 'inexistente (0 hojas)',
     'Hoja «Financiación»: usos y orígenes + cuadro de amortización '
     'francés',
     'TEC-08/DOM-10/COM-04 (FAMILIA 10/10): la landing lo promete en las '
     '10 líneas y ningún fichero lo tenía'),
    ('Tesorería mensual', 'inexistente (0 hojas)',
     'Hoja «Tesorería 12 meses»: cobros, pagos, IVA trimestral y saldo '
     'acumulado', 'DOM-14/DOM-17 (FAMILIA 10/10)'),
    ('Varios e imprevistos', '2.500 €/año fijo dentro de COSTES FIJOS',
     '1 % de las ventas, coste VARIABLE',
     'RT-04/RT-05: un coste que sube y baja con la facturación no puede '
     'vivir en los costes fijos (movía el punto de equilibrio de forma no '
     'lineal)'),
)
