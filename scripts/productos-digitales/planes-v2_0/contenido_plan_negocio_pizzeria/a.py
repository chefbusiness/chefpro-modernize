#!/usr/bin/env python3
"""
Contenido de `plan-negocio-pizzeria` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Camino de la Heladería ES 1.0 con semilla del Tapas Bar
ES 2.2: `plan-pizzeria/semilla_piz.py` copia los dos xlsx publicados del tapas bar (solo lectura), les pone las 18
partidas, los 9 fijos y los títulos de la pizzería, y `main.py` + `grupo_a.py` los reconstruyen con este módulo
(mecánica del tapas bar: dos servicios, producción antes de abrir, rotación encendida; formato de la heladería).
SPEC: `plan-pizzeria/SPEC.md` (D1-D19); cómo se construye: `plan-pizzeria/F1-camino.md` §1-§3; caso:
`plan-pizzeria/F1-research-pizzeria.md` §3; normativa: ídem §0-§1.

MOTOR DE INGRESOS (restaurante de dos servicios con para llevar y domicilio)
---------------------------------------------------------------------------
    cubiertos_dia (B4) = COMENSALES EQUIVALENTES AL DÍA (51 de sala + 15 de llevar y domicilio)   66
    ticket_medio  (B5) = € POR COMENSAL SIN IVA                                                 19,50 €
    dias_apertura (B6) = DÍAS DE APERTURA AL AÑO                                                300
Ventas a régimen = 66 × 19,50 × 300 = 386.100 €. La estacionalidad va ROTADA: el Mes 1 de la Tesorería es SEPTIEMBRE
(SPEC D7), por eso las pagas extra salen en los meses 11 (julio) y 4 (diciembre).

IVA (SPEC D6): la comida al 10 % (sala, llevar y domicilio, sin partir); la bebida con la LÍNEA PARTIDA del motor
(`grupo_a.py:2291-2314`): su columna H («Bebida para llevar o a domicilio al 21 %») declara la parte que sale del local
al tipo general (alcohol y refrescos con azúcares añadidos), H = 7 %; el resto, al 10 %. Con la línea partida,
`iva_bebida` (B63) no tiene efecto y `pct_bebida_alc` (B62) sólo mueve el IVA SOPORTADO de la compra de bebida: por eso
lleva rótulo propio y vale el 80 % de la compra (cerveza, vino y refrescos con azúcar al 21 %; agua y café al 10 %).
`IVA_COMPRAS` es la compra de COMIDA (6,4 %); con la bebida al 18,8 %, la compra entera sale al 8,9 % del research.

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §n» = `F1-research-pizzeria.md` §n (casi
todo [estimado], criterio de kit, con el cálculo a la vista); «BOE» / «DOUE» = norma leída en origen en la F1;
«calibrado D9» = ajustado en F2 para cumplir los gates del caso de la SPEC.

⚠️ Rótulos de importe: sin «comensales», «personas», «días», «meses», «años», «plazas» ni «unidades»
(`motor.RX_RECUENTO_DV` les quita el formato de euro). Las notas no usan «cubierto» (el VOCABULARIO lo traduce) ni
«tapa», «helado» o «pasteurizar» (restos del molde que caza `barrido_es.py`). Sesión Claude Code, 25-oct-2026.
"""

