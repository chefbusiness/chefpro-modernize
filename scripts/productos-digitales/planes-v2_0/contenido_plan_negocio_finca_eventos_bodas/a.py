#!/usr/bin/env python3
"""
Contenido de `plan-negocio-finca-eventos-bodas` 1.0 para el grupo A (molde A-β).

Producto NUEVO de la familia Planes (sin versión anterior). Contenido clonado del Parrillero ES 2.2 (motor de eventos)
con los injertos de local fijo de la Heladería ES 1.0, sobre la semilla de la Panadería ES 2.2:
`plan-finca-eventos/semilla_fin.py` copia los dos xlsx publicados de la panadería (solo lectura), les pone las 19
partidas, los 10 fijos y los títulos de la finca, y `main.py` + `grupo_a.py` los reconstruyen con este módulo.
SPEC: `plan-finca-eventos/SPEC.md` (D1-D14); cómo: `F1-camino.md` §2; caso: `F1-research-finca.md` §3; normativa: §1.

MODELO (SPEC D2): finca ARRENDADA con edificaciones existentes + CATERING EXCLUSIVO CONCESIONADO que paga canon. La
finca factura el espacio y los servicios; el catering factura el menú y la barra a los novios y paga a la finca un
canon. Dos líneas, las dos al 21 % de IVA (SPEC D4): espacio y servicios (`comida`, 78 %) y canon (`bebida`, 22 %).

MOTOR DE INGRESOS SIN PERMUTAR (como parrillero, paellero y catering ES)
------------------------------------------------------------------------
    cubiertos_dia (B4) = INVITADOS POR EVENTO (media)       82
    ticket_medio  (B5) = € POR INVITADO SIN IVA             37 €  (espacio y servicios + canon)
    dias_apertura (B6) = EVENTOS AL AÑO                     120
Ventas = 82 × 37 × 120 = 364.080 €. El crecimiento de los años 2 y 3 (8 % y 5 %) lo aplica el motor a B4 (invitados
por evento). Se descartó permutar B4 y B6 (catering-es-2_0/F1-camino-2_0.md:44): la cobertura de personal multiplica
por B6 y dejaría de contar eventos. En euros es lo mismo; la nota de la celda lo traduce a eventos (F2-NOTAS §2).

ORIGEN DE CADA CIFRA (sexto campo de cada tupla, no se imprime): «research §n» = `F1-research-finca.md` §n (casi todo
[estimado], criterio de kit, con el cálculo a la vista); «BOE» = norma leída en origen en la F1; «calibrado D9» =
ajustado en F2 para cumplir los gates del caso de la SPEC.

⚠️ Rótulos de importe: sin «eventos», «invitados», «personas», «días», «meses», «plazas» ni «unidades»
(`motor.RX_RECUENTO` les quita el formato de euro). Las notas no usan «sala», «cubierto», «comensal», «ticket» ni
«local»: el VOCABULARIO los traduciría. Sesión Claude Code, 25-oct-2026.
"""

CONCEPTO = 'Finca de Eventos y Bodas'

