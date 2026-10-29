#!/usr/bin/env python3
"""
Contenido de `plan-negocio-taqueria` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Semilla = la Pizzería ES 1.0 publicada:
`plan-taqueria/semilla_taq.py` copia sus dos xlsx (plan + checklist, solo lectura), les pone las 18 partidas, los 9
fijos, los títulos, las pagas 7/12 y el checklist de la taquería, y `main.py` + `grupo_a.py` los reconstruyen con este
módulo (mecánica de la pizzería: dos servicios, producción antes de abrir, rotación encendida, bebida con línea
partida). Cómo y por qué: `plan-taqueria/F1-camino.md` §1-§3 (la §2 hace de SPEC, firmada el 29-oct); caso y fuentes:
`plan-taqueria/F1-research-taqueria.md` §1-§3 (R §n).

MOTOR DE INGRESOS (taquería de dos servicios con para llevar y domicilio)
-----------------------------------------------------------------------
    cubiertos_dia (B4) = COMENSALES EQUIVALENTES AL DÍA (57 de sala + 20 de llevar y domicilio)   77
    ticket_medio  (B5) = € POR COMENSAL SIN IVA                                                 15,50 €
    dias_apertura (B6) = DÍAS DE APERTURA AL AÑO                                                300
Ventas a régimen = 77 × 15,50 × 300 = 358.050 €. Mes 1 = ENERO, sin girar (F1-camino §2): la estacionalidad va en el
orden del calendario y las pagas extra salen en los meses 7 (julio) y 12 (diciembre).

IVA: la comida al 10 % (sala, llevar y domicilio, sin partir); la bebida con la LÍNEA PARTIDA del motor
(`grupo_a.py:2291-2314`): su columna H («Bebida para llevar o a domicilio al 21 %») declara la parte que sale del local
al tipo general (alcohol y aguas frescas o refrescos con azúcares o edulcorantes añadidos, LIVA 91.Uno.1.1.º a y b),
H = 7,5 % (= 1,5 % de las ventas, R §3); el resto, al 10 %. Con la línea partida, `iva_bebida` (B63) no tiene efecto y
`pct_bebida_alc` (B62) sólo mueve el IVA SOPORTADO de la compra de bebida: rótulo propio, 75 % (cerveza, mezcal,
tequila y refrescos al 21 %; agua e ingredientes de las aguas frescas al 10 %) → 18,25 % (R §1).
`IVA_COMPRAS` es SOLO la compra de COMIDA (8,5 %): la bebida ya lleva su tipo (lección de la Pizzería, F2-NOTAS §2.3).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «R §n» = `F1-research-taqueria.md` §n (casi todo
[estimado], criterio de kit, con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado D9» =
ajustado en F2 para cumplir los gates del caso.

⚠️ Rótulos de importe: sin «comensales», «personas», «días», «meses», «años», «plazas» ni «unidades»
(`motor.RX_RECUENTO_DV` les quita el formato de euro). «Campana» siempre «campana extractora» (`motor.TILDES` la
acentúa a «campaña») y nunca el verbo «publica» (lo acentúa a «pública»). Las notas no usan «cubierto» (el VOCABULARIO
lo traduce) ni restos de los moldes (pizza, napolitana, leña, masa de trigo…: `barrido_es.py`). Sesión Claude Code,
29-oct-2026.
"""

