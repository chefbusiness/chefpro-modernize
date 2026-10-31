#!/usr/bin/env python3
"""
Contenido de `plan-negocio-sushi-bar` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Semilla = la Taquería ES 1.0 publicada:
`plan-sushi/semilla_sus.py` copia sus dos xlsx (plan + checklist, solo lectura), les pone las 18 partidas, los 9 fijos,
los títulos y el checklist del sushi bar (las pagas 7/12 ya vienen de la Taquería), y `main.py` + `grupo_a.py` los
reconstruyen con este módulo (mecánica de la Taquería: dos servicios, producción antes de abrir, ROTACIÓN ENCENDIDA,
bebida con línea partida). Cómo y por qué: `plan-sushi/F1-camino.md` §1-§3 (la §2 hace de SPEC); caso y fuentes:
`plan-sushi/F1-research-sushi.md` §1-§3 (R §n).

MOTOR DE INGRESOS (sushi bar con barra a la vista, mesas, para llevar y a domicilio)
------------------------------------------------------------------------------------
    cubiertos_dia (B4) = COMENSALES EQUIVALENTES AL DÍA (45 de sala + 34 de llevar y domicilio)   79
    ticket_medio  (B5) = € POR COMENSAL SIN IVA                                                 20,00 €
    dias_apertura (B6) = DÍAS DE APERTURA AL AÑO                                                300
Un pedido para llevar o de plataforma = 1,6 comensales equivalentes (R §3). Ventas a régimen = 79 × 20,00 × 300 =
474.000 €. Mes 1 = ENERO, sin girar: la estacionalidad va en el orden del calendario y las pagas extra salen en los
meses 7 (julio) y 12 (diciembre).

IVA: la comida al 10 % (sala, llevar y domicilio, sin partir); la bebida con la LÍNEA PARTIDA del motor: su columna H
(«Bebida para llevar o a domicilio al 21 %») declara la parte que sale del local al tipo general (cerveza, sake, vino y
refrescos con azúcares o edulcorantes añadidos, LIVA 91.Uno.1.1.º a y b), H = 7 % (= 1,05 % de las ventas, R §3); el
resto, al 10 %. Con la línea partida, `iva_bebida` (B63) no tiene efecto y `pct_bebida_alc` (B62) sólo mueve el IVA
SOPORTADO de la compra de bebida (75 % al 21 % → 18,25 %). `IVA_COMPRAS` es SOLO la compra de COMIDA (8,7 %: el arroz,
la verdura, el aguacate, el huevo y el queso al 4 %, LIVA 91.Dos.1.1.º d-f, R §1).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «R §n» = `F1-research-sushi.md` §n (casi todo
[estimado], criterio de kit, con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado D9» =
ajustado en F2 para cumplir los gates del caso.

⚠️ Rótulos de importe: sin «comensales», «personas», «días», «meses», «años», «plazas» ni «unidades»
(`motor.RX_RECUENTO_DV` les quita el formato de euro). «Campana» siempre «campana extractora» (`motor.TILDES` la
acentúa a «campaña») y nunca el verbo «publica» (lo acentúa a «pública»). Las notas no usan «cubierto» (el VOCABULARIO
lo traduce) ni restos de los moldes (taco, trompo, pollo asado, pizza…: `barrido_es.py`). Sesión Claude Code,
31-oct-2026.
"""

