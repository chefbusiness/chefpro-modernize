// guia-restaurante-peruano.ts — Copy VERBATIM de src/pages/GuiaRestaurantePeruano.tsx +
// componentes de src/components/guia-restaurante-peruano/* +
// data/testimonials-guia-restaurante-peruano.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
// Sin divergencias estructurales respecto al producto de referencia (guia-restaurante-gastronomico):
// showCompatibleApps false (default, la SPA no importa CompatibleAppsMarquee), bonus.layout 'split'
// (5 bonus, igual que gastronómico), breadcrumb 3 ítems, avatarAltPrefix/titleGold por defecto.
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-restaurante-peruano',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_PERUANO',

  seo: {
    title: 'Cómo Montar un Restaurante Peruano 80 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium para montar un restaurante peruano en España: 20 capítulos, 60+ páginas, cevichería, Nikkei, barra de piscos, proveedores peruanos. 8 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    keywords: 'como montar restaurante peruano españa, abrir cevicheria, restaurante peruano autentico, cocina nikkei, proveedores productos peruanos españa, barra piscos, ceviche, lomo saltado, plan financiero restaurante peruano, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-peruano-hero.jpg',
  },

  hero: {
    badge: 'La cocina peruana es la más premiada de Latinoamérica — 3 restaurantes entre los 50 Best del mundo',
    titlePre: 'Cómo Montar un ',
    titleGold: 'Restaurante Peruano',
    subtitleLine: '80 Plazas · Guía Completa España',
    description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para abrir tu restaurante de cocina peruana y cevichería.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas: plan financiero, escandallos, menú engineering',
      '6 checklists de apertura: legal, equipamiento, APPCC, sala, contratación, marketing',
      'Business Plan modelo para presentar a bancos e inversores',
      'Manual de operaciones: cevichería, anticuchería, barra de piscos, delivery',
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
      '/lovable-uploads/ai-gallery/guia-peruano-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-peruano-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-peruano-sala.jpg',
      '/lovable-uploads/ai-gallery/guia-peruano-plato.jpg',
      '/lovable-uploads/ai-gallery/guia-peruano-barra.jpg',
      '/lovable-uploads/ai-gallery/guia-peruano-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-peruano-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-peruano-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-peruano-sala.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 8 Plantillas + 6 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu restaurante peruano en España, escrito por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    chapters: [
      { icon: 'Building2', num: '01', title: 'Qué es un Restaurante Peruano', desc: 'Cevichería, criollo, Nikkei, Chifa, Novoandino. El fenómeno de la cocina peruana en el mundo y en España.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado de la Cocina Peruana en España 2026', desc: 'Crecimiento +40% en 5 años, ciudades con mayor demanda, perfil del cliente y competencia actual.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio', desc: 'Cevichería pura, restaurante criollo, Nikkei fusion, pollería, chifa, casual peruano y dark kitchen.' },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 130K-300K€, food cost 28-32%, márgenes pisco sour 78%, break-even mes 8-14.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, importación de productos peruanos (ají, pisco), registro sanitario, terraza.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'APPCC para ceviche (pescado crudo), cadena de frío, alérgenos, trazabilidad de importados.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales, metros para 80 plazas, barra de ceviche abierta, barra de piscos.' },
      { icon: 'Layout', num: '08', title: 'Diseño de Cocina Peruana', desc: 'Estación de ceviche, wok para chifa/Nikkei, parrilla para anticuchos, zona de salsas (ají amarillo, rocoto).' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento Específico', desc: 'Mesa refrigerada ceviche, wok industrial, parrilla anticuchos, vitrina de piscos. Costes detallados.' },
      { icon: 'Armchair', num: '10', title: 'Diseño de Sala: Ambiente Peruano', desc: 'Interiorismo moderno con toques peruanos: textiles andinos, cerámica, madera, colores tierra, barra abierta.' },
      { icon: 'GlassWater', num: '11', title: 'Vajilla y Presentación', desc: 'Platos de piedra para ceviche, cuencos de cerámica, vasos de pisco, presentación tipo Lima gourmet.' },
      { icon: 'GlassWater', num: '12', title: 'Barra de Piscos y Coctelería', desc: 'Pisco sour, chilcano, capitán, maracuyá sour. 20-30 referencias de pisco, márgenes 75-80%.' },
      { icon: 'Users', num: '13', title: 'Brigada de Cocina (6-10 personas)', desc: 'Cevichero, wokero, parrillero, cocineros. Salarios España 2026, formación en cocina peruana.' },
      { icon: 'UserCheck', num: '14', title: 'Equipo de Sala (6-8 personas)', desc: 'Servicio con conocimiento de pisco, maridaje, storytelling de platos peruanos, upselling.' },
      { icon: 'UtensilsCrossed', num: '15', title: 'La Carta: Menú Engineering Peruano', desc: 'Ceviches, tiraditos, causas, lomo saltado, ají de gallina, anticuchos. Matrix de rentabilidad.' },
      { icon: 'Flame', num: '16', title: 'Proveedores: Productos Peruanos en España', desc: 'Importadores de ají amarillo, rocoto, maíz morado, pisco, chicha morada. Proveedores nacionales.' },
      { icon: 'Utensils', num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos: ceviche clásico, lomo saltado, causa limeña, ají de gallina, anticuchos.' },
      { icon: 'Truck', num: '18', title: 'Delivery y Take Away Peruano', desc: 'Ceviches no viajan bien, pero causas, lomos, arroces sí. Menú delivery específico, packaging.' },
      { icon: 'Megaphone', num: '19', title: 'Marketing y Posicionamiento', desc: 'Instagram, TikTok, Fiestas Patrias (28 julio), eventos Nikkei, influencers food, Google My Business.' },
      { icon: 'Tablet', num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas, delivery, contabilidad, turnos, carta digital con fotos de platos peruanos.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Chefs, propietarios, inversores y consultores que ya usaron esta guía',
    items: [
      { name: 'Diego Castillo', role: 'Chef peruano, cevichería en Madrid', text: 'Los escandallos de ceviche con food cost real de pescado en España son brutales. El capítulo de proveedores me conectó directamente con importadores de ají amarillo y pisco.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María Gonzáles', role: 'Propietaria de restaurante criollo, Barcelona', text: 'La sección de barra de piscos con márgenes del 78% en pisco sour fue reveladora. Pasé de tener 5 piscos a 25 referencias y la facturación de barra se triplicó.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Andrés Velasco', role: 'Consultor gastronómico, especialista en Latinoamérica', text: 'La mejor guía que he visto sobre cocina peruana en España. Los 6 modelos de negocio (cevichería, criollo, Nikkei, chifa, pollería, dark kitchen) están perfectamente diferenciados.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Isabel Torres', role: 'Inversora, 4 restaurantes en Valencia', text: 'El business plan modelo lo presenté al banco con las proyecciones de la guía. Financiación aprobada en 10 días. Los números del sector peruano en España son muy convincentes.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Roberto Paredes', role: 'Chef Nikkei, formación en Lima y Tokio', text: 'El capítulo de cocina Nikkei es sorprendentemente profundo. La fusión peruano-japonesa es tendencia total en España y esta guía explica cómo montarlo con números reales.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Carmen Delgado', role: 'Diseñadora de interiores para restaurantes', text: 'La sección de interiorismo peruano moderno es excelente. Textiles andinos, cerámica, madera, colores tierra... lejos del cliché, más cerca de lo que piden los clientes hoy.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pablo Quispe', role: 'Importador de productos peruanos, Madrid', text: 'Como importador, puedo confirmar que los proveedores listados en la guía son los principales del mercado español. Ají amarillo, rocoto, maíz morado, pisco... todo correcto.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Laura Mendoza', role: 'Community manager de restaurantes, Málaga', text: 'El capítulo de marketing con Fiestas Patrias, contenido de ceviche en TikTok y eventos de pisco sour me dio ideas para todo el año. El engagement se disparó.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Escrita por un Profesional', desc: 'Chef desde los 17 años y consultor desde 2010, 200+ aperturas asesoradas. Incluye proveedores reales de productos peruanos en España.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (130K-300K€), food cost 28-32%, márgenes pisco sour 78%, break-even calculado y 3 escenarios.' },
      { icon: 'FileSpreadsheet', title: 'Incluye Plantillas por Valor de 80€+', desc: 'Plan financiero, escandallos de ceviche/lomo saltado/causa, menú engineering, Gantt y más — todo en Excel.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000-10.000€', desc: 'La misma información que reciben los clientes de consultoría gastronómica, en formato guía por un pago único de 65€.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos en España y Europa, incluyendo restaurantes de cocina internacional y cevicherías.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Incluye sección específica de cocina peruana y proveedores de importación.', image: '/lovable-uploads/ai-gallery/guia-peruano-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual de Operaciones Peruano', value: '39 EUR', desc: 'Protocolo completo: cevichería, anticuchería, barra de piscos, preparación de leche de tigre, delivery, eventos temáticos (Fiestas Patrias).', image: '/lovable-uploads/ai-gallery/guia-peruano-sala.jpg' },
      { icon: 'ClipboardCheck', label: 'BONUS 3', title: 'Checklist Equipamiento Cocina Peruana', value: '29 EUR', desc: '35 ítems específicos: mesa refrigerada ceviche, wok industrial, parrilla anticuchos, vitrina piscos, molino de ajíes.', image: '/lovable-uploads/ai-gallery/guia-peruano-cocina.jpg' },
      { icon: 'CalendarRange', label: 'BONUS 4', title: 'Cronograma de Apertura Gantt 12 Meses', value: '24 EUR', desc: 'Fases específicas para peruano: importación de productos, diseño de cevichería, formación en cocina peruana, soft opening.', image: '/lovable-uploads/ai-gallery/guia-peruano-barra.jpg' },
      { icon: 'PieChart', label: 'BONUS 5', title: 'Escandallos: 15 Recetas Base Peruanas', value: '19 EUR', desc: 'Fichas técnicas con food cost real: ceviche clásico, lomo saltado, causa limeña, ají de gallina, anticuchos, suspiro limeño.', image: '/lovable-uploads/ai-gallery/guia-peruano-plato.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu restaurante peruano, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar un restaurante peruano en España?', a: 'Entre 130.000€ y 300.000€ dependiendo de la ubicación, nivel de acabados y si incluyes barra de piscos premium. La estación de ceviche refrigerada y la importación de productos peruanos añaden coste, pero los márgenes en coctelería (pisco sour 78%) lo compensan.' },
    { q: '¿Dónde consigo productos peruanos auténticos en España?', a: 'La guía incluye un capítulo completo (cap. 16) con proveedores de importación de ají amarillo, rocoto, maíz morado, pisco, chicha morada y más. Hay importadores especializados en Madrid, Barcelona y distribución nacional.' },
    { q: '¿Cevichería pura o restaurante peruano completo?', a: 'Depende de la zona y el ticket. Una cevichería pura tiene menor inversión y carta más enfocada. Un peruano completo (criollo + Nikkei + ceviches) tiene ticket más alto y mayor atracción. La guía analiza los 6 modelos en detalle.' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 8 plantillas incluyen fórmulas automáticas: plan financiero, escandallos de 15 platos peruanos clave (ceviche, lomo saltado, causa), menú engineering con coctelería de pisco, cash flow y más.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Restaurante a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta un ceviche para cuatro.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual de operaciones peruano',
      'Escandallos de 15 recetas base peruanas',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'GUÍA RESTAURANTE PERUANO — 65 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Guía Restaurante Mexicano', href: '/guia-restaurante-mexicano' },
    { label: 'Guía Restaurante Casual', href: '/guia-restaurante-casual' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  alreadyBought: {
    product: 'guia-restaurante-peruano',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar un Restaurante Peruano 80 Plazas — Guía Completa España',
    productDescription: 'Guía premium de 20 capítulos para montar un restaurante peruano: cevichería, Nikkei, barra de piscos, proveedores peruanos en España. Incluye 8 plantillas Excel, 6 checklists, business plan y manual de operaciones.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar un restaurante peruano en España?', a: 'Entre 130.000€ y 300.000€ para 80 plazas. La estación de ceviche y barra de piscos añaden inversión, pero los márgenes en coctelería (78%) compensan.' },
      { q: '¿Dónde consigo productos peruanos auténticos en España?', a: 'La guía incluye un capítulo completo con proveedores de ají amarillo, rocoto, maíz morado, pisco y chicha morada con distribución nacional.' },
      { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Plan financiero a 3 años, escandallos de 15 platos peruanos, menú engineering con coctelería de pisco, cash flow y break-even.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Restaurante Peruano', item: 'https://aichef.pro/guia-restaurante-peruano' },
    ],
  },
};

export default data;
