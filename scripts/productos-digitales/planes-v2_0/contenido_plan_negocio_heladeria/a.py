#!/usr/bin/env python3
"""
Contenido de `plan-negocio-heladeria` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Camino del Parrillero ES 2.2 con semilla de la Panadería
ES 2.2: `plan-heladeria/semilla_hel.py` copia los dos xlsx publicados de la panadería (solo lectura), les pone las 19
partidas, los 10 fijos y los títulos de la heladería, y `main.py` + `grupo_a.py` los reconstruyen con este módulo.
SPEC: `plan-heladeria/SPEC.md` (D1-D18); cómo se construye: `plan-heladeria/F1-camino.md` §2; caso:
`plan-heladeria/F1-research-heladeria.md` §3; normativa: ídem §1.

MOTOR DE INGRESOS (mostrador, como la panadería)
------------------------------------------------
    cubiertos_dia (B4) = CLIENTES AL DÍA, media del año     143
    ticket_medio  (B5) = € POR CLIENTE SIN IVA              4,90 €
    dias_apertura (B6) = DÍAS DE APERTURA AL AÑO            310
Ventas a régimen = 143 × 4,90 × 310 = 217.217 €. La estacionalidad va ROTADA: el Mes 1 de la Tesorería es MARZO (SPEC
D6), por eso las pagas extra salen en los meses 5 (julio) y 10 (diciembre).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §n» = `F1-research-heladeria.md` §n (casi
todo [estimado], criterio de kit, con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado D9» =
ajustado en F2 para cumplir los gates del caso de la SPEC.

⚠️ Rótulos de importe: sin «clientes», «personas», «días», «meses», «años», «plazas» ni «unidades»
(`motor.RX_RECUENTO_DV` les quita el formato de euro). Las notas no usan «sala», «cubierto» ni «comensal»: el
VOCABULARIO los traduciría. Sesión Claude Code, 25-oct-2026.
"""

