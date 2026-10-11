#!/usr/bin/env python3
"""
Contenido de `plan-negocio-paellero-eventos` 2.2 para el grupo A (molde A-β).

El paellero 1.x era de línea B (molde B-δ): sin personal, sin amortización, sin IVA, IS, préstamo ni tesorería, y
con un equilibrio de 10 eventos al año. La 2.2 entra en la línea A con el camino del Catering ES 2.2:
`paellero-2_2/semilla_pae.py` copia el libro del Food Truck ES v2.2, le pone las partidas y los títulos del paellero,
y `main.py` + `grupo_a.py` lo reconstruyen con este módulo (clonado del del catering). SPEC:
`paellero-2_2/SPEC-2_2.md` (D1-D16); caso: `paellero-2_2/F1-research-paellero.md` §3.

MOTOR DE INGRESOS SIN PERMUTAR (SPEC D2)
---------------------------------------
    cubiertos_dia (B4) = INVITADOS (RACIONES) POR EVENTO   94
    ticket_medio  (B5) = PRECIO POR INVITADO SIN IVA       16 €
    dias_apertura (B6) = EVENTOS AL AÑO                    105
Ingresos = 94 × 16 × 105 = 157.920 € (año 1). El crecimiento de los años 2 y 3 lo aplica el motor a las raciones
por evento, con los mismos eventos: así lo cuenta el docx (lección M2 del catering). Los rótulos del oficio van
SIEMPRE por `VOCABULARIO` (con `VOCABULARIO_SIN_TILDES`): las demos de `grupo_a` buscan las filas por su rótulo
canónico pasado por el vocabulario.

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §n» = `F1-research-paellero.md` §n (casi
todo [estimado], criterio de kit, con la fuente que haya); «catering §1» = `catering-es-2_0/F1-research-es.md` §1;
«BOE» = norma leída en F1; «calibrado D15» = ajustado en F2 para cumplir la regla de calibración de la SPEC.

⚠️ Rótulos de importe: sin «eventos», «invitados», «personas», «días», «mes» ni «clientes» (`motor.RX_RECUENTO` les
quita el formato de euro). Sesión Claude Code, 11-oct-2026.
"""

