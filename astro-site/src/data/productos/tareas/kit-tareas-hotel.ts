// astro-site/src/data/productos/tareas/kit-tareas-hotel.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasHotel.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-hotel/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-hotel.ts  (marquee de testimonios)
// NO parafrasear.
//
// DIVERGENCIA ESTRUCTURAL (documentada en types.ts): este es el ÚNICO producto de la
// línea Tareas cuyo H2 del ContentGrid lleva DOS números dorados en vez de uno
// ("53 Hojas de Checklist en 19 Ficheros — 11 Departamentos"). Se resuelve con `grid.headingHtml`.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-hotel',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_HOTEL_V2',

  seo: {
    title:
      'Kit de Tareas Recurrentes — 53 Checklists Operativos para Hotel Completo | AI Chef Pro',
    description:
      '53 checklists operativos en 19 ficheros Excel (636 tareas) para 11 departamentos de hotel: F&B, recepción, housekeeping, piscina, mantenimiento, spa y más. Solo €18,50.',
    keywords:
      'checklist hotel, tareas hotel, checklist housekeeping, checklist recepción hotel, checklist mantenimiento hotel, tareas buffet hotel, checklist room service, plantilla tareas hotel, checklist piscina, spa hotel, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-hotel.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — 53 Checklists Operativos para Hotel Completo',
    productDescription:
      '53 checklists operativos en 19 ficheros Excel con 636 tareas ya escritas para 11 departamentos de hotel: F&B (6 outlets), recepción, housekeeping, piscina, terraza, mantenimiento, administración y spa.',
    price: '18.50',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Patricia Moreno',
        rating: '5',
        body: 'El checklist de desayuno buffet eliminó los olvidos en el montaje. Ahora el estándar es el mismo en cada turno.',
      },
      {
        author: 'Elena Vargas',
        rating: '5',
        body: 'Los checklists de banquetes cubren bodas, convenciones y cenas de gala con el nivel de detalle que necesitamos.',
      },
      {
        author: 'Isabel Fernández',
        rating: '5',
        body: 'Recomiendo este kit a todos mis clientes hoteleros. Cubren el 95% de la operativa F&B.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para hotel?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un departamento F&B de hotel profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Cubre todos los departamentos del hotel?',
        a: 'Sí. Incluye 11 departamentos: F&B (6 outlets), recepción, housekeeping, áreas públicas, piscina, terraza, mantenimiento, administración, guest services y spa.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da 53 checklists (636 tareas) para todo el hotel en 19 ficheros Excel por €18,50, pago único.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Hotel F&B / Buffet',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-buffet.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-roomservice.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-banquete.jpg',
      '/lovable-uploads/ai-gallery/tareas-hotel-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-hotel-buffet.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-hotel-roomservice.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €18,50 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Hotel Completo — 11 Departamentos',
    description:
      '53 checklists operativos en 19 ficheros Excel con 636 tareas ya escritas para todo el hotel: F&B (6 outlets), recepción, housekeeping, piscina, terraza, mantenimiento, administración, spa y más. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'F&B completo: 6 outlets (buffet, à la carte, pool bar, lobby bar, room service, banquetes)',
      'Recepción: 3 turnos + protocolo check-in/out + auditoría nocturna',
      'Housekeeping: checkout, estancia, turndown, deep cleaning, lencería',
      'Piscina, terraza, áreas públicas, spa/wellness',
      'Mantenimiento: diario, semanal, mensual y revisión legal Trimestral y Anual (DDD, extintores, gas, legionela) + HVAC, fontanería, electricidad',
      'Apertura/cierre de negocio y arqueo de caja con recuento por denominaciones y descuadre automático',
    ],
    ctaLabel: 'COMPRAR AHORA — €18,50',
  },

  stickyLabel: 'KIT TAREAS HOTEL COMPLETO — €18,50',

  grid: {
    countGold: '53',
    headingRest: ' Hojas de Checklist en 19 Ficheros — 11 Departamentos',
    headingHtml:
      '<span class="text-[#FFD700]">53</span> Hojas de Checklist en <span class="text-[#FFD700]">19</span> Ficheros — 11 Departamentos',
    subtitle:
      '636 tareas de hotel profesional ya escritas y repartidas por departamento. Cada plantilla viene pre-rellenada: solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'Sunrise',
        title: 'Buffet Desayuno',
        desc: 'Higiene y arranque seguro de cocina, montaje, reposición, show cooking, prevención de anisakis en el pescado crudo o marinado, mermas. 64 tareas ya escritas solo en este fichero.',
      },
      {
        icon: 'UtensilsCrossed',
        title: 'Buffet Almuerzo / Cena',
        desc: 'Montaje de estaciones, show cooking, reposición, temperaturas APPCC. Diferencias almuerzo vs. cena.',
      },
      {
        icon: 'ClipboardList',
        title: 'Restaurante À la Carte',
        desc: 'Apertura: reservas, montaje, briefing. Cierre: caja, reposición, feedback. 2 checklists.',
      },
      {
        icon: 'ConciergeBell',
        title: 'Outlets: Pool · Lobby · Snack',
        desc: 'Pool bar, lobby bar/lounge y snack bar/grab & go. Cada outlet con su checklist específico.',
      },
      {
        icon: 'ConciergeBell',
        title: 'Room Service + Minibar',
        desc: 'Room service completo (pedido→entrega→recogida) + minibar (reposición, PMS, caducidades).',
      },
      {
        icon: 'PartyPopper',
        title: 'Banquetes y Eventos',
        desc: 'Bodas, convenciones, galas. BEO, montaje sala, audiovisuales, timing pases, desmontaje.',
      },
      {
        icon: 'Building2',
        title: 'Recepción — 3 Turnos',
        desc: 'Mañana, tarde, noche/auditoría nocturna + protocolo check-in/check-out paso a paso. 4 checklists.',
      },
      {
        icon: 'Users',
        title: 'Guest Services',
        desc: 'Conserjería (transfers, excursiones) + Guest Experience (VIPs, reviews, CRM, fidelización).',
      },
      {
        icon: 'Bed',
        title: 'Housekeeping',
        desc: 'Checkout, estancia, turndown, deep cleaning semanal y control de lencería. 5 checklists.',
      },
      {
        icon: 'Building2',
        title: 'Áreas Públicas',
        desc: 'Lobby, pasillos y ascensores, baños públicos, parking. 4 checklists de limpieza y control.',
      },
      {
        icon: 'Waves',
        title: 'Piscina',
        desc: 'Apertura/cierre diario, mantenimiento semanal (filtros, químicos) y servicio de toallas.',
      },
      {
        icon: 'Sun',
        title: 'Terraza',
        desc: 'Montaje de temporada + servicio diario: mobiliario, parasoles, limpieza, carta.',
      },
      {
        icon: 'Wrench',
        title: 'Mantenimiento',
        desc: 'Ronda diaria, semanal, mensual + HVAC, fontanería y electricidad. Hoja nueva Trimestral y Anual: DDD, conductos de extracción, extintores y BIE, gas, legionela y OCA de baja tensión, con nº de parte y firma. 7 checklists técnicos.',
      },
      {
        icon: 'BarChart3',
        title: 'Administración',
        desc: 'Revenue management, reservas, contabilidad cierre día, RRHH operativo. 4 checklists.',
      },
      {
        icon: 'Sparkles',
        title: 'Spa / Wellness',
        desc: 'Apertura/cierre, cabinas entre tratamientos, vestuarios. 4 checklists.',
      },
      {
        icon: 'Building2',
        title: 'Apertura y Cierre de Negocio',
        desc: 'Checklist del hotel completo (no solo cocina): luces, alarma, TPV, sistemas. Responsable y hora límite precargados en cada tarea, con ancla a las 05:30.',
      },
      {
        icon: 'Wallet',
        title: 'Arqueo y Registro de Caja',
        desc: 'Apertura y cierre de caja con recuento por denominaciones, fondo de caja y descuadre automático frente al Z del TPV. Incluye registro mensual con descuadre por fórmula en 31 días.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Diario F&B',
        desc: 'Plantilla de reunión diaria: ocupación, VIPs, menú del día, equipo, incidencias.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '24 fechas clave para F&B hotelero: temporadas, festividades (Día del Padre, comuniones, puentes de Todos los Santos y de la Constitución) y congresos.',
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
        title: 'Pre-Rellenadas para Hotel',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un departamento F&B profesional. Solo ajusta y añade lo específico de tu hotel.',
      },
      {
        icon: 'Building',
        title: '11 Departamentos Cubiertos',
        desc: 'F&B, recepción, housekeeping, piscina, terraza, mantenimiento, administración, spa. La operativa completa que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: '53 Checklists Pre-Rellenados',
        desc: 'Cada departamento con tareas reales: desde el chef ejecutivo hasta mantenimiento HVAC. Onboarding inmediato.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €18,50',
        desc: 'Las mismas listas de tareas que usan hoteles con SaaS premium, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado operativas de F&B para hoteles de 4 y 5 estrellas en España y Latinoamérica.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Además de los 17 ficheros operativos, recibirás estos recursos adicionales — valorados en €18',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Diario F&B del Hotel',
        value: '€9',
        desc: 'Plantilla de reunión diaria del departamento F&B: ocupación, VIPs, menú del día, equipo, alérgenos e incidencias pendientes.',
        image: '/lovable-uploads/ai-gallery/tareas-hotel-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual F&B Hotelero',
        value: '€9',
        desc: '24 fechas clave para F&B en hoteles: temporadas alta/baja, festividades (Día del Padre, comuniones, puentes de Todos los Santos y de la Constitución) y congresos. Con antelación de preparación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-hotel-banquete.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT COMPLETO — €18,50',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones F&B de tu hotel, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para hotel?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un departamento F&B de hotel profesional. Solo tienes que personalizar: ajustar a tu hotel, borrar lo que no aplique y añadir lo específico. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Cubre todos los departamentos del hotel?',
      a: 'Sí. Incluye 11 departamentos: F&B (6 outlets), recepción (3 turnos), housekeeping, áreas públicas, piscina, terraza, mantenimiento (HVAC, fontanería, electricidad), administración (revenue, reservas, contabilidad, RRHH), guest services y spa/wellness.',
    },
    {
      q: '¿Sirve para hoteles de 3, 4 y 5 estrellas?',
      a: 'Sí. Las plantillas son escalables. Un hotel de 3* puede usar desayuno + room service. Un 5* o resort puede usar todas las plantillas con show cooking, sommelier y protocolo premium.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da 53 checklists (636 tareas) para todo el hotel en 19 ficheros Excel por €18,50, pago único. Sin suscripción, sin internet, ilimitado en outlets.',
    },
    {
      q: '¿Puedo usarlo en varios hoteles?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas hoteleras y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Estandariza las Operaciones de Todo Tu Hotel',
    subtitle:
      '53 checklists operativos en 19 ficheros para 11 departamentos, con 636 tareas ya escritas, por menos de lo que cuesta una hora de consultoría.',
    items: [
      'F&B completo: buffet, à la carte, pool bar, lobby bar, room service, banquetes',
      'Recepción: 3 turnos + protocolo check-in/out + auditoría nocturna',
      'Housekeeping: checkout, estancia, turndown, deep cleaning, lencería',
      'Piscina, terraza y áreas públicas (lobby, pasillos, baños, parking)',
      'Mantenimiento: diario, semanal, mensual, trimestral y anual (DDD, extintores, gas, legionela) + HVAC, fontanería, electricidad',
      'Administración: revenue management, reservas, contabilidad, RRHH',
      'Spa / Wellness: apertura, cierre, cabinas, vestuarios',
      'Apertura y cierre de negocio + arqueo de caja con recuento por denominaciones',
      'BONUS: Briefing Diario F&B (€9) + Calendario Anual Hotelero (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT COMPLETO — €18,50',
  },

  testimonials: {
    subtitle: 'F&B managers, chefs ejecutivos y directores de hotel que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Pablo Moreno',
        role: 'F&B Manager, Hotel Palace 5* Madrid',
        text: 'El checklist de desayuno buffet eliminó los olvidos en el montaje. Antes cada turno montaba diferente. Ahora el estándar es el mismo a las 6:30 de la mañana que a las 10.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Ricardo Castillo',
        role: 'Chef Ejecutivo, Resort Meliá Costa del Sol',
        text: 'Gestiono 4 outlets y 120 cubiertos de buffet. Los checklists por outlet me permiten delegar con confianza. El personal eventual sabe exactamente qué hacer desde el primer día.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Elena Vargas',
        role: 'Directora de Banquetes, Hotel W Barcelona',
        text: 'Los checklists de banquetes cubren bodas, convenciones y cenas de gala con el nivel de detalle que necesitamos. El BEO checklist es justo lo que faltaba en nuestra operativa.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Miguel Ángel Torres',
        role: 'Maître, Hotel Ritz-Carlton',
        text: 'Las tareas por perfil para camarero de hotel son perfectas para onboarding. Protocolo de servicio, descorche, cargo a habitación... todo está cubierto.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Ruiz',
        role: 'Jefa de Room Service, Hotel Four Seasons',
        text: 'Implementamos el checklist de room service y los tiempos de entrega mejoraron un 30%. El protocolo de servicio en habitación es exactamente el estándar que necesitábamos.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Daniela Hernández',
        role: 'Revenue Manager, Cadena Hotelera NH',
        text: 'Como F&B manager de grupo, estos checklists me permiten estandarizar la operativa en 6 hoteles. El briefing diario es obligatorio en todas nuestras propiedades.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Santiago Delgado',
        role: 'Gobernante / Housekeeping, Boutique Hotel',
        text: 'El checklist de minibar me ha organizado las rondas de reposición. Antes perdíamos stock y los cargos no se facturaban. Ahora todo queda registrado.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Javier Martín',
        role: 'Director de Operaciones, Grupo Hoteles Ibéricos',
        text: 'El calendario anual F&B hotelero es brutal. Temporadas, festividades, congresos... nos permite planificar personal eventual y compras con meses de antelación.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Isabel Fernández',
        role: 'Consultora Hotelera, Hospitality Experts',
        text: 'Recomiendo este kit a todos mis clientes hoteleros. Desayuno, room service, banquetes... cubren el 95% de la operativa F&B de cualquier hotel de 4 o 5 estrellas.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Carlos Navarro',
        role: 'Profesor, Escuela Superior de Hostelería',
        text: 'Mis alumnos del máster en dirección hotelera usan estos checklists como referencia. Las tareas de F&B manager y los perfiles están perfectamente estructurados.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€95',
    price: '€18,50',
    discountBadge: '-81%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 81% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €76,50 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-tareas-catering', label: 'Kit Tareas Catering' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-hotel',
    label: '¿Ya compraste el Kit de Tareas Hotel? Vuelve a entrar al dashboard',
  },
};

export default data;
