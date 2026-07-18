// guia-panaderia-obrador.ts — Copy VERBATIM de src/pages/GuiaPanaderiaObrador.tsx + componentes de
// src/components/guia-panaderia-obrador/* + data/testimonials-guia-panaderia-obrador.ts.
// Avatares de testimonios: import '@/assets/avatars/avatar-N.jpg' → ruta pública '/avatars/avatar-N.jpg'
// (excepto el de Elena Solís, que usa un avatar de nicho específico ya publicado en
// '/lovable-uploads/avatars-nicho/avatar-panadera-celiaca.jpg' — NO sigue el patrón avatar-N).
//
// Divergencias de la línea que aplican aquí (documentadas en types.ts):
//  - hero.avatarAltPrefix = 'Panadero' (no 'Professional').
//  - testimonials.titleGold = 'Panaderos' (no 'Profesionales').
//  - showCompatibleApps: ausente → false (SPA no renderiza CompatibleAppsMarquee).
//  - bonus.layout: 'split' (5 bonus, slice(0,3) + slice(3), igual que gastronómico).
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-panaderia-obrador',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_PANADERIA_OBRADOR',

  seo: {
    title: 'Cómo Montar una Panadería con Obrador — Guía Completa España 2026 | AI Chef Pro',
    description: 'Guía premium para montar una panadería con obrador en España 2026: 20 capítulos, 70+ páginas, plan financiero, recetario masa madre, salida de humos, APPCC obrador, alérgenos. 9 plantillas Excel + 6 checklists + business plan + manual del obrador. 65 EUR.',
    keywords: 'como montar panaderia, abrir panaderia con obrador, panaderia masa madre España, plan financiero panaderia, salida de humos panaderia, licencia clasificada panaderia, APPCC obrador panaderia, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-panaderia-obrador.jpg',
  },

  hero: {
    badge: 'El pan industrial cae -22% mientras el artesanal con masa madre crece +9% interanual — el momento es ahora',
    titlePre: 'Cómo Montar una ',
    titleGold: 'Panadería con Obrador',
    subtitleLine: 'Modelo Artesanal con Masa Madre · Guía España 2026',
    description: 'Guía completa con 20 capítulos, 70+ páginas, 9 plantillas Excel, 6 checklists, business plan modelo y manual del obrador. Todo para abrir tu panadería boutique con masa madre.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 70+ páginas)',
      '9 plantillas Excel con fórmulas: plan financiero, CAPEX, escandallos por harina, plan fermentación',
      '6 checklists de apertura: legal, APPCC obrador, equipamiento, salida de humos, contratación, marketing',
      'Business Plan modelo para bancos con números reales del sector panadería 2026',
      'Manual del obrador: masa madre, fermentaciones, recetario maestro, turnos madrugada',
    ],
    ctaLabel: 'COMPRAR GUÍA — 65 EUR',
    avatarAltPrefix: 'Panadero',
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
      '/lovable-uploads/ai-gallery/guia-panaderia-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-panaderia-1.jpg',
      '/lovable-uploads/ai-gallery/guia-panaderia-2.jpg',
      '/lovable-uploads/ai-gallery/guia-panaderia-3.jpg',
      '/lovable-uploads/ai-gallery/guia-panaderia-4.jpg',
      '/lovable-uploads/ai-gallery/guia-panaderia-5.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-panaderia-3.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-panaderia-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-panaderia-2.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 9 Plantillas + 6 Checklists + 2 Documentos',
    subtitle: 'Todo lo que necesitas saber para montar tu panadería con obrador en España, con recetario de masa madre y planes de fermentación 18-72h.',
    chapters: [
      { icon: 'Wheat', num: '01', title: 'Qué es una Panadería con Obrador', desc: 'Modelo artesanal con producción propia desde harina. Ticket medio 4,80-8,50€, margen 45-58%.' },
      { icon: 'TrendingUp', num: '02', title: 'El Sector de la Panadería Artesanal 2026', desc: '30.500 establecimientos España, masa madre pasa del 14% al 26% del mercado, +9% interanual.' },
      { icon: 'Briefcase', num: '03', title: 'Modelos de Negocio Panadería', desc: 'Obrador+tienda, despacho, panadería-bistró y boutique especializada. Inversión 35K-250K€.' },
      { icon: 'Calculator', num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 120K-200K€, food cost 18-22%, EBITDA 15-22%, break-even mes 8-14.' },
      { icon: 'Scale', num: '05', title: 'Requisitos Legales España 2026', desc: 'RGSEAA + licencia clasificada + salida humos + APPCC + Verifactu + control horario digital.' },
      { icon: 'ShieldCheck', num: '06', title: 'APPCC Obrador + Alérgenos Cruzados', desc: 'Trazabilidad harinas, contaminación gluten/sin gluten, control plagas en silos.' },
      { icon: 'MapPin', num: '07', title: 'Ubicación y Local', desc: 'Salida humos viable (killer), paso peatonal, 60-90 m², trifásica 30 kW mínimo.' },
      { icon: 'Layout', num: '08', title: 'Diseño del Obrador Profesional', desc: 'Flujo lineal harina → pan: amasado, división, fermentación, horneado, enfriamiento.' },
      { icon: 'Wrench', num: '09', title: 'Equipamiento Profesional', desc: 'Hornos piso vs rotativo, amasadora espiral, cámara fermentación, divisora, formadora.' },
      { icon: 'Package', num: '10', title: 'Materias Primas: Harinas y Proveedores', desc: 'T55/T65/T80/T110, espelta, centeno, kamut. Vilafranquina, Claudio Aponte, Puratos.' },
      { icon: 'FlaskConical', num: '11', title: 'Masa Madre y Fermentaciones Largas', desc: 'Líquida vs sólida, refrescos diarios, plan fermentación 18-72h por tipo de pan.' },
      { icon: 'Croissant', num: '12', title: 'Carta de Producto: 25 Referencias', desc: '12 panes + 8 bollerías + 5 pastelerías. Rotación semanal pan especial del chef.' },
      { icon: 'FileSpreadsheet', num: '13', title: 'Pricing y Escandallos por Tipo', desc: 'Food cost real 14-26% según pan. Escandallos masa madre, baguette, croissant, sin gluten.' },
      { icon: 'Store', num: '14', title: 'Diseño de Tienda y Vitrina', desc: 'Vitrina seca pan + refrigerada bollería. Cestos mimbre, etiquetado kraft, iluminación cálida.' },
      { icon: 'Users', num: '15', title: 'Brigada de Obrador', desc: 'Panadero of.1ª + ayudante + bollero + dependientes. Salarios España 2026 + plus nocturnidad.' },
      { icon: 'Clock', num: '16', title: 'Operativa Diaria del Obrador', desc: 'Jornada 03:00-11:00: refresco masa madre, formado, fermentación final, hornadas.' },
      { icon: 'Sun', num: '17', title: 'Plan de Producción Semanal', desc: 'Ajuste tirada por día de la semana + clima + festivos. Reducir mermas con histórico.' },
      { icon: 'Recycle', num: '18', title: 'Mermas y Devoluciones Cero Residuos', desc: 'Pan del día -40% / 2 días donación Banco Alimentos. Reduce mermas 12% → 4%.' },
      { icon: 'Megaphone', num: '19', title: 'Marketing Local + Digital + B2B Horeca', desc: 'Google Local, Instagram obrador, suscripción pan semanal, contratos restaurantes y hoteles.' },
      { icon: 'Award', num: '20', title: 'Casos Éxito y Roadmap Escalado', desc: 'Levaduramadre, Panic, Crustó, Hofmann. Escalado a 2º local, obrador central o franquicia.' },
    ],
  },

  testimonials: {
    titleGold: 'Panaderos',
    subtitle: 'Maestros panaderos, emprendedores e inversores que ya usaron esta guía',
    items: [
      { name: 'Marta Vidal', role: 'Panadera artesana, primera apertura en Madrid', text: 'La parte de licencia clasificada con salida de humos me ahorró meses de retraso. Verifiqué la viabilidad antes de firmar el alquiler como dice el manual y descarté dos locales que me habrían costado una fortuna en cambios.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Javier Marca', role: 'Maestro panadero con obrador propio, Barcelona', text: 'Llevo 12 años haciendo pan y aún así el plan de fermentación 24-72h y la calculadora de masa madre me dieron criterios técnicos que no había sistematizado. Lo recomiendo a cualquiera que se quiera profesionalizar.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Carmen Iglesias', role: 'Emprendedora, abriendo panadería-bistró en Bilbao', text: 'El business plan modelo me lo aceptó el banco prácticamente sin cambios. Conseguí la financiación de 130.000€ en 18 días. Vale 10 veces el precio de la guía solo por eso.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Daniel Romero', role: 'Antiguo chef pastelero reconvertido a panadero', text: 'El recetario maestro con baguette tradition, hogaza T80 masa madre, croissant clásico y panettone es muy técnico. Las hidrataciones, los plegados, los tiempos. Información de obrador real, no de blog.', avatar: '/avatars/avatar-8.jpg' },
      { name: 'Lucía Bermúdez', role: 'Asesora financiera especializada hostelería', text: 'El P&L mensual con 3 escenarios + cash flow 24 meses + calculadora CAPEX es lo más completo que he visto a este precio. Lo doy a todos mis clientes que quieren entrar en panadería.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Estévez', role: 'Inversor con 3 locales de gastrobar buscando diversificar', text: 'El capítulo de modelos de negocio (tradicional vs despacho vs bistró vs boutique) me ayudó a decidir el modelo correcto para mi ubicación. Cada uno tiene márgenes muy distintos y el análisis es preciso.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Elena Solís', role: 'Panadera celíaca, especialidad sin gluten', text: 'El protocolo de alérgenos cruzados con separación física es exactamente lo que necesitaba para certificarme FACE. Me aclaró por qué tantas panaderías cometen errores graves al ofrecer sin gluten.', avatar: '/lovable-uploads/avatars-nicho/avatar-panadera-celiaca.jpg' },
      { name: 'Roberto Casas', role: 'Gestor laboral hostelería', text: 'El control horario digital 2026 con plus nocturnidad para turnos de madrugada está bien resuelto en la plantilla de turnos. Cumplimiento legal + rentabilidad. Mis clientes panaderos lo agradecen.', avatar: '/avatars/avatar-3.jpg' },
    ],
  },

  why: {
    reasons: [
      { icon: 'Wheat', title: 'Escrita para Panadería Real', desc: 'Recetario maestro masa madre, fermentaciones 18-72h, escandallos por tipo de harina T55/T65/T80. No es una guía genérica.' },
      { icon: 'Calculator', title: 'Números Reales del Sector 2026', desc: 'Inversión 120K-200K€, food cost 18-22%, EBITDA 15-22%, break-even mes 8-14. Casos Levaduramadre, Panic, Crustó.' },
      { icon: 'FileSpreadsheet', title: 'Plantillas por Valor de 80€+', desc: 'Plan financiero, escandallos por pan, calculadora harinas, plan fermentación, Gantt apertura, turnos madrugada — todo Excel.' },
      { icon: 'FlaskConical', title: 'Técnica + Negocio en un mismo Documento', desc: 'Lo único que combina recetario técnico (masa madre + croissant + panettone) con plan de negocio + APPCC obrador + salida humos.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años en alta hostelería y 15 años en consultoría gastronómica. Ha asesorado la apertura de más de 200 establecimientos en España y Europa, incluyendo panaderías boutique con masa madre, obradores artesanales y panaderías-bistró.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR',
    layout: 'split',
    items: [
      { icon: 'FileText', label: 'BONUS 1', title: 'Business Plan Modelo para Bancos', value: '49 EUR', desc: 'Plantilla rellenable con estructura profesional para presentar a bancos. Resumen ejecutivo, proyecciones financieras a 3 años específicas panadería, análisis de mercado con datos sector 2026.', image: '/lovable-uploads/ai-gallery/guia-panaderia-hero.jpg' },
      { icon: 'BookOpen', label: 'BONUS 2', title: 'Manual del Obrador (Operaciones Completo)', value: '39 EUR', desc: 'Protocolo completo: refresco masa madre, recetario maestro (baguette, hogaza, croissant, panettone), planes de limpieza diaria/semanal/mensual, trazabilidad lotes harina.', image: '/lovable-uploads/ai-gallery/guia-panaderia-3.jpg' },
      { icon: 'FlaskConical', label: 'BONUS 3', title: 'Plan de Fermentación + Escandallos Harina', value: '29 EUR', desc: 'Excel completo con tiempos, hidrataciones, masa madre %, plegados para 15 tipos de pan. Calculadora de escandallos por harina T55/T65/T80/T110/espelta/centeno/sin gluten.', image: '/lovable-uploads/ai-gallery/guia-panaderia-2.jpg' },
      { icon: 'Wind', label: 'BONUS 4', title: 'Checklist Salida de Humos + Licencia Clasificada', value: '24 EUR', desc: 'Killer #1 de aperturas frustradas. 28 ítems pre-alquiler + proyecto técnico + licencia municipal + ejecución. Ahorra 4-6 meses de retraso.', image: '/lovable-uploads/ai-gallery/guia-panaderia-4.jpg' },
      { icon: 'FileSpreadsheet', label: 'BONUS 5', title: 'Calculadora CAPEX + Cronograma Gantt', value: '19 EUR', desc: 'Desglose inversión 120K-200K€ por categoría (obrador + tienda + licencias + maniobra) + cronograma Gantt 6 meses con fases críticas (proyecto humos → licencia → equipamiento).', image: '/lovable-uploads/ai-gallery/guia-panaderia-1.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te aporta valor real para montar tu panadería con obrador, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Cuánto cuesta montar una panadería con obrador en España?', a: 'Entre 120.000€ y 200.000€ para un local de 60-90 m² con obrador propio. La guía desglosa cada partida en el capítulo 4 y en la calculadora CAPEX incluida (Excel): 40% equipamiento obrador, 20% obra + salida humos, 15% tienda + branding, 25% fondo maniobra + licencias.' },
    { q: '¿Sirve para cualquier modelo de panadería?', a: 'Sí. La guía cubre los 4 modelos principales: obrador propio + tienda (modelo principal), despacho con horno de regeneración, panadería-bistró (cross-sell con brunch), y boutique especializada (solo masa madre / solo ecológico / solo sin gluten). El capítulo 3 ayuda a elegir el modelo correcto para tu zona.' },
    { q: '¿Incluye recetario maestro de masa madre?', a: 'Sí. El manual de operaciones incluye recetario técnico con hidrataciones, masa madre %, plegados y tiempos de fermentación para baguette tradition, hogaza T80 masa madre, croissant clásico mantequilla, brioche, panettone y más. Incluye también el protocolo de refresco diario de masa madre líquida y sólida.' },
    { q: '¿Cubre el problema de la salida de humos y licencia clasificada?', a: 'Sí. Es el capítulo 5 + un checklist específico de 28 ítems. La salida de humos es el killer #1 de las aperturas de panadería en España. La guía te enseña a verificar la viabilidad ANTES de alquilar, qué proyectos técnicos necesitas (1.500-4.000€), y cómo resolverlo con la comunidad de vecinos.' },
    { q: '¿Las plantillas Excel incluyen fórmulas?', a: 'Sí. Las 9 plantillas Excel incluyen fórmulas automáticas: plan financiero 3 años, P&L 3 escenarios, cash flow + break-even, calculadora CAPEX, escandallo maestro con food cost por tipo de pan, plan de fermentación, calculadora ticket medio, cronograma Gantt apertura y plantilla turnos brigada con control horario.' },
    { q: '¿Cubre línea sin gluten certificada?', a: 'Sí. El capítulo 6 (APPCC y alérgenos cruzados) y el checklist APPCC obrador detallan los requisitos para ofrecer línea sin gluten con certificación FACE (Espiga Barrada): separación física del obrador, utensilios exclusivos, etiquetado y procedimientos.' },
    { q: '¿El DOCX es editable?', a: 'Sí. Recibes dos versiones: el PDF editorial profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas, adaptar a tu proyecto concreto y presentar a socios o inversores.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'No Abras Tu Panadería a Ciegas',
    subtitle: 'Todo lo que necesitas por menos de lo que cuesta un saco de harina premium ecológica.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 70+ páginas)',
      '9 plantillas Excel con fórmulas (CAPEX, escandallos, fermentación, turnos…)',
      '6 checklists de apertura completos',
      'Business Plan modelo para bancos',
      'Manual del obrador con recetario maestro masa madre',
      'Capítulos exclusivos: salida de humos, alérgenos cruzados, B2B Horeca, cero residuos',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'GUÍA PANADERÍA + OBRADOR — 65 EUR',

  footerLinks: [
    { label: 'aichef.pro', href: 'https://aichef.pro' },
    { label: 'Kit Tareas Panadería', href: '/kit-tareas-panaderia' },
    { label: 'Plan Negocio Panadería', href: '/plan-negocio-panaderia' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  alreadyBought: {
    product: 'guia-panaderia-obrador',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Cómo Montar una Panadería con Obrador — Guía Completa España 2026',
    productDescription: 'Guía premium de 20 capítulos para montar una panadería con obrador artesanal: plan financiero, recetario masa madre, salida de humos, licencia clasificada, APPCC obrador con alérgenos cruzados, planes de fermentación 18-72h. Incluye 9 plantillas Excel, 6 checklists, business plan y manual del obrador.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    faqs: [
      { q: '¿Cuánto cuesta montar una panadería con obrador en España?', a: 'Entre 120.000€ y 200.000€ para 60-90 m² con obrador propio. La guía desglosa cada partida con costes reales del mercado español 2026 e incluye calculadora CAPEX en Excel.' },
      { q: '¿Incluye recetario de masa madre?', a: 'Sí. Manual del obrador con recetario técnico: baguette tradition, hogaza T80 masa madre, croissant clásico, brioche, panettone. Incluye refrescos diarios masa madre líquida y sólida.' },
      { q: '¿Cubre la salida de humos y licencia clasificada?', a: 'Sí. Capítulo 5 + checklist específico de 28 ítems con todos los pasos: verificación pre-alquiler, proyecto técnico, licencia municipal y ejecución. Killer #1 de aperturas frustradas.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Panadería con Obrador', item: 'https://aichef.pro/guia-panaderia-obrador' },
    ],
  },
};

export default data;