CONCEPTO = 'Paellero / Paella para Eventos'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Con tildes: requiere el opt-in de abajo.
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubiertos/día necesarios': 'invitados por evento necesarios',
    'cubiertos/día': 'invitados por evento',
    'cubiertos necesarios al día': 'invitados necesarios por evento',
    'cubiertos al día': 'invitados por evento',
    'cubiertos que tendría que sacar': 'raciones que tendría que servir',
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
    'en sala': 'en el servicio de paella',
    'servida en sala': 'servida en el evento',
    'ventas por delivery': 'ventas de paella para recoger (sin servicio)',
    'comisión de la plataforma de delivery': 'comisión de la plataforma de pedidos',
    'comisiones de delivery': 'comisiones de la paella para recoger',
    'delivery': 'paella para recoger',
    'alquiler mensual del local': 'cuota mensual de la cocina de apoyo',
    'alquiler de los meses previos a la apertura': 'cuota de la cocina de apoyo de los meses previos al arranque',
    'fianza del alquiler': 'fianza de la cocina de apoyo',
    'alquiler del local': 'cuota de la cocina de apoyo',
    'local y fijos': 'cocina de apoyo y fijos',
    'un local que acaba de abrir': 'un negocio de paellas que acaba de arrancar',
    'un local que abre': 'un negocio de paellas que arranca',
    'el local': 'la cocina de apoyo',
    'del local': 'de la cocina de apoyo',
    'tu local': 'tu cocina de apoyo',
    'arranque y aforo': 'arranque y capacidad',
    'suministros mensuales de luz, agua y gas': 'suministros mensuales (consumos propios fuera de la cuota)',
    'en cada franja': 'en cada evento',
    # Lo que cazó la revisión del catering (m8/m9): restos de otros moldes en las frases del motor
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'el alcohol que sale en la paella para recoger mueve',
    'los alimentos —bollería y pastelería incluidas—, que son': 'los alimentos, que son',
    'refrescos o zumos con azúcares añadidos': 'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos',
    'imprevistos de obra y acondicionamiento': 'imprevistos de la compra y preparación de la furgoneta',
    'partidas de obra y acondicionamiento': 'partidas de la furgoneta',
    'de obra y licencias': 'de puesta en marcha (pruebas de arroz y degustaciones)',
    'un banco no financia una reforma sin colchón': 'un banco no financia una compra así sin colchón',
    # REVISION-FINAL M1: el Word del pack 2.2 sí cita el payback; frase fija del motor (grupo_a.py:3766)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # La versión anterior del paellero es la 1.2 (Instrucciones, cuadro «qué ha cambiado»)
    'qué ha cambiado respecto de la versión 1.1': 'QUÉ HA CAMBIADO RESPECTO DE LA VERSIÓN 1.2',
    'v1.1': 'v1.2',
    # REVISION-FINAL m8: restos de otros moldes en las frases del motor
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
        None, None, 94, None,
        'Invitados (raciones) de media por evento en el año 1. Sale de la mezcla de cuatro tipos de evento de la '
        'tabla de referencias de la hoja de Instrucciones: bodas de 120, comidas de empresa de 70, fiestas privadas '
        'de 40 y fiestas populares de 400 raciones',
        'research §3 (mezcla 94,3 raciones/evento, redondeada) [estimado]'),
    'ticket_medio': (
        None, None, 16.00, None,
        'SIN IVA, por ración. Media ponderada de la misma mezcla: 28 € la boda (dos variedades y entrantes), 24 € la '
        'comida de empresa, 18 € la fiesta privada y 5 € la ración de una fiesta popular. Por eso la media baja: '
        'no es el precio de un menú de boda. El precio con IVA (10 % en un servicio de comidas) está en la fila '
        '«PVP equivalente con IVA» de abajo',
        'research §3 (mezcla 15,8 €, redondeada) [estimado]'),
    'crec_a2': (
        None, None, 0.10, None,
        'Más volumen el segundo año: repetición de empresas, peñas y comisiones de fiestas, y bodas que llegan por '
        'recomendación. El libro lo aplica a las raciones por evento con los mismos eventos; en euros da lo mismo '
        'que hacer más eventos del mismo tamaño',
        'research §3 [estimado]'),
    'crec_a3': (
        None, None, 0.06, None,
        'Sobre el año 2. Conservador: el techo lo ponen los fines de semana de temporada y un solo paellero titular',
        'research §3 [estimado]'),
    'dias_apertura': (
        None, None, 105, None,
        'Eventos servidos en el año: 15 bodas, 30 comidas de empresa, 50 fiestas privadas (cumpleaños, comuniones, '
        'peñas, urbanizaciones) y 10 fiestas populares. Es el MISMO dato para la cuenta de resultados, el punto de '
        'equilibrio, los escenarios y las horas de personal',
        'research §3 [estimado]'),
    'pct_comida': (
        None, None, 0.92, None,
        'Comida (paellas, entrantes y postre) sobre las ventas; el 8 % restante es el pack opcional de bebida. Es la '
        'suma de las líneas de comida del P&L',
        'research §3 · SPEC D4 (92/8)'),
    'coste_comida': (
        None, None, 0.28, None,
        'Materia prima de la comida sobre las ventas de comida: arroz, carne, marisco, verdura, caldo, azafrán, '
        'aceite, entrantes y pan. En las fiestas populares sube al 45 % (paella sola a precio de volumen); la media '
        'de la mezcla queda en el 28 %. Escandalla cada arroz con la calculadora de este kit',
        'research §2-§3 (food cost de la ración) [estimado]'),
    'coste_bebida': (
        None, None, 0.30, None,
        'Bebida sobre las ventas de bebida: el pack opcional de vino, cerveza, refrescos y agua. Si el cliente pone '
        'la bebida, esta línea baja',
        'research §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Gas, leña, desechables, hielo y papel: unos 45 € por evento. Una paellera de 90 cm gasta 1-1,5 kg de gas '
        'por cocción (propano de 35 kg a 78,80 € en julio de 2026, boletín del IDAE)',
        'research §2 (gas) [estimado]'),
    'pct_delivery': (
        None, None, 0.05, None,
        'Parte de las ventas que se entrega SIN servicio: paella para recoger o entregada en su paellera, sin '
        'paellero en el evento. Es entrega de bienes: la comida va al 10 % y el alcohol y los refrescos, zumos y '
        'gaseosas con azúcares o edulcorantes añadidos, al 21 % (art. 91.Uno.1.1.º de la Ley 37/1992); el libro lo '
        'aplica al alcohol de esta parte',
        'SPEC D6 (canal del motor reutilizado) · research §4 («paellas a domicilio», 1.900 búsquedas/mes)'),
    'comision_delivery': (
        None, None, 0.10, None,
        'Comisión media de la parte de la paella para recoger que entra por plataformas de pedidos o '
        'intermediarios. Si todos los pedidos los vendes tú, pon 0',
        'SPEC D6 (comisión > 0, como exige la demo del motor) [estimado]'),
    'comision_tpv': (
        None, None, 0.005, None,
        'Casi todo se cobra por transferencia (anticipos y facturas de empresas y ayuntamientos); el datáfono queda '
        'para los cobros del día del evento',
        'research §3 [estimado]'),
    'alquiler_mes': (
        None, None, 900, None,
        'Cuota de una cocina de apoyo compartida y autorizada: unas 35 horas al mes para caldos, sofritos y '
        'preparación, cámara frigorífica y almacén de paelleras y quemadores. La paella se cocina en el evento, pero '
        'lo que se prepara antes no se puede hacer en casa (art. 13.5.b del RD 1021/2022). No hay tarifa pública: '
        'pide dos presupuestos en tu zona',
        'research §3 [estimado] · RD 1021/2022 art. 13.5.b (BOE, vía catering §1)'),
    'fianza_meses': (
        None, 'Fianza de la cocina de apoyo (meses)', 2, None,
        'Dos cuotas de fianza, lo habitual en un contrato de uso de cocina compartida',
        'research §3 [estimado]'),
    'suministros_mes': (
        None, None, 50, None,
        'Consumos propios fuera de la cuota de la cocina (datos móviles, luz del almacén). El gas de las paellas va en '
        'los consumibles, porque sube y baja con los eventos',
        'research §3 [estimado]'),
    'seguros_ano': (
        None, None, 1750, None,
        'Responsabilidad civil de explotación con incendio y explosión (por el gas) y daños al recinto, y de '
        'producto con intoxicación alimentaria de al menos 600.000 € (unos 700 €); seguro de la furgoneta de uso '
        'comercial (900 €) y de los equipos que salen a cada evento (150 €). La cancelación por una prohibición de '
        'fuego no se asegura: va en la cláusula de fuerza mayor del contrato',
        'research §1 y §3 [estimado]'),
    'pct_varios': (
        None, None, 0.045, None,
        'Combustible de la furgoneta e imprevistos (3 puntos) y el canon que algunas fincas y wedding planners '
        'cobran al proveedor externo (1,5 puntos). Es variable: sube y baja con los eventos',
        'research §3 [estimado]'),
    'recursos_propios': (
        None, None, 20000, None,
        'Aportación del socio. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §3 [estimado]'),
    'prestamo': (
        None, None, 51600, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja '
        'de inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D15: cubre la necesidad de caja con 20.000 € propios (research: ≈ 49.000 €)'),
    'tipo_prestamo': (
        None, None, 0.065, None,
        'Tipo nominal anual de un préstamo de empresa sin garantía inmobiliaria. Pide oferta a dos entidades y a '
        'una línea ICO o ENISA antes de fijarlo',
        'research §3 [estimado] (= catering)'),
    'plazo_prestamo': (
        None, None, 6, None, 'Años totales, carencia incluida: el plazo de vida de la furgoneta y del equipo',
        'research §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: es cuando la caja está más tensa, con la agenda de bodas y fiestas aún por '
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
        'La furgoneta isoterma y su rotulación se amortizan en ocho años, el 12,5 % anual, por debajo '
        'del 16 % máximo para elementos de transporte de la tabla del art. 12.1 de la Ley del Impuesto sobre '
        'Sociedades. Confírmalo con tu asesor',
        'research §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Paelleras, quemadores, equipos de frío, carpa, utensilios y equipos informáticos: el coeficiente máximo de '
        'la tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades es del 12 % para maquinaria y del 10 % para '
        'mobiliario',
        'research §3 · LIS art. 12.1'),
    'pct_bebida_alc': (
        None, None, 0.50, None,
        'Parte ALCOHÓLICA de la bebida (vino y cerveza del pack). Reparte el IVA que soportas al comprarla (21 % el '
        'alcohol) y el que repercutes en la paella para recoger',
        'research §3 [estimado]'),
    'aforo': (
        None, 'Capacidad máxima por evento (invitados)', 500, None,
        'DATO INFORMATIVO: no entra en ningún cálculo. Es la fiesta más grande que puedes servir con dos paelleros, '
        'los dos auxiliares y tus paelleras (incluida la de 150 cm, de 90-120 raciones)',
        'research §3 · manual técnico 1.2, tabla 1 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'El servicio de comidas para eventos está dentro del convenio de hostelería (art. 4 del V Acuerdo Laboral de '
        'ámbito Estatal para el sector de Hostelería): copia aquí el salario base del grupo más bajo de la tabla de '
        'TU provincia. Con 0 el semáforo compara sólo contra el SMI',
        'ALEH V art. 4 (BOE, vía catering §1)'),
    'meses_renta_previa': (
        None, 'Meses de cuota de la cocina de apoyo ANTES del primer evento', 1, None,
        'Un mes de cuota para montar el almacén, probar los caldos y hacer las primeras degustaciones antes de '
        'facturar',
        'research §3 [estimado]'),
    'pct_imprevistos': (
        None, 'Imprevistos sobre la compra y la preparación de la furgoneta (%)', 0.08, None,
        'Se calcula sobre la furgoneta y su rotulación: es donde aparecen las sorpresas (revisión del equipo de '
        'frío o del certificado ATP, anclajes de las botellas de gas)',
        'research §3 (8 % sobre la furgoneta) [estimado]'),
    'dias_cobro': (
        None, None, 20, None,
        'Media ponderada: los particulares pagan el 30 % al firmar y el 70 % el día del evento (contratos del kit); '
        'las empresas, a 30 días de la factura, y los ayuntamientos, a 30 días desde la conformidad (art. 198.4 de '
        'la Ley 9/2017), unos 45 días en la práctica. Empresas y ayuntamientos son el 45 % de las ventas. El libro '
        'no admite días negativos, así que los anticipos no se modelan: tu caja real será algo MEJOR que la de la '
        'hoja de Tesorería',
        'research §3 [derivado] · LCSP art. 198.4 (BOE)'),
    'dias_pago': (
        None, None, 20, None,
        'Plazo de pago a proveedores: el marisco y la carne se pagan a plazo corto; el arroz y el gas, a 30 días',
        'research §3 [estimado]'),
    'rampa_mes1': (
        None, None, 0.55, None,
        'Un negocio de paellas que arranca factura poco el primer mes: las bodas se reservan con meses de antelación '
        'y las empresas y ayuntamientos tardan en repetir. Con 100 % se elimina la rampa',
        'molde · research §3'),
    'meses_rampa': (
        None, None, 6, None, 'Seis meses hasta el ritmo de crucero: una temporada de bodas y fiestas',
        'molde · research §3'),
    'iva_bebida': (
        None, 'IVA de la bebida ALCOHÓLICA servida en el evento', 0.10, None,
        '10 %: el art. 91.Uno.2.2.º de la Ley 37/1992 grava al tipo reducido el «suministro de comidas y bebidas '
        'para consumir en el acto», sin excluir el alcohol, y un servicio de paella en directo lo es. El libro aplica '
        'el 21 % sólo al alcohol de la paella para recoger, que no se sirve',
        'Ley 37/1992 art. 91.Uno.2.2.º (BOE, vía catering §1) · SPEC D6'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente). Sin «eventos» ni «días» en el rótulo (formato de euro, §1.4).
LINEAS_INGRESO = (
    ('Ventas de comida (paellas y arroces en directo, entrantes y postre)', 0.92, 'comida',
     'Paellas y arroces cocinados en el evento, con show cooking cuando se contrata, entrantes, pan, alioli y '
     'postre. Las fiestas populares son paella sola por ración',
     'research §3 [estimado]'),
    ('Ventas de bebida (pack opcional de vino, cerveza y refrescos)', 0.08, 'bebida',
     'Pack de bebida que algunos clientes contratan con la paella; en muchas fiestas la bebida la pone el cliente',
     'research §3 [estimado]'),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Las 4 filas del molde FT.
PLANTILLA = (
    ('Propietario/a — paellero titular, ventas y compras', 1, 1800,
     'Cocina en cada evento, vende, compra el producto y lleva la agenda. Como administrador de la SL cotiza en el '
     'régimen de autónomos: confirma con tu gestoría la cuota y si te aplica la reducida de inicio',
     'research §3 [estimado]', 1.0),
    ('Ayudante de cocina y 2.º paellero (fijo discontinuo)', 1, 943,
     'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) al 65 % de jornada en cómputo anual: '
     'caldos y preparación en la cocina de apoyo, montaje, fuegos y la segunda tanda de paelleras. Bruto a '
     'jornada completa: 1.450 € en 14 pagas',
     'research §3 [estimado] · ET art. 16 (BOE)', 0.65),
    ('Auxiliar de evento: montaje y caldo (fijo discontinuo)', 1, 108,
     'Llamado para las bodas y las fiestas populares (unas 140 horas al año). Bruto a jornada completa: 1.350 €. '
     'Nunca como autónomo que te factura: con tu horario y tu dirección es falso autónomo (art. 1.1 ET)',
     'research §3 [estimado] · ET arts. 1.1 y 16 (BOE)', 0.08),
    ('Auxiliar de evento: emplatado y servicio (fijo discontinuo)', 1, 108,
     'Mismo contrato y mismas horas que el anterior: sirve la paella, repone y recoge. Por encima del SMI en '
     'proporción a su jornada',
     'research §3 [estimado] · ET art. 16 (BOE)', 0.08),
)

#: Cobertura: horas de trabajo por evento × personas a la vez × eventos al año, frente a las horas contratadas.
COBERTURA = {
    'horas_dia': 8,
    'personas_franja': 2,
    'nota_horas': 'Horas por evento y persona: carga, viaje, montaje, encendido, cocción, servicio, recogida y '
                  'descarga. Los caldos y la preparación en la cocina de apoyo van aparte',
    'nota_personas': 'Personas trabajando a la vez en un evento medio de 94 raciones: el paellero titular y el '
                     'ayudante. En bodas y fiestas populares entran uno o dos auxiliares: súbelo y la hoja te dice '
                     'si llega la plantilla',
}

ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_pae.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-20
#: del molde; aquí sólo la clasificación para la amortización.
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|cuota|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|'
           r'marca|web|foto|dossier|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|al[eé]rgenos|'
           r'formaci|seguro|licencia|permiso|tasa|iva',),
    'obra': (r'furgoneta|rotulaci',),
    'maquinaria': (r'paellera|quemador|tr[ií]pode|gas y seguridad|regulador|extintor|nevera|sonda|carpa|'
                   r'mesa|lavamanos|utensilio|olla|cuchiller|b[aá]scula|uniforme|epi|software|tablet|dat[aá]fono',),
}

