#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura del Plan de Negocio: Sushi Bar ES 1.0 (F1-camino §4:
12/15/14/13/13/13, mismas filas que la Taquería y la Pollería). Producto nuevo: no hay versión anterior; formato de
`plan-polleria/datos_checklist.py`. Marco legal: `F1-research-sushi.md` §0-§1 (R) y la lista de tareas obligadas de
R §3 (lo marcado 🟡 va como «compruébalo»). Fuente primaria de cada cita:
  · RDLeg 1175/1990 (tarifas del IAE): con comedor, grupo 671 (por categoría); de barra sin comedor separado, 673; la
    nota común de los grupos 671-673 faculta la venta para llevar; si los pedidos fueran la actividad principal (formato
    de sólo para llevar y a domicilio), 677.9; exención de cuota, art. 82.1.c del TRLRHL;
  · Ley 12/2012: los restaurantes no están en su anexo → licencia o declaración responsable por la ordenanza municipal;
  · Ordenanza 4/2021 de Calidad del Aire de Madrid, arts. 12, 23 (limpieza ≥ 1/año) y anexo I, como ejemplo;
  · RD 1021/2022: registro autonómico previa declaración responsable, art. 3 (RGSEAA sólo para el suministro a otros
    negocios por encima de lo marginal), art. 4.1 (productos de la pesca frescos, 0-4 °C), 4.2 (temperatura de la
    etiqueta), 4.3 (transporte) y **art. 8.1-8.2** (pescado para consumir crudo o casi crudo: ≤ −20 °C en la totalidad
    del producto ≥ 24 h o ≤ −35 °C ≥ 15 h, o tratado en una etapa anterior con su documento; información a las personas
    consumidoras en carteles o cartas-menú). El RD 1420/2006 está DEROGADO: no se cita;
  · Reglamento (CE) 853/2004, anexo III, sección VIII, capítulo III, parte D (redacción del Reglamento (UE) 1276/2011):
    excepción de la acuicultura libre de parásitos, acreditada por escrito por el proveedor;
  · RD 1086/2020, art. 30, en la redacción de la disposición final 2.ª del RD 1021/2022: servir cuanto antes, refrigerar,
    congelar o mantener a ≥ 63 °C (30.2); refrigeradas ≤ 4 °C u ≤ 8 °C con vida útil < 24 h (30.3); **30.5**: otras
    temperaturas de conservación sólo si el operador demuestra a la autoridad competente que se basan en evidencias
    científicas (la única vía del shari a temperatura ambiente); enfriamiento de 60 a 10 °C en < 2 h (30.6) y recalentado
    ≥ 74 °C 15 s (30.7). NUNCA «art. 30 del RD 1021/2022». Ninguna norma española fija un pH ni un tiempo para el arroz de
    sushi: el pH ≤ 4,6 es el límite crítico del APPCC del Kit de Tareas Sushi Bar (Codex CXC 23-1979);
  · RD 126/2015, art. 4 (sin envasar o envasado a petición: denominación y alérgenos), art. 5 (envasado por el
    comercio para su venta inmediata: arts. 9 y 10 del Reglamento (UE) 1169/2011 salvo la nutricional) y arts. 4.1.b y
    6.5.a (alérgenos por escrito, o de palabra con registro escrito o electrónico accesible); Reglamento (UE)
    1169/2011, art. 14 (venta a distancia); Reglamento de Ejecución (UE) 828/2014 («sin gluten» ≤ 20 mg/kg: no se
    promete con salsa de soja de trigo, tempura y freidora compartida);
  · Ley 37/1992, art. 91.Uno.1.1.º a y b y 91.Uno.2.2.º (para llevar: alcohol y bebidas con azúcares o edulcorantes
    añadidos al 21 %; la comida al 10 %); Ley 1/2025, art. 8 (llevarse lo no consumido, aviso en la carta); Ley 7/2022,
    art. 55 (cobro del envase de plástico de un solo uso);
  · ET arts. 1.1, 34.9 y DA 23.ª (registro de jornada: sin afirmar que sea «digital» por ley); ALEH VI art. 4 (convenio
    provincial de hostelería: no nombra el sushi bar); Ley 31/1995 (PRL); Ley 18/2022 (SL desde 1 €).
