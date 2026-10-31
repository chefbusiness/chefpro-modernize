#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura del Plan de Negocio: Hamburguesería Smash ES 1.0
(F1-camino §4: 12/15/14/13/13/13, mismas filas que el Sushi Bar, la Taquería y la Pollería). Producto nuevo: no hay
versión anterior; formato de `plan-sushi/datos_checklist.py`. Marco legal: `F1-research-hamburgueseria.md` §0-§1 (R) y la
lista de tareas obligadas de R §3 (lo marcado 🟡 va como «compruébalo» o «confírmalo»). Fuente primaria de cada cita:
  · RDLeg 1175/1990 (tarifas del IAE): con comedor, grupo 671 (por categoría); de barra y mostrador sin comedor
    separado, 673; la nota común de los grupos 671-673 faculta la venta para llevar; si el reparto a domicilio fuera la
    actividad principal (formato de sólo delivery), 677.9; exención de cuota, art. 82.1.c del TRLRHL;
  · Ley 12/2012: los restaurantes no están en su anexo → licencia o declaración responsable por la ordenanza municipal;
  · Ordenanza 4/2021 de Calidad del Aire de Madrid (OCAS), arts. 12 y anexo I (conducto exclusivo a cubierta, +1 m sobre
    lo que haya en 15 m), 23 (limpieza ≥ 1 vez al año) y 24 (sólo exime lo eléctrico ≤ 4 kW sin olores: no una plancha
    con dos freidoras), como ejemplo; fuera de Madrid, la ordenanza de cada ayuntamiento;
  · RD 919/2006, ITC-ICG 07 e ITC-ICG 08: gas por empresa instaladora habilitada, certificado de la instalación y puesta
    en marcha de cada aparato, inspección (red) o revisión (gas envasado) cada 5 años;
  · RD 1021/2022: art. 2.2.a (la restauración es «comercio al por menor»); art. 3 (registro autonómico previa
    declaración responsable; RGSEAA sólo para el suministro a otros negocios por encima de lo marginal, localizado y
    restringido; la carne picada que compras a una carnicería entra por esa vía, con su declaración); art. 4.1 (carne
    picada ≤ 2 °C, preparados de carne ≤ 4 °C, frutas y hortalizas cortadas listas para consumo ≤ 4 °C), 4.2
    (temperatura de la etiqueta) y 4.3 (transporte); art. 5 (congelación en el comercio minorista: envasado y
    etiquetado con fechas de elaboración, congelación y caducidad, 5.3; equipo que llegue a ≤ −18 °C en el centro con un
    descenso ininterrumpido, 5.4-5.5; registro, 5.6; descongelación en frío, 5.8; nunca recongelar, 5.9); art. 7.2 (el
    picado previo, «con arreglo a las necesidades del despacho diario, no pudiendo conservarse de un día para otro») y
    7.3 (quien pica cumple los caps. II y III de la secc. V del anexo III del Rgto. 853/2004). Con picada propia, la
    congelación del art. 5 se lee junto al 7.2: «confírmalo con tu inspector» [criterio del plan];
  · Reglamento (CE) 853/2004: anexo I 1.13 («carne picada»: menos de un 1 % de sal) y 1.15 (preparado de carne: la
    bola salada o aliñada); anexo III, secc. V, cap. II (sólo músculo esquelético con su grasa, sin recortes ni
    desperdicios; carne a ≤ 7 °C al picar) y cap. III (picada dentro de los 6 días siguientes al sacrificio o de los 15
    si es vacuno deshuesado y envasado al vacío; ≤ 2 °C nada más picarla);
  · Madrid Salud, informe Inf26008 (2-feb-2026): no se pica carne madurada más de 15 días; la Comunidad de Madrid: la
    carne picada de carne madurada «no es una práctica permitida»;
  · AESAN, «Toxiinfección por Escherichia coli» (18-abr-2022): RECOMIENDA el cocinado completo a ≥ 70 °C durante al
    menos 2 minutos (recomendación, no norma: en España no hay temperatura legal de cocción de la hamburguesa; la fija el
    PCC del APPCC);
  · RD 1086/2020, art. 30, en la redacción de la disposición final 2.ª del RD 1021/2022: caliente ≥ 63 °C (30.2),
    refrigeradas ≤ 4 °C u ≤ 8 °C con vida útil < 24 h (30.3), enfriamiento de 60 a 10 °C en < 2 h (30.6) y recalentado
    ≥ 74 °C 15 s (30.7). NUNCA «art. 30 del RD 1021/2022»;
  · Reglamento (UE) 2017/2158 (acrilamida): art. 2.2 (la restauración aplica el anexo II, parte A); anexo II, parte A
    (patata con poco azúcar, almacenada a más de 6 °C; la fresca en remojo o escaldada; la congelada, con las
    instrucciones del fabricante; freír por debajo de 175 °C; espumar; guía de colores a la vista; pan tostado hasta el
    color óptimo); art. 4.6 sin muestreo, pero con pruebas de aplicación; la parte B, sólo con suministro central de
    franquicia; anexo IV (nivel de referencia de las patatas fritas, 500 µg/kg);
  · Orden de 26 de enero de 1989 (aceites y grasas calentados, vigente salvo sus arts. 7, 8 y 10-12): art. 3 (bares,
    comida para llevar), art. 6.3 (componentes polares por debajo del 25 %) y art. 9 (nada añadido al baño; el aceite
    usado no vuelve a la cadena alimentaria). No obliga a un medidor;
  · RD 126/2015, art. 4 (sin envasar o envasado a petición: denominación y alérgenos), art. 5 (envasado por el
    comercio para su venta inmediata: arts. 9 y 10 del Reglamento (UE) 1169/2011 salvo la nutricional) y arts. 4.1.b y
    6.5.a (alérgenos por escrito, o de palabra con registro escrito o electrónico accesible); Reglamento (UE)
    1169/2011, art. 14 (venta a distancia, 🟡 no releído); Reglamento de Ejecución (UE) 828/2014 («sin gluten» ≤ 20
    mg/kg: no se promete con pan de trigo, freidora compartida con rebozados ni plancha común);
  · Ley 37/1992, art. 91.Uno.1.1.º a y b y 91.Uno.2.2.º (para llevar: alcohol y bebidas con azúcares o edulcorantes
    añadidos al 21 %, también los zero; la comida al 10 %; el batido de leche, al 10 % 🟡) y 91.Dos.1.1.º a, d-g (el pan
    de hamburguesa no es pan común; queso, huevo, patata fresca, verdura y leche al 4 %; sólo los aceites de oliva al
    4 %); Ley 1/2025, art. 8 (llevarse lo no consumido, aviso visible); Ley 7/2022, art. 55 (cobro del envase de plástico
    de un solo uso);
  · ET arts. 1.1, 34.9 y DA 23.ª (registro de jornada: sin afirmar que sea «digital» por ley); ALEH VI art. 4 (convenio
    provincial de hostelería: nombra las hamburgueserías); Ley 31/1995 (PRL); Ley 18/2022 (SL desde 1 €).
