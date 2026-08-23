// astro-site/src/data/productos/tareas/kit-tareas-dark-kitchen.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasDarkKitchen.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-dark-kitchen/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-dark-kitchen.ts  (marquee de testimonios)
// NOTA: los componentes fuente de este producto en la SPA NO llevan tildes/eñes
// ("produccion", "gestion", "anos", "hosteleria", "Que" sin tilde, etc.). En v2.0 (2026-08-23)
// la ORTOGRAFÍA SÍ SE CORRIGE en esta landing —regla capital: ortografía perfecta en contenido
// publicado—; la SPA queda como estaba y ya NO es byte a byte en este punto.
// El resto del copy se porta verbatim: NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-dark-kitchen',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_DARK_KITCHEN',

  seo: {
    title: 'Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen | AI Chef Pro',
    description:
      '9 plantillas + 2 bonus (11 ficheros): checklists operativos pre-rellenados para dark kitchen multi-marca — estaciones de producción, empaquetado, plataformas (Glovo, Uber Eats, Just Eat), riders, perfiles y eventos. Solo €12.',
    keywords:
      'checklist dark kitchen, tareas dark kitchen, checklist ghost kitchen, checklist cocina fantasma, tareas cocina virtual, dark kitchen multi-marca, gestión plataformas delivery, empaquetado dark kitchen, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-dark-kitchen.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Dark Kitchen',
    productDescription:
      '9 plantillas + 2 bonus (11 ficheros): checklists operativos pre-rellenados para dark kitchen multi-marca con 331 tareas ya escritas — estaciones de producción, empaquetado, plataformas delivery, riders, perfiles y eventos.',
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
        body: 'Abrí mi dark kitchen hace 6 meses y me perdía con las tablets y el packaging. Estas checklists me organizaron desde el día uno.',
      },
      {
        author: 'Daniel Ortiz',
        rating: '5',
        body: 'El checklist de gestión de plataformas es oro puro. Activar marcas, pausar en horas pico, revisar valoraciones. Cero incidencias.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para dark kitchen multi-marca?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una dark kitchen multi-marca. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tus marcas.',
      },
      {
        q: '¿Incluye gestión de plataformas como Glovo, Uber Eats y Just Eat?',
        a: 'Sí. Activación/pausa de marcas, control de tiempos <12 min, gestión de incidencias, revisión de valoraciones y facturación por marca/plataforma.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varias dark kitchens?',
        a: 'Sí. Licencia personal para todos los establecimientos y marcas que gestiones.',
      },
      {
        q: '¿Incluye tareas de empaquetado y packaging por marca?',
        a: 'Sí. Packaging diferenciado por marca virtual, precintos de seguridad, etiquetado correcto y verificación de pedido completo.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
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
    // QUIRK de la SPA (no estructural): WhySection usa la imagen -producción (correcta), pero
    // BuyBox y CtaFinal NO usan imágenes de dark-kitchen — usan imágenes de la línea "restaurante"
    // (BuyBox.tsx / CtaFinal.tsx literales). Se porta verbatim, sin "corregir" el bug de origen.
    whyBg: '/lovable-uploads/ai-gallery/tareas-dk-produccion.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-restaurante-cocina.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-restaurante-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Dark Kitchen — Checklists Operativos Multi-Marca por Turno, Área y Perfil',
    description:
      '9 plantillas + 2 bonus (11 ficheros) en Excel con 331 tareas de dark kitchen ya escritas: estaciones de producción multi-marca, empaquetado y expedición, gestión de plataformas (Glovo, Uber Eats, Just Eat), riders, perfiles y eventos. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: estaciones de producción multi-marca, empaquetado, expedición',
      'Gestión de plataformas: activar/pausar marcas en Glovo, Uber Eats, Just Eat, tiempos <12 min',
      'Empaquetado por marca: precintos de seguridad, etiquetado, control de packaging diferenciado',
      'Coordinación de riders: zona de recogida, tiempos de espera, picos de demanda por plataforma',
      '3 plantillas maestras personalizables + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS DARK KITCHEN — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas + 2 Bonus (11 ficheros)',
    subtitle:
      '331 tareas de dark kitchen multi-marca ya escritas y repartidas por turno, estación y perfil. Ajusta a tus marcas, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '2 checklists: apertura y cierre de la cocina de producción multi-marca. Cada tarea con responsable, hora límite y firma. 55 tareas ya escritas solo en este fichero.',
      },
      {
        icon: 'Warehouse',
        title: 'Estaciones de Producción',
        desc: 'Encendido de equipos por estación, mise en place multi-marca, control de temperaturas, reposición de envases y packaging diferenciado por marca virtual.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información entre turnos.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: cocinero multi-marca, empaquetador/expedidor, gestor de plataformas y encargado/a de operaciones.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras (con tabla de vida útil en congelación), mantenimiento mensual de equipos, calibración de balanzas y revisión de packaging. + hoja Trimestral y Anual: DDD, extractores, extintores y BIE, gas, legionela y Verifactu, con número de parte y firma.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Checklist pre-evento (48h y día), picos de demanda (viernes/sábado noche), festivos con menú limitado, gestión de saturación de plataformas.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas maestras ya estructuradas (por franja horaria, por área y por perfil) con las secciones y la zona o el responsable puestos: tú solo escribes tus tareas en las celdas verdes.',
      },
      {
        icon: 'Building2',
        title: 'Apertura y Cierre de Negocio',
        desc: 'Checklist del local completo (no solo la cocina de producción): luces, alarma, TPV, accesos y zona de recogida de riders. Responsable y hora límite precargados en las 33 tareas.',
      },
      {
        icon: 'Wallet',
        title: 'Arqueo y Registro de Caja',
        desc: 'Apertura y cierre de caja con recuento por denominaciones, fondo de caja y descuadre automático frente al Z del TPV. Incluye registro mensual con descuadre por fórmula en las 31 filas del mes.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing pre-turno: marcas activas, promociones por plataforma, platos agotados, equipo del turno. Imprime y pega en cocina.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '22 fechas clave de hostelería con tareas asociadas y antelación recomendada, más 5 huecos para tus fechas locales.',
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
        title: 'Pre-Rellenadas para Dark Kitchen',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de una dark kitchen multi-marca. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Tablet',
        title: 'Gestión de Plataformas y Tablets',
        desc: 'Activar/pausar marcas en Glovo, Uber Eats, Just Eat. Control de tiempos de preparación <12 min, gestión de incidencias y facturación por marca/plataforma.',
      },
      {
        icon: 'Package',
        title: 'Empaquetado Multi-Marca y Riders',
        desc: 'Checklists para packaging diferenciado por marca virtual, precintos de seguridad, etiquetado, coordinación de riders y zona de expedición.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan las dark kitchens con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes, dark kitchens y ghost kitchens.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Plantilla de Briefing Pre-Turno',
        value: '€7',
        desc: 'La reunión de 5 minutos que separa a las dark kitchens buenas de las excelentes. Marcas activas, promociones por plataforma, platos agotados, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-dk-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '22 fechas clave de hostelería (San Valentín, Día del Padre, comuniones, Semana Santa, Black Friday, Todos los Santos, Navidad, días de pico delivery) con tareas y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-dk-tablets.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu dark kitchen, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para dark kitchen multi-marca?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una dark kitchen que opera varias marcas virtuales. Solo tienes que personalizar: ajustar tareas a tu operación, borrar las que no apliquen y añadir las específicas de tus marcas. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye gestión de plataformas como Glovo, Uber Eats y Just Eat?',
      a: 'Sí. Las tareas cubren activación/pausa de marcas por plataforma, control de tiempos de preparación (<12 min), gestión de incidencias, revisión de valoraciones, actualización de menús y facturación por marca/plataforma.',
    },
    {
      q: '¿Incluye tareas de empaquetado y packaging por marca?',
      a: 'Sí. Hay tareas específicas para packaging diferenciado por marca virtual, precintos de seguridad, etiquetado correcto, control de temperatura del packaging, y verificación de pedido completo antes de expedición.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias dark kitchens o marcas virtuales?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos y marcas que gestiones. Ideal para operadores multi-sede y consultores de dark kitchens.',
    },
    {
      q: '¿Incluye tareas de coordinación con riders?',
      a: 'Sí. Las tareas cubren gestión de zona de recogida, tiempos de espera por plataforma, protocolo de entrega, gestión de picos de demanda y comunicación con riders en hora punta.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle:
      '9 plantillas + 2 bonus (11 ficheros) por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: estaciones producción, empaquetado, expedición',
      'Gestión de plataformas: Glovo, Uber Eats, Just Eat, activar/pausar marcas',
      'Empaquetado multi-marca: packaging diferenciado, precintos, etiquetado',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: cocinero multi-marca, empaquetador, gestor plataformas, encargado',
      'Coordinación de riders: zona recogida, tiempos, picos de demanda',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle:
      'Operadores de dark kitchen, gestores de plataformas y empaquetadores que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Roberto Navarro',
        role: 'Operador Dark Kitchen, 4 marcas virtuales',
        text: 'Gestionar 4 marcas en la misma cocina era un caos. Desde que imprimimos los checklists por estación y por marca, los errores de empaquetado bajaron un 85%. Cada turno sabe exactamente qué hacer.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Morales',
        role: 'Duena, Ghost Kitchen Multi-Marca',
        text: 'Abrí mi dark kitchen hace 6 meses y me perdía con las tablets, las plataformas y el packaging diferente para cada marca. Estas checklists me organizaron desde el día uno. Imprescindible.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Daniel Ortiz',
        role: 'Encargado de Operaciones, CloudEats',
        text: 'El checklist de gestión de plataformas es oro puro. Activar marcas, pausar en horas pico, revisar valoraciones, actualizar menús. Antes se nos olvidaba la mitad. Ahora cero incidencias.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Carmen Ruiz',
        role: 'Cocinera Multi-Concepto, 3 marcas',
        text: 'Cocinar para 3 marcas distintas en la misma estación requiere organización militar. Los checklists por perfil me salvan el turno cada día. Sé exactamente qué preparar para cada marca.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Marcos Gimenez',
        role: 'Empaquetador/Expedidor, FoodFactory BCN',
        text: 'El checklist de empaquetado por marca me cambió la vida. Precintos de seguridad, etiquetado correcto, packaging diferenciado. Las reclamaciones por pedido incorrecto bajaron a cero.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Laura Serrano',
        role: 'Gestora de Plataformas, DarkKitchen Madrid',
        text: 'Gestionar Glovo, Uber Eats y Just Eat a la vez sin un checklist es imposible. Ahora tengo claro qué revisar al abrir, durante el servicio y al cerrar. Los tiempos de preparación bajaron a 10 min.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Pascual',
        role: 'Director de Operaciones, Grupo Virtual Foods',
        text: 'Tenemos 3 dark kitchens y antes cada encargado hacía las cosas diferente. Con los checklists estandarizamos la operación. El onboarding de personal nuevo pasó de 2 semanas a 3 días.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Hugo Martinez',
        role: 'Fundador, GhostBurger + GhostPoke + GhostWok',
        text: 'Lanzar una nueva marca virtual con estos checklists es mucho más fácil. Ya tienes las tareas base y solo adaptas los platos y el packaging. Ahorramos semanas en cada lanzamiento.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo Herrero',
        role: 'Chef Ejecutivo, Dark Kitchen Valencia',
        text: 'Solo la plantilla de briefing pre-turno ya vale el precio. Antes no hacíamos briefing. Ahora en 5 minutos repasamos marcas activas, promociones activas y platos agotados. El servicio sale perfecto.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Adrián Soto',
        role: 'Consultor de Dark Kitchens',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Les pone orden desde el día uno. Producción, empaquetado, plataformas, riders... cubren el 95% de lo que necesita cualquier dark kitchen.',
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
    { href: '/kit-tareas-hamburgueseria', label: 'Kit Tareas Hamburguesería' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-dark-kitchen',
    label: '¿Ya compraste el Kit de Tareas Dark Kitchen? Vuelve a entrar al dashboard',
  },
};

export default data;
