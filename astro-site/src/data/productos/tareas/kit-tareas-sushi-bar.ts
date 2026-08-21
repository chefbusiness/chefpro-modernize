// astro-site/src/data/productos/tareas/kit-tareas-sushi-bar.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasSushiBar.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-sushi-bar/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-sushi-bar.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-sushi-bar',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_SUSHI_BAR',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Sushi Bar — Checklists Operativos con Protocolo Anisakis | AI Chef Pro',
    description:
      '11 checklists operativos para sushi bar: barra sushi, arroz con control pH, protocolo anisakis APPCC obligatorio (RD 1420/2006), vitrina neta case, perfiles itamae, temporadas pescado y omakase. Solo €14.',
    keywords:
      'checklist sushi bar, tareas sushi bar, protocolo anisakis APPCC, control pH arroz sushi, vitrina neta case, itamae checklist, restaurante japonés operativa, RD 1420/2006, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-sushi-bar.jpg',
  },

  schema: {
    productName:
      'Kit de Tareas Recurrentes: Sushi Bar — Checklists Operativos con Protocolo Anisakis',
    productDescription:
      '11 checklists operativos pre-rellenados para sushi bar: barra sushi, preparación arroz con control pH, protocolo anisakis APPCC obligatorio, vitrina neta case, perfiles itamae, temporadas pescado y omakase.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Los checklists de barra sushi son muy completos. Neta case, arroz, cuchillería japonesa, rotación FIFO… todo el equipo sigue el mismo estándar.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El protocolo de anisakis con registro de congelación a -20 ºC durante 7 días nos ha salvado en dos inspecciones de Sanidad. Imprescindible.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Implementamos en 3 locales. La consistencia en preparación de arroz (control pH ≤4.6) y corte de pescado es ahora uniforme.',
      },
    ],
    faqs: [
      {
        q: '¿Incluye el protocolo de anisakis obligatorio por ley?',
        a: 'Sí. Registro de congelación a -20 ºC durante 7 días por lote y proveedor, control de temperaturas y trazabilidad completa del pescado. Cumple con el RD 1420/2006.',
      },
      {
        q: '¿Sirve para mi tipo de restaurante japonés?',
        a: 'Sí. Sushi bar tradicional, japonés con cocina caliente, nikkei, kaiten, omakase y cualquier local que sirva pescado crudo. 100% editable.',
      },
      {
        q: '¿Incluye preparación de arroz sushi profesional?',
        a: 'Sí. Lavado, cocción, sazonado con sushi-zu, control de pH obligatorio (≤4.6), tiempos de descarte y temperaturas de servicio.',
      },
      {
        q: '¿Qué es la vitrina neta case?',
        a: 'La vitrina refrigerada de la barra de sushi (2-4 ºC). El kit incluye montaje, rotación FIFO y exposición máxima de 2 horas.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Sushi Bar',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-arroz.jpg',
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-corte.jpg',
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-sushi-bar-emplatado.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-sushi-bar-barra.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-sushi-bar-emplatado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-sushi-bar-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €14 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Sushi Bar — Checklists Operativos con Protocolo Anisakis',
    description:
      '11 checklists Excel pre-rellenados para sushi bar y restaurante japonés: barra sushi, preparación de arroz con control de pH, protocolo anisakis APPCC obligatorio por ley, vitrina neta case, perfiles itamae, temporadas de pescado y omakase. Imprime, organiza y cumple Sanidad.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Protocolo anisakis APPCC obligatorio (RD 1420/2006) con registro -20 ºC / 7 días',
      'Preparación de arroz sushi con control de pH (≤4.6) y tiempos de descarte',
      'Barra sushi y vitrina neta case (2-4 ºC) con rotación FIFO',
      'Tareas por perfil: itamae, ayudante, cocina caliente, sala',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  stickyLabel: 'KIT TAREAS SUSHI BAR — €14',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Sushi Bar',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de un sushi bar profesional. Solo ajusta a tu carta, imprime y empieza a operar con estándar Sanidad.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre Sushi',
        desc: 'Checklists de barra sushi, cocina caliente y sala: temperaturas de neta case, arroz cocido del día, pescado expuesto, cierre completo y arqueo.',
      },
      {
        icon: 'Sparkles',
        title: 'Arroz Sushi y Corte de Pescado',
        desc: 'Protocolo de arroz: lavado, cocción, sazonado con sushi-zu, control de pH (≤4.6) y tiempos de descarte. Técnicas de corte: yanagiba, sashimi, nigiri y maki.',
      },
      {
        icon: 'ShieldCheck',
        title: 'Seguridad Anisakis y APPCC',
        desc: 'Registro de congelación a -20 ºC durante 7 días por lote (RD 1420/2006), control de temperaturas, alérgenos y trazabilidad completa de pescado y proveedores.',
      },
      {
        icon: 'Refrigerator',
        title: 'Barra Sushi y Vitrina Neta Case',
        desc: 'Mise en place de la vitrina refrigerada (2-4 ºC), rotación FIFO por lotes, exposición máxima de 2 horas, organización de la estación itamae y limpieza por turno.',
      },
      {
        icon: 'Briefcase',
        title: 'Tareas del Manager',
        desc: 'Pedidos a lonja, control de stock de pescado, gestión del equipo, reservas (incluido omakase), revenue diario, comparativa de proveedores y reporting.',
      },
      {
        icon: 'Users',
        title: 'Perfiles: Itamae y Equipo',
        desc: 'Tareas claras por perfil: itamae, ayudante de sushi, cocina caliente, sala y servicio, delivery. Roles y responsabilidades sin solapes.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Cuchillería japonesa (afilado yanagiba, deba), limpieza profunda de neta case, stock de productos secos, formación del equipo y revisión de proveedores.',
      },
      {
        icon: 'CalendarDays',
        title: 'Eventos y Temporadas',
        desc: 'Calendario de temporadas de pescado en España (atún rojo, bonito, salmón salvaje), omakases especiales, Nochevieja, San Valentín y festivos asiáticos.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para que crees checklists a medida del concepto exacto de tu sushi bar (omakase, kaiten, takeaway, fusión nikkei).',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing de Servicio',
        desc: 'Briefing pre-servicio de 5 minutos: pescado del día, alérgenos críticos, VIPs, omakase, stock disponible y avisos para itamae y sala.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con temporadas de pescado, festivos asiáticos, mantenimientos de equipos, formación del equipo y cierres por vacaciones.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010 y experiencia en cocina japonesa.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñados para Sushi Bar',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de un sushi bar: barra abierta a sala, neta case, itamae con cuchillería japonesa.',
      },
      {
        icon: 'Fish',
        title: 'Anisakis APPCC Cumplido',
        desc: 'Registro de congelación a -20 ºC durante 7 días por lote, conforme al RD 1420/2006. Si Sanidad pide auditoría, tienes todo documentado por proveedor y partida.',
      },
      {
        icon: 'Thermometer',
        title: 'pH del Arroz Bajo Control',
        desc: 'Protocolo de arroz con control de pH (≤4.6), tiempos de descarte y temperaturas. Lo que diferencia un sushi bar profesional de uno aficionado.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €14',
        desc: 'Las mismas listas de tareas que usan sushi bars con software premium, pero en Excel por un pago único. Sin suscripción, sin tablets, ilimitado en clientes.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a sushi bars y restaurantes japoneses en la profesionalización de su operativa, especialmente en cumplimiento de protocolo anisakis APPCC y control de calidad de arroz.',

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
        desc: 'Briefing pre-servicio de 5 minutos: pescado del día por proveedor, alérgenos críticos, VIPs y reservas omakase, stock disponible y avisos para itamae y sala. La hoja que alinea al equipo cada turno.',
        image: '/lovable-uploads/ai-gallery/tareas-sushi-bar-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: '12 meses con temporadas de pescado en España (atún rojo, bonito del norte, salmón salvaje), festivos asiáticos, mantenimientos de equipos (vitrina, máquinas de arroz), formación del equipo y cierres por vacaciones.',
        image: '/lovable-uploads/ai-gallery/tareas-sushi-bar-arroz.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS SUSHI BAR — €14',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu sushi bar y cumplir el protocolo anisakis APPCC, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Incluye el protocolo de anisakis obligatorio por ley?',
      a: 'Sí. El kit incluye un checklist específico con registro de congelación a -20 ºC durante 7 días por lote y proveedor, control de temperaturas y trazabilidad completa del pescado. Cumple con el RD 1420/2006 vigente y te deja todo documentado para auditorías de Sanidad.',
    },
    {
      q: '¿Sirve para mi tipo de restaurante japonés?',
      a: 'Sí. Las plantillas cubren sushi bar tradicional, restaurante japonés con cocina caliente, nikkei (fusión peruano-japonesa), kaiten, omakase y cualquier local que sirva pescado crudo. Todo es 100% editable para adaptar a tu carta y formato.',
    },
    {
      q: '¿Incluye preparación de arroz sushi profesional?',
      a: 'Sí. Protocolo completo de arroz: lavado, cocción, sazonado con sushi-zu, control de pH obligatorio (≤4.6 según APPCC), tiempos de descarte y temperaturas de servicio. Es lo que diferencia un sushi bar profesional de uno amateur.',
    },
    {
      q: '¿Qué es la vitrina neta case?',
      a: 'Es la vitrina refrigerada de la barra de sushi donde se exponen las piezas de pescado a la vista del cliente. El kit incluye checklist específico de montaje, rotación FIFO por lotes, control de temperatura (2-4 ºC) y exposición máxima de 2 horas.',
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
    heading: 'Tu Sushi Bar a Estándar Sanidad — En 11 Checklists',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu sushi bar: arroz, pescado, anisakis, neta case, perfiles. Por menos de lo que cuesta un omakase básico.',
    items: [
      'Apertura y cierre completo de barra sushi, cocina y sala',
      'Preparación de arroz con control de pH (≤4.6) y técnicas de corte',
      'Protocolo anisakis APPCC: -20 ºC / 7 días por lote, RD 1420/2006',
      'Vitrina neta case (2-4 ºC), rotación FIFO y mise en place itamae',
      'Tareas por perfil: itamae, ayudante, cocina caliente, sala, delivery',
      'Calendario anual de pescado, omakases y festivos asiáticos',
      'BONUS: Briefing de Servicio (€15)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS SUSHI BAR — €14',
  },

  testimonials: {
    subtitle:
      'Itamaes, propietarios de sushi bar y consultores que ya tienen su operativa bajo control',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Itamae, Sushi Bar Madrid',
        text: 'Los checklists de barra sushi son muy completos. Neta case, arroz, cuchillería japonesa, rotación FIFO… todo el equipo sigue el mismo estándar. Antes cada turno hacía las cosas a su manera.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Propietaria Restaurante Japonés, Valencia',
        text: 'El protocolo de anisakis con registro de congelación a -20 ºC durante 7 días nos ha salvado en dos inspecciones de Sanidad. Lo tenemos todo documentado por lote y por proveedor. Imprescindible.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director Cadena Sushi (3 locales)',
        text: 'Implementamos los checklists en los 3 locales. La consistencia en preparación de arroz (control de pH ≤4.6) y corte de pescado es ahora uniforme. El cliente percibe la misma calidad esté donde esté.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Jefa de Sala Sushi Bar, Bilbao',
        text: 'Las tareas por perfil clarifican quién hace qué: itamae, ayudante, cocina caliente, sala. El briefing pre-servicio con el pescado del día y los VIPs es genial para alinear al equipo en 5 minutos.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Consultor Hostelero especializado en restaurantes japoneses',
        text: 'Para sushi bars es el kit más completo del mercado. Anisakis, arroz, vitrina neta case, perfiles, omakase, temporadas de pescado… cubre todos los puntos críticos en los que los locales suelen fallar.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Encargada Sushi-Fusion Bar, Sevilla',
        text: 'El calendario con las temporadas de pescado en España nos permite planificar la carta con antelación: atún rojo en primavera, bonito del norte en verano… ya no improvisamos.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Ayudante Sushi en formación',
        text: 'Las tareas del ayudante están muy claras: arroz, bamboo mats, reposición de neta case, mise en place. Sé exactamente qué hacer en cada momento sin que el itamae tenga que estar dirigiéndome.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Chef Ejecutivo Nikkei, Marbella',
        text: 'El control de pH del arroz y la trazabilidad del pescado por lotes son detalles que marcan la diferencia profesional. Lo hemos integrado en nuestro APPCC y nos ha pasado de "improvisado" a "auditable".',
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
    product: 'kit-tareas-sushi-bar',
    label: '¿Ya compraste el Kit de Tareas Sushi Bar? Vuelve a entrar al dashboard',
  },
};

export default data;