CONCEPTO = 'Taquería'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Masculino «comensal» = masculino
#: «cubierto»: sin arreglos de concordancia. Las 9 frases del motor = las de la Pizzería (F1-camino §1), con la compra
#: al 21 % y «los tacos incluidos» de la taquería; sin las 2 de septiembre. La última traduce la nota `O5` de la
#: Tesorería al calendario de la taquería (Mes 1 = enero).
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
        '21 %» de esta hoja: la cerveza, el mezcal, el tequila y los refrescos con azúcares o edulcorantes añadidos, '
        'cuya factura va al 21',
    'el alcohol que sale por delivery, al general; el pan común y las harinas panificables, al superreducido (art. '
    '91.Dos.1.1.º':
        'la parte de la bebida que sale para llevar o a domicilio y declara la columna H de su línea (alcohol y aguas '
        'frescas o refrescos con azúcares o edulcorantes añadidos), al general (art. 91.Uno.1.1.º',
    'los alimentos —bollería y pastelería incluidas—, que son':
        'los alimentos —los tacos incluidos—, que son',
    # Instrucciones!A8 (frase del motor; LIVA art. 91.Uno.1.1.º b): «azúcares o edulcorantes añadidos»
    'el alcohol y los refrescos o zumos con azúcares añadidos para llevar':
        'el alcohol y las aguas frescas, los refrescos o los zumos con azúcares o edulcorantes añadidos para llevar',
    # resto del molde en Tesorería!D31 (barrido_es.py: «versión 1.1»)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # Tesorería!O5 (nota del motor de la fila de estacionalidad), F1-camino §2: Mes 1 = enero
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = ENERO, en el orden del calendario: enero y agosto son los meses más flojos y los picos llegan en '
        'septiembre (Independencia de México, 15 y 16), noviembre (Día de Muertos) y diciembre. Si abres en otro mes, '
        'gira la fila',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 77, None,
        'Comensales equivalentes al día, media del año: unos 57 en sala (la terraza incluida de abril a octubre) y unos '
        '20 de para llevar y domicilio, que son los pedidos (unos 15 al día de unos 20,50 € sin IVA) divididos por el '
        'ticket. Un sábado, unos 125 con los pedidos; un martes, unos 55. Contrástalo con el paso de gente de tu calle '
        'un viernes por la noche y un martes a mediodía',
        'R §3 [estimado]'),
    'ticket_medio': (
        None, None, 15.50, None,
        'SIN IVA, por comensal: una orden de 3 tacos (8,50 € con IVA), medio taco suelto, algo de gringa o quesadilla, '
        'algún entrante, 1,1 bebidas y algún postre suman unos 17,40 € con IVA en sala; el caso se queda en 15,50 € sin '
        'IVA por los combos de mediodía. El taco al pastor del caso cuesta 3,00 € con IVA, dentro de la franja de '
        '2,50-3,50 € de las taquerías casuales de ciudad (cartas leídas en octubre de 2026). El precio con IVA está en la '
        'fila «PVP equivalente con IVA» de abajo',
        'R §2-§3 (carta del caso) [estimado]'),
    'dias_apertura': (
        None, None, 300, None,
        '365 días menos los 52 lunes de cierre, 12 días de cierre en enero (mantenimiento y vacaciones) y el 25 de '
        'diciembre. Es el MISMO dato para la cuenta de resultados, el punto de equilibrio, los escenarios y las horas de '
        'personal',
        'R §3 [estimado]'),
    'crec_a2': (
        None, None, 0.06, None,
        'Clientela que repite y más pedidos para llevar el segundo año. Se aplica a los comensales con el mismo ticket; '
        'el personal NO sube con este porcentaje: sale de la hoja Personal',
        'R §3 [estimado] (= pizzería)'),
    'crec_a3': (
        None, None, 0.04, None,
        'Sobre el año 2. Conservador: el techo lo ponen el trompo, la plancha y las 32 plazas los viernes y los sábados '
        'por la noche',
        'R §3 [estimado]'),
    'pct_comida': (
        None, None, 0.80, None,
        'Tacos, gringas y quesadillas, entrantes y postres (en sala, para llevar y a domicilio) sobre las ventas; el 20 % '
        'restante es la bebida. Es el peso de la primera línea de ventas del P&L',
        'R §3 [estimado] (80/20)'),
    'coste_comida': (
        None, None, 0.27, None,
        'Materia prima de la comida sobre sus ventas: el taco al pastor sale a un 22,5 % (un 24 % en la orden de 3), las '
        'carnitas, el suadero y la barbacoa a un 26-30 %, la gringa a un 23 % y el guacamole a un 22-28 % según el '
        'aguacate: un 25 % de media, más 1,5 puntos de merma (el sobrante del trompo y las salsas crudas que se tiran) y '
        'medio punto de prudencia, porque la carne y la tortilla son precios estimados por el kit. Escandalla cada taco '
        'con la calculadora del pack',
        'R §2-§3 [estimado]'),
    'coste_bebida': (
        None, None, 0.26, None,
        'Aguas frescas al 12 %, cerveza mexicana al 33 %, mezcal y tequila al 28 % y refrescos y agua al 30 % de su '
        'precio de venta, en una mezcla de 30/45/10/15. Si la cervecera te cede el equipo de tiraje, pide el precio del '
        'barril por escrito',
        'R §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.035, None,
        'Envases para llevar y a domicilio, tarrinas de salsa, papel, servilletas, guantes y los envases para que el '
        'cliente se lleve lo que no consuma (Ley 1/2025, art. 8). El envase de plástico de un solo uso se cobra aparte '
        'en el tique (Ley 7/2022, art. 55)',
        'R §1-§3 [estimado] · BOE'),
    'pct_delivery': (
        None, None, 0.12, None,
        'Ventas por PLATAFORMA con su reparto (Glovo, Just Eat, Uber Eats) sobre el total. Lo que se recoge en el local '
        'NO paga comisión y no va aquí. La tortilla llega peor tras el viaje: la orden «para armar» lo aguanta, pero no '
        'subas de aquí sin probarlo',
        'R §3 [estimado]'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión de la plataforma con su reparto sobre lo que vende ese canal: el plan básico de Uber Eats ronda el '
        '30 % más IVA, Glovo va del 15 al 35 % según la zona y Just Eat, del 25 al 35 % con su reparto. Compruébala en '
        'tu contrato. Si repartes tú, pon 0 y suma el repartidor, con contrato laboral, a la hoja Personal',
        'R §2 (guías del sector) [estimado]'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado',
        'molde (= pizzería)'),
    'alquiler_mes': (
        None, None, 1450, None,
        'Local de 80 m² con salida de humos a cubierta posible (es el filtro del local): sala de 45 m² con 24 plazas en '
        'mesa y 8 en barra, cocina de 20 m² a la vista con el trompo, la plancha y el comal, aseos (uno adaptado) y '
        'almacén, en una calle con paso cerca de una zona universitaria o de ocio de una ciudad media, sin traspaso: '
        'unos 18 € el m². El peso sobre las ventas lo calcula el propio libro en la fila «Alquiler / Ventas» del P&L',
        'R §2-§3 [estimado]'),
    'fianza_meses': (
        None, None, 2, None,
        'Dos meses de renta, lo habitual en un contrato de local de negocio: compruébalo con tu abogado',
        'R §3 [estimado]'),
    'suministros_mes': (
        None, None, 850, None,
        'Luz (frío, extracción, climatización y cafetera), el gas del trompo, la plancha, el comal y los fogones, y el '
        'agua. Pide el histórico del local',
        'R §3 [estimado]'),
    'seguros_ano': (
        None, None, 1400, None,
        'Responsabilidad civil de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la '
        'aseguradora que trabajas con trompo, plancha y freidora a gas: cambia la prima y las condiciones',
        'R §3 [estimado]'),
    'pct_varios': (
        None, None, 0.02, None,
        'Colchón de gasto corriente no presupuestado (pequeñas reparaciones, utillaje que se rompe, pruebas de carta)',
        'molde (= pizzería)'),
    'recursos_propios': (
        None, None, 55000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'R §3 [estimado]'),
    'prestamo': (
        None, None, 118000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D9, vuelta 1: cubre la necesidad de caja del libro con 55.000 € propios (R §3: 115.000 €; el libro '
        'sale unos 3.000 € por encima de la cuenta a mano con la fila de suplencias y la tasa de terraza)'),
    'tipo_prestamo': (
        None, None, 0.06, None,
        'Tipo nominal anual. Pide oferta a dos entidades y a una línea ICO antes de fijarlo; el frío y el equipo de '
        'cocina se pueden pagar con leasing o renting: compáralo',
        'R §3 (= pizzería) [estimado]'),
    'plazo_prestamo': (
        None, None, 7, None, 'Años totales, carencia incluida',
        'R §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: obra, conducto de humos y cocina antes de facturar. Desde el segundo año se '
        'devuelve el principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'R §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: el colchón para la rampa del arranque, que con el Mes 1 en enero cae sobre los '
        'meses más flojos del año (enero y febrero)',
        'molde (mínimo de la familia) · R §3'),
    'vida_obra': (
        None, None, 10, None,
        'Obra, conducto de extracción hasta cubierta, instalación eléctrica, fontanería, gas, climatización, rótulo y '
        'fachada. Coeficientes de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades: confírmalo con tu '
        'asesor',
        'R §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Trompo, plancha y comal, freidora, campana extractora, frío, lavavajillas, barra, mobiliario y TPV: un 10 % '
        'anual, dentro del coeficiente máximo de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades para la '
        'maquinaria (12 %) y para el mobiliario (10 %). Confírmalo con tu asesor',
        'R §3 dice 9 años; 10, como la pizzería (F1-camino §2: cumple también el coeficiente del mobiliario)'),
    'pct_bebida_alc': (
        None, 'Bebida que compras al 21 % (cerveza, mezcal, tequila y refrescos azucarados o edulcorados) sobre el '
              'total de bebida', 0.75, None,
        'Sólo mueve el IVA que SOPORTAS al comprar la bebida: la cerveza, el mezcal, el tequila y los refrescos con '
        'azúcares o edulcorantes añadidos te los facturan al 21 %; el agua y los ingredientes de las aguas frescas que '
        'preparas tú, al 10 % (la fruta fresca, al 4 %). Con un 75 % sale un 18,3 %. El IVA que REPERCUTES lo fija la '
        'línea de bebida del P&L (columna H)',
        'R §1 (IVA de compras) · LIVA art. 91 (BOE)'),
    'aforo': (
        None, 'Aforo del local (plazas sentadas, sin la terraza)', 32, None,
        'Plazas interiores: 24 en mesa y 8 en barra. La terraza suma 16 plazas de abril a octubre, con su autorización '
        'municipal aparte, y quien se lleva los tacos o los recibe en casa no ocupa mesa: por eso la rotación de la fila '
        'de arriba es más alta que la real de tu sala',
        'R §3 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'Las taquerías van al convenio PROVINCIAL de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal '
        'para el sector de Hostelería no nombra la palabra «taquería», pero incluye los restaurantes y el reparto de '
        'comidas preparadas. Copia aquí el salario base del grupo más bajo de la tabla de TU provincia. Con 0 el '
        'semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.75, None,
        'Una taquería que abre trae curiosos el primer mes, pero la clientela fija tarda un trimestre: el Mes 1 '
        '(enero) factura un 75 % de lo que facturará a los cuatro meses. Con 100 % se elimina la rampa',
        'R §3 [estimado] (= pizzería)'),
    'meses_rampa': (
        None, None, 4, None,
        'Cuatro meses hasta el ritmo de crucero: de enero a abril, para llegar a la terraza de primavera con clientela',
        'R §3 [estimado]'),
    'meses_renta_previa': (
        None, None, 2, None,
        'Dos meses de renta antes de abrir: la obra, el conducto de humos y la licencia. Si el banco te da el préstamo '
        'al empezar la obra, súmale los intereses de esos meses, que este libro no cuenta, y ten en cuenta que la '
        'carencia corre desde la firma',
        'R §3 [estimado] (obra más corta que la de la pizzería: sin chimenea de leña)'),
    'pct_imprevistos': (
        None, None, 0.10, None,
        'Colchón sobre la obra y las instalaciones del local, que es donde aparecen las sorpresas (el conducto hasta '
        'cubierta, la instalación de gas, el separador de grasas). Un banco no financia una reforma sin él',
        'R §3 (10 % sobre la obra) [estimado]'),
    'dias_cobro': (
        None, None, 2, None,
        'Media ponderada: la sala y lo que se recoge en el local cobran al momento y la plataforma liquida cada 7-15 '
        'días lo que vende por ella (un 12 % de las ventas)',
        'R §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a los proveedores de carne, tortilla, verdura y bebida: lo que te financian. Es lo primero que '
        'se pierde si te retrasas en un pago',
        'molde (= pizzería)'),
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
        '91.Uno.2.2.º de la Ley 37/1992); para llevar o a domicilio, el alcohol y las aguas frescas y los refrescos con '
        'azúcares o edulcorantes añadidos, al 21 %, en la columna H de esa línea',
        'Ley 37/1992 art. 91.Uno.1.1.º y 2.2.º (BOE)'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente, tipo de IVA). Dos líneas: `mix_en_supuestos` (el peso se teclea en
#: Supuestos). La comida va al 10 % sin partir; la bebida, PARTIDA (sexto campo, `grupo_a.py:2291-2314`).
LINEAS_INGRESO = (
    ('Ventas de taquería y cocina (sala, para llevar y a domicilio)', 0.80, 'comida',
     'Tacos, gringas y quesadillas, entrantes y postres: en sala unos 74 % de las ventas, para llevar unos 14 % y por '
     'plataforma un 12 %. Todo al 10 % de IVA, se coma en la mesa o salga del local (art. 91.Uno.1.1.º y 2.2.º de la '
     'Ley 37/1992)',
     'R §3 [estimado] · LIVA (BOE)'),
    ('Ventas de bebida (aguas frescas, cerveza, mezcal y tequila, refrescos y agua)', 0.20, 'bebida',
     'Bebida de sala y la que sale con los pedidos',
     'R §3 [estimado]',
     {'cabecera': 'Bebida para llevar o a domicilio al 21 % (%)',
      'pct': 0.075,
      'tipo': 0.21,
      'nota': 'La columna H es la parte de la bebida que sale del local y va al 21 %: el alcohol y las aguas frescas y '
              'los refrescos con azúcares o edulcorantes añadidos (art. 91.Uno.1.1.º a y b de la Ley 37/1992); el agua '
              'y lo que no lleve azúcares ni edulcorantes añadidos, y toda la bebida en sala, al 10 %. Un 7,5 % = un '
              '1,5 % de las ventas'}),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada; todos por encima del SMI 2026 en proporción (1.221 € × jornada, RD 126/2026). Las 6
#: filas de R §3 + la de suplencias que exige el molde (7 filas: Pizzería F2-NOTAS §2.1) = 4,60 jornadas.
PLANTILLA = (
    ('Titular — taquero/a jefe: marinado, trompo, compras y gestión', 1, 1900,
     'Marina y monta el trompo, lleva el corte en el turno fuerte, compra (el importador de chiles y producto mexicano '
     'incluido) y gestiona. Como administrador de la SL cotiza en el régimen de autónomos: el libro le imputa el 33 % '
     'de Seguridad Social sobre 14 pagas como si fuera nómina, que es el lado prudente. Confirma con tu gestoría la '
     'cuota real y si te aplica la reducida de inicio',
     'R §3 [estimado]', 1.0),
    ('Taquero/a de trompo, plancha y comal', 1, 1450,
     'Corta el trompo, lleva la plancha y el comal y sabe marinar con el titular. Es inversión, no gasto: si sólo el '
     'titular sabe marinar y cortar el trompo, una baja cierra la taquería',
     'R §3 y §6 [estimado]', 1.0),
    ('Cocinero/a de producción y salsas', 1, 1013,
     'Carnitas y guisados, salsas, aguas frescas, mise en place y friegue, 30 horas a la semana',
     'R §3 [estimado]', 0.75),
    ('Encargado/a de sala, barra y mostrador', 1, 1450,
     'Todo el año: sala, barra, caja, pedidos para llevar, la tablet de las plataformas y la información de alérgenos',
     'R §3 [estimado]', 1.0),
    ('Camarero/a de cenas y fines de semana', 1, 675,
     '20 horas a la semana: las cenas y el fin de semana, cuando la sala se llena',
     'R §3 [estimado]', 0.50),
    ('Refuerzo de viernes a domingo: barra, terraza y recogidas', 1, 338,
     'Barra y terraza en temporada y el mostrador de recogidas. Este plan NO tiene reparto propio: si lo pones, el '
     'repartidor va con contrato laboral del convenio de hostelería, nunca como autónomo',
     'R §3 [estimado] · ALEH VI art. 4 · ET DA 23.ª', 0.25),
    # RC-19: la fila de suplencias que trae el molde (7 filas); sin ella el control de «fórmulas perdidas» de main.py
    # marca las del total de la hoja Personal (Pizzería F2-NOTAS §2.1)
    ('Suplencias de vacaciones y descansos', 1, 130,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso semanal del equipo de todo el año',
     'molde (RC-19, = pizzería)', 0.10),
)

#: Cobertura: sala, trompo y plancha (horas × personas a la vez) + producción ANTES de abrir, por los días de apertura.
COBERTURA = {
    'horas_dia': 8.5,
    'personas_franja': 2.7,
    'horas_produccion': 2.5,
    'personas_produccion': 1.5,
    'nota_horas': 'Horas con el local abierto al público, sumando las comidas (13:30-16:30) y las cenas (20:00-23:30) '
                  'y la preparación de cada servicio. La tarde de cierre entre los dos no se cuenta',
    'nota_personas': 'Presencia media a la vez entre el trompo, la plancha o el comal, la sala y el mostrador. El sábado '
                     'por la noche hacen falta cinco: entran el refuerzo y el camarero de cenas (el cuadrante anual no '
                     'lo ve: ponlo en el turno)',
    'nota_horas_produccion': 'Marinado del día siguiente, montaje del cono, carnitas y guisados, salsas y mise en place '
                             'antes de abrir',
    'nota_personas_produccion': 'El titular con el cocinero de producción. El cierre, la limpieza y las compras quedan '
                                'fuera de este cuadrante: son el margen entre las horas contratadas y las necesarias',
}

#: Rotación ENCENDIDA: techo 3 (sábado 1,06 + 1,94, R §3) y la referencia de que el domicilio no ocupa mesa (< 255 car.).
ROTACION = {
    'max': 3.0,
    'nota_max': 'Servicios completos por plaza y día que puedes hacer con comidas, cenas y un segundo turno de cena el '
                'sábado (estancias de 35-45 minutos). Es el techo físico del local, no un objetivo',
    'referencia': 'Incluye a quien se lleva los tacos o los recibe en casa, que no ocupa mesa: la rotación real de tu '
                  'sala es menor (en el caso, unos 57 comensales de sala, 1,8 por plaza y día).',
}

#: Partidas de la hoja de inversión: las escribe `semilla_taq.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-24
#: del molde; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = base de los
#: imprevistos, 10 años; 'maquinaria' = 10 años).
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|marca|\bweb\b|'
           r'foto|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|formaci[oó]n|seguro|licencia|permiso|'
           r'\btasas?\b',),
    'obra': (r'proyecto t[eé]cnico|\bobra\b|conducto|salida de humos|instalaci[oó]n el[eé]ctrica|fontaner|'
             r'climatizaci|r[oó]tulo|fachada',),
    'maquinaria': (r'trompo|asador|plancha|comal|freidora|fog[oó]n|ba[ñn]o mar[ií]a|campana|armarios?|congelador|'
                   r'lavavajillas|fregadero|utillaje|menaje|barra|cafetera|mobiliario|terraza|tpv|dat[aá]fono',),
}

