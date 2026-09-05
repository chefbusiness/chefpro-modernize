#!/usr/bin/env python3
"""
Contenido de `plan-negocio-bar-restaurante` para el grupo A (§2 de la SPEC).

Aquí NO hay lógica: sólo los datos propios de este plan —supuestos, plantilla,
partidas, umbrales y textos legales del checklist— con **la fuente de cada
cifra**. La mecánica (dónde va cada celda, qué fórmula la enlaza y cómo se
reconstruye la hoja) es de `grupo_a.py`, que sirve a los cinco productos de
línea A.

DE DÓNDE SALE CADA NÚMERO — tres orígenes, siempre declarados:

  * «fichero v1.1» — estaba ya en `plan-financiero-bar-restaurante.xlsx` o en
    `checklist-apertura-bar-restaurante.xlsx` y se conserva.
  * «SPEC/R1» — lo fija `planes-v2-SPEC.md` o el hallazgo del R1 que se cita.
  * «parametrizado» — no está en la SPEC ni en el fichero, así que va en celda
    VERDE editable con su nota. Ninguna cifra del sector se teclea sin marcarla
    como parámetro: es la regla dura 6 del encargo.

RECALIBRACIÓN DEL CASO BASE (§7-bis.17, DOM-13, TEC-01)
------------------------------------------------------
El defecto que hunde los cinco planes de línea A es que el P&L imputa 115.200 €
de personal mientras su propia hoja `Personal` suma **209.171,20 €**. Con la
cifra correcta el coste laboral es el **66,3 %** de las ventas, casi el doble
del 35 % que fija `Instrucciones!A13`, y el plan es inviable con sus propios
datos. La SPEC obliga a recalibrar hasta que el caso base pase su propio
semáforo, «por los dos lados y dentro de rangos con fuente», y prohíbe
cuadrarlo tocando un porcentaje escondido.

Lo que se ha hecho, y por qué se puede defender ante un banco:

1. **La plantilla estaba sobredimensionada para el aforo.** El pack describe
   12 mesas × 4 sillas + 8 taburetes = **56 plazas** (`'1. Inversion
   Inicial'!A26:A27` del fichero v1.1) y el propio docx trabaja con **1,8
   rotaciones**, es decir un techo de ~100 cubiertos/día. Siete personas a
   jornada completa (209.171 €) sólo se pagan con ~600.000 € de ventas, que ese
   aforo no da. Se redimensiona por horas de servicio a **7 puestos, tres de
   ellos a tiempo parcial (uno es la línea de suplencias de vacaciones y
   descansos, RC-19)**, con los brutos del propio fichero como referencia y
   el SMI 2026 como suelo: 151.939 €/año.
2. **El ticket pasa a declararse SIN IVA** (TEC-11, DOM-30). Los 18,50 € del
   fichero v1.1 son PVP —así se habla en hostelería—; sin IVA (10 % en sala,
   comida y bebida, RD-17) equivalen a 16,82 €. Se fijó 17,20 € sin IVA y
   RD-08 lo subió a **18,20 € sin IVA**, que son 20,02 € de PVP: dentro del
   rango «15-22 EUR» que declara `Instrucciones!A19` del propio fichero.
3. **Los cubiertos suben de 55 a 80** (1,43 rotaciones sobre 56 plazas), por
   debajo del MÍNIMO de 1,8 que el propio documento pide en temporada alta
   —el caso base se proyecta prudente a propósito— y del techo que se deduce
   de `'3. Punto Equilibrio'`.
4. **El alquiler se queda en 3.000 €/mes** (se probó bajarlo a 2.900 € y
   RD-31 lo revirtió): con el ticket recalibrado son el 8,0 % de las ventas,
   dentro del rango «2.000-4.500 EUR/mes» de `Instrucciones!A20` y del techo
   de 8-10 % de `Instrucciones!A14`.
5. **Aparecen los costes fijos que el plan no tenía y que el checklist sí
   obliga a contratar** (TEC-18): residuos y aceite usado, DDD, derechos de
   autor por la música, PRL, lavandería y reposición de menaje. Todos en celda
   verde con nota de «pide presupuesto en tu zona».

Resultado del caso base (medido en el libro del 2026-09-05): coste de personal
**33,7 %** (techo 34 %), alquiler **8,0 %** (techo 10 %), coste de mercancía
**27,2 %** (techo 32 %) y resultado neto **10,8 %**, algo por encima del
«5-10 %» que el propio libro declara como margen medio del sector. **El plan
ya no se suspende a sí mismo.** Las tres
demostraciones que lo comprueban son las 3, 5 y 6 de §2.11 y las corre
`grupo_a.demos()`.
"""

CONCEPTO = 'Bar-Restaurante / Restaurante Casual'

