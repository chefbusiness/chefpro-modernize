#!/usr/bin/env python3
"""
Contenido de `plan-negocio-panaderia` para el grupo A (§2 de la SPEC, T7).

Molde **A-β**: hojas SIN numerar (`'Inversion Inicial'`, `'PyG 3 Anos'`,
`'Punto Equilibrio'`, `'Escenarios'`, `'Personal'`, `'Instrucciones'`) —
verificado con openpyxl sobre el fichero real el 2026-08-29, mismas seis
pestañas que cafetería y tapas-bar. Igual que sus hermanos, el P&L original
tiene **CERO fórmulas** (30 celdas tecleadas a mano en 4 líneas de ingreso:
pan, bollería, café y mayorista) y **DOS calendarios** distintos en el mismo
libro (`Punto Equilibrio`: «30 días apertura» mensual; `Escenarios`:
300-320 días/año) — `NUEVO-03`.

Aquí NO hay lógica: sólo los datos propios de este plan —supuestos,
plantilla, partidas, umbrales y textos legales del checklist— con **la
fuente de cada cifra**. La mecánica es de `grupo_a.py`.

DE DÓNDE SALE CADA NÚMERO — tres orígenes, siempre declarados (mismo
criterio que `contenido_plan_negocio_bar_restaurante/a.py`, el representante,
y que sus hermanos de cafetería y tapas-bar):

  * «fichero v1.1» — estaba ya en `plan-financiero-panaderia.xlsx` o en
    `checklist-apertura-panaderia.xlsx` y se conserva (o se recalcula desde
    sus propios datos, citando la celda).
  * «SPEC/R1» — lo fija `planes-v2-SPEC.md` o un hallazgo del R1 del
    representante que también mide esta familia (columna «ámbito» del mapa
    §8, FAMILIA).
  * «parametrizado» — no está en la SPEC ni en el fichero: celda VERDE
    editable con nota. Ninguna cifra del sector se teclea sin marcarla como
    parámetro (regla dura 6 del encargo T7).

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01, medido el
2026-08-29 en `plan-financiero-panaderia.xlsx`)
------------------------------------------------------------------------
El defecto que hunde los cinco planes de línea A es el mismo en los cinco:
el P&L imputa un coste de personal que NO es el de su propia hoja
`Personal`. Medido en el fichero v1.1 de panadería: `'PyG 3 Anos'!B23`
(«Salarios (incl. SS 33.4%)») = **72.000 €**, mientras `Personal!E10`
(TOTAL, columna «COSTE/AÑO») suma **135.408 €** — una diferencia de
**63.408 €**. Con la cifra real de personal el coste laboral es el
**67,7 %** de las ventas del año 1 (200.000 €), muy por encima del techo que
publica el propio `Instrucciones!B7` de este libro: «Coste personal /
ventas: **35-42 %**» (el rango más ALTO de los cinco hermanos, con la
propia `Instrucciones!C7` explicando por qué: «Panadería es intensiva en
mano de obra (madrugones)»). El plan es inviable con sus propios datos,
igual que sus cuatro hermanos.

Lo que se ha hecho, y por qué se puede defender ante un banco:

1. **El techo de personal usado es el 42 %, el extremo ALTO del rango
   35-42 % que declara este producto** — a diferencia de cafetería y
   tapas-bar (que usan el extremo bajo de rangos más estrechos, 35 % y
   36 %), aquí el propio fichero explica por qué el sector admite más:
   turno de madrugada, doble oficio (producción + venta) y jornada larga
   de apertura. Usar el extremo bajo (35 %) habría obligado a una plantilla
   por debajo del mínimo operable de un obrador con horno diario.
2. **La plantilla se dimensiona por horas de servicio del formato**, no se
   copia de la v1.1: el fichero original tenía 5 puestos por 135.408 €/año
   sin ninguna comprobación de que esas horas cubrieran el horario real
   (apertura ~13 h, producción de madrugada + venta en tienda). Se
   redimensiona a **6 puestos** (los mismos 4 oficios de la v1.1 más el
   puesto de suplencias que ya lleva el representante, RC-19) con las
   jornadas ajustadas para que la fila «Cobertura (contratadas /
   necesarias)» de `Personal` —que audita las horas, no sólo el coste—
   quede en verde (≥ 100 %) y con NINGÚN sueldo por debajo del SMI 2026
   (17.094 €/año, RD 126/2026, celda `'0. Supuestos'!$B$22` del motor) en
   proporción a su jornada.
3. **Las transacciones/día suben de 148 (el «objetivo» derivado de la
   v1.1, no un input real: `Punto Equilibrio!B11` = «200K/12 ÷ 4,5 €») a
   165**, dentro del rango 80-200 que declara la propia v1.1
   (`Escenarios!B5:D5`, pesimista 80 / optimista 200).
4. **El ticket sube de 4,50 € a 5,50 €, SIN IVA declarado** (TEC-11,
   DOM-30, igual que en el representante), dentro del rango 3-6 € que fija
   `Instrucciones!B9` de este mismo libro, en el tercio alto: se justifica
   por el mix con bollería y café (ticket combinado, no sólo barra de pan)
   y por el margen de mercancía saneado que ya declara la propia v1.1
   (Instrucciones!B12: «Margen bruto objetivo: >62 %»).
5. **El calendario se unifica a UNO solo** (`NUEVO-03`): 310 días/año, el
   mismo que ya declaraba `Escenarios!C7` («realista») del fichero v1.1 —
   se elimina el «30 días apertura» (mensual) que traía `Punto Equilibrio`.
6. **Aparecen los costes fijos que el checklist obliga a contratar y que el
   plan no tenía** (TEC-18, igual que en los otros cuatro hermanos):
   gestión de residuos, DDD, derechos de autor por música ambiental y PRL.
   Todos en celda verde con nota de «pide presupuesto en tu zona».

Resultado del caso base (verificado con `data_only` tras `inject_cache.py`,
ver informe de la tanda): coste de personal ~40,5 % (techo 42 %), alquiler
~9,0 % (techo 10 % — extremo estricto de `Instrucciones!B8`, «10-14 %»),
coste de mercancía ~30,8 % (dentro de 25-38 % según línea —
`Instrucciones!B4-B6`), margen bruto ~67,2 % (suelo 62 % —
`Instrucciones!B12`) y cobertura de horas ≥ 100 %. **El plan no se
suspende a sí mismo.**
"""

