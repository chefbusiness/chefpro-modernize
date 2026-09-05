#!/usr/bin/env python3
"""
Contenido de `plan-negocio-food-truck` para el grupo A (§2 de la SPEC, T7).

Molde **A-β** (mismo patrón que cafetería, panadería y tapas-bar, ya
construidos como hermanos de referencia de esta tanda): hojas SIN numerar
(`'Inversion Inicial'`, `'PyG 3 Anos'`, `'Punto Equilibrio'`, `'Escenarios'`,
`'Personal'`, `'Instrucciones'`) y **sin ningún input de ticket ni de
cubiertos en el P&L** en el fichero original (§2.12 del encargo: el driver
vive repartido entre `Escenarios` y `'Punto Equilibrio'`, con hasta TRES
calendarios que no coinciden entre sí — ver «RECONCILIACIÓN DEL CALENDARIO»
más abajo, el `NUEVO-03` propio de este hermano).

Aquí NO hay lógica: sólo los datos propios de este plan —supuestos,
plantilla, partidas, umbrales y textos legales del checklist— con **la fuente
de cada cifra**. La mecánica es de `grupo_a.py`.

DE DÓNDE SALE CADA NÚMERO — tres orígenes, siempre declarados (mismo criterio
que `contenido_plan_negocio_bar_restaurante/a.py`,
`contenido_plan_negocio_cafeteria/a.py`, `contenido_plan_negocio_panaderia/a.py`
y `contenido_plan_negocio_tapas_bar/a.py`):

  * «fichero v1.1» — estaba ya en `plan-financiero-food-truck.xlsx` o en
    `checklist-apertura-food-truck.xlsx` y se conserva (o se reconcilia entre
    hojas que se contradecían).
  * «SPEC/R1» — lo fija `planes-v2-SPEC.md` o un hallazgo del R1 del
    representante que también mide esta familia (columna «ámbito» del mapa
    §8, FAMILIA).
  * «parametrizado» — no está en la SPEC ni en el fichero: celda VERDE
    editable con nota. Ninguna cifra del sector se teclea sin marcarla como
    parámetro (regla dura 6 del encargo T7).

MOLDE PROPIO — el food truck NO es un local con alquiler
------------------------------------------------------------------------
Los otros cuatro hermanos de línea A operan desde un local fijo; el food
truck no. `grupo_a.SUPUESTOS_BASE` reserva una celda `alquiler_mes`
(«Alquiler mensual del local») que este negocio no tiene en ese sentido
literal. **No se deja en cero** (eso falsearía el ratio «Alquiler / Ventas»
y dejaría fuera un coste real): se reutiliza la celda para el coste mensual
de **aparcamiento/base fija del vehículo fuera de servicio** —un food truck
necesita dónde guardarse y prepararse cada noche, sea nave, parking cubierto
o plaza reservada—, distinto del «Generador (combustible/alquiler)» que ya
tenía el fichero v1.1 (ese va a `suministros_mes`, ver más abajo). Se
documenta expresamente en la nota de la celda para que no se lea como una
renta de local que no existe. Mismo criterio con `aforo` (§SUPUESTOS_BASE):
no hay «plazas sentadas», así que se reutiliza como capacidad informal de
cola + mesas plegables alrededor del vehículo, con nota.

RECONCILIACIÓN DEL CALENDARIO (NUEVO-03 propio de este hermano, medido el
2026-08-29)
------------------------------------------------------------------------
El fichero v1.1 trae TRES lecturas del mismo negocio que no coinciden:

  * `'Punto Equilibrio'!B11` («Clientes/día objetivo Año 1») = 45, con
    `C8` = «Asumiendo 25 días de servicio/mes» (= 300 días/año) y
    `B9` (ticket) = 12 €. 45 × 12 × 300 = **162.000 €**.
  * `Escenarios!C5:C8` (columna REALISTA) = 5 servicios/semana × 45
    clientes/servicio × 12 € × 48 semanas/año. 5 × 45 × 12 × 48 =
    **129.600 €**, que es justo lo que `Escenarios!C9` ya publica.
  * `'PyG 3 Anos'!B9` (TOTAL INGRESOS, año 1) = **135.000 €** — la cifra que
    también repite la portada del docx original («facturación de
    aproximadamente 135.000 euros», «300 días de operación»).

Ninguna de las tres reproduce a las otras dos: la de Punto de Equilibrio se
queda un 20 % por encima de la del propio P&L: la de Escenarios, un 4 % por
debajo. Se reconcilia con el mismo criterio que ya usaron cafetería y
tapas-bar: se eligen, DE ENTRE LOS DATOS QUE YA ESTABAN, los que hacen CIERTA
la cifra más repetida y más visible (el total del P&L, que es también la que
imprime la portada del documento), sin inventar ningún número nuevo:

    cubiertos_dia = 45   (el mismo dato que ya declaraba 'Punto Equilibrio'!B11
                           y que 'Escenarios'!C6 usa en su columna realista)
    ticket_medio  = 12 € (el mismo dato que ya usan 'Punto Equilibrio'!B9 y
                           'Escenarios'!C7 en su columna realista)
    dias_apertura = 250  (45 × 12 × 250 = 135.000 € EXACTOS — reproduce al
                           céntimo el total que ya publica 'PyG 3 Anos'!B9 y
                           que repite la portada del docx. 250 días equivale
                           a 5 días de servicio/semana × 50 semanas activas,
                           dentro del rango «4-6 días operativos/semana» que
                           ya declara Instrucciones!B13 de este mismo libro)

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01, medido en el censo de
familia del 2026-08-29)
------------------------------------------------------------------------
El defecto que hunde los cinco planes de línea A es el mismo en los cinco: el
P&L imputa un coste de personal que NO es el de su propia hoja `Personal`.
Medido en `plan-financiero-food-truck.xlsx` v1.1: `'PyG 3 Anos'!B21`
(«Salarios (incl. SS 33.4%)») = **42.000 €** mientras `Personal!E8`
(«TOTAL PERSONAL», columna «COSTE/AÑO») suma **76.566 €** — una diferencia de
**34.566 €**, la MENOR de los cinco hermanos en términos absolutos pero
igual de inviable en proporción (censo de familia, `planes-v2-SPEC.md`:
«food-truck 42.000 frente a 76.566 (−34.566)»). Con la cifra real de
personal, el coste laboral es el **56,7 %** de las ventas (135.000 €), muy
por encima del techo 25-32 % que publica `Instrucciones!B7` del mismo libro
(«Coste personal / ventas: 25-32%. Menos personal que restaurante: 2-3
personas»). El plan es inviable con sus propios datos, igual que sus cuatro
hermanos.

Lo que se ha hecho, y por qué se puede defender ante un banco:

1. **La plantilla de tres puestos ya declarados se REDIMENSIONA por horas de
   servicio**, no se elimina ningún puesto. El fichero v1.1 tenía al
   propietario y al ayudante a jornada PRÁCTICAMENTE COMPLETA (2.000 € y
   1.500 € brutos/mes) para un negocio que sólo opera **250 días/año en
   servicios de 4-6 horas** (Instrucciones!B14: «Servicios por día: 1-2»,
   docx: «10-12 horas de jornada efectiva» INCLUYENDO desplazamiento, montaje
   y desmontaje, no sólo el servicio al cliente). Se escala cada puesto por
   la fracción de jornada que de verdad exige ese calendario, con el
   propietario cubriendo el turno fuerte y el ayudante y el refuerzo de
   eventos a tiempo parcial — el mismo patrón de «jornada» que ya usan
   tapas-bar, cafetería y panadería.
2. **Cubiertos, ticket y días se mantienen en los valores que el propio
   fichero ya declaraba** (45 clientes/día, 12 € SIN IVA, ver reconciliación
   de arriba): no hace falta inflar ingresos para cuadrar el plan, con sólo
   redimensionar la plantilla el caso base pasa su propio semáforo.
3. **El ticket pasa a declararse SIN IVA** (TEC-11, DOM-30, igual que en el
   representante y en los otros tres A-β): 12 € SIN IVA es justo el valor que
   ya usaban 'Punto Equilibrio'!B9 y la columna realista de `Escenarios`, así
   que no hay ningún salto de cifra, sólo se declara qué es lo que esa cifra
   ya era.
4. **Se elimina un doble conteo propio de este hermano** que ningún R1 podía
   ver: `'Inversion Inicial'!B14` («Seguro vehiculo + RC actividad», 2.500 €)
   es la MISMA prima anual que `'PyG 3 Anos'!B23` («Seguro vehiculo + RC»,
   2.500 €/año) ya carga como coste fijo recurrente del año 1 — el mismo
   síntoma que TEC-12 mide en la línea B, aquí en la línea A. Se retira de la
   Inversión (mismo criterio que TEC-12: las partidas RECURRENTES que el P&L
   ya carga en el año 1 no se cuentan también como desembolso inicial) y el
   Generador «(combustible/alquiler)» de `'PyG 3 Anos'!A25` (2.400 €/año) se
   redirige a la celda `suministros_mes` de Supuestos en vez de vivir como
   fila fija suelta, para que no quede huérfano de fórmula (§1.2: «ningún
   literal sobrevive dentro de una fórmula ni de un rótulo aparte»).
5. **Aparecen los costes fijos que el checklist obliga a contratar y que el
   plan no tenía** (TEC-18, igual que en los otros cuatro hermanos): gestión
   de residuos y aceite usado (crítico en un food truck: la plancha y la
   freidora generan aceite usado de forma continua y el propio checklist ya
   avisa de «filtro y gestión aceite usado», `'F3 - Equipamiento'!E6`), DDD,
   PRL y derechos de autor por música ambiental en eventos. Todos en celda
   verde con nota de «pide presupuesto en tu zona».

6. **El vehículo entra en la base amortizable, que es de donde faltaba.** La
   clasificación por defecto del motor reconoce «obra», «instalaciones» y
   «equipamiento», pero no la palabra «vehículo»: los 25.000 € del food truck
   —la partida más grande del plan, el 38 % de la inversión— caían fuera de
   toda base y el libro amortizaba 4.510 €/año sobre 27.800 € de inmovilizado
   cuando el inmovilizado real de este plan son 53.600 €. Este módulo declara
   su propia tabla `AMORTIZABLE`. Sin ella el resultado del año 1 salía
   inflado y el semáforo de rentabilidad daba verde por una amortización que
   faltaba: es el defecto de `CRIT-02`/`NUEVO-02` por FALTA de patrón, el
   mismo que se midió en panadería.
7. **La vida útil del equipamiento pasa de 5 a 10 años** (`RD-15`, el mismo
   defecto que ya corrigió el representante): 5 años son el 20 % anual, muy
   por encima del coeficiente lineal máximo de la tabla del art. 12.1 LIS
   —12 % para maquinaria y 10 % para mobiliario—, así que el exceso no sería
   deducible y la base imponible del modelo quedaba mal calculada. El
   vehículo sí se queda en 8 años (12,5 %): es elemento de transporte, cuyo
   coeficiente lineal máximo es el 16 %.
8. **Ningún sueldo por debajo del SMI en proporción a la jornada.** El
   refuerzo de eventos (120 €/mes al 10 % de jornada) y la línea de
   suplencias (70 € al 6 %) quedaban unos euros por debajo del SMI 2026
   prorrateado —1.221 €/mes a jornada completa— y el semáforo de la hoja de
   Personal las sacaba en ROJO en el fichero que se entrega.

Resultado del caso base (medido en el libro del 2026-09-05): coste de personal
**31,2 %** (techo 32 %), coste de mercancía **27,1 %** (techo 33 %), margen
bruto **64,1 %** (suelo 62 %), aparcamiento y base **3,6 %** (techo 5 %) y
resultado neto **5,1 %** (suelo 4 %). **Las cinco pasan y el plan ya no se
suspende a sí mismo.** El margen del primer año es estrecho a propósito: el
plan carga la amortización completa del vehículo y los intereses del préstamo
desde el primer ejercicio y opera con 45 clientes al día, el extremo BAJO del
rango «40-80 clientes por servicio» que declara el propio libro.
"""