# ==========================================================================
# §2.1 — `0. Supuestos`
# {clave: (coord, etiqueta, valor, formato, nota, fuente)}
# `None` en coord/etiqueta/formato/nota = se queda el que trae `grupo_a`.
# ==========================================================================
SUPUESTOS = {
    # RD-24 — la nota citaba MAL su fuente: presentaba el 1,8 como un TECHO
    # de rotación cuando el documento del propio producto lo enuncia como
    # «mínimo 1,8 covers por servicio por mesa» y, dos apartados después,
    # como «rotación media de 1,8 servicios diarios en temporada alta». Y las
    # 56 plazas iban escritas a mano, contradiciendo las «40 a 50 comensales
    # en interior» del documento. Ahora el aforo vive en celda (B51), la
    # rotación implícita se CALCULA (B50) y la nota cita literalmente.
    'cubiertos_dia': (
        None, None, 80, None,
        'Comensales servidos al día de media del año, contando todos los '
        'servicios. La rotación que implica sobre el aforo la calcula la '
        'celda «Rotaciones al día implícitas» de esta misma hoja; el '
        'documento del plan pide un MÍNIMO de 1,8 covers por mesa y servicio '
        'en temporada alta',
        'recalibrado §7-bis.17 (v1.1: 55)'),
    'ticket_medio': (
        None, None, 18.20, None,
        'SIN IVA. El PVP equivalente lo calcula la celda «PVP equivalente '
        'con IVA» de abajo (al 10 % en sala son 20,02 € con los supuestos de '
        'partida): dentro del rango 15-22 € que declara este mismo libro y '
        'del 18-25 € que fija el documento del plan',
        'recalibrado por TEC-11/DOM-30 y RD-08 (v1.1: 18,50 € sin declarar si '
        'llevaba IVA; paso intermedio 17,20 €). Única entrada: la de RD-08 '
        'se fundió aquí el 2026-09-05 (RD17-COD-12)'),
    'dias_apertura': (
        None, None, 310, None,
        'Cierre semanal de un día y vacaciones. El MISMO dato lo usan el P&L, '
        'el punto de equilibrio y los escenarios',
        'fichero v1.1'),
    'crec_a2': (None, None, 0.10, None,
                'Segundo año con la clientela ya asentada',
                'parametrizado (v1.1 implicaba 55 → 65 cubiertos = +18 %)'),
    'crec_a3': (None, None, 0.06, None,
                'Tercer año, cerca del techo de rotación del local',
                'parametrizado (v1.1 implicaba 65 → 75 = +15 %)'),
    'coste_comida': (
        None, None, 0.30, None,
        'Food cost objetivo del bar-restaurante casual: 28-32 % según las '
        'referencias de este mismo libro. Se aplica SOLO a la comida',
        'fichero v1.1 (Instrucciones: «Food cost objetivo 28-32 %»)'),
    'coste_bebida': (
        None, None, 0.22, None,
        'Coste de la bebida sobre las ventas de bebida, no sobre el total',
        'fichero v1.1 (rótulo de la fila «Bebidas cost»)'),
    'pct_consumibles': (
        None, None, 0.015, None,
        'Servilletas, papel, productos de limpieza y envases de llevar',
        'parametrizado (v1.1: 4.800 € fijos = 1,5 % de sus ventas)'),
    'pct_delivery': (
        None, None, 0.0, None,
        'A CERO por defecto: si no repartes no arrastras un coste inventado. '
        'Súbelo al peso REAL del canal y la comisión se aplica sólo sobre esa '
        'parte',
        'TEC-23/DOM-34 (v1.1 cobraba el 5 % de TODA la facturación)'),
    'comision_delivery': (
        None, None, 0.28, None,
        'Comisión típica de las plataformas sobre el pedido servido por ese '
        'canal; confírmala en tu contrato antes de proyectar',
        'parametrizado'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado; pide oferta a dos '
        'proveedores de TPV',
        'parametrizado (el plan v1.1 no lo contemplaba)'),
    # RD-31 — el alquiler bajaba de 3.000 a 2.900 €/mes sin ninguna
    # justificación y sin necesidad: es un ajuste a la baja de un coste REAL
    # que arrastra la fianza y el fondo de maniobra. Con el ticket
    # recalibrado, 3.000 € son el 7,9 % de las ventas, dentro del techo de
    # 8-10 % que fija el propio libro.
    'alquiler_mes': (
        None, None, 3000, None,
        'Dentro del rango 2.000-4.500 €/mes que declara este libro para un '
        'local de 80-120 m² en zona urbana, y respetando el techo del 10 % '
        'sobre ventas',
        'fichero v1.1'),
    'fianza_meses': (None, None, 3, None,
                     'Tres meses de renta, como en el contrato tipo de local '
                     'de negocio', 'fichero v1.1'),
    'suministros_mes': (
        None, None, 1800, None,
        'Luz, agua y gas de una cocina con horno, cámaras y campana: pide el '
        'histórico del local antes de firmar',
        'recalibrado (v1.1: 1.200 €/mes, 3,4 % de ventas, por debajo de lo '
        'que consume una cocina caliente)'),
    'seguros_ano': (None, None, 2000, None,
                    'Responsabilidad civil + multirriesgo del local + '
                    'convenio', 'fichero v1.1'),
    'pct_varios': (None, None, 0.02, None,
                   'Colchón de gasto corriente no presupuestado',
                   'fichero v1.1 (rótulo «Varios e imprevistos (2%)»)'),
    'recursos_propios': (
        None, None, 75000, None,
        'Aportación de los socios. Con menos, el banco no entra: pide un '
        '35-40 % de fondos propios sobre la inversión',
        'parametrizado'),
    # Recalibrado al alza porque la inversión creció al incorporar la
    # terraza, las existencias iniciales y los imprevistos de obra que exige
    # §2.2 (RD-02): con 110.000 € el origen de fondos se quedaba 16.629 €
    # por debajo de la necesidad de caja y la hoja de Financiación lo
    # marcaba en ROJO. La cifra sale de la propia celda «Préstamo que
    # ajustaría el origen a la necesidad» de esa hoja.
    'prestamo': (
        None, None, 128000, None,
        'Principal solicitado. La hoja de Financiación comprueba que origen y '
        'usos cuadran, y trae una celda que calcula el importe exacto que los '
        'ajusta',
        'recalibrado (v1.1: 110.000 €; la hoja de Financiación lo cuadra con '
        'la necesidad de caja)'),
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
        'Mínimo que exige este mismo libro: «Fondo de maniobra: mínimo 3 '
        'meses de costes fijos antes de abrir»',
        'SPEC §2.2 / TEC-07 (v1.1 dotaba 30.000 €, que eran 1,8 meses)'),
    'vida_obra': (None, None, 10, None,
                  'Obra, instalaciones y decoración. Coeficientes de la tabla '
                  'del art. 12.1 LIS: confírmalo con tu asesor',
                  'fichero v1.1 (rótulo «Amortizacion equipos (10 anos)»)'),
    # RD-15 — 8 años son el 12,5 % anual, POR ENCIMA del coeficiente lineal
    # máximo de la tabla del art. 12.1 LIS que la propia nota invoca (12 %
    # maquinaria, 10 % mobiliario). El exceso no sería deducible en el
    # ejercicio y la base imponible del modelo quedaba infravalorada.
    'vida_maquinaria': (
        None, None, 10, None,
        'Maquinaria de cocina, mobiliario y equipos. El coeficiente lineal '
        'máximo de la tabla del art. 12.1 LIS es del 12 % para maquinaria y '
        'del 10 % para mobiliario: por debajo de 9-10 años el exceso no es '
        'deducible. Confírmalo con tu asesor',
        'recalibrado por RD-15 (v2.0 previa: 8 años = 12,5 % anual)'),
}

