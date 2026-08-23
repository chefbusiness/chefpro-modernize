// astro-site/src/data/productos/tareas/kit-tareas-heladeria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasHeladeria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-heladeria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-heladeria.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-heladeria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_HELADERIA',

  seo: {
    title: 'Kit de Tareas Recurrentes — Checklists Operativos para Heladería Artesanal | AI Chef Pro',
    description: 'Kit de 9 plantillas + 2 bonus (11 ficheros): checklists operativos para heladería artesanal con las tareas más habituales ya escritas — producción, vitrina, servicio, gestión y temporada. Imprime, delega y firma. Solo €12.',
    keywords: 'checklist heladería, tareas heladero, checklist apertura heladería, tareas producción helados, control stock heladería, plantilla tareas vitrina, checklist cierre heladería, inventario heladería, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-heladeria.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Heladería Artesanal',
    productDescription: '9 plantillas + 2 bonus (11 ficheros): checklists operativos para heladería artesanal con 298 tareas ya escritas — producción, vitrina, servicio, gestión y temporada.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Adrián Molina',
        rating: '5',
        body: 'El checklist de producción me salvó. Ahora todo queda documentado y el control de calidad es impecable.',
      },
      {
        author: 'Raúl Ibáñez',
        rating: '5',
        body: 'Tenemos 6 heladerías y ahora con los checklists estandarizados la experiencia es la misma en todas.',
      },
      {
        author: 'Sofía Delgado',
        rating: '5',
        body: 'Lo primero que hago con cada cliente de heladería es entregarle estos checklists. Cubren el 95% de lo que necesita.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para heladería?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una heladería artesanal. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Cubre producción y servicio?',
        a: 'Sí. Pasteurización, maduración, mantecación, envasado, vitrina, mostrador y gestión.',
      },
      {
        q: '¿En qué se diferencia del software de gestión?',
        a: 'El software de gestión cobra €40/mes por local. Este kit da las mismas listas en Excel por €12, pago único.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Heladería Artesanal',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-heladeria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-heladeria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/tareas-heladeria-obrador.jpg',
      '/lovable-uploads/ai-gallery/tareas-heladeria-produccion.jpg',
      '/lovable-uploads/ai-gallery/tareas-heladeria-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-heladeria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-heladeria-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-heladeria-produccion.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-heladeria-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Heladería Artesanal — Checklists por Turno, Zona y Perfil',
    description: '9 plantillas + 2 bonus (11 ficheros) en Excel con 298 tareas de heladería artesanal ya escritas: producción, vitrina, servicio, gestión y temporada. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Producción: pasteurización, maduración, mantecación, envasado',
      'Servicio: vitrina, toppings, salsas, mostrador',
      'Perfiles: heladero/obrador, dependiente, encargado',
      'Gestión: manager diario/semanal/mensual + food cost',
      'Temporada: carta estacional, catering eventos, calendario anual',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS HELADERÍA — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas + 2 Bonus (11 ficheros)',
    subtitle: '298 tareas de heladería artesanal ya escritas y repartidas por turno, zona y perfil. Ajusta a tu local, imprime y delega.',
    templates: [
      {
        icon: 'IceCream',
        title: 'Apertura y Cierre',
        desc: 'Checklists completos: higiene personal y arranque seguro, vitrina, toppings, salsas, caja, mostrador, limpieza de obrador y cierre administrativo. 43 tareas ya escritas solo en este fichero.',
      },
      {
        icon: 'Beaker',
        title: 'Partidas de Producción',
        desc: 'Pasteurización, maduración, mantecación, envasado, control de calidad, temperaturas y registro de lotes por sabor.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus control de food cost y mermas de producción.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists para: heladero/obrador, dependiente de mostrador y encargado de turno. Cada puesto sabe qué hacer.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Deep clean de obrador, mantenimiento de mantecadora, inventario semanal por categoría (bases, frutas, toppings, envases). + hoja Trimestral y Anual: DDD, conductos de extracción, gases fluorados, extintores, gas, legionela y registro sanitario, con nº de parte y firma.',
      },
      {
        icon: 'Sun',
        title: 'Eventos y Temporada',
        desc: 'Carta estacional (verano/invierno), catering para eventos, fechas clave (Día del Helado, ferias, fiestas locales).',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas maestras ya estructuradas —por zona, por turno y por perfil— con las secciones ya montadas: tú solo escribes tus tareas en las celdas verdes.',
      },
      {
        icon: 'Building2',
        title: 'Apertura y Cierre de Negocio',
        desc: 'Checklist del local completo (no solo obrador): luces, alarma, TPV, vitrina y terraza. Responsable y hora límite precargados en las 33 tareas.',
      },
      {
        icon: 'Wallet',
        title: 'Arqueo y Registro de Caja',
        desc: 'Apertura y cierre de caja con recuento por denominaciones, fondo de caja y descuadre automático frente al Z del TPV. Incluye registro mensual con descuadre por fórmula en las 31 filas del mes.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Diario',
        desc: 'Plantilla de briefing diario: sabores del día, stock de cucuruchos, eventos, equipo del turno, promociones activas.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Calendario mensual con los 12 meses del año y las fechas señaladas de heladería ya colocadas dentro de cada mes (Día de la Madre, comuniones, San Juan, verano, 15 de agosto, Navidad y más) con la acción clave de cada una.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle: 'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Heladería',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de producción artesanal de helados. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'IceCream',
        title: 'Producción + Servicio Cubiertos',
        desc: 'Obrador, pasteurización, mantecación, vitrina, mostrador y gestión. Las tareas que los sistemas genéricos no cubren para heladería artesanal.',
      },
      {
        icon: 'Users',
        title: 'Perfiles Específicos',
        desc: 'Checklists para heladero/obrador, dependiente de mostrador y encargado de turno. Cada puesto sabe exactamente qué hacer.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan heladerías con SaaS premium, pero en Excel por un pago único. Sin suscripción.',
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

  authorBio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes, heladerías y obradores.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €18',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Diario de Heladería',
        value: '€9',
        desc: 'La reunión de 5 minutos que marca la diferencia. Sabores del día, stock de cucuruchos, eventos, equipo del turno, promociones activas.',
        image: '/lovable-uploads/ai-gallery/tareas-heladeria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Heladería',
        value: '€9',
        desc: 'Calendario mensual con los 12 meses del año y las fechas señaladas de heladería ya colocadas en cada mes (Día de la Madre, comuniones, San Juan, verano, 15 de agosto, Navidad y más) con la acción clave de cada fecha.',
        image: '/lovable-uploads/ai-gallery/tareas-heladeria-vitrina.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu heladería, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para heladería?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una heladería artesanal: producción, vitrina, mostrador, obrador y gestión. Solo tienes que personalizar: ajustar tareas a tu heladería, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Cubre producción y servicio?',
      a: 'Sí. Las plantillas cubren todo el ciclo: pasteurización, maduración, mantecación, envasado, control de calidad en obrador, y también vitrina, toppings, salsas, mostrador y gestión diaria.',
    },
    {
      q: '¿Sirve para heladerías pequeñas y grandes?',
      a: 'Sí. Las plantillas son escalables. Una heladería pequeña puede usar producción + vitrina + cierre. Una cadena puede usar todos los perfiles, zonas y el calendario completo. Adapta lo que necesites.',
    },
    {
      q: '¿En qué se diferencia del software de gestión?',
      a: 'El software de gestión cobra €40/mes por local y requieren tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias heladerías?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de heladerías y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle: '9 plantillas + 2 bonus (11 ficheros) para heladería por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: vitrina, toppings, caja, limpieza',
      'Partidas de producción: pasteurización, mantecación, envasado',
      'Inventario semanal: bases, frutas, toppings, envases, consumibles',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: heladero, dependiente, encargado',
      'Eventos y temporada: carta estacional, catering, fechas clave',
      'BONUS: Briefing Diario de Heladería (€9)',
      'BONUS: Calendario Anual de Heladería (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle: 'Heladeros, encargados y dueños de heladería que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Adrián Molina',
        role: 'Heladero artesanal, Gelateria Dolce Vita',
        text: 'El checklist de producción me salvó. Antes olvidaba registrar temperaturas de pasteurización y maduración. Ahora todo queda documentado y el control de calidad es impecable.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Lucía Torres',
        role: 'Propietaria, Heladería La Cremería',
        text: 'Abrí mi heladería hace un año y el caos de temporada alta era insostenible. Con los checklists por turno y zona, el equipo sabe exactamente qué hacer sin que yo esté encima.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Pablo Reyes',
        role: 'Jefe de producción, Helados Artesanos Reyes',
        text: 'Las partidas de producción están perfectamente estructuradas: pasteurización, mantecación, envasado, etiquetado. Mis heladeros nuevos aprenden el proceso en la mitad de tiempo.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Carmen Ortiz',
        role: 'Encargada de mostrador, Heladería El Polo Norte',
        text: 'El checklist de vitrina es genial. Toppings, salsas, cucuruchos, limpieza de cristales... todo está listado. El mostrador siempre está perfecto para el cliente.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Raúl Ibáñez',
        role: 'Director, Cadena Heladerías Frozen Art',
        text: 'Tenemos 6 heladerías y cada encargado hacía las cosas diferente. Ahora con los checklists estandarizados, la experiencia del cliente es la misma en todas. El onboarding pasó de 2 semanas a 4 días.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Sofía Delgado',
        role: 'Consultora gastronómica, Heladerías & Obradores',
        text: 'Lo primero que hago con cada cliente de heladería es entregarle estos checklists. Producción, vitrina, gestión, temporada... cubren el 95% de lo que necesita cualquier heladería artesanal.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Marco Valentini',
        role: 'Maestro heladero, Gelateria Valentini',
        text: 'El calendario estacional es oro puro. Carta de verano, carta de invierno, fechas clave, preparación de catering... por fin tengo la planificación anual que siempre quise tener.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Ana Belén Ruiz',
        role: 'Gerente, Heladería Sabores del Sur',
        text: 'El control de food cost y mermas de producción que incluye el checklist del manager es justo lo que necesitábamos. Antes las mermas nos sorprendían a final de mes. Ahora las controlamos a diario.',
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
    { href: '/kit-tareas-bar', label: 'Kit Tareas Bar' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-heladeria',
    label: '¿Ya compraste el Kit de Tareas Heladería? Vuelve a entrar al dashboard',
  },
};

export default data;