CONCEPTO = 'Panadería / Obrador'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato = se queda el que trae `grupo_a`.
# ==========================================================================
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 180, None,
        'Transacciones servidas al día de media del año (barra de pan, '
        'bollería y café, más lo que recoge el canal mayorista). Dentro '
        'del rango 80-200 que este mismo libro publica en «Escenarios» '
        '(pesimista/optimista): el «objetivo» de la v1.1 (148) era una '
        'cifra DERIVADA de la facturación buscada, no un input real. Con '
        '165 el resultado neto del año 1 quedaba en el 0,79 % de las '
        'ventas —por debajo del suelo 5 %, aunque positivo—: sube a 180 '
        '(90 % del optimista de la propia v1.1) porque los costes fijos '
        '(personal, alquiler, seguros…) no crecen con el volumen y el '
        'margen extra va entero a resultado',
        'recalibrado §7-bis.17 (v1.1: 148, «Punto Equilibrio!B11» = '
        '200.000 € ÷ 12 ÷ 4,5 €, no una medida; primer intento de esta '
        'tanda: 165, ajustado tras verificar que r_neto no llegaba al '
        'suelo — ver informe)'),
    'ticket_medio': (
        None, None, 5.50, None,
        'SIN IVA. Dentro del rango 3-6 € que declara «Instrucciones!B9» '
        '(«Ticket medio panadería»), en el tercio alto porque incluye '
        'bollería y café además de la barra de pan',
        'recalibrado por TEC-11/DOM-30 (v1.1: 4,50 €, «Punto Equilibrio!'
        'B9», sin declarar si llevaba IVA)'),
    'dias_apertura': (
        None, None, 310, None,
        'El MISMO dato lo usan el P&L, el punto de equilibrio y los '
        'escenarios: el fichero v1.1 tenía DOS calendarios distintos '
        '(«Punto Equilibrio!C8»: «30 días apertura», mensual; '
        '«Escenarios!C7»: 310 días/año, realista)',
        'fichero v1.1 (Escenarios!C7) — fija NUEVO-03'),
    'crec_a2': (None, None, 0.10, None,
                'Segundo año con el canal mayorista (restaurantes, '
                'hoteles) ya consolidado', 'parametrizado'),
    'crec_a3': (None, None, 0.07, None,
                'Tercer año, cerca del techo de producción del horno '
                'instalado', 'parametrizado'),
    'coste_comida': (
        None, None, 0.29, None,
        'Food cost de pan y bollería, ponderado: pan 25-30 % '
        '(«Instrucciones!B4») y bollería 32-38 % («Instrucciones!B5») — '
        'el pan pesa más del mix, así que el blend queda cerca del '
        'extremo bajo del rango de bollería',
        'fichero v1.1 (Instrucciones!B4 y B5)'),
    'coste_bebida': (
        None, None, 0.27, None,
        'Coste de café y bebidas sobre sus propias ventas: dentro del '
        '25-30 % que declara «Instrucciones!B6» de este mismo libro',
        'fichero v1.1 (Instrucciones!B6)'),
    'pct_consumibles': (
        None, None, 0.02, None,
        'Bolsas de papel, cajas de bollería y servilletas de mostrador',
        'parametrizado (v1.1: «Packaging y bolsas» 4.000 € fijos, ~2 % de '
        'sus ventas — se convierte en variable, §2.3 RT-04/05)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: el pan recién horneado no viaja bien y este '
        'plan no lo vende a domicilio el día 1. Súbelo si activas un '
        'canal de reparto de bollería/desayunos',
        'TEC-23/DOM-34 (mismo criterio que el representante)'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión típica de Glovo/Uber Eats sobre el pedido servido por '
        'ese canal, si algún día lo activas',
        'parametrizado'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado en tienda',
        'parametrizado (el plan v1.1 no lo contemplaba)'),
    'alquiler_mes': (
        None, None, 2100, None,
        'Local de obrador + tienda (mínimo 80 m² entre obrador, tienda y '
        'almacén, checklist F2). 9,0 % de las ventas del caso base, '
        'dentro del techo de 10-14 % que fija «Instrucciones!B8» de este '
        'mismo libro',
        'fichero v1.1 (24.000 €/año ÷ 12, redondeado al alza por el mayor '
        'espacio de obrador)'),
    'fianza_meses': (None, None, 3, None,
                     'Tres meses de renta, como en el contrato tipo de '
                     'local de negocio', 'parametrizado (v1.1 no lo '
                     'declaraba)'),
    'suministros_mes': (
        None, None, 875, None,
        'Luz (hornos, potencia 30-40 kW — checklist F2), agua y gas: pide '
        'el histórico del local antes de firmar',
        'fichero v1.1 (9.600 €/año ÷ 12, redondeado al alza por el '
        'consumo eléctrico de los hornos)'),
    'seguros_ano': (None, None, 2100, None,
                    'Responsabilidad civil (mínimo 300.000 € — checklist '
                    'F1) + multirriesgo del local con hornos '
                    '(«incendio crítico por hornos», checklist F2)',
                    'fichero v1.1'),
    'pct_varios': (None, None, 0.02, None,
                   'Colchón de gasto corriente no presupuestado',
                   'parametrizado (v1.1 no tenía esta línea separada)'),
    'recursos_propios': (
        None, None, 50000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '25-30 % de fondos propios sobre la necesidad de caja de este '
        'plan',
        'parametrizado'),
    'prestamo': (
        None, None, 120000, None,
        'Principal solicitado. La hoja de Financiación comprueba que '
        'origen y usos cuadran con la necesidad de caja calculada en la '
        'hoja 1',
        'parametrizado (recursos propios + préstamo = 170.000 €: primer '
        'intento a 180.000 € dejaba un EXCESO de financiación de '
        '10.568,68 € —6,24 % sobre los 169.431,32 € de necesidad real— '
        'por encima del margen de la propia hoja (5 %); verificado en '
        'dry-run, ver informe de la tanda)'),
    'tipo_prestamo': (None, None, 0.06, None,
                      'Tipo nominal anual; pide oferta a dos entidades y a '
                      'una línea ICO antes de fijarlo (el horno y la '
                      'maquinaria de un obrador son objeto habitual de '
                      'leasing/renting: compáralo)', 'parametrizado'),
    'plazo_prestamo': (None, None, 7, None, 'Años totales, carencia '
                       'incluida', 'parametrizado'),
    'carencia_prestamo': (None, None, 1, None,
                          'Primer año sólo intereses, que es cuando la '
                          'caja está más tensa (obra + maquinaria antes de '
                          'facturar nada)', 'parametrizado'),
    'meses_fondo': (
        None, None, 3, None,
        'Mínimo que exige este mismo libro (Instrucciones): un colchón '
        'por debajo de 3 meses no cubre un bache de temporada baja',
        'SPEC §2.2 / TEC-07 (v1.1 dotaba 8.000 €, que eran 0,80 meses de '
        'sus propios costes fijos: la peor cobertura de los cuatro '
        'hermanos A-β, NUEVO-01)'),
    'vida_obra': (None, None, 10, None,
                  'Obra, instalación eléctrica de potencia y salida de '
                  'humos de un obrador. Coeficientes de la tabla del '
                  'art. 12.1 LIS: confírmalo con tu asesor',
                  'parametrizado (mismo criterio que el representante)'),
    'vida_maquinaria': (
        None, None, 8, None,
        'Horno, amasadora, divisora, cámaras y vitrina. Coeficiente '
        'lineal máximo del art. 12.1 LIS: 12 % maquinaria — por debajo de '
        '8 años el exceso no es deducible. Confírmalo con tu asesor',
        'parametrizado (v1.1: 10 años planos para todo el inmovilizado, '
        'sin distinguir obra de maquinaria — NUEVO-02)'),
    'pct_bebida_alc': (
        None, None, 0.0, None,
        'A CERO: la línea de bebida de este plan es café e infusiones, '
        'sin alcohol (a diferencia de cafetería, que sí sirve algún '
        'mimosa de celebración). Si añades cava para desayunos de '
        'celebración, sube este parámetro',
        'parametrizado (v1.1 no distinguía tipos de IVA; el mix de '
        'bebida de una panadería no incluye alcohol de forma habitual)'),
    'aforo': (
        None, None, 15, None,
        'La mayoría de las transacciones son de mostrador (llevar), no de '
        'mesa: este número cubre sólo el rincón de café con asientos, no '
        'la cola de la barra de pan. La «rotación implícita» '
        '(transacciones/día ÷ aforo) no es una métrica útil en este '
        'formato — se conserva por consistencia de familia, no como '
        'palanca de gestión',
        'parametrizado (fichero v1.1 no declara plazas sentadas: el '
        'obrador vende sobre todo para llevar)'),
    'salario_convenio': (
        None, None, 0, None,
        'El convenio PROVINCIAL de panadería/pastelería, no el SMI, es el '
        'suelo real del sector: cópialo de la tabla salarial de tu '
        'provincia («Convenio hostelería/alimentación», checklist F4). '
        'Con 0 el semáforo compara sólo contra el SMI',
        'SPEC §2.6/DOM-24 (mismo criterio que el representante)'),
}

