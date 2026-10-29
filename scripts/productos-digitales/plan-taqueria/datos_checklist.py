#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura de la Taquería ES 1.0 (F1-camino §4: 12/15/14/13/13/13,
mismas filas que la Pizzería). Producto nuevo: no hay versión anterior; formato de `plan-pizzeria/datos_checklist.py`.
Marco legal: `F1-research-taqueria.md` §0-§1 (R) y la lista de tareas obligadas de R §3 (lo marcado 🟡 va como
«compruébalo»). Fuente primaria de cada cita:
  · RDLeg 1175/1990 (tarifas del IAE): grupo 671 «servicios en restaurantes» por categoría; 673 (cafés y bares con
    comida) sin comedor separado; epígrafe 677.9 para la venta para llevar y a domicilio (aplicación por analogía de
    las consultas de pizzerías: «confírmalo con tu gestoría»); exención de cuota, art. 82.1.c del TRLRHL;
  · Ley 12/2012: los restaurantes no están en su anexo → licencia o declaración responsable por la ordenanza
    municipal; la terraza, siempre con autorización de ocupación de la vía pública (art. 2.2);
  · Ordenanza 4/2021 de Calidad del Aire de Madrid (BOCM 16-04-2021), arts. 12, 23 (23.1.e: limpieza ≥ 1/año) y anexo
    I: conducto exclusivo a cubierta, +1 m sobre lo que haya en 15 m y, con combustible sólido (carbón), filtrado
    específico de partículas; fuera de Madrid, la ordenanza de cada ayuntamiento;
  · RD 919/2006, ITC-ICG 07 (ap. 4.1-4.2) e ITC-ICG 08: gas por empresa instaladora habilitada, puesta en marcha
    certificada de cada aparato, inspección o revisión cada 5 años;
  · RD 1021/2022: registro autonómico previa declaración responsable, art. 3 (RGSEAA sólo para el suministro a otros
    negocios por encima de sus límites), art. 4.1 (preparados de carne ≤ 4 °C, carne picada ≤ 2 °C, frutas y
    vegetales cortados o pelados listos para consumo ≤ 4 °C), 4.2 (temperatura de la etiqueta), 4.3 (transporte) y
    8.1 (pescado crudo: −20 °C 24 h o −35 °C 15 h);
  · RD 1086/2020, art. 30, en la redacción de la disposición final 2.ª del RD 1021/2022: caliente ≥ 63 °C (30.2),
    refrigeradas ≤ 4 °C o ≤ 8 °C con vida útil < 24 h (30.3), enfriamiento de 60 a 10 °C en < 2 h (30.6) y recalentado
    ≥ 74 °C 15 s en el centro en la hora siguiente a sacarlo del frío (30.7). NUNCA «art. 30 del RD 1021/2022»;
  · RD 126/2015, arts. 4.1.b y 6.5.a (alérgenos sin envasar: por escrito, o de palabra con registro escrito o
    electrónico accesible); Reglamento (UE) 1169/2011, art. 14 (venta a distancia); Reglamento de Ejecución (UE)
    828/2014 («sin gluten» ≤ 20 mg/kg: no se promete con comal, freidora o pinzas compartidas);
  · Ley 37/1992, art. 91.Uno.1.1.º a y b y 91.Uno.2.2.º (para llevar: alcohol y bebidas con azúcares o edulcorantes
    añadidos al 21 %); Ley 1/2025, art. 8 (llevarse lo no consumido, aviso en la carta); Ley 7/2022, art. 55 (cobro del
    envase de plástico de un solo uso);
  · ET arts. 1.1, 34.9 y DA 23.ª (registro de jornada: sin afirmar que sea «digital» por ley, R §1); ALEH VI art. 4
    (convenio provincial de hostelería: no nombra la taquería, entra como restaurante); Ley 31/1995 (PRL); Ley 18/2022
    (SL desde 1 €).
