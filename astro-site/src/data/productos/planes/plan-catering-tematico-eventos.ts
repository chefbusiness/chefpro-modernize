// astro-site/src/data/productos/planes/plan-catering-tematico-eventos.ts
// LÍNEA PLANES (sub-línea B "planes de eventos") — mismo template único que bar-restaurante (A)
// y cocteleria-eventos (B). Copy VERBATIM de la SPA:
//   · src/pages/PlanCateringTematicoEventos.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-catering-tematico-eventos/*  (los 10 componentes)
//   · src/data/testimonials-plan-catering-tematico-eventos.ts (8 testimonios + checkItems del hero)
//   · CompatibleAppsMarquee variant="tareas" (constante de línea, hardcodeada en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_CATERING_TEMATICO (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Lanzar tu ' (patrón de la sub-línea B).
//   · hero.checkItems tiene 9 elementos (bar-restaurante tenía 5) — longitud variable, sin impacto estructural.
//   · grid.templates tiene 11 tarjetas (icono nuevo LayoutGrid añadido a Icon.astro para este producto).
//   · authorBadges se OMITE → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto).
//
// QUIRKS VERBATIM:
//   · titlePre / seo.title / schema.productName llevan un '&' literal (la SPA lo escribe '&amp;' en JSX y
//     como '&' en JSON.stringify; aquí se escribe '&' y el template/BaseLayout lo escapan igual en HTML).
//   · schema.faqs (FAQPage JSON-LD) = 5 preguntas más cortas; faqs on-page (acordeón) = 8, más largas.
//   · images.gallery (hero, empieza en -hero.jpg y sigue -1..-5) DIFIERE de images.gridGallery
//     (ContentGrid, -1..-6, sin -hero) — igual que cocteleria-eventos.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-catering-tematico-eventos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_CATERING_TEMATICO',

  seo: {
    title:
      'Plan de Negocio para Catering & Kit Temático para Eventos — 11 Entregables | AI Chef Pro',
    description:
      'Plan + kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España 2026. El único kit que enseña a montar 5 conceptos en paralelo (sushi-bar, tacos al pastor, pizza al horno de leña, asado argentino, ceviche peruano, vegano premium, BBQ texano, tandoor indio…). Modelo dual B2C bodas multiculturales + B2B corporate brand events. 11 entregables: plan de negocio en Word, plan financiero Excel de 9 hojas, calculadora de precios por invitado y checklist de 82 tareas. €45.',
    keywords:
      'plan negocio catering temático, catering eventos multi-concepto, catering bodas multiculturales, brand events corporate, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-catering-tematico-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio para Catering & Kit Temático para Eventos — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium de catering temático multi-concepto para eventos en España 2026. El único kit del mercado español enfocado en multi-concepto (3-5 cocinas del mundo en paralelo en un mismo evento). Modelo dual B2C bodas multiculturales + B2B corporate brand events. Incluye plan de negocio en Word de 10 secciones, plan financiero Excel de 9 hojas (PyG 3 años, punto de equilibrio, escenarios, tesorería 12 meses y financiación), calculadora de precios por invitado con IVA al 10 %, plantilla de 96 proveedores especializados en 12 cocinas del mundo (importadores asiáticos, latinos, italianos, BBQ texano, indios), catálogo equipamiento multi-cocina (cuchillería japonesa, horno leña, tandoor, smoker, wok), 12 conceptos pre-empaquetados, carta 12 menús cocinas del mundo, manual técnico APPCC multi-concepto, modelos contrato B2C + B2B corporate, guía especialización progresiva y checklist de apertura de 82 tareas en 6 fases.',
    price: '45.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Yuki Tanaka',
        rating: '5',
        body: 'El kit me dio el blueprint para escalar de hacer sushi para amigos y familia a montar 4 estaciones (sushi + ramen + dim sum + bao) en bodas multiculturales premium. Subí ticket de 38 € a 75 €/pax en 8 meses.',
      },
      {
        author: 'Miguel Hernández',
        rating: '5',
        body: 'Empecé con tacos al pastor en cumpleaños familiares. Tras el plan añadí cochinita pibil + ceviche peruano + barra mezcal y ahora hago corporate brand events de 80-150 pax con 4 estaciones.',
      },
      {
        author: 'Giuseppe Romano',
        rating: '5',
        body: 'Tenía un horno de leña móvil y hacía bodas con sólo pizza. El kit me enseñó a integrar pasta fresca + antipasti + dolci en mi servicio. Ahora ofrezco trattoria completa por 65 €/pax y subí volumen 3x.',
      },
    ],
    // FAQPage schema (5 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 8, más largas)
    faqs: [
      {
        q: '¿Para quién está pensado este plan?',
        a: 'Para chefs y emprendedores en España que quieren montar un servicio premium de catering temático multi-concepto para eventos especializado en 12 cocinas del mundo. Cubre B2C (bodas multiculturales, cumpleaños temáticos, aniversarios) y B2B (corporate brand events, embajadas, wedding planners, festivales gastronómicos). Es el único plan del mercado español enfocado en multi-concepto.',
      },
      {
        q: '¿Qué hace este kit diferente del Parrillero, Paellero o Chef Privado?',
        a: 'Esos productos son monoconcepto. Este es el ÚNICO multi-concepto: enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (sushi-bar + pizza al horno de leña + asado argentino simultáneamente). La calculadora suma el coste de cada estación temática en directo y te da el precio por invitado con el margen que tú fijes.',
      },
      {
        q: '¿Cuántos conceptos temáticos cubre?',
        a: '12 conceptos pre-empaquetados: sushi-bar omakase, tacos al pastor, trattoria italiana, asado argentino, ceviche peruano, marisquería gallega, tandoor indio, mediterráneo griego/turco, plant-based premium, brasileño rodízio, BBQ texano slow-smoked, brunch internacional. Cada uno con menú propuesto, equipamiento clave, ambientación, operativa y precio orientativo.',
      },
      {
        q: '¿Cómo cubre la normativa sanitaria del catering?',
        a: 'El plan de negocio (sección de aspectos legales) y el checklist explican lo que pide la norma estatal: cocina central autorizada (cocinar en casa para eventos está prohibido, RD 1021/2022), registro sanitario de tu comunidad autónoma previa declaración responsable (el RGSEAA, sólo si suministras a otros establecimientos), APPCC, transporte en vehículo ATP y seguros. Los trámites y plazos concretos los fija tu comunidad y tu ayuntamiento.',
      },
      {
        q: '¿Cómo funciona la garantía?',
        a: '30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
      },
      {
        q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
        a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio para Catering & Kit Temático para Eventos» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, «tesorería» es «flujo de efectivo» en México y «flujo de caja» en Argentina; «camarero» es «mesero» en México y «mozo» en Argentina. Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
      },
    ],
    breadcrumbName: 'Plan de Negocio Catering Temático Eventos',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-1.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-3.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-5.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (empieza en -1, termina en -6, sin -hero)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-1.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-3.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-5.jpg',
      '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-6.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-4.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-hero.jpg',
  },

  hero: {
    badge:
      'El único kit que enseña a montar 5 conceptos en paralelo, no uno solo. Catering temático multi-cocina del mundo',
    titlePre: 'Plan de Negocio para ',
    titleGold: 'Catering & Kit Temático',
    titleSubtitle: 'para Eventos — 11 Entregables Profesionales',
    description:
      'El kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España. Modelo dual B2C bodas multiculturales + B2B corporate brand events, con 11 entregables y 96 proveedores especializados en 12 cocinas del mundo (sushi-bar, tacos al pastor, pizza al horno de leña, asado argentino, ceviche peruano, vegano premium, BBQ texano, tandoor indio…). Sin obra de cocina propia: el modelo trabaja desde una cocina central compartida y autorizada.',
    checkItems: [
      'Plan de negocio en Word: 10 secciones (más de 7.000 palabras) con las mismas cifras que el Excel',
      'Plan financiero Excel de 9 hojas: eventos × invitados × precio por invitado, PyG 3 años, tesorería y financiación',
      'Plantilla 96 proveedores reales (12 cocinas del mundo + equipamiento + servicios)',
      'Catálogo equipamiento multi-cocina: cuchillería japonesa, horno leña, tandoor, smoker, wok',
      '12 conceptos temáticos pre-empaquetados con menú, ambientación, equipamiento y precio orientativo',
      'Carta 12 menús temáticos cocinas del mundo (sushi, mexicano, italiano, argentino, indio…)',
      'Manual técnico APPCC multi-concepto (7 PCC adaptados + cronograma multi-station)',
      'Modelos contrato B2C + B2B corporate (con MSA acuerdo marco anual y confidencialidad)',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales, con la fiscalidad y los trámites de España, para montar tu catering temático multi-concepto premium con 12 cocinas del mundo en portafolio.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 Secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, equipo, plan financiero, aspectos legales y plan de acción: más de 7.000 palabras en A4, con las cifras del Excel. Caso de ejemplo: 130 eventos al año de 65 invitados a 53 € por invitado sin IVA.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (9 Hojas)', desc: 'Supuestos, inversión inicial, PyG 3 años, punto de equilibrio (en invitados por evento y en ingresos; el plan en Word lo traduce a eventos al año), escenarios, personal, tesorería 12 meses, financiación con cuadro del préstamo y DSCR, e instrucciones. Ventas = eventos al año × invitados por evento × precio por invitado sin IVA, con IVA del 10 %, cocina central compartida, sueldo del dueño, amortización, extras fijos discontinuos y estacionalidad de bodas y Navidad de empresa.' },
      { icon: 'Calculator', title: 'Calculadora de Precios por Invitado', desc: 'Del escandallo de comida y bebida, el personal del evento con su Seguridad Social, el número de estaciones temáticas en directo, los kilómetros de ida y vuelta y los alquileres, al precio por invitado sin IVA y con IVA (10 %). Particular o empresa, mínimo facturable, anticipo del 40 %, importes por tramo de cancelación y margen bruto calculado; la propina voluntaria queda fuera del total. 3 presupuestos de ejemplo calculados.' },
      { icon: 'Truck', title: 'Plantilla 96 Proveedores · 12 Cocinas', desc: 'Importadores asiáticos (EMB Food, Cominport, Garmiko) + latinos (Imp. Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento + plataformas.' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento Multi-cocina', desc: 'Por concepto: cuchillería japonesa sushi (Tojiro, Yoshihiro) + horno leña pizza (Pizza Party, Ooni Pro) + parrilla argentina + trompo pastor + tandoor portátil + smoker offset texano + wok pro (Wokinox) + sous-vide (Anova, Sammic) + vajilla premium.' },
      { icon: 'ShieldCheck', title: 'Checklist de Apertura (82 Tareas)', desc: 'Seis fases: constitución y fiscalidad (IAE 677.9, Veri*factu, IVA al 10 %, RGPD y LSSI) · cocina central autorizada, registro sanitario autonómico, APPCC, seguros RC con intoxicación y permisos · equipamiento y proveedores · personal y formación · marca y captación B2C + B2B · primer evento y primeros 90 días.' },
      { icon: 'LayoutGrid', title: '12 Conceptos Temáticos Pre-empaquetados', desc: 'Sushi-bar omakase + tacos al pastor + trattoria italiana + asado argentino + ceviche peruano + marisquería gallega + tandoor indio + mediterráneo + vegano premium + brasileño rodízio + BBQ texano + brunch internacional. Cada uno con menú + ambientación + equipamiento + operativa.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B Corporate', desc: 'Plantillas legales editables: B2C particular (boda multicultural, cumpleaños temático, aniversarios) + B2B corporate (brand event, embajada, festival gastronómico, planner) con MSA acuerdo marco anual, confidencialidad y propiedad intelectual del menú multi-concepto.' },
      { icon: 'Utensils', title: 'Carta 12 Menús Cocinas del Mundo', desc: 'Boda multicultural premium 6 estaciones + activación previa + tasting Asia 7 pasos + mexicano Día de Muertos + italiano trattoria + argentino tradicional + peruano Lima + indio Bollywood + griego/turco + vegano premium + BBQ texano + brunch internacional + mariscada gallega.' },
      { icon: 'Flame', title: 'Manual Técnico APPCC Multi-concepto', desc: '7 PCC adaptados a multi-cocina simultánea (cadena frío diferenciada, T° servicio por concepto, alérgenos en multi-station) + cronograma evento 80 pax + layout multi-station + coordinación del equipo de eventos por concepto.' },
      { icon: 'BookOpen', title: 'Guía Especialización Progresiva', desc: 'Cómo construir tu portafolio de cocinas del mundo: empieza con 1-2 conceptos, añade 1-2/año validando demanda. Roadmap 12 meses para llegar a 6 conceptos. Top 5 mejores conceptos para empezar + 4 sub-explotados (oportunidad). Modelo escalable, paso a paso.' },
    ],
  },

  testimonials: {
    subtitle:
      'Sushi masters, taqueros, pizzaiolos, asadores argentinos, chefs ceviche peruano, tandoor masters, plant-based premium y BBQ pitmasters que usaron el plan para montar o escalar su catering temático multi-concepto en España',
    items: [
      { name: 'Yuki Tanaka', role: 'Sushi master para eventos premium, Madrid', text: 'El kit me dio el blueprint para escalar de hacer sushi para amigos y familia a montar 4 estaciones (sushi + ramen + dim sum + bao) en bodas multiculturales premium. Subí ticket de 38 € a 75 €/pax en 8 meses.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Miguel Hernández', role: 'Taquero pro showcooking, Madrid', text: 'Empecé con tacos al pastor en cumpleaños familiares. Tras el plan añadí cochinita pibil + ceviche peruano + barra mezcal y ahora hago corporate brand events de 80-150 pax con 4 estaciones. La guía de especialización progresiva fue clave.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Giuseppe Romano', role: 'Pizzaiolo móvil + trattoria eventos, Toledo', text: 'Tenía un horno de leña móvil y hacía bodas con sólo pizza. El kit me enseñó a integrar pasta fresca + antipasti + dolci en mi servicio. Ahora ofrezco trattoria completa por 65 €/pax y subí volumen 3x.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Diego Ferreyra', role: 'Asador argentino premium, Madrid', text: 'El plan financiero con multi-concepto me convenció de añadir BBQ texano a mi asado argentino. Ahora cubro bodas y corporate outdoor con 2 conceptos potentes. Margen subió del 48 % al 58 %.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Carolina Vega', role: 'Chef ceviche + barra Pisco, Barcelona', text: 'La calculadora pricing dual + el factor multi-concepto me ahorró 6 meses de prueba y error. Hago bodas premium peruano + brunch latino y ya cierro presupuestos en 10 minutos con margen real del 55 %.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Rajesh Patel', role: 'Tandoor master + curry station, Madrid', text: 'Ofrezco tandoor móvil para bodas multiculturales y embajadas. El kit me organizó proveedores premium (Spice Box, TRS Foods) y la matriz de 96 proveedores fue oro. Ticket medio embajadas 110 €/pax.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Carmen Soler', role: 'Catering vegano premium, Madrid', text: 'El catering vegano ESG está explotando para corporate. El plan + la guía de especialización me clarificaron cómo posicionarme premium (45-85 €/pax) y no como alternativa low-cost. Brand events corporate son ahora mi 65 % de ingresos.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sam Williams', role: 'Texas BBQ pitmaster, Madrid', text: 'Slow-smoked BBQ con smoker offset es nicho en España. El plan me dio los contratos B2B y los modelos de contrato MSA — cerré acuerdo marco anual con 2 empresas tech corporate creativo en Madrid.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo del mercado español para montar tu catering temático multi-concepto premium: 11 entregables con 12 cocinas del mundo, 96 proveedores especializados (importadores asiáticos, latinos, italianos, BBQ texano), un plan financiero de 9 hojas con la fiscalidad española y un checklist de apertura de 82 tareas.',
    reasons: [
      { icon: 'Globe', title: 'Único Plan España con Modelo Multi-concepto', desc: 'El ÚNICO plan del mercado español que enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (sushi-bar + pizza al horno de leña + asado argentino simultáneamente), no monoconcepto. La calculadora suma el coste de cada estación temática en directo y te da el precio por invitado con el margen que tú fijes.' },
      { icon: 'BarChart3', title: 'Modelo Dual B2C Bodas Multiculturales + B2B Corporate', desc: 'Caso de ejemplo con 130 eventos al año: 45 de particulares (bodas multiculturales, cumpleaños temáticos, aniversarios) y 85 de empresa (corporate brand events, coffee breaks, cócteles, comidas y Navidad). Calculadora con selector particular / empresa (precio con IVA o «+ IVA» y tramos de cancelación de cada canal) y modelos de contrato para cada uno.' },
      { icon: 'ShieldCheck', title: '96 Proveedores · 12 Cocinas del Mundo', desc: 'Importadores asiáticos premium (EMB Food, Cominport, Garmiko) + latinos/mexicanos (Importaciones Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ texano (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento + plataformas.' },
      { icon: 'Banknote', title: 'Caso Calculado, sin Obra de Cocina', desc: 'El caso de ejemplo factura 447.850 € sin IVA el primer año (130 eventos de 65 invitados a 53 € sin IVA) y alcanza el punto de equilibrio en torno a 108 eventos al año. Unos 130.000 € de inversión total, fondo de maniobra incluido: furgoneta frigorífica, estaciones temáticas, menaje y lanzamiento, trabajando desde una cocina central compartida y autorizada. Pago único, sin suscripciones.' },
    ],
    compatLabel: 'Compatible con cualquier software ofimático:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Word' },
      { label: 'Google Sheets' },
      { label: 'Google Docs' },
      { label: 'LibreOffice' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a chefs y emprendedores en el lanzamiento de servicios premium de catering temático multi-concepto para eventos en España (sushi-bar, tacos al pastor, trattoria italiana, asado argentino, ceviche peruano, tandoor indio, BBQ texano, vegano premium…).',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €129',
    items: [
      {
        icon: 'LayoutGrid',
        label: 'BONUS 1',
        title: '12 Conceptos Temáticos Pre-empaquetados',
        value: '€65',
        desc: 'Sushi-bar omakase + tacos al pastor + trattoria italiana + asado argentino + ceviche peruano + marisquería gallega + tandoor indio + mediterráneo griego/turco + plant-based premium + brasileño rodízio + BBQ texano + brunch internacional. Cada uno con menú propuesto + ambientación + equipamiento clave + operativa específica. Tu catálogo comercial multi-concepto listo para vender desde el día 1.',
        image: '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-3.jpg',
      },
      {
        icon: 'BookOpen',
        label: 'BONUS 2',
        title: 'Guía Especialización Multi-concepto Progresiva',
        value: '€49',
        desc: 'Hoja de ruta para construir tu portafolio de cocinas del mundo de manera escalable: empieza con 1-2 conceptos dominados, añade 1-2/año validando demanda. Top 5 mejores conceptos para empezar (pizza, tacos, sushi, asado argentino, vegano) + 4 sub-explotados con oportunidad (tandoor, turco, vegano tematizado, KBBQ coreano) + roadmap 12 meses para llegar a 6 conceptos en producción.',
        image: '/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-5.jpg',
      },
      {
        icon: 'Globe',
        label: 'BONUS 3',
        title: 'Guía de Equivalencias para tu país',
        value: '€15',
        desc: 'Los términos de tu producto dichos país por país en 20 países, más una ficha de una página por país con impuestos, sanidad, normas laborales, licencias y unidades.',
        image: '/lovable-uploads/ai-gallery/es-guia-equivalencias.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  guarantee: {
    text:
      'Si el plan de negocio para tu servicio de catering temático multi-concepto no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (8 preguntas; más largas que schema.faqs)
  faqs: [
    {
      q: '¿Para quién está pensado este plan?',
      a: 'Para chefs y emprendedores en España que quieren montar un servicio premium de catering temático para eventos especializado en cocinas del mundo (japonés, mexicano, italiano, argentino, peruano, indio, vegano, BBQ texano, mediterráneo, etc.). Cubre tanto el cliente B2C (bodas multiculturales, cumpleaños temáticos, aniversarios) como el B2B (corporate brand events, embajadas, wedding planners, agencias eventos, hoteles boutique 4-5 estrellas, festivales gastronómicos). Es el único plan del mercado español enfocado en multi-concepto, no en monoproducto.',
    },
    {
      q: '¿Qué hace este kit diferente del Parrillero, Paellero o Chef Privado?',
      a: 'Esos productos son monoconcepto (un único producto/servicio: parrilla, paella o chef privado). Este es el ÚNICO multi-concepto: enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (ejemplo: sushi-bar + pizza al horno de leña + asado argentino simultáneamente). Cada estación temática en directo suma su coste (gas, montaje y menaje específico) y la calculadora te sugiere un cocinero más por estación; con eso te da el precio por invitado con el margen que tú fijes. Pensado para emprendedores que quieren un sistema operativo, no una receta.',
    },
    {
      q: '¿Sirve si nunca he montado mi propio negocio antes?',
      a: 'Sí. El plan está pensado para chefs que arrancan desde cero. El checklist de apertura reúne 82 tareas en 6 fases: SL o autónomo (con la cuota reducida de inicio de actividad, si te aplica), alta en el epígrafe 677.9 del IAE, facturación Veri*factu, IVA al 10 %, contrato de cocina central autorizada, registro sanitario autonómico, APPCC y seguro de responsabilidad civil con cobertura de intoxicación alimentaria. La guía de especialización progresiva te orienta para empezar con 1-2 conceptos dominados y añadir 1-2/año.',
    },
    {
      q: '¿Cuántos conceptos temáticos cubre el plan?',
      a: 'El plan documenta 12 conceptos pre-empaquetados (sushi-bar omakase, tacos al pastor + trompo móvil, trattoria italiana, asado argentino, ceviche peruano, marisquería gallega, tandoor indio, mediterráneo griego/turco, plant-based premium, brasileño rodízio, BBQ texano slow-smoked, brunch internacional). Cada uno con menú propuesto + equipamiento clave + ambientación + operativa y precio orientativo. La guía de especialización te orienta cómo elegir cuáles dominar primero según tu perfil y zona.',
    },
    {
      q: '¿Qué incluye la plantilla de 96 proveedores?',
      a: 'Cada proveedor lleva web, zona de cobertura y notas operativas, y una columna de estado que arranca en «Por verificar» para que lleves el seguimiento. 12 bloques: importadores asiáticos premium (EMB Food, Cominport, Garmiko, Janax) + latinos/mexicanos (Importaciones Cuesta, CMA, Jasa Internacional, Maíz Maya) + italiano/mediterráneo (Caputo Harinas, Italfoods, Galbani) + indio/tandoor (Spice Box, Patak\'s, TRS Foods, Bombay Spices, iCatering Indian) + BBQ texano (ALEXS BBQ, Dame la Brasa, Smokefire) + carniceros premium (Cesáreo Gómez, Discarlux, El Capricho León, Treviño) + pescaderías + vegano + equipamiento (Wokinox, Josper, Pizza Party, Sammic) + vajilla (Pordamsa, Steelite, Schönwald) + plataformas. Confirma disponibilidad y condiciones con cada uno antes de pedir.',
    },
    {
      q: '¿Cómo cubre el plan la normativa sanitaria del catering?',
      a: 'Con la sección de aspectos legales del plan de negocio y la fase 2 del checklist: cocina central autorizada (para eventos no se puede cocinar en casa, RD 1021/2022), inscripción en el registro sanitario de tu comunidad autónoma previa declaración responsable (el RGSEAA, sólo si suministras a otros establecimientos), transporte en vehículo ATP, seguros y permisos de evento. Los trámites y plazos concretos los fija tu comunidad y tu ayuntamiento: confírmalos antes de abrir. Además, el manual técnico trae el APPCC multi-concepto (cada concepto tiene riesgos distintos: pescado crudo sushi vs cordero asado argentino vs tandoor indio).',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El plan financiero Excel tiene 9 hojas: inversión inicial, PyG previsional a 3 años, punto de equilibrio en invitados por evento y en ingresos (el plan en Word lo traduce a eventos al año), escenarios pesimista y optimista, personal, tesorería de 12 meses con el IVA trimestral y financiación con recursos propios, préstamo con carencia, cuadro de amortización y DSCR. El plan de negocio en Word cuenta las mismas cifras. Sirve para presentarlo al banco, aunque la aprobación siempre depende de la entidad.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
    },
    {
      q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
      a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio para Catering & Kit Temático para Eventos» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, «tesorería» es «flujo de efectivo» en México y «flujo de caja» en Argentina; «camarero» es «mesero» en México y «mozo» en Argentina. Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Lanzar tu ',
    headingGold: 'Catering Temático Multi-concepto',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a sushi masters, taqueros, pizzaiolos, asadores argentinos, chefs ceviche y tandoor masters que ya montaron o escalaron su catering temático multi-concepto con un plan adaptado al mercado español premium.',
    items: [
      'Plan de negocio en Word (10 secciones) + Plan financiero Excel de 9 hojas',
      'Calculadora de precios por invitado + Plantilla de 96 proveedores · 12 cocinas del mundo',
      'Catálogo equipamiento multi-cocina (cuchillería japonesa, horno leña, tandoor, smoker, wok)',
      '12 conceptos pre-empaquetados + Carta 12 menús temáticos cocinas del mundo',
      'Manual técnico APPCC multi-concepto + Modelos contrato B2C + B2B corporate (con MSA)',
      'Guía especialización progresiva — escalar de 1 a 6+ conceptos en portafolio',
      'Checklist de apertura: 82 tareas en 6 fases, con los trámites españoles',
      'BONUS: Guía de Equivalencias para tu país',
      'Acceso de por vida + 30 días garantía devolución',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  pricing: {
    priceOld: '€165',
    price: '€45',
    discountBadge: '-73%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 73 % de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €120 HOY!',
  },

  stickyLabel: 'PLAN CATERING TEMÁTICO — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-chef-privado-showcooking-eventos', label: 'Plan Chef Privado / Showcooking' },
    { href: '/plan-negocio-paellero-eventos', label: 'Plan Paellero Eventos' },
    { href: '/plan-negocio-finca-eventos-bodas', label: 'Plan Finca de Eventos y Bodas' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.2 · octubre 2026',

  alreadyBought: {
    product: 'plan-catering-tematico-eventos',
    label: '¿Ya compraste el Plan Catering Temático? Vuelve a entrar al dashboard',
  },
};

export default data;
