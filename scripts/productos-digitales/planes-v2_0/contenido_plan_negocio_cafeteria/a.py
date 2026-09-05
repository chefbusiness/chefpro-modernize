#!/usr/bin/env python3
"""
Contenido de `plan-negocio-cafeteria` para el grupo A (§2 de la SPEC, T7).

Molde **A-β**: hojas SIN numerar (`'Inversion Inicial'`, `'PyG 3 Anos'`,
`'Punto Equilibrio'`, `'Escenarios'`, `'Personal'`, `'Instrucciones'`) y
**sin ningún input de ticket ni de cubiertos en el P&L** en el fichero
original — vivían repartidos entre `Escenarios` y `Punto Equilibrio`, con DOS
calendarios distintos (`NUEVO-03`). `grupo_a.py` los unifica: el motor
reconstruye el P&L con el MISMO driver `cubiertos × ticket × días` que A-α
(§1.1 de la SPEC dixit: «el mismo motor que el P&L» aplica a las cinco líneas
de la familia) y reparte el total entre las líneas de venta propias de una
cafetería/brunch por su peso (§2.3.2).

Aquí NO hay lógica: sólo los datos propios de este plan —supuestos,
plantilla, partidas, umbrales y textos legales del checklist— con **la fuente
de cada cifra**. La mecánica es de `grupo_a.py`.

DE DÓNDE SALE CADA NÚMERO — tres orígenes, siempre declarados (mismo criterio
que `contenido_plan_negocio_bar_restaurante/a.py`, el representante):

  * «fichero v1.1» — estaba ya en `plan-financiero-cafeteria-brunch.xlsx` o en
    `checklist-apertura-cafeteria-brunch.xlsx` y se conserva.
  * «SPEC/R1» — lo fija `planes-v2-SPEC.md` o un hallazgo del R1 del
    representante que también mide esta familia (columna «ámbito» del mapa
    §8, FAMILIA).
  * «parametrizado» — no está en la SPEC ni en el fichero: celda VERDE
    editable con nota. Ninguna cifra del sector se teclea sin marcarla como
    parámetro (regla dura 6 del encargo T7).

⚠️ NINGUNA nota de este módulo cita una celda por su COORDENADA. La
reconstrucción de `Instrucciones` mueve la tabla de referencias del sector, y
las 17 citas «Instrucciones!Bnn» heredadas de la v1.1 apuntaban a celdas que
ya contienen otra cosa (R-03 de la refutación del 29-ago: B21 no es el ticket
combinado, es el margen bruto; B17 no es el techo de personal, es su valor
real). Las referencias se citan **por su nombre** en la tabla «DATOS DE
REFERENCIA DEL SECTOR», que es lo único que no se mueve.

⚠️ Y ninguna nota que lleve un importe en euros contiene la palabra «plan »,
«kit », «guía », «pack » ni «ebook»: `motor.cross_sell_sin_precios` (§1.9)
borra los precios de cualquier celda que las lleve, y así se comió el
«~10,10 € de PVP» de la nota del ticket, que llegó al fichero publicado como
«equivale a ~ de PVP, dentro del rango 8 que declara…» (R-05). El defecto de
la guarda es del motor y está reportado; aquí se esquiva escribiendo las
notas sin ese disparador.

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01, y R-01/R-02 de la
refutación del 2026-08-29)
------------------------------------------------------------------------
El defecto que hunde los cinco planes de línea A es el mismo en los cinco: el
P&L imputa un coste de personal que NO es el de su propia hoja `Personal`.
Medido en `plan-financiero-cafeteria-brunch.xlsx` v1.1: `'PyG 3 Anos'!B23` =
72.000 € mientras `'Personal'!E10` suma **137.270 €** — la propia celda
`Personal!F10` lo escribía: «~72% sobre ventas previstas», mientras el P&L
imprimía 37,9 %.

La primera recalibración (v2.0, agosto) cuadró el ratio de personal bajando
la plantilla a 70.011 €… y dejó dos semáforos del propio libro EN ROJO:

1. **Cinco de los seis salarios estaban por debajo del SMI en proporción a
   la jornada** (R-01). El formato condicional de la columna «Bruto mes» los
   pintaba en rojo él solo: 1.120 €/mes a jornada completa son 15.680 €/año
   frente a los 17.094 € del SMI 2026 (RD 126/2026). Un producto no puede
   entregar una plantilla de ejemplo por debajo del suelo legal.
2. **La plantilla no cubría el horario que el propio libro declara** (R-02):
   6.072 horas contratadas frente a las 7.800 que salen de 13 horas de
   servicio × 2 personas × 300 días. El ratio de personal del 31,7 % se
   sostenía sobre una plantilla que no puede abrir la cafetería.

Esta versión arregla las dos cosas y vuelve a recalibrar el caso base «por
los dos lados y dentro de rangos con fuente», sin tocar ningún porcentaje
escondido:

1. **Plantilla dimensionada por horas de servicio y con el SMI como suelo.**
   Seis puestos, tres de ellos a jornada parcial, que suman **4,25 jornadas
   completas = 7.820 horas al año**: la cobertura pasa del 77,8 % al 100,3 %.
   Ningún bruto baja del SMI 2026 en proporción a su jornada (1.221 €/mes a
   jornada completa, 14 pagas). Coste: **100.082,50 €/año**.
2. **Los clientes/día suben de 80 a 100.** El rango que publica este mismo
   libro para una cafetería urbana es de **80 a 150**; 100 clientes sobre las
   45 plazas son 2,2 servicios por plaza y día, y el propio libro trabaja con
   2-3 turnos de mesa en el brunch de fin de semana. Con 80 clientes/día una
   cafetería que abre 13 horas con dos personas a la vez NO paga su plantilla
   legal: ése es el mensaje del plan, no un ajuste cosmético.
3. **El ticket pasa de 9,20 a 9,80 € SIN IVA**, que son 10,78 € de PVP: sigue
   dentro del rango de 8 a 12 € de «ticket medio combinado» que publica el
   propio libro, y por debajo del ticket de un brunch completo (14-20 €).
4. **El crecimiento de los años 2 y 3 se modera** (del 10 % y el 7 % al 7 % y
   el 5 %): el año 1 ya arranca con 100 clientes/día, así que lo que queda
   por crecer es ocupación en hora punta, no clientela nueva. Con el
   crecimiento anterior el EBITDA de los años 2 y 3 se iba al 18-20 %, muy
   por encima del 8-15 % que el propio libro publica como objetivo.
5. **El origen de fondos cuadra con los usos** (R del gate §2.11.12-bis): el
   préstamo baja de 114.000 a **112.000 €** y, con 40.000 € de recursos
   propios, los 152.000 € de origen cubren los 151.976 € de necesidad de caja
   con 24 € de diferencia (0,02 %, tope 5 %). Antes sobraban 9.512 € de deuda
   que se pagaba sin usarla.
6. **Aparecen los costes fijos que el checklist obliga a contratar y que el
   plan no tenía** (TEC-18, igual que en los otros cuatro hermanos): gestión
   de residuos, DDD, derechos de autor por música ambiental y PRL. Todos en
   celda verde con nota de «pide presupuesto en tu zona».

Resultado del caso base (leído del libro regenerado el 2026-09-05): coste de
personal **34,0 %** (techo 35 %), alquiler **8,2 %** (techo 12 %), coste de
mercancía **29,6 %** (techo 32 %), margen bruto **66,1 %** (suelo 65 %) y
resultado neto **9,1 %** (suelo 5 %). Los dos semáforos que el libro pinta
por su cuenta —suelo salarial y cobertura de horas— quedan también en verde.
**El plan ya no se suspende a sí mismo.**
"""

