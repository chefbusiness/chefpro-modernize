// guia-dark-kitchen.ts — Copy VERBATIM de src/pages/GuiaDarkKitchen.tsx + componentes de
// src/components/guia-dark-kitchen/* + data/testimonials-guia-dark-kitchen.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
//
// DIVERGENCIAS vs producto de referencia (guia-restaurante-gastronomico), todas cubiertas
// por las props opcionales de types.ts:
//  1. showCompatibleApps = true (único de la línea que renderiza <CompatibleAppsMarquee variant="tareas">).
//  2. bonus.layout = 'single' (3 bonus, grid-cols-3 max-w-4xl — NO split).
//  3. schema.breadcrumb = 2 ítems (AI Chef Pro → guía; NO pasa por "Productos Digitales").
//  4. hero.avatarAltPrefix = default 'Professional' (HeroSection.tsx usa `Professional ${i+1}`).
//  5. testimonials.titleGold = 'Profesionales' (igual que el default de la línea).
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-dark-kitchen',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_DARK_KITCHEN',

  seo: {
    title: 'Cómo Montar una Dark Kitchen en España — Guía Completa | AI Chef Pro',
    description: 'Guía completa para montar una dark kitchen en España: 12 capítulos, requisitos legales, plan financiero, diseño de cocina, tecnología, marketing y 3 checklists Excel. 24 EUR.',
    keywords: 'como montar dark kitchen, abrir dark kitchen españa, ghost kitchen, cloud kitchen, cocina fantasma, dark kitchen madrid, dark kitchen barcelona, montar negocio delivery, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-dark-kitchen.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'Las dark kitchens crecen un 25% anual en España — pero el 40% cierra el primer año',
    titlePre: 'Cómo Montar una ',
    titleGold: 'Dark Kitchen',
    subtitleLine: 'De la Idea a la Primera Entrega en 90 Días',
    description: 'Guía completa con 12 capítulos, 3 checklists Excel, calculadora de viabilidad e infografías. Todo lo que necesitas para abrir tu dark kitchen sin cometer los errores que cuestan miles de euros.',
    checkItems: [
      'Guía completa PDF + DOCX editable (12 capítulos, +40 páginas)',
      'Checklist de apertura legal: 35 trámites paso a paso',
      'Checklist de equipamiento y obra con presupuesto real',
      'Calculadora de viabilidad financiera con 3 escenarios',
      'Infografías: layout de cocina + timeline de 90 días',
    ],
    ctaLabel: 'COMPRAR GUÍA — 24 EUR',
  },

  pricing: {
    priceOld: '90 EUR',
    price: '24 EUR',
    discountBadge: '-73%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71% de descuento',
    bonusTotalLabel: 'Valor total: guía + 3 bonus',
    bonusSaveLine: 'Ahorra 66 EUR HOY',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-dk-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-dk-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-dk-packaging.jpg',
      '/lovable-uploads/ai-gallery/guia-dk-tablets.jpg',
      '/lovable-uploads/ai-gallery/guia-dk-delivery.jpg',
      '/lovable-uploads/ai-gallery/guia-dk-plano.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-dk-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-dk-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-dk-delivery.jpg',
  },

  grid: {
    countGold: '12',
    headingRest: ' Capítulos + 3 Checklists + Calculadora',
    subtitle: 'Todo lo que necesitas saber para montar tu dark kitchen en España, escrito por un profesional con 29 años en hostelería.',
    chapters: [
      { icon: 'Building2', num: '01', title: '¿Qué es una Dark Kitchen?', desc: 'Definiciones, origen del modelo y diferencias clave con un restaurante tradicional.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado Delivery en España', desc: 'Datos de Glovo, Uber Eats, Just Eat. Ciudades con mayor demanda y ticket medio.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio', desc: 'Marca única, multi-marca, cocina compartida, franquicia virtual. Pros y contras.' },
      { icon: 'Calculator', num: '04', title: 'Viabilidad y Plan Financiero', desc: 'Inversión (30K-80K€), costes, break-even y márgenes reales tras comisiones.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales en España', desc: 'Licencia de actividad, registro sanitario, Hacienda, seguros, LOPD.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC obligatorio, trazabilidad, alérgenos, temperaturas, inspecciones.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas industriales vs. comerciales, metros mínimos, ventilación, acceso riders.' },
      { icon: 'Layout', num: '08', title: 'Diseño y Layout de Cocina', desc: 'Flujo delivery-only: recepción, preparación, emplatado, expedición.' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento y Proveedores', desc: 'Lista completa con costes: hornos, freidoras, cámaras, estanterías.' },
      { icon: 'Tablet', num: '10', title: 'Tecnología y Gestión de Pedidos', desc: 'Integradores, TPV, KDS, gestión de stock, automatización.' },
      { icon: 'Package', num: '11', title: 'Packaging y Sostenibilidad', desc: 'Envases delivery, temperatura de llegada, branding, normativa plásticos 2026.' },
      { icon: 'Rocket', num: '12', title: 'Marketing y Lanzamiento', desc: 'Alta en plataformas, fotos, promos de lanzamiento y 10 errores fatales.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Emprendedores, consultores e inversores que ya usaron esta guía para abrir dark kitchens',
    items: [
      { name: 'Sergio Molina', role: 'Fundador de dark kitchen multi-marca en Madrid', text: 'Ojalá hubiese tenido esta guía antes de abrir. Me habría ahorrado 15.000€ en errores de ubicación y equipamiento. El capítulo de viabilidad financiera es oro puro.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Patricia Herrera', role: 'Consultora de nuevos negocios hosteleros', text: 'La uso con todos mis clientes que quieren abrir una dark kitchen. El checklist legal y la calculadora de viabilidad son imprescindibles para cualquier plan de negocio.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Daniel Marcos', role: 'Chef y emprendedor, 2 dark kitchens en Barcelona', text: 'El capítulo de diseño de cocina me abrió los ojos. El flujo de trabajo delivery-only es completamente diferente al de un restaurante.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Sánchez', role: 'Directora de expansión, cadena de delivery', text: 'La sección de tecnología y gestión de pedidos es brutal. Integrador de plataformas, KDS, gestión de stock... todo lo que necesitas para no ahogarte en tablets.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Roberto Jiménez', role: 'Propietario, restaurante casual + dark kitchen', text: 'Abrí la dark kitchen como extensión de mi restaurante. La guía me ayudó a evitar los errores típicos: ubicación cara, equipamiento innecesario, packaging equivocado.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Carmen Vidal', role: 'Asesora fiscal especializada en hostelería', text: 'El capítulo de requisitos legales es el más completo que he visto en español. Licencias, registro sanitario, APPCC, seguros... todo paso a paso con plazos reales.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Alejandro Torres', role: 'Inversor, fondo de hostelería', text: 'Pedimos esta guía a todos los emprendedores que nos presentan proyectos de dark kitchen. Si no han hecho los números del capítulo 4, no les financiamos.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Diego Ruiz', role: 'Chef, dark kitchen vegana en Valencia', text: 'Los 10 errores fatales del último capítulo son 100% reales. Yo cometí 4 de ellos en mi primera dark kitchen. Con esta guía, en la segunda no cometí ninguno.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'Utensils', title: 'Escrita por un Profesional', desc: '29 años en alta hostelería y 15 años de consultoría gastronómica. No es teoría: es experiencia real asesorando aperturas de dark kitchens.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (30K-80K€), márgenes después de comisiones de plataformas (25-35%), y punto de equilibrio calculado con datos del mercado español.' },
      { icon: 'ShieldCheck', title: 'Requisitos Legales Actualizados', desc: 'Licencias, APPCC, registro sanitario, seguros — todo actualizado a 2026 para España, con diferencias por comunidad autónoma.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000€. Esto es 24€', desc: 'La misma información que reciben los clientes de consultoría, pero en formato guía por un pago único. Sin suscripción.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años en alta hostelería y 15 años en consultoría gastronómica. Ha asesorado la apertura de más de 200 establecimientos hosteleros, incluyendo dark kitchens multi-marca en Madrid, Barcelona y Valencia.',
    badge3: '+200 aperturas asesoradas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 3 recursos Excel — valorados en 47 EUR',
    layout: 'single',
    items: [
      { icon: 'ClipboardList', label: 'BONUS 1', title: 'Checklist de Apertura Legal', value: '24 EUR', desc: '35 trámites organizados por categoría: constitución, licencias municipales, sanidad, seguros, Hacienda, protección de datos y APPCC. Con estado, responsable y fecha límite.', image: '/lovable-uploads/ai-gallery/guia-dk-tablets.jpg' },
      { icon: 'Wrench', label: 'BONUS 2', title: 'Checklist de Equipamiento y Obra', value: '24 EUR', desc: '40 ítems con presupuesto real: obra civil, instalaciones, cocina caliente, cocina fría, almacenamiento, expedición y tecnología. Presupuesto vs real con % de desviación.', image: '/lovable-uploads/ai-gallery/guia-dk-cocina.jpg' },
      { icon: 'Calculator', label: 'BONUS 3', title: 'Calculadora de Viabilidad Financiera', value: '19 EUR', desc: 'Inversión inicial, P&L mensual con comisiones de plataformas y punto de equilibrio automático con 3 escenarios (pesimista, realista, optimista).', image: '/lovable-uploads/ai-gallery/guia-dk-plano.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 24 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu dark kitchen, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
  },

  faqs: [
    { q: '¿Incluye los requisitos legales actualizados a 2026?', a: 'Sí. La guía cubre licencias de actividad, registro sanitario, alta en Hacienda, APPCC obligatorio, seguros y normativa de plásticos 2026. Actualizada para España con diferencias por CCAA.' },
    { q: '¿El DOCX es editable? ¿Puedo personalizarlo?', a: 'Sí. Recibes dos versiones: el PDF editorial (diseño profesional para leer) y el DOCX editable (para personalizar, añadir notas, adaptar a tu proyecto y presentar a socios o bancos).' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. La calculadora de viabilidad calcula automáticamente el punto de equilibrio, márgenes tras comisiones de plataformas y proyecciones a 12 meses. Los checklists tienen validación de datos y estados.' },
    { q: '¿Sirve si ya tengo un restaurante y quiero expandir a delivery?', a: 'Especialmente para eso. El capítulo 3 explica los modelos de negocio: marca propia, multi-marca desde tu cocina existente, o cocina satélite. Muchos restaurantes usan dark kitchens como extensión.' },
    { q: '¿Cuánto cuesta montar una dark kitchen?', a: 'Entre 30.000€ y 80.000€ dependiendo de la ubicación, equipamiento y número de marcas. La guía desglosa cada partida con costes reales del mercado español en el capítulo 4 y el checklist de equipamiento.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.' },
  ],

  cta: {
    heading: 'No Abras Tu Dark Kitchen a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta una consulta.',
    items: [
      'Guía completa PDF (12 capítulos, +40 páginas)',
      'Versión DOCX editable para personalizar',
      'Checklist de apertura legal (35 trámites)',
      'Checklist de equipamiento y obra (40 ítems con costes)',
      'Calculadora de viabilidad financiera (3 escenarios)',
      'Infografías: layout de cocina + timeline 90 días',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 24 EUR',
  },

  stickyLabel: 'GUÍA DARK KITCHEN — 24 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Kit Tareas Dark Kitchen', href: '/kit-tareas-dark-kitchen' },
    { label: 'Kit Plan Financiero', href: '/kit-plan-financiero' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  alreadyBought: {
    product: 'guia-dark-kitchen',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar una Dark Kitchen en España — Guía Completa',
    productDescription: 'Guía completa de 12 capítulos para montar una dark kitchen: requisitos legales, plan financiero, diseño, tecnología, marketing. Incluye 3 checklists Excel y calculadora de viabilidad.',
    price: '24.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar una dark kitchen?', a: 'Entre 30.000€ y 80.000€ dependiendo de ubicación, equipamiento y número de marcas. La guía desglosa cada partida.' },
      { q: '¿Incluye los requisitos legales actualizados?', a: 'Sí. Licencias, APPCC, registro sanitario, seguros, normativa plásticos 2026. Actualizada para España.' },
      { q: '¿El DOCX es editable?', a: 'Sí. Recibes PDF editorial + DOCX editable para personalizar y presentar a socios o bancos.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Cómo Montar una Dark Kitchen', item: 'https://aichef.pro/guia-dark-kitchen' },
    ],
  },
};

export default data;
