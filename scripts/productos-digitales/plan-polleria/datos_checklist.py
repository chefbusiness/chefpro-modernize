#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura de la Pollería y Asador de Pollos ES 1.0 (F1-camino §4:
12/15/14/13/13/13, mismas filas que la Taquería). Producto nuevo: no hay versión anterior; formato de
`plan-taqueria/datos_checklist.py`. Marco legal: `F1-research-polleria.md` §0-§1 (R) y la lista de tareas obligadas de
R §3 (lo marcado 🟡 va como «compruébalo»). Fuente primaria de cada cita:
  · RDLeg 1175/1990 (tarifas del IAE): epígrafe 677.9 para la venta para llevar («condimentación y venta de alimentos
    para ser consumidos fuera del lugar de elaboración en raciones»); con sala, grupo 671 (por categoría) o 673.2, cuya
    nota común faculta a vender en el propio establecimiento; el 642.5 (comercio al por menor de aves) NO ampara asar;
    exención de cuota, art. 82.1.c del TRLRHL;
  · Ley 12/2012: los restaurantes no están en su anexo → licencia o declaración responsable por la ordenanza municipal;
  · Ordenanza 4/2021 de Calidad del Aire de Madrid (BOCM 16-04-2021), arts. 12, 23 (limpieza ≥ 1/año) y anexo I:
    conducto exclusivo a cubierta, +1 m sobre lo que haya en 15 m y, con combustible sólido (leña o carbón), filtrado
    específico de partículas; fuera de Madrid, la ordenanza de cada ayuntamiento;
  · RD 919/2006, ITC-ICG 07 e ITC-ICG 08: gas por empresa instaladora habilitada, puesta en marcha certificada de cada
    aparato, inspección o revisión cada 5 años;
  · RD 1021/2022: registro autonómico previa declaración responsable, art. 3 (RGSEAA sólo para el suministro a otros
    negocios por encima de lo marginal: ≤ 25 % del volumen anual o ≤ 500 kg a la semana), art. 4.1 (aves ≤ 4 °C,
    despojos de aves ≤ 3 °C, preparados de carne ≤ 4 °C, vegetal cortado listo para consumo ≤ 4 °C), 4.2 (temperatura
    de la etiqueta), 4.3 (transporte), art. 9.2-9.3 (ovoproducto sin cocción, ≤ 8 °C, 24 h, fecha y hora) y art. 11
    («elaboración propia»);
  · RD 1086/2020, art. 30, en la redacción de la disposición final 2.ª del RD 1021/2022: caliente ≥ 63 °C (30.2),
    refrigeradas ≤ 4 °C u ≤ 8 °C con vida útil < 24 h (30.3), enfriamiento de 60 a 10 °C en < 2 h (30.6) y recalentado
    ≥ 74 °C 15 s en el centro en la hora siguiente a sacarlo del frío (30.7). NUNCA «art. 30 del RD 1021/2022». Ninguna
    norma fija la temperatura de cocción del pollo: los 74 °C en el muslo son criterio del APPCC del caso;
  · RD 126/2015, art. 4 (sin envasar o envasado a petición: denominación y alérgenos), art. 5 (envasado por el
    comercio para su venta inmediata: arts. 9 y 10 del Reglamento (UE) 1169/2011 salvo la nutricional) y arts. 4.1.b y
    6.5.a (alérgenos por escrito, o de palabra con registro escrito o electrónico accesible); Reglamento (UE)
    1169/2011, art. 14 (venta a distancia); Reglamento de Ejecución (UE) 828/2014 («sin gluten» ≤ 20 mg/kg: no se
    promete con freidora compartida con las croquetas);
  · Ley 37/1992, art. 91.Uno.1.1.º a y b, 91.Uno.2.2.º y 91.Dos.1.1.º a (para llevar: alcohol y bebidas con azúcares o
    edulcorantes añadidos al 21 %; pan común al 4 %); Ley 1/2025, art. 8 (llevarse lo no consumido, aviso en la carta);
    Ley 7/2022, art. 55 (cobro del envase de plástico de un solo uso);
  · ET arts. 1.1, 34.9 y DA 23.ª (registro de jornada: sin afirmar que sea «digital» por ley); ALEH VI art. 4 (convenio
    provincial de hostelería: no nombra la pollería); Ley 31/1995 (PRL); Ley 18/2022 (SL desde 1 €).
