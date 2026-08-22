// astro-site/src/data/productos/tareas/kit-tareas-restaurante-creativo.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasRestauranteCreativo.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-restaurante-creativo/*.tsx  (Hero, ContentGrid, WhySection,
//     AuthorSection, BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-restaurante-creativo.ts  (marquee de testimonios)
// NO parafrasear. QUIRK: la SPA de este producto omite tildes/ñ en gran parte del copy
// (p.ej. "gestion", "degustacion", "anos", "disenado") de forma INCONSISTENTE — algunas
// frases sí llevan tilde (los checkItems del hero, el título "Software de Gestión Cobra..."
// de WhySection). Se porta tal cual, sin homogeneizar ni corregir ortografía.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-restaurante-creativo',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_RESTAURANTE_CREATIVO',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor | AI Chef Pro',
    description:
      '11 checklists operativos pre-rellenados para restaurante creativo y de autor: I+D, menu degustacion, brigada creativa, sumiller, eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist restaurante creativo, tareas restaurante de autor, checklist menu degustacion, mise en place fine dining, checklist sumiller, tareas brigada cocina creativa, plantilla tareas chef ejecutivo, checklist I+D cocina, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-restaurante-creativo.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor',
    productDescription:
      '11 checklists operativos pre-rellenados para restaurante creativo: I+D, menu degustacion, brigada creativa, sumiller y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alberto Riera',
        rating: '5',
        body: 'El checklist de mise en place para degustacion me cambio la vida. Cada pase documentado con timing, temperaturas y responsable.',
      },
      {
        author: 'Marina Delgado',
        rating: '5',
        body: 'La plantilla de I+D es increible. Fichas tecnicas, pruebas de concepto, evaluacion sensorial... por fin tengo un sistema.',
      },
      {
        author: 'Patricia Vega',
        rating: '5',
        body: 'Lo primero que hago con cada cliente de restaurante creativo es entregarle estos checklists. Cubren el 95% de lo que necesita.',
      },
    ],
    faqs: [
      {
        q: '¿Las tareas vienen ya rellenadas para restaurante creativo?',
        a: 'Si. Cada checklist viene pre-rellenado con las tareas reales de un restaurante creativo o de autor: I+D, degustacion, brigada, sumiller y eventos. Solo personaliza: ajustar, borrar lo que no aplique y anadir lo especifico.',
      },
      {
        q: '¿Cubre I+D y desarrollo de menu?',
        a: 'Si. Fichas tecnicas de nuevos platos, pruebas de concepto, evaluacion sensorial, costes I+D y registro fotografico.',
      },
      {
        q: '¿En que se diferencia del software de gestion?',
        a: 'El software de gestion cobra €40/mes por local. Este kit da las mismas listas en Excel por €12, pago unico.',
      },
      {
        q: '¿Hay garantia de devolucion?',
        a: '30 dias de garantia completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Restaurante Creativo / De Autor',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-emplatado.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-id.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-sumiller.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-chefstable.jpg',
      '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-emplatado.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestion cobra €40/mes, tu lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Restaurante Creativo / De Autor — Checklists por Turno, Partida y Perfil',
    description:
      '11 plantillas Excel pre-rellenadas para tu restaurante creativo o de autor: I+D, mise en place degustacion, brigada creativa, sumiller, eventos y mas. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'I+D y desarrollo de menú: fichas técnicas, pruebas, evolución de platos',
      'Menú degustación: mise en place, timing de pases, servicio de sala',
      'Brigada creativa: chef ejecutivo, sous-chef, jefe de partida, pastelero',
      'Sumiller y maridajes: carta de vinos, catas, servicio de bodega',
      "Eventos: chef's table, cenas maridaje, showcookings, prensa",
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS RESTAURANTE CREATIVO — €12',

  grid: {
    countGold: '11',
    headingRest: ' Plantillas de Tareas Operativas',
    subtitle:
      'Cada plantilla viene pre-rellenada con las tareas reales de un restaurante creativo o de autor. Solo ajusta, imprime y delega.',
    templates: [
      {
        icon: 'ChefHat',
        title: 'Apertura y Cierre',
        desc: 'Checklists completos: cocina, pass, sala, bodega, mise en place degustacion, cierre administrativo. ~40 tareas pre-rellenadas para fine dining.',
      },
      {
        icon: 'Beaker',
        title: 'Mise en Place Degustacion',
        desc: 'Checklist de preparacion de cada pase del menu degustacion: bases, salsas, guarniciones, pre-emplatado, temperaturas y timing de servicio.',
      },
      {
        icon: 'FlaskConical',
        title: 'I+D y Desarrollo de Menu',
        desc: 'Fichas tecnicas de nuevos platos, pruebas de concepto, evaluacion sensorial, costes I+D, registro fotografico y evolucion de la carta.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Brigada Creativa',
        desc: 'Checklists para: chef ejecutivo, sous-chef, jefe de partida, commis, chef pastelero creativo y stagiaire. Cada puesto sabe que hacer.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Deep clean de cocina, revision de maquinaria, inventario semanal (premium, fresco, seco), reunion creativa, actualizacion de carta.',
      },
      {
        icon: 'Wine',
        title: 'Sumiller y Maridajes',
        desc: 'Gestion de bodega, carta de vinos, maridajes por pase, servicio de sumilleria, catas para equipo, temperaturas de servicio.',
      },
      {
        icon: 'Sparkles',
        title: "Chef's Table y Eventos",
        desc: "Chef's table, cenas maridaje, showcookings, prensa y criticos, pop-ups y colaboraciones entre chefs.",
      },
      {
        icon: 'Camera',
        title: 'Fotografia y Storytelling',
        desc: 'Sesion de fotos de platos, contenido para RRSS, storytelling del menu, documentacion de procesos creativos.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas en blanco (por partida, por turno y por perfil) para crear tus propias listas de tareas.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Diario de Servicio',
        desc: 'La reunion de 5 minutos antes de abrir: menu del dia, alergias confirmadas, VIPs, cambios de carta, timing de pases.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual de Eventos y Carta',
        desc: '15+ fechas clave: cambios estacionales de carta, eventos gastronomicos, guias, premios, temporadas de producto.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Que Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genericas. Son checklists disenados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010 y restauracion creativa.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Cocina Creativa',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un restaurante creativo: I+D, degustacion, emplatado, bodega. Solo ajusta, borra lo que no aplique y anade lo que te falte.',
      },
      {
        icon: 'FlaskConical',
        title: 'I+D + Servicio Cubiertos',
        desc: 'Desarrollo de nuevos platos, fichas tecnicas, pruebas de concepto, mise en place de degustacion, timing de pases y servicio de sala. Las tareas que los sistemas genericos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Perfiles Especificos de Brigada Creativa',
        desc: 'Checklists para chef ejecutivo, sous-chef, jefe de partida, commis, chef pastelero creativo y stagiaire. Cada puesto sabe exactamente que hacer.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan restaurantes con estrella con SaaS premium, pero en Excel por un pago unico. Sin suscripcion.',
      },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de calculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha disenado sistemas operativos y checklists para cientos de restaurantes creativos y de autor.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Ademas de las 9 plantillas, recibiras estos recursos adicionales — valorados en €18',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Diario de Servicio',
        value: '€9',
        desc: 'La reunion de 5 minutos antes de abrir: menu del dia, alergias confirmadas, VIPs, cambios de carta, timing de pases, asignacion de rangos de sala.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Eventos y Carta',
        value: '€9',
        desc: '15+ fechas clave: cambios estacionales de carta, eventos gastronomicos (guias, premios), temporadas de producto premium, jornadas tematicas y pop-ups.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-chefstable.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SI, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu restaurante creativo, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Dias de garantia' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incomodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para restaurante creativo?',
      a: 'Si. Cada checklist viene pre-rellenado con las tareas reales de un restaurante creativo o de autor: I+D de platos, mise en place de degustacion, brigada creativa, sumiller y eventos. Solo tienes que personalizar: ajustar tareas a tu negocio, borrar las que no apliquen y anadir las especificas. Las celdas editables estan marcadas en verde.',
    },
    {
      q: '¿Cubre I+D y desarrollo de menu?',
      a: 'Si. Incluye una plantilla completa de I+D: fichas tecnicas de nuevos platos, pruebas de concepto, evaluacion sensorial, costes de investigacion, registro fotografico y seguimiento de la evolucion de la carta.',
    },
    {
      q: '¿Incluye tareas de sumiller y bodega?',
      a: 'Si. Una plantilla entera dedicada al sumiller: gestion de bodega, carta de vinos, maridajes por pase del menu degustacion, servicio de sumilleria, catas para equipo, temperaturas de servicio y control de stock de referencias premium.',
    },
    {
      q: '¿Es solo para fine dining o sirve para cocina creativa casual?',
      a: 'Sirve para ambos. Las plantillas son escalables: un restaurante con menu degustacion de 12 pases puede usar todas. Un bistro creativo con carta corta puede simplificar y quedarse con apertura/cierre, brigada y periodicas. Adapta lo que necesites.',
    },
    {
      q: '¿En que se diferencia del software de gestion?',
      a: 'El software de gestion cobra €40/mes por local y requieren tablets/moviles. Este kit te da las mismas listas de tareas en Excel por €12, pago unico. Sin suscripcion, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Hay garantia de devolucion?',
      a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle: '11 checklists operativos para restaurante creativo por menos de lo que cuesta una hora de consultoria.',
    items: [
      'Checklists de apertura y cierre: cocina, pass, sala, bodega',
      'Mise en place degustacion: bases, salsas, timing de pases',
      'I+D y desarrollo de menu: fichas tecnicas, pruebas, costes',
      'Tareas por brigada creativa: chef ejecutivo, sous-chef, jefe de partida',
      'Semanales y mensuales: deep clean, inventario, reunion creativa',
      'Sumiller y maridajes: bodega, carta de vinos, catas',
      "Chef's table y eventos: cenas maridaje, showcookings, prensa",
      'Fotografia y storytelling: sesion de fotos, contenido RRSS',
      'BONUS: Briefing Diario de Servicio (€9)',
      'BONUS: Calendario Anual de Eventos y Carta (€9)',
    ],
    ctaLabel: 'SI, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle:
      'Chefs ejecutivos, sous-chefs, sumilleres y gerentes de restaurante creativo que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Alberto Riera',
        role: 'Chef ejecutivo, restaurante con estrella Michelin',
        text: 'El checklist de mise en place para degustacion me cambio la vida. Cada pase documentado con timing, temperaturas y responsable. Mi sous-chef ya no necesita preguntarme nada, todo esta en la plantilla.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Marina Delgado',
        role: 'Sous-chef, restaurante degustacion 2 estrellas',
        text: 'La plantilla de I+D es increible. Fichas tecnicas, pruebas de concepto, evaluacion sensorial... por fin tengo un sistema para documentar toda la investigacion que hacemos en cocina.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Fernando Casas',
        role: 'Sumiller, restaurante gastronomico',
        text: 'Por fin un checklist que entiende el trabajo del sumiller: gestion de bodega, maridajes por pase, temperaturas de servicio, catas de equipo. Los agentes IA genericos no cubren ni el 20% de esto.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Lucia Navarro',
        role: 'Jefa de sala, restaurante de autor',
        text: 'El briefing diario de servicio lo usamos antes de cada pase. VIPs, alergias, cambios de carta, rangos de sala... en 5 minutos todo el equipo esta alineado. Imprescindible para fine dining.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Carlos Iniesta',
        role: 'Chef propietario de 2 restaurantes creativos',
        text: 'Tengo dos restaurantes creativos y cada sous-chef hacia las cosas a su manera. Con los checklists estandarizados, la calidad es la misma en ambos. El onboarding de stagiaires paso de 2 semanas a 4 dias.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Consultora gastronomica, alta cocina',
        text: 'Lo primero que hago con cada cliente de restaurante creativo es entregarle estos checklists. I+D, degustacion, sumiller, eventos... cubren el 95% de lo que necesita cualquier restaurante de autor.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Diego Morales',
        role: 'Chef pastelero creativo',
        text: 'La seccion de I+D me permite documentar cada prueba de postre nuevo con costes, tiempos y evaluacion. Antes perdia ideas geniales porque no las registraba. Ahora tengo un historico completo.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Javier Ortega',
        role: 'Director de operaciones, grupo gastronomico',
        text: 'Gestionamos 4 restaurantes creativos. El calendario anual de eventos y carta nos permite planificar cambios estacionales, guias, premios y jornadas tematicas con meses de antelacion. Oro puro.',
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
    { href: '/kit-tareas-chef-privado', label: 'Kit Tareas Chef Privado' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-restaurante-creativo',
    label: '¿Ya compraste el Kit de Tareas Restaurante Creativo? Vuelve a entrar al dashboard',
  },
};

export default data;
