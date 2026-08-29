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

Resultado del caso base (verificado con `data_only` tras `inject_cache.py`,
ver informe de la tanda): coste de personal por debajo del techo 32 % de
`Instrucciones!B7`, margen bruto por encima del suelo «>62 %» de
`Instrucciones!B10`, y resultado neto positivo. **El plan no se suspende a sí
mismo.**
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
    'dias_apertura': (
        None, None, 250, None,
        'El MISMO dato lo usan el P&L, el punto de equilibrio y los '
        "escenarios: el fichero v1.1 traía TRES calendarios distintos "
        "('Punto Equilibrio': 25 días/mes = 300 días/año; 'Escenarios' "
        'realista: 5 servicios/semana × 48 semanas = 240 días/año; el total '
        "de 'PyG 3 Anos' no declaraba ninguno). Se eligen 250 días (5 "
        'días/semana × 50 semanas activas, dentro de las «4-6 días '
        'operativos/semana» de Instrucciones!B13) porque son los que hacen '
        'EXACTA la cifra más repetida del paquete (135.000 €: portada del '
        "docx y el propio total de 'PyG 3 Anos'!B9), sin inventar ningún "
        'dato nuevo: 45 × 12 × 250 = 135.000 € al céntimo',
        "fichero v1.1 (reconciliación de tres calendarios propios — fija "
        'NUEVO-03 de este hermano)'),
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
    'coste_comida': (
        None, None, 0.28, None,
        'Food cost de comida: dentro del 28-33 % que declara '
        'Instrucciones!B4 de este mismo libro («depende del concepto: '
        'burger 30 %, tacos 25 %, poke 35 %»); se toma el extremo bajo del '
        'rango porque el modelo de compra diaria que exige un food truck '
        '(sin cámara grande) reduce la merma frente a un local fijo',
        "fichero v1.1 (Instrucciones!B4; 'PyG 3 Anos'!B12 usaba 30 % sólo "
        'sobre la línea de comida, sin costear el catering — ver nota de '
        "LINEAS_INGRESO)"),
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
    'alquiler_mes': (
        None, None, 400, None,
        'ESTE NEGOCIO NO TIENE LOCAL: esta celda se reutiliza para el coste '
        'mensual de aparcamiento/nave donde el vehículo pernocta y se '
        'prepara cada día (distinto del «Generador» del fichero v1.1, que '
        'va a Suministros, ver esa celda). 400 €/mes es el precio de una '
        'plaza cubierta con toma de agua y desagüe para vehículo comercial '
        'grande en una ciudad media española: pide presupuesto de tu zona '
        'antes de firmar',
        'parametrizado (concepto nuevo: el fichero v1.1 no tenía ninguna '
        'fila de aparcamiento/base)'),
    'fianza_meses': (
        None, None, 2, None,
        'Dos meses de fianza para la plaza de aparcamiento/nave, menores '
        'que los tres habituales de un local comercial',
        'parametrizado'),
    'suministros_mes': (
        None, None, 200, None,
        'Combustible del generador eléctrico y mantenimiento de las tomas '
        'de agua/vertido: es el mismo concepto que el fichero v1.1 llamaba '
        '«Generador (combustible/alquiler)» en la fila fija de PyG, ahora '
        'en celda para que no quede un número suelto dentro de un rótulo',
        "fichero v1.1 ('PyG 3 Anos'!B25 = 2.400 €/año ÷ 12; §1.2, ningún "
        'literal sobrevive dentro de una fórmula ni de un rótulo)'),
    'seguros_ano': (
        None, None, 2500, None,
        'Responsabilidad civil profesional alimentaria (mínimo 300.000 € — '
        "checklist 'F1 - Constitucion'!E12) + seguro del vehículo a todo "
        'riesgo. Es la MISMA prima que citaba la Inversión Inicial del '
        'fichero v1.1: se retira de ahí para no contarla dos veces (ver '
        'INVERSION más abajo)',
        "fichero v1.1 ('PyG 3 Anos'!B23 = 'Inversion Inicial'!B14, misma "
        'cifra en las dos hojas — doble conteo propio de este hermano)'),
    'pct_varios': (
        None, None, 0.05, None,
        'Combustible del vehículo (desplazamiento entre ubicaciones) + '
        'colchón de gasto corriente no presupuestado. Es un coste VARIABLE '
        '(sube y baja con los servicios realizados, no puede vivir en los '
        'fijos: RT-04/RT-05, mismo criterio que los otros tres A-β) — '
        'agrega DOS filas que el fichero v1.1 tenía sueltas: Combustible '
        '(ya estaba en COSTES VARIABLES) y Varios e imprevistos (estaba mal '
        'clasificado dentro de COSTES FIJOS)',
        "fichero v1.1: ('PyG 3 Anos'!B15 «Combustible vehiculo» = 4.800 + "
        "B30 «Varios e imprevistos» = 2.000) / 135.000 = 5,04 %, redondeado"),
    'recursos_propios': (
        None, None, 25000, None,
        'Aportación del titular. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja de este plan',
        'parametrizado'),
    'prestamo': (
        None, None, 72000, None,
        'Principal solicitado. La hoja de Financiación comprueba que '
        'origen y usos cuadran con la necesidad de caja calculada en la '
        'hoja 1 (recursos propios + préstamo = 97.000 €; muy por encima de '
        'los 73.400 € que sumaba la v1.1 porque el fondo de maniobra real '
        'es mayor que el que dotaba el fichero original — NUEVO-01 — y '
        'porque se añaden el IVA soportado sobre la inversión y los '
        'imprevistos de obra por fórmula, que el fichero original no '
        'sumaba a la necesidad de caja)',
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
    'vida_obra': (
        None, None, 8, None,
        'Vehículo, adaptación e instalación de gas: coincide aproximado con '
        'los «7 años» que ya citaba la v1.1, ajustado a los coeficientes de '
        'elementos de transporte de la tabla del art. 12.1 LIS. Confírmalo '
        'con tu asesor',
        "fichero v1.1 ('PyG 3 Anos'!A34 «Amortizacion (7 anos vehiculo)», "
        'redondeado a 8 dentro del mismo orden de magnitud)'),
    'vida_maquinaria': (
        None, None, 5, None,
        'Equipamiento de cocina móvil, generador, TPV y menaje: uso mucho '
        'más intenso que el de una cocina fija (montaje y desmontaje '
        'diarios), por eso una vida útil más corta que en el resto de '
        'hermanos de línea A. Coeficiente lineal máximo del art. 12.1 LIS: '
        'confírmalo con tu asesor',
        'parametrizado (v1.1: 7 años planos para TODO el inmovilizado, sin '
        'distinguir vehículo de equipamiento — NUEVO-02, mismo criterio que '
        'cafetería y panadería)'),
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
        None, None, 12, None,
        'ESTE NEGOCIO NO TIENE «PLAZAS SENTADAS»: se reutiliza como '
        'capacidad informal de cola + mesas altas plegables alrededor del '
        'vehículo (Inversion Inicial: «Toldo, mobiliario exterior '
        'plegable»). De aquí sale sólo una rotación INFORMATIVA; no '
        'condiciona ninguna licencia como en un local con aforo legal',
        "fichero v1.1 ('Inversion Inicial'!A20 «Toldo, mobiliario exterior "
        'plegable», mesas altas plegables, capacidad estimada)'),
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
        None, None, 2, None,
        'La adaptación del vehículo dura 4-8 semanas según el propio '
        "checklist ('F2 - Vehiculo'!D6): son dos meses de aparcamiento/base "
        'antes de abrir que sí forman parte de la inversión, no del P&L',
        "fichero v1.1 (checklist 'F2 - Vehiculo'!D6 «4-8 semanas»)"),
    'pct_imprevistos': (
        None, None, 0.08, None,
        'Se conserva el mismo 8 % que ya declaraba la v1.1 en su fila '
        '«Imprevistos (8%)», ahora calculado por fórmula sobre el bloque de '
        'obra y adaptación en vez de tecleado a mano',
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
    ('Ventas de comida (menú del día a pie de calle y catering/eventos '
     'privados)', 0.8519, 'comida',
     'Producto principal servido en ubicaciones fijas y mercados, más '
     'catering y eventos privados (la línea «Catering/eventos privados» de '
     'la v1.1, que en el fichero original NO llevaba food cost propio: '
     'aquí SÍ lo lleva, con el mismo tipo que la comida de calle)',
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
     'servicio al año (Supuestos!dias_apertura)',
     'recalibrado §7-bis.17 (v1.1: «Propietario / Chef principal» 2.000 €, '
     'coste/año 37.352 €, jornada completa sin ninguna referencia de horas '
     'de servicio real)',
     1.0),
    ('Ayudante de cocina y servicio', 1, 550,
     'Prep, montaje, atención al cliente y desmontaje. A tiempo parcial: '
     'un food truck de dos servicios diarios como máximo '
     '(Instrucciones!B14: «Servicios por día: 1-2») no necesita una segunda '
     'persona a jornada completa',
     'recalibrado (v1.1: «Ayudante cocina / Servicio» 1.500 € a jornada '
     'prácticamente completa)',
     0.45),
    ('Refuerzo de festivales y eventos grandes', 1, 120,
     'Sólo para los picos de afluencia que el propio fichero describe '
     '(«Festivales = facturación x3-5 en un día», checklist '
     "'F6 - 90 Dias'!E11): unas pocas jornadas al mes, no un puesto "
     'estable',
     'recalibrado (v1.1: «Extra eventos (eventual)» 600 € — se ajusta a la '
     'proporción real de eventos grandes sobre 250 días de servicio '
     'normal)',
     0.10),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que sí impone
    # la ley: 30 días naturales de vacaciones (art. 38 ET) son días de
    # servicio que alguien tiene que cubrir, o el food truck simplemente no
    # abre esos días (lo que también es una decisión, pero se declara).
    ('Suplencias de vacaciones y descansos', 1, 70,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) del propietario y '
     'del ayudante, y del descanso semanal',
     'parametrizado (RC-19, mismo criterio que el representante y los '
     'otros tres A-β)', 0.06),
)

