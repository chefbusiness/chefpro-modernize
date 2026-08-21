// astro-site/src/data/productos/tareas/kit-tareas-pizzeria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasPizzeria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-pizzeria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-pizzeria.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-pizzeria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_PIZZERIA',

  seo: {
    title: 'Kit de Tareas Recurrentes — Checklists Operativos para Pizzería | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para pizzería: horno de leña/piedra, masa napolitana, línea de montaje, delivery, perfiles y eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist pizzería, tareas apertura pizzería, checklist horno pizza, tareas pizzero, checklist delivery pizzería, lista tareas pizzería, plantilla tareas pizzería, control horno pizza, masa napolitana checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-pizzeria.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Pizzería',
    productDescription:
      '9 checklists operativos pre-rellenados para pizzería: horno de leña/piedra, masa napolitana, línea de montaje, delivery, perfiles y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '10', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Marco Ferrara',
        rating: '5',
        body: 'El checklist de horno de leña me ha salvado. Ahora seguimos el mismo protocolo y el leopardo sale perfecto en cada pizza.',
      },
      {
        author: 'Elena Campos',
        rating: '5',
        body: 'Gestionar la apertura de una pizzería con delivery y sala era un caos. Los checklists por zona nos organizaron desde el día uno.',
      },
      {
        author: 'Daniel Ortiz',
        rating: '5',
        body: 'Las tareas de fermentación, estirado a mano y control de cocción están perfectamente estructuradas. Es lo que debería tener toda pizzería.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para pizzería?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una pizzería. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local.',
      },
      {
        q: '¿Sirve para horno de leña y horno eléctrico?',
        a: 'Sí. Las tareas cubren horno de leña (encendido, gestión de leña, limpieza ceniza) y horno eléctrico/piedra (precalentamiento, limpieza solera, control resistencias).',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varias pizzerías?',
        a: 'Sí. Licencia personal para todos los establecimientos que gestiones.',
      },
      {
        q: '¿Incluye tareas de delivery y take-away?',
        a: 'Sí. Gestión de riders, control de tiempos, packaging, etiquetado y cierre de plataformas de delivery.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Pizzería',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-linea.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-delivery.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-mesa.jpg',
    ],
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-linea.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-delivery.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/tareas-pizzeria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-pizzeria-masa.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-pizzeria-horno.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Pizzería — Checklists Operativos por Turno, Área y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu pizzería: horno de leña/piedra, masa napolitana, línea de montaje, delivery, perfiles y eventos. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: horno, línea de montaje, sala, barra',
      'Control de horno de leña/piedra: temperatura 400-450 °C, limpieza, encendido',
      'Tareas del pizzero: fermentación lenta, estirado a mano, cocción 60-90s',
      'Gestión de delivery y take-away: packaging, riders, control de tiempos',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS PIZZERÍA — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de una pizzería. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '6 checklists: apertura y cierre de horno, línea de montaje, sala y barra. Cada tarea con responsable, hora límite y firma. ~80 tareas pre-rellenadas.',
      },
      {
        icon: 'Flame',
        title: 'Tareas del Horno',
        desc: 'Encendido de horno de leña/piedra, control de temperatura 400-450 °C, limpieza de solera, gestión de leña, rotación de pizzas en cámara.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: pizzero/maestro pizzero, cocinero de línea, encargado/a, camarero/a y repartidor.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de horno, amasadora y cámara de fermentación.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Checklist pre-evento (48h→día), noche de pizza especial, festivos con menú limitado, gestión de picos de delivery.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por área, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing pre-servicio: reservas, pizza del día, alérgenos, equipo del turno. Imprime y pega en cocina.',
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
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Pizzería',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de una pizzería. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Flame',
        title: 'Control de Horno y Masa',
        desc: 'Encendido, temperatura 400-450 °C, limpieza de solera, fermentación lenta de masa, estirado a mano, cocción 60-90s. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Delivery y Packaging',
        desc: 'Checklists para gestión de riders, control de tiempos de entrega, packaging correcto, take-away y plataformas de delivery.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan las pizzerías con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes y pizzerías.',

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
        desc: 'La reunión de 5 minutos que separa a las pizzerías buenas de las excelentes. Reservas, pizza del día, alérgenos, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-pizzeria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '17 fechas clave de hostelería (San Valentín, Navidad, Semana Santa, fútbol) con tareas y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-pizzeria-mesa.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu pizzería, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para pizzería?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una pizzería. Solo tienes que personalizar: ajustar tareas a tu local, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Sirve para horno de leña y horno eléctrico/piedra?',
      a: 'Sí. Las tareas de control de horno cubren tanto horno de leña (encendido, gestión de leña, limpieza de ceniza, control de llama) como horno eléctrico/piedra (precalentamiento, limpieza de solera, control de resistencias). Adapta el checklist a tu tipo de horno.',
    },
    {
      q: '¿Incluye tareas de gestión de delivery y take-away?',
      a: 'Sí. Hay tareas específicas para gestión de riders, control de tiempos de entrega, packaging correcto, etiquetado, preparación de pedidos y cierre de plataformas de delivery.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias pizzerías?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de pizzerías y consultores.',
    },
    {
      q: '¿Incluye tareas de fermentación y masa napolitana?',
      a: 'Sí. Las tareas del pizzero incluyen fermentación lenta de masa (24-72h), control de temperatura de masa madre, estirado a mano, control del patrón leopardo en la cocción y gestión del banco de masas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Día',
    subtitle: '9 checklists operativos para pizzería por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: horno, línea, sala, barra',
      'Tareas del pizzero: fermentación, estirado, cocción 60-90s',
      'Control de horno: temperatura 400-450 °C, limpieza, leña',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: pizzero, cocinero línea, encargado, repartidor',
      'Delivery y take-away: packaging, riders, tiempos',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle: 'Pizzeros, encargados y dueños de pizzería que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Marco Ferrara',
        role: 'Maestro Pizzero, Forno Napoli',
        text: 'El checklist de horno de leña me ha salvado. Antes cada pizzero encendía el horno a su manera y la temperatura era inconsistente. Ahora seguimos el mismo protocolo y el leopardo sale perfecto en cada pizza.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Campos',
        role: 'Encargada, Pizza & Brasa',
        text: 'Gestionar la apertura de una pizzería con delivery y sala era un caos. Desde que imprimimos los checklists por zona, el equipo sabe exactamente qué hacer antes de abrir. Los olvidos bajaron un 90%.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Alberto Moreno',
        role: 'Dueño, La Masa Madre Pizzería',
        text: 'Abrí mi pizzería hace 6 meses y me olvidaba de todo: encender el horno a tiempo, sacar las masas de la cámara, preparar el banco de ingredientes. Estas checklists me organizaron desde el día uno.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Lucía Hernández',
        role: 'Gerente de Operaciones, Grupo Pizzería Roma',
        text: 'Tenemos 3 pizzerías y antes cada encargado hacía las cosas diferente. Ahora con los checklists hemos estandarizado la operación. El onboarding de personal nuevo pasó de 2 semanas a 3 días.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Daniel Ortiz',
        role: 'Pizzero y Formador',
        text: 'Como formador de pizzeros, recomiendo este kit a todos mis alumnos. Las tareas de fermentación, estirado a mano y control de cocción están perfectamente estructuradas. Es lo que debería tener toda pizzería.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Carmen Ruiz',
        role: 'Directora, Pizzería Artesana BCN',
        text: 'El checklist de delivery nos cambió el negocio. Control de tiempos, packaging correcto, etiquetado para repartidores. Las quejas por pedidos incorrectos bajaron de 12 al mes a 1 o 2.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Domínguez',
        role: 'Cocinero de Línea, Il Forno',
        text: 'La línea de montaje de pizza es donde más nos ayudó. Cada ingrediente en su sitio, reposición a tiempo, limpieza entre turnos. Antes improvisábamos, ahora todo fluye.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Roberto Sánchez',
        role: 'Repartidor y Encargado de Delivery, PizzaExpress',
        text: 'El checklist de cierre de delivery es genial. Antes siempre se nos olvidaba cerrar alguna plataforma o limpiar las bolsas térmicas. Ahora todo queda hecho y documentado.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo García',
        role: 'Chef Pizzero, Napoli Street Food',
        text: 'Solo la plantilla de briefing pre-servicio ya vale el precio. Antes no hacíamos briefing. Ahora en 5 minutos repasamos reservas, pizza especial del día y alérgenos. El servicio sale mucho mejor.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Sergio Navarro',
        role: 'Consultor de Pizzerías',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Les pone orden desde el día uno. Horno, masa, línea, delivery... cubren el 95% de lo que necesita cualquier pizzería.',
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
    { href: '/kit-tareas-cafeteria', label: 'Kit Tareas Cafetería' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  alreadyBought: {
    product: 'kit-tareas-pizzeria',
    label: '¿Ya compraste el Kit de Tareas Pizzería? Vuelve a entrar al dashboard',
  },
};

export default data;