# ---------------------------------------------------------------------------
# §7-bis.17 — recalibración del ticket para cumplir el techo de labour cost
# del 34 % (RD-08). Se hace por el lado del PRECIO, dentro de los dos rangos
# que el propio producto publica: 15-22 € de PVP en el bloque de referencias
# del libro y «ticket medio objetivo de 18 a 25 euros» en el documento. NO se
# toca ningún porcentaje escondido.
# ---------------------------------------------------------------------------
# (El valor de RD-08 —18,20 €— vive en la ÚNICA entrada `ticket_medio` de
# SUPUESTOS: tener dos, una muerta a diez líneas de la viva, dejó publicada
# una tabla de recalibrado con 17,20 € cuando B5 valía 18,20.)

# ==========================================================================
# §2.3.2 — líneas de venta y su peso (resuelve el doble conteo de la bebida)
# (rótulo, peso sobre ventas, grupo, nota, fuente)
# ==========================================================================
LINEAS_INGRESO = (
    ('Ventas de comida (cocina y barra)', 0.65, 'comida',
     'Menú del mediodía, carta y raciones',
     'fichero v1.1: el rótulo de la fila de bebidas decía «ingresos bebida '
     '~35%», así que la comida es el 65 % restante'),
    ('Ventas de bebida (cañas, vinos, cafés y copas)', 0.35, 'bebida',
     'Se calcula como el resto: comida + bebida = 100 %',
     'fichero v1.1'),
)

# ==========================================================================
# §2.6 — plantilla redimensionada
# (puesto, personas, bruto mes TOTAL de la fila, nota, fuente, jornada)
# La JORNADA es el porcentaje sobre la completa del convenio: el semáforo del
# SMI compara contra el SMI en proporción, así que un contrato de 20 h no
# aparece en rojo por cobrar menos que una jornada entera.
# ==========================================================================
PLANTILLA = (
    ('Gerente / Propietario', 1, 1900,
     'Trabaja en sala: compras, cierre de caja, proveedores y RRSS',
     'recalibrado (v1.1: 2.200 €)', 1.0),
    ('Jefe de cocina', 1, 1800,
     'Escandallos, pedidos y línea caliente',
     'recalibrado (v1.1: 2.000 €)', 1.0),
    ('Ayudante de cocina', 1, 1250,
     'Mise en place, fríos y limpieza de cocina. Por encima del SMI de '
     'jornada completa', 'recalibrado (v1.1: 1.300 €)', 1.0),
    ('Camarero/a de barra y sala', 1, 1300,
     'Jornada completa, con el servicio de mediodía y el de noche',
     'fichero v1.1', 1.0),
    ('Camarero/a a tiempo parcial', 1, 1000,
     'Refuerzo de los dos servicios fuertes, 30 horas semanales',
     'recalibrado (v1.1: dos camareros a jornada completa)', 0.75),
    ('Extra de fin de semana', 1, 650,
     'Viernes, sábado y domingo, 20 horas semanales',
     'parametrizado', 0.50),
    # RC-19 — la plantilla no tenía ninguna fila de suplencias, vacaciones ni
    # descansos, que el convenio provincial que el propio libro invoca sí
    # impone: seis personas con 30 días naturales de vacaciones (art. 38 ET)
    # son 180 días de servicio que alguien tiene que cubrir.
    ('Suplencias de vacaciones y descansos', 1, 260,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso '
     'semanal de los seis puestos. Equivale a una jornada del 15 %',
     'parametrizado (RC-19)', 0.15),
)

