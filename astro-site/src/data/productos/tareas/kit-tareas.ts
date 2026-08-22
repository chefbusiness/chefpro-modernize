// astro-site/src/data/productos/tareas/kit-tareas.ts
// Producto BASE de la Línea Tareas (restaurante casual genérico). Copy VERBATIM (byte a byte)
// extraído de:
//   - src/pages/KitTareas.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-tareas.ts  (marquee de testimonios)
//
// ⚠️ DIVERGENCIA (paridad exacta): en la SPA, HeroSection.tsx y ContentGrid.tsx usan DOS
// arrays de imágenes DISTINTOS (a diferencia de kit-tareas-asador, donde son la misma lista):
//   Hero (heroImages):    hero, apertura, manager, sala, limpieza, eventos
//   Grid (galleryImages):        apertura, manager, sala, limpieza, eventos, perfiles
// Comparten 5/6; difieren solo en el extremo (Hero añade "-hero.jpg", Grid añade "-perfiles.jpg").
// RESUELTO: images.gallery = lista del HERO (fondo hero) e images.gridGallery = lista del GRID
// (strip visible del ContentGrid). El template usa `gridGallery ?? gallery`, de modo que Asador
// (listas idénticas) sigue omitiendo gridGallery sin cambio de comportamiento.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS',

  seo: {
    title: 'Kit de Tareas Recurrentes — Checklists Operativos para Restaurante | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para restaurante casual: apertura, cierre, partidas, manager, perfiles, eventos. Imprime, delega y firma. Solo €14.',
    keywords:
      'checklist restaurante, tareas apertura restaurante, checklist cierre cocina, lista tareas cocina, checklist manager restaurante, tareas recurrentes hostelería, mise en place checklist, plantilla tareas restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes Pro — Checklists Operativos para Restaurante',
    productDescription:
      '9 checklists operativos pre-rellenados para restaurante casual: apertura, cierre, partidas de cocina, manager, perfiles profesionales, eventos y festivos.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '10', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Diego Martín',
        rating: '5',
        body: 'Desde que imprimimos los checklists de apertura y cierre, no se olvida ni una tarea. El equipo sabe exactamente qué hacer.',
      },
      {
        author: 'Ana Belén Roca',
        rating: '5',
        body: 'Gestiono 3 restaurantes y ahora todos siguen el mismo estándar. Las listas por perfil son geniales para el onboarding.',
      },
      {
        author: 'Javier López',
        rating: '5',
        body: 'Pagábamos €60 al mes por Trail. Esto hace lo mismo en Excel por €14. No necesito más.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un restaurante casual. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local.',
      },
      {
        q: '¿Cómo funciona el sistema de firma?',
        a: 'Cada checklist tiene columnas de responsable, hora límite, completada y firma. El manager imprime, entrega al equipo, cada persona marca y firma.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €14, pago único. Sin suscripción, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varios restaurantes?',
        a: 'Sí. Licencia personal para todos los establecimientos que gestiones.',
      },
      {
        q: '¿Incluye tareas para eventos?',
        a: 'Sí. Checklists para eventos privados, San Valentín, Navidad, apertura y cierre de terraza.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes',
  },

  images: {
    // DIVERGENCIA (ver nota arriba): SPA usa DOS listas distintas.
    // gallery = heroImages (HeroSection.tsx) → fondo del hero.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-restaurante-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-apertura.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-manager.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-sala.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-limpieza.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
    ],
    // gridGallery = galleryImages (ContentGrid.tsx) → strip visible del ContentGrid.
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-restaurante-apertura.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-manager.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-sala.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-limpieza.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-perfiles.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60/mes, tú lo tienes por €14 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Restaurante Casual — Checklists Operativos por Turno, Área y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu restaurante: apertura, cierre, partidas de cocina, manager, perfiles, eventos y festivos. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre por área (cocina, sala, barra)',
      'Tareas por perfil: chef, sous chef, jefe sala, camarero, barman',
      'Tareas del manager: diario, semanal y mensual',
      'Plantillas de eventos y festivos (San Valentín, Navidad)',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  stickyLabel: 'KIT TAREAS — €14',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de un restaurante casual. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '6 checklists: apertura cocina, sala, barra + cierre cocina, sala, barra. Cada tarea con responsable, hora límite y firma. ~90 tareas pre-rellenadas.',
      },
      {
        icon: 'ChefHat',
        title: 'Partidas de Cocina',
        desc: 'Tareas antes, durante y después del servicio para partida de calientes, fríos y mise en place general. Control de tiempos y calidad.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: jefe de cocina, sous chef, jefe de sala, camarero y barman. Las responsabilidades diarias de cada puesto.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de equipos y seguridad.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Checklist pre-evento (48h→día), San Valentín, Navidad/Nochevieja, apertura y cierre de temporada de terraza.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por área, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing pre-servicio: reservas, platos del día, 86s, alérgenos, equipo del turno. Imprime y pega en el pase.',
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
        title: 'Pre-Rellenadas y Listas para Usar',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un restaurante casual. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Clock',
        title: 'Organizadas por Turno y Área',
        desc: 'Apertura, servicio, cierre. Cocina, sala, barra, terraza. Cada tarea en su momento y su lugar. Tu equipo sabe exactamente qué hacer y cuándo.',
      },
      {
        icon: 'Users',
        title: 'Delegación con Firma',
        desc: "Imprime el checklist, entrégalo al responsable. Cuando termine, firma y archiva. Fin de las excusas de 'no sabía que tenía que hacerlo'.",
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €14',
        desc: 'Las mismas listas de tareas que usan los restaurantes con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes.',

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
        desc: 'La reunión de 5 minutos que separa a los restaurantes buenos de los excelentes. Reservas, platos del día, alérgenos, 86s, equipo.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-manager.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '17 fechas clave de hostelería (San Valentín, Navidad, Semana Santa, terraza) con tareas y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €14',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu restaurante, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un restaurante casual. Solo tienes que personalizar: ajustar tareas a tu local, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Cómo funciona el sistema de firma?',
      a: 'Cada checklist tiene columnas de: responsable, hora límite, completada (✓) y firma. El manager imprime el checklist, lo entrega al equipo, cada persona marca y firma sus tareas. Al final del turno, el encargado verifica y firma al pie.',
    },
    {
      q: '¿Funcionan con Google Sheets?',
      a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets. Pero la idea es imprimirlos en A4 — son checklists operativos diseñados para tener en la cocina, no en una pantalla.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €14, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varios restaurantes?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para grupos de restauración y consultores.',
    },
    {
      q: '¿Incluye tareas para eventos y festivos?',
      a: 'Sí. Hay checklists específicos para eventos privados (48h antes → post-evento), San Valentín, Navidad/Nochevieja, apertura y cierre de temporada de terraza.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Día',
    subtitle: '9 checklists operativos por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: cocina, sala, barra',
      'Tareas por partida de cocina: calientes, fríos, mise en place',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: chef, sous chef, sala, camarero, barman',
      'Limpieza profunda semanal + FIFO + mantenimiento',
      'Eventos y festivos: San Valentín, Navidad, terraza',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €14',
  },

  testimonials: {
    subtitle: 'Hosteleros que ya tienen sus operaciones bajo control con los checklists',
    items: [
      {
        name: 'Alberto Riera',
        role: 'Chef Ejecutivo, Restaurante Origen',
        text: 'Antes la mise en place dependía de quién estuviera en la partida. Desde que imprimimos los checklists de apertura y partidas, la preparación es consistente cada día. Los cocineros saben exactamente qué hacer sin que yo tenga que repetirlo.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Elena Navarro',
        role: 'Directora de Operaciones, Grupo Tres Tenedores',
        text: 'Gestionar 3 restaurantes con equipos distintos era un caos. Con estas checklists hemos estandarizado la apertura, cierre y tareas de manager en los tres locales. Ahora todos siguen el mismo sistema y los resultados se notan.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'David Molina',
        role: 'Propietario, Gastrobar La Esquina',
        text: 'Abrí mi primer restaurante hace un año y se me olvidaba todo: encender el horno, revisar reservas, reponer servilletas. Con las checklists reduje los olvidos un 80%. Literalmente salvaron mi operación diaria.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Marta Herrero',
        role: 'Consultora de Hostelería',
        text: 'Cada vez que empiezo con un cliente nuevo, lo primero que hago es entregarle estas checklists. Les pone orden desde el día uno. Es lo más práctico que he encontrado para organizar las tareas de un restaurante.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Sergio Blanco',
        role: 'Gerente, Brasserie Central',
        text: 'Antes, un nuevo camarero necesitaba dos semanas para aprender la rutina completa. Ahora con las checklists por perfil, en 2 días ya sabe qué hacer en cada turno. La rotación de personal ya no es un drama.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Cristina Pardo',
        role: 'Propietaria, Café Amanecer',
        text: 'Imprimí la checklist de apertura y la pegué en la puerta de la cocina. El equipo la sigue como un ritual cada mañana. Ya no tengo que preguntar si han encendido la cafetera o revisado la vitrina. Está todo marcado.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Fernando López',
        role: 'Propietario, Restaurante Mesa Abierta',
        text: 'Solo la plantilla de briefing pre-servicio ya vale el precio. Antes el briefing era improvisado y duraba 30 segundos. Ahora repasamos platos del día, alérgenos, reservas VIP y objetivos en 5 minutos. El servicio sale mucho mejor.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Raúl Domínguez',
        role: 'Jefe de Cocina, Hotel Litoral',
        text: 'Llevo 25 años en cocina y siempre me fié de mi memoria para las tareas diarias. Cuando pasé todo a checklists en papel, descubrí que se me escapaban 4-5 cosas al día. Ahora no se me olvida nada y duermo más tranquilo.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Pablo Santana',
        role: 'Consultor Gastronómico',
        text: 'Lo recomiendo a todos mis clientes de consultoría sin excepción. Las checklists de apertura, cierre y tareas del manager cubren el 90% de lo que necesita cualquier restaurante para funcionar con orden. Es un must-have.',
        avatar: '/avatars/chef-avatar-5.jpg',
      },
      {
        name: 'Ignacio Ferrer',
        role: 'Director F&B, Hotel Gran Bahía',
        text: 'La checklist semanal del manager es mi herramienta favorita. Controlo inventarios, reuniones con proveedores, revisión de costes y formación del equipo en un solo documento. Gestionar 4 outlets de F&B nunca fue tan organizado.',
        avatar: '/avatars/avatar-1.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€49',
    price: '€14',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €35 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas',
    label: '¿Ya compraste el Kit de Tareas? Vuelve a entrar al dashboard',
  },
};

export default data;