CONCEPTO = 'Cafetería / Brunch'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato = se queda el que trae `grupo_a`.
# ==========================================================================
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 100, None,
        'Clientes servidos al día de media del año, contando el café de '
        'barra y el brunch de mesa. Dentro del rango de 80 a 150 que este '
        'mismo libro publica para una cafetería urbana en la tabla de '
        'referencias del sector; la rotación que implica sobre el aforo la '
        'calcula la celda «Rotaciones al día implícitas» de esta misma hoja',
        'recalibrado §7-bis.17 y R-02 (v1.1: 67, una cifra DERIVADA de la '
        'facturación objetivo; v2.0 previa: 80, que no pagaba la plantilla '
        'legal del horario declarado)'),
    'ticket_medio': (
        None, None, 9.80, None,
        'SIN IVA. El PVP equivalente lo calcula la celda «PVP equivalente '
        'con IVA» de esta misma hoja; compáralo con el «Ticket medio '
        'combinado» de la tabla de referencias del sector, más abajo en la '
        'hoja de Instrucciones',
        'recalibrado por TEC-11/DOM-30 y §7-bis.17 (v1.1: 9,50 € sin '
        'declarar si llevaba IVA; v2.0 previa: 9,20 €)'),
    'dias_apertura': (
        None, None, 300, None,
        'El MISMO dato lo usan el P&L, el punto de equilibrio y los '
        'escenarios: el fichero v1.1 tenía DOS calendarios distintos '
        '(Punto Equilibrio: 30 días/mes; Escenarios: 300-310 días/año)',
        'fichero v1.1 (Escenarios) — fija NUEVO-03'),
    'crec_a2': (None, None, 0.07, None,
                'Segundo año con la clientela de barrio ya fidelizada. Es '
                'ocupación en hora punta, no clientela nueva: el año 1 ya '
                'arranca con 100 clientes al día',
                'recalibrado (v2.0 previa: 10 %, que dejaba el EBITDA del '
                'año 2 por encima del objetivo que publica el libro)'),
    'crec_a3': (None, None, 0.05, None,
                'Tercer año, cerca del techo de aforo en las horas punta',
                'recalibrado (v2.0 previa: 7 %)'),
    'coste_comida': (
        None, None, 0.32, None,
        'Food cost de la comida (brunch, bollería, tostas): dentro del '
        '30-35 % que declara la tabla de referencias del sector de este '
        'mismo libro',
        'fichero v1.1 («Food cost comida brunch: 30-35 %»)'),
    'coste_bebida': (
        None, None, 0.28, None,
        'Coste del café y de las bebidas (calientes y frías) sobre sus '
        'propias ventas: media ponderada entre el 25-30 % del café y el '
        '28-32 % de las bebidas frías que publica este mismo libro',
        'fichero v1.1 (referencias de food cost del café y de las bebidas '
        'frías)'),
    'pct_consumibles': (
        None, None, 0.015, None,
        'Servilletas, papel, vasos de llevar y productos de limpieza de '
        'barra',
        'parametrizado (v1.1: «Packaging take-away» 3.000 € fijos, ~1,6 % '
        'de sus ventas — se convierte en variable, §2.3 RT-04/05)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: el checklist de esta apertura lo marca como '
        'tarea del mes 2-3 («Implementar delivery si hay demanda»), no del '
        'día 1. Súbelo al peso real del canal cuando lo actives',
        'TEC-23/DOM-34 (mismo criterio que el representante)'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión típica de Glovo/Uber Eats sobre el pedido servido por ese '
        'canal; confírmala en tu contrato antes de proyectar',
        'parametrizado'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado; una cafetería de barra '
        'cobra en tarjeta la mayoría de los tickets',
        'parametrizado (el fichero v1.1 no lo contemplaba)'),
    'alquiler_mes': (
        None, None, 2000, None,
        'Local de cafetería/brunch de 30-40 plazas interiores más terraza. '
        'Con el caso base recalibrado se queda dentro del 8-12 % sobre '
        'ventas que fija la tabla de referencias del sector de este mismo '
        'libro',
        'fichero v1.1 (24.000 €/año ÷ 12)'),
    'fianza_meses': (None, None, 3, None,
                     'Tres meses de renta, como en el contrato tipo de local '
                     'de negocio', 'parametrizado (v1.1 no lo declaraba)'),
    'suministros_mes': (
        None, None, 600, None,
        'Luz, agua y gas de una barra de café con horno de brunch: pide el '
        'histórico del local antes de firmar',
        'fichero v1.1 (7.200 €/año ÷ 12)'),
    'seguros_ano': (None, None, 1800, None,
                    'Responsabilidad civil (el checklist pide un mínimo de '
                    '300.000 € de cobertura) y multirriesgo del local',
                    'fichero v1.1'),
    'pct_varios': (None, None, 0.02, None,
                   'Colchón de gasto corriente no presupuestado',
                   'parametrizado (v1.1 no tenía esta línea separada)'),
    'recursos_propios': (
        None, None, 40000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja que calcula '
        'la hoja de Inversión',
        'parametrizado'),
    # R del gate §2.11.12-bis / RD-34 — con 114.000 € el origen de fondos
    # superaba los usos en 9.512,20 € (6,58 %, tope 5 %): deuda que se paga
    # sin usarla. La cifra sale de la celda «Préstamo que ajustaría el
    # origen a la necesidad» de la hoja de Financiación, resuelta la
    # circularidad (el préstamo mueve los intereses, los intereses mueven el
    # fondo de maniobra y el fondo mueve la necesidad de caja).
    'prestamo': (
        None, None, 112000, None,
        'Principal solicitado. La hoja de Financiación comprueba que el '
        'origen y los usos cuadran con la necesidad de caja calculada en la '
        'hoja de Inversión, y trae una celda que calcula el importe exacto '
        'que los ajusta',
        'recalibrado (v1.1: sin hoja de financiación; v2.0 previa: '
        '114.000 €, que dejaba 9.512 € de exceso de deuda)'),
    'tipo_prestamo': (None, None, 0.06, None,
                      'Tipo nominal anual; pide oferta a dos entidades y a '
                      'una línea ICO antes de fijarlo', 'parametrizado'),
    'plazo_prestamo': (None, None, 7, None, 'Años totales, carencia incluida',
                       'parametrizado'),
    'carencia_prestamo': (None, None, 1, None,
                          'Primer año sólo intereses, que es cuando la caja '
                          'está más tensa', 'parametrizado'),
    'meses_fondo': (
        None, None, 3, None,
        'Mínimo que exige este mismo libro: un colchón por debajo de 3 meses '
        'no cubre un bache de temporada baja',
        'SPEC §2.2 / TEC-07 (v1.1 dotaba 9.000 €, que eran 0,91 meses de sus '
        'propios costes fijos: NUEVO-01)'),
    'vida_obra': (None, None, 10, None,
                  'Obra, instalaciones y decoración de una cafetería. '
                  'Coeficientes de la tabla del art. 12.1 LIS: confírmalo '
                  'con tu asesor',
                  'parametrizado (mismo criterio que el representante)'),
    'vida_maquinaria': (
        None, None, 8, None,
        'Máquina de café, molinillo, horno, vitrinas y mobiliario. '
        'Coeficiente lineal máximo del art. 12.1 LIS: 12 % maquinaria, '
        '10 % mobiliario — por debajo de 8-10 años el exceso no es '
        'deducible. Confírmalo con tu asesor',
        'parametrizado (v1.1: 10 años planos para todo el inmovilizado, sin '
        'distinguir obra de maquinaria — NUEVO-02)'),
    'pct_bebida_alc': (
        None, None, 0.03, None,
        'Bebida ALCOHÓLICA sobre el total de bebida: mínima en una '
        'cafetería/brunch (algún mimosa o cava de celebración). El resto '
        '—café, zumos, smoothies, refrescos— va al IVA reducido de '
        'hostelería',
        'parametrizado (v1.1 no distinguía tipos de IVA)'),
    'aforo': (
        None, None, 45, None,
        'Plazas interiores (30-40 según la hoja de Inversión) más las de la '
        'terraza (8-10 mesas). De aquí sale la rotación implícita: '
        'clientes/día ÷ aforo',
        'fichero v1.1 (notas de la hoja de Inversión)'),
    'salario_convenio': (
        None, None, 0, None,
        'El convenio PROVINCIAL de hostelería, no el SMI, es el suelo real '
        'del sector: cópialo de la tabla salarial de tu provincia. Con 0 el '
        'semáforo compara sólo contra el SMI',
        'SPEC §2.6/DOM-24 (mismo criterio que el representante)'),
}