# ==========================================================================
# §2.2 — partidas de la inversión (RD-01, RD-02, RC-01, RC-02, RT-14)
# ==========================================================================
#: Reglas por rótulo NORMALIZADO: `('suprimir', motivo)` o `(importe, nota)`.
INVERSION = {
    # RD-01 / RC-01 / RT-14 — doble conteo de 3.800 € entre la inversión y el
    # año 1 del P&L: el seguro y la gestoría del primer año se capitalizaban
    # en la inversión Y se volvían a cargar como coste fijo anual. Es el
    # mismo defecto que la SPEC §3.4.1 obliga a quitar en la línea B
    # (TEC-12). Se quedan en el P&L, que es donde son gasto del ejercicio, y
    # salen de la inversión.
    'alta gestoria + contabilidad primer ano': (
        'suprimir',
        'RD-01: la anualidad de gestoría ya está en «Gestoría + '
        'contabilidad» de los costes fijos del P&L. El alta en sí no llega a '
        'los 100 € y va dentro de los gastos de constitución'),
    'seguros (rc + multirriesgo + empleados)': (
        'suprimir',
        'RD-01: la prima del primer año ya está en «Seguros (RC + '
        'multirriesgo)» de los costes fijos del P&L. Capitalizarla además '
        'inflaba el IVA soportado y la necesidad de financiación'),
}

#: Partidas nuevas: `(bloque, rótulo, importe, nota, fuente)`.
#: RD-02 / RC-02 — DOM-19 seguía abierto: terraza, stock inicial e
#: imprevistos sólo existían en el Word, y la propia nota de la hoja los
#: citaba como si estuvieran. Un bar-restaurante que abre sin presupuesto de
#: primera compra de bodega y despensa no es financiable. Los imprevistos NO
#: van aquí: los calcula `grupo_a` por fórmula sobre el bloque de obra.
INVERSION_EXTRA = (
    ('EQUIPAMIENTO SALA Y BARRA', 'Mobiliario y toldo de terraza', 4200,
     'Mesas, sillas, toldo y estufas para las plazas de terraza que describe '
     'el plan. Ponlo a 0 si tu local no tiene terraza o si la licencia no '
     'sale', 'parametrizado (RD-02/DOM-19)'),
    ('EXISTENCIAS INICIALES',
     'Primera compra de despensa y cámaras', 6500,
     'Materia prima para arrancar el servicio: seco, fresco y congelado. NO '
     'se amortiza, es circulante', 'parametrizado (RD-02/DOM-19)'),
    ('EXISTENCIAS INICIALES', 'Primera compra de bodega y barra', 5500,
     'Vinos, cervezas, destilados y refrescos de la carta de salida. Pide '
     'depósito a tus distribuidores antes de presupuestarlo',
     'parametrizado (RD-02/DOM-19)'),
)

# ==========================================================================
# §2.3 — costes fijos que el plan v1.1 no tenía y el checklist sí obliga
# (rótulo, importe, nota, fuente)
# ==========================================================================
FIJOS_EXTRA = (
    ('Limpieza, lavandería y lencería', 3600,
     'Mantelería, paños y uniformes. Pide presupuesto en tu zona: es un '
     'importe orientativo y editable', 'parametrizado (TEC-18)'),
    ('Gestión de residuos y de aceite vegetal usado', 1200,
     'Gestor autorizado. Lo pide la inspección y el aceite no puede ir al '
     'desagüe', 'parametrizado (TEC-18)'),
    ('Desinsectación, desratización y desinfección (DDD)', 900,
     'Empresa inscrita en el ROESB; forma parte del plan APPCC',
     'parametrizado (TEC-18)'),
    ('Derechos de autor por música ambiental', 900,
     'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los '
     'metros y del aforo', 'parametrizado (TEC-18)'),
    ('Prevención de riesgos laborales y vigilancia de la salud', 600,
     'El plan de prevención es obligatorio; el proveedor externo, no (art. '
     '30.5 de la Ley 31/1995)', 'parametrizado (DOM-26)'),
    ('Comisiones de reservas online', 2400,
     'TheFork y similares cobran por comensal sentado: mira la letra pequeña '
     'antes de firmar', 'parametrizado'),
    ('Reposición de menaje, cristalería y vajilla', 2400,
     'Roturas del ejercicio. En un casual con barra se rompe más de lo que '
     'se presupuesta', 'parametrizado'),
)