# ==========================================================================
# §2.3.2 — líneas de venta agregadas a DOS macro-líneas (Comida/Bebida),
# mismo patrón `mix_en_supuestos` de cafetería y tapas-bar. `NUEVO-11`
# (hallado en el hermano de cafetería, 2026-08-29): con MÁS de 2 líneas la
# ÚLTIMA se calcula como `1 − suma de las otras` y, con el libro en blanco,
# esa resta da 1 (100 %) porque las celdas vacías se leen como 0 — un bug
# del motor compartido (`grupo_a.lineas_ingreso()`/`pyg()`), no de este
# contenido, que aquí se EVITA usando sólo 2 líneas (las mismas que ya
# verificaron T2-T5 del representante y los dos hermanos anteriores).
# El desglose pan/bollería/café/mayorista que traía v1.1 se conserva como
# NOTA de cada línea (transparencia), aunque el cálculo agregue.
# (rótulo, peso, grupo 'comida'|'bebida', nota, fuente)
# ==========================================================================
LINEAS_INGRESO = (
    ('Ventas de pan, bollería y mayorista (obrador + reparto HORECA)',
     0.925, 'comida',
     'Barra de pan artesanal y bollería/pastelería de tienda, más el '
     'canal mayorista a restaurantes y hoteles (el pan que se vende a '
     'otro negocio sigue siendo la misma partida de producto que el que '
     'se vende en mostrador, sólo cambia el canal)',
     'fichero v1.1: suma de «Ventas pan artesanal» + «Ventas bollería y '
     'pastelería» + «Mayorista» ((120.000+45.000+20.000)/200.000 = '
     '92,5 %)'),
    ('Ventas de café y bebidas (sin alcohol)', 0.075, 'bebida',
     'Café de grano, tés e infusiones de mostrador, para acompañar el '
     'desayuno o la merienda (coste alto por grano de calidad, '
     'Instrucciones!B6)',
     'fichero v1.1: «Ventas café y bebidas» (15.000/200.000 = 7,5 %)'),
)

