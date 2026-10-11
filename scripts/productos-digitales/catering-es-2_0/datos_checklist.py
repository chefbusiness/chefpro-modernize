#!/usr/bin/env python3
"""datos_checklist.py — las 82 tareas del checklist de apertura del Catering ES 2.0 (SPEC D7: 12/15/14/10/16/15).

Origen: las 108 tareas del 1.x (`business-plans-en-4/fuente_es_cat.json`), las del Food Truck ES v2.2 que valen para
un catering y el marco legal leído en el BOE el 11-oct-2026 (`F1-research-es.md` §1 y la verificación de F2):
  · RD 1021/2022, art. 13.5.b (no se cocina en casa para eventos) y su DF 1.ª, que reescribe el art. 2 del RD 191/2011
    (registro autonómico previa declaración responsable; RGSEAA sólo si se suministra a otros establecimientos);
  · RDLeg 1175/1990, epígrafe 677.9 (su nota incluye el «catering»);
  · TRLGDCU art. 103.l (sin desistimiento en servicios de comida con fecha);
  · RD 237/2000 (ATP en transporte nacional de perecederos); ET arts. 1.1, 15.2, 16 y 34.9; Ley 37/1992 art. 91.
Cada tarea: (trámite / acción, responsable, plazo, notas). Sesión Claude Code, 11-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — CATERING TEMÁTICO DE EVENTOS'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (semanas 1-4)', [
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Semana 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades). Como autónomo tributas por IRPF: '
         'compara las dos opciones con tu gestoría con las cifras del plan'),
        ('Constituir la SL o darte de alta como autónomo', 'Notaría / Gestoría', 'Semanas 1-2',
         'La SL se puede constituir con 1 € de capital (Ley 18/2022, «Crea y Crece»)'),
        ('Alta censal (modelo 036/037) en el epígrafe 677.9 del IAE', 'Gestoría', 'Semana 2',
         'La nota del epígrafe 677.9 («otros servicios de alimentación propios de la restauración», RDLeg '
         '1175/1990) incluye los productos elaborados para «catering» o colectividades. Exento de cuota con una '
         'cifra de negocio inferior a 1 millón de euros'),
        ('Alta en la Seguridad Social (administrador o autónomo)', 'Gestoría', 'Semana 2',
         'Consulta la cuota del ejercicio en curso y si te aplica la cuota reducida de inicio de actividad'),
        ('Certificado digital', 'Titular', 'Semana 1',
         'Imprescindible para Hacienda, la Seguridad Social y la declaración responsable sanitaria'),
        ('Cuenta bancaria del negocio', 'Titular', 'Semana 2',
         'Separada de la personal: por ella pasan los anticipos, las facturas de empresa y los proveedores'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Semanas 2-4',
         'Nóminas de fijos discontinuos cada mes con llamamientos. El software de facturación tiene que cumplir el '
         'RD 1007/2023 (Veri*factu): confirma la fecha que te aplica antes de contratarlo'),
        ('IVA trimestral (modelo 303) al 10 %', 'Gestoría', 'Cada trimestre',
         'Catering con servicio al 10 %, alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992). Mobiliario, '
         'carpas o decoración facturados aparte, al 21 %'),
        ('Pagos fraccionados y retenciones (modelos 202 o 130, y 111)', 'Gestoría', 'Cada trimestre',
         'SL: modelo 202; autónomo: modelo 130. Las retenciones de las nóminas van en el 111'),
        ('Declaraciones anuales: 390, 347 y 349', 'Gestoría', 'Enero-febrero',
         '390: resumen anual del IVA. 347: clientes o proveedores con más de 3.005,06 € en el año. 349: sólo si '
         'facturas a empresas de otros países de la UE'),
        ('RGPD: registro de actividades de tratamiento y cláusulas en presupuestos y contratos', 'Titular',
         'Antes del primer presupuesto',
         'Art. 30 del RGPD y LOPDGDD. Tratas datos de clientes, de invitados (las alergias son datos de salud) y '
         'del personal'),
        ('Web: aviso legal, privacidad, cookies (LSSI) y condiciones de contratación', 'Titular',
         'Antes de publicar la web',
         'En un servicio de comida para una fecha concreta no hay derecho de desistimiento de 14 días (art. 103.l '
         'del TRLGDCU): por eso tu política de anticipo y cancelación tiene que estar escrita y firmada'),
    ]),
    ('F2 - Cocina y permisos', 'FASE 2: COCINA CENTRAL, SANIDAD, SEGUROS Y PERMISOS (semanas 3-8)', [
        ('Contrato de uso de una cocina central o compartida autorizada', 'Titular', 'Semanas 3-6',
         'Para eventos no se puede cocinar en casa: lo prohíbe el art. 13.5.b del RD 1021/2022. Pide en el '
         'contrato horas, cámara, almacén, plaza de furgoneta, DDD y residuos'),
        ('Declaración responsable e inscripción en el registro sanitario autonómico', 'Titular',
         'Antes del primer evento',
         'Un catering que sirve al consumidor final se inscribe en el registro de su comunidad autónoma previa '
         'declaración responsable (RD 1021/2022, que reescribe el art. 2 del RD 191/2011). El RGSEAA sólo hace '
         'falta si suministras a otros establecimientos de forma no marginal'),
        ('Plan APPCC del catering: prerrequisitos y puntos de control', 'Jefe/a de cocina', 'Antes del primer evento',
         'Cadena de frío y de caliente en producción, transporte y estación: 63 °C o más en caliente, 4-8 °C o '
         'menos en frío (art. 30 del RD 1086/2020). Registros de temperatura en cada evento'),
        ('Fichas de alérgenos por menú y por estación', 'Jefe/a de cocina', 'Antes del primer evento',
         'Reglamento (UE) 1169/2011 y RD 126/2015: información de los 14 alérgenos en alimentos sin envasar, '
         'también en las estaciones en directo'),
        ('Certificado ATP de la furgoneta frigorífica e inspección periódica', 'Titular', 'Antes del primer evento',
         'El transporte de perecederos en furgoneta isoterma o frigorífica exige el certificado ATP también en '
         'transporte nacional (RD 237/2000)'),
        ('Seguro de responsabilidad civil de explotación y de producto con intoxicación alimentaria', 'Aseguradora',
         'Antes del primer evento',
         'Recomendado: al menos 600.000 €; es lo que suelen pedir las fincas, los hoteles y las empresas grandes. '
         'Pide el certificado para adjuntarlo a los presupuestos'),
        ('Seguro de la furgoneta para uso comercial', 'Aseguradora', 'Al comprarla',
         'Con la carga y el equipo transportado'),
        ('Seguro de equipos y, si lo quieres, de cancelación por fuerza mayor', 'Aseguradora', 'Semanas 6-8',
         'Las estaciones, el menaje y el mobiliario salen del almacén en cada evento'),
        ('Autorización municipal para eventos en vía pública o espacios municipales', 'Titular',
         '30-60 días antes del evento', 'La pide el organizador o tú, según el contrato: déjalo escrito'),
        ('Ferias y festivales: autorización de venta en cada recinto', 'Titular', 'Antes de cada feria',
         'Sólo si vendes directamente al público en ferias o festivales gastronómicos'),
        ('Fuego y brasas al aire libre: permiso municipal y extintores', 'Titular', 'Antes de cada evento con fuego',
         'Parrillas, horno de leña o asado a la cruz: consulta la ordenanza del municipio y el espacio'),
        ('Comprobar la instalación de cada espacio: electricidad, agua, gas y licencia para servir alcohol',
         'Coordinador/a de eventos', 'En la visita técnica',
         'La bebida se sirve dentro del servicio de hostelería en un espacio con licencia (finca, hotel, local). '
         'Nunca se sirve alcohol a menores'),
        ('Hojas de reclamaciones oficiales y su cartel', 'Titular', 'Antes del primer evento',
         'Según la normativa de consumo de tu comunidad autónoma'),
        ('Residuos orgánicos, cartón y aceite usado con gestor autorizado', 'Titular', 'Antes del primer evento',
         'O el de la cocina central, si lo incluye la cuota: que figure en el contrato'),
        ('Desinsectación, desratización y desinfección (DDD) de la cocina', 'Titular', 'Antes del primer evento',
         'Lo contrata la cocina central compartida: pide el certificado de la empresa inscrita en el ROESB'),
    ]),
    ('F3 - Equipamiento', 'FASE 3: EQUIPAMIENTO Y PROVEEDORES (semanas 4-10)', [
        ('Comprar la furgoneta frigorífica usada con el certificado ATP vigente', 'Titular', 'Semanas 4-6',
         'Revisa el equipo de frío y la fecha del certificado antes de pagar'),
        ('Rotular la furgoneta y montar las estanterías', 'Proveedor', 'Semanas 6-8',
         'Con el logo, la web y el teléfono: es publicidad en cada evento'),
        ('Contenedores isotérmicos GN y carros de transporte', 'Jefe/a de cocina', 'Semanas 6-8',
         'Para mantener las temperaturas del plan APPCC desde la cocina hasta la estación'),
        ('Equipo de producción: gastronorms, roner, sondas, básculas y cuchillería', 'Jefe/a de cocina',
         'Semanas 6-8', 'Lo que no ponga la cocina central compartida'),
        ('Estaciones temáticas portátiles: empieza por las 2-3 que vas a vender', 'Titular', 'Semanas 6-10',
         'Módulos con inducción, plancha y wok. El equipo específico de cada cocina del mundo (horno de leña, '
         'tandoor, trompo, ahumador) se compra cuando esa estación se venda, no antes'),
        ('Chafing dishes y expositores de bufé', 'Jefe/a de cocina', 'Semanas 6-8', 'Para bufés y desayunos'),
        ('Menaje base: vajilla, cubertería y cristalería para 150 invitados', 'Titular', 'Semanas 6-8',
         'Lo que pase de 150 se alquila para cada evento'),
        ('Mantelería y uniformes con la marca', 'Titular', 'Semanas 6-8',
         'Con recambios: la lavandería tarda entre eventos'),
        ('Mobiliario de catering: mesas altas y barra plegable', 'Titular', 'Semanas 8-10',
         'El resto del mobiliario y las carpas se alquilan y se facturan aparte (21 % de IVA)'),
        ('Software de presupuestos y agenda, tablet y datáfono', 'Titular', 'Semanas 4-6',
         'El mismo software tiene que cumplir Veri*factu (fase 1)'),
        ('Proveedores de producto étnico y de importación', 'Jefe/a de cocina', 'Semanas 4-8',
         'Asiático, latino, indio, italiano: usa la plantilla de proveedores del kit y confirma disponibilidad y '
         'plazos de pedido'),
        ('Proveedores de carne, pescado y verdura frescos con entrega en la cocina central', 'Jefe/a de cocina',
         'Semanas 4-8', 'Pedido con 48-72 horas para los eventos grandes'),
        ('Alquiladores de mobiliario, carpas y menaje para eventos grandes', 'Coordinador/a de eventos',
         'Semanas 6-10', 'Ten dos: en mayo y junio no dan abasto'),
        ('Bebida: distribuidor de vino, cava y cerveza con condiciones de devolución', 'Titular', 'Semanas 6-10',
         'Pacta la devolución de las botellas cerradas: en una barra libre no sabes cuánto se va a beber'),
    ]),
    ('F4 - Personal', 'FASE 4: PERSONAL Y FORMACIÓN (semanas 6-10)', [
        ('Definir el equipo fijo y la bolsa de personal de eventos', 'Titular', 'Semana 6',
         'Referencia del kit: un camarero por cada 10-12 invitados sentados y uno por cada 20-25 en un cóctel'),
        ('Contratos fijos discontinuos para el equipo de eventos', 'Gestoría', 'Antes del primer evento',
         'Art. 16 del Estatuto de los Trabajadores. El eventual ocasional tiene un tope de 90 días al año (art. 15.2) '
         'y el autónomo que te factura con tu horario y bajo tu dirección es falso autónomo (art. 1.1)'),
        ('Alta en la Seguridad Social antes de cada llamamiento', 'Gestoría', 'Antes de cada evento',
         'Nadie trabaja un evento sin el alta comunicada'),
        ('Aplicar el convenio provincial de hostelería', 'Gestoría', 'Antes de contratar',
         'El catering está dentro del V Acuerdo Laboral de ámbito Estatal para el sector de Hostelería (art. 4): '
         'salarios y categorías de tu provincia'),
        ('Formación en higiene alimentaria de todo el equipo', 'Jefe/a de cocina', 'Antes del primer evento',
         'La acredita la empresa y se documenta en el plan APPCC: el antiguo «carnet de manipulador» ya no existe'),
        ('Protocolo de alérgenos en las estaciones y en la barra', 'Jefe/a de cocina', 'Antes del primer evento',
         'Quién atiende las dietas especiales, cómo se marcan los platos y qué se hace ante una duda'),
        ('Plan de prevención de riesgos laborales', 'Titular', 'Antes del primer evento',
         'Obligatorio (Ley 31/1995): cargas, quemaduras, cortes y conducción'),
        ('Registro diario de jornada de todo el equipo', 'Coordinador/a de eventos', 'Desde el primer evento',
         'Art. 34.9 del Estatuto de los Trabajadores, también en los fijos discontinuos'),
        ('Informar a la plantilla del registro de jornada y del tratamiento de sus datos', 'Titular',
         'Al contratar', 'Cláusula informativa del RGPD en el contrato'),
        ('Ensayo de montaje y fichas de cada estación', 'Jefe/a de cocina', 'Semana 10',
         'Montaje completo de un evento tipo con el equipo, cronometrado. Una ficha por estación (receta, '
         'emplatado, temperaturas, alérgenos)'),
    ]),
    ('F5 - Marketing', 'FASE 5: MARCA Y CAPTACIÓN (semanas 4-12)', [
        ('Nombre, logo e identidad visual', 'Titular', 'Semanas 4-6',
         'Una marca que aguante varias cocinas del mundo sin parecer un bufé de hotel'),
        ('Dominio y correos profesionales', 'Titular', 'Semana 4', 'info@, eventos@ y el tuyo'),
        ('Web con galería, menús de muestra y formulario de presupuesto', 'Titular', 'Semanas 6-10',
         'Con fichas de estaciones, precio orientativo por invitado y SEO local («catering para eventos» y la '
         'ciudad)'),
        ('Sesión de fotos y vídeo de las estaciones', 'Titular', 'Semanas 8-10',
         'Show cooking, emplatado y montaje: es lo que venden las fincas y los planners por ti'),
        ('Perfil de Google Business y primeras reseñas', 'Titular', 'Semanas 6-12',
         'Pide la reseña a las 24 horas de cada evento con un enlace directo'),
        ('Instagram y TikTok con contenido de cada evento', 'Titular', 'Desde la semana 8',
         'Una estación por semana; etiqueta al espacio y al planner'),
        ('LinkedIn de la empresa para captar empresas', 'Titular', 'Desde la semana 8',
         'Recursos humanos, oficinas y agencias de eventos'),
        ('WhatsApp Business con plantillas', 'Coordinador/a de eventos', 'Semana 8',
         'Bienvenida, presupuesto, confirmación y seguimiento después del evento'),
        ('Directorios de bodas (Bodas.net, Zankyou)', 'Titular', 'Semanas 8-12',
         'Compara la cuota con los presupuestos que te traen antes de renovar'),
        ('Directorios profesionales y del sector (incluido Hosply)', 'Titular', 'Semanas 8-12',
         'Para agencias, hoteles y empresas'),
        ('Lista de wedding planners y fincas de tu zona y primer contacto', 'Titular', 'Semanas 6-10',
         'Pregunta por el canon al catering externo antes de presupuestar'),
        ('Degustación para planners y fincas', 'Titular', 'Semanas 10-12',
         'Una tarde con 3 estaciones: es tu mejor comercial'),
        ('Empresas, hoteles y agencias: lista y propuesta', 'Titular', 'Semanas 8-12',
         'Coffee breaks, cócteles de presentación y Navidad: son el 65 % de los eventos del plan'),
        ('Dossier de menús para empresas y para particulares', 'Titular', 'Semanas 8-10',
         'Con precio por invitado, mínimos, anticipo y política de cancelación'),
        ('Publicidad en Google Ads y ferias de novios', 'Titular', 'Desde la semana 10',
         'El presupuesto está en la línea «Marketing y publicidad» del plan financiero'),
        ('Programa de recomendación y boletín a clientes', 'Titular', 'Desde el primer evento',
         'Con el consentimiento del RGPD para enviarlo'),
    ]),
    ('F6 - Primer evento', 'FASE 6: PRIMER EVENTO Y PRIMEROS 90 DÍAS', [
        ('Briefing del cliente con formulario', 'Coordinador/a de eventos', 'D-60 o antes',
         'Invitados, horario, espacio, estaciones, dietas y alergias, presupuesto'),
        ('Visita técnica al espacio', 'Coordinador/a de eventos', 'D-30',
         'Accesos, electricidad, agua, zona de cocina de apoyo, recorrido de servicio y plan B si es al aire libre'),
        ('Presupuesto firmado y anticipo del 40 % cobrado', 'Titular', 'Para bloquear la fecha',
         'Particulares: 40 % al firmar y el resto 7 días antes. Empresas: 40/30/30 según el contrato del kit'),
        ('Contrato firmado con la política de cancelación', 'Titular', 'Con el anticipo',
         'Particulares: más de 21 días, se devuelve el anticipo; 21-7 días, se retiene el 50 % del anticipo; menos '
         'de 7 días, el anticipo entero (y con menos de 48 horas, además, el 50 % del total). Empresas: tramos de 28, '
         '14 y 7 días'),
        ('Menús y alergias confirmados por escrito', 'Coordinador/a de eventos', 'D-14',
         'Número final de invitados con su mínimo facturable'),
        ('Plan B por mal tiempo si el evento es al aire libre', 'Coordinador/a de eventos', 'D-14',
         'Carpa o espacio interior, por escrito en el contrato'),
        ('Pedidos de producto de importación y compras de fresco', 'Jefe/a de cocina', 'D-7 a D-1',
         'Lo de importación con una semana; el pescado y la verdura, el día antes'),
        ('Producción y mise en place en la cocina central', 'Jefe/a de cocina', 'D-1',
         'Con los registros de temperatura del plan APPCC'),
        ('Carga de la furgoneta con la lista de cada estación y salida con margen', 'Ayudante y conductor/a',
         'Día del evento', 'Salida con hora y media de margen sobre el tiempo del navegador'),
        ('Montaje de las estaciones y briefing del equipo', 'Coordinador/a de eventos', 'Día del evento',
         '60-90 minutos de montaje; en el briefing: horarios, alergias y quién atiende cada estación'),
        ('Servicio y show cooking', 'Equipo', 'Día del evento',
         'Temperaturas registradas en cada estación'),
        ('Recogida y entrega del espacio con fotos', 'Coordinador/a de eventos', 'Final del evento',
         'Fotos del espacio antes y después'),
        ('Factura final en 24-48 horas y cobro', 'Titular', 'D+1 / D+2',
         'Particulares: ya pagado antes del evento. Empresas: al plazo del contrato (máximo 60 días)'),
        ('Reseña, fotos y contenido del evento', 'Titular', 'D+1',
         'Pide la reseña y el permiso para publicar las fotos'),
        ('CRM, costes reales frente al presupuesto y cierre trimestral', 'Titular', 'D+7 y cada trimestre',
         'Compara el coste real de cada estación con la calculadora y ajusta precios'),
    ]),
]

assert [len(t) for _, _, t in FASES] == [12, 15, 14, 10, 16, 15], [len(t) for _, _, t in FASES]
