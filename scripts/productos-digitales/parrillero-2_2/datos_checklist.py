#!/usr/bin/env python3
"""datos_checklist.py — las 83 tareas del checklist de apertura del Parrillero / Asador ES 2.2 (SPEC D10: 12/16/14/10/16/15).
Origen: las 93 tareas de la 1.1 (`dl/plan-negocio-parrillero-asador-eventos/checklist-apertura-parrillero-asador-eventos.xlsx`,
6 hojas C3; mapa fila a fila en `F1-camino-2_2.md` §3), las del Paellero ES 2.2 que valen para un parrillero
(`paellero-2_2/datos_checklist.py`, con su marco legal ya verificado) y el delta del research
(`F1-research-parrillero.md` §0-§1):
  · RD 1021/2022, art. 13.5.b (no se prepara en casa para eventos) y su DF 1.ª (registro autonómico previa
    declaración responsable; RGSEAA sólo si se suministra a otros establecimientos);
  · Reglamento (CE) 853/2004 (temperaturas de recepción, como estándar del APPCC); RD 1086/2020, arts. 26.2 y 30
    (MER y deshuesado; 63 °C y comida testigo); AESAN 70/74 °C (recomendación);
  · RD 919/2006, art. 2.1.h e ITC-ICG 08/06 (gas del plan B); ADR 1.1.3.6 (🟡); Ley 43/2003, art. 44.3 (fuego);
  · Ley 9/2017, arts. 118 y 198.4; Ley 25/2013, art. 4; Ley 7/1996, arts. 53-54; TRLGDCU art. 103.l;
    RDLeg 1175/1990, epígrafe 677.9; Reglamento del IRPF, art. 95.6 (sin retención en las facturas);
  · ET arts. 1.1, 16 y 34.9; Reglamento (CE) 852/2004, anexo II, cap. XII; Reglamento (UE) 1169/2011.
Sin «carné» en todo el libro (el gate de ortografía del motor confunde «carne» y «carné»: F2-NOTAS del paellero §5).
Cada tarea: (trámite / acción, responsable, plazo, notas). Pestañas ≤ 31 caracteres. Sesión Claude Code, 12-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — PARRILLERO / ASADOR PARA EVENTOS'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036/037) en el epígrafe 677.9 del IAE', 'Gestoría', 'Semana 2',
         'La nota del epígrafe 677.9 («otros servicios de alimentación propios de la restauración», RDLeg '
         '1175/1990) incluye el servicio de comidas para eventos. Exento de cuota con una cifra de negocio inferior '
         'a 1 millón de euros'),
        ('Alta en la Seguridad Social (administrador o autónomo)', 'Gestoría', 'Semana 2',
         'Consulta la cuota del ejercicio en curso y si te aplica la cuota reducida de inicio de actividad'),
        ('Certificado digital', 'Titular', 'Semana 1',
         'Imprescindible para Hacienda, la Seguridad Social, la declaración responsable sanitaria y FACe'),
        ('Cuenta bancaria y tarjeta del negocio', 'Titular', 'Semana 2',
         'Separadas de las personales: por ellas pasan las señales, las facturas de empresas y ayuntamientos y '
         'los pagos a la carnicería'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Semanas 2-4',
         'Nóminas de los fijos discontinuos cada mes con llamamientos. El software de facturación tiene que cumplir '
         'el RD 1007/2023 (Veri*factu): confirma la fecha que te aplica antes de contratarlo'),
        ('IVA trimestral (modelo 303) al 10 %', 'Gestoría', 'Cada trimestre',
         'Servicio de parrilla en el evento al 10 %, alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992). '
         'Carpas o mobiliario facturados aparte, al 21 %'),
        ('Pagos fraccionados y retenciones de las nóminas (modelos 202 o 130, y 111)', 'Gestoría', 'Cada trimestre',
         'SL: modelo 202; autónomo: modelo 130. Tus facturas a empresas NO llevan retención de IRPF: el epígrafe '
         '677.9 es una actividad empresarial (art. 95.6 del Reglamento del IRPF). El 111 recoge las retenciones '
         'de las nóminas'),
        ('Declaraciones anuales: 390 y 347', 'Gestoría', 'Enero-febrero',
         '390: resumen anual del IVA. 347: clientes o proveedores con más de 3.005,06 € en el año (la carnicería, '
         'las fincas y los ayuntamientos habituales suelen pasarlo)'),
        ('RGPD: registro de actividades de tratamiento y cláusulas en presupuestos y contratos', 'Titular',
         'Antes del primer presupuesto',
         'Art. 30 del RGPD y LOPDGDD. Tratas datos de clientes, de invitados (las alergias son datos de salud) y '
         'del personal'),
        ('Web: aviso legal, privacidad, cookies (LSSI) y condiciones de contratación', 'Titular',
         'Antes de publicar la web',
         'Precio final con IVA para particulares. En un servicio de comida con fecha no hay derecho de '
         'desistimiento de 14 días (art. 103.l del TRLGDCU): tu política de señal (30 %), pagos y cancelación tiene '
         'que estar escrita y firmada, como en los contratos del kit'),
    ]),
    ('F2 - Sanidad, fuego y brasa', 'FASE 2: COCINA DE APOYO, SANIDAD, FUEGO, BRASA Y PERMISOS (semanas 3-8)', [
        ('Contrato de uso de una cocina de apoyo compartida y autorizada', 'Titular', 'Semanas 3-6',
         'La carne se asa en el evento, pero los marinados, las salmueras y el porcionado no se pueden hacer en '
         'casa: lo prohíbe el art. 13.5.b del RD 1021/2022. Pide en el contrato horas, cámara para la carne, '
         'almacén de parrillas, carbón y remolque, DDD y residuos'),
        ('Declaración responsable e inscripción en el registro sanitario autonómico', 'Titular',
         'Antes del primer evento',
         'Un servicio que vende al consumidor final se inscribe en el registro de su comunidad autónoma previa '
         'declaración responsable (RD 1021/2022, que reescribe el art. 2 del RD 191/2011)'),
        ('RGSEAA: sólo si suministras a otros establecimientos', 'Titular', 'Solo si aplica',
         'El Registro General Sanitario (RGSEAA) sólo hace falta si suministras a otros establecimientos (carne '
         'marinada o asada para restaurantes) de forma no marginal; para servir al cliente final, no (art. 2 del '
         'RD 191/2011)'),
        ('Plan APPCC itinerante: recepción, frío, cocción y mantenimiento en caliente', 'Titular',
         'Antes del primer evento',
         'Recepción con sonda: carne a 7 °C o menos, despojos (achuras, mollejas) a 3 °C, aves y preparados '
         '(chorizo criollo, hamburguesas) a 4 °C y picada a 2 °C (Reglamento (CE) 853/2004, como estándar). '
         'Cocción: 70 °C en el centro de la carne y 74 °C en las aves (recomendación de AESAN); «poco hecho» sólo '
         'en piezas enteras de vacuno o cordero y a petición. Lo que se sirve en caliente, a 63 °C o más (art. 30 '
         'del RD 1086/2020); alioli con huevo pasteurizado'),
        ('Comida testigo de cada plato', 'Titular', 'Desde el primer evento',
         'Guarda 100 g de cada plato, identificados y fechados, a 4 °C o menos o congelados, durante 7 días: '
         'obligatoria en eventos de más de 40 personas y si los eventos son tu actividad principal (art. 30.8 y '
         '30.10 del RD 1086/2020)'),
        ('Fichas de alérgenos de cada menú y de las salsas', 'Titular', 'Antes del primer evento',
         'Reglamento (UE) 1169/2011 y RD 126/2015: leche de la provoleta, gluten del pan, de las empanadas y de '
         'algunas salsas y embutidos, sulfitos del vinagre y del vino de los marinados, mostaza, apio y soja de '
         'rubs y salsas, huevo del alioli. El embutido manda por su etiqueta. Rejilla aparte para las opciones sin '
         'gluten o veganas'),
        ('Carne: etiqueta, trazabilidad y chuletón con vértebra', 'Titular', 'Desde la primera compra',
         'Guarda etiquetas y albaranes (Reglamento (CE) 178/2002, art. 18). Chuletón o T-bone con vértebra sólo de '
         'vacuno de origen de riesgo insignificante (España) o de menos de 30 meses; si la pieza llega con banda '
         'roja, nunca la deshuesas tú (RD 1086/2020, art. 26.2). En la carta, la denominación de la etiqueta '
         '(ternera, añojo, vaca) y «madurada» sólo con el documento del proveedor'),
        ('Seguro de responsabilidad civil con incendio e intoxicación alimentaria', 'Aseguradora',
         'Antes del primer evento',
         'Recomendado: al menos 600.000 €, con incendio (brasas y chispas sobre carpas, césped y pavimento), daños '
         'al recinto y RC de producto. Es lo que suelen pedir fincas, empresas y ayuntamientos: adjunta el '
         'certificado a los presupuestos'),
        ('Seguro de la furgoneta y del remolque', 'Aseguradora', 'Al comprarlos',
         'Declara el uso profesional, el remolque-parrilla y la carga de botellas de gas y de carbón'),
        ('Seguro de equipos y cláusula de fuerza mayor con plan B', 'Titular / Aseguradora', 'Antes del primer evento',
         'La cancelación por una prohibición de fuego no se asegura: va en la cláusula de fuerza mayor de los dos '
         'contratos (particular y empresa), con el plan B de gas o el cambio de fecha'),
        ('Plan B de gas: una botella de menos de 15 kg por aparato', 'Titular', 'Antes del primer evento',
         'Plancha o parrilla de piedra volcánica: una botella de menos de 15 kg conectada a un solo aparato móvil '
         'no es una instalación y la conectas tú, con regulador y tubo flexible en fecha (RD 919/2006, art. 2.1.h; '
         'ITC-ICG 08 §5.2). Aparatos con marcado CE (Reglamento (UE) 2016/426). Con botellas de 35 kg o varias '
         'conectadas, la monta una empresa instaladora (ITC-ICG 06)'),
        ('Transporte de las botellas y del carbón en la furgoneta', 'Titular', 'Antes del primer evento',
         'Hasta 333 kg de gas por vehículo se viaja en el régimen de exención del ADR (1.1.3.6): botellas en pie y '
         'sujetas, ventilación, válvulas cerradas y un extintor de 2 kg (fuente secundaria: confírmalo con tu '
         'aseguradora). El carbón, con su ficha de datos de seguridad, seco y lejos de las botellas'),
        ('Extintores, manta y distancias en cada evento', 'Titular', 'Antes del primer evento',
         'Un extintor de polvo ABC de 6 kg por zona de fuego, revisado por una empresa mantenedora (RD 513/2017), '
         'manta ignífuga y arena. La parrilla, a 3 m o más de carpas y lonas y a sotavento de los invitados'),
        ('Brasas, cenizas, residuos y hojas de reclamaciones', 'Titular', 'Antes del primer evento',
         'Brasas y cenizas apagadas con agua en un contenedor metálico con tapa; la ceniza fría, a la fracción '
         'resto, nunca enterrada ni en terreno forestal. Nunca ensaques brasa recién apagada. Aceite usado a un '
         'gestor autorizado y hojas de reclamaciones según la norma de tu comunidad'),
        ('Fuego y leña: época de peligro y franja forestal de cada comunidad', 'Titular', 'Por evento',
         'Cada comunidad regula el fuego en montes y zonas colindantes (Ley 43/2003, art. 44.3): franja de 400-500 m '
         'y época de peligro en verano. La brasa es tu producto: en alerta máxima caen las autorizaciones y algunas '
         'prohíben también el gas. La licencia de la finca no levanta la restricción. Consulta el anexo autonómico '
         'del plan de negocio'),
        ('Autorización del recinto o municipal, humos y venta al público', 'Titular', '30-60 días antes',
         'Vía pública: autorización del ayuntamiento. Finca privada: permiso del propietario; en terreno forestal, '
         'manda la norma autonómica. En suelo urbano, mira la ordenanza de humos y lleva el gas. Asador a la cruz o '
         'fuego en el suelo: base incombustible, perímetro y permiso expreso de la finca. Vender raciones al público '
         'por tu cuenta (barra o puesto de fiestas con canon) es venta no sedentaria con autorización municipal '
         '(Ley 7/1996, arts. 53-54)'),
    ]),
    ('F3 - Equipo y proveedores', 'FASE 3: EQUIPAMIENTO Y PROVEEDORES (semanas 4-8)', [
        ('Parrillas y remolque-parrilla según la tabla de escalado', 'Titular', 'Mes 1',
         'Una parrilla de 120 cm por cada 60-80 invitados en dos o tres tandas (tabla de escalado del manual '
         'técnico); el remolque con cruz para bodas y fiestas. El catálogo trae los modelos'),
        ('Cruces, brasero y kit de costillar', 'Titular', 'Mes 1',
         'Cordero o cochinillo a la cruz y costillar; el brasero mantiene la brasa de reserva'),
        ('Ahumador, sólo si vendes el BBQ texano', 'Titular', 'Mes 2',
         'Brisket de 8-12 horas y pulled pork: planificación de un día y sonda con registro'),
        ('Plancha o parrilla de piedra volcánica de gas (plan B)', 'Titular', 'Mes 1',
         'Con sus botellas y reguladores: es lo que salva el evento cuando una alerta prohíbe la brasa'),
        ('Carbón y leña con proveedor fijo y ficha de seguridad', 'Titular', 'Mes 1',
         'Encina, quebracho o marabú con su ficha de datos de seguridad (UNE-EN 1860-2). Si es importado, pide al '
         'importador su declaración de diligencia debida (Reglamento (UE) 2023/1115, que le obliga a él)'),
        ('Cuchillería, tablas de colores y pinzas', 'Titular', 'Mes 1',
         'Tablas por colores para separar carne cruda, carne cocinada y verdura (APPCC), y pinzas distintas para '
         'lo crudo y lo hecho'),
        ('Vajilla, cubertería y tablas de servicio para tu dotación', 'Titular', 'Mes 1-2',
         'Para los invitados de un evento medio; en bodas grandes y fiestas, menaje de alquiler o desechable '
         'compostable'),
        ('Armario refrigerado, isotermos, acumuladores y sondas', 'Titular', 'Mes 1',
         'La carne, a 7 °C o menos hasta que entra en la parrilla; sonda en la recepción y en la nevera del evento'),
        ('Básculas de cocina y de precisión', 'Titular', 'Mes 1',
         'Para escandallar cada evento con la calculadora del kit: 350-450 g de carne cruda por invitado con '
         'entrantes'),
        ('Carpa, mesas, lavamanos portátil y protector de césped', 'Titular', 'Mes 1',
         'Carpa a 3 m o más de la parrilla, mesa de corte y de servicio, y protección del césped o del pavimento'),
        ('EPI de calor y uniformes', 'Titular', 'Mes 1',
         'Delantal de cuero, guantes térmicos y calzado de seguridad para cada persona del equipo'),
        ('Carnicería mayorista con trazabilidad y precio pactado', 'Titular', 'Mes 1',
         'Vacuno con etiqueta (nacido, criado y sacrificado en), achuras y embutido en frío; pacta el precio por '
         'trimestre: el vacuno se mueve mucho'),
        ('Pan, verdura, salsas y bebida del pack', 'Titular', 'Mes 1',
         'Pan del día, verdura de temporada para la parrilla y bebida para el pack de celebraciones y empresas'),
        ('Furgoneta frigorífica, TPV y software de presupuestos', 'Titular', 'Mes 1-2',
         'Certificado ATP vigente (RD 237/2000), anclajes de botellas y carbón; datáfono y software de facturación '
         'Veri*factu'),
    ]),
    ('F4 - Personal', 'FASE 4: PERSONAL (semanas 6-10)', [
        ('Segundo parrillero y auxiliares como fijos discontinuos o a través de una ETT', 'Gestoría',
         'Antes del primer evento',
         'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) con llamamiento por evento. Nunca '
         'con facturas de autónomo: con tu horario y tu dirección es falso autónomo (art. 1.1 ET)'),
        ('Alta en la Seguridad Social antes de cada llamamiento', 'Gestoría', 'Antes de cada evento',
         'El alta va antes de empezar a trabajar, también para un solo día'),
        ('Formación en higiene alimentaria acreditada por la empresa', 'Titular', 'Antes del primer evento',
         'El antiguo título de manipulador de alimentos ya no se exige: la empresa forma y acredita a su personal '
         '(Reglamento (CE) 852/2004, anexo II, cap. XII). Con un módulo de carne cruda, temperaturas y alérgenos'),
        ('Formación en alérgenos y en el plan APPCC', 'Titular', 'Antes del primer evento',
         'Cada persona que sirve tiene que saber qué lleva cada plato y cómo evitar el contacto cruzado con pinzas, '
         'tablas y la parrilla compartida; rejilla aparte para lo sin gluten o vegano'),
        ('Prevención de riesgos laborales: quemaduras, humo, calor y cargas', 'Servicio de prevención',
         'Antes del primer evento',
         'Evaluación de riesgos y plan de prevención (Ley 31/1995), EPI de calor, agua y pausas en los eventos de '
         'verano'),
        ('Registro de jornada', 'Titular', 'Desde el primer día',
         'Obligatorio para todo el personal, también los fijos discontinuos (art. 34.9 ET)'),
        ('Información de protección de datos al trabajador', 'Gestoría', 'Al contratar',
         'Cláusula informativa en el contrato y en el registro de jornada'),
        ('Segundo parrillero para los eventos grandes', 'Titular', 'Antes de la temporada',
         'Un parrillero por cada 60-80 invitados en buffet o por cada 40-50 con cortes en mesa, y un ayudante desde '
         '40 invitados (tabla de escalado del manual técnico): tenlo localizado en tu bolsa de fijos discontinuos'),
        ('Guion del show de fuego', 'Titular', 'Antes del primer evento',
         'Qué cuentas del corte, de la brasa y del punto mientras cortas en directo. Flambeados sólo con el extintor '
         'a mano, lejos de los invitados y nunca con alerta de incendios'),
        ('Fichas de trabajo por formato de evento', 'Titular', 'Antes del primer evento',
         'Gramos de carne cruda, tandas, carbón y tiempos de cada formato (asado completo, plato principal, '
         'brunch), sacados de la tabla de escalado del manual técnico'),
    ]),
    ('F5 - Marca y captación', 'FASE 5: MARCA Y CAPTACIÓN (meses 1-3)', [
        ('Nombre, logo e identidad visual', 'Titular', 'Mes 1',
         'Comprueba que el nombre está libre en la OEPM y como dominio'),
        ('Dominio y correos profesionales', 'Titular', 'Mes 1', 'Presupuestos, reservas y empresas'),
        ('Web con formulario de presupuesto y SEO técnico', 'Titular', 'Mes 1-2',
         'Galería, experiencias, zona de servicio y formulario; datos estructurados y Search Console. «Barbacoa a '
         'domicilio» suma unas 320 búsquedas al mes en España y «parrillero para eventos», unas 70 (DataForSEO, '
         'octubre de 2026)'),
        ('Fotos y vídeo profesionales de la brasa y del corte', 'Titular', 'Mes 1-2',
         'Es lo que miran los novios y los planners antes de pedir presupuesto'),
        ('Perfil de empresa en Google y primeras reseñas', 'Titular', 'Mes 1-3',
         'Categorías de servicio de comidas para eventos y la zona que cubres; pide la reseña después de cada '
         'evento'),
        ('Instagram, TikTok y Pinterest con cocciones reales', 'Titular', 'Mes 1+',
         'El cordero a la cruz y el corte en mesa funcionan solos en vídeo'),
        ('LinkedIn para empresas y agencias', 'Titular', 'Mes 2', 'Comidas de empresa, team building y Navidad'),
        ('WhatsApp Business con plantillas', 'Titular', 'Mes 1',
         'Bienvenida, presupuesto, confirmación y recordatorio de alérgenos'),
        ('Alta en directorios de bodas', 'Titular', 'Mes 2', 'Bodas.net y Zankyou, con fotos y precios orientativos'),
        ('Alta en directorios de eventos para empresas y en Hosply', 'Titular', 'Mes 2',
         'Visibilidad ante agencias, planners y empresas'),
        ('Wedding planners: lista y primer contacto', 'Titular', 'Mes 1-3',
         'Lista de los planners de tu zona y un correo personal a cada uno (sección 5 del plan de negocio)'),
        ('Degustación para planners y fincas', 'Titular', 'Mes 2-4',
         'Una parrilla en directo para los que más bodas mueven: es tu mejor dossier'),
        ('Agencias, empresas y hoteles de la zona', 'Titular', 'Mes 2-4',
         'Comidas de verano, team building, show cooking y Navidad en terrazas, fincas y hoteles'),
        ('Ayuntamientos y comisiones de fiestas: encargo por contrato menor y factura por FACe', 'Titular',
         'Mes 2-6',
         'Un ayuntamiento compra por contrato menor (servicios de menos de 15.000 €, Ley 9/2017 art. 118) y paga a '
         '30 días desde la conformidad (art. 198.4), sin anticipo. Si eres SL, la factura va en electrónico a su punto '
         'general de entrada (FACe en la mayoría; Ley 25/2013, art. 4), salvo que exima las de hasta 5.000 €. Si lo '
         'que te adjudican es la barra o un puesto con canon, vendes tú al público: venta no sedentaria (Ley 7/1996)'),
        ('Dossiers para bodas, empresas y fiestas', 'Titular', 'Mes 1-2',
         'Con las 10 experiencias y la carta de 12 cortes del kit, y el precio por invitado de cada tipo de evento'),
        ('Publicidad, referidos y degustación abierta', 'Titular', 'Mes 2+',
         'Google Ads local en temporada, un detalle por recomendación y una degustación abierta al año para '
         'planners'),
    ]),
    ('F6 - Primer evento', 'FASE 6: PRIMER EVENTO Y 90 DÍAS', [
        ('Briefing del cliente', 'Titular', '30 días antes',
         'Invitados, formato (asado completo, plato principal o brunch), experiencia, alergias, horario, lugar, '
         'agua, luz y acceso para la furgoneta y el remolque'),
        ('Visita técnica del lugar', 'Titular', '21 días antes',
         'Si son más de 80 invitados o es un lugar nuevo: punto de fuego, viento y humo, sombra, suelo, agua, '
         'distancia a carpas y si está en terreno forestal o en su franja'),
        ('Presupuesto firmado y señal del 30 %', 'Titular', 'Al reservar la fecha',
         'Sin señal no se bloquea la fecha. Particulares: 30 % al firmar, 40 % siete días antes y 30 % en las 48 '
         'horas siguientes; empresas: 30 % al confirmar y 70 % a 30 días de la factura. Factura cada pago, también '
         'la señal (art. 75.Dos de la Ley 37/1992). En efectivo, sólo pagos por debajo de 1.000 € (Ley 7/2012, '
         'art. 7). Los ayuntamientos no adelantan: pagan a 30 días desde la conformidad'),
        ('Contrato firmado con cancelación, fuerza mayor y plan B', 'Titular', 'Al reservar la fecha',
         'Modelos del kit: tramos de cancelación, sin desistimiento en un servicio con fecha (art. 103.l TRLGDCU) y '
         'plan B de gas o cambio de fecha si una alerta de incendios prohíbe la brasa'),
        ('Menú y alérgenos confirmados por escrito', 'Titular', '7 días antes',
         'Invitados definitivos, cortes, puntos y qué invitados tienen alergias o intolerancias'),
        ('Plan B de lluvia, viento o alerta de incendios', 'Titular', '7 días antes',
         'Carpa y cortavientos; el equipo de gas cargado si la previsión de riesgo de incendio es alta'),
        ('Pedido de carne, carbón y verdura', 'Titular', '5-7 días antes',
         'Confirma la entrega 48-72 horas antes y recibe la carne con sonda (7 °C o menos; despojos, 3 °C)'),
        ('Marinados, salmueras y porcionado en la cocina de apoyo', 'Titular / Ayudante', 'Día anterior',
         'En la cocina autorizada, nunca en casa (art. 13.5.b del RD 1021/2022), y en cámara hasta la carga'),
        ('Carga de la furgoneta con la lista del manual', 'Ayudante', 'Día del evento',
         'Parrillas, cruces, carbón, botellas en pie y sujetas, extintores, armario refrigerado, sondas y fichas de '
         'alérgenos'),
        ('Salida con margen, montaje y encendido', 'Titular', 'Día del evento',
         'Una hora de margen sobre el trayecto y entre 45 y 60 minutos hasta tener la brasa lista'),
        ('Cocción, show de fuego y servicio', 'Titular', 'Día del evento',
         'Sonda en el centro (70 °C la carne, 74 °C las aves; poco hecho sólo en piezas enteras de vacuno o cordero '
         'y a petición), registro en el APPCC y lo caliente a 63 °C o más. Aparta la comida testigo de cada plato '
         '(art. 30.8 del RD 1086/2020)'),
        ('Brasas apagadas, recogida y fotos del espacio', 'Ayudante', 'Final del evento',
         'Brasas y cenizas apagadas con agua en el contenedor metálico; fotos del espacio antes y después: te '
         'protegen ante una reclamación de daños'),
        ('Cobro y factura', 'Titular', 'D+1 / D+2',
         'Particulares: el 30 % final en las 48 horas siguientes. Empresas: a 30 días de la factura. Ayuntamientos: '
         'factura electrónica en su punto general de entrada (FACe en la mayoría, salvo que exima las de hasta '
         '5.000 €) y cobro a 30 días desde la conformidad'),
        ('Reseña, fotos y agradecimiento al planner', 'Titular', 'D+2',
         'Pide la reseña y el permiso para publicar las fotos; si vino por un planner, agradéceselo'),
        ('CRM, costes reales frente al presupuesto y cierre trimestral', 'Titular', 'D+7 y cada trimestre',
         'Compara la carne y el carbón reales de cada evento con la calculadora y ajusta precios'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 16, 14, 10, 16, 15], [len(t) for _, _, t in FASES]
assert all(len(n) <= 31 for n, _c, _t in FASES), [n for n, _c, _t in FASES]