# ==========================================================================
# §2.9 — umbrales que auditan el caso base (clave, rótulo, valor, comentario)
# Los rótulos los pone `grupo_a`; aquí van el valor y el comentario.
# ==========================================================================
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.65,
     'Por debajo, revisa precios de carta y escandallos'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.32,
     'Techo del propio libro: «Food cost objetivo 28-32 %»'),
    # RD-08 — el producto publicaba TRES techos de labour cost (35 % en el
    # Excel, 34 % y 30-35 % en el documento) y el caso base se declaraba
    # viable contra el más laxo de los tres. Se elige el MÁS ESTRICTO que el
    # producto publica, y el caso base se recalibra hasta cumplirlo (§2.3.1).
    ('r_personal', 'Coste de personal / Ventas', 0.34,
     'Techo MÁS ESTRICTO de los que publica este producto: «el labor cost no '
     'debe superar el 34 %». Es el que manda'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del propio libro: «Alquiler: no superar 8-10 % de los ingresos»'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo del propio libro: «Margen neto medio sector: 5-10 %»'),
)

# ==========================================================================
# §2.5 — escenarios extremos (cubiertos/día, ticket sin IVA, días)
# El «Realista» NO se teclea: lo lee de Supuestos y reproduce el P&L.
# ==========================================================================
ESCENARIOS = {
    'pesimista': (58, 15.90, 300),
    'optimista': (95, 18.50, 320),
}

# ==========================================================================
# §2.7 — reparto de la actividad por mes (suma 1)
# ==========================================================================
#: Estacionalidad de un bar-restaurante urbano: agosto flojo por vacaciones,
#: diciembre fuerte por comidas de empresa. Es un PARÁMETRO editable: si tu
#: zona es de costa, el perfil se invierte.
ESTACIONALIDAD = (0.070, 0.072, 0.082, 0.085, 0.090, 0.088,
                  0.085, 0.062, 0.085, 0.088, 0.087, 0.106)

# ==========================================================================
# §2.9 — textos de la hoja de Instrucciones
# ==========================================================================
INSTRUCCIONES = {
    'uso': [
        '6. La hoja «6. Tesorería 12 meses» responde la pregunta que decide '
        'una operación bancaria: en qué mes se agota la caja. El saldo mínimo '
        'del año nunca puede salir en rojo.',
        '7. La hoja «7. Financiación» cuadra lo que hace falta con lo que se '
        'aporta y monta el cuadro de amortización del préstamo. Si la '
        'diferencia sale en rojo, el plan no está financiado.',
    ],
    # (rótulo, valor, FUENTE, nota). RD-33: la fuente va en su propia
    # columna, también en la fila del ticket, que era la única que no la
    # llevaba pese a venir del mismo sitio que las demás.
    # RD-04 / RC-09: el post-proceso había BORRADO del bloque las tres filas
    # que el nuevo caso base contradice o que aportan el riesgo —la inversión
    # media de apertura y las dos tasas de cierre—, y son justo las que la
    # landing sigue vendiendo. Vuelven, con su fuente, y la de la inversión
    # con la nota de que este plan queda por encima del rango.
    'referencias': [
        # ⚠️ sin importe en la frase: `motor.cross_sell_sin_precios` borra los
        # euros de cualquier línea que hable de un «plan», y se llevaba por
        # delante el PVP. La cifra vive calculada en «0. Supuestos».
        ('Ticket medio de restaurante casual (PVP)', '15-22 €',
         'Fichero v1.1',
         'El PVP equivalente de este plan lo calcula la hoja 0. Supuestos'),
        ('Alquiler de local de 80-120 m² en zona urbana', '2.000-4.500 €/mes',
         'Fichero v1.1', ''),
        ('Food cost objetivo', '28-32 %', 'Fichero v1.1', ''),
        ('Coste de personal sobre ventas', 'máx. 34 %', 'Fichero v1.1',
         'Se aplica el más estricto de los techos que publica este producto'),
        ('Margen neto medio del sector', '5-10 %', 'Fichero v1.1', ''),
        ('Punto de equilibrio', 'alcanzable en menos de 12 meses',
         'Fichero v1.1', ''),
        ('Inversión media de apertura', '80.000-150.000 €', 'Fichero v1.1',
         'Es el rango de referencia del sector. La inversión de ESTE plan la '
         'calcula la hoja 1: si queda por encima, es porque incluye el fondo '
         'de maniobra, las existencias iniciales y el IVA que hay que '
         'adelantar, que ese rango no siempre cuenta'),
        ('Tasa de cierre de restaurantes en el primer año', '25 %',
         'Fichero v1.1',
         'Es el dato que más pesa en un comité de riesgos: por eso el plan '
         'lleva fondo de maniobra, escenario pesimista y tesorería mes a mes'),
        ('Tasa de cierre de restaurantes a los cinco años', '50 %',
         'Fichero v1.1', ''),
        ('Convenio colectivo aplicable', 'PROVINCIAL de hostelería',
         'DOM-24 / checklist F37',
         'No existe una tabla salarial estatal única: copia la tabla de tu '
         'provincia en la celda de Supuestos'),
    ],
}

