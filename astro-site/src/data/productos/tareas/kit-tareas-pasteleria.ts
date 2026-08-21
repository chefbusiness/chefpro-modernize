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
      'Kit de Tareas Recurrentes — 13 Checklists Operativos + 2 Bonus para Pastelería / Obrador | AI Chef Pro',
    description:
      '13 plantillas + 2 bonus para pastelería y obrador: 9 checklists pre-rellenados con las tareas reales de un obrador (masas, fermentación, cremas, vitrina) y 4 registros listos para rellenar: producción y mermas, encargos, alérgenos de vitrina (14 UE) y temperaturas. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist pastelería, tareas obrador, checklist apertura pastelería, tareas pastelero, control producción pastelería, plantilla tareas obrador, checklist vitrina pastelería, fermentación croissant checklist, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-pasteleria.jpg',
  },

  schema: {
    productName:
      'Kit de Tareas Recurrentes — 13 Checklists Operativos + 2 Bonus para Pastelería / Obrador',
    productDescription:
      '13 plantillas + 2 bonus para pastelería y obrador: 9 checklists pre-rellenados con las tareas reales de un obrador (masas, fermentación, cremas, decoración, vitrina) y 4 registros listos para rellenar: producción y mermas, encargos, alérgenos de vitrina (14 UE) y temperaturas.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    // = faqs on-page, mismo texto y orden (Google exige que el FAQPage sea visible tal cual)
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para pastelería?',
        a: 'Los 9 checklists vienen pre-rellenados con las tareas reales de una pastelería / obrador: solo tienes que ajustar tareas a tu negocio, borrar las que no apliquen y añadir las específicas de tu obrador. Los 4 registros (producción y mermas, encargos, alérgenos y temperaturas) se entregan listos para rellenar con tus datos; la matriz de alérgenos trae más de 30 productos de partida que debes verificar con tus recetas y proveedores. Las celdas editables están marcadas en verde.',
      },
      {
        q: '¿Incluye tareas de producción artesanal (croissants, tartas, pan)?',
        a: 'Sí. Las partidas de producción cubren masas de bollería (croissant, brioche, danesa), masas de pan artesano, masas quebradas, cremas y rellenos (pastelera, ganache, mousse), decoración y montaje de vitrina.',
      },
      {
        q: '¿Sirve para una pastelería pequeña y para un obrador grande?',
        a: 'Sí. Las plantillas son escalables. Una pastelería pequeña puede usar las tareas de obrador y vitrina. Un obrador industrial puede usar todas las partidas de producción, el control de encargos (ficha imprimible, registro mensual y agenda de entregas) y el plan de producción semanal.',
      },
      {
        q: '¿Qué incluye la versión 2.0?',
        a: 'La versión 2.0 amplía el kit a 13 checklists operativos + 2 bonus. Se suman cuatro plantillas nuevas: el plan de producción semanal con control de mermas en porcentaje y en euros, el control de encargos (ficha imprimible, registro mensual y agenda de entregas), la matriz de alérgenos de vitrina con los 14 de declaración obligatoria (con carta, cartel y etiquetas) y el registro de temperaturas con recepción de mercancía y etiquetas de elaborado. Además, la apertura y el cierre del negocio se han reescrito para una pastelería con tienda y todas las plantillas llevan la impresión A4 ya configurada.',
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
      '13 plantillas Excel: 9 checklists pre-rellenados con las tareas reales de tu pastelería (masas, fermentación, cremas, decoración, vitrina) y 4 registros listos para rellenar (producción y mermas, encargos, alérgenos, temperaturas). Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre del obrador: equipos, producción y vitrina/despacho',
      'Partidas de producción: masas, fermentación, cremas, decoración',
      'Tareas por perfil: jefe pastelero, oficial, ayudante, dependiente',
      'Eventos y temporadas: Navidad, Reyes, San Valentín, Semana Santa, comuniones, Todos los Santos',
      'Plantilla en blanco personalizable + briefing de servicio',
      'Plan de producción con mermas, fichas de encargo, alérgenos de vitrina (14 UE) y registro de temperaturas',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS PASTELERÍA — €12',

  grid: {
    countGold: '13',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      '9 checklists pre-rellenados con las tareas reales de una pastelería / obrador y 4 registros listos para rellenar. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '2 checklists (apertura y cierre del obrador) con 6 bloques y 42 tareas pre-rellenadas. Cada tarea con zona, responsable, hora límite y firma.',
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
        desc: 'Navidad y Reyes (roscón, turrones), San Valentín, Semana Santa (torrijas, monas), Día de la Madre y del Padre, comuniones (flujo de encargo completo) y Todos los Santos (huesos de santo, panellets, buñuelos). Cada campaña cierra con su post-campaña.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por zona, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Store',
        title: 'Apertura y Cierre del Negocio',
        desc: 'Pastelería con tienda: vitrinas encendidas y a 2-6 °C, montaje del expositor, etiquetas de precio y alérgenos, encargos del día, TPV y cierre con el sobrante anotado en mermas.',
      },
      {
        icon: 'Euro',
        title: 'Apertura y Cierre de Caja',
        desc: 'Fondo de caja, recuento por denominación al cierre, Z del TPV, descuadre calculado cada día y registro mensual de facturación por forma de pago.',
      },
      {
        icon: 'CalendarRange',
        title: 'Plan de Producción Semanal y Mermas',
        desc: 'Plan de la semana por partida con productos ya listados, producido frente a vendido, sobrante, merma en porcentaje y en euros, y resumen semanal con objetivo.',
      },
      {
        icon: 'ShoppingCart',
        title: 'Control de Encargos',
        desc: 'Ficha de encargo imprimible (cliente, entrega, alérgenos, señal y pendiente), registro mensual de encargos con estado y agenda de entregas por franjas horarias.',
      },
      {
        icon: 'ShieldAlert',
        title: 'Alérgenos de Vitrina (14 UE)',
        desc: 'Matriz de los 14 alérgenos referencia por referencia para contrastar con tus fichas técnicas, carta de alérgenos, cartel para la vitrina y etiquetas recortables.',
      },
      {
        icon: 'Thermometer',
        title: 'Temperaturas, Recepción y Etiquetas',
        desc: 'Registro mensual de temperaturas por equipo con dos tomas al día, control de recepción de mercancía con criterios de rechazo y etiquetas de elaborado con fecha y lote.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef y consultor gastronómico en activo desde 2010, en cocina desde los 17 años.',
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
    'John Guerrero, CEO de AI Chef Pro. Chef y consultor gastronómico: en cocina desde los 17 años y asesorando negocios desde 2010. Ha sido chef propietario y ha dirigido operaciones de grupos de restauración. Ha diseñado sistemas operativos y checklists para cientos de restaurantes, pastelerías y obradores. Más en johnguerrero.es.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 13 plantillas del kit, recibirás estos dos recursos adicionales — valorados en €16',
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
      a: 'Los 9 checklists vienen pre-rellenados con las tareas reales de una pastelería / obrador: solo tienes que ajustar tareas a tu negocio, borrar las que no apliquen y añadir las específicas de tu obrador. Los 4 registros (producción y mermas, encargos, alérgenos y temperaturas) se entregan listos para rellenar con tus datos; la matriz de alérgenos trae más de 30 productos de partida que debes verificar con tus recetas y proveedores. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye tareas de producción artesanal (croissants, tartas, pan)?',
      a: 'Sí. Las partidas de producción cubren masas de bollería (croissant, brioche, danesa), masas de pan artesano, masas quebradas, cremas y rellenos (pastelera, ganache, mousse), decoración y montaje de vitrina.',
    },
    {
      q: '¿Sirve para una pastelería pequeña y para un obrador grande?',
      a: 'Sí. Las plantillas son escalables. Una pastelería pequeña puede usar las tareas de obrador y vitrina. Un obrador industrial puede usar todas las partidas de producción, el control de encargos (ficha imprimible, registro mensual y agenda de entregas) y el plan de producción semanal.',
    },
    {
      q: '¿Qué incluye la versión 2.0?',
      a: 'La versión 2.0 amplía el kit a 13 checklists operativos + 2 bonus. Se suman cuatro plantillas nuevas: el plan de producción semanal con control de mermas en porcentaje y en euros, el control de encargos (ficha imprimible, registro mensual y agenda de entregas), la matriz de alérgenos de vitrina con los 14 de declaración obligatoria (con carta, cartel y etiquetas) y el registro de temperaturas con recepción de mercancía y etiquetas de elaborado. Además, la apertura y el cierre del negocio se han reescrito para una pastelería con tienda y todas las plantillas llevan la impresión A4 ya configurada.',
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
      '13 checklists operativos + 2 bonus para pastelería por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre del obrador y de la tienda',
      'Partidas: masas, fermentación, cremas, mousse, decoración',
      'Control de producción: temperaturas, tiempos, FIFO',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: jefe pastelero, oficial, ayudante, dependiente',
      'Eventos: Navidad, Reyes, San Valentín, Semana Santa, comuniones, Todos los Santos',
      'Plan de producción semanal con control de mermas',
      'Fichas y registro de encargos',
      'Matriz de alérgenos de vitrina (14 UE) con cartel y etiquetas',
      'Registro de temperaturas y recepción de mercancía',
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
        role: 'Chef Pâtissier, hotel boutique en Valencia',
        text: 'En un hotel con buffet de desayuno y pastelería de tarde necesitas que todo esté listo a tiempo. Los checklists de apertura por turno eliminaron los olvidos del equipo de noche.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Ana Belén Torres',
        role: 'Propietaria, Macarons & Co',
        text: 'Las tareas de control de vitrina y etiquetado de alérgenos son oro. Tener el registro firmado cada día nos ordenó el control de vitrina y el etiquetado.',
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
        role: 'Ayudante de Pastelería, obrador industrial en Barcelona',
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
        role: 'Formador de Pastelería, escuela de pastelería en Barcelona',
        text: 'Recomiendo este kit a todos mis alumnos que van a abrir su propio obrador. Las tareas de producción están perfectamente estructuradas por partida. Es el estándar que debería tener toda pastelería.',
        avatar: '/avatars/chef-avatar-3.jpg',
      },
    ],
  },

  pricing: {
    price: '€12',
    heroNote: 'Pago único · acceso de por vida · actualizaciones incluidas',
    buyBoxNote: 'Pago único. Sin suscripción: descarga, imprime y úsalo en tu obrador desde hoy',
    bonusTotalLabel: 'Kit completo: 13 plantillas + 2 bonus',
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

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-pasteleria',
    label: '¿Ya compraste el Kit de Tareas Pastelería? Vuelve a entrar al dashboard',
  },
};

export default data;