#: Rótulos del oficio sobre las frases del motor (grupo_a.vocabulario, M9). Femenino «la finca»: concordancias medidas
#: con `plan-finca-eventos/barrido_es.py`. Las frases largas arreglan restos de otros moldes que el motor escribe.
VOCABULARIO_SIN_TILDES = True
VOCABULARIO = {
    'cubiertos/día necesarios': 'invitados por evento necesarios',
    'cubiertos/día': 'invitados por evento',
    'cubiertos necesarios al día': 'invitados necesarios por evento',
    'cubiertos al día': 'invitados por evento',
    'cubiertos que tendría que sacar': 'invitados que tendría que recibir',
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
    'en barra y sala': 'en la finca',
    'servida en sala': 'servida en el evento',
    'en sala': 'en la finca',
    'ventas por delivery': 'ventas que llegan por wedding planners y agencias',
    'comisión de la plataforma de delivery': 'comisión de los wedding planners y agencias',
    'comisiones de delivery': 'comisiones de wedding planners y agencias',
    'delivery': 'intermediarios',
    'alquiler mensual del local': 'renta mensual de la finca',
    'alquiler de los meses previos a la apertura': 'renta de la finca durante la obra',
    'fianza del alquiler': 'fianza del arrendamiento',
    'alquiler del local': 'renta de la finca',
    'local y fijos': 'finca y fijos',
    'un local que acaba de abrir': 'una finca que acaba de abrir',
    'un local que abre': 'una finca que abre',
    'el local': 'la finca',
    'del local': 'de la finca',
    'tu local': 'tu finca',
    'al local': 'a la finca',
    'suministros mensuales de luz, agua y gas': 'suministros mensuales (luz, agua, gasoil y teléfono)',
    'en cada franja': 'en cada evento',
    'Horas de producción al día ANTES de abrir': 'Horas de estructura por evento, fuera del día del evento',
    # mezcla y coste de las dos líneas: «comida» = espacio y servicios, «bebida» = canon (SPEC D4)
    'MIX Y COSTE DE MERCANCÍA': 'MEZCLA DE VENTAS Y COSTE DIRECTO',
    'Ventas de COMIDA sobre el total': 'Ventas de ESPACIO Y SERVICIOS sobre el total',
    'Ventas de BEBIDA sobre el total': 'Ventas del CANON DEL CATERING sobre el total',
    'Peso de la COMIDA sobre el total de ventas': 'Peso del ESPACIO Y LOS SERVICIOS sobre el total de ventas',
    'comida + bebida = 100': 'espacio y servicios + canon = 100',
    'Coste de mercancía sobre las ventas de COMIDA': 'Coste directo del evento sobre las ventas de ESPACIO Y SERVICIOS',
    'Coste de mercancía sobre las ventas de BEBIDA': 'Coste del canon sobre las ventas del CANON',
    'Coste de mercancía — comida': 'Coste directo del evento',
    'Coste de mercancía — bebida': 'Coste del canon (no tiene)',
    'Coste de mercancía (comida + bebida': 'Coste directo del evento (el canon no tiene coste',
    'de las ventas de COMIDA, no del total: la bebida tiene su propia línea':
        'de las ventas de ESPACIO Y SERVICIOS, no del total: el canon tiene su propia línea',
    'de las ventas de BEBIDA': 'de las ventas del CANON',
    'mezcla de comida y bebida, coste de mercancía, alquiler':
        'mezcla de espacio y canon, coste directo del evento, renta de la finca',
    'Materia prima, consumibles, comisiones e imprevistos':
        'Coste directo del evento, consumibles, comisiones e imprevistos',
    'Consumibles y envases': 'Consumibles de los montajes',
    'Suministros (luz, agua, gas': 'Suministros (luz, agua, gasoil y teléfono',
    'bloque de local': 'bloque de la finca',
    'cámbialo si tu carta tributa a otro tipo': 'cámbialo sólo si tu asesoría te confirma otro tipo',
    # Instrucciones, punto 4: el divisor del IVA de un bar (1,10 en sala) no sirve aquí (SPEC D4)
    'divide por el tipo que le corresponda: entre 1,10 en sala (comida y bebida, alcohol incluido: art. '
    '91.Uno.2.2.º de la Ley 37/1992 del IVA) y, cuando se venden para llevar, los alimentos —bollería y pastelería '
    'incluidas—, que son productos alimenticios al tipo reducido por el art. 91.Uno.1.1.º; y entre 1,21 el tipo '
    'general, que en hostelería sólo alcanza a lo que sale del local como entrega de bienes excluida del reducido: '
    'el alcohol y los refrescos o zumos con azúcares añadidos para llevar o a domicilio (la comida para llevar sigue '
    'al 10 %); el libro lo aplica al alcohol del canal de delivery':
        'divide entre 1,21: todo lo que factura la finca —espacio, servicios y canon— va al tipo general. El menú y '
        'la barra los factura el catering a los novios, al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992), y no entran '
        'en este libro',
    'Personas en el turno de producción': 'Personas de estructura por evento',
    # SPEC D4: las dos líneas al 21 %; la nota del PVP (Supuestos!C9) hablaba de un bar con todo al 10 %
    'En sala todo va al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992, alcohol incluido); el alcohol que sale por '
    'delivery y el pan común, si los tienes, mueven la media':
        'La finca factura el espacio, los servicios y el canon al 21 %, el tipo general; el menú y la barra los '
        'factura el catering a los novios, al 10 % (art. 91.Uno.2.2.º de la Ley 37/1992), y no entran en este libro',
    # restos de la panadería y de otros moldes en frases fijas del motor (barrido_es.py los caza)
    'el alcohol que sale por delivery y el pan común, si los tienes, mueven':
        'el canon y el espacio, los dos al 21 %, fijan',
    'los alimentos —bollería y pastelería incluidas—, que son': 'los alimentos, que son',
    'refrescos o zumos con azúcares añadidos': 'refrescos, zumos y gaseosas con azúcares o edulcorantes añadidos',
    'el pan común y las harinas panificables, al superreducido (art. 91.Dos.1.1.º':
        'el espacio, los servicios y el canon de la finca, al general (el 21 %',
    'El documento Word del pack sigue en la versión 1.1 y no lee esta celda: las cifras válidas son las de este libro':
        'El plan de negocio en Word cita esta cifra; si cambias una celda verde, manda este libro',
    # Tesorería (injertos de la heladería): Mes 1 girado, personal en doce meses y trimestres del 303
    'Perfil de tu zona: agosto flojo en ciudad y fuerte en costa':
        'Mes 1 = MARZO: la obra y la licencia se hacen en otoño e invierno y se abre con las comuniones y la empresa '
        'de primavera. Los picos son junio (Mes 4) y septiembre (Mes 7); el valle, enero (Mes 11). Si abres en otro '
        'mes, gira la fila',
    'La suma del año es la misma que la del P&L':
        'La suma del año es la misma que la del P&L. El personal se reparte en doce meses, pero la coordinación y los '
        'auxiliares fijos discontinuos sólo trabajan de marzo a noviembre: aquí la temporada sale más barata y el '
        'invierno más caro que en la realidad. A final de noviembre tu caja real será unos 9.000 € menor que la de '
        'esta hoja (tres mensualidades de esos dos puestos), y en febrero se iguala',
    'El IVA del cuarto trimestre se liquida en enero del año siguiente, así que no aparece en este cuadro':
        'Los trimestres de esta hoja son de tres meses del plan (marzo-mayo, junio-agosto y septiembre-noviembre), no '
        'los naturales: con el Mes 1 en marzo, el modelo 303 se presenta en abril (por marzo), julio, octubre y enero '
        '(por octubre-diciembre, ya en el Mes 11). En el caso todos los trimestres salen a compensar y la finca no '
        'paga IVA en su primer año: el de la obra se descuenta de lo que repercutes, y tras el tercer trimestre del '
        'plan aún quedan unos 18.760 € por compensar',
}

