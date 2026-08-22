// astro-site/src/data/productos/tareas/kit-tareas-chef-privado.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasChefPrivado.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-chef-privado/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-chef-privado.ts  (marquee de testimonios)
// NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-chef-privado',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_CHEF_PRIVADO',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Chef Privado / Personal Chef | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para chef privado: ficha de cliente con alergias, equipo y transporte, APPCC móvil, servicio completo, fidelización y administración del autónomo. Solo €18.',
    keywords:
      'checklist chef privado, tareas personal chef, chef a domicilio checklist, APPCC chef privado, gestión cliente chef, equipo chef portátil, ficha alergias chef, checklist servicio catering, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-chef-privado.jpg',
  },

  schema: {
    productName:
      'Kit de Tareas Recurrentes — Checklists Operativos para Chef Privado / Personal Chef',
    productDescription:
      '9 checklists operativos pre-rellenados para chef privado: ficha de cliente, equipo, APPCC móvil, servicio, fidelización y administración.',
    price: '18.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Raúl Ibáñez',
        rating: '5',
        body: 'La ficha de cliente me cambió la vida. Ahora tengo todo centralizado: preferencias, equipamiento de cocina, historial de menús. Cero errores en 6 meses.',
      },
      {
        author: 'Carolina Valls',
        rating: '5',
        body: 'El checklist de equipo y transporte es imprescindible. Ya no llego a la villa de un cliente y descubro que olvidé algo.',
      },
      {
        author: 'Martín del Río',
        rating: '5',
        body: 'En un yate no hay segunda oportunidad. El briefing pre-servicio me salvó de más de un desastre.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para chef privado?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un chef privado profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Sirve para diferentes tipos de chef privado?',
        a: 'Sí. Cenas a domicilio, meal prep, eventos, yates, villas, clases de cocina y corporativo.',
      },
      {
        q: '¿En qué se diferencia del software de gestión?',
        a: 'El software de gestión cobra €40/mes. Este kit da las mismas listas en Excel por €18, pago único.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Chef Privado / Personal Chef',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-chef-privado-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-chef-privado-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-chef-privado-transporte.jpg',
      '/lovable-uploads/ai-gallery/tareas-chef-privado-emplatado.jpg',
      '/lovable-uploads/ai-gallery/tareas-chef-privado-cliente.jpg',
      '/lovable-uploads/ai-gallery/tareas-chef-privado-cocina.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-chef-privado-transporte.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-chef-privado-servicio.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-chef-privado-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €18 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Chef Privado / Personal Chef — Checklists por Servicio, Cliente y Logística',
    description:
      '9 plantillas Excel pre-rellenadas para chefs privados: gestión de clientes, equipo y transporte, seguridad alimentaria, ejecución de servicio, fidelización y administración. Imprime, organiza y profesionaliza tu negocio.',
    checkItems: [
      'Clientes: ficha completa con alergias, preferencias y equipamiento de cocina',
      'Logística: equipo portátil, transporte frío, mini-despensa, vehículo',
      'Servicio: pre-servicio, ejecución por pases, post-servicio y limpieza',
      'Seguridad: APPCC móvil, temperaturas, alérgenos, trazabilidad',
      'Negocio: facturación, costes, fidelización, calendario de demanda',
    ],
    ctaLabel: 'COMPRAR AHORA — €18',
  },

  stickyLabel: 'KIT TAREAS CHEF PRIVADO — €18',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Gestión Profesional',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de un chef privado profesional. Solo ajusta, imprime y organiza tu negocio.',
    templates: [
      {
        icon: 'UserCheck',
        title: 'Ficha de Cliente',
        desc: 'Datos completos, alergias (14 alérgenos UE), intolerancias, preferencias culinarias, dieta, equipamiento de la cocina del cliente. Una ficha por cliente.',
      },
      {
        icon: 'ShoppingCart',
        title: 'Menú y Compras',
        desc: 'Planificación de menú por servicio, lista de compras con cantidades, control de coste por comensal y margen bruto del servicio.',
      },
      {
        icon: 'Briefcase',
        title: 'Equipo y Transporte',
        desc: 'Checklist de cuchillos, sartenes, transporte frío, mini-despensa portátil, textiles y verificación del vehículo. Nada se queda en casa.',
      },
      {
        icon: 'ShieldCheck',
        title: 'APPCC Móvil',
        desc: 'Control de temperaturas, gestión de alérgenos, higiene en cocina ajena, trazabilidad, etiquetado de meal prep. Cumplimiento legal.',
      },
      {
        icon: 'UtensilsCrossed',
        title: 'Servicio Completo',
        desc: 'Pre-servicio (montaje, mise en place), durante (timing por pases, emplatado) y post-servicio (limpieza total, recogida de equipo).',
      },
      {
        icon: 'Heart',
        title: 'Seguimiento y Fidelización',
        desc: 'Post-servicio 24h, solicitud de reseñas, historial de servicios por cliente, fechas especiales, programa de recurrencia.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Administración',
        desc: 'Facturación por servicio, control de gastos, obligaciones fiscales del autónomo (303, 130, 390), seguros y carnets.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Pre-Servicio',
        desc: 'Hoja de ruta para cada servicio: cliente, alergias, menú, equipo, verificación final. Tu checklist de vuelo antes de despegar.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario de Demanda',
        desc: '12 meses con picos de demanda, tipos de servicio estacionales y estrategia de marketing por temporada.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñadas para Chef Privado',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación móvil del chef privado: transporte, cocina ajena, clientes individuales.',
      },
      {
        icon: 'Briefcase',
        title: 'Logística + Servicio + Negocio',
        desc: 'Cubre las 3 patas del chef privado: la logística de ir al cliente, la ejecución del servicio y la gestión del negocio como autónomo.',
      },
      {
        icon: 'Users',
        title: 'Gestión de Múltiples Clientes',
        desc: 'Fichas individuales con alergias, preferencias e historial. Nunca más confundir las restricciones de un cliente con las de otro.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €18',
        desc: 'Las mismas listas de tareas que usan chefs privados con software premium, pero en Excel por un pago único. Sin suscripción.',
      },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de cálculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a decenas de chefs privados en la profesionalización de sus operaciones.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 7 plantillas principales, recibirás estos recursos adicionales — valorados en €18',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Pre-Servicio',
        value: '€9',
        desc: 'Tu hoja de ruta para cada servicio: datos del cliente, alergias, menú del día, equipo necesario y verificación final. El checklist que completas 24h antes de cada evento.',
        image: '/lovable-uploads/ai-gallery/tareas-chef-privado-emplatado.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Demanda',
        value: '€9',
        desc: '12 meses con picos de demanda (San Valentín, verano en costa, Navidad), tipos de servicio por temporada y estrategia de marketing. El mapa de tu año como chef privado.',
        image: '/lovable-uploads/ai-gallery/tareas-chef-privado-cliente.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €18',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor tu negocio como chef privado, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para chef privado?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un chef privado profesional: gestión de clientes, transporte de equipo, APPCC móvil, ejecución de servicio y administración del negocio. Solo tienes que personalizar: ajustar tareas a tu tipo de servicio, borrar las que no apliquen y añadir las específicas.',
    },
    {
      q: '¿Sirve para diferentes tipos de chef privado?',
      a: 'Sí. Las plantillas cubren todos los tipos de servicio: cenas a domicilio, meal prep semanal, eventos privados, chef de yate/villa, clases de cocina y catering corporativo. Adapta lo que necesites según tu especialidad.',
    },
    {
      q: '¿Incluye gestión de alérgenos?',
      a: 'Sí, es una de las partes más críticas. La ficha de cliente incluye registro completo de los 14 alérgenos UE, intolerancias, dietas especiales y restricciones. El APPCC móvil tiene checklist de verificación de alérgenos antes de cada servicio.',
    },
    {
      q: '¿En qué se diferencia del software de gestión?',
      a: 'El software de gestión cobra €40/mes y requieren tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €18, pago único. Sin suscripción, sin internet, ilimitado en clientes.',
    },
    {
      q: '¿Puedo usarlo si trabajo con ayudante?',
      a: 'Sí. Los checklists están pensados para compartir con tu ayudante o segundo chef. El briefing pre-servicio es perfecto para alinear al equipo antes de cada evento.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Tú Eres la Cocina, el Camarero, el Logístico y el Contable',
    subtitle:
      '9 checklists que organizan las 10 áreas críticas de tu negocio como chef privado. Por menos de lo que cobras por una guarnición.',
    items: [
      'Ficha de cliente: alergias, preferencias, equipamiento de cocina',
      'Planificación de menú + lista de compras + control de coste',
      'Checklist de equipo y transporte: nada se queda en casa',
      'APPCC móvil: temperaturas, alérgenos, trazabilidad',
      'Servicio completo: pre, durante y post con limpieza',
      'Seguimiento y fidelización de clientes',
      'BONUS: Briefing Pre-Servicio (€9)',
      'BONUS: Calendario Anual de Demanda (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €18',
  },

  testimonials: {
    subtitle:
      'Chefs privados, personal chefs y consultores que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Raúl Ibáñez',
        role: 'Chef privado, Ibiza & Mallorca',
        text: 'La ficha de cliente me cambió la vida. Antes llevaba las alergias en notas del móvil. Ahora tengo todo centralizado: preferencias, equipamiento de cocina, historial de menús. Cero errores en 6 meses.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Carolina Valls',
        role: 'Chef privada, villas de lujo en Marbella',
        text: 'El checklist de equipo y transporte es imprescindible. Ya no llego a la villa de un cliente y descubro que olvidé la mandolina o la nevera portátil. Todo marcado antes de salir.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Martín del Río',
        role: 'Chef de yates, Costa del Sol',
        text: 'En un yate no hay segunda oportunidad: si olvidas un ingrediente estás en medio del mar. El briefing pre-servicio me salvó de más de un desastre. Lo uso religiosamente.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Elena Pascual',
        role: 'Personal chef, meal prep semanal en Barcelona',
        text: 'El control de costes por servicio es brutal. Antes no sabía cuánto ganaba realmente por cliente. Ahora calculo margen por servicio y he ajustado mis precios. Gano un 30% más.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Diego Serrano',
        role: 'Chef privado para eventos, Madrid',
        text: 'El APPCC móvil me da tranquilidad. Registro temperaturas, alérgenos y trazabilidad en cada servicio. Si algún día hay una incidencia, tengo todo documentado.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Lucía Romero',
        role: 'Consultora gastronómica, chefs privados',
        text: 'Lo primero que hago con cada chef que asesoro es darle estos checklists. Cubren las 10 áreas críticas del negocio: desde la consulta inicial hasta la facturación. Profesionaliza al instante.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Alejandro Cortés',
        role: 'Chef privado corporativo, Valencia',
        text: 'El calendario anual de demanda es oro. Ahora sé cuándo invertir en marketing (noviembre) y cuándo maximizar servicios (verano, Navidad). Mi facturación subió un 40%.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Marcos Torres',
        role: 'Chef privado, aviación y yates premium',
        text: 'Trabajo para clientes muy exigentes: aviones privados, yates, CEOs. Los checklists me dan un nivel de profesionalidad y organización que mis clientes valoran enormemente.',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€85',
    price: '€18',
    discountBadge: '-79%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 79% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €67 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-tareas-chocolateria', label: 'Kit Tareas Chocolatería' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-chef-privado',
    label: '¿Ya compraste el Kit de Tareas Chef Privado? Vuelve a entrar al dashboard',
  },
};

export default data;
