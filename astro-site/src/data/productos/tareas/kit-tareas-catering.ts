// astro-site/src/data/productos/tareas/kit-tareas-catering.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasCatering.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-catering/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-catering.ts  (marquee de testimonios)
// NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-catering',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_CATERING',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Catering / Eventos | AI Chef Pro',
    description:
      '9 plantillas + 2 bonus (11 ficheros): checklists operativos para catering y eventos con 347 tareas ya escritas — producción off-site, transporte, apertura/cierre de negocio, cobros y facturación por evento, montaje, servicio, desmontaje. Bodas, corporativos, cocktails. Solo €12.',
    keywords:
      'checklist catering, tareas evento, checklist montaje evento, tareas catering bodas, control logística catering, plantilla tareas evento, checklist desmontaje, inventario catering, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-catering.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Catering / Eventos',
    productDescription:
      '9 plantillas + 2 bonus (11 ficheros): checklists operativos para catering y eventos con 347 tareas ya escritas — producción off-site, transporte, apertura y cierre de negocio, cobros y facturación por evento (anticipos, liquidación y saldos), montaje, servicio, desmontaje y post-evento.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Marta Domínguez',
        rating: '5',
        body: 'Los checklists de producción y transporte eliminaron el 90% de los olvidos. El equipo eventual sabe exactamente qué hacer.',
      },
      {
        author: 'Laura Sánchez',
        rating: '5',
        body: 'Hago 3-4 bodas por semana en temporada alta. Los checklists por tipo de evento me ahorran horas de preparación.',
      },
      {
        author: 'Isabel García',
        rating: '5',
        body: 'Recomiendo este kit a todos mis clientes de catering. Cubren el ciclo completo del evento.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para catering?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una empresa de catering profesional. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Cubre todo el ciclo del evento?',
        a: 'Sí. Incluye producción off-site, transporte y logística, montaje del venue, servicio durante el evento, desmontaje y post-evento.',
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
    breadcrumbName: 'Kit de Tareas Recurrentes: Catering / Eventos',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-transporte.jpg',
      '/lovable-uploads/ai-gallery/tareas-catering-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Catering / Eventos — Del Obrador al Venue',
    description:
      '9 plantillas + 2 bonus (11 ficheros) en Excel con 347 tareas de catering y eventos ya escritas: producción off-site, transporte, apertura/cierre de negocio, cobros y facturación por evento, montaje, servicio, desmontaje y post-evento. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Producción off-site: mise en place, elaboraciones, empaquetado',
      'Transporte y logística: cadena de frío, carga, descarga',
      'Apertura/cierre de negocio y cobros por evento: anticipo, liquidación y saldo',
      'Montaje y desmontaje del venue: sala, cocina, barra',
      'Tipos de evento: bodas, corporativos, cocktails, outdoor',
      'Plantilla personalizable + briefing pre-evento',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS CATERING — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas + 2 Bonus (11 ficheros)',
    subtitle:
      '347 tareas de catering y eventos ya escritas y repartidas por fase, zona y perfil. Ajusta a tu operación, imprime y delega.',
    templates: [
      {
        icon: 'ChefHat',
        title: 'Producción Off-Site',
        desc: 'Higiene personal y arranque seguro de la cocina, elaboraciones D-1, cocciones día D, prevención de ANISAKIS en pescado crudo o semicrudo, emplatado previo y empaquetado en GN e isotermos. 38 tareas ya escritas, con tabla de vida útil en congelación al pie.',
      },
      {
        icon: 'Truck',
        title: 'Transporte y Logística',
        desc: 'Carga con certificado ATP del vehículo, cadena de frío, monitorización de temperatura y descarga en venue. Cumple normativa APPCC de transporte.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Event Manager',
        desc: 'Coordinación semana previa, día del evento (pre-servicio, durante, post) y retrospectiva con equipo, con registro de jornada archivado. + hoja Trimestral y Anual: DDD de la cocina central, conductos y extintores, ATP del vehículo, calibración de sondas, gas, aceite usado, carnés de manipulador, póliza de eventos y Verifactu, con nº de parte y firma.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists para: chef de evento, maître, camarero/runner, barman. Cada rol sabe qué hacer antes, durante y después.',
      },
      {
        icon: 'Tent',
        title: 'Montaje y Desmontaje',
        desc: 'Cocina temporal, sala, buffet/estaciones con los alérgenos señalizados, check pre-apertura. Desmontaje: sala, cocina, control de sobrantes con cadena de frío y merma, carga y salida.',
      },
      {
        icon: 'PartyPopper',
        title: 'Tipos de Evento',
        desc: 'Bodas con alérgenos e intolerancias en el plano de asientos, corporativos con restricciones por escrito, cocktail/standing con prevención de ANISAKIS en las estaciones de ceviche y tartar, y outdoor con la regla horaria de temperatura ambiente. Checklists específicos para cada formato.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas maestras ya estructuradas —por fase, por zona y por perfil— con las secciones y la columna de cada eje ya puestas: tú solo escribes tus tareas en las celdas verdes. Sin contador: están en blanco para que las completes tú.',
      },
      {
        icon: 'Building2',
        title: 'Apertura y Cierre de Negocio',
        desc: 'Checklist del obrador y la base de operaciones completa (no solo cocina): órdenes de servicio del día, hoja de ruta de cada vehículo, carga de isotermos con temperatura de salida, material y accesos de cada recinto. Responsable y hora precargados en 33 tareas.',
      },
      {
        icon: 'Wallet',
        title: 'Cobros y Facturación por Evento',
        desc: 'El dinero de cada evento, no un cajón de mostrador: checklist de lo que hay que cerrar antes (presupuesto firmado, anticipo del 30-50 % cobrado, datos de facturación) y después (comensales reales, extras, factura, saldo). Liquidación con IVA 10/21 %, total, saldo tras anticipo y PENDIENTE DE COBRO en ámbar, con ESTADO automático que pasa a VENCIDO al llegar la fecha. Registro de 25 eventos con totales y recuento de vencidos.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Pre-Evento',
        desc: 'Plantilla de briefing 30 min antes de puertas: evento, menú, alérgenos, equipo, VIPs y protocolo.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '22 fechas clave para catering: bodas, corporativos, Navidad, comuniones, Día del Padre y el puente de diciembre. Con antelación recomendada.',
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
        title: 'Pre-Rellenadas para Catering',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de una empresa de catering profesional. Solo ajusta, borra lo que no aplique y añade lo específico.',
      },
      {
        icon: 'Truck',
        title: 'Del Obrador al Venue',
        desc: 'Cubre toda la cadena: producción, transporte, montaje, servicio y desmontaje. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Perfiles de Evento',
        desc: 'Checklists para chef de evento, maître, camarero, barman. Cada miembro sabe exactamente qué hacer en cada fase.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan empresas de catering con SaaS premium, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha coordinado cientos de caterings y eventos, desde bodas íntimas hasta convenciones de +500 comensales.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Plantilla de Briefing Pre-Evento',
        value: '€7',
        desc: 'La reunión de 30 min antes de abrir puertas. Info del evento, menú, alérgenos, equipo, VIPs y protocolo.',
        image: '/lovable-uploads/ai-gallery/tareas-catering-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Temporada Alta',
        value: '€9',
        desc: '22 fechas clave para catering (bodas, corporativos, Navidad, comuniones, Día del Padre, puente de diciembre) con antelación de preparación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu empresa de catering, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para catering y eventos?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una empresa de catering profesional. Solo tienes que personalizar: ajustar tareas a tu operación, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Cubre todo el ciclo del evento, no solo el servicio?',
      a: 'Sí. Incluye producción off-site (cocina central), transporte y logística, montaje del venue, servicio durante el evento, desmontaje y post-evento. Es el ciclo completo.',
    },
    {
      q: '¿Sirve para bodas, corporativos y cocktails?',
      a: 'Sí. Incluye checklists genéricos (producción, transporte, montaje) que sirven para cualquier evento, más checklists específicos por tipo: bodas, corporativos, cocktail/standing y eventos outdoor.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en eventos.',
    },
    {
      q: '¿Puedo usarlo en varios eventos simultáneos?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los eventos que gestiones. Ideal para empresas de catering con varios eventos por semana.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Improvisar en Cada Evento',
    subtitle:
      '9 plantillas + 2 bonus (11 ficheros) para catering por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Producción off-site: planificación, mise en place, empaquetado',
      'Transporte: cadena de frío, carga, descarga, APPCC',
      'Cobros por evento: anticipos, liquidación con IVA 10/21 % y saldos vencidos',
      'Montaje: cocina temporal, sala, buffet, estaciones de acción',
      'Tareas del event manager: semana previa + día del evento',
      'Tareas por perfil: chef, maître, camarero, barman',
      'Tipos de evento: bodas, corporativos, cocktails, outdoor',
      'BONUS: Briefing Pre-Evento (€7)',
      'BONUS: Calendario Anual Temporada Alta (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle:
      'Event managers, chefs de catering y coordinadores que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Manuel Domínguez',
        role: 'Director, Catering Elegance Madrid',
        text: 'Antes cada evento era un caos organizado. Los checklists de producción y transporte eliminaron el 90% de los olvidos. Ahora el equipo eventual sabe exactamente qué hacer sin preguntar.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Javier Montero',
        role: 'Chef Ejecutivo, Grupo Banquetes del Sur',
        text: 'El checklist de producción off-site es oro puro. Mise en place, empaquetado, control de temperatura... todo en una hoja. Mis cocineros lo imprimen y lo siguen paso a paso.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Laura Sánchez',
        role: 'Event Manager, Bodas con Alma',
        text: 'Hago 3-4 bodas por semana en temporada alta. Los checklists por tipo de evento me ahorran horas de preparación. El de bodas cubre desde el cocktail hasta la recena.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Roberto Ibáñez',
        role: 'Gerente, Catering Corporativo BCN',
        text: 'Los coffee breaks y eventos corporativos requieren precisión militar. El timing sheet del event manager y las tareas por perfil han profesionalizado nuestra operación.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Torres',
        role: 'Coordinadora Logística, Grupo Eventos Premium',
        text: 'El checklist de transporte y cadena de frío es exactamente lo que necesitábamos para cumplir normativa APPCC. Ya no improvisamos con las temperaturas.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Diana Fernández',
        role: 'Maître, Hotel Palace Catering',
        text: 'Las tareas por perfil para camareros de evento son geniales para personal eventual. Les damos la hoja impresa y saben qué hacer antes, durante y después del servicio.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Carmen Ruiz',
        role: 'Propietaria, Catering a Domicilio Valencia',
        text: 'El checklist de montaje y desmontaje del venue me salvó la vida. Antes siempre nos dejábamos algo. Ahora hacemos el recorrido final con la lista y nunca falla.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Sergio Navarro',
        role: 'Director de Operaciones, Catering 360',
        text: 'El calendario anual de temporada alta es brutal para planificar personal eventual. Sabemos exactamente cuándo necesitamos más gente y podemos anticiparnos meses.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Isabel García',
        role: 'Consultora de Eventos y Catering',
        text: 'Recomiendo este kit a todos mis clientes de catering. Producción, transporte, montaje, servicio... cubren el ciclo completo. Es el estándar que debería tener toda empresa de eventos.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Francisco López',
        role: 'Formador, Escuela de Hostelería y Eventos',
        text: 'Mis alumnos de catering usan estos checklists como referencia. Las tareas están perfectamente estructuradas por fase del evento. Es material de formación de primera.',
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
    { href: '/kit-tareas-bar', label: 'Kit Tareas Bar' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-catering',
    label: '¿Ya compraste el Kit de Tareas Catering? Vuelve a entrar al dashboard',
  },
};

export default data;