CONCEPTO = 'Food Truck'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato = se queda el que trae `grupo_a`.
# pct_comida/pct_bebida NO se declaran aquí: con dos líneas de venta
# comida/bebida (`LINEAS_INGRESO`, abajo) `grupo_a.supuestos_calculadas()`
# las escribe SOLAS desde el peso de esas líneas — mismo patrón que
# cafetería, panadería y tapas-bar.
# ==========================================================================
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 45, None,
        'Clientes servidos al día de media del año. Es el mismo «Clientes/'
        'día objetivo (Año 1)» que ya declaraba el fichero v1.1',
        "fichero v1.1 ('Punto Equilibrio'!B11, coincide con 'Escenarios'!"
        "C6 columna REALISTA)"),
    'ticket_medio': (
        None, None, 12.00, None,
        'SIN IVA. Es el mismo 12 € que ya usaban Punto Equilibrio y la '
        'columna realista de Escenarios (declarar que es SIN IVA no cambia '
        'ningún número, sólo aclara qué era). Dentro del rango 10-15 € que '
        'fija Instrucciones!B8 «Ticket medio food truck»',
        "fichero v1.1 ('Punto Equilibrio'!B9 y 'Escenarios'!C7, TEC-11/"
        'DOM-30)'),
    'crec_a2': (
        None, None, 0.15, None,
        'El fichero v1.1 proyectaba 175.000 € en el año 2 sobre 135.000 € '
        '(+29,6 %): se redondea a la baja porque un food truck de un año no '
        'tiene todavía rutas ni clientela corporativa consolidadas (mismo '
        'criterio conservador que tapas-bar y cafetería)',
        'fichero v1.1 (redondeado a la baja, conservador)'),
    'crec_a3': (
        None, None, 0.10, None,
        'El fichero v1.1 proyectaba 215.000 € sobre 175.000 € (+22,9 %): '
        'igual, redondeado a la baja',
        'fichero v1.1 (redondeado a la baja, conservador)'),
    'dias_apertura': (
        None, None, 250, None,
        'El MISMO dato lo usan la cuenta de resultados, el punto de '
        'equilibrio y los escenarios. La versión anterior traía TRES '
        'calendarios que no coincidían: 25 días de servicio al mes en el '
        'punto de equilibrio (300 al año), 5 servicios por semana durante '
        '48 semanas en los escenarios (240 al año) y ninguno declarado en '
        'la cuenta de resultados. Se fijan 250 días —5 días de servicio a '
        'la semana por 50 semanas activas, dentro de los «4-6 días '
        'operativos por semana» que declara este mismo libro— porque son '
        'los únicos que reproducen al céntimo la facturación que el propio '
        'libro ya publicaba: 45 × 12 × 250 = 135.000 €',
        'fichero v1.1 (reconciliación de los tres calendarios propios — '
        'fija NUEVO-03 de este hermano. El documento hablaba de 300 días, '
        'que con 45 clientes y 12 € darían 162.000 € y no los 135.000 € que '
        'publica el propio libro; el documento se reescribe desde estas '
        'celdas en T9)'),
    'coste_comida': (
        None, None, 0.28, None,
        'Coste de mercancía de la comida: dentro del 28-33 % que declara '
        'este mismo libro («depende del concepto: burger 30 %, tacos 25 %, '
        'poke 35 %»). Se toma el extremo bajo del rango porque la compra '
        'diaria que exige un food truck, sin cámara grande, reduce la merma '
        'frente a una cocina fija. Es la palanca más sensible del plan: con '
        'el 33 % el resultado del primer año se queda muy justo',
        "fichero v1.1 (Instrucciones!B4; 'PyG 3 Anos'!B12 usaba 30 % sólo "
        'sobre la línea de comida de calle, sin costear el catering — ver '
        'LINEAS_INGRESO)'),
    'coste_bebida': (
        None, None, 0.22, None,
        'Bebidas embotelladas y refrescos: extremo bajo del 22-28 % que '
        'declara Instrucciones!B5 («refrescos y agua embotellada, margen '
        'alto»)',
        'fichero v1.1 (Instrucciones!B5)'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Packaging biodegradable: extremo bajo del 3-5 % que declara '
        'Instrucciones!B6. Es una partida realmente cara en un food truck '
        '(obligatoria por normativa municipal en muchos casos, '
        "'F3 - Equipamiento'!E14 del checklist) y por eso se cita al lado "
        "del food cost, no dentro de «varios»",
        "fichero v1.1 (Instrucciones!B6; 'PyG 3 Anos'!B14 = 5.400/135.000 "
        '= 4,0 %, dentro del mismo rango)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: este negocio vende en el punto de venta móvil, '
        'no reparte a domicilio. Súbelo si activas un canal de delivery '
        'desde una ubicación fija',
        'TEC-23/DOM-34 (mismo criterio que el representante y los otros '
        'tres A-β)'),
    'comision_delivery': (
        None, None, 0.28, None,
        'Sin uso mientras pct_delivery esté a 0: rango habitual de '
        'comisión de plataforma si algún día operas desde una ubicación '
        'fija con reparto',
        'parametrizado (el fichero v1.1 no lo contemplaba; sin efecto con '
        'el canal a 0)'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado: un food truck urbano '
        'cobra en tarjeta/contactless la mayoría de los tickets',
        'parametrizado (el fichero v1.1 no lo contemplaba)'),
    # ⚠️ el rótulo se queda en el que trae `grupo_a` ('Alquiler mensual del
    # local (€)') porque es la CLAVE con la que `grupo_a.demos()` localiza
    # la fila; rotularla «del aparcamiento» rompe el dry-run con «no se
    # localizan las filas alquiler_sup».  Que aquí no hay local lo dice la
    # nota, en mayúsculas y en primera línea.
    'alquiler_mes': (
        None, None, 400, None,
        'ESTE NEGOCIO NO PAGA RENTA DE LOCAL: esta celda es el coste '
        'mensual del aparcamiento o la nave en la que el vehículo pernocta '
        'y se prepara cada jornada, y de ella salen también la fianza y los '
        'meses previos a la apertura. Es un concepto distinto del '
        'generador, que va en la celda de suministros. 400 €/mes es lo que '
        'cuesta una plaza cubierta con toma de agua y desagüe para un '
        'vehículo comercial grande en una ciudad media española: pide '
        'presupuesto en tu zona antes de firmar',
        'parametrizado (concepto nuevo: el fichero v1.1 no tenía ninguna '
        'fila de aparcamiento ni de base del vehículo)'),
    'fianza_meses': (
        None, 'Fianza del aparcamiento (meses)', 2, None,
        'Dos meses de fianza por la plaza o la nave, menos que los tres '
        'habituales de un local comercial',
        'parametrizado'),
    'suministros_mes': (
        None, None, 200, None,
        'Combustible del generador eléctrico y mantenimiento de las tomas '
        'de agua y de vertido. Es el mismo concepto que la versión anterior '
        'llamaba «Generador (combustible/alquiler)» dentro de los costes '
        'fijos: ahora vive en una celda, para poder cambiarlo en un solo '
        'sitio y que el resto del libro se entere',
        "fichero v1.1 ('PyG 3 Anos'!B25 = 2.400 €/año ÷ 12; §1.2, ningún "
        'literal sobrevive dentro de una fórmula ni de un rótulo)'),
    'seguros_ano': (
        None, None, 2500, None,
        'Responsabilidad civil profesional alimentaria —la fase 1 de tu '
        'checklist pide un mínimo de 300.000 € de cobertura— más el seguro '
        'del vehículo a todo riesgo. Es la MISMA prima que la versión '
        'anterior contaba dos veces, una en la inversión y otra como gasto '
        'del año: aquí se cuenta una sola vez, que es como se paga',
        "fichero v1.1 ('PyG 3 Anos'!B23 = 'Inversion Inicial'!B14, misma "
        'cifra en las dos hojas — doble conteo propio de este hermano)'),
    'pct_varios': (
        None, None, 0.05, None,
        'Combustible del vehículo para desplazarse entre ubicaciones más el '
        'colchón de gasto corriente no presupuestado. Es un coste VARIABLE: '
        'sube y baja con los servicios que se hacen, así que no puede vivir '
        'entre los fijos, porque movería el punto de equilibrio sin que se '
        'notara. Agrupa dos partidas que la versión anterior tenía sueltas: '
        'el combustible, que ya era variable, y los varios e imprevistos, '
        'que estaban mal clasificados como fijos',
        "fichero v1.1: ('PyG 3 Anos'!B15 «Combustible vehiculo» = 4.800 + "
        "B30 «Varios e imprevistos» = 2.000) / 135.000 = 5,04 %, redondeado "
        '(RT-04/RT-05)'),
    'recursos_propios': (
        None, None, 25000, None,
        'Aportación del titular. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja de este plan',
        'parametrizado'),
    'prestamo': (
        None, None, 72000, None,
        'Principal solicitado. La hoja de Financiación comprueba que el '
        'origen de fondos cuadra con la necesidad de caja de la hoja 1 '
        '(25.000 € de recursos propios + 72.000 € de préstamo = 97.000 €). '
        'Está por encima de los 73.400 € que sumaba la versión anterior '
        'porque el fondo de maniobra pasa a ser de verdad de tres meses, y '
        'porque ahora se suman a la necesidad de caja el IVA de la '
        'inversión —que hay que adelantar aunque se recupere— y los '
        'imprevistos de la puesta en marcha',
        'parametrizado (ajustado desde un primer intento más bajo tras '
        'comprobar la necesidad de caja real del caso base — mismo gotcha '
        'que tapas-bar y cafetería)'),
    'tipo_prestamo': (
        None, None, 0.065, None,
        'Tipo nominal anual; un préstamo de menor importe y sin garantía '
        'inmobiliaria (el vehículo es la garantía) suele salir algo por '
        'encima del de un local: pide oferta a dos entidades y a una línea '
        'ICO/ENISA de emprendedores antes de fijarlo',
        'parametrizado'),
    'plazo_prestamo': (
        None, None, 6, None,
        'Años totales, carencia incluida. Un vehículo se amortiza más '
        'rápido que unas obras de local, así que el plazo también es más '
        'corto',
        'parametrizado'),
    'carencia_prestamo': (
        None, None, 1, None,
        'Primer año sólo intereses, que es cuando la caja está más tensa '
        '(adaptación del vehículo + primeras semanas de rodaje probando '
        'ubicaciones)',
        'parametrizado'),
    'meses_fondo': (
        None, None, 3, None,
        'Mínimo que exige este mismo libro (Instrucciones): un colchón por '
        'debajo de 3 meses no cubre un bache de mal tiempo o de temporada '
        'baja de eventos',
        'SPEC §2.2 / TEC-07 (v1.1 dotaba 6.000 €, que eran 1,14 meses de '
        'sus propios costes fijos de entonces — NUEVO-01, la MENOR '
        'desviación absoluta de los cinco hermanos pero igual de '
        'incumplida)'),
    # ⚠️ misma cautela que en `vida_maquinaria`: el rótulo es la clave con
    # la que `grupo_a.demos()` localiza la fila ('Vida útil de obra e
    # instalaciones (años)').  En este producto ese grupo NO es obra: es el
    # vehículo y todo lo que va montado en él, y así lo dice la nota.
    'vida_obra': (
        None, None, 8, None,
        'Vehículo, adaptación y rotulación, instalación de gas, depósito de '
        'aguas y proyecto técnico: todo lo que va montado en el vehículo se '
        'amortiza con él. Ocho años son el 12,5 % anual, por debajo del '
        'coeficiente lineal máximo del 16 % que la tabla del art. 12.1 de '
        'la Ley del Impuesto sobre Sociedades fija para los elementos de '
        'transporte. Confírmalo con tu asesor',
        "fichero v1.1 ('PyG 3 Anos'!A34 «Amortizacion (7 anos vehiculo)», "
        'ajustado a 8 para quedar dentro del coeficiente y del uso real)'),
    # ⚠️ la ETIQUETA de esta celda NO se puede cambiar desde contenido:
    # `grupo_a.demos()` localiza la fila por su RÓTULO NORMALIZADO exacto
    # ('Vida útil de maquinaria y mobiliario (años)') y, si no la encuentra,
    # el dry-run falla con «no se localizan las filas vida_maq_sup».  Medido
    # el 2026-09-05 al intentar rotularla «del equipamiento y el mobiliario».
    # La aclaración va en la NOTA, que es lo que el cliente lee al lado.
    'vida_maquinaria': (
        None, None, 10, None,
        'Equipamiento de cocina, generador, TPV, menaje y toldo. El uso es '
        'más intenso que en una cocina fija por el montaje y el desmontaje '
        'diarios, pero el coeficiente lineal máximo de la tabla del art. '
        '12.1 de la Ley del Impuesto sobre Sociedades es del 12 % para '
        'maquinaria y del 10 % para mobiliario: por debajo de 9-10 años el '
        'exceso no sería deducible. Confírmalo con tu asesor',
        'recalibrado por RD-15 (la v2.0 previa puso 5 años = 20 % anual, '
        'muy por encima del coeficiente máximo; v1.1: 7 años planos para '
        'TODO el inmovilizado sin distinguir el vehículo del equipamiento '
        '— NUEVO-02)'),
    'pct_bebida_alc': (
        None, None, 0.05, None,
        'Bebida ALCOHÓLICA sobre el total de bebida: casi nula — la línea '
        'de bebida de este plan es refrescos, agua y zumos (Instrucciones!'
        'B5 «refrescos y agua embotellada»); sólo alguna cerveza envasada '
        'ocasional en festivales de música. El resto va al IVA reducido de '
        'hostelería',
        'parametrizado (composición de la línea de bebida de este plan: '
        "'PyG 3 Anos'!A7 «Ventas bebidas» sin desglose alcohólico/sin "
        'alcohol en el fichero original)'),
    'aforo': (
        None, 'Plazas de pie y mesas altas junto al vehículo', 16, None,
        'ESTE NEGOCIO NO TIENE PLAZAS SENTADAS: son las cuatro mesas altas '
        'plegables de cuatro posiciones que presupuesta la partida «Toldo, '
        'mobiliario exterior plegable» de la hoja de inversión. De aquí '
        'sale sólo una rotación INFORMATIVA y el aviso de capacidad del '
        'punto de equilibrio; no condiciona ninguna licencia, porque un '
        'food truck no tiene aforo legal. El techo real de este negocio son '
        'los clientes por servicio, que este mismo libro sitúa en 40-80',
        'parametrizado (la v2.0 previa puso 12 y el punto de equilibrio '
        'salía exigiendo 3,11 rotaciones al día contra un techo declarado '
        'de 3,0: el semáforo de capacidad quedaba en ROJO en el caso base)'),

    'salario_convenio': (
        None, None, 0, None,
        'El convenio PROVINCIAL de hostelería (o el de comercio, según '
        'cómo se clasifique la actividad de venta ambulante en tu '
        'provincia) es el suelo real del sector: cópialo de la tabla '
        'salarial que corresponda. Con 0 el semáforo compara sólo contra el '
        'SMI',
        'SPEC §2.6/DOM-24 (mismo criterio que el representante y los otros '
        'tres A-β)'),
    'meses_renta_previa': (
        None, 'Meses de alquiler del aparcamiento ANTES de abrir', 2, None,
        'La adaptación del vehículo dura 4-8 semanas según la fase 2 de tu '
        'propio checklist: son dos meses de aparcamiento y base que se '
        'pagan antes de facturar el primer euro, así que forman parte de la '
        'inversión y no de la cuenta de resultados',
        "fichero v1.1 (checklist, fase 2: «4-8 semanas» de adaptación)"),
    'pct_imprevistos': (
        None, None, 0.08, None,
        'Se conserva el mismo 8 % que la versión anterior tenía escrito a '
        'mano en su fila de imprevistos, ahora calculado por fórmula sobre '
        'las partidas de compra y adaptación del vehículo: si cambias el '
        'precio del vehículo, los imprevistos se recalculan solos',
        "fichero v1.1 ('Inversion Inicial'!A22 «Imprevistos (8%)», mismo "
        'porcentaje, RD-02)'),
}

