// astro-site/src/data/productos/tareas/kit-tareas-asador.ts
// PRODUCTO DE REFERENCIA de la Línea Tareas. Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasAsador.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-asador/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-asador.ts  (marquee de testimonios)
// NO parafrasear. Al replicar otros productos, copiar el string exacto de su equivalente.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-asador',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_ASADOR',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper — Checklists Operativos | AI Chef Pro',
    description:
      '11 checklists operativos para asador y parrilla con horno Josper: encendido brasas, protocolo Josper, maduración y despiece de carne, temperaturas por corte, pescados y verduras a la brasa. Solo €14.',
    keywords:
      'checklist asador, tareas asador, protocolo Josper, horno Josper restaurante, maduración dry-age, despiece carne, temperaturas corte chuletón, parrilla profesional, steakhouse operativa, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-asador.jpg',
  },

  schema: {
    productName:
      'Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper — Checklists Operativos',
    productDescription:
      '11 checklists operativos pre-rellenados para asador y parrilla con horno Josper: encendido y mantenimiento de brasas, maduración dry-age y despiece, temperaturas por corte, pescados y verduras a la brasa, eventos y temporadas.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Los checklists del Josper son muy completos. Encendido, zonas de calor, regulación de compuertas, gestión del carbón… todo el equipo sigue el mismo protocolo.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El control de maduración y temperaturas por corte ha elevado la calidad de nuestras carnes. Los clientes lo notan.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Implementamos en 3 asadores. La consistencia en puntos de cocción y presentación es ahora uniforme en todos.',
      },
    ],
    faqs: [
      {
        q: '¿Incluye el protocolo del horno Josper?',
        a: 'Sí. Encendido, precalentamiento, zonas de calor, tipos de carbón, regulación de compuertas, mantenimiento semanal y limpieza profunda anual.',
      },
      {
        q: '¿Sirve para mi tipo de asador?',
        a: 'Sí. Cubre asador tradicional, steakhouse, parrilla argentina, gastrobar con Josper y cualquier local con cocina a las brasas. 100% editable.',
      },
      {
        q: '¿Incluye control de maduración de carne?',
        a: 'Sí. Fichas dry-age y wet-age, control de piezas por peso y fecha, temperaturas de cámara y cálculo de mermas reales.',
      },
      {
        q: '¿Qué cortes y puntos de cocción incluye?',
        a: 'Chuletón, entrecot, tomahawk, costillar, hamburguesa. Con temperaturas internas para blue, rare, medium rare, medium, medium well y well done.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Asador / Parrilla y Horno Josper',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-asador-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-asador-parrilla.jpg',
      '/lovable-uploads/ai-gallery/tareas-asador-josper.jpg',
      '/lovable-uploads/ai-gallery/tareas-asador-maduracion.jpg',
      '/lovable-uploads/ai-gallery/tareas-asador-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-asador-emplatado.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-asador-parrilla.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-asador-emplatado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-asador-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €14 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Asador / Parrilla y Horno Josper',
    description:
      '11 checklists Excel pre-rellenados para asador, steakhouse y parrilla con horno Josper: encendido y zonas de calor, maduración dry-age y despiece, temperaturas por corte, pescados y verduras a la brasa, eventos y temporadas. Imprime, delega y firma.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Protocolo del horno Josper: encendido, zonas de calor, regulación de carbón',
      'Maduración dry-age y despiece profesional con fichas por pieza',
      'Temperaturas de cocción por corte y punto (blue, rare, medium, well done)',
      'Tareas por perfil: parrillero, ayudante, cocina, sala',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  stickyLabel: 'KIT TAREAS ASADOR — €14',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Asador',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de un asador profesional con horno Josper. Solo ajusta a tu carta, imprime y empieza a operar con estándar profesional.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre Asador',
        desc: 'Checklists de encendido del Josper, parrilla abierta, cocina caliente y sala: brasas, carne expuesta, control de temperaturas, cierre completo y arqueo.',
      },
      {
        icon: 'Flame',
        title: 'Horno Josper y Brasas',
        desc: 'Protocolo Josper completo: encendido, precalentamiento, zonas de calor, tipos de carbón (encina, quebracho), regulación de compuertas y mantenimiento por turno.',
      },
      {
        icon: 'Beef',
        title: 'Maduración y Despiece de Carne',
        desc: 'Fichas dry-age y wet-age, control de piezas por peso y fecha, temperaturas de cámara (≤4 ºC), cálculo de mermas reales y temperaturas internas por punto de cocción.',
      },
      {
        icon: 'Fish',
        title: 'Parrilla Pescados y Verduras',
        desc: 'Técnicas para pescados (lubina, rodaballo, dorada) y verduras de temporada (espárragos, alcachofas, calçots) con tiempos por pieza y zonas de la parrilla.',
      },
      {
        icon: 'Briefcase',
        title: 'Tareas del Manager',
        desc: 'Pedidos de carne, control de stock de carbón, gestión del equipo, reservas para grupos grandes, revenue diario, comparativa de proveedores y reporting.',
      },
      {
        icon: 'Users',
        title: 'Perfiles: Parrillero y Equipo',
        desc: 'Tareas claras por perfil: parrillero/asador, ayudante de parrilla, cocina caliente, sala y servicio. Roles y responsabilidades sin solapes.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda del Josper, cuchillería de trinchado y deshuesado, control de stock de carbón y carne, formación del equipo y revisión de proveedores.',
      },
      {
        icon: 'CalendarDays',
        title: 'Eventos y Temporadas',
        desc: 'Calçotada, chuletón para grupos, Nochevieja, San Valentín, temporadas de caza (octubre-febrero) y carnes de temporada con piezas especiales.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para que crees checklists a medida del concepto exacto de tu asador (steakhouse, parrilla argentina, gastrobar con Josper).',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing de Servicio',
        desc: 'Briefing pre-servicio de 5 minutos: carnes del día, piezas especiales (chuletón maduro, tomahawk), grupos, stock de carbón y avisos para parrilla y sala.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con temporadas de carne y caza, festivos, mantenimientos del Josper, formación del equipo y cierres por vacaciones.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010 y experiencia en parrilla, asador y cocina al carbón.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñados para Asador',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de un asador con horno Josper: brasas, maduración, despiece, parrilla abierta a sala.',
      },
      {
        icon: 'Flame',
        title: 'Protocolo Josper Profesional',
        desc: 'Encendido, precalentamiento, zonas de calor, tipos de carbón (encina/quebracho), regulación de compuertas y mantenimiento por turno. Lo que el software premium cobra por suscripción.',
      },
      {
        icon: 'Thermometer',
        title: 'Temperaturas por Corte',
        desc: 'Fichas de cocción interna por pieza (chuletón, entrecot, tomahawk, costillar) con todos los puntos: blue, rare, medium rare, medium, medium well, well done. Cero improvisación.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €14',
        desc: 'Las mismas listas de tareas que usan asadores con software premium, pero en Excel por un pago único. Sin suscripción, sin tablets, ilimitado en clientes.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a asadores, steakhouses y parrillas con horno Josper en la profesionalización de su operativa: maduración de carnes, despiece, gestión de brasas y temperaturas por corte.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de los 9 checklists principales, recibirás estos recursos adicionales — valorados en €34',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing de Servicio',
        value: '€15',
        desc: 'Briefing pre-servicio de 5 minutos: carnes del día por proveedor, piezas especiales (chuletón maduro, tomahawk), grupos y VIPs, stock de carbón y avisos para parrilla y sala. La hoja que alinea al equipo cada turno.',
        image: '/lovable-uploads/ai-gallery/tareas-asador-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: '12 meses con temporadas de carne y caza (octubre-febrero), calçotada, festivos navideños, mantenimientos del Josper y cuchillería de trinchado, formación del equipo y cierres por vacaciones.',
        image: '/lovable-uploads/ai-gallery/tareas-asador-josper.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS ASADOR — €14',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu asador y dominar el horno Josper, las brasas y la maduración, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Incluye el protocolo del horno Josper?',
      a: 'Sí. Encendido, precalentamiento, zonas de calor, tipos de carbón (encina, quebracho), regulación de compuertas, mantenimiento semanal y limpieza profunda anual. Todo el ciclo del Josper documentado por turno.',
    },
    {
      q: '¿Sirve para mi tipo de asador?',
      a: 'Sí. Cubre asador tradicional, steakhouse, parrilla argentina, gastrobar con Josper y cualquier local con cocina a las brasas. Todo es 100% editable para adaptar a tu carta y formato.',
    },
    {
      q: '¿Incluye control de maduración de carne?',
      a: 'Sí. Fichas de dry-age y wet-age, control de piezas por peso y fecha, temperaturas de cámara (≤4 ºC), humedad y ventilación, más cálculo de mermas reales por pieza. Todo lo necesario para auditar y vender carne premium.',
    },
    {
      q: '¿Qué cortes y puntos de cocción incluye?',
      a: 'Chuletón, entrecot, tomahawk, costillar, solomillo, hamburguesa premium. Con temperaturas internas para blue (45 ºC), rare (50 ºC), medium rare (55 ºC), medium (60 ºC), medium well (65 ºC) y well done (70 ºC).',
    },
    {
      q: '¿Funcionan en Google Sheets y otros programas?',
      a: 'Sí. Los archivos son .xlsx estándar. Compatibles con Microsoft Excel, Google Sheets, LibreOffice Calc, Apple Numbers e imprimibles directamente en A4 si prefieres trabajar en papel.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas y sin complicaciones.',
    },
  ],

  cta: {
    heading: 'Tu Asador a Estándar Profesional — En 11 Checklists',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu asador: Josper, brasas, maduración, despiece, perfiles. Por menos de lo que cuesta un chuletón premium.',
    items: [
      'Apertura y cierre completo de Josper, parrilla, cocina y sala',
      'Protocolo del horno Josper: encendido, zonas de calor, regulación',
      'Maduración dry-age, despiece y temperaturas internas por punto',
      'Parrilla de pescados (lubina, rodaballo) y verduras de temporada',
      'Tareas por perfil: parrillero, ayudante, cocina caliente, sala',
      'Calendario anual de carne, caza, calçotada y eventos navideños',
      'BONUS: Briefing de Servicio (€15)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS ASADOR — €14',
  },

  testimonials: {
    subtitle:
      'Parrilleros, propietarios de asador y consultores que ya tienen su operativa bajo control',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Parrillero, Asador Madrid',
        text: 'Los checklists del Josper son muy completos. Encendido, zonas de calor, regulación de compuertas, gestión del carbón… todo el equipo sigue el mismo protocolo y ya no hay mermas por descontrol.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Propietaria Asador, Bilbao',
        text: 'El control de maduración dry-age con fichas por pieza, fecha y peso, más las temperaturas de cocción por corte, ha elevado la calidad de nuestras carnes. Los clientes lo notan en cada chuletón.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director Cadena de Asadores (3 locales)',
        text: 'Implementamos en los 3 asadores. La consistencia en puntos de cocción y presentación es ahora uniforme. Un cliente recibe el mismo entrecot esté donde esté.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Jefa de Sala Steakhouse, Madrid',
        text: 'Las tareas del parrillero están muy bien definidas y el briefing pre-servicio con las carnes del día y las piezas especiales es genial para alinear sala y cocina en 5 minutos.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Consultor Hostelero especializado en asadores',
        text: 'Para asadores y steakhouse es el kit más completo del mercado. Josper, maduración, cortes, carbón, perfiles, temporadas… cubre todos los puntos críticos donde los locales suelen fallar.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Encargada Parrilla Gastrobar, Barcelona',
        text: 'El calendario con temporadas de caza, calçotada y eventos navideños nos permite planificar grupos y carta especial con antelación. Ya no improvisamos las piezas grandes.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Ayudante de Parrilla en formación',
        text: 'Las tareas del ayudante están muy claras: carbón, cenizas, guarniciones, tablas, mise en place. Sé exactamente qué preparar sin que el parrillero tenga que estar detrás de mí.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Chef Ejecutivo Steakhouse, Marbella',
        text: 'El protocolo del Josper y las fichas de maduración son detalles que marcan la diferencia profesional. Lo hemos integrado en nuestro APPCC y ha pasado de "improvisado" a "auditable".',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€69',
    price: '€14',
    discountBadge: '-80%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 80% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €55 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-tareas-chef-privado', label: 'Kit Tareas Chef Privado' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  alreadyBought: {
    product: 'kit-tareas-asador',
    label: '¿Ya compraste el Kit de Tareas Asador? Vuelve a entrar al dashboard',
  },
};

export default data;
