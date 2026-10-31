#!/usr/bin/env python3
"""
Contenido de `plan-negocio-hamburgueseria` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Semilla = el Sushi Bar ES 1.0 publicado:
`plan-hamburgueseria/semilla_ham.py` copia sus dos xlsx (plan + checklist, solo lectura), les pone las 18 partidas, los 9
fijos, los títulos y el checklist de la hamburguesería (las pagas 7/12 ya vienen del Sushi Bar), y `main.py` +
`grupo_a.py` los reconstruyen con este módulo (mecánica del Sushi Bar: dos servicios, producción antes de abrir,
ROTACIÓN ENCENDIDA, bebida con línea partida). Cómo y por qué: `plan-hamburgueseria/F1-camino.md` §1-§3 (la §2 hace de
SPEC); caso y fuentes: `plan-hamburgueseria/F1-research-hamburgueseria.md` §1-§3 (R §n).

MOTOR DE INGRESOS (hamburguesería de smash burgers fast casual: sala, para llevar y a domicilio)
-------------------------------------------------------------------------------------------------
    cubiertos_dia (B4) = COMENSALES EQUIVALENTES AL DÍA (53 de sala + 42 de llevar y domicilio)   95
    ticket_medio  (B5) = € POR COMENSAL SIN IVA                                                 16,00 €
    dias_apertura (B6) = DÍAS DE APERTURA AL AÑO                                                300
Un pedido para llevar o de plataforma = 1,7 comensales equivalentes (R §3). Canales (F1-camino §2, rehechos para la demo
§2.11.9): sala 52,7 comensales × 15,45 € · para llevar 12,9 pedidos × 26,45 € sin IVA (29,10 € con IVA) · plataforma
12,0 pedidos × 30,42 € sin IVA (33,47 € con IVA: la carta, un 15 % más cara) → 95,0 comensales y 1.521 €/día = 16,00 €;
sala 54 %, para llevar 22 %, plataforma 24 %. Ventas a régimen = 95 × 16,00 × 300 = 456.000 €. Mes 1 = ENERO, sin girar:
la estacionalidad va en el orden del calendario y las pagas extra salen en los meses 7 (julio) y 12 (diciembre).

IVA: la comida al 10 % (sala, llevar y domicilio, sin partir); la bebida con la LÍNEA PARTIDA del motor: su columna H
(«Bebida para llevar o a domicilio al 21 %») declara la parte que sale del local al tipo general (cerveza y refrescos con
azúcares o edulcorantes añadidos, también los zero, LIVA 91.Uno.1.1.º a y b), H = 28 % (= 4,5 % de las ventas, R §3); el
resto, al 10 %. Con la línea partida, `iva_bebida` (B63) no tiene efecto y `pct_bebida_alc` (B62) sólo mueve el IVA
SOPORTADO de la compra de bebida (75 % al 21 %). `IVA_COMPRAS` es SOLO la compra de COMIDA (9,0 %: el queso, el huevo,
la patata fresca, la verdura y la leche al 4 %; el pan de hamburguesa, que no es «pan común», y el aceite de girasol, al
10 %: LIVA 91.Dos.1.1.º a, d-g, R §1).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «R §n» = `F1-research-hamburgueseria.md` §n (casi todo
[criterio del plan], con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado F1» = ajustado en la
F1 con la fórmula de la necesidad de caja (F1-camino §1(b)) y confirmado en la F2 con RD-34.

⚠️ Rótulos de importe: sin «comensales», «personas», «días», «meses», «años», «plazas» ni «unidades»
(`motor.RX_RECUENTO_DV` les quita el formato de euro). «Campana» siempre «campana extractora» (`motor.TILDES` la
acentúa a «campaña») y nunca el verbo «publica» (lo acentúa a «pública»). Las notas no usan «cubierto» (el VOCABULARIO
lo traduce) ni restos de los moldes (sushi, taco, pollo asado, pizza…: `barrido_es.py`). Sesión Claude Code,
31-oct-2026.
"""

