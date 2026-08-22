// astro-site/src/data/productos/tareas/kit-tareas-panaderia.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasPanaderia.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-panaderia/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-panaderia.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-panaderia',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_PANADERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Panadería / Obrador — Checklists con Masas Madre, Hornos y Turno Madrugada | AI Chef Pro',
    description:
      '11 checklists operativos para panadería y obrador: turno madrugada, masas madre y fermentación, hornos y cocción, expositor, perfiles del equipo, temporadas y calendario anual. Solo €12.',
    keywords:
      'checklist panadería, tareas obrador, masas madre, pre-fermentos poolish biga, hornos panadería, turno madrugada panadería, expositor panadería, calendario anual panadería, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-panaderia.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes: Panadería / Obrador — Checklists Operativos',
    productDescription:
      '11 checklists operativos pre-rellenados para panadería y obrador: turno madrugada, masas madre y pre-fermentos, hornos y cocción, expositor y venta, tareas del manager, perfiles del equipo, semanales y mensuales, eventos y temporadas, plantilla personalizable, briefing de producción diaria y calendario anual.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Los checklists de turno madrugada son imprescindibles. Encendido de hornos, masas del día, fermentaciones… todo el equipo sigue el mismo protocolo desde las 03:00.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El control de masas madre y pre-fermentos nos salvó. Cada refresco, cada poolish y cada biga está documentado con temperaturas y tiempos exactos.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Implementamos en 4 obradores. La consistencia en hornos, fermentaciones y producción es ahora uniforme en todas las tiendas.',
      },
    ],
    faqs: [
      {
        q: '¿Incluye control de masas madre y pre-fermentos?',
        a: 'Sí. Control completo de masa madre natural: refresco, temperatura, hidratación y tiempos de fermentación. También pre-fermentos como poolish, biga y esponja, con registros de actividad y protocolos de recuperación si la masa pierde fuerza.',
      },
      {
        q: '¿Cómo gestiona el turno de madrugada?',
        a: 'Checklist completo desde las 03:00: encendido y precalentamiento de hornos, preparación de masas del día, división y formado, control de fermentación en cámara y a temperatura ambiente, primera hornada y apertura de tienda.',
      },
      {
        q: '¿Cubre diferentes tipos de horno?',
        a: 'Sí. Protocolos para horno de piso (solera refractaria), horno rotativo y horno de convección con vapor. Incluye temperaturas, tiempos de cocción, uso de vapor, grenado y carga óptima para cada tipo de pan y bollería.',
      },
      {
        q: '¿Sirve también para bollería y panes especiales?',
        a: 'Sí. Además del pan básico, cubre bollería fermentada (croissants, brioches, ensaimadas), panes especiales (centeno, espelta, semillas), panes de temporada y productos de pastelería de obrador.',
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
    breadcrumbName: 'Kit de Tareas Recurrentes: Panadería / Obrador',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-fermentacion.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-masa.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
      '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg',
  },

  hero: {
    badge: 'El kit operativo para panaderías y obradores de pan',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Panadería / Obrador',
    description:
      '11 checklists Excel pre-rellenados para panadería y obrador. Turno madrugada, masas madre y fermentación, hornos y cocción, expositor y venta, perfiles del equipo, temporadas y calendario anual. Imprime, delega y produce con estándar artesano profesional.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Turno madrugada: apertura del obrador desde las 03:00',
      'Masas madre, pre-fermentos y control de fermentación',
      'Hornos de piso y rotativo: temperaturas y tiempos',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS PANADERÍA — €12',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Panadería',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de un obrador profesional con turno madrugada, masas madre y pre-fermentos, hornos de piso y rotativo, expositor y venta. Solo ajusta a tu surtido de panes, imprime y empieza a producir con estándar artesano.',
    templates: [
      {
        icon: 'Sunrise',
        title: 'Apertura y Cierre (Turno Madrugada)',
        desc: 'Apertura del obrador desde las 03:00, encendido y precalentamiento de hornos, masas del día, división y formado, primera hornada, apertura de tienda y cierre con limpieza profunda.',
      },
      {
        icon: 'Wheat',
        title: 'Masas Madre y Fermentación',
        desc: 'Refresco de masa madre natural, pre-fermentos como poolish y biga, control de temperatura, hidratación y tiempos. Protocolos para recuperar masas que pierden fuerza.',
      },
      {
        icon: 'Flame',
        title: 'Hornos y Cocción',
        desc: 'Horno de piso (solera refractaria), rotativo y de convección con vapor. Temperaturas, tiempos, grenado, carga óptima y uso del vapor para cada tipo de pan y bollería.',
      },
      {
        icon: 'Store',
        title: 'Expositor y Venta',
        desc: 'Montaje del expositor, rotación de producto, etiquetado obligatorio, atención al cliente, gestión de cola en horas punta y reposición a lo largo del día.',
      },
      {
        icon: 'Users',
        title: 'Tareas del Manager',
        desc: 'Planificación de producción semanal, stock de harinas y materias primas, food cost, pricing por línea, gestión de proveedores y reporting con KPIs del obrador.',
      },
      {
        icon: 'UserCog',
        title: 'Tareas por Perfil',
        desc: 'Maestro panadero, oficial de obrador, ayudante de panadería y dependiente de tienda. Roles claros sin solapes ni huecos en producción ni en línea de venta.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda de hornos, revisión de harinas y materias primas, calibración de básculas y termómetros, auditoría APPCC y mantenimiento preventivo del obrador.',
      },
      {
        icon: 'Gift',
        title: 'Eventos y Temporadas',
        desc: 'Navidad, Reyes, Semana Santa, San Juan y otras campañas con panes especiales y bollería de temporada. Producción estacional planificada con margen y stock controlado.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu panadería u obrador (panes especiales, sin gluten, ecológicos, bollería, salados…).',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Briefing Producción Diaria',
        desc: 'Briefing de producción del día: cantidades por línea, masas activas, hornadas planificadas, equipo asignado y avisos clave para arrancar la jornada sin sorpresas.',
      },
      {
        icon: 'CalendarDays',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con producción por mes, panes de temporada, mantenimiento programado de hornos y maquinaria, y acciones de marketing por estación.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010 y experiencia asesorando panaderías artesanas, obradores y cadenas de panificación.',
    reasons: [
      {
        icon: 'Sunrise',
        title: 'Pensados para Turno Madrugada',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de un obrador desde las 03:00: apertura, encendido de hornos, masas del día y primera hornada antes de abrir la tienda.',
      },
      {
        icon: 'Wheat',
        title: 'Masas Madre y Pre-Fermentos',
        desc: 'Refresco de masa madre, poolish, biga y esponja con control de temperatura, hidratación y tiempos. Protocolos para recuperar masas que pierden fuerza y mantener la consistencia día tras día.',
      },
      {
        icon: 'Flame',
        title: 'Hornos y Cocción al Detalle',
        desc: 'Horno de piso, rotativo y convección con vapor. Temperaturas, tiempos, grenado, carga óptima y uso del vapor para cada tipo de pan y bollería. Sin hornadas perdidas por errores operativos.',
      },
      {
        icon: 'RefreshCw',
        title: 'Operativo Todo el Año',
        desc: 'Calendario con Navidad, Reyes, Semana Santa, San Juan y otras campañas. Stock de harinas, panes de temporada y mantenimiento preventivo de hornos planificados por mes y estación.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a panaderías artesanas, obradores y cadenas de panificación en la profesionalización de su operativa: turno madrugada, masas madre y pre-fermentos, gestión de hornos y campañas estacionales como Navidad, Reyes y Semana Santa.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de los 9 checklists principales, recibirás estos recursos adicionales — valorados en €38',
    items: [
      {
        icon: 'Calendar',
        label: 'BONUS 1',
        title: 'Briefing Producción Diaria',
        value: '€19',
        desc: 'Briefing de producción del día: cantidades por línea de pan y bollería, masas activas y pre-fermentos, hornadas planificadas, equipo asignado y avisos clave para arrancar la jornada sin sorpresas.',
        image: '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
      },
      {
        icon: 'CalendarDays',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: 'Planificación anual con producción por mes, panes de temporada (Navidad, Reyes, Semana Santa), mantenimiento programado de hornos y maquinaria, y acciones de marketing por estación. Año completo bajo control.',
        image: '/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS PANADERÍA — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu panadería u obrador y dominar el turno madrugada, las masas madre, los hornos y la producción diaria, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Incluye control de masas madre y pre-fermentos?',
      a: 'Sí. Control completo de masa madre natural: refresco, temperatura, hidratación y tiempos de fermentación. También pre-fermentos como poolish, biga y esponja con registros de actividad y protocolos de recuperación si la masa pierde fuerza.',
    },
    {
      q: '¿Cómo gestiona el turno de madrugada?',
      a: 'Checklist completo desde las 03:00: encendido y precalentamiento de hornos, preparación de masas del día, división y formado, control de fermentación en cámara y a temperatura ambiente, primera hornada y apertura de tienda. Todo paso a paso.',
    },
    {
      q: '¿Cubre diferentes tipos de horno?',
      a: 'Sí. Protocolos para horno de piso (solera refractaria), horno rotativo y horno de convección con vapor. Incluye temperaturas, tiempos de cocción, uso de vapor, grenado y carga óptima para cada tipo de pan y bollería.',
    },
    {
      q: '¿Sirve también para bollería y panes especiales?',
      a: 'Sí. Además del pan básico, cubre bollería fermentada (croissants, brioches, ensaimadas), panes especiales (centeno, espelta, semillas), panes de temporada y productos de pastelería de obrador. Cada categoría con sus tiempos y temperaturas.',
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
    heading: 'Es Hora de Organizar la Producción de tu Panadería',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu panadería u obrador: turno madrugada, masas madre, hornos, expositor, perfiles del equipo y campañas estacionales. No dejes pasar esta oportunidad.',
    items: [
      '9 checklists operativos + 2 bonus',
      'Apertura desde las 03:00 con turno madrugada bajo control',
      'Masas madre, pre-fermentos (poolish, biga) y fermentación',
      'Hornos de piso, rotativo y convección con vapor',
      'Expositor, venta y atención al cliente en horas punta',
      'Tareas por perfil: maestro, oficial, ayudante, dependiente',
      'BONUS: Briefing Producción Diaria (€19)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS PANADERÍA — €12',
  },

  testimonials: {
    subtitle:
      'Maestros panaderos, oficiales de obrador y consultores de panificación que ya tienen su producción bajo control',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Maestro Panadero Madrid',
        text: 'Los checklists de turno madrugada son imprescindibles. Encendido de hornos, masas del día, fermentaciones… todo el equipo sigue el mismo protocolo desde las 03:00 y entramos a producir sin caos.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Propietaria Obrador Barcelona',
        text: 'El control de masas madre y pre-fermentos nos salvó. Ahora cada refresco, cada poolish y cada biga está documentado con temperaturas y tiempos exactos. Cero hornadas perdidas.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director Cadena Panaderías (4 obradores)',
        text: 'Implementamos en 4 obradores. La consistencia en hornos, fermentaciones y producción es ahora uniforme en todas las tiendas. Mismo pan en cada punto de venta.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Encargada Panadería Artesana',
        text: 'Las tareas por perfil clarifican quién hace qué: maestro, oficial, ayudante, dependiente. El briefing de producción diaria nos ahorra tiempo y errores en cada hornada.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Consultor Panificación',
        text: 'Para panaderías y obradores es el kit más completo del mercado. Masas madre, hornos, expositor, turno madrugada… todo cubierto sin huecos operativos.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Oficial de Obrador',
        text: 'El control de hornos y cocción está muy bien detallado. Horno de piso, rotativo, vapor, tiempos, temperaturas… sé exactamente qué hacer en cada hornada y cada tipo de pan.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Responsable Producción Panadería',
        text: 'Las tareas semanales y mensuales de limpieza de hornos, revisión de harinas y calibración de básculas nos mantienen siempre a punto para cualquier inspección sanitaria.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Maestro Panadero Obrador Premium',
        text: 'El calendario anual con panes de temporada y campañas especiales nos ayuda a planificar Navidad, Reyes, Semana Santa y toda la producción estacional sin sorpresas.',
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
    { href: '/kit-tareas-pasteleria', label: 'Kit Tareas Pastelería' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-panaderia',
    label: '¿Ya compraste el Kit de Tareas Panadería? Vuelve a entrar al dashboard',
  },
};

export default data;