# ==========================================================================
# §2.3.2 — líneas de venta. DOS líneas (comida/bebida), el patrón
# `mix_en_supuestos` que ya usan cafetería, panadería y tapas-bar: con más de
# dos, `grupo_a.pyg()` deja `pct_bebida` en 0 % con el libro en blanco
# (defecto de MOTOR, no de este contenido). La línea «Catering/eventos
# privados» de la v1.1 (10.000 €, sin food cost propio en el fichero
# original) se funde en la línea de comida, igual que tapas-bar fundió su
# línea «Otros»: así SÍ se le aplica un food cost, en vez de facturar a
# margen 100 % como hacía la v1.1.
# (rótulo, peso, grupo 'comida'|'bebida', nota, fuente)
# ==========================================================================
LINEAS_INGRESO = (
    # ⚠️ el rótulo NO puede llevar «eventos» ni «día»: `motor` decide el
    # formato de la fila por su rótulo (§1.4) y cualquier palabra de
    # RECUENTO le quita el formato de euro a una fila que son euros.  La
    # v2.0 previa rotulaba «…menú del día… y catering/eventos privados» y
    # las seis celdas de la fila salían marcadas por el gate de formatos.
    ('Ventas de comida (calle, mercados y catering privado)', 0.8519,
     'comida',
     'Producto principal servido en ubicaciones fijas y mercados, más el '
     'catering y las celebraciones privadas (la línea «Catering/eventos '
     'privados» de la v1.1, que en el fichero original NO llevaba coste de '
     'mercancía propio: aquí SÍ lo lleva, con el mismo tipo que la comida '
     'de calle)',
     "fichero v1.1: suma de «Ventas comida» + «Catering/eventos privados» "
     '((105.000+10.000)/135.000 = 85,19 %)'),
    ('Ventas de bebida (refrescos, agua y zumos embotellados)', 0.1481,
     'bebida',
     'Bebidas embotelladas de acompañamiento del menú: el food truck no '
     'sirve bebida de barra',
     "fichero v1.1: «Ventas bebidas» / 135.000 = 20.000/135.000 = 14,81 %"),
)