Sin «carné», sin «licencia de apertura», sin «sin gluten» prometido, sin temperatura legal de cocción, sin «7 días» de
congelación o de picada ni restos del sushi bar, la taquería, la pollería o la pizzería en todo el libro. Cada tarea:
(trámite / acción, responsable, plazo, notas). Pestañas ≤ 29 caracteres. Sesión Claude Code, 31-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — HAMBURGUESERÍA SMASH'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Consulta urbanística previa: extracción a cubierta, potencia eléctrica y aforo', 'Titular / Técnico',
         'Antes de firmar el alquiler',
         'Pregunta al ayuntamiento si el uso permite una hamburguesería con plancha y dos freidoras, si el local admite un '
         'conducto exclusivo de extracción hasta la cubierta (en Madrid, que supere en 1 m lo que haya en 15 m: '
         'Ordenanza 4/2021, art. 12 y anexo I), qué potencia eléctrica tiene, si llega el gas y qué aforo. Sin salida a '
         'cubierta no hay plancha ni freidora'),
        ('Decidir el formato ANTES de firmar el local: sala con mostrador, sólo a domicilio o con servicio de mesa',
         'Titular', 'Antes de firmar el alquiler',
         'Sala con pedido en el mostrador, para llevar y a domicilio (este plan: 36 plazas en unos 90 m²); sólo a '
         'domicilio en 40-60 m² (la Guía Dark Kitchen de AI Chef Pro); una hamburguesería con servicio de mesa en '
         '120-150 m²; o un carrito o un puesto en la calle y en eventos (el Plan de Negocio: Food Truck). Cada uno pide '
         'otro local, otra inversión y otro margen'),
        ('Decidir antes de firmar: carne comprada picada o picada en el local', 'Titular', 'Antes de firmar el alquiler',
         'Si la compras picada (o en bolas ya porcionadas), el proveedor responde de la elaboración; si la compra a una '
         'carnicería, ese suministro entre minoristas tiene que ser marginal, localizado y restringido (RD 1021/2022, '
         'art. 3). Si la picas tú, cumples el art. 7 del mismo real decreto: del día, sólo músculo sin recortes y con la '
         'picadora y su sitio en el proyecto de la cocina'),
        ('Decidir antes de firmar: patata congelada o fresca', 'Titular', 'Antes de firmar el alquiler',
         'El plan usa patata congelada. La fresca pide pelar, cortar, remojar o escaldar (Reglamento (UE) 2017/2158, '
         'anexo II, parte A), sitio, agua y horas de cocina: la calculadora del pack te dice hasta qué coste de mano de '
         'obra te compensa'),
        ('Elegir la forma jurídica y constituir la SL o darte de alta como autónomo', 'Gestoría / Notaría',
         'Semanas 1-2',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades); la SL se puede constituir con 1 € de '
         'capital (Ley 18/2022, «Crea y Crece»). Como autónomo tributas por IRPF: compara las dos opciones con tu '
         'gestoría con las cifras del plan'),
        ('Alta censal (modelo 036) en el grupo 671 o 673 del IAE, o en el 677.9 si manda el reparto a domicilio',
         'Gestoría', 'Semana 2',
         'Con comedor, el grupo 671 («servicios en restaurantes», por categoría); de barra y mostrador sin comedor '
         'separado, el 673. La nota común de esos grupos ya te faculta para vender para llevar. Si el reparto a '
         'domicilio fuera tu actividad principal, el 677.9 (RDLeg 1175/1990). Confírmalo con tu gestoría. Exento de cuota '
         'con una cifra de negocio inferior a 1 millón de euros (art. 82.1.c de la Ley de Haciendas Locales)'),
        ('Alta en la Seguridad Social (administrador o autónomo)', 'Gestoría', 'Semana 2',
         'Consulta la cuota del ejercicio en curso y si te aplica la cuota reducida de inicio de actividad'),
        ('Certificado digital', 'Titular', 'Semana 1',
         'Imprescindible para Hacienda, la Seguridad Social, el ayuntamiento y el registro sanitario'),
        ('Cuenta bancaria y tarjeta del negocio', 'Titular', 'Semana 2',
         'Separadas de las personales: por ellas pasan las liquidaciones del datáfono y de las plataformas y los pagos '
         'a proveedores'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Semanas 2-4',
         'Nóminas y contratos de la plantilla. El software de facturación del TPV tiene que cumplir Veri*factu: '
         'consulta con tu gestoría la fecha que te aplica antes de comprar el TPV'),
        ('Presentar el plan al banco y pedir dos ofertas de préstamo', 'Titular', 'Semanas 2-4',
         'Lleva el plan financiero completo, con la tesorería mes a mes. Pide también oferta de leasing o renting de la '
         'plancha, las freidoras y el frío y de una línea ICO'),
        ('Seguro de responsabilidad civil y multirriesgo con avería del frío', 'Corredor de seguros', 'Antes de la obra',
         'RC de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la aseguradora que trabajas con '
         'una plancha de gas y dos freidoras: cambia la prima y las condiciones'),
    ]),
    ('F2 - Local, humos y gas', 'FASE 2: LOCAL, HUMOS, GAS Y LICENCIA (semanas 3-14)', [
        ('Elegir el local: unos 90 m² ya de restauración con salida a cubierta posible', 'Titular', 'Semanas 3-6',
         'Sitio para la cocina a la vista con la plancha y dos freidoras, un mostrador de pedidos con pantalla de '
         'turnos, una sala de 30 plazas y una barra de ventana de 6 taburetes, aseos (uno adaptado) y una zona de '
         'empaquetado y de recogida de los repartidores junto a la puerta. Barrio con vida de noche o zona universitaria'),
        ('Comprobar la potencia eléctrica y la acometida de gas', 'Técnico / Distribuidora', 'Antes de firmar',
         'Las freidoras eléctricas suelen pedir corriente trifásica, y el frío, la extracción y la climatización suman. '
         'Si no llega el gas, la plancha tendrá que ser eléctrica y la potencia, mayor. Una ampliación o una acometida '
         'nueva tarda: pregunta plazo y coste'),
        ('Comprobar con el técnico el recorrido del conducto hasta cubierta', 'Técnico', 'Antes de firmar',
         'Conducto exclusivo, continuo y estanco hasta la cubierta, por patio o fachada, con el permiso de la comunidad '
         'de propietarios si cruza zonas comunes. En Madrid, sólo se libra lo eléctrico de hasta 4 kW sin olores '
         '(Ordenanza 4/2021, art. 24): una plancha con dos freidoras no'),
        ('Negociar el alquiler: carencia de obra y fianza', 'Titular', 'Antes de firmar',
         'El plan cuenta dos meses de renta antes de abrir y dos de fianza. Pide carencia mientras duran la obra, el '
         'conducto y la instalación de gas'),
        ('Contrato de arrendamiento con el uso de restaurante y la salida de humos', 'Titular / Abogado', 'Semana 6',
         'Que diga «restaurante» u «hostelería» y que autorice la obra de la cocina, del conducto a cubierta y de la '
         'instalación de gas'),
        ('Encargar el proyecto técnico de la actividad y de la extracción', 'Arquitecto/a o ingeniero/a',
         'Semanas 6-8',
         'Distribución de la cocina, el mostrador y la sala, potencia, gas, aforo, ventilación, accesibilidad y el '
         'conducto a cubierta. Fuera de Madrid, pide la ordenanza de humos y de calidad del aire de tu ayuntamiento'),
        ('Licencia o declaración responsable de la actividad', 'Técnico / Ayuntamiento', 'Antes de la obra',
         'Los restaurantes no están en el anexo de la Ley 12/2012: van por el régimen de tu ayuntamiento, licencia o '
         'declaración responsable según su ordenanza. Pregunta cuál te toca en la consulta previa'),
        ('Licencia, declaración o comunicación previa de la obra', 'Técnico / Ayuntamiento',
         'Semanas 6-8, antes de empezar la obra',
         'La obra y el conducto van por su propio trámite municipal: pregunta en la consulta previa qué título piden'),
        ('Conducto exclusivo de extracción a cubierta', 'Instalador / Técnico', 'Semanas 8-12',
         'Ejemplo de Madrid (Ordenanza 4/2021): conducto exclusivo que supere en 1 m lo que haya en 15 m (art. 12 y '
         'anexo I). La plancha y las freidoras echan mucha grasa: pide al instalador los registros de limpieza del '
         'conducto'),
        ('Campana extractora sobre la plancha y las freidoras', 'Instalador', 'Semanas 10-12',
         'Campana extractora con motor y filtros de grasa que cubra toda la línea caliente, conectada al conducto '
         'exclusivo. Pide al instalador el caudal y el plan de limpieza de los filtros'),
        ('Instalación de gas por empresa habilitada o potencia para una plancha eléctrica', 'Instalador de gas habilitado',
         'Durante la obra',
         'Certificado de la instalación y puesta en marcha certificada de la plancha y de cada aparato de gas, e '
         'inspección (red) o revisión (gas envasado) cada 5 años (RD 919/2006, ITC-ICG 07 e ITC-ICG 08). Con plancha '
         'eléctrica, el boletín tiene que cubrir su potencia'),
        ('Obra de la cocina, el mostrador y la sala: superficies lisas y lavables', 'Constructor', 'Semanas 8-12',
         'Paredes alicatadas, suelo antideslizante (la grasa de la plancha llega al suelo), falsos techos lavables, '
         'lavamanos de accionamiento no manual en la cocina, aseos (uno adaptado) y aislamiento acústico si hay vecinos'),
        ('Fontanería, separador de grasas y climatización', 'Instalador', 'Semanas 8-12',
         'Agua fría y caliente en la cocina, desagües con separador de grasas (la plancha y las freidoras echan mucha) y '
         'climatización de la sala: con la plancha encendida, la cocina a la vista calienta el local'),
        ('Zona de empaquetado y de recogida de los repartidores junto a la puerta', 'Titular', 'Semanas 10-12',
         'Una mesa con las cajas, los cucuruchos de patatas, las salsas y las bolsas, la impresora de comandas y las '
         'tablets de las plataformas, para que los repartidores no crucen la sala ni entren en la cocina'),
        ('Boletín eléctrico, certificado de gas y certificado final de obra', 'Instalador autorizado / Técnico',
         'Durante la obra y al acabarla',
         'El boletín (certificado de la instalación eléctrica) para el contrato de luz, el certificado de la '
         'instalación de gas y el certificado final del técnico. Guárdalos: te los pedirá el ayuntamiento'),
    ]),
    ('F3 - Carne, fritura y sanidad', 'FASE 3: CARNE, FRITURA Y REGISTRO SANITARIO (semanas 6-14)', [
        ('Declaración responsable al registro sanitario autonómico', 'Titular / Gestoría',
         'Antes de la primera prueba de carta',
         'Va al registro sanitario de tu comunidad autónoma (RD 1021/2022). El registro estatal (RGSEAA) sólo aplica '
         'si sirves a otros negocios por encima de lo que permite el art. 3 del mismo real decreto: vender bolas a otros '
         'bares, sólo de forma marginal'),
        ('APPCC: carne picada a 2 °C o menos y la bola salada como preparado de carne', 'Consultor / Titular',
         'Antes de abrir',
         'La carne picada va a 2 °C o menos y los preparados de carne, a 4 °C o menos (RD 1021/2022, art. 4.1). La bola '
         'sin sal es carne picada; salada o aliñada antes de la plancha pasa a preparado de carne (Reglamento (CE) '
         '853/2004, anexo I, 1.13 y 1.15): sala la smash en la plancha. Armario de carne con termómetro y registro'),
        ('Si picas en el local: sólo lo del día y nunca de un día para otro', 'Jefe/a de plancha', 'Desde el primer día',
         'El picado previo sólo vale «con arreglo a las necesidades del despacho diario, no pudiendo conservarse de un '
         'día para otro» (RD 1021/2022, art. 7.2). Calcula los kilos de cada día con la calculadora del pack y pica en '
         'tandas: lo que sobre al cierre no se guarda para mañana'),
        ('Si picas: músculo sin recortes, carne fría y dentro de plazo del sacrificio', 'Jefe/a de plancha',
         'Con cada compra',
         'Sólo músculo esquelético con su grasa, sin recortes ni desperdicios; la carne a 7 °C o menos al picarla y la '
         'picada a 2 °C o menos nada más picarla; picada dentro de los 6 días siguientes al sacrificio o de los 15 si es '
         'vacuno deshuesado y envasado al vacío (RD 1021/2022, art. 7.3, y Reglamento (CE) 853/2004, anexo III, sección '
         'V, capítulos II y III). Pide la fecha de sacrificio en cada albarán'),
        ('Nada de carne madurada para picar', 'Titular', 'Antes de diseñar la carta',
         'No se pica carne madurada más de 15 días: Madrid Salud lo dejó escrito en su informe Inf26008 (febrero de '
         '2026) ante una hamburguesería que servía bolas de carne madurada. La «dry aged burger» que vende internet no '
         'cabe en un plan que vas a enseñar a un inspector'),
        ('Punto de control crítico de la cocción con sonda', 'Consultor / Titular', 'Antes de abrir',
         'En España no hay una temperatura de cocción fijada por ley para la hamburguesa: la decide tu APPCC. La AESAN '
         'recomienda cocinar la carne picada por completo, a 70 °C o más durante al menos 2 minutos, y la smash fina sale '
         'hecha en la plancha; mide con sonda una bola por tanda y anótalo. Si la etiqueta del proveedor pide cocinarla, '
         'no se sirve poco hecha. Nunca prometas el punto en la carta sin un APPCC que lo respalde'),
        ('Recepción de la carne y utensilios de crudo separados', 'Jefe/a de plancha', 'Desde la primera compra',
         'Mide la temperatura de cada entrega y rechaza la que llegue fuera de la que fije tu APPCC. Espátulas, pinzas, '
         'tablas y bandejas de la carne cruda, separadas de las de la hamburguesa hecha, y lavado de manos entre una y '
         'otra'),
        ('Congelar bolas propias: sólo con el equipo y el permiso adecuados', 'Titular', 'Antes de congelar nada',
         'El plan compra y no congela. Si congelas, las bolas van envasadas y etiquetadas con las fechas de elaboración, '
         'congelación y caducidad, en un equipo que las lleve a −18 °C o menos en el centro con un descenso '
         'ininterrumpido (no un arcón de mantenimiento), con registro, descongelación en frío y sin recongelar (RD '
         '1021/2022, art. 5). Con carne picada en el local, confírmalo antes con tu inspector'),
        ('Acrilamida: patatas, temperatura de la freidora y guía de colores', 'Cocinero/a de montaje y freidora',
         'Antes de abrir',
         'Patatas guardadas a más de 6 °C; la fresca, en remojo o escaldada; la congelada, con las instrucciones del '
         'fabricante; freír por debajo de 175 °C; espumar el aceite a menudo; y una guía de colores de las patatas y '
         'del pan tostado a la vista del personal (Reglamento (UE) 2017/2158, anexo II, parte A). Guarda las pruebas de '
         'que lo haces'),
        ('Aceite de fritura: compuestos polares por debajo del 25 % y registro de cambios',
         'Cocinero/a de montaje y freidora', 'Antes de abrir',
         'Los compuestos polares tienen que quedar por debajo del 25 %, no se añade al baño nada ajeno al aceite y el usado no vuelve '
         'a la cocina (Orden de 26 de enero de 1989, arts. 6.3 y 9). La norma no te obliga a tener un medidor: tu APPCC '
         'elige tiras, medidor o cambio por frecuencia. Filtra, rellena y anota cada cambio'),
        ('Salsas cocinadas y elaboraciones en caliente: 63 °C, enfriado y recalentado', 'Cocinero/a de montaje y freidora',
         'Antes de abrir',
         'En caliente, a 63 °C o más; lo que se guarda, enfriado de 60 a 10 °C en menos de 2 horas, y recalentado a '
         '74 °C durante 15 segundos en el centro (RD 1086/2020, art. 30, en la redacción del RD 1021/2022)'),
        ('Verdura cortada a 4 °C o menos en la línea de montaje', 'Cocinero/a de montaje y freidora', 'Antes de abrir',
         'La lechuga, el tomate y la cebolla cortados y listos para montar van a 4 °C o menos (RD 1021/2022, art. 4.1): '
         'en la mesa refrigerada, en cubetas tapadas, y lo que se corta cada día'),
        ('Trazabilidad y registros: lotes, fechas y temperaturas', 'Titular', 'Desde la primera compra',
         'Lote, proveedor y fecha de sacrificio o de envasado de la carne; lote del pan, el queso, las patatas y las '
         'salsas; temperaturas del armario de carne, de la mesa refrigerada y de la sonda de cocción; cambios de aceite'),
        ('Fichas técnicas de cada hamburguesa con sus alérgenos', 'Jefe/a de plancha', 'Antes de abrir',
         'Gramos de bola, pan, queso, salsas y guarnición de cada producto, con sus alérgenos: el pan (gluten, huevo, '
         'leche y sésamo si lleva semillas; soja en algunos), el queso (leche), las salsas (huevo y mostaza), los '
         'encurtidos (mostaza y sulfitos según la marca) y los rebozados (gluten, huevo y leche). Con la calculadora del '
         'pack, el coste de cada una'),
    ]),
    ('F4 - Personal y alérgenos', 'FASE 4: PERSONAL, FORMACIÓN, PREVENCIÓN Y ALÉRGENOS (semanas 6-14)', [
        ('Copiar la tabla salarial del convenio provincial de hostelería', 'Gestoría', 'Semana 10',
         'Las hamburgueserías van al convenio provincial de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito '
         'Estatal para el sector de Hostelería las nombra expresamente. Pon su salario más bajo en la hoja de Supuestos '
         'del plan'),
        ('Contratar al cocinero de plancha ANTES de la obra', 'Titular', 'Semanas 6-8',
         'La plancha es el cuello de botella del servicio: que quien la va a llevar pruebe el modelo y opine sobre la '
         'línea de montaje antes de cerrar la cocina. Si sólo el titular sabe llevarla, una baja la cierra'),
        ('Contratos por escrito a jornada completa y parcial', 'Gestoría', 'Antes de abrir',
         'Con su horario y su grupo del convenio. Una factura de «autónomo» con tu horario y tu dirección es falso '
         'autónomo (art. 1.1 del Estatuto de los Trabajadores)'),
        ('Registro de jornada', 'Titular', 'Desde el primer contrato',
         'Obligatorio para toda la plantilla (art. 34.9 ET), también a tiempo parcial. Acuerda con tu gestoría cómo '
         'llevarlo y consérvalo'),
        ('Cuadrante de los dos servicios y de las noches del viernes y el sábado', 'Titular', 'Semana 12',
         'Comidas y cenas de martes a domingo, con el lunes de cierre; el viernes y el sábado por la noche hacen falta '
         'unas seis personas: dos en la plancha, una en montaje y freidora, una en el mostrador, una empaquetando y una '
         'llevando bandejas'),
        ('Reparto propio: sólo con contrato laboral', 'Gestoría', 'Si repartes tú',
         'El repartidor propio es hostelería (ALEH VI, art. 4) y trabaja por cuenta ajena; en el reparto organizado por '
         'una plataforma digital, la ley presume la relación laboral (ET, disposición adicional 23.ª). Nunca con '
         '«autónomos»'),
        ('Formación de manipuladores con la carne picada y la freidora', 'Titular', 'Antes de abrir',
         'La da y la acredita la empresa (no hay un documento oficial que sacar): higiene, temperaturas de la carne '
         'picada, la sonda de cocción, el aceite de la freidora, alérgenos y contacto cruzado'),
        ('Formación de la línea: gramos de la bola, smash y montaje', 'Jefe/a de plancha', 'Antes de abrir',
         'Todo el equipo porciona, aplasta y monta igual: pesa 10 bolas de cada persona y corrige. La bola que pesa de '
         'más es food cost que no sale en el escandallo'),
        ('Plan de prevención de riesgos laborales', 'Servicio de prevención', 'Antes de abrir',
         'Obligatorio (Ley 31/1995): quemaduras de la plancha y de las freidoras, resbalones con la grasa, cortes y '
         'cargas'),
        ('Vigilancia de la salud de la plantilla', 'Servicio de prevención', 'Al contratar',
         'Reconocimientos médicos ofrecidos a cada persona que entra'),
        ('Información de alérgenos por escrito o de palabra con registro', 'Titular', 'Antes de abrir',
         'Por escrito en la carta o, si la das de palabra, registrada por escrito o en formato electrónico en el local, '
         'accesible y con un cartel que diga dónde pedirla (RD 126/2015, arts. 4.1.b y 6.5.a)'),
        ('Matriz de los 14 alérgenos con el pan, las salsas y los rebozados', 'Jefe/a de plancha', 'Antes de abrir',
         'Una fila por producto y una columna por alérgeno, con lo que más se olvida: el sésamo del pan de semillas, el '
         'huevo y la mostaza de las salsas, los sulfitos de los encurtidos y el gluten de los rebozados. Revísala cada '
         'vez que cambie un proveedor o una receta'),
        ('No prometer «sin gluten» con pan de trigo, freidora compartida y plancha común', 'Titular',
         'Antes de imprimir la carta',
         '«Sin gluten» sólo con 20 mg/kg o menos tal como se vende (Reglamento de Ejecución (UE) 828/2014). Con pan de '
         'trigo en la misma plancha y una freidora que comparte aceite con los rebozados, informa del alérgeno y de las '
         'trazas y ofrece un pan sin gluten aparte sin prometerlo'),
    ]),
    ('F5 - Carta, marca y delivery', 'FASE 5: CARTA, MARCA, DELIVERY Y PROVEEDORES (semanas 8-16)', [
        ('Carta corta de unas 14 referencias y el menú', 'Jefe/a de plancha', 'Semana 8',
         'Seis smash (simple, doble, triple, con bacon, estilo Oklahoma y la de la casa), un pollo crujiente, una vegetal, '
         'patatas clásicas y cargadas, batido, postre, el menú de doble con patatas y bebida y el pedido para dos: las 14 '
         'filas del escandallo de la calculadora. Aparte, tres salsas, refrescos, cerveza de tirador y agua. Una carta de '
         '12 hamburguesas y 6 salsas llena la cámara de pan y de ingredientes que se tiran'),
        ('Escandallo de cada hamburguesa y del menú por canal', 'Jefe/a de plancha', 'Semanas 10-14',
         'Con la calculadora de la carne, las patatas y el escandallo del pack: el coste de cada producto, siempre sobre '
         'el precio SIN IVA, y el margen en sala, para llevar y en plataforma. En plataforma, el margen del menú cae '
         'casi un tercio'),
        ('IVA de la carta para llevar: la comida al 10 %, la cerveza y los refrescos al 21 %',
         'Gestoría / Titular', 'Antes de abrir',
         'En sala, todo al 10 % (Ley 37/1992, art. 91.Uno.2.2.º). Para llevar y a domicilio, la comida al 10 %, pero la '
         'cerveza y los refrescos con azúcares o edulcorantes añadidos, también los zero, van al 21 % (art. '
         '91.Uno.1.1.º a y b). Configúralo así en el TPV y en cada plataforma'),
        ('El batido y el menú para llevar: confírmalos con tu gestoría', 'Gestoría', 'Antes de abrir',
         'El batido de leche no es una bebida refrescante: el plan lo lleva al 10 %, pero pide a tu gestoría que lo '
         'confirme. El menú que sale del local se desglosa por componentes en el tique: la comida al 10 % y la bebida a '
         'su tipo'),
        ('Envases: lo que no se consume, sin coste; el plástico de un solo uso, cobrado', 'Titular', 'Antes de abrir',
         'El cliente puede llevarse lo que no consuma sin coste, y hay que avisarlo de forma visible, mejor en la carta '
         '(Ley 1/2025, art. 8). Los recipientes de plástico de un solo uso para llevar se cobran aparte en el tique (Ley '
         '7/2022, art. 55): pregunta a tu proveedor cuáles de tus envases lo son'),
        ('Dos proveedores de carne con su ficha técnica', 'Titular', 'Semanas 8-12',
         'Con un solo proveedor, una mala semana te deja sin carta. Pide a cada uno la ficha del blend (la mezcla de '
         'cortes), el porcentaje de grasa (el caso trabaja con un 20 %), la fecha de sacrificio o de envasado en cada '
         'albarán, la temperatura de entrega y el precio por escrito: el plan lo estima'),
        ('Proveedores de pan y de patatas con su ficha técnica y sus alérgenos', 'Titular', 'Semanas 8-12',
         'El pan de hamburguesa (brioche o de patata) con su lista de alérgenos y su factura al 10 %, que no es pan '
         'común; la patata congelada con su ficha (variedad y azúcares, para la acrilamida) y sus instrucciones de '
         'fritura'),
        ('Contrato y alta en las plataformas de reparto con un techo', 'Titular', 'Antes de abrir',
         'Lee la comisión (del 13 al 35 % más IVA según la plataforma y la zona), cada cuánto liquidan, quién paga las '
         'promociones y el coste de las tablets. Fija un techo: en este plan, el 24 % de las ventas'),
        ('Precios para la plataforma y para la recogida en el local', 'Titular', 'Antes de abrir',
         'Calcula el margen del menú en la plataforma con su comisión, el recargo y la caja; la recogida en el local '
         'no paga comisión: empújala con la web y el teléfono. La hamburguesa viaja bien; las patatas, peor: cucurucho '
         'ventilado y fritas al final'),
        ('Pedidos: los alérgenos antes de comprar y el pedido en su temperatura', 'Titular', 'Antes del primer pedido',
         'En la venta a distancia, la información de alérgenos tiene que estar disponible antes de que el cliente '
         'compre (Reglamento (UE) 1169/2011, art. 14): la misma ficha en cada plataforma y en tu web. Y el pedido viaja '
         'en cajas y bolsas que mantengan la temperatura (RD 1021/2022, art. 4.3)'),
        ('Marca en la OEPM, identidad, fotos y web con la carta y los alérgenos', 'Titular / Diseñador/a',
         'Semanas 2-14',
         'Comprueba antes que el nombre no está registrado en tu clase (servicios de restauración). Fotos y vídeos '
         'reales de la plancha y de las hamburguesas; web con la carta, los alérgenos, el horario, los pedidos para '
         'recoger y la cláusula de protección de datos de cada canal'),
        ('Ficha de Google Business, redes con vídeo y fechas fuertes', 'Titular', 'Antes de abrir',
         'Horario de comidas y cenas, fotos de la plancha y respuesta a cada reseña. En el calendario, la vuelta de '
         'septiembre, el fútbol y Halloween en octubre y el buen tiempo y el fin de curso en mayo y junio'),
        ('Música ambiental: licencias de SGAE y AGEDI-AIE', 'Titular', 'Antes de abrir',
         'Son dos licencias de propiedad intelectual, distintas de la municipal: pide las dos si pones música'),
    ]),
    ('F6 - Apertura y 90 días', 'FASE 6: APERTURA Y PRIMEROS 90 DÍAS', [
        ('Abrir en enero, el Mes 1 del plan', 'Titular', 'Mes 1',
         'El plan arranca en enero y la rampa va de enero a abril; enero es el mes más flojo del año (el cierre de 10 '
         'días y la cuesta de enero) y agosto baja con la ciudad vacía: por eso el fondo de maniobra cuenta. Si abres en '
         'otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Desinsectación, desratización y desinfección (DDD)', 'Empresa del ROESB', 'Antes de abrir',
         'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
        ('Plan de limpieza de la plancha, las freidoras y la línea de montaje', 'Titular', 'Antes de abrir',
         'La plancha y sus raspadores, las freidoras y su filtrado, los filtros de la campana extractora, la mesa '
         'refrigerada, el armario de carne y la zona de empaquetado, con su registro'),
        ('Servicios de prueba con la carta completa', 'Jefe/a de plancha', 'Semana previa',
         'Varios servicios de prueba para ajustar los gramos de bola, los tiempos de la plancha, el montaje y el '
         'empaquetado de los pedidos antes de abrir'),
        ('Comprobar temperaturas y registros del primer día', 'Titular', 'Día 1',
         'Armario de carne, mesa refrigerada, sonda de cocción, temperatura de la freidora y la hoja de limpieza; '
         'corrige cualquier desviación antes de servir'),
        ('Inspección sanitaria: APPCC y registros a mano', 'Titular', 'Desde el día 1',
         'Albaranes con la fecha de sacrificio o de envasado de la carne, temperaturas, sonda de cocción, cambios de '
         'aceite, fichas de alérgenos, trazabilidad, limpieza, formación y DDD'),
        ('Pesar 10 bolas, medir la merma y las raciones de patata y recalcular', 'Jefe/a de plancha', 'Semanas 1-4',
         'Pesa 10 bolas antes y después de la plancha (la merma de cocción), cuenta las raciones de patata que salen de '
         'cada kilo y lleva las medias a la calculadora del pack; compara después tu consumo real (compras de comida ÷ '
         'ventas de comida del mes) con el 28 % del plan'),
        ('Medir los compuestos polares y anotar cada cambio de aceite', 'Cocinero/a de montaje y freidora',
         'Cada servicio',
         'Con tiras o medidor, o por la frecuencia que fije tu APPCC; anota cuántas raciones aguanta cada cuba y lleva '
         'el dato a la calculadora. El aceite usado, al gestor autorizado'),
        ('Mantenimiento de la plancha, la instalación de gas, el frío y la campana extractora',
         'Titular / Empresa de mantenimiento', 'Desde el mes 1',
         'Revisión de la plancha y de la instalación de gas (inspección o revisión cada 5 años: RD 919/2006), el '
         'frigorista para el armario de carne y la mesa refrigerada, y la limpieza de la campana extractora y del '
         'conducto al menos una vez al año (Madrid, Ordenanza 4/2021, art. 23)'),
        ('Calibrar la sonda de cocción', 'Jefe/a de plancha', 'Según su fabricante',
         'En agua con hielo o como diga el fabricante, y anotado: una sonda sin calibrar da por hecha una bola que no lo '
         'está'),
        ('Revisar la cuenta de la plataforma cada mes', 'Titular', 'Mensual',
         'Ventas, comisión, promociones y cajas: si la plataforma pasa del 24 % de las ventas o su margen no cubre la '
         'comisión, recorta o sube precio. Reparto propio, sólo con contrato laboral y cuando el volumen lo pague'),
        ('Comparar ventas y costes reales con el plan cada mes', 'Titular', 'Mensual',
         'Comensales al día, ticket, mercancía y personal frente a la cuenta de resultados del Excel; revisa el '
         'escandallo cada vez que cambie el precio de la carne'),
        ('Seguir la tesorería mes a mes y el saldo mínimo', 'Titular', 'Mensual',
         'Enero abre la rampa y es el mes más flojo, y agosto baja: mira el saldo de cada mes antes de un pago grande'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 14, 13, 13, 13], [len(t) for _, _, t in FASES]
assert all(len(n) <= 29 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
