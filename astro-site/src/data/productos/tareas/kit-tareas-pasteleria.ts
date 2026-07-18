// astro-site/src/data/productos/tareas/kit-tareas-pasteleria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasPasteleria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-pasteleria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-pasteleria.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-pasteleria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_PASTELERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Pastelería / Obrador | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para pastelería y obrador: producción de masas, fermentación, cremas, decoración, vitrina, perfiles y eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist pastelería, tareas obrador, checklist apertura pastelería, tareas pastelero, control producción pastelería, plantilla tareas obrador, checklist vitrina pastelería, fermentación croissant checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-pasteleria.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Pastelería / Obrador',
    productDescription:
      '9 checklists operativos pre-rellenados para pastelería y obrador: producción de masas, fermentación, cremas, decoración, vitrina, perfiles y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Marta Vidal',
        rating: '5',
        body: 'El checklist de fermentación y laminado nos salvó. Ahora seguimos el mismo protocolo y los croissants salen perfectos cada día.',
      },
      {
        author: 'Laura Fernández',
        rating: '5',
        body: 'Gestionar un obrador que produce bollería, pan y pastelería era caótico. Los checklists por zona y perfil pusieron orden desde el primer día.',
      },
      {
        author: 'Raquel Sánchez',
        rating: '5',
        body: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Producción, vitrinas, limpieza, inventario... cubren el 95% de lo que necesita cualquier obrador.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para pastelería?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una pastelería / obrador. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu negocio.',
      },
      {
        q: '¿Incluye tareas de producción artesanal?',
        a: 'Sí. Masas de bollería, fermentación, laminado, cremas, mousses, decoración y montaje de vitrina. Todo detallado por partida de producción.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varias pastelerías?',
        a: 'Sí. Licencia personal para todos los establecimientos que gestiones.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Pastelería / Obrador',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-horno.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-decoracion.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-produccion.jpg',
    ],
    // ContentGrid strip difiere del hero en la 6ª imagen (equipo en vez de produccion).
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-horno.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-decoracion.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/tareas-pasteleria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-pasteleria-horno.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60-75/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Pastelería / Obrador — Checklists por Turno, Área y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu pastelería: producción de masas, fermentación, cremas, decoración, vitrina, eventos y perfiles. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: obrador, horno, vitrina, despacho',
      'Partidas de producción: masas, fermentación, cremas, decoración',
      'Tareas por perfil: jefe pastelero, oficial, ayudante, dependiente',
      'Eventos y temporadas: Navidad, Reyes, San Valentín, Día de la Madre',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS PASTELERÍA — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de una pastelería / obrador. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '6 checklists: apertura y cierre de obrador, horno, vitrina y despacho. Cada tarea con responsable, hora límite y firma. ~45 tareas pre-rellenadas.',
      },
      {
        icon: 'Croissant',
        title: 'Partidas de Producción',
        desc: 'Masas y fermentación (croissant, brioche, pan), cremas y rellenos (pastelera, ganache, mousse), decoración y montaje de vitrina.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: jefe pastelero, pastelero oficial, ayudante de pastelería y dependiente de vitrina.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de hornos, amasadora y laminadora.',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Navidad (roscón, turrones), San Valentín (bombones, tartas corazón), Semana Santa (torrijas, monas), Día de la Madre y más.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por zona, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing diario: producción del día, encargos especiales, alérgenos, equipo del turno. Imprime y pega en obrador.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: '17 fechas clave de pastelería con producción especial y antelación recomendada. Añade tus fechas locales.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un profesional con 29 años en alta hostelería.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Pastelería',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un obrador. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Croissant',
        title: 'Producción Artesanal Completa',
        desc: 'Masas, fermentación, laminado, cremas, mousses, decoración, montaje de vitrina. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Perfiles Específicos',
        desc: 'Checklists para jefe pastelero, oficial, ayudante y dependiente. Cada puesto sabe exactamente qué hacer cada turno.',
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan obradores con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha diseñado sistemas operativos y checklists para cientos de restaurantes, pastelerías y obradores.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 9 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Plantilla de Briefing Pre-Servicio',
        value: '€7',
        desc: 'La reunión de 5 minutos que separa a los obradores buenos de los excelentes. Producción del día, encargos especiales, alérgenos, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-pasteleria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '17 fechas clave de pastelería (Reyes, San Valentín, Día de la Madre, Navidad) con producción especial y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-pasteleria-vitrina.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu pastelería, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para pastelería?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una pastelería / obrador. Solo tienes que personalizar: ajustar tareas a tu negocio, borrar las que no apliquen y añadir las específicas de tu obrador. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye tareas de producción artesanal (croissants, tartas, pan)?',
      a: 'Sí. Las partidas de producción cubren masas de bollería (croissant, brioche, danesa), masas de pan artesano, masas quebradas, cremas y rellenos (pastelera, ganache, mousse), decoración y montaje de vitrina.',
    },
    {
      q: '¿Sirve para una pastelería pequeña y para un obrador grande?',
      a: 'Sí. Las plantillas son escalables. Una pastelería pequeña puede usar las tareas de obrador + vitrina. Un obrador industrial puede usar todas las partidas de producción + gestión de pedidos.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias pastelerías u obradores?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de pastelerías y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Día',
    subtitle:
      '9 checklists operativos para pastelería por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: obrador, horno, vitrina',
      'Partidas: masas, fermentación, cremas, mousse, decoración',
      'Control de producción: temperaturas, tiempos, FIFO',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: jefe pastelero, oficial, ayudante, dependiente',
      'Eventos: Navidad, Reyes, San Valentín, Día de la Madre',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle: 'Pasteleros, encargados y dueños de obrador que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Marc Vidal',
        role: 'Jefe de Pastelería, Obrador Sant Jordi',
        text: 'El checklist de fermentación y laminado nos salvó. Antes cada pastelero laminaba a su manera y la bollería era inconsistente. Ahora seguimos el mismo protocolo y los croissants salen perfectos cada día.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Pablo Roca',
        role: 'Dueño, Pastelería La Miga de Oro',
        text: 'Abrí mi pastelería hace un año y me olvidaba de todo: encender hornos a tiempo, sacar masas de fermentación, controlar vitrinas. Estas checklists me organizaron desde la primera semana.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Encargada, Dulce Tradición Obrador',
        text: 'Gestionar un obrador que produce bollería, pan y pastelería era caótico. Los checklists por zona y por perfil pusieron orden. El onboarding de ayudantes pasó de 2 semanas a 4 días.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Carlos Martín',
        role: 'Chef Pâtissier, Hotel Meliá Valencia',
        text: 'En un hotel con buffet de desayuno y pastelería de tarde necesitas que todo esté listo a tiempo. Los checklists de apertura por turno eliminaron los olvidos del equipo de noche.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Torres',
        role: 'Propietaria, Macarons & Co',
        text: 'Las tareas de control de vitrina y etiquetado de alérgenos son oro. Con la normativa actual, tener un checklist impreso cada día nos da tranquilidad ante cualquier inspección.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Javier Molina',
        role: 'Maestro Pastelero, Obrador Artesano BCN',
        text: 'Las tareas de mantenimiento mensual de hornos y amasadoras son justo lo que necesitábamos. Antes no teníamos protocolo y los equipos se averiaban por falta de mantenimiento preventivo.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Isabel García',
        role: 'Gerente, Pastelería Familiar El Rincón Dulce',
        text: 'El calendario anual de tareas especiales es increíble. Navidad, Reyes, San Valentín, Día de la Madre... ahora planificamos la producción con semanas de antelación en vez de improvisar.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Diego Alonso',
        role: 'Ayudante de Pastelería, Grupo Europastry',
        text: 'Como ayudante, el checklist de mi perfil me dice exactamente qué se espera de mí cada turno. No tengo que preguntar constantemente qué hacer. Me da autonomía.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Raquel Sánchez',
        role: 'Consultora de Obradores',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Les pone orden desde el primer día. Producción, vitrinas, limpieza, inventario... cubren el 95% de lo que necesita cualquier obrador.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Fernando López',
        role: 'Formador de Pastelería, Escuela Hofmann',
        text: 'Recomiendo este kit a todos mis alumnos que van a abrir su propio obrador. Las tareas de producción están perfectamente estructuradas por partida. Es el estándar que debería tener toda pastelería.',
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
    product: 'kit-tareas-pasteleria',
    label: '¿Ya compraste el Kit de Tareas Pastelería? Vuelve a entrar al dashboard',
  },
};

export default data;