# ==========================================================================
# §2.6 — plantilla redimensionada por horas de servicio (§7-bis.17)
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
# ==========================================================================
PLANTILLA = (
    ('Propietario/a — chef, gestión y conducción', 1, 1500,
     'Elabora el producto, conduce el vehículo entre ubicaciones y lleva la '
     'gestión, compras y RRSS. Cubre el turno fuerte de los 250 días de '
     'servicio al año',
     'recalibrado §7-bis.17 (v1.1: «Propietario / Chef principal» 2.000 €, '
     'coste/año 37.352 €, jornada completa sin ninguna referencia de horas '
     'de servicio real)',
     1.0),
    # ⚠️ el bruto de cada fila tiene que quedar por encima del SMI EN
    # PROPORCIÓN a la jornada (17.094 €/14 pagas = 1.220,71 €/mes a jornada
    # completa, RD 126/2026), o el semáforo de la columna «Bruto mes» sale
    # en ROJO en el fichero que se entrega.  Los tres parciales van unos
    # euros por encima de su suelo: 549,32 · 122,07 · 73,24.
    ('Ayudante de cocina y servicio', 1, 560,
     'Prep, montaje, atención al cliente y desmontaje. A tiempo parcial: un '
     'food truck de dos servicios diarios como máximo no necesita una '
     'segunda persona a jornada completa. Por encima del SMI en proporción '
     'a su jornada',
     'recalibrado (v1.1: «Ayudante cocina / Servicio» 1.500 € a jornada '
     'prácticamente completa; 550 € quedaban a 0,68 € del suelo del SMI '
     'prorrateado)',
     0.45),
    ('Refuerzo de festivales y eventos grandes', 1, 125,
     'Sólo para los picos de afluencia que el propio fichero describe '
     '(«Festivales = facturación x3-5 en un día»): unas pocas jornadas al '
     'mes, no un puesto estable. Por encima del SMI en proporción a su '
     'jornada',
     'recalibrado (v1.1: «Extra eventos (eventual)» 600 €; la v2.0 previa '
     'puso 120 €, por DEBAJO del SMI prorrateado de una jornada del 10 % '
     '—122,07 €— y el semáforo lo sacaba en rojo)',
     0.10),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que sí impone
    # la ley: 30 días naturales de vacaciones (art. 38 ET) son días de
    # servicio que alguien tiene que cubrir, o el food truck simplemente no
    # abre esos días (lo que también es una decisión, pero se declara).
    ('Suplencias de vacaciones y descansos', 1, 75,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) del propietario y '
     'del ayudante, y del descanso semanal. Por encima del SMI en '
     'proporción a su jornada',
     'parametrizado (RC-19; la v2.0 previa puso 70 €, por DEBAJO del SMI '
     'prorrateado de una jornada del 6 % —73,24 €—)', 0.06),
)