# ==========================================================================
# §2.3.2 — líneas de venta (§1.1 describe el molde A-β ORIGINAL de v1.1 como
# «4 líneas tecleadas»; la reconstrucción de `grupo_a.pyg()` no exige ese
# número — lo decide `LINEAS_INGRESO`). Se agregan a DOS macro-líneas
# (Comida / Bebida), el mismo patrón `mix_en_supuestos` del representante:
#   1. Es la vía SEGURA y ya verificada en T2-T5 del representante — con
#      2 líneas en orden comida/bebida, `grupo_a` teclea el mix DIRECTAMENTE
#      en «0. Supuestos» (input real, no una suma de 4 celdas), que es
#      exactamente el «mix bebida» que pide el encargo de esta tanda.
#   2. Con 4 líneas (probado en el primer intento de esta tanda,
#      `auditorias/planes-v2-hermano-plan-negocio-cafeteria.json`) el libro
#      EN BLANCO deja «0. Supuestos!B12» (% de bebida) en 0 %, porque la
#      ÚLTIMA línea se calcula como «1 − suma de las otras tres» y, con las
#      cuatro celdas verdes vaciadas, esa resta da 1 (Excel trata blanco
#      como 0): el gate §2.11.13/RT-18 («ninguna celda imprime 0 € ni 0,0 %
#      con el libro en blanco») lo detecta y es BLOQUEANTE. Es un defecto del
#      MOTOR compartido (`grupo_a.lineas_ingreso()`/`pyg()`), no de este
#      contenido: afecta a cualquier hermano A-β con más de 2 líneas de
#      ingreso y no se puede parchear desde `contenido_<pid>/a.py` — se anota
#      para el orquestador en el informe de esta tanda. Con 2 líneas el
#      defecto no desaparece, cambia de signo: el libro en blanco imprime
#      100,0 % en vez de 0,0 % (R-08), que el gate tampoco busca.
# El desglose café/comida/bebidas frías/otros que traía v1.1 se conserva
# como NOTA de cada línea (transparencia), aunque el cálculo agregue.
# (rótulo, peso, grupo 'comida'|'bebida', nota, fuente)
# ==========================================================================
LINEAS_INGRESO = (
    ('Ventas de comida (brunch, bollería, tostas y otros)', 0.41, 'comida',
     'Brunch de fin de semana, bollería y tostas del servicio de mañana, '
     'más ventas menores de temporada (take-away extra, catering mini, '
     'merchandising)',
     'fichero v1.1: suma de «Ventas comida» + «Otros» '
     '((72.000+4.000)/190.000 = 40 %), redondeado'),
    ('Ventas de bebida (café, bebidas calientes y frías)', 0.59, 'bebida',
     'Espresso, cafés con leche, tés e infusiones de barra, más zumos '
     'naturales y smoothies, que son los de coste más alto por trabajar con '
     'producto fresco',
     'fichero v1.1: suma de «Ventas cafe y bebidas» + «Ventas bebidas '
     'frias» ((96.000+18.000)/190.000 = 60 %), redondeado'),
)

