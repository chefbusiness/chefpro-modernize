// astro-site/src/data/productos/planes/plan-negocio-cocteleria-eventos.ts
// LÍNEA PLANES (sub-línea B "planes de eventos") — producto que VALIDA que el template único sirve
// también a la sub-línea de eventos (mismo esqueleto DOM que bar-restaurante; solo cambia el copy).
// Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioCocteleriaEventos.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-cocteleria-eventos/*  (los 10 componentes)
//   · src/data/testimonials-plan-cocteleria-eventos.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (constante de línea, hardcodeada en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_COCTELERIA (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Lanzar tu ' (patrón de la sub-línea B, distinto del "Hacer Realidad tu" de A).
//   · hero.checkItems tiene 6 elementos (bar-restaurante tenía 5) — longitud variable, sin impacto estructural.
//   · authorBadges se OMITE → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto).
//
// QUIRKS VERBATIM:
//   · titlePre / seo.title / schema.productName llevan un '&' literal (la SPA lo escribe '&amp;' en JSX y
//     como '&' en JSON.stringify; aquí se escribe '&' y el template/BaseLayout lo escapan igual en HTML).
//   · schema.faqs (FAQPage JSON-LD) = 5 preguntas más cortas; faqs on-page (acordeón) = 6, más largas.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-cocteleria-eventos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_COCTELERIA',

  seo: {
    title:
      'Plan de Negocio & Kit Coctelería de Eventos / Barra Móvil — 9 Entregables | AI Chef Pro',
    description:
      'Plan de negocio + kit profesional completo para montar tu empresa de coctelería itinerante con barra móvil en España 2026. 9 entregables: DOCX 10 secciones + Plan Financiero Excel + 96 proveedores + Catálogo equipamiento + 15 cocktails + 10 experiencias + Modelo contrato + Checklist 71 trámites. Inversión 18-35K EUR. €55.',
    keywords:
      'plan de negocio coctelería eventos, barra móvil bodas, empresa coctelería itinerante, montar barra móvil, plan financiero coctelería, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-cocteleria-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio & Kit de Coctelería de Eventos / Barra Móvil — 9 Entregables',
    productDescription:
      'Plan de negocio + kit profesional completo para montar una empresa de coctelería itinerante con barra móvil en España 2026. Incluye DOCX 10 secciones, Plan Financiero Excel con estacionalidad de eventos, Calculadora Pricing, plantilla de 96 proveedores reales, catálogo de equipamiento (GGM/Mewindo/Deus), carta de 15 cocktails temáticos, modelo de contrato profesional, 10 experiencias temáticas premium y checklist de apertura con 71 trámites adaptado al modelo itinerante.',
    price: '55.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Nadia y Lidia',
        rating: '5',
        body: 'Buscábamos un plan específico para nuestro modelo de barra móvil con experiencias temáticas y este es exactamente lo que necesitábamos. Las 10 experiencias y los proveedores nos han ahorrado meses de investigación.',
      },
      {
        author: 'Alejandro Vela',
        rating: '5',
        body: 'Ojalá hubiera tenido este plan cuando arranqué hace dos años. La calculadora de pricing es oro: ahora cobro lo que vale realmente cada evento, no lo que me parecía.',
      },
      {
        author: 'Laura Manchón',
        rating: '5',
        body: 'Recomiendo este plan a TODOS los proveedores de coctelería que entran en mi red. La plantilla de proveedores y el modelo de contrato les ahorran 40 horas de trabajo administrativo.',
      },
    ],
    // FAQPage schema (5 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6, más largas)
    faqs: [
      {
        q: '¿Es válido si nunca he montado una empresa de eventos antes?',
        a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. Incluye desde la constitución como autónomo hasta los primeros 90 días de operación. El checklist de 71 trámites en 6 fases no deja nada al azar.',
      },
      {
        q: '¿Qué diferencia hay con un Plan de Negocio para un bar fijo?',
        a: 'Modelo itinerante: sin licencia clasificada (autorizaciones puntuales por evento), sin plantilla fija (bartenders freelance), inversión 4-7x menor, ingresos por evento, estacionalidad agresiva (60-70 % facturación mayo-septiembre + diciembre), captación B2B intensiva con wedding planners.',
      },
      {
        q: '¿La plantilla de 96 proveedores incluye contactos reales?',
        a: 'Sí. Cada proveedor lleva web/contacto, cobertura, precio orientativo y plazo. Distribuidores oficiales como Damm (Fever-Tree), Disbesa (Schweppes HORECA), Latin Hotel (Spiegelau) y SERHS Equipments (Hoshizaki).',
      },
      {
        q: '¿Sirve para presentar al banco?',
        a: 'Sí. El Plan Financiero Excel incluye P&L 3 años, punto de equilibrio (31 eventos/año break-even), escenarios pesimista/realista/optimista y cuadro de personal freelance. Formato ICO/microcrédito.',
      },
      {
        q: '¿Cómo funciona la garantía?',
        a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe. Los 9 entregables son tuyos para siempre + actualizaciones gratuitas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio Coctelería de Eventos',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-1.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-2.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-3.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-5.jpeg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (empieza en -1, termina en -6)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-1.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-2.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-3.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-5.jpeg',
      '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-6.jpeg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-2.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-4.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-hero.jpg',
  },

  hero: {
    badge: 'El plan más completo de España para montar tu barra móvil de coctelería',
    titlePre: 'Plan de Negocio & Kit de ',
    titleGold: 'Coctelería de Eventos',
    titleSubtitle: 'Barra Móvil — 9 Entregables Profesionales',
    description:
      'El kit profesional completo para montar tu empresa de coctelería itinerante con barra móvil en España. 9 entregables y 96 proveedores reales validados, con carta de 15 cocktails temáticos y checklist de 71 trámites. Inversión 4-7x menor que un bar con local fijo.',
    checkItems: [
      'Plan de negocio DOCX 10 secciones (~6.600 palabras profesionales)',
      'Plan Financiero Excel con estacionalidad de eventos + Calculadora Pricing',
      'Plantilla con 96 proveedores reales validados (Damm, Disbesa, GGM, etc.)',
      'Catálogo equipamiento + 15 cocktails temáticos + 10 experiencias premium',
      'Modelo de contrato profesional + checklist 71 trámites adaptados',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €55',
  },

  grid: {
    subtitle:
      '9 entregables profesionales con datos reales del mercado de eventos español 2026 para validar la viabilidad de tu barra móvil de coctelería.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Resumen ejecutivo, concepto itinerante, mercado eventos España, competencia, marketing B2B, operaciones, RRHH freelance, financiero, legal y plan de financiación. ~6.600 palabras editables.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con estacionalidad eventos, inversión inicial 18-35K EUR, break-even por nº de eventos (31/año), 3 escenarios y ratios sector itinerante.' },
      { icon: 'Calculator', title: 'Calculadora Pricing por Evento', desc: 'Excel con fórmulas: invitados + horas + tipo + complejidad ⇒ precio sugerido en 3 niveles + margen estimado. Con 10 ejemplos reales del sector.' },
      { icon: 'Truck', title: 'Plantilla 96 Proveedores Reales', desc: 'Excel categorizado: licores, mixers (Damm/Disbesa), cristalería (Schott Zwiesel/Spiegelau), hielo (Hoshizaki) y captación B2B con wedding planners.' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento (SKU reales)', desc: 'Barras móviles GGM MCSH 2.420 EUR + Mewindo + Station Deus + Flexbar. Máquinas de hielo Hoshizaki/ITV. Cristalería profesional con precios orientativos.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (71 trámites)', desc: 'Constitución, seguros (RC obligatorio), equipamiento, marca y web, captación B2B y operativa primeros 90 días. Modelo itinerante sin licencia clasificada.' },
      { icon: 'GlassWater', title: 'Carta 15 Cocktails Temáticos', desc: 'Speakeasy + Gin Lounge + Tropical + Mediterranean + Signature. Receta + escandallo + escalado a 50/100/200 invitados + glasería recomendada.' },
      { icon: 'ScrollText', title: 'Modelo de Contrato Profesional', desc: '11 cláusulas listas para firmar: anticipo, cancelación 30/60 días, fuerza mayor, RC, derechos imagen, RGPD, jurisdicción. Plantilla DOCX editable.' },
      { icon: 'Sparkles', title: '10 Experiencias Temáticas Premium', desc: 'Speakeasy Años 20, Gin Lounge, Tropical Tiki, Mixología Molecular, Bourbon Tasting, Mediterranean, Latin, Whisky Tasting, Champagne y Signature.' },
    ],
  },

  testimonials: {
    subtitle:
      'Bartenders, wedding planners y emprendedores que usaron el plan para montar o impulsar su empresa de coctelería de eventos',
    items: [
      { name: 'Nadia y Lidia', role: 'Fundadoras Empresa Coctelería Eventos', text: 'Buscábamos un plan específico para nuestro modelo de barra móvil con experiencias temáticas y este es exactamente lo que necesitábamos. Las 10 experiencias y los proveedores nos han ahorrado meses de investigación.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Alejandro Vela', role: 'Bartender, segundo año con barra móvil Madrid', text: 'Ojalá hubiera tenido este plan cuando arranqué hace dos años. La calculadora de pricing es oro: ahora cobro lo que vale realmente cada evento, no lo que me parecía.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Laura Manchón', role: 'Wedding Planner, Madrid centro', text: 'Recomiendo este plan a TODOS los proveedores de coctelería que entran en mi red. La plantilla de proveedores y el modelo de contrato les ahorran 40 horas de trabajo administrativo.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Carlos Ferreras', role: 'Coctelero freelance pasando a empresa propia', text: 'El plan financiero me convenció: con 50 eventos al año puedes facturar 70K EUR con margen del 42 %. Mi próximo paso es aplicar el checklist y arrancar en septiembre.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'María Pino', role: 'Profesora Escuela de Coctelería Madrid', text: 'Lo recomiendo en todos los cursos avanzados. Nadie en el mercado español ha empaquetado tan bien el conocimiento de cómo montar este negocio.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ferran Llopis', role: 'Empresario hostelería Barcelona', text: 'Iba a abrir un bar fijo de 150K EUR. Después de leer este plan he pivotado a barra móvil de eventos: misma rentabilidad esperada, 1/4 del riesgo financiero.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex hostelería que monta su barra móvil', text: 'Venía del bar tradicional y no sabía nada de captar bodas. La estrategia de wedding planners y la lista de plataformas (Bodas.net, Zankyou) me dieron la hoja de ruta clara.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Inversor en proyectos hostelería', text: 'El plan financiero es realista: 50 eventos/año, ticket medio 1.400 EUR, break-even mes 10. Esto es lo que esperaba de un plan profesional, no un PowerPoint inflado.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo de España para montar tu empresa de coctelería itinerante con datos reales del mercado eventos 2026.',
    reasons: [
      { icon: 'GlassWater', title: 'Específico Modelo Itinerante', desc: 'No es un plan genérico de bar fijo. Está diseñado para barra móvil de eventos: sin licencia clasificada (autorizaciones puntuales), bartenders freelance, ingresos por evento y estacionalidad agresiva.' },
      { icon: 'BarChart3', title: 'Datos Reales Mercado Eventos 2026', desc: 'Inversión 18-35K EUR (4-7x menor que un bar fijo), ticket medio 1.400 EUR/evento, 50 eventos al año = 70K EUR de facturación con margen del 42 %. Cifras del mercado español verificadas.' },
      { icon: 'ShieldCheck', title: '96 Proveedores Reales Validados', desc: 'Damm (oficial Fever-Tree), Disbesa (Schweppes HORECA), Latin Hotel (Spiegelau), SERHS (Hoshizaki). Web, contacto, cobertura, precio y plazo verificados. No vendor lists genéricas.' },
      { icon: 'Banknote', title: 'Listo para Banco e Inversores', desc: 'P&L 3 años, break-even 31 eventos, escenarios pesimista/realista/optimista, cuadro freelance y plan de financiación. Formato ICO/microcrédito. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a empresas de eventos, bartenders freelance y wedding planners en el lanzamiento y escalado de barras móviles de coctelería en España.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y los 7 entregables principales, accedes a estos recursos extra — valorados en €68',
    items: [
      {
        icon: 'ScrollText',
        label: 'BONUS 1',
        title: 'Modelo de Contrato Profesional',
        value: '€29',
        desc: '11 cláusulas listas para firmar: anticipo, cancelación 30/60 días, fuerza mayor, RC, derechos imagen, RGPD, jurisdicción. Plantilla DOCX editable que sustituye una asesoría jurídica de 200-400 EUR.',
        image: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-3.jpeg',
      },
      {
        icon: 'Sparkles',
        label: 'BONUS 2',
        title: '10 Experiencias Temáticas Premium',
        value: '€39',
        desc: 'Speakeasy Años 20, Gin Lounge, Tropical Tiki, Mixología Molecular, Bourbon Tasting, Mediterranean, Latin, Whisky, Champagne y Signature. Cada una lista para vender en eventos con su carta de cocktails y briefing operativo.',
        image: '/lovable-uploads/ai-gallery/plan-cocteleria-eventos-5.jpeg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €55',
  },

  guarantee: {
    text:
      'Si el plan de negocio para tu barra móvil de coctelería no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (6 preguntas; más largas que schema.faqs)
  faqs: [
    {
      q: '¿Es válido si nunca he montado una empresa de eventos antes?',
      a: 'Sí. El plan está pensado precisamente para emprendedores que arrancan desde cero. Incluye desde la constitución como autónomo (1 día, tarifa plana 80 EUR/mes el primer año) hasta los primeros 90 días de operación. El checklist de 71 trámites organizados en 6 fases no deja nada al azar.',
    },
    {
      q: '¿Qué diferencia hay con un Plan de Negocio para un bar fijo?',
      a: 'Todo. Modelo itinerante: sin licencia de actividad clasificada (autorizaciones puntuales por evento), sin plantilla fija (bartenders freelance bajo demanda), inversión 4-7x menor, ingresos por evento (no diarios), estacionalidad agresiva (mayo-septiembre + diciembre = 60-70 % facturación), captación B2B intensiva con wedding planners. El plan refleja todos estos pilares.',
    },
    {
      q: '¿La plantilla de 96 proveedores incluye contactos reales?',
      a: 'Sí. Cada proveedor lleva web/contacto, cobertura, precio orientativo, plazo y notas. Distribuidores oficiales como Damm (Fever-Tree), Disbesa (Schweppes HORECA), Latin Hotel (Spiegelau) y SERHS Equipments (Hoshizaki). Verifica con cada uno antes de cerrar acuerdos.',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El Plan Financiero Excel incluye P&L previsional a 3 años, punto de equilibrio (31 eventos/año break-even), escenarios pesimista/realista/optimista y cuadro de personal freelance. Es el formato que piden bancos para microcrédito o ICO emprendedores.',
    },
    {
      q: '¿Puedo personalizar la Carta de 15 Cocktails para mi marca?',
      a: 'Sí, el DOCX es totalmente editable. Cada cocktail incluye receta, escandallo, escalado por nº de invitados (50/100/200), glasería recomendada y consejo pro. Puedes usarlo como base y crear tu carta signature en pocas horas.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 9 entregables son tuyos para siempre + actualizaciones gratuitas.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Lanzar tu ',
    headingGold: 'Barra Móvil de Coctelería',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a bartenders, wedding planners y emprendedores que ya escalaron su empresa de coctelería de eventos con un plan profesional completo.',
    items: [
      'DOCX 10 secciones (~6.600 palabras) + Plan Financiero Excel',
      'Calculadora Pricing por Evento + 96 proveedores reales',
      'Catálogo equipamiento (GGM/Mewindo/Deus) + 15 cocktails',
      'Modelo de contrato profesional + 10 experiencias premium',
      'Checklist 71 trámites adaptado al modelo itinerante',
      'Acceso de por vida + 30 días de garantía de devolución',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €55',
  },

  pricing: {
    priceOld: '€165',
    price: '€55',
    discountBadge: '-67%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 67 % de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €110 HOY!',
  },

  stickyLabel: 'PLAN COCTELERÍA EVENTOS — €55',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: '/plan-negocio-food-truck', label: 'Plan Food Truck' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'plan-negocio-cocteleria-eventos',
    label: '¿Ya compraste el Plan Coctelería de Eventos? Vuelve a entrar al dashboard',
  },
};

export default data;
