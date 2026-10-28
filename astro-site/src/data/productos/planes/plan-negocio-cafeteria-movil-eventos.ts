// astro-site/src/data/productos/planes/plan-negocio-cafeteria-movil-eventos.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (octubre 2026), 45 €.
// Landing NATIVA. Molde: plan-negocio-finca-eventos-bodas.ts (con los arreglos de la pizzería). Fuentes:
//   scripts/productos-digitales/plan-cafeteria-movil/{SPEC.md (D1, D10-D12, D16), F1-research-cafeteria-movil.md (§0, §6, §8)}.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Cafetería Móvil para Eventos» (H1, schema.productName, products-catalog,
//    tarjeta del hub y breadcrumb). Descriptor SEO: «barra de café de especialidad para bodas, empresas y ferias».
//  · SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials` (producto recién nacido; la clave
//    `testimonials` se OMITE por completo: PlanNegocioLandingPage pinta marquee con 5 estrellas si es un objeto).
//  · Nunca «verificado contra el BOE», «quedarás legal», promesas de rentabilidad ni «España 2026» como sello.
//    Lo legal que se afirma es solo lo de SPEC D10-D11; el resto, «compruébalo con tu ayuntamiento / comunidad / asesoría».
//    Prohibidos (research §8): «sin licencias», «vaso compostable = sin plástico», «enchufa en cualquier finca», «desde 3.000 €»,
//    «carné de manipulador», «freelance», alcohol en la carta, venta en la calle como línea del plan.
//  · Cifras en la landing: SOLO las estables (6 entregables, 80 tareas en 6 fases, 9 hojas, 10 secciones, 4 hojas de la
//    calculadora, 21 países) y las 3 configuraciones de inversión de la FAQ (orientativas, del Word §5). Nada de DSCR,
//    payback, saldos, ventas ni neto.
//  · MODELO: barra de café de especialidad para EVENTOS CONTRATADOS (bodas, empresa, ferias como jornada con canon); la
//    venta en la calle es el Plan Food Truck. Sin alcohol: la coctelería es otro plan.
//  · CRIPTO: nada que tocar (PlanNegocioLandingPage monta las puertas si cryptoEnabledFor('plan-negocio-cafeteria-movil-eventos')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ furgoneta de café de especialidad montada para un evento
//   barra ....... barista preparando café en la barra de una boda
//   empresa ..... barra de café en un evento de empresa
//   feria ....... puesto de café en una feria
//   montaje ..... montaje de la barra y la máquina de espresso antes del evento
//   equipo ...... equipo de baristas de la cafetería móvil
//   plan ........ plan de negocio y hojas de cálculo sobre una mesa
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 9 FAQ (research §0 y §6 + SPEC D10, D11, D16). Una sola fuente: el acordeón y el FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Cuánto cobra una barra de café para eventos: por invitado o por evento?',
    a: 'El mercado cobra por evento y con un mínimo (una tarifa por unas horas de servicio y hasta cierto número de invitados), más extras como horas adicionales y desplazamiento. Casi nadie publica precio por invitado y hora, y ahí está el hueco. La calculadora del plan te da las dos lecturas: calcula la logística según los invitados y las horas (baristas, máquinas, café, leche, vasos y toma eléctrica), suma el coste directo y te devuelve el precio por invitado con su equivalente por hora y por taza, con el margen que tú fijes para particulares, empresas y ferias. Así presupuestas con números y puedes explicar al cliente por qué hay un mínimo.',
  },
  {
    q: '¿Qué toma eléctrica necesito: un enchufe de 16 A o un generador?',
    a: 'Es lo que decide el soporte de tu negocio. Una cafetera de dos grupos consume entre 2,4 y 4,5 kW y un enchufe de 16 A da unos 3,7 kW. Por eso, con un enchufe normal solo cabe una máquina de hasta 3,5 kW; si no, hace falta una toma dedicada, un generador inverter o baterías de litio (silenciosas, útiles en bodas). No se puede dar por hecho que cualquier finca tenga enchufe. El plan trae la tabla de escalado con la potencia que pide cada tamaño de evento, y el modelo de contrato incluye que el cliente confirme la toma por escrito.',
  },
  {
    q: '¿Es lo mismo una feria que un evento contratado? ¿Y la venta ambulante?',
    a: 'No. Una barra contratada en una finca, un hotel o una oficina es un servicio en recinto privado. La venta al público en mercados, ferias o vía pública es venta no sedentaria: pide autorización municipal por emplazamiento (RD 199/2010) y el organizador suele cobrar un canon. Por eso el plan trata las ferias como jornadas de evento con canon y una previsión de la jornada (tazas por ticket, menos canon y coste), y deja la venta en la calle al Plan Food Truck. Qué te exige cada ayuntamiento y cada organizador, compruébalo antes de reservar plaza.',
  },
  {
    q: '¿Necesito comida testigo si solo sirvo café?',
    a: 'Según nuestra lectura de la norma (RD 1086/2020), un espresso o un latte no es una «elaboración culinaria», y tampoco la bollería de obrador que se sirve tal cual, así que la comida testigo no afectaría a las bebidas. Es una interpretación nuestra, sin criterio oficial: confírmala con tu autoridad sanitaria autonómica. Cambia si añades salado (sándwiches, tostas, quiches): entonces guardas una ración de al menos 100 g, 7 días, en cada evento. El plan y el checklist lo explican y te dicen qué preguntar en tu comunidad.',
  },
  {
    q: '¿Sirven los vasos compostables? ¿Qué dice la Ley 7/2022?',
    a: 'Cuidado con el «compostable»: un vaso de papel con forro de PE o PLA cuenta como plástico a efectos de la Ley 7/2022 (arts. 2.aa y 55.2), y por cada vaso de plástico de un solo uso hay que cobrar un precio aparte, visible en el ticket. Pajitas y agitadores de plástico están prohibidos, y en eventos festivos el promotor tiene que ofrecer alternativas reutilizables (RD 1055/2022). El plan lo resuelve así: loza en bodas y empresa, que además se ve mejor, y vaso de un solo uso con precio aparte solo en la venta directa. Cómo lo aplica tu ayuntamiento, confírmalo allí.',
  },
  {
    q: '¿Cuánto cuesta montar una cafetería móvil para eventos?',
    a: 'Depende de la configuración. El plan compara tres: la mínima (barra-carro, cafetera de dos grupos o reacondicionada, un molino y menaje, con vehículo propio y sin generador) ronda los 12.000-15.000 € y sirve para probar con empresas y fincas con toma de 16 A; la del caso (furgoneta, barra-carro y generador) ronda los 42.000 € de equipo y puesta en marcha; y la de imagen (Ape o remolque homologado más el vehículo de traslado) va de unos 55.000 a 65.000 €. Son cifras orientativas del plan, no un presupuesto: el Excel tiene la inversión por partidas, editable, y el fondo de maniobra y el IVA de la inversión aparte.',
  },
  {
    q: '¿Cuánta señal pido y qué pasa si el cliente cancela?',
    a: 'El plan propone un cobro por canal: en particulares, una señal a cuenta del precio al firmar y el resto antes del evento; en empresas, señal y resto contra factura; en ferias, cobro en el acto. La cancelación va por tramos proporcionados («de X a menos de Y» días) y recíprocos: si cancela el cliente, retienes un porcentaje creciente menos los costes que te ahorras, y si cancelas tú, devuelves lo cobrado y asumes lo del mismo tramo. La calculadora y el modelo de contrato usan los mismos porcentajes y plazos, que son ejemplos para adaptar. Son plantillas orientativas: revísalas con tu asesor o abogado antes de firmar con un cliente.',
  },
  {
    q: '¿Es rentable una cafetería móvil para eventos?',
    a: 'No te prometemos rentabilidad: depende de tu zona, de tu captación y de cuántos eventos cierres al año. Lo que sí hace el plan es ponerte la cuenta delante con honestidad: eventos al año por invitados por euros por invitado, con el personal como partida grande, tres escenarios (el pesimista incluido), el punto de equilibrio expresado en eventos y la tesorería mes a mes con la estacionalidad de bodas, empresa y ferias. Cambias un supuesto y todo se recalcula.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Cafetería Móvil para Eventos» recibes la Guía de Equivalencias para tu país, con 21 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, el «camarero» es «mesero» en México y Colombia y «mozo» en Argentina, la «nata» es «crema de leche» o «crema para batir», la «bollería» son «facturas» en Argentina y «pan dulce» en México, y la «nevera» es «heladera» en Argentina y «refrigerador» en México. Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-cafeteria-movil-eventos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA_MOVIL',

  seo: {
    title: 'Plan de Negocio Cafetería Móvil para Eventos | Excel y Word',
    description:
      'Plan de negocio de cafetería móvil para eventos: barra de café de especialidad para bodas, empresas y ferias. Plan financiero en Excel de 9 hojas, plan en Word, checklist de 80 tareas, calculadora de precio por invitado y contrato. 45 €, pago único.',
    keywords:
      'plan de negocio cafetería móvil para eventos, cafetería móvil, carrito de café, coffee truck, barra de café para eventos, café para bodas, barista para eventos, cómo montar una cafetería móvil, plan financiero cafetería móvil excel, contrato barra de café eventos, AI Chef Pro',
    // No existe og-plan-negocio-cafeteria-movil-eventos.jpg: se usa la imagen del hero de la landing.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Cafetería Móvil para Eventos',
    productDescription:
      'Plan de negocio para montar una cafetería móvil para eventos: una barra de café de especialidad para bodas, empresas y ferias. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 80 tareas en 6 fases, una calculadora de escandallo y presupuesto por evento (escandallo de bebidas, logística según los invitados, precio por invitado, cobro y cancelación por tramos; con 3 ejemplos), un modelo de contrato de servicio (particulares y anexo para empresas y organizadores de ferias) y la Guía de Equivalencias para Latinoamérica. No es un curso ni asesoría legal, y no promete rentabilidad.',
    price: '45.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Cafetería Móvil para Eventos',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-empresa.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-feria.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-feria.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-equipo.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-movil-empresa.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-equipo.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-barra.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-cafeteria-movil-hero.jpg',
  },

  hero: {
    badge: 'Para montar tu barra de café para eventos con las cuentas claras',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Cafetería Móvil para Eventos',
    titleSubtitle: 'Barra de café de especialidad para bodas, empresas y ferias',
    description:
      'El plan para montar una cafetería móvil que sirve café de especialidad en bodas, eventos de empresa y ferias: el precio por invitado, la toma eléctrica, el vaso y la diferencia entre un evento contratado y la venta ambulante. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones, checklist de apertura de 80 tareas, calculadora de escandallo y presupuesto, y modelo de contrato.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Calculadora de escandallo y presupuesto: coste de cada bebida, logística según los invitados y precio por invitado',
      'Modelo de contrato de servicio: particulares, empresas y ferias, con cobro y cancelación por tramos',
      'Plan de negocio en Word (10 secciones) y checklist de apertura de 80 tareas en 6 fases',
      'Eventos contratados y ferias con canon: sin venta en la calle ni alcohol en la carta',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      'Es el plan de un negocio de café para eventos: sus números, sus trámites y su logística. No es un curso de barista ni asesoría legal, y no sustituye a tu asesoría ni a tu abogado: la plantilla de contrato es orientativa.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias los eventos al año, los invitados o el precio por invitado y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Las partidas de una cafetería móvil: furgoneta con rotulación, barra-carro, cafetera, molinos, energía, agua, frío, menaje y loza, marca y lanzamiento, más el fondo de maniobra y el IVA de la inversión. Todo editable, con tres configuraciones comparadas en el Word.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos eventos al año necesitas para cubrir costes y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo de reservas. El personal es la partida grande, y el plan te lo pone delante.' },
      { icon: 'CalendarRange', title: 'Tesorería Mes a Mes y Temporada', desc: 'La estacionalidad de bodas, empresa y ferias, con sus meses fuertes y sus meses flojos, y una rampa de captación realista. Ves la caja mes a mes y la liquidación del IVA.' },
      { icon: 'Calculator', title: 'Calculadora de Escandallo y Presupuesto (4 hojas)', desc: 'Escandallo de tus bebidas (coste, food cost y margen), logística según invitados y horas (baristas, máquinas, café, leche, vasos y toma eléctrica), precio por invitado con IVA, cobro y cancelación por tramos. Con 3 ejemplos calculados: boda, evento de empresa y feria.' },
      { icon: 'Truck', title: 'Electricidad, Agua y Vaso Resueltos', desc: 'La tabla de escalado con la potencia que pide cada evento, cuándo basta un enchufe de 16 A y cuándo hace falta generador o baterías, el agua del depósito y el vaso ante la Ley 7/2022. Lo que casi nadie explica en español.' },
      { icon: 'ScrollText', title: 'Modelo de Contrato de Servicio', desc: 'Plantilla editable y orientativa (revísala con tu abogado): contrato para particulares y anexo para empresas y organizadores de ferias, con la toma eléctrica por escrito, alérgenos, señal, cancelación proporcionada y recíproca, plan B de lluvia y fuerza mayor.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con las tres configuraciones de inversión y un evento tipo.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución; vehículo y sanidad; equipo y proveedores; personal y formación; marca y captación; y primer evento y primeros 90 días. Con responsable, plazo y nota en cada tarea.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de cafetería. Es el plan de una barra de café que va a donde está el evento, con su logística, su electricidad y su contrato.',
    reasons: [
      { icon: 'Users', title: 'Un Negocio de Manos y Kilómetros', desc: 'Una taza cuesta poco; lo que pesa es el personal y el tiempo de carga, viaje, montaje y limpieza de cada servicio. El plan lo pone en el Excel, con el personal como partida grande, para que no presupuestes dos horas de servicio como si fueran dos horas de trabajo.' },
      { icon: 'Truck', title: 'La Electricidad Decide el Soporte', desc: 'Una cafetera de dos grupos no cabe en cualquier enchufe. El plan te dice cuándo basta una toma de 16 A y cuándo necesitas generador o baterías, y el contrato pide la toma por escrito antes del evento.' },
      { icon: 'ShieldCheck', title: 'Evento Contratado, Feria y Vaso, Bien Separados', desc: 'Servir en un recinto privado no es vender en la calle: ni los permisos ni el canon son los mismos. Y el vaso «compostable» también cuenta como plástico para la Ley 7/2022. El plan lo ordena y te dice qué comprobar en tu ayuntamiento.' },
      { icon: 'Scale', title: 'Precio por Invitado con Contrato Equilibrado', desc: 'El mercado cobra por evento y con mínimo; tú puedes explicar el porqué con números. Señal y cancelación proporcionales y recíprocas, como pide la ley de consumidores, en una plantilla orientativa para adaptar con tu abogado.' },
    ],
    compatLabel: 'Compatible con cualquier software ofimático:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Word' },
      { label: 'Google Sheets' },
      { label: 'Google Docs' },
      { label: 'LibreOffice' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha acompañado a emprendedores y a empresas de hostelería en España, combinando experiencia operativa con análisis financiero para que cada decisión de inversión se tome con las cuentas delante.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años']

  bonus: {
    subtitle:
      'Además del plan financiero, el plan en Word, el checklist, la calculadora y el contrato, te llevas un extra — valorado en €15',
    items: [
      {
        icon: 'Globe',
        label: 'BONUS',
        title: 'Guía de Equivalencias para tu país',
        value: '€15',
        desc: 'Los términos de tu producto dichos país por país en 21 países, más una ficha de una página por país con impuestos, sanidad, normas laborales, licencias y unidades.',
        image: '/lovable-uploads/ai-gallery/es-guia-equivalencias.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  guarantee: {
    text:
      'Si el plan de negocio no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: FAQS,

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Cafetería Móvil',
    subtitle:
      'Antes de comprar la furgoneta y la cafetera, ten las cuentas, la logística, el contrato y el calendario de tu barra de café sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes con la estacionalidad de bodas, empresa y ferias',
      'Tres escenarios financieros (pesimista, realista y optimista)',
      'Calculadora de escandallo y presupuesto con 3 ejemplos',
      'Modelo de contrato de servicio para particulares, empresas y ferias',
      'Checklist de apertura con 80 tareas en 6 fases',
      'Plan de negocio en Word con 10 secciones',
      'BONUS: Guía de Equivalencias para tu país (€15)',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  pricing: {
    price: '€45',
    heroNote: 'Pago único. Acceso inmediato y actualizaciones incluidas',
    buyBoxNote: 'Pago único · Acceso inmediato · 30 días de garantía',
    bonusTotalLabel: 'El pack completo, en un solo pago',
  },

  stickyLabel: 'PLAN CAFETERÍA MÓVIL — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-cafeteria', label: 'Kit de Tareas Recurrentes: Cafetería' },
    { href: '/plan-negocio-cafeteria', label: 'Plan de Negocio Cafetería' },
    { href: '/plan-negocio-cocteleria-eventos', label: 'Plan de Negocio Coctelería para Eventos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · octubre 2026',

  alreadyBought: {
    product: 'plan-negocio-cafeteria-movil-eventos',
    label: '¿Ya compraste el Plan de Negocio: Cafetería Móvil para Eventos? Vuelve a entrar al dashboard',
  },
};

export default data;