#: clave → (fila, rótulo, valor, formato, nota, fuente). Fila, rótulo y formato a None: los pone el motor. La semilla
#: escribe los valores en el libro (grupo_a conserva lo que ya traen las celdas verdes).
SUPUESTOS = {
    'cubiertos_dia': (
        None, None, 82, None,
        'Invitados de media por evento en el año 1. Sale de la mezcla de la tabla de referencias de la hoja de '
        'Instrucciones: bodas de 120, eventos de empresa de 80, celebraciones privadas de 70 y eventos pequeños de 40. '
        'Es una media: el aforo de la finca está más abajo',
        'research §3 (mezcla 81,7 invitados por evento, redondeada) [estimado]'),
    'ticket_medio': (
        None, None, 37.00, None,
        'SIN IVA, por invitado: lo que factura la FINCA, no lo que pagan los novios por la boda entera. Suma el '
        'espacio y los servicios (ceremonia, montaje, coordinación, limpieza y aparcamiento) y el canon que te paga '
        'el catering por cada invitado. Media de la mezcla: 47 € la boda, 34 € el evento de empresa, 29 € la '
        'celebración privada y 30 € el evento pequeño. El precio con IVA (21 %) está en la fila de abajo',
        'research §3 (mezcla 37,1 €, redondeada) [estimado]'),
    'dias_apertura': (
        None, None, 120, None,
        'Eventos celebrados en el año: 30 bodas, 35 de empresa (jornadas, comidas, Navidad), 40 celebraciones '
        'privadas (comuniones, bautizos, cumpleaños) y 15 pequeños (preboda, brunch, bodas íntimas). Es el MISMO dato '
        'para la cuenta de resultados, el punto de equilibrio, los escenarios y las horas de personal',
        'research §3 [estimado]'),
    'crec_a2': (
        None, None, 0.08, None,
        'Más actividad el segundo año: bodas que llegan por recomendación, empresas que repiten y planners que ya te '
        'conocen. El libro lo aplica a los invitados por evento con los mismos eventos; en euros es lo mismo que un '
        '8 % más de eventos del mismo tamaño (unos 130). El personal no sube con este porcentaje: crece con las '
        'incorporaciones de la hoja Personal',
        'research §3 [estimado] · SPEC D3'),
    'crec_a3': (
        None, None, 0.05, None,
        'Sobre el año 2 (unos 136 eventos equivalentes). Conservador: el techo lo ponen los sábados de temporada y '
        'el aforo de la finca',
        'research §3 [estimado]'),
    'pct_comida': (
        None, None, 0.78, None,
        'Alquiler del espacio y servicios del evento sobre las ventas; el 22 % restante es el canon del catering. '
        'Es el peso de la primera línea de ventas del P&L',
        'research §3 · SPEC D4 (78/22)'),
    'coste_comida': (
        None, None, 0.163, None,
        'Coste directo del evento sobre las ventas de espacio y servicios: limpieza tras el evento, reposición de '
        'aseos y consumibles, gasoil del grupo electrógeno, vigilancia y aparcamiento, y la tarifa de SGAE y '
        'AGEDI-AIE de cada evento. Unos 650 € por boda, 350 € por evento de empresa, 300 € por celebración privada y '
        '150 € por evento pequeño: 46.000 € al año',
        'research §2-§3 [estimado] · SPEC D4 (16,3 %)'),
    'coste_bebida': (
        None, None, 0.0, None,
        'A CERO: el canon no tiene coste para la finca. La comida y la bebida las compra el catering, que es quien '
        'las vende a los novios',
        'SPEC D4'),
    'pct_consumibles': (
        None, None, 0.02, None,
        'Velas, flores base, papel y productos de los aseos, y los pequeños consumibles de cada montaje',
        'research §3 [estimado]'),
    'pct_delivery': (
        None, None, 0.20, None,
        'Parte de las ventas que llega por un wedding planner o una agencia de eventos, que cobra una comisión. No '
        'cambia el IVA: todo lo que factura la finca va al 21 %',
        'research §3 (25 %) · calibrado D9: 20 %, porque la demo §2.11.9 del motor sube este input al 25 % y '
        'exige que el coste suba; el coste del canal es el mismo (2,5 % de las ventas)'),
    'comision_delivery': (
        None, None, 0.125, None,
        'Comisión media sobre lo que vende ese canal: el punto medio de un 10-15 %. Si todas las reservas te llegan '
        'directas, pon 0',
        'research §3 (10 % sobre el 25 %) · calibrado D9 (12,5 % sobre el 20 %: mismo 2,5 % de las ventas) [estimado]'),
    'comision_tpv': (
        None, None, 0.003, None,
        'Casi todo se cobra por transferencia (señales, pagos de los novios y facturas de empresa); el datáfono '
        'queda para los extras del día',
        'research §3 [estimado]'),
    'alquiler_mes': (
        None, None, 3500, None,
        'Renta de mercado de una finca con edificaciones existentes (salón, aseos y office) arrendada a una SL, con '
        'contrato de quince años o más. Lleva IVA al 21 %. Si la finca es de tu familia, la renta tiene que ser la de '
        'mercado igual. El peso sobre las ventas lo calcula el libro en la fila «Renta de la finca / Ventas» del P&L',
        'research §3 [estimado]'),
    'fianza_meses': (
        None, None, 2, None,
        'Dos meses de renta como fianza, lo habitual en un arrendamiento de uso distinto del de vivienda; los avales '
        'o garantías adicionales se negocian aparte. Compruébalo con tu abogado antes de firmar',
        'research §3 [estimado]'),
    'suministros_mes': (
        None, None, 1600, None,
        'Luz con potencia para el salón y el exterior, agua de riego, gasoil del grupo electrógeno fuera de los '
        'eventos y teléfono. Pide al propietario el histórico de consumos',
        'research §2-§3 [estimado]'),
    'seguros_ano': (
        None, None, 5500, None,
        'Responsabilidad civil de la actividad con el capital que fije tu comunidad por aforo (en Andalucía, '
        '526.000 € para 101-300 personas), daños a las mejoras de la finca, pérdida de beneficio y accidentes. '
        'Exige además al catering su propio seguro de responsabilidad civil e intoxicación',
        'research §1 y §3 [estimado] · cuantía andaluza: D. 109/2005 (fuente municipal)'),
    'pct_varios': (
        None, None, 0.02, None,
        'Roturas, imprevistos de cada montaje y desplazamientos comerciales (ferias y visitas a planners)',
        'research §3 [estimado]'),
    'recursos_propios': (
        None, None, 100000, None,
        'Aportación de los socios. Un banco pide entre el 25 y el 30 % de la necesidad de caja con dinero propio',
        'research §3 [estimado]'),
    'prestamo': (
        None, None, 263000, None,
        'Principal solicitado. La hoja de Financiación compara lo que aportas con la necesidad de caja de la hoja de '
        'inversión y te dice si sobra o falta: ajústalo con ese dato. La finca no es tuya, así que no hay garantía '
        'inmobiliaria: pregunta por avales y por líneas públicas',
        'research §3 (≈ 255.000 €) · calibrado D9: 263.000 € cubren la necesidad de caja del libro con 100.000 € '
        'propios (el IVA de la inversión y el fondo de maniobra salen algo más altos que la cuenta a mano)'),
    'tipo_prestamo': (
        None, None, 0.065, None,
        'Tipo nominal anual de un préstamo de empresa sin garantía inmobiliaria. Pide oferta a dos entidades y a una '
        'línea ICO antes de fijarlo',
        'research §3 [estimado] (= hermanos de eventos)'),
    'plazo_prestamo': (
        None, None, 8, None,
        'Años totales, carencia incluida. Con seis años la cuota no cabe en un negocio con tanta estructura fija',
        'research §3 (con 6 años el DSCR cae a ≈ 1,25) [estimado]'),
    'carencia_prestamo': (
        None, None, 1, None,
        'El primer año sólo intereses: la primera temporada se vendió antes de tener la licencia y llega corta. '
        'Desde el segundo año se devuelve el principal: mira la holgura de caja de ese año en el Punto de Equilibrio',
        'research §3 [estimado]'),
    'meses_fondo': (
        None, None, 3, None,
        'Tres meses de costes fijos: son el colchón del primer invierno. En un año normal, de noviembre a febrero '
        'entra alrededor del 23 % de la venta con la renta y la plantilla planas',
        'molde (mínimo de la familia) · research §3 · SPEC D7'),
    'vida_obra': (
        None, None, 15, None,
        'Obra en una finca ARRENDADA: se amortiza en el plazo del contrato si es menor que la vida útil del bien. Por '
        'eso el plan pide un arrendamiento de quince años o más; con un contrato más corto, la amortización anual sube. '
        'Confírmalo con tu asesoría',
        'research §3 · PGC NRV 3.ª (fuente secundaria)'),
    'vida_maquinaria': (
        None, None, 10, None,
        'Carpa, grupo electrógeno, mobiliario y sonido: un 10 % anual, dentro del coeficiente máximo de la tabla del '
        'art. 12.1 de la Ley del Impuesto sobre Sociedades para el mobiliario. Confírmalo con tu asesoría',
        'research §3 · LIS art. 12.1'),
    'pct_bebida_alc': (
        None, 'Bebida ALCOHÓLICA vendida por la finca (no la vende: a cero)', 0.0, None,
        'A CERO: la finca no vende bebida. La barra es del catering, que la factura él; la segunda línea de ventas '
        'del P&L es el canon que te paga',
        'SPEC D4'),
    'aforo': (
        None, 'Aforo de la finca (invitados sentados en el salón y la carpa)', 300, None,
        'DATO INFORMATIVO: no entra en ningún cálculo. Es el banquete más grande que caben sentado entre el salón y '
        'la carpa; el aforo legal lo fija tu licencia. Con 300 invitados la finca queda por debajo del plan de '
        'autoprotección estatal (Orden INT/1068/2026: 1.000 personas en edificio cerrado o carpa)',
        'research §1 y §3 [estimado] · Orden INT/1068/2026 (BOE)'),
    'salario_convenio': (
        None, None, 0, None,
        'El VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería (art. 4) nombra el catering, pero no el '
        'alquiler de espacios, y su lista no es exhaustiva: usa el convenio provincial de hostelería como referencia '
        'prudente y confírmalo con tu asesoría. Copia aquí el salario base del grupo más bajo de tu provincia. Con 0 '
        'el semáforo compara sólo contra el SMI',
        'ALEH VI art. 4 (BOE)'),
    'rampa_mes1': (
        None, None, 0.45, None,
        'Una finca que acaba de abrir no factura el primer mes lo que factura al año: las bodas se reservan con 12-18 '
        'meses de antelación y la primera temporada sólo trae lo que se vendió desde la licencia. Con 100 % se '
        'elimina la rampa',
        'research §0 y §3 (Bodas.net, fuente secundaria) · SPEC D8'),
    'meses_rampa': (
        None, None, 12, None,
        'Doce meses hasta el ritmo de crucero: la primera temporada entera',
        'research §3 · SPEC D8'),
    'meses_renta_previa': (
        None, 'Meses de renta ANTES de abrir (obra y licencias)', 1, None,
        'Un mes de renta antes de abrir. La carencia de renta durante la obra y la licencia se negocia aparte en el '
        'arrendamiento: sin ella, súmale los meses que dure la tramitación (de 6 a 12 o más en suelo rústico)',
        'research §1 y §3 [estimado]'),
    'pct_imprevistos': (
        None, None, 0.08, None,
        'Colchón sobre la obra y las instalaciones de unas edificaciones que no son nuevas, que es donde aparecen las '
        'sorpresas (tejados, acometida eléctrica, saneamiento y agua). Un banco no financia una reforma sin él',
        'calibrado D9 (inversión total ≈ 242.000 €, SPEC D7) [estimado]'),
    'dias_cobro': (
        None, None, 10, None,
        'Media ponderada: los novios pagan la señal y el resto antes de la boda, y las empresas a 30-45 días de la '
        'factura. El libro no admite días negativos, así que las señales no se modelan: tu caja real será algo '
        'MEJOR que la de la hoja de Tesorería',
        'research §3 [derivado]'),
    'dias_pago': (
        None, None, 30, None,
        'Plazo de pago a proveedores de limpieza, mantenimiento y consumibles: lo que te financian. Es lo primero que '
        'se pierde si te retrasas en un pago',
        'research §3 [estimado]'),
    'mes_paga_1': (
        None, None, 5, None,
        'Mes de la TESORERÍA en el que sale la paga extra de verano: julio es el Mes 5, porque el Mes 1 del plan es '
        'marzo',
        'SPEC D8 (Mes 1 = marzo)'),
    'mes_paga_2': (
        None, None, 10, None,
        'Mes de la TESORERÍA en el que sale la paga extra de Navidad: diciembre es el Mes 10, porque el Mes 1 del '
        'plan es marzo',
        'SPEC D8 (Mes 1 = marzo)'),
    'iva_bebida': (
        None, 'IVA de la bebida ALCOHÓLICA (la finca no la vende)', 0.21, None,
        'Esta celda no mueve nada en este plan: la finca no vende bebida (la vende el catering, que la factura él) y '
        'la línea del canon lleva su propio tipo, el 21 %, en el P&L',
        'SPEC D4'),
}