# ==========================================================================
# §2.2 — partidas de la inversión
# ==========================================================================
#: Reglas por rótulo NORMALIZADO (después de que `_limpiar_rotulo` quite el
#: paréntesis con el parámetro, §7-bis.11): `('suprimir', motivo)` o
#: `(importe, nota)`.
INVERSION = {
    # §1.7 — tres NOTAS heredadas de la v1.1 con palabras sin tilde
    # («Varia», «movil», «Genero»).  El rótulo de la fila no se puede
    # cambiar desde contenido (`INVERSION` sólo admite «suprimir» o un
    # importe), pero pasando el MISMO importe se reescribe la nota sin
    # tocar ni el orden de la hoja ni la cifra que el cliente pueda estar
    # usando (§1.3).  Los rótulos que siguen sin tilde («Vehiculo food
    # truck», «Adaptación y rotulación vehiculo», «Equipamiento cocina
    # movil», «TPV movil + datafono» y «Mantenimiento vehiculo + ITV» del
    # P&L) son de MOTOR: piden «vehiculo»→«vehículo» y «movil»→«móvil» en
    # `motor.TILDES`, y van reportados en el informe de esta tanda.
    'licencias y permisos (promedio)': (
        2000, 'Varía mucho por municipio y comunidad autónoma: pide el '
        'importe en el tuyo antes de cerrar el presupuesto'),
    'proyecto tecnico sanitario': (
        1500, 'Obligatorio para la actividad alimentaria móvil: planos de '
        'instalación, flujos y depósitos de agua'),
    'stock inicial de producto': (
        1000, 'Género para las primeras dos semanas de servicio'),
    'imprevistos': (
        'suprimir',
        'RD-02 (mismo patrón que el representante y los otros tres A-β): '
        'el 8 % tecleado a mano se sustituye por la fila «Imprevistos de '
        'obra y adaptación», que `grupo_a` calcula por fórmula sobre las '
        'partidas de obra de este mismo bloque con el porcentaje de '
        'Supuestos (§2.2)'),
    # Hallazgo propio de este hermano (ver preámbulo, punto 4): la misma
    # prima anual de seguro está en DOS hojas a la vez.
    'seguro vehiculo + rc actividad': (
        'suprimir',
        'Doble conteo propio de este hermano: es la MISMA prima anual '
        "(2.500 €) que 'PyG 3 Anos'!B23 «Seguro vehiculo + RC» ya carga "
        'como coste fijo recurrente del año 1 (ahora en Supuestos!'
        'seguros_ano). Contarla también aquí sumaría dos veces la prima del '
        'primer año a la necesidad de caja — mismo síntoma que TEC-12 mide '
        'en la línea B de esta familia, aquí en línea A'),
}

#: Sin altas nuevas: las tres partidas que TEC-18 añade en los otros
#: hermanos (residuos, DDD, PRL) son costes RECURRENTES de operación, no
#: desembolsos de puesta en marcha, y van en FIJOS_EXTRA (más abajo), no
#: aquí.
INVERSION_EXTRA = ()

# ==========================================================================
# §2.3.6 / TEC-20 / `NUEVO-02` — qué partidas de la inversión son
# inmovilizado y con qué vida útil.
#
# ⚠️ SIN esta tabla el hermano pierde su activo principal.  `grupo_a`
# clasifica por RÓTULO con `AMORT_DEFECTO`, cuyos patrones son los de un
# local: «obra civil», «instalaci», «equipamiento», «mobiliario»…  Ninguno
# casa con «Vehiculo food truck (nuevo o segunda mano)» ni con «Deposito
# agua + aguas residuales», y `_clasificar_amortizable` manda por defecto al
# grupo «no»: 25.800 € —el 39 % de la inversión y el activo que da nombre al
# negocio— quedaban FUERA de la base amortizable, con el libro amortizando
# 4.510 €/año sobre 27.800 € en vez de 6.280 € sobre 53.600 €.  Es el mismo
# defecto por FALTA de patrón que se midió en panadería (`AMORT_DEFECTO`,
# comentario de `grupo_a`), aquí sobre la partida más cara del plan.
#
# Los dos grupos NO son «obra» y «maquinaria» en sentido literal: son las
# dos vidas útiles que necesita un food truck.  El vehículo y todo lo que
# va montado en él son ELEMENTOS DE TRANSPORTE (coeficiente lineal máximo
# del 16 % en la tabla del art. 12.1 LIS → 8 años son el 12,5 %, dentro);
# el equipamiento y el mobiliario van al grupo de 10 años (12 % maquinaria
# y 10 % mobiliario).  El grupo «no» se prueba ANTES que los otros dos.
# ==========================================================================
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|inmobiliaria|stock|existencias|'
           r'primera compra|fondo de maniobra|colch[oó]n|imprevisto|'
           r'marketing|lanzamiento|web|constituci|notar[ií]a|registro|'
           r'gestor[ií]a|seguro|licencia|permiso|tasa|iva|marca|dise[ñn]o',),
    'obra': (r'veh[ií]culo|food truck|furgoneta|remolque|adaptaci|rotulaci|'
             r'instalaci|dep[oó]sito|deposito|proyecto t[eé]cnico',),
    'maquinaria': (r'equipamiento|generador|tpv|dat[aá]fono|datafono|menaje|'
                   r'utensilios|packaging|toldo|mobiliario|mesa|plancha|'
                   r'freidora|nevera|c[aá]mara|fregadero|campana|balanza',),
}

# ==========================================================================
# §2.3 (COSTES FIJOS del P&L) — la MISMA lógica de `INVERSION`, pero sobre
# las filas fijas que ya trae `'PyG 3 Anos'`. Hallazgo propio de este
# hermano: «Generador (combustible/alquiler)» (2.400 €/año) es el MISMO
# concepto que ahora vive en `Supuestos!suministros_mes` (ver esa celda) —
# a diferencia de «Seguro vehiculo + RC», que el motor ya excluye solo por
# canon, «generador» no coincide con ningún patrón reservado y quedaría
# como fila preservada ADEMÁS del `cf_suministros` hardcodeado, contando el
# mismo gasto dos veces. Se suprime aquí explícitamente.
# ==========================================================================
FIJOS = {
    'generador (combustible/alquiler)': (
        'suprimir',
        'Doble conteo propio de este hermano: es el MISMO gasto que ahora '
        "vive en Supuestos!suministros_mes (200 €/mes = 2.400 €/año, "
        "redirigido desde esta misma fila de 'PyG 3 Anos'!A25 — §1.2, "
        'ningún literal sobrevive dentro de una fórmula ni de un rótulo '
        'aparte). Dejarla también aquí sumaría el generador dos veces al '
        'total de costes fijos'),
}

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (TEC-18, FAMILIA(5): el mismo defecto que en los otros cuatro hermanos)
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Gestión de residuos (orgánico, cartón y aceite usado)', 400,
     'Gestor autorizado. El propio checklist ya avisa de que la freidora '
     'genera aceite usado que hay que gestionar, pero nunca contrataba el '
     'servicio. Pide presupuesto en tu zona',
     'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 400,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC móvil que el '
     'checklist ya exige en su fase de personal',
     'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 350,
     'El plan de prevención es obligatorio; el proveedor externo, no (art. '
     '30.5 de la Ley 31/1995). A quién se marca como responsable se corrige '
     'en el propio checklist',
     'parametrizado (DOM-26)'),
    # ⚠️ el rótulo NO puede llevar la palabra «eventos»: `motor` clasifica
    # el formato de la fila por su rótulo (§1.4) y cualquier palabra de
    # RECUENTO («eventos», «días», «clientes»…) le quita el formato de euro
    # a una fila que son euros.  «Ventas» y «Derechos» no están en la lista
    # de rótulos de importe fuerte del motor, así que la única salida desde
    # contenido es no usar la palabra.
    ('Derechos de autor por música ambiental (SGAE/AGEDI-AIE)', 200,
     'Sólo se paga si el food truck pone música propia en ferias y '
     'festivales (distinto de la licencia del organizador, que cubre el '
     'recinto y no cada puesto). Presupuesto mínimo por si se usa',
     'parametrizado (TEC-18)'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Las CINCO ratios que exige el gate de la tanda (dry-run: «caso base que
# pasa sus 5 ratios»). Los rótulos los pone `grupo_a`; aquí van el valor y el
# comentario, con la cita literal de `Instrucciones` de ESTE producto.
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.62,
     'Suelo del propio libro: «Instrucciones!B10 — Margen bruto objetivo: '
     '>62%. Inferior a restaurante por packaging y combustible»'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.33,
     'Blend de los food cost que publica este producto (comida 28-33 %, '
     'bebida 22-28 %, packaging 3-5 % — Instrucciones!B4-B6): 33 % deja '
     'margen sobre el 30 % real del caso base (comida 28 %, bebida 22 %, '
     'packaging 3 %)'),
    ('r_personal', 'Coste de personal / Ventas', 0.32,
     'Techo del propio libro: «Instrucciones!B7 — Coste personal / ventas: '
     '25-32%. Menos personal que restaurante: 2-3 personas»'),
    ('r_alquiler', 'Alquiler / Ventas', 0.05,
     'No hay referencia de local en este libro (el food truck no paga '
     'renta de local): 5 % es un techo prudente para el aparcamiento/base '
     'del vehículo, muy por debajo del 8-12 % de un negocio con local fijo '
     '(mismo orden que el resto de la familia, adaptado a este molde)'),
    ('r_neto', 'Resultado neto / Ventas', 0.04,
     'Derivado del suelo de EBITDA que declara este producto para el año 2 '
     '(«Instrucciones!B11 — EBITDA objetivo (Año 2): 20-30%»): '
     'descontando amortización, intereses e Impuesto de Sociedades, un '
     'EBITDA en la franja baja del rango deja un resultado neto positivo '
     'ya en el año 1, aunque ajustado por ser el primer ejercicio'),
)