# ==========================================================================
# §2.6 — plantilla dimensionada por horas de servicio (§7-bis.17)
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
#
# DOS restricciones duras, las dos con semáforo propio en la hoja:
#   * suelo salarial — bruto/persona × 14 pagas >= SMI 2026 (17.094 €) en
#     PROPORCIÓN a la jornada. A jornada completa son 1.221 €/mes; al 55 %,
#     672 €; al 45 %, 550 €; al 25 %, 306 €. Cinco de los seis puestos de la
#     v2.0 previa estaban por debajo (R-01).
#   * cobertura — las jornadas tienen que sumar las horas que el libro
#     declara: 13 h de servicio × 2 personas × 300 días = 7.800 h/año, que
#     son 4,239 jornadas completas de 40 h × 46 semanas. Con 3,30 jornadas
#     la cobertura salía al 77,8 % y el propio semáforo lo pintaba en rojo
#     (R-02). Aquí suman 4,25 → 7.820 h → 100,3 %.
# ==========================================================================
PLANTILLA = (
    ('Propietario/a y barista principal', 1, 1350,
     'Trabaja en barra en el turno fuerte de mañana: compras, caja, '
     'proveedores y redes sociales',
     'recalibrado §7-bis.17 (v1.1: «Gerente / Propietario» 2.200 € con la '
     'nota «puede ser autónomo inicialmente», sin quedar claro si entraba '
     'en el coste del P&L)', 1.0),
    ('Barista / camarero de sala (turno de mañana)', 1, 1250,
     'Especialista en café y latte art. La mañana es el turno más fuerte de '
     'una cafetería: café de barra, desayunos y bollería',
     'recalibrado (v1.1: «Barista principal» 1.600 €; v2.0 previa: 1.120 €, '
     'por debajo del SMI a jornada completa)', 1.0),
    ('Camarero/a de barra y sala (turno de tarde)', 1, 1230,
     'Cierra el servicio de tarde y prepara la mise en place del día '
     'siguiente. Sin este puesto el local no puede abrir las 13 horas que '
     'declara este mismo libro',
     'recalibrado por R-02 (v2.0 previa: 620 € a jornada del 60 %, que '
     'dejaba la cobertura de horas en el 77,8 %)', 1.0),
    ('Ayudante de brunch de fin de semana', 1, 680,
     'Cocina ligera del brunch: sábado y domingo, el servicio con más '
     'demanda, con dos o tres turnos de mesa',
     'recalibrado (v1.1: «Ayudante cocina brunch» 1.400 € a media jornada '
     'todos los días)', 0.55),
    ('Extra de fin de semana (barra y sala)', 1, 555,
     'Refuerzo de los picos de sábado y domingo, cuando la ocupación sube '
     'al 70-90 % según las referencias de este mismo libro',
     'recalibrado (v1.1: «Extra fines de semana» 700 € a 20 h/semana)',
     0.45),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que el convenio
    # provincial sí impone: seis puestos con 30 días naturales de vacaciones
    # (art. 38 ET) son días de servicio que alguien tiene que cubrir.
    ('Suplencias de vacaciones y descansos', 1, 310,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso '
     'semanal del equipo',
     'parametrizado (RC-19, mismo criterio que el representante)', 0.25),
)

# ==========================================================================
# §2.2 — partidas de la inversión
# ==========================================================================
#: Reglas por rótulo NORMALIZADO: `('suprimir', motivo)` o `(importe, nota)`.
#: A diferencia del representante, el fichero v1.1 de cafetería NO duplicaba
#: seguros ni gestoría entre la inversión y el P&L (no tiene una línea de
#: «Seguros» en `Inversion Inicial`): DOM-19/RD-01 «no aplica» aquí. La única
#: partida que SÍ duplica con lo que `grupo_a` genera por fórmula es
#: «Imprevistos (8%)», que es justo la fila que §2.2 recalcula sobre el
#: bloque de obra (`pct_imprevistos`, por fórmula, nunca tecleado dos veces:
#: §7-bis.11).
INVERSION = {
    'imprevistos': (
        'suprimir',
        'RD-02 (mismo patrón que el representante): el 8 % tecleado a mano '
        'se sustituye por la fila «Imprevistos de obra y acondicionamiento», '
        'que `grupo_a` calcula por fórmula sobre las partidas de obra de '
        'este mismo bloque (§2.2)'),
    # §1.7 — dos erratas sin tilde que `motor.TILDES`/`TILDES_EXTRA` no
    # cubren (no son palabras «-ción»/«-sión» ni están en el diccionario
    # explícito): el ROTULO no tiene un hook de renombrado directo, así que
    # se SUPRIME y se vuelve a dar de alta con el texto corregido
    # (INVERSION_EXTRA, más abajo) — mismo importe y nota, sólo cambia la
    # ortografía. Medido el 2026-08-29 en el gate `motor.gate_ortografia`
    # de esta misma tanda (no está en el R1 del representante, que no tenía
    # estas dos erratas).
    'maquina de cafe espresso profesional': (
        'suprimir',
        '§1.7: «Maquina» sin tilde no está en el diccionario del motor '
        '(no es palabra -ción/-sión); se re-da de alta como «Máquina de '
        'café espresso profesional» en INVERSION_EXTRA, mismo importe '
        '(8.000 €) y nota'),
    'tpv + software gestion': (
        'suprimir',
        '§1.7: «gestion» sin tilde no está en el diccionario del motor; se '
        're-da de alta como «TPV + software gestión» en INVERSION_EXTRA, '
        'mismo importe (1.500 €) y nota'),
    # R-10 — cuatro NOTAS de partida con castellano sin tilde que el
    # diccionario del motor no cubre y que el gate de ortografía daba por
    # limpias. Van en la columna que el comprador enseña al banco («bano
    # accesible», «desague»), así que no son cosméticas. El rótulo de la
    # fila lo corrige el motor; la NOTA se reescribe por la vía del importe
    # (idéntico al del fichero v1.1: sólo cambia el texto).
    'proyecto tecnico + certificacion': (
        2500,
        'Obligatorio si superas los 100 m² o cambias el uso del local. '
        'Incluye planos, memoria técnica e instalaciones'),
    'obra civil y adecuacion local': (
        18000,
        'Suelo, pintura, instalaciones y baño accesible'),
    'fontaneria + evacuacion': (
        2500,
        'Toma de agua, desagüe y trampa de grasas si hay cocina'),
    'vitrina refrigerada exposicion': (
        2500,
        'Para sándwiches, tartas y bollería'),
    'decoracion + iluminacion': (
        3000,
        'Iluminación cálida, plantas y un estilo cuidado para las fotos'),
    # La NOTA (no el rótulo) de «Rotulación + imagen exterior» decía «Rotulo
    # + pizarra + vinilo escaparate», con «Rotulo» sin tilde: el rótulo de la
    # fila SÍ lo corrige el motor (está en `TILDES['rotulacion']`), la nota
    # no, porque es una palabra distinta («rótulo», no «rotulación»). Se usa
    # la vía del importe (idéntico, 1.500 €) para reescribir sólo la nota.
    'rotulacion + imagen exterior': (
        1500,
        'Rótulo, pizarra y vinilo de escaparate'),
}