#: (rótulo, peso, 'comida'|'bebida', nota, fuente, tipo de IVA). Dos líneas (`mix_en_supuestos`): el peso se teclea en
#: Supuestos. SPEC D4: las DOS al 21 % (sexto campo numérico → celda G verde del P&L). Sin «evento(s)» suelto que no
#: vaya con «Ventas» (RX_RECUENTO / RX_EURO_FUERTE).
LINEAS_INGRESO = (
    ('Ventas de alquiler del espacio y servicios del evento', 0.78, 'comida',
     'Lo que pagan los novios y las empresas a la finca: el espacio, la ceremonia, el montaje, la coordinación del '
     'día, la limpieza y el aparcamiento. Con precio propio va al 21 %',
     'research §3 · SPEC D4', 0.21),
    ('Canon del catering exclusivo', 0.22, 'bebida',
     'Lo que te paga el catering de la casa por servir en la finca. El plan supone el 12 % de lo que factura en '
     'ella, unos 13 € por invitado en una boda: es un supuesto, negócialo. Factura de la finca al catering, al 21 %',
     'research §2-§3 (canon del 12 %, sin fuente pública) · SPEC D4 y D11', 0.21),
)

#: (puesto, personas, bruto mes TOTAL de la fila en 14 pagas, nota, fuente, jornada). Bruto de la fila = bruto de
#: jornada completa × jornada × personas. Sin camareros ni cocina: los pone el catering (SPEC D6). Sin «evento» en el
#: puesto (RX_RECUENTO).
PLANTILLA = (
    ('Titular — gerencia, ventas y visitas', 1, 2000,
     'Vende, enseña la finca, firma los contratos, lleva el calendario y coordina al catering. Como administrador de '
     'la SL cotiza en el régimen de autónomos: el libro le imputa el 33 % de Seguridad Social sobre 14 pagas como si '
     'fuera nómina, que es el lado prudente. Confirma con tu gestoría la cuota real',
     'research §3 [estimado]', 1.0),
    ('Coordinación de bodas y celebraciones (fijo discontinuo, marzo-noviembre)', 1, 1240,
     'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) a jornada completa de marzo a noviembre: '
     'equivale al 75 % en cómputo anual. Prepara cada evento con los novios y el catering y lo dirige el día. Bruto a '
     'jornada completa: unos 1.650 €',
     'research §3 [estimado] · ET art. 16', 0.75),
    ('Mantenimiento y jardinería', 1, 1120,
     'Jardines, riego, caminos, pequeñas reparaciones, grupo electrógeno y puesta a punto del salón y de la carpa. '
     'Al 80 % de jornada; lo grande (poda, pintura) va en los costes fijos. Bruto a jornada completa: 1.400 €',
     'research §3 [estimado]', 0.80),
    ('Auxiliares de montaje, acceso y aseos (fijos discontinuos)', 2, 1080,
     'Dos personas al 40 % de jornada en cómputo anual: montaje, control de acceso y aparcamiento, reposición de '
     'aseos y recogida. Dos en cada boda y una en el resto. Nunca como autónomos que te facturan: con tu horario y '
     'tu dirección es falso autónomo (art. 1.1 ET). Bruto a jornada completa: 1.350 €',
     'research §3 [estimado] · ET arts. 1.1 y 16', 0.40),
    ('Comercial de bodas a tiempo parcial', 1, 300,
     'Al 20 % de jornada: visitas de los sábados por la mañana, ferias nupciales y seguimiento de las peticiones '
     'de los portales. Bruto a jornada completa: 1.500 €',
     'SPEC D6 [estimado]', 0.20),
    ('Limpieza y puesta a punto a tiempo parcial', 1, 260,
     'Al 20 % de jornada: limpieza entre eventos del salón, los aseos y el office. La limpieza a fondo tras cada boda '
     'va en el coste directo del evento. Bruto a jornada completa: 1.300 €',
     'SPEC D6 [estimado]', 0.20),
)