CONCEPTO = 'Heladería Artesanal'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Masculino «cliente» = masculino
#: «cubierto»: sin arreglos de concordancia. Las frases largas arreglan restos de otros moldes que el motor escribe.
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubierto': 'cliente',
    'cubiertos': 'clientes',
    'comensal': 'cliente',
    'comensales': 'clientes',
    'sala': 'mostrador',
    'en sala': 'en el local',
    'en barra y sala': 'en el mostrador y en la mesa',
    # restos de la panadería y de otros moldes en frases fijas del motor (barrido_es.py los caza)
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'sólo el alcohol que saliera por delivery movería',
    'los alimentos —bollería y pastelería incluidas—, que son':
        'los alimentos —helado y tartas heladas incluidos—, que son',
    'refrescos o zumos con azúcares añadidos': 'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos',
    'el pan común y las harinas panificables, al superreducido (art. 91.Dos.1.1.º':
        'el helado y la comida para llevar, al reducido (art. 91.Uno.1.1.º',
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # SPEC D6 y D13: las dos notas de la Tesorería
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = MARZO: el plan abre en temporada para llegar al primer invierno con la caja del verano. El pico es '
        'julio (Mes 5) y el valle, enero (Mes 11), con tres semanas de cierre. Si abres en otro mes, gira la fila',
    # m4 (revisión final): no es sólo «prudente»: el verano sale más barato y la caja de junio a enero, inflada
    'La suma del año es la misma que la del P&L':
        'La suma del año es la misma que la del P&L. El personal se reparte en doce meses, pero los fijos '
        'discontinuos de temporada sólo cobran de abril a septiembre: aquí el invierno sale más caro y el verano más '
        'barato que en la realidad. El saldo de marzo y el de febrero apenas cambian, pero de junio a enero tu caja '
        'real será menor que la de esta hoja (en el caso, hasta unos 10.000 € menos en septiembre)',
    # M7 (revisión final): nota de Tesorería!A34, resto del molde con el Mes 1 en enero
    'El IVA del cuarto trimestre se liquida en enero del año siguiente, así que no aparece en este cuadro':
        'Los trimestres de esta hoja son de tres meses del plan (marzo-mayo, junio-agosto y septiembre-noviembre), '
        'no los naturales: con el Mes 1 en marzo, el modelo 303 se presenta en abril (por marzo), julio, octubre y '
        'enero (por octubre-diciembre, ya en el Mes 11). En el caso todos los trimestres salen a compensar y no '
        'mueven la caja; a 31 de diciembre quedan unos 17.750 € por compensar, que puedes pedir como devolución en '
        'el 303 de enero',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 143, None,
        'Clientes servidos al día de media del año 1, en mostrador, para llevar y en mesa: unos 236 en julio y unos '
        '70 en enero. Sale de dividir la venta prevista entre el ticket y los días de apertura; contrástalo con el paso '
        'de gente de tu calle en una tarde de verano y en una de febrero',
        'research §3 [estimado]'),
    'ticket_medio': (
        None, None, 4.90, None,
        'SIN IVA, por persona que compra: dos bolas, más las tarrinas de medio litro, las tartas por encargo y las '
        'crepes del invierno. Equivale a un tique de caja de unos 7 € sin IVA, porque cada tique es de 1,45 personas '
        'de media. El precio con IVA está en la fila «PVP equivalente con IVA» de abajo',
        'research §2-§3 (carta del caso) [estimado]'),
    'dias_apertura': (
        None, None, 310, None,
        '365 días menos tres semanas de cierre en enero (vacaciones y mantenimiento del frío), los lunes de octubre a '
        'marzo y algún festivo. Es el MISMO dato para la cuenta de resultados, el punto de equilibrio, los escenarios '
        'y las horas de personal',
        'research §3 [estimado]'),
    'crec_a2': (
        None, None, 0.08, None,
        'Más clientela el segundo verano, las tartas heladas por encargo y el canal de restaurantes ya rodados. Se '
        'aplica a los clientes; el personal NO sube con este porcentaje: crece con las incorporaciones que declares '
        'en la hoja Personal (6.000 € el año 2 y otros 6.000 € el año 3)',
        'research §3 [estimado]'),
    'crec_a3': (
        None, None, 0.05, None,
        'Sobre el año 2. Conservador: el techo lo ponen la vitrina de 18 cubetas y las tardes de julio y agosto',
        'research §3 [estimado]'),
    'pct_comida': (
        None, None, 0.90, None,
        'Helado, obrador e invierno (bola, tarrina, para llevar, tartas heladas, crepes y gofres, restaurantes) sobre '
        'las ventas; el 10 % restante es cafetería y bebidas. Es el peso de la primera línea de ventas del P&L',
        'research §3 [estimado] · SPEC D5 (90/10)'),
    'coste_comida': (
        None, None, 0.20, None,
        'Materia prima del helado y del obrador sobre sus ventas: el helado de mostrador sale al 16 %, el de llevar al '
        '18 %, las crepes y los gofres al 28 % y lo que vendes a restaurantes al 32 % (18,6 % de media), y el plan '
        'suma 1,4 puntos por lo que se mueven el pistacho, el cacao y la vainilla. Escandalla cada sabor cada temporada',
        'research §2-§3 [estimado]'),
    'coste_bebida': (
        None, None, 0.25, None,
        'Café, chocolate a la taza, batidos, granizado y horchata propios, agua y refrescos sobre sus ventas: el '
        'granizado propio sale al 15 % y los refrescos, al 35-40 %',
        'research §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.04, None,
        'Barquillos y cucuruchos, tarrinas, cucharillas de madera, envases isotérmicos de cartón para llevar y '
        'servilletas: unos 0,28 € por tique de caja. Sin poliestireno expandido para el consumo inmediato',
        'research §3 [estimado]'),
    'pct_delivery': (
        None, None, 0.03, None,
        'Tarrinas de medio litro y de litro en envase isotérmico por plataforma, las noches de verano: la tarrina viaja '
        'bien, la bola no. Es entrega de bienes: el helado va al 10 %',
        'research §3 [estimado]'),
    'comision_delivery': (
        None, None, 0.30, None,
        'Comisión media de la plataforma sobre lo que vende ese canal. Si repartes tú, pon 0',
        'research §3 [estimado]'),
    'comision_tpv': (
        None, None, 0.008, None,
        'Tarjeta y bizum sobre el total facturado',
        'molde (= panadería)'),
    'alquiler_mes': (
        None, None, 1700, None,
        'Local de 85 m² (obrador de 20-25 m², tienda con vitrina de 18 cubetas y 20 plazas, almacén y aseo) en una '
        'calle comercial de barrio o un paseo de una ciudad media, sin traspaso: unos 20 € el m². El peso sobre las '
        'ventas lo calcula el propio libro en la fila «Alquiler / Ventas» del P&L',
        'research §3 [estimado]'),
    'fianza_meses': (
        None, None, 3, None,
        'Tres meses de renta, lo habitual en un contrato de local de negocio',
        'research §3 [estimado]'),
    'suministros_mes': (
        None, None, 700, None,
        'Sobre todo luz: unos 30 kW en trifásica y las vitrinas encendidas las 24 horas (cada módulo de 10 cubetas '
        'gasta unos 23 kWh al día). Unos 800-850 € en verano y 450-500 € en invierno; pide el histórico del local',
        'research §2-§3 [estimado]'),
    'seguros_ano': (
        None, None, 1500, None,
        'Responsabilidad civil de al menos 300.000 € y multirriesgo CON avería de maquinaria y deterioro de mercancía '
        'en frío: una vitrina parada en agosto es una cubeta perdida por sabor',
        'research §3 [estimado]'),
    'pct_varios': (
        None, None, 0.02, None,
        'Colchón de gasto corriente no presupuestado (pequeñas reparaciones, catas y degustaciones)',
        'molde (= panadería)'),
    'recursos_propios': (
        None, None, 55000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §3 [estimado]'),
    'prestamo': (
        None, None, 129000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D9: cubre la necesidad de caja del libro con 55.000 € propios (research: 125.000 €; el IVA de la '
        'inversión y el fondo de maniobra salen algo más altos que la cuenta a mano)'),
    'tipo_prestamo': (
        None, None, 0.06, None,
        'Tipo nominal anual. Pide oferta a dos entidades y a una línea ICO antes de fijarlo; la maquinaria de frío es '
        'objeto habitual de leasing o renting: compáralo',
        'research §3 (= panadería) [estimado]'),
    'plazo_prestamo': (
        None, None, 7, None, 'Años totales, carencia incluida',
        'research §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: obra y maquinaria antes de facturar y un primer invierno por delante. Desde el '
        'segundo año se devuelve el principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'research §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: son el colchón del primer invierno, cuando de noviembre a febrero entra '
        'alrededor del 15 % de la venta del año con los fijos planos',
        'molde (mínimo de la familia) · research §6'),
    'vida_obra': (
        None, None, 10, None,
        'Obra del obrador, instalación eléctrica trifásica, fontanería, desagües, climatización y rótulo. Coeficientes '
        'de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades: confírmalo con tu asesor',
        'research §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Pasteurizador, mantecadora, abatidor, armarios, vitrina, cafetera, mobiliario y TPV: un 10 % anual, dentro '
        'del coeficiente máximo de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades para la maquinaria '
        '(12 %) y para el mobiliario (10 %). Confírmalo con tu asesor',
        'calibrado D9 (research: 9 años, el máximo de la maquinaria; 10 cumple también el del mobiliario y abre la '
        'ventana de la demo §2.11.5 del motor)'),
    'pct_bebida_alc': (
        None, None, 0.0, None,
        'A CERO: la carta de bebida de este plan es café, chocolate, batidos, granizado, horchata, agua y refrescos, '
        'sin alcohol. Si sirves algún licor con el helado, súbelo',
        'research §3'),
    'aforo': (
        None, 'Aforo del local (plazas sentadas, sin la terraza)', 20, None,
        'DATO INFORMATIVO: la mayoría de la venta es de mostrador y para llevar. La terraza suma otras 20 plazas en '
        'temporada (5 mesas), con su autorización municipal aparte',
        'research §3 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'Las heladerías están en el convenio PROVINCIAL de hostelería (art. 4 del VI Acuerdo Laboral de ámbito Estatal '
        'para el sector de Hostelería): copia aquí el salario base del grupo más bajo de la tabla de TU provincia. '
        'Con 0 el semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.70, None,
        'Una heladería que abre en marzo no factura el primer mes lo que factura a los cuatro: la compra es de impulso '
        'y el barrio tarda en descubrirte, aunque la curva de temporada ya hace lenta la primavera. Con 100 % se '
        'elimina la rampa',
        'research §3 [estimado]'),
    'meses_rampa': (
        None, None, 4, None,
        'Cuatro meses hasta el ritmo de crucero: de marzo a junio, justo antes del pico del verano',
        'research §3 [estimado]'),
    'meses_renta_previa': (
        None, None, 2, None,
        'Dos meses de renta antes de abrir: la obra del obrador, el aumento de potencia a trifásica y la '
        'declaración responsable. Si el banco te da el préstamo al empezar la obra, súmale los intereses de esos '
        'meses (en el caso, unos 1.290 €), que este libro no cuenta, y ten en cuenta que la carencia corre desde la '
        'firma',
        'research §3 [estimado] · revisión final m17 (2 × 645 € de intereses al mes)'),
    'pct_imprevistos': (
        None, None, 0.10, None,
        'Colchón sobre la obra y las instalaciones del local, que es donde aparecen las sorpresas (acometida '
        'eléctrica, desagües, salida de aire de los condensadores). Un banco no financia una reforma sin él',
        'research §3 (10 % sobre la obra) [estimado]'),
    'dias_cobro': (
        None, None, 2, None,
        'Media ponderada: el mostrador cobra al contado y los restaurantes a los que vendes helado (un 5 % de las '
        'ventas) pagan a 30 días',
        'research §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a proveedores de leche, nata, fruta, pastas y envases: lo que te financian. Es lo primero que se '
        'pierde si te retrasas en un pago',
        'research §3 (= panadería)'),
    'mes_paga_1': (
        None, None, 5, None,
        'Mes de la TESORERÍA en el que sale la paga extra de verano: julio es el Mes 5, porque el Mes 1 del plan es '
        'marzo',
        'SPEC D6 (Mes 1 = marzo)'),
    'mes_paga_2': (
        None, None, 10, None,
        'Mes de la TESORERÍA en el que sale la paga extra de Navidad: diciembre es el Mes 10, porque el Mes 1 del plan '
        'es marzo',
        'SPEC D6 (Mes 1 = marzo)'),
    'iva_bebida': (
        None, None, 0.10, None,
        'Este plan no sirve alcohol (celda de arriba a 0), así que esta celda no mueve nada. Si lo sirves, el '
        'consumido en el local va al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992) y el que sale para llevar, al 21 %',
        'Ley 37/1992 art. 91.Uno.2.2.º'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente). Dos líneas: `mix_en_supuestos` (el peso se teclea en Supuestos).
#: Todo al 10 % de IVA (helado, art. 91.Uno.1.1.º y 2.2.º LIVA): sin línea partida.
LINEAS_INGRESO = (
    ('Ventas de helado y obrador (mostrador, para llevar, tartas, invierno y restaurantes)', 0.90, 'comida',
     'Del total de ventas: helado de mostrador (bola, copa y cucurucho) 58 %, para llevar y tartas heladas 17 %, '
     'invierno (crepes y gofres, tartas y turrón helado de Navidad por encargo) 10 % y restaurantes y eventos 5 %. '
     'Todo al 10 % de IVA, se tome en el local o se lleve',
     'research §3 [estimado]'),
    ('Ventas de cafetería y bebidas (sin alcohol)', 0.10, 'bebida',
     'Café, chocolate a la taza, batidos, granizados, horchata, agua y refrescos',
     'research §3 [estimado]'),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada: 1.300 € a jornada completa, por encima del SMI en proporción.
PLANTILLA = (
    ('Titular — maestro heladero, compras y gestión', 1, 1750,
     'Balancea las mezclas, pasteuriza, manteca y abate, compra y lleva la gestión. Como administrador de la SL '
     'cotiza en el régimen de autónomos: el libro le imputa el 33 % de Seguridad Social sobre 14 pagas como si '
     'fuera nómina (con este bruto, unos 8.085 € al año), que es el lado prudente. Confirma con tu gestoría la '
     'cuota real y si te aplica la reducida de inicio',
     'research §3 [estimado]', 1.0),
    ('Dependiente/a y encargado/a de turno (todo el año)', 1, 1300,
     'Mostrador, caja, vitrina y cierre; abre y cierra cuando el titular está en el obrador',
     'research §3 [estimado]', 1.0),
    ('Dependiente/a de temporada (fijo discontinuo, abril-septiembre)', 1, 650,
     'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) a jornada completa de abril a septiembre: '
     'equivale a media jornada en cómputo anual. Llamamiento por escrito',
     'research §3 [estimado] · ET art. 16', 0.50),
    ('Dependiente/a de verano (fijo discontinuo, junio-septiembre)', 1, 325,
     'Fijo discontinuo de 30 horas a la semana de junio a septiembre: las tardes y noches del pico. Nunca como '
     'autónomo que te factura: con tu horario y tu dirección es falso autónomo (art. 1.1 ET)',
     'research §3 [estimado] · ET arts. 1.1 y 16', 0.25),
    ('Ayudante de obrador (fijo discontinuo, mayo-septiembre)', 1, 260,
     'Media jornada de mayo a septiembre: pesaje, limpieza del pasteurizador y de la mantecadora, cubetas y apoyo en '
     'las tandas del verano',
     'research §3 [estimado] · ET art. 16', 0.20),
    ('Suplencias de vacaciones y descansos', 1, 130,
     'Cobertura de los 30 días de vacaciones (art. 38 ET) y del descanso semanal del equipo de todo el año',
     'molde (RC-19, = panadería)', 0.10),
)

#: Cobertura: tienda (horas × personas a la vez) + obrador ANTES de abrir, por los días de apertura.
COBERTURA = {
    'horas_dia': 9.5,
    'personas_franja': 1.6,
    'horas_produccion': 2.75,
    'personas_produccion': 1,
    'nota_horas': 'Media del año de la apertura de la TIENDA: 12 h en temporada alta (de mediados de abril a '
                  'septiembre), 8 h en marzo y octubre y 6 h entre semana en invierno. El obrador va en la fila de abajo',
    'nota_personas': 'Presencia media a la vez en el mostrador: 1,8-2 personas en verano, 1,3 en primavera y otoño y '
                     '1 en invierno. En julio y agosto el cuadrante va justo: el titular hace horas o entra un extra '
                     'de fin de semana',
    'nota_horas_produccion': 'Tandas del obrador antes de abrir: pasteurizar, enfriar, madurar, mantecar y abatir. '
                             'Unas 4 h en julio y 1,5 h en invierno',
    'nota_personas_produccion': 'El maestro heladero; en verano le ayuda el ayudante de obrador',
}

ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_hel.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-25
#: del molde de la panadería; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = base de
#: los imprevistos, 10 años; 'maquinaria' = 9 años).
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|marca|\bweb\b|'
           r'foto|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|formaci[oó]n|seguro|licencia|permiso|'
           r'\btasas?\b',),
    'obra': (r'proyecto t[eé]cnico|\bobra\b|instalaci[oó]n el[eé]ctrica|fontaner|desag[uü]|climatizaci|ventilaci|'
             r'r[oó]tulo|escaparate',),
    'maquinaria': (r'pasteurizador|mantecadora|abatidor|armario|mesas inox|fregadero|vitrina|mostrador|'
                   r'lavaporcionador|cafetera|crepera|gofrera|mobiliario|terraza|tpv|dat[aá]fono|b[aá]scula|menaje|'
                   r'uniforme|carteler',),
}

#: Costes fijos. Las 10 partidas propias las escribe `semilla_hel.py` en las filas 26-35 (rótulo e importe); aquí,
#: la nota por rótulo normalizado (minúsculas y sin tildes) y la de las filas canónicas.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Los dos meses de renta '
              'previos a la apertura están en la hoja de Inversión y NO se cuentan dos veces'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL y nóminas de los fijos discontinuos, con sus llamamientos de cada '
              'temporada'),
    'mantenimiento del frio (contrato con frigorista certificado)': (
        None, 'Revisión de vitrinas, abatidor, mantecadora y armarios antes del verano y en las semanas de cierre de '
              'enero. La carga de gases refrigerantes la hace sólo un técnico certificado: el personal no la toca'),
    'marketing y publicidad de temporada': (
        None, 'Redes sociales, ficha de Google Business, cartelería y la campaña de apertura de cada temporada, más '
              'la de tartas y turrón helado de Navidad'),
    'software, telefono e internet': (
        None, 'Cuota del TPV con Veri*factu, teléfono e internet'),
    'limpieza, lavanderia, epi y analisis de autocontrol': (
        None, 'Productos de limpieza y desinfección, lavado de uniformes, guantes para trabajar a −20 °C y los '
              'análisis de autocontrol que fije tu APPCC'),
    'tasa de terraza (pon la de tu ayuntamiento)': (
        None, 'Ocupación de la vía pública con 5 mesas en temporada. Cada ayuntamiento tiene su ordenanza fiscal y '
              'este plan no ha leído ninguna: sustituye esta cifra por la de tu ayuntamiento'),
    'gestion de residuos': (
        None, 'Cartón, envases y orgánico del obrador con gestor autorizado o por el servicio municipal'),
    'desinsectacion, desratizacion y desinfeccion (ddd)': (
        None, 'Empresa inscrita en el ROESB; forma parte del plan APPCC'),
    'derechos de autor por musica ambiental (sgae y agedi-aie)': (
        None, 'SGAE y AGEDI-AIE son dos licencias distintas; el importe depende de los metros y del aforo de tu tienda'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): trabajo en frío, cargas y cortes, y '
              'reconocimientos médicos de la plantilla'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Margen bruto al 70 % y no al 72 % del research: el propio caso da un 71,8 %
#: con mercancía, consumibles, plataforma, TPV y varios (research §3, cuenta a mano) y gelatomaps publica 60-70 %.
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.70,
     'Suelo del margen tras TODOS los costes variables (mercancía, envases, plataforma, medios de pago y varios): un '
     'helado artesano con obrador propio deja por encima del 70 %. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.25,
     'Techo de la materia prima sobre ventas: el helado de mostrador sale al 14-16 % y el pistacho, el cacao y la '
     'vainilla lo mueven. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.40,
     'Techo del personal sobre ventas, más alto que en una cafetería: la temporada obliga a doblar mostrador de junio '
     'a septiembre. Estimación del kit'),
    ('r_alquiler', 'Alquiler / Ventas', 0.12,
     'Techo del alquiler sobre ventas para un local con obrador: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga: estimación del kit'),
)

