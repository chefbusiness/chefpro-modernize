#!/usr/bin/env python3
"""datos_checklist.py — las 84 tareas del checklist de apertura de la Finca de Eventos y Bodas ES 1.0 (F1-camino §4:
12/16/15/13/14/14). Producto nuevo: no hay versión anterior; formato del `plan-heladeria/datos_checklist.py`.
Modelo de la SPEC D2: finca ARRENDADA con edificaciones existentes y catering exclusivo concesionado con canon (la
finca no cocina: las tareas sanitarias del menú son del catering y la finca se las exige por contrato).
Marco legal = SOLO lo permitido por la SPEC D11 (marcado ✅ en `F1-research-finca.md` §0-§1):
  · urbanismo en suelo rústico: Madrid (Ley 8/2012 art. 9; Ley 9/2001 art. 148, silencio negativo), Andalucía (LISTA
    arts. 20-22, prestación compensatoria del 10 %), Cataluña (TRLU arts. 47.3 bis y 50, masías del catálogo) y C.
    Valenciana (TRLOTUP arts. 216, 219 y 221, DIC y canon del 2 %);
  · espectáculos: la boda es privada, la finca que la alquila es establecimiento público (C. Valenciana: «salón de
    banquetes», Ley 14/2010);
  · Orden INT/1068/2026 (Directriz Básica de Autoprotección: 1.000 / 5.000); RD 1367/2007 (ruido); RD 3/2023 (agua de
    pozo); RD 1086/2020 art. 30 (comida testigo); TRLGDCU arts. 85.6, 87.2, 90.2 y 103.l; LAU arts. 3-4; LIVA art. 91;
  · ET arts. 1.1 y 16 y ALEH VI art. 4 (hermanos); Ley 31/1995 (PRL).
Lo demás va con «compruébalo en tu ayuntamiento / comunidad / asesoría». Prohibido (D11): el RD derogado de
autoprotección, el 10 % para todo el paquete, «carné de manipulador», «España 2026» como sello, cifras de seguro fuera de
Andalucía y el canon del 12 % como dato. Cada tarea: (trámite / acción, responsable, plazo, notas). Pestañas ≤ 31
caracteres. Sesión Claude Code, 25-oct-2026.
"""

TITULO = 'CHECKLIST DE APERTURA — FINCA DE EVENTOS Y BODAS'

