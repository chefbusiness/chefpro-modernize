// guia-restaurante-casual.ts — Copy VERBATIM de src/pages/GuiaRestauranteCasual.tsx +
// componentes de src/components/guia-restaurante-casual/* + data/testimonials-guia-restaurante-casual.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'.
// Sin divergencias estructurales: NO CompatibleAppsMarquee (showCompatibleApps omitido = false),
// bonus.layout 'split' (5 bonus, igual que gastronómico), avatarAltPrefix/testimonials.titleGold
// = defaults de la línea ('Professional' / 'Profesionales').
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-restaurante-casual',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_CASUAL',

  seo: {
    title: 'Cómo Montar un Restaurante Casual 80 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium para montar un restaurante casual en España: 20 capítulos, 60+ páginas, plan financiero, diseño de cocina y sala, delivery, terraza, menú del día. 8 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    keywords: 'como montar restaurante casual, abrir restaurante casual dining, plan financiero restaurante, equipamiento cocina restaurante, delivery restaurante, terraza restaurante licencia, menu del dia restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
  },

  hero: {
    badge: 'El 60% de los restaurantes casuales cierra en los primeros 3 años — planificar bien marca la diferencia',
    titlePre: 'Cómo Montar un ',
    titleGold: 'Restaurante Casual',
    subtitleLine: '80 Plazas · Guía Completa España',
    description: 'Guía completa con 20 capítulos, 60+ páginas, 8 plantillas Excel, 6 checklists, business plan modelo y manual de operaciones. Todo para abrir tu restaurante casual dining.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas: plan financiero, escandallos, menú engineering',
      '6 checklists de apertura: legal, equipamiento, APPCC, sala, contratación, marketing',
      'Business Plan modelo para presentar a bancos e inversores',
      'Manual de operaciones: apertura, cierre, delivery, terraza, reclamaciones',
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
      '/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-casual-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-casual-sala.jpg',
      '/lovable-uploads/ai-gallery/guia-casual-plato.jpg',
      '/lovable-uploads/ai-gallery/guia-casual-terraza.jpg',
      '/lovable-uploads/ai-gallery/guia-casual-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-casual-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-casual-sala.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 8 Plantillas + 6 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu restaurante casual en España, escrito por un profesional con 29 años en hostelería.',
    chapters: [
      { icon: 'Building2', num: '01', title: 'Qué es un Restaurante Casual', desc: 'Definición, diferencias con fast casual y fine dining. Ticket medio 18-35€, ambiente y público objetivo.' },
      { icon: 'TrendingUp', num: '02', title: 'El Mercado del Casual Dining en España 2026', desc: 'Datos del sector: 12.400M EUR, crecimiento +8% anual, ciudades con mayor demanda y tendencias.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio Casual', desc: 'Barrio premium, gastrobar, temático (brunch, bowls) y casual + delivery híbrido. Pros y contras.' },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 150K-350K€, food cost 28-32%, EBITDA 12-18%, break-even mes 8-14.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, registro sanitario, Hacienda, seguros, LOPD, terraza y alcohol.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC obligatorio, trazabilidad, alérgenos, control de temperaturas.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales, metros para 80 plazas, salida de humos, terraza y accesibilidad.' },
      { icon: 'Layout', num: '08', title: 'Diseño de Cocina Profesional', desc: 'Flujo lineal: recepción → preparación → cocción → emplatado → pase. 40-55 m².' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento de Cocina', desc: 'Lista completa con costes: horno mixto, plancha, freidora, cámaras, tren de lavado. 30-60K€.' },
      { icon: 'Armchair', num: '10', title: 'Diseño de Sala para 80 Plazas', desc: 'Distribución mesas, iluminación regulable, acústica, interiorismo y terraza.' },
      { icon: 'GlassWater', num: '11', title: 'Mobiliario, Vajilla y Menaje', desc: 'Selección inteligente: porcelana reforzada, cristalería resistente, sin manteles. 3-6K€.' },
      { icon: 'GlassWater', num: '12', title: 'Carta de Bebidas y Coctelería', desc: 'Vinos, cervezas craft, cócteles signature, happy hour. Margen 65-80%.' },
      { icon: 'Users', num: '13', title: 'Brigada de Cocina (6-10 personas)', desc: 'Organigrama compacto, salarios España 2026, turnos y polivalencia.' },
      { icon: 'UserCheck', num: '14', title: 'Equipo de Sala (6-8 personas)', desc: 'Encargado, camareros, runner, barra. Servicio eficiente y upselling natural.' },
      { icon: 'UtensilsCrossed', num: '15', title: 'Menú Engineering y Carta', desc: 'Estructura 18-26 platos, matrix Stars/Plowhorses/Puzzles/Dogs y rotación de carta.' },
      { icon: 'Utensils', num: '16', title: 'Menú del Día y Ofertas', desc: 'Estructura, pricing 12-16€, food cost 30-35%, brunch, happy hour y noches temáticas.' },
      { icon: 'Truck', num: '17', title: 'Delivery y Take Away', desc: 'Plataformas vs delivery propio, packaging eco, menú delivery optimizado, zona de packaging.' },
      { icon: 'Sun', num: '18', title: 'Terraza: Licencias y Rentabilidad', desc: 'Licencia municipal, mobiliario, 20-40% facturación extra en temporada.' },
      { icon: 'Megaphone', num: '19', title: 'Marketing Digital y Redes Sociales', desc: 'Google My Business, Instagram, TikTok, TheFork, delivery, presupuesto 500-1.500€/mes.' },
      { icon: 'Tablet', num: '20', title: 'Tecnología para Casual Dining', desc: 'TPV, reservas, integrador delivery, contabilidad, RRHH, carta digital, WiFi.' },
    ],
  },

  testimonials: {
    titleGold: 'Profesionales',
    subtitle: 'Propietarios, chefs, inversores y consultores que ya usaron esta guía',
    items: [
      { name: 'Laura Fernández', role: 'Propietaria de restaurante casual en Madrid', text: 'Abrí mi restaurante con esta guía como hoja de ruta. El plan financiero me salvó de errores que habrían costado miles de euros. Los números son reales, no fantasía.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'David García', role: 'Chef y emprendedor, Valencia', text: 'Después de 10 años como jefe de cocina, quería abrir mi propio casual. La guía cubre TODO: desde la SL hasta el menú engineering. El cronograma Gantt fue clave para no perderme.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'María Sánchez', role: 'Consultora de restauración, Barcelona', text: 'Recomiendo esta guía a todos mis clientes que quieren abrir un casual. El capítulo de delivery es oro puro — muchos restaurantes lo ignoran y pierden un 20% de facturación.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Alejandro Ruiz', role: 'Inversor en hostelería, 5 locales en Málaga', text: 'El business plan modelo lo presenté tal cual al banco. Me aprobaron la financiación en dos semanas. Una plantilla que vale 10 veces el precio de la guía.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Carmen López', role: 'Encargada de sala, aspirante a primera apertura', text: 'Llevaba años queriendo dar el salto. La sección de equipo y turnos me ayudó a calcular exactamente cuánto personal necesito y cuánto me va a costar. Sin sorpresas.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Roberto Martín', role: 'Arquitecto especializado en hostelería', text: 'El capítulo de diseño de sala con ratios m²/plaza y distribución de mesas es impecable. Incluye terraza, acústica e iluminación por turnos. Muy profesional.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Patricia Navarro', role: 'Propietaria, gastrobar en Sevilla', text: 'Lo que más me gustó: el capítulo de menú del día con food cost controlado. Pasé de perder dinero en el menú a que sea mi mejor herramienta de captación.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Javier Torres', role: 'Gestor fiscal especializado en hostelería', text: 'El checklist legal es el más completo que he visto para un restaurante en España. 32 trámites con responsable, coste y orden. Se lo paso a mis clientes nuevos.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'UtensilsCrossed', title: 'Escrita por un Profesional', desc: '29 años en hostelería, 200+ aperturas asesoradas. Datos reales de restaurantes casuales en España, no teoría de manual.' },
      { icon: 'Calculator', title: 'Números Reales, No Fantasía', desc: 'Inversión real (150K-350K€), food cost 28-32%, salarios España 2026, break-even calculado y 3 escenarios financieros.' },
      { icon: 'FileSpreadsheet', title: 'Incluye Plantillas por Valor de 80€+', desc: 'Plan financiero, escandallos, menú engineering, cronograma Gantt, turnos y más — todo en Excel con fórmulas automáticas.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 3.000-10.000€', desc: 'La misma información que reciben los clientes de consultoría gastronómica, en formato guía por un pago único de 65€.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años en alta hostelería y 15 años en consultoría gastronómica. Ha asesorado la apertura de más de 200 establecimientos en España y Europa, incluyendo restaurantes casuales, gastrobares y franquicias.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Resumen ejecutivo, proyecciones financieras a 3 años y análisis de mercado.', image: '/lovable-uploads/ai-gallery/guia-casual-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual de Operaciones', value: '39 EUR', desc: 'Protocolo completo: apertura, cierre, servicio mediodía y cena, gestión de delivery, terraza, reclamaciones y alérgenos. Para formar a tu equipo desde el día 1.', image: '/lovable-uploads/ai-gallery/guia-casual-sala.jpg' },
      { icon: 'ClipboardCheck', label: 'BONUS 3', title: 'Checklist Diseño Sala + Terraza', value: '29 EUR', desc: '29 ítems: distribución, mobiliario, iluminación regulable, acústica, decoración, terraza completa con sombrillas, estufas y macetas.', image: '/lovable-uploads/ai-gallery/guia-casual-terraza.jpg' },
      { icon: 'CalendarRange', label: 'BONUS 4', title: 'Cronograma de Apertura Gantt 12 Meses', value: '24 EUR', desc: 'Todas las fases: planificación, local, licencias, obra, equipamiento, equipo, marketing, soft opening e inauguración.', image: '/lovable-uploads/ai-gallery/guia-casual-cocina.jpg' },
      { icon: 'PieChart', label: 'BONUS 5', title: 'Calculadora Menú Engineering + Menú del Día', value: '19 EUR', desc: 'Matrix automática Stars/Plowhorses/Puzzles/Dogs + simulador de menú del día con food cost controlado.', image: '/lovable-uploads/ai-gallery/guia-casual-plato.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu restaurante casual, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar un restaurante casual?', a: 'Entre 150.000€ y 350.000€ dependiendo de la ubicación, nivel de acabados y si el local requiere obra completa. La guía desglosa cada partida con costes reales del mercado español en el capítulo 4 y las plantillas Excel.' },
    { q: '¿Sirve para cualquier tipo de restaurante casual?', a: 'Sí. La guía cubre los 4 modelos principales: restaurante de barrio premium, gastrobar, temático (brunch, bowls, comfort food) y casual + delivery híbrido. La base financiera, legal y operativa es universal.' },
    { q: '¿Incluye capítulos sobre delivery y terraza?', a: 'Sí. Los capítulos 17 y 18 cubren en detalle delivery (plataformas, packaging, menú delivery específico) y terraza (licencias, rentabilidad, mobiliario). Dos fuentes de ingresos clave en casual dining.' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 8 plantillas Excel incluyen fórmulas automáticas: plan financiero con P&L y break-even, escandallos por plato, calculadora de menú engineering y menú del día, cronograma Gantt y más.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas, adaptar a tu proyecto y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Restaurante a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta una cena para dos.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)',
      '8 plantillas Excel con fórmulas',
      '6 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual de operaciones completo',
      'Capítulos exclusivos: delivery, terraza, menú del día',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'GUÍA RESTAURANTE CASUAL — 65 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Guía Restaurante Gastronómico', href: '/guia-restaurante-gastronomico' },
    { label: 'Kit Plan Financiero', href: '/kit-plan-financiero' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  alreadyBought: {
    product: 'guia-restaurante-casual',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar un Restaurante Casual 80 Plazas — Guía Completa España',
    productDescription: 'Guía premium de 20 capítulos para montar un restaurante casual dining: plan financiero, diseño cocina y sala, delivery, terraza, menú del día. Incluye 8 plantillas Excel, 6 checklists, business plan y manual de operaciones.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar un restaurante casual?', a: 'Entre 150.000€ y 350.000€ para 80 plazas dependiendo de ubicación y acabados. La guía desglosa cada partida con costes reales.' },
      { q: '¿Incluye capítulos sobre delivery y terraza?', a: 'Sí. Los capítulos 17 y 18 cubren delivery (plataformas, packaging, menú optimizado) y terraza (licencias, rentabilidad, mobiliario).' },
      { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Plan financiero a 3 años, escandallos, menú engineering, cash flow, break-even y calculadora de menú del día. Todo con fórmulas.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Restaurante Casual', item: 'https://aichef.pro/guia-restaurante-casual' },
    ],
  },
};

export default data;