#: Costes fijos. Las 9 partidas propias (13.800 €/año) las escribe `semilla_taq.py` en las filas 26-34 (rótulo e
#: importe); aquí, la nota por rótulo normalizado (minúsculas y sin tildes) y la de la fila canónica del alquiler.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Los dos meses de renta '
              'previos a la apertura están en la hoja de Inversión y NO se cuentan dos veces'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL, nóminas y contratos de la plantilla'),
    'mantenimiento de la campana extractora, el gas y el frio': (
        None, 'Limpieza de la campana extractora y del conducto al menos una vez al año (Madrid lo exige en su '
              'Ordenanza 4/2021, art. 23; mira la de tu ayuntamiento), revisión del gas y del trompo y el frigorista'),
    'marketing y publicidad': (
        None, 'Ficha de Google Business, redes sociales, fotos y las fechas mexicanas (la Independencia en septiembre, '
              'el Día de Muertos en noviembre); la campaña de apertura va en la inversión'),
    'software, tpv, telefono e internet': (
        None, 'Cuota del TPV con Veri*factu, la tablet de las plataformas, teléfono e internet'),
    'limpieza, lavanderia, epi y analisis de autocontrol': (
        None, 'Productos de limpieza, lavado de uniformes y paños, guantes y los análisis de autocontrol que fije tu '
              'APPCC'),
    # calibrado (F1-camino §1, vuelta 1): la terraza de 16 plazas paga su tasa de ocupación, que el research no
    # contaba; va en la fila de los residuos (las dos son tasas municipales) para no pasar de las 9 filas del molde
    # (una 10.ª desplaza el P&L: Pizzería F2-NOTAS §2.2). 500 € de residuos + 1.200 € de terraza = 1.700 €.
    'tasa de terraza y gestion de residuos (pon las de tu ayuntamiento)': (
        None, 'La ocupación de la vía pública con 4 mesas de abril a octubre (unos 1.200 € de ejemplo: cada '
              'ayuntamiento tiene su ordenanza fiscal y este plan no ha leído ninguna) y la tasa de basuras, el cartón '
              'y el aceite y la grasa usados con gestor autorizado (unos 500 €). Pon las de tu ayuntamiento'),
    'desinsectacion, desratizacion y desinfeccion (ddd)': (
        None, 'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
    'derechos de autor por musica ambiental (sgae y agedi-aie)': (
        None, 'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los metros y del aforo de tu sala'),
    'prevencion de riesgos laborales, vigilancia de la salud y formacion': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): cortes en el trompo, quemaduras de la plancha y la '
              'freidora, gas y calor; los reconocimientos médicos de la plantilla y la formación en higiene y '
              'alérgenos'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Margen bruto al 60 % y no al 72 % del research: el 72 % es el margen sobre la