#: Cobertura: (horas del día del evento × personas a la vez + horas de estructura × personas de estructura) × eventos,
#: frente a las horas contratadas de toda la plantilla (3,75 jornadas × 1.840 h).
COBERTURA = {
    'horas_dia': 9.2,
    'personas_franja': 2.3,
    'horas_produccion': 12,
    'personas_produccion': 3,
    'nota_horas': 'Media del día del evento, de montaje a recogida: boda 13 h, empresa 9 h, celebración privada 8 h y '
                  'evento pequeño 5 h (9,2 h de media con la mezcla del plan)',
    'nota_personas': 'Personal de la finca a la vez en el evento: coordinación y dos auxiliares en las bodas, y '
                     'coordinación y un auxiliar en el resto (2,3 de media). Camareros y cocina los pone el catering',
    'nota_horas_produccion': 'Horas por evento fuera del día del evento: visitas y reuniones con los novios, '
                             'preparación con el catering, mantenimiento, jardín, limpieza y gestión. Es la parte de '
                             'la plantilla que trabaja todo el año, repartida entre los eventos',
    'nota_personas_produccion': 'Gerencia, mantenimiento y apoyo (comercial o limpieza) a la vez',
}

ROTACION = {'activa': False}

#: Partidas de la hoja de inversión: las escribe `semilla_fin.py` (rótulo, importe, nota, ¿IVA?) en las filas 7-25
#: del molde de la panadería; aquí sólo la clasificación para la amortización ('no' se mira primero; 'obra' = base de
#: los imprevistos, 15 años; 'maquinaria' = 10 años). Ojo: «registrador» no es «registro» (\b).
INVERSION = {}
INVERSION_EXTRA = ()
AMORTIZABLE = {
    'no': (r'fianza|primer mes|alquiler|\brenta\b|stock|existencias|fondo de maniobra|colch[oó]n|imprevisto|marca|'
           r'\bweb\b|foto|lanzamiento|constituci|notar[ií]a|\bregistro\b|declaraci|appcc|formaci[oó]n|seguro|'
           r'licencia|permiso|\btasas?\b|calificaci|prestaci[oó]n compensatoria',),
    'obra': (r'proyecto t[eé]cnico|adecuaci[oó]n|ac[uú]stica|aseos|instalaci[oó]n el[eé]ctrica|climatizaci|office|'
             r'aparcamiento|caminos|jardiner|incendios|accesibilidad',),
    'maquinaria': (r'carpa|p[eé]rgola|grupo electr[oó]geno|mobiliario|chill|sonido|limitador|proyector',),
}

