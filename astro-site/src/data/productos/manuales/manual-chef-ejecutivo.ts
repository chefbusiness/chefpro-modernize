// manual-chef-ejecutivo.ts — LÍNEA MANUALES OPERATIVOS, producto 47 (2026-09-06).
//
// Segundo producto de la línea «Manuales operativos» (hermano del Manual del Manager de
// Restaurante) y tercera landing NATIVA en Astro. Reutiliza el contrato `GuiaData` y el
// template `GuiaLandingPage.astro` (D29 de la SPEC): `why.titlePre` / `why.titleGold`
// convierten el único H2 que decía «Guía» en «Manual».
//
// Fuente del copy: la SPEC firmada (scripts/productos-digitales/manual-chef-ejecutivo-SPEC.md,
// §0, §1, §4 y §11) y el research consolidado
// (scripts/productos-digitales/auditorias/manual-chef-ejecutivo-RESEARCH-2026-09-06.md,
// §5.3 vocabulario, §11 copy, §12 FAQ, §13 canales).
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  - D1: PRECIO 65 €. NUNCA se menciona el precio del Manual del Manager ni se compara
//    con él; «los dos manuales juntos» son 120 €. El precio del hermano es una cadena
//    PROHIBIDA en cualquier pieza de este producto (lista negra, SPEC §8), y por eso no
//    aparece escrito ni siquiera en este comentario: un grep de auditoría no distingue.
//  - D2: producto nuevo → SIN `priceOld`, SIN `discountBadge`, SIN `aggregateRating` y con
//    `testimonials.items: []` (no ha vendido una unidad: no hay reseñas que enseñar).
//  - D26: hero, hub, Stripe, changelog y asuntos de email lideran con ENTREGABLES y
//    BENEFICIO, sin siglas españolas y sin la verificación oficial como gancho. La
//    mención al boletín oficial aparece UNA sola vez en toda la landing, dentro de la
//    FAQ «¿sirve fuera de España?», acotada al caso español y ofreciendo la adaptación
//    a la normativa de cada país como servicio de consultoría.
//  - §5.3: vocabulario ES con equivalencia LATAM en la PRIMERA mención — chef ejecutivo
//    (chef corporativo), jefe de cocina (chef de cocina), partida (estación), ficha
//    técnica (receta estándar), merma (desperdicio), escandallo (costeo).
//  - D9: término único «partida»; «(estación)» sólo en la primera mención.
//  - D6: «una cocina, con las herramientas para comparar varias» — el hero lidera con
//    quien dirige UNA cocina y dice que sirve al chef corporativo.
//  - D10: cero benchmarks de merma, de tiempo de pase y de horas de formación: se miden,
//    no se citan. Cero cifras sin fuente primaria; el único ancla externa es el coste
//    anual del software de gestión de cocina comparable (tSpoonLab, precio oficial
//    consultado el 2026-09-06).
//  - D3: son SIETE libros de Excel, no ocho (el research proponía ocho).
//  - `75` y `25` son TOKENS de páginas: se sustituyen por las MEDIDAS con PyMuPDF cuando
//    el PDF esté construido (D25). NO publicar con la cifra provisional.
import type { GuiaData } from '../guias/types';