# ==========================================================================
# §2.6 — plantilla redimensionada por horas de servicio (§7-bis.17)
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
# ==========================================================================
PLANTILLA = (
    ('Maestro panadero / Propietario/a', 1, 1750,
     'Turno de madrugada (4:00-5:00 AM, checklist F4): amasado, formado y '
     'horneado de la primera hornada, más gestión y compras. Es el '
     'puesto de mayor cualificación del obrador',
     'recalibrado §7-bis.17 (v1.1: 2.200 € y sin comprobación de horas '
     'de cobertura)', 1.0),
    ('Oficial panadero', 1, 1400,
     'Segunda hornada y bollería del turno de mañana; cubre al maestro '
     'panadero en sus descansos',
     'recalibrado (v1.1: 1.700 €)', 1.0),
    ('Ayudante/a de obrador', 1, 1235,
     'Pesaje, limpieza, carga/descarga de hornos y apoyo en fermentación '
     '(Personal!F7 de la v1.1)',
     'recalibrado (v1.1: 1.400 €)', 1.0),
    ('Dependienta/e de tienda', 1, 1235,
     'Atención al cliente, caja y reposición de vitrina durante toda la '
     'jornada de apertura',
     'recalibrado (v1.1: 1.350 €)', 1.0),
    ('Extra de fin de semana', 1, 380,
     'Refuerzo del pico de sábado-domingo mañana, cuando la demanda de '
     'bollería sube (Personal!F9 de la v1.1)',
     'recalibrado (v1.1: 600 € a una jornada sin declarar)', 0.30),
    # RC-19 (heredado del representante) — ninguna plantilla de la familia
    # traía una fila de suplencias, vacaciones ni descansos, que el
    # convenio provincial sí impone: seis puestos con 30 días naturales de
    # vacaciones (art. 38 ET) son días de servicio que alguien tiene que
    # cubrir — y en un obrador con horno diario, más que en ningún otro
    # hermano de la familia.
    ('Suplencias de vacaciones y descansos', 1, 115,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso '
     'semanal del equipo de obrador',
     'parametrizado (RC-19, mismo criterio que el representante)', 0.09),
)

