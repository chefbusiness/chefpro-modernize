// astro-site/src/data/productos/tareas/kit-tareas-bar.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasBar.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-bar/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-bar.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-bar',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_BAR',

  seo: {
    title: 'Kit de Tareas Recurrentes — Checklists Operativos para Bar / Cocktails | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para bar y cocktail bar: coctelería, barra, cerveza de grifo, vinos por copa, terraza, inventario y eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist bar, tareas bartender, checklist apertura bar, tareas coctelería, control stock bar, plantilla tareas barra, checklist cierre bar, inventario bar, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-bar.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Bar / Cocktails',
    productDescription:
      '9 checklists operativos pre-rellenados para bar y cocktail bar: coctelería, barra, cerveza de grifo, vinos por copa, terraza, inventario y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Álvaro Reyes',
        rating: '5',
        body: 'El checklist de mise en place de barra me cambió la vida. Ahora todo está listo antes de abrir.',
      },
      {
        author: 'Roberto Vega',
        rating: '5',
        body: 'Tenemos 4 bares y ahora con los checklists hemos estandarizado la operación.',
      },
      {
        author: 'Pablo García',
        rating: '5',
        body: 'Lo primero que hago con cada cliente nuevo es entregarle estos checklists. Cubren el 95% de lo que necesita cualquier bar.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para bar?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un bar profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Incluye tareas de coctelería?',
        a: 'Sí. Mise en place de coctelería, batches, jarabes, garnish, control de spirits y técnicas clásicas.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Bar / Cocktails',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
    ],
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Bar / Cocktails — Checklists por Turno, Zona y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu bar: coctelería, barra, cerveza de grifo, vinos por copa, terraza, inventario, eventos y perfiles. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: barra, coctelería, terraza, bodega',
      'Partidas: coctelería clásica, cerveza/grifo, vinos por copa, café',
      'Tareas por perfil: head bartender, bartender, barback, camarero',
      'Eventos: Nochevieja, Halloween, after-work, catas y maridajes',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS BAR — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de un bar de cocktails. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: 'Checklists completos: mise en place de barra, cristalería, máquina de café, terraza, cierre administrativo y limpieza. ~55 tareas pre-rellenadas.',
      },
      {
        icon: 'Wine',
        title: 'Partidas de Barra',
        desc: 'Coctelería clásica (spirits, batches, jarabes), cerveza de grifo (CO₂, temperatura, purga), vinos por copa y bodega.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus briefing con equipo y control de ambiente.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists para: head bartender, bartender, barback/auxiliar y camarero de sala/terraza.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda de grifos, mantenimiento de espresso, inventario semanal por categoría (spirits, cerveza, vino, mixers).',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Nochevieja, Halloween, St. Patrick, after-work semanal, noches de cócteles especiales, catas y maridajes.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por zona, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing diario: cóctel del día, reservas, VIPs, promociones activas, equipo del turno.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '17 fechas clave para bares con preparación especial y antelación recomendada.',
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
        title: 'Pre-Rellenadas para Bar',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un bar profesional. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Wine',
        title: 'Coctelería y Barra Completa',
        desc: 'Spirits, batches, jarabes, cerveza de grifo, vinos por copa, café espresso. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Perfiles Específicos',
        desc: 'Checklists para head bartender, bartender, barback y camarero. Cada puesto sabe exactamente qué hacer cada turno.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan bares con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes, bares y cocktail bars.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Plantilla de Briefing Pre-Servicio',
        value: '€7',
        desc: 'La reunión de 5 minutos que separa a los bares buenos de los excelentes. Cóctel del día, reservas, VIPs, promociones, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Fechas Clave',
        value: '€9',
        desc: '17 fechas clave para bares (Nochevieja, Halloween, St. Patrick, Negroni Week) con preparación especial y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu bar, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para bar de cocktails?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un bar profesional. Solo tienes que personalizar: ajustar tareas a tu bar, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye tareas de coctelería clásica y contemporánea?',
      a: 'Sí. Las partidas de barra cubren mise en place de coctelería, preparación de batches, jarabes especiales, garnish, control de spirits y técnicas clásicas. Adapta con tus recetas propias.',
    },
    {
      q: '¿Sirve para un bar de copas, cocktail bar y bar de hotel?',
      a: 'Sí. Las plantillas son escalables. Un bar pequeño puede usar barra + terraza. Un cocktail bar premium puede usar coctelería + bodega + eventos. Un hotel puede usar todas las zonas.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varios bares?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para grupos de bares y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle: '9 checklists operativos para bar por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: barra, coctelería, terraza',
      'Partidas: spirits, batches, cerveza grifo, vinos, café',
      'Inventario semanal: spirits, cerveza, vino, mixers, consumibles',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: head bartender, bartender, barback, camarero',
      'Eventos: Nochevieja, Halloween, after-work, catas',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Fechas Clave (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle: 'Bartenders, encargados y dueños de bar que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Álvaro Reyes',
        role: 'Head Bartender, The Alchemist Bar',
        text: 'El checklist de mise en place de barra me cambió la vida. Antes cada bartender montaba a su manera y siempre faltaba algo en medio del servicio. Ahora todo está listo antes de abrir.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Claudia Martín',
        role: 'Propietaria, Cocktail Lab BCN',
        text: 'Abrí mi bar de cócteles hace 8 meses y el caos de las primeras semanas fue brutal. Los checklists por zona y turno pusieron orden desde el día que los imprimimos.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Roberto Vega',
        role: 'Gerente, Grupo Bar Madrid',
        text: 'Tenemos 4 bares y antes cada encargado hacía las cosas diferente. Ahora con los checklists hemos estandarizado la operación. El onboarding de barbacks pasó de 3 semanas a 5 días.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Marina Torres',
        role: 'Bartender, Hotel Arts Barcelona',
        text: 'Las tareas por perfil son geniales. Como bartender, sé exactamente qué tengo que hacer antes, durante y después del servicio. No hay excusas para olvidar nada.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Ruiz',
        role: 'Head Bartender, Speakeasy Madrid',
        text: 'El control de inventario semanal por categoría (spirits, cerveza, vino, mixers) es justo lo que necesitábamos. Antes el pour cost nos sorprendía cada mes. Ahora lo controlamos.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Sofía Hernández',
        role: 'Encargada, Vermutería El Rincón',
        text: 'Los checklists de limpieza de grifos de cerveza y mantenimiento de máquina de espresso nos han salvado de averías. Antes no teníamos protocolo de mantenimiento preventivo.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Ignacio López',
        role: 'Barback, Cocktail Bar Negroni',
        text: 'Como barback, el checklist de mi perfil me dice exactamente qué reponer, cuándo y dónde. No tengo que estar preguntando al bartender cada 5 minutos. Me da autonomía.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Enrique Campos',
        role: 'Director de Operaciones, Grupo Nightlife',
        text: 'El calendario anual con las fechas clave (Nochevieja, Halloween, St. Patrick) nos ayuda a planificar stock y personal con semanas de antelación. Antes improvisábamos y se notaba.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo García',
        role: 'Consultor de Bares y Restaurantes',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estos checklists. Barra, bodega, terraza, inventario... cubren el 95% de lo que necesita cualquier bar profesional.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Carlos Navarro',
        role: 'Formador de Bartenders, Escuela de Hostelería',
        text: 'Recomiendo este kit a todos mis alumnos. Las tareas de coctelería, control de stock y cierre de barra están perfectamente estructuradas. Es el estándar que debería tener todo bar.',
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
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-tareas-pasteleria', label: 'Kit Tareas Pastelería' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-bar',
    label: '¿Ya compraste el Kit de Tareas Bar? Vuelve a entrar al dashboard',
  },
};

export default data;
