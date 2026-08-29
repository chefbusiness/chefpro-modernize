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
de la familia) y reparte el total entre las **4 líneas de venta** propias de
una cafetería/brunch por su peso (§2.3.2).

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

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01, medido en el censo de
familia del 2026-08-29)
------------------------------------------------------------------------
El defecto que hunde los cinco planes de línea A es el mismo en los cinco: el
P&L imputa un coste de personal que NO es el de su propia hoja `Personal`.
Medido en `plan-financiero-cafeteria-brunch.xlsx` v1.1: `'PyG 3 Anos'!B23` =
72.000 € mientras `'Personal'!E10` suma **137.270 €** — la propia celda
`Personal!F10` lo escribe: «~72% sobre ventas previstas», mientras el P&L
imprime 37,9 %. Con la cifra real de personal, el coste laboral es el
**72,2 %** de las ventas (190.000 €), muy por encima del techo 35-40 % que
publica `Instrucciones!B17` del mismo libro. El plan es inviable con sus
propios datos, igual que sus cuatro hermanos.

Lo que se ha hecho, y por qué se puede defender ante un banco:

1. **La plantilla estaba sobredimensionada para lo que paga el negocio.** El
   fichero v1.1 tenía 5 puestos (incluido un «Gerente / Propietario» a jornada
   completa con nota «Puede ser autónomo inicialmente», es decir, un coste que
   ni siquiera estaba claro que fuera del P&L) sumando 137.270 €/año. Se
   redimensiona a **6 puestos por horas de servicio**, con el propietario
   trabajando en barra (no como gerente puro) y el resto del equipo escalado
   por franja horaria: mañana fuerte (café + desayunos), tarde floja, y
   refuerzo de findes para el brunch, que es el propio patrón que describe
   `Instrucciones!B23` («Rotación mesa (brunch fin de semana): 2-3 turnos»)
   y `Instrucciones!B27-B28` («Ocupación media semana: 40-60 % / fin de
   semana: 70-90 %»).
2. **Los cubiertos suben de los 67 «objetivo» del fichero (una cifra
   derivada, no un input) a 80/día**, dentro del rango «80-150» que el propio
   libro publica en `Instrucciones!B22` para «cafetería urbana» — en el
   extremo bajo del rango, conservador para un año 1.
3. **El ticket pasa a declararse SIN IVA** (TEC-11, DOM-30, igual que en el
   representante). 9,20 € sin IVA equivalen a ~10,10 € de PVP con el mix de
   este plan, dentro del rango «8-12 €» de `Instrucciones!B21` («Ticket medio
   combinado»).
4. **El calendario se unifica a UNO solo** (`NUEVO-03`): 300 días/año, el
   mismo que ya declaraba `Escenarios!C7` del fichero v1.1 — se elimina el
   «asumiendo 30 días de apertura» (mensual) que traía `Punto Equilibrio`.
5. **Aparecen los costes fijos que el checklist obliga a contratar y que el
   plan no tenía** (TEC-18, igual que en los otros cuatro hermanos): gestión
   de residuos, DDD, derechos de autor por música ambiental y PRL. Todos en
   celda verde con nota de «pide presupuesto en tu zona».