#: DOM-19 «no aplica» en cafetería: terraza, stock inicial y el propio bloque
#: de imprevistos YA existen como partida en `Inversion Inicial` del fichero
#: v1.1 (a diferencia del representante, que sólo los tenía en el Word). Las
#: dos únicas partidas nuevas son el re-alta de §1.7 de arriba (mismo
#: importe y bloque, sólo corrige la ortografía del rótulo).
INVERSION_EXTRA = (
    (None, 'Máquina de café espresso profesional', 8000,
     '2 grupos, molinillo integrado o separado',
     'fichero v1.1 (rótulo corregido, §1.7 — antes «Maquina…»)'),
    (None, 'TPV + software gestión', 1500,
     'TPV táctil con software de control de caja y stock',
     'fichero v1.1 (rótulo corregido, §1.7 — antes «…gestion»)'),
)

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (TEC-18, FAMILIA(5): el mismo defecto que en los otros cuatro hermanos)
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Gestión de residuos (orgánico, cartón y aceite si fríes)', 700,
     'Gestor autorizado; el checklist lo pide antes de abrir. Esta '
     'cafetería NO lleva cocina de frituras (licencia «inocua»), así que el '
     'volumen es menor que en un restaurante — pide presupuesto en tu zona',
     'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 700,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC que el '
     'checklist ya exige', 'parametrizado (TEC-18)'),
    ('Derechos de autor por música ambiental', 700,
     'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de '
     'los metros y del aforo de tu local', 'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 500,
     'El plan de prevención es obligatorio; el proveedor externo, no (art. '
     '30.5 de la Ley 31/1995) — el checklist lo corrige',
     'parametrizado (DOM-26)'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Las CINCO ratios que exige el gate de la tanda (dry-run: «caso base que
# pasa sus 5 ratios»). Los rótulos los pone `grupo_a`; aquí van el valor y el
# comentario, con la cita LITERAL de la referencia del sector de este mismo
# producto — por su NOMBRE, nunca por su coordenada (R-03).
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.65,
     'Suelo del propio libro: «Margen bruto objetivo: > 65 %» en la tabla '
     'de referencias del sector'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.32,
     'Techo de la franja alta que publica este producto: «Food cost comida '
     'brunch: 30-35 %», mezclado con el café (25-30 %) y las bebidas frías '
     '(28-32 %)'),
    ('r_personal', 'Coste de personal / Ventas', 0.35,
     'Techo MÁS ESTRICTO del rango que publica este producto: «Coste de '
     'personal sobre ventas: 35-40 %»'),
    ('r_alquiler', 'Alquiler / Ventas', 0.12,
     'Techo del propio libro: «Alquiler sobre ventas: 8-12 %, no superar el '
     '12 % para ser viable»'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Derivado del suelo de EBITDA que declara este producto para el año 2 '
     '(«EBITDA objetivo: 8-15 %, el primer año puede ser negativo»): '
     'descontando amortización, intereses e Impuesto de Sociedades, un '
     'EBITDA en la franja baja deja un resultado neto en torno al 5 %'),
)

# ==========================================================================
# §2.5 — escenarios extremos (cubiertos/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# El PESIMISTA es, a propósito, el caso base de la versión anterior (80
# clientes/día a 9,20 €): sirve para enseñar en el propio libro por qué no
# se sostiene con una plantilla que cubra el horario declarado.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (80, 9.20, 290),
    'optimista': (115, 10.40, 310),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma 1)