CONCEPTO = 'Hamburguesería Smash'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Masculino «comensal» = masculino
#: «cubierto»: sin arreglos de concordancia. Las 9 frases del motor = las del Sushi Bar (F1-camino §2), con la compra
#: al 21 % de la hamburguesería (la cerveza y los refrescos con azúcares o edulcorantes añadidos, también los zero) y
#: «las hamburguesas y las patatas incluidas». La última traduce la nota `O5` de la Tesorería al calendario de la
#: hamburguesería (Mes 1 = enero). `VOCABULARIO_SIN_TILDES` (= Sushi Bar): sin él, las claves con tilde no casan.
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
        '21 %» de esta hoja: la cerveza y los refrescos con azúcares o edulcorantes añadidos (también los zero), cuya '
        'factura va al 21',
    # Tesorería (nota de la fila del IVA repercutido): el motor cierra el paréntesis.
    'el alcohol que sale por delivery, al general; el pan común y las harinas panificables, al superreducido (art. '
    '91.Dos.1.1.º':
        'la parte de la bebida que sale para llevar o a domicilio y declara la columna H de su línea (cerveza y '
        'refrescos con azúcares o edulcorantes añadidos, también los zero), al general (art. 91.Uno.1.1.º a y b); la '
        'comida, también la que sale para llevar o a domicilio, al reducido (art. 91.Uno.1.1.º y 2.2.º',
    'los alimentos —bollería y pastelería incluidas—, que son':
        'los alimentos —las hamburguesas y las patatas incluidas—, que son',
    # Instrucciones!A8 (frase del motor; LIVA art. 91.Uno.1.1.º b): «azúcares o edulcorantes añadidos»
    'el alcohol y los refrescos o zumos con azúcares añadidos para llevar':
        'el alcohol y los refrescos o los zumos con azúcares o edulcorantes añadidos para llevar',
    # resto del molde en Tesorería!D31 (barrido_es.py: «versión 1.1»)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # Tesorería!O5 (nota del motor de la fila de estacionalidad). Picos que casan con la tupla (m7): enero 0,072 (el
    # mínimo), agosto 0,076, mayo 0,089 (el máximo) y junio 0,088.
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = ENERO, en el orden del calendario: enero es el mes más flojo (cierre de 10 días y cuesta de enero) y '
        'agosto baja con la ciudad vacía; mayo y junio son los picos (buen tiempo y fin de curso). En la costa, julio y '
        'agosto suben. Si abres en otro mes, gira la fila',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 95, None,
        'Comensales equivalentes al día, media del año: unos 53 en sala (mesas y barra de ventana) y unos 42 de para '
        'llevar y domicilio, que son los pedidos (unos 13 para recoger y 12 de plataforma al día) contando cada pedido '
        'como 1,7 comensales. Un sábado, unos 138 con los pedidos; un martes, unos 61. Contrástalo con el paso de gente '
        'de tu calle un viernes por la noche y un martes a mediodía',
        'R §3 [criterio del plan] · F1-camino §2 (reparto de canales)'),
    'ticket_medio': (
        None, None, 16.00, None,
        'SIN IVA, por comensal: en sala, la hamburguesa con patatas, bebida y algún extra, con el descuento del menú, '
        'deja unos 17,00 € con IVA (15,45 € sin IVA); el pedido para llevar (de media 29,10 € con IVA: casi dos menús) '
        'sale a 15,56 € por comensal equivalente y el de plataforma, con la carta un 15 % más cara (33,47 € con IVA), a '
        '17,90 €. La media de los tres canales da 16,00 €. El precio con IVA está en la fila «PVP equivalente con IVA» '
        'de abajo',
        'R §2-§3 (carta del caso) [criterio del plan] · F1-camino §2'),
    'dias_apertura': (
        None, None, 300, None,
        '365 días menos los 52 lunes de cierre, 10 días de cierre en la segunda quincena de enero y 3 festivos sueltos '
        '(Navidad, Año Nuevo y Reyes). El año de la apertura, la rampa del arranque absorbe ese enero. Es el MISMO dato '
        'para la cuenta de resultados, el punto de equilibrio, los escenarios y las horas de personal',
        'R §3 [criterio del plan]'),
    'crec_a2': (
        None, None, 0.06, None,
        'Clientela que repite y más pedidos para recoger el segundo año. Se aplica a los comensales con el mismo '
        'ticket; el personal NO sube con este porcentaje: sale de la hoja Personal',
        'R §3 [criterio del plan] (= Sushi Bar)'),
    'crec_a3': (
        None, None, 0.04, None,
        'Sobre el año 2. Conservador: el techo lo ponen la plancha, las 36 plazas los viernes y los sábados por la '
        'noche y los pedidos que caben en una hora punta',
        'R §3 [criterio del plan]'),
    'pct_comida': (
        None, None, 0.84, None,
        'Hamburguesas, patatas, entrantes y postres, en sala, para llevar y a domicilio, sobre las ventas; el 16 % '
        'restante es la bebida (un 19 % de lo que se vende en sala y un 12 % de lo que sale del local). Es el peso de '
        'la primera línea de ventas del P&L',
        'R §3 [criterio del plan] (84/16)'),
    'coste_comida': (
        None, None, 0.28, None,
        'Materia prima de la comida sobre sus ventas: un 28 %, el lado prudente. El escandallo teórico de la '
        'calculadora del pack sale en un 24 % de media ponderada (la smash doble con queso, en un 27 %; la ración de '
        'patatas congeladas, en un 8 %), pero la cuenta real es lo que compras frente a lo que vendes: las bolas, el pan '
        'y las salsas que se tiran al cierre suman un punto y medio; las comidas del personal, las invitaciones, los '
        'errores y las reclamaciones de la plataforma, otro punto y medio, y las promociones de la plataforma (el dos '
        'por uno, la primera compra), un punto más. La carne es un precio estimado por el kit. Mide tu consumo el primer '
        'trimestre y cambia esta celda: cada punto vale unos 3.800 € al año',
        'R §2-§3 [criterio del plan] · calculadora (FC_PONDERADO, FC_DOBLE, FC de la patata congelada)'),
    'coste_bebida': (
        None, None, 0.25, None,
        'La lata de refresco ronda un 19 % de su precio de venta, el tercio de cerveza un 22 % y el batido un 18 %, '
        'pero en el menú la bebida se vende con descuento y la cerveza de tirador tiene merma: el caso cuenta un 25 %. '
        'Pide por escrito las condiciones de la cervecera (si te cede el tirador, el volumen mínimo y los descuentos)',
        'R §3 [criterio del plan]'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Cajas de hamburguesa, cucuruchos de patatas, tarrinas de salsa, bolsas, precinto, papel, servilletas y '
        'guantes (unos 1,10 € por pedido que sale del local y 0,20 € por comensal de sala) y los envases para que el '
        'cliente se lleve lo que no consuma (Ley 1/2025, art. 8). El envase de plástico de un solo uso se cobra aparte '
        'en el tique (Ley 7/2022, art. 55)',
        'R §1-§3 [criterio del plan] · BOE'),
    'pct_delivery': (
        None, None, 0.24, None,
        'Ventas por PLATAFORMA con su reparto (Glovo, Just Eat, Uber Eats) sobre el total: unos 12 pedidos al día. Lo '
        'que se recoge en el local (unos 13 pedidos al día, por la web o por teléfono) NO paga comisión y no va aquí: '
        'empújalo. La hamburguesa viaja bien; las patatas, peor (cucurucho ventilado y fritas al final). Si la '
        'plataforma llegara a un tercio de las ventas, pagarías unos 12.000 € más de comisión al año',
        'R §3 [criterio del plan] · F1-camino §2 (0,24 < 0,25 de la demo §2.11.9)'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión de la plataforma con su reparto sobre lo que vende ese canal: el plan básico de Uber Eats ronda el '
        '30 % más IVA, Glovo va del 15 al 35 % según la zona y Just Eat, del 13 al 35 %. Compruébala en tu contrato. '
        'Si repartes tú, pon 0 y suma el repartidor, con contrato laboral, a la hoja Personal',
        'R §2 (guías del sector) [estimado]'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado',
        'molde (= Sushi Bar)'),
    'alquiler_mes': (
        None, None, 1500, None,
        'Local de 90 m² que ya fue de restauración, con salida de humos a cubierta posible: cocina a la vista con la '
        'plancha y dos freidoras, mostrador de pedidos con pantalla de turnos, sala de 30 plazas y 6 taburetes en una '
        'barra de ventana, y una zona de empaquetado y de recogida de los repartidores junto a la puerta, en un barrio '
        'con vida de noche o una zona universitaria de una ciudad de 150.000 a 500.000 habitantes, sin traspaso: unos '
        '16,7 € el m². El peso sobre las ventas lo calcula el propio libro en la fila «Alquiler / Ventas» del P&L',
        'R §2-§3 [criterio del plan]'),
    'fianza_meses': (
        None, None, 2, None,
        'Dos meses de renta, lo habitual en un contrato de local de negocio: compruébalo con tu abogado',
        'R §3 [estimado]'),
    'suministros_mes': (
        None, None, 1100, None,
        'Gas de la plancha, luz de las freidoras eléctricas, de la extracción (potente: la plancha y las freidoras echan '
        'mucha grasa), del frío y de la climatización, y agua. Pide el histórico del local',
        'R §3 (1.150 €) [criterio del plan] · calibrado F2: 1.100 € (= Sushi Bar) para que la demo §2.11.5 encuentre su '
        'escenario (con 1.150 €, a 74 comensales la suma del RAI de los 3 años salía en −80 €: F2-NOTAS §2)'),
    'seguros_ano': (
        None, None, 1500, None,
        'Responsabilidad civil de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la '
        'aseguradora que trabajas con una plancha de gas y dos freidoras: cambia la prima y las condiciones',
        'R §3 [criterio del plan]'),
    'pct_varios': (
        None, None, 0.02, None,
        'Colchón de gasto corriente no presupuestado (pequeñas reparaciones, utillaje que se rompe, pruebas de carta)',
        'molde (= Sushi Bar)'),
    'recursos_propios': (
        None, None, 55000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'R §3 [criterio del plan]'),
    'prestamo': (
        None, None, 130000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado F1, §1(b): cubre la necesidad de caja del libro con 55.000 € propios (R §3: unos 127.000 €); la F2 '
        'lo confirma con RD-34'),
    'tipo_prestamo': (
        None, None, 0.06, None,
        'Tipo nominal anual. Pide oferta a dos entidades y a una línea ICO antes de fijarlo; la plancha, las freidoras '
        'y el frío se pueden pagar con leasing o renting: compáralo',
        'R §3 (= Sushi Bar) [estimado]'),
    'plazo_prestamo': (
        None, None, 7, None, 'Años totales, carencia incluida',
        'R §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: la obra, el conducto de extracción y la cocina antes de facturar. Desde el '
        'segundo año se devuelve el principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'R §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: el colchón para la rampa del arranque, que con el Mes 1 en enero va de enero a '
        'abril, y para agosto, cuando la ciudad se vacía',
        'molde (mínimo de la familia) · R §3'),
    'vida_obra': (
        None, None, 10, None,
        'Obra con el mostrador y la cocina a la vista, conducto de extracción hasta cubierta, instalación eléctrica y '
        'de gas, fontanería, climatización, rótulo y fachada. Coeficientes de la tabla del art. 12.1 de la Ley del '
        'Impuesto sobre Sociedades: confírmalo con tu asesor',
        'R §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Plancha, freidoras, campana extractora, mesa refrigerada, frío, barra de bebidas, lavavajillas, utillaje, '
        'mobiliario y TPV: un 10 % anual, dentro del coeficiente máximo de la tabla del art. 12.1 de la Ley del '
        'Impuesto sobre Sociedades para la maquinaria (12 %) y para el mobiliario (10 %). Confírmalo con tu asesor',
        'R §3 (= Sushi Bar)'),
    'pct_bebida_alc': (
        None, 'Bebida que compras al 21 % (cerveza y refrescos con azúcares o edulcorantes añadidos) sobre el total de '
              'bebida', 0.75, None,
        'Sólo mueve el IVA que SOPORTAS al comprar la bebida: la cerveza y los refrescos con azúcares o edulcorantes '
        'añadidos (también los zero) te los facturan al 21 %; el agua, la leche y el helado de los batidos, al 10 % o '
        'al 4 %. El IVA que REPERCUTES lo fija la línea de bebida del P&L (columna H)',
        'R §1 (IVA de compras) · LIVA art. 91 (BOE)'),
    'aforo': (
        None, 'Aforo del local (plazas sentadas, con la barra de ventana)', 36, None,
        'Plazas interiores: 30 en mesa y 6 taburetes en la barra de ventana. Quien se lleva el pedido o lo recibe en '
        'casa no ocupa mesa: por eso la rotación de la fila de arriba es más alta que la real de tu sala',
        'R §3 [criterio del plan]'),
    'salario_convenio': (
        None, None, 0, None,
        'Las hamburgueserías van al convenio PROVINCIAL de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito '
        'Estatal para el sector de Hostelería las nombra expresamente. Copia aquí el salario base del grupo más bajo de '
        'la tabla de TU provincia. Con 0 el semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.75, None,
        'Una hamburguesería que abre trae curiosos el primer mes, pero la clientela fija y la nota en las plataformas '
        'tardan un trimestre: el Mes 1 (enero) factura un 75 % de lo que facturará a los cuatro meses. Con 100 % se '
        'elimina la rampa',
        'R §3 [criterio del plan] (= Sushi Bar)'),
    'meses_rampa': (
        None, None, 4, None,
        'Cuatro meses hasta el ritmo de crucero: de enero a abril',
        'R §3 [criterio del plan]'),
    'meses_renta_previa': (
        None, None, 2, None,
        'Dos meses de renta antes de abrir: la obra, el conducto de extracción, la instalación de gas y la licencia. Si '
        'el banco te da el préstamo al empezar la obra, súmale los intereses de esos meses, que este libro no cuenta, y '
        'ten en cuenta que la carencia corre desde la firma',
        'R §3 [criterio del plan]'),
    'pct_imprevistos': (
        None, None, 0.10, None,
        'Colchón sobre la obra y las instalaciones del local, que es donde aparecen las sorpresas (el conducto hasta '
        'cubierta, la potencia de las freidoras, la acometida de gas, el separador de grasas). Un banco no financia una '
        'reforma sin él',
        'R §3 (10 % sobre la obra) [criterio del plan]'),
    'dias_cobro': (
        None, None, 2, None,
        'Media ponderada: la sala y lo que se recoge en el local cobran al momento y la plataforma liquida cada semana '
        'o cada quince días lo que vende por ella (un 24 % de las ventas). Con liquidación semanal salen unos 2 días',
        'R §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a los proveedores de carne, pan, patatas y bebida: lo que te financian. Negócialo por escrito: '
        'si el proveedor de carne te pide pago semanal, baja esta cifra',
        'molde (= Sushi Bar)'),
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
        '91.Uno.2.2.º de la Ley 37/1992); para llevar o a domicilio, la cerveza y los refrescos con azúcares o '
        'edulcorantes añadidos (también los zero), al 21 %, en la columna H de esa línea',
        'Ley 37/1992 art. 91.Uno.1.1.º y 2.2.º (BOE)'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente, tipo de IVA). Dos líneas: `mix_en_supuestos` (el peso se teclea en
#: Supuestos). La comida va al 10 % sin partir; la bebida, PARTIDA (sexto campo).
LINEAS_INGRESO = (
    ('Ventas de hamburguesas y cocina (sala, para llevar y a domicilio)', 0.84, 'comida',
     'Hamburguesas, patatas, entrantes y postres: en sala, alrededor del 54 % de las ventas; para llevar, del 22 %, y '
     'por plataforma, del 24 %. Todo al 10 % de IVA, se coma en el local o salga de él (art. 91.Uno.1.1.º y 2.2.º de la '
     'Ley 37/1992)',
     'R §3 [criterio del plan] · F1-camino §2 · LIVA (BOE)'),
    ('Ventas de bebida (refrescos, cerveza, batidos y agua)', 0.16, 'bebida',
     'Bebida de sala y la que sale con los pedidos',
     'R §3 [criterio del plan]',
     {'cabecera': 'Bebida para llevar o a domicilio al 21 % (%)',
      'pct': 0.28,
      'tipo': 0.21,
      'nota': 'La columna H es la parte de la bebida que sale del local y va al 21 %: la cerveza y los refrescos con '
              'azúcares o edulcorantes añadidos, también los zero (art. 91.Uno.1.1.º a y b de la Ley 37/1992); el '
              'agua, el batido de leche (confírmalo con tu gestoría) y toda la bebida en sala, al 10 %. Un 28 % = un '
              '4,5 % de las ventas. El menú para llevar se desglosa: cada parte, a su tipo'}),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada; todos por encima del SMI 2026 en proporción (1.221 € × jornada, RD 126/2026). Las 7
#: filas de R §3 (la de suplencias incluida, RC-19) = 5,35 jornadas, 8.178 € al mes.
PLANTILLA = (
    ('Titular — gerente y jefe/a de plancha: compra de la carne, carta y gestión', 1, 2000,
     'El jefe de plancha y gerente: compra la carne y elige el blend (la mezcla de cortes) y los proveedores, firma la '
     'carta y el APPCC, lleva la plancha en el servicio fuerte, las plataformas y la gestión. Como administrador de la '
     'SL cotiza en el régimen de autónomos: el libro le imputa el 33 % de Seguridad Social sobre 14 pagas como si fuera '
     'nómina, que es el lado prudente. Confirma con tu gestoría la cuota real y si te aplica la reducida de inicio',
     'R §3 [criterio del plan]', 1.0),
    ('Cocinero/a de plancha: smash, costra y tiempos', 1, 1500,
     'La plancha en los dos servicios: aplasta cada bola, saca la costra y lleva los tiempos de la comanda. Es '
     'inversión, no gasto: si sólo el titular sabe llevar la plancha, una baja la cierra',
     'R §3 [criterio del plan]', 1.0),
    ('Cocinero/a de montaje y freidora', 1, 1400,
     'La línea de montaje, las patatas, las salsas, el porcionado de las bolas y la mise en place',
     'R §3 [criterio del plan]', 1.0),
    ('Encargado/a de mostrador y pedidos', 1, 1450,
     'Todo el año: caja, pantalla de turnos, los pedidos para recoger, las tablets de las plataformas, el empaquetado '
     'y la información de alérgenos',
     'R §3 [criterio del plan]', 1.0),
    ('Auxiliar de sala y empaquetado', 1, 1013,
     '30 horas a la semana: lleva las bandejas a la mesa, recoge, friega y ayuda a empaquetar en las horas fuertes',
     'R §3 [criterio del plan]', 0.75),
    ('Refuerzo de viernes a domingo: segunda plancha y empaquetado', 1, 675,
     'Segunda plancha y empaquetado de las noches fuertes. Este plan NO tiene reparto propio: si lo pones, el '
     'repartidor va con contrato laboral del convenio de hostelería, nunca como autónomo',
     'R §3 [criterio del plan] · ALEH VI art. 4 · ET DA 23.ª', 0.50),
    # RC-19: la fila de suplencias que trae el molde (7 filas)
    ('Suplencias de vacaciones y descansos', 1, 140,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso semanal del equipo de todo el año',
     'molde (RC-19, = Sushi Bar)', 0.10),
)

#: Cobertura: plancha, montaje, mostrador y sala (horas × personas a la vez) + producción ANTES de abrir, por los días
#: de apertura. 7,5 × 3,5 + 2,5 × 1,5 = 30,0 h al día × 300 = 9.000 h frente a 5,35 × 40 × 46 = 9.844 h (≈ 109 %).
COBERTURA = {
    'horas_dia': 7.5,
    'personas_franja': 3.5,
    'horas_produccion': 2.5,
    'personas_produccion': 1.5,
    'nota_horas': 'Horas con el local abierto al público, sumando las comidas (13:00-16:30) y las cenas (20:00-24:00). '
                  'La tarde de cierre entre los dos servicios no se cuenta',
    'nota_personas': 'Presencia media a la vez entre la plancha, el montaje y la freidora, el mostrador y la sala. El '
                     'viernes y el sábado por la noche hacen falta seis (dos en la plancha, uno en montaje y freidora, '
                     'uno en el mostrador, uno empaquetando y uno llevando bandejas): entran el refuerzo y el auxiliar '
                     '(el cuadrante anual no lo ve: ponlo en el turno)',
    'nota_horas_produccion': 'El porcionado de las bolas, las salsas, la verdura cortada y reponer la línea antes de '
                             'abrir',
    'nota_personas_produccion': 'El cocinero de montaje con el de plancha o el titular. El cierre, la limpieza de la '
                                'plancha y de las freidoras y las compras quedan fuera de este cuadrante: son el margen '
                                'entre las horas contratadas y las necesarias',
}

#: Rotación ENCENDIDA: techo 3,5 (comida y cena con pedido en el mostrador y estancias de 30-40 min) y la referencia de
#: que el domicilio no ocupa mesa (< 255 car.). Caso 95 / 36 = 2,64; equilibrio de caja ≈ 2,0.
ROTACION = {
    'max': 3.5,
    'nota_max': 'Servicios completos por plaza y día que puedes hacer con comidas y cenas, pedido en el mostrador y '
                'estancias de 30-40 minutos. Es el techo físico del local, no un objetivo',
    'referencia': 'Incluye los pedidos para llevar y a domicilio (1 pedido = 1,7 comensales), que no ocupan mesa: la '
                  'rotación real de tu sala ronda 1,5 por plaza y día.',
}

#: Partidas de la hoja de inversión: las escribe `semilla_ham.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-24
#: del molde; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = base de los
#: imprevistos, 10 años; 'maquinaria' = 10 años). = Sushi Bar sin vitrina, arrocera, hangiri, inducción ni pH-metro.
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|marca|\bweb\b|'
           r'foto|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|formaci[oó]n|seguro|licencia|permiso|'
           r'\btasas?\b',),
    'obra': (r'proyecto t[eé]cnico|\bobra\b|conducto|salida de humos|instalaci[oó]n el[eé]ctrica|fontaner|'
             r'climatizaci|r[oó]tulo|fachada',),
    'maquinaria': (r'congelador|arc[oó]n|plancha|freidora|campana|armarios?|frío|frio|lavavajillas|fregadero|'
                   r'utillaje|menaje|barra|mobiliario|tpv|dat[aá]fono',),
}

