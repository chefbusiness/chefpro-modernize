#!/usr/bin/env python3
"""
Contenido de `plan-catering-tematico-eventos` 2.0 para el grupo A (molde A-β).

El catering 1.x era de línea B (molde B-δ) con un modelo no financiable (L1-L16 de
`business-plans-en-4/F1-inventario-delta.md`). La 2.0 entra en la línea A: `semilla_cat.py` copia el libro del
Food Truck ES v2.2, le pone las partidas y los títulos del catering, y `main.py` + `grupo_a.py` lo reconstruyen con
este módulo. SPEC: `catering-es-2_0/SPEC-2_0.md` (D1-D12); caso: `catering-es-2_0/F1-research-es.md` §3.

MOTOR DE INGRESOS SIN PERMUTAR (SPEC D2)
---------------------------------------
    cubiertos_dia (B4) = INVITADOS POR EVENTO      65
    ticket_medio  (B5) = PRECIO POR INVITADO SIN IVA 53 €
    dias_apertura (B6) = EVENTOS AL AÑO             130
Ingresos = 65 × 53 × 130 = 447.850 € (año 1). La cobertura de personal (horas por evento × personas por evento ×
eventos) y la capacidad (aforo = invitados máximos por evento) salen bien sin tocar fórmulas. Los rótulos del oficio
van SIEMPRE por `VOCABULARIO` (con `VOCABULARIO_SIN_TILDES`): las demos de `grupo_a` buscan las filas por su rótulo
canónico pasado por el vocabulario, y un rótulo de driver cambiado con el 2.º campo de `SUPUESTOS` las deja ciegas
(«no se localizan las filas dias_sup», medido en F1).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §3» = `F1-research-es.md` §3 (casi todo
[estimado], criterio de kit, con la fuente que haya); «BOE» = norma leída el 11-oct-2026; «calibrado D15» = ajustado
en F2 para cumplir la regla de calibración de la SPEC.

⚠️ Rótulos de importe: sin «eventos», «invitados», «personas», «días», «mes» ni «clientes» (`motor.RX_RECUENTO` les
quita el formato de euro). Sesión Claude Code, 11-oct-2026.
"""

CONCEPTO = 'Catering Temático de Eventos'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Con tildes: requiere el opt-in de abajo.
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubiertos/día necesarios': 'invitados por evento necesarios',
    'cubiertos/día': 'invitados por evento',
    'cubiertos necesarios al día': 'invitados necesarios por evento',
    'cubiertos al día': 'invitados por evento',
    'cubiertos que tendría que sacar': 'invitados que tendría que atender',
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
    'en sala': 'en el servicio de catering',
    'servida en sala': 'servida en el evento',
    'ventas por delivery': 'ventas en drop-off (entrega sin servicio)',
    'comisión de la plataforma de delivery': 'comisión de la plataforma de drop-off',
    'comisiones de delivery': 'comisiones del drop-off',
    'delivery': 'drop-off',
    'alquiler mensual del local': 'cuota mensual de la cocina central',
    'alquiler de los meses previos a la apertura': 'cuota de la cocina central de los meses previos al arranque',
    'fianza del alquiler': 'fianza de la cocina central',
    'alquiler del local': 'cuota de la cocina central',
    'local y fijos': 'cocina central y fijos',
    'un local que acaba de abrir': 'un catering que acaba de arrancar',
    'un local que abre': 'un catering que arranca',
    'el local': 'la cocina central',
    'del local': 'de la cocina central',
    'tu local': 'tu cocina central',
    'arranque y aforo': 'arranque y capacidad',
    'suministros mensuales de luz, agua y gas': 'suministros mensuales (gas de las estaciones y consumos propios)',
    'en cada franja': 'en cada evento',
    # Ronda de arreglos (REVISION-FINAL m8/m9): restos de otros moldes en las frases del motor
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven': 'el alcohol que sale por drop-off mueve',
    'los alimentos —bollería y pastelería incluidas—, que son': 'los alimentos, que son',
    'refrescos o zumos con azúcares añadidos': 'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos',
    'imprevistos de obra y acondicionamiento': 'imprevistos de la compra y preparación de la furgoneta',
    'partidas de obra y acondicionamiento': 'partidas de la furgoneta',
    'de obra y licencias': 'de puesta en marcha (pruebas de menú y degustaciones)',
    'un banco no financia una reforma sin colchón': 'un banco no financia una compra así sin colchón',
    # REVISION-FINAL M1: el Word del pack 2.2 sí cita el payback; frase fija del motor (grupo_a.py:3766)
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
}

SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 65, None,
        'Invitados de media por evento en el año 1. Sale de la mezcla de cinco tipos de evento de la tabla de '
        'referencias de la hoja de Instrucciones: coffee breaks de 35, cócteles de empresa de 80, comidas de empresa '
        'de 100, bodas de 110 y celebraciones familiares de 45 invitados',
        'research §3 (mezcla 65,6 inv./evento, redondeada) [estimado]'),
    'ticket_medio': (
        None, None, 53.00, None,
        'SIN IVA. Media ponderada de la misma mezcla: 16 € el coffee break, 40 € el cóctel con estaciones, 62 € la '
        'comida de empresa, 98 € la boda y 48 € la celebración familiar. El precio con IVA (10 % en el catering con '
        'servicio) está en la fila «PVP equivalente con IVA» de abajo',
        'research §3 (mezcla 52,9 €, redondeada) [estimado]'),
    'crec_a2': (
        None, None, 0.12, None,
        'Más volumen el segundo año: repetición de empresas y bodas que llegan por recomendación. El libro lo aplica '
        'a los invitados por evento; en euros da lo mismo que hacer más eventos del mismo tamaño',
        'research §3 [estimado]'),
    'crec_a3': (
        None, None, 0.08, None, 'Sobre el año 2. Conservador: el techo lo pone la capacidad de la cocina central',
        'research §3 [estimado]'),
    'dias_apertura': (
        None, None, 130, None,
        'Eventos servidos en el año: 85 de empresa (coffee breaks, cócteles y comidas) y 45 de particulares (bodas, '
        'comuniones y cumpleaños). Es el MISMO dato para la cuenta de resultados, el punto de equilibrio, los '
        'escenarios y las horas de personal',
        'research §3 (35 % particulares / 65 % empresa por número de eventos) [estimado]'),
    'coste_comida': (
        None, None, 0.30, None,
        'Materia prima de la comida sobre las ventas de comida. Las estaciones en directo (sushi, parrilla, tacos) '
        'suben el coste por la merma de presentación: escandalla cada menú con la calculadora de este kit',
        'research §3 [estimado]'),
    'coste_bebida': (
        None, None, 0.28, None,
        'Bebida sobre las ventas de bebida: vino, cava, cerveza, refrescos y agua de la barra que sirves tú. Si el '
        'cliente pone la bebida y cobras descorche, esta línea baja',
        'research §3 [estimado]'),
    'pct_consumibles': (
        None, None, 0.03, None,
        'Desechables, gas de las estaciones, hielo, film y bolsas de vacío: todo lo que se gasta en cada evento y no '
        'se amortiza',
        'research §3 [estimado]'),
    'pct_delivery': (
        None, None, 0.05, None,
        'Parte de las ventas que se entrega SIN servicio (drop-off: bandejas de coffee break o de almuerzo que se '
        'dejan en la oficina). Es entrega de bienes: la comida va al 10 % y el alcohol y los refrescos, zumos y '
        'gaseosas con azúcares o edulcorantes añadidos, al 21 % (art. 91.Uno.1.1.º de la Ley 37/1992); el libro lo '
        'aplica al alcohol de esta parte',
        'SPEC D5 (canal del motor reutilizado como drop-off) · research §3 (coffee break ≈ 4 % de las ventas)'),
    'comision_delivery': (
        None, None, 0.10, None,
        'Comisión media de la parte del drop-off que entra por plataformas de catering para empresas o por '
        'intermediarios. Si todo el drop-off lo vendes tú, pon 0',
        'SPEC D5 · research §3 (10 % de comisión de intermediarios) [estimado]'),
    'comision_tpv': (
        None, None, 0.005, None,
        'Casi todo se cobra por transferencia (anticipos y facturas de empresa); el datáfono queda para la prueba de '
        'menú y los extras del día',
        'research §3 [estimado]'),
    'alquiler_mes': (
        None, None, 2000, None,
        'Cuota de una cocina central compartida y autorizada: unas 80 horas al mes de cocina, cámara, almacén y plaza '
        'para la furgoneta. Para eventos no se puede cocinar en casa (art. 13.5.b del RD 1021/2022), así que este '
        'coste no es opcional. No hay tarifa pública: pide dos presupuestos en tu zona',
        'research §3 [estimado] · RD 1021/2022 art. 13.5.b (BOE)'),
    'fianza_meses': (
        None, 'Fianza de la cocina central (meses)', 2, None,
        'Dos cuotas de fianza, lo habitual en un contrato de uso de cocina compartida',
        'research §3 [estimado]'),
    'suministros_mes': (
        None, None, 150, None,
        'Gas de las estaciones y consumos propios fuera de la cuota: la cocina compartida ya incluye luz y agua',
        'research §3 [estimado]'),
    'seguros_ano': (
        None, None, 2200, None,
        'Responsabilidad civil de explotación y de producto con cobertura de intoxicación alimentaria de al menos '
        '600.000 € (unos 900 €), seguro de la furgoneta de uso comercial (1.000 €) y de los equipos que salen a cada '
        'evento (300 €)',
        'research §3 [estimado]'),
    'pct_varios': (
        None, None, 0.05, None,
        'Combustible de la furgoneta, cánones que algunas fincas y wedding planners cobran al catering externo '
        '(unos 2 puntos) e imprevistos. Es variable: sube y baja con los eventos',
        'research §3 (varios 3 % + 20 % de ventas vía intermediarios × 10 % de canon) · SPEC D5'),
    'recursos_propios': (
        None, None, 35000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §3 [estimado]'),
    'prestamo': (
        None, None, 111000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja '
        'de inversión y te dice si sobra o falta: ajústalo con ese dato',
        'calibrado D15 (research: ≈ 105.000 €)'),
    'tipo_prestamo': (
        None, None, 0.065, None,
        'Tipo nominal anual de un préstamo de empresa sin garantía inmobiliaria. Pide oferta a dos entidades y a '
        'una línea ICO o ENISA antes de fijarlo',
        'research §3 [estimado] (= Food Truck ES)'),
    'plazo_prestamo': (
        None, None, 6, None, 'Años totales, carencia incluida: el plazo de vida de la furgoneta y del equipo',
        'research §3 [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: es cuando la caja está más tensa, con la cartera de bodas aún por llenar',
        'research §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: cubren los meses flojos (enero y agosto son los más bajos del año) y '
        'los 30-60 días que tardan en pagar las empresas',
        'molde (mínimo de la familia)'),
    'vida_obra': (
        None, None, 8, None,
        'En este plan la «obra» es la furgoneta frigorífica y su rotulación: ocho años son el 12,5 % anual, por '
        'debajo del 16 % máximo para elementos de transporte de la tabla del art. 12.1 de la Ley del Impuesto sobre '
        'Sociedades. Confírmalo con tu asesor',
        'research §3 · LIS art. 12.1'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Estaciones, equipo de producción, menaje, mobiliario y equipos informáticos: el coeficiente máximo de la '
        'tabla del art. 12.1 de la Ley del Impuesto sobre Sociedades es del 12 % para maquinaria y del 10 % para '
        'mobiliario',
        'research §3 · LIS art. 12.1'),
    'pct_bebida_alc': (
        None, None, 0.65, None,
        'Parte ALCOHÓLICA de la bebida (vino, cava, cerveza, barra). Reparte el IVA que soportas al comprarla (21 % '
        'el alcohol) y el que repercutes en el drop-off',
        'research §3 [estimado]'),
    'aforo': (
        None, 'Capacidad máxima por evento (invitados)', 250, None,
        'DATO INFORMATIVO: no entra en ningún cálculo. Es el evento más grande que puedes servir con el equipo y el '
        'menaje propios; por encima, se alquila menaje y se amplía la bolsa de personal',
        'research §3 [estimado]'),
    'salario_convenio': (
        None, None, 0, None,
        'El catering está dentro del convenio de hostelería (art. 4 del V Acuerdo Laboral de ámbito Estatal para el '
        'sector de Hostelería): copia aquí el salario base del grupo más bajo de la tabla de TU provincia. Con 0 el '
        'semáforo compara sólo contra el SMI',
        'ALEH V art. 4 (BOE)'),
    'meses_renta_previa': (
        None, 'Meses de cuota de la cocina central ANTES del primer evento', 1, None,
        'Un mes de cuota para montar la producción, hacer las pruebas de menú y las primeras degustaciones antes de '
        'facturar',
        'research §3 [estimado]'),
    'pct_imprevistos': (
        None, 'Imprevistos sobre la compra y la preparación de la furgoneta (%)', 0.08, None,
        'Se calcula sobre la furgoneta y su rotulación: es donde aparecen las sorpresas (reparación del equipo de '
        'frío, revisión del certificado ATP)',
        'research §3 (8 % sobre la furgoneta) [estimado]'),
    'dias_cobro': (
        None, None, 25, None,
        'Media ponderada: las empresas pagan a 30-60 días (máximo legal de 60, art. 4 de la Ley 3/2004) y los '
        'particulares pagan por adelantado. El libro no admite días negativos, así que los anticipos del 40 % de '
        'las bodas no se modelan: tu caja real será algo MEJOR que la de la hoja de Tesorería',
        'research §3 [derivado] · SPEC D6'),
    'dias_pago': (
        None, None, 30, None, 'Plazo de pago a proveedores de producto fresco y de menaje',
        'research §3 [estimado]'),
    'rampa_mes1': (
        None, None, 0.55, None,
        'Un catering que arranca factura poco el primer mes: las bodas se reservan con meses de antelación y las '
        'empresas tardan en repetir. Con 100 % se elimina la rampa',
        'molde · research §3'),
    'meses_rampa': (
        None, None, 6, None, 'Seis meses hasta el ritmo de crucero: una temporada de bodas',
        'molde · research §3'),
    'iva_bebida': (
        None, 'IVA de la bebida ALCOHÓLICA servida en el evento', 0.10, None,
        '10 %: el art. 91.Uno.2.2.º de la Ley 37/1992 grava al tipo reducido el «suministro de comidas y bebidas '
        'para consumir en el acto», sin excluir el alcohol, y un catering con servicio lo es. El libro aplica el '
        '21 % sólo al alcohol del drop-off, que no se sirve',
        'Ley 37/1992 art. 91.Uno.2.2.º (BOE) · SPEC D5'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente). Sin «eventos» ni «días» en el rótulo (formato de euro, §1.4).
LINEAS_INGRESO = (
    ('Ventas de comida (menús, estaciones temáticas en directo y coffee breaks)', 0.82, 'comida',
     'Menús de cóctel y banquete, estaciones de cocina del mundo en directo, bufés y coffee breaks. La prueba de '
     'menú se cobra y se descuenta del evento',
     'research §3 [estimado]'),
    ('Ventas de bebida (barra, vinos y refrescos servidos)', 0.18, 'bebida',
     'Barra libre por horas, vinos del menú, cava del brindis, refrescos y agua',
     'research §3 [estimado]'),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada).
PLANTILLA = (
    ('Propietario/a — chef ejecutivo, ventas y degustaciones', 1, 2000,
     'Diseña los menús y las estaciones, vende, hace las degustaciones y dirige los eventos grandes',
     'research §3 [estimado]', 1.0),
    ('Jefe/a de cocina de producción', 1, 1700,
     'Producción en la cocina central, compras, escandallos y control del plan APPCC',
     'research §3 [estimado]', 1.0),
    ('Ayudante de cocina y conductor/a', 1, 1400,
     'Producción, carga de la furgoneta, transporte y montaje',
     'research §3 [estimado]', 1.0),
    ('Equipo de evento: coordinador/a-maître, camareros, barra y cocineros de estación (fijos discontinuos)', 8,
     3642,
     'Ocho personas con contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) llamadas para cada '
     'evento: la coordinadora-maître a media jornada en cómputo anual (800 € brutos al mes) y siete camareros y '
     'cocineros de estación a unas 513 horas al año cada uno (1.400 € a jornada completa). Nunca como autónomos '
     'que te facturan: con horario y dirección tuyos es falso autónomo (art. 1.1 ET). Por encima del SMI en '
     'proporción a su jornada',
     'research §3 (coordinador 1 × 1.600 × 0,5 + equipo 7 × 1.400 × 0,29, en una fila: el molde FT tiene 4 filas '
     'de plantilla) · ET arts. 1.1 y 16 (BOE) · SPEC D6', 0.31625),
)

#: Cobertura: horas de trabajo por evento × personas a la vez × eventos al año, frente a las horas contratadas.
COBERTURA = {
    'horas_dia': 8,
    'personas_franja': 8,
    'nota_horas': 'Horas por evento y persona: carga, viaje, montaje, servicio, recogida y descarga. La producción en '
                  'la cocina central de los fijos va aparte',
    'nota_personas': 'Personas trabajando a la vez en un evento medio de 65 invitados: los tres fijos a jornada '
                     'completa, la coordinadora y cuatro extras. Una boda de 110 pide más: súbelo y la hoja te dice si llega la plantilla',
}

ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_cat.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-20
#: del molde; aquí sólo la clasificación para la amortización.
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|cuota|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|'
           r'marca|web|foto|dossier|lanzamiento|constituci|notar[ií]a|registro|declaraci|appcc|al[eé]rgenos|'
           r'formaci|seguro|licencia|permiso|tasa|iva',),
    'obra': (r'furgoneta|rotulaci',),
    'maquinaria': (r'contenedor|carro|equipo|estaci|chafing|exposit|menaje|vajilla|manteler|uniforme|mobiliario|'
                   r'software|tablet|dat[aá]fono',),
}