#: Costes fijos. Las partidas propias las escribe `semilla_pae.py` en las filas del molde; aquí, el rótulo de las
#: filas canónicas y las notas. Clave = rótulo normalizado (el canónico y el que trae el FT).
_NOTA_COCINA = ('El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Es el contrato de uso '
                'de una cocina de apoyo compartida y autorizada (horas de cocina, cámara y almacén de paelleras y '
                'quemadores). El mes previo al primer evento está en la hoja de Inversión y NO se cuenta dos veces')
FIJOS = {
    'alquiler del local': (None, _NOTA_COCINA, 'Cuota de la cocina de apoyo compartida'),
    'aparcamiento y base del vehiculo': (None, _NOTA_COCINA, 'Cuota de la cocina de apoyo compartida'),
    'suministros (luz, agua, gas)': (
        None, 'Consumos propios fuera de la cuota de la cocina. El gas de las paellas va en los consumibles. Va al '
              '21 % de IVA',
        'Suministros (consumos propios fuera de la cuota)'),
    'asesoria fiscal y laboral (nominas de fijos discontinuos)': (
        None, 'Contabilidad, impuestos de la SL y nóminas de los fijos discontinuos de cada mes con llamamientos'),
    'furgoneta: mantenimiento, itv e inspeccion atp': (
        None, 'Taller, neumáticos, ITV y la inspección periódica del certificado ATP del equipo de frío (RD 237/2000)'),
    'marketing y publicidad': (
        None, 'Google Ads local, un escaparate de bodas, redes sociales y una feria al año'),
    'software de gestion comercial, crm y telefono': (
        None, 'Presupuestos, agenda de eventos, CRM de clientes y línea de teléfono'),
    'revision de gas por instaladora y mantenimiento de extintores': (
        None, 'Revisión de reguladores, flexibles y quemadores por una empresa instaladora de gas y mantenimiento '
              'anual de los extintores por una empresa mantenedora. Estimación del kit'),
    'uniformes y lavanderia': (None, 'Chaquetas, delantales y paños: lavado y reposición'),
    'gestion de residuos (organico y aceite usado)': (
        None, 'Gestor autorizado del aceite usado, salvo que la cocina de apoyo lo incluya en la cuota'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'Plan de prevención obligatorio (Ley 31/1995): quemaduras, gas, calor y cargas, y reconocimientos '
              'médicos de la plantilla'),
    'pruebas de arroz y degustaciones comerciales': (
        None, 'Producto y horas de las pruebas para novios y de las degustaciones a empresas y comisiones de fiestas '
              'que no se cobran'),
    'permisos y autorizaciones municipales': (
        None, 'Autorizaciones de ocupación de la vía pública o de uso del fuego y tasas que no repercutes al '
              'cliente. Estimación del kit: varía mucho por municipio'),
}
FIJOS_EXTRA = ()

UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.60,
     'Los costes variables de la paella incluyen gas, desechables, combustible y cánones de fincas además de la '
     'mercancía: un margen bruto por debajo del 60 % no paga la plantilla'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.32,
     'Techo de la mercancía (comida y bebida) sobre ventas: estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'Techo del personal sobre ventas: montaje, cocción, servicio y recogida en cada evento. Estimación del kit'),
    ('r_alquiler', 'Cocina de apoyo / Ventas', 0.08,
     'Techo de la cuota de la cocina de apoyo sobre las ventas: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.04,
     'Suelo de resultado neto para que el plan se sostenga: estimación del kit'),
)

#: (invitados por evento, precio por invitado sin IVA, eventos al año).
ESCENARIOS = {
    'pesimista': (85, 15.00, 85),
    'optimista': (100, 17.00, 125),
}

#: Bodas y comuniones de mayo a octubre, fiestas patronales en agosto y septiembre, Navidad de empresa en
#: diciembre; enero, febrero y noviembre son los meses flojos.
ESTACIONALIDAD = (0.030, 0.035, 0.060, 0.070, 0.110, 0.130,
                  0.120, 0.120, 0.130, 0.090, 0.040, 0.065)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. El saldo mínimo del año nunca puede salir en rojo. Los anticipos de los particulares (30 % al '
        'firmar) no se modelan: tu caja real será algo mejor.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El documento Word de este pack y la calculadora de precios usan las cifras de este Excel: si cambias '
        'una celda verde, el Excel manda.',
    ],
    'referencias': [
        ('Mezcla de eventos del plan', '105 eventos: 15 bodas, 30 de empresa, 50 fiestas privadas y 10 populares',
         'Estimación del kit',
         'Bodas (15 eventos × 120 raciones × 28 €), comidas de empresa (30 × 70 × 24 €), fiestas privadas '
         '(50 × 40 × 18 €) y fiestas populares (10 × 400 × 5 €), precios sin IVA. Media: 94 raciones a 16 €'),
        ('Fiesta popular contratada por un ayuntamiento', '400 raciones por 1.480 €',
         'Plataforma de Contratación del Sector Público (contrato menor de Sayalonga, 2025)',
         'Paella mixta con menaje, pan y servicio: unos 3,70 € por ración'),
        ('Paella sola para grupos', '11-14 € por persona', 'Tarifa publicada de un proveedor de Cataluña (2026)',
         '14 € de 30 a 49 personas, 12 € de 50 a 99 y 11 € a partir de 100; desplazamiento aparte'),
        ('Paella en directo con experiencia', '20-39 € por persona', 'Fichas de proveedores en plataformas de eventos',
         'Con show cooking y mínimo de servicio'),
        ('Raciones por paellera', '90 cm: 30-40 · 120 cm: 60-80 · 150 cm: 90-120',
         'Manual técnico de este kit (cartas de capacidad de los fabricantes)',
         '100 g de arroz por ración de evento'),
        ('Personal por evento', '1 paellero hasta 3 paelleras; ayudante desde 4 paelleras u 80 invitados',
         'Manual técnico de este kit', 'Segundo paellero a partir de unos 150 invitados'),
        ('Coste de mercancía sobre ventas', '25-28 % con entrantes; 45 % en fiestas populares', 'Estimación del kit',
         'El plan usa el 28 % en comida y el 30 % en bebida'),
        ('Gas por evento de 100 invitados', '4-6 kg de propano (10-15 €)', 'Boletín de precios del IDAE, julio de 2026',
         'Propano de 35 kg a 78,80 € (≈ 2,25 €/kg); 1-1,5 kg por paellera de 90 cm'),
        ('Botellas de gas', 'Una botella de menos de 15 kg por quemador', 'RD 919/2006, art. 2.1.h',
         'Así no es una instalación y la conectas tú, con regulador y tubo flexible en fecha. Con botellas de '
         '35 kg o varias conectadas, la monta una empresa instaladora (ITC-ICG 06)'),
        ('IVA de un servicio de paella en el evento', '10 %', 'Ley 37/1992, art. 91.Uno.2.2.º',
         'Alcohol incluido. Paella para recoger: comida al 10 % y alcohol al 21 %'),
        ('Pago de los ayuntamientos', '30 días desde la conformidad', 'Ley 9/2017, art. 198.4',
         'Contrato menor de servicios por debajo de 15.000 € (art. 118) y factura electrónica por FACe si eres SL '
         '(Ley 25/2013, art. 4)'),
        ('Temperaturas de servicio', '≥ 63 °C en caliente', 'RD 1086/2020, art. 30',
         'Nunca arroz tibio a temperatura ambiente (Bacillus cereus): sírvelo recién hecho o enfríalo de 60 a 10 °C '
         'en menos de 2 horas'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'V Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_pae.py` entero (83 tareas, SPEC D10): aquí no hay reemplazos.
CHECKLIST = {}

RECALIBRADO = (
    ('Modelo de ingresos', 'eventos y tickets medios tecleados, con un margen neto irreal (la mitad de las ventas)',
     'invitados (raciones) por evento × precio por invitado × eventos al año, en la hoja de Supuestos',
     'Ahora cualquier cambio de precio o de volumen recalcula todo el libro'),
    ('Cocina', 'no había ninguna: la mise en place se hacía en casa',
     'cuota de una cocina de apoyo compartida y autorizada',
     'Lo que se prepara para un evento no se puede hacer en casa (art. 13.5.b del RD 1021/2022)'),
    ('Personal', 'un 12 % de ayudantes subcontratados sobre las ventas y ningún sueldo para el paellero',
     'plantilla con el sueldo del titular, fijos discontinuos y Seguridad Social',
     'Las facturas de autónomo con horario y dirección del empresario son falso autónomo (art. 1.1 ET)'),
    ('Punto de equilibrio', '10 eventos al año, sin amortización, sueldos ni cocina',
     'con todos los costes fijos, en invitados por evento, en ingresos y en caja',
     'El anterior salía irrealmente bajo; éste es el que mira un banco'),
    ('Impuestos, caja y financiación', 'no había IVA, Impuesto de Sociedades, tesorería ni préstamo',
     'IVA al 10 %, Impuesto de Sociedades, tesorería de 12 meses y préstamo con su cuadro y su DSCR',
     'Es lo que pide cualquier entidad para estudiar la operación'),
)