#: (clientes al día, € por cliente sin IVA, días de apertura).
ESCENARIOS = {
    'pesimista': (120, 4.60, 300),     # un verano frío y lluvioso
    'optimista': (165, 5.20, 320),
}

#: Mes 1 = MARZO (SPEC D6). Calendario: ene .025 · feb .030 · mar .050 · abr .075 · may .100 · jun .135 · jul .165 ·
#: ago .150 · sep .110 · oct .065 · nov .035 · dic .060 (research §3: abril-septiembre al 73 % frente al 81,6 % de
#: los hogares del MAPA, porque el invierno vende crepes, chocolate y Navidad). Rotada al orden del motor (Mes 1…12).
ESTACIONALIDAD = (0.050, 0.075, 0.100, 0.135, 0.165, 0.150,
                  0.110, 0.065, 0.035, 0.060, 0.025, 0.030)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es MARZO: el plan abre en temporada para llegar al primer invierno con la caja del '
        'verano. El saldo mínimo del año nunca puede salir en rojo.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El documento Word de este pack usa las cifras de este Excel: si cambias una celda verde, el Excel manda.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Marzo', 'Decisión del plan',
         'Abrir en otoño gasta el fondo de maniobra antes del primer verano. La fila de estacionalidad de la '
         'Tesorería ya va girada'),
        ('Consumo de helado en los hogares de abril a septiembre', '81,6 % del volumen del año',
         'MAPA, nota de prensa del 12 de agosto de 2026',
         'Julio el 20 %, junio el 17,8 % y agosto el 17,1 %. Este plan pone el 73 % de abril a septiembre porque '
         'en invierno vende crepes, chocolate y tartas de Navidad'),
        ('Coste del helado de mostrador', '14-16 % de su venta', 'Estimación del kit',
         'Dos bolas con mezcla a unos 3,2 € el kg, con merma, toppings y catas. Las crepes y lo que vendes a '
         'restaurantes cuestan más'),
        ('Precio de la bola', '2-4 €, hasta 6 € en las gourmet', 'Prensa local, mayo de 2026',
         'Con IVA. El ticket SIN IVA de este plan está en la hoja 0. Supuestos'),
        ('Densidad mínima del helado', '430 g por litro', 'RD 618/1998, art. 3',
         'Entre 375 y 430 g/l se llama «espuma», «mousse» o «montado». El mismo artículo fija las denominaciones: '
         '«helado crema», «mantecado» (4 % de yema o más) y «sorbete» (15 % de fruta o más)'),
        ('Conservación del helado', '−18 °C o menos, sin recongelar', 'RD 1021/2022, arts. 4.1 y 5.9',
         'La temperatura de la vitrina no la fija ninguna norma estatal: la fija tu APPCC'),
        ('Huevo en la mezcla', '70 °C durante 2 s, u ovoproducto', 'RD 1021/2022, art. 9',
         'Pasteurizar a 85 °C lo cumple. Yemas, nata y grasas van ANTES de pasteurizar, nunca después; con huevo, se '
         'manteca en las 24 horas siguientes'),
        ('Coste de personal sobre ventas', '34-40 %', 'Estimación del kit',
         'La temporada dobla el mostrador de junio a septiembre con fijos discontinuos'),
        ('Alquiler sobre ventas', '8-12 %', 'Estimación del kit', 'Un local con obrador necesita más metros que un '
         'quiosco o una vitrina sin obrador'),
        ('Merma de la producción', '5-8 %', 'Estimación del kit — mídela tú cada semana',
         'El helado derretido o devuelto no se recongela'),
        ('Potencia eléctrica del local', 'Unos 30 kW en trifásica', 'Estimación del kit',
         'Vitrinas las 24 horas, pasteurizador, mantecadora, abatidor, crepera y climatización. Compruébalo antes de '
         'firmar el alquiler'),
        ('IVA del helado', '10 %', 'Ley 37/1992, art. 91.Uno.1.1.º y 2.2.º',
         'En el mostrador, en la mesa y para llevar. Los refrescos con azúcares añadidos para llevar, al 21 %'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Nombra las heladerías. Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_hel.py` entero (`datos_checklist.py`, SPEC D14): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO de la compra de comida: leche, huevos, fruta y quesos al 4 % (≈ 30 % de la compra); nata, azúcar,
#: chocolate, pastas, barquillos y envases al 10 % (≈ 70 %) → 0,3 × 4 % + 0,7 × 10 % = 8,2 %.
IVA_COMPRAS = {
    'comida': 0.082,
    'nota': 'El IVA que SOPORTAS al comprar: la leche, los huevos, la fruta y los quesos van al 4 % (art. 91.Dos.1.1.º '
            'de la Ley 37/1992) y la nata, el azúcar, el chocolate, las pastas y los barquillos al 10 %; con un 30 % de '
            'la compra al 4 % sale un 8,2 %. Ajústalo a tus facturas',
}