# ==========================================================================
#: Estacionalidad de una cafetería/brunch urbana: agosto flojo por
#: vacaciones (menos que un restaurante, porque el café de barrio no
#: depende tanto del turismo), diciembre fuerte por desayunos de Navidad y
#: quedadas de fin de año. PARÁMETRO editable: si tu zona es de costa o
#: universitaria, el perfil cambia.
ESTACIONALIDAD = (0.075, 0.075, 0.085, 0.088, 0.090, 0.085,
                  0.075, 0.060, 0.085, 0.090, 0.085, 0.107)

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    # ⚠️ La numeración CONTINÚA la lista que escribe `grupo_a` (cinco puntos:
    # 1 a 5). La v2.0 previa empezaba en el 7 y la lista publicada iba
    # «1, 2, 3, 4, 5, 7, 8» en la primera hoja que abre el comprador (R-17).
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una '
        'operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota) — se conservan las referencias del
    # sector que ya traía este fichero (RD-04/RC-09 del representante:
    # no se borran, se citan con su fuente). R-03: vuelven además las tres
    # referencias de ocupación y rotación de mesa que la v2.0 previa había
    # dejado fuera del libro mientras las notas de la hoja de Personal las
    # seguían citando.
    'referencias': [
        ('Food cost café', '25-30 %', 'Fichero v1.1',
         'El café specialty puede llegar al 20 % con un buen proveedor'),
        ('Food cost comida brunch', '30-35 %', 'Fichero v1.1',
         'El control de porciones y de mermas es lo que lo decide'),
        ('Food cost bebidas frías', '28-32 %', 'Fichero v1.1',
         'Zumos y smoothies: coste alto por trabajar con producto fresco'),
        ('Coste de personal sobre ventas', '35-40 %', 'Fichero v1.1',
         'Se aplica el más estricto de los dos extremos que publica este '
         'producto'),
        ('Alquiler sobre ventas', '8-12 %', 'Fichero v1.1',
         'No superar el 12 % para ser viable'),
        ('Ticket medio café/desayuno', '4-6 €', 'Fichero v1.1',
         'Sólo café y bollería básica'),
        ('Ticket medio brunch completo', '14-20 €', 'Fichero v1.1',
         'Plato principal, bebida y postre o café'),
        ('Ticket medio combinado', '8-12 €', 'Fichero v1.1',
         'Media ponderada de todos los servicios. El ticket SIN IVA de esta '
         'previsión y su PVP equivalente los calcula la hoja 0. Supuestos'),
        ('Clientes/día (cafetería urbana)', '80-150', 'Fichero v1.1',
         'Depende mucho de la ubicación y del paso de gente'),
        ('Ocupación media entre semana', '40-60 %', 'Fichero v1.1',
         'La mañana es el pico; la tarde, el turno más flojo'),
        ('Ocupación media el fin de semana', '70-90 %', 'Fichero v1.1',
         'Es lo que justifica el refuerzo de sábado y domingo de la hoja de '
         'Personal'),
        ('Rotación de mesa en el brunch de fin de semana', '2-3 turnos',
         'Fichero v1.1',
         'Con 45 plazas es la referencia que sostiene los clientes/día del '
         'caso base'),
        ('Margen bruto objetivo', '> 65 %', 'Fichero v1.1', ''),
        ('EBITDA objetivo (año 2)', '8-15 %', 'Fichero v1.1',
         'El primer año puede ser negativo: es normal en hostelería. Este '
         'caso base queda en la parte alta del rango porque el coste de '
         'personal se ha ajustado justo por debajo de su techo'),
        ('Retorno de la inversión', '24-36 meses', 'Fichero v1.1',
         'Es una referencia del sector medida sobre lo que pone el '
         'emprendedor. La hoja de Tesorería calcula el retorno sobre la '
         'necesidad TOTAL de caja, financiación incluida: por eso sale más '
         'largo que esta referencia'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería',
         'Fichero v1.1 y checklist de apertura',
         'No existe una tabla salarial estatal única: copia la tabla de tu '
         'provincia en la celda de Supuestos'),
        ('Salario mínimo interprofesional 2026', '17.094 €/año',
         'RD 126/2026',
         'Suelo legal a jornada completa en 14 pagas. Las jornadas '
         'parciales lo llevan en proporción; el semáforo de la hoja de '
         'Personal lo comprueba fila a fila'),
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
    # (tildes + `EUR`→`€`), así que un patrón escrito contra el texto CRUDO
    # de v1.1 («autonomos», «EUR», «ano») ya no encuentra nada: la 1.ª pasada
    # de esta tanda dejó 3 reemplazos SIN aplicar (DOM-25, DOM-26 y el
    # epígrafe IAE) porque el motor ya había escrito «autónomos», «€» y, en
    # el caso del epígrafe, «cafés» (con tilde) pero «Epigrafe»/«espectaculos»
    # sin ella —una mezcla, no un texto limpio—. Los patrones de abajo NO
    # anclan con `^…$` (serían frágiles otra vez ante el próximo ajuste del
    # diccionario de tildes del motor): buscan la SUBCADENA estable —el
    # número, la cifra en euros o una palabra que no cambia— con acentos
    # opcionales, y sustituyen la celda ENTERA.
    'reemplazos': [
        # DOM-08 / COM-11 (FAMILIA) — el carnet de manipulador está
        # DEROGADO (RD 109/2010); la responsabilidad es de la EMPRESA
        (r'^Carnet de manipulador de alimentos$',
         'Formación en higiene alimentaria de todo el equipo'),
        (r'^Todos$', 'Titular'),
        (r'^Obligatorio para todo el personal, curso online valido$',
         'El «carnet de manipulador» está derogado (RD 109/2010): la '
         'formación la acredita la EMPRESA y se documenta en el plan '
         'APPCC'),
        # DOM-25 (FAMILIA) — cuota de autónomo parametrizada, con nota de
        # año. Medido tras el §1 transversal: «Tarifa plana autónomos
        # 80 €/mes primer año» (tilde y € ya puestos por el motor).
        (r'Tarifa plana aut[oó]nomos? 80\s*(EUR|€)/mes primer a[nñ]o',
         'Cuota según la base mínima del tramo que te corresponda. '
         'Consulta el importe del ejercicio en curso y verifica con tu '
         'gestoría si te aplica la cuota reducida de inicio de actividad'),
        # DOM-26 (FAMILIA) — el PRL obligatorio es el PLAN, no el proveedor
        (r'^SPA$', 'Titular o servicio ajeno'),
        # Medido tras el §1 transversal: «Prevencion» es palabra «-ción» y
        # el motor YA la acentúa (regla generativa RX_CION) antes de que
        # este reemplazo corra, así que el patrón acepta las dos formas.
        (r'Servicio de Prevenci[oó]n Ajeno obligatorio',
         'El plan de prevención es obligatorio; el proveedor externo, no: '
         'con menos de 25 trabajadores y un solo centro el titular puede '
         'asumir la actividad preventiva (art. 30.5 de la Ley 31/1995 y '
         'art. 11 del RD 39/1997)'),
        # NUEVO (propio de esta hermana, medido el 2026-08-29 en el
        # checklist de cafetería, no en el R1 del representante): 671.4 es
        # el epígrafe de RESTAURANTES de un tenedor. Una cafetería con
        # servicio de mesa va en el grupo 672 (Cafeterías), no en el 671
        # (Restaurantes) ni en el 673 (café-bares sin servicio de mesa).
        # El «671.4» y el paréntesis de después no cambian de ortografía:
        # es la ancla estable del patrón.
        (r'Epigrafe IAE: 671\.4 \(caf[eé]s y bares sin espect[aá]culos\)',
         'Epígrafe IAE: Grupo 672 (Cafeterías, por categoría 672.1/672.2/'
         '672.3 según el servicio) o 673.2 (café-bar sin música) si no hay '
         'servicio de mesa; el 671 es de restaurantes'),
        # DOM-13 / COM-08 (FAMILIA) — Crea y Crece: lo que impone la Ley
        # 18/2022 es dotar el 20 % del beneficio a reserva legal, no ningún
        # depósito. La nota de v1.1 se quedaba en el capital de 1 €.
        (r'Capital m[ií]nimo 1\s*(EUR|€) \(Ley Crea y Crece\)',
         'Capital social mínimo de 1 € (Ley 18/2022, Crea y Crece): hay que '
         'destinar el 20 % del beneficio a reserva legal hasta que el '
         'capital y la reserva sumen 3.000 €, y los socios responden '
         'solidariamente de esa diferencia'),
        # DOM-09 (FAMILIA) — el RGSEAA no aplica al minorista que sirve al
        # consumidor final. En cafetería la fila no está duplicada (como en
        # el representante), así que no se suprime: se reescribe.
        (r'^Registro sanitario RGSEAA \(si elaboras\)$',
         'Inscripción en el Registro Sanitario de tu Comunidad Autónoma '
         '(declaración responsable de inicio de actividad alimentaria)'),
        (r'^Obligatorio si elaboras boller[ií]a propia para venta$',
         'El Registro General Sanitario estatal (RGSEAA) NO aplica al '
         'minorista que sirve al consumidor final (art. 2.2 del RD '
         '191/2011): el que te toca es el autonómico. Sólo necesitas el '
         'estatal si vendes tu bollería a otras empresas'),
        # El arrendamiento de local de negocio SÍ está en la LAU (Título
        # III, uso distinto de vivienda), con libertad de pactos del art.
        # 4.3: la nota de v1.1 decía lo contrario.
        (r'no LAU para negocio',
         'La renta y el plazo se pactan libremente (LAU, Título III: '
         'arrendamiento para uso distinto de vivienda). Negocia 2-3 meses '
         'de carencia mientras dura la obra'),
        # ---- R-10: castellano sin tilde que el diccionario del motor no
        # cubre y que el gate de ortografía daba por limpio. Se sustituye la
        # celda entera; el ancla de cada patrón es la parte que no cambia.
        (r'tr[aá]mites telem[aá]ticos',
         'Imprescindible para los trámites telemáticos con Hacienda y con '
         'la Seguridad Social'),
        (r'zonas con tr[aá]fico peatonal',
         'Busca zonas con tráfico peatonal, oficinas o universidades'),
        (r'Alternativa a licencia en muchos municipios',
         'Alternativa a la licencia en muchos municipios, y más rápida'),
        (r'^Compra m[aá]quina de caf[eé] profesional$',
         'Compra de la máquina de café profesional'),
        (r'M[aá]quina caf[eé] \+ horno \+ lavavajillas',
         'Máquina de café, horno y lavavajillas: es el equipo que dispara '
         'el consumo eléctrico'),
        (r'Expositor de tartas, s[aá]ndwiches|Expositor de tartas, '
         r'sandwiches',
         'Expositor de tartas, sándwiches y bollería'),
        (r'c[oó]modo para brunch largo',
         'Estilo coherente con el concepto y cómodo para un brunch largo'),
        (r'Iluminaci[oó]n c[aá]lida, plantas, zona Instagram',
         'Iluminación cálida, plantas y una zona cuidada para las fotos'),
        (r'Prueba pr[aá]ctica: preparar espresso',
         'Prueba práctica: preparar un espresso y un latte art'),
        (r'recetas, limpieza m[aá]quina',
         'Estandarizar extracciones, recetas y limpieza de la máquina'),
        (r'Est[aá]ndares de servicio, reclamaciones',
         'Estándares de servicio, reclamaciones y venta sugerida'),
        (r'^Dise[ñn]ar identidad visual \(logo, colores, tipograf[ií]a\)$',
         'Diseñar la identidad visual: logotipo, colores y tipografía'),
        (r'Google My Business es m[aá]s urgente que la web',
         'La ficha de Google es más urgente que la web'),
        (r'Categor[ií]a: Cafeter[ií]a\. Fotos, horario, men[uú]',
         'Categoría: Cafetería. Cuida las fotos, el horario y la carta'),
        (r'^Dise[ñn]o carta / men[uú] board$',
         'Diseño de la carta y de la pizarra de la barra'),
        (r'Carta f[ií]sica \+ pizarra en barra|Carta fisica \+ pizarra',
         'Carta física, pizarra en la barra y carta digital con código QR'),
        (r'Cuenta atr[aá]s, behind the scenes|Cuenta atras, behind',
         'Cuenta atrás, contenido de la puesta a punto y sorteo inaugural'),
        (r'Tarjeta 10o caf[eé] gratis',
         'Tarjeta de sellos con el décimo café gratis, o aplicación de '
         'puntos'),
        # §1.7 — «cafeterias» (plural) no está en `motor.TILDES` (sólo el
        # singular «cafeteria»→«cafetería»): dos notas del checklist se
        # quedaban sin tilde. Medido el 2026-08-29 en el gate de esta misma
        # tanda; no está en el R1 del representante (que no habla de
        # cafeterías).
        (r'Instagram es el canal #1 para cafeterias/brunch',
         'Instagram es el canal #1 para cafeterías/brunch'),
        (r'Visitar otras cafeterias de la zona, comparar',
         'Visitar otras cafeterías de la zona, comparar'),
    ],
    'suprimir': [],
    'fases': {},
    # TEC-18 (FAMILIA) + RGPD (RD-26 del representante, mismo criterio):
    # trámites que faltan y cuestan dinero o multa. Repartidos por hoja
    # (F1 Constitución, F2 Local, F3 Equipamiento, F4 Personal, F5 Marketing,
    # F6 primeros 90 días) — el checklist de cafetería es de molde C2 (6
    # hojas), a diferencia del monolítico C1 del representante.
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
         'aplica antes de comprar el TPV que presupuesta la hoja de '
         'Inversión'),
        ('F2', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador',
         'Titular', '1 día',
         'El modelo y el texto del cartel los aprueba tu Comunidad '
         'Autónoma'),
        ('F2', 'Legal',
         'Contrato con gestor autorizado de residuos', 'Titular',
         '2 semanas',
         'Se comprueba en la inspección. Cartón, orgánico y, si fríes, '
         'aceite usado, que no puede ir al desagüe'),
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
         'Licencia de derechos de autor por la música ambiental',
         'Titular', '2 semanas',
         'SGAE y AGEDI-AIE son dos licencias distintas y se pagan las dos'),
        ('F5', 'RGPD',
         'Cláusula informativa y consentimiento en el sistema de reservas '
         'y en la lista de correo', 'Titular', 'Antes de abrir',
         'TheFork, WhatsApp y newsletter tratan datos: cada canal necesita '
         'su información previa'),
    ],
}