const data: GuiaData = {
  slug: 'manual-chef-ejecutivo',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_MANUAL_CHEF_EJECUTIVO',

  seo: {
    title: 'Manual del Chef Ejecutivo | Brigada, Producción y Carta',
    description: 'Para quien ya dirige una cocina: brigada y partidas, planificación de producción, fichas técnicas, KPI de cocina y alérgenos. 20 capítulos y 7 Excel.',
    keywords: 'manual del chef ejecutivo, chef ejecutivo, jefe de cocina, brigada de cocina, organigrama de cocina, ficha técnica de cocina, receta estándar, sous chef, funciones del jefe de cocina, planificación de producción en cocina, KPI de cocina, dirección de cocina, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-manual-chef-ejecutivo.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'Para quien ya dirige la cocina: criterio para decidir, no otro recetario',
    titlePre: 'El Manual del ',
    titleGold: 'Chef Ejecutivo',
    subtitleLine: 'Brigada, producción, estándares y seguridad alimentaria: el criterio de quien dirige la cocina, no de quien la cocina',
    description: 'El Manager lleva el negocio. El Chef Ejecutivo lleva la cocina. Si diriges las dos cosas, necesitas los dos. Éste es el de la cocina, y empieza por decir lo que no es: no te enseña a cocinar. Te da el sistema para que tu cocina funcione igual estés tú o no — quién hace qué en cada partida (estación), cuánto se produce cada día, cómo se estandariza un plato con una ficha técnica (receta estándar) que alguien sigue de verdad, y de qué respondes tú ante una inspección. Está escrito para el chef ejecutivo (chef corporativo, cuando dirige varias cocinas) y para el jefe de cocina (chef de cocina) que ya lleva el mando de una: una cocina, con las herramientas para comparar varias.',
    checkItems: [
      'Manual completo PDF + DOCX editable (20 capítulos, 96 páginas)',
      '7 herramientas Excel con fórmulas vivas: cuadro de mando de cocina, planificación de producción semanal, ficha técnica de proceso, brigada con puestos y evaluación, desarrollo de carta y control de calidad, banquetes y comidas testigo, y auditoría interna de cocina',
      'Temperaturas, alérgenos, vida útil, comidas testigo y prevención de riesgos en cocina: cada norma con su artículo, su enlace y la fecha en que se comprobó, el 6 de septiembre de 2026',
      'El marco legal explicado es el español; todos los parámetros viven en casillas editables para adaptarlos a tu país',
      'Bonus: 12 situaciones resueltas en cocina (34 páginas)',
    ],
    ctaLabel: 'COMPRAR MANUAL — 65 EUR',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    price: '65 EUR',
    heroNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    buyBoxNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    bonusTotalLabel: 'Incluido en el precio: el manual, las 7 herramientas Excel y el bonus de 12 situaciones resueltas en cocina',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/manual-chef-hero.jpg',
      '/lovable-uploads/ai-gallery/manual-chef-brigada.jpg',
      '/lovable-uploads/ai-gallery/manual-chef-pase.jpg',
      '/lovable-uploads/ai-gallery/manual-chef-produccion.jpg',
      '/lovable-uploads/ai-gallery/manual-chef-oficina.jpg',
      '/lovable-uploads/ai-gallery/manual-chef-formacion.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/manual-chef-oficina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/manual-chef-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/manual-chef-pase.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 7 Herramientas Excel + 1 Bonus',
    subtitle: 'Criterio, no teoría. Cada capítulo se apoya en una de las siete herramientas Excel del pack y sus tablas salen de las celdas de esos ficheros o de la norma citada, nunca de un ejemplo inventado. Escrito por un chef y consultor gastronómico que lleva desde 2010 dentro de cocinas reales.',
    chapters: [
      { icon: 'ChefHat', num: '01', title: 'Qué Es Exactamente un Chef Ejecutivo (y para Quién Es Este Manual)', desc: 'Dónde acaba el jefe de cocina y dónde empieza el chef ejecutivo, con el mapa problema → capítulo → herramienta, la cadencia de uso de los siete libros y qué no vas a encontrar aquí.' },
      { icon: 'Users', num: '02', title: 'La Brigada Real: los 10 Puestos del Convenio y el Organigrama Que Sí Tienes', desc: 'Los diez puestos de cocina con sus funciones escritas en el convenio, y por qué una brigada de seis personas no está «mal»: cambia quién acumula funciones, no el sistema.' },
      { icon: 'ScrollText', num: '03', title: 'Lo Que tu Convenio Dice de la Cocina (y No del Resto del Restaurante)', desc: 'Salarios en bruto anual con la etiqueta de cada tabla, movilidad entre partidas, turnos y descansos: lo que aplica a cocina, separado de lo que aplica a sala.' },
      { icon: 'Megaphone', num: '04', title: 'Mandar en una Cocina sin Gritar', desc: 'Los tres niveles de delegación del convenio llevados al pase, qué se decide en marcha y qué se decide fuera del servicio, y cómo se sostiene una orden sin levantar la voz.' },
      { icon: 'FileText', num: '05', title: 'La Ficha Técnica de Proceso: Que el Plato Salga Igual lo Haga Quien lo Haga', desc: 'Pasos, técnica, tiempos, punto, temperatura de servicio, montaje, alérgenos de proceso, conservación y versión — con el coste copiado de tu escandallo (costeo), no recalculado aquí.' },
      { icon: 'Target', num: '06', title: 'Estandarizar de Verdad: por Qué la Ficha Existe y Nadie la Sigue', desc: 'Las cinco razones por las que una ficha se queda en el cajón y qué se cambia en cada una: dónde vive, quién la actualiza, cómo se enseña y cómo se comprueba en el pase.' },
      { icon: 'ClipboardList', num: '07', title: 'Mise en Place y Planificación de Producción', desc: 'Cuánto producir hoy en cada partida a partir de cubiertos, mix y stock elaborado, con la lista de producción diaria imprimible y la alerta de sobreproducción.' },
      { icon: 'ConciergeBell', num: '08', title: 'El Pase: Protocolo, No Cultura', desc: 'Cantar, marcar, montar y entregar como protocolo escrito, los tiempos medidos con tu propia herramienta y el epígrafe del plato que sale por la puerta en delivery.' },
      { icon: 'BarChart3', num: '09', title: 'Los KPI Que Son de Cocina (y los Que No)', desc: 'Siete indicadores de cocina con su fórmula, su unidad y su error típico, y la frontera con los financieros: qué mide el chef y qué se mira en el cuadro del negocio.' },
      { icon: 'TrendingDown', num: '10', title: 'La Merma de tu Partida', desc: 'Merma (desperdicio, cuando es comida tirada) agregada por partida contra la producción del día: qué la dispara, cómo se aísla y qué conversación toca cuando se repite.' },
      { icon: 'Truck', num: '11', title: 'Compras y Especificaciones desde la Cocina', desc: 'Escribir la especificación de un producto para que llegue lo que pediste, qué se comprueba en recepción y cómo se defiende un cambio de proveedor con datos.' },
      { icon: 'UtensilsCrossed', num: '12', title: 'Desarrollo de Carta y Menús de Temporada con Criterio de Coste', desc: 'El calendario de probar, costear, documentar, formar y lanzar, con la alerta del plato que lleva semanas en prueba sin ficha cerrada y sin nadie formado.' },
      { icon: 'Thermometer', num: '13', title: 'Seguridad Alimentaria: de lo Que Respondes Tú, No el Propietario', desc: 'Las cinco temperaturas que gobiernan una cocina y el enfriamiento rápido, con el epígrafe de qué se tira y qué no cuando se cae el frío, y qué se apunta.' },
      { icon: 'ShieldAlert', num: '14', title: 'Alérgenos desde Dentro de la Cocina', desc: 'Contacto y traza en la elaboración, utensilio y superficie compartidos, sustitución posible y el pase: lo que pasa dentro, no la declaración de la carta.' },
      { icon: 'Refrigerator', num: '15', title: 'Vida Útil, Envasado al Vacío y lo Que la Ley NO Dice', desc: 'No existe una cifra legal de días: cuándo hace falta un estudio de vida útil, las tres fechas al congelar y qué obliga de verdad el envasado al vacío.' },
      { icon: 'PartyPopper', num: '16', title: 'Comidas Testigo y Banquetes (y Qué Se Hace con el Excedente)', desc: 'Cuándo se dispara la obligación de guardar comida testigo, cuánto y cómo, la producción de un evento por partidas y qué excedente de cocina caliente es donable.' },
      { icon: 'ShieldCheck', num: '17', title: 'Prevención de Riesgos en la Cocina: lo Que la Evaluación de Riesgos Convierte en Obligación', desc: 'Cortes, quemaduras, suelos, cargas, temperatura del puesto y equipos de protección: qué obliga la norma, qué lo decide tu evaluación de riesgos y qué es un mito.' },
      { icon: 'GraduationCap', num: '18', title: 'Formar y Evaluar a la Brigada: Cobertura No Es Competencia', desc: 'Que alguien pueda cubrir una partida no significa que la domine: rúbrica de competencias técnicas, prueba práctica y plan de desarrollo con la siguiente partida a aprender.' },
      { icon: 'Shuffle', num: '19', title: 'Cocina, Sala y Dirección: Quién Decide Qué — y Cómo Llevar la Cifra al Gerente', desc: 'La matriz de decisiones que cruzan (la 86, la ficha nueva, la compra fuera de escandallo, la incidencia de alérgeno) y cómo se lleva una propuesta con la cifra de la semana delante.' },
      { icon: 'Building2', num: '20', title: 'Varias Cocinas a la Vez — y los 90 Días Siguientes', desc: 'Los mismos indicadores en seis unidades con su desviación contra el estándar del grupo, la auditoría comparable entre cocinas y trece semanas con responsable y fecha.' },
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
      { icon: 'Target', title: 'Criterio, No un Recetario', desc: 'Recetas y técnicas hay a miles y no es lo que te falta cuando diriges. Lo que falta es el sistema: qué se produce hoy, quién puede hacerlo, cómo se estandariza para que salga igual sin ti delante y qué decisión toca cuando la merma de una partida se dispara tres semanas seguidas.' },
      { icon: 'ScrollText', title: 'Cada Norma con su Artículo y su Fecha', desc: 'Temperaturas, alérgenos, vida útil, comidas testigo y prevención de riesgos: cada afirmación lleva la norma, el artículo y el enlace, y cada celda con dato legal lleva la fecha en que se comprobó, el 6 de septiembre de 2026. Nunca «es obligatorio» a secas.' },
      { icon: 'FileSpreadsheet', title: 'Siete Excel Que de Verdad Calculan', desc: 'No son PDF para rellenar a mano: metes tus datos y calculan. Construidos a propósito sin las funciones que rompen la compatibilidad y sin una sola referencia entre ficheros, así que funcionan igual en Excel, Google Sheets, LibreOffice y Numbers, con los parámetros en casillas editables.' },
      { icon: 'Wallet', title: 'Un Pago Único Frente a una Cuota Anual', desc: 'El software de gestión de cocina comparable se paga por meses: tSpoonLab cuesta 95 € al mes, 1.140 € al año, según su precio oficial consultado el 6 de septiembre de 2026. Este manual es un pago único con acceso de por vida y actualizaciones incluidas.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además del manual PDF + DOCX, recibes 7 herramientas Excel con fórmulas vivas y el bonus de situaciones resueltas en cocina',
    layout: 'split',
    items: [
      { icon: 'BarChart3', label: 'HERRAMIENTA 1', title: 'Cuadro de Mando de Cocina', value: 'Incluido en el pack', desc: 'Cincuenta y dos semanas con merma y producción por partida, tiempos de pase muestreados, incidencias de alérgenos, horas de cocina y cubiertos, una hoja donde cada indicador trae su fórmula y su error típico, y una comparativa entre unidades con desviación y ranking. Los objetivos los pones tú: el semáforo no se enciende hasta que hay uno.', image: '/lovable-uploads/ai-gallery/manual-chef-oficina.jpg' },
      { icon: 'CalendarRange', label: 'HERRAMIENTA 2', title: 'Planificación de Producción Semanal', value: 'Incluido en el pack', desc: 'Previsión de cubiertos, producción por partida hasta ocho partidas, lista de producción diaria imprimible —la que se cuelga en la cocina— y ajuste por desviación, con alerta de sobreproducción cuando la cantidad calculada se dispara sobre el stock elaborado.', image: '/lovable-uploads/ai-gallery/manual-chef-produccion.jpg' },
      { icon: 'FileText', label: 'HERRAMIENTA 3', title: 'Ficha Técnica de Proceso', value: 'Incluido en el pack', desc: 'La plantilla, un ejemplo relleno y el índice de fichas: pasos, técnica, tiempos, punto, temperatura de servicio, montaje, alérgenos de proceso, conservación, vida útil, versión y fecha de revisión. El coste va en casilla verde, copiado de tu escandallo: la ficha dice cómo se hace, no cuánto cuesta.', image: '/lovable-uploads/ai-gallery/manual-chef-pase.jpg' },
      { icon: 'Users', label: 'HERRAMIENTA 4', title: 'Brigada: Puestos y Evaluación', value: 'Incluido en el pack', desc: 'Organigrama por partidas activas, diez fichas de puesto con las funciones literales del convenio y una columna propia para las tuyas, matriz de decisiones entre cocina, sala y dirección, rúbrica de siete competencias técnicas con pesos por puesto, prueba práctica, plan de desarrollo individual e histórico.', image: '/lovable-uploads/ai-gallery/manual-chef-brigada.jpg' },
      { icon: 'UtensilsCrossed', label: 'HERRAMIENTA 5', title: 'Desarrollo de Carta y Control de Calidad', value: 'Incluido en el pack', desc: 'Calendario de temporada con las cinco fases —probar, costear, documentar, formar y lanzar—, registro de pruebas de plato y control de calidad del pase, con alerta cuando un plato lleva demasiados días en prueba sin la ficha cerrada.', image: '/lovable-uploads/ai-gallery/manual-chef-formacion.jpg' },
      { icon: 'ClipboardList', label: 'HERRAMIENTA 6', title: 'Banquetes y Comidas Testigo', value: 'Incluido en el pack', desc: 'Registro de comidas testigo con la alerta que salta cuando el encargo dispara la obligación, la cuenta atrás de conservación, la ubicación y la temperatura; y la producción del banquete con cubiertos, mix, cantidades por partida, timing de pase y personal.', image: '/lovable-uploads/ai-gallery/manual-chef-produccion.jpg' },
      { icon: 'ClipboardCheck', label: 'HERRAMIENTA 7', title: 'Auditoría Interna de Cocina', value: 'Incluido en el pack', desc: 'Alrededor de cincuenta puntos de control —orden y mise en place, aplicación de las fichas, mermas por partida, prevención de riesgos y alérgenos en el pase— con puntuación, resumen por área, histórico, histórico por unidad y una hoja de estado normativo con su fecha de corte. Deja fuera a propósito los registros sanitarios, que tienen su propio pack.', image: '/lovable-uploads/ai-gallery/manual-chef-oficina.jpg' },
      { icon: 'GraduationCap', label: 'BONUS', title: '12 Situaciones Resueltas en Cocina', value: 'Incluido en el pack', desc: 'Doce marrones reales con datos: el jefe de partida que se va a mitad de temporada, la alergia que se declara con el plato ya montado, la inspección en mitad del servicio, el banquete de 120 personas, el pase desbordado un viernes, el plato que sale distinto según el turno, la cámara que se cae un domingo por la noche o el corte con la cortadora. Cada uno con qué NO hacer, protocolo, norma aplicable con su fecha, herramienta usada y el guion de la conversación cuando la hay.', image: '/lovable-uploads/ai-gallery/manual-chef-brigada.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL MANUAL — 65 EUR',
  },

  guarantee: {
    text: 'Si el manual no te sirve para dirigir tu cocina con más criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿En qué se diferencia del Manual del Manager de Restaurante? ¿Necesito los dos?', a: 'Son dos oficios distintos y por eso son dos manuales. El Manager lleva el negocio: sala, caja, contratación, jornada, quejas y el cumplimiento legal transversal. El Chef Ejecutivo lleva la cocina: brigada y partidas, producción, estandarización, seguridad alimentaria, prevención de riesgos de cocina y desarrollo de carta. Si sólo diriges la cocina, con éste basta y no te falta nada. Si diriges las dos cosas —el caso del propietario-chef y el de muchos hoteles pequeños—, necesitas los dos, y cada capítulo de éste dice explícitamente qué se trata aquí y qué vive en el otro para que no leas dos veces lo mismo.' },
    { q: '¿Qué diferencia hay entre un chef ejecutivo y un jefe de cocina, y cuál soy yo?', a: 'Es la pregunta que más se repite y casi nadie la contesta igual. En la práctica: el jefe de cocina (chef de cocina) responde del día a día de una cocina —el pase, la producción, la brigada del turno—, y el chef ejecutivo (chef corporativo, cuando dirige varias cocinas) responde del criterio y del estándar por encima del servicio: la carta, los procesos, los costes, la gente que dirige a la gente y, cuando hay más de un centro, la coherencia entre ellos. En muchas casas la misma persona hace las dos cosas, y el convenio no reparte la plantilla por títulos de puesto sino por áreas y grupos, así que el nombre de tu nómina no decide nada. Este manual está escrito para quien ya dirige, se llame como se llame el puesto.' },
    { q: '¿Sirve si mi cocina es de cuatro o cinco personas?', a: 'Sí, y es donde más rápido se nota, con un matiz que decimos de frente: cada capítulo trae su ejemplo por escala, para brigadas de cuatro a seis personas, de quince a veinticinco y de más de cien (hotel o grupo). El capítulo 2 dice literalmente que una brigada de seis no está «mal» comparada con la clásica de Escoffier: lo que cambia es cuántas funciones acumula cada persona, no el sistema. Las herramientas se dimensionan con una casilla de partidas activas, de tres a ocho, y las hojas se adaptan a lo que pongas ahí.' },
    { q: '¿Sirve para un hotel, un catering de colectividades o un grupo con varias cocinas?', a: 'Sí, y es donde más aporta. El capítulo 20 y dos hojas específicas están hechos para comparar varias cocinas con los mismos indicadores y la misma auditoría puntuada: una cocina, con las herramientas para comparar varias. El capítulo 16 cubre las comidas testigo, que es justo lo que obliga en catering, comedores de empresa y encargos grandes, con su registro, su cuenta atrás y su alerta. Y el capítulo 3 explica qué cambia cuando tienes centros en dos comunidades con convenios provinciales distintos.' },
    { q: 'Todavía no soy chef ejecutivo: dirijo una sola cocina. ¿Me vale igual?', a: 'Vale igual, y de hecho es el lector más frecuente. El manual está escrito para quien ya dirige una cocina, tenga el puesto el nombre que tenga en la nómina. Los capítulos 1, 2 y 20 son además los que explican qué cambia al subir de escalón —más criterio y menos ejecución, más estándar y menos servicio— para quien esté a punto de dar ese paso o acabe de darlo. El bonus cierra con las primeras semanas de un segundo de cocina que asciende.' },
    { q: 'Soy propietario-chef y lo llevo todo yo. ¿Qué me falta con este manual?', a: 'Con éste tienes resuelta la cocina entera: brigada, producción, estándares, seguridad alimentaria, prevención de riesgos y carta. Lo que no cubre, porque es el otro oficio, es la cara de negocio: contratación y jornada, caja y tique, quejas y reclamaciones, reservas y el cumplimiento legal que no es de cocina. Eso vive en el Manual del Manager de Restaurante, y los dos juntos salen por 120 €. Preferimos decirlo así, en dos productos, antes que venderte uno que finja cubrir las dos cosas a medias.' },
    { q: '¿Sirve si mi restaurante está fuera de España?', a: 'Sí, con un matiz que conviene decir claro antes de comprar: el bloque normativo está escrito con la ley española, y sus artículos y enlaces son españoles (en el caso de España, cada norma está verificada contra su publicación en el Boletín Oficial del Estado, el BOE, con la fecha al pie de cada tabla). Lo que viaja es todo lo demás, que es la mayor parte: la dirección de brigada, la ficha técnica de proceso, la planificación de producción, el protocolo del pase, los indicadores de cocina, la evaluación técnica y el desarrollo de carta con método. Las siete herramientas llevan todos los parámetros —temperaturas, plazos, umbrales y objetivos— en casillas editables para que pongas los de tu país, y el vocabulario trae las equivalencias de Hispanoamérica: partida y estación, ficha técnica y receta estándar, escandallo y costeo, merma y desperdicio, ayudante y auxiliar. Y si prefieres que adaptemos el bloque normativo y los parámetros a la legislación de tu país, escríbenos a info@aichef.pro: lo hacemos como servicio de consultoría.' },
    { q: '¿Necesito el Pack APPCC si compro este manual?', a: 'Son cosas distintas y hay que decirlo. El manual da el criterio: de qué respondes tú, qué mira el inspector, cómo se dirige la seguridad alimentaria desde dentro de la cocina y qué temperaturas gobiernan cada proceso. El Pack da los registros diarios que hay que rellenar y firmar. Ni se solapan ni se sustituyen: la auditoría interna de cocina de este manual excluye a propósito la limpieza, las plagas y las temperaturas registradas, y remite al Pack, para que no acabes con dos sistemas que dicen cosas distintas del mismo frigorífico.' },
    { q: '¿Y el Kit de Escandallos o la Guía Food Cost? ¿Se solapan con la ficha técnica?', a: 'No, y la frontera es la misma en los dos casos: el escandallo (costeo) dice cuánto cuesta un plato; la ficha técnica de proceso dice cómo se hace. Por eso la ficha no recalcula ningún coste: trae una casilla verde donde copias el coste por ración que ya salió de tu escandallo, con el enlace al producto que lo calcula. El rendimiento del ingrediente y la merma de cocción, que también son cálculo de coste, viven en la Guía Food Cost. El manual funciona perfectamente sin ellos, con esa casilla en blanco.' },
    { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí, y en Microsoft Excel y LibreOffice. Están construidos a propósito sin las funciones que rompen la compatibilidad entre programas y sin una sola referencia entre ficheros: ningún libro depende de que tengas otro abierto, ni se rompe si renombras una carpeta. Además guardan dentro del fichero los valores ya calculados, así que también se leen bien en el móvil y en visores que no recalculan. Las casillas editables van marcadas en verde y las hojas llevan una protección suave que se quita en un clic.' },
    { q: '¿Qué pasa cuando cambie la normativa? ¿Recibo la versión actualizada?', a: 'Sí: el acceso es de por vida y las actualizaciones van incluidas. Cuando cambie algo relevante regeneramos el documento y lo tienes en tu dashboard, con el historial de cambios de cada versión a la vista. Y hay dos redes más: los datos normativos nunca están dentro de una fórmula, sino en casillas editables con su nota y su fecha, así que puedes actualizarlos tú el mismo día; y la herramienta de auditoría interna de cocina incluye una hoja de estado normativo con fecha de corte y enlace editables, donde ves de un vistazo qué se comprobó y cuándo.' },
    { q: '¿Puedo ver el índice antes de comprar? ¿Y si al final no me sirve?', a: 'El índice completo de los 20 capítulos está aquí arriba, capítulo a capítulo y con lo que resuelve cada uno, y más abajo tienes descritas las siete herramientas Excel y el bonus con su contenido real. Si aun así no te sirve, tienes 30 días de garantía: escribes, te devolvemos el 100% y no hay que dar explicaciones.' },
  ],

  cta: {
    heading: 'Deja de Ser el Único Que Sabe Cómo Se Hace',
    subtitle: 'El criterio, las herramientas y los casos resueltos para que tu cocina salga igual estés tú o no.',
    items: [
      'Manual completo PDF + DOCX (20 capítulos, 96 páginas)',
      '7 herramientas Excel con fórmulas vivas',
      'Cuadro de mando de cocina con merma y producción por partida',
      'Ficha técnica de proceso, planificación de producción y desarrollo de carta',
      'Brigada con fichas de puesto y evaluación técnica, banquetes y auditoría interna',
      'Bonus: 12 situaciones resueltas en cocina (34 páginas)',
    ],
    ctaLabel: 'SÍ, QUIERO EL MANUAL — 65 EUR',
  },

  stickyLabel: 'MANUAL DEL CHEF EJECUTIVO — 65 EUR',

  footerLinks: [
    { label: 'Manual del Manager de Restaurante', href: '/manual-manager-restaurante' },
    { label: 'Pack Plantillas APPCC', href: '/pack-appcc' },
    { label: 'Kit de Escandallos', href: '/kit-escandallos' },
    { label: 'Guía Food Cost + Ingeniería de Menú', href: '/guia-food-cost-ingenieria-menu' },
    { label: 'Kit de Tareas Recurrentes', href: '/kit-tareas' },
    { label: 'Kit de Inventario', href: '/kit-inventario' },
    { label: 'IA para Chef Ejecutivo', href: '/usos/rol/chef-ejecutivo-corporativo' },
    { label: 'IA para Jefe de Cocina', href: '/usos/rol/chef-jefe-cocina' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Versión 1.0 · septiembre 2026',

  alreadyBought: {
    product: 'manual-chef-ejecutivo',
    label: '¿Ya compraste el manual? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Manual del Chef Ejecutivo',
    productDescription: 'Manual operativo de 20 capítulos para quien ya dirige una cocina: brigada y partidas, planificación de producción, fichas técnicas de proceso, indicadores de cocina, seguridad alimentaria, alérgenos, prevención de riesgos y desarrollo de carta, con cada norma citada y fechada. Incluye 7 herramientas Excel con fórmulas vivas y un bonus de 12 situaciones resueltas en cocina.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    faqs: [
      { q: '¿En qué se diferencia del Manual del Manager de Restaurante? ¿Necesito los dos?', a: 'El Manager lleva el negocio: sala, caja, contratación, jornada y cumplimiento legal transversal. El Chef Ejecutivo lleva la cocina: brigada y partidas, producción, estandarización, seguridad alimentaria y carta. Si sólo diriges la cocina, con éste basta; si diriges las dos cosas, necesitas los dos.' },
      { q: '¿Qué diferencia hay entre un chef ejecutivo y un jefe de cocina, y cuál soy yo?', a: 'El jefe de cocina (chef de cocina) responde del día a día de una cocina; el chef ejecutivo (chef corporativo, cuando dirige varias) responde del criterio y del estándar por encima del servicio. El convenio clasifica por áreas y grupos, no por títulos de puesto: el manual sirve a los dos.' },
      { q: '¿Sirve para un hotel, un catering de colectividades o un grupo con varias cocinas?', a: 'Sí. El capítulo 20 y dos hojas específicas comparan varias cocinas con los mismos indicadores y la misma auditoría puntuada, el capítulo 16 cubre las comidas testigo y el capítulo 3 explica qué cambia con centros en comunidades con convenios distintos.' },
      { q: '¿Sirve si mi restaurante está fuera de España?', a: 'El bloque normativo está escrito con la ley española y sus artículos citados. El método, los protocolos y las siete herramientas viajan: los parámetros viven en casillas editables para sustituirlos por los de cada país, y la adaptación a la normativa de tu país se puede contratar como servicio.' },
      { q: '¿Necesito el Pack APPCC si compro este manual?', a: 'Son cosas distintas: el manual da el criterio de seguridad alimentaria desde dentro de la cocina y el Pack da los registros diarios que se rellenan y se firman. La auditoría interna de cocina del manual excluye a propósito limpieza, plagas y temperaturas registradas, y remite al Pack.' },
      { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí, y en Microsoft Excel y LibreOffice. Están construidos sin las funciones que rompen la compatibilidad y sin una sola referencia entre ficheros, y guardan los valores ya calculados dentro del fichero.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Manual del Chef Ejecutivo', item: 'https://aichef.pro/manual-chef-ejecutivo' },
    ],
  },
};

export default data;