# ==========================================================================
# §2.5 — escenarios extremos (cubiertos/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# El fichero v1.1 tenía dos escenarios más (pesimista/optimista) con su
# propio ticket y días, con un TERCER calendario (46/50 semanas × 4/6
# servicios/semana): se unifican a los 250 días de Supuestos (NUEVO-03),
# conservando cubiertos y ticket de cada extremo.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (30, 10.00, 250),
    'optimista': (65, 14.00, 250),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma 1)
# ==========================================================================
#: Estacionalidad de un food truck urbano dependiente de eventos y clima:
#: verano fuerte (festivales, terrazas, turismo — docx: «festivales
#: musicales y gastronómicos»), diciembre fuerte por mercados navideños,
#: enero-febrero flojos por clima y por la vuelta de las vacaciones.
#: PARÁMETRO editable: si el concepto se especializa en catering corporativo
#: de oficinas, el pico de verano se modera y sube el de otoño-invierno.
ESTACIONALIDAD = (0.060, 0.062, 0.075, 0.080, 0.088, 0.098,
                  0.105, 0.100, 0.088, 0.080, 0.074, 0.090)

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    # ⚠️ `grupo_a` escribe los puntos 1 a 5 de «CÓMO SE USA ESTE LIBRO»: la
    # numeración de aquí CONTINÚA esa lista.  La v2.0 previa empezaba en el
    # 7 y el libro publicado saltaba del 5 al 7, sin punto 6.
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una '
        'operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota) — se conservan las referencias del
    # sector que ya traía este fichero (mismo criterio que el resto de la
    # familia: no se borran, se citan con su fuente).  La columna de FUENTE
    # la lee el cliente: nada de ids internos de auditoría (CON-08).
    'referencias': [
        ('Food cost comida', '28-33 %', 'Fichero v1.1',
         'Depende del concepto: burger 30 %, tacos 25 %, poke 35 %. Este '
         'plan trabaja con el 28 %, el extremo bajo: si tu carta va al 33 %, '
         'el resultado del primer año se queda muy justo'),
        ('Food cost bebidas', '22-28 %', 'Fichero v1.1',
         'Refrescos y agua embotellada, margen alto'),
        ('Coste packaging / ventas', '3-5 %', 'Fichero v1.1',
         'Packaging eco más caro pero obligatorio en muchos municipios'),
        ('Coste personal sobre ventas', '25-32 %', 'Fichero v1.1',
         'Menos personal que un restaurante: 2-3 personas'),
        ('Ticket medio food truck', '10-15 €', 'Fichero v1.1',
         'Menú completo: plato + bebida + extra. El de este plan son 12 € '
         'SIN IVA, que con el tipo de hostelería salen 13,20 € de PVP'),
        ('Clientes por servicio', '40-80', 'Fichero v1.1',
         'Depende de ubicación, evento y día de la semana. Este plan '
         'proyecta 45, el extremo bajo del rango, a propósito'),
        ('Margen bruto objetivo', '> 62 %', 'Fichero v1.1',
         'Inferior a un restaurante por el peso del packaging y el '
         'combustible'),
        ('EBITDA objetivo (año 2)', '20-30 %', 'Fichero v1.1',
         'Muy rentable si aciertas las ubicaciones. Con los supuestos de '
         'partida este plan se queda por debajo del rango: es lo que hay '
         'que mejorar subiendo clientes por servicio o ticket'),
        ('Retorno de la inversión', '12-24 meses', 'Fichero v1.1',
         'Es la referencia del sector. El de ESTE plan lo calcula la hoja '
         'de Tesorería y sale más largo, porque cuenta también el IVA que '
         'hay que adelantar y el fondo de maniobra'),
        ('Días operativos/semana', '4-6', 'Fichero v1.1',
         'Mercados, eventos, zona de oficinas, festivales'),
        ('Servicios por día', '1-2', 'Fichero v1.1',
         'Comida (12-15 h) y/o cena (19-23 h) según ubicación'),
        ('Coste de combustible/mes', '300-500 €', 'Fichero v1.1',
         'Desplazamiento entre ubicaciones. En este plan va dentro del '
         '«Varios e imprevistos» de los costes variables'),
        ('Permisos anuales (promedio)', '2.000-5.000 €', 'Fichero v1.1',
         'Varía mucho por municipio y comunidad autónoma'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería o de '
         'comercio (según clasificación de la venta ambulante)',
         'Fichero v1.1 (fase 4 del checklist)',
         'No existe una tabla salarial estatal única: copia la tabla que '
         'te corresponda en la celda de Supuestos'),
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
    # cambia— con acentos opcionales, mismo criterio que el resto de la
    # familia (que perdió reemplazos en su primera pasada por anclar contra
    # el texto de ANTES del §1 transversal).
    'reemplazos': [
        # DOM-08 / COM-11 (FAMILIA) — el carnet de manipulador está
        # DEROGADO (RD 109/2010); la responsabilidad es de la EMPRESA. En
        # este hermano vive en 'F4 - Personal', no en la hoja de
        # constitución.
        (r'^Carnet manipulador alimentos$',
         'Formación en higiene alimentaria de todo el equipo'),
        (r'^Todos$', 'Titular'),
        (r'^Obligatorio todo personal$',
         'El «carnet de manipulador» está derogado (RD 109/2010): la '
         'formación la acredita la EMPRESA y se documenta en el plan '
         'APPCC móvil'),
        # DOM-09 (FAMILIA) — un food truck vende directamente al
        # consumidor final: el registro que corresponde es el AUTONÓMICO,
        # no el RGSEAA estatal (RD 191/2011 art. 2.2).
        (r'^Registro sanitario RGSEAA$',
         'Inscripción en el Registro Sanitario de tu Comunidad Autónoma '
         '(declaración responsable de inicio de actividad alimentaria)'),
        (r'^Sanidad$', 'Sanidad CCAA'),
        (r'^Obligatorio para elaboraci[oó]n alimentaria$',
         'El Registro General Sanitario estatal NO aplica al minorista que '
         'sirve al consumidor final (art. 2.2 del RD 191/2011): el que te '
         'toca es el autonómico, el mismo que pide la fase 2 de este '
         'checklist con la autorización sanitaria del vehículo'),
        # DOM-25 (FAMILIA) — cuota de autónomo parametrizada, con nota de
        # año. Medido tras el §1 transversal: «autónomos» y «€» ya puestos
        # por el motor.
        (r'Tarifa plana aut[oó]nomos? 80\s*(EUR|€)/mes',
         'Cuota según la base mínima del tramo que te corresponda. '
         'Consulta el importe del ejercicio en curso y verifica con tu '
         'gestoría si te aplica la cuota reducida de inicio de actividad'),
        # DOM-26 (FAMILIA) — el PRL obligatorio es el PLAN, no el
        # proveedor externo.
        (r'^SPA$', 'Titular o servicio ajeno'),
        # DOM-33 (REPRESENTANTE, extendido a esta hermana) — el epígrafe de
        # IAE 671.4 («restaurantes de dos tenedores») es de un
        # establecimiento FIJO, no de un vehículo de venta ambulante.
        (r'Epigrafe IAE: 671\.4 o 677\.9 \(venta ambulante\)',
         'Epígrafe IAE: 672.x (servicios de restauración en quioscos, '
         'food trucks e instalaciones móviles análogas) o 677.9 (venta '
         'ambulante sin elaboración) — la elección la valida tu gestor '
         'según si elaboras el producto en el vehículo o sólo lo vendes'),
        # §1.7 — tildes que `motor.TILDES` no lleva como palabra suelta
        # («vehiculo», «movil», «datafono», «genero», «rapido», «depositos»,
        # «carroceria», «via», «telematicos», «cuales», «estaras»).
        # Dos cautelas medidas:
        #  (a) se anclan contra el texto POSTERIOR al §1 transversal, que es
        #      lo que ve `grupo_a.checklist()`.  Los tres reemplazos que la
        #      v2.0 previa escribió contra el texto CRUDO («resenas»,
        #      «minimo») no llegaron a dispararse NUNCA porque el motor ya
        #      los había acentuado, y el dry-run salía verde igual: ningún
        #      gate mide si un reemplazo se ejecutó.
        #  (b) el acento va OPCIONAL en el patrón y el patrón casa también
        #      con su propio resultado.  Así siguen valiendo el día que el
        #      motor incorpore «vehiculo»/«movil» a `TILDES` (fix pedido en
        #      el informe de esta tanda) y son idempotentes: la 2.ª pasada
        #      encuentra el texto ya corregido y no lo vuelve a tocar.
        (r'^Imprescindible( para los)? tr[aá]mites telem[aá]ticos$',
         'Imprescindible para los trámites telemáticos'),
        (r'^Seguro (del )?veh[ií]culo \((furgoneta/remolque|furgoneta o '
         r'remolque)\)$',
         'Seguro del vehículo (furgoneta o remolque)'),
        (r'^FASE 2: VEH[IÍ]CULO Y PERMISOS$', 'FASE 2: VEHÍCULO Y PERMISOS'),
        (r'^Selecci[oó]n y compra (del )?veh[ií]culo$',
         'Selección y compra del vehículo'),
        (r'^Adaptaci[oó]n (del )?veh[ií]culo para cocina$',
         'Adaptación del vehículo para cocina'),
        (r'^Obligatorio si se modifica (la )?carrocer[ií]a$',
         'Obligatorio si se modifica la carrocería'),
        (r'^Planos (de )?instalaci[oó]n,? (flujos|y flujos)[ ,y]+dep[oó]sitos '
         r'(de )?agua$',
         'Planos de instalación, flujos y depósitos de agua'),
        (r'^Autorizaci[oó]n sanitaria (del )?veh[ií]culo$',
         'Autorización sanitaria del vehículo'),
        (r'^Inspecci[oó]n del veh[ií]culo (ya )?equipado$',
         'Inspección del vehículo ya equipado'),
        (r'^Permiso (de )?ocupaci[oó]n (de la )?v[ií]a p[uú]blica$',
         'Permiso de ocupación de la vía pública'),
        (r'^Dep[oó]sito (de )?agua limpia (\+|y de aguas) residual(es)?$',
         'Depósito de agua limpia y de aguas residuales'),
        (r'^M[ií]nimo 40 ?L (de agua )?limpia (\+|y) 60 ?L (de )?residual$',
         'Mínimo 40 L de agua limpia y 60 L de residual'),
        (r'^TPV m[oó]vil (\+|y) dat[aá]fono 4G$', 'TPV móvil y datáfono 4G'),
        (r'^Tablet (\+|y) dat[aá]fono,? (con )?cobertura 4G$',
         'Tablet y datáfono con cobertura 4G'),
        (r'^Rotulaci[oó]n integral (del )?veh[ií]culo$',
         'Rotulación integral del vehículo'),
        (r'^Kit (de )?montaje r[aá]pido para cada servicio$',
         'Kit de montaje rápido para cada servicio'),
        (r'^Formaci[oó]n (en )?APPCC m[oó]vil$', 'Formación en APPCC móvil'),
        (r'^Temperaturas, cadena (de )?fr[ií]o en (el )?veh[ií]culo,? '
         r'(y )?trazabilidad$',
         'Temperaturas, cadena de frío en el vehículo y trazabilidad'),
        (r'^(Setup|Montaje), servicio r[aá]pido, (teardown|desmontaje),? '
         r'(y )?limpieza$',
         'Montaje, servicio rápido, desmontaje y limpieza'),
        (r'^P[aá]gina web con (el )?calendario (de )?ubicaciones$',
         'Página web con el calendario de ubicaciones'),
        (r'^D[oó]nde estar[aá]s cada d[ií]a de la semana$',
         'Dónde estarás cada día de la semana'),
        (r'^Programa (de )?fidelizaci[oó]n m[oó]vil$',
         'Programa de fidelización móvil'),
        (r'^Tarjeta digital o QR: (10o men[uú] gratis|el d[eé]cimo men[uú], '
         r'gratis)$',
         'Tarjeta digital o QR: el décimo menú, gratis'),
        (r'^Saber qu[eé] ubicaciones funcionan y cu[aá]les no$',
         'Saber qué ubicaciones funcionan y cuáles no'),
        (r'^Pesar (el )?g[eé]nero, controlar mermas,? (y )?ajustar pedidos$',
         'Pesar el género, controlar mermas y ajustar pedidos'),
        (r'^Encuestas (a )?clientes (\+|y) rese[ñn]as (de )?Google$',
         'Encuestas a clientes y reseñas de Google'),
        (r'^Plan (de )?expansi[oó]n \((2o truck o local|segundo truck o '
         r'local fijo)\)$',
         'Plan de expansión (segundo truck o local fijo)'),
        (r'^Si funciona, evaluar (un )?segundo veh[ií]culo o (un )?local '
         r'fijo$',
         'Si funciona, evaluar un segundo vehículo o un local fijo'),
    ],
    'suprimir': [],
    'fases': {},
    # TEC-18 (FAMILIA) + RGPD: trámites que faltan y cuestan dinero o multa.
    # Repartidos por hoja (F1 Constitución, F2 Vehículo, F3 Equipamiento,
    # F4 Personal, F5 Marketing, F6 primeros 90 días) — molde C2 (6 hojas),
    # igual que el resto de A-β.
    'altas': [
        ('F1', 'RGPD',
         'Registro de actividades de tratamiento de datos personales',
         'Titular', 'Antes de abrir',
         'Art. 30 del RGPD y art. 31 de la LOPDGDD: lo pide la AEPD en la '
         'primera inspección. Incluye clientes del programa de '
         'fidelización, personal y proveedores'),
        ('F1', 'Fiscal',
         'Adaptar el TPV móvil al sistema Veri*factu / factura '
         'electrónica', 'Gestor', 'Antes de abrir',
         'El RD 1007/2023 y su calendario escalonado obligan a que el '
         'software de facturación sea verificable. Consulta la fecha que '
         'te aplica antes de comprar el TPV móvil y el datáfono que ya '
         'presupuesta la hoja de Inversión Inicial: cambiarlo después '
         'cuesta el doble'),
        ('F2', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador',
         'Titular', '1 día',
         'También son obligatorias en venta ambulante: el modelo y el '
         'texto del cartel los aprueba tu Comunidad Autónoma'),
        ('F2', 'Legal',
         'Contrato con gestor autorizado de residuos y aceite usado',
         'Titular', '2 semanas',
         'Se comprueba en la inspección sanitaria del vehículo. Este mismo '
         'checklist ya avisa de que la freidora genera aceite usado que '
         'hay que gestionar, pero nunca contrataba el servicio'),
        ('F2', 'APPCC',
         'Contrato de desinsectación, desratización y desinfección (DDD)',
         'Titular', '1 semana',
         'Empresa inscrita en el ROESB; el certificado forma parte del '
         'plan APPCC móvil que ya exige la fase 4 de este checklist'),
        ('F4', 'Laboral',
         'Registro horario diario de la jornada de todo el equipo',
         'Gestor', 'Desde el primer contrato',
         'Art. 34.9 del Estatuto de los Trabajadores; se conserva cuatro '
         'años. Aplica desde el primer contrato del ayudante, aunque sea a '
         'tiempo parcial'),
        ('F4', 'RGPD',
         'Informar al equipo del registro horario y del tratamiento de sus '
         'datos', 'Gestor', 'Desde el primer contrato',
         'La cláusula informativa se entrega con el contrato; el fichaje '
         'es un tratamiento de datos, no sólo una obligación laboral'),
        ('F5', 'Legal',
         'Licencia de derechos de autor por música ambiental en ferias y '
         'festivales (SGAE/AGEDI-AIE)',
         'Titular', 'Antes de poner música propia',
         'Distinta de la licencia del organizador del festival, que cubre '
         'el recinto, no cada puesto individual'),
        ('F5', 'RGPD',
         'Cláusula informativa y consentimiento en el programa de '
         'fidelización con QR', 'Titular', 'Antes de abrir',
         'El propio checklist promete un programa de fidelización móvil '
         'con QR que recoge datos de contacto: necesita su información '
         'previa'),
    ],
}

