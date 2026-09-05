// astro-site/src/data/productos/planes/plan-negocio-cafeteria.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioCafeteria.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-cafeteria/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-cafeteria.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (título/subtítulo constantes de línea, hardcodeados en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Hacer Realidad tu ' (patrón de la sub-línea A).
//   · authorBadges se OMITE → cae en el default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],
//     que es EXACTAMENTE el par de este producto.
//   · hero.titlePost se omite (Forma B: titlePre + gold + titleSubtitle en bloque).
//   · images.gridGallery se OMITE: el set de 6 imágenes del ContentGrid de la SPA es IDÉNTICO
//     al hero salvo el orden (interior/latte/brunch/barra/bolleria/terraza vs hero
//     hero/latte/brunch/barra/bolleria/interior) — NO es un set nuevo, reutiliza las mismas 7
//     imágenes cafetería con una imagen (terraza) que el hero no usa. Como el template cae en
//     `gallery` si se omite gridGallery, y la SPA SÍ tiene un orden distinto en ContentGrid,
//     se declara explícitamente para paridad byte a byte (ver bloque `images` abajo).
//
// QUIRK VERBATIM: schema.faqs (FAQPage JSON-LD) = 4 preguntas (subconjunto), mientras que faqs
// on-page (acordeón) = 6 preguntas. Cada bloque copiado según su origen en la SPA.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-cafeteria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_CAFETERIA',

  seo: {
    title:
      'Plan de Negocio: Cafetería / Brunch — Plan Financiero Excel + Checklist Apertura | AI Chef Pro',
    description:
      'Plan de negocio completo para abrir una cafetería o brunch en España 2026. Plan financiero Excel con P&L 3 años, tesorería a 12 meses, plan de financiación, punto de equilibrio en 84 clientes/día y checklist de apertura con 75 trámites bajo licencia inocua. €29.',
    keywords:
      'plan de negocio cafetería, plan financiero brunch España, abrir cafetería, checklist apertura cafetería, licencia inocua hostelería, máquina espresso profesional, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-cafeteria.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio: Cafetería / Brunch — Plan Financiero Excel, Inversión Inicial y Checklist Apertura',
    productDescription:
      'Plan de negocio completo para abrir una cafetería o brunch en España. Incluye plan financiero Excel de 9 hojas con P&L previsional a 3 años, inversión inicial detallada (130.176 €: 91.650 € de CAPEX más 38.526 € de fondo de maniobra), punto de equilibrio en 84 clientes/día con ticket medio de 9,80 € sin IVA (10,78 € de PVP), escenarios financieros, tesorería a 12 meses con liquidación de IVA, plan de financiación con cuadro de amortización y DSCR, cuadro de personal con Seguridad Social, checklist de apertura con 75 trámites bajo licencia de actividad inocua y registro sanitario autonómico, equipamiento específico cafetería y ratios sectoriales del mercado español 2026.',
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
        body: 'El plan financiero me ayudó a conseguir financiación ICO. El desglose de inversión en máquina de café, horno y mobiliario era exacto.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'Gracias al checklist no se me pasó ningún trámite. La licencia de actividad inocua fue clave para abrir rápido.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'El punto de equilibrio de 53 clientes/día con ticket medio €9,50 es realista. Números que cuadran con el mercado.',
      },
    ],
    // FAQPage schema (4 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6)
    faqs: [
      {
        q: '¿Es un plan genérico o específico para cafetería?',
        a: 'Es 100% específico para cafetería y brunch en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de cafetería con barra, sala y terraza.',
      },
      {
        q: '¿Puedo presentar este plan al banco o a inversores?',
        a: 'Sí. Incluye P&L 3 años, punto de equilibrio y 3 escenarios. Es exactamente el formato que piden bancos e inversores.',
      },
      {
        q: '¿Qué trámites legales incluye el checklist?',
        a: '75 trámites en 6 fases: constitución de la SL, licencias municipales (inocua + registro sanitario autonómico + terraza), equipamiento, RRHH, marketing pre-apertura y primeros 90 días.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio: Cafetería / Brunch',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-cafeteria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-latte.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-bolleria.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-interior.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (termina en -terraza en vez de -interior)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-cafeteria-interior.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-latte.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-bolleria.jpg',
      '/lovable-uploads/ai-gallery/plan-cafeteria-terraza.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-cafeteria-barra.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-cafeteria-brunch.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-cafeteria-hero.jpg',
  },

  hero: {
    badge: 'El plan de negocio más completo para abrir tu cafetería o brunch',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Cafetería / Brunch',
    titleSubtitle: 'Plan Financiero Excel, Inversión Inicial y Checklist de Apertura',
    description:
      'El plan de negocio completo para abrir una cafetería o brunch en España. Plan financiero Excel con P&L a 3 años, inversión inicial detallada, tesorería a 12 meses, plan de financiación, punto de equilibrio en 84 clientes/día y checklist de apertura con 75 trámites bajo licencia de actividad inocua.',
    checkItems: [
      'Plan financiero Excel: P&L previsional a 3 años con fórmulas',
      'Inversión inicial detallada por partidas (130.176 €, fondo de maniobra incluido)',
      'Punto de equilibrio: 84 clientes/día con ticket medio de 9,80 € sin IVA',
      'Checklist apertura: 75 trámites y licencias España 2026',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €29',
  },

  grid: {
    subtitle:
      '9 secciones profesionales con datos reales del mercado español para construir la viabilidad financiera de tu cafetería o brunch y presentarla a banco o inversores.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Excel (9 hojas)', desc: 'Supuestos, inversión inicial, P&L previsional a 3 años, punto de equilibrio, escenarios, cuadro de personal, tesorería a 12 meses, plan de financiación e instrucciones. 739 fórmulas enlazadas: cambias una celda verde y se recalcula el libro entero.' },
      { icon: 'Coins', title: 'Inversión Inicial Detallada', desc: 'Local, máquina de café, horno, vitrina refrigerada, mobiliario, terraza y fondo de maniobra desglosados (130.176 € de referencia: 91.650 € de CAPEX más 38.526 € de fondo de maniobra), con el IVA soportado y la necesidad total de caja calculados aparte.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio (Break-Even)', desc: '84 clientes al día con ticket medio de 9,80 € sin IVA (79 en el umbral de caja, con la cuota del préstamo dentro). Cálculo de margen de seguridad, tabla de sensibilidad al ticket y al coste variable, e interpretación de resultados.' },
      { icon: 'BarChart3', title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes de clientes y ticket medio. Útil para presentar a banco e inversores.' },
      { icon: 'Users', title: 'Cuadro de Personal y Costes', desc: 'Seis puestos —propietario-barista, barista de mañana, camarero de tarde, ayudante de brunch, extra de fin de semana y suplencias— con salarios brutos, Seguridad Social al 33 %, 14 pagas, coste real por puesto y dos semáforos: suelo del SMI por jornada y cobertura de las horas de servicio.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, licencia de actividad inocua, RGSEAA, terraza, equipamiento, RRHH, marketing pre-apertura y primeros 90 días.' },
      { icon: 'Wrench', title: 'Equipamiento Específico Cafetería', desc: 'Máquina espresso 2 grupos, molinillo profesional, horno de convección, vitrina refrigerada para bollería y mobiliario, con marcas de referencia y precios.' },
      { icon: 'ListChecks', title: 'Ratios de Referencia Cafetería', desc: 'Food cost café 25-30 %, ticket medio €8-12, margen bruto >65 %, rotación por franja horaria (mañana / mediodía / tarde) y datos del sector.' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'Opciones reales: ICO, ENISA, préstamo bancario, inversores privados, business angels y subvenciones autonómicas con orden recomendado de gestión.' },
    ],
  },

  testimonials: {
    subtitle:
      'Propietarios e inversores que abrieron su cafetería o brunch con un plan financiero profesional',
    items: [
      { name: 'Alejandro Ruiz', role: 'Propietario Cafetería Specialty Madrid', text: 'El plan financiero me ayudó a conseguir financiación ICO. El desglose de inversión en máquina de café, horno y mobiliario era exacto, sin sorpresas.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Emprendedora Brunch Barcelona', text: 'Gracias al checklist de apertura no se me pasó ningún trámite. La licencia de actividad inocua fue clave para abrir rápido y sin retrasos.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Inversor Hostelería', text: 'El punto de equilibrio de 53 clientes/día con ticket medio €9,50 es realista. Números que cuadran con el mercado real de cafeterías.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Socia Cafetería Brunch Sevilla', text: 'Los escenarios financieros nos dieron confianza para firmar el alquiler. Sabíamos exactamente cuánto necesitábamos facturar para ser rentables.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Consultor Hostelería', text: 'Lo recomiendo a todo emprendedor que quiera abrir una cafetería en España. Datos reales del sector, no plantillas de relleno.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Propietaria Coffee Shop Valencia', text: 'Los ratios de café (food cost 25-30 %) y el cuadro de personal con SS me ahorraron errores de miles de euros antes de firmar nada.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex Corporativo, Abrió Cafetería Brunch', text: 'No sabía nada de licencias hostelería. El checklist con las 6 fases me guió paso a paso. Abrí en 3 meses sin ningún problema legal.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Dueño Cadena 3 Cafeterías', text: 'Hemos usado el plan financiero Excel para nuestras 3 aperturas. Solo cambias la ubicación y tienes un business plan profesional listo para presentar.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado español para abrir una cafetería o brunch con cabeza.',
    reasons: [
      { icon: 'Coffee', title: 'Plan Específico para Café', desc: 'No es una plantilla genérica. Está adaptado al modelo cafetería/brunch: máquina espresso 2 grupos, vitrina de bollería, ratios food cost de café (25-30 %) y ticket medio realista €8-12.' },
      { icon: 'BarChart3', title: 'Datos Reales Cafetería 2026', desc: 'Ticket medio de 9,80 € sin IVA (10,78 € de PVP), food cost café 25-30 %, margen bruto del 66 %, rotación por franja horaria (mañana, mediodía, tarde) y break-even en 84 clientes/día. Cifras del mercado español real.' },
      { icon: 'ShieldCheck', title: 'Licencia Inocua + 75 Trámites', desc: 'Cafetería entra en licencia de actividad inocua (más rápida que clasificada). Checklist con 75 trámites en 6 fases incluyendo el registro sanitario autonómico, la terraza, el RGPD y la adaptación a Veri*factu.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a propietarios de cafeterías, brunch y coffee shops en España, combinando experiencia operativa con análisis financiero profesional para garantizar viabilidad y rentabilidad desde el primer día.',
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
        desc: 'Cuadro completo de personal con salarios brutos, Seguridad Social al 33 %, 14 pagas y coste real por puesto, con el suelo del SMI y la cobertura de horas comprobados fila a fila: propietario-barista, baristas, camareros, ayudante de brunch y suplencias.',
        image: '/lovable-uploads/ai-gallery/plan-cafeteria-barra.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Ratios de Referencia Cafetería 2026',
        value: '€19',
        desc: 'Datos actualizados del sector: food cost café 25-30 %, ticket medio €8-12, margen bruto >65 % y rotación por franja horaria (mañana / mediodía / tarde).',
        image: '/lovable-uploads/ai-gallery/plan-cafeteria-latte.jpg',
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
      q: '¿Es un plan genérico o específico para cafetería?',
      a: 'Es 100 % específico para cafetería y brunch en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de cafetería con barra, sala y terraza, incluyendo la licencia de actividad inocua y el registro sanitario de tu Comunidad Autónoma (el RGSEAA estatal no aplica al minorista que sirve al consumidor final: art. 2.2 del RD 191/2011).',
    },
    {
      q: '¿Puedo presentar este plan al banco o a inversores?',
      a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. Es exactamente el formato que piden bancos e inversores para evaluar la financiación de una cafetería.',
    },
    {
      q: '¿Puedo modificar las cifras del Excel?',
      a: 'Sí. Las celdas VERDES son las que se teclean —alquiler, clientes al día, ticket medio, salarios y cualquier partida de inversión— y las 739 fórmulas del libro recalculan el resto solo. Si quieres tocar una celda calculada, Revisar → Desproteger hoja (no lleva contraseña). Incluye hoja de instrucciones.',
    },
    {
      q: '¿Qué trámites legales incluye el checklist de apertura?',
      a: '75 trámites organizados en 6 fases: constitución de la SL (notaría, registro mercantil, Hacienda, Veri*factu y registro de tratamientos del RGPD), licencias municipales (licencia inocua, registro sanitario autonómico, terraza, residuos y DDD), equipamiento (proyecto técnico, instalaciones), RRHH (contratos, Seg. Social, PRL y registro horario), marketing pre-apertura y primeros 90 días.',
    },
    {
      q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
      a: 'Los planes gratuitos son plantillas genéricas sin datos reales. Este plan incluye cifras del mercado español 2026, ratios financieros específicos de cafetería (food cost café 25-30 %, ticket medio €8-12), cuadro de personal con Seg. Social y un checklist de 75 trámites verificado con la legislación vigente.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu cafetería con total confianza.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Cafetería',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a propietarios que ya abrieron su cafetería o brunch con un plan financiero profesional y un checklist de apertura completo.',
    items: [
      'Plan financiero Excel con P&L previsional 3 años',
      'Inversión inicial detallada (130.176 € de referencia)',
      'Punto de equilibrio: 84 clientes/día con ticket de 9,80 € sin IVA',
      '3 escenarios financieros (pesimista/realista/optimista)',
      'Checklist apertura con 75 trámites en 6 fases',
      'Equipamiento específico cafetería + ratios sectoriales',
      'BONUS: Cuadro Personal con Seg. Social (€19)',
      'BONUS: Ratios Referencia Cafetería 2026 (€19)',
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

  stickyLabel: 'PLAN CAFETERÍA — €29',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: '/kit-tareas-cafeteria', label: 'Kit Tareas Cafetería' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.2 · septiembre 2026',

  alreadyBought: {
    product: 'plan-negocio-cafeteria',
    label: '¿Ya compraste el Plan de Negocio Cafetería? Vuelve a entrar al dashboard',
  },
};

export default data;
