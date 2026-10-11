#!/usr/bin/env python3
"""datos_checklist.py — las 83 tareas del checklist de apertura del Paellero ES 2.2 (SPEC D10: 12/16/14/10/16/15).
Origen: los 104 hitos de la 1.2 (`dl/plan-negocio-paellero-eventos/checklist-apertura-paellero-eventos.xlsx`, filas
6-119), las tareas del Catering ES 2.2 que valen para un paellero (`catering-es-2_0/datos_checklist.py`) y el marco
legal de los dos research (`catering-es-2_0/F1-research-es.md` §1 y `F1-research-paellero.md` §1):
  · RD 1021/2022, art. 13.5.b (no se prepara en casa para eventos) y su DF 1.ª (registro autonómico previa
    declaración responsable; RGSEAA sólo si se suministra a otros establecimientos);
  · RD 919/2006, art. 2.1.h e ITC-ICG 08 §5.2 (botella < 15 kg con un aparato: no es instalación) e ITC-ICG 06 §2.2
    (botellas de 35 kg o baterías: empresa instaladora); ADR 1.1.3.6 (≤ 333 kg de GLP por vehículo, 🟡);
  · Ley 43/2003, art. 44.3 (las comunidades autónomas regulan el fuego en montes y zonas colindantes);
  · Ley 9/2017, arts. 118 y 198.4 (contrato menor y pago a 30 días); Ley 25/2013, art. 4 (factura electrónica);
    Ley 7/1996, arts. 53-54 (venta no sedentaria); TRLGDCU art. 103.l; RDLeg 1175/1990, epígrafe 677.9;
  · ET arts. 1.1, 16 y 34.9; Reglamento (CE) 852/2004, anexo II, cap. XII; Reglamento (UE) 1169/2011.
Cada tarea: (trámite / acción, responsable, plazo, notas). Sesión Claude Code, 11-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — PAELLERO / PAELLA PARA EVENTOS'

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
         'Separadas de las personales: por ellas pasan los anticipos, las facturas de empresas y ayuntamientos y '
         'los proveedores'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Semanas 2-4',
         'Nóminas de los fijos discontinuos cada mes con llamamientos. El software de facturación tiene que cumplir '
         'el RD 1007/2023 (Veri*factu): confirma la fecha que te aplica antes de contratarlo'),
        ('IVA trimestral (modelo 303) al 10 %', 'Gestoría', 'Cada trimestre',
         'Servicio de paella en el evento al 10 %, alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992). '
         'Carpas o mobiliario facturados aparte, al 21 %'),
        ('Pagos fraccionados y retenciones (modelos 202 o 130, y 111)', 'Gestoría', 'Cada trimestre',
         'SL: modelo 202; autónomo: modelo 130. Las retenciones de las nóminas van en el 111'),
        ('Declaraciones anuales: 390 y 347', 'Gestoría', 'Enero-febrero',
         '390: resumen anual del IVA. 347: clientes o proveedores con más de 3.005,06 € en el año (ayuntamientos '
         'y fincas habituales suelen pasarlo)'),
        ('RGPD: registro de actividades de tratamiento y cláusulas en presupuestos y contratos', 'Titular',
         'Antes del primer presupuesto',
         'Art. 30 del RGPD y LOPDGDD. Tratas datos de clientes, de invitados (las alergias son datos de salud) y '
         'del personal'),
        ('Web: aviso legal, privacidad, cookies (LSSI) y condiciones de contratación', 'Titular',
         'Antes de publicar la web',
         'Precio final con IVA para particulares. En un servicio de comida con fecha no hay derecho de '
         'desistimiento de 14 días (art. 103.l del TRLGDCU): tu política de anticipo (30 %) y cancelación tiene '
         'que estar escrita y firmada, como en los contratos del kit'),
    ]),
    ('F2 - Sanidad, fuego y gas', 'FASE 2: COCINA DE APOYO, SANIDAD, FUEGO, GAS Y PERMISOS (semanas 3-8)', [
        ('Contrato de uso de una cocina de apoyo compartida y autorizada', 'Titular', 'Semanas 3-6',
         'La paella se cocina en el evento, pero los caldos, sofritos y la preparación del marisco no se pueden '
         'hacer en casa: lo prohíbe el art. 13.5.b del RD 1021/2022. Pide en el contrato horas, cámara, almacén de '
         'paelleras y quemadores, DDD y residuos'),
        ('Declaración responsable e inscripción en el registro sanitario autonómico', 'Titular',
         'Antes del primer evento',
         'Un servicio que vende al consumidor final se inscribe en el registro de su comunidad autónoma previa '
         'declaración responsable (RD 1021/2022, que reescribe el art. 2 del RD 191/2011)'),
        ('RGSEAA: sólo si suministras a otros establecimientos', 'Titular', 'Solo si aplica',
         'El Registro General Sanitario (RGSEAA) sólo hace falta si suministras a otros establecimientos (paellas o '
         'caldos para restaurantes) de forma no marginal; para servir al cliente final, no (art. 2 del RD 191/2011)'),
        ('Plan APPCC itinerante: prerrequisitos y puntos de control', 'Titular', 'Antes del primer evento',
         'Puntos críticos: frío del marisco y la carne en el transporte, cocción y servicio a 63 °C o más (art. 30 '
         'del RD 1086/2020) y alioli con huevo pasteurizado o sin huevo. Nunca arroz tibio a temperatura ambiente. '
         'Guarda una comida testigo de cada arroz (100 g, identificada y fechada, a 4 °C o menos o congelada, 7 '
         'días): obligatoria en todos tus eventos, porque son tu actividad principal (art. 30.8.d del RD '
         '1086/2020), y en cualquier encargo de más de 40 personas (30.8.e); conservación según el 30.10'),
        ('Fichas de alérgenos de cada arroz y de las salsas', 'Titular', 'Antes del primer evento',
         'Reglamento (UE) 1169/2011 y RD 126/2015: crustáceos, moluscos, pescado, apio de los caldos, sulfitos, '
         'huevo del alioli, gluten de la fideuá. La tabla del manual técnico es tu punto de partida'),
        ('Agua: análisis sólo si llevas depósito propio', 'Titular', 'Solo si aplica',
         'Si usas el agua de red del recinto no hace falta. Con depósito propio, agua apta para consumo y registro '
         'de su limpieza en el APPCC'),
        ('Seguro de responsabilidad civil con incendio, explosión e intoxicación alimentaria', 'Aseguradora',
         'Antes del primer evento',
         'Recomendado: al menos 600.000 €, con daños al recinto (césped, pavimento) y RC de producto. Es lo que '
         'suelen pedir fincas, empresas y ayuntamientos: adjunta el certificado a los presupuestos'),
        ('Seguro de la furgoneta para uso comercial', 'Aseguradora', 'Al comprarla',
         'Declara el uso profesional y la carga de botellas de gas'),
        ('Seguro de equipos y cláusula de fuerza mayor en los contratos', 'Titular / Aseguradora',
         'Antes del primer evento',
         'La cancelación por una prohibición de fuego no se asegura: va en la cláusula de fuerza mayor del '
         'contrato, con un plan B pactado (cocina del recinto o equipos sin llama)'),
        ('Gas: una botella de menos de 15 kg por quemador, con regulador y tubo flexible en fecha', 'Titular',
         'Antes del primer evento',
         'Una botella de menos de 15 kg conectada a un solo aparato móvil no es una instalación y la conectas tú '
         '(RD 919/2006, art. 2.1.h; ITC-ICG 08 §5.2). Aparatos con marcado CE (Reglamento (UE) 2016/426); revisa la '
         'fecha del tubo y prueba fugas con agua jabonosa'),
        ('Botellas de 35 kg o varias conectadas: montaje por una empresa instaladora de gas', 'Instaladora',
         'Solo si aplica',
         'Una instalación de envases de más de 15 kg o en batería la ejecuta una empresa instaladora (ITC-ICG 06 '
         '§2.2). Confirma con Industria de tu comunidad cómo lo aplica a un montaje de un día'),
        ('Transporte de las botellas en la furgoneta', 'Titular', 'Antes del primer evento',
         'Hasta 333 kg de gas por vehículo se viaja en el régimen de exención del ADR (1.1.3.6): botellas en pie y '
         'sujetas, ventilación, válvulas cerradas y un extintor de 2 kg en el vehículo (fuente secundaria: '
         'confírmalo con tu aseguradora)'),
        ('Extintores, manta ignífuga y cubo de arena en cada evento', 'Titular', 'Antes del primer evento',
         'Un extintor de polvo ABC de 6 kg por zona de fuego, revisado por una empresa mantenedora (RD 513/2017). '
         'Es lo que suelen exigir ayuntamientos y fincas'),
        ('Fuego y leña: época de peligro y franja forestal de cada comunidad', 'Titular', 'Por evento',
         'Cada comunidad regula el fuego en montes y zonas colindantes (Ley 43/2003, art. 44.3): franja de 400-500 m '
         'y época de peligro en verano. En alerta máxima caen las autorizaciones y algunas prohíben también el gas. '
         'Consulta el anexo autonómico del plan de negocio'),
        ('Autorización municipal o del recinto para cocinar al aire libre', 'Titular', '30-60 días antes',
         'Vía pública: autorización del ayuntamiento (ordenanza o bando). Finca privada: permiso del propietario; si '
         'está en terreno forestal o en su franja, manda la norma autonómica. Vender raciones al público por tu '
         'cuenta es venta no sedentaria con autorización municipal (Ley 7/1996, arts. 53-54)'),
        ('Hojas de reclamaciones, residuos y aceite usado', 'Titular', 'Antes del primer evento',
         'Hojas de reclamaciones según la norma de tu comunidad. Aceite usado a un gestor autorizado, salvo que lo '
         'recoja la cocina de apoyo'),
    ]),
    ('F3 - Equipo y proveedores', 'FASE 3: EQUIPAMIENTO Y PROVEEDORES (semanas 4-8)', [
        ('Paelleras por diámetro según la tabla de escalado del manual', 'Titular', 'Mes 1',
         'De 60 a 120 cm para bodas, empresas y fiestas privadas y una de 150 cm para fiestas populares. Raciones '
         'por paellera: tabla 1 del manual técnico; el catálogo trae los modelos'),
        ('Quemadores de anillos con sus patas', 'Titular', 'Mes 1',
         'Un quemador por paellera que vayas a cocinar a la vez, del tamaño que pide la tabla del manual'),
        ('Trípodes y leña, sólo donde el fuego esté permitido', 'Titular', 'Mes 1',
         'Leña seca de naranjo, olivo o sarmiento; cubo de arena y extintor al lado'),
        ('Botellas de gas y reserva', 'Titular', 'Mes 1',
         'Propano en exterior (el butano vaporiza mal con frío). Una botella de reserva por evento'),
        ('Cuchillería, tablas de colores, paletas y cucharas', 'Titular', 'Mes 1',
         'Tablas de colores para separar carne, pescado y verdura (APPCC)'),
        ('Vajilla, cubertería y cuencos de alioli para tu dotación', 'Titular', 'Mes 1-2',
         'Para los invitados de un evento medio; en bodas grandes y fiestas populares, menaje de alquiler o '
         'desechable'),
        ('Neveras, isotermos, acumuladores y sondas', 'Titular', 'Mes 1',
         'Cadena de frío del marisco y la carne hasta el evento y sondas para el registro del APPCC'),
        ('Básculas de cocina y de precisión', 'Titular', 'Mes 1',
         'Para escandallar cada arroz con la calculadora del kit: 100 g de arroz por ración de evento'),
        ('Cajas de transporte, carpa, mesa de show cooking y protector de suelo', 'Titular', 'Mes 1',
         'Zona de cocción bajo carpa y protección del césped o del pavimento del recinto'),
        ('EPI de calor y uniformes', 'Titular', 'Mes 1', 'Delantal de cuero o algodón grueso y guantes térmicos'),
        ('Arroz con denominación de origen a precio trimestral', 'Titular', 'Mes 1',
         'Bomba o variedades de la DO Arroz de Valencia o de Calasparra; pacta precio por trimestre'),
        ('Carne, marisco y verdura con trazabilidad', 'Titular', 'Mes 1',
         'Mayorista de carne, pescadero con lote y fecha, y verdura de temporada (garrofó y ferraura) de '
         'cooperativa'),
        ('Caldos, azafrán y pimentón', 'Titular', 'Mes 1',
         'Caldos propios en la cocina de apoyo o comprados con su ficha de alérgenos; azafrán y pimentón con DO'),
        ('Furgoneta, TPV y software de presupuestos', 'Titular', 'Mes 1-2',
         'Furgoneta isoterma con ATP y anclajes de botellas; datáfono y software de facturación Veri*factu'),
    ]),
    ('F4 - Personal', 'FASE 4: PERSONAL (semanas 6-10)', [
        ('Ayudantes como fijos discontinuos o a través de una ETT', 'Gestoría', 'Antes del primer evento',
         'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) con llamamiento por evento. Nunca '
         'con facturas de autónomo: con tu horario y tu dirección es falso autónomo (art. 1.1 ET)'),
        ('Alta en la Seguridad Social antes de cada llamamiento', 'Gestoría', 'Antes de cada evento',
         'El alta va antes de empezar a trabajar, también para un solo día'),
        ('Formación en higiene alimentaria acreditada por la empresa', 'Titular', 'Antes del primer evento',
         'El antiguo título de manipulador de alimentos ya no se exige: la empresa forma y acredita a su personal '
         '(Reglamento (CE) 852/2004, anexo II, cap. XII). Con un módulo de alérgenos y de marisco'),
        ('Formación en alérgenos y en el plan APPCC', 'Titular', 'Antes del primer evento',
         'Cada persona que sirve tiene que saber qué lleva cada arroz y cómo evitar el contacto cruzado con '
         'paletas y paelleras compartidas'),
        ('Prevención de riesgos laborales: quemaduras, gas, calor y cargas', 'Servicio de prevención',
         'Antes del primer evento',
         'Evaluación de riesgos y plan de prevención (Ley 31/1995), EPI de calor y pausas en los eventos de verano'),
        ('Registro de jornada', 'Titular', 'Desde el primer día',
         'Obligatorio para todo el personal, también los fijos discontinuos (art. 34.9 ET)'),
        ('Información de protección de datos al trabajador', 'Gestoría', 'Al contratar',
         'Cláusula informativa en el contrato y en el registro de jornada'),
        ('Segundo paellero para los eventos grandes', 'Titular', 'Antes de la temporada',
         'El manual técnico pone el techo de un paellero en tres paelleras y pide un segundo paellero a partir de '
         'unos 150 invitados: tenlo localizado en tu bolsa de fijos discontinuos'),
        ('Guion del show cooking', 'Titular', 'Antes del primer evento',
         'Qué cuentas del sofrito, del caldo y del socarrat mientras cocinas: lo que convierte la paella en una '
         'experiencia y justifica el suplemento'),
        ('Fichas de trabajo por diámetro de paellera', 'Titular', 'Antes del primer evento',
         'Arroz, caldo, tiempos y quemador de cada paellera, sacados de las tablas del manual técnico'),
    ]),
    ('F5 - Marca y captación', 'FASE 5: MARCA Y CAPTACIÓN (meses 1-3)', [
        ('Nombre, logo e identidad visual', 'Titular', 'Mes 1',
         'Comprueba que el nombre está libre en la OEPM y como dominio'),
        ('Dominio y correos profesionales', 'Titular', 'Mes 1', 'Presupuestos, reservas y empresas'),
        ('Web con formulario de presupuesto y SEO técnico', 'Titular', 'Mes 1-2',
         'Galería, tipos de evento, zona de servicio y formulario; datos estructurados y Search Console. «Paellas a '
         'domicilio» suma unas 1.900 búsquedas al mes en España'),
        ('Fotos y vídeo profesionales del show cooking', 'Titular', 'Mes 1-2',
         'Es lo que miran los novios y los planners antes de pedir presupuesto'),
        ('Perfil de empresa en Google y primeras reseñas', 'Titular', 'Mes 1-3',
         'Categorías de servicio de comidas para eventos y la zona que cubres; pide la reseña después de cada '
         'evento'),
        ('Instagram, TikTok y Pinterest con cocciones reales', 'Titular', 'Mes 1+',
         'El socarrat y la paella de 150 cm funcionan solos en vídeo'),
        ('LinkedIn para empresas y agencias', 'Titular', 'Mes 2', 'Comidas de empresa, team building y Navidad'),
        ('WhatsApp Business con plantillas', 'Titular', 'Mes 1',
         'Bienvenida, presupuesto, confirmación y recordatorio de alérgenos'),
        ('Alta en directorios de bodas', 'Titular', 'Mes 2', 'Bodas.net y Zankyou, con fotos y precios orientativos'),
        ('Alta en directorios de eventos para empresas y en Hosply', 'Titular', 'Mes 2',
         'Visibilidad ante agencias, planners y empresas'),
        ('Wedding planners: lista y primer contacto', 'Titular', 'Mes 1-3',
         'Lista de los planners de tu zona y un correo personal a cada uno (sección 5 del plan de negocio)'),
        ('Degustación para planners y fincas', 'Titular', 'Mes 2-4',
         'Una paella en directo para los que más bodas mueven: es tu mejor dossier'),
        ('Agencias, empresas y hoteles de la zona', 'Titular', 'Mes 2-4',
         'Comidas de verano, Navidad y show cooking en terrazas y hoteles'),
        ('Ayuntamientos y comisiones de fiestas: contrato menor y factura por FACe', 'Titular', 'Mes 2-6',
         'Un ayuntamiento compra por contrato menor (servicios de menos de 15.000 €, Ley 9/2017 art. 118) y paga a '
         '30 días desde la conformidad (art. 198.4), sin anticipo. Si eres SL, la factura va en electrónico a su punto '
         'general de entrada (FACe en la mayoría; Ley 25/2013, art. 4), salvo que exima las de hasta 5.000 €. Alta en '
         'la Plataforma de Contratación para ver las licitaciones'),
        ('Dossiers para bodas, empresas y ayuntamientos', 'Titular', 'Mes 1-2',
         'Con las 10 experiencias y la carta de 12 arroces del kit, y los precios por ración de cada tipo de evento'),
        ('Publicidad, referidos y jornada de puertas abiertas', 'Titular', 'Mes 2+',
         'Google Ads local en temporada, un detalle por recomendación y una paella abierta al año para planners'),
    ]),
    ('F6 - Primer evento', 'FASE 6: PRIMER EVENTO Y 90 DÍAS', [
        ('Briefing del cliente', 'Titular', '30 días antes',
         'Invitados, arroces, alergias, horario, lugar, agua, luz y acceso para la furgoneta'),
        ('Visita técnica del lugar', 'Titular', '21 días antes',
         'Si son más de 80 invitados o es un lugar nuevo: punto de fuego, viento, sombra, suelo, agua y si está en '
         'terreno forestal o en su franja'),
        ('Presupuesto firmado y anticipo del 30 %', 'Titular', 'Al reservar la fecha',
         'Sin anticipo no se bloquea la fecha. Particulares: el 70 % restante el día del evento; empresas: a 30 días '
         'de la factura. En efectivo, sólo pagos por debajo de 1.000 € (Ley 7/2012, art. 7). Los ayuntamientos no '
         'adelantan: pagan a 30 días desde la conformidad'),
        ('Contrato firmado con cancelación, fuerza mayor y plan B', 'Titular', 'Al reservar la fecha',
         'Modelos del kit: tramos de cancelación, sin desistimiento en un servicio con fecha (art. 103.l TRLGDCU) y '
         'plan B si una alerta de incendios prohíbe el fuego o el gas'),
        ('Menú y alérgenos confirmados por escrito', 'Titular', '7 días antes',
         'Cuántas raciones de cada arroz y qué invitados tienen alergias o intolerancias'),
        ('Plan B de lluvia, viento o prohibición de fuego', 'Titular', '7 días antes',
         'Carpa y cortavientos; cocina del recinto o equipos sin llama si la alerta lo exige'),
        ('Pedidos de arroz, carne y verdura; marisco el día antes', 'Titular', '5-7 días antes',
         'Confirma la entrega 48-72 horas antes; el marisco fresco, el día anterior y en frío'),
        ('Caldos y mise en place en la cocina de apoyo', 'Titular / Ayudante', 'Día anterior',
         'Caldos, sofritos y marisco limpio en la cocina autorizada, nunca en casa (art. 13.5.b del RD 1021/2022)'),
        ('Carga de la furgoneta con la lista del manual', 'Ayudante', 'Día del evento',
         'Paelleras, quemadores, botellas en pie y sujetas, extintores, neveras y fichas de alérgenos'),
        ('Salida con margen, montaje y encendido', 'Titular', 'Día del evento',
         'Una hora de margen sobre el trayecto y 30-45 minutos para montar y encender'),
        ('Cocción, show cooking y servicio', 'Titular', 'Día del evento',
         'Registro de temperaturas en el APPCC y servicio a 63 °C o más; nada de arroz tibio a temperatura ambiente. '
         'Aparta la comida testigo de cada arroz (art. 30.8 del RD 1086/2020)'),
        ('Recogida, limpieza y fotos del espacio', 'Ayudante', 'Final del evento',
         'Fotos del espacio antes y después: te protegen ante una reclamación de daños'),
        ('Cobro y factura', 'Titular', 'D+1 / D+2',
         'Particulares: el 70 % el día del evento. Empresas: a 30 días de la factura. Ayuntamientos: factura '
         'electrónica en su punto general de entrada (FACe en la mayoría, salvo que exima las de hasta 5.000 €) y '
         'cobro a 30 días desde la conformidad'),
        ('Reseña, fotos y agradecimiento al planner', 'Titular', 'D+2',
         'Pide la reseña y el permiso para publicar las fotos; si vino por un planner, agradéceselo'),
        ('CRM, costes reales frente al presupuesto y cierre trimestral', 'Titular', 'D+7 y cada trimestre',
         'Compara el coste real de cada evento con la calculadora y ajusta precios'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 16, 14, 10, 16, 15], [len(t) for _, _, t in FASES]
