// astro-site/src/data/productos/planes/plan-negocio-finca-eventos-bodas.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (noviembre 2026), 45 €.
// Landing NATIVA. Molde: plan-negocio-heladeria.ts. Fuentes: scripts/productos-digitales/plan-finca-eventos/
//   {SPEC.md (D1, D2, D10, D11, D12), F1-research-finca.md (§0, §1, §5, §6), F2-NOTAS.md}.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Finca de Eventos y Bodas» (H1, schema.productName, products-catalog,
//    tarjeta del hub y breadcrumb).
//  · SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials` (producto recién nacido; la clave
//    `testimonials` se OMITE por completo: PlanNegocioLandingPage pinta marquee con 5 estrellas si es un objeto).
//  · Nunca «verificado contra el BOE», «quedarás legal», promesas de rentabilidad ni «España 2026» como sello.
//    Lo legal que se afirma es solo lo permitido por SPEC D11; el resto, «consúltalo con tu ayuntamiento / comunidad /
//    asesoría». Prohibido: RD 393/2007, «10 % para todo el paquete», «carné de manipulador», canon del 12 % como dato.
//  · Cifras en la landing: SOLO las estables (6 entregables, 84 tareas en 6 fases, 9 hojas, 10 secciones, 4 tipos de
//    evento). Nada de DSCR, payback, saldos, ventas ni neto.
//  · MODELO (D2): finca ARRENDADA con edificaciones existentes + CATERING EXCLUSIVO concesionado que paga canon.
//    La finca no se compra. Catering propio y «solo alquiler» se razonan en el Word, sin Excel.
//  · CRIPTO: nada que tocar (PlanNegocioLandingPage monta las puertas si cryptoEnabledFor('plan-negocio-finca-eventos-bodas')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ finca de eventos con el jardín preparado para una boda
//   cocina ...... office del catering de una finca de eventos
//   banquete .... banquete de boda montado en el salón de la finca
//   ceremonia ... ceremonia de boda al aire libre en el jardín de la finca
//   barra ....... barra de bebidas de un evento en la finca
//   montaje ..... montaje de mesas y carpa para un evento de empresa
//   plan ........ plan de negocio y hojas de cálculo sobre una mesa de la finca
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 9 FAQ (research §6 + SPEC D11). Una sola fuente: el acordeón de la página y el FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Qué licencias necesito para celebrar bodas en una finca rústica?',
    a: 'Es lo primero que hay que resolver, porque en suelo rústico celebrar eventos no es un uso ordinario: suele pedir una autorización previa a la licencia municipal, que cambia según la comunidad autónoma y tiene plazos largos. El plan lo explica con ejemplos de Madrid (calificación urbanística y edificaciones existentes), Andalucía (actuación extraordinaria con prestación compensatoria), Cataluña (masías catalogadas) y la Comunidad Valenciana (declaración de interés comunitario). En el resto de comunidades te damos el método: pregunta en urbanismo qué figura usa la tuya. Por eso el contrato de arrendamiento lleva condición suspensiva de licencias y no se confirma ninguna fecha sin licencia: antes de tenerla, solo reservas condicionadas a ella, con devolución íntegra si no llega. Qué te piden exactamente en tu municipio, compruébalo en tu ayuntamiento y con tu asesoría antes de firmar.',
  },
  {
    q: '¿Cuánto cuesta montar una finca para bodas y eventos?',
    a: 'Depende de las edificaciones que tenga la finca, de la obra que necesiten y de los trámites urbanísticos de tu comunidad. El plan parte de una finca arrendada con edificaciones ya existentes y no cuenta con comprarla: la compra de la finca multiplicaría la inversión y cambiaría el negocio por completo. El Excel trae la inversión inicial por partidas (proyecto, calificación urbanística, licencia, tasas, obra, carpa, mobiliario, imprevistos…), el fondo de maniobra y el IVA de la inversión, todo editable, para que veas cuánto necesitas tú con tu finca.',
  },
  {
    q: '¿Es rentable una finca de bodas?',
    a: 'No te prometemos rentabilidad: depende de tu finca, de tu comarca y de lo que llenes el calendario. Lo que sí hace el plan es enseñarte la cuenta con honestidad: eventos al año × invitados por evento × euros por invitado, cuatro tipos de evento (bodas, empresa, celebraciones privadas y eventos pequeños), tres escenarios con el pesimista incluido, el punto de equilibrio expresado en eventos y la tesorería mes a mes. La clave está en la ocupación y en cómo llenas el invierno, y ahí es donde el plan te pone los números delante.',
  },
  {
    q: '¿Catering propio, exclusivo o libre?',
    a: 'El plan se construye sobre el catering exclusivo concesionado: un catering de confianza es el único que sirve en tu finca y te paga un canon. Así no necesitas cocina de producción ni brigada propia, y la responsabilidad sanitaria del menú es de quien cocina. Si prefieres el catering propio, el Word razona cuándo compensa y por qué es otro negocio, mucho más grande, para el que tienes el Plan de Negocio Catering Temático para Eventos. El «solo alquiler» también se explica, con su límite: cubre menos fijos. El canon del caso es un supuesto editable, negócialo con tu catering. Y con los modelos de contrato tienes las condiciones del catering exclusivo ya redactadas para adaptar.',
  },
  {
    q: '¿Qué IVA lleva el alquiler de la finca y el banquete?',
    a: 'En el modelo del plan, todo lo que factura la finca va al 21 %: el alquiler del espacio y los servicios del evento, y el canon que paga el catering. El menú lo factura el catering con su propio IVA. Si quieres vender un paquete de precio único (espacio más banquete), el IVA se complica: ponle precio propio al espacio o haz una consulta vinculante a Hacienda antes. Cómo te afecta con tu régimen y tu comunidad, confírmalo con tu asesoría.',
  },
  {
    q: '¿Cuánta señal pido y qué pasa si los novios cancelan?',
    a: 'La calculadora de presupuesto del espacio trae un calendario de pagos con la señal y una cancelación por tramos. Las penalizaciones tienen que ser proporcionales y recíprocas: la ley de consumidores (TRLGDCU, arts. 85.6 y 87.2) considera abusivo retener lo pagado si el cliente renuncia sin prever una indemnización equivalente cuando renuncia la finca. Los modelos de contrato (reserva con los novios y anexo para empresas) recogen esos tramos para que los adaptes. Son plantillas orientativas: revísalas con tu abogado antes de firmar con un cliente.',
  },
  {
    q: '¿Qué mínimo de invitados y qué tarifa pongo?',
    a: 'La calculadora está hecha para eso: tarifa por tipología de evento, temporada y día de la semana con su suplemento o descuento a la vista, mínimo de invitados, servicios extra, IVA y el canon estimado del catering como dato informativo. Trae tres ejemplos calculados para que la adaptes a tu finca. Pon el mínimo de invitados que cubra el coste real de abrir la finca un sábado, no el que te gustaría.',
  },
  {
    q: '¿Sirve si la finca es de mi familia?',
    a: 'Sí, y de hecho es un caso muy habitual. El plan sirve tanto para arrendar una finca de terceros como para poner en marcha la de la familia. En ese caso, cuenta una renta de mercado igual que si fuera de un tercero: así sabes si el negocio se sostiene por sí mismo y no por una renta regalada. Las condiciones concretas entre familiares (arrendamiento, tributación) consúltalas con tu asesoría.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Finca de Eventos y Bodas» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, la «fianza» del arrendamiento es el «depósito en garantía» en México o Colombia (allí la «fianza» es una póliza), los «aseos» son «baños», el «catering» es «banquetería» en Chile o Argentina, y la «barra libre» es «open bar» en casi todas partes. Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-finca-eventos-bodas',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_FINCA_EVENTOS',

  seo: {
    title: 'Plan de Negocio Finca de Eventos y Bodas — Excel, Word y Contratos | AI Chef Pro',
    description:
      'Plan de negocio para montar una finca de eventos y bodas: plan financiero en Excel de 9 hojas, plan en Word de 10 secciones, checklist de 84 tareas, calculadora de presupuesto del espacio y modelos de contrato. 45 €, pago único.',
    keywords:
      'plan de negocio finca de eventos, plan de negocio finca para bodas, cómo montar una finca para bodas, cómo montar una finca de eventos, plan financiero finca de eventos excel, licencia finca de bodas suelo rústico, contrato alquiler finca bodas, AI Chef Pro',
    // No existe og-plan-negocio-finca-eventos-bodas.jpg: se usa la imagen del hero de la landing.
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-finca-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Finca de Eventos y Bodas',
    productDescription:
      'Plan de negocio para montar una finca de eventos y bodas: una finca arrendada con edificaciones existentes y un catering exclusivo concesionado que paga canon. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 84 tareas en 6 fases, una calculadora de presupuesto del espacio (tarifa por tipología, temporada y día, mínimo de invitados, extras, IVA, calendario de pagos y cancelación por tramos; con 3 ejemplos), modelos de contrato (reserva con los novios, anexo para empresas y condiciones del catering exclusivo) y la Guía de Equivalencias para Latinoamérica. Cuatro tipos de evento: bodas, empresa, celebraciones privadas y eventos pequeños. No es un curso ni asesoría legal, y no promete rentabilidad.',
    price: '45.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Finca de Eventos y Bodas',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-finca-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-ceremonia.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-banquete.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-cocina.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-finca-banquete.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-ceremonia.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-montaje.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-finca-cocina.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-finca-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-finca-banquete.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-finca-hero.jpg',
  },

  hero: {
    badge: 'Para montar tu finca de eventos con las cuentas claras',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Finca de Eventos y Bodas',
    titleSubtitle: 'Plan Financiero en Excel, Plan en Word, Calculadora y Contratos',
    description:
      'El plan para montar una finca de eventos y bodas con edificaciones existentes y un catering exclusivo que te paga canon: la licencia en suelo rústico, la temporada de bodas y el invierno. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones, checklist de apertura de 84 tareas, calculadora de presupuesto del espacio y modelos de contrato.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Un modelo claro: finca arrendada y catering exclusivo que paga canon (la finca no se compra)',
      'Calculadora de presupuesto del espacio: tarifa por temporada y día, mínimo de invitados, extras, IVA, señal y cancelación por tramos',
      'Modelos de contrato: reserva con los novios, anexo para empresas y condiciones del catering exclusivo',
      'Plan de negocio en Word (10 secciones) y checklist de apertura de 84 tareas en 6 fases',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      'Es el plan de un negocio de espacio para eventos: sus números, sus trámites y su calendario. No es un curso de organización de bodas ni asesoría legal, y no sustituye a tu asesoría, al proyecto técnico ni a tu abogado: las plantillas de contrato son orientativas.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias la renta, los eventos al año o el precio por invitado y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Las partidas de una finca de eventos sobre edificaciones existentes: proyecto, calificación urbanística, licencia y tasas, obra, carpa, mobiliario, instalaciones e imprevistos, más el fondo de maniobra y el IVA de la inversión. Todo editable para tu finca.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos eventos al año necesitas para cubrir costes, con cuatro tipos de evento (bodas, empresa, celebraciones privadas y eventos pequeños), y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo de reservas.' },
      { icon: 'CalendarRange', title: 'Tesorería Mes a Mes y Temporada de Bodas', desc: 'La estacionalidad de las bodas, con sus picos y su invierno, y una rampa de ocupación realista: las bodas se reservan con mucha antelación, así que la primera temporada se reserva antes de abrir, condicionada a la licencia. Ves la caja mes a mes y la liquidación del IVA.' },
      { icon: 'Users', title: 'Catering Exclusivo con Canon', desc: 'El modelo del plan: un catering de confianza sirve en exclusiva y paga un canon, sin que montes cocina de producción ni brigada propia. Con alternativas razonadas en el Word: catering propio y solo alquiler.' },
      { icon: 'Calculator', title: 'Calculadora de Presupuesto del Espacio', desc: 'Tarifa por tipología de evento, temporada y día de la semana, mínimo de invitados, servicios extra, IVA, calendario de pagos con la señal y cancelación por tramos proporcionados y recíprocos. Con 3 presupuestos de ejemplo calculados.' },
      { icon: 'ScrollText', title: 'Modelos de Contrato', desc: 'Plantillas editables y orientativas (revísalas con tu abogado): reserva con los novios, anexo para empresas y condiciones del catering exclusivo con canon auditable, comida testigo, alérgenos, seguros y horarios.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con la licencia en suelo rústico, el ruido y el plan de invierno.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (84 tareas, 6 fases)', desc: 'Constitución y fiscalidad; finca y licencia; obra; personal y catering; marca y reservas; temporada. Con responsable, plazo y nota en cada tarea.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de una finca de eventos, con su licencia, su temporada y su catering.',
    reasons: [
      { icon: 'ShieldCheck', title: 'La Licencia Es el Negocio', desc: 'En suelo rústico celebrar eventos no es un uso ordinario: pide una autorización previa a la licencia, distinta en cada comunidad, con plazos largos. Madrid, Andalucía, Cataluña y la Comunidad Valenciana, con su artículo. Por eso el contrato lleva condición suspensiva y no se confirma ninguna fecha sin licencia.' },
      { icon: 'Building', title: 'Un Modelo que no Exige Ser Hostelero', desc: 'Finca arrendada con sus edificaciones y catering exclusivo que paga canon: sin cocina de producción, sin brigada y con la responsabilidad sanitaria del menú en quien cocina. Si eres hostelero y prefieres catering propio, el Word te dice cuándo compensa.' },
      { icon: 'Heart', title: 'La Temporada de Bodas, con Números', desc: 'Las bodas se concentran de mayo a octubre y se reservan con meses de antelación. El plan lo traduce en una rampa realista, en la tesorería mes a mes y en cómo llenar el invierno con empresa, celebraciones privadas y bodas entre semana.' },
      { icon: 'Scale', title: 'Contratos Equilibrados', desc: 'Señal y cancelación proporcionales y recíprocas, como pide la ley de consumidores, y las condiciones que la finca impone al catering: canon auditable, comida testigo, alérgenos y seguros. Plantillas orientativas para adaptar con tu abogado.' },
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
      'Además del plan financiero, el plan en Word, el checklist, la calculadora y los contratos, te llevas un extra — valorado en €15',
    items: [
      {
        icon: 'Globe',
        label: 'BONUS',
        title: 'Guía de Equivalencias para tu país',
        value: '€15',
        desc: 'Los términos de tu producto dichos país por país en 20 países, más una ficha de una página por país con impuestos, sanidad, normas laborales, licencias y unidades.',
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
    headingGold: 'Finca de Eventos',
    subtitle:
      'Antes de firmar el arrendamiento y de pedir la licencia, ten las cuentas, los trámites, los contratos y el calendario de tu finca sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes con la temporada de bodas y el invierno a la vista',
      'Tres escenarios financieros (pesimista, realista y optimista)',
      'Calculadora de presupuesto del espacio con 3 ejemplos',
      'Modelos de contrato: novios, empresas y catering exclusivo',
      'Checklist de apertura con 84 tareas en 6 fases',
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

  stickyLabel: 'PLAN FINCA DE EVENTOS — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-catering-tematico-eventos', label: 'Plan de Negocio Catering Temático para Eventos' },
    { href: '/plan-negocio-cocteleria-eventos', label: 'Plan de Negocio Coctelería para Eventos' },
    { href: '/kit-tareas-catering', label: 'Kit de Tareas Recurrentes de Catering' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · noviembre 2026',

  alreadyBought: {
    product: 'plan-negocio-finca-eventos-bodas',
    label: '¿Ya compraste el Plan de Negocio: Finca de Eventos y Bodas? Vuelve a entrar al dashboard',
  },
};

export default data;