# ==========================================================================
# §2.10 — checklist de apertura: legal vigente y sin inventos
# ==========================================================================
CHECKLIST = {
    # (patrón que busca, texto nuevo). Se aplica celda a celda.
    'reemplazos': [
        # DOM-08 / COM-11 — el carnet de manipulador está DEROGADO
        (r'^Carnet de manipulador',
         'Formación en higiene alimentaria de todo el equipo'),
        # la responsabilidad de la formación es de la EMPRESA, no del empleado
        (r'^Empleados$', 'Titular'),
        (r'^Obligatorio, online',
         'El «carnet de manipulador» está derogado (RD 109/2010): la '
         'formación la acredita la EMPRESA y se documenta en el plan APPCC'),
        # DOM-09 — el RGSEAA no aplica al minorista que sirve al consumidor
        (r'^Autorizaci[óo]n sanitaria de funcionamiento',
         'Inscripción en el Registro Sanitario de tu Comunidad Autónoma '
         '(declaración responsable de inicio de actividad alimentaria)'),
        (r'^Registro RGSEAA$',
         'El Registro General Sanitario estatal NO aplica al minorista que '
         'sirve al consumidor final (art. 2.2 del RD 191/2011): el que te '
         'toca es el autonómico'),
        # DOM-25 — la cuota de autónomo, parametrizada y con nota de año
        (r'^Tarifa plana 80 EUR/mes',
         'Cuota según la base mínima del tramo que te corresponda. Consulta '
         'el importe del ejercicio en curso y verifica con tu gestoría si te '
         'aplica la cuota reducida de inicio de actividad'),
        # DOM-26 — el PRL obligatorio es el PLAN, no el proveedor
        (r'^Obligatorio contratar servicio externo',
         'Obligatorio es el PLAN de prevención, no contratar un servicio '
         'ajeno: con menos de 25 trabajadores y un solo centro el empresario '
         'puede asumir la actividad preventiva (art. 30.5 de la Ley 31/1995 '
         'y art. 11 del RD 39/1997)'),
        # TEC-25 / DOM-33 — el epígrafe de IAE, con los dos que pueden tocar
        (r'^Alta en el IAE',
         'Alta en el IAE: epígrafe 671.4 (restaurantes de dos tenedores) o '
         '673.1 (servicios de bar especiales), según el peso de la barra'),
        # RC-25 — la nota explicaba la exención por cifra de negocio y
        # omitía la de los DOS PRIMEROS ejercicios para entidades de nueva
        # creación, que es justo la que aplica al comprador de un plan de
        # apertura. ⚠️ El texto final se escribe de UNA vez: encadenar dos
        # reemplazos (uno al texto intermedio y otro al definitivo) rompe la
        # idempotencia, porque la 2.ª pasada corrige lo que hizo la 1.ª.
        (r'^(Exento si facturaci[oó]n|Exento mientras la cifra)',
         'Doble exención: los dos primeros períodos impositivos de la '
         'actividad (art. 82.1.b del TRLRHL) y, después, mientras la cifra '
         'de negocio no llegue al millón de euros. La elección del epígrafe '
         'la valida tu gestor: condiciona inspecciones y licencia'),
        # DOM-13 / COM-08 — Crea y Crece, sin el depósito de 3.000 € inventado
        (r'^Ley Crea y Crece',
         'Ley 18/2022 (Crea y Crece): capital mínimo 1 €, con la obligación '
         'de destinar el 20 % del beneficio a reserva legal hasta que capital '
         'y reserva sumen 3.000 €, y responsabilidad solidaria de los socios '
         'por esa diferencia'),
        (r'^Capital social min 1 EUR',
         'Capital social mínimo 1 € (Ley 18/2022). No existe ningún depósito '
         'obligatorio de 3.000 € a cinco años'),
        # DOM-26 / RD-29 / RC-24 — la nota decía que el servicio ajeno NO es
        # obligatorio y la columna RESPONSABLE seguía asignando la tarea a un
        # «Servicio PRL» externo: la celda que el usuario lee para saber a
        # quién llamar contradecía a la que explica la ley.
        (r'^Servicio PRL$', 'Titular o servicio ajeno'),
        (r'^Prevención riesgos laborales$',
         'Plan de prevención de riesgos laborales (asumido por el titular o '
         'con servicio ajeno)'),
        # RC-25 — DOM-33 pedía DOS cosas y sólo se hizo una: faltaba la
        # exención de los dos primeros ejercicios para entidades de nueva
        # creación, que es justo la que aplica al comprador de un plan de
        # apertura. Y TEC-25 dejaba el 671.4 («dos tenedores») como primera
        # opción para un casual con ticket de 20,02 € de PVP.
        # (Tabla de recalibrado y notas al cliente: lenguaje llano, sin ids
        # internos; los ids van en los comentarios del código, CON-08.)
        (r'^Alta en el IAE',
         'Alta en el IAE: epígrafe 671.5 (restaurantes de un tenedor), 671.4 '
         '(dos tenedores) o 673.1 (servicios de bar especiales), según el '
         'peso de la barra y el nivel de servicio'),

        # TEC-26 — la errata visible del entregable
        (r'Priorizarcexperiencia',
         'Prioriza la experiencia en hostelería'),
    ],
    # DOM-09 — la segunda fila del RGSEAA duplicaba el trámite
    'suprimir': [
        'Inscripcion Registro General Sanitario',
        'Inscripción Registro General Sanitario',
    ],
    # DOM-23 — UN solo cronograma, el conservador: si las licencias tardan
    # 1-3 meses y la obra 4-8 semanas, no se puede abrir el mes 6
    'fases': {
        r'^FASE 1': 'FASE 1: CONSTITUCIÓN DE LA EMPRESA (meses 1-2)',
        r'^FASE 2': 'FASE 2: LOCAL Y LICENCIAS (meses 2-6)',
        r'^FASE 3': 'FASE 3: OBRA Y EQUIPAMIENTO (meses 4-7)',
        r'^FASE 4': 'FASE 4: PERSONAL (mes 7)',
        r'^FASE 5': 'FASE 5: MARKETING Y LANZAMIENTO (meses 7-8)',
        # ⚠️ la fase de los primeros 90 días se identifica por su CONTENIDO,
        # no por su número: `_altas_checklist` la renumera al empujarla por
        # debajo del bloque nuevo (RD-28), y un patrón por número renombraría
        # en la 2.ª pasada el bloque equivocado.
        r'^FASE \d+: PRIMEROS 90': 'FASE 7: PRIMEROS 90 DÍAS (meses 8-11)',
    },
    'cabecera_altas': 'FASE 6: OBLIGACIONES QUE HAY QUE TENER CERRADAS ANTES '
                      'DE ABRIR (meses 6-8)',
    # RD-28 / RC-12 — un checklist se trabaja de arriba abajo. Con el bloque
    # nuevo añadido al final, el seguro de RC, los boletines de gas y la
    # gestión de residuos quedaban DESPUÉS de los primeros 90 días de
    # operación, es decir se contrataban con el local ya abierto. La fase de
    # los primeros 90 días se empuja hacia abajo y queda la última.
    'fase_final': r'^FASE \d+: PRIMEROS 90',
    'fase_final_nueva': 'FASE 7: PRIMEROS 90 DÍAS (meses 8-11)',
    # TEC-18 — trámites que faltaban y cuestan dinero o multa
    # (hoja, categoría, tarea, responsable, plazo, nota)
    'altas': [
        ('.', 'Seguros',
         'Contratar el seguro de responsabilidad civil y el multirriesgo del '
         'local', 'Socios', 'Antes de abrir',
         'Está presupuestado en la hoja de Inversión y hasta ahora no había '
         'ninguna tarea que lo ejecutara'),
        ('.', 'Legal',
         'Hojas de reclamaciones oficiales y su cartel anunciador', 'Socios',
         '1 día',
         'El modelo y el texto del cartel los aprueba tu Comunidad '
         'Autónoma'),
        ('.', 'Laboral',
         'Registro horario diario de la jornada de todo el equipo',
         'Gestoría', 'Desde el primer contrato',
         'Art. 34.9 del Estatuto de los Trabajadores; se conserva cuatro '
         'años'),
        ('.', 'Legal',
         'Contrato con gestor autorizado de residuos y de aceite vegetal '
         'usado', 'Socios', '2 semanas',
         'Se comprueba en la inspección; el aceite usado no puede ir al '
         'desagüe'),
        ('.', 'APPCC',
         'Contrato de desinsectación, desratización y desinfección (DDD)',
         'Socios', '1 semana',
         'Empresa inscrita en el ROESB; el certificado forma parte del plan '
         'APPCC'),
        ('.', 'Legal',
         'Licencia de derechos de autor por la música ambiental', 'Socios',
         '2 semanas',
         'SGAE y AGEDI-AIE son dos licencias distintas y se pagan las dos'),
        ('.', 'APPCC',
         'Plan de prevención de las pérdidas y el desperdicio alimentario',
         'Cocina', '1 semana',
         'Ley 1/2025: obliga a tener un plan escrito y a ofrecer la comida '
         'sobrante para donación'),
        ('.', 'Obra',
         'Boletines de la instalación eléctrica y de la instalación de gas',
         'Instalador', 'Con la obra',
         'Sin ellos no hay alta de suministros ni licencia de actividad'),
        ('.', 'Laboral',
         'Comunicación de apertura del centro de trabajo a la autoridad '
         'laboral', 'Gestoría', 'Primeros 30 días',
         'Se presenta en los treinta días siguientes al inicio de la '
         'actividad'),
        ('.', 'Legal',
         'Cartel de prohibición de venta de alcohol y tabaco a menores',
         'Socios', '1 día',
         'La redacción exacta y el tamaño los fija tu Comunidad Autónoma'),
        # RD-26 — en 59 trámites no había NI UNO de protección de datos. Un
        # bar-restaurante con reservas online, fichaje de jornada,
        # videovigilancia y proveedores trata datos personales desde el día
        # uno, y la AEPD sanciona la falta de registro de actividades y de
        # cartel de videovigilancia.
        ('.', 'RGPD',
         'Registro de actividades de tratamiento de datos personales',
         'Socios', 'Antes de abrir',
         'Art. 30 del RGPD y art. 31 de la LOPDGDD: lo pide la AEPD en la '
         'primera inspección. Incluye clientes, personal y proveedores'),
        ('.', 'RGPD',
         'Informar al equipo del registro horario y del tratamiento de sus '
         'datos', 'Gestoría', 'Desde el primer contrato',
         'La cláusula informativa se entrega con el contrato; el fichaje es '
         'un tratamiento de datos, no sólo una obligación laboral'),
        ('.', 'RGPD',
         'Cartel y contrato de videovigilancia con la empresa de seguridad',
         'Socios', 'Con la obra',
         'Cartel homologado en zona visible, contrato de encargado de '
         'tratamiento y plazo máximo de conservación de 30 días'),
        ('.', 'RGPD',
         'Cláusula informativa y consentimiento en el sistema de reservas y '
         'en la lista de correo', 'Socios', 'Antes de abrir',
         'Reservas online, WhatsApp y newsletter tratan datos: cada canal '
         'necesita su información previa'),
        # RD-27 — ningún ítem sobre la adaptación del sistema de facturación,
        # que es una obligación viva en el ejercicio que el propio fichero
        # rotula «España 2026» y que obliga a cambiar o actualizar el TPV que
        # la hoja de inversión presupuesta.
        ('.', 'Fiscal',
         'Adaptar el TPV y la facturación al sistema Veri*factu / factura '
         'electrónica', 'Gestoría', 'Antes de abrir',
         'El RD 1007/2023 y su calendario escalonado obligan a que el '
         'software de facturación sea verificable. Consulta la fecha que te '
         'aplica antes de comprar el TPV que presupuesta la hoja de '
         'Inversión: cambiarlo después cuesta el doble'),
    ],
}