CONCEPTO = 'Pizzería Napolitana'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Masculino «comensal» = masculino
#: «cubierto»: sin arreglos de concordancia. Las frases largas traducen al caso las tres frases del motor que
#: hablan del «alcohol que sale por delivery» (F1-camino §1) y los restos de otros moldes.
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubierto': 'comensal',
    'cubiertos': 'comensales',
    # las tres frases del motor (F1-camino §1): la línea partida de la bebida, no el canal de delivery
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'la bebida que sale para llevar o a domicilio (columna H de su línea en el P&L) mueve',
    'el libro lo aplica al alcohol del canal de delivery':
        'el libro lo aplica a la parte de la bebida que declara la columna H de su línea en el P&L',
    'que repercutes por el alcohol que sale por delivery':
        'que repercutes por la bebida que sale para llevar o a domicilio',
    'El alcohol servido en sala va al reducido: su tipo está en el bloque de desglose del IVA':
        'El alcohol servido en sala va al reducido, como fija la línea de bebida del P&L',
    'El libro manda al general sólo el alcohol: si compras refrescos o zumos con azúcares añadidos, su factura '
    'también va al 21':
        'En las compras, el libro manda al general la parte de la bebida que declara la celda «Bebida que compras al '
        '21 %» de esta hoja: la cerveza, el vino y los refrescos con azúcares añadidos, cuya factura va al 21',
    'el alcohol que sale por delivery, al general; el pan común y las harinas panificables, al superreducido (art. '
    '91.Dos.1.1.º':
        'la parte de la bebida que sale para llevar o a domicilio y declara la columna H de su línea (alcohol y '
        'refrescos con azúcares añadidos), al general (art. 91.Uno.1.1.º',
    'los alimentos —bollería y pastelería incluidas—, que son':
        'los alimentos —las pizzas incluidas—, que son',
    # resto del molde en Tesorería!D31 (barrido_es.py: «versión 1.1»; = heladería)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # SPEC D7: las dos notas de la Tesorería con el Mes 1 en septiembre
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = SEPTIEMBRE: el plan abre después del verano para llegar a la Navidad con clientela y a enero y '
        'febrero (Meses 5 y 6, los más flojos) con el fondo intacto. El pico es diciembre (Mes 4) y el valle, enero '
        '(Mes 5), con dos semanas de cierre. Si abres en otro mes, gira la fila',
    'El IVA del cuarto trimestre se liquida en enero del año siguiente, así que no aparece en este cuadro':
        'Los trimestres de esta hoja son de tres meses del plan (septiembre-noviembre, diciembre-febrero, marzo-mayo '
        'y junio-agosto), no los naturales: con el Mes 1 en septiembre, el modelo 303 se presenta en octubre (por '
        'septiembre), enero (por octubre-diciembre), abril (por enero-marzo) y julio (por abril-junio); el de julio '
        'y agosto (Meses 11 y 12) se presenta en octubre del año 2',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 66, None,
        'Comensales equivalentes al día, media del año: unos 51 en sala (la terraza incluida de abril a octubre) y unos '
        '15 de para llevar y domicilio, que son los pedidos (unos 13 al día de unos 23 € sin IVA) divididos por el '
        'ticket. Un sábado, unos 110; un martes, unos 45. Contrástalo con el paso de gente de tu calle un viernes por '
        'la noche y un martes a mediodía',
        'research §3 [estimado]'),
    'ticket_medio': (
        None, None, 19.50, None,
        'SIN IVA, por comensal: medio entrante, una pizza, 1,3 bebidas y algún postre o café, unos 22 € con IVA en sala. '
        'La Margherita de la carta del caso cuesta 10 € con IVA, en la parte baja de la mediana de 10,90 € de 14 '
        'pizzerías de Madrid, Barcelona, Valencia, Marbella y Tenerife (octubre de 2026). El precio con IVA está en la '
        'fila «PVP equivalente con IVA» de abajo',
        'research §2-§3 (carta del caso) [estimado]'),
    'dias_apertura': (
        None, None, 300, None,
        '365 días menos los 52 lunes de cierre, dos semanas de cierre en enero (mantenimiento del horno y vacaciones) '
        'y el 25 de diciembre. Es el MISMO dato para la cuenta de resultados, el punto de equilibrio, los escenarios '
        'y las horas de personal',
        'research §3 [estimado]'),
    'crec_a2': (
        None, None, 0.06, None,
        'Clientela de barrio que repite y más recogida en el local el segundo año. Se aplica a los comensales con el '
        'mismo ticket; el personal NO sube con este porcentaje: sale de la hoja Personal',
        'research §3 [estimado]'),
    'crec_a3': (
        None, None, 0.04, None,
        'Sobre el año 2. Conservador: es un mercado maduro y el techo lo ponen el horno y las 50 plazas los viernes '
        'y los sábados por la noche',
        'research §3 [estimado]'),
    'pct_comida': (
        None, None, 0.82, None,
        'Pizzas, entrantes y postres (en sala, para llevar y a domicilio) sobre las ventas; el 18 % restante es la '
        'bebida. Es el peso de la primera línea de ventas del P&L',
        'research §3 [estimado] · SPEC D5 (82/18)'),
    'coste_comida': (
        None, None, 0.235, None,
        'Materia prima de la comida sobre sus ventas: las pizzas (el 70 % de la comida) salen a un 20 % de media (la '
        'Margherita, a un 15 %; con búfala, burrata o embutido italiano, al 22-28 %), los entrantes al 28 % y los '
        'postres al 25 %, y el plan suma 1,5 puntos de merma (bolas pasadas, masa sobrante y pruebas). Escandalla '
        'cada pizza con la calculadora del pack',
        'research §2-§3 [estimado]'),
    'coste_bebida': (
        None, None, 0.27, None,
        'Cerveza al 30 %, vino al 35 %, refrescos al 35 % y agua y café al 20 % de su precio de venta. Si la cervecera '
        'te cede el equipo de tiraje, pide el precio del barril por escrito',
        'research §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Cajas de cartón para las pizzas que salen del local (unas 8.000 al año a 1 € cada una, el 2,1 % de las '
        'ventas), papel, servilletas y los envases para que el cliente se lleve lo que no consuma (Ley 1/2025, '
        'art. 8). El envase de plástico de un solo uso se cobra aparte en el tique (Ley 7/2022, art. 55)',
        'research §1-§3 [estimado] · BOE'),
    'pct_delivery': (
        None, None, 0.10, None,
        'Ventas por PLATAFORMA con su reparto (Glovo, Just Eat, Uber Eats) sobre el total. La recogida en el local y '
        'el reparto propio NO pagan comisión y no van aquí. La pizza de masa blanda llega peor que otros platos: no '
        'subas de aquí sin probarlo',
        'research §3 [estimado]'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión de la plataforma con su reparto sobre lo que vende ese canal: el plan básico de Uber Eats ronda el '
        '30 % más IVA y Glovo y Just Eat, del 25 al 35 % según la zona. Compruébala en tu contrato. Si repartes tú, '
        'pon 0 y suma el repartidor, con contrato laboral, a la hoja Personal',
        'research §2-§3 (guías del sector) [estimado]'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado',
        'molde (= tapas bar)'),
    'alquiler_mes': (
        None, None, 2100, None,
        'Local de 130 m² con salida de humos a cubierta posible (es el filtro del local): sala de 70 m² con 50 plazas, '
        'obrador de 30 m² con el horno a la vista, almacén de leña, aseos y vestuario, en una calle de barrio con paso '
        'de una ciudad media, sin traspaso: unos 16 € el m². El peso sobre las ventas lo calcula el propio libro en la '
        'fila «Alquiler / Ventas» del P&L',
        'research §3 [estimado]'),
    'fianza_meses': (
        None, None, 3, None,
        'Tres meses de renta, lo habitual en un contrato de local de negocio: compruébalo con tu abogado',
        'research §3 [estimado]'),
    'suministros_mes': (
        None, None, 1100, None,
        'Luz de unos 25 kW en trifásica (frío, amasadora, lavavajillas, extracción, climatización y cafetera), agua y '
        'el gas de la cocina de apoyo. La leña del horno NO va aquí: es un coste fijo del P&L. Pide el histórico del '
        'local',
        'research §3 [estimado]'),
    'seguros_ano': (
        None, None, 1800, None,
        'Responsabilidad civil de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la '
        'aseguradora que el horno es de leña: cambia la prima y las condiciones',
        'research §3 [estimado]'),
    'pct_varios': (
        None, None, 0.02, None,
        'Colchón de gasto corriente no presupuestado (pequeñas reparaciones, utillaje que se rompe, pruebas de carta)',
        'molde (= tapas bar)'),
    'recursos_propios': (
        None, None, 65000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §3 [estimado]'),
    'prestamo': (
        None, None, 159000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D9, vueltas 1-2: cubre la necesidad de caja del libro con 65.000 € propios (research: 155.000 €; '
        'el libro sale unos 2.500 € por encima de la cuenta a mano con la fila de suplencias y la tasa de terraza)'),
    'tipo_prestamo': (
        None, None, 0.06, None,
        'Tipo nominal anual. Pide oferta a dos entidades y a una línea ICO antes de fijarlo; el horno, el frío y la '
        'cafetera se pueden pagar con leasing o renting: compáralo',
        'research §3 (= heladería) [estimado]'),
    'plazo_prestamo': (
        None, None, 7, None, 'Años totales, carencia incluida',
        'research §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: obra, chimenea y horno antes de facturar. Desde el segundo año se devuelve el '
        'principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'research §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: el colchón para la rampa del arranque y para enero y febrero, los meses más '
        'flojos (los Meses 5 y 6 del plan)',
        'molde (mínimo de la familia) · research §3'),
    'vida_obra': (
        None, None, 10, None,
        'Obra, chimenea hasta cubierta, instalación eléctrica trifásica, fontanería, climatización y rótulo. '
        'Coeficientes de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades: confírmalo con tu asesor',
        'research §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Horno, amasadora, mesa fría, armarios, campana extractora, lavavajillas, barra, mobiliario y TPV: un 10 % anual, dentro '
        'del coeficiente máximo de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades para la maquinaria '
        '(12 %) y para el mobiliario (10 %). Confírmalo con tu asesor',
        'research §3 dice «= heladería»: 10 años, el valor publicado de la heladería (cumple el coeficiente del '
        'mobiliario)'),
    'pct_bebida_alc': (
        None, 'Bebida que compras al 21 % (alcohol y refrescos con azúcar) sobre el total de bebida', 0.80, None,
        'Sólo mueve el IVA que SOPORTAS al comprar la bebida: la cerveza, el vino y los refrescos con azúcares '
        'añadidos te los facturan al 21 % y el agua y el café, al 10 %; con un 80 % sale un 18,8 %. El IVA que '
        'REPERCUTES lo fija la línea de bebida del P&L (columna H)',
        'research §1 (IVA de compras) · LIVA art. 91 (BOE)'),
    'aforo': (
        None, 'Aforo del local (plazas sentadas, sin la terraza)', 50, None,
        'Plazas de la sala. La terraza suma 24 plazas de abril a octubre, con su autorización municipal aparte, y '
        'quien se lleva la pizza o la recibe en casa no ocupa mesa: por eso la rotación de la fila de arriba es más '
        'alta que la real de tu sala',
        'research §3 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'Las pizzerías están en el convenio PROVINCIAL de hostelería (el art. 4 del VI Acuerdo Laboral de ámbito '
        'Estatal para el sector de Hostelería las nombra, y también el reparto propio): copia aquí el salario base del '
        'grupo más bajo de la tabla de TU provincia. Con 0 el semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.75, None,
        'Una pizzería que abre trae curiosos el primer mes, pero la clientela fija tarda un trimestre: el Mes 1 '
        '(septiembre) factura un 75 % de lo que facturará a los cuatro meses. Con 100 % se elimina la rampa',
        'research §3 [estimado]'),
    'meses_rampa': (
        None, None, 4, None,
        'Cuatro meses hasta el ritmo de crucero: de septiembre a diciembre, para llegar a la Navidad con clientela',
        'research §3 [estimado]'),
    'meses_renta_previa': (
        None, None, 3, None,
        'Tres meses de renta antes de abrir: la obra, la chimenea hasta cubierta y la licencia tardan más que en un '
        'local sin humos. Si el banco te da el préstamo al empezar la obra, súmale los intereses de esos meses, que '
        'este libro no cuenta, y ten en cuenta que la carencia corre desde la firma',
        'research §3 [estimado]'),
    'pct_imprevistos': (
        None, None, 0.10, None,
        'Colchón sobre la obra y las instalaciones del local, que es donde aparecen las sorpresas (la chimenea hasta '
        'cubierta, la acometida trifásica, el separador de grasas). Un banco no financia una reforma sin él',
        'research §3 (10 % sobre la obra) [estimado]'),
    'dias_cobro': (
        None, None, 2, None,
        'Media ponderada: la sala y la recogida cobran al momento y la plataforma liquida cada 7-15 días lo que vende '
        'por ella (un 10 % de las ventas)',
        'research §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a los proveedores de harina, tomate, quesos y bebida: lo que te financian. Es lo primero que '
        'se pierde si te retrasas en un pago',
        'research §3 (= heladería)'),
    'mes_paga_1': (
        None, None, 11, None,
        'Mes de la TESORERÍA en el que sale la paga extra de verano: julio es el Mes 11, porque el Mes 1 del plan es '
        'septiembre',
        'SPEC D7 (Mes 1 = septiembre)'),
    'mes_paga_2': (
        None, None, 4, None,
        'Mes de la TESORERÍA en el que sale la paga extra de Navidad: diciembre es el Mes 4, porque el Mes 1 del plan '
        'es septiembre',
        'SPEC D7 (Mes 1 = septiembre)'),
    'iva_bebida': (
        None, None, 0.10, None,
        'SIN EFECTO en este libro: el IVA que repercute la bebida lo fija su línea del P&L. En sala, todo al 10 % (art. '
        '91.Uno.2.2.º de la Ley 37/1992); para llevar o a domicilio, el alcohol y los refrescos con azúcares añadidos, '
        'al 21 %, en la columna H de esa línea',
        'SPEC D6 · Ley 37/1992 art. 91.Uno.1.1.º y 2.2.º'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente, tipo de IVA). Dos líneas: `mix_en_supuestos` (el peso se teclea en
#: Supuestos). La comida va al 10 % sin partir; la bebida, PARTIDA (sexto campo, `grupo_a.py:2291-2314`).
LINEAS_INGRESO = (
    ('Ventas de pizzería y cocina (sala, para llevar y a domicilio)', 0.82, 'comida',
     'Pizzas, entrantes y postres: en sala unos 77 % de las ventas, para llevar unos 13 % y por plataforma un 10 %. '
     'Todo al 10 % de IVA, se coma en la mesa o salga del local (art. 91.Uno.1.1.º y 2.2.º de la Ley 37/1992)',
     'research §3 [estimado] · LIVA (BOE)'),
    ('Ventas de bebida (cerveza, vino, refrescos, agua y café)', 0.18, 'bebida',
     'Bebida de sala y la que sale con los pedidos',
     'research §3 [estimado]',
     {'cabecera': 'Bebida para llevar o a domicilio al 21 % (%)',
      'pct': 0.07,
      'tipo': 0.21,
      'nota': 'La columna H es la parte de la bebida que sale del local y va al 21 % (alcohol y refrescos con '
              'azúcares añadidos: art. 91.Uno.1.1.º de la Ley 37/1992); el agua, el café y los zumos sin azúcar, y '
              'toda la bebida en sala, al 10 %. Un 7 % = un 1,3 % de las ventas'}),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada; todos por encima del SMI 2026 en proporción (1.221 € × jornada, RD 126/2026). Las 6
#: filas del research §3 + la de suplencias del molde (SPEC D8).
PLANTILLA = (
    ('Titular — pizzaiolo jefe, masa, compras y gestión', 1, 1900,
     'Hace la masa, lleva el horno en el turno fuerte, compra y gestiona. Como administrador de la SL cotiza en el '
     'régimen de autónomos: el libro le imputa el 33 % de Seguridad Social sobre 14 pagas como si fuera nómina, que '
     'es el lado prudente. Confirma con tu gestoría la cuota real y si te aplica la reducida de inicio',
     'research §3 [estimado]', 1.0),
    ('Pizzaiolo/a de horno y estirado', 1, 1500,
     'Estira y hornea; sabe hacer la masa con el titular. Es inversión, no gasto: si sólo el titular sabe la masa y '
     'el horno, una baja cierra la pizzería',
     'research §3 y §6 [estimado]', 1.0),
    ('Ayudante de cocina y masa', 1, 1013,
     'Entrantes, postres, mise en place, boleado y friegue, 30 horas a la semana',
     'research §3 [estimado]', 0.75),
    ('Camarero/a encargado/a de sala y barra', 1, 1450,
     'Todo el año: sala, barra, caja y reservas',
     'research §3 [estimado]', 1.0),
    ('Camarero/a de cenas y fines de semana', 1, 844,
     '25 horas a la semana: las cenas y el fin de semana, cuando la sala se llena',
     'research §3 [estimado]', 0.625),
    ('Refuerzo de viernes a domingo: sala, terraza y recogida', 1, 675,
     'Sala y terraza en temporada, el mostrador de recogida y la tablet de las plataformas. Este plan NO tiene '
     'reparto propio: si lo pones, el repartidor va con contrato laboral del convenio de hostelería, nunca como '
     'autónomo',
     'research §3 [estimado] · ALEH VI art. 4 · ET DA 23.ª', 0.50),
    # RC-19 (SPEC D8): la fila de suplencias que trae el molde del tapas bar (7 filas); sin ella el control de
    # «fórmulas perdidas» de main.py marca las del total de la hoja Personal (calibrado D9, vuelta 1)
    ('Suplencias de vacaciones y descansos', 1, 130,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso semanal del equipo de todo el año',
     'molde (RC-19, = tapas bar y heladería)', 0.10),
)

#: Cobertura: sala y horno (horas × personas a la vez) + producción ANTES de abrir, por los días de apertura.
COBERTURA = {
    'horas_dia': 8.5,
    'personas_franja': 3.0,
    'horas_produccion': 2.5,
    'personas_produccion': 1.5,
    'nota_horas': 'Horas con el local abierto al público, sumando las comidas (13:30-16:00) y las cenas (20:00-23:30) '
                  'y la preparación de cada servicio. La tarde de cierre entre los dos no se cuenta',
    'nota_personas': 'Presencia media a la vez entre el horno, el estirado o el ayudante y la sala. El sábado por la '
                     'noche hacen falta cinco: entran el refuerzo y el camarero de cenas',
    'nota_horas_produccion': 'Masa, salsa y mise en place antes de abrir, y el encendido del horno, que tarda una '
                             'hora y media o dos en llegar a temperatura',
    'nota_personas_produccion': 'El titular con el ayudante. El cierre, la limpieza y las compras quedan fuera de '
                                'este cuadrante: son el margen entre las horas contratadas y las necesarias',
}

#: Rotación ENCENDIDA (SPEC D13): techo 3 y la referencia de que el domicilio no ocupa mesa.
ROTACION = {
    'max': 3.0,
    'nota_max': 'Servicios completos por plaza y día que puedes hacer con comidas, cenas y un segundo turno de cena '
                'el sábado. Es el techo físico del local, no un objetivo',
    'referencia': 'Incluye a quien se lleva la pizza o la recibe en casa, que no ocupa mesa: la rotación real de tu '
                  'sala es menor (en el caso, unos 51 comensales de sala, 1,0 por plaza y día).',
}

#: Partidas de la hoja de inversión: las escribe `semilla_piz.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-24
#: del molde del tapas bar; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = base de
#: los imprevistos, 10 años; 'maquinaria' = 10 años).
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|marca|\bweb\b|'
           r'foto|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|formaci[oó]n|seguro|licencia|permiso|'
           r'\btasas?\b',),
    'obra': (r'proyecto t[eé]cnico|\bobra\b|chimenea|salida de humos|instalaci[oó]n el[eé]ctrica|fontaner|'
             r'climatizaci|r[oó]tulo|fachada',),
    'maquinaria': (r'horno|amasadora|mesa fr[ií]a|armarios?|campana|lavavajillas|fregadero|utillaje|menaje|barra|'
                   r'cafetera|mobiliario|terraza|tpv|dat[aá]fono',),
}

#: Costes fijos. Las 9 partidas propias (18.800 €/año) las escribe `semilla_piz.py` en las filas 26-34 (rótulo e importe); aquí,
#: la nota por rótulo normalizado (minúsculas y sin tildes) y la de la fila canónica del alquiler.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Los tres meses de renta '
              'previos a la apertura están en la hoja de Inversión y NO se cuentan dos veces'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL, nóminas y contratos de la plantilla'),
    'mantenimiento del horno, la campana extractora y el frio': (
        None, 'Deshollinado y filtro de partículas del horno, revisión del refractario, limpieza de la campana '
              'extractora y de los conductos al menos una vez al año (Madrid lo exige en su Ordenanza 4/2021, art. 23; mira la de tu '
              'ayuntamiento) y el frigorista'),
    'marketing y publicidad': (
        None, 'Ficha de Google Business, redes sociales, fotos de temporada y promociones; la campaña de apertura va '
              'en la inversión'),
    'software, tpv, telefono e internet': (
        None, 'Cuota del TPV con Veri*factu, reservas, la tablet de las plataformas, teléfono e internet'),
    'limpieza, lavanderia, epi, ddd y analisis de autocontrol': (
        None, 'Productos de limpieza, lavado de uniformes y paños, guantes de horno, la empresa de DDD (inscrita en '
              'el ROESB) y los análisis de autocontrol que fije tu APPCC'),
    'lena para el horno': (
        None, 'Encina, roble, haya u olivo, seca y sin tratar: unos 5 kg por hora de fuego, 11 horas al día y 300 '
              'días, a unos 0,22 € el kg. Es FIJO porque el horno quema por hora encendido, no por pizza. Con horno '
              'eléctrico, pasa a suministros'),
    # calibrado D9, vuelta 2 (demo §2.11.5 del motor, ramas del Impuesto de Sociedades): la terraza de 24 plazas paga
    # su tasa de ocupación, que el research y la SPEC D8 no contaban; va en la fila de los residuos (las dos son
    # tasas municipales) para no pasar de las 9 filas del molde: una 10.ª desplaza el P&L y main.py marca las
    # fórmulas perdidas (medido). 600 € de residuos + 1.200 € de terraza (= heladería) = 1.800 €.
    'tasa de terraza y gestion de residuos (pon las de tu ayuntamiento)': (
        None, 'La ocupación de la vía pública con 6 mesas de abril a octubre (unos 1.200 € de ejemplo: cada '
              'ayuntamiento tiene su ordenanza fiscal y este plan no ha leído ninguna) y la tasa de basuras, el cartón, '
              'el aceite usado y las cenizas del horno con gestor autorizado (unos 600 €). Pon las de tu ayuntamiento'),
    'derechos de autor por musica ambiental (sgae y agedi-aie)': (
        None, 'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los metros y del aforo de tu sala'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): quemaduras del horno, cortes, cargas de leña y '
              'humo, y los reconocimientos médicos de la plantilla'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Margen bruto al 65 % y no al 74 % del research: el 74 % es el margen sobre la
#: mercancía sola (el caso da un 75,9 %), y el del libro descuenta TODOS los costes variables (el caso da un 67 %).
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.65,
     'Suelo del margen tras TODOS los costes variables (mercancía, cajas y envases, plataforma, medios de pago y '
     'varios). Sólo con la mercancía, una pizzería con horno de leña deja en torno a un 76 %. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.27,
     'Techo de la materia prima sobre ventas: la Margherita sale a un 15 % y la búfala, la burrata y los embutidos '
     'italianos la suben. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'Techo del personal sobre ventas con dos pizzaiolos y una sala de dos servicios. Estimación del kit'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del alquiler sobre ventas para un local con salida de humos a cubierta: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga. Una pizzería de barrio bien llevada deja en '
     'torno a un 9 %. Estimación del kit'),
)

#: (comensales al día, € por comensal sin IVA, días de apertura). Research §3.
ESCENARIOS = {
    'pesimista': (56, 18.50, 295),     # menos comensales, ticket más bajo y una semana más de cierre
    'optimista': (76, 20.50, 305),
}

#: Mes 1 = SEPTIEMBRE (SPEC D7). Calendario: ene .068 · feb .072 · mar .082 · abr .086 · may .090 · jun .090 ·
#: jul .088 · ago .072 · sep .084 · oct .088 · nov .084 · dic .096 (research §3: enero y febrero los más flojos,
#: terraza de abril a junio, agosto cae y diciembre es el pico). Rotada al orden del motor (Mes 1…12).
ESTACIONALIDAD = (0.084, 0.088, 0.084, 0.096, 0.068, 0.072,
                  0.082, 0.086, 0.090, 0.090, 0.088, 0.072)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es SEPTIEMBRE: el plan abre después del verano para llegar a la Navidad con clientela y a '
        'enero y febrero con el fondo intacto. El saldo mínimo del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El plan de negocio en Word de este pack cita las cifras de este Excel: si cambias una celda verde, el Excel '
        'manda. La calculadora de masa y escandallo del pack va aparte: el coste de cada pizza que te dé es el que '
        'tienes que llevar a la celda de coste de la comida de la hoja de Supuestos.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Septiembre', 'Decisión del plan',
         'La rampa cae en meses medios y altos, la Navidad llega con clientela y enero y febrero, con el fondo '
         'intacto. La fila de estacionalidad de la Tesorería ya va girada'),
        ('Coste de la Margherita', 'Un 15 % de su precio sin IVA',
         'Estimación del kit con los gramajes del pliego de la ETG (Reglamento (UE) 97/2010)',
         'Harina, fior di latte, tomate y aceite: unos 1,36 € con merma sobre 9,09 € sin IVA. Con búfala, burrata o '
         'embutido italiano, un 20-28 %'),
        ('Margherita en carta', '10,90 € con IVA (mediana)',
         'Cartas de 14 pizzerías de Madrid, Barcelona, Valencia, Marbella y Tenerife, octubre de 2026',
         '10,50-12,90 € en Madrid y Barcelona; 8-9 € en Canarias'),
        ('Masa del pliego de la ETG «Pizza Napoletana»', '1 l de agua, 1.800 g de harina, 50-55 g de sal, 3 g de '
         'levadura', 'Reglamento (UE) 97/2010, anexo II, apartado 3',
         'Un 55,6 % de hidratación; bolas de 180-250 g; 2 h de primera fermentación y 4-6 h de segunda a temperatura '
         'ambiente'),
        ('Cocción del pliego', 'Solera a unos 485 °C y bóveda a unos 430 °C, 60-90 s',
         'Reglamento (UE) 97/2010, anexo II', 'Exclusivamente en horno de leña'),
        ('Nombre «pizza napoletana» (también traducido)', 'Reservado desde el 18-12-2022',
         'Reglamento de Ejecución (UE) 2022/2313 y Reglamento (UE) 2024/1143, art. 68.1',
         'Sólo para la pizza que cumple el pliego y pasó la verificación oficial. La carta del caso usa «Margherita», '
         '«Marinara»…'),
        ('Comisión de la plataforma con su reparto', '25-35 % más IVA',
         'Guías del sector, 2025-2026: compruébalo en tu contrato',
         'El plan básico de Uber Eats ronda el 30 %. La recogida en el local no paga comisión'),
        ('IVA de la pizza', '10 %', 'Ley 37/1992, art. 91.Uno.1.1.º y 2.2.º',
         'En sala, para llevar y a domicilio. El alcohol y los refrescos con azúcares añadidos que salen del local, '
         'al 21 %'),
        ('Salario mínimo interprofesional 2026', '1.221 € al mes en 14 pagas', 'Real Decreto 126/2026',
         'A prorrata en jornada parcial'),
        ('Coste de personal sobre ventas', '34-38 %', 'Estimación del kit',
         'Con el titular de pizzaiolo y un segundo pizzaiolo: el pizzaiolo único es un riesgo, no un ahorro'),
        ('Alquiler sobre ventas', '6-10 %', 'Estimación del kit',
         'Un local con salida de humos a cubierta cuesta más encontrarlo que pagarlo'),
        ('Leña del horno', 'Unos 3.600 € al año', 'Estimación del kit',
         'Unos 5 kg por hora de fuego, 11 horas al día y 300 días. Va como coste FIJO: se quema por hora, no por pizza'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Nombra las pizzerías y el reparto propio. Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_piz.py` entero (`datos_checklist.py`, SPEC D14): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO de la compra de COMIDA (research §1): quesos 35 % + harina 12 % + aceite 5 % + hortaliza fresca 8 % al
#: 4 % (= 60 % de la compra); conservas, embutidos, levadura, sal y resto al 10 % (40 %) → 0,6 × 4 + 0,4 × 10 = 6,4 %.
#: La bebida tiene su propio tipo de compra (`pct_bebida_alc`, 18,8 %): ponderado, 8,9 % (SPEC D6).
IVA_COMPRAS = {
    'comida': 0.064,
    'nota': 'Harina, quesos, aceite de oliva y hortaliza fresca van al 4 % (art. 91.Dos.1.1.º de la Ley 37/1992); '
            'tomate en conserva, embutidos, levadura y sal, al 10 %. Ajústalo a tus facturas',
}
