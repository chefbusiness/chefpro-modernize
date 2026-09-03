// guia-restaurante-gastronomico.ts — PRODUCTO DE REFERENCIA de la línea Guías "Cómo Montar".
// Copy VERBATIM de src/pages/GuiaRestauranteGastronomico.tsx + componentes de
// src/components/guia-restaurante-gastronomico/* + data/testimonials-guia-restaurante-gastronomico.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-restaurante-gastronomico',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_GASTRONOMICO',

  seo: {
    title: 'Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España (Michelin · Sol Repsol) | AI Chef Pro',
    description: 'Guía premium para montar un restaurante gastronómico en España: 22 capítulos, 119 páginas, plan financiero, diseño de cocina y sala, brigada, bodega, Michelin, Sol Repsol. 10 plantillas Excel + 8 checklists + business plan. 85 EUR.',
    keywords: 'como montar restaurante gastronomico, abrir restaurante fine dining, estrella michelin requisitos, sol repsol restaurante, plan financiero restaurante, equipamiento cocina profesional, brigada cocina, restaurante 65 plazas, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-gastro-hero.jpg',
  },

  hero: {
    badge: 'Solo el 15% de los restaurantes gastronómicos supera los 3 años — los que planifican bien, lo logran',
    titlePre: 'Cómo Montar un ',
    titleGold: 'Restaurante Gastronómico',
    subtitleLine: '65 Plazas · Guía Completa España (Michelin · Sol Repsol)',
    description: 'Guía completa con 22 capítulos, 119 páginas, 10 plantillas Excel, 8 checklists, business plan modelo y manual de servicio. Todo para abrir tu restaurante fine dining.',
    checkItems: [
      'Guía completa PDF + DOCX editable (22 capítulos, 119 páginas)',
      '10 plantillas Excel con fórmulas: plan financiero, escandallos, menú engineering',
      '8 checklists de apertura incluyendo preparación Michelin y Sol Repsol',
      'Business Plan modelo para presentar a bancos e inversores',
      'Manual de servicio de sala: protocolo completo fine dining',
    ],
    ctaLabel: 'COMPRAR GUÍA — 85 EUR',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    priceOld: '220 EUR',
    price: '85 EUR',
    discountBadge: '-61%',
    heroNote: 'Precio de lanzamiento — ahorra 135 EUR',
    buyBoxNote: 'Precio de lanzamiento — ahorra 135 EUR',
    bonusTotalLabel: 'Valor total: guía + 5 bonus',
    bonusSaveLine: 'Ahorra 135 EUR HOY',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-gastro-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-gastro-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-gastro-sala.jpg',
      '/lovable-uploads/ai-gallery/guia-gastro-plato.jpg',
      '/lovable-uploads/ai-gallery/guia-gastro-bodega.jpg',
      '/lovable-uploads/ai-gallery/guia-gastro-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-gastro-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-gastro-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-gastro-sala.jpg',
  },

  grid: {
    countGold: '22',
    headingRest: ' Capítulos + 10 Plantillas + 8 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu restaurante gastronómico en España, escrito por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    chapters: [
      { icon: 'Building2', num: '01', title: 'Qué es un Restaurante Gastronómico', desc: 'Definición, categorías (fine dining, casual fine, tasting menu) y diferencias con la restauración convencional.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado de la Alta Cocina en España 2026', desc: 'Datos del sector, ticket medio, tendencias de gasto y ciudades con mayor demanda gastronómica.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio', desc: "Menú degustación, carta premium, omakase, chef's table. Pros, contras y márgenes de cada formato." },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 500K-900K€, P&L mensual, food cost 25-28%, break-even y proyecciones a 3 años.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, registro sanitario, Hacienda, seguros, LOPD, normativa de terraza y alcohol.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC obligatorio, trazabilidad premium, alérgenos, control de temperaturas y auditorías.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas prime, metros mínimos para 65 plazas, accesibilidad, aparcamiento y entorno competitivo.' },
      { icon: 'Layout', num: '08', title: 'Diseño de Cocina Profesional', desc: 'Flujo de trabajo fine dining: recepción, mise en place, partidas, pase y emplatado de precisión.' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento de Cocina', desc: 'Lista completa con costes: hornos Rational, Thermomix, abatidores, Pacojet, Roner, plancha Josper.' },
      { icon: 'Armchair', num: '10', title: 'Diseño de Sala para 65 Plazas', desc: 'Distribución, iluminación, acústica, mobiliario premium, interiorismo y experiencia del comensal.' },
      { icon: 'GlassWater', num: '11', title: 'Vajilla, Cristalería y Cubertería Premium', desc: 'Selección de marcas (Riedel, Zwiesel, RAK), inversión por cubierto y reposición anual.' },
      { icon: 'Wine', num: '12', title: 'Bodega y Servicio de Vinos', desc: 'Diseño de carta de vinos, maridajes, almacenamiento, sommelier y márgenes por copa/botella.' },
      { icon: 'Users', num: '13', title: 'Brigada de Cocina (12-17 personas)', desc: 'Organigrama, perfiles, salarios España 2026, turnos, formación continua y retención de talento.' },
      { icon: 'UserCheck', num: '14', title: 'Equipo de Sala (9-12 personas)', desc: 'Maître, sumiller, jefes de rango, runners. Salarios, formación en protocolo y gestión de turnos.' },
      { icon: 'UtensilsCrossed', num: '15', title: 'Menú Engineering para Fine Dining', desc: 'Diseño de carta, food cost por plato, matrix Stars/Plowhorses/Puzzles/Dogs y pricing psicológico.' },
      { icon: 'Leaf', num: '16', title: 'Proveedores Km0 y Producto de Temporada', desc: 'Red de proveedores locales, lonjas, huertos propios, temporalidad y trazabilidad del producto.' },
      { icon: 'Star', num: '17', title: 'Cómo Aspirar a Estrella Michelin', desc: 'Criterios de evaluación, qué buscan los inspectores, timeline realista y casos de éxito en España.' },
      { icon: 'Sun', num: '18', title: 'Cómo Aspirar a Sol Repsol', desc: 'Diferencias con Michelin, proceso de evaluación, requisitos y estrategia de posicionamiento.' },
      { icon: 'Globe', num: '19', title: "The World's 50 Best", desc: 'Cómo funciona el ranking, votantes, categorías y qué hacer para entrar en el radar internacional.' },
      { icon: 'Megaphone', num: '20', title: 'Marketing, PR y Lanzamiento', desc: 'Estrategia pre-apertura, prensa gastronómica, influencers food, redes sociales y evento inaugural.' },
      { icon: 'Tablet', num: '21', title: 'Tecnología para Fine Dining', desc: 'TPV, reservas (TheFork, Resy), CRM de comensales, gestión de alérgenos y digitalización discreta.' },
      { icon: 'Sparkles', num: '22', title: 'Tendencias 2025-2026', desc: 'Sostenibilidad, fermentación, cocina vegetal, experiencias inmersivas, IA aplicada y nuevos formatos.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Chefs, sommeliers, inversores y consultores que ya usaron esta guía',
    items: [
      { name: 'Marcos Delgado', role: 'Chef ejecutivo, 1 Estrella Michelin en Madrid', text: 'El capítulo sobre cómo aspirar a la Estrella Michelin es el más realista que he leído. Los 5 criterios explicados con ejemplos concretos. Ojalá lo hubiese tenido hace 10 años.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Ana Beltrán', role: 'Consultora gastronómica, ex-directora Guía Repsol', text: 'La sección de plan financiero con inversiones reales de 500K-900K€ es brutal. Por fin una guía que no vende fantasías de abrir un gastronómico con 100K€.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Fernando Ruiz', role: 'Propietario, restaurante 2 Soles Repsol en Galicia', text: 'El cronograma Gantt de 18 meses es exactamente lo que necesita cualquiera que quiera abrir un gastronómico. Cada fase con sus dependencias. Imprescindible.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Isabel Navarro', role: 'Sommelier, directora de bodega en Barcelona', text: 'El capítulo de bodega es muy completo: desde la inversión inicial (15-80K€) hasta el software de gestión. El budget de bodega con márgenes por referencia es oro puro.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Carlos Herrera', role: 'Arquitecto especializado en interiorismo gastronómico', text: 'El diseño de cocina por partidas y el ratio cocina/sala están perfectamente calculados. La sección de iluminación 2700-3000K demuestra que el autor sabe de lo que habla.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Lucía Martín', role: 'Maître y formadora de equipos de sala', text: 'El manual de servicio de sala que incluye como bonus vale más que el precio de la guía entera. Protocolo de recepción, servicio de vinos, gestión de quejas... todo.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pablo Fernández', role: 'Inversor, 3 restaurantes en Madrid y Valencia', text: 'El business plan modelo para bancos me ahorró 5.000€ en consultoría. Lo presenté tal cual a mi banco y me aprobaron la financiación. Plantilla perfecta.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Javier Moreno', role: 'Chef de partida, aspirante a primer restaurante propio', text: 'Después de 12 años como jefe de partida, esta guía me dio la hoja de ruta completa para abrir mi propio gastronómico. Los salarios, las brigadas, el equipamiento... todo con datos reales.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Escrita por un Profesional', desc: 'Chef desde los 17 años y consultor desde 2010, 200+ aperturas asesoradas, clientes con Estrella Michelin y Soles Repsol. Experiencia real, no teoría de manual.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (500K-900K€), food cost 25-28%, salarios España 2026, márgenes por cubierto y punto de equilibrio calculado.' },
      { icon: 'FileSpreadsheet', title: 'Incluye Plantillas por Valor de 100€+', desc: 'Plan financiero completo, escandallos por plato, menú engineering matrix, cronograma Gantt de apertura y más — todo en Excel con fórmulas.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000-20.000€', desc: 'La misma información que reciben los clientes de consultoría gastronómica premium, en formato guía por un pago único de 85€.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Incluye resumen ejecutivo, proyecciones financieras a 3 años y análisis de mercado.', image: '/lovable-uploads/ai-gallery/guia-gastro-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual de Servicio de Sala', value: '39 EUR', desc: 'Protocolo completo de recepción, toma de comanda, servicio de vinos, gestión de quejas y atención VIP. Estándar fine dining para formar a tu equipo de sala.', image: '/lovable-uploads/ai-gallery/guia-gastro-sala.jpg' },
      { icon: 'ClipboardCheck', label: 'BONUS 3', title: 'Checklist Inspección Michelin/Repsol', value: '29 EUR', desc: '45 ítems que buscan los inspectores: desde la calidad del producto hasta la coherencia del menú, el servicio, la vajilla y la experiencia global del comensal.', image: '/lovable-uploads/ai-gallery/guia-gastro-plato.jpg' },
      { icon: 'CalendarRange', label: 'BONUS 4', title: 'Cronograma de Apertura Gantt 18 Meses', value: '24 EUR', desc: 'Todas las fases y dependencias: desde la búsqueda de local hasta la inauguración. Hitos, responsables y fechas límite en formato visual Gantt.', image: '/lovable-uploads/ai-gallery/guia-gastro-cocina.jpg' },
      { icon: 'PieChart', label: 'BONUS 5', title: 'Calculadora Menú Engineering', value: '19 EUR', desc: 'Matrix automática Stars/Plowhorses/Puzzles/Dogs. Introduce tus platos, food cost y ventas, y obtén recomendaciones de pricing y carta al instante.', image: '/lovable-uploads/ai-gallery/guia-gastro-bodega.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 85 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu restaurante gastronómico, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar un restaurante gastronómico?', a: 'Entre 500.000€ y 900.000€ dependiendo de la ubicación, nivel de acabados, equipamiento de cocina y tamaño de la bodega. La guía desglosa cada partida con costes reales del mercado español en el capítulo 4 y las plantillas Excel.' },
    { q: '¿Sirve para cualquier tipo de restaurante?', a: 'Está diseñada específicamente para restaurantes de alta cocina y fine dining (65 plazas). Dicho esto, la base de planificación financiera, legal y operativa es aplicable a cualquier restaurante de nivel medio-alto que aspire a la excelencia.' },
    { q: '¿Incluye información sobre cómo aspirar a Estrella Michelin?', a: "Sí. Los capítulos 17, 18 y 19 cubren en detalle cómo aspirar a Estrella Michelin, Sol Repsol y The World's 50 Best. Incluye criterios de evaluación, qué buscan los inspectores y un checklist de 45 ítems como bonus." },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 10 plantillas Excel incluyen fórmulas automáticas: plan financiero con P&L y break-even, escandallos por plato, calculadora de menú engineering (matrix Stars/Plowhorses/Puzzles/Dogs), cronograma Gantt y más.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas, adaptar a tu proyecto y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Restaurante a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta una hora de consultoría.',
    items: [
      'Guía completa PDF + DOCX (22 capítulos, 119 páginas)',
      '10 plantillas Excel con fórmulas',
      '8 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual de servicio de sala',
      'Checklist preparación Michelin/Repsol',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 85 EUR',
  },

  stickyLabel: 'GUÍA RESTAURANTE GASTRONÓMICO — 85 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Kit Tareas Restaurante Creativo', href: '/kit-tareas-restaurante-creativo' },
    { label: 'Kit Plan Financiero', href: '/kit-plan-financiero' },
    { label: 'Guía Food Cost + Ingeniería de Menú', href: '/guia-food-cost-ingenieria-menu' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'guia-restaurante-gastronomico',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España (Michelin · Sol Repsol)',
    productDescription: 'Guía premium de 22 capítulos para montar un restaurante gastronómico: plan financiero, diseño cocina y sala, brigada, bodega, Michelin, Sol Repsol. Incluye 10 plantillas Excel, 8 checklists, business plan y manual de sala.',
    price: '85.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar un restaurante gastronómico?', a: 'Entre 500.000€ y 900.000€ para 65 plazas de nivel medio-alto en capital de provincia española. La guía desglosa cada partida.' },
      { q: '¿Incluye información sobre cómo aspirar a Estrella Michelin?', a: "Sí. Los capítulos 17-19 cubren Michelin, Sol Repsol y The World's 50 Best con criterios, proceso de inspección y estrategia." },
      { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Plan financiero a 3 años, escandallos, menu engineering, cash flow, break-even y más. Todo con fórmulas encadenadas.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Restaurante Gastronómico', item: 'https://aichef.pro/guia-restaurante-gastronomico' },
    ],
  },
};

export default data;
