#!/usr/bin/env python3
"""
Contenido de `plan-negocio-parrillero-asador-eventos` 2.2 para el grupo A (molde A-β).

El parrillero 1.1 era de línea B (molde B-gamma): eventos y facturación tecleados, una cuenta de resultados con las
fórmulas desplazadas (margen bruto negativo en la caché), sin personal del titular, sin IVA, IS, préstamo ni
tesorería, y un equilibrio de 5,4 eventos al año. La 2.2 entra en la línea A con el camino del Paellero ES 2.2:
`parrillero-2_2/semilla_par.py` copia el libro del Food Truck ES v2.2, le pone las partidas y los títulos del
parrillero, y `main.py` + `grupo_a.py` lo reconstruyen con este módulo (clonado del del paellero). SPEC:
`parrillero-2_2/SPEC-2_2.md` (D1-D16); caso: `parrillero-2_2/F1-research-parrillero.md` §3.

MOTOR DE INGRESOS SIN PERMUTAR (SPEC D2)
---------------------------------------
    cubiertos_dia (B4) = INVITADOS POR EVENTO              80
    ticket_medio  (B5) = PRECIO POR INVITADO SIN IVA       25 €
    dias_apertura (B6) = EVENTOS AL AÑO                    95
Ingresos = 80 × 25 × 95 = 190.000 € (año 1, antes de la rampa). El crecimiento de los años 2 y 3 lo aplica el motor
a los invitados por evento, con los mismos eventos: así lo cuenta el docx (lección M2 del catering). Los rótulos del
oficio van SIEMPRE por `VOCABULARIO` (con `VOCABULARIO_SIN_TILDES`): las demos de `grupo_a` buscan las filas por su
rótulo canónico pasado por el vocabulario.

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §n» = `F1-research-parrillero.md` §n (casi
todo [estimado], criterio de kit, con la fuente que haya); «catering §1» = `catering-es-2_0/F1-research-es.md` §1;
«paellero §1» = `paellero-2_2/F1-research-paellero.md` §1; «BOE» = norma leída en F1; «calibrado D15» = ajustado en
F2 para cumplir la regla de calibración de la SPEC.

⚠️ Rótulos de importe: sin «eventos», «invitados», «personas», «días», «mes» ni «clientes» (`motor.RX_RECUENTO` les
quita el formato de euro). Sesión Claude Code, 12-oct-2026.
"""

