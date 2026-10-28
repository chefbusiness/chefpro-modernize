#!/usr/bin/env python3
"""
Contenido de `plan-negocio-cafeteria-movil-eventos` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior), línea de eventos con el motor 2.2. Contenido clonado del
Parrillero ES 2.2 (motor de eventos sin permutar, base sin local por `VOCABULARIO`, vehículo como «obra», fijos
discontinuos) con el injerto del Mes 1 girado de la Finca 1.0, sobre la semilla del Food Truck ES 2.2:
`plan-cafeteria-movil/semilla_caf.py` copia los dos xlsx publicados del food truck (solo lectura), les pone las 14
partidas, los 10 fijos, los títulos y el checklist de la cafetería móvil, y `main.py` + `grupo_a.py` los reconstruyen
con este módulo. SPEC: `plan-cafeteria-movil/SPEC.md` (D1-D15); cómo: `F1-camino.md` §1-§2; caso:
`F1-research-cafeteria-movil.md` §4 y §8; normativa: §2.

MOTOR DE INGRESOS SIN PERMUTAR (como parrillero, paellero, catering ES y finca)
------------------------------------------------------------------------------
    cubiertos_dia (B4) = INVITADOS POR EVENTO (media)       135   (en la venta directa, tazas vendidas)
    ticket_medio  (B5) = € POR INVITADO SIN IVA             6,20 €  (research 6,10 €; palanca 1 de D9: bodas a 9 €)
    dias_apertura (B6) = EVENTOS AL AÑO                     130
Ventas = 135 × 6,20 × 130 = 108.810 €. La SPEC D5 dice «B4 = eventos (como catering y finca)»; catering y finca NO
permutan (catering-es-2_0/F1-camino-2_0.md §1.2: permutar rompe la cobertura de personal, que multiplica por B6): se
sigue a los hermanos, como manda el camino §2. El crecimiento de los años 2 y 3 (10 % y 8 %, calibrado D9) lo aplica el motor a B4;
en euros es lo mismo que más eventos del mismo tamaño (la nota de B7 lo dice). La venta directa en mercados y ferias va
por el canal `delivery` del motor (8,4 % de las ventas, canon del organizador del 15 %), nunca como 3.ª línea del P&L.

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §n» = `F1-research-cafeteria-movil.md` §n
(casi todo [estimado], criterio de kit, con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado
D9» = ajustado en F2 para cumplir los gates del caso de la SPEC.

⚠️ Rótulos de importe: sin «eventos», «invitados», «personas», «días», «meses», «plazas» ni «unidades»
(`motor.RX_RECUENTO` les quita el formato de euro). Las notas no usan «sala», «cubierto», «comensal», «ticket» ni
«local» (el VOCABULARIO los traduciría): el recibo es el «tique». Sesión Claude Code, 28-oct-2026.
"""
import os
import sys

