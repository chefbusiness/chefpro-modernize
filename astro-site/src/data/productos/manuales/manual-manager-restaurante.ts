// manual-manager-restaurante.ts — LÍNEA MANUALES OPERATIVOS, producto 46 (2026-09-04).
//
// Primer producto de la línea «Manuales operativos» y segunda landing NATIVA en Astro
// (no hay página SPA de la que portar copy). Reutiliza el contrato `GuiaData` y el
// template `GuiaLandingPage.astro` (decisión D20 de la SPEC): el tipo no tiene ninguna
// palabra «guía» a fuego y el único H2 que la decía ya está parametrizado con
// `why.titlePre` / `why.titleGold`.
//
// Fuente del copy: la SPEC firmada (scripts/productos-digitales/manual-manager-SPEC.md)
// y el research consolidado
// (scripts/productos-digitales/auditorias/manual-manager-RESEARCH-2026-09-04.md).
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  - D1/D2: producto nuevo → SIN `priceOld` ni `discountBadge` (no existe «precio
//    anterior de 30 días»: art. 20 TRLGDCU / RDL 24/2021), SIN `aggregateRating` y con
//    `testimonials.items: []` (no ha vendido una unidad, así que no hay reseñas).
//  - CERO cifras sin fuente primaria. La ÚNICA cifra de mercado admitida es el coste
//    anual del software de gestión comparable (1.140 € sin IVA, plan Growth de Last.app,
//    precio oficial consultado el 2026-09-04). Prohibido el plan Starter, el «5,7 %» y
//    cualquier variante del «60 % de los restaurantes cierra» (lista negra, SPEC §8).
//  - D5/D6/D8/D9/D10/D11: nada de «SS a cargo de la empresa 23,60 %», nada de «el
//    permiso parental es (o no es) retribuido» sin distinguir las dos figuras, nada de
//    umbrales de prime cost presentados como cifra de fuente.
//  - D22: la landing dice en la PRIMERA pantalla y en la FAQ que el marco legal
//    explicado es el español y que los parámetros viven en casillas editables.
//  - «manager (gerente/encargado)» en la primera mención (hero.description).
//  - `77` y `28` son TOKENS: se sustituyen por las páginas
//    MEDIDAS con PyMuPDF cuando el PDF esté construido (D17). NO publicar con el token.
import type { GuiaData } from '../guias/types';

const data: GuiaData = {
  slug: 'manual-manager-restaurante',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_MANUAL_MANAGER',

  seo: {
    title: 'Manual del Manager de Restaurante | Operaciones y Equipo',
    description: 'Para quien ya gestiona un restaurante: cuadro de mando semanal, cuadrante y registro de jornada, KPIs, quejas y cumplimiento 2026. 20 capítulos y 7 Excel.',
    keywords: 'manual del manager de restaurante, gerente de restaurante, encargado de restaurante, manual de operaciones de un restaurante, gestión de restaurantes, administrador de restaurante, jefe de sala, KPI restaurante, cuadrante de turnos, registro de jornada hostelería, convenio hostelería ALEH, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-manual-manager-restaurante.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'Para quien ya dirige el turno: criterio para decidir, no otro checklist',
    titlePre: 'Manual del ',
    titleGold: 'Manager de Restaurante',
    subtitleLine: 'Operaciones, personas, números, servicio y ley: el criterio del día a día, con cada norma citada y con fecha',
    description: 'Un manager (gerente/encargado) no se atasca por no tener plantillas: se atasca por no saber qué decidir con lo que sale de ellas. Este manual es la capa que falta: qué mirar cada lunes, qué firmar, qué se puede exigir a alguien y qué no, y qué hacer cuando el viernes se cae una persona a dos horas del servicio.',
    checkItems: [
      'Manual completo PDF + DOCX editable (20 capítulos, 77 páginas)',
      '7 herramientas Excel con fórmulas vivas: cuadro de mando semanal, matriz de polivalencia, quejas y reseñas, scorecard de selección, calendario de cumplimiento legal, reuniones con plan de 90 días y auditoría interna de servicio',
      'Normativa al día a 4 de septiembre de 2026: cada tabla legal lleva norma, artículo, fuente oficial y fecha (incluida la última modificación del convenio estatal de hostelería)',
      'El marco legal explicado es el español, con norma, artículo y enlace citados; los parámetros viven en casillas editables para adaptarlos a tu país',
      'Bonus: 12 situaciones resueltas (28 páginas)',
    ],
    ctaLabel: 'COMPRAR MANUAL — 55 EUR',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    price: '55 EUR',
    heroNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    buyBoxNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    bonusTotalLabel: 'Incluido en el precio: el manual, las 7 herramientas Excel y el bonus de 12 situaciones resueltas',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/manual-manager-hero.jpg',
      '/lovable-uploads/ai-gallery/manual-manager-sala.jpg',
      '/lovable-uploads/ai-gallery/manual-manager-briefing.jpg',
      '/lovable-uploads/ai-gallery/manual-manager-oficina.jpg',
      '/lovable-uploads/ai-gallery/manual-manager-pase.jpg',
      '/lovable-uploads/ai-gallery/manual-manager-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/manual-manager-oficina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/manual-manager-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/manual-manager-sala.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 7 Herramientas Excel + 1 Bonus',
    subtitle: 'Criterio, no teoría. Cada capítulo se apoya en una de las siete herramientas Excel del pack y sus tablas salen de las celdas de esos ficheros o de la norma citada, nunca de un ejemplo inventado. Escrito por un chef y consultor gastronómico que lleva desde 2010 dentro de operaciones reales.',
    chapters: [
      { icon: 'Users', num: '01', title: 'Qué Es Exactamente un Manager de Restaurante (y para Quién Es Este Manual)', desc: 'Gerente, encargado, director, jefe de sala y administrador con el organigrama real del convenio; mapa problema → capítulo → herramienta, y qué no vas a encontrar aquí.' },
      { icon: 'BarChart3', num: '02', title: 'Los Números Que Gobiernan tu Turno: 12 Definiciones Que Casi Nadie Distingue', desc: 'Ticket medio, gasto por cubierto, ventas por hora, food cost, coste de personal, prime cost, rotación, absentismo y temporalidad: qué mide cada uno y cuál manda.' },
      { icon: 'CalendarDays', num: '03', title: 'El Cuadro de Mando Semanal: por Qué la Semana y No el Mes', desc: 'Qué se mira cada lunes en quince minutos, cómo se lee un semáforo y qué esconde el promedio del mes cuando una semana se ha ido al garete.' },
      { icon: 'Banknote', num: '04', title: 'Prime Cost y Coste de Personal: Dónde Se Pierde el Margen', desc: 'Del salario bruto al coste-empresa con la cotización desglosada partida a partida en celda editable, y por qué un food cost bueno puede estar tapando un problema de horas.' },
      { icon: 'Clock', num: '05', title: 'El Día del Manager: Apertura, Servicio, Cierre y Handover', desc: 'El criterio detrás del checklist: qué decide cada bloque del día, qué se delega, qué firma el manager y qué se transmite al turno siguiente.' },
      { icon: 'Coins', num: '06', title: 'La Caja y el Tique: Corte, Arqueo, Cierre — y lo Que Viene', desc: 'Los tres pasos y por qué no son sinónimos, qué hacer con un descuadre que se repite, propinas, factura simplificada y las fechas reales de Verifactu y la factura electrónica.' },
      { icon: 'Megaphone', num: '07', title: 'Mandar sin Quemar al Equipo: Autoridad, Delegación y Cómo Defender un Cambio con Números', desc: 'Autoridad formal frente a autoridad real, señales tempranas de desgaste y cómo llevar una propuesta al propietario con la cifra de la semana delante.' },
      { icon: 'ScrollText', num: '08', title: 'El Convenio Que Te Aplica: el Estatal de Hostelería, tu Provincia y lo Que No Se Negocia', desc: 'Las materias que el convenio provincial no puede tocar, cómo se busca el tuyo en el registro público de convenios y qué pasa cuando el de tu provincia ha vencido.' },
      { icon: 'FileEdit', num: '09', title: 'Contratar sin Fabricar un Indefinido por Accidente', desc: 'El contrato se presume indefinido: circunstancias de la producción, sustitución, fijo-discontinuo, periodo de prueba del convenio y el encadenamiento de 18 meses en 24.' },
      { icon: 'UserPlus', num: '10', title: 'Selección con Criterio y los Primeros 30 Días', desc: 'Entrevista estructurada con scorecard, lo que no se puede preguntar por ley, plan de acogida y las cuatro formaciones distintas que se confunden entre sí.' },
      { icon: 'CalendarRange', num: '11', title: 'Jornada, Cuadrante y Registro de Jornada: Tres Documentos Que No Son lo Mismo', desc: 'Cuarenta horas de promedio en cómputo anual, doce horas entre jornadas, nueve horas diarias, cuatro años de conservación del registro y el nuevo régimen disciplinario del convenio.' },
      { icon: 'Palmtree', num: '12', title: 'Permisos, Vacaciones y Conciliación sin Sustos', desc: 'Treinta días naturales, fallecimiento, enfermedad grave, las dos figuras del permiso parental, fuerza mayor, guarda legal y la adaptación de jornada con silencio positivo.' },
      { icon: 'Shuffle', num: '13', title: 'Rotación, Absentismo y Polivalencia: Qué Se Puede Medir de Verdad', desc: 'Las tres cosas separadas con su fórmula, qué dato existe y cuál no, la matriz de polivalencia y el punto único de fallo calculado con tus propias cifras.' },
      { icon: 'UserCheck', num: '14', title: 'Evaluar, Corregir y, si Toca, Despedir', desc: 'Régimen disciplinario del convenio, la audiencia previa obligatoria de dos días con su excepción, indemnizaciones y qué lleva un finiquito.' },
      { icon: 'ShieldCheck', num: '15', title: 'Lo Que Obliga Aunque Seáis Tres: Igualdad, Acoso, Desconexión y PRL', desc: 'Registro retributivo y protocolo de acoso sin umbral de plantilla, política escrita de desconexión digital y por qué los reconocimientos médicos son voluntarios salvo tres excepciones.' },
      { icon: 'ConciergeBell', num: '16', title: 'El Servicio: Estándares, Briefing y la Conversación Cocina-Sala', desc: 'Briefing, reunión y handover no son lo mismo: guion de siete minutos, estándares escritos y el conflicto cocina-sala tratado como problema de sistema.' },
      { icon: 'MessageSquare', num: '17', title: 'Quejas, Hojas de Reclamaciones y Reseñas: Tres Cosas Distintas', desc: 'Protocolo de queja en sala, la hoja oficial como competencia autonómica con sus plazos, y quién responde las reseñas, en cuántos días y con qué tono.' },
      { icon: 'Smartphone', num: '18', title: 'Reservas, No-Shows y Datos del Cliente', desc: 'Política de garantía y cómo comunicarla, el efecto de la espera y el tratamiento de datos de una reserva: qué base legal aplica y qué registro hay que llevar.' },
      { icon: 'Thermometer', num: '19', title: 'Seguridad Alimentaria y el Local: de lo Que Responde el Manager', desc: 'Cultura de seguridad alimentaria como obligación de la dirección, alérgenos, temperaturas vigentes, anisakis, trazabilidad, terraza, música y desperdicio alimentario.' },
      { icon: 'ClipboardCheck', num: '20', title: 'El Calendario del Manager, la Auditoría Interna y los 90 Días Siguientes', desc: 'Qué obligaciones tienen periodicidad fijada por una norma estatal y cuáles se venden como tal sin serlo, la auditoría puntuable y trece semanas con responsable y fecha.' },
    ],
  },

  // D2: producto recién lanzado, sin una sola venta → sin testimonios y sin
  // aggregateRating. El template oculta esta sección con items vacío.
  testimonials: {
    titleGold: '',
    subtitle: '',
    items: [],
  },

  why: {
    titlePre: '¿Por Qué Este ',
    titleGold: 'Manual',
    reasons: [
      { icon: 'Target', title: 'Criterio, No Otro Checklist', desc: 'Plantillas gratuitas hay a cientos y no es lo que te falta. Lo que falta es saber qué hacer con lo que sale de ellas: qué mirar cada lunes, qué decisión tomar cuando el número se pone rojo y qué conversación toca tener. Eso es lo que este manual escribe, capítulo a capítulo.' },
      { icon: 'ScrollText', title: 'Cada Norma Citada, con Fecha', desc: 'Cada afirmación normativa lleva norma, artículo y enlace, y cada tabla legal lleva al pie la fecha en la que se verificó: 4 de septiembre de 2026, el mismo día en que se publicó la modificación del convenio estatal de hostelería. Nunca «es obligatorio» a secas.' },
      { icon: 'FileSpreadsheet', title: 'Siete Excel Que de Verdad Calculan', desc: 'No son PDF para rellenar a mano: metes tus datos y calculan. Construidos a propósito sin las funciones que rompen la compatibilidad, así que funcionan igual en Excel, Google Sheets, LibreOffice y Numbers, con los parámetros legales en casillas editables.' },
      { icon: 'Wallet', title: 'Un Pago Único Frente a una Cuota Anual', desc: 'El plan Growth de Last.app, el software de gestión más comparable, cuesta 1.140 € al año sin IVA según su precio oficial consultado el 4 de septiembre de 2026. Este manual es un pago único con acceso de por vida y actualizaciones incluidas.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además del manual PDF + DOCX, recibes 7 herramientas Excel con fórmulas vivas y el bonus de situaciones resueltas',
    layout: 'split',
    items: [
      { icon: 'BarChart3', label: 'HERRAMIENTA 1', title: 'Cuadro de Mando Semanal del Manager', value: 'Incluido en el pack', desc: 'Cincuenta y dos semanas ISO con ventas, cubiertos, coste de producto y coste de personal con su cotización empresarial desglosada en nota, prime cost semanal, semáforos y una hoja de definiciones para que nadie discuta qué mide cada KPI.', image: '/lovable-uploads/ai-gallery/manual-manager-oficina.jpg' },
      { icon: 'Layers', label: 'HERRAMIENTA 2', title: 'Matriz de Formación y Polivalencia', value: 'Incluido en el pack', desc: 'Tu plantilla cruzada con las estaciones del local: quién sabe hacer qué y a qué nivel, plan de formación cruzada, cobertura por estación y el coste real de una baja calculado con tus datos.', image: '/lovable-uploads/ai-gallery/manual-manager-pase.jpg' },
      { icon: 'MessageSquare', label: 'HERRAMIENTA 3', title: 'Quejas, Reclamaciones y Reseñas', value: 'Incluido en el pack', desc: 'Registro de quejas en sala, seguimiento de reclamaciones formales con los plazos de respuesta que sí están verificados y una casilla editable para el resto, control de reseñas por plataforma y resumen del periodo.', image: '/lovable-uploads/ai-gallery/manual-manager-sala.jpg' },
      { icon: 'UserPlus', label: 'HERRAMIENTA 4', title: 'Scorecard de Selección y Entrevista', value: 'Incluido en el pack', desc: 'Scorecard por competencias con puntuación ponderada, comparativa de candidatos y un banco de preguntas por competencia con la nota legal de lo que no se puede preguntar en una entrevista.', image: '/lovable-uploads/ai-gallery/manual-manager-briefing.jpg' },
      { icon: 'ScrollText', label: 'HERRAMIENTA 5', title: 'Calendario de Cumplimiento Legal', value: 'Incluido en el pack', desc: 'Estado normativo con fecha de corte editable, calendario de vencimientos con la columna «¿lo fija una norma estatal?», documentación obligatoria y tres hojas de referencia: topes de jornada, permisos con su cómputo y régimen disciplinario del convenio.', image: '/lovable-uploads/ai-gallery/manual-manager-oficina.jpg' },
      { icon: 'ClipboardList', label: 'HERRAMIENTA 6', title: 'Reuniones, Acuerdos y Plan de 90 Días', value: 'Incluido en el pack', desc: 'Calendario de reuniones, guion de la semanal, ficha de uno-a-uno, actas con acuerdos y responsable, y un plan de noventa días con veinte decisiones, su herramienta de origen, su semana y su estado.', image: '/lovable-uploads/ai-gallery/manual-manager-briefing.jpg' },
      { icon: 'ClipboardCheck', label: 'HERRAMIENTA 7', title: 'Auditoría Interna de Servicio', value: 'Incluido en el pack', desc: 'Alrededor de sesenta puntos de control repartidos en seis áreas del servicio, con puntuación, resumen por área e histórico para comparar auditorías. Deja fuera a propósito los registros de APPCC, que tienen su propio pack.', image: '/lovable-uploads/ai-gallery/manual-manager-pase.jpg' },
      { icon: 'GraduationCap', label: 'BONUS', title: '12 Situaciones Resueltas del Manager', value: 'Incluido en el pack', desc: 'Doce marrones reales con datos: la baja a dos horas del servicio, la caja que descuadra tres días seguidos, la hoja de reclamaciones, la reseña de una estrella que habla de intoxicación, el prime cost disparado, la inspección sin avisar o el despido disciplinario. Cada uno con qué NO hacer, protocolo, norma aplicable, herramienta del pack y el guion literal de la conversación cuando la hay.', image: '/lovable-uploads/ai-gallery/manual-manager-equipo.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL MANUAL — 55 EUR',
  },

  guarantee: {
    text: 'Si el manual no te sirve para dirigir tu restaurante con más criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Qué hace exactamente el manager (gerente/encargado) de un restaurante?', a: 'Responde de que el servicio salga y de que el negocio aguante: abre y cierra, coordina sala y cocina durante el pase, decide sobre el cuadrante y las horas, contrata y forma, controla caja y compras, atiende las quejas y firma lo que la ley obliga a firmar. En Hispanoamérica el mismo puesto se llama a menudo administrador o administrador de restaurante, y las funciones son las mismas: cambia el nombre, no el trabajo. El capítulo 1 delimita el puesto y el capítulo 5 desglosa el día completo, bloque a bloque.' },
    { q: '¿Cuáles son los rangos en un restaurante?', a: 'Depende de a qué llames rango. El convenio estatal de hostelería no organiza la plantilla por títulos de puesto, sino por áreas funcionales y grupos profesionales, y de ahí salen la retribución y la clasificación. «Encargado», «director» o «administrador» son denominaciones de uso interno, no categorías del convenio: por eso dos locales de la misma calle pueden llamar distinto al mismo puesto y estar los dos bien. El capítulo 1 pinta el organigrama con las áreas y los grupos reales del convenio vigente y explica dónde encaja cada nombre de uso.' },
    { q: '¿Qué debe contener un manual de operaciones y cómo escribo el de mi restaurante?', a: 'Cinco bloques: la operación del día (apertura, pase, cierre y traspaso de turno), las personas (contratación, jornada, permisos, evaluación), los números (qué se mide, cada cuánto y con qué umbral), el servicio (estándares, briefing, quejas y reservas) y el cumplimiento legal, que atraviesa a los cuatro anteriores. Lo que casi nunca se dice es que un manual sin dueño y sin fecha de revisión es papel mojado: cada procedimiento necesita responsable, herramienta donde se registra y momento en el que se revisa. Este manual trae los cinco bloques escritos y las siete herramientas donde se registran, para que el tuyo sea una adaptación y no una hoja en blanco.' },
    { q: '¿Cómo se hace un cuadrante de trabajo por turnos?', a: 'Se parte de la demanda real por franja, no de la costumbre: cubiertos o tickets por hora de las últimas semanas marcan cuánta gente hace falta y cuándo. Encima se colocan los límites que no son negociables (descanso entre jornadas, máximo diario, descanso semanal, vacaciones y permisos ya concedidos) y solo después se reparten nombres, cruzando el cuadrante con la matriz de polivalencia para no dejar una estación sin nadie que sepa cubrirla. El capítulo 11 explica los tres documentos que suelen confundirse —cuadrante, registro de jornada y calendario laboral— y qué obliga cada uno.' },
    { q: '¿Cuándo me tienen que entregar el cuadrante de trabajo?', a: 'La distribución irregular de la jornada exige un preaviso mínimo de cinco días para conocer el día y la hora de trabajo (art. 34.2 del Estatuto de los Trabajadores), y el calendario laboral anual se publica y se expone en un sitio visible del centro. Ojo con no mezclarlo con el registro de jornada, que es otra cosa: se anota cada día, con hora de inicio y fin, y se conserva cuatro años a disposición de la persona trabajadora, de la representación legal y de la Inspección. El capítulo 11 trae la tabla de topes con su norma, su enlace y la fecha de verificación.' },
    { q: '¿Qué establecimientos están obligados a tener hoja de reclamaciones?', a: 'En la práctica, cualquier establecimiento abierto al público que preste servicios a consumidores, y un restaurante lo es. El matiz importante es que las hojas de reclamaciones son competencia autonómica: el modelo, el cartel que hay que exponer, el plazo para responder y hasta el formato electrónico cambian de una comunidad a otra. En Cataluña el plazo de respuesta es de un mes; en Andalucía, de diez días hábiles, y la hoja electrónica es obligatoria desde mayo de 2026. El capítulo 17 y la herramienta de quejas traen lo verificado y dejan casilla editable para tu comunidad, con la advertencia de comprobarlo en tu boletín autonómico.' },
    { q: '¿Este manual sirve si mi restaurante está fuera de España?', a: 'Sí, con un matiz que conviene decir claro antes de comprar: el bloque normativo está escrito con la ley española, y sus artículos y enlaces son españoles (en el caso de España, cada norma está verificada contra su publicación en el Boletín Oficial del Estado, el BOE, con fecha 4 de septiembre de 2026 al pie de cada tabla). Lo que viaja es todo lo demás, que es la mayor parte: el método de dirección, la manera de leer los números, los protocolos de servicio, las conversaciones difíciles y las siete herramientas, cuyos parámetros (tipos de cotización, umbrales, plazos, objetivos y periodicidades) viven en casillas editables para que sustituyas los valores por los de tu país. El vocabulario incluye las equivalencias de Hispanoamérica: gerente/encargado y administrador, cuadrante y rol de horario, arqueo y corte de caja, nómina y planilla, sala y salón. Y si prefieres que adaptemos el bloque normativo y los parámetros a la legislación de tu país, escríbenos a info@aichef.pro: lo hacemos como servicio de consultoría.' },
    { q: '¿Necesito el Kit de Gestión de Personal o el Kit de Tareas si compro este manual?', a: 'No, y tampoco compras nada repetido si ya los tienes. La jerarquía es clara: los kits son las plantillas de ejecución (checklists del día, cuadrante, control de horas, coste laboral, onboarding, vacaciones, evaluación) y el manual es el criterio y la decisión: cuándo usar cada plantilla, qué significa lo que sale de ella y qué hacer a continuación. El manual trae sus siete herramientas propias, que no están en ningún kit, y dice explícitamente en el capítulo 1 qué incluye el pack y qué vive en los otros productos, para que no compres dos veces lo mismo.' },
    { q: '¿Qué pasa cuando cambie la normativa? ¿Recibo la versión actualizada?', a: 'Sí: el acceso es de por vida y las actualizaciones van incluidas. Cuando cambie algo relevante regeneramos el documento y lo tienes en tu dashboard, con el historial de cambios de cada versión a la vista. Y hay dos redes más: los datos normativos nunca están dentro de una fórmula, sino en celdas editables con su nota y su fecha, así que puedes actualizarlos tú el mismo día; y el manual incluye una hoja de estado normativo y un capítulo que enseña a comprobar por tu cuenta si una norma sigue vigente en su fuente oficial y qué convenio te aplica en el registro público de convenios. Hay cosas ya anunciadas y sin publicar —el reglamento del registro de jornada, entre otras— y esas entran en la próxima versión cuando salgan.' },
    { q: '¿Los siete Excel funcionan en Google Sheets y en Numbers?', a: 'Sí, y en Microsoft Excel y LibreOffice. Están construidos a propósito sin las funciones que rompen la compatibilidad entre programas, y guardan dentro del fichero los valores ya calculados, así que también se leen bien en el móvil y en visores que no recalculan. Las casillas editables van marcadas en verde y las hojas llevan una protección suave que se quita en un clic si quieres reorganizarlo todo a tu manera.' },
    { q: '¿Sirve para un local pequeño o está pensado para cadenas?', a: 'Está escrito para quien dirige un local o un turno, no para un departamento de operaciones. Los problemas estructurales de un independiente y de un grupo son los mismos —cuadrar personas y demanda, controlar caja y coste, sostener el estándar, cumplir la ley—; lo que cambia es la escala y la profundidad de los sistemas, y eso se dice sin fingir lo contrario: cada capítulo indica qué es imprescindible en un local de una decena de personas y qué solo tiene sentido cuando hay varios centros. Las herramientas están dimensionadas para una plantilla pequeña y admiten crecer sin rehacerlas.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'Deja de Apagar Fuegos y Empieza a Dirigir',
    subtitle: 'El criterio, las herramientas y los casos resueltos para llevar el restaurante con los números y la ley de tu lado.',
    items: [
      'Manual completo PDF + DOCX (20 capítulos, 77 páginas)',
      '7 herramientas Excel con fórmulas vivas',
      'Cuadro de mando semanal con prime cost y KPI operativos',
      'Calendario de cumplimiento legal con topes de jornada, permisos y régimen disciplinario',
      'Matriz de polivalencia, scorecard de selección, quejas y reseñas y auditoría de servicio',
      'Bonus: 12 situaciones resueltas (28 páginas)',
    ],
    ctaLabel: 'SÍ, QUIERO EL MANUAL — 55 EUR',
  },

  stickyLabel: 'MANUAL DEL MANAGER DE RESTAURANTE — 55 EUR',

  footerLinks: [
    { label: 'Kit Gestión de Personal', href: '/kit-gestion-personal' },
    { label: 'Kit de Tareas Recurrentes', href: '/kit-tareas' },
    { label: 'Pack Plantillas APPCC', href: '/pack-appcc' },
    { label: 'Guía Food Cost + Ingeniería de Menú', href: '/guia-food-cost-ingenieria-menu' },
    { label: 'IA para Director de Operaciones', href: '/usos/rol/director-operaciones-grupo-restauracion' },
    { label: 'IA para Gerente de Restaurante', href: '/usos/rol/gerente-restaurante' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Versión 1.0 · septiembre 2026',

  alreadyBought: {
    product: 'manual-manager-restaurante',
    label: '¿Ya compraste el manual? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Manual del Manager de Restaurante',
    productDescription: 'Manual operativo de 20 capítulos para quien ya dirige un restaurante o un turno: operación del día, personas y jornada, números del turno, servicio y cumplimiento legal con cada norma citada y fechada. Incluye 7 herramientas Excel con fórmulas vivas y un bonus de 12 situaciones resueltas.',
    price: '55.00',
    priceValidUntil: '2026-12-31',
    faqs: [
      { q: '¿Qué hace exactamente el manager (gerente/encargado) de un restaurante?', a: 'Responde de que el servicio salga y de que el negocio aguante: operación del día, cuadrante y horas, contratación y formación, caja y compras, quejas y cumplimiento legal. En Hispanoamérica el mismo puesto se llama a menudo administrador.' },
      { q: '¿Cuáles son los rangos en un restaurante?', a: 'El convenio estatal de hostelería clasifica por áreas funcionales y grupos profesionales, no por títulos de puesto. «Encargado», «director» o «administrador» son denominaciones de uso interno, no categorías del convenio.' },
      { q: '¿Qué debe contener un manual de operaciones?', a: 'Operación del día, personas, números, servicio y cumplimiento legal, y cada procedimiento con responsable, herramienta de registro y fecha de revisión. Un manual sin dueño y sin revisión no se aplica.' },
      { q: '¿Cuándo me tienen que entregar el cuadrante de trabajo?', a: 'La distribución irregular de la jornada exige un preaviso mínimo de cinco días (art. 34.2 del Estatuto de los Trabajadores) y el calendario laboral anual se expone en el centro. El registro de jornada es otro documento: diario y conservado cuatro años.' },
      { q: '¿Este manual sirve si mi restaurante está fuera de España?', a: 'El bloque normativo está escrito con la ley española y sus artículos citados. El método, los protocolos y las siete herramientas viajan: los parámetros legales viven en casillas editables para sustituirlos por los de cada país, y la adaptación a la normativa de tu país se puede contratar como servicio.' },
      { q: '¿Necesito el Kit de Gestión de Personal o el Kit de Tareas si compro este manual?', a: 'No. Los kits son las plantillas de ejecución; el manual es el criterio y la decisión, y trae sus siete herramientas propias. El capítulo 1 dice qué incluye el pack y qué vive en los otros productos.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Manual del Manager de Restaurante', item: 'https://aichef.pro/manual-manager-restaurante' },
    ],
  },
};

export default data;