Sin «carné», sin «licencia de apertura», sin «sin gluten» prometido ni restos de la taquería en todo el libro. Cada
tarea: (trámite / acción, responsable, plazo, notas). Pestañas ≤ 29 caracteres. Sesión Claude Code, 29-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — POLLERÍA Y ASADOR DE POLLOS'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Consulta urbanística previa: salida de humos, potencia trifásica y aforo', 'Titular / Técnico',
         'Antes de firmar el alquiler',
         'Pregunta al ayuntamiento si el uso permite un asador de pollos con freidora y sala, si el local admite un '
         'conducto de humos exclusivo hasta la cubierta (en Madrid, que supere en 1 m lo que haya en 15 m: Ordenanza '
         '4/2021, art. 12 y anexo I), qué potencia tiene (¿trifásica?) y qué aforo. Sin salida de humos a cubierta no '
         'hay asador ni freidora'),
        ('Decidir asador de gas o brasa de leña o carbón ANTES de firmar el local', 'Titular',
         'Antes de firmar el alquiler',
         'El asador de gas de espadas (el del plan) cabe en una salida de humos normal, con la instalación por empresa '
         'habilitada (RD 919/2006). El horno de brasa de leña o carbón de la pollería peruana y la parrilla de carbón '
         'piden además filtro de partículas en el conducto (en Madrid, Ordenanza 4/2021, art. 23): pregunta en la '
         'consulta previa si tu local lo admite. Es decisión de producto, no de decoración'),
        ('Decidir el tamaño del asador con la cuenta del domingo', 'Titular', 'Antes de firmar el alquiler',
         'Con la hoja del asador de la calculadora del pack: cuántos pollos vendes el domingo, cuántos caben por carga '
         'y cuántas cargas salen antes de las tres. Con doce espadas caben unos 60 por carga; con ocho, unos 40, y '
         'agosto y los festivos van justos. El asador tiene que caber en el local con su campana extractora'),
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036) en el epígrafe 677.9 del IAE y, con sala, en el 671 o el 673.2', 'Gestoría',
         'Semana 2',
         'El 677.9 cubre la condimentación y venta de comida para consumir fuera del local; con mesas, el grupo 671 '
         '(restaurante, por categoría) o el 673.2, que facultan a vender en el propio local (RDLeg 1175/1990). NUNCA '
         'sólo el 642.5 («pollería» de aves crudas): no ampara asar. Confírmalo con tu gestoría. Exento de cuota con '
         'una cifra de negocio inferior a 1 millón de euros (art. 82.1.c de la Ley de Haciendas Locales)'),
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
         'Lleva el plan financiero completo, con la tesorería mes a mes. Pide también oferta de leasing o renting del '
         'asador, el frío y la freidora y de una línea ICO'),
        ('Seguro de responsabilidad civil y multirriesgo con incendio', 'Corredor de seguros', 'Antes de la obra',
         'RC de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la aseguradora que trabajas '
         'con asador de pollos y freidora a gas'),
    ]),
    ('F2 - Local, humos y gas', 'FASE 2: LOCAL, SALIDA DE HUMOS, GAS Y LICENCIA (semanas 3-14)', [
        ('Elegir el local: unos 80 m² con salida de humos a cubierta posible', 'Titular', 'Semanas 3-6',
         'Obrador y zona de asado de unos 25 m² a la vista, mostrador con vitrina caliente, sala de 16 plazas en mesa y '
         '4 en barra, aseos (uno adaptado) y almacén. Barrio residencial con paso de familias el fin de semana y '
         'cómodo para parar el coche y recoger el encargo'),
        ('Comprobar la potencia eléctrica y la acometida de gas', 'Técnico / Distribuidora', 'Antes de firmar',
         'Freidora, frío, extracción, climatización y lavavajillas en la luz (trifásica si el asador es eléctrico: '
         'ampliarla tarda de 4 a 8 semanas); asador y fogón en el gas, natural o envasado. Pregunta plazo y coste a la '
         'distribuidora'),
        ('Comprobar con el técnico el recorrido del conducto hasta cubierta', 'Técnico', 'Antes de firmar',
         'Conducto exclusivo, continuo y estanco hasta la cubierta, por patio o fachada, con el permiso de la comunidad '
         'de propietarios si cruza zonas comunes. Con doce espadas, la extracción ronda los 1.800-2.200 m³/h'),
        ('Negociar el alquiler: carencia de obra y fianza', 'Titular', 'Antes de firmar',
         'El plan cuenta dos meses de renta antes de abrir y dos de fianza. Pide carencia mientras duran la obra, el '
         'conducto y el gas'),
        ('Contrato de arrendamiento con el uso de asador con salida de humos', 'Titular / Abogado', 'Semana 6',
         'Que diga «restaurante» o «asador de pollos con cocina» y que autorice la obra del conducto y la salida de '
         'humos a cubierta'),
        ('Encargar el proyecto técnico de la actividad y de la salida de humos', 'Arquitecto/a o ingeniero/a',
         'Semanas 6-8',
         'Distribución del obrador y del mostrador, potencia, aforo, ventilación, accesibilidad, la instalación de gas '
         'y el conducto a cubierta. Fuera de Madrid, pide la ordenanza de humos y de calidad del aire de tu '
         'ayuntamiento'),
        ('Licencia o declaración responsable de la actividad', 'Técnico / Ayuntamiento', 'Antes de la obra',
         'Las pollerías y los asadores de pollos no están en el anexo de la Ley 12/2012: van por el régimen de tu '
         'ayuntamiento, licencia o declaración responsable según su ordenanza. Pregunta cuál te toca en la consulta '
         'previa'),
        ('Licencia, declaración o comunicación previa de la obra', 'Técnico / Ayuntamiento',
         'Semanas 6-8, antes de empezar la obra',
         'La obra y el conducto van por su propio trámite municipal: pregunta en la consulta previa qué título piden'),
        ('Gas por empresa instaladora habilitada y certificado del asador', 'Instalador de gas habilitado',
         'Durante la obra',
         'Certificado de la instalación, puesta en marcha certificada del asador, la freidora y el fogón e inspección '
         '(red) o revisión (gas envasado) cada 5 años (RD 919/2006, ITC-ICG 07 e ITC-ICG 08). Un técnico de conexión '
         'sin certificado no vale'),
        ('Conducto exclusivo a cubierta y filtro de partículas si hay leña o carbón', 'Instalador / Técnico',
         'Semanas 8-12',
         'Ejemplo de Madrid (Ordenanza 4/2021): conducto exclusivo que supere en 1 m lo que haya en 15 m (art. 12 y '
         'anexo I) y, con leña, carbón u otro combustible sólido, sistemas específicos de filtrado de partículas (art. '
         '23). Con asador de gas, el conducto normal'),
        ('Obra del obrador, el mostrador y la sala: superficies lavables', 'Constructor', 'Semanas 8-12',
         'Paredes alicatadas, suelo antideslizante (también alrededor del asador), falsos techos lavables, lavamanos de '
         'accionamiento no manual, aseos (uno adaptado) y aislamiento acústico si hay vecinos'),
        ('Fontanería, separador de grasas y climatización', 'Instalador', 'Semanas 8-12',
         'Agua fría y caliente en el obrador, desagües con separador de grasas (el asador y la freidora echan mucha) y '
         'climatización de la sala'),
        ('Campana extractora sobre el asador, la freidora y el fogón', 'Instalador', 'Semanas 10-12',
         'Campana extractora con motor y filtros de grasa que cubra toda la línea de fuego, conectada al conducto '
         'exclusivo. Pide al instalador el caudal y el plan de limpieza de los filtros'),
        ('Instalación eléctrica trifásica, boletín y certificado final de obra', 'Instalador autorizado / Técnico',
         'Durante la obra y al acabarla',
         'El boletín (certificado de la instalación) para el contrato de luz y el certificado final del técnico. '
         'Guárdalos con el del gas: te los pedirá el ayuntamiento'),
        ('Rótulo y fachada con el teléfono de encargos', 'Titular / Rotulista', 'Semanas 10-14',
         'Pregunta en la consulta previa si tu ayuntamiento pide un permiso aparte para el rótulo. Pon el teléfono de '
         'encargos bien visible desde la calle'),
    ]),
    ('F3 - Cocina, asador y sanidad', 'FASE 3: OBRADOR, ASADOR Y REGISTRO SANITARIO (semanas 6-14)', [
        ('Comprar el asador, la vitrina caliente, la freidora y el fogón', 'Titular', 'Semanas 6-8',
         'Asador de pollos de gas de doce espadas (de 4.373 a 5.967 € sin IVA en catálogo, espadas aparte), vitrina '
         'caliente que mantenga 63 °C o más, freidora doble y fogón. Pide ficha técnica, pollos por espada, consumo de '
         'gas, plazo de entrega y montaje'),
        ('Comprar el frío: armarios de pollo crudo y adobado, congelador y vitrina', 'Titular', 'Semanas 8-10',
         'Armarios para el pollo crudo y el adobado a 4 °C o menos, congelador y una vitrina refrigerada que mantenga '
         'las guarniciones del mostrador a 4 °C o menos'),
        ('Declaración responsable al registro sanitario autonómico', 'Titular / Gestoría',
         'Antes de la primera prueba de carta',
         'Va al registro sanitario de tu comunidad autónoma (RD 1021/2022). El registro estatal (RGSEAA) sólo aplica '
         'si sirves a otros negocios por encima de lo que permite el art. 3 del mismo real decreto (venta marginal, '
         'localizada y restringida: por ejemplo, pollo asado o croquetas a un bar de otro titular)'),
        ('APPCC del pollo crudo: cámara a 4 °C o menos y mollejas a 3 °C o menos', 'Consultor / Titular',
         'Antes de abrir',
         'La carne de aves va a 4 °C o menos, los despojos de aves a 3 °C o menos y el pollo adobado crudo es un '
         'preparado de carne: también a 4 °C o menos (RD 1021/2022, art. 4.1). Anota la temperatura de cada recepción'),
        ('Mesa de crudo separada y el pollo crudo sin lavar', 'Maestro/a asador', 'Antes de abrir',
         'Espetar y adobar en una mesa de acero inoxidable SEPARADA de la de servir, con sus tablas y utensilios. El '
         'pollo crudo no se lava: salpica y contamina la zona'),
        ('APPCC del asado: sonda a 74 °C o más en el muslo y registro', 'Maestro/a asador', 'Antes de abrir',
         'Ninguna norma fija la temperatura de cocción del pollo: tu APPCC la fija. El caso pide 74 °C o más en la '
         'parte más gruesa del muslo, con sonda en cada carga y registro. Dorado por fuera no quiere decir hecho junto '
         'al hueso'),
        ('Vitrina caliente a 63 °C o más con hora límite propia', 'Dependiente/a de mostrador', 'Antes de abrir',
         'El pollo asado en vitrina, a 63 °C o más (RD 1086/2020, art. 30, en la redacción del RD 1021/2022). Ninguna '
         'norma fija cuánto puede estar en la vitrina: la hora límite la fija tu APPCC y se anota'),
        ('Pollo sobrante: enfriado de 60 a 10 °C en menos de 2 horas y su destino', 'Asador/a-cocinero/a',
         'Antes de abrir',
         'Lo que sobra al cierre o se mantiene a 63 °C o más, o se enfría de 60 a 10 °C en menos de 2 horas y se '
         'reaprovecha al día siguiente (croquetas, ensalada de pollo) recalentando a 74 °C durante 15 segundos en el '
         'centro (RD 1086/2020, art. 30, en la redacción del RD 1021/2022). Anota cuántos pollos sobran cada día'),
        ('Alioli, mayonesa, ensaladilla y cremas: ovoproducto, 8 °C y 24 horas', 'Asador/a-cocinero/a',
         'Antes de abrir',
         'Lo que lleva huevo y no se cocina se hace con ovoproducto de un establecimiento autorizado, a 8 °C o menos, se '
         'consume en 24 horas y se registra la fecha y la hora de elaboración (RD 1021/2022, art. 9.2 y 9.3). Nada de '
         'huevo crudo'),
        ('Etiqueta completa en lo que envases antes de que el cliente lo pida', 'Titular', 'Antes de abrir',
         'El pollo que embolsas al pedirlo o el encargo preparado a nombre del cliente llevan denominación y alérgenos '
         '(RD 126/2015, art. 4). Las bandejas de medio pollo, croquetas o ensaladilla ya cerradas en la vitrina llevan '
         'TODA la información del Reglamento (UE) 1169/2011 menos la nutricional: ingredientes, alérgenos resaltados, '
         'peso, fecha y conservación (art. 5)'),
        ('Trazabilidad y registros: lotes, temperaturas y proveedores', 'Titular', 'Desde la primera compra',
         'Lote, fecha y temperatura de recepción del pollo, temperaturas del frío, de la sonda y de la vitrina, '
         'enfriado del sobrante y proveedor de cada materia prima'),
        ('Fichas técnicas por producto con sus alérgenos', 'Maestro/a asador', 'Antes de abrir',
         'Adobo (soja y gluten si lleva sillao o cerveza; sulfitos si lleva vino), alioli y ensaladilla (huevo), '
         'croquetas (gluten, leche y huevo), cremas peruanas (huevo, leche y cacahuete según receta) y patata pelada '
         'envasada con conservante (sulfitos). Con la calculadora del pack, el coste de cada uno'),
        ('Alérgenos en la venta por plataforma o por tu web', 'Titular', 'Antes de darte de alta',
         'En la venta a distancia, la información de alérgenos tiene que estar disponible antes de que el cliente '
         'compre (Reglamento (UE) 1169/2011, art. 14). Revisa la ficha de cada producto en cada plataforma'),
        ('Temperatura de los pedidos que salen del local', 'Titular', 'Antes del primer pedido',
         'Bolsas térmicas y envases que mantengan la temperatura durante el transporte (RD 1021/2022, art. 4.3), '
         'también en el reparto de la plataforma; el pollo entero viaja bien, las patatas fritas no'),
    ]),
    ('F4 - Personal y alérgenos', 'FASE 4: PERSONAL, FORMACIÓN, PREVENCIÓN Y ALÉRGENOS (semanas 10-14)', [
        ('Copiar la tabla salarial del convenio provincial de hostelería', 'Gestoría', 'Semana 10',
         'La pollería va al convenio provincial de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal para '
         'el sector de Hostelería no la nombra, pero incluye los restaurantes y el reparto de comidas preparadas. Pon '
         'su salario más bajo en la hoja de Supuestos del plan'),
        ('Contratos por escrito a jornada completa y parcial', 'Gestoría', 'Antes de abrir',
         'Con su horario y su grupo del convenio. Una factura de «autónomo» con tu horario y tu dirección es falso '
         'autónomo (art. 1.1 del Estatuto de los Trabajadores)'),
        ('Contratar al segundo asador antes de abrir', 'Titular', 'Semanas 10-12',
         'Que aprenda contigo a espetar, cargar, sondear y trinchar antes de abrir: si sólo tú sabes llevar el asador, '
         'una baja cierra el domingo, que es un tercio de la semana'),
        ('Registro de jornada', 'Titular', 'Desde el primer contrato',
         'Obligatorio para toda la plantilla (art. 34.9 ET), también a tiempo parcial. Acuerda con tu gestoría cómo '
         'llevarlo y consérvalo'),
        ('Cuadrante del domingo y de los festivos', 'Titular', 'Semana 12',
         'De martes a domingo al mediodía y las cenas de jueves a sábado, con el lunes de cierre. El domingo de 11:00 a '
         '15:30 hacen falta unas seis personas: el maestro asador, el segundo asador, el mostrador, la sala, el '
         'refuerzo y el ayudante. Los festivos, como un domingo'),
        ('Reparto propio: sólo con contrato laboral', 'Gestoría', 'Si repartes tú',
         'El repartidor propio es hostelería (ALEH VI, art. 4) y trabaja por cuenta ajena; en el reparto organizado por '
         'una plataforma digital, la ley presume la relación laboral (ET, disposición adicional 23.ª). Nunca con '
         '«autónomos»'),
        ('Formación de manipuladores de alimentos', 'Titular', 'Antes de abrir',
         'La da y la acredita la empresa (no hay un documento oficial que sacar): higiene, crudo y cocinado separados, '
         'temperaturas de la sonda, la vitrina y el enfriado, ovoproducto, alérgenos y contacto cruzado'),
        ('Formación del asador: espetar, cargar, sondear y trinchar', 'Titular', 'Antes de abrir',
         'Calibre y bridado del pollo, espetado sin dejar huecos, orden de carga, sonda en el muslo y trinchado en '
         'medios y cuartos: es inversión, no gasto'),
        ('Plan de prevención de riesgos laborales', 'Servicio de prevención', 'Antes de abrir',
         'Obligatorio (Ley 31/1995): quemaduras del asador, las espadas calientes y la freidora, cortes al trinchar y '
         'al espetar, gas, calor y cargas'),
        ('Vigilancia de la salud de la plantilla', 'Servicio de prevención', 'Al contratar',
         'Reconocimientos médicos ofrecidos a cada persona que entra'),
        ('Información de alérgenos por escrito o de palabra con registro', 'Titular', 'Antes de abrir',
         'Por escrito en la carta o, si la das de palabra, registrada por escrito o en formato electrónico en el local, '
         'accesible y con un cartel que diga dónde pedirla (RD 126/2015, arts. 4.1.b y 6.5.a)'),
        ('Cartel de alérgenos en el mostrador', 'Dependiente/a de mostrador', 'Antes de abrir',
         'Cada adobo, salsa y guarnición con sus alérgenos a la vista del cliente: soja y gluten del adobo, huevo del '
         'alioli, leche y cacahuete de las cremas según tu receta. Revísalo cada vez que cambie una receta'),
        ('No prometer «sin gluten» con freidora compartida', 'Titular', 'Antes de imprimir la carta',
         '«Sin gluten» sólo con 20 mg/kg o menos tal como se vende (Reglamento de Ejecución (UE) 828/2014). El pollo '
         'asado sin adobo con gluten no lo lleva por receta, pero las patatas fritas en la misma freidora que las '
         'croquetas rompen la promesa: informa del alérgeno y de las trazas, no lo prometas'),
    ]),
    ('F5 - Carta, marca y encargos', 'FASE 5: CARTA, MARCA, ENCARGOS Y PROVEEDORES (semanas 8-16)', [
        ('Decidir el tipo de pollería y su carta', 'Titular', 'Semana 8',
         'Asador solo para llevar de fin de semana, pollería-asador de barrio con sala (este plan), pollo al ast con '
         'allioli y patates rostides, o pollería peruana con horno de brasa y cremas: cada una con otra inversión, otro '
         'local y otro margen. Para un restaurante peruano de mesa, la Guía Restaurante Peruano de AI Chef Pro'),
        ('Carta corta con combos y su escandallo', 'Maestro/a asador', 'Semanas 10-14',
         'Escandalla el pollo entero, el medio y el cuarto y cada combo (con patatas, con croquetas, el menú de sala y '
         'el familiar del domingo): el pollo solo deja poco, el margen está en lo que lo acompaña. Usa la calculadora '
         'del pollo, el asador y el escandallo del pack'),
        ('IVA de la carta para llevar: pollo al 10 %, cerveza y refrescos azucarados al 21 %', 'Gestoría / Titular',
         'Antes de abrir',
         'En sala, todo al 10 % (Ley 37/1992, art. 91.Uno.2.2.º). Para llevar y por plataforma, la comida al 10 %, pero '
         'la cerveza, el vino y los refrescos y zumos con azúcares o edulcorantes añadidos van al 21 % (art. '
         '91.Uno.1.1.º a y b); el pan común que vendas suelto, al 4 % (91.Dos.1.1.º a). Configúralo así en el TPV y en '
         'cada plataforma'),
        ('Aviso en la carta: el cliente puede llevarse lo que no consuma', 'Titular', 'Antes de abrir',
         'Sin coste, salvo el del envase de plástico de un solo uso si lo hay, y avisado de forma visible, mejor en la '
         'carta (Ley 1/2025, art. 8). Ten envases para ello'),
        ('Cobro aparte del envase de plástico de un solo uso', 'Titular', 'Antes de abrir',
         'Los recipientes de plástico de un solo uso para llevar se cobran aparte en el tique (Ley 7/2022, art. 55). '
         'Las bandejas de cartón sin recubrimiento de plástico no lo son; la bolsa de pollo con lámina y la bandeja de '
         'aluminio, pregúntalo a tu proveedor'),
        ('Dos proveedores de pollo con calibre fijo y temperatura de recepción', 'Titular', 'Semanas 8-12',
         'Pollo de asar de calibre fijo (1,4-1,5 kg en canal), recibido a 4 °C o menos y anotado. El precio del pollo se '
         'movió un 10-12 % en un año: dos proveedores y el precio por escrito. Un calibre irregular descuadra las cargas '
         'y el escandallo'),
        ('Proveedores de patata, aceite, envases y bebida', 'Titular', 'Semanas 10-14',
         'Patata congelada o fresca (la fresca baja el coste pero pide pelado y corte), aceite de girasol alto oleico, '
         'bolsas térmicas y envases. El plan los estima con precios de referencia: pon los tuyos'),
        ('Gestor autorizado del aceite y de la grasa de la bandeja de goteo', 'Titular', 'Antes de abrir',
         'Contrato con un gestor autorizado que retire el aceite de la freidora y la grasa del asador con certificado '
         'de cada recogida. Nunca por el desagüe'),
        ('Sistema de encargos: teléfono, WhatsApp y hora de recogida', 'Titular', 'Antes de abrir',
         'Encargos con nombre, teléfono y hora de recogida, cerrados el sábado para el domingo: con ellos sabes cuántos '
         'pollos cargar. Un cartel en el mostrador y el teléfono en las bolsas'),
        ('Contrato y alta en las plataformas de reparto', 'Titular', 'Antes de abrir',
         'Lee la comisión (del 13 al 35 % más IVA según la plataforma y la zona), cada cuánto liquidan, quién paga las '
         'promociones y el coste de la tablet. Fija un techo: en este plan, el 11 % de las ventas. Recoger en el '
         'mostrador no paga comisión: empújalo con precio'),
        ('Registro de la marca en la OEPM', 'Titular', 'Semanas 2-8',
         'Comprueba antes que el nombre no está registrado en tu clase (servicios de restauración)'),
        ('Identidad, fotos y web con la carta, los alérgenos y los encargos', 'Diseñador/a', 'Semanas 8-14',
         'Fotos reales del asador y de los combos; web con la carta, los alérgenos, el horario, el teléfono de encargos '
         'y la cláusula de protección de datos de cada canal'),
        ('Ficha de Google Business, redes y música ambiental', 'Titular', 'Antes de abrir',
         'Horario del mediodía y de las cenas, fotos del asador y respuesta a cada reseña. Si pones música, pide las '
         'dos licencias de propiedad intelectual (SGAE y AGEDI-AIE), distintas de la municipal'),
    ]),
    ('F6 - Apertura y 90 días', 'FASE 6: APERTURA Y PRIMEROS 90 DÍAS', [
        ('Abrir en enero, el Mes 1 del plan', 'Titular', 'Mes 1',
         'El plan arranca en enero y la rampa cae sobre los meses más flojos, enero y febrero: por eso el fondo de '
         'maniobra cuenta. Si abres en otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Desinsectación, desratización y desinfección (DDD)', 'Empresa del ROESB', 'Antes de abrir',
         'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
        ('Plan de limpieza del obrador, el asador y la vitrina', 'Titular', 'Antes de abrir',
         'Asador, espadas y bandeja de goteo, freidora, filtros de la campana extractora, vitrina caliente, mesa de '
         'crudo y frío, con su registro'),
        ('Pruebas de carga del asador con la carta completa', 'Maestro/a asador', 'Semana previa',
         'Varias cargas de prueba para ajustar el adobo, el tiempo de asado, la sonda y el trinchado, y un domingo de '
         'ensayo con encargos de amigos antes de abrir'),
        ('Comprobar temperaturas y registros del primer día', 'Titular', 'Día 1',
         'Cámara del pollo, sonda de cada carga, vitrina caliente, enfriado del sobrante, ovoproducto y la hoja de '
         'limpieza; corrige cualquier desviación antes de servir'),
        ('Inspección sanitaria: APPCC y registros a mano', 'Titular', 'Desde el día 1',
         'Fichas de alérgenos, etiquetas de lo envasado, trazabilidad, registros de temperatura, de enfriado y de '
         'limpieza, formación y DDD'),
        ('Calendario de limpieza de la campana extractora y del conducto', 'Titular / Empresa de mantenimiento',
         'Desde el mes 1',
         'Al menos una vez al año (Madrid, Ordenanza 4/2021, art. 23); el plan cuenta dos por la grasa del asador. Los '
         'filtros de grasa, con la frecuencia que fije tu plan de limpieza'),
        ('Revisión del gas cada 5 años y mantenimiento anual del asador', 'Instalador de gas habilitado', 'Calendario',
         'Inspección periódica (red) o revisión (gas envasado) cada 5 años (RD 919/2006, ITC-ICG 07), y una revisión '
         'al año de los quemadores, el motor y las espadas del asador. Apunta las fechas'),
        ('Medir el rendimiento del pollo y el tiempo de carga y recalcular', 'Maestro/a asador', 'Semanas 1-12',
         'Pesa cinco pollos crudos y asados de la misma carga, cronometra una carga completa y anota los pollos que '
         'sobran al cierre; lleva las medias a la calculadora del pack: el rendimiento y el tiempo de asado del plan '
         'son estimaciones del kit'),
        ('Cuadrante y stock del verano y de los encargos de Navidad', 'Titular', 'Mayo y noviembre',
         'Julio y agosto son el pico del año (la semana del 15 de agosto, la más fuerte) y diciembre repunta con los '
         'encargos de Nochebuena y Nochevieja: prepara el cuadrante, las cargas y el pollo con tiempo'),
        ('Revisar la cuenta de la plataforma cada mes', 'Titular', 'Mensual',
         'Ventas, comisión, promociones y envases: si la plataforma pasa del 11 % de las ventas o su margen no cubre '
         'la comisión, recorta o sube precio. Reparto propio, sólo con contrato laboral y cuando el volumen lo pague'),
        ('Comparar ventas y costes reales con el plan cada mes', 'Titular', 'Mensual',
         'Pedidos al día, ticket, pollos vendidos, mercancía y personal frente a la cuenta de resultados del Excel; '
         'revisa el escandallo cada vez que cambie el precio del pollo'),
        ('Seguir la tesorería mes a mes y el saldo mínimo', 'Titular', 'Mensual',
         'Enero y febrero son los meses más flojos y coinciden con el arranque: mira el saldo de cada mes antes de un '
         'pago grande'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 14, 13, 13, 13], [len(t) for _, _, t in FASES]
assert all(len(n) <= 29 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
