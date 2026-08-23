// astro-site/src/data/productos/tareas/kit-tareas-restaurante-creativo.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasRestauranteCreativo.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-restaurante-creativo/*.tsx  (Hero, ContentGrid, WhySection,
//     AuthorSection, BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-restaurante-creativo.ts  (marquee de testimonios)
// NO parafrasear. QUIRK: la SPA de este producto omite tildes/ñ en gran parte del copy
// (p.ej. "gestion", "degustacion", "anos", "disenado") de forma INCONSISTENTE. En v2.0
// (2026-08-23) la ORTOGRAFÍA SÍ SE CORRIGE aquí —regla capital: ortografía perfecta en
// contenido publicado—; la SPA queda como estaba y ya NO es byte a byte en este punto.
// El resto del copy se porta verbatim.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-restaurante-creativo',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_RESTAURANTE_CREATIVO',

  seo: {
    title:
      'Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor | AI Chef Pro',
    description:
      '11 plantillas + 2 bonus (13 ficheros): checklists operativos para restaurante creativo y de autor con 477 tareas ya escritas — I+D, menú degustación, brigada creativa, sumiller, apertura y cierre de negocio, arqueo de caja, eventos. Imprime, delega y firma. Solo €12.',
    keywords:
      'checklist restaurante creativo, tareas restaurante de autor, checklist menú degustación, mise en place fine dining, checklist sumiller, tareas brigada cocina creativa, plantilla tareas chef ejecutivo, checklist I+D cocina, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-restaurante-creativo.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes — Checklists Operativos para Restaurante Creativo / De Autor',
    productDescription:
      '11 plantillas + 2 bonus (13 ficheros): checklists operativos para restaurante creativo con 477 tareas ya escritas — I+D, menú degustación, brigada creativa, sumiller, apertura y cierre de negocio, arqueo de caja y eventos.',
    price: '12.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alberto Riera',
        rating: '5',
        body: 'El checklist de mise en place para degustación me cambió la vida. Cada pase documentado con timing, temperaturas y responsable.',
      },
      {
        author: 'Marina Delgado',
        rating: '5',
        body: 'La plantilla de I+D es increíble. Fichas técnicas, pruebas de concepto, evaluación sensorial... por fin tengo un sistema.',
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
        a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un restaurante creativo o de autor: I+D, degustación, brigada, sumiller y eventos. Solo personaliza: ajustar, borrar lo que no aplique y añadir lo específico.',
      },
      {
        q: '¿Cubre I+D y desarrollo de menú?',
        a: 'Sí. Fichas técnicas de nuevos platos, pruebas de concepto, evaluación sensorial, costes I+D y registro fotográfico.',
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
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €12 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Restaurante Creativo / De Autor — Checklists por Turno, Partida y Perfil',
    description:
      '11 plantillas + 2 bonus (13 ficheros) en Excel con 477 tareas de restaurante creativo ya escritas: I+D, mise en place degustación, brigada creativa, sumiller, apertura y cierre de negocio, arqueo de caja, eventos y más. Imprime, delega al equipo, firma y archiva.',
    checkItems: [
      'I+D y desarrollo de menú: fichas técnicas, pruebas, evolución de platos',
      'Menú degustación: mise en place, timing de pases, servicio de sala',
      'Brigada creativa: chef ejecutivo, sous-chef, jefe de partida, pastelero',
      'Sumiller y maridajes: carta de vinos, catas, servicio de bodega',
      'Apertura/cierre de negocio y arqueo de caja con recuento por denominaciones',
      "Eventos: chef's table, cenas maridaje, showcookings, prensa",
    ],
    ctaLabel: 'COMPRAR AHORA — €12',
  },

  stickyLabel: 'KIT TAREAS RESTAURANTE CREATIVO — €12',

  grid: {
    countGold: '11',
    headingRest: ' Plantillas de Tareas Operativas + 2 Bonus (13 ficheros)',
    subtitle:
      '477 tareas de restaurante creativo o de autor ya escritas y repartidas por turno, partida y perfil. Ajusta a tu local, imprime y delega.',
    templates: [
      {
        icon: 'ChefHat',
        title: 'Apertura y Cierre',
        desc: 'Checklists completos: cocina, pass, sala, bodega, mise en place degustación, cierre administrativo. 55 tareas ya escritas solo en este fichero, con higiene personal y arranque seguro (campana → gas → equipos) al inicio del turno.',
      },
      {
        icon: 'Beaker',
        title: 'Mise en Place Degustación',
        desc: 'Checklist de preparación de cada pase del menú degustación: bases, salsas, guarniciones, pre-emplatado, temperaturas y timing de servicio, con la congelación preventiva de anisakis para el pescado que se sirve crudo o semicrudo.',
      },
      {
        icon: 'FlaskConical',
        title: 'I+D y Desarrollo de Menu',
        desc: 'Fichas técnicas de nuevos platos, pruebas de concepto, evaluación sensorial, costes I+D, registro fotográfico y evolución de la carta.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Brigada Creativa',
        desc: 'Checklists para: chef ejecutivo, sous-chef, jefe de partida, commis, chef pastelero creativo y stagiaire. Cada puesto sabe qué hacer.',
      },
      {
        icon: 'CalendarDays',
        title: 'Semanales y Mensuales',
        desc: 'Deep clean de cocina, revisión de maquinaria, inventario semanal (premium, fresco, seco), reunión creativa, actualización de carta. + hoja Trimestral y Anual: DDD, extintores y BIE, conductos de extracción, gas, legionela, calibración de básculas y sondas y revisión del TPV/Verifactu, con nº de parte y firma.',
      },
      {
        icon: 'Wine',
        title: 'Sumiller y Maridajes',
        desc: 'Gestión de bodega, carta de vinos, maridajes por pase, servicio de sumillería, catas para equipo, temperaturas de servicio.',
      },
      {
        icon: 'Sparkles',
        title: "Chef's Table y Eventos",
        desc: "Chef's table, cenas maridaje, showcookings, prensa y críticos, pop-ups y colaboraciones entre chefs.",
      },
      {
        icon: 'Camera',
        title: 'Fotografía y Storytelling',
        desc: 'Sesión de fotos de platos, contenido para RRSS, storytelling del menú, documentación de procesos creativos.',
      },
      {
        icon: 'FileEdit',
        title: 'Plantilla Personalizable',
        desc: '3 plantillas maestras ya estructuradas —por franja horaria, por partida y por perfil— con 3 filas de ejemplo cada una (marcadas N/A para que no cuenten): tú solo escribes tus tareas en las celdas verdes.',
      },
      {
        icon: 'Building2',
        title: 'Apertura y Cierre de Negocio',
        desc: 'Checklist del local completo (no solo cocina): sala, bodega, TPV, accesos. 33 tareas con responsable y hora límite precargados.',
      },
      {
        icon: 'Wallet',
        title: 'Arqueo y Registro de Caja',
        desc: 'Apertura y cierre de caja con recuento por denominaciones, fondo de caja y descuadre automático frente al Z del TPV. Incluye registro mensual con descuadre por fórmula.',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing Diario de Servicio',
        desc: 'La reunión de 5 minutos antes de abrir: menú del día, alergias confirmadas, VIPs, cambios de carta, timing de pases.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual de Eventos y Carta',
        desc: 'Calendario mensual (12 meses) con las fechas clave de cada uno: cambios estacionales de carta, eventos gastronómicos, guías, premios y temporadas de producto.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años, consultor gastronómico desde 2010 y especializado en restauración creativa.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Pre-Rellenadas para Cocina Creativa',
        desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un restaurante creativo: I+D, degustación, emplatado, bodega. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
      },
      {
        icon: 'FlaskConical',
        title: 'I+D + Servicio Cubiertos',
        desc: 'Desarrollo de nuevos platos, fichas técnicas, pruebas de concepto, mise en place de degustación, timing de pases y servicio de sala. Las tareas que los sistemas genéricos no cubren.',
      },
      {
        icon: 'Users',
        title: 'Perfiles Específicos de Brigada Creativa',
        desc: 'Checklists para chef ejecutivo, sous-chef, jefe de partida, commis, chef pastelero creativo y stagiaire. Cada puesto sabe exactamente qué hacer.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €12',
        desc: 'Las mismas listas de tareas que usan restaurantes con estrella con SaaS premium, pero en Excel por un pago único. Sin suscripción.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas operativos y checklists para cientos de restaurantes creativos y de autor.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle: 'Además de las 11 plantillas, recibirás estos recursos adicionales — valorados en €18',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Diario de Servicio',
        value: '€9',
        desc: 'La reunión de 5 minutos antes de abrir: menú del día, alergias confirmadas, VIPs, cambios de carta, timing de pases, asignación de rangos de sala.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Eventos y Carta',
        value: '€9',
        desc: 'Calendario mensual (12 meses) con las fechas clave de cada uno: cambios estacionales de carta, eventos gastronomicos (guias, premios), temporadas de producto premium, jornadas tematicas y pop-ups.',
        image: '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-chefstable.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a organizar mejor las operaciones de tu restaurante creativo, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Las tareas vienen ya rellenadas para restaurante creativo?',
      a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un restaurante creativo o de autor: I+D de platos, mise en place de degustación, brigada creativa, sumiller y eventos. Solo tienes que personalizar: ajustar tareas a tu negocio, borrar las que no apliquen y añadir las específicas. Las celdas editables están marcadas en verde.',
    },
    {
      q: '¿Cubre I+D y desarrollo de menú?',
      a: 'Sí. Incluye una plantilla completa de I+D: fichas técnicas de nuevos platos, pruebas de concepto, evaluación sensorial, costes de investigación, registro fotográfico y seguimiento de la evolución de la carta.',
    },
    {
      q: '¿Incluye tareas de sumiller y bodega?',
      a: 'Sí. Una plantilla entera dedicada al sumiller: gestión de bodega, carta de vinos, maridajes por pase del menú degustación, servicio de sumillería, catas para equipo, temperaturas de servicio y control de stock de referencias premium.',
    },
    {
      q: '¿Es solo para fine dining o sirve para cocina creativa casual?',
      a: 'Sirve para ambos. Las plantillas son escalables: un restaurante con menú degustación de 12 pases puede usar todas. Un bistro creativo con carta corta puede simplificar y quedarse con apertura/cierre, brigada y periódicas. Adapta lo que necesites.',
    },
    {
      q: '¿En qué se diferencia del software de gestión?',
      a: 'El software de gestión cobra €40/mes por local y requieren tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Repetir las Mismas Instrucciones Cada Turno',
    subtitle: '11 plantillas + 2 bonus (13 ficheros) por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Checklists de apertura y cierre: cocina, pass, sala, bodega',
      'Apertura/cierre de negocio y arqueo de caja con descuadre automático',
      'Mise en place degustación: bases, salsas, timing de pases',
      'I+D y desarrollo de menú: fichas técnicas, pruebas, costes',
      'Tareas por brigada creativa: chef ejecutivo, sous-chef, jefe de partida',
      'Semanales, mensuales y trimestral/anual: deep clean, inventario, mantenimiento legal',
      'Sumiller y maridajes: bodega, carta de vinos, catas',
      "Chef's table y eventos: cenas maridaje, showcookings, prensa",
      'Fotografía y storytelling: sesión de fotos, contenido RRSS',
      'BONUS: Briefing Diario de Servicio (€9)',
      'BONUS: Calendario Anual de Eventos y Carta (€9)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS — €12',
  },

  testimonials: {
    subtitle:
      'Chefs ejecutivos, sous-chefs, sumilleres y gerentes de restaurante creativo que ya tienen sus operaciones bajo control',
    items: [
      {
        name: 'Alberto Riera',
        role: 'Chef ejecutivo, restaurante con estrella Michelin',
        text: 'El checklist de mise en place para degustación me cambió la vida. Cada pase documentado con timing, temperaturas y responsable. Mi sous-chef ya no necesita preguntarme nada, todo está en la plantilla.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Marina Delgado',
        role: 'Sous-chef, restaurante degustación 2 estrellas',
        text: 'La plantilla de I+D es increíble. Fichas técnicas, pruebas de concepto, evaluación sensorial... por fin tengo un sistema para documentar toda la investigación que hacemos en cocina.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Fernando Casas',
        role: 'Sumiller, restaurante gastronómico',
        text: 'Por fin un checklist que entiende el trabajo del sumiller: gestión de bodega, maridajes por pase, temperaturas de servicio, catas de equipo. Los agentes IA genéricos no cubren ni el 20% de esto.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Lucía Navarro',
        role: 'Jefa de sala, restaurante de autor',
        text: 'El briefing diario de servicio lo usamos antes de cada pase. VIPs, alergias, cambios de carta, rangos de sala... en 5 minutos todo el equipo está alineado. Imprescindible para fine dining.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Carlos Iniesta',
        role: 'Chef propietario de 2 restaurantes creativos',
        text: 'Tengo dos restaurantes creativos y cada sous-chef hacía las cosas a su manera. Con los checklists estandarizados, la calidad es la misma en ambos. El onboarding de stagiaires pasó de 2 semanas a 4 días.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Patricia Vega',
        role: 'Consultora gastronómica, alta cocina',
        text: 'Lo primero que hago con cada cliente de restaurante creativo es entregarle estos checklists. I+D, degustación, sumiller, eventos... cubren el 95% de lo que necesita cualquier restaurante de autor.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Diego Morales',
        role: 'Chef pastelero creativo',
        text: 'La sección de I+D me permite documentar cada prueba de postre nuevo con costes, tiempos y evaluación. Antes perdía ideas geniales porque no las registraba. Ahora tengo un histórico completo.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Javier Ortega',
        role: 'Director de operaciones, grupo gastronómico',
        text: 'Gestionamos 4 restaurantes creativos. El calendario anual de eventos y carta nos permite planificar cambios estacionales, guias, premios y jornadas tematicas con meses de antelación. Oro puro.',
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

  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-restaurante-creativo',
    label: '¿Ya compraste el Kit de Tareas Restaurante Creativo? Vuelve a entrar al dashboard',
  },
};

export default data;
