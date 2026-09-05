// astro-site/src/data/productos/planes/plan-negocio-bar-restaurante.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto de REFERENCIA. Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioBarRestaurante.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-bar-restaurante/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-bar-restaurante.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (título/subtítulo constantes de línea, hardcodeados en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_BAR_RESTAURANTE (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Hacer Realidad tu ' (patrón de la sub-línea A).
//   · authorBadges se OMITE → cae en el default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],
//     que es EXACTAMENTE el par de este producto.
//   · hero.titlePost se omite (Forma B: titlePre + gold + titleSubtitle en bloque).
//
// QUIRK VERBATIM: schema.faqs (FAQPage JSON-LD) = 5 preguntas (subconjunto), mientras que faqs on-page
// (acordeón) = 6 preguntas. Cada bloque copiado según su origen en la SPA.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-bar-restaurante',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_BAR_RESTAURANTE',

  seo: {
    title:
      'Plan de Negocio: Bar-Restaurante — Plan Financiero Excel, Inversión Inicial y Checklist Apertura | AI Chef Pro',
    description:
      'Plan de negocio completo para abrir un bar-restaurante en España 2026. Plan financiero Excel con P&L 3 años, punto de equilibrio, escenarios. Checklist apertura con 64 trámites. Datos reales mercado español. €35.',
    keywords:
      'plan de negocio bar-restaurante, plan financiero restaurante España, abrir restaurante, checklist apertura restaurante, inversión inicial restaurante, punto de equilibrio hostelería, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-bar-restaurante.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio: Bar-Restaurante — Plan Financiero Excel, Inversión Inicial y Checklist Apertura',
    productDescription:
      'Plan de negocio completo para abrir un bar-restaurante en España. Incluye plan financiero Excel con P&L previsional a 3 años, inversión inicial detallada, punto de equilibrio, 3 escenarios financieros, cuadro de personal con Seg. Social, checklist de apertura con 64 trámites y análisis de mercado España 2026.',
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
        body: 'Presenté el plan financiero al banco y me aprobaron la financiación en 10 días. Las proyecciones a 3 años con escenarios les dieron mucha confianza.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El checklist de apertura me salvó meses de trabajo. 50+ trámites organizados por fases, desde constituir la SL hasta la licencia de actividad.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Uso este plan como base para evaluar proyectos de restauración. El punto de equilibrio y los escenarios financieros son exactamente lo que necesito.',
      },
    ],
    // FAQPage schema (5 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6)
    faqs: [
      {
        q: '¿Es un plan genérico o específico para bar-restaurante?',
        a: 'Es 100% específico para bar-restaurante en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de bar-restaurante con barra y sala, incluyendo licencias de hostelería españolas actualizadas a 2026.',
      },
      {
        q: '¿Puedo presentar este plan al banco o a inversores?',
        a: 'Sí. El plan financiero Excel incluye cuenta de resultados (P&L) previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. Es exactamente el formato que piden bancos e inversores.',
      },
      {
        q: '¿Puedo modificar las cifras del Excel?',
        a: 'Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, el número de cubiertos, el ticket medio, los salarios y cualquier partida de inversión.',
      },
      {
        q: '¿Qué trámites legales incluye el checklist de apertura?',
        a: '64 trámites en 7 fases: constitución de la SL, licencias municipales, obra y acondicionamiento, RRHH, marketing pre-apertura y primeros 90 días de operación.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio: Bar-Restaurante',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-interior.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-cocina.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-plato.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (termina en -terraza)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-interior.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-cocina.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-plato.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-equipo.jpg',
      '/lovable-uploads/ai-gallery/plan-bar-restaurante-terraza.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-bar-restaurante-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-bar-restaurante-plato.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-bar-restaurante-hero.jpg',
  },

  hero: {
    badge: 'El plan de negocio más completo para abrir tu restaurante en España',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Bar-Restaurante',
    titleSubtitle: 'Plan Financiero Excel, Inversión Inicial y Checklist de Apertura',
    description:
      'El plan de negocio completo para abrir un bar-restaurante en España. Plan financiero Excel con P&L a 3 años, inversión inicial detallada, punto de equilibrio, escenarios pesimista/realista/optimista y checklist de apertura con 64 trámites y licencias.',
    checkItems: [
      'Plan financiero Excel: P&L previsional a 3 años con fórmulas',
      'Inversión inicial detallada por partidas (~80K-150K EUR)',
      'Punto de equilibrio y análisis de viabilidad financiera',
      'Checklist apertura: 64 trámites y licencias España 2026',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      '9 secciones profesionales con datos reales del mercado español para construir la viabilidad financiera de tu bar-restaurante y presentarla a banco o inversores.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Excel (9 hojas)', desc: 'Hoja de supuestos que manda sobre todo el libro, P&L previsional a 3 años, inversión inicial, punto de equilibrio, escenarios, personal, tesorería mensual, cuadro de amortización del préstamo e instrucciones. Las celdas verdes se editan; el resto se calcula.' },
      { icon: 'Coins', title: 'Inversión Inicial Detallada', desc: 'Local, cocina, sala, marketing, legal y fondo de maniobra desglosados (~133K EUR de referencia para bar-restaurante medio en España).' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio (Break-Even)', desc: 'Cuántos cubiertos al día necesitas para cubrir costes fijos, margen de contribución e interpretación de resultados con sensibilidad a ticket medio.' },
      { icon: 'BarChart3', title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes ocupaciones y ticket medio para presentar a banco o inversores.' },
      { icon: 'Users', title: 'Cuadro de Personal y Costes', desc: 'Salarios brutos por puesto, Seguridad Social al 33 %, 14 pagas y coste real por jefe de cocina, jefe de sala, cocineros, camareros y ayudantes.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (7 fases)', desc: 'Constitución SL, licencias hostelería, obra y acondicionamiento, RRHH, marketing pre-apertura, obligaciones que hay que tener cerradas antes de abrir y primeros 90 días de operación.' },
      { icon: 'Globe', title: 'Análisis de Mercado España 2026', desc: '81K+ restaurantes activos, ticket medio por comunidad, inversión media por tipo de local y tasa de cierre en los 3 primeros años.' },
      { icon: 'FileText', title: 'Instrucciones y Ratios de Referencia', desc: 'Food cost 28-32 %, personal inferior a 35 %, alquiler inferior a 10 % y datos sectoriales para comparar con tu proyecto y detectar desviaciones.' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'Opciones reales: ICO, ENISA, préstamo bancario, inversores privados, business angels y subvenciones autonómicas con orden recomendado de gestión.' },
    ],
  },

  testimonials: {
    subtitle:
      'Emprendedores e inversores que usaron el plan de negocio para abrir su restaurante en España',
    items: [
      { name: 'Alejandro Ruiz', role: 'Propietario Bar-Restaurante Madrid', text: 'Presenté el plan financiero al banco y me aprobaron la financiación en 10 días. Las proyecciones a 3 años con escenarios les dieron mucha confianza. Inversión total: 135K EUR.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Emprendedora Hostelería Barcelona', text: 'El checklist de apertura me salvó meses de trabajo. 50+ trámites organizados por fases, desde constituir la SL hasta la licencia de actividad. No me dejé nada pendiente.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Inversor Restauración', text: 'Uso este plan como base para evaluar proyectos de restauración. El punto de equilibrio y los escenarios financieros son exactamente lo que necesito para tomar decisiones de inversión.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Directora Restaurante Sevilla', text: 'El cuadro de personal con Seg. Social al 33,4 % y 14 pagas me abrió los ojos. Antes subestimaba los costes laborales. Ahora tengo el equipo justo para ser rentable.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Consultor Hostelería', text: 'Lo recomiendo a todos mis clientes que quieren abrir un restaurante en España. Es el plan de negocio más completo y actualizado que he visto, con datos reales del mercado español.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Propietaria Gastrobar Valencia', text: 'Los ratios de referencia — food cost 28-32 %, personal inferior a 35 %, alquiler inferior a 10 % — me ayudaron a negociar mejor el local. Ahorré más de 300 EUR al mes en alquiler.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex Directivo que Abrió su Restaurante', text: 'Venía del mundo corporativo y no sabía nada de licencias hostelería. El checklist de apertura con las 6 fases me guió paso a paso. Abrí en 4 meses sin ningún problema legal.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Socio Fundador Grupo Restauración', text: 'Hemos usado el plan financiero Excel para 3 aperturas distintas. Solo cambias las cifras del local y tienes un business plan profesional listo para presentar a inversores.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado español para abrir un bar-restaurante con cabeza.',
    reasons: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Profesional', desc: 'No es una plantilla genérica. Es un plan financiero Excel con P&L previsional a 3 años, fórmulas activas y celdas editables. Cambias el alquiler o el ticket medio y todo se recalcula automáticamente.' },
      { icon: 'BarChart3', title: 'Datos Reales España 2026', desc: '81K+ restaurantes activos en España, ticket medio por comunidad autónoma, inversión media por tipo de local y tasa de cierre del sector en los primeros 3 años. No supuestos: cifras del mercado real.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura Completo', desc: '64 trámites organizados en 7 fases: constitución SL, licencias hostelería, obra, RRHH, marketing pre-apertura y primeros 90 días. No te dejas nada pendiente.' },
      { icon: 'Banknote', title: 'Listo para Banco e Inversores', desc: 'Es exactamente el formato que pide un banco para evaluar la financiación: P&L 3 años, punto de equilibrio, 3 escenarios, ratios financieros y plan de financiación. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a emprendedores, inversores y grupos de restauración en la apertura de bares-restaurantes en España, combinando experiencia operativa con análisis financiero profesional.',
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
        desc: 'Cuadro completo de personal con salarios brutos, Seguridad Social al 33 %, 14 pagas y coste real por puesto: jefe de cocina, jefe de sala, cocineros, camareros y ayudantes.',
        image: '/lovable-uploads/ai-gallery/plan-bar-restaurante-equipo.jpg',
      },
      {
        icon: 'BarChart3',
        label: 'BONUS 2',
        title: 'Análisis de Mercado España 2026',
        value: '€19',
        desc: 'Datos actualizados del sector: 81K+ restaurantes activos, ticket medio por comunidad autónoma, inversión media por tipo de local y tasa de cierre en los 3 primeros años.',
        image: '/lovable-uploads/ai-gallery/plan-bar-restaurante-interior.jpg',
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
      q: '¿Es un plan genérico o específico para bar-restaurante?',
      a: 'Es 100 % específico para bar-restaurante en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de bar-restaurante con barra y sala, incluyendo licencias de hostelería españolas actualizadas a 2026.',
    },
    {
      q: '¿Puedo presentar este plan al banco o a inversores?',
      a: 'Sí. El plan financiero Excel incluye cuenta de resultados (P&L) previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios (pesimista, realista, optimista). Es exactamente el formato que piden bancos e inversores para evaluar la financiación de un restaurante.',
    },
    {
      q: '¿Puedo modificar las cifras del Excel?',
      a: 'Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, el número de cubiertos, el ticket medio, los salarios y cualquier partida de inversión para adaptarlo a tu proyecto concreto. Incluye hoja de instrucciones.',
    },
    {
      q: '¿Qué trámites legales incluye el checklist de apertura?',
      a: '64 trámites organizados en 7 fases: constitución de la SL (notaría, registro mercantil, Hacienda), licencias municipales (actividad, terraza, música), obra y acondicionamiento (proyecto técnico, licencia de obra), RRHH (contratos, Seg. Social, PRL), marketing pre-apertura y primeros 90 días de operación.',
    },
    {
      q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
      a: 'Los planes gratuitos son plantillas genéricas sin datos reales. Este plan incluye cifras del mercado español 2026 (81K+ restaurantes, ticket medio, tasa de cierre), ratios financieros profesionales (food cost, personal, alquiler), cuadro de personal con Seg. Social y un checklist de trámites verificado con la legislación vigente.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu restaurante con total confianza.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Bar-Restaurante',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a emprendedores que ya abrieron su restaurante con un plan financiero profesional y un checklist de apertura completo.',
    items: [
      'Plan financiero Excel con P&L previsional a 3 años',
      'Inversión inicial detallada (~133K EUR de referencia)',
      'Punto de equilibrio + 3 escenarios (pesimista/realista/optimista)',
      'Checklist apertura con 64 trámites en 7 fases',
      'Análisis de mercado España 2026 con ratios sectoriales',
      'Plan de financiación: ICO, ENISA, banca, business angels',
      'BONUS: Cuadro Personal con Seg. Social (€19)',
      'BONUS: Análisis de Mercado España 2026 (€19)',
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

  stickyLabel: 'PLAN BAR-RESTAURANTE — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-plan-financiero', label: 'Kit Plan Financiero' },
    { href: '/guia-restaurante-casual', label: 'Guía Restaurante Casual' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.2 · septiembre 2026',

  alreadyBought: {
    product: 'plan-negocio-bar-restaurante',
    label: '¿Ya compraste el Plan de Negocio Bar-Restaurante? Vuelve a entrar al dashboard',
  },
};

export default data;
