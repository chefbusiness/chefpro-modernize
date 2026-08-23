// astro-site/src/data/productos/tareas/kit-tareas-chocolateria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasChocolateria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-chocolateria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-chocolateria.ts  (marquee de testimonios)
// NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-chocolateria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_CHOCOLATERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Chocolatería / Obrador de Chocolate | AI Chef Pro',
    description:
      '9 plantillas + 2 bonus (11 ficheros) con 338 tareas ya escritas para chocolatería artesanal: producción (templado, moldeado, bombones), apertura/cierre de negocio, arqueo de caja, vitrina, servicio, gestión y temporada. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist chocolatería, tareas chocolatero, checklist apertura chocolatería, tareas producción chocolate, control stock chocolatería, plantilla tareas obrador chocolate, checklist cierre chocolatería, inventario chocolatería, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-chocolateria.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Chocolatería / Obrador de Chocolate',
    productDescription:
      '9 plantillas + 2 bonus (11 ficheros) con 338 tareas ya escritas para chocolatería artesanal: producción, apertura y cierre de negocio, arqueo de caja, vitrina, servicio, gestión y temporada.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Miguel Ángel Roca',
        rating: '5',
        body: 'El checklist de producción me salvó. Ahora el templado, moldeado y envasado quedan documentados y el control de calidad es impecable.',
      },
      {
        author: 'Elena Montero',
        rating: '5',
        body: 'Tenemos 4 tiendas y ahora con los checklists estandarizados la experiencia es la misma en todas.',
      },
      {
        author: 'Patricia Vega',
        rating: '5',
        body: 'Lo primero que hago con cada cliente de chocolatería es entregarle estos checklists. Cubren el 95% de lo que necesita.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para chocolatería?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una chocolatería artesanal. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Cubre producción artesanal y tienda?',
        a: 'Sí. Templado, moldeado, bombones, tabletas, envasado, vitrina, mostrador y gestión.',
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
    breadcrumbName: 'Kit de Tareas Recurrentes: Chocolatería / Obrador de Chocolate',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-chocolateria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-chocolateria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/tareas-chocolateria-obrador.jpg',
      '/lovable-uploads/ai-gallery/tareas-chocolateria-produccion.jpg',
      '/lovable-uploads/ai-gallery/tareas-chocolateria-servicio.jpg',
      '/lovable-uploads/ai-gallery/tareas-chocolateria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-chocolateria-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-chocolateria-produccion.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-chocolateria-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Chocolatería / Obrador de Chocolate — Checklists por Turno, Zona y Perfil',
    description:
      '9 plantillas + 2 bonus (11 ficheros) en Excel con 338 tareas de chocolatería artesanal ya escritas: producción, apertura/cierre de negocio, arqueo de caja, vitrina, servicio, gestión y temporada. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Producción: templado, moldeado, bombones, tabletas, envasado',
      'Apertura/cierre de negocio y arqueo de caja con recuento por denominaciones y báscula de mostrador',
      'Servicio: vitrina, mostrador, packaging, degustación',
      'Perfiles: chocolatero/maestro, dependiente, encargado',
      'Gestión: manager diario/semanal/mensual + food cost',
      'Temporada: Navidad, San Valentín, Pascua, calendario anual',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS CHOCOLATERÍA — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas + 2 Bonus (11 ficheros)',
    subtitle:
      '338 tareas de chocolatería artesanal ya escritas y repartidas por turno, zona y perfil. Ajusta a tu obrador, imprime y delega.',
    templates: [
      {
        icon: 'CakeSlice',
        title: 'Apertura y Cierre',
        desc: 'Checklists completos: vitrina, mostrador, obrador, higiene personal y arranque seguro, control de cámaras y vitrina temperada. 41 tareas ya escritas solo en este fichero.',
      },
      {
        icon: 'Beaker',
        title: 'Partidas de Producción',
        desc: 'Templado de chocolate, moldeado de bombones y tabletas, envasado, control de temperaturas, etiquetado y registro de lotes.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus control de food cost y mermas de producción.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists para: maestro chocolatero/obrador, dependiente de tienda y encargado de turno. Cada puesto sabe qué hacer.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Deep clean de obrador, mantenimiento de temperadora, inventario semanal por categoría (coberturas, rellenos, packaging, moldes). + hoja Trimestral y Anual: DDD, extintores y BIE, gas, legionela, SAT de temperadora y cámaras, calibración de sondas y báscula, con nº de parte y firma.',
      },
      {
        icon: 'Gift',
        title: 'Eventos y Temporada',
        desc: 'Navidad, San Valentín, Pascua, Día de la Madre. Producción especial, packaging gift, catálogo estacional.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas maestras ya estructuradas —por zona, por turno y por perfil— con el contador ya calculado por fórmula: tú solo escribes tus tareas en las celdas verdes.',
      },
      {
        icon: 'Building2',
        title: 'Apertura y Cierre de Negocio',
        desc: 'Checklist del local completo (no solo obrador): vitrinas temperadas, escaparate, encargos y mobiliario de tienda. Responsable y hora precargados en 32 tareas.',
      },
      {
        icon: 'Wallet',
        title: 'Arqueo y Registro de Caja',
        desc: 'Apertura y cierre de caja con recuento por denominaciones, báscula de mostrador y cuadre del precio por kilo, con descuadre automático frente al Z del TPV. Incluye registro mensual con descuadre por fórmula.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Diario',
        desc: 'Plantilla de briefing diario: producción del día, pedidos especiales, stock packaging, equipo del turno, promociones activas.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Calendario mensual de 12 meses con las fechas señaladas dentro de cada mes (Navidad, San Valentín, Pascua, Reyes, comuniones, 15 de agosto, Todos los Santos, puente de diciembre…) y su preparación recomendada.',
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
        title: 'Pre-Rellenadas para Chocolatería',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de producción artesanal de chocolate. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'CakeSlice',
        title: 'Producción + Servicio Cubiertos',
        desc: 'Obrador, templado, moldeado, bombones, tabletas, vitrina, mostrador y gestión. Las tareas que los sistemas genéricos no cubren para chocolatería artesanal.',
      },
      {
        icon: 'Users',
        title: 'Perfiles Específicos',
        desc: 'Checklists para maestro chocolatero/obrador, dependiente de tienda y encargado de turno. Cada puesto sabe exactamente qué hacer.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan chocolaterías con SaaS premium, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes, chocolaterías y obradores.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €18',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Diario de Chocolatería',
        value: '€9',
        desc: 'La reunión de 5 minutos que marca la diferencia. Producción del día, pedidos especiales, stock packaging, equipo del turno, promociones activas.',
        image: '/lovable-uploads/ai-gallery/tareas-chocolateria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Chocolatería',
        value: '€9',
        desc: 'Calendario mensual de 12 meses con las fechas señaladas dentro de cada mes (Navidad, San Valentín, Pascua, Día de la Madre, comuniones, ferias…) y su preparación con antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-chocolateria-vitrina.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu chocolatería, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para chocolatería?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una chocolatería artesanal: producción (templado, moldeado, bombones), vitrina, mostrador, obrador y gestión. Solo tienes que personalizar: ajustar tareas a tu negocio, borrar las que no apliquen y añadir las específicas. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Cubre producción artesanal y tienda?',
      a: 'Sí. Las plantillas cubren todo el ciclo: templado de coberturas, moldeado de bombones y tabletas, envasado, control de temperaturas en obrador, y también vitrina, packaging, mostrador, degustación y gestión diaria.',
    },
    {
      q: '¿Sirve para obradores pequeños y cadenas?',
      a: 'Sí. Las plantillas son escalables. Un obrador pequeño puede usar producción + vitrina + cierre. Una cadena puede usar todos los perfiles, zonas y el calendario completo. Adapta lo que necesites.',
    },
    {
      q: '¿En qué se diferencia del software de gestión?',
      a: 'El software de gestión cobra €40/mes por local y requieren tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias chocolaterías?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de chocolaterías y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle: '9 plantillas + 2 bonus (11 ficheros) por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: vitrina, mostrador, obrador, limpieza',
      'Apertura/cierre de negocio y arqueo de caja con descuadre automático',
      'Partidas de producción: templado, moldeado, bombones, tabletas',
      'Inventario semanal: coberturas, rellenos, moldes, packaging, consumibles',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: chocolatero, dependiente, encargado',
      'Eventos y temporada: Navidad, San Valentín, Pascua, fechas clave',
      'BONUS: Briefing Diario de Chocolatería (€9)',
      'BONUS: Calendario Anual de Chocolatería (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle: 'Chocolateros, encargados y dueños de chocolatería que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Miguel Ángel Roca',
        role: 'Maestro chocolatero, Chocolatería Roca',
        text: 'El checklist de producción me salvó. Antes olvidaba registrar temperaturas de templado y tiempos de cristalización. Ahora todo queda documentado y el control de calidad es impecable.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Elena Montero',
        role: 'Propietaria, Bombonería La Trufa Dorada',
        text: 'Abrí mi chocolatería hace un año y el caos de Navidad era insostenible. Con los checklists por turno y zona, el equipo sabe exactamente qué hacer sin que yo esté encima.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Javier Solís',
        role: 'Jefe de obrador, Chocolates Artesanos Solís',
        text: 'Las partidas de producción están perfectamente estructuradas: templado, moldeado, bombones, tabletas, envasado. Mis chocolateros nuevos aprenden el proceso en la mitad de tiempo.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fuentes',
        role: 'Encargada de tienda, Cacao & Co.',
        text: 'El checklist de vitrina es genial. Bombones, tabletas, packaging, limpieza de expositores... todo está listado. La tienda siempre está perfecta para el cliente.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Carlos Mendoza',
        role: 'Director, Cadena Chocolaterías Mendoza',
        text: 'Tenemos 4 tiendas y cada encargado hacía las cosas diferente. Ahora con los checklists estandarizados, la experiencia del cliente es la misma en todas. El onboarding pasó de 2 semanas a 4 días.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Consultora gastronómica, Chocolaterías & Obradores',
        text: 'Lo primero que hago con cada cliente de chocolatería es entregarle estos checklists. Producción, vitrina, gestión, temporada... cubren el 95% de lo que necesita cualquier chocolatería artesanal.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Andrés Beltrán',
        role: 'Maestro chocolatero, Obrador Beltrán',
        text: 'El calendario estacional es oro puro. Navidad, San Valentín, Pascua, Día de la Madre, ferias... por fin tengo la planificación anual que siempre quise tener.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Sergio Herrera',
        role: 'Gerente, Chocolatería Origen',
        text: 'El control de food cost y mermas de producción que incluye el checklist del manager es justo lo que necesitábamos. Antes las mermas de cobertura nos sorprendían a final de mes. Ahora las controlamos a diario.',
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
    { href: '/kit-tareas-heladeria', label: 'Kit Tareas Heladería' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-chocolateria',
    label: '¿Ya compraste el Kit de Tareas Chocolatería? Vuelve a entrar al dashboard',
  },
};

export default data;
