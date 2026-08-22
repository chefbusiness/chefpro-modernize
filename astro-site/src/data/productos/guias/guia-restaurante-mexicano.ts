// guia-restaurante-mexicano.ts — Copy VERBATIM de src/pages/GuiaRestauranteMexicano.tsx +
// componentes de src/components/guia-restaurante-mexicano/* +
// data/testimonials-guia-restaurante-mexicano.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
// Sin divergencias estructurales respecto al producto de referencia (guia-restaurante-gastronomico):
// showCompatibleApps false (default, la SPA no importa CompatibleAppsMarquee), bonus.layout 'split'
// (5 bonus, igual que gastronómico), breadcrumb 3 ítems, avatarAltPrefix/titleGold por defecto.
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-restaurante-mexicano',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_MEXICANO',

  seo: {
    title: 'Cómo Montar un Restaurante Mexicano 80 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium para montar un restaurante mexicano en España: 20 capítulos, 60+ páginas, proveedores de productos mexicanos, barra de tequilas, tacos, escandallos. 8 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    keywords: 'como montar restaurante mexicano españa, abrir taqueria, restaurante mexicano autentico, proveedores productos mexicanos españa, barra tequilas mezcal, tacos al pastor, plan financiero restaurante mexicano, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg',
  },

  hero: {
    badge: 'La cocina mexicana es la más demandada de Latinoamérica en España — el momento de abrir es ahora',
    titlePre: 'Cómo Montar un ',
    titleGold: 'Restaurante Mexicano',
    subtitleLine: '80 Plazas · Guía Completa España',
    description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para abrir tu restaurante de cocina mexicana.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas: plan financiero, escandallos, menú engineering',
      '6 checklists de apertura: legal, equipamiento, APPCC, sala, contratación, marketing',
      'Business Plan modelo para presentar a bancos e inversores',
      'Manual de operaciones: apertura, cierre, servicio, taquería, barra de tequilas',
    ],
    ctaLabel: 'COMPRAR GUÍA — 65 EUR',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    priceOld: '180 EUR',
    price: '65 EUR',
    discountBadge: '-64%',
    heroNote: 'Precio de lanzamiento — ahorra 115 EUR',
    buyBoxNote: 'Precio de lanzamiento — ahorra 115 EUR',
    bonusTotalLabel: 'Valor total: guía + 5 bonus',
    bonusSaveLine: 'Ahorra 115 EUR HOY',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-mexicano-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-mexicano-sala.jpg',
      '/lovable-uploads/ai-gallery/guia-mexicano-plato.jpg',
      '/lovable-uploads/ai-gallery/guia-mexicano-barra.jpg',
      '/lovable-uploads/ai-gallery/guia-mexicano-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-mexicano-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-mexicano-sala.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 8 Plantillas + 6 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu restaurante mexicano en España, escrito por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    chapters: [
      { icon: 'Building2', num: '01', title: 'Qué es un Restaurante Mexicano en España', desc: 'Diferencia entre mexicano auténtico, tex-mex y fusion. Posicionamiento, público objetivo y ticket medio 18-30€.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado de la Cocina Mexicana en España 2026', desc: 'Datos del sector, crecimiento de la demanda, ciudades con mayor oportunidad y competencia actual.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio', desc: 'Taquería gourmet, cantina mexicana, casual mexicano, cocina de autor mexicana y dark kitchen de tacos.' },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 120K-280K€, food cost 28-33%, márgenes en bebidas (tequila/mezcal 75-80%), break-even.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, registro sanitario, importación de productos mexicanos, licencia de alcohol, terraza.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC adaptado: chiles secos, masa de maíz, importación, trazabilidad de productos mexicanos.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales en España, metros para 80 plazas, barra de tequilas, cocina abierta y terraza.' },
      { icon: 'Layout', num: '08', title: 'Diseño de Cocina Mexicana', desc: 'Plancha/comal, estación de tacos, zona de salsas, parrilla, freidora para totopos. Flujo específico.' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento Específico', desc: 'Comal, tortillera, molcajete industrial, parrilla, ahumador, máquina de margaritas. Costes detallados.' },
      { icon: 'Armchair', num: '10', title: 'Diseño de Sala: Ambiente Mexicano', desc: 'Interiorismo auténtico: colores vivos, azulejos Talavera, plantas, luces de verbena, arte mexicano.' },
      { icon: 'GlassWater', num: '11', title: 'Vajilla, Menaje y Presentación', desc: 'Platos de barro, cazuelas, vasos de vidrio soplado, cestitas para totopos. Autenticidad en cada detalle.' },
      { icon: 'GlassWater', num: '12', title: 'Barra de Tequilas y Mezcales', desc: 'Selección de 30-50 referencias, coctelería mexicana (margarita, paloma, michelada), márgenes 75-80%.' },
      { icon: 'Users', num: '13', title: 'Brigada de Cocina (6-10 personas)', desc: 'Taquero, parrillero, salsero, cocineros polivalentes. Salarios España 2026 y formación en cocina mexicana.' },
      { icon: 'UserCheck', num: '14', title: 'Equipo de Sala (6-8 personas)', desc: 'Servicio cercano y festivo, conocimiento de tequilas/mezcales, upselling de margaritas y guacamole.' },
      { icon: 'UtensilsCrossed', num: '15', title: 'La Carta: Menú Engineering Mexicano', desc: 'Tacos, burritos, enchiladas, quesadillas, ceviches, guacamole. Matrix de rentabilidad por plato.' },
      { icon: 'Flame', num: '16', title: 'Proveedores: Productos Mexicanos en España', desc: 'Importadores de chiles, masa de maíz, tortillas, salsas, tequila, mezcal. Proveedores nacionales y directos.' },
      { icon: 'Utensils', num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos clave: tacos al pastor, carnitas, guacamole, mole, churros. Food cost real.' },
      { icon: 'Truck', num: '18', title: 'Delivery y Take Away Mexicano', desc: 'Tacos y burritos viajan bien. Packaging específico, menú delivery optimizado, plataformas vs propio.' },
      { icon: 'Megaphone', num: '19', title: 'Marketing y Posicionamiento', desc: 'Instagram, TikTok, influencers food, eventos temáticos (Día de Muertos, Cinco de Mayo), Google My Business.' },
      { icon: 'Tablet', num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas, delivery, contabilidad, turnos, carta digital con fotos de platos mexicanos.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Propietarios, chefs, inversores y consultores que ya usaron esta guía',
    items: [
      { name: 'Carlos Mendoza', role: 'Propietario de taquería gourmet en Madrid', text: 'La sección de proveedores de productos mexicanos en España me ahorró meses de búsqueda. Chiles, masa de maíz, tequilas premium... todo con contactos reales.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Patricia Ramírez', role: 'Chef mexicana, 12 años en España', text: 'Por fin una guía que entiende la diferencia entre mexicano auténtico y tex-mex. Los escandallos de tacos al pastor y mole poblano con food cost real son oro puro.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Roberto Díaz', role: 'Consultor de restauración, Barcelona', text: 'El capítulo de barra de tequilas y mezcales es impresionante. Los márgenes del 75-80% en coctelería mexicana son los mejores del sector. Mis clientes se sorprenden.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Ana Moreno', role: 'Inversora, 3 restaurantes en Valencia', text: 'Presenté el business plan modelo al banco con los números de la guía y me aprobaron la financiación. La proyección financiera con escenarios fue clave.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Miguel Torres', role: 'Diseñador de interiores, especializado en hostelería', text: 'El capítulo de interiorismo mexicano auténtico versus el cliché de sombreros es exactamente lo que mis clientes necesitan leer. Azulejos Talavera, colores, materiales...', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Lucía Hernández', role: 'Propietaria cantina mexicana, Sevilla', text: 'La guía de delivery para comida mexicana me ayudó a diseñar un menú que viaja perfecto. Los tacos y burritos son el producto ideal para delivery. Facturamos 25% más.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Fernando García', role: 'Importador de productos mexicanos, Madrid', text: 'Como importador, confirmo que los proveedores listados en la guía son los principales del mercado español. Información difícil de conseguir si no estás en el sector.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sofía López', role: 'Community manager de restaurantes, Málaga', text: 'El capítulo de marketing con eventos temáticos (Día de Muertos, Cinco de Mayo) me dio ideas para un calendario de contenido de todo el año. Engagement por las nubes.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Escrita por un Profesional', desc: 'Chef desde los 17 años y consultor desde 2010, 200+ aperturas asesoradas. Incluye proveedores reales de productos mexicanos en España.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (120K-280K€), food cost 28-33%, márgenes en tequila/mezcal del 75-80%, break-even calculado.' },
      { icon: 'FileSpreadsheet', title: 'Incluye Plantillas por Valor de 80€+', desc: 'Plan financiero, escandallos de tacos/burritos/guacamole, menú engineering, Gantt y más — todo en Excel.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000-10.000€', desc: 'La misma información que reciben los clientes de consultoría gastronómica, en formato guía por un pago único de 65€.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos en España y Europa, incluyendo restaurantes de cocina internacional y conceptos temáticos.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Incluye sección específica de cocina mexicana y proveedores de importación.', image: '/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual de Operaciones Mexicano', value: '39 EUR', desc: 'Protocolo completo: apertura, cierre, servicio, preparación de salsas, barra de tequilas, gestión de delivery y eventos temáticos (Día de Muertos, Cinco de Mayo).', image: '/lovable-uploads/ai-gallery/guia-mexicano-sala.jpg' },
      { icon: 'ClipboardCheck', label: 'BONUS 3', title: 'Checklist Equipamiento Cocina Mexicana', value: '29 EUR', desc: '35 ítems específicos: comal, tortillera, molcajete, ahumador, máquina de margaritas, freidora para totopos, parrilla y más.', image: '/lovable-uploads/ai-gallery/guia-mexicano-cocina.jpg' },
      { icon: 'CalendarRange', label: 'BONUS 4', title: 'Cronograma de Apertura Gantt 12 Meses', value: '24 EUR', desc: 'Fases específicas para mexicano: importación de productos, diseño temático, formación en cocina mexicana, soft opening.', image: '/lovable-uploads/ai-gallery/guia-mexicano-barra.jpg' },
      { icon: 'PieChart', label: 'BONUS 5', title: 'Escandallos: 15 Recetas Base Mexicanas', value: '19 EUR', desc: 'Fichas técnicas con food cost real: tacos al pastor, carnitas, guacamole, mole poblano, enchiladas, churros y más.', image: '/lovable-uploads/ai-gallery/guia-mexicano-plato.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu restaurante mexicano, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar un restaurante mexicano en España?', a: 'Entre 120.000€ y 280.000€ dependiendo de la ubicación, nivel de acabados y si incluyes barra de tequilas premium. La cocina mexicana requiere equipamiento específico (comal, tortillera, ahumador) pero es más económica que otros conceptos.' },
    { q: '¿Dónde consigo productos mexicanos auténticos en España?', a: 'La guía incluye un capítulo completo (cap. 16) con proveedores de importación de chiles secos, masa de maíz, tortillas, tequila, mezcal y más. Hay importadores especializados en Madrid, Barcelona, Valencia y distribución nacional.' },
    { q: '¿Mexicano auténtico o tex-mex? ¿Qué funciona mejor?', a: 'Depende de la zona. En ciudades grandes con comunidad latina, el mexicano auténtico triunfa. En zonas más turísticas, un concepto que mezcle autenticidad con accesibilidad funciona mejor. La guía analiza los 4 modelos en detalle.' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 8 plantillas incluyen fórmulas automáticas: plan financiero, escandallos de 15 platos mexicanos clave (tacos, guacamole, mole), menú engineering, cash flow y más.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Restaurante a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta una cena para cuatro.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual de operaciones mexicano',
      'Escandallos de 15 recetas base mexicanas',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'GUÍA RESTAURANTE MEXICANO — 65 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Guía Restaurante Casual', href: '/guia-restaurante-casual' },
    { label: 'Guía Restaurante Gastronómico', href: '/guia-restaurante-gastronomico' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'guia-restaurante-mexicano',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar un Restaurante Mexicano 80 Plazas — Guía Completa España',
    productDescription: 'Guía premium de 20 capítulos para montar un restaurante mexicano: plan financiero, proveedores de productos mexicanos, barra de tequilas, escandallos de tacos. Incluye 8 plantillas Excel, 6 checklists, business plan y manual de operaciones.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar un restaurante mexicano en España?', a: 'Entre 120.000€ y 280.000€ para 80 plazas. La cocina mexicana requiere equipamiento específico (comal, tortillera) pero es más económica que otros conceptos.' },
      { q: '¿Dónde consigo productos mexicanos auténticos en España?', a: 'La guía incluye un capítulo completo con proveedores de importación de chiles, masa de maíz, tortillas, tequila y mezcal con distribución nacional.' },
      { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Plan financiero a 3 años, escandallos de 15 platos mexicanos clave, menú engineering, cash flow y break-even. Todo con fórmulas automáticas.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Restaurante Mexicano', item: 'https://aichef.pro/guia-restaurante-mexicano' },
    ],
  },
};

export default data;