#: Costes fijos. Las 9 partidas propias (14.400 €/año) las escribe `semilla_ham.py` en las filas 26-34 (rótulo e
#: importe); aquí, la nota por rótulo normalizado (minúsculas y sin tildes) y la de la fila canónica del alquiler.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Los dos meses de renta '
              'previos a la apertura están en la hoja de Inversión y NO se cuentan dos veces'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL, nóminas y contratos de la plantilla'),
    'mantenimiento de la campana extractora y el conducto, la plancha y el gas, las freidoras y el frio': (
        None, 'La limpieza de la campana extractora y del conducto al menos una vez al año (Madrid lo exige en su '
              'Ordenanza 4/2021, art. 23; mira la de tu ayuntamiento), la revisión de la plancha y de la instalación '
              'de gas, las freidoras y el frigorista para los armarios, el congelador y la mesa refrigerada'),
    'marketing y publicidad': (
        None, 'Ficha de Google Business, redes sociales con vídeo (la smash se vende en vídeo), fotos y las '
              'promociones de las plataformas; la campaña de apertura va en la inversión'),
    'software, tpv, integrador de plataformas, telefono e internet': (
        None, 'Cuota del TPV con Veri*factu, el integrador que junta los pedidos de las plataformas en una pantalla, '
              'teléfono e internet'),
    'limpieza, lavanderia, epi y analisis de autocontrol': (
        None, 'Productos de limpieza y desengrasantes, lavado de uniformes y paños, guantes y los análisis de '
              'autocontrol que fije tu APPCC'),
    'gestion de residuos y del aceite usado de las freidoras': (
        None, 'La tasa de basuras, el cartón de las cajas y el aceite usado de las freidoras, que recoge un gestor '
              'autorizado: nunca al desagüe ni de vuelta a la cocina. Pon las de tu ayuntamiento'),
    'desinsectacion, desratizacion y desinfeccion (ddd)': (
        None, 'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
    'derechos de autor por musica ambiental (sgae y agedi-aie)': (
        None, 'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los metros y del aforo de tu sala'),
    'prevencion de riesgos laborales, vigilancia de la salud y formacion': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): quemaduras de la plancha y de las freidoras, cortes, '
              'resbalones con la grasa y cargas; los reconocimientos médicos de la plantilla y la formación en higiene '
              'de la carne picada y en alérgenos'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Margen bruto al 52 %: el caso da un 59,5 % tras TODOS los costes variables (la
#: plataforma pesa un 24 % de las ventas).
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.52,
     'Suelo del margen tras TODOS los costes variables (mercancía, envases, plataforma, medios de pago y varios). Con '
     'casi un cuarto de las ventas por plataforma, una hamburguesería deja menos que una sala sola. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.30,
     'Techo de la materia prima sobre ventas: la carne es más de la mitad de la compra de comida y su precio manda. '
     'Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'Techo del personal sobre ventas con plancha, montaje, mostrador y dos servicios. Estimación del kit'),
    ('r_alquiler', 'Alquiler / Ventas', 0.10,
     'Techo del alquiler sobre ventas para un local con salida de humos a cubierta: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga. Una hamburguesería bien llevada deja en torno a '
     'un 8-10 %. Estimación del kit'),
)

