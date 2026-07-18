// astro-site/src/data/productos/tareas/kit-tareas-marisqueria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasMarisqueria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-marisqueria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-marisqueria.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-marisqueria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_MARISQUERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC — Checklists Operativos | AI Chef Pro',
    description:
      '11 checklists operativos para marisquería y restaurante de pescado: control del vivero (oxígeno, salinidad, temperatura), expositor de hielo, trazabilidad APPCC, alérgenos de crustáceos y moluscos, lonjas y temporadas de pesca de España. Solo €14.',
    keywords:
      'checklist marisquería, tareas marisquería, control vivero marisco, trazabilidad APPCC pescado, alérgenos crustáceos moluscos, expositor hielo marisco, temporadas pesca España, vedas marisco, restaurante de pescado, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-marisqueria.jpg',
  },

  schema: {
    productName:
      'Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC — Checklists Operativos',
    productDescription:
      '11 checklists operativos pre-rellenados para marisquería y restaurante de pescado: control del vivero, expositor de hielo, trazabilidad APPCC, alérgenos de crustáceos y moluscos, lonjas y temporadas de pesca de España.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Los checklists del vivero son muy completos. Temperatura, oxígeno, salinidad… todo el equipo sigue el mismo estándar cada mañana.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'La trazabilidad APPCC con registro de lotes y alérgenos nos ha salvado en dos inspecciones de Sanidad. Imprescindible.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Implementamos en 3 marisquerías. La consistencia en el control del expositor y la rotación FIFO es ahora uniforme.',
      },
    ],
    faqs: [
      {
        q: '¿Incluye el control completo del vivero?',
        a: 'Sí. Temperatura del agua, oxígeno disuelto, salinidad, pH, densidad de carga, limpieza de filtros y control de mortalidad, con frecuencias y valores de referencia por especie.',
      },
      {
        q: '¿Sirve para mi tipo de marisquería?',
        a: 'Sí. Cubre marisquería gallega tradicional, restaurante de pescado y marisco, marisquería con barra, locales con vivero propio y restaurantes costeros. 100% editable.',
      },
      {
        q: '¿Cubre la trazabilidad obligatoria del marisco?',
        a: 'Sí. Cumple con el Reglamento UE 1379/2013. Incluye registro de lotes, etiquetado obligatorio, zona FAO, método de captura y alérgenos de crustáceos y moluscos.',
      },
      {
        q: '¿Las temporadas de pesca son de España?',
        a: 'Sí. Atlántico y Mediterráneo español: percebes, nécoras, centollos, gamba roja, langostinos, cigalas, bogavantes y mejillones, con calendario de vedas actualizado.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-vivero.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-expositor.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-mariscos.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-marisqueria-emplatado.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-marisqueria-vivero.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-marisqueria-emplatado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €14 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Marisquería con Vivero y APPCC',
    description:
      '11 checklists Excel pre-rellenados para marisquería y restaurante de pescado: control del vivero (oxígeno, salinidad, temperatura), expositor de hielo y rotación FIFO, trazabilidad APPCC y alérgenos, lonjas y temporadas de pesca. Imprime, delega y firma.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Vivero, expositor de hielo y control diario de frescura',
      'Trazabilidad APPCC y alérgenos de crustáceos y moluscos (UE 1379/2013)',
      'Temporadas de pesca de España y calendario de vedas',
      'Tareas por perfil: mariscador, partida pescados, partida mariscos, sala',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  stickyLabel: 'KIT TAREAS MARISQUERÍA — €14',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Marisquería',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de una marisquería profesional con vivero, expositor de hielo y trazabilidad APPCC. Solo ajusta a tu carta, imprime y empieza a operar con estándar profesional.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre Marisquería',
        desc: 'Vivero, expositor de hielo, cámaras, mise en place de salsas, montaje de sala con cubertería de marisco y cierre con arqueo, lavado de filtros y temperaturas.',
      },
      {
        icon: 'Droplets',
        title: 'Vivero, Lonjas y Pescado Fresco',
        desc: 'Control diario del vivero (temperatura del agua, oxígeno disuelto, salinidad, pH, densidad), compras en lonja e indicadores de frescura por pieza y especie.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Trazabilidad y APPCC Marisco',
        desc: 'Registro de lotes, etiquetado UE 1379/2013, zona FAO, método de captura, alérgenos de crustáceos y moluscos y puntos críticos HACCP de la cadena del frío.',
      },
      {
        icon: 'Snowflake',
        title: 'Expositor y Barra de Mariscos',
        desc: 'Montaje del expositor de hielo, rotación FIFO, mantenimiento durante el servicio, apertura segura de ostras, navajas y almejas y reposición sin romper la cadena.',
      },
      {
        icon: 'Briefcase',
        title: 'Tareas del Manager',
        desc: 'Pedidos en lonja, gestión de proveedores, food cost por especie, revenue diario, RRHH, administración y reporting semanal de mermas y rotación.',
      },
      {
        icon: 'Users',
        title: 'Perfiles: Mariscador y Equipo',
        desc: 'Tareas claras por perfil: jefe de cocina/mariscador, partida de pescados, partida de mariscos, maître y camarero. Roles y responsabilidades sin solapes.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda del vivero, inventarios, afilado de cuchillería de pescado, auditoría APPCC, evaluación de proveedores y formación del equipo.',
      },
      {
        icon: 'CalendarDays',
        title: 'Eventos y Temporadas',
        desc: 'Temporadas de pesca de España (percebes, gamba roja, centollo, bogavante), Navidad, Nochevieja, San Valentín y vedas oficiales por especie.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para que crees checklists a medida de tu marisquería (gallega, mediterránea, restaurante de pescado, gastrobar de mariscos).',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing de Servicio',
        desc: 'Briefing pre-servicio de 5 minutos: capturas del día, alérgenos activos, reservas VIP, maridajes recomendados y avisos para barra y sala.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con temporadas de pesca por mes, eventos, mantenimientos del vivero, formación del equipo y cierres por vacaciones.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un profesional con 29 años en alta hostelería y experiencia en marisquerías, restaurantes de pescado y barra de mariscos.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñados para Marisquería',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de una marisquería: vivero vivo, expositor de hielo, lonja, trazabilidad y barra de mariscos.',
      },
      {
        icon: 'Droplets',
        title: 'Protocolo Vivero Profesional',
        desc: 'Temperatura del agua, oxígeno disuelto, salinidad, pH, densidad de carga, limpieza de filtros y control de mortalidad. Lo que el software premium cobra por suscripción.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Trazabilidad APPCC Marisco',
        desc: 'Fichas de lotes, etiquetado UE 1379/2013, zona FAO, método de captura y alérgenos de crustáceos y moluscos. Listo para inspección de Sanidad sin sustos.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €14',
        desc: 'Las mismas listas de tareas que usan marisquerías con software premium, pero en Excel por un pago único. Sin suscripción, sin tablets, ilimitado en clientes.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha asesorado a marisquerías, restaurantes de pescado y barras de mariscos en la profesionalización de su operativa: control del vivero, trazabilidad APPCC, expositor de hielo y temporadas de pesca de España.',

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
        desc: 'Briefing pre-servicio de 5 minutos: capturas del día por proveedor y lonja, piezas especiales (gamba roja, percebe, ostra grande), grupos y VIPs, alérgenos activos y avisos para barra y sala. La hoja que alinea al equipo cada turno.',
        image: '/lovable-uploads/ai-gallery/tareas-marisqueria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: '12 meses con temporadas de pesca de España (gamba roja, percebes, centollo, bogavante), vedas oficiales por especie, festivos navideños, mantenimientos del vivero, formación del equipo y cierres por vacaciones.',
        image: '/lovable-uploads/ai-gallery/tareas-marisqueria-expositor.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS MARISQUERÍA — €14',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu marisquería y dominar el vivero, el expositor de hielo y la trazabilidad APPCC, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Incluye el control completo del vivero?',
      a: 'Sí. Temperatura del agua, oxígeno disuelto, salinidad, pH, densidad de carga, limpieza de filtros y control de mortalidad. Frecuencias de medición por turno y valores de referencia para bogavante, centollo, percebe y demás especies vivas.',
    },
    {
      q: '¿Sirve para mi tipo de marisquería?',
      a: 'Sí. Cubre marisquería gallega tradicional, restaurante de pescado y marisco, marisquería con barra, locales con vivero propio y restaurantes costeros. Todo es 100% editable para adaptar a tu carta y formato.',
    },
    {
      q: '¿Cubre la trazabilidad obligatoria del marisco?',
      a: 'Sí. Cumple con el Reglamento UE 1379/2013 de organización común de mercados de productos de la pesca. Incluye registro de lotes, etiquetado obligatorio, zona FAO, método de captura y alérgenos de crustáceos y moluscos.',
    },
    {
      q: '¿Las temporadas de pesca son de España?',
      a: 'Sí. Incluye temporadas de las principales especies del Atlántico y Mediterráneo español: percebes, nécoras, centollos, gamba roja, langostinos, cigalas, bogavantes y mejillones, con calendario de vedas actualizado por mes.',
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
    heading: 'Tu Marisquería a Estándar Profesional — En 11 Checklists',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu marisquería: vivero, expositor, trazabilidad APPCC, lonjas, perfiles. Por menos de lo que cuesta una buena mariscada.',
    items: [
      'Apertura y cierre completo de vivero, expositor, cámaras y sala',
      'Protocolo del vivero: oxígeno, salinidad, temperatura, mortalidad',
      'Trazabilidad APPCC, lotes, zona FAO y alérgenos de crustáceos y moluscos',
      'Expositor de hielo, rotación FIFO y apertura de ostras y navajas',
      'Tareas por perfil: mariscador, partida pescados, partida mariscos, sala',
      'Calendario anual con temporadas de pesca y vedas oficiales',
      'BONUS: Briefing de Servicio (€15)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS MARISQUERÍA — €14',
  },

  testimonials: {
    subtitle:
      'Mariscadores, propietarios de marisquería y consultores que ya tienen su operativa bajo control',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Jefe de Cocina, Marisquería Madrid',
        text: 'Los checklists del vivero son muy completos. Temperatura, oxígeno, salinidad, densidad de carga… todo el equipo sigue el mismo estándar cada mañana y los animales llegan al plato en óptimas condiciones.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Propietaria Marisquería Gallega',
        text: 'La trazabilidad APPCC con registro de lotes, zona FAO y alérgenos de crustáceos y moluscos nos ha salvado en dos inspecciones de Sanidad. Imprescindible para cumplir con el reglamento UE.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director Cadena de Marisquerías (3 locales)',
        text: 'Implementamos en los 3 locales. La consistencia en el control del expositor de hielo, la rotación FIFO y la apertura de ostras es ahora uniforme. Mismo estándar en Vigo, Madrid y Marbella.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Jefa de Sala Marisquería, Madrid',
        text: 'Las tareas por perfil clarifican quién hace qué. El briefing pre-servicio con capturas del día, piezas destacadas y reservas VIP alinea cocina y sala en 5 minutos antes de abrir.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Consultor Hostelero especializado en pescado y marisco',
        text: 'Para marisquerías es el kit más completo del mercado. Vivero, expositor, trazabilidad, lonjas, temporadas de pesca… cubre todos los puntos críticos donde los locales de pescado suelen fallar.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Encargada Restaurante de Pescado, Barcelona',
        text: 'El calendario con temporadas de pesca en España y vedas nos permite planificar la carta y las compras en lonja con antelación. Ya no compramos langostino congelado en pleno temporada de gamba roja.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Mariscador profesional, Galicia',
        text: 'Las tareas de control del vivero están muy claras: oxígeno, salinidad, pH, limpieza de filtros, mortalidad. Sé exactamente qué revisar en cada turno sin tener que ir preguntando al chef.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Chef Ejecutivo Marisquería Premium, Marbella',
        text: 'El control de frescura del pescado y la trazabilidad de lotes son detalles que marcan la diferencia profesional. Lo hemos integrado en nuestro APPCC y ha pasado de "improvisado" a "auditable".',
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
    product: 'kit-tareas-marisqueria',
    label: '¿Ya compraste el Kit de Tareas Marisquería? Vuelve a entrar al dashboard',
  },
};

export default data;