# ==========================================================================
# §2.2 — partidas de la inversión
# ==========================================================================
#: Reglas por rótulo NORMALIZADO (después de que `_limpiar_rotulo` quite el
#: paréntesis con el parámetro, §7-bis.11): `('suprimir', motivo)` o
#: `(importe, nota)`.
INVERSION = {
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
     'Gestor autorizado; el propio checklist ya avisa de que la freidora '
     "genera aceite usado que hay que gestionar ('F3 - Equipamiento'!E6: "
     '«con filtro y gestión aceite usado») pero nunca contrata el servicio. '
     'Pide presupuesto en tu zona',
     'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 400,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC móvil que '
     "el checklist ya exige ('F4 - Personal'!B8: «Formación APPCC movil»)",
     'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 350,
     'El plan de prevención es obligatorio (checklist '
     "'F4 - Personal'!B10); el proveedor externo, no (art. 30.5 de la Ley "
     '31/1995) — la corrección de a quién se marca como responsable va en '
     'el propio checklist, ver CHECKLIST más abajo',
     'parametrizado (DOM-26)'),
    ('Derechos de autor por música ambiental en eventos (SGAE/AGEDI-AIE)',
     200,
     'Sólo se paga si el food truck pone música propia en ferias y '
     'festivales (distinto de la licencia del organizador del evento, que '
     'cubre el recinto, no cada puesto). Presupuesto mínimo por si se usa',
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
    'uso': [
        '7. La hoja «Tesorería 12 meses» responde la pregunta que decide una '
        'operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '8. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota) — se conservan las referencias del
    # sector que ya traía este fichero (mismo criterio que el resto de la
    # familia: no se borran, se citan con su fuente).
    'referencias': [
        ('Food cost comida', '28-33 %', 'Fichero v1.1',
         'Depende del concepto: burger 30 %, tacos 25 %, poke 35 %'),
        ('Food cost bebidas', '22-28 %', 'Fichero v1.1',
         'Refrescos y agua embotellada, margen alto'),
        ('Coste packaging / ventas', '3-5 %', 'Fichero v1.1',
         'Packaging eco más caro pero obligatorio en muchos municipios'),
        ('Coste personal sobre ventas', '25-32 %', 'Fichero v1.1',
         'Menos personal que un restaurante: 2-3 personas'),
        ('Ticket medio food truck', '10-15 €', 'Fichero v1.1',
         'Menú completo: plato + bebida + extra'),
        ('Clientes por servicio', '40-80', 'Fichero v1.1',
         'Depende de ubicación, evento y día de la semana'),
        ('Margen bruto objetivo', '> 62 %', 'Fichero v1.1',
         'Inferior a un restaurante por el peso del packaging y el '
         'combustible'),
        ('EBITDA objetivo (año 2)', '20-30 %', 'Fichero v1.1',
         'Muy rentable si aciertas las ubicaciones'),
        ('Retorno de la inversión', '12-24 meses', 'Fichero v1.1',
         'Mucho más rápido que un restaurante por la menor inversión'),
        ('Días operativos/semana', '4-6', 'Fichero v1.1',
         'Mercados, eventos, zona de oficinas, festivales'),
        ('Servicios por día', '1-2', 'Fichero v1.1',
         'Comida (12-15 h) y/o cena (19-23 h) según ubicación'),
        ('Coste de combustible/mes', '300-500 €', 'Fichero v1.1',
         'Desplazamiento entre ubicaciones'),
        ('Permisos anuales (promedio)', '2.000-5.000 €', 'Fichero v1.1',
         'Varía mucho por municipio y comunidad autónoma'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería o de '
         'comercio (según clasificación de la venta ambulante)',
         'DOM-24 / checklist F4',
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
         'toca es el autonómico, el mismo que ya pide '
         "'F2 - Vehiculo'!B10 «Autorización sanitaria vehiculo»"),
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
        # §1.7 — «musica»/«resenas»/«afluencia» sin tilde en textos que no
        # cambian de número ni de cifra: se corrigen aquí porque no todas
        # las variantes están en `motor.TILDES` como palabra suelta.
        # Medido el 2026-08-29 en el gate de esta misma tanda.
        (r'^Encuestas clientes \+ resenas Google$',
         'Encuestas a clientes y reseñas de Google'),
        (r'Testear ubicaciones \(minimo 5\)',
         'Testear ubicaciones (mínimo 5)'),
        (r'Evaluar eventos y festivales',
         'Evaluar eventos y festivales'),
        # DOM-33 (REPRESENTANTE, extendido a esta hermana) — el epígrafe de
        # IAE 671.4 («restaurantes de dos tenedores») es de un
        # establecimiento FIJO, no de un vehículo de venta ambulante: no
        # encaja con este negocio aunque el fichero lo ofrezca como
        # alternativa. El 677.9 (venta ambulante) SÍ es correcto y se
        # conserva; se sustituye el otro por el grupo 672 (servicios en
        # instalaciones móviles/análogas), que es el que de verdad se aplica
        # cuando hay elaboración y servicio en el propio vehículo.
        (r'Epigrafe IAE: 671\.4 o 677\.9 \(venta ambulante\)',
         'Epígrafe IAE: 672.x (servicios de restauración en quioscos, '
         'food trucks e instalaciones móviles análogas) o 677.9 (venta '
         'ambulante sin elaboración) — la elección la valida tu gestor '
         'según si elaboras el producto en el vehículo o sólo lo vendes'),
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
         "te aplica antes de comprar el «TPV movil + datafono» que ya "
         "presupuesta 'Inversión Inicial'!B16"),
        ('F2', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador',
         'Titular', '1 día',
         'También son obligatorias en venta ambulante: el modelo y el '
         'texto del cartel los aprueba tu Comunidad Autónoma'),
        ('F2', 'Legal',
         'Contrato con gestor autorizado de residuos y aceite usado',
         'Titular', '2 semanas',
         'Se comprueba en la inspección sanitaria del vehículo. El propio '
         "checklist ya avisa de que la freidora genera aceite usado "
         "('F3 - Equipamiento'!E6) pero no contrataba el servicio"),
        ('F2', 'APPCC',
         'Contrato de desinsectación, desratización y desinfección (DDD)',
         'Titular', '1 semana',
         'Empresa inscrita en el ROESB; el certificado forma parte del '
         "plan APPCC móvil que ya exige 'F4 - Personal'!B8"),
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
         'Licencia de derechos de autor por música ambiental en eventos '
         '(SGAE/AGEDI-AIE)',
         'Titular', 'Antes de cada evento con música propia',
         'Distinta de la licencia del organizador del festival, que cubre '
         'el recinto, no cada puesto individual'),
        ('F5', 'RGPD',
         'Cláusula informativa y consentimiento en el programa de '
         'fidelización con QR', 'Titular', 'Antes de abrir',
         "El propio checklist promete un «Programa fidelización movil "
         "(QR)» ('F5 - Marketing'!B14) que recoge datos de contacto: "
         'necesita su información previa'),
    ],
}