Sin «carné», sin «licencia de apertura», sin «sin gluten» prometido ni restos de la pizzería en todo el libro. Cada
tarea: (trámite / acción, responsable, plazo, notas). Pestañas ≤ 29 caracteres. Sesión Claude Code, 29-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — TAQUERÍA'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Consulta urbanística previa: salida de humos, potencia, aforo y terraza', 'Titular / Técnico',
         'Antes de firmar el alquiler',
         'Pregunta al ayuntamiento si el uso permite un restaurante con cocina de plancha, trompo y freidora, si el '
         'local admite un conducto de humos exclusivo hasta la cubierta (en Madrid, que supere en 1 m lo que haya en '
         '15 m: Ordenanza 4/2021, art. 12 y anexo I), qué potencia y qué aforo tiene y si la calle admite terraza. Sin '
         'salida de humos a cubierta no hay trompo, plancha ni comal'),
        ('Decidir trompo de gas o de carbón ANTES de firmar el local', 'Titular', 'Antes de firmar el alquiler',
         'El de gas (el del plan) cabe en una salida de humos normal, con la instalación por empresa habilitada (RD '
         '919/2006). El de carbón, y la parrilla de carne asada, piden además filtro de partículas en el conducto (en '
         'Madrid, Ordenanza 4/2021, art. 23): pregunta en la consulta previa si tu local lo admite'),
        ('Decidir tortilla comprada o nixtamal propio ANTES de firmar el local', 'Titular', 'Antes de firmar el alquiler',
         'El plan compra la tortilla. Hacerla en casa pide molino, cocedor y tortilladora, sitio en la cocina y un '
         'tortillero: por coste sólo compensa por encima de unas 700 tortillas al día (la calculadora del pack hace la '
         'cuenta con tus precios). Si la haces tú, el molino y la tortilladora tienen que caber en el local'),
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036) en el grupo 671 o 673 y el epígrafe 677.9 del IAE', 'Gestoría', 'Semana 2',
         'Con comedor y servicio de mesa, el grupo 671 («servicios en restaurantes», por categoría); de barra y '
         'mostrador sin comedor separado, el 673. El 677.9 cubre la venta para llevar y a domicilio (RDLeg 1175/1990). '
         'Confírmalo con tu gestoría. Exento de cuota con una cifra de negocio inferior a 1 millón de euros (art. '
         '82.1.c de la Ley de Haciendas Locales)'),
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
         'frío y del equipo de cocina y de una línea ICO'),
        ('Seguro de responsabilidad civil y multirriesgo con incendio', 'Corredor de seguros', 'Antes de la obra',
         'RC de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la aseguradora que trabajas '
         'con trompo, plancha y freidora a gas'),
    ]),
    ('F2 - Local, humos y gas', 'FASE 2: LOCAL, SALIDA DE HUMOS, GAS, LICENCIA Y TERRAZA (semanas 3-14)', [
        ('Elegir el local: 70-90 m² con salida de humos a cubierta posible', 'Titular', 'Semanas 3-6',
         'Sala de unos 45 m² para 24 plazas en mesa y 8 en barra, cocina de unos 20 m² a la vista con el trompo, aseos '
         '(uno adaptado) y almacén. Calle con paso de gente por la noche y el fin de semana, cerca de una zona '
         'universitaria o de ocio'),
        ('Comprobar la potencia eléctrica y la acometida de gas', 'Técnico / Distribuidora', 'Antes de firmar',
         'Frío, extracción, climatización, lavavajillas y cafetera en la luz; trompo, plancha, comal y fogones en el '
         'gas (natural o envasado). Una acometida nueva tarda: pregunta plazo y coste a la distribuidora'),
        ('Comprobar con el técnico el recorrido del conducto hasta cubierta', 'Técnico', 'Antes de firmar',
         'Conducto exclusivo, continuo y estanco hasta la cubierta, por patio o fachada, con el permiso de la comunidad '
         'de propietarios si cruza zonas comunes'),
        ('Negociar el alquiler: carencia de obra y fianza', 'Titular', 'Antes de firmar',
         'El plan cuenta dos meses de renta antes de abrir y dos de fianza. Pide carencia mientras duran la obra y el '
         'conducto'),
        ('Contrato de arrendamiento con el uso de restaurante con salida de humos', 'Titular / Abogado', 'Semana 6',
         'Que diga «restaurante» (o «taquería con cocina») y que autorice la obra del conducto y la salida de humos a '
         'cubierta'),
        ('Encargar el proyecto técnico de la actividad y de la salida de humos', 'Arquitecto/a o ingeniero/a',
         'Semanas 6-8',
         'Distribución de la cocina, potencia, aforo, ventilación, accesibilidad, la instalación de gas y el conducto '
         'a cubierta. Fuera de Madrid, pide la ordenanza de humos y de calidad del aire de tu ayuntamiento'),
        ('Licencia o declaración responsable de la actividad', 'Técnico / Ayuntamiento', 'Antes de la obra',
         'Los restaurantes (grupos 671 y 673 y epígrafe 677.9) no están en el anexo de la Ley 12/2012: van por el '
         'régimen de tu ayuntamiento, licencia o declaración responsable según su ordenanza. Pregunta cuál te toca en '
         'la consulta previa'),
        ('Licencia, declaración o comunicación previa de la obra', 'Técnico / Ayuntamiento',
         'Semanas 6-8, antes de empezar la obra',
         'La obra y el conducto van por su propio trámite municipal: pregunta en la consulta previa qué título piden'),
        ('Solicitar la autorización de la terraza', 'Titular / Ayuntamiento', 'Con la licencia de la actividad',
         'Es ocupación de la vía pública y siempre se pide aparte (Ley 12/2012, art. 2.2). Pregunta la tasa y el '
         'horario de tu ayuntamiento: el plan cuenta 1.200 € de ejemplo'),
        ('Gas por empresa instaladora habilitada y certificado de cada aparato', 'Instalador de gas habilitado',
         'Durante la obra',
         'Certificado de la instalación, puesta en marcha certificada del trompo, la plancha, el comal y los fogones e '
         'inspección (red) o revisión (gas envasado) cada 5 años (RD 919/2006, ITC-ICG 07 e ITC-ICG 08)'),
        ('Conducto exclusivo a cubierta y filtro de partículas si hay carbón', 'Instalador / Técnico', 'Semanas 8-12',
         'Ejemplo de Madrid (Ordenanza 4/2021): conducto exclusivo que supere en 1 m lo que haya en 15 m (art. 12 y '
         'anexo I) y, con carbón u otro combustible sólido, sistemas específicos de filtrado de partículas (art. 23). '
         'Con trompo de gas, el conducto normal'),
        ('Obra de la cocina y de la sala: superficies lavables', 'Constructor', 'Semanas 8-12',
         'Paredes alicatadas, suelo antideslizante, falsos techos lavables, lavamanos de accionamiento no manual, '
         'aseos (uno adaptado) y aislamiento acústico si hay vecinos'),
        ('Fontanería, separador de grasas y climatización', 'Instalador', 'Semanas 8-12',
         'Agua fría y caliente en la cocina, desagües con separador de grasas (la plancha y la freidora echan mucha) y '
         'climatización de la sala'),
        ('Campana extractora sobre el trompo, la plancha, el comal y la freidora', 'Instalador', 'Semanas 10-12',
         'Campana extractora con motor y filtros de grasa que cubra toda la línea de fuego, conectada al conducto '
         'exclusivo. Pide al instalador el caudal y el plan de limpieza de los filtros'),
        ('Boletín eléctrico y certificado final de obra', 'Instalador autorizado / Técnico',
         'Durante la obra y al acabarla',
         'El boletín (certificado de la instalación) para el contrato de luz y el certificado final del técnico. '
         'Guárdalos con el del gas: te los pedirá el ayuntamiento'),
    ]),
    ('F3 - Cocina, trompo y sanidad', 'FASE 3: COCINA, TROMPO Y REGISTRO SANITARIO (semanas 6-14)', [
        ('Comprar el trompo, la plancha, el comal y la freidora', 'Titular', 'Semanas 6-8',
         'Asador vertical de gas de cuatro quemadores para conos de 30-35 kg (de 1.279 a 1.784 € sin IVA en catálogo), '
         'plancha lisa de acero, comal y freidora. Pide ficha técnica, consumo de gas, plazo de entrega y montaje'),
        ('Comprar el frío: armarios, congelador y mesa refrigerada de salsas', 'Titular', 'Semanas 8-10',
         'Armarios para la carne marinada y los conos montados, congelador y una mesa refrigerada que mantenga las '
         'salsas y las guarniciones de la barra a 4 °C o menos'),
        ('Declaración responsable al registro sanitario autonómico', 'Titular / Gestoría',
         'Antes de la primera prueba de carta',
         'Va al registro sanitario de tu comunidad autónoma (RD 1021/2022). El registro estatal (RGSEAA) sólo aplica '
         'si sirves a otros negocios por encima de lo que permite el art. 3 del mismo real decreto (por ejemplo, si '
         'vendes tortilla o masa a otras taquerías)'),
        ('APPCC del trompo: el cono en cámara a 4 °C o menos', 'Consultor / Titular', 'Antes de abrir',
         'La carne marinada para el pastor es un preparado de carne: en cámara a 4 °C o menos (RD 1021/2022, art. 4.1); '
         'la carne picada, a 2 °C o menos. Anota la hora de marinado y la de montaje de cada cono'),
        ('APPCC del trompo en servicio: sonda y hora límite del cono', 'Taquero/a jefe', 'Antes de abrir',
         'Sonda al inicio y a mitad del servicio y corte sólo de la capa exterior bien hecha (guías de buenas prácticas '
         'del asador vertical). Ninguna norma fija cuánto puede estar montado el cono: la hora límite la fija tu APPCC '
         'y se anota'),
        ('Salsas crudas, guacamole y vegetal cortado a 4 °C o menos', 'Cocinero/a de producción', 'Antes de abrir',
         'Cebolla, cilantro y piña picados, aguacate cortado y salsas crudas son vegetal cortado listo para consumo: a '
         '4 °C o menos (RD 1021/2022, art. 4.1). Tandas cortas; la oxidación del aguacate es calidad, no seguridad: lima '
         'y film en contacto'),
        ('Carnitas y guisados: caliente, enfriado y recalentado', 'Cocinero/a de producción', 'Antes de abrir',
         'En caliente, a 63 °C o más; lo que se guarda, enfriado de 60 a 10 °C en menos de 2 horas, y recalentado a '
         '74 °C durante 15 segundos en el centro en la hora siguiente a sacarlo del frío (RD 1086/2020, art. 30, en la '
         'redacción del RD 1021/2022)'),
        ('Barra de salsas con reglas: recipiente, hora y utensilio', 'Encargado/a de sala', 'Antes de abrir',
         'Recipiente limpio en cada reposición (nunca rellenar encima), hora de puesta y de descarte anotadas y un '
         'utensilio por salsa. La salsa macha, con su cuchara propia por el cacahuete y el sésamo'),
        ('Pescado crudo (aguachile, ceviche): congelación previa', 'Titular', 'Si lo pones en carta',
         'A −20 °C durante al menos 24 horas o a −35 °C durante al menos 15 horas, o pescado que ya llegue tratado del '
         'proveedor (RD 1021/2022, art. 8.1). Anótalo en el registro'),
        ('Quesos, crema y tortilla envasada a la temperatura de su etiqueta', 'Titular', 'Antes de abrir',
         'Lo que no está en la tabla de temperaturas del real decreto va a la que marque la etiqueta del fabricante (RD '
         '1021/2022, art. 4.2)'),
        ('Trazabilidad y registros: lotes, temperaturas y proveedores', 'Titular', 'Desde la primera compra',
         'Lote y fecha de la carne, la tortilla y los quesos, hora de marinado y de montaje de cada cono, temperaturas '
         'del frío y del caliente y proveedor de cada materia prima'),
        ('Fichas técnicas por taco y por salsa con sus alérgenos', 'Taquero/a jefe', 'Antes de abrir',
         'Gluten (tortilla de harina de la gringa, cerveza), leche (quesos, crema), cacahuete y sésamo (salsa macha, '
         'moles), frutos de cáscara (moles), mostaza y sulfitos según receta. Con la calculadora del pack, el coste de '
         'cada uno'),
        ('Alérgenos en la venta por plataforma o por tu web', 'Titular', 'Antes de darte de alta',
         'En la venta a distancia, la información de alérgenos tiene que estar disponible antes de que el cliente '
         'compre (Reglamento (UE) 1169/2011, art. 14). Revisa la ficha de cada taco en cada plataforma'),
        ('Temperatura de los pedidos que salen del local', 'Titular', 'Antes del primer pedido',
         'Envases y bolsas que mantengan la temperatura durante el transporte (RD 1021/2022, art. 4.3), también en el '
         'reparto de la plataforma; la orden «para armar» (tortilla y relleno aparte) llega mejor'),
    ]),
    ('F4 - Personal y alérgenos', 'FASE 4: PERSONAL, FORMACIÓN, PREVENCIÓN Y ALÉRGENOS (semanas 10-14)', [
        ('Copiar la tabla salarial del convenio provincial de hostelería', 'Gestoría', 'Semana 10',
         'La taquería va al convenio provincial de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal para '
         'el sector de Hostelería no nombra la palabra, pero incluye los restaurantes. Pon su salario más bajo en la '
         'hoja de Supuestos del plan'),
        ('Contratos por escrito a jornada completa y parcial', 'Gestoría', 'Antes de abrir',
         'Con su horario y su grupo del convenio. Una factura de «autónomo» con tu horario y tu dirección es falso '
         'autónomo (art. 1.1 del Estatuto de los Trabajadores)'),
        ('Contratar al segundo taquero antes de abrir', 'Titular', 'Semanas 10-12',
         'Que aprenda contigo el marinado, el montaje del cono y el corte antes de abrir: si sólo tú sabes llevar el '
         'trompo, una baja cierra la taquería'),
        ('Registro de jornada', 'Titular', 'Desde el primer contrato',
         'Obligatorio para toda la plantilla (art. 34.9 ET), también a tiempo parcial. Acuerda con tu gestoría cómo '
         'llevarlo y consérvalo'),
        ('Cuadrante de los dos servicios y del sábado por la noche', 'Titular', 'Semana 12',
         'Comidas y cenas de martes a domingo, con el lunes de cierre; el sábado por la noche hacen falta unas cinco '
         'personas'),
        ('Reparto propio: sólo con contrato laboral', 'Gestoría', 'Si repartes tú',
         'El repartidor propio es hostelería (ALEH VI, art. 4) y trabaja por cuenta ajena; en el reparto organizado por '
         'una plataforma digital, la ley presume la relación laboral (ET, disposición adicional 23.ª). Nunca con '
         '«autónomos»'),
        ('Formación de manipuladores de alimentos', 'Titular', 'Antes de abrir',
         'La da y la acredita la empresa (no hay un documento oficial que sacar): higiene, temperaturas del trompo y de '
         'las salsas, alérgenos y contacto cruzado'),
        ('Formación del trompo: marinado, montaje del cono y corte', 'Titular', 'Antes de abrir',
         'Adobo, capas, piña, encendido, corte fino de la capa hecha y gramaje por taco: es inversión, no gasto'),
        ('Plan de prevención de riesgos laborales', 'Servicio de prevención', 'Antes de abrir',
         'Obligatorio (Ley 31/1995): cortes en el trompo, quemaduras de la plancha y la freidora, gas, calor y cargas'),
        ('Vigilancia de la salud de la plantilla', 'Servicio de prevención', 'Al contratar',
         'Reconocimientos médicos ofrecidos a cada persona que entra'),
        ('Información de alérgenos por escrito o de palabra con registro', 'Titular', 'Antes de abrir',
         'Por escrito en la carta o, si la das de palabra, registrada por escrito o en formato electrónico en el local, '
         'accesible y con un cartel que diga dónde pedirla (RD 126/2015, arts. 4.1.b y 6.5.a)'),
        ('Cartel de alérgenos en la barra de salsas', 'Encargado/a de sala', 'Antes de abrir',
         'Cada salsa con sus alérgenos a la vista del cliente: la macha lleva cacahuete o sésamo, o los dos, según tu '
         'receta. Revísalo cada vez que cambie una receta'),
        ('No prometer «sin gluten» con comal o freidora compartidos', 'Titular', 'Antes de imprimir la carta',
         '«Sin gluten» sólo con 20 mg/kg o menos tal como se vende (Reglamento de Ejecución (UE) 828/2014). La tortilla '
         'de maíz no lleva gluten por receta, pero el comal, la freidora o las pinzas compartidos con la tortilla de '
         'harina rompen la promesa: informa del alérgeno y de las trazas, no lo prometas'),
    ]),
    ('F5 - Carta, marca y delivery', 'FASE 5: CARTA, MARCA, DELIVERY Y PROVEEDORES (semanas 8-16)', [
        ('Decidir el tipo de taquería y su carta', 'Titular', 'Semana 8',
         'De barrio sin trompo, con trompo y barra de salsas (este plan), con tortillería propia o taquería-cantina con '
         'barra de mezcal: cada una con otra inversión, otro local y otro margen. Para un restaurante mexicano de mesa '
         'con 60-100 plazas, la Guía Restaurante Mexicano de AI Chef Pro'),
        ('Carta de 8-10 tacos con su escandallo', 'Taquero/a jefe', 'Semanas 10-14',
         'Escandalla cada taco, la orden y la gringa, no sólo el pastor: carnitas, suadero y barbacoa rinden menos y el '
         'aguacate sube y baja. Usa la calculadora del trompo y escandallo del pack'),
        ('IVA de la carta para llevar: tacos al 10 %, alcohol y bebidas azucaradas al 21 %', 'Gestoría / Titular',
         'Antes de abrir',
         'En sala, todo al 10 % (Ley 37/1992, art. 91.Uno.2.2.º). Para llevar y a domicilio, la comida al 10 %, pero el '
         'alcohol y las aguas frescas, los refrescos y los zumos con azúcares o edulcorantes añadidos van al 21 % (art. '
         '91.Uno.1.1.º a y b). Configúralo así en el TPV y en cada plataforma'),
        ('Aviso en la carta: el cliente puede llevarse lo que no consuma', 'Titular', 'Antes de abrir',
         'Sin coste, salvo el del envase de plástico de un solo uso si lo hay, y avisado de forma visible, mejor en la '
         'carta (Ley 1/2025, art. 8). Ten envases para ello'),
        ('Cobro aparte del envase de plástico de un solo uso', 'Titular', 'Antes de abrir',
         'Los recipientes de plástico de un solo uso para llevar se cobran aparte en el tique (Ley 7/2022, art. 55). '
         'Las bandejas de cartón sin recubrimiento de plástico no lo son; las de aluminio, pregúntalo a tu proveedor'),
        ('Importador de chiles secos y producto mexicano: plazo y segundo proveedor', 'Titular', 'Semanas 8-12',
         'Los chiles secos, el achiote, la masa y el producto importado tardan semanas en llegar: pide el plazo por '
         'escrito, ten stock de seguridad y un segundo proveedor. Es el cuello de botella real del negocio'),
        ('Proveedor de tortilla: lote, temperatura de recepción y segundo proveedor', 'Titular', 'Semanas 10-14',
         'Tortilla de maíz nixtamalizado con lote y fecha, recibida a la temperatura que marque su etiqueta y anotada. '
         'Pide muestra a dos fabricantes y precio por caja: el plan la estima con un precio de referencia: pon el tuyo'),
        ('Contrato y alta en las plataformas de reparto', 'Titular', 'Antes de abrir',
         'Lee la comisión (del 15 al 35 % más IVA según la plataforma y la zona), cada cuánto liquidan, quién paga las '
         'promociones y el coste de la tablet. Fija un techo: en este plan, el 12 % de las ventas'),
        ('Precios para la plataforma y para la recogida en el local', 'Titular', 'Antes de abrir',
         'Calcula el margen de la orden y de la gringa en la plataforma con su comisión y el envase; la recogida en el '
         'local no paga comisión: empújala'),
        ('Registro de la marca en la OEPM', 'Titular', 'Semanas 2-8',
         'Comprueba antes que el nombre no está registrado en tu clase (servicios de restauración)'),
        ('Identidad, fotos y web con la carta y los alérgenos', 'Diseñador/a', 'Semanas 8-14',
         'Fotos reales del trompo y de los tacos; web con la carta, los alérgenos, el horario, los pedidos para recoger '
         'y la cláusula de protección de datos de cada canal'),
        ('Ficha de Google Business, redes y fechas mexicanas', 'Titular', 'Antes de abrir',
         'Horario de comidas y cenas, fotos del trompo y respuesta a cada reseña. En el calendario, la Independencia de '
         'México (15 y 16 de septiembre) y el Día de Muertos (1 y 2 de noviembre)'),
        ('Música ambiental: licencias de SGAE y AGEDI-AIE', 'Titular', 'Antes de abrir',
         'Son dos licencias de propiedad intelectual, distintas de la municipal: pide las dos si pones música'),
    ]),
    ('F6 - Apertura y 90 días', 'FASE 6: APERTURA Y PRIMEROS 90 DÍAS', [
        ('Abrir en enero, el Mes 1 del plan', 'Titular', 'Mes 1',
         'El plan arranca en enero y la rampa cae sobre los meses más flojos, enero y febrero: por eso el fondo de '
         'maniobra cuenta. Si abres en otro mes, gira la fila de estacionalidad de la Tesorería'),
        ('Desinsectación, desratización y desinfección (DDD)', 'Empresa del ROESB', 'Antes de abrir',
         'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
        ('Plan de limpieza de la cocina, el trompo y la barra de salsas', 'Titular', 'Antes de abrir',
         'Trompo y bandeja, plancha, comal, freidora, filtros de la campana extractora, mesa refrigerada y recipientes '
         'de salsas, con su registro'),
        ('Servicios de prueba con la carta completa', 'Taquero/a jefe', 'Semana previa',
         'Varios servicios de prueba para ajustar el marinado, el gramaje por taco y los tiempos del pase antes de '
         'abrir'),
        ('Comprobar temperaturas y registros del primer día', 'Titular', 'Día 1',
         'Cámara de la carne, mesa de salsas, caliente de los guisados, sonda del trompo y la hoja de limpieza; corrige '
         'cualquier desviación antes de servir'),
        ('Inspección sanitaria: APPCC y registros a mano', 'Titular', 'Desde el día 1',
         'Fichas de alérgenos, trazabilidad, registros de temperatura y de limpieza, formación y DDD'),
        ('Calendario de limpieza de la campana extractora y del conducto', 'Titular / Empresa de mantenimiento',
         'Desde el mes 1',
         'Al menos una vez al año (Madrid, Ordenanza 4/2021, art. 23); los filtros de grasa, con la frecuencia que fije '
         'tu plan de limpieza'),
        ('Revisión de la instalación de gas cada 5 años', 'Instalador de gas habilitado', 'Calendario',
         'Inspección periódica (red) o revisión (gas envasado) cada 5 años (RD 919/2006, ITC-ICG 08). Apunta la '
         'fecha'),
        ('Medir el rendimiento del trompo y recalcular', 'Taquero/a jefe', 'Semanas 1-12',
         'Pesa el cono crudo y el sobrante al cierre cada día con la hoja del Kit de Tareas Recurrentes: Taquería '
         'Mexicana y lleva la media a la calculadora del pack: mide en el kit, recalcula en el plan'),
        ('Cuadrante del sábado por la noche y de las fechas fuertes', 'Titular', 'Agosto',
         'Diciembre es el pico del año y septiembre y noviembre traen las fechas mexicanas: prepara el cuadrante y el stock con tiempo'),
        ('Revisar la cuenta de la plataforma cada mes', 'Titular', 'Mensual',
         'Ventas, comisión, promociones y envases: si la plataforma pasa del 12 % de las ventas o su margen no cubre '
         'la comisión, recorta o sube precio. Reparto propio, sólo con contrato laboral y cuando el volumen lo pague'),
        ('Comparar ventas y costes reales con el plan cada mes', 'Titular', 'Mensual',
         'Comensales al día, ticket, mercancía y personal frente a la cuenta de resultados del Excel; revisa el '
         'escandallo cuando cambie el precio de la carne, la tortilla o el aguacate'),
        ('Seguir la tesorería mes a mes y el saldo mínimo', 'Titular', 'Mensual',
         'Enero y febrero son los meses más flojos y coinciden con el arranque: mira el saldo de cada mes antes de un '
         'pago grande'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 14, 13, 13, 13], [len(t) for _, _, t in FASES]
assert all(len(n) <= 29 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