CONCEPTO = 'Sushi Bar'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Masculino «comensal» = masculino
#: «cubierto»: sin arreglos de concordancia. Las 9 frases del motor = las de la Pollería (F1-camino §2), con la compra
#: al 21 % del sushi bar (cerveza, sake, vino y refrescos con azúcares o edulcorantes añadidos), «el sushi y el poke
#: incluidos» y SIN pan. La última traduce la nota `O5` de la Tesorería al calendario del sushi bar (Mes 1 = enero).
#: `VOCABULARIO_SIN_TILDES` (= Pollería): sin él, las claves con tilde no casan (`grupo_a.compilar_vocabulario`).
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubierto': 'comensal',
    'cubiertos': 'comensales',
    # las tres frases del motor: la línea partida de la bebida, no el canal de delivery
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
        '21 %» de esta hoja: la cerveza, el sake, el vino y los refrescos con azúcares o edulcorantes añadidos, cuya '
        'factura va al 21',
    # Tesorería (nota de la fila del IVA repercutido): el motor cierra el paréntesis. Sin pan en el sushi bar.
    'el alcohol que sale por delivery, al general; el pan común y las harinas panificables, al superreducido (art. '
    '91.Dos.1.1.º':
        'la parte de la bebida que sale para llevar o a domicilio y declara la columna H de su línea (cerveza, sake, '
        'vino y refrescos con azúcares o edulcorantes añadidos), al general (art. 91.Uno.1.1.º a y b); la comida, '
        'también la que sale para llevar o a domicilio, al reducido (art. 91.Uno.2.2.º',
    'los alimentos —bollería y pastelería incluidas—, que son':
        'los alimentos —el sushi y el poke incluidos—, que son',
    # Instrucciones!A8 (frase del motor; LIVA art. 91.Uno.1.1.º b): «azúcares o edulcorantes añadidos»
    'el alcohol y los refrescos o zumos con azúcares añadidos para llevar':
        'el alcohol y los refrescos o los zumos con azúcares o edulcorantes añadidos para llevar',
    # resto del molde en Tesorería!D31 (barrido_es.py: «versión 1.1»)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # Tesorería!O5 (nota del motor de la fila de estacionalidad). Picos que casan con la tupla (m7): diciembre 0,092
    # (el máximo), febrero sube de 0,082 a 0,086 y agosto 0,066 (el mínimo).
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = ENERO, en el orden del calendario: diciembre es el pico (bandejas de Nochebuena y Nochevieja), '
        'febrero sube con San Valentín y agosto es el mes más flojo (cierre de 10 días y ciudad vacía). En la costa, '
        'agosto sube. Si abres en otro mes, gira la fila',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 79, None,
        'Comensales equivalentes al día, media del año: unos 45 en sala (barra y mesas) y unos 34 de para llevar y '
        'domicilio, que son los pedidos (unos 7,5 para recoger y 14 de plataforma al día) contando cada pedido como '
        '1,6 comensales. Un sábado, unos 114 con los pedidos; un martes, unos 52. Contrástalo con el paso de gente de '
        'tu calle un viernes por la noche y un martes a mediodía',
        'R §3 [estimado]'),
    'ticket_medio': (
        None, None, 20.00, None,
        'SIN IVA, por comensal: en sala, el menú del día de mediodía (14,90 € con IVA, un 30 % de la sala) y la cena '
        'o el fin de semana (28,60 € con IVA) dejan unos 22,26 € sin IVA; el pedido para llevar (un combinado de 24 '
        'piezas y un extra, 27,00 € con IVA) sale a 15,34 € por comensal equivalente y el de plataforma, con el precio '
        'un 15 % más alto, a 18,47 €. La media de los tres canales da 20,14 €; el caso se queda en 20,00 €. El precio '
        'con IVA está en la fila «PVP equivalente con IVA» de abajo',
        'R §2-§3 (carta del caso) [estimado]'),
    'dias_apertura': (
        None, None, 300, None,
        '365 días menos los 52 lunes de cierre, 10 días de cierre en agosto y 3 festivos sueltos (Navidad, Año Nuevo '
        'y Reyes). Es el MISMO dato para la cuenta de resultados, el punto de equilibrio, los escenarios y las horas '
        'de personal',
        'R §3 [estimado]'),
    'crec_a2': (
        None, None, 0.06, None,
        'Clientela que repite y más pedidos para llevar el segundo año. Se aplica a los comensales con el mismo '
        'ticket; el personal NO sube con este porcentaje: sale de la hoja Personal',
        'R §3 [estimado] (= Taquería)'),
    'crec_a3': (
        None, None, 0.04, None,
        'Sobre el año 2. Conservador: el techo lo ponen la barra, las 36 plazas los viernes y los sábados por la '
        'noche y lo que puede cortar un solo itamae',
        'R §3 [estimado]'),
    'pct_comida': (
        None, None, 0.85, None,
        'Sushi, sashimi y poke, la cocina caliente (gyozas, tempura, sopa de miso) y los postres, en sala, para llevar '
        'y a domicilio, sobre las ventas; el 15 % restante es la bebida (un 22 % de lo que se vende en sala y un 4 % '
        'de lo que sale del local). Es el peso de la primera línea de ventas del P&L',
        'R §3 [estimado] (85/15)'),
    'coste_comida': (
        None, None, 0.29, None,
        'Materia prima de la comida sobre sus ventas: un 29 %, el lado prudente. El escandallo teórico de la '
        'calculadora del pack sale en un 16 % de media ponderada (el nigiri de salmón, en un 11 %; el combinado de 24 '
        'piezas, en un 16 %), pero la cuenta real es lo que compras frente a lo que vendes: se pierden la merma del '
        'pescado que no se vende en la vitrina y del recorte que no se reaprovecha, la neta y el shari que pesan más '
        'que en el escandallo, el shari, el nori y las salsas que se tiran al cierre, las comidas del personal, las '
        'invitaciones y los errores de pedido y el menú del día, que deja poco margen; y el pescado es un precio '
        'estimado por el kit. Un japonés con pescado de calidad trabaja con un 30-35 %. Mide tu consumo el primer '
        'trimestre y cambia esta celda: cada punto vale unos 4.000 € al año',
        'R §2-§3 [estimado] · calculadora (FC_PONDERADO 16,1 %, FC_NIGIRI_SALMON 11,3 %, FC_COMBINADO_24 15,9 %)'),
    'coste_bebida': (
        None, None, 0.28, None,
        'Cerveza japonesa al 32 %, sake y vino al 30 %, refrescos y agua al 28 % y té al 10 % de su precio de venta, '
        'en una mezcla de 45/20/25/10. Pide el precio del sake y de la cerveza japonesa por escrito: dependen de un '
        'importador',
        'R §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Cajas de sushi, tarrinas de soja, palillos, bolsas, servilletas y toallitas (unos 0,90-1,20 € por pedido que '
        'sale del local) y los envases para que el cliente se lleve lo que no consuma (Ley 1/2025, art. 8). El envase '
        'de plástico de un solo uso se cobra aparte en el tique (Ley 7/2022, art. 55)',
        'R §1-§3 [estimado] · BOE'),
    'pct_delivery': (
        None, None, 0.25, None,
        'Ventas por PLATAFORMA con su reparto (Glovo, Just Eat, Uber Eats) sobre el total. Lo que se recoge en el local '
        'NO paga comisión y no va aquí. El combinado viaja bien; la tempura y las gyozas llegan peor: no subas de aquí '
        'sin probarlo',
        'R §3 [estimado]'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión de la plataforma con su reparto sobre lo que vende ese canal: el plan básico de Uber Eats ronda el '
        '30 % más IVA, Glovo va del 15 al 35 % según la zona y Just Eat, del 13 al 35 %. Compruébala en tu contrato. '
        'Si repartes tú, pon 0 y suma el repartidor, con contrato laboral, a la hoja Personal',
        'R §2 (guías del sector) [estimado]'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado',
        'molde (= Taquería)'),
    'alquiler_mes': (
        None, None, 1600, None,
        'Local de 95 m² que ya fue de restauración, con salida de humos a cubierta posible: barra de sushi a la vista '
        'con 8 taburetes, sala de 28 plazas, cocina eléctrica, cuarto frío y una zona de empaquetado de pedidos junto '
        'a la puerta, en un barrio con vida de noche de una ciudad de 150.000 a 500.000 habitantes, sin traspaso: unos '
        '17 € el m². El peso sobre las ventas lo calcula el propio libro en la fila «Alquiler / Ventas» del P&L',
        'R §2-§3 [estimado]'),
    'fianza_meses': (
        None, None, 2, None,
        'Dos meses de renta, lo habitual en un contrato de local de negocio: compruébalo con tu abogado',
        'R §3 [estimado]'),
    'suministros_mes': (
        None, None, 1100, None,
        'Luz (la cocina es eléctrica: arroceras, inducción, freidora y plancha; el frío del pescado y el congelador de '
        '−20 °C, la extracción y la climatización) y agua. Pide el histórico del local',
        'R §3 [estimado]'),
    'seguros_ano': (
        None, None, 1800, None,
        'Responsabilidad civil de al menos 300.000 € y multirriesgo con incendio y avería del frío, que es el pescado de '
        'la cámara y del congelador. Dile a la aseguradora que sirves pescado crudo y que trabajas con freidora: cambia '
        'la prima y las condiciones',
        'R §3 [estimado]'),
    'pct_varios': (
        None, None, 0.02, None,
        'Colchón de gasto corriente no presupuestado (pequeñas reparaciones, utillaje que se rompe, pruebas de carta)',
        'molde (= Taquería)'),
    'recursos_propios': (
        None, None, 55000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'R §3 [estimado]'),
    'prestamo': (
        None, None, 128000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D9: cubre la necesidad de caja del libro con 55.000 € propios (R §3: unos 128.000 €)'),
    'tipo_prestamo': (
        None, None, 0.06, None,
        'Tipo nominal anual. Pide oferta a dos entidades y a una línea ICO antes de fijarlo; el frío y el equipo de '
        'cocina se pueden pagar con leasing o renting: compáralo',
        'R §3 (= Taquería) [estimado]'),
    'plazo_prestamo': (
        None, None, 7, None, 'Años totales, carencia incluida',
        'R §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: la obra de la barra, el conducto de extracción y la cocina antes de facturar. '
        'Desde el segundo año se devuelve el principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'R §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: el colchón para la rampa del arranque, que con el Mes 1 en enero va de enero a '
        'abril, y para agosto, el mes más flojo del año',
        'molde (mínimo de la familia) · R §3'),
    'vida_obra': (
        None, None, 10, None,
        'Obra y barra de sushi, conducto de extracción hasta cubierta, instalación eléctrica, fontanería, '
        'climatización, rótulo y fachada. Coeficientes de la tabla del art. 12.1 de la Ley del Impuesto sobre '
        'Sociedades: confírmalo con tu asesor',
        'R §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Vitrina de sushi, arroceras, congelador, cocina caliente, campana extractora, frío, lavavajillas, utillaje, '
        'mobiliario y TPV: un 10 % anual, dentro del coeficiente máximo de la tabla del art. 12.1 de la Ley del '
        'Impuesto sobre Sociedades para la maquinaria (12 %) y para el mobiliario (10 %). Confírmalo con tu asesor',
        'R §3 (= Taquería)'),
    'pct_bebida_alc': (
        None, 'Bebida que compras al 21 % (cerveza, sake, vino y refrescos con azúcares o edulcorantes añadidos) sobre '
              'el total de bebida', 0.75, None,
        'Sólo mueve el IVA que SOPORTAS al comprar la bebida: la cerveza, el sake, el vino y los refrescos con azúcares '
        'o edulcorantes añadidos te los facturan al 21 %; el agua, el té y lo que no lleve azúcares ni edulcorantes '
        'añadidos, al 10 %. Con un 75 % sale un 18,3 %. El IVA que REPERCUTES lo fija la línea de bebida del P&L '
        '(columna H)',
        'R §1 (IVA de compras) · LIVA art. 91 (BOE)'),
    'aforo': (
        None, 'Aforo del local (plazas sentadas, con la barra)', 36, None,
        'Plazas interiores: 8 taburetes en la barra de sushi y 28 en mesa. Quien se lleva el pedido o lo recibe en '
        'casa no ocupa mesa: por eso la rotación de la fila de arriba es más alta que la real de tu sala',
        'R §3 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'Los sushi bares van al convenio PROVINCIAL de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal '
        'para el sector de Hostelería no nombra el sushi bar, pero incluye los restaurantes y el reparto de comidas '
        'preparadas. Copia aquí el salario base del grupo más bajo de la tabla de TU provincia. Con 0 el semáforo '
        'compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.75, None,
        'Un sushi bar que abre trae curiosos el primer mes, pero la clientela fija y la nota en las plataformas tardan '
        'un trimestre: el Mes 1 (enero) factura un 75 % de lo que facturará a los cuatro meses. Con 100 % se elimina '
        'la rampa',
        'R §3 [estimado] (= Taquería)'),
    'meses_rampa': (
        None, None, 4, None,
        'Cuatro meses hasta el ritmo de crucero: de enero a abril',
        'R §3 [estimado]'),
    'meses_renta_previa': (
        None, None, 2, None,
        'Dos meses de renta antes de abrir: la obra de la barra, el conducto de extracción y la licencia. Si el banco '
        'te da el préstamo al empezar la obra, súmale los intereses de esos meses, que este libro no cuenta, y ten en '
        'cuenta que la carencia corre desde la firma',
        'R §3 [estimado]'),
    'pct_imprevistos': (
        None, None, 0.10, None,
        'Colchón sobre la obra y las instalaciones del local, que es donde aparecen las sorpresas (el conducto hasta '
        'cubierta, la potencia eléctrica de la cocina, el separador de grasas). Un banco no financia una reforma sin él',
        'R §3 (10 % sobre la obra) [estimado]'),
    'dias_cobro': (
        None, None, 2, None,
        'Media ponderada: la sala y lo que se recoge en el local cobran al momento y la plataforma liquida cada semana '
        'o cada quince días lo que vende por ella (un 25 % de las ventas). Con liquidación semanal salen unos 2 días',
        'R §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a los proveedores de pescado, arroz, algas y bebida: lo que te financian. Negócialo por escrito: '
        'si el proveedor de pescado te pide pago semanal, baja esta cifra',
        'molde (= Taquería)'),
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
        '91.Uno.2.2.º de la Ley 37/1992); para llevar o a domicilio, la cerveza, el sake, el vino y los refrescos con '
        'azúcares o edulcorantes añadidos, al 21 %, en la columna H de esa línea',
        'Ley 37/1992 art. 91.Uno.1.1.º y 2.2.º (BOE)'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente, tipo de IVA). Dos líneas: `mix_en_supuestos` (el peso se teclea en
#: Supuestos). La comida va al 10 % sin partir; la bebida, PARTIDA (sexto campo).
LINEAS_INGRESO = (
    ('Ventas de sushi y cocina (sala, para llevar y a domicilio)', 0.85, 'comida',
     'Sushi, sashimi y poke, gyozas, tempura, sopa de miso y postres: en sala unos 62 % de las ventas, para llevar unos '
     '12 % y por plataforma unos 26 %. Todo al 10 % de IVA, se coma en la barra o salga del local (art. 91.Uno.1.1.º y '
     '2.2.º de la Ley 37/1992)',
     'R §3 [estimado] · LIVA (BOE)'),
    ('Ventas de bebida (cerveza, sake, vino, refrescos, agua y té)', 0.15, 'bebida',
     'Bebida de sala y la que sale con los pedidos',
     'R §3 [estimado]',
     {'cabecera': 'Bebida para llevar o a domicilio al 21 % (%)',
      'pct': 0.07,
      'tipo': 0.21,
      'nota': 'La columna H es la parte de la bebida que sale del local y va al 21 %: la cerveza, el sake, el vino y '
              'los refrescos con azúcares o edulcorantes añadidos (art. 91.Uno.1.1.º a y b de la Ley 37/1992); el '
              'agua, el té y lo que no lleve azúcares ni edulcorantes añadidos, y toda la bebida en sala, al 10 %. Un '
              '7 % = un 1,05 % de las ventas'}),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada; todos por encima del SMI 2026 en proporción (1.221 € × jornada, RD 126/2026). Las 7
#: filas de R §3 (la de suplencias incluida, RC-19) = 5,35 jornadas, 8.578 € al mes.
PLANTILLA = (
    ('Titular — itamae y gerente: compra y corte del pescado, carta y gestión', 1, 2200,
     'El itamae (jefe de barra): compra, limpia y corta el pescado, lleva la barra en el servicio fuerte, firma la '
     'carta y el APPCC del anisakis y gestiona. Como administrador de la SL cotiza en el régimen de autónomos: el libro '
     'le imputa el 33 % de Seguridad Social sobre 14 pagas como si fuera nómina, que es el lado prudente. Confirma con '
     'tu gestoría la cuota real y si te aplica la reducida de inicio',
     'R §3 [estimado]', 1.0),
    ('Sushiman o sushiwoman: shari, rolls y combinados', 1, 1650,
     'El shari de cada tanda, los rolls, los combinados de las plataformas y la barra cuando el itamae no está. Es '
     'inversión, no gasto: si sólo el titular sabe cortar y montar, una baja cierra la barra',
     'R §3 y §6 [estimado]', 1.0),
    ('Cocinero/a de cocina caliente y arroz', 1, 1400,
     'Las arroceras, las gyozas, la tempura, la sopa de miso y el office',
     'R §3 [estimado]', 1.0),
    ('Encargado/a de sala y pedidos', 1, 1500,
     'Todo el año: sala, caja, los pedidos para llevar, las tablets de las plataformas y la información de alérgenos',
     'R §3 [estimado]', 1.0),
    ('Camarero/a de cenas y fines de semana', 1, 1013,
     '30 horas a la semana: las cenas y el fin de semana, cuando la sala se llena',
     'R §3 [estimado]', 0.75),
    ('Refuerzo de viernes a domingo: sala y empaquetado de pedidos', 1, 675,
     'Sala y empaquetado de los pedidos de las noches fuertes. Este plan NO tiene reparto propio: si lo pones, el '
     'repartidor va con contrato laboral del convenio de hostelería, nunca como autónomo',
     'R §3 [estimado] · ALEH VI art. 4 · ET DA 23.ª', 0.50),
    # RC-19: la fila de suplencias que trae el molde (7 filas)
    ('Suplencias de vacaciones y descansos', 1, 140,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso semanal del equipo de todo el año',
     'molde (RC-19, = Taquería)', 0.10),
)

#: Cobertura: sala, barra y cocina (horas × personas a la vez) + producción ANTES de abrir, por los días de apertura.
COBERTURA = {
    'horas_dia': 6.5,
    'personas_franja': 3.5,
    'horas_produccion': 3.0,
    'personas_produccion': 2.0,
    'nota_horas': 'Horas con el local abierto al público, sumando las comidas (13:00-16:00) y las cenas (20:00-23:30). '
                  'La tarde de cierre entre los dos servicios no se cuenta',
    'nota_personas': 'Presencia media a la vez entre la barra, la cocina caliente, la sala y los pedidos. El viernes y '
                     'el sábado por la noche hacen falta seis (dos en la barra, uno en caliente, dos en sala y uno '
                     'empaquetando): entran el refuerzo y el camarero de cenas (el cuadrante anual no lo ve: ponlo en '
                     'el turno)',
    'nota_horas_produccion': 'El shari del día, el corte y la limpieza del pescado, las salsas y la mise en place '
                             'antes de abrir',
    'nota_personas_produccion': 'El itamae con el sushiman o el cocinero. El cierre, la limpieza y las compras quedan '
                                'fuera de este cuadrante: son el margen entre las horas contratadas y las necesarias',
}

#: Rotación ENCENDIDA: techo 3 (comida, cena y segundo turno de cena el viernes y el sábado) y la referencia de que el
#: domicilio no ocupa mesa (< 255 car.). Caso 79 / 36 = 2,2.
ROTACION = {
    'max': 3.0,
    'nota_max': 'Servicios completos por plaza y día que puedes hacer con comidas, cenas y un segundo turno de cena el '
                'viernes y el sábado (estancias de 45-60 minutos). Es el techo físico del local, no un objetivo',
    'referencia': 'Incluye los pedidos para llevar y a domicilio (1 pedido = 1,6 comensales), que no ocupan mesa: la '
                  'rotación real de tu sala ronda 1,25 por plaza y día.',
}

#: Partidas de la hoja de inversión: las escribe `semilla_sus.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-24
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
    'maquinaria': (r'vitrina|arrocera|hangiri|congelador|arc[oó]n|inducci[oó]n|ph-metro|plancha|freidora|'
                   r'campana|armarios?|frío|frio|lavavajillas|fregadero|utillaje|menaje|barra|mobiliario|tpv|'
                   r'dat[aá]fono',),
}

#: Costes fijos. Las 9 partidas propias (13.850 €/año) las escribe `semilla_sus.py` en las filas 26-34 (rótulo e
#: importe); aquí, la nota por rótulo normalizado (minúsculas y sin tildes) y la de la fila canónica del alquiler.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Los dos meses de renta '
              'previos a la apertura están en la hoja de Inversión y NO se cuentan dos veces'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL, nóminas y contratos de la plantilla'),
    'mantenimiento del frio, el congelador, la campana extractora y el ph-metro': (
        None, 'El frigorista para la cámara, los armarios y el congelador, que tiene que llegar a −20 °C en el centro '
              'del pescado (anisakis); la limpieza de la campana extractora y del conducto al menos una vez al año '
              '(Madrid lo exige en su Ordenanza 4/2021, art. 23; mira la de tu ayuntamiento) y las soluciones de '
              'calibración del pH-metro'),
    'marketing y publicidad': (
        None, 'Ficha de Google Business, redes sociales, fotos, las promociones de las plataformas y las fechas fuertes '
              '(San Valentín, Nochebuena y Nochevieja); la campaña de apertura va en la inversión'),
    'software, tpv, telefono e internet': (
        None, 'Cuota del TPV con Veri*factu, las tablets de las plataformas, teléfono e internet'),
    'limpieza, lavanderia, epi y analisis de autocontrol': (
        None, 'Productos de limpieza, lavado de uniformes y paños, guantes y los análisis de autocontrol que fije tu '
              'APPCC'),
    'gestion de residuos y del aceite usado de la freidora': (
        None, 'La tasa de basuras, el cartón de las cajas y el aceite usado de la freidora de tempura con gestor '
              'autorizado. Pon las de tu ayuntamiento'),
    'desinsectacion, desratizacion y desinfeccion (ddd)': (
        None, 'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
    'derechos de autor por musica ambiental (sgae y agedi-aie)': (
        None, 'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los metros y del aforo de tu sala'),
    'prevencion de riesgos laborales, vigilancia de la salud y formacion': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): cortes con los cuchillos de la barra, quemaduras de '
              'la freidora y la plancha, el frío del congelador y las cargas; los reconocimientos médicos de la '
              'plantilla y la formación en higiene del pescado crudo y en alérgenos'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Margen bruto al 52 %: el caso da un 57,8 % tras TODOS los costes variables (la
#: plataforma pesa un 25 % de las ventas).
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.52,
     'Suelo del margen tras TODOS los costes variables (mercancía, envases, plataforma, medios de pago y varios). Con '
     'un cuarto de las ventas por plataforma, un sushi bar deja menos que una sala sola. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.31,
     'Techo de la materia prima sobre ventas: el salmón paga la carta y el atún, el langostino y la merma de la vitrina '
     'la encarecen. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'Techo del personal sobre ventas con itamae, sushiman y una sala de dos servicios. Estimación del kit'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del alquiler sobre ventas para un local con salida de humos a cubierta: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga. Un sushi bar bien llevado deja en torno a un '
     '8-9 %. Estimación del kit'),
)