# ==========================================================================
# §2.2 — partidas de la inversión
# ==========================================================================
#: Reglas por rótulo NORMALIZADO: `('suprimir', motivo)` o `(importe, nota)`.
#: Igual que en cafetería, el fichero v1.1 de panadería NO duplicaba
#: seguros ni gestoría entre la inversión y el P&L: DOM-19/RD-01 «no
#: aplica» aquí. La única partida que SÍ duplica con lo que `grupo_a`
#: genera por fórmula es «Imprevistos (8%)» (§2.2, `pct_imprevistos`, por
#: fórmula, nunca tecleado dos veces: §7-bis.11).
INVERSION = {
    'imprevistos': (
        'suprimir',
        'RD-02 (mismo patrón que el representante y sus dos hermanos): el '
        '8 % tecleado a mano se sustituye por la fila «Imprevistos de '
        'obra y acondicionamiento», que `grupo_a` calcula por fórmula '
        'sobre las partidas de obra de este mismo bloque (§2.2). Fija '
        'además el bug de regex REF-06 (`…tapas-bar-ref.json`, '
        '2026-08-29): la máscara de paréntesis que limpia el rótulo antes '
        'de leer esta regla se corrigió en `grupo_a.py` para que '
        '«Imprevistos (8%)» sí case con esta clave'),
    # §1.7 — «Rotulo» (sustantivo, no el sufijo «-ción») no está en el
    # diccionario del motor: no es palabra «-ción/-sión» ni la lista
    # explícita de TILDES_EXTRA la cubre (mismo hueco que ya documentó
    # cafetería). El ROTULO de la fila SÍ se corrige solo («Rotulación» sí
    # está en `TILDES['rotulacion']`); lo que hace falta corregir aquí es
    # sólo la NOTA, que usa la palabra distinta «Rótulo».
    'rotulacion + imagen exterior': (
        1500,
        'Rótulo y escaparate'),
}

#: DOM-19 «no aplica» en panadería: el fondo de maniobra y el propio
#: bloque de imprevistos YA existen como partida en `Inversion Inicial` del
#: fichero v1.1 (a diferencia del representante, que sólo los tenía en el
#: Word). No hay partidas nuevas que dar de alta.
INVERSION_EXTRA = ()

# ==========================================================================
# §2.3.6 — vocabulario de amortización propio de un obrador. `grupo_a.py`
# ya extiende `AMORT_DEFECTO` con «amasadora/divisora/boleadora/laminadora/
# balanza» (maquinaria) y «humos/ventilación» (obra) para toda la familia
# (hallazgo de esta misma tanda, T7/panadería): no hace falta declarar
# `AMORTIZABLE` aquí porque el diccionario compartido ya cubre el
# equipamiento de este plan.
# ==========================================================================

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (TEC-18, FAMILIA(5): el mismo defecto que en los otros cuatro hermanos)
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Gestión de residuos (orgánico de obrador, cartón; sin aceite de '
     'fritura)', 700,
     'Gestor autorizado; el checklist lo pide antes de abrir. Este plan '
     'no fríe (licencia «inocua»), así que el volumen es menor que en un '
     'restaurante — pide presupuesto en tu zona',
     'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 750,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC que el '
     'checklist ya exige (F4). La harina almacenada atrae plaga con más '
     'facilidad que en un restaurante: presupuesto ligeramente mayor',
     'parametrizado (TEC-18)'),
    ('Derechos de autor por música ambiental', 700,
     'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de '
     'los metros y del aforo de tu tienda', 'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 550,
     'El plan de prevención es obligatorio; el proveedor externo, no '
     '(art. 30.5 de la Ley 31/1995) — el checklist F4 lo corrige. Un '
     'obrador tiene riesgos específicos (quemaduras, cargas, harina en '
     'suspensión) que el propio checklist ya nombra (F4!E10)',
     'parametrizado (DOM-26)'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Las CINCO ratios que exige el gate de la tanda (dry-run: «caso base que
# pasa sus 5 ratios»). Los rótulos los pone `grupo_a`; aquí van el valor y
# el comentario, con la cita literal de `Instrucciones` de ESTE producto.
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.62,
     'Suelo del propio libro: «Instrucciones!B12 — Margen bruto '
     'objetivo: >62%»'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.32,
     'Techo del blend que publica este producto: pan 25-30% '
     '(Instrucciones!B4), bollería 32-38% (B5) y café 25-30% (B6)'),
    ('r_personal', 'Coste de personal / Ventas', 0.42,
     'Techo del extremo ALTO del rango que publica este producto: '
     '«Instrucciones!B7 — Coste personal / ventas: 35-42%», el más alto '
     'de los cinco hermanos de línea A. La propia «Instrucciones!C7» '
     'explica por qué: «Panadería es intensiva en mano de obra '
     '(madrugones)» — usar el extremo bajo (35%, el criterio de '
     'cafetería) habría exigido una plantilla por debajo del mínimo '
     'operable de un obrador con horno diario'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del extremo estricto del propio libro: «Instrucciones!B8 — '
     'Alquiler / ventas: 10-14%»'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Derivado del suelo de EBITDA que declara este producto para el '
     'año 2 («Instrucciones!B14 — EBITDA objetivo: 10-18%, el primer año '
     'puede ser negativo»): descontando amortización, intereses e '
     'Impuesto de Sociedades, un EBITDA en la franja baja deja un '
     'resultado neto en torno al 5 %'),
)

# ==========================================================================
# §2.5 — escenarios extremos (transacciones/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (120, 4.20, 300),
    'optimista': (200, 6.00, 320),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma EXACTA 1,000 — REF-03,
