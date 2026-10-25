#!/usr/bin/env python3
"""datos_checklist.py — las 80 tareas del checklist de apertura de la Pizzería Napolitana ES 1.0 (SPEC D14; F1-camino §4:
12/15/14/13/13/13). Producto nuevo: no hay versión anterior; formato de `plan-heladeria/datos_checklist.py`.
Marco legal: `F1-research-pizzeria.md` §0-§1 y la lista de tareas obligadas de §3 (lo marcado 🟡 va como «compruébalo»):
  · RDLeg 1175/1990 (tarifas del IAE): grupo 671 «servicios en restaurantes» por categoría y epígrafe 677.9 «otros
    servicios de alimentación propios de la restauración» (venta para llevar y a domicilio); 673 sin comedor separado;
  · Ley 12/2012: los restaurantes no están en su anexo → licencia o declaración responsable por la ordenanza municipal;
    la terraza, siempre con autorización de ocupación de la vía pública (art. 2.2);
  · Ordenanza 4/2021 de Calidad del Aire de Madrid (BOCM 16-04-2021), arts. 12, 23 y anexo I: conducto exclusivo a
    cubierta, +1 m sobre lo que haya en 15 m, limpieza ≥ 1/año y filtro de partículas con leña (fuera de Madrid: la
    ordenanza de cada ayuntamiento); RD 100/2011 con RD 1042/2017: el horno < 1 MW no es actividad contaminadora;
  · RD 919/2006, ITC-ICG 07 (ap. 4.1-4.2) e ITC-ICG 08: instalación de gas por empresa habilitada, control cada 5 años;
  · RD 1021/2022: registro autonómico previa declaración responsable, art. 3 (RGSEAA sólo para el suministro a otros
    negocios por encima de sus límites), arts. 4.2 (temperatura de la etiqueta), 4.3 (transporte) y 5.3 (congelación);
  · RD 126/2015 (alérgenos sin envasar) y Reglamento (UE) 1169/2011, art. 14 (venta a distancia);
    Reglamento de Ejecución (UE) 828/2014 («sin gluten» ≤ 20 mg/kg); RD 760/2021, art. 7 (aceite en envase irrellenable);
  · Ley 1/2025, art. 8 (llevarse lo no consumido, aviso en la carta); Ley 7/2022, art. 55 (cobro del envase de plástico);
  · Reglamento (UE) 97/2010 (pliego de la ETG), Reglamento de Ejecución (UE) 2022/2313 (reserva del nombre) y
    Reglamento (UE) 2024/1143, arts. 68, 72 y 73 (protección y verificación previa);
  · ET arts. 1.1, 6 y 34.9 y DA 23.ª; ALEH VI art. 4 (convenio provincial de hostelería: pizzerías y reparto propio);
    Ley 31/1995 (PRL); Ley 18/2022 (SL desde 1 €).
Sin «carné», sin «licencia de apertura» y sin «tapa» en todo el libro. Cada tarea: (trámite / acción, responsable,
plazo, notas). Pestañas ≤ 31 caracteres. Sesión Claude Code, 25-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — PIZZERÍA NAPOLITANA'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Consulta urbanística previa: salida de humos a cubierta', 'Titular / Técnico', 'Antes de firmar el alquiler',
         'Pregunta al ayuntamiento si el uso permite un restaurante con horno de leña, si el local admite una salida de '
         'humos exclusiva hasta la cubierta (en Madrid, que supere en 1 m lo que haya en 15 m: Ordenanza 4/2021, art. 12 '
         'y anexo I), qué potencia y qué aforo tiene y si la calle admite terraza. Sin chimenea a cubierta no hay horno '
         'de leña'),
        ('Decidir horno de leña, de gas o eléctrico ANTES de firmar el local', 'Titular', 'Antes de firmar el alquiler',
         'La leña pide chimenea a cubierta y, en Madrid, filtro de partículas (Ordenanza 4/2021, art. 23); el gas, '
         'empresa instaladora habilitada (RD 919/2006); el eléctrico (unos 16,4 kW en trifásica el de seis pizzas) '
         'también necesita campana extractora y conducto para los vahos. Sólo la leña cumple el pliego de la ETG «Pizza '
         'Napoletana»'),
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036) en el grupo 671 y el epígrafe 677.9 del IAE', 'Gestoría', 'Semana 2',
         'El 671 («servicios en restaurantes», por categoría, de uno a cinco tenedores) cubre la sala; el 677.9 («otros '
         'servicios de alimentación propios de la restauración») cubre la venta para llevar y a domicilio (RDLeg '
         '1175/1990). Sin comedor separado, el grupo 673. Exento de cuota con una cifra de negocio inferior a 1 millón '
         'de euros (art. 82.1.c de la Ley de Haciendas Locales; confírmalo con tu gestoría)'),
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
         'horno y del frío y de una línea ICO'),
        ('Seguro de responsabilidad civil y multirriesgo con incendio', 'Corredor de seguros', 'Antes de la obra',
         'RC de al menos 300.000 € y multirriesgo con incendio y avería del frío. Dile a la aseguradora que el horno es '
         'de leña'),
        ('Registro de la marca en la OEPM', 'Titular', 'Semanas 2-4',
         'Comprueba antes que el nombre no está registrado en tu clase (servicios de restauración). No metas '
         '«napolitana» ni «napoletana» en la marca sin consultarlo: el nombre de la ETG está protegido frente a la '
         'evocación (Reglamento (UE) 2024/1143, art. 68.1)'),
    ]),
    ('F2 - Local, humos y licencia', 'FASE 2: LOCAL, SALIDA DE HUMOS, LICENCIA Y TERRAZA (semanas 3-14)', [
        ('Elegir el local: 120-140 m² con salida de humos a cubierta posible', 'Titular', 'Semanas 3-6',
         'Sala de unos 70 m² para 50 plazas, obrador de unos 30 m² con el horno a la vista, almacén de leña seco, '
         'aseos y vestuario. Calle de barrio con paso de gente por la noche y el fin de semana'),
        ('Comprobar la potencia: unos 25 kW en trifásica', 'Técnico / Distribuidora', 'Antes de firmar',
         'Frío, amasadora, lavavajillas, extracción, climatización y cafetera; con horno eléctrico, unos 16 kW más. Un '
         'local monofásico obliga a una acometida nueva: pregunta plazo y coste a la distribuidora'),
        ('Comprobar con el técnico el recorrido de la chimenea hasta cubierta', 'Técnico', 'Antes de firmar',
         'Conducto exclusivo, continuo y estanco hasta la cubierta, por patio o fachada, con el permiso de la comunidad '
         'de propietarios si cruza zonas comunes'),
        ('Negociar el alquiler: carencia de obra y fianza', 'Titular', 'Antes de firmar',
         'El plan cuenta tres meses de renta antes de abrir y tres de fianza. Pide carencia mientras duran la obra y la '
         'chimenea'),
        ('Contrato de arrendamiento con el uso de pizzería con horno de leña', 'Titular / Abogado', 'Semana 6',
         'Que diga «restaurante-pizzería con horno de leña» y que autorice la obra de la chimenea y la salida de humos'),
        ('Encargar el proyecto técnico de la actividad y de la salida de humos', 'Arquitecto/a o ingeniero/a',
         'Semanas 6-8',
         'Distribución del obrador, potencia, aforo, ventilación, accesibilidad y la chimenea con su filtro de '
         'partículas si es de leña (Madrid, Ordenanza 4/2021, art. 23). Fuera de Madrid, pide la ordenanza de humos y '
         'de calidad del aire de tu ayuntamiento'),
        ('Licencia o declaración responsable de la actividad', 'Técnico / Ayuntamiento', 'Antes de la obra',
         'Los restaurantes (grupo 671 y epígrafe 677.9) no están en el anexo de la Ley 12/2012: van por el régimen de '
         'tu ayuntamiento, licencia o declaración responsable según su ordenanza. Pregunta cuál te toca en la consulta '
         'previa'),
        ('Licencia, declaración o comunicación previa de la obra', 'Técnico / Ayuntamiento',
         'Semanas 6-8, antes de empezar la obra',
         'La obra y la chimenea van por su propio trámite municipal: pregunta en la consulta previa qué título piden'),
        ('Solicitar la autorización de la terraza', 'Titular / Ayuntamiento', 'Con la licencia de la actividad',
         'Es ocupación de la vía pública y siempre se pide aparte (Ley 12/2012, art. 2.2). Pregunta la tasa y el '
         'horario de tu ayuntamiento'),
        ('Si hay gas: empresa instaladora habilitada y certificado', 'Instalador de gas habilitado', 'Durante la obra',
         'Certificado de la instalación, puesta en marcha certificada del aparato e inspección o revisión cada 5 años '
         '(RD 919/2006, ITC-ICG 07 e ITC-ICG 08)'),
        ('Obra del obrador y de la sala: superficies lavables', 'Constructor', 'Semanas 8-12',
         'Paredes alicatadas, suelo antideslizante, falsos techos lavables, lavamanos de accionamiento no manual, '
         'aseos (uno adaptado) y aislamiento acústico si hay vecinos'),
        ('Chimenea, filtro de partículas y bancada del horno', 'Instalador / Técnico', 'Semanas 8-12',
         'Conducto de doble pared hasta cubierta y una bancada que aguante el peso del horno: pide el dato al '
         'fabricante antes de la obra'),
        ('Fontanería, separador de grasas, climatización y extracción', 'Instalador', 'Semanas 8-12',
         'Agua fría y caliente en el obrador, desagües con separador de grasas, climatización de la sala y extracción '
         'de la cocina de apoyo'),
        ('Montaje del horno y curado del refractario', 'Fabricante / Instalador', 'Semanas 11-13',
         'El refractario nuevo se cura con fuegos crecientes, según las instrucciones del fabricante: no lo lleves a '
         'la temperatura de servicio el primer día'),
        ('Aumento de potencia, boletín eléctrico y certificado final de obra', 'Instalador autorizado / Técnico',
         'Durante la obra y al acabarla',
         'El boletín (certificado de la instalación) para el nuevo contrato de luz en trifásica y el certificado final '
         'del técnico. Guárdalos: te los pedirá el ayuntamiento'),
    ]),
    ('F3 - Cocina, horno y sanidad', 'FASE 3: COCINA, HORNO Y REGISTRO SANITARIO (semanas 6-14)', [
        ('Comprar el horno, la amasadora y la mesa fría de pizza', 'Titular', 'Semanas 6-8',
         'Horno de leña de 120-130 cm de diámetro (unas seis pizzas a la vez), amasadora de espiral para 30-40 kg de '
         'masa y mesa fría con granito. Pide ficha técnica, potencia, plazo de entrega y montaje'),
        ('Comprar los armarios para las cajas de bolas y el frío de ingredientes', 'Titular', 'Semanas 8-10',
         'Armarios ventilados para las cajas de bolas y los quesos, un arcón y las cajas con cierre para las bolas'),
        ('Almacén de leña seca y sin tratar, separado del horno', 'Titular', 'Antes de abrir',
         'Encina, roble, haya u olivo, seca; nunca madera pintada, barnizada ni aglomerado. Almacén seco, ventilado y '
         'separado de la boca del horno, y un proveedor con entrega regular'),
        ('Declaración responsable al registro sanitario autonómico', 'Titular / Gestoría',
         'Antes de la primera prueba de carta',
         'Va al registro sanitario de tu comunidad autónoma (RD 1021/2022). El registro estatal (RGSEAA) sólo aplica '
         'si sirves a otros negocios por encima de lo que permite el art. 3 del mismo real decreto'),
        ('Plan APPCC con la masa: tiempos y temperaturas de las bolas', 'Consultor / Titular', 'Antes de abrir',
         'Masa del día: primera fermentación, boleado, segunda fermentación a temperatura ambiente y uso en las horas '
         'que fije tu APPCC (el pliego de la ETG pide 2 h + 4-6 h y usar la bola en las 6 h siguientes). Masa en frío: '
         'la temperatura y el tiempo que valide tu APPCC, con el registro de cada amasada'),
        ('APPCC: quesos y embutidos a la temperatura de su etiqueta', 'Titular', 'Antes de abrir',
         'Ninguna norma estatal fija la temperatura del fior di latte, la búfala o los embutidos: manda la etiqueta del '
         'fabricante (RD 1021/2022, art. 4.2). Lo que congeles, envasado y con la fecha de elaboración y la de '
         'congelación (art. 5.3)'),
        ('Trazabilidad y registros: amasadas, temperaturas y proveedores', 'Titular', 'Desde la primera amasada',
         'Lote y fecha de la harina y de los quesos, hora de cada amasada, temperaturas del frío y proveedor de cada '
         'materia prima'),
        ('Fichas técnicas por pizza con sus alérgenos', 'Pizzaiolo jefe', 'Antes de abrir',
         'Gluten (todas), leche (quesos), frutos de cáscara (pesto, pistacho), pescado (anchoa), mostaza y sulfitos '
         '(embutidos, vino), y sésamo y huevo si los usas. Con la calculadora del pack, el coste de cada una'),
        ('Información de alérgenos en la carta y en la sala', 'Titular', 'Antes de abrir',
         'Por escrito en la carta, o de palabra si está registrada por escrito y un cartel dice dónde pedirla (RD '
         '126/2015)'),
        ('Alérgenos en la venta por plataforma o por tu web', 'Titular', 'Antes de darte de alta',
         'En la venta a distancia, la información de alérgenos tiene que estar disponible antes de que el cliente '
         'compre (Reglamento (UE) 1169/2011, art. 14). Revisa la ficha de cada pizza en cada plataforma'),
        ('No prometer «sin gluten» sin protocolo y analítica', 'Titular', 'Antes de imprimir la carta',
         '«Sin gluten» sólo con 20 mg/kg o menos tal como se vende (Reglamento de Ejecución (UE) 828/2014). Con harina '
         'en el aire del obrador no lo pongas, salvo masa comprada sin gluten, zona y horno separados y analítica'),
        ('Aceite en la mesa en envase irrellenable', 'Titular', 'Antes de abrir',
         'Envase etiquetado, con un cierre que no se pueda reutilizar (RD 760/2021, art. 7). Las garrafas grandes, sólo '
         'en la cocina'),
        ('Temperatura de los pedidos que salen del local', 'Titular', 'Antes del primer pedido',
         'Cajas y bolsas que mantengan la temperatura durante el transporte (RD 1021/2022, art. 4.3), también en el '
         'reparto de la plataforma'),
        ('Proveedores de harina, tomate, quesos y cajas', 'Titular', 'Semanas 10-14',
         'Dos proveedores por materia prima clave (harina, fior di latte, tomate) y cajas de cartón para llevar. El '
         'cartón no es plástico de un solo uso; si la caja lleva película plástica, pregúntalo al proveedor'),
    ]),
    ('F4 - Personal y prevención', 'FASE 4: PERSONAL, FORMACIÓN Y PREVENCIÓN (semanas 10-14)', [
        ('Copiar la tabla salarial del convenio provincial de hostelería', 'Gestoría', 'Semana 10',
         'Las pizzerías están en el convenio provincial de hostelería (VI Acuerdo Laboral de ámbito Estatal para el '
         'sector de Hostelería, art. 4). Pon su salario más bajo en la hoja de Supuestos del plan'),
        ('Contratos por escrito a jornada completa y parcial', 'Gestoría', 'Antes de abrir',
         'Con su horario y su grupo del convenio. Una factura de «autónomo» con tu horario y tu dirección es falso '
         'autónomo (art. 1.1 del Estatuto de los Trabajadores)'),
        ('Contratar al segundo pizzaiolo antes de abrir', 'Titular', 'Semanas 10-12',
         'Que aprenda la masa y el horno contigo antes de abrir: si sólo tú los sabes, una baja cierra la pizzería'),
        ('Registro de jornada', 'Titular', 'Desde el primer contrato',
         'Obligatorio para toda la plantilla (art. 34.9 ET), también a tiempo parcial'),
        ('Cuadrante de los dos servicios y del sábado por la noche', 'Titular', 'Semana 12',
         'Comidas y cenas de martes a domingo, con el lunes de cierre; el sábado por la noche hacen falta unas cinco '
         'personas'),
        ('Reparto propio: sólo con contrato laboral', 'Gestoría', 'Si repartes tú',
         'El repartidor propio es hostelería (ALEH VI, art. 4) y trabaja por cuenta ajena; en el reparto organizado por '
         'una plataforma digital, la ley presume la relación laboral (ET, disposición adicional 23.ª). Nunca con '
         '«autónomos»'),
        ('Menores de 18 años: sin noche ni horas extra', 'Gestoría', 'Si contratas a menores',
         'No pueden trabajar de noche ni hacer horas extraordinarias (art. 6 ET): confírmalo con tu gestoría si las '
         'cenas acaban a medianoche'),
        ('Formación de manipuladores de alimentos', 'Titular', 'Antes de abrir',
         'La da y la acredita la empresa (no hay un documento oficial que sacar): higiene, temperaturas de la masa y '
         'de los quesos, alérgenos y contacto cruzado'),
        ('Formación de pizzaiolo y del horno de leña', 'Titular', 'Antes de abrir',
         'Masa, fermentación, estirado a mano, manejo del fuego y de la pala: es inversión, no gasto'),
        ('Plan de prevención de riesgos laborales', 'Servicio de prevención', 'Antes de abrir',
         'Obligatorio (Ley 31/1995): quemaduras del horno, cortes, cargas de leña y de sacos de harina, humo y calor'),
        ('Vigilancia de la salud de la plantilla', 'Servicio de prevención', 'Al contratar',
         'Reconocimientos médicos ofrecidos a cada persona que entra'),
        ('Desinsectación, desratización y desinfección (DDD)', 'Empresa del ROESB', 'Antes de abrir',
         'Contrato con una empresa inscrita en el ROESB: forma parte de los prerrequisitos del APPCC'),
        ('Plan de limpieza del obrador, la sala y el horno', 'Titular', 'Antes de abrir',
         'Mesa fría, amasadora, cajas de bolas, palas y la boca del horno; las cenizas, en un recipiente metálico; con '
         'su registro'),
    ]),
    ('F5 - Carta, marca y delivery', 'FASE 5: CARTA, MARCA, DELIVERY Y CAPTACIÓN (semanas 8-16)', [
        ('Decidir el tipo de pizzería y su carta', 'Titular', 'Semana 8',
         'Con sala y horno de leña (este plan), al corte, sólo de reparto o franquicia: cada una con otra inversión, '
         'otro local y otro margen'),
        ('Carta sin «pizza napolitana» salvo verificación de la ETG', 'Titular', 'Antes de imprimir la carta',
         '«Pizza Napoletana» es una especialidad tradicional garantizada con reserva de nombre desde el 18-12-2022 '
         '(Reglamento de Ejecución (UE) 2022/2313), protegida también traducida (Reglamento (UE) 2024/1143, art. 68.1). '
         'Sin el pliego y la verificación, usa el nombre de la receta: «Margherita», «Marinara», «Diavola». «Estilo '
         'napolitano» en el rótulo: consúltalo antes. La certificación de la AVPN es privada y no la sustituye'),
        ('Aviso en la carta: el cliente puede llevarse lo que no consuma', 'Titular', 'Antes de abrir',
         'Sin coste, salvo el del envase de plástico de un solo uso si lo hay, y avisado de forma visible, mejor en la '
         'carta (Ley 1/2025, art. 8). Ten envases para ello'),
        ('Cobro aparte del envase de plástico de un solo uso', 'Titular', 'Antes de abrir',
         'Los envases de plástico de un solo uso para llevar se cobran aparte en el tique (Ley 7/2022, art. 55). La '
         'caja de cartón no es plástico'),
        ('Carta de 14-16 pizzas, entrantes y postres con su escandallo', 'Pizzaiolo jefe', 'Semanas 10-14',
         'Escandalla cada pizza, no sólo la Margherita: con búfala, burrata o embutido italiano y la comisión de la '
         'plataforma, la que más se vende puede irse al 25-35 %. Usa la calculadora de masa y escandallo del pack'),
        ('Contrato y alta en las plataformas de reparto', 'Titular', 'Antes de abrir',
         'Lee la comisión (del 25 al 35 % más IVA con su reparto, según la zona), cada cuánto liquidan, quién paga las '
         'promociones y el coste de la tablet. Fija un techo: en este plan, el 10 % de las ventas'),
        ('Precios para la plataforma y para la recogida en el local', 'Titular', 'Antes de abrir',
         'Calcula el margen de cada pizza en la plataforma con su comisión y la caja; la recogida en el local no paga '
         'comisión: empújala'),
        ('Identidad, fotos y web con la carta', 'Diseñador/a', 'Semanas 8-14',
         'Fotos reales del horno y de las pizzas; web con la carta, los alérgenos, el horario y los pedidos para '
         'recoger'),
        ('Ficha de Google Business y reseñas', 'Titular', 'Antes de abrir',
         'Horario de comidas y cenas, fotos del horno y respuesta a cada reseña'),
        ('Redes sociales: la obra, el horno y la masa', 'Titular', 'Desde la obra',
         'El montaje del horno, el primer fuego, la masa y la pizza de la semana'),
        ('Fiesta de apertura para el barrio', 'Titular', 'Semana de apertura',
         'Degustación para vecinos, comercios y colegios: el horno a la vista es tu escaparate'),
        ('Música ambiental: licencias de SGAE y AGEDI-AIE', 'Titular', 'Antes de abrir',
         'Son dos licencias de propiedad intelectual, distintas de la municipal: pide las dos si pones música'),
        ('Cláusula informativa de protección de datos', 'Titular', 'Antes de abrir',
         'En la web, en las reservas y en los pedidos: cada canal necesita su información previa'),
    ]),
    ('F6 - Apertura y 90 días', 'FASE 6: APERTURA Y PRIMEROS 90 DÍAS', [
        ('Abrir en septiembre', 'Titular', 'Mes 1',
         'El plan abre después del verano: la rampa cae en meses medios y altos, llegas a la Navidad con clientela y a '
         'enero y febrero, los meses más flojos, con el fondo intacto'),
        ('Pruebas de masa y de horno con la carta completa', 'Pizzaiolo jefe', 'Semana previa',
         'Varias amasadas y servicios de prueba para ajustar la masa, el fuego y los tiempos del pase antes de abrir'),
        ('Comprobar temperaturas y registros del primer día', 'Titular', 'Día 1',
         'Frío de las bolas y de los quesos, hora de cada amasada y la hoja de limpieza; corrige cualquier desviación '
         'antes de servir'),
        ('Inspección sanitaria: APPCC y registros a mano', 'Titular', 'Desde el día 1',
         'Fichas de alérgenos, trazabilidad, registros de temperatura y de limpieza, formación y DDD'),
        ('Calendario de deshollinado, campana extractora y refractario', 'Titular / Empresa de mantenimiento', 'Desde el mes 1',
         'Limpieza de la campana extractora y de los conductos al menos una vez al año (Madrid, Ordenanza 4/2021, art. 23), '
         'deshollinado y filtro de partículas del horno según su uso, y revisión del refractario en el cierre de enero'),
        ('Cuadrante de diciembre y del sábado por la noche', 'Titular', 'Noviembre',
         'Cenas de empresa y de grupo: diciembre es el pico del año (el Mes 4 del plan)'),
        ('Controlar las bolas: producción por día de la semana', 'Pizzaiolo jefe', 'Semanal',
         'Bolas pasadas un sábado flojo y faltas uno lleno: ajusta la amasada a las reservas y anota la merma'),
        ('Medir el coste de cada pizza cada mes', 'Titular', 'Mensual',
         'El precio de la harina, del queso y del tomate frente al escandallo; revísalo cuando cambie un proveedor'),
        ('Revisar la cuenta de la plataforma cada mes', 'Titular', 'Mensual',
         'Ventas, comisión, promociones y cajas: si la plataforma pasa del 10 % de las ventas o su margen no cubre la '
         'comisión, recorta o sube precio. Reparto propio, sólo con contrato laboral y cuando el volumen lo pague'),
        ('Comparar ventas y costes reales con el plan cada mes', 'Titular', 'Mensual',
         'Comensales al día, ticket, mercancía y personal frente a la cuenta de resultados del Excel'),
        ('Seguir la tesorería mes a mes y el saldo mínimo', 'Titular', 'Mensual',
         'Enero y febrero son los meses más flojos: mira cuánta caja te llega de diciembre'),
        ('Cierre de dos semanas en enero: mantenimiento y vacaciones', 'Titular', 'Enero',
         'Revisión del horno, de la campana extractora y del frío con el local cerrado, y vacaciones de la plantilla'),
        ('Si quieres la ETG: comunicación, autocontrol y verificación previa', 'Titular',
         'Cuando la masa y el horno cumplan el pliego',
         'Para poner «Pizza Napoletana ETG» en la carta: informa a la autoridad competente, documenta el autocontrol y '
         'pasa una verificación del pliego antes de vender (Reglamento (UE) 2024/1143, arts. 72-73); los costes pueden '
         'ser tuyos. Pregunta en tu comunidad autónoma quién la hace y cuánto cuesta'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 14, 13, 13, 13], [len(t) for _, _, t in FASES]
assert all(len(n) <= 31 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
