// astro-site/src/data/productos/kits/kit-inventario.ts
// LÍNEA KITS EXCEL — Kit Control de Inventario y Compras. Copy VERBATIM de la SPA:
//   · src/pages/KitInventario.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/kit-inventario/*  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-inventario.ts (8 testimonios)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_INVENTARIO (resuelto en el wrapper .astro).
//
// Divergencias vs. el producto de referencia (kit-escandallos), ya cubiertas por props
// opcionales de types.ts:
//   · hero.badgeTone = 'red' (no 'gold').
//   · hero H1 = Forma B: titlePre + titleGold + titleSubtitle en <span block> (SIN titlePost).
//   · grid.fourCols = omitido (9 tarjetas, grid-cols-2 md:grid-cols-3 — NO 4 columnas).
//   · guarantee.headingPre = 'Garantia de Satisfaccion ' (sin tildes).
//   · authorBadges = ['Consultor Gastronomico', '+29 anos en alta hosteleria'] (sin tildes).
//   · stickyVariant = omitido (default 'v2', igual que la SPA: px-3 max-w-screen-sm, CTA "COMPRAR").
//   · images.gridGallery = omitido: ContentGrid.tsx usa el MISMO set de 6 imágenes que el hero
//     (heroImages === galleryImages en la SPA), cae en `images.gallery` por el default del template.
// NOTA quirk-tildes: el copy de este producto está redactado MAYORMENTE sin tildes (hosteleria,
// disenadas, anos, mas, etc.), copiado VERBATIM tal cual la SPA — no hay normalización.
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'kit-inventario',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_INVENTARIO',

  seo: {
    title: 'Kit Control de Inventario y Compras — Plantillas Excel para Hosteleria | AI Chef Pro',
    description:
      '9 plantillas Excel con formulas automaticas para controlar inventario, proveedores, pedidos, mermas, FIFO y costes de compras en hosteleria. Solo 14 EUR.',
    keywords:
      'control inventario restaurante, gestion compras hosteleria, plantilla mermas excel, control stock cocina, fifo restaurante, proveedores hosteleria, food cost control, pedidos compra restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-inventario.jpg',
  },

  schema: {
    productName: 'Kit Control de Inventario y Compras — Plantillas Excel para Hosteleria',
    productDescription:
      '9 plantillas Excel con formulas automaticas para controlar inventario, proveedores, pedidos, mermas, FIFO y costes de compras en hosteleria.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Miguel Fernandez',
        rating: '5',
        body: 'El control de mermas fue revelador. Descubrimos que perdiamos 400 EUR/mes solo en verdura mal almacenada.',
      },
      {
        author: 'Laura Martinez',
        rating: '5',
        body: 'La comparativa de proveedores nos ahorro mas de 2.000 EUR el primer trimestre.',
      },
      {
        author: 'Elena Ruiz',
        rating: '5',
        body: 'Es el kit mas completo que he visto en espanol: desde el inventario diario hasta el analisis de costes con dashboard.',
      },
    ],
    // FAQPage schema (VERBATIM del Helmet — MÁS CORTAS que las FAQ on-page)
    faqs: [
      {
        q: '¿Sirve para cualquier tipo de restaurante?',
        a: 'Si. Las categorias estan pre-cargadas para hosteleria: carnicos, pescados, lacteos, verduras, secos, congelados, bebidas, limpieza.',
      },
      {
        q: '¿Las plantillas se conectan entre si?',
        a: 'Si. Los niveles de stock alimentan las sugerencias de pedido. Las fichas de proveedores se enlazan con los pedidos de compra.',
      },
      {
        q: '¿Cumple con los requisitos de APPCC?',
        a: 'Si. Incluye control de temperaturas en recepcion, trazabilidad FIFO y registro de caducidades con alertas por colores.',
      },
      {
        q: '¿Hay garantia de devolucion?',
        a: '30 dias de garantia completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit Control de Inventario y Compras',
  },

  images: {
    // hero bg (6) — IDÉNTICAS a ContentGrid.galleryImages en la SPA → gridGallery se omite
    gallery: [
      '/lovable-uploads/ai-gallery/inventario-hero.jpg',
      '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
      '/lovable-uploads/ai-gallery/inventario-recepcion.jpg',
      '/lovable-uploads/ai-gallery/inventario-proveedores.jpg',
      '/lovable-uploads/ai-gallery/inventario-cocina.jpg',
      '/lovable-uploads/ai-gallery/inventario-analisis.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/inventario-hero.jpg',
  },

  hero: {
    badgeTone: 'red',
    badge: 'Los restaurantes pierden entre 3.000 y 5.000 EUR/ano en mermas evitables',
    titlePre: 'Kit Control de ',
    titleGold: 'Inventario y Compras',
    // sin titlePost (Forma B: subtítulo en bloque, no inline)
    titleSubtitle: 'Controla Stock, Reduce Mermas y Optimiza Compras',
    description:
      '9 plantillas Excel con formulas automaticas para gestionar inventario, proveedores, pedidos, recepcion de mercancias, mermas, FIFO y analisis de costes de compras. Deja de perder dinero.',
    checkItems: [
      'Inventario diario con par levels y alertas de reposicion automaticas',
      'Fichas de proveedores con comparativa de precios entre 5 proveedores',
      'Pedidos de compra auto-calculados desde niveles de stock',
      'Control de recepcion con verificacion de temperatura y caducidad',
      'Mermas por categoria con dashboard y plan de accion',
    ],
    ctaLabel: 'COMPRAR AHORA — 14 EUR',
  },

  // variant="tareas" en la SPA (CompatibleAppsMarquee)
  compatApps: {
    titleHtml: 'Imprime, Delega y <span class="text-[#FFD700]">Controla</span>',
    subtitleHtml:
      'Plantillas Excel optimizadas para imprimir en A4. Compatible con Excel, Google Sheets, LibreOffice y Numbers',
  },

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Control de Inventario',
    subtitle:
      'Cada plantilla incluye formulas automaticas y esta disenada para la realidad de la hosteleria. Solo ajusta a tu negocio y empieza a controlar.',
    // fourCols omitido → grid-cols-2 md:grid-cols-3 (9 tarjetas, paridad ContentGrid.tsx)
    templates: [
      { icon: 'Package', title: 'Inventario de Stock Diario', desc: 'Control de stock por zona (cocina, barra, almacen) con par levels, alertas de reposicion automaticas y valoracion de stock. Semaforo rojo/amarillo/verde.' },
      { icon: 'Users', title: 'Fichas de Proveedores', desc: 'Directorio completo, comparativa de precios entre 5 proveedores por producto, evaluacion de calidad/precio/entrega y condiciones comerciales.' },
      { icon: 'ShoppingCart', title: 'Pedidos de Compra', desc: 'Generacion automatica de pedidos desde niveles de stock. Dropdown de proveedores, subtotales con IVA y formato imprimible para enviar.' },
      { icon: 'ClipboardCheck', title: 'Recepcion de Mercancias', desc: 'Checklist de verificacion: cantidad, calidad, temperatura, caducidad. Registro de incidencias y discrepancias vs pedido original.' },
      { icon: 'Trash2', title: 'Control de Mermas', desc: 'Registro diario por categoria (caducidad, preparacion, devolucion). Coste automatico, dashboard mensual y plan de accion. Objetivo: <3%.' },
      { icon: 'RotateCcw', title: 'FIFO y Caducidades', desc: 'Control de rotacion First In First Out con alertas por colores: rojo (caduca manana), amarillo (3 dias), verde (OK). Mapa de almacen incluido.' },
      { icon: 'BarChart3', title: 'Analisis de Costes de Compras', desc: 'Coste por categoria, evolucion mensual, top 20 productos, alertas de variacion de precios (>5%) y dashboard de KPIs: food cost %, coste por cubierto.' },
      { icon: 'Clock', title: 'BONUS: Inventario Rapido Mensual', desc: 'Conteo simplificado de una pagina para inventario mensual completo. Auto-calcula valoracion y variaciones vs mes anterior.' },
      { icon: 'Calculator', title: 'BONUS: Calculadora Punto de Pedido', desc: 'Calcula cuando pedir cada ingrediente segun consumo diario, tiempo de entrega y stock de seguridad. Simulador de demanda variable.' },
    ],
  },

  why: {
    headingPre: '¿Por Que Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genericas de almacen. Son herramientas disenadas por un profesional con 29 anos en alta hosteleria.',
    reasons: [
      { icon: 'Utensils', title: 'Disenadas para Hosteleria', desc: 'Categorias pre-cargadas para restaurantes: carnicos, pescados, lacteos, verduras, secos, congelados, bebidas, limpieza. No son plantillas genericas de almacen.' },
      { icon: 'Calculator', title: 'Formulas que Ahorran Dinero', desc: 'Par levels con alertas, coste de mermas automatico, variacion de precios entre proveedores y food cost % por categoria. Los numeros trabajan por ti.' },
      { icon: 'ShieldCheck', title: 'Cumplimiento APPCC', desc: 'Control de temperaturas en recepcion, trazabilidad FIFO, registro de caducidades y mapa de almacen. Todo lo que necesitas para las inspecciones.' },
      { icon: 'RefreshCw', title: 'Software de Gestión Cobra 60 EUR/mes. Esto es 14 EUR', desc: 'Las mismas funciones que los SaaS de gestion de inventario, pero en Excel por un pago unico. Sin suscripcion, sin limite de productos.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Mas de 29 anos de carrera profesional en alta hosteleria y restauracion, y 15 anos en consultoria gastronomica. Especialista en control de costes, gestion de compras y optimizacion de food cost en cientos de establecimientos.',
  authorBadges: ['Consultor Gastronomico', '+29 anos en alta hosteleria'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Ademas de las 7 plantillas principales, recibes estos recursos adicionales — valorados en 18 EUR',
    items: [
      {
        icon: 'Clock',
        label: 'BONUS 1',
        title: 'Inventario Rapido Mensual',
        value: '9 EUR',
        desc: 'Conteo simplificado de una pagina para inventario mensual completo. Auto-calcula valoracion de stock y variaciones significativas vs mes anterior. Optimizado para imprimir.',
        image: '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
      },
      {
        icon: 'Calculator',
        label: 'BONUS 2',
        title: 'Calculadora Punto de Pedido',
        value: '9 EUR',
        desc: 'Introduce consumo diario, tiempo de entrega y stock de seguridad — calcula automaticamente el punto optimo de reposicion y la cantidad economica de pedido (EOQ).',
        image: '/lovable-uploads/ai-gallery/inventario-analisis.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SI, QUIERO EL KIT DE INVENTARIO — 14 EUR',
  },

  guarantee: {
    headingPre: 'Garantia de Satisfaccion ',
    text:
      'Si las plantillas no te ayudan a reducir mermas y controlar mejor las compras de tu restaurante, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Dias de garantia' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incomodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (más largas que schema.faqs)
  faqs: [
    {
      q: '¿Sirve para cualquier tipo de restaurante?',
      a: 'Si. Las categorias estan pre-cargadas para hosteleria en general: carnicos, pescados, lacteos, verduras, secos, congelados, bebidas, limpieza. Solo elimina las que no apliquen a tu negocio y anade las que falten.',
    },
    {
      q: '¿Las plantillas se conectan entre si?',
      a: 'Si. Los niveles de stock alimentan automaticamente las sugerencias de pedido. Las fichas de proveedores se enlazan con los pedidos de compra. El control de mermas calcula el coste en tiempo real.',
    },
    {
      q: '¿Cumple con los requisitos de APPCC?',
      a: 'Si. La plantilla de recepcion incluye control de temperaturas y la de FIFO gestiona caducidades con alertas por colores. Ambas son trazables y auditables para inspecciones.',
    },
    {
      q: '¿En que se diferencia del software de inventario?',
      a: 'El software de inventario cobra entre 50 y 100 EUR/mes por restaurante. Este kit cuesta 14 EUR, pago unico, sin suscripcion ni limite de productos. Y puedes personalizar todo al 100%.',
    },
    {
      q: '¿Puedo usarlo en varios restaurantes?',
      a: 'Si. La licencia es personal — puedes usar las plantillas en todos los establecimientos que gestiones. Ideal para grupos de restauracion, multi-unidades y consultores.',
    },
    {
      q: '¿Hay garantia de devolucion?',
      a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Perder Dinero en Mermas y Compras a Ciegas',
    subtitle:
      '9 plantillas profesionales para controlar inventario por menos de lo que cuestas en mermas un solo dia.',
    items: [
      'Inventario diario con par levels y alertas de reposicion',
      'Fichas de proveedores con comparativa de precios',
      'Pedidos de compra auto-generados desde stock',
      'Recepcion de mercancias con control de temperatura',
      'Control de mermas con dashboard y plan de accion',
      'FIFO y caducidades con semaforo de colores',
      'Analisis de costes con KPIs: food cost %, coste/cubierto',
      'BONUS: Inventario Rapido Mensual (9 EUR)',
      'BONUS: Calculadora Punto de Pedido (9 EUR)',
    ],
    ctaLabel: 'SI, QUIERO EL KIT DE INVENTARIO — 14 EUR',
  },

  testimonials: {
    subtitle:
      'Jefes de cocina, gerentes y directores de operaciones que ya controlan su inventario con estas plantillas',
    items: [
      { name: 'Miguel Fernandez', role: 'Jefe de cocina, restaurante casual (60 cubiertos)', text: 'El control de mermas fue revelador. Descubrimos que perdíamos 400 EUR/mes solo en verdura mal almacenada. En 3 meses redujimos las mermas un 60%. La plantilla se pago sola el primer dia.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Laura Martinez', role: 'Directora de operaciones, grupo de 4 restaurantes', text: 'La comparativa de proveedores nos ahorro mas de 2.000 EUR el primer trimestre. Tener los precios de 5 proveedores en una tabla con semaforo de variacion es brutal para negociar.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Ramos', role: 'Propietario, gastrobar en Barcelona', text: 'Antes haciamos pedidos a ojo. Con la plantilla de pedidos de compra y los puntos de reposicion, ya no nos quedamos sin producto un viernes noche ni tiramos genero el lunes.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Patricia Vega', role: 'Jefa de economato, hotel 4* (180 habitaciones)', text: 'El control de recepcion de mercancias nos ha evitado 3 incidencias de temperatura en el ultimo mes. Ahora todo queda registrado: proveedor, cantidad, temperatura, caducidad.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Andres Lopez', role: 'Chef ejecutivo, catering de eventos', text: 'El FIFO por colores es genial. Mis cocineros lo entienden de un vistazo: rojo = caduca manana, amarillo = 3 dias, verde = OK. Las perdidas por caducidad bajaron un 80%.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Elena Ruiz', role: 'Consultora gastronomica, +12 anos', text: 'Lo uso con todos mis clientes. Es el kit mas completo que he visto en espanol: desde el inventario diario hasta el analisis de costes con dashboard. Profesionaliza la gestion desde el dia uno.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Jorge Navarro', role: 'Gerente, pizzeria artesanal (2 locales)', text: 'La calculadora de punto de pedido nos cambio la vida. Sabemos exactamente cuando pedir cada ingrediente segun nuestro consumo diario y el tiempo de entrega del proveedor.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Diego Serrano', role: 'Director de compras, cadena de restaurantes', text: 'El analisis de costes por categoria me da vision total: que porcentaje gastamos en carnicos, pescados, verdura, secos. Ahora negocio con datos reales, no con sensaciones.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  pricing: {
    priceOld: '49 EUR',
    price: '14 EUR',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: 'Ahorra 35 EUR HOY',
  },

  stickyLabel: 'KIT INVENTARIO Y COMPRAS — 14 EUR',
  // stickyVariant omitido → default 'v2' (paridad StickyBar.tsx: px-3 max-w-screen-sm, CTA "COMPRAR")

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/kit-gestion-personal', label: 'Kit Gestion Personal' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'kit-inventario',
    label: '¿Ya compraste el Kit de Inventario? Vuelve a entrar al dashboard',
  },
};

export default data;