Resultado del caso base (verificado con `data_only` tras `inject_cache.py`,
ver informe de la tanda): coste de personal ~31,7 % (techo 35 %), alquiler
~10,9 % (techo 12 % — `Instrucciones!B18`), coste de mercancía ~29,6 %
(dentro de 25-35 % — `Instrucciones!B14-B16`), margen bruto ~68 % (suelo 65 %
— `Instrucciones!B24`) y resultado neto positivo, dentro de lo razonable
frente al EBITDA objetivo del año 2 (8-15 %, `Instrucciones!B25`, que la
propia hoja admite negativo en el año 1 — no hace falta forzarlo aquí porque
el caso base YA es positivo). **El plan no se suspende a sí mismo.**
"""

CONCEPTO = 'Cafetería / Brunch'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato = se queda el que trae `grupo_a`.
# ==========================================================================
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 80, None,
        'Clientes servidos al día de media del año, contando café de barra y '
        'brunch de mesa. Extremo BAJO del rango «80-150» que este mismo '
        'libro publica para «cafetería urbana» (Instrucciones): conservador '
        'para un año 1',
        'recalibrado §7-bis.17 (v1.1: 67, una cifra DERIVADA de la '
        'facturación objetivo, no un input real)'),
    'ticket_medio': (
        None, None, 9.20, None,
        'SIN IVA. Con el mix de este plan equivale a ~10,10 € de PVP, dentro '
        'del rango 8-12 € que declara «Instrucciones!B21» (Ticket medio '
        'combinado) de este mismo libro',
        'recalibrado por TEC-11/DOM-30 (v1.1: 9,50 € sin declarar si '
        'llevaba IVA)'),
    'dias_apertura': (
        None, None, 300, None,
        'El MISMO dato lo usan el P&L, el punto de equilibrio y los '
        'escenarios: el fichero v1.1 tenía DOS calendarios distintos '
        '(Punto Equilibrio: 30 días/mes; Escenarios: 300-310 días/año)',
        'fichero v1.1 (Escenarios!C7) — fija NUEVO-03'),
    'crec_a2': (None, None, 0.10, None,
                'Segundo año con la clientela de barrio ya fidelizada',
                'parametrizado'),
    'crec_a3': (None, None, 0.07, None,
                'Tercer año, cerca del techo de aforo en las horas punta',
                'parametrizado'),
    'coste_comida': (
        None, None, 0.32, None,
        'Food cost de comida (brunch, bollería, tostas): dentro del '
        '30-35 % que declara «Instrucciones!B15» de este mismo libro',
        'fichero v1.1 (Instrucciones!B15: «Food cost comida brunch: '
        '30-35%»)'),
    'coste_bebida': (
        None, None, 0.28, None,
        'Coste de café y bebidas (calientes y frías) sobre sus propias '
        'ventas: media ponderada entre el 25-30 % del café '
        '(Instrucciones!B14) y el 28-32 % de las bebidas frías '
        '(Instrucciones!B16)',
        'fichero v1.1 (Instrucciones!B14 y B16)'),
    'pct_consumibles': (
        None, None, 0.015, None,
        'Servilletas, papel, vasos de llevar y productos de limpieza de '
        'barra',
        'parametrizado (v1.1: «Packaging take-away» 3.000 € fijos, ~1,6 % '
        'de sus ventas — se convierte en variable, §2.3 RT-04/05)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: el checklist de este plan lo marca como tarea '
        'del mes 2-3 («Implementar delivery si hay demanda»), no del día 1. '
        'Súbelo al peso real del canal cuando lo actives',
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
        'parametrizado (el plan v1.1 no lo contemplaba)'),
    'alquiler_mes': (
        None, None, 2000, None,
        'Local de cafetería/brunch de 30-40 plazas interior + terraza. '
        '10,9 % de las ventas del caso base, dentro del techo de 12 % que '
        'fija «Instrucciones!B18» de este mismo libro',
        'fichero v1.1 (24.000 €/año ÷ 12)'),
    'fianza_meses': (None, None, 3, None,
                     'Tres meses de renta, como en el contrato tipo de local '
                     'de negocio', 'parametrizado (v1.1 no lo declaraba)'),
    'suministros_mes': (
        None, None, 600, None,
        'Luz, agua y gas de una barra de café + horno de brunch: pide el '
        'histórico del local antes de firmar',
        'fichero v1.1 (7.200 €/año ÷ 12)'),
    'seguros_ano': (None, None, 1800, None,
                    'Responsabilidad civil (mínimo 300.000 € — checklist F2) '
                    '+ multirriesgo del local',
                    'fichero v1.1'),
    'pct_varios': (None, None, 0.02, None,
                   'Colchón de gasto corriente no presupuestado',
                   'parametrizado (v1.1 no tenía esta línea separada)'),
    'recursos_propios': (
        None, None, 40000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja de este plan',
        'parametrizado'),
    'prestamo': (
        None, None, 114000, None,
        'Principal solicitado. La hoja de Financiación comprueba que origen '
        'y usos cuadran con la necesidad de caja calculada en la hoja 1',
        'parametrizado (recursos propios + préstamo = 154.000 €; se ajustó '
        'de un primer intento de 100.000 € porque la hoja de Financiación '
        'marcaba un déficit de 13.447,80 € frente a la necesidad de caja '
        'real del caso base)'),
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
        'Mínimo que exige este mismo libro (Instrucciones): un colchón por '
        'debajo de 3 meses no cubre un bache de temporada baja',
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
        'Plazas interiores (30-40, Inversión!C20) + terraza (8-10 mesas, '
        'Inversión!C22). De aquí sale la rotación implícita: cubiertos/día '
        '÷ aforo',
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
#      cuatro celdas verdes vaciadas, esa resta dan 1 (Excel trata blanco
#      como 0): el gate §2.11.13/RT-18 («ninguna celda imprime 0 € ni 0,0 %
#      con el libro en blanco») lo detecta y es BLOQUEANTE. Es un defecto del
#      MOTOR compartido (`grupo_a.lineas_ingreso()`/`pyg()`), no de este
#      contenido: afecta a cualquier hermano A-β con más de 2 líneas de
#      ingreso y no se puede parchear desde `contenido_<pid>/a.py` — se anota
#      para el orquestador en el informe de esta tanda.
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
     'naturales y smoothies (coste alto por producto fresco, '
     'Instrucciones!B16)',
     'fichero v1.1: suma de «Ventas cafe y bebidas» + «Ventas bebidas '
     'frias» ((96.000+18.000)/190.000 = 60 %), redondeado'),
)

# ==========================================================================
# §2.6 — plantilla redimensionada por horas de servicio (§7-bis.17)
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
# ==========================================================================
PLANTILLA = (
    ('Propietario/a y barista principal', 1, 1250,
     'Trabaja en barra en el turno fuerte de mañana: compras, caja, '
     'proveedores y RRSS',
     'recalibrado §7-bis.17 (v1.1: «Gerente / Propietario» 2.200 € con la '
     'nota «puede ser autónomo inicialmente», sin quedar claro si entraba '
     'en el coste del P&L)', 1.0),
    ('Barista / camarero de sala (turno de mañana)', 1, 1120,
     'Especialista en café y latte art; el turno de mañana es el más '
     'fuerte en una cafetería (Instrucciones!B27: «mañana pico»)',
     'recalibrado (v1.1: «Barista principal» 1.600 €)', 1.0),
    ('Camarero/a de tarde (refuerzo)', 1, 620,
     'Cubre la tarde, más floja según el propio libro '
     '(Instrucciones!B27: «tarde más flojo»)',
     'recalibrado (v1.1: «Barista / Camarero 2» 1.450 € a jornada '
     'completa)', 0.60),
    ('Ayudante de brunch de fin de semana', 1, 420,
     'Cocina ligera del brunch: sábado y domingo, el servicio con más '
     'demanda (Instrucciones!B23: «brunch fin de semana: 2-3 turnos»)',
     'recalibrado (v1.1: «Ayudante cocina brunch» 1.400 € a media jornada '
     'todos los días)', 0.35),
    ('Extra de fin de semana (barra y sala)', 1, 270,
     'Refuerzo de los picos de sábado y domingo, cuando la ocupación sube '
     'al 70-90 % (Instrucciones!B28)',
     'recalibrado (v1.1: «Extra fines de semana» 700 € a 20 h/semana)',
     0.25),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que el convenio
    # provincial sí impone: seis puestos con 30 días naturales de vacaciones
    # (art. 38 ET) son días de servicio que alguien tiene que cubrir.
    ('Suplencias de vacaciones y descansos', 1, 80,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso '
     'semanal del equipo',
     'parametrizado (RC-19, mismo criterio que el representante)', 0.10),
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
     'TPV táctil + software con control de caja y stock',
     'fichero v1.1 (rótulo corregido, §1.7 — antes «…gestion»)'),
)

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (TEC-18, FAMILIA(5): el mismo defecto que en los otros cuatro hermanos)
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Gestión de residuos (orgánico, cartón y aceite si fríes)', 700,
     'Gestor autorizado; el checklist lo pide antes de abrir. Este plan NO '
     'incluye cocina de frituras (licencia «inocua»), así que el volumen es '
     'menor que en un restaurante — pide presupuesto en tu zona',
     'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 700,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC que el '
     'checklist ya exige (F4)', 'parametrizado (TEC-18)'),
    ('Derechos de autor por música ambiental', 700,
     'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de '
     'los metros y del aforo de tu local', 'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 500,
     'El plan de prevención es obligatorio; el proveedor externo, no (art. '
     '30.5 de la Ley 31/1995) — el checklist F4 lo corrige',
     'parametrizado (DOM-26)'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Las CINCO ratios que exige el gate de la tanda (dry-run: «caso base que
# pasa sus 5 ratios»). Los rótulos los pone `grupo_a`; aquí van el valor y el
# comentario, con la cita literal de `Instrucciones` de ESTE producto.
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.65,
     'Suelo del propio libro: «Instrucciones!B24 — Margen bruto objetivo: '
     '>65%»'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.32,
     'Techo de la franja alta que publica este producto: «Food cost comida '
     'brunch: 30-35%» (Instrucciones!B15), blend con café 25-30 % y '
     'bebidas frías 28-32 %'),
    ('r_personal', 'Coste de personal / Ventas', 0.35,
     'Techo MÁS ESTRICTO del rango que publica este producto: '
     '«Instrucciones!B17 — Coste personal / ventas: 35-40%»'),
    ('r_alquiler', 'Alquiler / Ventas', 0.12,
     'Techo del propio libro: «Instrucciones!B18 — Alquiler / ventas: '
     '8-12%, no superar 12% para ser viable»'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Derivado del suelo de EBITDA que declara este producto para el año 2 '
     '(«Instrucciones!B25 — EBITDA objetivo: 8-15%, primer año puede ser '
     'negativo»): descontando amortización, intereses e Impuesto de '
     'Sociedades, un EBITDA en la franja baja deja un resultado neto en '
     'torno al 5 %'),
)

# ==========================================================================
# §2.5 — escenarios extremos (cubiertos/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (60, 8.20, 290),
    'optimista': (105, 10.00, 310),
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
    'uso': [
        '7. La hoja «Tesorería 12 meses» responde la pregunta que decide una '
        'operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '8. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota) — se conservan las referencias del
    # sector que ya traía este fichero (RD-04/RC-09 del representante:
    # no se borran, se citan con su fuente).
    'referencias': [
        ('Food cost café', '25-30 %', 'Fichero v1.1',
         'Café specialty puede llegar al 20 % con buen proveedor'),
        ('Food cost comida brunch', '30-35 %', 'Fichero v1.1',
         'Control de porciones y mermas es clave'),
        ('Food cost bebidas frías', '28-32 %', 'Fichero v1.1',
         'Zumos y smoothies: coste alto por producto fresco'),
        ('Coste de personal sobre ventas', '35-40 %', 'Fichero v1.1',
         'Se aplica el más estricto de los dos extremos que publica este '
         'producto'),
        ('Alquiler sobre ventas', '8-12 %', 'Fichero v1.1',
         'No superar el 12 % para ser viable'),
        ('Ticket medio café/desayuno', '4-6 €', 'Fichero v1.1',
         'Sólo café + bollería básica'),
        ('Ticket medio brunch completo', '14-20 €', 'Fichero v1.1',
         'Plato principal + bebida + postre/café'),
        ('Ticket medio combinado', '8-12 €', 'Fichero v1.1',
         'Media ponderada de todos los servicios. El ticket SIN IVA de '
         'ESTE plan lo calcula la hoja 0. Supuestos'),
        ('Clientes/día (cafetería urbana)', '80-150', 'Fichero v1.1',
         'Depende mucho de la ubicación y el paso'),
        ('Margen bruto objetivo', '> 65 %', 'Fichero v1.1', ''),
        ('EBITDA objetivo (año 2)', '8-15 %', 'Fichero v1.1',
         'El primer año puede ser negativo: es normal en hostelería'),
        ('Retorno de la inversión', '24-36 meses', 'Fichero v1.1',
         'Las cafeterías retornan más rápido que los restaurantes por su '
         'menor inversión inicial'),
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
        # DOM-25 (FAMILIA) — cuota de autónomo parametrizada, con nota de año
        (r'^Tarifa plana autonomos 80 EUR/mes primer ano$',
         'Cuota según la base mínima del tramo que te corresponda. '
         'Consulta el importe del ejercicio en curso y verifica con tu '
         'gestoría si te aplica la cuota reducida de inicio de actividad'),
        # DOM-26 (FAMILIA) — el PRL obligatorio es el PLAN, no el proveedor
        (r'^SPA$', 'Titular o servicio ajeno'),
        (r'^Servicio de Prevencion Ajeno obligatorio$',
         'El plan de prevención es obligatorio; el proveedor externo, no: '
         'con menos de 25 trabajadores y un solo centro el titular puede '
         'asumir la actividad preventiva (art. 30.5 de la Ley 31/1995 y '
         'art. 11 del RD 39/1997)'),
        # NUEVO (propio de esta hermana, medido el 2026-08-29 en el
        # checklist de cafetería, no en el R1 del representante): 671.4 es
        # el epígrafe de RESTAURANTES de un tenedor. Una cafetería con
        # servicio de mesa va en el grupo 672 (Cafeterías), no en el 671
        # (Restaurantes) ni en el 673 (café-bares sin servicio de mesa).
        (r'^Epigrafe IAE: 671\.4 \(cafes y bares sin espectaculos\)$',
         'Epígrafe IAE: Grupo 672 (Cafeterías, por categoría 672.1/672.2/'
         '672.3 según el servicio) o 673.2 (café-bar sin música) si no hay '
         'servicio de mesa; el 671 es de restaurantes'),
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
# ==========================================================================
RECALIBRADO = (
    ('Coste de personal imputado al P&L', '72.000 €',
     'Sale de la hoja Personal, por fórmula',
     'TEC-01/DOM-01 (FAMILIA): el P&L usaba una cifra tecleada distinta de '
     'su propia hoja Personal (137.270 €); la propia Personal!F10 lo '
     'escribía: «~72% sobre ventas previstas»'),
    ('Plantilla', '5 puestos / 137.270 €',
     '6 puestos (dos a jornada parcial y suplencias) / ~70.000 €',
     '§7-bis.17: dimensionada por horas de servicio; con la plantilla '
     'anterior el coste laboral era el 72,2 % de las ventas'),
    ('Cubiertos/día', '67 (derivado de la facturación objetivo, no un '
     'input)', '80', 'Dentro del rango 80-150 que declara Instrucciones!B22 '
     'para «cafetería urbana»'),
    ('Ticket medio', '9,50 € (sin declarar IVA)', '9,20 € SIN IVA',
     'TEC-11/DOM-30: equivale a ~10,10 € de PVP, dentro del rango 8-12 € '
     'del propio libro (Instrucciones!B21)'),
    ('Calendario', 'Punto Equilibrio: 30 días/mes · Escenarios: 300-310 '
     'días/año (dos calendarios distintos)', '300 días/año, un único dato '
     'en Supuestos', 'NUEVO-03 (defecto propio de los cuatro hermanos '
     'A-β, no visto por el R1 del representante A-α)'),
    ('Fondo de maniobra', '9.000 € etiquetados «3 meses»',
     '3 × costes fijos de caja mensuales, por fórmula',
     'TEC-07/DOM-12/NUEVO-01: los 9.000 € cubrían 0,91 meses, la mitad de '
     'mal que el representante'),
    ('Amortización', '9.490 €/año a 10 años planos sobre TODO el '
     'inmovilizado (incluidos fondo de maniobra, stock e imprevistos)',
     'Base amortizable real (sólo obra y maquinaria) / vida útil por '
     'fórmula, por fórmula',
     'NUEVO-02: la base incluía circulante, que no es inmovilizado'),
    ('Imprevistos de obra', '7.000 € (8 % tecleado a mano sobre el total)',
     'Por fórmula sobre las partidas de obra del bloque, con el '
     'porcentaje en Supuestos',
     '§7-bis.11: ningún número vive dentro de una fórmula ni de un rótulo'),
    ('Impuesto de Sociedades', '25 % en los años 2 y 3, sin compensar la '
     'BIN del año 1', '15 % los dos primeros ejercicios con base positiva y '
     'compensación de bases negativas',
     'TEC-06/DOM-15 (FAMILIA): arts. 26 y 29.1 LIS'),
    ('Plan de financiación', 'inexistente (0 hojas)',
     'Hoja «Financiación»: usos y orígenes + cuadro de amortización '
     'francés',
     'TEC-08/DOM-10/COM-04 (FAMILIA 10/10): la landing lo promete en las '
     '10 líneas y ningún fichero lo tenía'),
    ('Tesorería mensual', 'inexistente (0 hojas)',
     'Hoja «Tesorería 12 meses»: cobros, pagos, IVA trimestral y saldo '
     'acumulado', 'DOM-14/DOM-17 (FAMILIA 10/10)'),
)