#: Costes fijos. Las partidas propias las escribe `semilla_cat.py` en las filas del molde; aquí, el rótulo de las
#: filas canónicas y las notas. Clave = rótulo normalizado (el canónico y el que trae el FT).
_NOTA_COCINA = ('El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Es el contrato de uso '
                'de una cocina central compartida y autorizada (cámara, almacén y plaza de la furgoneta). El mes '
                'previo al primer evento está en la hoja de Inversión y NO se cuenta dos veces')
FIJOS = {
    'alquiler del local': (None, _NOTA_COCINA, 'Cuota de la cocina central compartida'),
    'aparcamiento y base del vehiculo': (None, _NOTA_COCINA, 'Cuota de la cocina central compartida'),
    'suministros (luz, agua, gas)': (
        None, 'Gas de las estaciones y consumos fuera de la cuota de la cocina. Va al 21 % de IVA',
        'Suministros (gas de las estaciones y consumos propios)'),
    'asesoria fiscal y laboral (nominas de fijos discontinuos)': (
        None, 'Contabilidad, impuestos y nóminas de los fijos discontinuos de cada mes con llamamientos'),
    'furgoneta: mantenimiento, itv e inspeccion atp': (
        None, 'Taller, neumáticos, ITV y la inspección periódica del certificado ATP del equipo de frío (RD 237/2000)'),
    'marketing y publicidad': (
        None, 'Escaparates de bodas, Google Ads, dos ferias de novios al año y LinkedIn para empresas'),
    'software de gestion comercial, crm y telefono': (
        None, 'Presupuestos, agenda de eventos, CRM de clientes y línea de teléfono'),
    'lavanderia de manteleria y uniformes': (None, 'Lavado y planchado industrial después de cada evento'),
    'pruebas de menu y degustaciones comerciales': (
        None, 'Producto y horas de las pruebas de menú de bodas y de las degustaciones a empresas que no se cobran'),
    'gestion de residuos (organico, carton y aceite usado)': (
        None, 'Gestor autorizado, salvo que la cocina central lo incluya en la cuota'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'Plan de prevención obligatorio (Ley 31/1995) y reconocimientos médicos de la plantilla'),
    'reposicion de menaje y roturas': (
        None, 'Vajilla, copas y bandejas que se rompen o se pierden en los eventos. Estimación del kit'),
    'permisos y autorizaciones municipales': (
        None, 'Autorizaciones para eventos en espacios públicos y tasas que no repercutes al cliente. Estimación del '
              'kit: varía mucho por municipio'),
}
FIJOS_EXTRA = ()

UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.60,
     'En catering los costes variables incluyen desechables, combustible y cánones de fincas además de la '
     'mercancía: un margen bruto por debajo del 60 % no paga la plantilla'),
    ('r_cogs', 'Coste de mercancía / Ventas', 0.33,
     'Techo de la mercancía (comida y bebida) sobre ventas: estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.38,
     'El catering es intensivo en mano de obra (montaje, servicio y recogida): techo del 38 %, estimación del kit'),
    ('r_alquiler', 'Cocina central / Ventas', 0.07,
     'Techo de la cuota de la cocina central sobre las ventas: estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.04,
     'Suelo de resultado neto para que el plan se sostenga: estimación del kit'),
)

#: (invitados por evento, precio por invitado sin IVA, eventos al año).
ESCENARIOS = {
    'pesimista': (60, 50.00, 105),
    'optimista': (70, 57.00, 150),
}

#: Bodas de mayo a octubre, comuniones en mayo, Navidad de empresa en diciembre y agosto flojo.
ESTACIONALIDAD = (0.040, 0.055, 0.070, 0.075, 0.105, 0.120,
                  0.090, 0.050, 0.110, 0.100, 0.070, 0.115)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. El saldo mínimo del año nunca puede salir en rojo. Los anticipos de los particulares no se '
        'modelan: tu caja real será algo mejor.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El documento Word de este pack y la calculadora de precios usan las cifras de este Excel: si cambias '
        'una celda verde, el Excel manda.',
    ],
    'referencias': [
        ('Mezcla de eventos del plan', '130 eventos: 85 de empresa y 45 de particulares',
         'Estimación del kit',
         'Coffee breaks (35 eventos × 35 invitados × 16 €), cócteles (35 × 80 × 40 €), comidas de empresa '
         '(15 × 100 × 62 €), bodas (15 × 110 × 98 €) y celebraciones familiares (30 × 45 × 48 €), precios sin IVA'),
        ('Invitados por boda', '115', 'Bodas.net, Informe del Sector Nupcial 2026',
         'Parejas millennial; 118 en la generación Z. El plan usa 110'),
        ('Coste total medio de una boda', '25.183 €', 'Bodas.net, Informe del Sector Nupcial 2026',
         'Toda la boda, no sólo el banquete'),
        ('Coste de mercancía sobre ventas', '28-32 %', 'Estimación del kit',
         'El plan usa el 30 % en comida y el 28 % en bebida'),
        ('Coste de personal sobre ventas', '33-38 %', 'Estimación del kit',
         'Montaje, servicio y recogida: el catering es intensivo en mano de obra'),
        ('Personal de sala', '1 camarero por 10-12 invitados sentados; 1 por 20-25 en cóctel', 'Estimación del kit',
         'Para dimensionar la bolsa de fijos discontinuos y la cobertura de la hoja Personal'),
        ('Cuota de cocina central compartida', '1.500-2.500 €/mes', 'Estimación del kit (no hay tarifa pública)',
         'Con cámara, almacén y unas 80 horas al mes. Pide dos presupuestos'),
        ('Furgoneta frigorífica usada (2021-2022)', '18.000-22.000 €', 'Anuncios de segunda mano, octubre 2026',
         'Con el certificado ATP vigente (RD 237/2000)'),
        ('IVA del catering con servicio', '10 %', 'Ley 37/1992, art. 91.Uno.2.2.º',
         'Alcohol incluido. Drop-off de alcohol y servicios facturados aparte (mobiliario, carpas, decoración): '
         '21 %'),
        ('Plazo de pago de las empresas', 'Máximo 60 días', 'Ley 3/2004, art. 4',
         'El plan usa 25 días medios de cobro mezclando empresas y particulares'),
        ('Temperaturas de servicio', '≥ 63 °C en caliente; ≤ 4-8 °C en frío', 'RD 1086/2020, art. 30',
         'Redacción del RD 1021/2022. Las vigila tu plan APPCC en el transporte y en cada estación'),
        ('Convenio colectivo aplicable', 'Provincial de hostelería',
         'V Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Incluye el catering. Copia tu tabla salarial en la celda de Supuestos'),
    ],
}