CONCEPTO = 'Cafetería Móvil para Eventos'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). «El almacén base» es masculino, como «el
#: local»: concordancias medidas con `plan-cafeteria-movil/barrido_es.py`. Las frases largas reescriben las notas del
#: IVA del motor que hablaban de alcohol (M7 de la finca; camino §1: Supuestos C9 y C40, Instrucciones A8, Tesorería O16).
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubiertos/día necesarios': 'invitados por evento necesarios',
    'cubiertos/día': 'invitados por evento',
    'cubiertos necesarios al día': 'invitados necesarios por evento',
    'cubiertos al día': 'invitados por evento',
    'cubiertos que tendría que sacar': 'invitados que tendría que servir',
    'cubiertos/ticket/días': 'invitados/precio/eventos',
    'el ticket y los días': 'el precio por invitado y los eventos',
    'cubierto': 'invitado',
    'cubiertos': 'invitados',
    'comensal': 'invitado',
    'comensales': 'invitados',
    'días de apertura al año': 'eventos al año',
    'días de apertura': 'eventos',
    'días que abres': 'eventos del año',
    'horas de servicio al día': 'horas de trabajo por evento',
    'ticket medio': 'precio medio por invitado',
    'ticket': 'precio por invitado',
    'en barra y sala': 'en los eventos',
    'en sala': 'en la barra del evento',
    'servida en sala': 'servida en el evento',
    'ventas por delivery': 'ventas directas en ferias y mercados',
    'comisión de la plataforma de delivery': 'canon o comisión del organizador de la feria',
    'comisiones de delivery': 'canon de ferias y mercados',
    'delivery': 'ferias y mercados',
    'alquiler mensual del local': 'cuota mensual del almacén base',
    'alquiler de los meses previos a la apertura': 'cuota del almacén base de los meses previos al arranque',
    'fianza del alquiler': 'fianza del almacén base',
    'alquiler del local': 'cuota del almacén base',
    'local y fijos': 'almacén base y fijos',
    'un local que acaba de abrir': 'una cafetería móvil que acaba de arrancar',
    'un local que abre': 'una cafetería móvil que arranca',
    'el local': 'el almacén base',
    'del local': 'del almacén base',
    'tu local': 'tu almacén base',
    'al local': 'al almacén base',
    'arranque y aforo': 'arranque y capacidad',
    'suministros mensuales de luz, agua y gas': 'suministros mensuales (teléfono, datos y luz del almacén base)',
    'en cada franja': 'en cada evento',
    # restos de otros moldes en las frases del motor (revisiones del catering m8/m9 y del paellero m8)
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'la venta directa de ferias y mercados, también al 10 %, no mueve',
    'los alimentos —bollería y pastelería incluidas—, que son': 'los alimentos —la bollería incluida—, que son',
    'refrescos o zumos con azúcares añadidos': 'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos',
    'imprevistos de obra y acondicionamiento': 'imprevistos de la compra y preparación de la furgoneta',
    'partidas de obra y acondicionamiento': 'partidas de la furgoneta',
    'de obra y licencias': 'de puesta en marcha (pruebas de carta, catas y primeras reservas)',
    'un banco no financia una reforma sin colchón': 'un banco no financia una compra así sin colchón',
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    'el pan común y las harinas panificables, al superreducido (art. 91.Dos.1.1.º':
        'los extras con precio propio (personalización de la barra, talleres de latte art), al general (art. 90',
    'obra, instalaciones y acondicionamiento': 'furgoneta, rotulación e imprevistos',
    'de obra e instalaciones': 'de la furgoneta y su rotulación',
    'lo que se compra: obra, equipamiento': 'lo que se compra: furgoneta, equipamiento',
    'lo que se COMPRA (obra, equipamiento': 'lo que se COMPRA (furgoneta, equipamiento',
    # SPEC D6 (camino §1, M7 de la finca): las cuatro frases del IVA del motor que hablan de alcohol. Claves que empiezan
    # y acaban en carácter de palabra (el `\b` del vocabulario); el «)» final de la frase del motor se queda.
    # Supuestos!C9 (nota del PVP con IVA)
    'En sala todo va al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992, alcohol incluido); el alcohol que sale por '
    'delivery y el pan común, si los tienes, mueven la media':
        'Todo lo que sirve la cafetería móvil va al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992), en la barra del '
        'evento y en la venta directa de ferias y mercados: el precio con IVA es el de sin IVA por 1,10',
    # Supuestos!C40 (nota del tipo general)
    'En este libro lo usan dos cosas: el IVA que soportas al comprar el alcohol (el proveedor lo factura al 21 %) y el '
    'que repercutes por el alcohol que sale por delivery (es una entrega de bienes). El alcohol servido en sala va al '
    'reducido: su tipo está en el bloque de desglose del IVA. Suministros, equipamiento y servicios tienen su tipo en la '
    'celda de abajo. El libro manda al general sólo el alcohol: si compras refrescos o zumos con azúcares añadidos, su '
    'factura también va al 21 % (art. 91.Uno.1.1.º de la Ley 37/1992':
        'En este plan es el de los extras con precio propio (personalización de la barra, talleres de latte art o '
        'alquiler de la cafetera sin barista), que no están en este libro; suministros, equipamiento y servicios '
        'tienen su tipo en la celda de abajo. La cafetería no sirve alcohol: todo lo que vende va al reducido, y el '
        'libro carga la compra de café y bebidas al 10 %. La leche se factura al 4 %, así que el IVA que soportas de '
        'verdad es algo menor que el del libro (art. 91.Dos.1.1.º de la Ley 37/1992',
    # Instrucciones!A8 (punto 4: el divisor del IVA)
    'divide por el tipo que le corresponda: entre 1,10 en sala (comida y bebida, alcohol incluido: art. '
    '91.Uno.2.2.º de la Ley 37/1992 del IVA) y, cuando se venden para llevar, los alimentos —bollería y pastelería '
    'incluidas—, que son productos alimenticios al tipo reducido por el art. 91.Uno.1.1.º; y entre 1,21 el tipo '
    'general, que en hostelería sólo alcanza a lo que sale del local como entrega de bienes excluida del reducido: '
    'el alcohol y los refrescos o zumos con azúcares añadidos para llevar o a domicilio (la comida para llevar sigue '
    'al 10 %); el libro lo aplica al alcohol del canal de delivery':
        'divide entre 1,10: todo lo que sirve la cafetería móvil, en la barra del evento o en la venta directa de '
        'ferias y mercados, va al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992 del IVA; la bollería y el café que se '
        'llevan, al mismo tipo por el art. 91.Uno.1.1.º). Entre 1,21 sólo van los extras con precio propio '
        '(personalización de la barra, talleres de latte art, alquiler de la cafetera sin barista) y un refresco '
        'envasado con azúcares o edulcorantes añadidos que se venda para llevar: ninguno de los dos está en este libro',
    # Tesorería!O16 (nota del IVA repercutido)
    'Cada línea de venta a SU tipo, leído de la columna de IVA del P&L: en sala, alcohol incluido, el reducido (art. '
    '91.Uno.2.2.º de la Ley 37/1992 del IVA); el alcohol que sale por delivery, al general; el pan común y las harinas '
    'panificables, al superreducido (art. 91.Dos.1.1.º':
        'Cada línea de venta a SU tipo, leído de la columna de IVA del P&L: las bebidas y la bollería, en la barra del '
        'evento y en la venta directa de ferias y mercados, al reducido del 10 % (art. 91.Uno.2.2.º de la Ley 37/1992',
    # Tesorería (injerto de la finca, SPEC D7): Mes 1 girado, personal en doce meses y trimestres del 303
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = MARZO: el café se reserva con uno a seis meses de antelación y se arranca en primavera, con la '
        'empresa y las comuniones. Los picos son mayo y junio (Meses 3 y 4) y septiembre y octubre (Meses 7 y 8); el '
        'valle, agosto (Mes 6) y enero (Mes 11). Si arrancas en otro mes, gira la fila',
    'La suma del año es la misma que la del P&L':
        'La suma del año es la misma que la del P&L. El personal se reparte en doce meses, pero los fijos '
        'discontinuos sólo trabajan en los meses con eventos: aquí la temporada sale algo más barata y el invierno algo '
        'más caro que en la realidad',
    'El IVA del cuarto trimestre se liquida en enero del año siguiente, así que no aparece en este cuadro':
        'Los trimestres de esta hoja son de tres meses del plan (marzo-mayo, junio-agosto y septiembre-noviembre), no '
        'los naturales: con el Mes 1 en marzo, el modelo 303 se presenta en abril (por marzo), julio, octubre y enero '
        '(por octubre-diciembre, ya en el Mes 11). El IVA de la inversión se descuenta del que repercutes en las '
        'primeras liquidaciones',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 135, None,
        'Invitados de media por evento en el año 1; en la venta directa, cada taza vendida cuenta como un invitado. '
        'Sale de la mezcla de la tabla de referencias de la hoja de Instrucciones: bodas de 120, empresa de 80, '
        'congresos o ferias de 300 asistentes, celebraciones privadas de 50 y unas 250 tazas por jornada de venta '
        'directa. Es una media: la capacidad por evento está más abajo',
        'research §4 (mezcla 136,8, redondeada) [estimado]'),
    'ticket_medio': (
        None, None, 6.20, None,
        'SIN IVA, por invitado: el precio del servicio de barra (paquete de bebidas ilimitadas durante unas horas) '
        'repartido entre los invitados y, en la venta directa, el precio de cada taza. Media ponderada de la mezcla: '
        '9,00 € la boda, 8,00 € el evento de empresa, 4,50 € el asistente a un congreso, 9,50 € la celebración privada '
        'y 3,00 € la taza en la feria. Por eso la media baja. El precio con IVA (10 %) está en la fila de abajo',
        'calibrado D9, palanca 1 (bodas a 9,00 €; research: 8,50 €): mezcla 6,15 €, redondeada como en el research'),
    'crec_a2': (
        None, None, 0.10, None,
        'Más actividad el segundo año: empresas y agencias que repiten, bodas que llegan por recomendación y planners '
        'que ya te conocen, sobre un primer año con la agenda aún por llenar. El libro lo aplica a los invitados por '
        'evento con los mismos eventos; en euros es lo mismo que un 10 % más de eventos del mismo tamaño. El personal '
        'no sube con este porcentaje: crece con las incorporaciones de la hoja Personal',
        'calibrado D9 (research: 8 %; la demo §2.11.5 del motor no tiene ventana por debajo del 10 % con unos costes '
        'fijos de unos 66.000 €)'),
    'crec_a3': (
        None, None, 0.08, None,
        'Sobre el año 2. El techo lo ponen los sábados de temporada, el calendario de congresos y una sola barra con '
        'su titular: más allá hace falta una segunda estación',
        'calibrado D9 (research: 5 %; ver la nota del año 2)'),
    'dias_apertura': (
        None, None, 130, None,
        'Eventos servidos en el año: 30 bodas, 40 de empresa (presentaciones, jornadas, team building, Navidad), 22 '
        'jornadas de congreso o feria con stand de marca, 25 celebraciones privadas y rodajes, y 12 jornadas de venta '
        'directa en mercados y festivales (la mezcla suma 129; el plan redondea a 130). Es el MISMO dato para la '
        'cuenta de resultados, el punto de equilibrio, los escenarios y las horas de personal',
        'research §4 y §8 [estimado] · SPEC D5'),
    'pct_comida': (
        None, None, 0.11, None,
        'Dulces y bollería de obrador sobre las ventas; el 89 % restante son las bebidas de café y sin café. Es el '
        'peso de la primera línea de ventas del P&L',
        'calibrado D9 (research y SPEC D5: 10/90; la demo §2.11.9 del motor exige que un +5 % de coste de la comida '
        'mueva el coste de mercancía más de 0,5 puntos, y con el 10 % se queda justo en 0,5)'),
    'coste_comida': (
        None, None, 0.46, None,
        'Bollería y dulces comprados hechos a un obrador (cruasanes pequeños, galletas, bizcocho) sobre su venta: se '
        'sirven tal cual, sin elaborar nada en la base. Pide la ficha de alérgenos de cada pieza',
        'research §4 [estimado]'),
    'coste_bebida': (
        None, None, 0.16, None,
        'Café, leche, bebidas vegetales, cacao, chai y siropes sobre las ventas de bebida, con la merma (purga del '
        'molino, leche que sobra en la jarra) y un punto de catas y pruebas: unos 0,59 € por bebida. Es la MEDIA de la '
        'mezcla del año, no la receta de una bebida: el coste de un espresso o de un latte concreto está en la '
        'calculadora del kit y no se copia aquí. Los vasos y las tapas van en los consumibles',
        'research §3.b y §4 [cálculo] · SPEC D5'),
    'pct_consumibles': (
        None, None, 0.04, None,
        'Vasos, tapas, servilletas y palillos de madera (unos 0,12 € por bebida servida en vaso de un solo uso), hielo, '
        'filtros de agua, detergente de grupos y gasolina del generador. En bodas y empresa se sirve en loza (se lava en la '
        'base); el vaso de un solo uso, con su precio aparte en el tique (Ley 7/2022, art. 55.2), sólo en la venta '
        'directa',
        'research §0.4 y §4 [cálculo] · Ley 7/2022 (BOE)'),
    'pct_delivery': (
        None, None, 0.084, None,
        'Parte de las ventas que se hace en VENTA DIRECTA al público, en mercados gastronómicos, ferias y festivales: '
        '12 jornadas al año con unas 250 tazas a 3,00 € sin IVA. Va también al 10 %. En la vía pública es venta no '
        'sedentaria y necesita autorización municipal (RD 199/2010); en un recinto privado, contrato con el '
        'organizador. No es venta diaria en la calle: ese es otro negocio',
        'research §0.5 y §4 · SPEC D5 (canal del motor reutilizado)'),
    'comision_delivery': (
        None, None, 0.15, None,
        'Canon del organizador de la feria o del mercado, como porcentaje de lo que vendes allí. Si cobra una cuota '
        'fija por jornada o por emplazamiento, divídela entre lo que prevés vender: 110 € por una jornada de 750 € '
        'sin IVA son un 15 %',
        'research §3.a y §4 [estimado] · SPEC D5'),
    'comision_tpv': (
        None, None, 0.006, None,
        'Casi todo se cobra por transferencia (señales de los particulares y facturas de empresa); el datáfono queda '
        'para la venta directa',
        'research §4 [estimado]'),
    'alquiler_mes': (
        None, None, 400, None,
        'Cuota del almacén base: una nave o un garaje con fregadero y punto de agua donde se lavan la loza, las jarras '
        'y los depósitos, se guardan el café, la leche y los vasos, y duerme la furgoneta. No hay cocina ni se elabora '
        'comida; la casa o un trastero sin agua no sirven (RD 1021/2022, art. 13.5.b). Pide dos presupuestos en tu '
        'zona',
        'research §2 y §4 [estimado] · RD 1021/2022 art. 13.5.b (BOE, vía catering)'),
    'fianza_meses': (
        None, 'Fianza del almacén base (meses)', 2, None,
        'Dos cuotas de fianza, lo habitual en un alquiler de nave o garaje',
        'research §4 [estimado]'),
    'suministros_mes': (
        None, None, 60, None,
        'Teléfono, datos y luz del almacén base fuera de la cuota. La gasolina del generador va en los consumibles y '
        'el combustible de la furgoneta en varios, porque suben y bajan con los eventos',
        'research §4 [estimado]'),
    'seguros_ano': (
        None, None, 1300, None,
        'Responsabilidad civil de explotación y de producto de 300.000 a 600.000 € (unos 500 €), seguro de la '
        'furgoneta de uso comercial (650 €) y de los equipos que salen a cada evento (150 €)',
        'research §3.b y §4 [estimado]'),
    'pct_varios': (
        None, None, 0.04, None,
        'Combustible de los desplazamientos (2 puntos), imprevistos (1 punto) y escaparates de bodas y planners (1 '
        'punto). Es variable: sube y baja con los eventos. El desplazamiento que cobras aparte por kilómetro no está '
        'en las ventas del libro: compensa este gasto',
        'research §4 [estimado]'),
    'recursos_propios': (
        None, None, 25000, None,
        'Aportación del socio. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §4 y §8 [estimado]'),
    'prestamo': (
        None, None, 44500, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja '
        'de inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D9: cubre la necesidad de caja con 25.000 € propios (research: ≈ 41.000 €)'),
    'tipo_prestamo': (
        None, None, 0.065, None,
        'Tipo nominal anual de un préstamo de empresa sin garantía inmobiliaria. Pide oferta a dos entidades y a '
        'una línea ICO o ENISA antes de fijarlo',
        'research §4 [estimado] (= hermanos)'),
    'plazo_prestamo': (
        None, None, 6, None, 'Años totales, carencia incluida: la vida de la cafetera y del equipo',
        'research §4 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: es cuando la caja está más tensa, con la agenda de bodas y empresas aún por '
        'llenar. Desde el segundo año se devuelve el principal: mira la holgura de caja de ese año en el Punto de '
        'Equilibrio',
        'research §4 [estimado] · lección M3 del catering'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: cubren el valle de agosto y el de enero y febrero, y los 30-60 días que tardan en '
        'pagar empresas y agencias',
        'research §4 (= hermanos)'),
    'vida_obra': (
        None, None, 8, None,
        'La furgoneta, su rotulación y sus anclajes se amortizan en ocho años, el 12,5 % anual, por debajo del 16 % '
        'máximo para elementos de transporte de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades. '
        'Confírmalo con tu asesor',
        'research §4 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Cafetera, molinos, generador o baterías, depósitos y bomba, frío, barra-carro, carpa, menaje y TPV: el '
        'coeficiente máximo de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades es del 12 % para '
        'maquinaria y del 10 % para mobiliario',
        'research §4 · LIS art. 12.1'),
    'pct_bebida_alc': (
        None, 'Bebida ALCOHÓLICA sobre el total de bebida (a cero: no se sirve)', 0.0, None,
        'A CERO: la cafetería móvil del plan no sirve alcohol. Una barra de cócteles es otro negocio, con su propio '
        'plan. Con 0 esta celda no mueve nada',
        'SPEC D6'),
    'aforo': (
        None, 'Capacidad máxima por evento (invitados)', 350, None,
        'DATO INFORMATIVO: no entra en ningún cálculo. Es el evento más grande del caso con una cafetera de dos grupos '
        'y dos baristas cuando el servicio es largo (una jornada de congreso con pausas); en una barra de 3 horas esa '
        'cafetera llega a unos 180 invitados y por encima hace falta una segunda estación: mira la tabla de escalado '
        'de la hoja Instrucciones',
        'research §4 [estimado] · tabla de escalado (datos_escalado.py)'),
    'salario_convenio': (
        None, None, 0, None,
        'El VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería (art. 4) incluye la hostelería en '
        '«instalaciones fijas o móviles»: el barista se contrata como camarero/a. Copia aquí el salario base de esa '
        'categoría en la tabla de TU provincia. Con 0 el semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 y anexo (BOE)'),
    'meses_renta_previa': (
        None, 'Meses de cuota del almacén base ANTES del primer evento', 1, None,
        'Un mes de cuota para montar el almacén, calibrar la cafetera y los molinos y hacer las primeras catas antes '
        'de facturar',
        'research §4 [estimado]'),
    'pct_imprevistos': (
        None, 'Imprevistos sobre la compra y la preparación de la furgoneta (%)', 0.08, None,
        'Se calcula sobre la furgoneta y su rotulación: es donde aparecen las sorpresas (neumáticos, frenos, anclajes, '
        'y el informe y la ITV de la reforma si fijas en ella el mueble o los depósitos)',
        'research §2 y §4 (8 % sobre la furgoneta) [estimado] · SPEC D8'),
    'dias_cobro': (
        None, None, 20, None,
        'Media ponderada: los particulares (bodas y celebraciones) pagan el 30 % de señal al firmar y el 70 % siete '
        'días antes del evento, y la venta directa se cobra en el momento; las empresas, agencias y congresos, el 52 % '
        'de las ventas, pagan el 30 % al confirmar y el 70 % a 30 días de la factura (contrato y calculadora del kit). '
        'El libro no admite días negativos, así que las señales no se modelan: tu caja real será algo MEJOR que la de '
        'la hoja de Tesorería',
        'research §4 [derivado] · SPEC D16'),
    'dias_pago': (
        None, None, 30, None,
        'El tostador, los lácteos y los vasos, a 30 días: lo que te financian. Es lo primero que se pierde si te '
        'retrasas en un pago',
        'research §4 [estimado]'),
    'rampa_mes1': (
        None, None, 0.45, None,
        'Una cafetería móvil que arranca factura poco el primer mes: el café se contrata después que la finca y el '
        'catering, con uno a seis meses de antelación, y las empresas tardan en repetir. Con 100 % se elimina la rampa',
        'research §1 y §4 · SPEC D7'),
    'meses_rampa': (
        None, None, 9, None,
        'Nueve meses hasta el ritmo de crucero: la primera temporada de bodas, empresa y congresos',
        'research §4 · SPEC D7'),
    'mes_paga_1': (
        None, None, 5, None,
        'Mes de la TESORERÍA en el que sale la paga extra de verano: julio es el Mes 5, porque el Mes 1 del plan es '
        'marzo',
        'SPEC D7 (Mes 1 = marzo, injerto de la finca)'),
    'mes_paga_2': (
        None, None, 10, None,
        'Mes de la TESORERÍA en el que sale la paga extra de Navidad: diciembre es el Mes 10, porque el Mes 1 del '
        'plan es marzo',
        'SPEC D7 (Mes 1 = marzo, injerto de la finca)'),
    'iva_bebida': (
        None, 'IVA de la bebida ALCOHÓLICA servida (sin efecto en este plan)', 0.10, None,
        'Sin efecto: la cafetería no sirve alcohol (la celda de la bebida alcohólica está a cero). Todo lo que sirve, '
        'en la barra del evento o en la venta directa, va al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992)',
        'Ley 37/1992 art. 91.Uno.2.2.º (BOE) · SPEC D6'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente). Sin «eventos» ni «días» en el rótulo (formato de euro, §1.4).