# ==========================================================================
# Registro de lo que cambia de valor respecto de la v1.1 (§1.3: «la
# diferencia entre el valor viejo y el nuevo queda anotada por fichero»)
# ==========================================================================
RECALIBRADO = (
    ('Coste de personal imputado al P&L', '42.000 €',
     'Sale de la hoja Personal, por fórmula',
     'TEC-01/DOM-01 (FAMILIA): el P&L usaba una cifra tecleada distinta de '
     'su propia hoja Personal (76.566 €), una diferencia de 34.566 € — la '
     'menor en términos absolutos de los cinco hermanos, pero un 56,7 % de '
     'las ventas igual de inviable'),
    ('Plantilla', '3 puestos / 76.566 €',
     '4 puestos (uno a jornada completa, dos a tiempo parcial y '
     'suplencias) / dentro del techo 32 % de Instrucciones!B7',
     '§7-bis.17: dimensionada por horas de servicio de los 250 días/año '
     'del caso base; con la plantilla anterior el coste laboral era el '
     '56,7 % de las ventas'),
    ('Calendario', "'Punto Equilibrio' (25 días de servicio/mes = 300 "
     "días/año) · 'Escenarios' realista (5 servicios/semana × 48 semanas "
     '= 240 días/año) · total de PyG sin calendario declarado (TRES '
     'lecturas distintas)', '250 días/año, un único dato en Supuestos '
     '(45 clientes/día × 12 € × 250 días = 135.000 €, reproduce EXACTO el '
     'total que ya publicaba PyG)',
     'NUEVO-03 (defecto propio de este hermano, no visto por el R1 del '
     'representante A-α: aquí son TRES calendarios, no dos)'),
    ('Ticket medio', '12 € (sin declarar IVA)', '12 € SIN IVA (mismo '
     'número)', 'TEC-11/DOM-30: se declara qué era el número, no se '
     'cambia el número'),
    ('Fondo de maniobra', '6.000 € etiquetados «3 meses»',
     '3 × costes fijos de caja mensuales, por fórmula',
     'TEC-07/DOM-12/NUEVO-01: los 6.000 € cubrían 1,14 meses de los '
     '5.275 €/mes de costes fijos de la v1.1 (con la cifra de personal '
     'correcta, el colchón necesario es aún mayor)'),
    ('Amortización', '10.343 €/año a 7 años planos sobre TODO el '
     'inmovilizado (incluido lo que no es inmovilizado)',
     'Base amortizable real (sólo vehículo/adaptación y equipamiento) / '
     'vida útil por fórmula, con vehículo (8 años) y equipamiento (5 '
     'años) separados',
     'NUEVO-02: la base plana no distinguía el vehículo del equipamiento '
     'de cocina, que se desgasta mucho más rápido por el montaje y '
     'desmontaje diarios'),
    ('Doble conteo de seguro', '2.500 € en la Inversión Inicial + 2.500 '
     '€/año en el P&L (la misma prima contada dos veces)',
     '2.500 €/año una sola vez, como coste fijo recurrente en Supuestos!'
     'seguros_ano',
     'Hallazgo propio de este hermano (§9, verificación T7): mismo '
     'síntoma que TEC-12 mide en la línea B, aquí en línea A'),
    ('Imprevistos de obra', '5.500 € (8 % tecleado a mano sobre el total)',
     'Por fórmula sobre las partidas de obra y adaptación del bloque, con '
     'el porcentaje en Supuestos',
     '§7-bis.11: ningún número vive dentro de una fórmula ni de un '
     'rótulo'),
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
    ('Varios e imprevistos + combustible', '2.000 €/año fijo dentro de '
     'COSTES FIJOS + 4.800 €/año variable suelto',
     '5 % de las ventas, un único coste VARIABLE',
     'RT-04/RT-05: un coste que sube y baja con los servicios realizados '
     'no puede vivir en los costes fijos (movía el punto de equilibrio de '
     'forma no lineal); se funden en una sola celda porque ambos '
     'responden al mismo tipo de gasto (desplazamiento y colchón '
     'operativo)'),
    ('Generador (combustible/alquiler)', '2.400 €/año como fila fija '
     'suelta EN PARALELO a lo que iba a ser Suministros (doble conteo si '
     'no se suprime; hallazgo propio de este hermano)',
     '2.400 €/año en Supuestos!suministros_mes (200 €/mes), fila original '
     'suprimida vía FIJOS',
     '§1.2: ningún literal vive dentro de un rótulo aparte cuando puede '
     'vivir en una celda de Supuestos'),
    ('Catering/eventos privados', '10.000 € de ingresos sin food cost '
     'propio en el fichero original (se facturaba a margen 100 %)',
     'Fundido en la línea de comida, con el mismo food cost que el resto '
     'de la comida (28 %)',
     'Hallazgo propio de este hermano: una línea de ingresos sin ningún '
     'coste de mercancía imputado infla el margen bruto de forma '
     'artificial'),
)