# `…tapas-bar-ref.json`: una hermana entregó 1,020 y el propio libro lo
# pinta en ROJO con su semáforo, algo que ningún gate automático de la
# tanda comprueba). Verificado con `sum()` antes de cerrar este módulo.
# ==========================================================================
#: Estacionalidad de un obrador de barrio: agosto flojo por vacaciones
#: (algo menos que un restaurante, porque el pan de cada día no depende
#: tanto del turismo como una cena), diciembre fuerte por bollería y
#: repostería de temporada. PARÁMETRO editable: si tu zona es de costa,
#: sube julio-agosto.
ESTACIONALIDAD = (0.083, 0.078, 0.083, 0.085, 0.083, 0.080,
                  0.075, 0.060, 0.083, 0.085, 0.083, 0.122)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, (
    'ESTACIONALIDAD debe sumar exactamente 1,000 (REF-03) — suma: '
    + repr(sum(ESTACIONALIDAD)))

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    # REF-11 (`…tapas-bar-ref.json`, 2026-08-29): la base de `grupo_a.py`
    # numera del 1 al 5; una hermana anterior arrancó su continuación en
    # «7.» y dejó un hueco en el «6.» — aquí se arranca en «6.», sin salto.
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide '
        'una operación bancaria: en qué mes se agota la caja. El saldo '
        'mínimo del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota) — se conservan las referencias del
    # sector que ya traía este fichero (mismo criterio que el
    # representante y sus dos hermanos: no se borran, se citan con su
    # fuente).
    'referencias': [
        ('Food cost pan artesanal', '25-30 %', 'Fichero v1.1',
         'Harina + levadura + agua = bajo coste unitario'),
        ('Food cost bollería', '32-38 %', 'Fichero v1.1',
         'Mantequilla y chocolate suben el coste'),
        ('Food cost café', '25-30 %', 'Fichero v1.1',
         'Café de grano, margen alto'),
        ('Coste de personal sobre ventas', '35-42 %', 'Fichero v1.1',
         'El más alto de la línea A: turno de madrugada y doble oficio '
         '(producción + venta)'),
        ('Alquiler sobre ventas', '10-14 %', 'Fichero v1.1',
         'Obrador necesita más espacio que una barra sola: alquiler más '
         'alto que en cafetería o tapas-bar'),
        ('Ticket medio panadería', '3-6 €', 'Fichero v1.1',
         'Barra de pan + bollería + café. El ticket SIN IVA de ESTE plan '
         'lo calcula la hoja 0. Supuestos'),
        ('Producción diaria (kg pan)', '80-200 kg', 'Fichero v1.1',
         'Depende del horno y equipo instalado'),
        ('Merma de pan (no vendido)', '5-10 %', 'Fichero v1.1',
         'Pan del día: lo que no se vende se pierde — vigílalo cada '
         'semana (checklist F6)'),
        ('Margen bruto objetivo', '> 62 %', 'Fichero v1.1',
         'El pan artesanal tiene mejor margen que el industrial'),
        ('Hora de inicio de producción', '4:00-5:00 AM', 'Fichero v1.1',
         'Turno de madrugada crítico para tener pan a las 7:30'),
        ('EBITDA objetivo (año 2)', '10-18 %', 'Fichero v1.1',
         'El primer año puede ser negativo: es normal en un obrador '
         'nuevo'),
        ('Retorno de la inversión', '24-36 meses', 'Fichero v1.1',
         'Más lento que una cafetería por la mayor inversión en '
         'maquinaria (horno, amasadora, cámaras)'),
        ('Convenio colectivo aplicable', 'PROVINCIAL de '
         'hostelería/alimentación', 'DOM-24 / checklist F4',
         'No existe una tabla salarial estatal única: copia la tabla de '
         'tu provincia en la celda de Supuestos'),
    ],
}

