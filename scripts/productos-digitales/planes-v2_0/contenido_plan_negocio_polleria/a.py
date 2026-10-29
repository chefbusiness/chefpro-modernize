#!/usr/bin/env python3
"""
Contenido de `plan-negocio-polleria` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Semilla = la Taquería ES 1.0 publicada:
`plan-polleria/semilla_pol.py` copia sus dos xlsx (plan + checklist, solo lectura), les quita el bloque de rotación
(16 fórmulas), les pone las 18 partidas, los 9 fijos, los títulos y el checklist de la pollería, y `main.py` +
`grupo_a.py` los reconstruyen con este módulo (mecánica de la taquería: producción antes de abrir, bebida con línea
partida, Mes 1 = enero, pagas 7/12; la rotación, APAGADA). Cómo y por qué: `plan-polleria/F1-camino.md` §1-§3 (la §2
hace de SPEC, firmada el 29-oct); caso y fuentes: `plan-polleria/F1-research-polleria.md` §1-§3 (R §n).

MOTOR DE INGRESOS (pollería-asador de barrio: mostrador, encargos, plataforma y sala)
------------------------------------------------------------------------------------
    cubiertos_dia (B4) = PEDIDOS AL DÍA (278 para llevar + 45 de plataforma + 140 de sala a la semana ÷ 6)   77
    ticket_medio  (B5) = € POR PEDIDO SIN IVA                                                              15,80 €
    dias_apertura (B6) = DÍAS DE APERTURA AL AÑO                                                           300
Ventas a régimen = 77 × 15,80 × 300 = 364.980 €. 1 pedido = un pedido de mostrador o encargo, uno de plataforma o un
cliente sentado en la sala (R §3). Unidad del motor: `VOCABULARIO` `cubierto → pedido` (masculino, sin arreglos de
concordancia). Mes 1 = ENERO, sin girar: la estacionalidad va en el orden del calendario (al revés que la taquería, el
verano SUBE) y las pagas extra salen en los meses 7 y 12.

IVA: la comida al 10 % (mostrador, encargos, plataforma y sala, sin partir; el pan común que se vende suelto, al 4 %, se
queda dentro: es una parte mínima, R §7); la bebida con la LÍNEA PARTIDA del motor (`grupo_a.py:2291-2314`): su columna
H («Bebida para llevar o por plataforma al 21 %») declara la parte que sale del local al tipo general (cerveza, vino y
refrescos con azúcares o edulcorantes añadidos, LIVA 91.Uno.1.1.º a y b), H = 31 % (= 3,1 % de las ventas, R §3); el
resto, al 10 %. `pct_bebida_alc` (B62) sólo mueve el IVA SOPORTADO de la compra de bebida: 70 % → 17,7 %.
`IVA_COMPRAS` es SOLO la compra de COMIDA (9,1 %): la bebida ya lleva su tipo (lección de la Pizzería).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «R §n» = `F1-research-polleria.md` §n (casi todo
[estimado], criterio de kit, con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado D9» =
ajustado en F2 para cumplir los gates del caso.

⚠️ Rótulos de importe: sin «comensales», «personas», «días», «meses», «años», «plazas» ni «unidades»
(`motor.RX_RECUENTO_DV` les quita el formato de euro). «Campana» siempre «campana extractora» (`motor.TILDES` la
acentúa a «campaña») y nunca el verbo «publica» (lo acentúa a «pública»). Las notas no usan «cubierto» ni «comensal»
(gate F2 (4)), ni «rotación» (bloque apagado), ni restos de los moldes (taco, trompo, tortilla de maíz, pizza…:
`plan-polleria/barrido_es.py`). Sesión Claude Code, 29-oct-2026.
"""