#: mercancía sola, y el del libro descuenta TODOS los costes variables (el caso da un 63 %; = pizzería).
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.60,
     'Suelo del margen tras TODOS los costes variables (mercancía, envases, plataforma, medios de pago y varios). Sólo '
     'con la mercancía, una taquería deja en torno a un 73 %. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.29,
     'Techo de la materia prima sobre ventas: el taco al pastor sale a un 22,5 % y las carnitas, el suadero, la barbacoa '
     'y el aguacate la suben. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'Techo del personal sobre ventas con dos taqueros y una sala de dos servicios. Estimación del kit'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del alquiler sobre ventas para un local con salida de humos a cubierta: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga. Una taquería bien llevada deja en torno a un 9 %. '
     'Estimación del kit'),
)

#: (comensales al día, € por comensal sin IVA, días de apertura). R §3.
ESCENARIOS = {
    'pesimista': (65, 14.75, 295),     # menos comensales, ticket más bajo y una semana más de cierre
    'optimista': (88, 16.50, 305),
}

#: Mes 1 = ENERO, sin girar (F1-camino §2): el calendario de R §3 tal cual (enero y febrero flojos, terraza de abril a
#: junio, agosto cae, septiembre y noviembre por las fechas mexicanas, diciembre pico). La tupla rotada de R §3 no se usa.
ESTACIONALIDAD = (0.070, 0.074, 0.082, 0.086, 0.088, 0.088,
                  0.084, 0.070, 0.088, 0.088, 0.086, 0.096)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es ENERO, en el orden del calendario: la rampa del arranque cae sobre enero y febrero, los '
        'meses más flojos, y por eso el fondo de maniobra cuenta. Si abres en otro mes, gira la fila de estacionalidad. '
        'El saldo mínimo del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El plan de negocio en Word de este pack cita las cifras de este Excel: si cambias una celda verde, el Excel '
        'manda. La calculadora del trompo y escandallo del pack va aparte y sirve para medir el rendimiento del cono y '
        'ESCANDALLAR cada taco: no copies el food cost de un taco en la hoja de Supuestos. La celda «Coste de mercancía '
        'sobre las ventas de COMIDA» es la media ponderada de TODA la carta (tacos, gringas, guisados, guacamole y '
        'postres, cada uno por lo que vende) más la merma, y por eso sale más alta que el food cost del taco al pastor. '
        'Con los escandallos de tu carta, comprueba que esa media cuadra.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Enero', 'Decisión del plan',
         'En el orden del calendario: la rampa cae sobre los meses más flojos y el fondo de maniobra lo cubre. Si '
         'abres en otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Taco al pastor en carta', '2,50-3,50 € con IVA',
         'Cartas de taquerías casuales de Madrid, Valencia y Bilbao leídas en octubre de 2026',
         'El caso lo pone a 3,00 € (la orden de 3, a 8,50 €). La taquería de volumen baja a 1-1,50 € y la de autor '
         'sube a 7-8 €'),
        ('Coste del taco al pastor', 'Un 22,5 % de su precio sin IVA (un 24 % en la orden de 3)',
         'Estimación del kit con los gramajes de la calculadora del pack (editables)',
         'Tortilla, 35 g de carne servida, piña, cebolla, cilantro, lima y salsa, con un 5 % de merma. La carne y la '
         'tortilla no tienen precio profesional publicado: pon los de tu proveedor'),
        ('Rendimiento del trompo', 'Unos 25 tacos por kg de carne cruda',
         'Puesto de Ciudad de México citado por Milenio (prensa)',
         'Con 35 g servidos y un 65 % de rendimiento salen unos 18-19 tacos por kg crudo: mide el tuyo con la '
         'calculadora del pack'),
        ('Trompo: asador vertical de gas de cuatro quemadores', '1.279-1.784 € sin IVA',
         'Catálogo de asadores verticales de un distribuidor de hostelería, octubre de 2026',
         'Para conos de 30-35 kg. El caso cuenta 1.800 € con la bandeja, los cuchillos y la base de la piña'),
        ('Comisión de la plataforma con su reparto', '15-35 % más IVA',
         'Guías del sector, 2025-2026: compruébalo en tu contrato',
         'El plan básico de Uber Eats ronda el 30 %. Lo que se recoge en el local no paga comisión'),
        ('IVA de los tacos', '10 %', 'Ley 37/1992, art. 91.Uno.1.1.º y 2.2.º',
         'En sala, para llevar y a domicilio. El alcohol y las aguas frescas y los refrescos con azúcares o '
         'edulcorantes añadidos que salen del local, al 21 %'),
        ('Comidas preparadas en caliente y en frío', '≥ 63 °C · 60 → 10 °C en < 2 h · 74 °C 15 s',
         'Real Decreto 1086/2020, art. 30, en la redacción del Real Decreto 1021/2022',
         'Caliente a 63 °C o más; enfriado de 60 a 10 °C en menos de 2 h; recalentado a 74 °C durante 15 s en el centro, '
         'en la hora siguiente a sacarlo del frío; refrigeradas a 4 °C o menos (8 °C si duran menos de 24 h). El pastor '
         'marinado es preparado de carne: 4 °C o menos en cámara (Real Decreto 1021/2022, art. 4.1)'),
        ('Salario mínimo interprofesional 2026', '1.221 € al mes en 14 pagas', 'Real Decreto 126/2026',
         'A prorrata en jornada parcial'),
        ('Coste de personal sobre ventas', '34-38 %', 'Estimación del kit',
         'Con el titular de taquero jefe y un segundo taquero: el taquero único es un riesgo, no un ahorro'),
        ('Alquiler sobre ventas', '5-10 %', 'Estimación del kit',
         'Un local con salida de humos a cubierta cuesta más encontrarlo que pagarlo'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'No nombra la «taquería»: entra como restaurante. Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_taq.py` entero (`datos_checklist.py`): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO de la compra de COMIDA (R §1): carne 45 % + tortilla 15 % + chiles, especias y producto importado 8 %
#: + manteca, aceite y otros 7 % al 10 % (= 75 %); verdura, fruta y aguacate 18 % + quesos 7 % al 4 % (= 25 %)
#: → 0,75 × 10 + 0,25 × 4 = 8,5 %. La bebida tiene su propio tipo de compra (`pct_bebida_alc`, 18,25 %): no se mezcla aquí.
IVA_COMPRAS = {
    'comida': 0.085,
    'nota': 'Carne, tortilla, chiles y especias al 10 %; verdura, fruta, aguacate y quesos al 4 % (art. 91.Dos.1.1.º '
            'de la Ley 37/1992). Ajústalo a tus facturas',
}
