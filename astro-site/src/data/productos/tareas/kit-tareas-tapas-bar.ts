// astro-site/src/data/productos/tareas/kit-tareas-tapas-bar.ts
// Copy VERBATIM (byte a byte) extraído de:
//   - src/pages/KitTareasTapasBar.tsx  (Helmet: SEO + 3 JSON-LD, orden de secciones, footer)
//   - src/components/kit-tareas-tapas-bar/*.tsx  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   - src/data/testimonials-tapas-bar.ts  (marquee de testimonios)
// NO parafraseado.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-tapas-bar',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_TAPAS_BAR',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Tapas Bar / Gastrobar — Checklists Operativos | AI Chef Pro',
    description:
      '11 checklists operativos para tapas bar y gastrobar: barra de pinchos y tapas frías, cocina de raciones, cerveza de grifo, vinos por copa, vermut, rotación de carta, terraza, perfiles y eventos. Solo €14.',
    keywords:
      'checklist tapas bar, tareas gastrobar, control cerveza grifo, barra de pinchos, cocina raciones, terraza tapas, vermut, vinos por copa, rotación carta tapas, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-tapas-bar.jpg',
  },

  schema: {
    productName: 'Kit de Tareas Recurrentes: Tapas Bar / Gastrobar — Checklists Operativos',
    productDescription:
      '11 checklists operativos pre-rellenados para tapas bar y gastrobar: barra de pinchos y tapas frías, cocina de raciones, cerveza de grifo, vinos por copa y vermut, rotación de carta, terraza, perfiles y eventos.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Los checklists de barra de pinchos y cocina de raciones son muy completos. Plancha, freidora, guisos, cazuelas… todo el equipo sigue el mismo estándar cada turno.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'La rotación de la vitrina de tapas con FIFO y el control de mermas en barra nos ha reducido el desperdicio a la mitad. Imprescindible para cualquier tapas bar.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'Implementamos en los 3 locales. La consistencia en el montaje de pinchos y la pizarra de tapas del día es ahora uniforme en todos.',
      },
    ],
    faqs: [
      {
        q: '¿Sirve para un gastrobar moderno?',
        a: 'Sí. Cubre desde tapas bar clásico hasta gastrobar contemporáneo con cocina de autor en formato tapa. Tapas tradicionales, pinchos, raciones, medias raciones y propuestas creativas. Todo es editable y adaptable a tu formato.',
      },
      {
        q: '¿Incluye control de cerveza de grifo?',
        a: 'Sí. Control completo de grifos: presión, CO2, temperatura, purga diaria, limpieza de líneas semanal, rotación de barriles y control de mermas. Todo con frecuencias y valores de referencia.',
      },
      {
        q: '¿Cubre la terraza?',
        a: 'Sí. Apertura y cierre de terraza, montaje de mesas y sillas, limpieza, eventos en terraza, control de stock terraza y protocolo de cierre por climatología.',
      },
      {
        q: '¿Incluye rotación de carta estacional?',
        a: 'Sí. El calendario anual incluye tapas por temporada (gazpacho en verano, guisos en invierno, setas en otoño…), eventos gastronómicos, rutas de tapas y fechas clave para planificar la carta.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Tapas Bar / Gastrobar',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
      '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €14 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Tapas Bar / Gastrobar',
    description:
      '11 checklists Excel pre-rellenados para tapas bar y gastrobar: barra de pinchos y tapas frías, cocina de raciones (plancha, freidora, guisos, cazuelas), cerveza de grifo, vinos por copa, vermut y terraza. Imprime, delega y firma.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Barra de pinchos, cocina raciones y cerveza de grifo bajo control',
      'Vinos por copa, vermut y coctelería ligera',
      'Terraza, eventos y rotación de carta estacional',
      'Tareas por perfil: cocina, barra, sala, terraza, encargado',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  stickyLabel: 'KIT TAREAS TAPAS BAR — €14',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Tapas Bar',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de un tapas bar o gastrobar profesional con barra de pinchos, cocina de raciones, cerveza de grifo y terraza. Solo ajusta a tu carta, imprime y empieza a operar con estándar profesional.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre Tapas Bar',
        desc: 'Barra, cocina, sala y terraza: vitrina de tapas, grifos de cerveza, mise en place, montaje de pizarra del día y cierre con arqueo de caja, limpiezas y temperaturas.',
      },
      {
        icon: 'Sandwich',
        title: 'Barra de Tapas y Pinchos',
        desc: 'Vitrina de tapas frías, montaje de pinchos, rotación FIFO, tapas del día, pizarra, control de mermas y reposición durante el servicio sin huecos en barra.',
      },
      {
        icon: 'ChefHat',
        title: 'Cocina de Raciones y Platos',
        desc: 'Plancha, freidora, cazuelas, guisos, emplatado y timing de servicio. Estándares de cocción, mise en place y cambios de turno con pase ordenado.',
      },
      {
        icon: 'Beer',
        title: 'Bebidas: Cerveza, Vino y Vermut',
        desc: 'Grifos de cerveza (presión, CO2, temperatura, purga, líneas), vinos por copa, vermut con sifón, coctelería ligera, inventario de barra y control de mermas.',
      },
      {
        icon: 'Briefcase',
        title: 'Tareas del Manager',
        desc: 'Revenue diario, food cost, compras, gestión de proveedores, RRHH, marketing, reservas, terraza y reporting semanal con KPIs operativos del local.',
      },
      {
        icon: 'Users',
        title: 'Tareas por Perfil',
        desc: 'Tareas claras por perfil: jefe de cocina, cocinero de raciones, camarero de barra, camarero de sala/terraza y encargado. Roles y responsabilidades sin solapes.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda de líneas de cerveza, inventarios, auditoría APPCC, evaluación de proveedores y rotación/evaluación de carta de tapas y raciones.',
      },
      {
        icon: 'CalendarDays',
        title: 'Eventos y Temporadas',
        desc: 'Tapas estacionales (gazpacho en verano, guisos en invierno, setas en otoño), Navidad, rutas de tapas, partidos de fútbol y after-work.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu tapas bar (clásico, moderno, gastrobar, tapas de barrio o terraza).',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing de Servicio',
        desc: 'Briefing pre-servicio de 5 minutos: tapas del día, bebidas destacadas, alérgenos activos, reservas, estado de terraza y avisos para barra y sala.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con tapas por temporada, eventos gastronómicos, rutas de tapas, mantenimientos del local, formación del equipo y cierres por vacaciones.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010 y experiencia en tapas bars, gastrobars y barras de pinchos.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñados para Tapas Bar',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de un tapas bar y gastrobar: barra de pinchos, cocina de raciones, cerveza de grifo y terraza.',
      },
      {
        icon: 'Beer',
        title: 'Protocolo Cerveza de Grifo',
        desc: 'Presión, CO2, temperatura, purga diaria, limpieza de líneas semanal, rotación de barriles y control de mermas. Lo que las cervezas premium exigen y los locales suelen descuidar.',
      },
      {
        icon: 'Sandwich',
        title: 'Barra de Pinchos con FIFO',
        desc: 'Vitrina de tapas frías, montaje de pinchos, rotación FIFO, tapas del día y control de mermas. Cero desperdicio sin perder vista comercial.',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €14',
        desc: 'Las mismas listas de tareas que usan tapas bars con software premium, pero en Excel por un pago único. Sin suscripción, sin tablets, ilimitado en clientes.',
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a tapas bars, gastrobars y barras de pinchos en la profesionalización de su operativa: control de cerveza de grifo, rotación FIFO de la vitrina, cocina de raciones y rotación de carta estacional.',

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
        desc: 'Briefing pre-servicio de 5 minutos: tapas del día por proveedor, pinchos destacados, bebidas en oferta, alérgenos activos, reservas, estado de terraza y avisos para barra y sala. La hoja que alinea al equipo cada turno.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: '12 meses con tapas por temporada, eventos gastronómicos, rutas de tapas, partidos de fútbol y after-work, mantenimientos del local, formación del equipo y cierres por vacaciones.',
        image: '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS TAPAS BAR — €14',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu tapas bar y dominar la barra de pinchos, la cocina de raciones y la cerveza de grifo, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Sirve para un gastrobar moderno?',
      a: 'Sí. Cubre desde tapas bar clásico hasta gastrobar contemporáneo con cocina de autor en formato tapa. Tapas tradicionales, pinchos, raciones, medias raciones y propuestas creativas. Todo es 100% editable y adaptable a tu formato.',
    },
    {
      q: '¿Incluye control de cerveza de grifo?',
      a: 'Sí. Control completo de grifos: presión, CO2, temperatura, purga diaria, limpieza de líneas semanal, rotación de barriles y control de mermas. Todo con frecuencias y valores de referencia para que el barril no pierda calidad.',
    },
    {
      q: '¿Cubre la terraza?',
      a: 'Sí. Apertura y cierre de terraza, montaje de mesas y sillas, limpieza, eventos en terraza, control de stock terraza y protocolo de cierre por climatología. Importante para locales con terraza temporal o anual.',
    },
    {
      q: '¿Incluye rotación de carta estacional?',
      a: 'Sí. El calendario anual incluye tapas por temporada (gazpacho en verano, guisos en invierno, setas en otoño, espárragos en primavera), eventos gastronómicos, rutas de tapas y fechas clave para planificar la carta.',
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
    heading: 'Tu Tapas Bar a Estándar Profesional — En 11 Checklists',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu tapas bar o gastrobar: barra de pinchos, cocina de raciones, bebidas, terraza, perfiles. Por menos de lo que cuesta una buena ronda de tapas con vino.',
    items: [
      'Apertura y cierre completo de barra, cocina, sala y terraza',
      'Barra de pinchos: vitrina, FIFO, tapas del día, mermas',
      'Cocina de raciones: plancha, freidora, cazuelas, guisos',
      'Cerveza de grifo, vinos por copa, vermut e inventario barra',
      'Tareas por perfil: cocina, barra, sala, terraza, encargado',
      'Calendario anual con tapas estacionales y eventos',
      'BONUS: Briefing de Servicio (€15)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS TAPAS BAR — €14',
  },

  testimonials: {
    subtitle:
      'Hosteleros, jefes de cocina y consultores que ya tienen su tapas bar o gastrobar bajo control',
    items: [
      {
        name: 'Alejandro Ruiz',
        role: 'Jefe de Cocina, Tapas Bar Madrid',
        text: 'Los checklists de barra de pinchos y cocina de raciones son muy completos. Plancha, freidora, guisos, cazuelas… todo el equipo sigue el mismo estándar cada turno y la barra se monta sin sobresaltos.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'María López',
        role: 'Propietaria Gastrobar Barcelona',
        text: 'La rotación de la vitrina de tapas con FIFO y el control de mermas en barra nos ha reducido el desperdicio a la mitad. Imprescindible para cualquier tapas bar o gastrobar moderno.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Carlos Méndez',
        role: 'Director Cadena Tapas Bars (3 locales)',
        text: 'Implementamos en los 3 locales. La consistencia en el montaje de pinchos, la pizarra de tapas del día y el control de cerveza de grifo es ahora uniforme en todos. Cero descoordinación.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Laura Fernández',
        role: 'Encargada Gastrobar, Madrid',
        text: 'Las tareas por perfil clarifican quién hace qué en barra, cocina, sala y terraza. El briefing pre-servicio con tapas del día y reservas alinea al equipo en 5 minutos antes de abrir.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'David Torres',
        role: 'Consultor Hostelero especializado en gastrobar',
        text: 'Para tapas bars y gastrobars es el kit más completo del mercado. Barra, cocina raciones, cerveza de grifo, vermut, terraza, eventos… cubre todos los puntos críticos sin huecos.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Ana García',
        role: 'Jefa de Barra Tapas Bar, Sevilla',
        text: 'El control de cerveza de grifo (presión, CO2, temperatura, purga, limpieza de líneas) y el inventario de barra nos permiten tener stock óptimo y cero mermas en barril. Gana margen.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Pedro Gutiérrez',
        role: 'Cocinero Gastrobar, Bilbao',
        text: 'Las tareas de cocina de raciones están muy bien detalladas. Plancha, freidora, cazuelas, guisos… sé exactamente qué revisar en cada momento del servicio sin tener que preguntar al jefe.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Delgado',
        role: 'Chef Ejecutivo Gastrobar Premium, Valencia',
        text: 'El calendario anual con tapas estacionales, rutas de tapas y rotación de carta nos ayuda a mantener la oferta fresca y atractiva todo el año. Pasa de "tapas de siempre" a propuesta dinámica.',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€49',
    price: '€14',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €35 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-tareas-bar', label: 'Kit Tareas Bar / Cocktails' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-tareas-tapas-bar',
    label: '¿Ya compraste el Kit de Tareas Tapas Bar? Vuelve a entrar al dashboard',
  },
};

export default data;