#: Costes fijos. Las 10 partidas propias las escribe `semilla_fin.py` en las filas 26-35 (rótulo e importe); aquí,
#: la nota por rótulo normalizado (minúsculas y sin tildes) y la de las filas canónicas.
FIJOS = {
    'alquiler del local': (
        None, 'El importe mensual está en la hoja de Supuestos; aquí se multiplica por doce. Lleva IVA al 21 %. El '
              'mes de renta previo a la apertura está en la hoja de Inversión y NO se cuenta dos veces'),
    'marketing: portales de bodas, google ads y redes': (
        None, 'Escaparate en los portales de bodas, Google Ads y redes sociales. Mide el coste por contacto de cada '
              'canal antes de renovar el escaparate premium'),
    'ferias nupciales y jornadas de puertas abiertas': (
        None, 'Dos ferias de novios al año y las jornadas de puertas abiertas de la finca, con el catering'),
    'jardineria y mantenimiento externo (poda, cesped y riego)': (
        None, 'Los trabajos grandes que no hace el personal propio: poda, césped, riego y tratamientos'),
    'reparaciones, pintura y reposicion de mobiliario': (
        None, 'Pintura, pequeñas obras entre temporadas y reposición de sillas, mesas y mantelería'),
    'gestoria laboral, fiscal y contable': (
        None, 'Contabilidad, impuestos de la SL y nóminas de los fijos discontinuos, con sus llamamientos de cada '
              'temporada'),
    'software de reservas, crm, web y telefono': (
        None, 'Calendario de fechas, presupuestos, CRM de novios y empresas, alojamiento de la web y teléfono'),
    'prevencion de riesgos laborales y vigilancia de la salud': (
        None, 'El plan de prevención es obligatorio (Ley 31/1995): montaje, cargas, trabajo en altura y jardinería, y '
              'reconocimientos médicos de la plantilla'),
    'tasas municipales e ibi repercutido': (
        None, 'Basuras y otras tasas municipales y el IBI que el propietario te repercuta según el contrato. Pon las '
              'de tu ayuntamiento'),
    'revisiones de baja tension, proteccion contra incendios y grupo electrogeno': (
        None, 'Inspecciones periódicas de la instalación eléctrica, mantenimiento de extintores y del sistema contra '
              'incendios por una empresa mantenedora y revisión del grupo electrógeno'),
    'limpieza general, desinsectacion y desratizacion (ddd)': (
        None, 'Limpieza a fondo de temporada, productos y control de plagas por una empresa inscrita'),
}
FIJOS_EXTRA = ()

