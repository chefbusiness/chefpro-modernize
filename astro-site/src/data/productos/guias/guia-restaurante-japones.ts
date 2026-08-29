// guia-restaurante-japones.ts — Producto de la línea Guías "Cómo Montar".
// Copy VERBATIM de src/pages/GuiaRestauranteJapones.tsx + componentes de
// src/components/guia-restaurante-japones/* + data/testimonials-guia-restaurante-japones.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
// Sin divergencias estructurales: showCompatibleApps=false (no lo tiene), bonus.layout='split'
// (5 bonus, igual que gastronómico), avatarAltPrefix/testimonials.titleGold = defaults ('Professional'/'Profesionales').
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-restaurante-japones',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_JAPONES',

  seo: {
    title: 'Cómo Montar un Restaurante Japonés 60 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium para montar un restaurante japonés en España: 20 capítulos, 60+ páginas, sushi-ya, ramen-ya, izakaya, omakase, robatayaki, proveedores pescado sashimi-grade. 8 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    keywords: 'como montar restaurante japones españa, abrir sushi bar, restaurante japones autentico, ramen-ya, izakaya, omakase, robatayaki, proveedores pescado sashimi grade, anisakis, sake, whisky japones, plan financiero restaurante japones, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg',
  },

  hero: {
    badge: 'La cocina japonesa es Patrimonio UNESCO — la segunda más demandada en España con ticket premium',
    titlePre: 'Cómo Montar un ',
    titleGold: 'Restaurante Japonés',
    subtitleLine: '60 Plazas · Guía Completa España',
    description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para abrir tu sushi-ya, ramen-ya, izakaya, omakase o robatayaki en España.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas: plan financiero, escandallos, menú engineering',
      '6 checklists de apertura: legal, equipamiento, APPCC anisakis, sala, contratación, marketing',
      'Business Plan modelo para presentar a bancos e inversores',
      'Manual de operaciones: sushi-ya, ramen, izakaya, omakase, robatayaki, barra sake',
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
      '/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-japones-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-japones-sala.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-japones-plato.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-japones-barra.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-japones-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-restaurante-japones-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-restaurante-japones-sala.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 8 Plantillas + 6 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu restaurante japonés en España, escrito por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    chapters: [
      { icon: 'Building2', num: '01', title: 'Qué es un Restaurante Japonés', desc: 'Sushi-ya, ramen-ya, izakaya, omakase, robatayaki. El universo de la cocina japonesa premium en España.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado Japonés en España 2026', desc: 'Crecimiento +35% en 5 años, ciudades con mayor demanda, omakase con listas de espera, público foodie.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio', desc: 'Sushi-ya, ramen-ya, izakaya, omakase premium, robatayaki, mixto y dark kitchen japonesa.' },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 250K-500K€, food cost 30-35%, márgenes sake/whisky 75-85%, break-even mes 10-16.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales + Normativa Anisakis', desc: 'Licencias, congelación preventiva anti-anisakis (RD 1021/2022, art. 8.1) -20°C/24h, importación, registro sanitario.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC para Pescado Crudo y Shari', desc: 'APPCC con PCC específicos: anisakis, temperatura arroz sushi, caldos ramen, alérgenos.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales, metros para 60 plazas, barra sushi, proximidad a mercados de pescado fresco.' },
      { icon: 'Layout', num: '08', title: 'Diseño de Cocina Japonesa', desc: 'Barra de sushi, estación shari, ramen station, robata binchotan, teppanyaki, zona tempura.' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento Específico Japonés', desc: 'Suihanki, vitrina sashimi, ramen cooker, robata, teppanyaki, cuchillos yanagiba/deba/usuba. Costes.' },
      { icon: 'Armchair', num: '10', title: 'Diseño de Sala: Estética Japonesa', desc: 'Wabi-sabi, ma, shibui. Madera natural, lámparas washi, jardín zen, bambú, minimalismo.' },
      { icon: 'GlassWater', num: '11', title: 'Vajilla y Presentación', desc: 'Cerámica japonesa artesanal, asimetría wabi-sabi, platos de pizarra, presentación tipo kaiseki.' },
      { icon: 'GlassWater', num: '12', title: 'Barra de Sake y Whisky Japonés', desc: 'Junmai, Ginjo, Daiginjo, Nigori + whisky Yamazaki/Hibiki. 30-50 refs, márgenes 75-85%.' },
      { icon: 'Users', num: '13', title: 'Brigada de Cocina (8-12 personas)', desc: 'Itamae, sushi chef, ramen cook, robata cook, tempura cook. Salarios España 2026.' },
      { icon: 'UserCheck', num: '14', title: 'Equipo de Sala (5-8 personas)', desc: 'Servicio con protocolo japonés, sommelier de sake, storytelling, upselling de whisky japonés.' },
      { icon: 'UtensilsCrossed', num: '15', title: 'La Carta: Menú Engineering Japonés', desc: 'Sashimi, nigiri, maki, ramen, yakitori, tempura, katsu. Matrix de rentabilidad.' },
      { icon: 'Flame', num: '16', title: 'Proveedores: Productos Japoneses en España', desc: 'Distribuidores de pescado sashimi-grade, arroz Koshihikari, algas nori, sake, whisky japonés.' },
      { icon: 'Utensils', num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos: sashimi moriawase, ramen tonkotsu, tempura, yakitori, katsu.' },
      { icon: 'Truck', num: '18', title: 'Delivery y Take Away Japonés', desc: 'Sushi boxes, bowls, katsudon, gyoza. Ramen especial. Packaging premium japonés.' },
      { icon: 'Megaphone', num: '19', title: 'Marketing y Calendario Cultural', desc: 'Instagram, TikTok, Hanami (marzo), Día del Sushi (18 junio), eventos de cata de sake.' },
      { icon: 'Tablet', num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas con depósito para omakase, delivery, contabilidad, turnos, carta de sakes.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Itamae, chefs, propietarios, inversores y consultores que ya usaron esta guía',
    items: [
      { name: 'Kenji Tanaka', role: 'Itamae, sushi-ya en Madrid', text: 'La guía me dio el plan financiero y el checklist APPCC específico para sashimi y anisakis que necesitaba para presentar al inversor. Los escandallos con food cost real de pescado sashimi-grade en España son precisos.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Elena Fujimoto', role: 'Propietaria omakase, Barcelona', text: 'Abrí un omakase de 12 plazas siguiendo esta guía. La sección de barra de sake y whisky japonés me ayudó a montar 40 referencias con márgenes del 78%. El ticket medio subió un 40% el primer trimestre.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Hiroshi Yamamoto', role: 'Chef ramen, ramen-ya en Valencia', text: 'La mejor guía sobre cocina japonesa en España. El capítulo de modelos de negocio diferencia perfectamente sushi-ya, ramen-ya, izakaya y omakase. Elegí ramen-ya puro y tengo cola diaria de 60 min.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Marta Saavedra', role: 'Inversora, 3 restaurantes japoneses en Málaga', text: 'El business plan modelo lo presenté al banco con las proyecciones de la guía. Financiación aprobada en dos semanas. Los números del sector japonés premium en España son muy convincentes.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Akira Watanabe', role: 'Sushi chef, formación en Tokio', text: 'El protocolo de anisakis y congelación preventiva está perfectamente explicado. La sección de arroz sushi (shari) con temperaturas del ohitsu es la más precisa que he visto en una guía en español.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Laura Bermejo', role: 'Interiorista especializada en restaurantes premium', text: 'El capítulo de decoración japonesa basado en wabi-sabi, ma y shibui es excelente. Madera, washi, jardín zen y minimalismo — lejos de los clichés de geishas y dragones. Me ha servido para 2 proyectos.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Daniel Moreno', role: 'Distribuidor pescado sashimi-grade, Mercamadrid', text: 'Como proveedor de pescado para sushi, puedo confirmar que los proveedores y precios listados en la guía son realistas. La parte de trazabilidad y normativa anisakis está impecable.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Patricia Okamoto', role: 'Sommelier de sake certificada WSET, Bilbao', text: 'El capítulo de barra de sake y whisky japonés con las 30-50 referencias recomendadas, los márgenes del 75-85% y los vuelos de sake me dio ideas que aplicamos el mismo mes. La facturación de barra se duplicó.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Escrita por un Profesional', desc: 'Chef desde los 17 años y consultor desde 2010, 200+ aperturas asesoradas. Incluye proveedores reales de pescado sashimi-grade y productos japoneses en España.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (250K-500K€), food cost 30-35%, márgenes sake/whisky 75-85%, break-even calculado y 3 escenarios.' },
      { icon: 'FileSpreadsheet', title: 'Incluye Plantillas por Valor de 80€+', desc: 'Plan financiero, escandallos de sashimi/ramen/yakitori, menú engineering, Gantt y más — todo en Excel.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000-10.000€', desc: 'La misma información que reciben los clientes de consultoría gastronómica, en formato guía por un pago único de 65€.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos en España y Europa, incluyendo restaurantes de cocina internacional, sushi-ya, ramen-ya y omakase premium.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Incluye sección específica de cocina japonesa premium y proveedores.', image: '/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual de Operaciones Japonés', value: '39 EUR', desc: 'Protocolo completo: barra de sushi, estación shari, ramen, robatayaki, barra de sake, anisakis, delivery y alérgenos japoneses.', image: '/lovable-uploads/ai-gallery/guia-restaurante-japones-sala.jpg' },
      { icon: 'ClipboardCheck', label: 'BONUS 3', title: 'Checklist Equipamiento Cocina Japonesa', value: '29 EUR', desc: '36 ítems específicos: suihanki, vitrina refrigerada sashimi, ramen cooker, robata binchotan, cuchillos yanagiba/deba/usuba.', image: '/lovable-uploads/ai-gallery/guia-restaurante-japones-cocina.jpg' },
      { icon: 'CalendarRange', label: 'BONUS 4', title: 'Cronograma de Apertura Gantt 12 Meses', value: '24 EUR', desc: 'Fases específicas para japonés: búsqueda del itamae, contacto proveedores pescado sashimi-grade, formación, soft opening.', image: '/lovable-uploads/ai-gallery/guia-restaurante-japones-barra.jpg' },
      { icon: 'PieChart', label: 'BONUS 5', title: 'Escandallos: 15 Recetas Base Japonesas', value: '19 EUR', desc: 'Fichas técnicas con food cost real: sashimi moriawase, nigiri, ramen tonkotsu, gyoza, yakitori wagyu, tempura, katsu.', image: '/lovable-uploads/ai-gallery/guia-restaurante-japones-plato.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu restaurante japonés, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar un restaurante japonés en España?', a: 'Entre 250.000€ y 500.000€ dependiendo de la ubicación, nivel de acabados, modelo (sushi-ya, ramen-ya, izakaya, omakase, robatayaki) y equipamiento japonés específico (suihanki, vitrina sashimi, robata, cuchillos yanagiba). Los márgenes en sake premium y whisky japonés (75-85%) ayudan a compensar el coste del pescado fresco.' },
    { q: '¿Dónde consigo pescado sashimi-grade y productos japoneses en España?', a: 'La guía incluye un capítulo completo (cap. 15) con proveedores: Mercamadrid, Mercabarna, lonjas, distribuidores especializados (Japan Sushi Express, Oriental Gourmet, Comercial Minamoto) y importadores directos de pescado premium, arroz Koshihikari, algas nori, sake y whisky japonés.' },
    { q: '¿Qué normativa debo cumplir para sushi y sashimi (anisakis)?', a: 'El RD 1021/2022, art. 8.1 (que derogó el RD 1420/2006) OBLIGA a congelar preventivamente todo pescado para consumo crudo a -20°C durante mínimo 24 horas en todo el producto, o -35°C durante 15 horas. La guía incluye un PCC específico en el plan APPCC, el checklist de anisakis y el protocolo completo de trazabilidad. Es crítico: un caso positivo puede cerrar tu restaurante.' },
    { q: '¿Sushi-ya, ramen-ya, izakaya u omakase?', a: 'Depende de tu inversión, equipo y zona. Un ramen-ya tiene menor inversión y carta enfocada. Un sushi-ya exige un itamae cualificado pero ofrece máximo prestigio. Un omakase premium tiene ticket 80-180€ pero requiere barra de 8-14 plazas. La guía analiza los 7 modelos en detalle.' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 8 plantillas incluyen fórmulas automáticas: plan financiero, escandallos de 15 platos japoneses (sashimi, ramen, nigiri, yakitori wagyu), menú engineering con coctelería de sake/whisky, cash flow y más.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Restaurante a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta un omakase para dos.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual de operaciones japonés',
      'Escandallos de 15 recetas base japonesas',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'GUÍA RESTAURANTE JAPONÉS — 65 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Guía Restaurante Peruano', href: '/guia-restaurante-peruano' },
    { label: 'Guía Restaurante Mexicano', href: '/guia-restaurante-mexicano' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'guia-restaurante-japones',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar un Restaurante Japonés 60 Plazas — Guía Completa España',
    productDescription: 'Guía premium de 20 capítulos para montar un restaurante japonés: sushi-ya, ramen-ya, izakaya, omakase, robatayaki, proveedores de pescado sashimi-grade en España. Incluye 8 plantillas Excel, 6 checklists, business plan y manual de operaciones.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar un restaurante japonés en España?', a: 'Entre 250.000€ y 500.000€ para 60 plazas. El equipamiento japonés específico (suihanki, vitrina sashimi, robata, teppanyaki, cuchillos japoneses) y el itamae cualificado suponen la mayor parte del coste, pero los márgenes en sake y whisky japonés (75-85%) lo compensan.' },
      { q: '¿Qué normativa debo cumplir para sushi y sashimi?', a: 'El RD 1021/2022, art. 8.1 (que derogó el RD 1420/2006) OBLIGA a congelar preventivamente todo pescado para consumo crudo a -20°C durante mínimo 24 horas en todo el producto, o -35°C durante 15 horas (anisakis). La guía incluye el PCC completo, el checklist y el protocolo de trazabilidad.' },
      { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Plan financiero a 3 años, escandallos de 15 platos japoneses, menú engineering con coctelería de sake y whisky, cash flow y break-even.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Restaurante Japonés', item: 'https://aichef.pro/guia-restaurante-japones' },
    ],
  },
};

export default data;