#: El checklist lo escribe `semilla_cat.py` entero (82 tareas, SPEC D7): aquí no hay reemplazos.
CHECKLIST = {}

RECALIBRADO = (
    ('Modelo de ingresos', 'ingresos mensuales tecleados a mano, sin relación con eventos ni precios',
     'invitados por evento × precio por invitado × eventos al año, en la hoja de Supuestos',
     'Ahora cualquier cambio de precio o de volumen recalcula todo el libro'),
    ('Cocina', 'no había ninguna: el plan decía que no hacía falta local',
     'cuota de una cocina central compartida y autorizada',
     'Para eventos no se puede cocinar en casa (art. 13.5.b del RD 1021/2022)'),
    ('Personal de eventos', 'un porcentaje de personal subcontratado sobre las ventas',
     'plantilla con fijos discontinuos y Seguridad Social',
     'Las facturas de autónomo con horario y dirección del empresario son falso autónomo (art. 1.1 ET)'),
    ('Punto de equilibrio', 'sin amortización, sin sueldos fijos ni cocina',
     'con todos los costes fijos, en invitados por evento, en ingresos y en caja',
     'El anterior salía irrealmente bajo; éste es el que mira un banco'),
    ('Impuestos, caja y financiación', 'no había IVA, Impuesto de Sociedades, tesorería ni préstamo',
     'IVA al 10 %, Impuesto de Sociedades, tesorería de 12 meses y préstamo con su cuadro y su DSCR',
     'Es lo que pide cualquier entidad para estudiar la operación'),
)