#: (clave, rótulo, valor, comentario). Research §3: coste directo ≤ 14 %, personal ≤ 33 %, renta ≤ 13 %, neto ≥ 5 %.
UMBRALES = (
    ('r_mb', 'Margen bruto / Ventas', 0.75,
     'Suelo del margen tras TODOS los costes variables (coste directo del evento, consumibles, comisiones, medios '
     'de pago y varios): sin mercancía que comprar, una finca deja más del 75 %. Estimación del kit'),
    ('r_cogs', 'Coste directo del evento / Ventas', 0.14,
     'Limpieza, aseos, gasoil, vigilancia y SGAE de cada evento sobre las ventas. Por encima del 14 %, algo se '
     'escapa en cada montaje. Estimación del kit'),
    ('r_personal', 'Coste de personal / Ventas', 0.33,
     'Techo del personal propio sobre ventas, sin camareros ni cocina (los pone el catering). Estimación del kit'),
    ('r_alquiler', 'Renta de la finca / Ventas', 0.13,
     'Techo de la renta de la finca sobre las ventas: por encima, la ocupación tiene que ser altísima para pagarla. '
     'Estimación del kit'),
    ('r_neto', 'Resultado neto / Ventas', 0.05,
     'Suelo de resultado neto a régimen para que el plan se sostenga: estimación del kit'),
)

#: (invitados por evento, € por invitado sin IVA, eventos al año). Research §3.
ESCENARIOS = {
    'pesimista': (78, 34.00, 100),     # una temporada floja y precios a la baja
    'optimista': (85, 39.00, 135),
}

#: Mes 1 = MARZO (SPEC D8). Calendario (research §3, ponderado por ventas): ene .031 · feb .047 · mar .063 · abr .084 ·
#: may .124 · jun .135 · jul .078 · ago .055 · sep .122 · oct .111 · nov .073 · dic .077. El research suma 99,9: se le
#: da el 0,1 a septiembre (el pico del INE). Rotada al orden del motor (Mes 1…12).
ESTACIONALIDAD = (0.063, 0.084, 0.124, 0.135, 0.078, 0.055,
                  0.122, 0.111, 0.073, 0.077, 0.031, 0.047)
assert abs(sum(ESTACIONALIDAD) - 1.0) < 1e-9, sum(ESTACIONALIDAD)

