// astro-site/src/data/productos/planes/plan-negocio-tapas-bar.ts
// LÍNEA PLANES (sub-línea A "planes de negocio"). Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioTapasBar.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-tapas-bar/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-tapas-bar.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (título/subtítulo constantes de línea, hardcodeados en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_TAPAS_BAR (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Hacer Realidad tu ' (patrón de la sub-línea A).
//   · authorBadges se OMITE → cae en el default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],
//     que es EXACTAMENTE el par de este producto.
//   · hero.titlePost se omite (Forma B: titlePre + gold + titleSubtitle en bloque).
//
// QUIRK VERBATIM: schema.faqs (FAQPage JSON-LD) = 4 preguntas (subconjunto), mientras que faqs on-page
// (acordeón) = 6 preguntas. Cada bloque copiado según su origen en la SPA.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-tapas-bar',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_TAPAS_BAR',

  seo: {
    title:
      'Plan de Negocio: Tapas Bar / Gastrobar — Plan Financiero Excel + DOCX + Checklist Apertura | AI Chef Pro',
    description:
      'Plan de negocio completo para abrir un tapas bar o gastrobar en España 2026. Documento DOCX 10 secciones + plan financiero Excel con P&L 3 años + checklist apertura con 63 trámites incluyendo licencia clasificada y salida de humos. €35.',
    keywords:
      'plan de negocio tapas bar, plan financiero gastrobar España, abrir tapas bar, checklist apertura tapas bar, licencia clasificada hostelería, salida de humos restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-tapas-bar.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio: Tapas Bar / Gastrobar — Plan Financiero Excel + DOCX + Checklist Apertura',
    productDescription:
      'Plan de negocio completo para abrir un tapas bar o gastrobar en España. Incluye documento DOCX de 10 secciones (resumen ejecutivo, concepto, mercado, DAFO, marketing, operaciones, RRHH, financiero, legal, conclusiones), plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada, punto de equilibrio, 3 escenarios financieros, cuadro de personal con Seg. Social, checklist de apertura con 63 trámites incluyendo licencia clasificada y salida de humos, y ratios sectoriales del mercado español 2026.',
    price: '35.00',
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
        body: 'El plan financiero me ayudó a conseguir el préstamo ICO en 2 semanas. El desglose de inversión para cocina y barra fue exacto.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El checklist de apertura fue clave. Descubrí que necesitaba licencia clasificada y no inocua por la potencia de cocina. Me ahorré meses de retrasos.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'El break-even de 34 clientes al día es realista para un tapas bar bien ubicado. Los márgenes en tapas y bebidas dan mucha confianza.',
      },
    ],
    // FAQPage schema (4 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6)
    faqs: [
      {
        q: '¿Es un plan genérico o específico para tapas bar?',
        a: 'Es 100% específico para tapas bar y gastrobar en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de tapas bar con barra y sala, incluyendo licencia clasificada, salida de humos y equipamiento específico.',
      },
      {
        q: '¿Puedo presentar este plan al banco o a inversores?',
        a: 'Sí. El plan financiero Excel incluye P&L 3 años, punto de equilibrio y 3 escenarios. El documento DOCX de 10 secciones tiene formato profesional, exactamente lo que piden bancos e inversores.',
      },
      {
        q: '¿Qué trámites legales incluye el checklist de apertura?',
        a: '63 trámites en 6 fases: constitución de la SL, licencia clasificada (no inocua, por potencia de cocina), salida de humos obligatoria, equipamiento, contratación de personal, marketing pre-apertura y primeros 90 días.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio: Tapas Bar / Gastrobar',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-tapas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-raciones.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-cerveza.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-cocina.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-vermut.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (termina en -terraza, sin -hero)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-tapas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-raciones.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-terraza.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-cerveza.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-cocina.jpg',
      '/lovable-uploads/ai-gallery/plan-tapas-bar-vermut.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-tapas-bar-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-tapas-bar-raciones.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-tapas-bar-hero.jpg',
  },

  hero: {
    badge: 'El plan de negocio más completo para abrir un tapas bar o gastrobar',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Tapas Bar / Gastrobar',
    titleSubtitle: 'Plan Financiero Excel + Documento DOCX + Checklist Apertura',
    description:
      'El plan de negocio completo para abrir un tapas bar o gastrobar en España. Documento DOCX de 10 secciones, plan financiero Excel con P&L a 3 años, inversión inicial detallada, punto de equilibrio, escenarios y checklist de apertura con 63 trámites incluyendo licencia clasificada y salida de humos.',
    checkItems: [
      'Plan de negocio DOCX completo: 10 secciones profesionales',
      'Plan financiero Excel: P&L previsional a 3 años con fórmulas',
      'Inversión inicial detallada por partidas (~90K-140K EUR)',
      'Checklist apertura: 63 trámites y licencias España 2026',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      '9 secciones profesionales con datos reales del mercado español para construir la viabilidad financiera de tu tapas bar y presentarla a banco o inversores.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Resumen ejecutivo, concepto, análisis de mercado, DAFO, marketing, operaciones, RRHH, financiero, legal y conclusiones. Listo para banco o inversores.' },
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años, inversión inicial, punto de equilibrio, escenarios, cuadro de personal e instrucciones. Todas las celdas editables.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio (Break-Even)', desc: 'Modelo realista: 34 clientes al día con ticket medio €18, margen de seguridad 25 % y sensibilidad a horas pico de barra y comedor.' },
      { icon: 'BarChart3', title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes y ticket medio. Útil para presentar a banco e inversores.' },
      { icon: 'Users', title: 'Cuadro de Personal y Costes', desc: 'Salarios brutos por puesto: jefe de cocina, cocineros, camareros de barra y de sala, con Seguridad Social al 33,4 % y 14 pagas.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, licencia clasificada (no inocua, por potencia de cocina), salida de humos, equipamiento, RRHH, marketing pre-apertura y primeros 90 días.' },
      { icon: 'Wrench', title: 'Equipamiento Específico Tapas Bar', desc: 'Plancha, freidora, grifos de cerveza, vitrina de tapas, salamandra, expositor de raciones y vinoteca, con marcas de referencia y precios orientativos.' },
      { icon: 'ListChecks', title: 'Ratios de Referencia Tapas Bar', desc: 'Food cost tapas 28-32 %, márgenes bebidas 22-28 %, margen bruto >68 %, ticket medio 15-22 EUR y rotación por turno.' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'ICO, ENISA, préstamo bancario, inversores privados, business angels y subvenciones autonómicas con orden recomendado de gestión.' },
    ],
  },

  testimonials: {
    subtitle:
      'Propietarios e inversores que abrieron su tapas bar o gastrobar con un plan financiero profesional',
    items: [
      { name: 'Alejandro Ruiz', role: 'Propietario Tapas Bar Madrid', text: 'El plan financiero me ayudó a conseguir el préstamo ICO en 2 semanas. El desglose de inversión para cocina y barra fue exacto, sin sorpresas. Inversión total: 120K EUR.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Emprendedora Gastrobar Barcelona', text: 'El checklist de apertura fue clave. Descubrí que necesitaba licencia clasificada y no inocua por la potencia de cocina. Me ahorré meses de retrasos y multas.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Inversor Hostelería', text: 'El break-even de 34 clientes al día es realista para un tapas bar bien ubicado. Los márgenes en tapas y bebidas dan mucha confianza para invertir.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Socia Gastrobar Sevilla', text: 'Los escenarios financieros me dieron la seguridad que necesitaba. Sabía exactamente la facturación mínima para ser rentable y la máxima si todo iba bien.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Consultor Hostelería', text: 'Lo recomiendo a todos mis clientes que quieren abrir un tapas bar o gastrobar. Es el plan de negocio más completo y actualizado que he visto para este formato.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Propietaria Tapas Bar Valencia', text: 'Los ratios de food cost tapas 28-32 % y los márgenes en bebidas me ahorraron miles de euros. Sabía exactamente dónde estaban los beneficios antes de abrir.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex Corporativo, Abrió Gastrobar', text: 'No sabía nada sobre salida de humos ni licencia clasificada. El checklist me guió paso a paso por los 63 trámites. Abrí sin ningún problema legal ni retrasos.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Propietario Grupo 4 Gastrobars', text: 'He usado este plan para las 4 aperturas de mis gastrobars. Solo cambias las cifras del local y tienes un business plan profesional listo para presentar.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado español para abrir un tapas bar o gastrobar con cabeza.',
    reasons: [
      { icon: 'FileText', title: 'Plan DOCX + Excel Profesional', desc: 'Documento Word de 10 secciones con resumen ejecutivo, DAFO, análisis de mercado y plan financiero. Excel con fórmulas activas que recalculan al cambiar cifras.' },
      { icon: 'BarChart3', title: 'Datos Reales Tapas Bar 2026', desc: 'Ticket medio €15-22, food cost 28-32 %, márgenes bebidas 22-28 %, ocupación por franja horaria y break-even en 34 clientes/día. Cifras del mercado español real.' },
      { icon: 'ShieldCheck', title: 'Licencia Clasificada Cubierta', desc: '63 trámites incluyendo licencia clasificada (no inocua, por potencia de cocina), salida de humos obligatoria, sanidad y prevención de incendios. No te dejas nada.' },
      { icon: 'Banknote', title: 'Listo para Banco e Inversores', desc: 'P&L 3 años, punto de equilibrio, 3 escenarios y plan de financiación con ICO, ENISA, banca y business angels. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a propietarios de tapas bars y gastrobars en España, combinando experiencia operativa con análisis financiero profesional para garantizar viabilidad y rentabilidad desde el día uno.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y el checklist de apertura, accedes a estos recursos extra — valorados en €38',
    items: [
      {
        icon: 'Users',
        label: 'BONUS 1',
        title: 'Cuadro de Personal con Seg. Social',
        value: '€19',
        desc: 'Cuadro completo de personal con salarios brutos, Seguridad Social al 33,4 %, 14 pagas y coste real por puesto: jefe de cocina, cocineros, camareros de barra y de sala.',
        image: '/lovable-uploads/ai-gallery/plan-tapas-bar-cocina.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Ratios Referencia Tapas Bar 2026',
        value: '€19',
        desc: 'Datos actualizados del sector: food cost tapas 28-32 %, márgenes bebidas 22-28 %, ticket medio 15-22 EUR y ratios de ocupación por franja horaria (mediodía / tarde / noche).',
        image: '/lovable-uploads/ai-gallery/plan-tapas-bar-vermut.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €35',
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
      q: '¿Es un plan genérico o específico para tapas bar?',
      a: 'Es 100 % específico para tapas bar y gastrobar en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de tapas bar con barra y sala, incluyendo licencia clasificada, salida de humos y equipamiento específico como grifos de cerveza y vitrina de tapas.',
    },
    {
      q: '¿Puedo presentar este plan al banco o a inversores?',
      a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. El documento DOCX de 10 secciones tiene formato profesional, exactamente lo que piden bancos e inversores para evaluar la financiación.',
    },
    {
      q: '¿Puedo modificar las cifras del Excel?',
      a: 'Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, el número de clientes, el ticket medio, los salarios y cualquier partida de inversión para adaptarlo a tu proyecto concreto. Incluye hoja de instrucciones.',
    },
    {
      q: '¿Qué trámites legales incluye el checklist de apertura?',
      a: '63 trámites organizados en 6 fases: constitución de la SL, licencia clasificada (no inocua, por potencia de cocina), salida de humos obligatoria, equipamiento, contratación de personal, marketing pre-apertura y primeros 90 días de operación.',
    },
    {
      q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
      a: 'Los planes gratuitos son plantillas genéricas sin datos reales. Este plan incluye cifras del mercado español 2026, documento DOCX de 10 secciones profesionales, ratios financieros específicos de tapas bar (food cost, bebidas, ticket medio), cuadro de personal con Seg. Social y un checklist de 63 trámites verificado con la legislación vigente.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu tapas bar con total confianza.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Tapas Bar',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a propietarios que ya abrieron su tapas bar o gastrobar con un plan financiero profesional y un checklist de apertura completo.',
    items: [
      'Plan de negocio DOCX completo (10 secciones)',
      'Plan financiero Excel con P&L previsional 3 años',
      'Inversión inicial detallada (~115K EUR de referencia)',
      'Punto de equilibrio + 3 escenarios financieros',
      'Checklist apertura con 63 trámites en 6 fases',
      'Equipamiento específico tapas bar + ratios sectoriales',
      'BONUS: Cuadro Personal con Seg. Social (€19)',
      'BONUS: Ratios Referencia Tapas Bar 2026 (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €35',
  },

  pricing: {
    priceOld: '€120',
    price: '€35',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71 % de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €85 HOY!',
  },

  stickyLabel: 'PLAN TAPAS BAR — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: '/kit-tareas-tapas-bar', label: 'Kit Tareas Tapas Bar' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'plan-negocio-tapas-bar',
    label: '¿Ya compraste el Plan de Negocio Tapas Bar? Vuelve a entrar al dashboard',
  },
};

export default data;