LINEAS_INGRESO = (
    ('Dulces y bollería de obrador', 0.11, 'comida',
     'Bollería y dulces comprados a un obrador que se añaden al paquete de café o se venden en la feria: se sirven '
     'tal cual, sin elaborar. Al 10 % de IVA',
     'research §1 y §4 · SPEC D5'),
    ('Bebidas de café y sin café', 0.89, 'bebida',
     'Espresso, americano, cortado, café con leche, flat white, capuchino, latte, mocha, chai y chocolate, con leche '
     'entera, sin lactosa o bebida vegetal. Sin alcohol. Al 10 % de IVA, en la barra del evento y en la venta '
     'directa',
     'research §1 y §4 · SPEC D5 y D6'),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Las 4 filas del molde FT (con 3
#: o 5 hay «fórmulas perdidas»). SPEC D8: titular a jornada completa + camarero/a fijo discontinuo al 36 %; las otras
#: dos filas no pueden ir a 0 (el semáforo del SMI se pone rojo con 0 personas: `jornada or 1.0` en grupo_a), así que
#: son suplencias pequeñas, como permite la SPEC («o como suplencias si el molde lo exige»).
PLANTILLA = (
    ('Propietario/a — titular-barista, ventas y compras', 1, 1800,
     'Sirve en cada evento, conduce, vende a novios, empresas y agencias, compra el café y lleva la agenda. Como '
     'administrador de la SL cotiza en el régimen de autónomos: confirma con tu gestoría la cuota y si te aplica la '
     'reducida de inicio',
     'research §4 [estimado]', 1.0),
    ('Camarero/a de barra (barista), fijo discontinuo', 1, 504,
     'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) al 36 % de jornada en cómputo anual: '
     'segundo barista en bodas, congresos, la mitad de los eventos de empresa y la venta directa (unas 650 horas). '
     '«Barista» no es categoría del convenio: se contrata como camarero/a. Bruto a jornada completa: 1.400 € en 14 '
     'pagas',
     'research §4 [estimado] · ET art. 16 y ALEH VI (BOE)', 0.36),
    ('Suplencias de vacaciones y bajas (fijo discontinuo)', 1, 56,
     'Bolsa para cubrir las vacaciones y las bajas del camarero/a en temporada: unas 75 horas al año, mismo contrato '
     'y misma categoría. Nunca como autónomo que te factura: con tu horario y tu dirección es falso autónomo '
     '(art. 1.1 del Estatuto de los Trabajadores)',
     'SPEC D8 (fila que exige el molde) · ET arts. 1.1 y 16 (BOE)', 0.04),
    ('Refuerzo para eventos grandes (fijo discontinuo)', 1, 56,
     'Tercer barista para los congresos y las bodas de más de 200 invitados que pidan una segunda estación (tabla '
     'de escalado de la hoja Instrucciones): unas 75 horas al año. Por encima del SMI en proporción a su jornada',
     'SPEC D8 (fila que exige el molde) · ET art. 16 (BOE)', 0.04),
)

#: Cobertura: horas de trabajo por evento × personas a la vez × eventos al año, frente a las horas contratadas.
COBERTURA = {
    'horas_dia': 7.5,
    'personas_franja': 1.6,
    'nota_horas': 'Horas por evento y persona: carga en la base, viaje, llegada una hora antes, montaje, servicio, '
                  'desmontaje, limpieza y descarga. Un servicio «de 2 horas» es una jornada de 7 a 9 horas. La '
                  'oficina y la limpieza de la base van aparte',
    'nota_personas': 'Personas trabajando a la vez en un evento medio: dos baristas en bodas, congresos, ferias y la '
                     'mitad de los eventos de empresa, y el titular solo en los pequeños. Ajústalo y la hoja te dice '
                     'si llega la plantilla',
}

ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_caf.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-20
#: del molde; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = furgoneta, 8 años, base
#: de los imprevistos; el resto del equipo va con la maquinaria, 10 años).
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|cuota|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|'
           r'marca|web|foto|dossier|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|al[eé]rgenos|'
           r'formaci|seguro|licencia|permiso|tasa|iva',),
    'obra': (r'furgoneta|rotulaci|veh[ií]culo',),
    'maquinaria': (r'cafetera|molino|generador|bater[ií]a|energ[ií]a|dep[oó]sito|agua|fr[ií]o|nevera|barra|carro|'
                   r'carpa|menaje|loza|jarra|b[aá]scula|tpv|dat[aá]fono|software|uniforme',),
}

