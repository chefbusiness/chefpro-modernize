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

Se reconcilia a **300 días/año, un único calendario**, porque es el más
PRUDENTE de los dos que ya estaban y el que la propia cuenta de resultados
usaba de forma implícita: no se inventa ningún dato nuevo, sólo se elige uno
de los dos que el fichero ya traía.

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
2. **⚠️ El primer redimensionado se pasó de frenada y entregaba sueldos por
   debajo del SMI** (REF-01 de la refutación del 29-ago: `Personal!D5`
   1.150 €/mes y `D7` 1.050 €/mes a jornada COMPLETA, es decir 16.100 € y
   14.700 €/año frente a los 17.094 € del SMI; y `D11` 90 € con jornada del
   8 %). Dos de ellos eran ilegales y el propio libro los pintaba en ROJO.
   Además la cobertura de horas quedaba en ÁMBAR al 93,4 % (REF-07): la
   plantilla no llegaba a cubrir las 13 h de servicio × 2 personas × 300 días
   que el mismo libro declara. **Ninguna de las dos cosas se arregla bajando
   el listón**: los sueldos suben por encima del SMI en proporción a su
   jornada y las jornadas suben hasta cubrir el horario (Σ jornadas = 4,30
   sobre las 4,24 necesarias → cobertura 101 %). Eso deja el coste laboral en
   **108.368 €/año**, y ahí es donde el plan deja de cuadrar con 270.000 € de
   ventas: 108.368/270.000 = **40,1 %**, por encima del 32-38 % que publica
   `Instrucciones!B9`.
3. **Por eso el caso base sube de 50 a 56 clientes/día** (§7-bis.17, «se
   recalibra por los dos lados y dentro de rangos con fuente»). Son **1,24
   servicios por plaza y día** sobre las 45 plazas del propio plan, muy por
   debajo de la ocupación que describe su documento: «rotación de 1,8
   servicios por cubierto en almuerzo y 1,5 en cena» con ocupaciones del
   65 % y el 75 % (docx párrafo 27), que sobre 45 plazas darían más de 100
   clientes/día. El caso base se proyecta a la mitad de eso, a propósito.
   Facturación del año 1: **56 × 18 × 300 = 302.400 €**.
4. **El ticket NO se toca: sigue siendo 18 €, y ahora se declara SIN IVA**
   (TEC-11, DOM-30, igual que en el representante y en cafetería). Con el IVA
   de sala son 19,80 € de PVP, dentro del «15-22 €» que publica
   `Instrucciones!B11`. La subida de ingresos viene del volumen, no del
   precio.
5. **Aparecen los costes fijos que el checklist obliga a contratar y que el
   plan no tenía** (TEC-18, igual que en los otros cuatro hermanos): gestión
   de residuos (crítico aquí: plancha y freidora generan aceite usado y grasa
   de forma continua, así que el volumen es MAYOR que en una cafetería), DDD,
   derechos de autor por música ambiental (distinto de la licencia municipal
   de música que el checklist YA tenía en `F2!B10`) y PRL. Todos en celda
   verde con nota de «pide presupuesto en tu zona».
6. **La financiación se cuadra con la necesidad de caja** (RD-34, que tumbaba
   el dry-run con 11.197,55 € de exceso, un 6,44 % sobre los usos): 50.000 €
   de recursos propios + 129.000 € de préstamo = 179.000 € frente a los
   ~178.400 € de necesidad de caja. Los socios ponen el **28 %**, dentro del
   25-30 % que exige la nota de esa misma celda (REF-17, que medía 24,33 %).