CONCEPTO = 'Pollería y Asador de Pollos'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Masculino «pedido» = masculino «cubierto»:
#: sin arreglos de concordancia. Las 9 frases del motor = las de la Taquería (F1-camino §2), con la compra al 21 % de la
#: pollería (cerveza, vino y refrescos con azúcares o edulcorantes añadidos), «el pollo asado incluido» y el pan común
#: al superreducido. La última traduce la nota `O5` de la Tesorería al calendario de la pollería (Mes 1 = enero).
#: `VOCABULARIO_SIN_TILDES` (= Pizzería; la Taquería no lo lleva): sin él, las 7 claves con tilde («común», «sólo»,
#: «bollería», «versión», «azúcares») no casan nunca (`grupo_a.compilar_vocabulario`) y el libro conserva las frases de
#: delivery y pan común del motor (medido en la vuelta 1 de la F2: C9, Instrucciones!A8, Tesorería!O16 y D31).
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubierto': 'pedido',
    'cubiertos': 'pedidos',
    # las tres frases del motor: la línea partida de la bebida, no el canal de delivery
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'la bebida que sale para llevar o por plataforma (columna H de su línea en el P&L) mueve',
    'el libro lo aplica al alcohol del canal de delivery':
        'el libro lo aplica a la parte de la bebida que declara la columna H de su línea en el P&L',
    'que repercutes por el alcohol que sale por delivery':
        'que repercutes por la bebida que sale para llevar o por plataforma',
    'El alcohol servido en sala va al reducido: su tipo está en el bloque de desglose del IVA':
        'El alcohol servido en sala va al reducido, como fija la línea de bebida del P&L',
    'El libro manda al general sólo el alcohol: si compras refrescos o zumos con azúcares añadidos, su factura '
    'también va al 21':
        'En las compras, el libro manda al general la parte de la bebida que declara la celda «Bebida que compras al '
        '21 %» de esta hoja: la cerveza, el vino y los refrescos con azúcares o edulcorantes añadidos, cuya factura '
        'va al 21',
    # Tesorería (nota de la fila del IVA repercutido): el motor cierra el paréntesis
    'el alcohol que sale por delivery, al general; el pan común y las harinas panificables, al superreducido (art. '
    '91.Dos.1.1.º':
        'la parte de la bebida que sale para llevar o por plataforma y declara la columna H de su línea (cerveza, vino '
        'y refrescos con azúcares o edulcorantes añadidos), al general (art. 91.Uno.1.1.º a y b); el pan común que '
        'vendas suelto, al superreducido (art. 91.Dos.1.1.º a: el libro lo deja en la comida al 10 % porque es una '
        'parte mínima de las ventas',
    'los alimentos —bollería y pastelería incluidas—, que son':
        'los alimentos —el pollo asado incluido—, que son',
    # Instrucciones!A8 (frase del motor; LIVA art. 91.Uno.1.1.º b): «azúcares o edulcorantes añadidos»
    'el alcohol y los refrescos o zumos con azúcares añadidos para llevar':
        'el alcohol y los refrescos o los zumos con azúcares o edulcorantes añadidos para llevar',
    # resto del molde en Tesorería!D31 (barrido_es.py: «versión 1.1»)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # Tesorería!O5 (nota del motor de la fila de estacionalidad), F1-camino §2: Mes 1 = enero, el verano arriba.
    # Picos que casan con la tupla (m7 de la Taquería): julio 0,096 y agosto 0,098; diciembre repunta (0,084 tras 0,076).
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = ENERO, en el orden del calendario: enero y febrero son los meses más flojos, julio y agosto el pico '
        '(la semana del 15 de agosto, la más fuerte) y diciembre repunta con los encargos de Nochebuena y Nochevieja. '
        'En la costa el verano sube más; en el centro de una gran ciudad, agosto puede bajar. Si abres en otro mes, '
        'gira la fila',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 77, None,
        'Pedidos al día, media del año: 1 pedido es un pedido de mostrador o un encargo, uno de plataforma o un cliente '
        'sentado en la sala. A la semana, unos 278 para llevar, 45 de plataforma y 140 de sala en 6 días. El domingo '
        'llega a unos 150 (un tercio de los pollos de la semana) y un martes se queda en unos 40. Contrástalo con el '
        'paso de gente de tu calle un domingo a mediodía y un martes',
        'R §3 [estimado]'),
    'ticket_medio': (
        None, None, 15.80, None,
        'SIN IVA, por pedido: el de mostrador (0,8 pollos, patatas, algún extra, pan, salsas y bebida) suma unos '
        '17,70 € con IVA; el de plataforma, unos 20,50 € con su precio más alto; el cliente de sala (menú de cuarto de '
        'pollo o medio pollo a la brasa, algo para compartir, bebida y postre), unos 16,10 €. La media sin IVA sale en '
        '15,80 €. El pollo entero del caso cuesta 12,90 € con IVA, dentro de los 11-14 € del asador de barrio (cartas '
        'leídas en 2026). El precio con IVA está en la fila «PVP equivalente con IVA» de abajo',
        'R §2-§3 (carta del caso) [estimado]'),
    'dias_apertura': (
        None, None, 300, None,
        '365 días menos los 52 lunes de cierre, 10 días de cierre en enero (mantenimiento del asador y vacaciones) y 3 '
        'días sueltos; los festivos abren como un domingo. Es el MISMO dato para la cuenta de resultados, el punto de '
        'equilibrio, los escenarios y las horas de personal',
        'R §3 [estimado]'),
    'crec_a2': (
        None, None, 0.06, None,
        'Clientela que repite y encargos del domingo que se hacen costumbre el segundo año. Se aplica a los pedidos con '
        'el mismo ticket; el personal NO sube con este porcentaje: sale de la hoja Personal',
        'R §3 [estimado] (= taquería)'),
    'crec_a3': (
        None, None, 0.04, None,
        'Sobre el año 2. Conservador: el techo lo pone el asador el domingo antes de las tres (60 pollos por carga con '
        'doce espadas) y el mostrador en la hora punta',
        'R §3 [estimado]'),
    'pct_comida': (
        None, None, 0.90, None,
        'Pollo asado, patatas, croquetas, ensaladilla, ensaladas, salsas y pan (para llevar, por plataforma y en sala) '
        'sobre las ventas; el 10 % restante es la bebida. Es el peso de la primera línea de ventas del P&L',
        'R §3 [estimado] (90/10)'),
    'coste_comida': (
        None, None, 0.32, None,
        'Materia prima de la comida sobre sus ventas: el pollo entero sale a un 38,8 % (el pollo es caro y se vende '
        'barato), el medio a un 35,8 %, las patatas a un 28 %, la ensaladilla a un 25 %, el menú de sala a un 26 % y las '
        'croquetas, hechas con el pollo del día anterior, a un 22 %: el pedido tipo para llevar queda en un 33 % y la sala '
        'en un 25 %. Un 31 % de media, más 1,5 puntos de merma (pollos que sobran y no llegan a croqueta, patata frita '
        'que se tira) y menos medio de redondeo. Cada 10 % que suba el pollo resta unos 6.700 € al resultado: el pollo '
        'es un precio estimado por el kit, pon el de tu proveedor y escandalla con la calculadora del pack',
        'R §2-§3 [estimado]'),
    'coste_bebida': (
        None, None, 0.30, None,
        'Lata o botella para llevar a unos 2,00 € y la caña, el refresco y el vino en la sala: un 30 % de media de su '
        'precio de venta. Si la cervecera te cede la nevera o el equipo de tiraje, pide el precio por escrito',
        'R §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Bolsas térmicas de pollo, bandejas, envases de salsa, bolsas de asa, etiquetas, servilletas y guantes: unos '
        '0,45 € por pedido (ningún proveedor publica tarifa: estimación del kit), y los envases para que el cliente de '
        'sala se lleve lo que no consuma (Ley 1/2025, art. 8). El envase de plástico de un solo uso se cobra aparte en '
        'el tique (Ley 7/2022, art. 55)',
        'R §1-§3 [estimado] · BOE'),
    'pct_delivery': (
        None, None, 0.11, None,
        'Ventas por PLATAFORMA con su reparto (Glovo, Just Eat, Uber Eats) sobre el total. Lo que se recoge en el '
        'mostrador o por encargo NO paga comisión y no va aquí. El pollo entero aguanta bien el viaje; las patatas '
        'fritas llegan blandas: no subas del 12-15 % sin probarlo',
        'R §3 [estimado]'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión de la plataforma con su reparto sobre lo que vende ese canal: el plan básico de Uber Eats ronda el '
        '30 % más IVA, Glovo va del 15 al 35 % según la zona y Just Eat, del 13 al 35 %. Compruébala en tu contrato. Si '
        'repartes tú, pon 0 y suma el repartidor, con contrato laboral, a la hoja Personal',
        'R §2 (guías del sector) [estimado]'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado',
        'molde (= taquería)'),
    'alquiler_mes': (
        None, None, 1200, None,
        'Local de 80 m² con salida de humos a cubierta posible (es el filtro del local): obrador y zona de asado de '
        '25 m² a la vista, mostrador con vitrina caliente, sala de 20 plazas (16 en mesa y 4 en barra), aseos (uno '
        'adaptado) y almacén, en un barrio residencial de una ciudad media, cómodo para parar el coche y recoger el '
        'encargo, sin traspaso: unos 15 € el m². El peso sobre las ventas lo calcula el propio libro en la fila '
        '«Alquiler / Ventas» del P&L',
        'R §2-§3 [estimado]'),
    'fianza_meses': (
        None, None, 2, None,
        'Dos meses de renta, lo habitual en un contrato de local de negocio: compruébalo con tu abogado',
        'R §3 [estimado]'),
    'suministros_mes': (
        None, None, 1000, None,
        'El gas del asador de pollos (uno de ocho espadas declara 56 kW en su ficha), la luz de la freidora, el frío, '
        'la extracción y la climatización, y el agua. Estimación del kit: pide el histórico del local y mide el consumo '
        'del asador con la calculadora del pack',
        'R §2-§3 [estimado]'),
    'seguros_ano': (
        None, None, 1400, None,
        'Responsabilidad civil de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la '
        'aseguradora que trabajas con asador de pollos y freidora a gas: cambia la prima y las condiciones',
        'R §3 [estimado] (= taquería)'),
    'pct_varios': (
        None, None, 0.02, None,
        'Colchón de gasto corriente no presupuestado (pequeñas reparaciones, espadas o utillaje que se rompen, pruebas '
        'de carta)',
        'molde (= taquería)'),
    'recursos_propios': (
        None, None, 50000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'R §3 [estimado]'),
    'prestamo': (
        None, None, 112000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D9, vuelta 2 del F1-camino: cubre la necesidad de caja del libro con 50.000 € propios (R §3: '
        '110.000 €; el libro sale unos 1.600 € por encima de la cuenta a mano, con la fila de suplencias y los 1.500 € '
        'más de mantenimiento y marketing)'),
    'tipo_prestamo': (
        None, None, 0.06, None,
        'Tipo nominal anual. Pide oferta a dos entidades y a una línea ICO antes de fijarlo; el asador, el frío y la '
        'freidora se pueden pagar con leasing o renting: compáralo',
        'R §3 (= taquería) [estimado]'),
    'plazo_prestamo': (
        None, None, 7, None, 'Años totales, carencia incluida',
        'R §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: obra, conducto de humos, gas y asador antes de facturar. Desde el segundo año se '
        'devuelve el principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'R §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: el colchón para la rampa del arranque, que con el Mes 1 en enero cae sobre los '
        'meses más flojos del año (enero y febrero)',
        'molde (mínimo de la familia) · R §3'),
    'vida_obra': (
        None, None, 10, None,
        'Obra, conducto de extracción hasta cubierta, instalación eléctrica trifásica, fontanería, gas, climatización, '
        'rótulo y fachada. Coeficientes de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades: confírmalo '
        'con tu asesor',
        'R §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Asador de pollos, vitrina caliente, freidora, campana extractora, frío, lavavajillas, botellero, mobiliario y '
        'TPV: un 10 % anual, dentro del coeficiente máximo de la tabla del art. 12.1 de la Ley del Impuesto sobre '
        'Sociedades para la maquinaria (12 %) y para el mobiliario (10 %). Confírmalo con tu asesor',
        'R §3 (= taquería)'),
    'pct_bebida_alc': (
        None, 'Bebida que compras al 21 % (cerveza, vino y refrescos con azúcares o edulcorantes añadidos) sobre el '
              'total de bebida', 0.70, None,
        'Sólo mueve el IVA que SOPORTAS al comprar la bebida: la cerveza, el vino y los refrescos con azúcares o '
        'edulcorantes añadidos te los facturan al 21 %; el agua y los refrescos sin azúcares ni edulcorantes añadidos, '
        'al 10 %. Con un 70 % sale un 17,7 %. El IVA que REPERCUTES lo fija la línea de bebida del P&L (columna H)',
        'R §1 (IVA de compras) · LIVA art. 91 (BOE) · 70 %: estimación del kit (R no lo da)'),
    'aforo': (
        None, 'Aforo de la sala (plazas sentadas)', 20, None,
        'Plazas de la sala: 16 en mesa y 4 en barra. Quien recoge un encargo o recibe el pedido en casa no ocupa mesa: '
        'la sala atiende unos 23 clientes al día de media, así que cada plaza se ocupa algo más de una vez al día. El '
        'cuello de botella de una pollería no son las mesas, es el asador el domingo',
        'R §3 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'Las pollerías y los asadores de pollos van al convenio PROVINCIAL de hostelería: el art. 4 del VI Acuerdo '
        'Laboral de ámbito Estatal para el sector de Hostelería no los nombra, pero incluye los restaurantes y el '
        'reparto de comidas preparadas. Copia aquí el salario base del grupo más bajo de la tabla de TU provincia. Con '
        '0 el semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.75, None,
        'Una pollería que abre trae curiosos el primer mes, pero los encargos del domingo tardan un trimestre en hacerse '
        'costumbre: el Mes 1 (enero) factura un 75 % de lo que facturará a los cuatro meses. Con 100 % se elimina la '
        'rampa',
        'R §3 [estimado] (= taquería)'),
    'meses_rampa': (
        None, None, 4, None,
        'Cuatro meses hasta el ritmo de crucero: de enero a abril, para llegar al verano, el pico del año, con la '
        'clientela hecha',
        'R §3 [estimado]'),
    'meses_renta_previa': (
        None, None, 2, None,
        'Dos meses de renta antes de abrir: la obra, el conducto de humos, la instalación de gas y la licencia. Si el '
        'banco te da el préstamo al empezar la obra, súmale los intereses de esos meses, que este libro no cuenta, y ten '
        'en cuenta que la carencia corre desde la firma',
        'R §3 [estimado]'),
    'pct_imprevistos': (
        None, None, 0.10, None,
        'Colchón sobre la obra y las instalaciones del local, que es donde aparecen las sorpresas (el conducto hasta '
        'cubierta, la potencia trifásica, la instalación de gas, el separador de grasas). Un banco no financia una '
        'reforma sin él',
        'R §3 (10 % sobre la obra) [estimado]'),
    'dias_cobro': (
        None, None, 2, None,
        'Media ponderada: el mostrador, los encargos y la sala cobran al momento y la plataforma liquida cada 7-15 días '
        'lo que vende por ella (un 11 % de las ventas)',
        'R §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a los proveedores de pollo, patata, aceite y bebida: lo que te financian. Pídelo por escrito: es '
        'lo primero que se pierde si te retrasas en un pago',
        'molde (= taquería)'),
    'mes_paga_1': (
        None, None, 7, None,
        'Mes de la TESORERÍA en el que sale la paga extra de verano: julio es el Mes 7, porque el Mes 1 del plan es '
        'enero',
        'F1-camino §2 (Mes 1 = enero)'),
    'mes_paga_2': (
        None, None, 12, None,
        'Mes de la TESORERÍA en el que sale la paga extra de Navidad: diciembre es el Mes 12, porque el Mes 1 del plan '
        'es enero',
        'F1-camino §2 (Mes 1 = enero)'),
    'iva_bebida': (
        None, None, 0.10, None,
        'SIN EFECTO en este libro: el IVA que repercute la bebida lo fija su línea del P&L. En sala, todo al 10 % (art. '
        '91.Uno.2.2.º de la Ley 37/1992); para llevar o por plataforma, la cerveza, el vino y los refrescos con azúcares '
        'o edulcorantes añadidos, al 21 %, en la columna H de esa línea',
        'Ley 37/1992 art. 91.Uno.1.1.º y 2.2.º (BOE)'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente, tipo de IVA). Dos líneas: `mix_en_supuestos` (el peso se teclea en
#: Supuestos). La comida va al 10 % sin partir; la bebida, PARTIDA (sexto campo, `grupo_a.py:2291-2314`).
LINEAS_INGRESO = (
    ('Ventas de pollo asado y cocina (mostrador, encargos, plataforma y sala)', 0.90, 'comida',
     'Pollo asado entero, medio y en cuartos, patatas, croquetas, ensaladilla, ensaladas, salsas y pan: para llevar '
     '(mostrador y encargos) unos 61 % de las ventas, por plataforma un 11 % y en sala un 28 %. Todo al 10 % de IVA, se '
     'coma en la mesa o salga del local (art. 91.Uno.1.1.º y 2.2.º de la Ley 37/1992); el pan común que vendas suelto va '
     'al 4 %, pero es una parte mínima y el libro lo deja aquí',
     'R §3 [estimado] · LIVA (BOE)'),
    ('Ventas de bebida (refrescos, agua, cerveza y vino)', 0.10, 'bebida',
     'Bebida de sala y la que sale con los pedidos',
     'R §3 [estimado]',
     {'cabecera': 'Bebida para llevar o por plataforma al 21 % (%)',
      'pct': 0.31,
      'tipo': 0.21,
      'nota': 'La columna H es la parte de la bebida que sale del local y va al 21 %: la cerveza, el vino y los refrescos '
              'con azúcares o edulcorantes añadidos (art. 91.Uno.1.1.º a y b de la Ley 37/1992); el agua y lo que no '
              'lleve azúcares ni edulcorantes añadidos, y toda la bebida en sala, al 10 %. Un 31 % = un 3,1 % de las '
              'ventas'}),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada; todos por encima del SMI 2026 en proporción (1.221 € × jornada, RD 126/2026). Las 7
#: filas de R §3 (la de suplencias incluida, la que exige el molde) = 4,60 jornadas, 6.911 €/mes → 128.683 €/año.
PLANTILLA = (
    ('Titular — maestro/a asador: compra del pollo, adobos, asador, encargos y gestión', 1, 1900,
     'Compra el pollo y fija el calibre, prepara los adobos, lleva el asador y las cargas del domingo, organiza los '
     'encargos y gestiona. Como administrador de la SL cotiza en el régimen de autónomos: el libro le imputa el 33 % '
     'de Seguridad Social sobre 14 pagas como si fuera nómina, que es el lado prudente. Confirma con tu gestoría la '
     'cuota real y si te aplica la reducida de inicio',
     'R §3 [estimado]', 1.0),
    ('Asador/a-cocinero/a: espetar, freidora, guarniciones y croquetas', 1, 1450,
     'Espeta y carga el asador, lleva la freidora, las guarniciones y las croquetas y sabe sondear y trinchar. Es '
     'inversión, no gasto: si sólo el titular sabe llevar el asador, una baja cierra el domingo, que es un tercio de '
     'la semana',
     'R §3 y §6 [estimado]', 1.0),
    ('Dependiente/a de mostrador y caja', 1, 1400,
     'Mostrador, caja, teléfono y encargos, la tablet de las plataformas y la información de alérgenos',
     'R §3 [estimado]', 1.0),
    ('Camarero/a de sala', 1, 1013,
     '30 horas a la semana: los mediodías y las cenas de jueves a sábado',
     'R §3 [estimado]', 0.75),
    ('Ayudante de cocina y friegue de fin de semana', 1, 473,
     'Sábado y domingo por la mañana: patatas, ensaladilla y las espadas al lavavajillas',
     'R §3 [estimado]', 0.35),
    ('Refuerzo de sábado, domingo y festivos', 1, 540,
     'Mostrador y despacho de encargos en la punta del fin de semana. Este plan NO tiene reparto propio: si lo pones, '
     'el repartidor va con contrato laboral del convenio de hostelería, nunca como autónomo',
     'R §3 [estimado] · ALEH VI art. 4 · ET DA 23.ª', 0.40),
    # RC-19: la fila de suplencias que trae el molde (7 filas); sin ella el control de «fórmulas perdidas» de main.py
    # marca las del total de la hoja Personal (Pizzería F2-NOTAS §2.1)
    ('Suplencias de vacaciones y descansos', 1, 135,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso semanal del equipo de todo el año',
     'molde (RC-19, = taquería)', 0.10),
)

#: Cobertura: asador, freidora, mostrador y sala (horas × personas a la vez) + producción ANTES de abrir, por los días
#: de apertura. R §3: 25,5 h × 300 = 7.650 h frente a 8.464 contratadas → 111 %.
COBERTURA = {
    'horas_dia': 7.0,
    'personas_franja': 3.0,
    'horas_produccion': 3.0,
    'personas_produccion': 1.5,
    'nota_horas': 'Horas con el local abierto al público de media: de 12:00 a 16:30 de martes a domingo y de 20:00 a '
                  '23:00 de jueves a sábado, con la preparación de cada servicio',
    'nota_personas': 'Presencia media a la vez entre el asador, la freidora, el mostrador y la sala. El domingo de 11:00 '
                     'a 15:30 hacen falta seis: entran el refuerzo y el ayudante (el cuadrante anual no lo ve: ponlo en '
                     'el turno)',
    'nota_horas_produccion': 'Espetar y adobar los pollos de la primera carga, encender el asador, croquetas, '
                             'ensaladilla y patatas antes de abrir',
    'nota_personas_produccion': 'El maestro asador con el asador-cocinero. La limpieza del asador y de la campana '
                                'extractora, el cierre y las compras quedan fuera de este cuadrante: son el margen entre '
                                'las horas contratadas y las necesarias',
}

#: Rotación APAGADA (= Heladería, F1-camino §2): con todos los pedidos saldría 3,9 por plaza y no significa nada; la
#: sala (≈ 1,2) va en la nota del aforo. La semilla quita del origen las 16 fórmulas del bloque (`_sin_rotacion`).
ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_pol.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-24
#: del molde; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = base de los
#: imprevistos, 10 años; 'maquinaria' = 10 años). R §3: obra 46.000 · maquinaria 33.000 · no amortizable 9.500.
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|marca|\bweb\b|'
           r'foto|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|formaci[oó]n|seguro|licencia|permiso|'
           r'\btasas?\b',),
    'obra': (r'proyecto t[eé]cnico|\bobra\b|conducto|salida de humos|instalaci[oó]n el[eé]ctrica|fontaner|'
             r'climatizaci|r[oó]tulo|fachada',),
    'maquinaria': (r'asador|vitrina|freidora|fog[oó]n|ba[ñn]o mar[ií]a|campana|armarios?|congelador|'
                   r'lavavajillas|fregadero|utillaje|menaje|botellero|nevera|barra|cafetera|mobiliario|tpv|'
                   r'dat[aá]fono',),
}

#: Costes fijos. Las 9 partidas propias (13.900 €/año) las escribe `semilla_pol.py` en las filas 26-34 (rótulo e
#: importe); aquí, la nota por rótulo normalizado (minúsculas y sin tildes) y la de la fila canónica del alquiler.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Los dos meses de renta '
              'previos a la apertura están en la hoja de Inversión y NO se cuentan dos veces'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL, nóminas y contratos de la plantilla'),
    # calibrado (F1-camino §1, vuelta 1): 1.800 € de R §3 + 1.000 € de una segunda limpieza de campana y conducto
    'mantenimiento de la campana extractora, el gas, el asador y el frio': (
        None, 'Dos limpiezas al año de la campana extractora y del conducto (la grasa del asador de pollos y de la '
              'freidora las pide; Madrid exige al menos una en su Ordenanza 4/2021, art. 23: mira la de tu '
              'ayuntamiento), la revisión del gas y del asador (quemadores, motor y espadas) y el frigorista'),
    'marketing y publicidad': (
        None, 'Ficha de Google Business, redes sociales, fotos, buzoneo y tarjetas con el teléfono de encargos, y las '
              'fechas fuertes: el verano, la Navidad y, si haces el pollo a la brasa al estilo peruano, el Día del '
              'Pollo a la Brasa (tercer domingo de julio). La campaña de apertura va en la inversión'),
    'software, tpv, telefono e internet': (
        None, 'Cuota del TPV con Veri*factu, la tablet de las plataformas, el teléfono de encargos e internet'),
    'limpieza, lavanderia, epi y analisis de autocontrol': (
        None, 'Productos de limpieza y desengrasantes, lavado de uniformes y paños, guantes y los análisis de '
              'autocontrol que fije tu APPCC'),
    'gestion de residuos y del aceite y la grasa usados': (
        None, 'La tasa de basuras y el cartón, y el aceite de la freidora y la grasa de la bandeja de goteo del asador '
              'con gestor autorizado y certificado de cada recogida (unos 30-60 € por recogida). Pon la tasa de tu '
              'ayuntamiento'),
    'desinsectacion, desratizacion y desinfeccion (ddd)': (
        None, 'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
    'derechos de autor por musica ambiental (sgae y agedi-aie)': (
        None, 'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los metros y del aforo de tu sala'),
    'prevencion de riesgos laborales, vigilancia de la salud y formacion': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): quemaduras del asador y de la freidora, cortes al '
              'trinchar y al espetar, gas y calor; los reconocimientos médicos de la plantilla y la formación en '
              'higiene y alérgenos'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Margen bruto al 55 %: el del libro descuenta TODOS los costes variables (el caso
#: da un 59 %); la mercancía con un techo del 33 % (el caso, un 31,8 %).
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.55,
     'Suelo del margen tras TODOS los costes variables (mercancía, envases, plataforma, medios de pago y varios). Una '
     'pollería deja menos que otros locales porque el pollo pesa: el margen está en lo que lo acompaña. Estimación del '
     'kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.33,
     'Techo de la materia prima sobre ventas: el pollo entero sale a un 38,8 % y las patatas, las croquetas y la bebida '
     'lo bajan. Si el precio del pollo sube, aquí se nota primero. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'Techo del personal sobre ventas con un maestro asador, un segundo asador y el refuerzo del domingo. Estimación '
     'del kit'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del alquiler sobre ventas para un local con salida de humos a cubierta: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga. Una pollería bien llevada deja en torno a un 7-8 %. '
     'Estimación del kit'),
)