#: Costes fijos. Las partidas propias las escribe `semilla_caf.py` en las filas del molde; aquí, el rótulo de las
#: filas canónicas y las notas. Clave = rótulo normalizado (el canónico y el que trae el FT).
_NOTA_BASE = ('El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Es la cuota de una nave o '
              'un garaje con fregadero y punto de agua (lavado de loza, jarras y depósitos, almacén de café, leche y '
              'vasos, y plaza para la furgoneta). El mes previo al primer evento está en la hoja de Inversión y NO se '
              'cuenta dos veces')
FIJOS = {
    'alquiler del local': (None, _NOTA_BASE, 'Cuota del almacén base'),
    'aparcamiento y base del vehiculo': (None, _NOTA_BASE, 'Cuota del almacén base'),
    'suministros (luz, agua, gas)': (
        None, 'Teléfono, datos y luz del almacén base. La gasolina del generador va en los consumibles. Va al 21 % de '
              'IVA',
        'Suministros (teléfono, datos y luz del almacén base)'),
    'asesoria fiscal y laboral (nominas de fijos discontinuos)': (
        None, 'Contabilidad, impuestos de la SL y nóminas de los fijos discontinuos de cada mes con llamamientos'),
    'furgoneta: mantenimiento, neumaticos e itv': (
        None, 'Taller, neumáticos e ITV de la furgoneta (y del remolque, si lo usas)'),
    'marketing: escaparate de bodas, google ads local, redes y feria nupcial': (
        None, 'Ficha en los portales de bodas, Google Ads local, redes sociales y una feria nupcial al año'),
    'software de gestion comercial, crm y telefono': (
        None, 'Presupuestos, agenda de eventos, CRM de clientes y línea de teléfono'),
    'mantenimiento de la cafetera y los molinos (tecnico, juntas y filtros)': (
        None, 'Revisión anual del técnico, juntas y duchas de los grupos, fresas del molino y cartuchos del filtro '
              'descalcificador'),
    'uniformes y lavanderia': (
        None, 'Delantales, camisas y paños: lavado y reposición'),
    'gestion de residuos (posos de cafe y envases)': (
        None, 'Retirada de posos y envases al punto autorizado; el agua gris de los depósitos, nunca al terreno de la '
              'finca'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'Plan de prevención obligatorio (Ley 31/1995): quemaduras de vapor, cargas, conducción y posturas, y '
              'reconocimientos médicos'),
    'catas y degustaciones comerciales': (
        None, 'Café, leche y horas de las catas para novios, agencias y planners que no se cobran'),
    'licencias y tasas de venta en ferias y mercados': (
        None, 'Autorizaciones municipales de venta no sedentaria y tasas de ocupación de las jornadas de venta '
              'directa (RD 199/2010). Las tasas no llevan IVA. Pon las de tu ayuntamiento'),
}
FIJOS_EXTRA = ()

UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.65,
     'Los costes variables de la barra incluyen vasos, gasolina, combustible, canon de ferias y medios de pago además '
     'de la mercancía: un margen bruto por debajo del 65 % no paga la plantilla. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.22,
     'Techo de la mercancía (café, leche y bollería) sobre ventas. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.45,
     'Techo del personal sobre ventas: carga, viaje, montaje, servicio y limpieza en cada evento. Estimación del kit'),
    ('r_alquiler', 'Cuota del almacén base / Ventas', 0.06,
     'Techo de la cuota del almacén base sobre las ventas: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto para que el plan se sostenga: estimación del kit'),
)

#: (invitados por evento, precio por invitado sin IVA, eventos al año). SPEC D9 (eventos · invitados · precio:
#: 110 · 130 · 5,70 y 145 · 140 · 6,30).
ESCENARIOS = {
    'pesimista': (130, 5.70, 110),
    'optimista': (140, 6.30, 145),
}

#: Mes 1 = MARZO (SPEC D7, injerto de la finca). Calendario (research §4, ponderado por ventas): ene 4,3 · feb 6,8 ·
#: mar 8,1 · abr 8,9 · may 11,4 · jun 11,6 · jul 6,8 · ago 3,9 · sep 11,0 · oct 11,3 · nov 9,0 · dic 6,9. Rotada al
#: orden del motor (Mes 1…12).
ESTACIONALIDAD = (0.081, 0.089, 0.114, 0.116, 0.068, 0.039,
                  0.110, 0.113, 0.090, 0.069, 0.043, 0.068)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)