# ==========================================================================
# Registro de lo que cambia de valor respecto de la v1.1 (§1.3: «la
# diferencia entre el valor viejo y el nuevo queda anotada por fichero»)
# ==========================================================================
RECALIBRADO = (
    ('Coste de personal en la cuenta de resultados', '42.000 €',
     '42.081 €, leídos de la hoja Personal',
     'La cuenta de resultados usaba una cifra tecleada a mano que no era la '
     'de su propia hoja de Personal, que sumaba 76.566 €. Ahora la lee de '
     'ahí: si cambias un sueldo, el plan entero se recalcula'),
    ('Plantilla', '3 puestos / 76.566 € al año',
     '4 puestos (1 a jornada completa y 3 parciales) / 42.081 € al año',
     'Dimensionada para los 250 días de servicio que hace este plan, con '
     'una línea nueva para cubrir vacaciones y descansos. Con la plantilla '
     'anterior el personal se comía el 56,7 % de las ventas y el negocio no '
     'era viable con sus propios números'),
    ('Días de servicio al año',
     'tres calendarios distintos en el mismo paquete: 300 días en el punto '
     'de equilibrio, 240 en los escenarios y ninguno declarado en la cuenta '
     'de resultados',
     '250 días, un solo dato para todo el libro',
     'Son los días que hacen exacta la facturación que el propio plan ya '
     'publicaba: 45 clientes × 12 € × 250 días = 135.000 €. Equivalen a 5 '
     'días de servicio por semana durante 50 semanas'),
    ('Ticket medio', '12 € sin decir si llevaba IVA', '12 € SIN IVA',
     'El número no cambia; lo que cambia es que ahora se declara qué es. '
     'Con el IVA de hostelería son 13,20 € de precio de venta al público, '
     'dentro del rango 10-15 € que recoge este mismo libro'),
    ('Aparcamiento y base del vehículo', 'no estaba',
     '400 €/mes (4.800 € al año), más dos meses de fianza y dos meses antes '
     'de abrir',
     'Un food truck necesita un sitio en el que pernoctar, cargar agua y '
     'vaciar residuos. El plan anterior no lo pagaba en ninguna línea, así '
     'que el negocio parecía no tener ningún coste de suelo'),
    ('Fondo de maniobra', '6.000 €, etiquetados «3 meses»',
     '18.053 €: tres meses de costes fijos de caja, calculados por fórmula',
     'Los 6.000 € daban para 1,1 meses, no para 3. Es el colchón que evita '
     'cerrar por una racha de mal tiempo o un mes flojo de eventos'),
    ('Amortización', '10.343 € al año, a 7 años planos sobre todo, incluido '
     'lo que no es inmovilizado',
     '6.280 € al año: el vehículo y su adaptación a 8 años y el '
     'equipamiento y el mobiliario a 10',
     'El vehículo se amortiza más rápido que el equipamiento porque son '
     'cosas distintas para Hacienda. Y el fondo de maniobra, el stock y el '
     'marketing no se amortizan: no son inmovilizado'),
    ('Seguro del vehículo y RC', '2.500 € en la inversión Y 2.500 € al año '
     'en los gastos: la misma prima contada dos veces',
     '2.500 € al año, una sola vez',
     'Contarla en los dos sitios inflaba la inversión, el IVA a adelantar y '
     'el dinero que hay que pedir al banco'),
    ('Generador', '2.400 € al año como línea suelta, además de los '
     'suministros', '2.400 € al año dentro de la celda de suministros',
     'Era el mismo gasto escrito en dos sitios. Ahora se cambia en uno solo '
     'y el resto del libro se entera'),
    ('Imprevistos de la puesta en marcha',
     '5.500 € escritos a mano (un 8 % del total)',
     'el mismo 8 %, pero calculado sobre la compra y la adaptación del '
     'vehículo',
     'Si cambias el precio del vehículo, los imprevistos se recalculan '
     'solos en vez de quedarse en la cifra vieja'),
    ('Impuesto de Sociedades', '25 % los tres años, sin compensar pérdidas',
     '15 % los dos primeros ejercicios con beneficio, compensando las '
     'pérdidas anteriores',
     'Es el tipo que la ley reserva a las empresas de nueva creación, y las '
     'pérdidas de un año se restan del beneficio de los siguientes'),
    ('Cuota del préstamo', 'la cuota entera restaba en el resultado',
     'sólo los intereses en el resultado; la devolución del principal, en '
     'la tesorería',
     'Meter la cuota completa antes del resultado convierte la cuenta de '
     'resultados en un flujo de caja y el banco lo ve al instante'),
    ('Plan de financiación', 'no existía',
     'hoja nueva: de dónde sale el dinero, a qué se destina y el cuadro de '
     'amortización del préstamo año a año',
     'Es la hoja que pide el banco junto con la cuenta de resultados, y la '
     'que avisa si el dinero que se aporta no llega a lo que hace falta'),
    ('Tesorería mes a mes', 'no existía',
     'hoja nueva de 12 meses: cobros, pagos, IVA trimestral y saldo '
     'acumulado',
     'Responde a la única pregunta que decide una operación bancaria: en '
     'qué mes se queda el negocio sin caja'),
    ('Combustible y varios', '4.800 € de combustible sueltos + 2.000 € de '
     'varios metidos entre los costes fijos',
     'un solo 5 % sobre las ventas, tratado como coste variable',
     'El combustible sube y baja con los servicios que se hacen: ponerlo '
     'entre los fijos falseaba el punto de equilibrio'),
    ('Catering y eventos privados', '10.000 € de ingresos sin ningún coste '
     'de materia prima imputado',
     'sumados a la línea de comida, con el mismo coste de mercancía que el '
     'resto (28 %)',
     'Una línea de ingresos que no paga género da un margen que no existe'),
    ('Sueldos y SMI', 'sueldos sin comparar con ningún suelo legal',
     'ninguna fila por debajo del SMI en proporción a su jornada, y una '
     'celda para el convenio de tu provincia',
     'El convenio provincial de hostelería manda sobre el SMI: cópialo en '
     'la hoja de Supuestos y el semáforo te avisa si algún sueldo se queda '
     'corto'),
)
