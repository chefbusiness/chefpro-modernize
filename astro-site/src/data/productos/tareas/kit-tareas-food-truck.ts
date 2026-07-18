// astro-site/src/data/productos/tareas/kit-tareas-food-truck.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasFoodTruck.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-food-truck/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-food-truck.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-food-truck',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_FOOD_TRUCK',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Food Truck — Checklists Operativos con Setup, APPCC Móvil y Permisos | AI Chef Pro',
    description:
      '11 checklists operativos para food truck: setup y teardown, operaciones móviles, APPCC seguridad alimentaria móvil, permisos y eventos, perfiles, temporadas y calendario anual. Solo €12.',
    keywords:
      'checklist food truck, tareas cocina móvil, setup teardown food truck, APPCC móvil, permisos food truck, eventos food truck, generador food truck, calendario anual food truck, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-food-truck.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes: Food Truck — Checklists Operativos',
    productDescription:
      '11 checklists operativos pre-rellenados para food truck: setup y teardown, operaciones móviles y vehículo, APPCC seguridad alimentaria móvil, permisos y licencias, gestión de eventos, perfiles y calendario anual.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Los checklists de setup y teardown son imprescindibles. Montaje del generador, gas, cocina… todo el equipo sigue el mismo protocolo en cada evento.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El APPCC móvil nos salvó en la última inspección. Temperaturas, cadena de frío, documentación… todo al día y listo para mostrar.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Implementamos en 3 trucks. La consistencia en operaciones móviles y el control del vehículo es ahora uniforme en toda la flota.',
      },
    ],
    faqs: [
      {
        q: '¿Incluye gestión de permisos y licencias?',
        a: 'Sí. Control completo de permisos municipales, licencias de actividad, seguros de responsabilidad civil, certificados de manipulador y documentación sanitaria, con checklist pre-evento para verificar que toda la documentación está en regla antes de cada localización.',
      },
      {
        q: '¿Cómo funciona el APPCC móvil?',
        a: 'Adaptado específicamente para cocinas móviles: control de temperaturas en condiciones variables, cadena de frío durante transporte, manipulación de alimentos en espacios reducidos, gestión de alérgenos y toda la documentación que exige sanidad para food trucks.',
      },
      {
        q: '¿Cubre el mantenimiento del generador?',
        a: 'Sí. Checklist completo de generador: nivel de combustible, aceite, arranque, potencia, conexiones eléctricas, mantenimiento preventivo y protocolo de emergencia, tanto en tareas diarias como en revisiones semanales y mensuales.',
      },
      {
        q: '¿Sirve para diferentes tipos de evento?',
        a: 'Sí. Cubre festivales de música, bodas, eventos corporativos, mercados gastronómicos, ferias, fiestas patronales y eventos privados. Cada tipo tiene sus particularidades en logística, menú, stock y equipo necesario.',
      },
      {
        q: '¿Funcionan en Google Sheets?',
        a: 'Sí. Compatibles con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días. Si no estás satisfecho, devolución 100% sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Food Truck',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-line.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-prep.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg',
      '/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-food-truck-counter.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-food-truck-hero.jpg',
  },

  hero: {
    badge: 'El kit operativo para food trucks y cocinas móviles',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Food Truck',
    description:
      '11 checklists Excel pre-rellenados para food truck. Setup y teardown, operaciones móviles, APPCC seguridad alimentaria móvil, permisos y licencias, gestión de eventos, perfiles y calendario anual. Imprime, delega y opera con estándar profesional.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Setup y teardown completo (montaje y desmontaje)',
      'APPCC seguridad alimentaria móvil obligatorio',
      'Permisos, licencias y gestión de eventos',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS FOOD TRUCK — €12',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Food Truck',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de un food truck profesional con setup y teardown, operaciones móviles, APPCC móvil, permisos y gestión de eventos. Solo ajusta a tu carta y ruta, imprime y empieza a operar con estándar profesional.',
    templates: [
      {
        icon: 'Truck',
        title: 'Setup y Teardown',
        desc: 'Montaje y desmontaje completos: generador, gas, agua, cocina, vitrina, puesto de servicio, caja y cierre del vehículo. Llegar, montar, vender y recoger sin huecos.',
      },
      {
        icon: 'Wrench',
        title: 'Operaciones Móviles y Vehículo',
        desc: 'Vehículo, generador, gestión de energía, gas, agua potable, aguas grises y residuos. Lo que mantiene el truck operativo todo el día sin sustos eléctricos ni sanitarios.',
      },
      {
        icon: 'ShieldCheck',
        title: 'APPCC Seguridad Alimentaria Móvil',
        desc: 'Temperaturas, cadena de frío durante transporte, manipulación en espacios reducidos, alérgenos y documentación sanitaria que exige el control oficial a una cocina móvil.',
      },
      {
        icon: 'MapPin',
        title: 'Permisos, Eventos y Localizaciones',
        desc: 'Licencias municipales, seguros de responsabilidad civil, certificados de manipulador, briefing pre-evento y tipos de evento (festivales, bodas, mercados, corporativos).',
      },
      {
        icon: 'Users',
        title: 'Tareas del Manager',
        desc: 'Planificación de rutas y eventos, stock, food cost, pricing por evento, RRSS, reservas privadas y reporting semanal con KPIs operativos del truck.',
      },
      {
        icon: 'UserCog',
        title: 'Tareas por Perfil',
        desc: 'Tareas claras por perfil: chef de food truck, ayudante de cocina, cajero/servicio y conductor/técnico. Roles y responsabilidades sin solapes ni huecos.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda del truck, mantenimiento del generador, ITV y revisiones del vehículo, auditoría APPCC móvil y revisión de permisos vigentes por localización.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Temporadas',
        desc: 'Temporada alta y baja, festivales de música, bodas, eventos corporativos, mercados gastronómicos y rutas urbanas. Stock y carta dinámicos todo el año.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu food truck (tacos, hamburguesas, fusión, dulce, café, etc.).',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Briefing Pre-Evento',
        desc: 'Briefing pre-evento de 5 minutos: tipo de evento, logística de localización, menú y stock necesario, asignación de equipo y avisos clave para el día.',
      },
      {
        icon: 'CalendarDays',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con eventos por mes, menú sugerido por temporada, mantenimiento del vehículo y generador, y acciones de marketing por estación.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un profesional con 29 años en alta hostelería y experiencia asesorando food trucks, street food y cocinas móviles de eventos.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñados para Food Truck',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de un food truck o cocina móvil: setup, teardown, vehículo, generador, gas y servicio en línea.',
      },
      {
        icon: 'ShieldCheck',
        title: 'APPCC Seguridad Móvil',
        desc: 'Temperaturas en condiciones variables, cadena de frío durante transporte, manipulación en espacios reducidos, alérgenos y documentación sanitaria que exige el control oficial a una cocina móvil.',
      },
      {
        icon: 'MapPin',
        title: 'Permisos y Gestión de Eventos',
        desc: 'Licencias municipales, seguros, certificados, briefing pre-evento y verificación de documentación por localización. Lo que evita multas y cierres en plena facturación.',
      },
      {
        icon: 'RefreshCw',
        title: 'Operativo Todo el Año',
        desc: 'Calendario con festivales, bodas, mercados gastronómicos y eventos corporativos. Stock, menú y mantenimiento del vehículo planificados por temporada.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha asesorado a food trucks, operadores de street food y cocinas móviles de eventos en la profesionalización de su operativa: setup y teardown, APPCC móvil, gestión de permisos por evento y calendario anual de eventos y temporadas.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de los 9 checklists principales, recibirás estos recursos adicionales — valorados en €38',
    items: [
      {
        icon: 'Calendar',
        label: 'BONUS 1',
        title: 'Briefing Pre-Evento',
        value: '€19',
        desc: 'Briefing pre-evento con tipo de evento, logística de localización (acceso, electricidad, agua), menú y stock necesario, asignación de equipo y avisos clave para que el día del evento todo salga sin sorpresas.',
        image: '/lovable-uploads/ai-gallery/use-case-food-truck-team.jpg',
      },
      {
        icon: 'CalendarDays',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: 'Planificación anual con eventos por mes, menú sugerido por temporada, mantenimiento programado del vehículo y generador, y acciones de marketing por estación. Año completo bajo control.',
        image: '/lovable-uploads/ai-gallery/use-case-food-truck-grill.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS FOOD TRUCK — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu food truck y dominar el setup, el APPCC móvil, los permisos por evento y las operaciones del vehículo, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Incluye gestión de permisos y licencias?',
      a: 'Sí. Control completo de permisos municipales, licencias de actividad, seguros de responsabilidad civil, certificados de manipulador y documentación sanitaria. Con checklist pre-evento para verificar que toda la documentación está en regla antes de cada localización.',
    },
    {
      q: '¿Cómo funciona el APPCC móvil?',
      a: 'Adaptado específicamente para cocinas móviles: control de temperaturas en condiciones variables, cadena de frío durante transporte, manipulación de alimentos en espacios reducidos, gestión de alérgenos y toda la documentación que exige sanidad para food trucks.',
    },
    {
      q: '¿Cubre el mantenimiento del generador?',
      a: 'Sí. Checklist completo de generador: nivel de combustible, aceite, arranque, potencia, conexiones eléctricas, mantenimiento preventivo y protocolo de emergencia. Tanto en tareas diarias como en revisiones semanales y mensuales.',
    },
    {
      q: '¿Sirve para diferentes tipos de evento?',
      a: 'Sí. Cubre festivales de música, bodas, eventos corporativos, mercados gastronómicos, ferias, fiestas patronales y eventos privados. Cada tipo tiene sus particularidades en logística, menú, stock y equipo necesario, y aquí está todo previsto.',
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
    heading: 'Es Hora de Organizar las Operaciones de tu Food Truck',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu food truck o cocina móvil: setup, teardown, vehículo, APPCC móvil, permisos, eventos y perfiles. No dejes pasar esta oportunidad.',
    items: [
      '9 checklists operativos + 2 bonus',
      'Setup y teardown completos del food truck',
      'Operaciones móviles, vehículo, generador, gas y agua',
      'APPCC seguridad alimentaria móvil obligatorio',
      'Permisos, licencias y gestión por evento',
      'Tareas por perfil: chef, ayudante, cajero, conductor',
      'BONUS: Briefing Pre-Evento (€19)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS FOOD TRUCK — €12',
  },

  testimonials: {
    subtitle:
      'Operadores de food trucks, chefs de cocina móvil y consultores de street food que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Propietario Food Truck Madrid',
        text: 'Los checklists de setup y teardown son imprescindibles. Montaje del generador, gas, cocina… todo el equipo sigue el mismo protocolo en cada evento y montamos en la mitad de tiempo.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Chef Food Truck Barcelona',
        text: 'El APPCC móvil nos salvó en la última inspección. Temperaturas, cadena de frío, documentación… todo al día y listo para mostrar. Cero estrés en eventos grandes.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director Flota Food Trucks (3 trucks)',
        text: 'Implementamos en 3 trucks. La consistencia en operaciones móviles y el control del vehículo y generador es ahora uniforme en toda la flota. Cero descoordinación.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Encargada Food Truck Gourmet',
        text: 'Las tareas por perfil clarifican quién hace qué: chef, ayudante, cajero, conductor. El briefing pre-evento nos ahorra tiempo y errores en cada localización nueva.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Consultor Street Food',
        text: 'Para food trucks es el kit más completo del mercado. Setup, teardown, APPCC móvil, permisos, eventos… cubre todos los puntos críticos sin huecos.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Operadora Food Truck Eventos',
        text: 'El control de permisos y licencias por evento nos evita problemas legales. Cada localización tiene sus requisitos y aquí está todo previsto antes de salir.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Técnico Food Truck',
        text: 'Las tareas de vehículo y generador están muy bien detalladas. Mantenimiento, energía, gas, agua… sé exactamente qué revisar antes de cada salida.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Chef Ejecutivo Street Food Premium',
        text: 'El calendario anual con eventos por temporada y el menú sugerido nos ayudan a planificar festivales, bodas y mercados gastronómicos todo el año sin huecos.',
        avatar: '/avatars/avatar-8.jpg',
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
    { href: '/kit-tareas-bar', label: 'Kit Tareas Bar / Cocktails' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  alreadyBought: {
    product: 'kit-tareas-food-truck',
    label: '¿Ya compraste el Kit de Tareas Food Truck? Vuelve a entrar al dashboard',
  },
};

export default data;