Resultado del caso base (verificado con `data_only` tras `inject_cache.py`,
ver informe de la tanda): coste de personal **35,8 %** (techo 36 %, dentro
del rango 32-38 % de `Instrucciones!B9`), alquiler **9,9 %** (techo 12 % —
`Instrucciones!B10`), coste de mercancía **27,8 %** (dentro de 22-32 % según
la línea — `Instrucciones!B6-B8`, y coincide con el 28,1 % que el propio
fichero v1.1 ya declaraba en `'PyG 3 Años'!E17`), margen bruto **69,4 %**
(suelo 68 % — `Instrucciones!B17`) y resultado neto **~7 %** (suelo 5 %).
Cobertura de horas **101 %** y ningún sueldo por debajo del SMI en
proporción a su jornada. **El plan no se suspende a sí mismo.**
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
    # RD-34 / REF-01 / REF-07 — el caso base subió de 50 a 56 clientes/día
    # porque la plantilla que de verdad cubre el horario (13 h × 2 personas ×
    # 300 días) y respeta el SMI cuesta 108.368 €/año: con 270.000 € de
    # ventas eso era el 40,1 % del labour cost, por encima del 32-38 % que
    # publica el propio libro. Se recalibra por VOLUMEN, no por precio, y muy
    # por debajo de la ocupación que describe el documento del plan.
    'cubiertos_dia': (
        None, None, 56, None,
        'Clientes servidos al día de media del año, tapeo de barra y '
        'raciones de mesa incluidos. Son 1,24 servicios por plaza y día '
        'sobre el aforo de esta misma hoja; el documento de este plan '
        'describe rotaciones de 1,8 en el almuerzo y 1,5 en la cena con '
        'ocupaciones del 65 % y el 75 %, así que el caso base se proyecta '
        'muy por debajo, a propósito',
        "recalibrado §7-bis.17 (v1.1: 50, 'Punto Equilibrio'!B11)"),
    'ticket_medio': (
        None, None, 18.00, None,
        'SIN IVA. Es el mismo 18 € del fichero v1.1: declarar que es SIN IVA '
        'no cambia ningún número, sólo aclara qué era. Con el IVA de sala '
        'son 19,80 € de PVP —lo calcula la celda «PVP equivalente con IVA» '
        'de abajo—, dentro del rango 15-22 € «Ticket medio tapas bar» de '
        'Instrucciones!B11',
        "fichero v1.1 ('Punto Equilibrio'!B9, TEC-11/DOM-30)"),
    'dias_apertura': (
        None, None, 300, None,
        'El MISMO dato lo usan el P&L, el punto de equilibrio y los '
        'escenarios: el fichero v1.1 tenía DOS calendarios distintos '
        "(Escenarios!B7:D7: 310-320 días/año; 'PyG 3 Años'!B10 = 270.000 € "
        'está calculado con 300 días). Se elige 300 por ser el más prudente '
        'de los dos y el que la propia cuenta de resultados ya usaba, no un '
        'dato nuevo',
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
        'terraza. 9,9 % de las ventas del caso base, por debajo del techo de '
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
        'Colchón de gasto corriente no presupuestado. Es un coste VARIABLE: '
        'sube y baja con la facturación, así que no puede vivir entre los '
        'costes fijos; la v1.1 lo llevaba ahí como una fila de importe fijo',
        "fichero v1.1 ('PyG 3 Años'!B31 = 2.500 €/270.000 = 0,93 %, "
        'redondeado)'),
    # REF-17 — 45.000 € eran el 24,33 % de la necesidad de caja y la propia
    # nota de esta celda exige el 25-30 %. Con 50.000 € son el 28 %.
    'recursos_propios': (
        None, None, 50000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja de este plan. '
        'En el caso base son el 28 %',
        'recalibrado por REF-17 (v2.0 previa: 45.000 €, el 24,33 %)'),
    # RD-34 — el origen de fondos superaba a los usos en 11.197,55 € (6,44 %,
    # tope 5 %): son intereses que se pagan por un dinero que no se usa. La
    # cifra sale de la celda «Préstamo que ajustaría el origen a la
    # necesidad» de la hoja de Financiación, recalculada con la plantilla y
    # los ingresos definitivos.
    'prestamo': (
        None, None, 129000, None,
        'Principal solicitado. La hoja de Financiación comprueba que origen '
        'y usos cuadran con la necesidad de caja calculada en la hoja de '
        'Inversión, y trae una celda que calcula el importe exacto que los '
        'ajusta',
        'recalibrado por RD-34 (v2.0 previa: 140.000 €, que dejaban 11.197,55 € '
        'de exceso de financiación). Muy por encima de los 115.500 € que '
        'sumaba la v1.1 porque el fondo de maniobra real es mayor que el que '
        'dotaba el fichero original (NUEVO-01), y porque el IVA soportado de '
        'la inversión y los imprevistos de obra por fórmula suman a la '
        'necesidad de caja'),
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
    # REF-18 — la nota decía «plazas interiores (40-50) + terraza» y ponía
    # 45, que es imposible: si la terraza suma, 40-50 interiores ya agotan el
    # rango. El documento del plan se contradice a sí mismo (párrafo 25:
    # «capacidad TOTAL de 40 a 50 plazas»; párrafo 74: «cuarenta a cincuenta
    # plazas interiores MÁS terraza»); se toma el párrafo 25, que es el que
    # deja el número coherente con la celda, y la nota lo dice.
    'aforo': (
        None, None, 45, None,
        'Aforo TOTAL del local: sala, barra y terraza. El documento de este '
        'plan describe «una capacidad total de 40 a 50 plazas» para un local '
        'de 60-80 m² con terraza, y 45 es el punto medio. De aquí sale la '
        'rotación implícita: clientes/día ÷ aforo. Cuéntalo sobre el plano '
        'de tu local, no lo copies: si tu terraza es grande, el aforo sube y '
        'la rotación baja',
        'fichero v1.1 (docx párrafo 25: «capacidad total de 40 a 50 '
        'plazas»)'),
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
# ⚠️ DOS SEMÁFOROS mandan sobre esta tabla y hay que mirarlos a la vez
# (REF-01 y REF-07 de la refutación del 29-ago, que el dry-run daba por
# buenos porque sus gates sólo miran los 5 ratios del P&L):
#
#   * `Personal!D5:D11` se pinta ROJO si `bruto/personas × pagas <
#     MAX(SMI; convenio) × jornada`. Con 14 pagas y el SMI en
#     `'0. Supuestos'!B22` (17.094 €), el SUELO por fila es
#     **1.221 € × jornada**: 1.221 a jornada completa, 732,60 al 60 %,
#     549,45 al 45 %, 183,15 al 15 % y 122,10 al 10 %.
#   * `Personal!B25` (cobertura) se pinta VERDE sólo con ≥ 100 %:
#     `Σ jornadas × 40 h × 46 semanas ≥ horas_día × personas_franja × días`.
#     Con los valores que trae `grupo_a` (13 h × 2 personas × 300 días =
#     7.800 h) hace falta **Σ jornadas ≥ 4,24**. Aquí suman **4,30**.
#
# El coste que sale de las dos condiciones (108.368 €/año) es lo que obligó a
# subir los clientes/día a 56: por debajo de ~301.000 € de ventas, un equipo
# legal que cubra el horario no cabe en el techo del 36 % de labour cost.
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
PLANTILLA = (
    ('Propietario/a y encargado/a de sala', 1, 1380,
     'Gestiona compras, caja, proveedores y RRSS, y cubre barra/sala en el '
     'turno fuerte de tarde-noche',
     'recalibrado §7-bis.17 + REF-01 (v1.1: «Gerente / Propietario» 2.400 €, '
     'coste/año 44.828 €, jornada completa sin ninguna referencia de horas; '
     'v2.0 previa: 1.150 €, por DEBAJO del SMI a jornada completa)',
     1.0),
    ('Jefe de cocina', 1, 1480,
     'Diseña la carta de tapas, coordina la línea de cocina y controla el '
     'food cost semanal (checklist F6!B6). Es el puesto cualificado del '
     'equipo y el único claramente por encima del suelo del convenio',
     'recalibrado (v1.1: «Jefe de cocina / Cocinero principal» 2.000 €; '
     'v2.0 previa: 1.350 €)',
     1.0),
    ('Camarero/a de barra (turno fuerte)', 1, 1280,
     'Tiraje de cerveza, vermut y cócteles: el afterwork representa el '
     '25-30 % de la facturación de un gastrobar (docx párrafo 58)',
     'recalibrado por REF-01 (v1.1: «Camarero/a principal (barra)» 1.550 €; '
     'v2.0 previa: 1.050 €, por DEBAJO del SMI a jornada completa)', 1.0),
    ('Camarero/a de sala y terraza', 1, 790,
     'Cubre el servicio de mesa y terraza en el turno de tarde-noche, 24 '
     'horas semanales (Instrucciones!B15: «ocupación media semana 50-65 %»)',
     'recalibrado (v1.1: «Camarero/a sala» 1.450 € a jornada completa; v2.0 '
     'previa: 550 € al 45 %). Sube al 60 % para cerrar la cobertura de '
     'horas (REF-07)',
     0.60),
    ('Ayudante de cocina', 1, 565,
     'Mise en place, limpieza y apoyo en plancha/freidora en el turno '
     'fuerte, 18 horas semanales',
     'recalibrado (v1.1: «Ayudante cocina» 1.400 € a jornada completa; v2.0 '
     'previa: 400 € al 28 %). Sube al 45 % por la cobertura de horas '
     '(REF-07)',
     0.45),
    ('Extra de fin de semana (barra y sala)', 1, 195,
     'Refuerzo de los picos de viernes-sábado, cuando la ocupación sube al '
     '80-95 % (Instrucciones!B16). Seis horas semanales',
     'recalibrado (v1.1: «Extra fines de semana» 800 € a 20 h/semana; v2.0 '
     'previa: 200 €, un 9 % por encima de su suelo)',
     0.15),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que el convenio
    # provincial sí impone: siete puestos con 30 días naturales de
    # vacaciones (art. 38 ET) son días de servicio que alguien tiene que
    # cubrir.
    ('Suplencias de vacaciones y descansos', 1, 130,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso '
     'semanal del equipo',
     'parametrizado (RC-19, mismo criterio que el representante y '
     'cafetería). v2.0 previa: 90 € al 8 %, por debajo del SMI en '
     'proporción (REF-01)', 0.10),
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
    # §1.7 / REF-08 — el barrido léxico de la refutación encontró 22 palabras
    # sin tilde con el gate `ortografia` en 0; el motor ya arregló la mayoría
    # («urbanístico», «frío», «Fotógrafo», «cámaras», «Análisis»), pero
    # «bano» y «calida» siguen vivas en las NOTAS de estas dos partidas, que
    # el motor preserva tal cual del fichero original. Misma vía del importe
    # idéntico que se usa arriba para reescribir sólo la nota.
    'obra civil y adecuacion local': (
        22000,
        'Suelo, pintura, instalaciones, baño accesible y extracciones'),
    'decoracion + iluminacion ambiente': (
        4000,
        'Iluminación cálida, azulejos, madera y pizarras'),
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
#: Reescalados con el caso base de 56 clientes/día: el pesimista se queda un
#: 25 % por debajo (42) con el ticket en el suelo del rango del libro (16 € =
#: 17,60 € de PVP) y el optimista un 25 % por encima (70) con el ticket en el
#: techo (20 € = 22,00 € de PVP). Con esos valores el pesimista cierra el año
#: con la caja en positivo —gracias al fondo de maniobra de 3 meses—, aunque
#: dé pérdidas: es exactamente lo que un escenario pesimista tiene que
#: enseñar.
ESCENARIOS = {
    'pesimista': (42, 16.00, 300),
    'optimista': (70, 20.00, 300),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma 1)
# ==========================================================================
#: Estacionalidad de un tapas bar/gastrobar urbano con terraza y afterwork:
#: verano fuerte (terraza + turismo, docx párrafo 56: «España recibió más de
#: 85 millones de turistas»), diciembre fuerte por cenas y vermuts de
#: Navidad, enero flojo por la cuesta de enero. PARÁMETRO editable: si el
#: local no tiene terraza, el pico de verano se modera.
#: ⚠️ REF-03 — la serie anterior sumaba **1,020**, no 1: la fila se rotula
#: «Estacionalidad del mes (suma 100 %)», su nota lo repite y su semáforo la
#: pintaba en ROJO en el caso base. El P&L no se descuadraba porque la fila
#: de actividad normaliza dividiendo por la suma, pero el comprador veía un
#: rojo y una contradicción en la primera hoja que mira un banco. Se conserva
#: el PERFIL y se recorta hasta 1,000 exacto. Si alguien la retoca, que
#: compruebe la suma: el semáforo del motor tolera ±0,5 puntos (redondeo
#: binario), no un 2 % de más.
ESTACIONALIDAD = (0.064, 0.068, 0.078, 0.080, 0.086, 0.093,
                  0.098, 0.093, 0.083, 0.080, 0.077, 0.100)

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    # ⚠️ REF-11 — `grupo_a` emite los puntos 1 a 5 de esta lista y aquí se
    # CONTINÚA la numeración: estos textos arrancaban en «7.» y la lista
    # publicada saltaba del 5 al 7. El ordinal se escribe a mano dentro de la
    # cadena, así que hay que contar los que emite el motor antes de tocar
    # esto.
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una '
        'operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado; muy por encima '
        'de cero tampoco es gratis, porque se pagan intereses por un dinero '
        'que no se usa.',
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
         '2-3 tapas + 2 bebidas por persona. Va con IVA: el PVP equivalente '
         'de ESTE plan lo calcula la hoja «0. Supuestos»'),
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
        # REF-13 — esta referencia contradecía al propio modelo dos bloques
        # más arriba («Payback del proyecto» = más de 3 años). No se retira:
        # se explica por qué las dos cosas son ciertas, que es lo que un
        # comité de riesgos pregunta.
        ('Retorno de la inversión', '18-30 meses', 'Fichero v1.1',
         'Es la referencia del sector, medida sobre la inversión en obra y '
         'equipamiento. El «Payback del proyecto» del bloque de arriba sale '
         'más largo porque lo que hay que recuperar incluye además el fondo '
         'de maniobra de tres meses y el IVA de la inversión, que hay que '
         'adelantar. La cifra de ESTE plan es la de arriba'),
        ('Merma media', '3-5 %', 'Fichero v1.1',
         'Las tapas permiten aprovechar recortes: menor merma que en un '
         'restaurante de carta'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería',
         'Checklist de apertura, fase de personal',
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
        # ⚠️ REF-09 — el patrón llevaba un «de» que el fichero NO tiene
        # («Servicio Prevencion Ajeno obligatorio»), así que la regla no
        # casaba y la fila quedaba con el responsable ya corregido
        # («Titular o servicio ajeno») y la nota diciendo justo lo
        # contrario. Un reemplazo que no casa no genera ningún aviso: es un
        # fallo SILENCIOSO. El «de» va opcional.
        (r'Servicio (?:de )?Prevenci[oó]n Ajeno obligatorio',
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

        # ------------------------------------------------------------------
        # §1.7 / REF-08 — las 12 celdas del checklist que sobreviven al §1
        # transversal del motor con una palabra sin tilde. El gate
        # `ortografia` del dry-run devuelve 0 porque su diccionario cubre
        # las familias -ción/-sión y una lista cerrada, no el léxico suelto
        # («bano», «mas», «practica», «tipografia», «video», «genero»,
        # «ingenieria», «menu», «rotulo», «atras», «fisica», «telematico»).
        # Cuatro de ellas están en rótulos de columna, siempre visibles.
        # Cada reemplazo sustituye la celda ENTERA, así que el patrón va
        # anclado con ^…$ para no tocar ninguna otra.
        # ------------------------------------------------------------------
        (r'^Imprescindible para tr[aá]mites telematicos$',
         'Imprescindible para trámites telemáticos'),
        (r'^Tapas bar con cocina = actividad clasificada \(mas exigente\)$',
         'Tapas bar con cocina = actividad clasificada (más exigente)'),
        # M5 / R22-TAP-07 — los cuatro patrones de abajo dejaron de casar
        # cuando el §1 transversal del motor 2.2 empezó a acentuar la palabra
        # ANTES de que corriera `grupo_a.checklist()`. El motor los rescata
        # probando también contra el texto de partida; los patrones se
        # escriben además con el acento OPCIONAL para que casen contra las
        # dos grafías sin depender de ese rescate.
        (r'^Plancha, freidora, horno, salamandra, ba[ñn]o mar[ií]a$',
         'Plancha, freidora, horno, salamandra y baño maría'),
        (r'^Prueba practica: elaborar 3 tapas en 20 min$',
         'Prueba práctica: elaborar 3 tapas en 20 min'),
        (r'^Logo, colores, tipograf[ií]a, estilo visual$',
         'Logo, colores, tipografía y estilo visual'),
        (r'^Instagram para fotos tapas, TikTok para videos cocina$',
         'Instagram para fotos de tapas, TikTok para vídeos de cocina'),
        (r'^Carta f[ií]sica \+ pizarra tapas del d[ií]a \+ QR digital$',
         'Carta física + pizarra de tapas del día + QR digital'),
        (r'^Rotulo \+ pizarra exterior \+ vinilo$',
         'Rótulo + pizarra exterior + vinilo'),
        (r'^Behind the scenes, cuenta atr[aá]s, sorteo inaugural$',
         'Cocina a la vista, cuenta atrás y sorteo inaugural'),
        (r'^Pesar genero: carnes, pescado, embutidos$',
         'Pesar el género: carnes, pescado y embutidos'),
        (r'^An[aá]lisis tapas mas vendidas vs menos vendidas$',
         'Análisis de las tapas más vendidas frente a las menos vendidas'),
        (r'^Aplicar ingenieria de menu: Stars, Puzzles, Dogs$',
         'Aplicar ingeniería de menú: Stars, Puzzles, Dogs'),
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
# ⚠️ La columna «Por qué» la LEE EL CLIENTE en la hoja de Instrucciones:
# lenguaje llano, sin códigos internos de auditoría (TEC-/DOM-/RC-/RD-/
# NUEVO-/§7-bis) y sin nombres de hoja que este molde no tiene. La
# trazabilidad va aquí, en el comentario, por fila: TEC-01/DOM-01 ·
# §7-bis.17 + RC-19 + REF-01/REF-07 · §7-bis.17 + RD-34 · TEC-11/DOM-30 ·
# §7-bis.17 · — · NUEVO-03 · TEC-07/DOM-12/NUEVO-01 · NUEVO-02 · §7-bis.11 ·
# TEC-06/DOM-15 · TEC-08/DOM-10/COM-04 · DOM-14/DOM-17 · RT-04/RT-05 ·
# RD-34 + REF-17 · REF-01/REF-07.
#
# ⚠️ Y las CIFRAS de esta tabla son las que el libro termina teniendo, no las
# de una versión intermedia: la fila de plantilla publicaba «~93.000 €»
# cuando `Personal!G12` valía 89.189,80 (REF-12). Al tocar `PLANTILLA`,
# `SUPUESTOS` o `ESCENARIOS` hay que volver a leer el xlsx y actualizar esta
# tabla; ninguna cifra de aquí se calcula sola.
#
# ⚠️ `motor.cross_sell_sin_precios` BORRA los importes en euros de cualquier
# celda de más de 25 caracteres que contenga «kit », «plan », «guía »,
# «pack» o «ebook». Ninguna celda de esta tabla puede llevar a la vez una de
# esas palabras y un «€»: se llevaría por delante la cifra.
RECALIBRADO = (
    ('Coste de personal en la cuenta de resultados', '96.000 €',
     'El que suma la hoja «Personal»: 108.368 €',
     'La cuenta de resultados llevaba una cifra tecleada a mano que no era '
     'la que sumaba su propia hoja de Personal (209.174 €). Ahora las dos '
     'son el mismo número y se recalcula sola cada vez que cambias un sueldo.'),
    ('Plantilla', '7 puestos / 209.174 € al año',
     '7 puestos, cuatro de ellos a jornada parcial / 108.368 € al año',
     'Dimensionada por horas de servicio: cubre las 13 horas de apertura con '
     'dos personas a la vez los 300 días que abre el local, con un 1 % de '
     'holgura. Ningún sueldo baja del salario mínimo, y las jornadas '
     'parciales lo respetan en proporción. Con la estructura anterior el '
     'coste laboral era el 77,5 % de las ventas; ahora es el 35,8 %, dentro '
     'del 32-38 % que este mismo libro publica como referencia.'),
    ('Clientes al día del año 1', '50', '56',
     'Son 1,24 servicios por plaza y día sobre las 45 plazas del aforo, la '
     'mitad de la ocupación que describe el documento (1,8 servicios en el '
     'almuerzo y 1,5 en la cena). Suben porque un equipo que cubra el '
     'horario de verdad y cobre al menos el salario mínimo no cabe dentro '
     'del techo de coste de personal con la facturación anterior.'),
    ('Ticket medio', '18 € (sin decir si llevaba IVA)',
     '18 € SIN IVA (el mismo número)',
     'Se declara qué era esa cifra, no se cambia: con el IVA de sala son '
     '19,80 € de precio de venta, dentro del rango de 15-22 € que publica '
     'este mismo libro.'),
    ('Facturación del año 1', '270.000 €', '302.400 €',
     '56 clientes × 18 € × 300 días. Sube por el número de clientes, no por '
     'el precio: el ticket es exactamente el mismo.'),
    ('Alquiler', '2.500 €/mes', '2.500 €/mes (sin cambio)',
     'Con la facturación recalibrada son el 9,9 % de las ventas, por debajo '
     'del techo del 12 % que fija este mismo libro.'),
    ('Calendario de apertura',
     'Escenarios: 310-320 días/año · cuenta de resultados: 300 implícitos',
     '300 días al año, un único dato en «0. Supuestos»',
     'El libro traía dos calendarios distintos y las hojas no cuadraban '
     'entre sí. Se toma el más prudente, que además es el que la cuenta de '
     'resultados ya usaba.'),
    ('Fondo de maniobra', '12.000 € etiquetados «3 meses»',
     '3 × los costes fijos de caja de un mes, por fórmula',
     'Los 12.000 € cubrían 0,93 meses, no 3. Ahora se recalcula solo cada '
     'vez que cambias un coste fijo.'),
    ('Amortización', '11.550 € al año, 10 años planos sobre toda la '
     'inversión',
     'Sólo sobre la obra (10 años) y la maquinaria (8 años), por fórmula',
     'El fondo de maniobra, la fianza, las existencias iniciales y el '
     'marketing de lanzamiento no son inmovilizado y no se amortizan.'),
    ('Imprevistos de obra', '8.500 € tecleados a mano',
     'Un porcentaje sobre las partidas de obra, editable en «0. Supuestos»',
     'El porcentaje vivía dentro del rótulo de la fila, así que mentía cada '
     'vez que se tocaba cualquier partida.'),
    ('Impuesto de Sociedades',
     '25 % los tres años, sin compensar pérdidas',
     '15 % los dos primeros ejercicios con beneficio, compensando las '
     'pérdidas anteriores',
     'Es el tipo de entidad de nueva creación y la compensación de bases '
     'negativas que permiten los artículos 26 y 29.1 de la Ley del Impuesto '
     'sobre Sociedades.'),
    ('Plan de financiación', 'no existía',
     'Hoja «Financiación»: de dónde sale el dinero, si cuadra con lo que '
     'hace falta, y el cuadro de amortización del préstamo',
     'La ficha del producto lo prometía y ningún fichero de la familia lo '
     'traía.'),
    ('Dinero que hay que poner', 'no se declaraba',
     '50.000 € de los socios y 129.000 € de préstamo',
     'Se ajusta a la necesidad de caja que calcula la hoja de Inversión: ni '
     'por debajo, porque entonces el proyecto no está financiado, ni muy por '
     'encima, porque se pagan intereses por un dinero que no se usa. Los '
     'socios ponen el 28 %, que es lo que suele pedir una entidad.'),
    ('Tesorería mes a mes', 'no existía',
     'Hoja «Tesorería 12 meses»: cobros, pagos, IVA trimestral y saldo '
     'acumulado',
     'Es la hoja que responde en qué mes se agota la caja, que es lo que '
     'decide una operación bancaria.'),
    ('Varios e imprevistos', '2.500 € al año dentro de los costes fijos',
     '1 % de las ventas, como coste variable',
     'Un gasto que sube y baja con la facturación no puede vivir en los '
     'costes fijos: movía el punto de equilibrio sin motivo.'),
    ('Sueldos y horario cubierto', 'sin ninguna comprobación',
     'Semáforo por sueldo y contador de horas contratadas frente a las '
     'necesarias',
     'La hoja de Personal avisa en rojo si un sueldo queda por debajo del '
     'mínimo legal en proporción a su jornada, y en ámbar si el equipo no '
     'llega a cubrir el horario que el propio proyecto declara.'),
)


# ==========================================================================
# §2.6 — CUADRANTE DE COBERTURA (A4 / MOT-03 · motor 2.2, 2026-09-05)
# ==========================================================================
#: FUENTE: el horario que declara el documento de ESTE plan — 12:00-16:00 y
#: 19:00-00:30, o sea 9,5 h de servicio al día, no las 13 h que el motor
#: traía cableadas del molde de restaurante (fixer.json de este hermano,
#: MOT-03). Con 13 h × 2 personas × 300 días el libro exigía 7.800 h, un
#: mínimo de 4,24 jornadas equivalentes y ~96.375 €/año de coste de personal
#: sólo para pintar el semáforo de verde: es lo que empujó los clientes/día
#: de 50 a 56 para caber en el techo del 36 % de labour cost.
#: La tarde de cierre (16:00-19:00) NO se cuenta: no hay servicio.
COBERTURA = {
    'horas_dia': 9.5,
    'personas_franja': 2,
    'nota_horas': 'Los dos servicios que declara el documento de este plan: '
                  '12:00-16:00 y 19:00-00:30. La tarde de cierre no se '
                  'cuenta. Cuéntalas sobre tu horario real',
    'nota_personas': 'Media de presencia simultánea entre barra y sala en los '
                     'dos servicios. En las puntas hará falta más y al final '
                     'de cada turno, menos',
}

# ==========================================================================
# §2.4 — la REFERENCIA de rotación de ESTE documento (A5 / MOT-02)
# ==========================================================================
#: El texto que publicaba la celda venía del documento del REPRESENTANTE
#: (bar-restaurante), que sí enuncia un mínimo de 1,8 rotaciones AL DÍA. El
#: documento de este plan dice otra cosa (párrafo 27): 1,8 servicios por
#: cubierto en ALMUERZO y 1,5 en CENA — sumados, ~3,3 al día. Comparar ese
#: 1,8 con la rotación diaria hacía parecer insuficiente un caso base que es
#: prudente.
ROTACION = {
    'referencia': 'El documento de este plan pide 1,8 servicios por cubierto '
                  'en el almuerzo y 1,5 en la cena (párrafo 27), que sumados '
                  'son unas 3,3 rotaciones al día: compáralo con tu horario '
                  'real antes de darlo por bueno.',
}
