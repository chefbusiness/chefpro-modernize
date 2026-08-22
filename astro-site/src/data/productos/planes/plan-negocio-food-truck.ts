// astro-site/src/data/productos/planes/plan-negocio-food-truck.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioFoodTruck.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-food-truck/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-food-truck.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (título/subtítulo constantes de línea, hardcodeados en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_FOOD_TRUCK (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Hacer Realidad tu ' (patrón de la sub-línea A).
//   · authorBadges se OMITE → cae en el default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],
//     que es EXACTAMENTE el par de este producto.
//   · hero.titlePost se omite (Forma B: titlePre + gold + titleSubtitle en bloque).
//   · images.gridGallery se declara explícito: el ContentGrid de la SPA usa un set DISTINTO al hero
//     (sustituye "hero.jpg" por "setup.jpg" y reordena mercado/cola) — no cae en el default `gallery`.
//
// QUIRK VERBATIM: schema.faqs (FAQPage JSON-LD) = 4 preguntas (subconjunto), mientras que faqs
// on-page (acordeón) = 6 preguntas. Cada bloque copiado según su origen en la SPA.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-food-truck',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_FOOD_TRUCK',

  seo: {
    title:
      'Plan de Negocio: Food Truck — Plan Financiero Excel + DOCX + Checklist Apertura | AI Chef Pro',
    description:
      'Plan de negocio completo para montar un food truck en España 2026. Documento DOCX 10 secciones + plan financiero Excel con P&L 3 años + checklist apertura con 59 trámites incluyendo licencia venta ambulante e ITV vehículo adaptado. €29.',
    keywords:
      'plan de negocio food truck, plan financiero food truck España, montar food truck, licencia venta ambulante, ITV vehículo adaptado, street food España, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-food-truck.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio: Food Truck — Plan Financiero Excel, Inversión Inicial y Checklist Apertura',
    productDescription:
      'Plan de negocio completo para montar un food truck en España. Incluye documento DOCX de 10 secciones, plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada (~62K EUR), punto de equilibrio en 27 clientes/día con ticket €12, escenarios financieros, cuadro de personal, checklist de apertura con 59 trámites incluyendo licencia de venta ambulante, ITV vehículo adaptado y autorización sanitaria RGSEAA, equipamiento cocina móvil y guía de permisos por CCAA.',
    price: '29.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Presenté el plan financiero al banco y me aprobaron el microcrédito en 2 semanas. Inversión total: 62K EUR.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El checklist de apertura con 59 trámites me salvó meses de trabajo. Permisos municipales, ITV vehículo, venta ambulante.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: '27 clientes/día a €12 de ticket medio cubre costes. La inversión es mucho menor que un restaurante y el retorno más rápido.',
      },
    ],
    // FAQPage schema (4 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6)
    faqs: [
      {
        q: '¿Qué permisos necesito para operar un food truck en España?',
        a: 'Licencia de venta ambulante, autorización sanitaria RGSEAA, ITV del vehículo adaptado, alta en Hacienda (modelo 036/037), seguro de responsabilidad civil y permiso de ocupación de vía pública. El checklist incluye los 59 trámites organizados por fases y por CCAA.',
      },
      {
        q: '¿Cuánto cuesta montar un food truck en España?',
        a: 'Entre 45K y 85K EUR según vehículo nuevo o segunda mano, equipamiento de cocina y permisos municipales. El plan financiero Excel desglosa todas las partidas.',
      },
      {
        q: '¿Puedo presentar este plan al banco o a inversores?',
        a: 'Sí. Incluye P&L 3 años, punto de equilibrio y 3 escenarios. Es el formato profesional que piden bancos y entidades como ICO emprendedores o ENISA.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio: Food Truck',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-food-truck-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-exterior.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-cocinando.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-plato.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-cola.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-mercado.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sustituye "hero" por "setup" y reordena mercado/cola)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-food-truck-exterior.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-cocinando.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-plato.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-mercado.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-cola.jpg',
      '/lovable-uploads/ai-gallery/plan-food-truck-setup.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-food-truck-cocinando.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-food-truck-plato.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-food-truck-hero.jpg',
  },

  hero: {
    badge: 'El plan de negocio más completo para montar tu food truck',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Food Truck',
    titleSubtitle: 'Plan Financiero Excel + DOCX + Checklist Apertura 59 Trámites',
    description:
      'El plan de negocio completo para montar un food truck en España. Documento DOCX de 10 secciones, plan financiero Excel con P&L a 3 años, inversión inicial detallada, punto de equilibrio en 27 clientes/día con ticket €12 y checklist de apertura con 59 trámites incluyendo licencia de venta ambulante e ITV del vehículo adaptado.',
    checkItems: [
      'Plan de negocio DOCX completo: 10 secciones profesionales',
      'Plan financiero Excel: P&L previsional a 3 años con fórmulas',
      'Inversión inicial detallada por partidas (~45K-85K EUR)',
      'Checklist apertura: 59 trámites, permisos y licencias',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €29',
  },

  grid: {
    subtitle:
      '9 secciones profesionales con datos reales del sector street food en España para montar tu food truck con cabeza y bajo riesgo.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Documento profesional completo con análisis de mercado, modelo de negocio, plan operativo de food truck, marketing y proyecciones financieras a 3 años.' },
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años, inversión inicial, punto de equilibrio, escenarios, cuadro de personal e instrucciones. Todas las celdas editables.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio (Break-Even)', desc: '27 clientes al día con ticket medio €12. Margen de contribución, días de operación y sensibilidad a ubicaciones (festivales, mercados, oficinas).' },
      { icon: 'BarChart3', title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes ubicaciones, días de operación y ticket medio para presentar a banco e inversores.' },
      { icon: 'Users', title: 'Cuadro Personal (2-3 personas)', desc: 'Equipo reducido típico de food truck con salarios brutos, Seguridad Social al 33,4 %, 14 pagas y coste real por puesto: cocinero, ayudante y atención al cliente.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Alta autónomo o SL, licencias municipales de venta ambulante, autorización sanitaria (RGSEAA), ITV del vehículo adaptado, seguros y primeros 90 días.' },
      { icon: 'Wrench', title: 'Equipamiento Cocina Móvil', desc: 'Plancha, freidora, generador eléctrico, depósitos de agua limpia y residual, extracción de humos con filtros y normativa técnica del vehículo adaptado.' },
      { icon: 'ListChecks', title: 'Ratios de Referencia Food Truck', desc: 'Food cost 30 %, margen bruto 65 %, retorno de inversión en 12-24 meses, ratios sector street food y break-even por ubicación tipo (festival, mercado, oficinas).' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'Opciones reales: ICO emprendedores, ENISA, microcréditos, crowdfunding, préstamo bancario e inversores privados con orden recomendado de gestión.' },
    ],
  },

  testimonials: {
    subtitle:
      'Propietarios de food trucks, flotas de gastro móvil e inversores que montaron su negocio con un plan financiero profesional',
    items: [
      { name: 'Alejandro Ruiz', role: 'Propietario Food Truck Madrid', text: 'Presenté el plan financiero al banco y me aprobaron el microcrédito en 2 semanas. Las proyecciones a 3 años con escenarios les dieron mucha confianza. Inversión total: 62K EUR.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Emprendedora Street Food Barcelona', text: 'El checklist de apertura con los 59 trámites me salvó meses de trabajo. Permisos municipales, ITV del vehículo, licencia de venta ambulante… no me dejé nada pendiente.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Inversor Food & Bev', text: 'Lo que más me convenció fue ver que con 27 clientes al día a €12 de ticket medio ya cubres costes. La inversión es mucho menor que un restaurante y el retorno más rápido.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Socia 2 Food Trucks Sevilla', text: 'Empecé con un truck y en 18 meses abrí el segundo. El plan financiero Excel me permitió proyectar la expansión con datos reales. La movilidad es la clave del negocio.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Consultor Hostelería', text: 'Lo recomiendo a todos mis clientes que quieren emprender con bajo riesgo. Un food truck requiere menos inversión, menos personal y puedes cambiar de ubicación si no funciona.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Propietaria Food Truck Valencia', text: 'Los ratios de referencia — food cost 30 %, margen 65 %, retorno 12-24 meses — me ayudaron a negociar con proveedores y elegir las mejores ubicaciones para maximizar ventas.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex Corporativo, Abrió Food Truck', text: 'Dejé mi trabajo corporativo y monté mi food truck en 3 meses. El checklist de permisos municipales y la guía de licencias por CCAA fueron fundamentales para no perder tiempo.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Propietario Flota 5 Trucks', text: 'Hemos usado el plan financiero Excel para las 5 aperturas. Solo cambias las cifras de cada ubicación y tienes un business plan profesional listo para presentar a inversores.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el plan financiero profesional con datos reales del sector street food para montar un food truck con bajo riesgo y rentabilidad rápida.',
    reasons: [
      { icon: 'Truck', title: 'Inversión Mínima vs Restaurante', desc: 'Inversión 45-85K EUR (vs 100-150K de un restaurante). Menos personal, sin alquiler de local fijo, posibilidad de cambiar de ubicación si no funciona. Negocio de bajo riesgo.' },
      { icon: 'BarChart3', title: 'Datos Reales Street Food 2026', desc: 'Ticket medio €12, food cost 30 %, margen bruto 65 %, retorno de inversión 12-24 meses y break-even en 27 clientes/día. Cifras del mercado español real.' },
      { icon: 'ShieldCheck', title: 'Permisos Municipales + ITV Vehículo', desc: '59 trámites en 6 fases incluyendo licencia de venta ambulante, ITV del vehículo adaptado, autorización sanitaria RGSEAA y permisos por CCAA. No te dejas nada.' },
      { icon: 'Banknote', title: 'Listo para Microcrédito + ICO', desc: 'P&L 3 años, punto de equilibrio, 3 escenarios y plan de financiación con ICO emprendedores, ENISA, microcréditos y crowdfunding. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a propietarios de food trucks, flotas de gastro móvil y operadores de street food en España, combinando experiencia operativa con análisis financiero profesional para garantizar viabilidad y rentabilidad rápida.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y el checklist de apertura, accedes a estos recursos extra — valorados en €38',
    items: [
      {
        icon: 'Map',
        label: 'BONUS 1',
        title: 'Guía Permisos Food Truck por CCAA',
        value: '€19',
        desc: 'Permisos de venta ambulante específicos por comunidad autónoma: Madrid, Cataluña, Andalucía, Comunidad Valenciana, País Vasco… con tasas, plazos y formularios oficiales de cada CCAA.',
        image: '/lovable-uploads/ai-gallery/plan-food-truck-mercado.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Ratios Referencia Street Food 2026',
        value: '€19',
        desc: 'Datos actualizados del sector street food: food cost 30 %, margen bruto 65 %, ticket medio €12, retorno de inversión 12-24 meses y comparativa de ubicaciones (festival, mercado, oficinas, eventos privados).',
        image: '/lovable-uploads/ai-gallery/plan-food-truck-cola.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €29',
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

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (6 preguntas; distinto subconjunto/texto que schema.faqs)
  faqs: [
    {
      q: '¿Qué permisos necesito para operar un food truck en España?',
      a: 'Los permisos varían por municipio, pero los principales son: licencia de venta ambulante, autorización sanitaria (registro sanitario RGSEAA), ITV del vehículo adaptado, alta en Hacienda (modelo 036/037), seguro de responsabilidad civil y permiso de ocupación de vía pública. El checklist incluye los 59 trámites organizados por fases y por CCAA.',
    },
    {
      q: '¿Qué requisitos debe cumplir el vehículo del food truck?',
      a: 'El vehículo debe pasar una ITV específica para vehículos adaptados, cumplir la normativa de instalaciones de gas (si aplica), tener depósitos de agua limpia y residual homologados, extracción de humos con filtros, generador eléctrico o conexión a red, y cumplir las medidas de seguridad contra incendios. Todo está detallado en la sección de equipamiento.',
    },
    {
      q: '¿Cuánto cuesta montar un food truck en España?',
      a: 'La inversión inicial oscila entre 45K y 85K EUR dependiendo de si compras un vehículo nuevo o de segunda mano, el nivel de equipamiento de cocina y los permisos de tu municipio. El plan financiero Excel desglosa todas las partidas: vehículo, adaptación, equipamiento cocina, permisos, marketing, stock inicial y fondo de maniobra.',
    },
    {
      q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
      a: 'Los planes gratuitos son plantillas genéricas sin datos reales. Este plan incluye cifras del mercado español de street food 2026, ratios financieros profesionales (food cost 30 %, margen 65 %), cuadro de personal con Seg. Social, punto de equilibrio calculado (27 clientes/día a €12), checklist de 59 trámites verificado y guía de permisos por CCAA.',
    },
    {
      q: '¿Puedo presentar este plan al banco o a inversores?',
      a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. El documento DOCX de 10 secciones complementa con análisis de mercado, modelo de negocio y plan operativo. Es el formato profesional que piden bancos y entidades como ICO emprendedores o ENISA.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que montes tu food truck con total confianza.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Food Truck',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a emprendedores que ya montaron su food truck con un plan financiero profesional, bajo riesgo y rentabilidad rápida.',
    items: [
      'Plan de negocio DOCX completo (10 secciones)',
      'Plan financiero Excel con P&L previsional 3 años',
      'Inversión inicial detallada (45K-85K EUR según opciones)',
      'Punto de equilibrio: 27 clientes/día con ticket €12',
      'Checklist apertura con 59 trámites + permisos municipales',
      'Equipamiento cocina móvil + ratios street food',
      'BONUS: Guía permisos por CCAA (€19)',
      'BONUS: Ratios referencia street food 2026 (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €29',
  },

  pricing: {
    priceOld: '€99',
    price: '€29',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71 % de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €70 HOY!',
  },

  stickyLabel: 'PLAN FOOD TRUCK — €29',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: '/kit-tareas-food-truck', label: 'Kit Tareas Food Truck' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'plan-negocio-food-truck',
    label: '¿Ya compraste el Plan de Negocio Food Truck? Vuelve a entrar al dashboard',
  },
};

export default data;