INSTRUCCIONES = {
    'uso': [
        '6. La hoja «Tesorería 12 meses» responde la pregunta que decide una operación bancaria: en qué mes se agota '
        'la caja. Su Mes 1 es MARZO: la finca abre en primavera y llega al primer invierno con la caja de la '
        'temporada. El saldo mínimo del año nunca puede salir en rojo. Las señales de los novios no se modelan: tu '
        'caja real será algo mejor.',
        '7. La hoja «Financiación» cuadra lo que hace falta con lo que se aporta y monta el cuadro de amortización '
        'del préstamo. Si la diferencia sale en rojo, el plan no está financiado.',
        '8. El documento Word de este pack, la calculadora de presupuestos y los modelos de contrato usan las cifras '
        'de este Excel: si cambias una celda verde, el Excel manda.',
    ],
    'referencias': [
        ('Mes 1 del plan', 'Marzo', 'Decisión del plan',
         'La obra y la licencia se hacen en otoño e invierno y se abre con las comuniones y la empresa de primavera. '
         'La fila de estacionalidad de la Tesorería ya va girada'),
        ('Mezcla de eventos del plan', '120 eventos: 30 bodas, 35 de empresa, 40 celebraciones privadas y 15 pequeños',
         'Estimación del kit',
         'Bodas (30 × 120 invitados × 47 €), empresa (35 × 80 × 34 €), celebraciones privadas (40 × 70 × 29 €) y '
         'pequeños (15 × 40 × 30 €), sin IVA, de espacio, servicios y canon. Media: 82 invitados a 37 €'),
        ('Techo de fechas', 'Unos 26 sábados de mayo a octubre', 'Estimación del kit',
         'Las 30 bodas son unas 21 en sábados de temporada (el 80 %) y el resto en viernes, domingos o fuera de '
         'temporada. El libro no comprueba este techo: compruébalo tú en tu calendario'),
        ('Bodas en España en 2024', '175.364, el 83,6 % civiles', 'INE, Movimiento Natural de la Población 2024',
         'De mayo a octubre se celebra el 63,7 %; septiembre (13,1 %) y junio (12,8 %) son los picos y enero se queda '
         'en el 3,8 %'),
        ('Antelación de la reserva de una boda', '12-18 meses (13 de media)',
         'Bodas.net, Informe del Sector Nupcial 2026',
         'Por eso la primera temporada se vende antes de abrir y la rampa del plan dura 12 meses'),
        ('Coste directo por evento', '650 € boda · 350 € empresa · 300 € celebración · 150 € pequeño',
         'Estimación del kit',
         'Limpieza tras el evento, reposición de aseos y consumibles, gasoil del grupo electrógeno, vigilancia y '
         'aparcamiento, y la tarifa de SGAE y AGEDI-AIE de cada evento'),
        ('Canon del catering exclusivo', '12 % de lo que factura el catering en la finca',
         'Supuesto del kit, sin fuente pública',
         'Unos 13 € por invitado en una boda. Negócialo y pon el tuyo: en este plan, cada punto de canon son unos '
         '6.700 € de ventas al año'),
        ('Personal de la finca en un evento', 'Coordinación y 1 auxiliar (2 en las bodas)', 'Estimación del kit',
         'Boda: 2 auxiliares × 12 h · empresa 1 × 9 h · celebración 1 × 8 h · pequeño 1 × 5 h. Camareros y cocina '
         'los pone el catering'),
        ('IVA de lo que factura la finca', '21 %', 'Ley 37/1992 del IVA',
         'El espacio y los servicios con precio propio y el canon que cobras al catering, al tipo general. El menú lo '
         'factura el catering a los novios, al 10 % (art. 91.Uno.2.2.º). Meter el espacio al 10 % dentro de un pack es '
         'arriesgado: confírmalo con tu asesoría o pide una consulta vinculante'),
        ('Plan de autoprotección', 'Desde 1.000 personas en edificio cerrado o carpa · 5.000 al aire libre',
         'Orden INT/1068/2026, Directriz Básica de Autoprotección (BOE del 10-10-2026)',
         'Una finca de 300 invitados queda por debajo de la norma estatal; tu comunidad o tu ayuntamiento pueden '
         'pedir más, por ejemplo en un entorno forestal'),
        ('Ruido al exterior en zona residencial', '55 dBA de día y de tarde · 45 dBA de noche',
         'RD 1367/2007, art. 24 y anexo III',
         'Limitador-registrador, baile final dentro y altavoces de espaldas a las viviendas. El horario de la música '
         'lo fijan tu comunidad y la ordenanza de tu ayuntamiento: compruébalo'),
        ('Comida testigo', 'Una ración de 100 g o más durante 7 días, a 4 °C o menos (o a −18 °C)',
         'RD 1086/2020, art. 30',
         'En bodas y encargos de más de 40 personas. La guarda quien sirve, el catering: exígelo en su contrato'),
        ('Agua de pozo propio', 'Zona de abastecimiento de tipo 1', 'RD 3/2023, arts. 2 y 4.3',
         'Con actividad comercial, el titular responde de la calidad del agua hasta el grifo: analíticas y protocolo'),
        ('Convenio colectivo de referencia', 'Provincial de hostelería',
         'VI Acuerdo Laboral de ámbito Estatal para el sector de Hostelería, art. 4',
         'Su lista nombra el catering, no el alquiler de espacios, y no es exhaustiva: es la referencia salarial '
         'prudente. Confírmalo con tu asesoría'),
    ],
}

#: El checklist lo escribe `semilla_fin.py` entero (`datos_checklist.py`): aquí no hay reemplazos.
CHECKLIST = {}

#: Producto nuevo: sin bloque «qué ha cambiado» (grupo_a no lo pinta si está vacío).
RECALIBRADO = ()

#: IVA SOPORTADO del coste directo del evento (limpieza, consumibles, gasoil, vigilancia, SGAE): casi todo al 21 %
#: (SPEC D4). La semilla lo escribe por valor en `PyG!G13` (en la panadería era una fórmula).
IVA_COMPRAS = {
    'comida': 0.21,
    'nota': 'El IVA que SOPORTAS en el coste directo del evento: limpieza, consumibles, gasoil, vigilancia y la '
            'tarifa de SGAE van al 21 %. Ajústalo a tus facturas',
}
