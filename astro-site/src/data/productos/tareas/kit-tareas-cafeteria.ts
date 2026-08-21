// astro-site/src/data/productos/tareas/kit-tareas-cafeteria.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasCafeteria.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-cafeteria/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-cafeteria.ts  (marquee de testimonios)
// NO parafrasear.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-cafeteria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_CAFETERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Cafetería / Brunch | AI Chef Pro',
    description:
      '9 checklists operativos pre-rellenados para cafetería y brunch: apertura, cierre, barista, vitrina, brunch, terraza, manager y eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist cafetería, tareas barista, checklist apertura cafetería, lista tareas brunch, checklist manager cafetería, tareas recurrentes hostelería, vitrina pastelería checklist, plantilla tareas cafetería, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-cafeteria.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Cafetería / Brunch',
    productDescription:
      '9 checklists operativos pre-rellenados para cafetería y brunch: apertura, cierre, barista, vitrina, brunch dominical, terraza, manager, eventos y festivos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '10', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Carlos Mendoza',
        rating: '5',
        body: 'Desde que usamos el checklist de barista, la calibración del molinillo es consistente cada mañana. La calidad del espresso mejoró muchísimo.',
      },
      {
        author: 'Laura Serrano',
        rating: '5',
        body: 'Gestionar la apertura de una cafetería con terraza y obrador era un caos. Los checklists por zona nos organizaron desde el día uno.',
      },
      {
        author: 'Andrés Gallego',
        rating: '5',
        body: 'El brunch dominical era siempre un estrés. Con el checklist pre-brunch ahora todo fluye sin que yo tenga que repetir nada.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para cafetería?',
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una cafetería / brunch. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico de tu local.',
      },
      {
        q: '¿Incluye tareas específicas de barista?',
        a: 'Sí. Checklist completo de barista: calibración de molinillo, purga de grupo, limpieza de vaporizador, stock de leches vegetales y más.',
      },
      {
        q: '¿En qué se diferencia de Trail?',
        a: 'Trail cobra €60-75/mes por local. Este kit da las mismas listas en Excel por €12, pago único. Sin suscripción, sin internet.',
      },
      {
        q: '¿Puedo usarlo en varias cafeterías?',
        a: 'Sí. Licencia personal para todos los establecimientos que gestiones.',
      },
      {
        q: '¿Incluye tareas para brunch y eventos?',
        a: 'Sí. Checklists para brunch dominical, eventos especiales, pop-ups, San Valentín, Navidad, apertura y cierre de terraza.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Cafetería / Brunch',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-cafeteria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-barista.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-terraza.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-inventario.jpg',
    ],
    // ContentGrid usa un strip DISTINTO al del hero (empieza en barista, termina en equipo).
    gridGallery: [
      '/lovable-uploads/ai-gallery/tareas-cafeteria-barista.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-brunch.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-terraza.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-inventario.jpg',
      '/lovable-uploads/ai-gallery/tareas-cafeteria-equipo.jpg',
    ],
    // QUIRK DE DATOS EN LA SPA (portado verbatim, no estructural): WhySection usa un fondo
    // que NO es de cafetería (imagen de cochinillo asado), y CtaFinal usa el mismo fondo
    // equivocado ya detectado en kit-tareas-cafeteria por el producto de referencia
    // (falso-risotto-semillas-plancton.jpeg). BuyBox usa gambas al ajillo. Los 3 son
    // imágenes "genéricas" reutilizadas de la galería global, no de esta línea de producto.
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badge: 'Lo que Trail cobra €60/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Cafetería / Brunch — Checklists Operativos por Turno, Área y Perfil',
    description:
      '9 plantillas Excel pre-rellenadas con todas las tareas de tu cafetería: apertura, cierre, barista, vitrina, brunch, terraza, manager y eventos. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'Checklists de apertura y cierre: barra, sala, terraza, cocina',
      'Tareas del barista: calibración, limpieza, latte art, stock leches',
      'Control de vitrina de pastelería y brunch dominical',
      'Tareas del manager: diario, semanal y mensual',
      'Plantilla en blanco personalizable + briefing de servicio',
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS CAFETERÍA — €12',

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de una cafetería / brunch. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre',
        desc: '6 checklists: apertura y cierre de barra, sala y terraza/cocina. Cada tarea con responsable, hora límite y firma. ~80 tareas pre-rellenadas.',
      },
      {
        icon: 'Coffee',
        title: 'Tareas del Barista',
        desc: 'Calibración de molinillo, purga de grupo, limpieza de vaporizador, latte art del día, stock de leches vegetales, control de temperatura de tazas.',
      },
      {
        icon: 'ClipboardList',
        title: 'Tareas del Manager',
        desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Checklists personalizados para: barista jefe, barista, encargado de sala, camarero y responsable de cocina/obrador.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de equipos (cafetera, horno, vitrina).',
      },
      {
        icon: 'PartyPopper',
        title: 'Eventos y Festivos',
        desc: 'Checklist pre-evento (48h→día), brunch especial de festivos, pop-ups de temporada, apertura y cierre de terraza.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por franja horaria, por área, por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Servicio',
        desc: 'Plantilla de briefing pre-servicio: reservas, platos del día, alérgenos, equipo del turno. Imprime y pega en barra.',
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
        title: 'Pre-Rellenadas para Cafetería',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de una cafetería/brunch. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'Coffee',
        title: 'Tareas Específicas de Barista',
        desc: 'Calibración de molinillo, purga de grupo, control de vitrina, stock de leches vegetales. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Delegación con Firma',
        desc: "Imprime el checklist, entrégalo al responsable. Cuando termine, firma y archiva. Fin de las excusas de 'no sabía que tenía que hacerlo'.",
      },
      {
        icon: 'RefreshCw',
        title: 'Trail Cobra €60/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan las cafeterías con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes y cafeterías.',

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
        desc: 'La reunión de 5 minutos que separa a las cafeterías buenas de las excelentes. Reservas, sugerencias del día, alérgenos, equipo del turno.',
        image: '/lovable-uploads/ai-gallery/tareas-cafeteria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas Especiales',
        value: '€9',
        desc: '17 fechas clave de hostelería (San Valentín, Navidad, Semana Santa, terraza) con tareas y antelación recomendada.',
        image: '/lovable-uploads/ai-gallery/tareas-cafeteria-terraza.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu cafetería, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para cafetería?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una cafetería / brunch. Solo tienes que personalizar: ajustar tareas a tu local, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Incluye tareas específicas de barista?',
      a: 'Sí. Hay un checklist completo de barista: calibración de molinillo, purga de grupo, limpieza de vaporizador, control de temperatura de tazas, stock de leches vegetales, latte art del día y más.',
    },
    {
      q: '¿Funcionan con Google Sheets?',
      a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets. Pero la idea es imprimirlos en A4 — son checklists operativos diseñados para tener en la barra o cocina, no en una pantalla.',
    },
    {
      q: '¿En qué se diferencia de Trail u otros sistemas?',
      a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Puedo usarlo en varias cafeterías?',
      a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de cafeterías y consultores.',
    },
    {
      q: '¿Incluye tareas para brunch y eventos?',
      a: 'Sí. Hay checklists específicos para brunch dominical, eventos especiales (pop-ups, catas), San Valentín, Navidad/Nochevieja, apertura y cierre de temporada de terraza.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Día',
    subtitle: '9 checklists operativos para cafetería por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: barra, sala, terraza, cocina',
      'Tareas específicas del barista: calibración, limpieza, stock',
      'Control de vitrina de pastelería y brunch dominical',
      'Checklist diario, semanal y mensual del manager',
      'Tareas por perfil: barista, encargado, camarero, cocina',
      'Eventos y festivos: brunch especial, pop-ups, terraza',
      'BONUS: Briefing de Servicio (€7)',
      'BONUS: Calendario Anual de Tareas (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle: 'Baristas, encargados y dueños de cafetería que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Carlos Mendoza',
        role: 'Barista Jefe, Café Arábica',
        text: 'Antes cada barista hacía la calibración del molinillo a su manera. Con el checklist de barista, ahora todos siguen el mismo protocolo cada mañana. La consistencia del espresso ha mejorado muchísimo.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Laura Serrano',
        role: 'Encargada, La Cafetería del Mercado',
        text: 'Gestionar la apertura de una cafetería con terraza y obrador era un caos. Desde que imprimimos los checklists de apertura por zona, el equipo sabe exactamente qué hacer antes de abrir puertas.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Miguel Ángel Ruiz',
        role: 'Dueño, Coffee Lab Barcelona',
        text: 'Abrí mi coffee shop hace 8 meses y me olvidaba de todo: purgar el grupo, revisar la vitrina, reponer leches vegetales. Con estas checklists reduje los olvidos un 90%. Literalmente me salvaron.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Pastelera y Socia, Dulce Brunch',
        text: 'El checklist de control de vitrina de pastelería es increíble. Rotación FIFO, temperaturas, etiquetado de alérgenos... todo en un A4 que pegamos dentro de la vitrina. Cero desperdicios desde entonces.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Andrés Gallego',
        role: 'Gerente, Brunch & Co.',
        text: 'El brunch dominical era siempre un estrés. Con el checklist pre-brunch (48h antes, día anterior, mañana) ahora todo fluye. El equipo prepara mise en place, decora y monta buffet sin que yo tenga que repetir nada.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Sofía Montero',
        role: 'Directora de Operaciones, Grupo Café Central',
        text: 'Tenemos 4 cafeterías y antes cada encargada hacía las cosas diferente. Ahora con los checklists hemos estandarizado la operación en los 4 locales. El onboarding de personal nuevo pasó de 2 semanas a 3 días.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Javier Reyes',
        role: 'Dueño, Tostadores Artesanos',
        text: 'Solo la plantilla de briefing pre-servicio ya vale el precio. Antes no hacíamos briefing. Ahora en 5 minutos repasamos sugerencias del día, alérgenos, reservas y equipo. El servicio sale mucho mejor preparado.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Rodrigo Espinosa',
        role: 'Barista y Formador',
        text: 'Como formador de baristas, recomiendo este kit a todos mis alumnos. Las tareas de calibración, limpieza y mantenimiento de la cafetera están perfectamente estructuradas. Es lo que debería tener toda cafetería.',
        avatar: '/avatars/avatar-8.jpg',
      },
      {
        name: 'Diego Navarro',
        role: 'Chef Pastelero, Café Gourmand',
        text: 'El checklist semanal del manager es mi herramienta favorita. Controlo pedidos a proveedores, rotación de vitrinas, limpieza profunda y formación del equipo en un solo documento. Todo organizado por día.',
        avatar: '/avatars/chef-avatar-1.jpg',
      },
      {
        name: 'Pablo Ibáñez',
        role: 'Consultor de Cafeterías de Especialidad',
        text: 'Lo primero que hago con cada cliente nuevo es entregarle estas checklists. Les pone orden desde el día uno. Apertura, cierre, barista, vitrina... cubren el 95% de lo que necesita cualquier cafetería.',
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
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  alreadyBought: {
    product: 'kit-tareas-cafeteria',
    label: '¿Ya compraste el Kit de Tareas Cafetería? Vuelve a entrar al dashboard',
  },
};

export default data;