CONCEPTO = 'Parrillero / Asador para Eventos'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Con tildes: requiere el opt-in de abajo.
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
    'en sala': 'en el servicio de parrilla',
    'servida en sala': 'servida en el evento',
    'ventas por delivery': 'ventas de asado para llevar (sin servicio)',
    'comisión de la plataforma de delivery': 'comisión de la plataforma de pedidos',
    'comisiones de delivery': 'comisiones del asado para llevar',
    'delivery': 'asado para llevar',
    'alquiler mensual del local': 'cuota mensual de la cocina de apoyo',
    'alquiler de los meses previos a la apertura': 'cuota de la cocina de apoyo de los meses previos al arranque',
    'fianza del alquiler': 'fianza de la cocina de apoyo',
    'alquiler del local': 'cuota de la cocina de apoyo',
    'local y fijos': 'cocina de apoyo y fijos',
    'un local que acaba de abrir': 'un negocio de parrilla para eventos que acaba de arrancar',
    'un local que abre': 'un negocio de parrilla para eventos que arranca',
    'el local': 'la cocina de apoyo',
    'del local': 'de la cocina de apoyo',
    'tu local': 'tu cocina de apoyo',
    'arranque y aforo': 'arranque y capacidad',
    'suministros mensuales de luz, agua y gas': 'suministros mensuales (consumos propios fuera de la cuota)',
    'en cada franja': 'en cada evento',
    # Lo que cazó la revisión del catering (m8/m9): restos de otros moldes en las frases del motor
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'el alcohol que sale en el asado para llevar mueve',
    'los alimentos —bollería y pastelería incluidas—, que son': 'los alimentos, que son',
    'refrescos o zumos con azúcares añadidos': 'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos',
    'imprevistos de obra y acondicionamiento': 'imprevistos de la compra y preparación de la furgoneta',
    'partidas de obra y acondicionamiento': 'partidas de la furgoneta',
    'de obra y licencias': 'de puesta en marcha (pruebas de menú y degustaciones)',
    'un banco no financia una reforma sin colchón': 'un banco no financia una compra así sin colchón',
    # SPEC D2 (REVISION-FINAL M1 del paellero): el Word del pack 2.2 sí cita el payback; frase fija del motor
    # (grupo_a.py:3766). La «versión 1.1» como versión ANTERIOR (cuadro de Instrucciones) es cierta y se deja.
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # REVISION-FINAL m8 del paellero: restos de otros moldes en las frases del motor
    'el pan común y las harinas panificables, al superreducido (art. 91.Dos.1.1.º':
        'la carpa o el mobiliario facturados aparte, al general (art. 90',
    'obra, instalaciones y acondicionamiento': 'furgoneta, rotulación e imprevistos',
    'de obra e instalaciones': 'de la furgoneta y su rotulación',
    'lo que se compra: obra, equipamiento': 'lo que se compra: furgoneta, equipamiento',
    'lo que se COMPRA (obra, equipamiento': 'lo que se COMPRA (furgoneta, equipamiento',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor.
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 80, None,
        'Invitados de media por evento en el año 1. Sale de la mezcla de cuatro tipos de evento de la tabla de '
        'referencias de la hoja de Instrucciones: bodas de 110, eventos de empresa de 70, celebraciones privadas de '
        '40 y fiestas o ferias de 300',
        'research §3 (mezcla 80,2 invitados/evento, redondeada) [estimado]'),
    'ticket_medio': (
        None, None, 25.00, None,
        'SIN IVA, por invitado. Media ponderada de la misma mezcla: 42 € la boda (entrantes, tres o cuatro cortes '
        'con vacuno madurado, guarniciones y postre a la brasa), 31 € el evento de empresa, 25 € la celebración '
        'privada y 10 € la chuletada o costillada de una fiesta. Por eso la media baja: no es el precio de una boda. '
        'El precio con IVA (10 % en un servicio de comidas) está en la fila «PVP equivalente con IVA» de abajo',
        'research §3 (mezcla 24,9 €, redondeada) [estimado]'),
    'crec_a2': (
        None, None, 0.08, None,
        'Más volumen el segundo año: empresas que repiten, bodas que llegan por recomendación y planners que ya te '
        'conocen. El libro lo aplica a los invitados por evento con los mismos eventos; en euros da lo mismo que '
        'hacer más eventos del mismo tamaño',
        'research §3 [estimado]'),
    'crec_a3': (
        None, None, 0.05, None,
        'Sobre el año 2. Conservador: el techo lo ponen los fines de semana de temporada y un solo parrillero titular',
        'research §3 [estimado]'),
    'dias_apertura': (
        None, None, 95, None,
        'Eventos servidos en el año: 12 bodas, 30 de empresa (comidas, team building, show cooking y Navidad), 45 '
        'celebraciones privadas (cumpleaños, comuniones, peñas, urbanizaciones) y 8 fiestas o ferias por encargo. Es '
        'el MISMO dato para la cuenta de resultados, el punto de equilibrio, los escenarios y las horas de personal',
        'research §3 [estimado]'),
    'pct_comida': (
        None, None, 0.88, None,
        'Comida (carne, entrantes, guarniciones y postre) sobre las ventas; el 12 % restante es el pack de bebida '
        '(cerveza, refrescos y vino) de las celebraciones privadas y de empresa. Es la suma de las líneas de comida '
        'del P&L',
        'research §3 · SPEC D4 (88/12)'),
    'coste_comida': (
        None, None, 0.32, None,
        'Materia prima de la comida sobre las ventas de comida: carne (350-450 g crudos por invitado con entrantes), '
        'achuras y embutido, verdura, pan, salsas y postre. El escandallo de la mezcla sale al 29,8 %; el plan suma '
        'dos puntos por la volatilidad del vacuno y las compras de seguridad. Escandalla cada evento con la '
        'calculadora de este kit',
        'research §2-§3 [estimado]'),
    'coste_bebida': (
        None, None, 0.30, None,
        'Bebida sobre las ventas de bebida: cerveza, refrescos, agua y vino del pack. Si el cliente pone la bebida, '
        'esta línea baja',
        'research §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.045, None,
        'Carbón, leña, pastillas de encendido, gas del plan B, papel de aluminio, desechables compostables y hielo: '
        'algo más de 1 € por invitado. Se gastan 0,7-1 kg de carbón por kg de carne cruda, y el carbón cuesta de 1,3 a '
        '2 € el kilo',
        'research §2 (carbón y leña) [estimado]'),
    'pct_delivery': (
        None, None, 0.05, None,
        'Parte de las ventas que se entrega SIN servicio: asado para llevar en bandejas (cordero, cochinillo, '
        'costillar), sin parrillero en el evento. Es entrega de bienes: la comida va al 10 % y el alcohol y los '
        'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos, al 21 % (art. 91.Uno.1.1.º de la Ley '
        '37/1992); el libro lo aplica al alcohol de esta parte',
        'SPEC D4 (canal del motor reutilizado, como el paellero)'),
    'comision_delivery': (
        None, None, 0.10, None,
        'Comisión media de la parte del asado para llevar que entra por plataformas de pedidos o intermediarios. Si '
        'todos los pedidos los vendes tú, pon 0',
        'SPEC D4 (research: 2 %; sube al 10 % del paellero porque la demo §2.11.5 del motor lo exige) [estimado]'),
    'comision_tpv': (
        None, None, 0.005, None,
        'Casi todo se cobra por transferencia (señales y facturas de empresas y ayuntamientos); el datáfono queda '
        'para los cobros del día del evento',
        'research §3 [estimado]'),
    'alquiler_mes': (
        None, None, 1000, None,
        'Cuota de una cocina de apoyo compartida y autorizada: unas 30 horas al mes de marinados, salmueras y '
        'porcionado, cámara para la carne y almacén de parrillas, carbón y remolque. La carne se asa en el evento, '
        'pero lo que se prepara antes no se puede hacer en casa (art. 13.5.b del RD 1021/2022). No hay tarifa '
        'pública: pide dos presupuestos en tu zona',
        'research §3 [estimado] · RD 1021/2022 art. 13.5.b (BOE, vía catering §1)'),
    'fianza_meses': (
        None, 'Fianza de la cocina de apoyo (meses)', 2, None,
        'Dos cuotas de fianza, lo habitual en un contrato de uso de cocina compartida',
        'research §3 [estimado]'),
    'suministros_mes': (
        None, None, 50, None,
        'Consumos propios fuera de la cuota de la cocina (datos móviles, luz del almacén). El carbón y el gas van en '
        'los consumibles, porque suben y bajan con los eventos',
        'research §3 [estimado]'),
    'seguros_ano': (
        None, None, 1950, None,
        'Responsabilidad civil de explotación con incendio (brasas y chispas sobre carpas, césped y pavimento) y de '
        'producto con intoxicación alimentaria de al menos 600.000 € (unos 750 €); seguro de la furgoneta de uso '
        'comercial (900 €), del remolque (150 €) y de los equipos que salen a cada evento (150 €). La cancelación por '
        'una prohibición de fuego no se asegura: va en la cláusula de fuerza mayor del contrato, con el plan B de gas',
        'research §1 y §3 [estimado]'),
    'pct_varios': (
        None, None, 0.05, None,
        'Combustible de la furgoneta y del remolque (2 puntos), imprevistos (1,5 puntos) y el canon que algunas '
        'fincas y wedding planners cobran al proveedor externo (1,5 puntos). Es variable: sube y baja con los eventos',
        'research §3 [estimado]'),
    'recursos_propios': (
        None, None, 22000, None,
        'Aportación del socio. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §3 [estimado]'),
    'prestamo': (
        None, None, 65400, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja '
        'de inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D15: cubre la necesidad de caja con 22.000 € propios (research: ≈ 62.000 €)'),
    'tipo_prestamo': (
        None, None, 0.065, None,
        'Tipo nominal anual de un préstamo de empresa sin garantía inmobiliaria. Pide oferta a dos entidades y a '
        'una línea ICO o ENISA antes de fijarlo',
        'research §3 [estimado] (= catering y paellero)'),
    'plazo_prestamo': (
        None, None, 6, None, 'Años totales, carencia incluida: el plazo de vida de la furgoneta y del equipo',
        'research §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: es cuando la caja está más tensa, con la agenda de bodas y empresas aún por '
        'llenar. Desde el segundo año se devuelve el principal: mira la holgura de caja de ese año en el Punto de '
        'Equilibrio',
        'research §3 [estimado] · lección M3 del catering'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: cubren el invierno (enero, febrero y noviembre son los meses más bajos del '
        'año) y los 30 días que tardan en pagar empresas y ayuntamientos',
        'molde (mínimo de la familia)'),
    'vida_obra': (
        None, None, 8, None,
        'La furgoneta frigorífica y su rotulación se amortizan en ocho años, el 12,5 % anual, por debajo del 16 % '
        'máximo para elementos de transporte de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades. '
        'Confírmalo con tu asesor',
        'research §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Remolque-parrilla, parrillas, cruces, ahumador, plan B de gas, equipos de frío, carpa, utensilios y equipos '
        'informáticos: el coeficiente máximo de la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades es del '
        '12 % para maquinaria y del 10 % para mobiliario',
        'research §3 · LIS art. 12.1'),
    'pct_bebida_alc': (
        None, None, 0.60, None,
        'Parte ALCOHÓLICA de la bebida (cerveza y vino del pack). Reparte el IVA que soportas al comprarla (21 % el '
        'alcohol) y el que repercutes en el asado para llevar',
        'research §3 [estimado]'),
    'aforo': (
        None, 'Capacidad máxima por evento (invitados)', 350, None,
        'DATO INFORMATIVO: no entra en ningún cálculo. Es el evento más grande que puedes servir con dos '
        'parrilleros, el remolque-parrilla, las dos parrillas móviles, los dos auxiliares y un tercero de tu bolsa de '
        'fijos discontinuos o de una ETT',
        'research §2-§3 (tabla de escalado) [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'El servicio de comidas para eventos está dentro del convenio de hostelería (art. 4 del V Acuerdo Laboral de '
        'ámbito Estatal para el sector de Hostelería): copia aquí el salario base del grupo más bajo de la tabla de '
        'TU provincia. Con 0 el semáforo compara sólo contra el SMI',
        'ALEH V art. 4 (BOE, vía catering §1)'),
    'meses_renta_previa': (
        None, 'Meses de cuota de la cocina de apoyo ANTES del primer evento', 1, None,
        'Un mes de cuota para montar el almacén, probar los marinados y hacer las primeras degustaciones antes de '
        'facturar',
        'research §3 [estimado]'),
    'pct_imprevistos': (
        None, 'Imprevistos sobre la compra y la preparación de la furgoneta (%)', 0.08, None,
        'Se calcula sobre la furgoneta y su rotulación: es donde aparecen las sorpresas (revisión del equipo de '
        'frío o del certificado ATP, anclajes de las botellas de gas y del carbón)',
        'research §3 (8 % sobre la furgoneta) [estimado]'),
    'dias_cobro': (
        None, None, 15, None,
        'Media ponderada: los particulares pagan el 30 % de señal al firmar, el 40 % siete días antes y el 30 % en '
        'las 48 horas siguientes al evento (contratos del kit); las empresas, a 30 días de la factura, y los '
        'ayuntamientos, a 30 días desde la conformidad (art. 198.4 de la Ley 9/2017). Empresas y fiestas son el 47 % '
        'de las ventas. El libro no admite días negativos, así que las señales no se modelan: tu caja real será '
        'algo MEJOR que la de la hoja de Tesorería',
        'research §3 [derivado] · LCSP art. 198.4 (BOE)'),
    'dias_pago': (
        None, None, 15, None,
        'Plazo de pago a proveedores: la carne fresca se paga a plazo corto (el carnicero, a 7-15 días); el carbón y '
        'los desechables, a 30 días',
        'research §3 [estimado]'),
    'rampa_mes1': (
        None, None, 0.55, None,
        'Un negocio de parrilla para eventos que arranca factura poco el primer mes: las bodas se reservan con meses '
        'de antelación y las empresas tardan en repetir. Con 100 % se elimina la rampa',
        'molde · research §3'),
    'meses_rampa': (
        None, None, 6, None, 'Seis meses hasta el ritmo de crucero: una temporada de bodas y eventos de empresa',
        'molde · research §3'),
    'iva_bebida': (
        None, 'IVA de la bebida ALCOHÓLICA servida en el evento', 0.10, None,
        '10 %: el art. 91.Uno.2.2.º de la Ley 37/1992 grava al tipo reducido el «suministro de comidas y bebidas '
        'para consumir en el acto», sin excluir el alcohol, y un servicio de parrilla en directo lo es. El libro '
        'aplica el 21 % sólo al alcohol del asado para llevar, que no se sirve',
        'Ley 37/1992 art. 91.Uno.2.2.º (BOE, vía catering §1) · SPEC D6'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente). Sin «eventos» ni «días» en el rótulo (formato de euro, §1.4).
LINEAS_INGRESO = (
    ('Ventas de comida (parrilla y asado en directo, entrantes y postre)', 0.88, 'comida',
     'Carne a la brasa cocinada en el evento, con show de fuego cuando se contrata, entrantes, guarniciones, pan, '
     'salsas y postre. Las fiestas son chuletada o costillada por invitado',
     'research §3 [estimado]'),
    ('Ventas de bebida (pack de cerveza, refrescos y vino)', 0.12, 'bebida',
     'Pack de bebida que contratan sobre todo las celebraciones privadas y las empresas; en las bodas y en las '
     'fiestas la bebida suele ponerla el cliente o el recinto',
     'research §3 [estimado]'),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Las 4 filas del molde FT.
PLANTILLA = (
    ('Propietario/a — parrillero titular, ventas y compras', 1, 1800,
     'Asa en cada evento, vende, compra la carne y lleva la agenda. Como administrador de la SL cotiza en el '
     'régimen de autónomos: confirma con tu gestoría la cuota y si te aplica la reducida de inicio',
     'research §3 [estimado]', 1.0),
    ('Segundo parrillero y ayudante (fijo discontinuo)', 1, 450,
     'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) al 30 % de jornada en cómputo anual: '
     'segunda parrilla en bodas, empresas y fiestas, y preparación en la cocina de apoyo. Bruto a jornada '
     'completa: 1.500 € en 14 pagas',
     'research §3 [estimado] · ET art. 16 (BOE)', 0.30),
    ('Auxiliar de parrilla y montaje (fijo discontinuo)', 1, 432,
     'Llamado para los eventos medianos y grandes: carga, montaje, brasa, emplatado de la carne y recogida. Bruto '
     'a jornada completa: 1.350 €. Nunca como autónomo que te factura: con tu horario y tu dirección es falso '
     'autónomo (art. 1.1 ET)',
     'research §3 [estimado] · ET arts. 1.1 y 16 (BOE)', 0.32),
    ('Auxiliar de servicio y emplatado (fijo discontinuo)', 1, 432,
     'Mismo contrato y mismas horas que el anterior: sirve, repone guarniciones y salsas y recoge. Por encima del '
     'SMI en proporción a su jornada',
     'research §3 [estimado] · ET art. 16 (BOE)', 0.32),
)

#: Cobertura: horas de trabajo por evento × personas a la vez × eventos al año, frente a las horas contratadas.
COBERTURA = {
    'horas_dia': 8,
    'personas_franja': 3,
    'nota_horas': 'Horas por evento y persona: carga, viaje, montaje, encendido de la brasa, cocción, servicio, '
                  'recogida de las cenizas y descarga. Los marinados y el porcionado en la cocina de apoyo van aparte',
    'nota_personas': 'Personas trabajando a la vez en un evento medio de 80 invitados: el parrillero titular, el '
                     'segundo parrillero y un auxiliar. En bodas y fiestas entran los dos auxiliares (y un tercero de '
                     'la bolsa o de una ETT si hace falta); en una celebración privada pequeña bastan dos personas: '
                     'ajústalo y la hoja te dice si llega la plantilla',
}

ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_par.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-20
#: del molde; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = furgoneta, 8 años,
#: base de los imprevistos; el remolque-parrilla es equipo de cocción y va con la maquinaria, 10 años).
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|cuota|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|'
           r'marca|web|foto|dossier|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|al[eé]rgenos|'
           r'formaci|seguro|licencia|permiso|tasa|iva',),
    'obra': (r'furgoneta|rotulaci',),
    'maquinaria': (r'remolque|parrilla|brasero|cruz|cruces|costillar|ahumador|plan b de gas|plancha|extintor|'
                   r'fr[ií]o|armario|isoterm|sonda|acumulador|carpa|mesa|lavamanos|cuchiller|b[aá]scula|'
                   r'uniforme|epi|software|tablet|dat[aá]fono',),
}

#: Costes fijos. Las partidas propias las escribe `semilla_par.py` en las filas del molde; aquí, el rótulo de las
#: filas canónicas y las notas. Clave = rótulo normalizado (el canónico y el que trae el FT).
_NOTA_COCINA = ('El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Es el contrato de uso '
                'de una cocina de apoyo compartida y autorizada (horas de cocina, cámara para la carne y almacén de '
                'parrillas, carbón y remolque). El mes previo al primer evento está en la hoja de Inversión y NO se '
                'cuenta dos veces')
FIJOS = {
    'alquiler del local': (None, _NOTA_COCINA, 'Cuota de la cocina de apoyo compartida'),
    'aparcamiento y base del vehiculo': (None, _NOTA_COCINA, 'Cuota de la cocina de apoyo compartida'),
    'suministros (luz, agua, gas)': (
        None, 'Consumos propios fuera de la cuota de la cocina. El carbón y el gas del plan B van en los consumibles. '
              'Va al 21 % de IVA',
        'Suministros (consumos propios fuera de la cuota)'),
    'asesoria fiscal y laboral (nominas de fijos discontinuos)': (
        None, 'Contabilidad, impuestos de la SL y nóminas de los fijos discontinuos de cada mes con llamamientos'),
    'furgoneta y remolque: mantenimiento, itv e inspeccion atp': (
        None, 'Taller, neumáticos, ITV de la furgoneta y del remolque y la inspección periódica del certificado ATP '
              'del equipo de frío (RD 237/2000)'),
    'marketing y publicidad': (
        None, 'Directorios de bodas, Google Ads local, redes sociales y una feria al año'),
    'software de gestion comercial, crm y telefono': (
        None, 'Presupuestos, agenda de eventos, CRM de clientes y línea de teléfono'),
    'mantenimiento de extintores y revision del gas': (
        None, 'Mantenimiento anual de los extintores por una empresa mantenedora y revisión de reguladores y tubos '
              'flexibles del plan B de gas. Estimación del kit'),
    'uniformes, epi y lavanderia': (
        None, 'Chaquetas, delantales de cuero, guantes térmicos y paños: lavado y reposición'),
    'gestion de residuos (cenizas, grasa y aceite)': (
        None, 'Retirada de cenizas frías y grasa, y gestor autorizado del aceite usado, salvo que la cocina de apoyo '
              'lo incluya en la cuota'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'Plan de prevención obligatorio (Ley 31/1995): quemaduras, humo, calor y cargas, y reconocimientos '
              'médicos de la plantilla'),
    'degustaciones comerciales y pruebas de menu': (
        None, 'Carne y horas de las pruebas de menú para novios y de las degustaciones a planners y empresas que no '
              'se cobran'),
    'afilado y reposicion de cuchilleria': (
        None, 'Afilado profesional periódico y reposición de cuchillos y tablas de corte'),
}
FIJOS_EXTRA = ()

UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.55,
     'Los costes variables de la parrilla incluyen carbón, leña, desechables, combustible y cánones de fincas '
     'además de la mercancía: un margen bruto por debajo del 55 % no paga la plantilla. Estimación del kit'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.34,
     'Techo de la mercancía (comida y bebida) sobre ventas: el vacuno es caro y su precio se mueve. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.36,
     'Techo del personal sobre ventas: montaje, brasa, servicio y recogida en cada evento. Estimación del kit'),
    ('r_alquiler', 'Cocina de apoyo / Ventas', 0.08,
     'Techo de la cuota de la cocina de apoyo sobre las ventas: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.04,
     'Suelo de resultado neto para que el plan se sostenga: estimación del kit'),
)