# ==========================================================================
# Registro de lo que cambia de valor respecto de la v1.1 (§1.3: «la
# diferencia entre el valor viejo y el nuevo queda anotada por fichero»)
# ==========================================================================
# La columna «Por qué» la LEE EL CLIENTE (Instrucciones): lenguaje llano y sin
# códigos internos de auditoría. Trazabilidad, por fila: TEC-01/DOM-01 ·
# §7-bis.17 + RC-19 · RD-24 · TEC-11/DOM-30 + RD-08 · RD-31 · — · TEC-07/
# DOM-12/NUEVO-01 · TEC-20 · TEC-10/DOM-15 · TEC-06/DOM-15 · TEC-23/DOM-34 ·
# TEC-04/DOM-04.
RECALIBRADO = (
    ('Coste de personal imputado al P&L', '115.200 €',
     'Sale de la hoja Personal, por fórmula',
     'El P&L decía «ver hoja Personal» y usaba otra cifra; ahora lee la '
     'hoja'),
    ('Plantilla', '7 personas / 209.171 €',
     '7 puestos, tres a tiempo parcial (uno de ellos, suplencias) / '
     '151.939 €',
     'Dimensionada por horas de servicio para 56 plazas; con la plantilla '
     'anterior el coste laboral era el 66,3 % de las ventas'),
    ('Cubiertos/día del año 1', '55', '80',
     '1,43 rotaciones sobre las 56 plazas del propio pack; el documento pide '
     'un MÍNIMO de 1,8 en temporada alta, así que el caso base se proyecta '
     'por debajo a propósito'),
    ('Ticket medio', '18,50 € (sin declarar IVA)', '18,20 € SIN IVA',
     'El ticket de la versión 1.1 no decía si llevaba IVA; ahora se declara '
     'sin IVA y equivale a 20,02 € de PVP al 10 % en sala, dentro del rango '
     '15-22 € del propio libro'),
    ('Alquiler', '3.000 €/mes', '3.000 €/mes (sin cambio)',
     'Con el ticket recalibrado son el 8,0 % de las ventas, dentro del techo '
     'de 8-10 % del propio libro'),
    ('Suministros', '1.200 €/mes', '1.800 €/mes',
     'Una cocina con horno, cámaras y campana no consume el 3,2 % de las '
     'ventas'),
    ('Fondo de maniobra', '30.000 € etiquetados «3 meses»',
     '3 × costes fijos de caja mensuales, por fórmula',
     'Los 30.000 € cubrían 1,8 meses, no 3'),
    ('Amortización', '5.000 €/año (base implícita 50.000 €)',
     'Base amortizable real / vida útil, por fórmula',
     'El inmovilizado del propio libro suma bastante más, y el fondo de '
     'maniobra no se amortiza'),
    ('Cuota del préstamo en el P&L', '7.200 €/año de cuota completa',
     'sólo los intereses; el principal va a tesorería',
     'Meter la cuota entera antes del resultado convierte el P&L en un flujo '
     'de caja'),
    ('Impuesto de Sociedades', '25 % en los años 2 y 3, sin compensar la BIN',
     '15 % los dos primeros ejercicios con base positiva y compensación de '
     'bases negativas',
     'Artículos 26 y 29.1 de la Ley del Impuesto sobre Sociedades'),
    ('Comisiones de delivery', '5 % de TODA la facturación, sin interruptor',
     '% del canal × comisión de la plataforma, a 0 por defecto',
     'Si no repartes, no arrastras un coste inventado'),
    ('Coste de la bebida', 'food cost del 30 % sobre el total MÁS un 22 % '
     'sobre la bebida', 'cada familia paga su propio coste',
     '33.119,63 € cobrados dos veces en el año 1'),
)