#: (comensales al día, € por comensal sin IVA, días de apertura). R §3.
ESCENARIOS = {
    'pesimista': (68, 19.00, 295),     # menos comensales, ticket más bajo y una semana más de cierre
    'optimista': (90, 21.00, 305),
}

#: Mes 1 = ENERO, sin girar: el calendario de R §3 tal cual (agosto el valle por el cierre de 10 días, febrero sube
#: con San Valentín, diciembre pico con las bandejas de Nochebuena y Nochevieja).
ESTACIONALIDAD = (0.082, 0.086, 0.086, 0.084, 0.086, 0.084,
                  0.080, 0.066, 0.082, 0.086, 0.086, 0.092)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es ENERO, en el orden del calendario: la rampa del arranque va de enero a abril y agosto, '
        'con el cierre de vacaciones, es el mes más flojo; por eso el fondo de maniobra cuenta. Si abres en otro mes, '
        'gira la fila de estacionalidad. El saldo mínimo del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El plan de negocio en Word de este pack cita las cifras de este Excel: si cambias una celda verde, el Excel '
        'manda. La calculadora del pescado, el arroz y el escandallo del pack va aparte: mide el rendimiento del '
        'salmón, el shari que sale de cada kilo de arroz y ESCANDALLA cada pieza en cada canal. No copies el food cost '
        'de un nigiri en la hoja de Supuestos: la celda «Coste de mercancía sobre las ventas de COMIDA» es la media '
        'ponderada de TODA la carta más la merma de pescado, el shari tirado y las comidas del personal, y por eso sale '
        'más alta que el escandallo teórico. Con los escandallos de tu carta, comprueba que esa media cuadra.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Enero', 'Decisión del plan',
         'En el orden del calendario: la rampa cae sobre enero-abril y agosto, con el cierre de vacaciones, es el mes '
         'más flojo. Si abres en otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Sushi en el reparto a domicilio', 'El maki, segundo plato más pedido',
         'Gastrómetro de Just Eat 2025, publicado en prensa en diciembre de 2025',
         'Sólo lo supera la hamburguesa. Por eso el caso cuenta un 25 % de las ventas por plataforma'),
        ('Nigiri y combinado en carta', '2,50-2,60 € la pieza de nigiri · 24,90-30,60 € el combinado de 24 piezas',
         'Cartas de cadenas y restaurantes de sushi leídas en octubre de 2026',
         'El caso: nigiri de salmón a 2,60 € la pieza (5,20 € las dos), combinado de 24 piezas a 29,00 € y menú del día '
         'de mediodía a 14,90 €, todo con IVA'),
        ('Coste del nigiri de salmón', 'Un 11 % de su precio sin IVA',
         'Estimación del kit con los gramajes de la calculadora del pack (editables)',
         '15 g de neta de salmón entero de acuicultura a 9,50 €/kg con un 55 % de lomo y un 15 % de recorte '
         'reaprovechado, y 20 g de shari. El 29 % del plan es el consumo real de TODA la carta, con la merma'),
        ('Rendimiento del salmón entero', 'Un 50-60 % de lomo limpio',
         'Guías de gestión de restaurantes (fuente secundaria)',
         'Mide el tuyo con 3 salmones y llévalo a la hoja «Pescado» de la calculadora del pack'),
        ('Arroz para sushi', '1,81-1,85 € el kg sin IVA', 'Catálogo de Makro, sacos de 5 kg, octubre de 2026',
         'Un kilo de arroz crudo da unos 2,4 kg de shari, unos 120 nigiris con 20 g (calculadora del pack). El arroz '
         'es barato: el coste está en el pescado y en la mano del itamae'),
        ('Comisión de la plataforma con su reparto', '13-35 % más IVA',
         'Guías del sector, 2025-2026: compruébalo en tu contrato',
         'El plan básico de Uber Eats ronda el 30 %. Lo que se recoge en el local no paga comisión'),
        ('IVA del sushi', '10 % en la venta · 4 % el arroz en la compra',
         'Ley 37/1992, art. 91.Uno.1.1.º, 91.Uno.2.2.º y 91.Dos.1.1.º',
         'La comida, al 10 % en sala, para llevar y a domicilio. La cerveza, el sake, el vino y los refrescos con '
         'azúcares o edulcorantes añadidos que salen del local, al 21 %. El arroz, la verdura, el huevo y el queso se '
         'compran al 4 %'),
        ('Pescado para consumir crudo (anisakis)', '−20 °C 24 h o −35 °C 15 h en la totalidad del producto',
         'Real Decreto 1021/2022, art. 8',
         'O que llegue tratado de una etapa anterior con su documento, o de acuicultura libre de anisakis acreditada por '
         'escrito. Y hay que informar al cliente en la carta o en un cartel (art. 8.2)'),
        ('Shari a temperatura ambiente', 'Sólo con una temperatura validada ante sanidad',
         'Real Decreto 1086/2020, art. 30.5',
         'La comida preparada se refrigera, se mantiene a 63 °C o más o se sirve cuanto antes (RD 1086/2020, art. 30.2). '
         'El shari a '
         'temperatura ambiente sólo si tu APPCC lo justifica con evidencia científica y lo comunicas a sanidad: pH de '
         'cada tanda y tiempo máximo. Si no, refrigerado'),
        ('Salario mínimo interprofesional 2026', '1.221 € al mes en 14 pagas', 'Real Decreto 126/2026',
         'A prorrata en jornada parcial'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'No nombra el sushi bar: entra como restaurante. Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_sus.py` entero (`datos_checklist.py`): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO de la compra de COMIDA (R §1): pescado, marisco, algas, salsas, surimi y gyozas al 10 % (≈ 79 % de la
#: compra de comida); arroz, verdura, aguacate, fruta, huevo y queso crema al 4 % (≈ 21 %) → 0,79 × 10 + 0,21 × 4 =
#: 8,7 %. La bebida tiene su propio tipo de compra (`pct_bebida_alc`, 18,25 %): no se mezcla aquí.
IVA_COMPRAS = {
    'comida': 0.087,
    'nota': 'Pescado, marisco, algas, salsas y surimi al 10 %; arroz, verdura, aguacate, huevo y queso al 4 % (art. '
            '91.Dos.1.1.º de la Ley 37/1992). Ajústalo a tus facturas',
}