#: (invitados por evento, precio por invitado sin IVA, eventos al año).
ESCENARIOS = {
    'pesimista': (75, 23.00, 80),
    'optimista': (85, 26.00, 110),
}

#: Bodas y comuniones de mayo a octubre con el pico en septiembre, Navidad de empresa y cordero o cochinillo a la
#: cruz en diciembre; agosto pierde por el calor y la época de peligro de incendios; enero, febrero y noviembre flojos.
ESTACIONALIDAD = (0.025, 0.030, 0.050, 0.070, 0.120, 0.140,
                  0.110, 0.080, 0.150, 0.100, 0.045, 0.080)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. El saldo mínimo del año nunca puede salir en rojo. Las señales de los particulares (30 % al '
        'firmar y 40 % siete días antes) no se modelan: tu caja real será algo mejor.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El documento Word de este pack y la calculadora de presupuestos usan las cifras de este Excel: si cambias '
        'una celda verde, el Excel manda.',
    ],
    'referencias': [
        ('Mezcla de eventos del plan', '95 eventos: 12 bodas, 30 de empresa, 45 celebraciones privadas y 8 fiestas',
         'Estimación del kit',
         'Bodas (12 eventos × 110 invitados × 42 €), empresa (30 × 70 × 31 €), celebraciones privadas (45 × 40 × '
         '25 €) y fiestas o ferias por encargo (8 × 300 × 10 €), precios sin IVA. Media: 80 invitados a 25 €'),
        ('Barbacoa para eventos (directorio)', '18-30 € básica · 30-55 € completa · 55-90 € premium',
         'artistealo.com (estimación del directorio)', 'Por persona; el directorio no indica si lleva IVA'),
        ('Buffet de barbacoa en Madrid', '15,95-19,95 € + IVA por persona', 'Tarifa publicada de un proveedor (2026)',
         'Desde 50 personas, con 500 g de carne cruda por invitado, parrilleros y desechables; desplazamiento aparte'),
        ('Asado argentino para bodas', '40-100 € por invitado', 'Ficha de un proveedor en Bodas.net',
         'Entre 50 y 200 invitados, con el 50 % por adelantado'),
        ('Carne cruda por invitado', '350-450 g con entrantes · 500-600 g sin entrantes',
         'Calculadoras de asado y tarifas publicadas', 'Sin hueso, un 20 % menos; los niños, la mitad'),
        ('Escalado por evento', '1 parrilla de 120 cm y 1 parrillero por cada 60-80 invitados',
         'Estimación del kit (manual técnico y calculadora)',
         'Ayudante desde 40 invitados; con cortes servidos en mesa, 1 parrillero por cada 40-50'),
        ('Carbón por evento', '0,7-1 kg por kg de carne cruda', 'Estimación del kit',
         'Unos 0,3-0,45 kg por invitado; de 1,3 a 2 € el kilo de carbón o encina'),
        ('Plan B de gas si hay alerta de incendios', 'Una botella de menos de 15 kg por aparato',
         'RD 919/2006, art. 2.1.h',
         'Plancha o parrilla de piedra volcánica: así no es una instalación y la conectas tú, con regulador y tubo '
         'flexible en fecha'),
        ('IVA de un servicio de parrilla en el evento', '10 %', 'Ley 37/1992, art. 91.Uno.2.2.º',
         'Alcohol incluido. Asado para llevar: comida al 10 % y alcohol al 21 %'),
        ('Retención de IRPF en tus facturas', 'Ninguna', 'Reglamento del IRPF, art. 95.6',
         'El epígrafe 677.9 es una actividad empresarial: tus facturas a empresas no llevan retención'),
        ('Pago de los ayuntamientos', '30 días desde la conformidad', 'Ley 9/2017, art. 198.4',
         'Contrato menor de servicios por debajo de 15.000 € (art. 118), sin anticipo, y factura electrónica por '
         'FACe si eres SL (Ley 25/2013, art. 4)'),
        ('Temperaturas de la carne', '≤ 7 °C al recibirla · 70 °C en el centro al cocinarla · ≥ 63 °C en caliente',
         'Reglamento (CE) 853/2004 y RD 1086/2020, art. 30',
         'Despojos ≤ 3 °C, aves y preparados ≤ 4 °C y picada ≤ 2 °C; aves a 74 °C en el centro (recomendación de '
         'AESAN)'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'V Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_par.py` entero (83 tareas, SPEC D10): aquí no hay reemplazos.
CHECKLIST = {}

RECALIBRADO = (
    ('Modelo de ingresos', 'eventos y facturación tecleados, con una cuenta de resultados cuyas fórmulas no '
     'sumaban las filas correctas', 'invitados por evento × precio por invitado × eventos al año, en la hoja de '
     'Supuestos', 'Ahora cualquier cambio de precio o de volumen recalcula todo el libro'),
    ('Cocina', 'no había ninguna: la mise en place del día anterior no tenía sitio',
     'cuota de una cocina de apoyo compartida y autorizada',
     'Lo que se prepara para un evento no se puede hacer en casa (art. 13.5.b del RD 1021/2022)'),
    ('Personal', 'ayudantes subcontratados por jornada y ningún sueldo para el parrillero',
     'plantilla con el sueldo del titular, fijos discontinuos y Seguridad Social',
     'Las facturas de autónomo con horario y dirección del empresario son falso autónomo (art. 1.1 ET)'),
    ('Punto de equilibrio', '5,4 eventos al año, sin amortización, sueldos ni cocina',
     'con todos los costes fijos, en invitados por evento, en ingresos y en caja',
     'El anterior salía irrealmente bajo; éste es el que mira un banco'),
    ('Impuestos, caja y financiación', 'no había IVA, Impuesto de Sociedades, tesorería ni préstamo',
     'IVA al 10 %, Impuesto de Sociedades, tesorería de 12 meses y préstamo con su cuadro y su DSCR',
     'Es lo que pide cualquier entidad para estudiar la operación'),
)