def _num(x, dec=0):
    """Número a la española (miles con punto, decimales con coma)."""
    t = ('{:,.%df}' % dec).format(x).replace(',', 'X').replace('.', ',').replace('X', '.')
    return t


def _referencias_escalado():
    """Filas de la tabla de escalado (SPEC D13) desde la FUENTE ÚNICA `plan-cafeteria-movil/datos_escalado.py`, la
    misma que usan la calculadora y el Word §6. Si el fichero no está, no se inventa: la tabla no sale."""
    ruta = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                        'plan-cafeteria-movil')
    if ruta not in sys.path:
        sys.path.insert(0, ruta)
    try:
        import datos_escalado as E
    except ImportError:
        return []
    filas = []
    beb = E.bebidas_por_invitado(E.HORAS_REF)
    for n, d in E.tabla_escalado():
        filas.append((
            'Escalado: barra de %d horas para %d invitados' % (E.HORAS_REF, n),
            '%d bebidas · %d barista%s · %d cafetera%s de dos grupos · %d molinos' % (
                d['bebidas'], d['baristas'], '' if d['baristas'] == 1 else 's', d['estaciones'],
                '' if d['estaciones'] == 1 else 's', d['molinos']),
            'Estimación del kit (ratios de EE. UU.)',
            '%s kg de café · %d l de leche · %d vasos desechables (o tazas de loza) · %s kW: %s · %d l de agua limpia. Con %s bebidas por invitado '
            '(barra de 2 a 4 horas); la calculadora lo hace con tus horas y tus invitados' % (
                _num(d['kg_cafe'], 1), d['l_leche'], d['vasos'], _num(d['kw'], 1),
                d['toma'][0].lower() + d['toma'][1:], d['agua'], _num(beb, 1))))
    tramos = ' · '.join('%s %s' % (nombre.replace(' (jornada)', '').lower(), rango)
                        for nombre, _h, _v, rango in E.BEBIDAS_POR_INVITADO if rango != 'mezcla del caso')
    filas.append((
        'Bebidas por invitado según las horas',
        tramos[0].upper() + tramos[1:],
        'Estimación del kit (ratios de EE. UU.)',
        'Por la mañana, un 20-30 % más; en una boda de noche, un 10 % menos. Un barista con dos grupos saca unas '
        '50-60 bebidas por hora y dos baristas, 100-120'))
    return filas


INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es MARZO: la cafetería arranca en primavera y llega al primer invierno con la caja de la '
        'temporada. El saldo mínimo del año nunca puede salir en rojo. Las señales de los particulares no se modelan: '
        'tu caja real será algo mejor.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El documento Word de este pack usa las cifras de este Excel; la calculadora de presupuestos y el modelo de '
        'contrato usan los mismos porcentajes de cobro y de cancelación, y la misma tabla de escalado. Si cambias una '
        'celda verde, el Excel manda. El coste de mercancía de Supuestos es la media de la mezcla con la merma: el de '
        'una bebida concreta está en la calculadora y no se copia aquí.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Marzo', 'Decisión del plan',
         'El café se reserva con uno a seis meses de antelación: se arranca en primavera, con la empresa y las '
         'comuniones, y enero y febrero (los meses más flojos) llegan con la caja de la temporada. La fila de '
         'estacionalidad de la Tesorería ya va girada'),
        ('Mezcla de eventos del plan',
         '130 eventos: 30 bodas, 40 de empresa, 22 jornadas de congreso o feria, 25 privados y 12 de venta directa',
         'Estimación del kit',
         'Bodas (30 × 120 invitados × 9,00 €), empresa (40 × 80 × 8,00 €), congresos (22 × 300 × 4,50 €), privados '
         'y rodajes (25 × 50 × 9,50 €) y venta directa (12 × 250 tazas × 3,00 €), sin IVA: 129 servicios y 108.575 €. '
         'El plan redondea a 130 eventos de 135 invitados a 6,20 €'),
    ] + _referencias_escalado() + [
        ('Electricidad de la barra', 'Cafetera de dos grupos: 2,4-4,5 kW · un enchufe de 16 A da unos 3,7 kW',
         'Ficha técnica de fabricante y cálculo (230 V × 16 A)',
         'Cafetera de 3,5 kW como máximo o toma dedicada; si no, generador inverter o baterías. El contrato del kit '
         'pide la toma por escrito'),
        ('Coste de una bebida', 'Unos 0,59 € de café, leche y siropes, más unos 0,12 € de vaso y tapa',
         'Calculadora del kit (estimación con precios de proveedor)',
         'Media de la mezcla de diez bebidas, con un doble de 16 g de café de especialidad a unos 22 €/kg y la merma. '
         'En loza sólo cuenta el producto. El coste de mercancía de Supuestos es la media del año con la merma'),
        ('Precios publicados de barras de café para bodas', 'Desde 295 € hasta 1.300 € por evento',
         'Fichas de proveedores en Bodas.net, consulta del 28-10-2026',
         'Precios «desde» de escaparate y sin desglose: sirven para situarte, no para copiarlos. Señal del 30-50 % y '
         'el resto antes del evento; hora extra de 37 a 50 €'),
        ('Cobro y cancelación del kit',
         'Particular: 30 % al firmar y 70 % siete días antes · Empresa: 30 % y 70 % a 30 días de la factura',
         'Contrato y calculadora del kit',
         'Cancelación en cuatro tramos (particular: 60, 30 y 7 días; empresa: 30, 15 y 7): se retiene el 10, el 30, el '
         '60 o el 100 % del precio, menos los costes que te ahorras; recíproca si cancelas tú. En la feria se cobra en '
         'el acto'),
        ('Canon de venta en ferias y mercados', '15 % de lo vendido en el caso', 'Supuesto del kit',
         'Hay organizadores que cobran un porcentaje y otros una cuota fija por jornada o emplazamiento: conviértela '
         'a porcentaje con tu previsión de ventas de la jornada'),
        ('IVA de lo que sirve la cafetería', '10 %', 'Ley 37/1992, art. 91.Uno.2.2.º',
         'En la barra del evento y en la venta directa. Los extras con precio propio (personalización, talleres de '
         'latte art, alquiler de la cafetera sin barista) van al 21 %'),
        ('Vasos de un solo uso', 'Precio aparte en el tique', 'Ley 7/2022, arts. 2.aa, 55.2 y 56',
         'El vaso de papel con forro de PE o PLA también es plástico. Las pajitas y los agitadores de plástico están '
         'prohibidos. En bodas y eventos de empresa, loza'),
        ('Comida testigo', 'Sólo si sirves salado', 'RD 1086/2020, arts. 2.h y 30.8-30.10',
         'Una ración de 100 g o más durante 7 días, en cada evento. Según nuestra lectura, las bebidas y la bollería '
         'servida tal cual quedan fuera, sin criterio oficial: confírmalo con tu autoridad sanitaria'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Incluye las «instalaciones fijas o móviles». El barista se contrata como camarero/a; copia tu tabla salarial '
         'en la celda de Supuestos'),
        ('Retención de IRPF en tus facturas', 'Ninguna', 'Reglamento del IRPF, art. 95.6',
         'El epígrafe 677.9 es una actividad empresarial: tus facturas a empresas no llevan retención'),
        ('Epígrafe del IAE', '677.9 (y 675 si vendes en mercados)', 'Tarifas del IAE (RDLeg 1175/1990)',
         'Elegir el epígrafe es criterio de asesoría: confírmalo con tu gestoría. Exento de cuota por debajo de 1 '
         'millón de euros de cifra de negocio'),
    ],
}

#: El checklist lo escribe `semilla_caf.py` entero (80 tareas): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto NUEVO (SPEC D3): sin cuadro de cambios frente a una versión anterior.
RECALIBRADO = ()
