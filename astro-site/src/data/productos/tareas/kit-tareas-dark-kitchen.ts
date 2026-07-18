// astro-site/src/data/productos/tareas/kit-tareas-dark-kitchen.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasDarkKitchen.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-dark-kitchen/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-dark-kitchen.ts  (marquee de testimonios)
// NOTA: los componentes fuente de este producto NO llevan tildes/eñes (quirk propio de este
// producto en la SPA: "produccion", "gestion", "anos", "hosteleria", "Que" sin tilde, etc.).
// Se porta VERBATIM tal cual está en el código fuente — NO se corrige ortografía.
// NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-dark-kitchen',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_DARK_KITCHEN',

  seo: {
    title: 'Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para dark kitchen multi-marca: estaciones de produccion, empaquetado, plataformas (Glovo, Uber Eats, Just Eat), riders, perfiles y eventos. Solo €12.',
    keywords:
      'checklist dark kitchen, tareas dark kitchen, checklist ghost kitchen, checklist cocina fantasma, tareas cocina virtual, dark kitchen multi-marca, gestion plataformas delivery, empaquetado dark kitchen, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-dark-kitchen.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen',
    productDescription:
      '9 checklists operativos pre-rellenados para dark kitchen multi-marca: estaciones de produccion, empaquetado, plataformas delivery, riders, perfiles y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '10', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Roberto Navarro',
        rating: '5',
        body: 'Gestionar 4 marcas en la misma cocina era un caos. Desde que imprimimos los checklists, los errores de empaquetado bajaron un 85%.',
      },
      {
        author: 'Elena Morales',
        rating: '5',
        body: 'Abri mi dark kitchen hace 6 meses y me perdia con las tablets y el packaging. Estas checklists me organizaron desde el dia uno.',
      },
      {
        author: 'Daniel Ortiz',
        rating: '5',
        body: 'El checklist de gestion de plataformas es oro puro. Activar marcas, pausar en horas pico, revisar valoraciones. Cero incidencias.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para dark kitchen multi-marca?',
        a: 'Si. Cada checklist viene pre-rellenado con las tareas reales de una dark kitchen multi-marca. Solo personaliza: ajustar, borrar lo que no aplique y anadir lo especifico de tus marcas.',
      },
      {
        q: '¿Incluye gestion de plataformas como Glovo, Uber Eats y Just Eat?',
        a: 'Si. Activacion/pausa de marcas, control de tiempos <12 min, gestion de incidencias, revision de valoraciones y facturacion por marca/plataforma.',
      },
      {
        q: '¿En que se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago unico. Sin suscripcion, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varias dark kitchens?',
        a: 'Si. Licencia personal para todos los establecimientos y marcas que gestiones.',
      },
      {
        q: '¿Incluye tareas de empaquetado y packaging por marca?',
        a: 'Si. Packaging diferenciado por marca virtual, precintos de seguridad, etiquetado correcto y verificacion de pedido completo.',
      },
      {
        q: '¿Hay garantia de devolucion?',
        a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Dark Kitchen',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-dk-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-produccion.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-empaquetado.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-expedicion.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-tablets.jpg',
      '/lovable-uploads/ai-gallery/tareas-dk-equipo.jpg',
    ],
    // QUIRK de la SPA (no estructural): WhySection usa la imagen -produccion (correcta), pero
    // BuyBox y CtaFinal NO usan imágenes de dark-kitchen — usan imágenes de la línea "restaurante"
    // (BuyBox.tsx / CtaFinal.tsx literales). Se porta verbatim, sin "corregir" el bug de origen.
    whyBg: '/lovable-uploads/ai-gallery/tareas-dk-produccion.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-restaurante-cocina.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-restaurante-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra 60-75/mes, tu lo tienes por 12 -- para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Dark Kitchen — Checklists Operativos Multi-Marca por Turno, Area y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu dark kitchen: estaciones de produccion multi-marca, empaquetado y expedicion, gestion de plataformas (Glovo, Uber Eats, Just Eat), riders, perfiles y eventos. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: estaciones de produccion multi-marca, empaquetado, expedicion',
      'Gestion de plataformas: activar/pausar marcas en Glovo, Uber Eats, Just Eat, tiempos <12 min',
      'Empaquetado por marca: precintos de seguridad, etiquetado, control de packaging diferenciado',
      'Coordinacion de riders: zona de recogida, tiempos de espera, picos de demanda por plataforma',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS DARK KITCHEN — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de una dark kitchen multi-marca. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '6 checklists: apertura y cierre de estaciones de produccion, zona de empaquetado, expedicion y zona de riders. Cada tarea con responsable, hora limite y firma. ~80 tareas pre-rellenadas.',
      },
      {
        icon: 'Warehouse',
        title: 'Estaciones de Produccion',
        desc: 'Encendido de equipos por estacion, mise en place multi-marca, control de temperaturas, reposicion de envases y packaging diferenciado por marca virtual.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por dia) y mensual. Plus handover de cambio de turno con traspaso de informacion entre turnos.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: cocinero multi-marca, empaquetador/expedidor, gestor de plataformas y encargado/a de operaciones.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revision FIFO de camaras, mantenimiento mensual de equipos, calibracion de balanzas y revision de packaging.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Checklist pre-evento (48h y dia), picos de demanda (viernes/sabado noche), festivos con menu limitado, gestion de saturacion de plataformas.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por area, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing pre-turno: marcas activas, promociones por plataforma, platos agotados, equipo del turno. Imprime y pega en cocina.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '17 fechas clave de hosteleria con tareas asociadas y antelacion recomendada. Anade tus fechas locales.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Que Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genericas. Son checklists disenados por un profesional con 29 anos en alta hosteleria.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Dark Kitchen',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de una dark kitchen multi-marca. Solo ajusta, borra lo que no aplique y anade lo que te falte.',
      },
      {
        icon: 'Tablet',
        title: 'Gestion de Plataformas y Tablets',
        desc: 'Activar/pausar marcas en Glovo, Uber Eats, Just Eat. Control de tiempos de preparacion <12 min, gestion de incidencias y facturacion por marca/plataforma.',
      },
      {
        icon: 'Package',
        title: 'Empaquetado Multi-Marca y Riders',
        desc: 'Checklists para packaging diferenciado por marca virtual, precintos de seguridad, etiquetado, coordinacion de riders y zona de expedicion.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra 60/mes. Esto es 12',
        desc: 'Las mismas listas de tareas que usan las dark kitchens con SaaS premium como Trail, pero en Excel por un pago unico. Sin suscripcion.',
      },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de calculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Mas de 29 anos de carrera profesional en alta hosteleria y restauracion, y 15 anos en consultoria gastronomica. Ha disenado sistemas operativos y checklists para cientos de restaurantes, dark kitchens y ghost kitchens.',
  // Quirk tilde-free de este producto: chips SIN tildes (AuthorSection.tsx L29/L32).
  authorBadges: ['Consultor Gastronomico', '+29 anos en alta hosteleria'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Ademas de las 9 plantillas, recibiras estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Plantilla de Briefing Pre-Turno',
        value: '€7',
        desc: 'La reunion de 5 minutos que separa a las dark kitchens buenas de las excelentes. Marcas activas, promociones por plataforma, platos agotados, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-dk-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '17 fechas clave de hosteleria (San Valentin, Navidad, Semana Santa, Black Friday, dias de pico delivery) con tareas y antelacion recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-dk-tablets.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SI, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu dark kitchen, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Dias de garantia' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incomodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para dark kitchen multi-marca?',
      a: 'Si. Cada checklist viene pre-rellenado con las tareas reales de una dark kitchen que opera varias marcas virtuales. Solo tienes que personalizar: ajustar tareas a tu operacion, borrar las que no apliquen y anadir las especificas de tus marcas. Las celdas editables estan marcadas en verde.',
    },
    {
      q: '¿Incluye gestion de plataformas como Glovo, Uber Eats y Just Eat?',
      a: 'Si. Las tareas cubren activacion/pausa de marcas por plataforma, control de tiempos de preparacion (<12 min), gestion de incidencias, revision de valoraciones, actualizacion de menus y facturacion por marca/plataforma.',
    },
    {
      q: '¿Incluye tareas de empaquetado y packaging por marca?',
      a: 'Si. Hay tareas especificas para packaging diferenciado por marca virtual, precintos de seguridad, etiquetado correcto, control de temperatura del packaging, y verificacion de pedido completo antes de expedicion.',
    },
    {
      q: '¿En que se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/moviles. Este kit te da las mismas listas de tareas en Excel por €12, pago unico. Sin suscripcion, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias dark kitchens o marcas virtuales?',
      a: 'Si. La licencia es personal — puedes usar los checklists en todos los establecimientos y marcas que gestiones. Ideal para operadores multi-sede y consultores de dark kitchens.',
    },
    {
      q: '¿Incluye tareas de coordinacion con riders?',
      a: 'Si. Las tareas cubren gestion de zona de recogida, tiempos de espera por plataforma, protocolo de entrega, gestion de picos de demanda y comunicacion con riders en hora punta.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle:
      '9 checklists operativos para dark kitchen por menos de lo que cuesta una hora de consultoria.',
    items: [
      'Checklists de apertura y cierre: estaciones produccion, empaquetado, expedicion',
      'Gestion de plataformas: Glovo, Uber Eats, Just Eat, activar/pausar marcas',
      'Empaquetado multi-marca: packaging diferenciado, precintos, etiquetado',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: cocinero multi-marca, empaquetador, gestor plataformas, encargado',
      'Coordinacion de riders: zona recogida, tiempos, picos de demanda',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SI, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle:
      'Operadores de dark kitchen, gestores de plataformas y empaquetadores que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Roberto Navarro',
        role: 'Operador Dark Kitchen, 4 marcas virtuales',
        text: 'Gestionar 4 marcas en la misma cocina era un caos. Desde que imprimimos los checklists por estacion y por marca, los errores de empaquetado bajaron un 85%. Cada turno sabe exactamente que hacer.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Morales',
        role: 'Duena, Ghost Kitchen Multi-Marca',
        text: 'Abri mi dark kitchen hace 6 meses y me perdia con las tablets, las plataformas y el packaging diferente para cada marca. Estas checklists me organizaron desde el dia uno. Imprescindible.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Daniel Ortiz',
        role: 'Encargado de Operaciones, CloudEats',
        text: 'El checklist de gestion de plataformas es oro puro. Activar marcas, pausar en horas pico, revisar valoraciones, actualizar menus. Antes se nos olvidaba la mitad. Ahora cero incidencias.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Carmen Ruiz',
        role: 'Cocinera Multi-Concepto, 3 marcas',
        text: 'Cocinar para 3 marcas distintas en la misma estacion requiere organizacion militar. Los checklists por perfil me salvan el turno cada dia. Se exactamente que preparar para cada marca.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Marcos Gimenez',
        role: 'Empaquetador/Expedidor, FoodFactory BCN',
        text: 'El checklist de empaquetado por marca me cambio la vida. Precintos de seguridad, etiquetado correcto, packaging diferenciado. Las reclamaciones por pedido incorrecto bajaron a cero.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Laura Serrano',
        role: 'Gestora de Plataformas, DarkKitchen Madrid',
        text: 'Gestionar Glovo, Uber Eats y Just Eat a la vez sin un checklist es imposible. Ahora tengo claro que revisar al abrir, durante el servicio y al cerrar. Los tiempos de preparacion bajaron a 10 min.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Pascual',
        role: 'Director de Operaciones, Grupo Virtual Foods',
        text: 'Tenemos 3 dark kitchens y antes cada encargado hacia las cosas diferente. Con los checklists estandarizamos la operacion. El onboarding de personal nuevo paso de 2 semanas a 3 dias.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Hugo Martinez',
        role: 'Fundador, GhostBurger + GhostPoke + GhostWok',
        text: 'Lanzar una nueva marca virtual con estos checklists es mucho mas facil. Ya tienes las tareas base y solo adaptas los platos y el packaging. Ahorramos semanas en cada lanzamiento.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo Herrero',
        role: 'Chef Ejecutivo, Dark Kitchen Valencia',
        text: 'Solo la plantilla de briefing pre-turno ya vale el precio. Antes no haciamos briefing. Ahora en 5 minutos repasamos marcas activas, promociones activas y platos agotados. El servicio sale perfecto.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Adrian Soto',
        role: 'Consultor de Dark Kitchens',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Les pone orden desde el dia uno. Produccion, empaquetado, plataformas, riders... cubren el 95% de lo que necesita cualquier dark kitchen.',
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
    { href: '/kit-tareas-hamburgueseria', label: 'Kit Tareas Hamburgueseria' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  alreadyBought: {
    product: 'kit-tareas-dark-kitchen',
    label: '¿Ya compraste el Kit de Tareas Dark Kitchen? Vuelve a entrar al dashboard',
  },
};

export default data;