#: (pedidos al día, € por pedido sin IVA, días de apertura). R §3.
ESCENARIOS = {
    'pesimista': (66, 15.00, 295),     # menos pedidos, ticket más bajo y unos días más de cierre
    'optimista': (88, 16.50, 305),
}

#: Mes 1 = ENERO, sin girar (F1-camino §2): el calendario de R §3 tal cual. Al revés que la pizzería y la taquería, el
#: verano SUBE (+15 % en el interior; pico la semana del 15 de agosto, R §2 [medido]); enero y febrero, los flojos;
#: diciembre repunta con los encargos de Nochebuena y Nochevieja. Pico/valle = agosto/enero = 1,40.
ESTACIONALIDAD = (0.070, 0.072, 0.080, 0.084, 0.086, 0.088,
                  0.096, 0.098, 0.084, 0.082, 0.076, 0.084)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es ENERO, en el orden del calendario: la rampa del arranque cae sobre enero y febrero, los '
        'meses más flojos, y por eso el fondo de maniobra cuenta; julio y agosto son el pico. Si abres en otro mes, '
        'gira la fila de estacionalidad. El saldo mínimo del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El plan de negocio en Word de este pack cita las cifras de este Excel: si cambias una celda verde, el Excel '
        'manda. La calculadora del pollo, el asador y el escandallo del pack va aparte: mide cuánto rinde un pollo y '
        'cuántos caben en el asador antes de la punta del domingo, y ESCANDALLA el pollo y los combos; no copies el '
        'food cost de un pollo o de un combo en la hoja de Supuestos. La celda «Coste de mercancía sobre las ventas de '
        'COMIDA» es la media ponderada de TODA la carta (pollo, patatas, croquetas, ensaladilla, menús de sala, cada uno '
        'por lo que vende) más la merma, y por eso sale más baja que el food cost del pollo entero. Con los escandallos '
        'de tu carta, comprueba que esa media cuadra.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Enero', 'Decisión del plan',
         'En el orden del calendario: la rampa cae sobre los meses más flojos y el fondo de maniobra lo cubre; julio y '
         'agosto son el pico. Si abres en otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Mercado del pollo asado en España', 'Unos 2,5 millones de pollos a la semana en unos 12.000 locales',
         'Interempresas / Efeagro, julio de 2026',
         'Unos 208 pollos por asador y semana de media; en verano, un 15 % más en el interior y hasta un 35 % más en la '
         'costa. El caso vende unos 301'),
        ('Pollo entero asado para llevar', '11-14 € con IVA',
         'Cartas de asadores de pollos de Getxo, Sevilla y Ciudad Real leídas en 2026',
         'El caso lo pone a 12,90 €. En Barcelona, el pollo al ast va de 13,90 a 20,50 €; en la pollería peruana, el '
         'medio pollo con papas de 14,50 a 16 €'),
        ('Coste del pollo entero', 'Un 38,8 % de su precio sin IVA',
         'Estimación del kit con los valores de la calculadora del pack (editables)',
         'Pollo de 1,45 kg en canal a 3,05 € el kilo más 0,13 € de sazón, aceite y sal: unos 4,55 €. El pollo es un '
         'precio estimado por el kit: pon el de tu proveedor'),
        ('Rendimiento del pollo entero asado', 'Un 78 % (de un 68 a un 84 %)',
         'USDA, Table of Cooking Yields for Meat and Poultry',
         'Dato de horno, no de asador de espadas: el caso usa un 76 %. Pesa cinco pollos crudos y asados de la misma '
         'carga y mide el tuyo con la calculadora del pack'),
        ('Asador de pollos de gas de doce espadas', '4.373-5.967 € sin IVA',
         'Catálogo de asadores de un distribuidor de hostelería, 2026',
         'De 4 a 6 pollos por espada; las espadas se compran aparte. El de ocho espadas va de 2.493 a 4.126 €'),
        ('Comisión de la plataforma con su reparto', '13-35 % más IVA',
         'Guías del sector, 2025-2026: compruébalo en tu contrato',
         'El plan básico de Uber Eats ronda el 30 %. Lo que se recoge en el mostrador o por encargo no paga comisión'),
        ('IVA del pollo asado', '10 %', 'Ley 37/1992, art. 91.Uno.1.1.º y 2.2.º',
         'En sala, para llevar y por plataforma. La cerveza, el vino y los refrescos con azúcares o edulcorantes '
         'añadidos que salen del local, al 21 %; el pan común, al 4 % (art. 91.Dos.1.1.º a)'),
        ('Comidas preparadas en caliente y en frío', '≥ 63 °C · 60 → 10 °C en < 2 h · 74 °C 15 s',
         'Real Decreto 1086/2020, art. 30, en la redacción del Real Decreto 1021/2022',
         'El pollo en la vitrina caliente, a 63 °C o más; lo que sobra se enfría de 60 a 10 °C en menos de 2 h y se '
         'recalienta a 74 °C durante 15 s en el centro, en la hora siguiente a sacarlo del frío. Ninguna norma fija la '
         'temperatura de cocción del pollo: el caso pide 74 °C en el muslo con sonda como criterio de su APPCC'),
        ('Mayonesa, alioli, ensaladilla y cremas sin cocción', 'Ovoproducto · ≤ 8 °C · 24 h',
         'Real Decreto 1021/2022, art. 9.2 y 9.3',
         'Sin huevo crudo: ovoproducto de un establecimiento autorizado, a 8 °C o menos, consumo en 24 horas y registro '
         'de la fecha y la hora de elaboración. El pollo crudo, a 4 °C o menos, y las mollejas, a 3 °C o menos (art. 4.1)'),
        ('Salario mínimo interprofesional 2026', '1.221 € al mes en 14 pagas', 'Real Decreto 126/2026',
         'A prorrata en jornada parcial'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'No nombra la pollería ni el asador de pollos: entran como restaurante. Copia tu tabla salarial en la celda de '
         'Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_pol.py` entero (`datos_checklist.py`): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO de la compra de COMIDA (R §1): pollo, aceite, patata congelada, croquetas y salsas compradas al 10 %
#: (≈ 85 %); patata fresca, verdura, pan y huevos al 4 % (≈ 15 %) → 0,85 × 10 + 0,15 × 4 = 9,1 %. La bebida tiene su
#: propio tipo de compra (`pct_bebida_alc`, 17,7 %): no se mezcla aquí.
IVA_COMPRAS = {
    'comida': 0.091,
    'nota': 'Pollo, aceite, patata congelada y salsas compradas al 10 %; patata fresca, verdura, pan y huevos al 4 % '
            '(art. 91.Dos.1.1.º de la Ley 37/1992). Ajústalo a tus facturas',
}