FASES = [
    ('F1 - Constitución', 'FASE 1: CONSTITUCIÓN Y FISCALIDAD (18-12 meses antes de abrir)', [
        ('Elegir forma jurídica: SL unipersonal o autónomo', 'Gestoría', 'Mes 1',
         'El plan financiero está hecho para una SL (Impuesto de Sociedades), que además es la que firma el '
         'arrendamiento de la finca. Como autónomo tributas por IRPF: compáralo con tu gestoría con las cifras del plan'),
        ('Constituir la SL', 'Notaría / Gestoría', 'Meses 1-2',
         'Antes de firmar el arrendamiento: el contrato, la calificación urbanística y las licencias van a su '
         'nombre. El capital, el que te recomiende tu gestoría'),
        ('Alta censal (modelo 036) y epígrafe del IAE', 'Gestoría', 'Mes 2',
         'Pregunta a tu gestoría si el alquiler del espacio va en el 861.2 (inmuebles urbanos) o en el grupo 862 '
         '(rústicos). El catering se da de alta en el suyo. Exento de cuota con una cifra de negocio inferior a '
         '1 millón de euros: confírmalo'),
        ('Alta en la Seguridad Social del administrador', 'Gestoría', 'Mes 2',
         'Consulta la cuota del ejercicio en curso y si te aplica la cuota reducida de inicio de actividad'),
        ('Certificado digital de la SL', 'Titular', 'Mes 1',
         'Imprescindible para Hacienda, la Seguridad Social y los trámites urbanísticos en sede electrónica'),
        ('Cuenta bancaria del negocio', 'Titular', 'Mes 2',
         'Separada de la personal: por ella pasan las señales de los novios, el canon del catering y la renta'),
        ('Gestoría laboral y fiscal y software de facturación Veri*factu', 'Titular', 'Meses 2-4',
         'Nóminas de los fijos discontinuos con sus llamamientos. Una factura por cada cobro, también por cada señal. '
         'Consulta con tu gestoría la fecha de Veri*factu que te aplica'),
        ('IVA trimestral (modelo 303) al 21 %', 'Gestoría', 'Cada trimestre',
         'Todo lo que factura la finca —espacio, servicios y canon— va al 21 %. El menú lo factura el catering a los '
         'novios, al 10 %. El IVA de la obra se recupera en los primeros 303'),
        ('Retención del arrendamiento (modelo 115)', 'Gestoría', 'Antes de pagar la primera renta',
         'Si la finca es un inmueble urbano, la renta puede llevar retención; si es rústica, en principio no. '
         'Compruébalo con tu asesoría antes de la primera factura del propietario'),
        ('Plan al banco y dos ofertas de préstamo', 'Titular', 'Meses 2-4',
         'Lleva el plan financiero completo, con la tesorería mes a mes. La finca no es tuya: pregunta por avales y '
         'por líneas públicas, porque no hay garantía inmobiliaria'),
        ('Registro de la marca en la OEPM', 'Titular', 'Meses 2-4',
         'Comprueba antes que el nombre de la finca no está registrado en tu clase (organización de eventos y '
         'alquiler de espacios)'),
        ('Protección de datos y web legal (RGPD y LSSI)', 'Titular', 'Antes de publicar la web',
         'Registro de actividades de tratamiento, cláusulas en presupuestos y contratos, aviso legal, privacidad y '
         'cookies. Pide permiso por escrito para usar fotos de los novios'),
    ]),
    ('F2 - Finca y licencia', 'FASE 2: FINCA, ARRENDAMIENTO Y LICENCIA (18-6 meses antes)', [
        ('Consulta urbanística previa de la finca', 'Titular / Técnico', 'Antes de firmar nada',
         'Pregunta en urbanismo de tu ayuntamiento si la finca es suelo urbano o rústico, qué figura usa tu '
         'comunidad para los eventos en suelo rústico y si el plan municipal lo prohíbe. En suelo urbano basta con '
         'el uso compatible y la licencia de actividad'),
        ('Elegir una finca con edificaciones existentes', 'Titular', 'Meses 1-4',
         'En suelo rústico, Madrid sólo admite los eventos en edificaciones existentes (Ley 8/2012, art. 9) y '
         'Cataluña sólo en masías del catálogo (TRLU, arts. 47.3 bis y 50). Salón, aseos y office ya construidos ahorran '
         'obra y tramitación'),
        ('Comprobar el agua, la luz y el saneamiento de la finca', 'Titular / Técnico', 'Antes de firmar',
         'Potencia eléctrica disponible, agua de red o pozo y fosa séptica o red de saneamiento. Una fosa para más de '
         '150 invitados o un vertido nuevo pueden necesitar autorización de la confederación hidrográfica: '
         'compruébalo'),
        ('Negociar el arrendamiento: plazo de quince años o más', 'Titular / Abogado', 'Meses 3-5',
         'Con edificaciones es un arrendamiento de uso distinto del de vivienda (art. 3 de la Ley de Arrendamientos '
         'Urbanos) y se pacta libremente (art. 4.3). Plazo largo, porque la obra se amortiza en el plazo del contrato'),
        ('Condición suspensiva de licencias en el contrato', 'Abogado', 'Al firmar',
         'Que el arrendamiento no obligue si se deniega la calificación o la licencia, con carencia de renta durante '
         'la obra y la tramitación'),
        ('Reversión de mejoras, opción de compra y renta de mercado', 'Abogado', 'Al firmar',
         'Qué pasa con la obra al acabar el contrato y si puedes comprar la finca. Si es de tu familia, la renta '
         'tiene que ser la de mercado igual: compruébalo con tu asesoría'),
        ('Madrid: calificación urbanística', 'Técnico', 'Meses 5-12',
         'Para actos sociales y eventos familiares en edificaciones existentes. La otorga el ayuntamiento; resolución '
         'en 3 meses y silencio NEGATIVO; caduca al año si no pides la licencia (Ley 9/2001, art. 148)'),
        ('Andalucía: autorización previa de actuación extraordinaria', 'Técnico', 'Meses 5-12',
         'Información pública de al menos un mes, 6 meses para resolver y silencio desestimatorio. Con la licencia se '
         'paga la prestación compensatoria del 10 % de las obras sin maquinaria (LISTA, art. 22)'),
        ('Cataluña y C. Valenciana: informe territorial o declaración de interés comunitario', 'Técnico',
         'Meses 5-12',
         'Cataluña: masía del catálogo con informe de la comisión territorial de urbanismo (TRLU, art. 50). C. '
         'Valenciana: DIC previa a la licencia, con canon del 2 % (TRLOTUP, arts. 216 y 221), o la reutilización de '
         'arquitectura tradicional (art. 219). En otra comunidad, pregunta en urbanismo qué figura usa'),
        ('No confirmar fechas en firme sin licencia', 'Titular', 'Hasta tener la licencia',
         'Si la calificación se deniega o se retrasa, hay que devolver lo cobrado. Antes de la licencia, sólo reservas '
         'condicionadas a la licencia, con devolución íntegra si no llega, pactada por escrito (cláusula segunda bis '
         'del modelo de contrato). Al obtenerla, se convierten en firmes'),
        ('Licencia municipal de actividad', 'Técnico', 'Meses 8-14',
         'La boda es un acto privado, pero la finca que la alquila a terceros es un establecimiento público: la C. '
         'Valenciana la cataloga como «salón de banquetes» (Ley 14/2010). Compruébalo en la ley de espectáculos de '
         'tu comunidad'),
        ('Aforo, evacuación y medidas de emergencia', 'Técnico', 'Con el proyecto',
         'El aforo legal lo fija la licencia. Con 300 invitados no hay plan de autoprotección estatal: empieza en '
         '1.000 personas en edificio cerrado o carpa y en 5.000 al aire libre en recinto delimitado (Orden '
         'INT/1068/2026). Tu comunidad o '
         'tu ayuntamiento pueden pedir más'),
        ('Ruido: estudio acústico y limitador-registrador', 'Técnico', 'Con el proyecto',
         'Límite al exterior en zona residencial: 55 dBA de día y de tarde y 45 de noche (RD 1367/2007, anexo III). '
         'El limitador lo exigen muchas ordenanzas: compruébalo en la tuya'),
        ('Horario de cierre y música exterior', 'Titular', 'Con la licencia',
         'Lo fijan una orden de tu comunidad y la ordenanza de ruido de tu ayuntamiento. Pregúntalo y escríbelo en '
         'el contrato con los novios'),
        ('Seguro de responsabilidad civil con el capital de tu comunidad', 'Corredor de seguros', 'Antes de abrir',
         'El capital mínimo depende del aforo y de la comunidad: en Andalucía, 526.000 € para 101-300 personas '
         '(Decreto 109/2005). Añade daños a las mejoras y pérdida de beneficio'),
        ('Agua de pozo propio: analíticas y protocolo', 'Titular / Laboratorio', 'Antes del primer evento',
         'Con actividad comercial, un pozo propio es una zona de abastecimiento de tipo 1 y el titular responde de la '
         'calidad del agua hasta el grifo (RD 3/2023, arts. 2 y 4.3)'),
    ]),
    ('F3 - Obra y equipamiento', 'FASE 3: OBRA Y EQUIPAMIENTO (12-3 meses antes)', [
        ('Tres presupuestos sobre el proyecto técnico', 'Titular / Técnico', 'Antes de la obra',
         'Compáralos partida a partida con la hoja de Inversión del plan financiero'),
        ('Licencia o comunicación de la obra', 'Técnico', 'Antes de empezar',
         'Pregunta en tu ayuntamiento qué título necesita la obra y no empieces sin él'),
        ('Adecuación del salón', 'Constructora', 'Meses 1-3 de obra',
         'Suelos, cerramientos, carpintería y pintura sobre la edificación existente'),
        ('Acústica y aislamiento del salón', 'Constructora', 'Meses 1-3 de obra',
         'Para que el baile final pueda ir dentro sin superar el límite de noche al exterior'),
        ('Aseos, con uno adaptado', 'Constructora', 'Meses 1-3 de obra',
         'Itinerario accesible hasta el salón, la carpa y los aseos: compruébalo con tu técnico'),
        ('Instalación eléctrica y boletín', 'Instalador autorizado', 'Mes 3 de obra',
         'Cuadro, alumbrado exterior y de emergencia, y potencia para salón, carpa y office'),
        ('Grupo electrógeno', 'Instalador autorizado', 'Mes 3 de obra',
         'Dimensionado para el salón y el office. Revisión antes de cada temporada'),
        ('Climatización del salón', 'Instalador autorizado', 'Mes 3 de obra',
         'Frío y calor: el salón se usa todo el año, también en agosto'),
        ('Office del catering con agua y desagüe', 'Constructora / Catering', 'Mes 3 de obra',
         'Diséñalo con el catering que vayas a homologar: cámara, fregaderos, mesas inox y zona de emplatado. La '
         'cocina de producción es suya'),
        ('Carpa o pérgola para ceremonia y cóctel', 'Proveedor', 'Antes de la temporada',
         'Es el plan B de lluvia. Pide el certificado de montaje y de resistencia al viento del fabricante'),
        ('Mobiliario, mantelería base y zona chill-out', 'Titular', 'Mes 3 de obra',
         'Mesas, 300 sillas y mantelería base; la decoración especial la contratan los novios'),
        ('Sonido, limitador-registrador y proyector', 'Instalador', 'Mes 3 de obra',
         'El limitador, precintado y con registro, es tu prueba ante una denuncia por ruido'),
        ('Aparcamiento, caminos y señalización', 'Constructora', 'Meses 2-3 de obra',
         'Una plaza por cada 2,5-3 invitados (estimación del kit), acceso que aguante la lluvia e iluminación'),
        ('Jardinería, zona de ceremonia y riego', 'Jardinero', 'Antes de la temporada',
         'Planta con tiempo: el jardín de las fotos tarda una temporada en estar bonito'),
        ('Protección contra incendios y certificado final de obra', 'Técnico / Empresa mantenedora',
         'Al acabar la obra',
         'Extintores, alumbrado y señales de evacuación y el certificado final que pide la licencia de actividad'),
    ]),
    ('F4 - Personal y catering', 'FASE 4: PERSONAL Y CATERING EXCLUSIVO (6-2 meses antes)', [
        ('Contratar la coordinación como fija discontinua', 'Gestoría', '3 meses antes',
         'Contrato fijo discontinuo (art. 16 del Estatuto de los Trabajadores) de marzo a noviembre, con '
         'llamamiento por escrito. De diciembre a febrero coordina el titular'),
        ('Auxiliares de montaje y acceso como fijos discontinuos', 'Gestoría', '2 meses antes',
         'Nunca como autónomos que te facturan: con tu horario y tu dirección es falso autónomo (art. 1.1 ET). Para '
         'los picos, una ETT'),
        ('Mantenimiento, comercial y limpieza', 'Gestoría', '3 meses antes',
         'Contratos a tiempo parcial con las horas del plan. Usa el convenio provincial de hostelería como referencia '
         'salarial prudente (ALEH VI, art. 4) y confírmalo con tu asesoría'),
        ('Alta en la Seguridad Social antes de cada llamamiento', 'Gestoría', 'Antes de cada temporada',
         'Y la baja al terminar el periodo de actividad'),
        ('Registro de jornada', 'Titular', 'Desde el primer día',
         'Obligatorio para toda la plantilla, también en los eventos que acaban tarde'),
        ('Prevención de riesgos laborales', 'Servicio de prevención', 'Antes de la primera contratación',
         'Plan de prevención (Ley 31/1995): montaje, cargas, trabajo en altura, jardinería y conducción en la finca'),
        ('Elegir uno o dos caterings para homologar', 'Titular', '6 meses antes',
         'Prueba de menú con cada uno, referencias de otras fincas, inscripción sanitaria de su cocina y su seguro. '
         'El catering exclusivo es la mitad de la reputación de tu finca'),
        ('Contrato de concesión del catering exclusivo', 'Titular / Abogado', '5 meses antes',
         'Exclusividad y plazo, horarios, limpieza del office, salida y penalizaciones. Con el modelo de contrato de '
         'este pack'),
        ('Canon pactado y auditable', 'Titular', 'En el contrato',
         'El plan supone un canon del 12 % de lo que factura el catering en la finca: es un supuesto, negócialo. '
         'Que el recuento de invitados de cada evento sea comprobable'),
        ('Comida testigo en cada boda y encargo de más de 40 personas', 'Catering', 'En el contrato',
         'Una ración de al menos 100 g de cada plato, a 4 °C o menos (o a −18 °C) durante 7 días. La guarda quien '
         'sirve, en el momento del servicio (RD 1086/2020, art. 30)'),
        ('Alérgenos de cada menú por escrito', 'Catering', 'En el contrato',
         'El catering informa de los alérgenos de cada plato y recoge las alergias de los invitados con el recuento '
         'final. Pídelo por escrito en cada evento'),
        ('Inscripción sanitaria del office y seguros del catering', 'Catering', 'Antes del primer evento',
         'El office que usa el catering lo inscribe él en el registro de tu comunidad (compruébalo allí). Pide su '
         'póliza de responsabilidad civil con intoxicación alimentaria'),
        ('Lista de proveedores de la finca', 'Titular', '4 meses antes',
         'Fotógrafos, música, flores y decoración que conocen la finca. Decide si cobras por los proveedores externos '
         'que traigan los novios y escríbelo en el contrato'),
    ]),
    ('F5 - Marca y reservas', 'FASE 5: MARCA, TARIFAS Y RESERVAS (12-3 meses antes)', [
        ('Nombre, logo e identidad de la finca', 'Titular', 'Mes 1',
         'Antes de la web y de los portales: es lo que verán las parejas al comparar'),
        ('Web con calendario, galería y formulario de visita', 'Titular', 'Mes 2',
         'Fotos reales de la finca montada, aforo, tipos de evento y cómo pedir una visita'),
        ('Fotos y vídeo profesionales de la finca montada', 'Fotógrafo', 'En cuanto haya obra acabada',
         'Monta una mesa de boda real con el catering para las fotos. Sin fotos no hay reservas'),
        ('Ficha de empresa en Google y primeras reseñas', 'Titular', 'Mes 2',
         'Con fotos, horario de visitas y respuesta a cada reseña'),
        ('Portales de bodas: medir el coste por contacto', 'Titular', 'Mes 3',
         'Empieza con la ficha básica y pasa al escaparate de pago si las cuentas salen. Anota de dónde viene cada '
         'pareja que reserva'),
        ('Redes sociales con bodas y eventos reales', 'Titular', 'Desde el mes 3',
         'Instagram y Pinterest con montajes reales y permiso por escrito de los novios'),
        ('Ferias nupciales', 'Titular', 'Según el calendario de tu zona',
         'Una o dos al año, con el catering. Lleva el dossier y una forma de reservar visita en el momento'),
        ('Jornada de puertas abiertas con el catering', 'Titular / Catering', 'Antes de la primera temporada',
         'La finca montada, el catering sirviendo una degustación y los proveedores de la lista'),
        ('Wedding planners y agencias de eventos', 'Titular', 'Meses 3-6',
         'Visita guiada, dossier y comisión pactada por escrito. El plan supone que una de cada cinco ventas llega por '
         'ellos'),
        ('Empresas, comuniones y celebraciones', 'Titular', 'Meses 3-6',
         'Son los eventos que llenan el invierno y los días de diario: jornadas de empresa, comidas de Navidad, '
         'comuniones y cumpleaños'),
        ('Tarifas por temporada y día', 'Titular', 'Antes de la primera visita',
         'Con la calculadora de presupuestos de este pack: temporada alta, media y baja, sábado frente a viernes, '
         'domingo y diario, mínimo de invitados y extras'),
        ('Dossier de bodas y de empresa', 'Titular', 'Mes 3',
         'Qué incluye el espacio, qué pone el catering, tarifas orientativas, calendario de pagos y condiciones'),
        ('Contrato de reserva con los novios', 'Titular / Abogado', 'Antes de la primera señal',
         'Con el modelo de este pack: señal y penalizaciones proporcionadas (art. 85.6 del TRLGDCU) y recíprocas: si '
         'retienes lo pagado cuando cancelan, pacta lo mismo si cancelas tú (art. 87.2)'),
        ('Calendario de fechas y CRM', 'Titular', 'Mes 2',
         'Una sola agenda para las visitas, las fechas bloqueadas, las señales y los pagos pendientes'),
    ]),
    ('F6 - Temporada y eventos', 'FASE 6: TEMPORADA Y CADA EVENTO', [
        ('Visita y presupuesto por escrito', 'Titular / Comercial', 'Al recibir la petición',
         'Presupuesto con la calculadora, válido por un plazo, con lo que incluye y lo que no'),
        ('Contrato firmado, señal y factura de la señal', 'Titular', 'Al reservar la fecha',
         'Cada cobro, también la señal, lleva su factura con el IVA del 21 %'),
        ('Sin derecho de desistimiento: avísalo por escrito', 'Titular', 'Al reservar la fecha',
         'Si contratas a distancia o fuera de la finca (web, correo o teléfono), un servicio de esparcimiento con fecha '
         'concreta queda fuera del derecho de desistimiento (TRLGDCU, art. 103.l). Dilo en el contrato para evitar '
         'discusiones'),
        ('Fuero del consumidor en el contrato', 'Abogado', 'En el contrato',
         'Con particulares es abusiva la cláusula que les lleve a un juzgado distinto del de su domicilio o del lugar '
         'donde se presta el servicio (TRLGDCU, art. 90.2)'),
        ('Prueba de menú con el catering', 'Catering / Titular', '4-6 meses antes',
         'Sin ella no se cierra el menú. El catering cobra o descuenta la prueba según su contrato'),
        ('Recuento final de invitados y alergias', 'Coordinación', '15 días antes',
         'Por escrito, con las alergias e intolerancias de cada mesa. Es la base del canon y del personal del día'),
        ('Plan B de lluvia, calor y alerta de incendios', 'Coordinación', '7 días antes',
         'Carpa preparada y avisos a los novios. Bengalas, fuegos artificiales y barbacoas, prohibidos en época de '
         'peligro de incendios: compruébalo con tu comunidad'),
        ('Montaje y control del aforo', 'Coordinación / Auxiliares', 'Día del evento',
         'Nunca más invitados de los que permite la licencia. Señalización y salidas despejadas'),
        ('Limitador y música exterior hasta la hora de la ordenanza', 'Coordinación', 'Día del evento',
         'El baile final, dentro y con el limitador. Altavoces de espaldas a las viviendas'),
        ('Comida testigo verificada', 'Coordinación', 'Día del evento',
         'Comprueba que el catering guarda las raciones testigo de cada plato (RD 1086/2020, art. 30)'),
        ('Recogida, limpieza y revisión de daños', 'Auxiliares / Limpieza', 'Final del evento y día siguiente',
         'Fotos del estado de la finca al acabar: si hay daños, se descuentan de la fianza según el contrato'),
        ('Liquidación del canon con el catering', 'Titular', 'Mensual',
         'Con el recuento firmado de cada evento. Factura del canon al 21 %'),
        ('Reseña, fotos y agradecimiento', 'Titular', 'Semana siguiente',
         'Pide la reseña a los novios y las fotos al fotógrafo, con permiso para publicarlas'),
        ('Cierre trimestral: ocupación, canon y caja', 'Titular', 'Cada trimestre',
         'Eventos celebrados frente al plan, precio medio por invitado, canon cobrado y saldo de caja frente a la '
         'hoja de Tesorería'),
    ]),
]

assert [len(t) for _f, _c, t in FASES] == [12, 16, 15, 13, 14, 14], [len(t) for _f, _c, t in FASES]
assert all(len(f) <= 31 for f, _c, _t in FASES)