Sin «carné», sin «licencia de apertura», sin «sin gluten» prometido, sin «7 días» de congelación (es la opción de
EE. UU., no la española) ni restos de la taquería en todo el libro. Cada tarea: (trámite / acción, responsable, plazo,
notas). Pestañas ≤ 29 caracteres. Sesión Claude Code, 31-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — SUSHI BAR'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Consulta urbanística previa: extracción, potencia eléctrica y aforo', 'Titular / Técnico',
         'Antes de firmar el alquiler',
         'Pregunta al ayuntamiento si el uso permite un restaurante con freidora y plancha, si el local admite un '
         'conducto exclusivo de extracción hasta la cubierta (en Madrid, que supere en 1 m lo que haya en 15 m: '
         'Ordenanza 4/2021, art. 12 y anexo I), qué potencia eléctrica tiene y qué aforo. Sin salida a cubierta no hay '
         'freidora de tempura ni plancha de gyozas: la carta se queda en frío'),
        ('Decidir el formato ANTES de firmar el local: barra y mesas, para llevar u omakase', 'Titular',
         'Antes de firmar el alquiler',
         'Barra a la vista con mesas, para llevar y a domicilio (este plan: 36 plazas en unos 95 m²); sólo para llevar '
         'y a domicilio en 40-60 m²; una barra omakase de 10-12 plazas con reserva; o un kaiten o un buffet libre de '
         '150-250 m². Cada uno pide otro local, otra inversión y otro margen. Para un japonés completo con ramen o '
         'robata, la Guía Restaurante Japonés de AI Chef Pro; para un nikkei, la Guía Restaurante Nikkei'),
        ('Decidir cómo cumplirás el anisakis: congelador propio o pescado ya tratado', 'Titular', 'Semanas 1-4',
         'El pescado que se sirve crudo se congela a −20 °C o menos en la totalidad del producto durante al menos 24 '
         'horas, o a −35 °C o menos durante al menos 15 horas, en tu local o en una etapa anterior con su documento; '
         'la acuicultura libre de anisakis sólo con acreditación escrita del proveedor (RD 1021/2022, art. 8.1). Si '
         'congelas tú, el congelador y su sitio entran en el proyecto del local'),
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036) en el grupo 671 o 673 del IAE, o en el 677.9 si sólo vendes para llevar',
         'Gestoría', 'Semana 2',
         'Con comedor y servicio de mesa, el grupo 671 («servicios en restaurantes», por categoría); de barra sin '
         'comedor separado, el 673. La nota común de esos grupos ya te faculta para vender para llevar. Si los pedidos '
         'fueran tu actividad principal (sólo para llevar y a domicilio), el 677.9 (RDLeg 1175/1990). Confírmalo con tu '
         'gestoría. Exento de cuota con una cifra de negocio inferior a 1 millón de euros (art. 82.1.c de la Ley de '
         'Haciendas Locales)'),
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
        ('Seguro de responsabilidad civil y multirriesgo con avería del frío', 'Corredor de seguros', 'Antes de la obra',
         'RC de al menos 300.000 € y multirriesgo con incendio y avería del frío, que es el pescado de la cámara y del '
         'congelador. Dile a la aseguradora que sirves pescado crudo y que trabajas con freidora'),
    ]),
    ('F2 - Local, frío y extracción', 'FASE 2: LOCAL, EXTRACCIÓN, FRÍO Y LICENCIA (semanas 3-14)', [
        ('Elegir el local: 90-100 m² ya de restauración con salida a cubierta posible', 'Titular', 'Semanas 3-6',
         'Sitio para una barra de sushi a la vista con 8 taburetes y una sala de 28 plazas, cocina, cuarto frío, aseos '
         '(uno adaptado) y una zona de empaquetado de pedidos junto a la puerta. Barrio con vida de noche y paso de '
         'gente el fin de semana'),
        ('Comprobar la potencia eléctrica para una cocina toda eléctrica', 'Técnico / Distribuidora', 'Antes de firmar',
         'Arroceras, inducción, freidora, plancha, el frío del pescado, el congelador, la extracción y la '
         'climatización van a la luz. Una ampliación de potencia o una acometida nueva tarda: pregunta plazo y coste a '
         'la distribuidora'),
        ('Comprobar con el técnico el recorrido del conducto hasta cubierta', 'Técnico', 'Antes de firmar',
         'Conducto exclusivo, continuo y estanco hasta la cubierta, por patio o fachada, con el permiso de la comunidad '
         'de propietarios si cruza zonas comunes'),
        ('Negociar el alquiler: carencia de obra y fianza', 'Titular', 'Antes de firmar',
         'El plan cuenta dos meses de renta antes de abrir y dos de fianza. Pide carencia mientras duran la obra de la '
         'barra y el conducto'),
        ('Contrato de arrendamiento con el uso de restaurante y la salida de humos', 'Titular / Abogado', 'Semana 6',
         'Que diga «restaurante» y que autorice la obra de la barra, del cuarto frío y del conducto a cubierta'),
        ('Encargar el proyecto técnico de la actividad y de la extracción', 'Arquitecto/a o ingeniero/a',
         'Semanas 6-8',
         'Distribución de la barra y de la cocina, potencia, aforo, ventilación, accesibilidad y el conducto a '
         'cubierta. Fuera de Madrid, pide la ordenanza de humos y de calidad del aire de tu ayuntamiento'),
        ('Licencia o declaración responsable de la actividad', 'Técnico / Ayuntamiento', 'Antes de la obra',
         'Los restaurantes no están en el anexo de la Ley 12/2012: van por el régimen de tu ayuntamiento, licencia o '
         'declaración responsable según su ordenanza. Pregunta cuál te toca en la consulta previa'),
        ('Licencia, declaración o comunicación previa de la obra', 'Técnico / Ayuntamiento',
         'Semanas 6-8, antes de empezar la obra',
         'La obra y el conducto van por su propio trámite municipal: pregunta en la consulta previa qué título piden'),
        ('Conducto exclusivo de extracción a cubierta', 'Instalador / Técnico', 'Semanas 8-12',
         'Ejemplo de Madrid (Ordenanza 4/2021): conducto exclusivo que supere en 1 m lo que haya en 15 m (art. 12 y '
         'anexo I). Una robata de carbón, si algún día la pones, pide además filtro de partículas (art. 23)'),
        ('Obra de la barra, la cocina y la sala: superficies lisas y lavables', 'Constructor', 'Semanas 8-12',
         'Barra de sushi con encimera lisa y lavable, paredes alicatadas, suelo antideslizante, falsos techos lavables, '
         'lavamanos de accionamiento no manual cerca de la barra y en la cocina, aseos (uno adaptado) y aislamiento '
         'acústico si hay vecinos'),
        ('Cuarto frío y zona de limpieza del pescado separada del corte', 'Constructor / Titular', 'Semanas 8-12',
         'El pescado entero se limpia en una zona con su fregadero, lejos del corte de la barra y de la cocina caliente; '
         'el armario de pescado y el congelador, en el cuarto frío. Ordena el recorrido: recepción, frío, limpieza, '
         'corte, barra'),
        ('Fontanería, separador de grasas y climatización', 'Instalador', 'Semanas 8-12',
         'Agua fría y caliente en la cocina y en la barra, desagües con separador de grasas (la freidora echa mucha) y '
         'climatización de la sala: la vitrina de la neta trabaja peor con la sala caliente'),
        ('Campana extractora sobre la freidora, la plancha y la inducción', 'Instalador', 'Semanas 10-12',
         'Campana extractora con motor y filtros de grasa que cubra la línea caliente, conectada al conducto exclusivo. '
         'Pide al instalador el caudal y el plan de limpieza de los filtros'),
        ('Zona de empaquetado de pedidos junto a la puerta', 'Titular', 'Semanas 10-12',
         'Una mesa con las cajas, las tarrinas de soja y las bolsas, la impresora de comandas y las tablets de las '
         'plataformas, para que los repartidores no crucen la sala ni entren en la cocina'),
        ('Boletín eléctrico y certificado final de obra', 'Instalador autorizado / Técnico',
         'Durante la obra y al acabarla',
         'El boletín (certificado de la instalación) para el contrato de luz y el certificado final del técnico. '
         'Guárdalos: te los pedirá el ayuntamiento'),
    ]),
    ('F3 - Pescado, arroz y sanidad', 'FASE 3: PESCADO, ARROZ Y REGISTRO SANITARIO (semanas 6-14)', [
        ('Comprar el congelador de −20 °C con registrador, la vitrina de la neta y las arroceras', 'Titular',
         'Semanas 6-10',
         'Pide la ficha técnica del congelador: tiene que llevar el pescado a −20 °C o menos en el centro y registrar '
         'la temperatura; uno que sólo marca −18 °C sirve para el congelado general, no para el anisakis. La vitrina, '
         'que mantenga la neta entre 0 y 4 °C con la sala llena; las arroceras, con el tamaño de tus tandas'),
        ('Declaración responsable al registro sanitario autonómico', 'Titular / Gestoría',
         'Antes de la primera prueba de carta',
         'Va al registro sanitario de tu comunidad autónoma (RD 1021/2022). El registro estatal (RGSEAA) sólo aplica '
         'si sirves a otros negocios por encima de lo que permite el art. 3 del mismo real decreto'),
        ('APPCC con el anisakis como punto de control crítico', 'Consultor / Titular', 'Antes de abrir',
         'Pescado para consumir crudo o casi crudo (nigiri, sashimi, maki, tartar, poke): a −20 °C o menos en la '
         'totalidad del producto durante al menos 24 horas, o a −35 °C o menos durante al menos 15 horas (RD '
         '1021/2022, art. 8.1). El atún y el pescado salvaje no están exentos: congelación o documento'),
        ('Registro de congelación por lote', 'Itamae', 'Desde la primera compra',
         'Especie, origen, lote, fecha y hora de entrada y de salida del congelador y temperatura, en cada lote que '
         'congeles tú. El Kit de Tareas Sushi Bar de AI Chef Pro trae la hoja de registro (03, seguridad y anisakis)'),
        ('Documento del proveedor si el pescado llega congelado o es de acuicultura', 'Titular', 'Con cada proveedor',
         'Si el pescado llega ya congelado para consumir crudo, que el documento lo diga; si es de acuicultura libre de '
         'anisakis (el salmón de piscifactoría, por ejemplo), sólo con la acreditación escrita del proveedor '
         '(Reglamento (CE) 853/2004, anexo III, sección VIII). Archívalos con el lote: es lo primero que pide la '
         'inspección'),
        ('Cartel o carta con la información del anisakis', 'Titular', 'Antes de abrir',
         'Hay que informar al cliente de que el pescado para consumir crudo se ha congelado o procede de acuicultura '
         'libre de anisakis, en la carta o en un cartel (RD 1021/2022, art. 8.2). Ponlo también en la ficha de cada '
         'plataforma y en tu web'),
        ('Pescado fresco y vitrina entre 0 y 4 °C; descongelación en cámara', 'Itamae', 'Antes de abrir',
         'El pescado fresco va entre 0 y 4 °C (RD 1021/2022, art. 4.1), en la cámara y en la vitrina de la barra. '
         'Descongela en cámara, nunca a temperatura ambiente, y anota cuándo sale del congelador'),
        ('Recepción del pescado: temperatura, aspecto y cuidado con el atún', 'Itamae', 'Desde la primera compra',
         'Mide la temperatura de cada entrega y rechaza la que llegue fuera de la que fije tu APPCC. Con el atún, la '
         'caballa y el bonito, la cadena de frío desde la recepción es la defensa contra la histamina, que no se va ni '
         'con la congelación ni con la cocción'),
        ('Shari: temperatura justificada ante sanidad o refrigerado', 'Consultor / Titular', 'Antes de abrir',
         'La comida preparada se refrigera, se mantiene a 63 °C o más o se sirve cuanto antes (RD 1086/2020, art. '
         '30.2). El shari a temperatura ambiente sólo si tu APPCC lo justifica con evidencias científicas y lo '
         'demuestras a sanidad (RD 1086/2020, art. 30.5), con el pH de cada tanda y un tiempo máximo. Si no, '
         'refrigerado. Ninguna norma española fija un pH ni un tiempo para el arroz de sushi'),
        ('pH del shari en cada tanda con un pH-metro calibrado', 'Sushiman', 'Desde la primera tanda',
         'Mide y anota el pH de cada tanda en la hoja 03 del Kit de Tareas Sushi Bar: su APPCC fija como límite crítico '
         'un pH de 4,6 o menos (criterio del Codex, no cifra legal); apunta a 4,2-4,3 para tener margen. Calibra el '
         'pH-metro con sus soluciones antes de empezar'),
        ('Cocina caliente: gyozas, tempura y miso a 63 °C, enfriado y recalentado', 'Cocinero/a de cocina caliente',
         'Antes de abrir',
         'En caliente, a 63 °C o más; lo que se guarda, enfriado de 60 a 10 °C en menos de 2 horas, y recalentado a '
         '74 °C durante 15 segundos en el centro en la hora siguiente a sacarlo del frío (RD 1086/2020, art. 30, en la '
         'redacción del RD 1021/2022)'),
        ('Trazabilidad y registros: lotes, temperaturas y proveedores', 'Titular', 'Desde la primera compra',
         'Lote y fecha del pescado, el arroz, las algas y las salsas, registros de congelación, temperaturas de la '
         'cámara, del congelador y de la vitrina, pH del shari y proveedor de cada materia prima'),
        ('Fichas técnicas por pieza con sus alérgenos', 'Itamae', 'Antes de abrir',
         'Pescado; crustáceos (langostino, ebi); moluscos (pulpo, vieira); soja y el trigo de la salsa de soja; sésamo; '
         'huevo (tamago, mayonesa japonesa); leche (queso crema); gluten de la tempura, el panko y el surimi; mostaza de '
         'algunas pastas de wasabi; sulfitos del vino y de algunos encurtidos. Lee cada etiqueta: cambian por marca. '
         'Con la calculadora del pack, el coste de cada pieza'),
        ('Etiqueta completa en las bandejas cerradas antes del pedido', 'Titular', 'Antes de abrir',
         'Las bandejas de combinado que preparas antes de que el cliente las pida, para la vitrina o para recoger, son '
         'envasado para la venta inmediata: denominación, ingredientes con los alérgenos resaltados, peso, fecha y '
         'conservación (RD 126/2015, art. 5). Lo que envasas a petición del cliente sólo necesita denominación y '
         'alérgenos (art. 4)'),
    ]),
    ('F4 - Personal y alérgenos', 'FASE 4: PERSONAL, FORMACIÓN, PREVENCIÓN Y ALÉRGENOS (semanas 6-14)', [
        ('Copiar la tabla salarial del convenio provincial de hostelería', 'Gestoría', 'Semana 10',
         'El sushi bar va al convenio provincial de hostelería: el art. 4 del VI Acuerdo Laboral de ámbito Estatal para '
         'el sector de Hostelería no lo nombra, pero incluye los restaurantes. Pon su salario más bajo en la hoja de '
         'Supuestos del plan'),
        ('Contratar al itamae y al sushiman ANTES de la obra', 'Titular', 'Semanas 6-8',
         'Si no eres tú el itamae (el jefe de barra que compra, limpia y corta el pescado), es la contratación difícil: '
         'las ofertas de sushiman van de 12.000 a 22.000 € brutos al año y las de un omakase pasan de 2.500 € al mes. '
         'Que los dos opinen sobre la barra y el frío antes de cerrar la obra: una baja del único que corta cierra la '
         'barra'),
        ('Contratos por escrito a jornada completa y parcial', 'Gestoría', 'Antes de abrir',
         'Con su horario y su grupo del convenio. Una factura de «autónomo» con tu horario y tu dirección es falso '
         'autónomo (art. 1.1 del Estatuto de los Trabajadores)'),
        ('Registro de jornada', 'Titular', 'Desde el primer contrato',
         'Obligatorio para toda la plantilla (art. 34.9 ET), también a tiempo parcial. Acuerda con tu gestoría cómo '
         'llevarlo y consérvalo'),
        ('Cuadrante de los dos servicios y de las noches del viernes y el sábado', 'Titular', 'Semana 12',
         'Comidas y cenas de martes a domingo, con el lunes de cierre; el viernes y el sábado por la noche hacen falta '
         'unas seis personas: dos en la barra, una en la cocina caliente, dos en sala y una empaquetando pedidos'),
        ('Reparto propio: sólo con contrato laboral', 'Gestoría', 'Si repartes tú',
         'El repartidor propio es hostelería (ALEH VI, art. 4) y trabaja por cuenta ajena; en el reparto organizado por '
         'una plataforma digital, la ley presume la relación laboral (ET, disposición adicional 23.ª). Nunca con '
         '«autónomos»'),
        ('Formación de manipuladores con el pescado crudo', 'Titular', 'Antes de abrir',
         'La da y la acredita la empresa (no hay un documento oficial que sacar): higiene, congelación del anisakis, '
         'temperaturas de la vitrina, pH del shari, alérgenos y contacto cruzado'),
        ('Formación de la barra: corte, gramos de neta y de shari', 'Itamae', 'Antes de abrir',
         'Todo el equipo de barra corta y forma con los mismos gramos: pesa 10 lonchas y 10 bolas de shari de cada uno y '
         'corrige. La neta y el shari que pesan de más son el food cost que no sale en el escandallo'),
        ('Plan de prevención de riesgos laborales', 'Servicio de prevención', 'Antes de abrir',
         'Obligatorio (Ley 31/1995): cortes con los cuchillos de la barra, quemaduras de la freidora y la plancha, el '
         'frío del congelador y las cargas'),
        ('Vigilancia de la salud de la plantilla', 'Servicio de prevención', 'Al contratar',
         'Reconocimientos médicos ofrecidos a cada persona que entra'),
        ('Información de alérgenos por escrito o de palabra con registro', 'Titular', 'Antes de abrir',
         'Por escrito en la carta o, si la das de palabra, registrada por escrito o en formato electrónico en el local, '
         'accesible y con un cartel que diga dónde pedirla (RD 126/2015, arts. 4.1.b y 6.5.a)'),
        ('Matriz de los 14 alérgenos con el pescado, el wasabi y la soja', 'Itamae', 'Antes de abrir',
         'Una fila por pieza y una columna por alérgeno, con lo que más se olvida: el pescado, la mostaza de algunas '
         'pastas de wasabi, el trigo de la salsa de soja y el del surimi y el sésamo de los uramaki. Revísala cada vez '
         'que cambie un proveedor o una receta'),
        ('No prometer «sin gluten» con soja de trigo, tempura y freidora compartida', 'Titular',
         'Antes de imprimir la carta',
         '«Sin gluten» sólo con 20 mg/kg o menos tal como se vende (Reglamento de Ejecución (UE) 828/2014). La salsa de '
         'soja lleva trigo, la tempura y el panko también y la freidora es compartida: informa del alérgeno y de las '
         'trazas y ofrece tamari sin prometerlo'),
    ]),
    ('F5 - Carta, marca y delivery', 'FASE 5: CARTA, MARCA, DELIVERY Y PROVEEDORES (semanas 8-16)', [
        ('Carta corta de unas 35 referencias y el menú del día', 'Itamae', 'Semana 8',
         'Nigiri, sashimi, hosomaki, uramaki, temaki, combinados de 12, 24 y 36 piezas, poke, gyozas, edamame, sopa de '
         'miso y mochi, más el menú del día de mediodía. Una carta de 60 platos llena la vitrina de neta que se tira'),
        ('Escandallo de cada pieza y de cada combinado por canal', 'Itamae', 'Semanas 10-14',
         'Con la calculadora del pescado, el arroz y el escandallo del pack: el coste de cada pieza y el margen en sala, '
         'para llevar y en plataforma. En plataforma el margen del combinado cae más de un cuarto'),
        ('IVA de la carta para llevar: la comida al 10 %, el alcohol y las bebidas azucaradas al 21 %',
         'Gestoría / Titular', 'Antes de abrir',
         'En sala, todo al 10 % (Ley 37/1992, art. 91.Uno.2.2.º). Para llevar y a domicilio, la comida al 10 %, pero la '
         'cerveza, el sake, el vino y los refrescos con azúcares o edulcorantes añadidos van al 21 % (art. '
         '91.Uno.1.1.º a y b). Configúralo así en el TPV y en cada plataforma'),
        ('Envases: lo que no se consume, sin coste; el plástico de un solo uso, cobrado', 'Titular', 'Antes de abrir',
         'El cliente puede llevarse lo que no consuma sin coste, y hay que avisarlo de forma visible, mejor en la carta '
         '(Ley 1/2025, art. 8). Los recipientes de plástico de un solo uso para llevar se cobran aparte en el tique (Ley '
         '7/2022, art. 55): pregunta a tu proveedor cuáles de tus cajas de sushi lo son'),
        ('Dos proveedores de pescado con su documentación', 'Titular', 'Semanas 8-12',
         'Uno de salmón y otro de atún y del resto, o dos de todo: con un solo proveedor, una mala semana te deja sin '
         'carta. Pide a cada uno el documento de congelación o de acuicultura, la temperatura de entrega y el precio por '
         'escrito: el plan los estima'),
        ('Proveedor de arroz para sushi, nori y salsas con su ficha técnica', 'Titular', 'Semanas 8-12',
         'Arroz de grano corto o medio para sushi (de 1,81 a 1,85 € el kilo sin IVA en sacos de 5 kg de mayorista, '
         'octubre de 2026), nori, vinagre de arroz, soja y wasabi, cada uno con su ficha y sus alérgenos'),
        ('Calendario de temporadas del pescado', 'Itamae', 'Semana 12',
         'Bonito del norte de junio a octubre, atún rojo de almadraba de abril a junio: las temporadas cambian el precio '
         'y la carta del mes. El Kit de Tareas Sushi Bar trae el calendario anual'),
        ('Contrato y alta en las plataformas de reparto con un techo', 'Titular', 'Antes de abrir',
         'Lee la comisión (del 13 al 35 % más IVA según la plataforma y la zona), cada cuánto liquidan, quién paga las '
         'promociones y el coste de las tablets. Fija un techo: en este plan, el 24 % de las ventas'),
        ('Precios para la plataforma y para la recogida en el local', 'Titular', 'Antes de abrir',
         'Calcula el margen del combinado en la plataforma con su comisión, el recargo y la caja; la recogida en el '
         'local no paga comisión: empújala. La tempura y las gyozas viajan mal: déjalas fuera del reparto o con envase '
         'ventilado'),
        ('Pedidos: alérgenos antes de comprar y frío durante el viaje', 'Titular', 'Antes del primer pedido',
         'En la venta a distancia, la información de alérgenos tiene que estar disponible antes de que el cliente '
         'compre (Reglamento (UE) 1169/2011, art. 14). Y el pedido viaja en cajas y bolsas que mantengan la '
         'temperatura (RD 1021/2022, art. 4.3), también en el reparto de la plataforma'),
        ('Marca en la OEPM, identidad, fotos y web con la carta y los alérgenos', 'Titular / Diseñador/a',
         'Semanas 2-14',
         'Comprueba antes que el nombre no está registrado en tu clase (servicios de restauración). Fotos reales de la '
         'barra y de las piezas; web con la carta, los alérgenos, el horario, los pedidos para recoger y la cláusula de '
         'protección de datos de cada canal'),
        ('Ficha de Google Business, redes y fechas fuertes', 'Titular', 'Antes de abrir',
         'Horario de comidas y cenas, fotos de la barra y respuesta a cada reseña. En el calendario, San Valentín y las '
         'bandejas de Nochebuena y Nochevieja, con encargo previo'),
        ('Música ambiental: licencias de SGAE y AGEDI-AIE', 'Titular', 'Antes de abrir',
         'Son dos licencias de propiedad intelectual, distintas de la municipal: pide las dos si pones música'),
    ]),
    ('F6 - Apertura y 90 días', 'FASE 6: APERTURA Y PRIMEROS 90 DÍAS', [
        ('Abrir en enero, el Mes 1 del plan', 'Titular', 'Mes 1',
         'El plan arranca en enero y la rampa va de enero a abril; agosto, con el cierre de vacaciones, es el mes más '
         'flojo: por eso el fondo de maniobra cuenta. Si abres en otro mes, gira la fila de estacionalidad de la '
         'Tesorería'),
        ('Desinsectación, desratización y desinfección (DDD)', 'Empresa del ROESB', 'Antes de abrir',
         'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
        ('Plan de limpieza de la barra, la vitrina y la cocina', 'Titular', 'Antes de abrir',
         'Vitrina de la neta, tablas por colores, cuchillos, arroceras y hangiri, freidora, plancha, filtros de la '
         'campana extractora y cuarto frío, con su registro'),
        ('Servicios de prueba con la carta completa', 'Itamae', 'Semana previa',
         'Varios servicios de prueba para ajustar los gramos de neta y de shari, los tiempos de la barra y el '
         'empaquetado de los pedidos antes de abrir'),
        ('Comprobar temperaturas y registros del primer día', 'Titular', 'Día 1',
         'Cámara, congelador, vitrina de la neta, pH del shari, caliente de las gyozas y la hoja de limpieza; corrige '
         'cualquier desviación antes de servir'),
        ('Inspección sanitaria: APPCC y registros a mano', 'Titular', 'Desde el día 1',
         'Registros de congelación y documentos de los proveedores, pH del shari, fichas de alérgenos, trazabilidad, '
         'temperaturas, limpieza, formación y DDD'),
        ('Mantenimiento del frío, del congelador y de la campana extractora', 'Titular / Empresa de mantenimiento',
         'Desde el mes 1',
         'Revisión del frigorista con la comprobación de que el congelador sigue llegando a −20 °C en el centro del '
         'pescado; la campana extractora y el conducto, al menos una vez al año (Madrid, Ordenanza 4/2021, art. 23)'),
        ('Calibración del pH-metro', 'Sushiman', 'Según su fabricante',
         'Con sus soluciones de calibración y anotada; un pH-metro sin calibrar da por bueno un shari que no lo está'),
        ('Medir el rendimiento del salmón y los gramos reales, y recalcular', 'Itamae', 'Semanas 1-12',
         'Limpia y pesa 3 salmones enteros, pesa 10 lonchas y 10 bolas de shari y lleva las medias a la calculadora del '
         'pack; compara después tu consumo real (compras de comida ÷ ventas de comida del mes) con el 29 % del plan'),
        ('Cuadrante y stock de las fechas fuertes y de agosto', 'Titular', 'Enero y julio',
         'Diciembre es el pico del año, con las bandejas de Nochebuena y Nochevieja, y febrero sube con San Valentín; '
         'agosto es el valle, con el cierre de 10 días: prepara el cuadrante, el pescado y los encargos con tiempo'),
        ('Revisar la cuenta de la plataforma cada mes', 'Titular', 'Mensual',
         'Ventas, comisión, promociones y cajas: si la plataforma pasa del 24 % de las ventas o su margen no cubre la '
         'comisión, recorta o sube precio. Reparto propio, sólo con contrato laboral y cuando el volumen lo pague'),
        ('Comparar ventas y costes reales con el plan cada mes', 'Titular', 'Mensual',
         'Comensales al día, ticket, mercancía y personal frente a la cuenta de resultados del Excel; revisa el '
         'escandallo cada vez que cambie el precio del salmón o del atún'),
        ('Seguir la tesorería mes a mes y el saldo mínimo', 'Titular', 'Mensual',
         'Enero abre la rampa y agosto es el mes más flojo: mira el saldo de cada mes antes de un pago grande'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 14, 13, 13, 13], [len(t) for _, _, t in FASES]
assert all(len(n) <= 29 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
