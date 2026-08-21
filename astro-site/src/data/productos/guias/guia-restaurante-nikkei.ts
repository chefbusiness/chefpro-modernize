// guia-restaurante-nikkei.ts — LÍNEA GUÍAS "Cómo Montar".
// Copy VERBATIM de src/pages/GuiaRestauranteNikkei.tsx + componentes de
// src/components/guia-restaurante-nikkei/* + data/testimonials-guia-restaurante-nikkei.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
// Sin divergencias estructurales: showCompatibleApps=false (default), avatarAltPrefix='Professional'
// (default), testimonials.titleGold='Profesionales' (default), bonus.layout='split' (5 bonus),
// breadcrumb de 3 ítems — todos coinciden con los defaults de la línea.
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-restaurante-nikkei',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_NIKKEI',

  seo: {
    title: 'Cómo Montar un Restaurante Nikkei 60 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium para montar un restaurante nikkei (fusión peruano-japonesa) en España: 20 capítulos, tiraditos, ceviches nikkei, omakase, barra de pisco y sake. 9 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    keywords: 'como montar restaurante nikkei españa, cocina nikkei fusion peruano japonesa, tiraditos, ceviche nikkei, omakase nikkei, leche de tigre, aji amarillo, barra pisco sake, proveedores pescado sashimi grade españa, anisakis, plan financiero restaurante nikkei, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
  },

  hero: {
    badge: 'Cocina nikkei: la fusión peruano-japonesa más deseada del mundo — tendencia premium alcista en España',
    titlePre: 'Cómo Montar un ',
    titleGold: 'Restaurante Nikkei',
    subtitleLine: '60 Plazas · Guía Completa España',
    description: 'Guía completa con 20 capítulos, 60+ páginas, 9 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para abrir tu barra de tiraditos, cevichería nikkei, robata nikkei u omakase peruano-japonés en España. Referentes: Nobu, Maido, Osaka, Pakta.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)',
      '9 plantillas Excel con fórmulas: plan financiero, escandallos nikkei, menú engineering',
      '6 checklists: legal, equipamiento cocina nikkei, APPCC anisakis + leche de tigre, sala, contratación, marketing',
      'Business Plan modelo para presentar a bancos e inversores',
      'Manual de operaciones: barra tiraditos, cold station leche de tigre, robata, cocina caliente, barra pisco/sake',
    ],
    ctaLabel: 'COMPRAR GUÍA — 65 EUR',
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
      '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-sala.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-plato.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-barra.jpg',
      '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-sala.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 9 Plantillas + 6 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu restaurante nikkei en España, escrito por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    chapters: [
      { icon: 'Building2', num: '01', title: 'Qué es la Cocina Nikkei', desc: 'Fusión peruano-japonesa nacida en Perú (siglo XIX). Referentes: Nobu, Maido, Osaka, Pakta. Identidad y técnica.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado Nikkei en España 2026', desc: 'Tendencia premium alcista, ciudades clave, omakase nikkei con lista de espera, público foodie 30-50.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio Nikkei', desc: 'Barra de tiraditos, cevichería nikkei, robata nikkei, omakase premium, casual premium, dark kitchen nikkei.' },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 280K-520K€, food cost 32-34%, márgenes pisco/sake 75-85%, break-even mes 10-16.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales + Normativa Anisakis', desc: 'Licencias, RD 1420/2006 congelación preventiva -20°C/24h para tiraditos, importación peruana, registro sanitario.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC Pescado Crudo + Leche de Tigre', desc: 'PCC específicos: anisakis tiraditos, cadena de frío leches de tigre, shari, alérgenos, ají.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas premium urbanas, metros para 60 plazas, barra tiraditos visible, proximidad mercados pescado.' },
      { icon: 'Layout', num: '08', title: 'Diseño de Cocina Nikkei', desc: 'Barra tiraditos, cold station leche de tigre, robata/josper, wok chaufa, hot kitchen anticuchos.' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento Específico Nikkei', desc: 'Vitrina sashimi, robata/josper, wok station, licuadoras leches de tigre, yanagiba, molcajete, teppanyaki.' },
      { icon: 'Armchair', num: '10', title: 'Diseño de Sala: Estética Nikkei', desc: 'Fusión: madera japonesa minimalista + textiles peruanos, cerámica Chulucanas, iluminación cálida, barra tiraditos protagonista.' },
      { icon: 'GlassWater', num: '11', title: 'Vajilla y Presentación', desc: 'Cerámica japonesa artesanal + cerámica peruana Chulucanas. Asimetría, pizarras, presentación de autor.' },
      { icon: 'GlassWater', num: '12', title: 'Barra de Pisco, Sake y Coctelería Nikkei', desc: 'Pisco puro/acholado, sakes Junmai/Ginjo, 40 refs, pisco sours, chilcanos, maridaje tiraditos. Márgenes 75-85%.' },
      { icon: 'Users', num: '13', title: 'Brigada de Cocina (14-18 personas)', desc: 'Chef ejecutivo, itamae nikkei, parrillero robata, cold station leches de tigre, hot kitchen chaufa/anticuchos, pastelería.' },
      { icon: 'UserCheck', num: '14', title: 'Equipo de Sala (6-9 personas)', desc: 'Servicio cálido, sommelier pisco/sake, storytelling nikkei, upselling de maridajes.' },
      { icon: 'UtensilsCrossed', num: '15', title: 'La Carta: Menú Engineering Nikkei', desc: 'Tiraditos, ceviches nikkei, causas, makis acevichados, tatakis, anticuchos, chaufa, postres. Matrix de rentabilidad.' },
      { icon: 'Flame', num: '16', title: 'Proveedores: Productos Peruanos y Japoneses en España', desc: 'Inkawasi, Latin Products (ají amarillo/limo/rocoto), pescado sashimi-grade Mercamadrid, arroz Koshihikari, nori, pisco, sake.' },
      { icon: 'Utensils', num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos nikkei: tiradito clásico, ceviche nikkei, causa, maki acevichado, tataki atún, anticucho, chaufa mariscos.' },
      { icon: 'Truck', num: '18', title: 'Delivery y Take Away Nikkei', desc: 'Sushi/tiradito boxes, ceviche en frío, bowls, chaufa. Packaging premium que preserve temperatura y textura.' },
      { icon: 'Megaphone', num: '19', title: 'Marketing y Calendario Cultural', desc: 'Instagram, TikTok, Día del Pisco Sour, Fiestas Patrias Perú (28 julio), eventos cata pisco/sake, colaboraciones con chefs nikkei.' },
      { icon: 'Tablet', num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas con depósito para omakase, delivery, contabilidad, turnos, carta digital.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Itamae, chefs, propietarios, inversores y consultores que ya usaron esta guía',
    items: [
      { name: 'Mitsuharu Nakasone', role: 'Chef nikkei, restaurante en Madrid', text: 'Esta guía me resolvió las dudas clave: proveedores de ají amarillo y rocoto en España, protocolo anisakis para tiraditos y leches de tigre, y escandallos reales con el coste del pescado premium mediterráneo. El business plan lo presenté al inversor y cerramos la ronda.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Valeria Tsumura', role: 'Propietaria cevichería-nikkei, Barcelona', text: 'Monté una barra nikkei de 60 plazas siguiendo la guía. La sección de tiraditos + causas nikkei + makis acevichados con menú engineering me ayudó a fijar un ticket medio de 58€. Margen bruto 66%. Invaluable.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Diego Matsufuji', role: 'Itamae nikkei, omakase en Valencia', text: 'La mejor guía sobre nikkei en español. Diferencia con claridad el nikkei tradicional de Lima, la escuela Nobu y la evolución contemporánea (Maido, Osaka). El capítulo de pescado sashimi-grade y leches de tigre es oro.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucía Benavides', role: 'Inversora, 2 restaurantes nikkei en Málaga', text: 'Presenté el business plan modelo al banco y obtuvimos financiación en 3 semanas. Los números del nikkei premium en España (ticket 65-85€, food cost 33%, break-even mes 12) son realistas y convincentes.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Akira Shimabukuro', role: 'Chef consultor nikkei, formación en Lima', text: 'El protocolo APPCC con PCC específico para pescado crudo y leches de tigre es lo mejor que he visto en una guía en español. Incluye temperaturas, tiempos, registros y trazabilidad. 100% implementable.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Claudia Ferrari', role: 'Interiorista especializada en restaurantes premium', text: 'El capítulo de diseño de sala nikkei (fusión estética japonesa minimalista + textiles peruanos + cerámica Chulucanas) es brillante. Lejos del cliché. Lo he aplicado en 2 proyectos en Madrid.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Javier Quispe', role: 'Importador de productos peruanos en España', text: 'Como proveedor de ají amarillo, limo y rocoto en España, confirmo que los proveedores y precios listados son reales y están actualizados. Lo recomiendo a todos mis clientes que abren nikkei.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Ricardo Miyashiro', role: 'Sommelier de pisco y sake, Bilbao', text: 'El capítulo de barra de pisco + sake + coctelería nikkei es excelente. Las 40 referencias recomendadas, los maridajes con tiraditos y los márgenes del 75-85% me dieron ideas que implementamos el mismo mes. Barra rentable.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Escrita por un Profesional', desc: 'Chef desde los 17 años y consultor desde 2010, 200+ aperturas asesoradas. Incluye proveedores reales de ají peruano, pescado sashimi-grade y pisco en España.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (280K-520K€), food cost 32-34%, márgenes pisco/sake/coctelería 75-85%, break-even mes 10-16 y 3 escenarios.' },
      { icon: 'FileSpreadsheet', title: 'Incluye Plantillas por Valor de 80€+', desc: 'Plan financiero, escandallos de tiraditos/ceviches/anticuchos, menú engineering, Gantt y más — todo en Excel.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000-10.000€', desc: 'La misma información que reciben los clientes de consultoría gastronómica, en formato guía por un pago único de 65€.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos en España y Europa, incluyendo restaurantes de cocina internacional, cevicherías, nikkei y omakase premium de fusión peruano-japonesa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Incluye sección específica de cocina nikkei premium y proveedores peruanos en España.', image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual de Operaciones Nikkei', value: '39 EUR', desc: 'Protocolo completo: barra de tiraditos, cold station leche de tigre, robata, cocina caliente (chaufa/anticuchos), barra pisco/sake, anisakis, delivery y alérgenos.', image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-sala.jpg' },
      { icon: 'ClipboardCheck', label: 'BONUS 3', title: 'Checklist Equipamiento Cocina Nikkei', value: '29 EUR', desc: '36 ítems específicos: vitrina sashimi, robata/josper, wok station, licuadoras leche de tigre, cuchillos yanagiba/deba, molcajete, teppanyaki.', image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-cocina.jpg' },
      { icon: 'CalendarRange', label: 'BONUS 4', title: 'Cronograma de Apertura Gantt 12 Meses', value: '24 EUR', desc: 'Fases específicas nikkei: búsqueda del chef nikkei, contacto importadores de ají peruano y pescado sashimi-grade, formación, soft opening.', image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-barra.jpg' },
      { icon: 'PieChart', label: 'BONUS 5', title: 'Escandallos: 15 Recetas Base Nikkei', value: '19 EUR', desc: 'Fichas técnicas con food cost real: tiradito clásico, ceviche nikkei, causa nikkei, maki acevichado, tataki de atún, anticucho, chaufa de mariscos.', image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-plato.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu restaurante nikkei, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar un restaurante nikkei en España?', a: 'Entre 280.000€ y 520.000€ para 60 plazas, dependiendo de la ubicación, nivel de acabados y modelo (cevichería nikkei, barra tiraditos, omakase, casual premium). El equipamiento mixto (robata/josper, wok station, licuadoras para leches de tigre, yanagiba, molcajete) y la brigada especializada son los mayores costes. Los márgenes de pisco, sake y coctelería nikkei (75-85%) compensan el food cost del pescado premium.' },
    { q: '¿Dónde consigo ají amarillo, rocoto, pisco y productos peruanos en España?', a: 'La guía incluye directorio completo de importadores peruanos en España (Inkawasi, Latin Products y otros) para ají amarillo, ají limo, rocoto, maíz gigante, choclo, quinoa y salsas nikkei. Para pescado sashimi-grade: Mercamadrid, Mercabarna y Krustagroup. Para arroz Koshihikari, nori, sake: Japan Sushi Express, Oriental Gourmet. Pisco peruano: distribuidores especializados.' },
    { q: '¿Qué normativa aplica a tiraditos, ceviches nikkei y leches de tigre?', a: 'El RD 1420/2006 OBLIGA a congelar preventivamente todo pescado destinado a ser consumido crudo o marinado (tiraditos, ceviches nikkei, sashimi) a -20°C durante mínimo 24 horas. La guía incluye un PCC específico para pescado crudo Y para leches de tigre (cadena de frío), checklist anisakis y protocolo completo de trazabilidad.' },
    { q: '¿Cevichería nikkei, omakase nikkei o casual premium?', a: 'Depende de inversión, equipo y zona. Una cevichería nikkei tiene ticket 45-65€ y alta rotación. Un omakase nikkei tiene ticket 90-150€ pero requiere barra de 10-14 plazas y chef de máximo nivel. Un casual premium de 60 plazas balancea carta amplia y rentabilidad. La guía analiza los 6 modelos en detalle.' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 9 plantillas incluyen fórmulas automáticas: plan financiero a 3 años, escandallos de 15 platos nikkei (tiradito, ceviche nikkei, causa, maki acevichado, anticucho, chaufa mariscos), menú engineering con coctelería de pisco y sake, cash flow y break-even.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Restaurante a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta un omakase para dos.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)',
      '9 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual de operaciones nikkei',
      'Escandallos de 15 recetas base nikkei',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'GUÍA RESTAURANTE NIKKEI — 65 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Guía Restaurante Peruano', href: '/guia-restaurante-peruano' },
    { label: 'Guía Restaurante Mexicano', href: '/guia-restaurante-mexicano' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  alreadyBought: {
    product: 'guia-restaurante-nikkei',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar un Restaurante Nikkei 60 Plazas — Guía Completa España',
    productDescription: 'Guía premium de 20 capítulos para montar un restaurante nikkei (fusión peruano-japonesa): tiraditos, ceviches nikkei, omakase, barra de pisco y sake, proveedores de ají amarillo, rocoto y pescado sashimi-grade en España. Incluye 9 plantillas Excel, 6 checklists, business plan y manual de operaciones.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar un restaurante nikkei en España?', a: 'Entre 280.000€ y 520.000€ para 60 plazas. El equipamiento mixto (barra de tiraditos, robata/josper, wok station, licuadoras para leches de tigre, cuchillos yanagiba y molcajete) y la brigada especializada son el mayor coste, pero los márgenes en pisco, sake y coctelería nikkei (75-85%) lo compensan.' },
      { q: '¿Qué normativa de anisakis aplica a tiraditos y leches de tigre?', a: 'El RD 1420/2006 OBLIGA a congelar preventivamente todo pescado para consumo crudo (incluidos tiraditos, ceviches nikkei y marinados en leche de tigre) a -20°C durante mínimo 24 horas. La guía incluye PCC específico, checklist y protocolo de trazabilidad.' },
      { q: '¿Dónde consigo ají amarillo, rocoto y productos peruanos en España?', a: 'La guía incluye directorio de importadores peruanos en España (Inkawasi, Latin Products y otros), productos japoneses (arroz Koshihikari, sake, nori) y pescado sashimi-grade en Mercamadrid/Mercabarna.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Restaurante Nikkei', item: 'https://aichef.pro/guia-restaurante-nikkei' },
    ],
  },
};

export default data;
