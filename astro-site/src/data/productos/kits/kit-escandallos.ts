// astro-site/src/data/productos/kits/kit-escandallos.ts
// LÍNEA KITS EXCEL — producto de REFERENCIA. Copy VERBATIM de la SPA:
//   · src/pages/KitEscandallos.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/kit-escandallos/*  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-escandallos.ts (10 testimonios)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS (resuelto en el wrapper .astro).
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'kit-escandallos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_ESCANDALLOS',

  seo: {
    title: 'Kit Escandallos Pro: 11 Plantillas Excel con Food Cost Automatico | AI Chef Pro',
    description:
      '11 plantillas de escandallos Excel profesionales: food cost automatico, mermas precargadas, calculadora PVP y simulador de rentabilidad. Para hosteleria. Solo 12 euros.',
    keywords:
      'plantilla escandallo excel, plantilla escandallo, simulador escandallos, calcular food cost restaurante, plantilla food cost excel, escandallo hosteleria, calculadora PVP restaurante, mermas restaurante excel, plantillas escandallos gratis, escandallo excel, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-escandallos.jpg',
  },

  schema: {
    productName: 'Kit de Escandallos Pro — 11 Plantillas Excel Profesionales',
    productDescription:
      '11 plantillas de escandallos con fórmulas automáticas, mermas precargadas y calculadora de PVP. Para chefs, gerentes y dueños de restaurante.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '10',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Antes hacía los escandallos en un cuaderno. Ahora con estas plantillas tengo el food cost de cada plato controlado al céntimo. He bajado del 35% al 28% en dos meses.',
      },
      {
        author: 'María José Pérez',
        rating: '5',
        body: 'Gestiono 4 restaurantes y estas plantillas me permiten estandarizar los escandallos en todos. El dashboard mensual es lo que más uso.',
      },
      {
        author: 'Antonio Delgado',
        rating: '5',
        body: 'Uso el kit con todos mis clientes de consultoría. Es la herramienta más práctica que he encontrado para enseñar control de costes.',
      },
    ],
    // FAQPage schema (MÁS CORTAS que las FAQ on-page — VERBATIM del Helmet)
    faqs: [
      {
        q: '¿Necesito Excel avanzado para usar las plantillas?',
        a: 'No. Las plantillas vienen con todo configurado: fórmulas, mermas, validaciones. Solo introduces tus ingredientes, cantidades y precios. Todo se calcula automáticamente.',
      },
      {
        q: '¿Funcionan con Google Sheets?',
        a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers.',
      },
      {
        q: '¿Los datos de merma son fiables?',
        a: 'Sí. Son los estándares utilizados en hostelería profesional y en consultoría gastronómica. Cubren 21 categorías de ingredientes con mermas mínimas, máximas y típicas.',
      },
      {
        q: '¿Puedo personalizar las plantillas?',
        a: 'Totalmente. Puedes añadir ingredientes, modificar precios, ajustar mermas, cambiar el food cost objetivo y añadir tus propias fotos de platos.',
      },
      {
        q: '¿Incluye actualizaciones futuras?',
        a: 'Sí. Tienes acceso de por vida al dashboard online. Cuando añadamos nuevas plantillas o mejoras, las recibirás sin coste adicional.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: 'Sí. 30 días de garantía completa. Si las plantillas no te ayudan a controlar tu food cost, te devolvemos el 100% sin hacer ninguna pregunta.',
      },
    ],
    breadcrumbName: 'Kit de Escandallos Pro',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/tataki-presa-iberica-chimichurri.jpeg',
      '/lovable-uploads/ai-gallery/tartaleta-de-yuzu-y-merengue.jpeg',
      '/lovable-uploads/ai-gallery/cocktail-green-margarita.jpeg',
      '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
      '/lovable-uploads/ai-gallery/croissant-bicolor-de-mantequilla-aichefpro.jpeg',
      '/lovable-uploads/ai-gallery/huevo-baja-temperatura-trufa.jpeg',
    ],
    // ContentGrid strip (6) — DIFIERE del hero
    gridGallery: [
      '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
      '/lovable-uploads/ai-gallery/cocktail-garibaldi-fermentado.jpeg',
      '/lovable-uploads/ai-gallery/milhojas-vertical-de-vainilla-con-frambuesas-aichefpro-2.jpeg',
      '/lovable-uploads/ai-gallery/carpaccio-gambas.jpeg',
      '/lovable-uploads/ai-gallery/torrija-caramelizada-con-helado.jpeg',
      '/lovable-uploads/ai-gallery/cocktail-tepache-pina-asada.jpeg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badgeTone: 'gold',
    badge: 'El kit #1 de escandallos para hostelería profesional',
    titlePre: 'Controla tu ',
    titleGold: 'Food Cost',
    titlePost: ' con Plantillas Excel Profesionales',
    // sin titleSubtitle (Forma A: sin subtítulo bloque)
    description:
      '11 plantillas de escandallos en Excel con fórmulas automáticas, mermas precargadas y calculadora de PVP. Calcula el food cost real de cada plato y controla los costes de tu restaurante, pastelería, catering o food truck desde el primer día.',
    checkItems: [
      '11 plantillas Excel profesionales con fórmulas automáticas',
      'Mermas estándar de la industria precargadas',
      'Calculadora de PVP para 10 tipos de establecimiento',
      'Dashboard de Food Cost mensual con gráfico de evolución',
      'Food cost REAL: escribe el PVP que cobras hoy y la hoja te avisa en rojo si te pasas del objetivo',
      'Zona para foto del plato en cada escandallo',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  compatApps: {
    titleHtml: 'Compatible con las <span class="text-[#FFD700]">Herramientas</span> que Ya Usas',
    subtitleHtml:
      'Funciona mejor con <a href="https://aichef.pro" class="text-[#FFD700] hover:underline">AI Chef Pro</a>. Compatible con Excel, Google Sheets, PDF y más',
  },

  grid: {
    countGold: '11',
    headingRest: ' Plantillas Profesionales',
    subtitle:
      'Cada plantilla de escandallo incluye fórmulas automáticas, mermas precargadas, zona para foto del plato y formato listo para imprimir.',
    fourCols: true,
    templates: [
      { icon: 'UtensilsCrossed', title: 'Escandallo Estándar', desc: 'La plantilla más completa para platos a la carta. Introduce ingredientes, cantidades y precios de compra — las fórmulas calculan automáticamente la merma, el coste real por ración, el food cost % y el PVP sugerido según tu margen objetivo. Y al revés: escribe el PVP que ya tienes en carta y la hoja te devuelve tu food cost REAL, en rojo si supera tu objetivo. Incluye zona para foto del plato terminado.' },
      { icon: 'ChefHat', title: 'Menú Degustación', desc: 'Diseñada para menús de 5 a 9 pases con escandallo individual por plato. La hoja resumen suma el coste total del menú completo, calcula el food cost global y sugiere el PVP por comensal. Perfecta para restaurantes gastronómicos y experiencias premium.' },
      { icon: 'ClipboardList', title: 'Menú del Día', desc: 'Estructura completa: primer plato, segundo, postre y extras (pan, bebida, café). Calcula automáticamente el coste total del menú y el PVP necesario para mantener tu margen. Incluye rotación semanal para planificar 5 menús diferentes con sus costes comparados.' },
      { icon: 'Wine', title: 'Cocktails y Bebidas', desc: 'Escandallo detallado de 4 cocktails con medidas exactas en cl/ml, coste por ingrediente y food cost unitario. Optimizada para barras con objetivo de food cost al 20-25%. Incluye cálculo de garnish, hielo y merma de destilados por evaporación y derrame.' },
      { icon: 'CakeSlice', title: 'Pastelería', desc: 'Plantilla especializada con mermas reales de pastelería: temperado de chocolate (12%), horneado de masas (8%), montaje de mousses. Incluye rendimiento por receta — cuántas raciones salen de cada elaboración. Con ejemplos de tarta, croissants y macarons listos para personalizar.' },
      { icon: 'PartyPopper', title: 'Catering', desc: 'La única plantilla que integra coste de materia prima + personal + logística + menaje en un solo presupuesto por persona. Define tu margen objetivo y obtén el precio por comensal al instante. Incluye checklist de evento y desglose para presentar al cliente.' },
      { icon: 'Coffee', title: 'Cafetería / Brunch', desc: 'Escandallos adaptados al formato cafetería con food cost objetivo del 25-30%. Incluye ejemplos reales: tostada de aguacate, açaí bowl, eggs benedict, carrot cake. Cada receta con coste real desglosado para que descubras qué platos te dan margen y cuáles te lo comen.' },
      { icon: 'Truck', title: 'Food Truck', desc: 'Plantilla pensada para street food: recetas rápidas con foco en velocidad de servicio y márgenes altos. Incluye smash burger, loaded fries y pulled pork con coste real por unidad. Calcula el punto de equilibrio diario: cuántas unidades necesitas vender para cubrir costes fijos.' },
      { icon: 'TrendingDown', title: 'Control de Mermas', desc: 'Sistema de registro semanal de desperdicio real en 16 categorías de producto (carnes, pescados, frutas, lácteos…), con objetivo mínimo, típico y máximo por categoría. El semáforo marca OK o ALERTA en cuanto el desperdicio real supera el objetivo. Incluye gráfico de evolución del desperdicio a 12 semanas.' },
      { icon: 'Calculator', title: 'Calculadora de PVP', desc: 'Introduce el coste de cualquier plato y obtén el PVP recomendado para 10 tipos de establecimiento: restaurante gastronómico, casual dining, fast casual, cafetería, food truck, catering, bar de copas, hotel, pastelería y delivery. Cada uno con su rango de food cost objetivo del sector.' },
      { icon: 'BarChart3', title: 'Dashboard Mensual', desc: 'Panel de control con seguimiento de food cost durante 12 meses consecutivos. Registra stock inicial, compras, stock final y ventas: el food cost sale del CONSUMO, no de las compras — una compra fuerte a fin de mes ya no te mueve el indicador. Incluye gráfico de evolución anual y alertas cuando el food cost supera tu límite. Tu cockpit financiero de cocina.' },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son escandallos diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      { icon: 'Calculator', title: 'Fórmulas Reales, No Valores Fijos', desc: 'Cambias un ingrediente y todo se recalcula: coste, merma, food cost % y PVP sugerido. Sin errores manuales.' },
      { icon: 'FileSpreadsheet', title: 'Para Todo Tipo de Establecimiento', desc: 'Restaurante, catering, pastelería, bar, food truck, cafetería. Cada plantilla adaptada a su formato real.' },
      { icon: 'TrendingDown', title: 'Mermas Estándar Precargadas', desc: '21 categorías de ingredientes con la merma típica de la industria. Editable para ajustar a tu realidad.' },
      { icon: 'RefreshCw', title: 'Paga Una Vez, Tuyo Para Siempre', desc: 'Sin suscripciones. Acceso permanente al dashboard con todas las plantillas. Nuevas plantillas sin coste adicional.' },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de cálculo:',
    compatPills: [
      { label: 'Microsoft Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice Calc' },
      { label: 'Apple Numbers' },
      { label: 'WPS Office' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas de control de costes para cientos de restaurantes.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 11 plantillas, recibirás estos recursos adicionales — valorados en €46',
    items: [
      {
        icon: 'BookOpen',
        label: 'BONUS 1',
        title: 'Guía: Controla tu Food Cost en 30 Días',
        value: '€27',
        desc: 'Plan de acción semana a semana para reducir tu food cost. Incluye tácticas de negociación con proveedores, checklist semanal y caso práctico construido a partir de intervenciones reales.',
        image: '/lovable-uploads/ai-gallery/focaccia-jardin-alta-hidratacion-aichefpro.jpeg',
      },
      {
        icon: 'FileSpreadsheet',
        label: 'BONUS 2',
        title: 'Checklist de Mermas + Inventario',
        value: '€19',
        desc: 'Plantilla Excel con registro diario de mermas (con motivos y acciones correctivas) y control de inventario con consumo real vs teórico.',
        image: '/lovable-uploads/ai-gallery/hogaza-masa-madre-oreja-perfecta-aichefpro.jpeg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT — €12',
  },

  guarantee: {
    // headingPre por defecto = "Garantía de Satisfacción " (acentuado); escandallos usa el default.
    text:
      'Si las plantillas no te ayudan a controlar tu food cost, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (más largas que schema.faqs)
  faqs: [
    {
      q: '¿Necesito Excel avanzado para usar las plantillas?',
      a: 'No. Las plantillas vienen con todo configurado: fórmulas, mermas, validaciones. Solo introduces tus ingredientes, cantidades y precios. Todo se calcula automáticamente.',
    },
    {
      q: '¿Funcionan con Google Sheets?',
      a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers.',
    },
    {
      q: '¿Los datos de merma son fiables?',
      a: 'Sí. Son los estándares utilizados en hostelería profesional y en consultoría gastronómica. Cubren 21 categorías de ingredientes con mermas mínimas, máximas y típicas. Puedes ajustarlas a tu realidad.',
    },
    {
      q: '¿Puedo personalizar las plantillas?',
      a: 'Totalmente. Puedes añadir ingredientes, modificar precios, ajustar mermas, cambiar el food cost objetivo y añadir tus propias fotos de platos. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye actualizaciones futuras?',
      a: 'Sí. Tienes acceso de por vida al dashboard online. Cuando añadamos nuevas plantillas o mejoras, las recibirás sin coste adicional.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: 'Sí. 30 días de garantía completa. Si las plantillas no te ayudan a controlar tu food cost, te devolvemos el 100% sin hacer ninguna pregunta.',
    },
  ],

  cta: {
    heading: 'Deja de Perder Dinero en tu Food Cost',
    subtitle:
      '11 plantillas profesionales por menos de lo que cuesta un menú del día. Empieza a controlar tus costes hoy.',
    items: [
      '11 plantillas Excel profesionales con fórmulas automáticas',
      'Mermas estándar de la industria precargadas (21 categorías)',
      'Calculadora de PVP para 10 tipos de establecimiento',
      'Dashboard de Food Cost mensual con gráfico de evolución',
      'Food cost REAL: escribe el PVP que cobras hoy y la hoja te avisa en rojo si te pasas del objetivo',
      'BONUS: Guía "Controla tu Food Cost en 30 Días" (€27)',
      'BONUS: Checklist de Mermas + Inventario (€19)',
      'Paga una vez — acceso de por vida al dashboard online',
      'Garantía de devolución 30 días',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT — €12',
  },

  testimonials: {
    subtitle:
      'Profesionales de la hostelería que ya controlan su food cost con el Kit de Escandallos Pro',
    items: [
      { name: 'Alejandro Ruiz', role: 'Jefe de Cocina, Restaurante Alma', text: 'Antes hacía los escandallos en un cuaderno. Ahora con estas plantillas tengo el food cost de cada plato controlado al céntimo. He bajado del 35% al 28% en dos meses.', avatar: '/avatars/chef-avatar-1.jpg' },
      { name: 'María José Pérez', role: 'Directora de Operaciones, Grupo MJP', text: 'Gestiono 4 restaurantes y estas plantillas me permiten estandarizar los escandallos en todos. El dashboard mensual es lo que más uso — veo la evolución de un vistazo.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Tomás Herrero', role: 'Dueño, Tapería El Rincón', text: 'Nunca me enseñaron a hacer escandallos en la escuela de hostelería. Con el kit, solo introduzco ingredientes y precios, y el Excel me dice exactamente a cuánto vender cada plato.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucía Fernández', role: 'Pastelera, Obrador La Dulce', text: 'La plantilla de pastelería tiene en cuenta las mermas de cada ingrediente. Descubrí que estaba perdiendo un 12% en chocolate por no calcular bien la merma de temperado.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Fernando Navarro', role: 'Director de Catering, Banquetes FN', text: 'La plantilla de catering con presupuesto por persona me ha cambiado la vida. Ahora preparo presupuestos profesionales en 10 minutos. Antes me llevaba toda la mañana.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Elena Molina', role: 'Bartender, Cóctel & Co', text: 'La plantilla de cocktails con medidas en cl es perfecta. He calculado que mi Gin Tonic premium tiene un food cost del 16% — mucho mejor de lo que pensaba.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Antonio Delgado', role: 'Consultor Gastronómico', text: 'Uso el kit con todos mis clientes de consultoría. Es la herramienta más práctica que he encontrado para enseñar control de costes. Se lo recomiendo a todo el sector.', avatar: '/avatars/chef-avatar-5.jpg' },
      { name: 'Gonzalo Romero', role: 'Gerente, Cafetería Central', text: 'La plantilla de cafetería me ayudó a descubrir que mi tostada de aguacate tenía un food cost del 42%. Ajusté la receta y ahora está en el 27%. El kit se paga solo.', avatar: '/avatars/avatar-8.jpg' },
      { name: 'Pablo Soto', role: 'Propietario, Food Truck Street Bites', text: 'Con el escandallo de food truck calculé que mi smash burger más vendida me dejaba solo €1.20 de margen. Reestructuré la receta y ahora son €2.80. Información es poder.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sergio Vega', role: 'Jefe de Compras, Hotel Panorama', text: 'El control de mermas me permitió negociar mejor con proveedores. Cuando les muestro datos reales de merma por categoría, consigo mejores precios. Herramienta imprescindible.', avatar: '/avatars/avatar-1.jpg' },
    ],
  },

  pricing: {
    priceOld: '€49',
    price: '€12',
    discountBadge: '-75%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 75% de descuento',
    bonusTotalLabel: 'Valor total del kit completo: €95 — 11 plantillas (€49) + 2 bonos (€46)',
    bonusSaveLine: '¡Ahorra €37 HOY!',
  },

  stickyLabel: 'KIT ESCANDALLOS — €12',
  stickyVariant: 'v1',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: '/guia-food-cost-ingenieria-menu', label: 'Guía Food Cost + Ingeniería de Menú' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-escandallos',
    label: '¿Ya compraste el Kit? Vuelve a entrar al dashboard',
  },
};

export default data;
