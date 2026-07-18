// astro-site/src/data/productos/tareas/kit-tareas-hamburgueseria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasHamburgueseria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-hamburgueseria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-hamburgueseria.ts  (marquee de testimonios)
// NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-hamburgueseria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_HAMBURGUESERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Hamburguesería | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para hamburguesería: plancha/grill, smash burgers, freidora, línea de montaje, delivery, perfiles y eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist hamburguesería, tareas apertura hamburguesería, checklist smash burger, tareas parrillero, checklist delivery hamburguesería, lista tareas hamburguesería, plantilla tareas hamburguesería, control plancha grill, freidora checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-hamburgueseria.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Hamburguesería',
    productDescription:
      '9 checklists operativos pre-rellenados para hamburguesería: plancha/grill, smash burgers, freidora, línea de montaje, delivery, perfiles y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '10', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'El checklist de plancha y grill me ha cambiado el turno. Ahora seguimos el mismo protocolo y el smash sale perfecto cada vez.',
      },
      {
        author: 'Marta Iglesias',
        rating: '5',
        body: 'Gestionar la apertura de una hamburguesería con delivery y sala era un caos. Los checklists por zona nos organizaron desde el día uno.',
      },
      {
        author: 'Alejandro Fuentes',
        rating: '5',
        body: 'La línea de montaje de burger es donde más nos ayudó. Cada ingrediente en su sitio, salsas repuestas, pan tostado a tiempo.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para hamburguesería?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una hamburguesería. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local.',
      },
      {
        q: '¿Incluye tareas de plancha, grill y smash burger?',
        a: 'Sí. Encendido, limpieza, temperatura, técnica smash burger, punto de carne (rare a well done) y limpieza entre turnos.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varias hamburgueserías?',
        a: 'Sí. Licencia personal para todos los establecimientos que gestiones.',
      },
      {
        q: '¿Incluye tareas de delivery y packaging?',
        a: 'Sí. Packaging correcto de burger, control de tiempos, gestión de riders, etiquetado y cierre de plataformas de delivery.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Hamburguesería',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-plancha.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-freidora.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-delivery.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-mesa.jpg',
    ],
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-plancha.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-freidora.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-delivery.jpg',
      '/lovable-uploads/ai-gallery/tareas-burger-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-burger-montaje.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-burger-plancha.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-burger-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Hamburguesería — Checklists Operativos por Turno, Área y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu hamburguesería: plancha/grill, smash burgers, freidora, línea de montaje, delivery, perfiles y eventos. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: plancha/grill, freidora, línea de montaje, sala, barra',
      'Control de plancha y grill: temperatura, limpieza, punto de carne (rare a well done)',
      'Tareas del parrillero: smash burger, punto de carne, test polares aceite freidora',
      'Gestión de delivery y take-away: packaging burger, riders, control de tiempos',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS HAMBURGUESERÍA — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de una hamburguesería. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '6 checklists: apertura y cierre de plancha/grill, freidora, línea de montaje, sala y barra. Cada tarea con responsable, hora límite y firma. ~80 tareas pre-rellenadas.',
      },
      {
        icon: 'Flame',
        title: 'Tareas de Plancha y Grill',
        desc: 'Encendido de plancha, temperatura óptima, limpieza de superficie, test de punto de carne, gestión de smash burgers, control de tiempos por grosor.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: parrillero/grill master, cocinero de línea, freidurista, encargado/a y camarero/a.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras, mantenimiento mensual de plancha, freidora y campana extractora.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Checklist pre-evento (48h→día), noche de burger especial, festivos con menú limitado, gestión de picos de delivery.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por área, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing pre-servicio: reservas, burger especial del día, alérgenos, equipo del turno. Imprime y pega en cocina.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '17 fechas clave de hostelería con tareas asociadas y antelación recomendada. Añade tus fechas locales.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un profesional con 29 años en alta hostelería.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Hamburguesería',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de una hamburguesería. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Flame',
        title: 'Control de Plancha y Punto de Carne',
        desc: 'Encendido de plancha, temperatura óptima, técnica smash burger, punto de carne (rare a well done), test polares de aceite de freidora. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Delivery y Packaging',
        desc: 'Checklists para gestión de riders, packaging de burger (que no se desmonte), control de tiempos de entrega, take-away y plataformas de delivery.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan las hamburgueserías con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha diseñado sistemas operativos y checklists para cientos de restaurantes y hamburgueserías.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Plantilla de Briefing Pre-Servicio',
        value: '€7',
        desc: 'La reunión de 5 minutos que separa a las hamburgueserías buenas de las excelentes. Reservas, burger especial del día, alérgenos, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-burger-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '17 fechas clave de hostelería (San Valentín, Navidad, Semana Santa, fútbol) con tareas y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-burger-mesa.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu hamburguesería, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para hamburguesería?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una hamburguesería. Solo tienes que personalizar: ajustar tareas a tu local, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye tareas de plancha, grill y smash burger?',
      a: 'Sí. Las tareas de plancha y grill cubren encendido, limpieza de superficie, control de temperatura, técnica smash burger (peso de bola, presión, tiempo), punto de carne (rare a well done) y limpieza entre turnos.',
    },
    {
      q: '¿Incluye tareas de freidora y control de aceite?',
      a: 'Sí. Hay tareas específicas para encendido y apagado de freidora, test polares del aceite, filtrado diario, cambio de aceite programado y control de temperatura para patatas, aros de cebolla y otros acompañamientos.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias hamburgueserías?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de hamburgueserías y consultores.',
    },
    {
      q: '¿Incluye tareas de delivery y packaging de burger?',
      a: 'Sí. Las tareas cubren packaging correcto de burger (que no se desmonte), control de tiempos de entrega, gestión de riders, etiquetado, preparación de pedidos y cierre de plataformas de delivery.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Día',
    subtitle:
      '9 checklists operativos para hamburguesería por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: plancha, freidora, línea, sala, barra',
      'Tareas del parrillero: smash burger, punto de carne, grill',
      'Control de freidora: test polares, filtrado, temperatura',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: parrillero, cocinero línea, freidurista, encargado',
      'Delivery y take-away: packaging burger, riders, tiempos',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle:
      'Parrilleros, encargados y dueños de hamburguesería que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Carlos Méndez',
        role: 'Parrillero / Grill Master, Smash & Co.',
        text: 'El checklist de plancha y grill me ha cambiado el turno. Antes cada parrillero limpiaba y calentaba la plancha a su manera. Ahora seguimos el mismo protocolo y el smash sale perfecto cada vez.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Marta Iglesias',
        role: 'Encargada, The Burger Lab',
        text: 'Gestionar la apertura de una hamburguesería con delivery y sala era un caos. Desde que imprimimos los checklists por zona, el equipo sabe exactamente qué hacer. Los olvidos bajaron un 90%.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Rubén Torres',
        role: 'Dueño, La Brasería Burger',
        text: 'Abrí mi hamburguesería hace 4 meses y me olvidaba de todo: encender la plancha a tiempo, filtrar la freidora, preparar los toppings. Estas checklists me organizaron desde el día uno.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Gerente de Operaciones, Grupo Burger Factory',
        text: 'Tenemos 4 hamburgueserías y antes cada encargado hacía las cosas diferente. Ahora con los checklists hemos estandarizado la operación. El onboarding de personal nuevo pasó de 2 semanas a 3 días.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Alejandro Fuentes',
        role: 'Cocinero de Línea, Stack Burger',
        text: 'La línea de montaje de burger es donde más nos ayudó. Cada ingrediente en su sitio, salsas repuestas, pan tostado a tiempo. Antes improvisábamos y los pedidos salían lentos. Ahora todo fluye.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Laura Navarro',
        role: 'Freidurista y Encargada, Crispy Burger Bar',
        text: 'El checklist de freidora es genial. Test polares del aceite, filtrado diario, control de temperatura para patatas y aros de cebolla. Antes se nos pasaba filtrar y el aceite duraba la mitad.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Sergio Ramos',
        role: 'Parrillero, Grill House BCN',
        text: 'Solo la parte de punto de carne ya vale el precio. Tenemos una guía clara para cada grosor y tipo de burger: rare, medium rare, medium, well done. Las quejas por punto bajaron a cero.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Diego Castillo',
        role: 'Responsable de Delivery, BurgerExpress',
        text: 'El checklist de packaging delivery nos cambió el negocio. Packaging correcto para que la burger no se desmonte, control de tiempos, etiquetado. Las devoluciones bajaron de 15 al mes a 2.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo Herrera',
        role: 'Chef Parrillero, Street Smash',
        text: 'Solo la plantilla de briefing pre-servicio ya vale el precio. Antes no hacíamos briefing. Ahora en 5 minutos repasamos reservas, burger especial del día y alérgenos. El servicio sale mucho mejor.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Andrés Molina',
        role: 'Consultor de Hamburgueserías',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Les pone orden desde el día uno. Plancha, freidora, línea, delivery... cubren el 95% de lo que necesita cualquier hamburguesería.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€39',
    price: '€12',
    discountBadge: '-69%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 69% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €27 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-tareas-pizzeria', label: 'Kit Tareas Pizzería' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  alreadyBought: {
    product: 'kit-tareas-hamburgueseria',
    label: '¿Ya compraste el Kit de Tareas Hamburguesería? Vuelve a entrar al dashboard',
  },
};

export default data;