#: (comensales al día, € por comensal sin IVA, días de apertura). R §3.
ESCENARIOS = {
    'pesimista': (80, 15.25, 295),     # menos comensales, ticket más bajo y una semana más de cierre
    'optimista': (110, 16.75, 305),
}

#: Mes 1 = ENERO, sin girar: el calendario de R §3 tal cual (enero el valle por el cierre de 10 días y la cuesta de
#: enero, agosto baja con la ciudad vacía, mayo y junio los picos).
ESTACIONALIDAD = (0.072, 0.080, 0.085, 0.086, 0.089, 0.088,
                  0.086, 0.076, 0.085, 0.087, 0.082, 0.084)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es ENERO, en el orden del calendario: la rampa del arranque va de enero a abril, enero es el '
        'mes más flojo (cierre de 10 días y cuesta de enero), agosto baja con la ciudad vacía y mayo es el pico; por '
        'eso el fondo de maniobra cuenta. Si abres en otro mes, gira la fila de estacionalidad. El saldo mínimo del año '
        'nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El plan de negocio en Word de este pack cita las cifras de este Excel: si cambias una celda verde, el Excel '
        'manda. La calculadora de la carne, las patatas y el escandallo del pack va aparte: saca el coste por kilo útil '
        'de la carne, las bolas que salen de cada kilo, el coste de cada ración de patatas y del aceite, y ESCANDALLA '
        'cada hamburguesa y el menú en cada canal. No copies el food cost de una hamburguesa en la hoja de Supuestos: '
        'la celda «Coste de mercancía sobre las ventas de COMIDA» es la media ponderada de TODA la carta más lo que se '
        'tira al cierre, las comidas del personal y las promociones de la plataforma, y por eso sale más alta que el '
        'escandallo teórico. Con los escandallos de tu carta, comprueba que esa media cuadra.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Enero', 'Decisión del plan',
         'En el orden del calendario: la rampa cae sobre enero-abril, enero es el mes más flojo y mayo el pico. Si '
         'abres en otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Hamburguesa en el reparto a domicilio', 'El plato más pedido por tercer año',
         'Gastrómetro de Just Eat 2025, publicado en prensa en diciembre de 2025',
         'Por eso el caso cuenta un 24 % de las ventas por plataforma, con techo'),
        ('Smash y menú en carta', '11,50-13,00 € la hamburguesa · 13,90-15,00 € el menú',
         'Cartas de una cadena de smash burgers en Málaga y Barcelona leídas en octubre de 2026',
         'El caso: menú de smash doble con patatas y bebida a 15,90 € con IVA'),
        ('Bola de carne de una smash', '80-100 g', 'Cartas de hamburgueserías de smash leídas en octubre de 2026',
         'El caso usa bolas de 100 g: la smash doble lleva dos'),
        ('Hamburguesas por kilo de carne', '10 bolas de 100 g', 'Cálculo de la calculadora del pack',
         'Cinco hamburguesas dobles. Con la merma de cierre salen menos: pesa tus bolas y lleva tus gramos a la '
         'calculadora'),
        ('Comisión de la plataforma con su reparto', '13-35 % más IVA',
         'Guías del sector, 2025-2026: compruébalo en tu contrato',
         'El plan básico de Uber Eats ronda el 30 %. Lo que se recoge en el local no paga comisión'),
        ('IVA de la hamburguesería', '10 % en la venta · 21 % la cerveza y los refrescos para llevar',
         'Ley 37/1992, art. 91.Uno.1.1.º, 91.Uno.2.2.º y 91.Dos.1.1.º',
         'La comida, al 10 % en sala, para llevar y a domicilio. La cerveza y los refrescos con azúcares o edulcorantes '
         'añadidos (también los zero) que salen del local, al 21 %. El queso, el huevo, la leche, la patata fresca y la '
         'verdura se compran al 4 %; el pan de hamburguesa no es pan común: va al 10 %'),
        ('Carne picada', '2 °C o menos · del día si la picas tú', 'Real Decreto 1021/2022, arts. 4.1 y 7.2',
         'Los preparados de carne (la bola salada o aliñada antes de la plancha), a 4 °C o menos. Si picas en el '
         'local, sólo lo que vayas a vender ese día: nunca de un día para otro'),
        ('Temperatura de fritura', 'Por debajo de 175 °C', 'Reglamento (UE) 2017/2158, anexo II, parte A',
         'Contra la acrilamida: patatas guardadas a más de 6 °C, la fresca en remojo o escaldada y una guía de colores '
         'a la vista del personal'),
        ('Aceite de fritura', 'Menos de un 25 % de compuestos polares', 'Orden de 26 de enero de 1989, art. 6.3',
         'Cámbialo antes de llegar ahí y anota cada cambio; el usado, a un gestor autorizado. Tu APPCC elige cómo lo '
         'controlas: tiras, medidor o cambio por frecuencia'),
        ('Salario mínimo interprofesional 2026', '1.221 € al mes en 14 pagas', 'Real Decreto 126/2026',
         'A prorrata en jornada parcial'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Nombra expresamente las hamburgueserías. Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_ham.py` entero (`datos_checklist.py`): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO de la compra de COMIDA (R §1): carne, pan de hamburguesa (no es «pan común»), salsas, bacon, patata
#: congelada, aceite de girasol (sólo los de oliva van al 4 %, letra g) y helado al 10 % (≈ 84 % de la compra de
#: comida); queso, huevo, patata fresca, verdura y leche al 4 % (≈ 16 %) → 0,84 × 10 + 0,16 × 4 = 9,0 %. La bebida
#: tiene su propio tipo de compra (`pct_bebida_alc`): no se mezcla aquí.
IVA_COMPRAS = {
    'comida': 0.090,
    'nota': 'Carne, pan de hamburguesa (no es pan común), salsas, bacon, patata congelada, aceite de girasol y helado '
            'al 10 %; queso, huevo, patata fresca, verdura y leche al 4 % (art. 91.Dos.1.1.º de la Ley 37/1992). '
            'Ajústalo a tus facturas',
}