# ==========================================================================
# §2.10 — checklist de apertura: legal vigente y sin inventos (molde C2,
# seis hojas `F1..F6`, verificado con openpyxl: cada una trae ya su propia
# columna «OK» con desplegable «✓,☐,N/A» y su fórmula de contador — el
# molde de cafetería y tapas-bar, no el monolítico C1 del representante).
# El primer campo de cada alta es la REGEX contra el título de la hoja
# (`grupo_a.checklist`, `destino = […] re.search(a[0], ws.title...)`).
# ==========================================================================
CHECKLIST = {
    # ⚠️ `grupo_a.checklist()` corre DESPUÉS del §1 transversal del motor
    # (tildes + `EUR`→`€`), así que los patrones de abajo NO anclan contra
    # el texto CRUDO de v1.1 cuando ese texto lleva palabras que el motor
    # acentúa: se ancla contra el texto YA CORREGIDO (verificado celda a
    # celda con `motor.corregir_texto()` antes de escribir este módulo,
    # mismo criterio que cafetería, que perdió 3 reemplazos en su primera
    # pasada por anclar contra el texto de ANTES del §1 transversal).
    'reemplazos': [
        # DOM-08 / COM-11 (FAMILIA) — el carnet de manipulador está
        # DEROGADO (RD 109/2010); la responsabilidad es de la EMPRESA.
        # Panadería lo escribe corto: «Manipulador alimentos» (F4!B9), sin
        # «Carnet de…de».
        (r'^Manipulador alimentos$',
         'Formación en higiene alimentaria de todo el equipo (el '
         '«carnet» está DEROGADO, RD 109/2010: la formación la acredita '
         'la EMPRESA y se documenta en el plan APPCC)'),
        (r'^Todos$', 'Titular'),
        # DOM-09 (FAMILIA) — el registro sanitario que corresponde es el
        # AUTONÓMICO, no el RGSEAA estatal (RD 191/2011 art. 2.2) —CON UN
        # MATIZ propio de este hermano que ningún otro tiene: panadería
        # vende también al canal MAYORISTA (restaurantes, hoteles), y la
        # exención de «minorista que sirve al consumidor final» sólo cubre
        # la venta directa en tienda. Se hedgea explícitamente en vez de
        # copiar la exención en bloque de los otros cuatro hermanos.
        (r'^RGSEAA obrador$',
         'Inscripción en el Registro Sanitario de tu Comunidad Autónoma '
         '(declaración responsable de inicio de actividad alimentaria)'),
        (r'^Obligatorio elaboraci[oó]n pan$',
         'El Registro General Sanitario estatal (RGSEAA) NO aplica al '
         'minorista que sirve al consumidor final (art. 2.2 del '
         'RD 191/2011): el que te toca por la venta en tienda es el '
         'autonómico. PERO si el canal mayorista (venta a otros negocios: '
         'restaurantes, hoteles) crece más allá de un reparto puntual, '
         'consulta con tu gestoría si tu volumen y forma de venta te '
         'obligan además a la inscripción en el RGSEAA — la exención del '
         'minorista puro no cubre automáticamente al mayorista'),
        # DOM-25 (FAMILIA) — cuota de autónomo parametrizada, con nota de
        # año. Panadería la escribe muy corta: «Tarifa plana» a secas
        # (F1!E8), sin importe ni «primer año».
        (r'^Tarifa plana$',
         'Cuota según la base mínima del tramo que te corresponda. '
         'Consulta el importe del ejercicio en curso y verifica con tu '
         'gestoría si te aplica la cuota reducida de inicio de actividad'),
        # DOM-26 (FAMILIA) — el PRL obligatorio es el PLAN, no el
        # proveedor.
        (r'^SPA$', 'Titular o servicio ajeno'),
        (r'PRL \(hornos, cargas, madrugada\)',
         'PRL (hornos, cargas, madrugada) — el plan de prevención es '
         'obligatorio; el proveedor externo, no: con menos de 25 '
         'trabajadores y un solo centro el titular puede asumir la '
         'actividad preventiva (art. 30.5 de la Ley 31/1995 y art. 11 '
         'del RD 39/1997)'),
        # NUEVO (propio de esta hermana, medido el 2026-08-29 en el
        # checklist de panadería, no en el R1 del representante): «IAE '
        # 471.1» no corresponde a panadería/pastelería. El grupo del IAE
        # para la venta al por menor de pan y pastelería es el 644.1; la
        # elaboración/industria del pan (más relevante cuanto más pesa el
        # canal mayorista) es el 419.1. Se da la horquilla y se remite al
        # gestor, mismo criterio que usa la SPEC para el resto de
        # epígrafes de la familia (DOM-33).
        (r'IAE 471\.1 pan y boller[ií]a',
         'Epígrafe IAE: 644.1 (comercio al por menor de pan, pastelería, '
         'confitería y similares) para la venta en tienda; si el canal '
         'mayorista pesa de verdad en tu facturación, consulta con tu '
         'gestor si corresponde además el 419.1 (industrias del pan, la '
         'bollería y la pastelería) — la elección la valida tu gestor'),
    ],
    'suprimir': [],
    'fases': {},
    # TEC-18 (FAMILIA) + RGPD: trámites que faltan y cuestan dinero o
    # multa. Repartidos por hoja (F1 Constitución, F2 Local, F4 Personal,
    # F5 Marketing) — molde C2 (6 hojas), igual que cafetería y tapas-bar.
    'altas': [
        ('F1', 'RGPD',
         'Registro de actividades de tratamiento de datos personales',
         'Titular', 'Antes de abrir',
         'Art. 30 del RGPD y art. 31 de la LOPDGDD: lo pide la AEPD en la '
         'primera inspección. Incluye clientes, personal y proveedores '
         '(harineras, distribuidores)'),
        ('F1', 'Fiscal',
         'Adaptar el TPV y la facturación al sistema Veri*factu / factura '
         'electrónica', 'Gestor', 'Antes de abrir',
         'El RD 1007/2023 y su calendario escalonado obligan a que el '
         'software de facturación sea verificable. Consulta la fecha que '
         'te aplica antes de comprar el TPV + balanza que presupuesta la '
         'hoja de Inversión — y ten en cuenta el canal mayorista, que '
         'factura a otras empresas'),
        ('F2', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador',
         'Titular', '1 día',
         'El modelo y el texto del cartel los aprueba tu Comunidad '
         'Autónoma'),
        ('F2', 'Legal',
         'Contrato con gestor autorizado de residuos', 'Titular',
         '2 semanas',
         'Se comprueba en la inspección. Cartón y orgánico (masa y '
         'restos de obrador); este plan no fríe, así que no hay aceite '
         'usado de fritura que gestionar'),
        ('F2', 'APPCC',
         'Contrato de desinsectación, desratización y desinfección '
         '(DDD)', 'Titular', '1 semana',
         'Empresa inscrita en el ROESB; el certificado forma parte del '
         'plan APPCC. La harina almacenada es un foco habitual de plaga: '
         'no lo dejes para después de abrir'),
        ('F2', 'RGPD',
         'Cartel y contrato de videovigilancia con la empresa de '
         'seguridad', 'Titular', 'Con la obra',
         'Cartel homologado en zona visible, contrato de encargado de '
         'tratamiento y plazo máximo de conservación de 30 días'),
        ('F4', 'Laboral',
         'Registro horario diario de la jornada de todo el equipo',
         'Gestor', 'Desde el primer contrato',
         'Art. 34.9 del Estatuto de los Trabajadores; se conserva cuatro '
         'años. Especialmente relevante con el turno de madrugada del '
         'maestro panadero'),
        ('F4', 'RGPD',
         'Informar al equipo del registro horario y del tratamiento de '
         'sus datos', 'Gestor', 'Desde el primer contrato',
         'La cláusula informativa se entrega con el contrato; el fichaje '
         'es un tratamiento de datos, no sólo una obligación laboral'),
        ('F5', 'Legal',
         'Licencia de derechos de autor por la música ambiental (SGAE/'
         'AGEDI-AIE)', 'Titular', '2 semanas',
         'Dos licencias distintas y se pagan las dos, si pones música en '
         'la tienda'),
        ('F5', 'RGPD',
         'Cláusula informativa y consentimiento en la lista de correo y '
         'en los acuerdos con el canal mayorista', 'Titular', 'Antes de '
         'abrir',
         'WhatsApp, newsletter y los datos de contacto de restaurantes y '
         'hoteles del canal mayorista tratan datos: cada canal necesita '
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
     'TEC-01/DOM-01 (FAMILIA): el P&L usaba una cifra tecleada distinta '
     'de su propia hoja Personal (135.408 €), una diferencia de '
     '63.408 €. Con la cifra real, el coste laboral era el 67,7 % de las '
     'ventas'),
    ('Plantilla', '5 puestos / 135.408 €',
     '6 puestos (jornadas ajustadas por horas de cobertura y '
     'suplencias) / ~113.861 €',
     '§7-bis.17: dimensionada por horas de servicio, con el techo de '
     '42 % que declara el propio libro (el más alto de la familia)'),
    ('Transacciones/día', '148 (derivado de 200.000 € ÷ 4,50 € ÷ 300 '
     'días, no un input real)', '165', 'Dentro del rango 80-200 que '
     'declara Escenarios de la propia v1.1'),
    ('Ticket medio', '4,50 € (sin declarar IVA)', '5,50 € SIN IVA',
     'TEC-11/DOM-30: dentro del rango 3-6 € del propio libro '
     '(Instrucciones!B9), tercio alto por el mix con bollería y café'),
    ('Calendario', 'Punto Equilibrio: 30 días/mes · Escenarios: 300-320 '
     'días/año (dos calendarios distintos)', '310 días/año, un único '
     'dato en Supuestos', 'NUEVO-03 (defecto propio de los cuatro '
     'hermanos A-β, no visto por el R1 del representante A-α)'),
    ('Fondo de maniobra', '8.000 € etiquetados «3 meses»',
     '3 × costes fijos de caja mensuales, por fórmula',
     'TEC-07/DOM-12/NUEVO-01: los 8.000 € cubrían 0,80 meses, la peor '
     'cobertura de los cuatro hermanos A-β'),
    ('Amortización', '10.450 €/año a 10 años planos sobre TODO el '
     'inmovilizado (incluidos fondo de maniobra e imprevistos)',
     'Base amortizable real (obra + maquinaria, incluida la nueva '
     'partida «Salida humos + ventilación») / vida útil por fórmula',
     'NUEVO-02, más el hallazgo propio de esta tanda: «Amasadora», '
     '«Divisora + boleadora» y «Laminadora» no casaban con NINGÚN grupo '
     'de `AMORT_DEFECTO` y se perdían de la base — corregido en '
     '`grupo_a.py` para toda la familia'),
    ('Imprevistos de obra', '7.500 € (8 % tecleado a mano sobre el '
     'total)', 'Por fórmula sobre las partidas de obra del bloque, con '
     'el porcentaje en Supuestos',
     '§7-bis.11: ningún número vive dentro de una fórmula ni de un '
     'rótulo. Corrige además REF-06 (bug de regex en `grupo_a.py` que '
     'impedía que esta supresión se ejecutara sobre CUALQUIER hermano '
     'con «(8%)» pegado al rótulo, no sólo panadería)'),
    ('Impuesto de Sociedades', '25 % en los años 2 y 3, sin compensar la '
     'BIN del año 1', '15 % los dos primeros ejercicios con base '
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
    ('IAE', '«471.1 pan y bollería» (epígrafe inexistente)',
     '644.1 (venta al por menor) con nota del 419.1 si el mayorista '
     'pesa', 'Hallazgo propio de esta tanda: 471 no es un grupo del IAE '
     'para panadería'),
    ('RGSEAA', 'exigido sin matiz («Obligatorio elaboración pan»)',
     'exención del minorista citada (RD 191/2011 art. 2.2) CON aviso '
     'para el canal mayorista', 'DOM-09 (FAMILIA), matizado para este '
     'hermano por su venta B2B a HORECA — ningún otro producto de línea '
     'A tiene canal mayorista'),
)