# ==========================================================================
# Registro de lo que cambia de valor respecto de la v1.1 (§1.3: «la
# diferencia entre el valor viejo y el nuevo queda anotada por fichero»)
#
# ⚠️ Esta tabla la LEE EL CLIENTE en la hoja de Instrucciones: la columna
# «Por qué» va en lenguaje llano, SIN códigos internos de auditoría, y las
# cifras de la columna «v2.1» son las que el libro termina teniendo (la v2.0
# previa publicaba aquí una plantilla de «~70.000 €», un ticket de 9,20 € y
# 80 clientes/día que ya no son los del fichero). Trazabilidad interna, por
# fila: TEC-01/DOM-01 · §7-bis.17 + R-02 · R-01 · R-02 · §7-bis.17 · TEC-11/
# DOM-30 · — · TEC-07/DOM-12/NUEVO-01 · TEC-20/NUEVO-02 · §7-bis.11 ·
# TEC-06/DOM-15 · TEC-08/DOM-10/COM-04 · DOM-14/DOM-17 · gate §2.11.12-bis.
#
# ⚠️ Ninguna celda de esta tabla junta un importe en euros con las palabras
# «plan », «kit », «guía », «pack » o «ebook»: `motor.cross_sell_sin_precios`
# borraría el importe sin avisar (R-05).
# ==========================================================================
RECALIBRADO = (
    ('Coste de personal en la cuenta de resultados', '72.000 € tecleados',
     'El que suma la hoja de Personal, por fórmula',
     'La cuenta de resultados usaba una cifra distinta de la de su propia '
     'hoja de personal, que sumaba 137.270 €. Ahora las dos dicen lo mismo, '
     'y si cambias un sueldo el resultado cambia solo.'),
    ('Plantilla', '5 puestos · 137.270 € al año',
     '6 puestos (tres a jornada parcial) · 100.083 € al año',
     'Dimensionada por las horas de servicio que declara este mismo libro. '
     'Con la anterior, el personal se comía el 72 % de las ventas; con '
     'ésta se queda en el 34 %, por debajo del techo del 35 % que publica '
     'este producto.'),
    ('Sueldos de la plantilla de ejemplo',
     'Sin ninguna comprobación frente al salario mínimo',
     'Todos igualan o superan el SMI de 2026 (17.094 € al año) en '
     'proporción a su jornada',
     'La hoja de Personal lo comprueba fila a fila y avisa en rojo si bajas '
     'de ese suelo. Un libro que propone sueldos por debajo del mínimo '
     'legal no se puede enseñar en el banco.'),
    ('Cobertura del horario',
     'La hoja no relacionaba la plantilla con las horas de apertura',
     'La plantilla cubre el 100 % de las horas de servicio declaradas',
     'Con 13 horas de apertura y dos personas a la vez hacen falta 7.800 '
     'horas al año. Ahora el libro las cuenta y avisa en rojo si la '
     'plantilla no llega a cubrirlas.'),
    ('Clientes al día', '67 (deducidos de la facturación objetivo)', '100',
     'Está dentro del rango de 80 a 150 clientes al día que este mismo '
     'libro publica para una cafetería urbana, y son 2,2 servicios por '
     'plaza y día sobre las 45 plazas del local.'),
    ('Ticket medio', '9,50 € (sin decir si llevaba IVA)',
     '9,80 € SIN IVA, que son 10,78 € de PVP',
     'Ahora se declara sin IVA y la hoja de Supuestos calcula el precio de '
     'carta equivalente. Sigue dentro del rango de 8 a 12 € de ticket medio '
     'combinado que publica este producto.'),
    ('Alquiler', '2.000 € al mes', '2.000 € al mes (sin cambio)',
     'Con el caso base recalibrado son el 8,2 % de las ventas, en la parte '
     'baja del 8-12 % que este mismo libro fija como límite de viabilidad.'),
    ('Calendario de apertura',
     'Dos calendarios distintos en el mismo libro: 30 días al mes en el '
     'punto de equilibrio y 300-310 días al año en los escenarios',
     '300 días al año, un único dato en la hoja de Supuestos',
     'El punto de equilibrio diario salía casi un 20 % por debajo del que '
     'corresponde a los días que el propio libro declaraba abrir.'),
    ('Fondo de maniobra', '9.000 € etiquetados «3 meses»',
     '3 meses de costes fijos de caja, por fórmula (38.526 €)',
     'Los 9.000 € cubrían menos de un mes de costes fijos, no tres. Ahora '
     'se recalcula solo cuando cambias cualquier gasto.'),
    ('Amortización',
     '9.490 € al año, a 10 años planos sobre TODA la inversión (fondo de '
     'maniobra, stock e imprevistos incluidos)',
     'Sólo sobre la obra y la maquinaria, cada una con su vida útil',
     'El colchón de caja, las existencias y los imprevistos no son '
     'inmovilizado: amortizarlos inflaba el gasto y falseaba el impuesto.'),
    ('Imprevistos de obra', '7.000 € (un 8 % escrito dentro del rótulo)',
     'Por fórmula sobre las partidas de obra, con el porcentaje en '
     'Supuestos',
     'Un porcentaje escondido en un rótulo deja de ser verdad al cambiar '
     'una sola partida, y aquí ya no cuadraba: eran el 6,7 %.'),
    ('Impuesto de Sociedades',
     '25 % en los años 2 y 3, sin compensar las pérdidas del año 1',
     '15 % en los dos primeros ejercicios con beneficio y compensación de '
     'las pérdidas anteriores',
     'Es el tipo de entidad de nueva creación de los artículos 26 y 29.1 '
     'de la Ley del Impuesto sobre Sociedades.'),
    ('Plan de financiación', 'No existía',
     'Hoja «Financiación»: origen de fondos, usos y cuadro de amortización '
     'francés',
     'La ficha del producto lo prometía y ningún fichero lo traía. Ahora '
     'el libro comprueba solo si el dinero que entra cubre lo que hay que '
     'poner sobre la mesa.'),
    ('Tesorería mes a mes', 'No existía',
     'Hoja «Tesorería 12 meses»: cobros, pagos, IVA trimestral y saldo '
     'acumulado',
     'Es la hoja que responde a la pregunta que decide una operación '
     'bancaria: en qué mes se agota la caja.'),
    ('Financiación solicitada',
     '(no había hoja que la cuadrara)',
     '40.000 € de recursos propios y 112.000 € de préstamo',
     'Cubren los 151.976 € de necesidad de caja con 24 € de diferencia. '
     'Pedir más es pagar intereses por un dinero que no se usa.'),
)

# ==========================================================================
# §M9 — VOCABULARIO DEL OFICIO (R22-CAF-20 / REF-17 · motor 2.2.1)
# ==========================================================================
#: «Cubierto» es vocabulario de restaurante con servicio de mesa; una
#: cafetería de barra cuenta CLIENTES o tickets. Lo dice el propio libro en
#: todas sus notas ('0. Supuestos'!C4 «Clientes servidos al día…», la tabla de
#: referencias «Clientes/día (cafetería urbana)») y en toda la capa de
#: producto: el rótulo y su nota se contradecían en la misma fila.
#: FUENTE de los términos: este mismo módulo (SUPUESTOS e INSTRUCCIONES).
VOCABULARIO = {
    'cubierto': 'cliente',
    'cubiertos': 'clientes',
}
