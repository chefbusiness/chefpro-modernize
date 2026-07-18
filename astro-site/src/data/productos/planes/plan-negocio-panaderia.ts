// astro-site/src/data/productos/planes/plan-negocio-panaderia.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioPanaderia.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-panaderia/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-panaderia.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (título/subtítulo constantes de línea, hardcodeados en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Hacer Realidad tu ' (patrón de la sub-línea A).
//   · authorBadges se OMITE → cae en el default ['Consultor Gastronómico', '+29 años en alta hostelería'],
//     que es EXACTAMENTE el par de este producto.
//   · hero.titlePost se omite (Forma B: titlePre + gold + titleSubtitle en bloque).
//   · images.gridGallery DIFIERE del hero (swap: sale -hero, entra -tienda; distinto orden).
//
// QUIRK VERBATIM: schema.faqs (FAQPage JSON-LD) = 4 preguntas (subconjunto), mientras que faqs on-page
// (acordeón) = 6 preguntas. Cada bloque copiado según su origen en la SPA.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-panaderia',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA',

  seo: {
    title:
      'Plan de Negocio: Panadería / Obrador — Plan Financiero Excel + Checklist Apertura | AI Chef Pro',
    description:
      'Plan de negocio completo para abrir una panadería u obrador artesanal en España 2026. Plan financiero Excel con P&L 3 años + estacionalidad navideña, inversión inicial, punto de equilibrio por kilos diarios y checklist apertura con 60+ trámites incluyendo RGSEAA obrador. €35.',
    keywords:
      'plan de negocio panadería, plan financiero obrador artesanal, abrir panadería España, RGSEAA obrador, horno pisos rotativo, masa madre, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-panaderia.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio: Panadería / Obrador — Plan Financiero Excel, Inversión Inicial y Checklist Apertura',
    productDescription:
      'Plan de negocio completo para abrir una panadería u obrador artesanal en España. Incluye plan financiero Excel con P&L previsional a 3 años con estacionalidad navideña, inversión inicial detallada (~88K EUR), punto de equilibrio por kilos diarios con ticket €4,50, escenarios financieros, cuadro de personal panadero con turno madrugada y plus de nocturnidad, checklist de apertura con 60+ trámites incluyendo RGSEAA obrador, equipamiento específico (horno de pisos rotativo, amasadora 40-80kg, cámara fermentación) y ratios sectoriales del mercado panadero español 2026.',
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
        body: 'Presenté el plan al banco y me aprobaron 65K EUR de financiación con leasing del horno. La proyección a 3 años con estacionalidad navideña fue clave.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El checklist con 60+ trámites me salvó del laberinto del RGSEAA y la licencia de obrador. Hubiera tardado el doble.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'El break-even por kilos de pan diarios y el mix bollería son exactamente los ratios que necesito ver.',
      },
    ],
    // FAQPage schema (4 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6)
    faqs: [
      {
        q: '¿Es un plan genérico o específico para panadería?',
        a: 'Es 100% específico para panadería y obrador artesanal en España. Las partidas de inversión, ratios financieros, costes de personal con turno madrugada y trámites legales (RGSEAA obrador, licencia actividad) están adaptados al modelo panadero.',
      },
      {
        q: '¿Puedo presentar este plan al banco o a inversores?',
        a: 'Sí. Incluye P&L 3 años con estacionalidad navideña, punto de equilibrio por kilos diarios y 3 escenarios. Es el formato que piden bancos para microcrédito ICO y leasing de horno y amasadora.',
      },
      {
        q: '¿Qué trámites legales incluye el checklist?',
        a: 'Más de 60 trámites en 6 fases: constitución SL, RGSEAA obrador, licencias municipales, equipamiento (proyecto técnico, salida de humos), RRHH (turno madrugada, PRL nocturnidad) y primeros 90 días.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio: Panadería / Obrador',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-panaderia-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-masa.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -tienda)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-panaderia-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-masa.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-tienda.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-panaderia-hero.jpg',
  },

  hero: {
    badge: 'El plan de negocio más completo para abrir tu panadería u obrador',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Panadería / Obrador',
    titleSubtitle: 'Plan Financiero Excel, Inversión Inicial y Checklist de Apertura',
    description:
      'El plan de negocio completo para abrir una panadería u obrador artesanal en España. Plan financiero Excel con P&L a 3 años y estacionalidad navideña, inversión inicial detallada, punto de equilibrio por kilos diarios y checklist de apertura con 60+ trámites incluyendo RGSEAA obrador y salida de humos.',
    checkItems: [
      'Plan financiero Excel: P&L 3 años con estacionalidad navideña',
      'Inversión inicial detallada por partidas (~70K-110K EUR)',
      'Punto de equilibrio por kilos diarios con ticket medio €4,50',
      'Checklist apertura: 60+ trámites incluyendo RGSEAA obrador',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      '9 secciones profesionales con datos reales del mercado panadero español para construir la viabilidad financiera de tu panadería u obrador y presentarla a banco o inversores.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años con estacionalidad navideña, inversión inicial, punto de equilibrio, escenarios, cuadro de personal panadero e instrucciones. Todas las celdas editables.' },
      { icon: 'Coins', title: 'Inversión Inicial Detallada', desc: 'Local, horno profesional de pisos, amasadora 40-80 kg, cámara de fermentación controlada, expositor refrigerado, mobiliario y fondo de maniobra (~88K EUR de referencia).' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio (Break-Even)', desc: 'Cálculo por kilos de pan diarios y unidades de bollería con ticket medio €4,50, margen de seguridad e interpretación de resultados con sensibilidad al mix de producción.' },
      { icon: 'BarChart3', title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes de producción y mix barra/bollería/cafetería para presentar a banco e inversores.' },
      { icon: 'Users', title: 'Cuadro de Personal Panadero', desc: 'Maestro panadero, oficial, ayudante de obrador y dependiente con salarios brutos, Seguridad Social al 33,4 %, 14 pagas, turno madrugada y plus de nocturnidad.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, RGSEAA obrador (Registro General Sanitario), licencias municipales, equipamiento (proyecto técnico, salida de humos), RRHH y primeros 90 días.' },
      { icon: 'Wrench', title: 'Equipamiento Específico Panadería', desc: 'Horno de pisos rotativo (Salva, Eurofours), amasadora 40-80 kg, cámara de fermentación controlada y expositor refrigerado, con marcas de referencia y precios.' },
      { icon: 'ListChecks', title: 'Ratios de Referencia Panadería', desc: 'Coste materia prima 22-28 %, personal <38 %, merma 3-5 %, margen bruto pan >70 % y bollería >75 %. Datos del sector panadero español 2026.' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'Opciones reales: ICO, ENISA, préstamo bancario, leasing de equipamiento (horno, amasadora), inversores privados y subvenciones autonómicas para obrador.' },
    ],
  },

  testimonials: {
    subtitle:
      'Maestros panaderos, propietarios de obrador artesanal e inversores que abrieron su panadería con un plan financiero profesional',
    items: [
      { name: 'Alejandro Ruiz', role: 'Maestro Panadero Madrid', text: 'Presenté el plan al banco y me aprobaron 65K EUR de financiación con leasing del horno. La proyección a 3 años con estacionalidad navideña fue clave para que confiaran en el proyecto.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Emprendedora Obrador Barcelona', text: 'El checklist con 60+ trámites me salvó del laberinto del RGSEAA y la licencia de obrador. Hubiera tardado el doble sin esta guía organizada por fases.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Inversor Sector Alimentación', text: 'Uso este plan para evaluar proyectos de panadería en mi cartera. El break-even por kilos de pan diarios y el mix bollería son exactamente los ratios que necesito ver.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Propietaria Panadería Artesanal Sevilla', text: 'El cuadro de personal con turno madrugada y plus nocturnidad me abrió los ojos. Antes calculaba mal los costes del maestro panadero. Ahora margen real superior al 25 %.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Consultor Hostelería y Obradores', text: 'Lo recomiendo a todos mis clientes panaderos. Es el plan más completo del mercado español con datos reales del sector: ratios materia prima, mermas y márgenes por categoría.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Propietaria Panadería con Cafetería Valencia', text: 'Los ratios — coste materia prima 22-28 %, merma 3-5 %, margen bollería >75 % — me ayudaron a renegociar precios con el molino harinero. Ahorré 800 EUR al mes.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex Corporativo, Abrió Obrador Pan', text: 'Venía del mundo financiero y no sabía nada de licencias de obrador ni RGSEAA. El checklist con las 6 fases me guió paso a paso. Abrí en 4 meses sin retrasos legales.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Socio Cadena 3 Panaderías', text: 'Hemos usado el plan financiero Excel para nuestras 3 aperturas. Solo cambias las cifras del local y mix de producción y tienes business plan profesional listo para inversores.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado panadero español para abrir una panadería u obrador con cabeza.',
    reasons: [
      { icon: 'Wheat', title: 'Plan Específico Panadero', desc: 'No es plantilla genérica. Adaptado al modelo panadería/obrador: horno profesional, amasadora 40-80 kg, cámara fermentación, mix barra/bollería/cafetería y estacionalidad navideña.' },
      { icon: 'BarChart3', title: 'Datos Reales Sector 2026', desc: 'Materia prima 22-28 %, merma 3-5 %, margen pan >70 %, bollería >75 %, ticket medio €4,50 y break-even por kilos diarios. Cifras del mercado panadero español real.' },
      { icon: 'ShieldCheck', title: 'RGSEAA Obrador + 60 Trámites', desc: 'Panadería con obrador requiere RGSEAA (Registro General Sanitario), licencia clasificada, salida de humos y proyecto técnico. Checklist con 60+ trámites en 6 fases.' },
      { icon: 'Banknote', title: 'Listo para Banco e Inversores', desc: 'P&L 3 años, punto de equilibrio, 3 escenarios y plan de financiación con ICO, ENISA, leasing de horno y subvenciones autonómicas. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha asesorado a maestros panaderos, propietarios de obrador artesanal y cadenas de panaderías en España, combinando experiencia operativa con análisis financiero profesional para garantizar la viabilidad y rentabilidad del negocio panadero.',
  // authorBadges omitido → default ['Consultor Gastronómico', '+29 años en alta hostelería'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y el checklist de apertura, accedes a estos recursos extra — valorados en €38',
    items: [
      {
        icon: 'Users',
        label: 'BONUS 1',
        title: 'Cuadro de Personal Panadero con Plus Nocturnidad',
        value: '€19',
        desc: 'Cuadro completo de personal con salarios brutos, Seguridad Social al 33,4 %, 14 pagas, turno madrugada y plus de nocturnidad: maestro panadero, oficial, ayudante de obrador y dependiente.',
        image: '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Ratios de Referencia Sector Panadero 2026',
        value: '€19',
        desc: 'Datos actualizados del sector: coste materia prima 22-28 %, merma 3-5 %, margen pan >70 %, margen bollería >75 %, ticket medio €4,50 y mix consumo barra/bollería/cafetería.',
        image: '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
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
      q: '¿Es un plan genérico o específico para panadería?',
      a: 'Es 100 % específico para panadería y obrador artesanal en España. Las partidas de inversión (horno profesional, amasadora, cámara fermentación), los ratios financieros (coste materia prima, merma, margen pan vs bollería), los costes de personal con turno madrugada y los trámites legales (RGSEAA obrador, licencia actividad) están adaptados al modelo panadero.',
    },
    {
      q: '¿Puedo presentar este plan al banco o a inversores?',
      a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años con estacionalidad navideña, punto de equilibrio por kilos diarios, análisis de viabilidad financiera y 3 escenarios. Es exactamente el formato que piden bancos para microcrédito o ICO emprendedores y leasing de equipamiento (horno, amasadora).',
    },
    {
      q: '¿Puedo modificar las cifras del Excel?',
      a: 'Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, los kilos producidos al día, el ticket medio, los salarios del maestro panadero y cualquier partida de inversión. Incluye hoja de instrucciones.',
    },
    {
      q: '¿Qué trámites legales incluye el checklist de apertura?',
      a: 'Más de 60 trámites organizados en 6 fases: constitución de la SL, RGSEAA obrador (Registro General Sanitario), licencias municipales (actividad, expositor en fachada), equipamiento (proyecto técnico, instalación de horno, salida de humos), RRHH (contratos panaderos, Seg. Social, PRL turno madrugada) y primeros 90 días de operación.',
    },
    {
      q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
      a: 'Los planes gratuitos son plantillas genéricas sin datos reales del sector panadero. Este plan incluye cifras del mercado español 2026 (10K+ panaderías, mix consumo barra/bollería/cafetería, tasa de cierre), ratios profesionales (materia prima 22-28 %, merma 3-5 %, margen pan >70 %, bollería >75 %), cuadro de personal con turno madrugada y un checklist de trámites verificado con la legislación obrador vigente.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu panadería con total confianza.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Panadería',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a maestros panaderos y emprendedores que ya abrieron su panadería u obrador artesanal con un plan financiero profesional.',
    items: [
      'Plan financiero Excel con P&L 3 años + estacionalidad navideña',
      'Inversión inicial detallada (~88K EUR de referencia)',
      'Punto de equilibrio por kilos diarios con ticket €4,50',
      '3 escenarios financieros (pesimista/realista/optimista)',
      'Checklist apertura con 60+ trámites incluyendo RGSEAA',
      'Equipamiento específico panadería + ratios sectoriales',
      'BONUS: Cuadro Personal Panadero con plus nocturnidad (€19)',
      'BONUS: Ratios Referencia Sector Panadero 2026 (€19)',
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

  stickyLabel: 'PLAN PANADERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: '/kit-tareas-panaderia', label: 'Kit Tareas Panadería' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'plan-negocio-panaderia',
    label: '¿Ya compraste el Plan de Negocio Panadería? Vuelve a entrar al dashboard',
  },
};

export default data;
