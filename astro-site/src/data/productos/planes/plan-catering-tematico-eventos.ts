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
      'Plan + kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España 2026. El único kit que enseña a montar 5 conceptos en paralelo (sushi-bar, tacos al pastor, pizza al horno de leña, asado argentino, ceviche peruano, vegano premium, BBQ texano, tandoor indio…). Modelo dual B2C bodas multiculturales + B2B corporate brand events. 11 entregables. Inversión desde 5.500 EUR. €45.',
    keywords:
      'plan negocio catering temático, catering eventos multi-concepto, catering bodas multiculturales, brand events corporate, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-catering-tematico-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio para Catering & Kit Temático para Eventos — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium de catering temático multi-concepto para eventos en España 2026. El único kit del mercado español enfocado en multi-concepto (3-5 cocinas del mundo en paralelo en un mismo evento). Modelo dual B2C bodas multiculturales + B2B corporate brand events. Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C 35 % + B2B 65 %, Calculadora Pricing multi-concepto, plantilla de 96 proveedores especializados en 12 cocinas del mundo (importadores asiáticos, latinos, italianos, BBQ texano, indios), catálogo equipamiento multi-cocina (cuchillería japonesa, horno leña, tandoor, smoker, wok), 12 conceptos pre-empaquetados, carta 12 menús cocinas del mundo, manual técnico APPCC multi-concepto, modelos contrato B2C + B2B corporate, guía especialización progresiva y checklist apertura con anexo regulación 17 CCAA catering itinerante.',
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
        body: 'El kit me dio el blueprint para escalar de hacer sushi en mi casa a montar 4 estaciones (sushi + ramen + dim sum + bao) en bodas multiculturales premium. Subí ticket de 38 € a 75 €/pax en 8 meses.',
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
        a: 'Esos productos son monoconcepto. Este es el ÚNICO multi-concepto: enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (sushi-bar + pizza al horno de leña + asado argentino simultáneamente). Justifica ticket 70-130 €/pax frente a 45-85 €/pax monoconcepto.',
      },
      {
        q: '¿Cuántos conceptos temáticos cubre?',
        a: '12 conceptos pre-empaquetados: sushi-bar omakase, tacos al pastor, trattoria italiana, asado argentino, ceviche peruano, marisquería gallega, tandoor indio, mediterráneo griego/turco, plant-based premium, brasileño rodízio, BBQ texano slow-smoked, brunch internacional. Cada uno con menú + escandallo + equipamiento + ambientación + operativa.',
      },
      {
        q: '¿Cómo cubre la regulación catering itinerante por CCAA?',
        a: 'Anexo dedicado con resumen operativo de 17 CCAA: Registro Sanitario + RGSEAA, requisitos cocina cliente, normativa transporte alimentos, etiquetado bilingüe Cataluña/País Vasco, trámites telemáticos vs presenciales. Plus orientación específica APPCC multi-concepto.',
      },
      {
        q: '¿Cómo funciona la garantía?',
        a: '30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
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
      'El kit profesional para montar tu servicio premium de catering temático multi-concepto para eventos en España. Modelo dual B2C bodas multiculturales + B2B corporate brand events, con 11 entregables y 96 proveedores especializados en 12 cocinas del mundo (sushi-bar, tacos al pastor, pizza al horno de leña, asado argentino, ceviche peruano, vegano premium, BBQ texano, tandoor indio…). Inversión 5-9x menor que un catering con cocina central.',
    checkItems: [
      'Plan de negocio DOCX completo (60+ pp.) con anexo regulación 17 CCAA catering itinerante',
      'Plan Financiero Excel: P&L 3 años con mix B2C 35 % + B2B 65 % multi-concepto',
      'Plantilla 96 proveedores reales (12 cocinas del mundo + equipamiento + servicios)',
      'Catálogo equipamiento multi-cocina: cuchillería japonesa, horno leña, tandoor, smoker, wok',
      '12 conceptos temáticos pre-empaquetados con menú + escandallo + ambientación + pricing',
      'Carta 12 menús temáticos cocinas del mundo (sushi, mexicano, italiano, argentino, indio…)',
      'Manual técnico APPCC multi-concepto (7 PCC adaptados + cronograma multi-station)',
      'Modelos contrato B2C + B2B corporate (con MSA acuerdo marco anual y confidencialidad)',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales con datos reales del mercado español 2026 para montar tu catering temático multi-concepto premium con 12 cocinas del mundo en portafolio.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026 (4.585 M€ catering, 25.183 € boda media), top 14 conceptos temáticos validados, modelo multi-concepto sin local fijo, anexo 17 CCAA, financiero 3 años, riesgos, roadmap progresivo.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 35 % + B2B 65 %, inversión 5.500-35.000 EUR según escenario, estacionalidad bodas mayo-octubre + corporate diciembre, break-even 14 eventos/mes año 1, ticket medio 2.200-4.500 €.' },
      { icon: 'Calculator', title: 'Calculadora Pricing Multi-concepto', desc: 'Excel con fórmulas duales B2C + B2B + factor multi-concepto. Inputs: pax, distancia, número conceptos (1-5+), nivel calidad, pairing, branded experience, freelance especializado ⇒ precio sugerido + margen. 10 ejemplos validados.' },
      { icon: 'Truck', title: 'Plantilla 96 Proveedores · 12 Cocinas', desc: 'Importadores asiáticos (EMB Food, Cominport, Garmiko) + latinos (Imp. Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento + plataformas.' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento Multi-cocina', desc: 'Por concepto: cuchillería japonesa sushi (Tojiro, Yoshihiro) + horno leña pizza (Pizza Party, Ooni Pro) + parrilla argentina + trompo pastor + tandoor portátil + smoker offset texano + wok pro (Wokinox) + sous-vide (Anova, Sammic) + vajilla premium.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC móvil multi-concepto + RGSEAA) · seguros RC eventos con cláusula intoxicación · proveedores especializados 12 cocinas · marca multi-concepto · captación B2C+B2B · operativa primer evento multi-station. 110 hitos.' },
      { icon: 'LayoutGrid', title: '12 Conceptos Temáticos Pre-empaquetados', desc: 'Sushi-bar omakase + tacos al pastor + trattoria italiana + asado argentino + ceviche peruano + marisquería gallega + tandoor indio + mediterráneo + vegano premium + brasileño rodízio + BBQ texano + brunch internacional. Cada uno con menú + ambientación + equipamiento + operativa.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B Corporate', desc: 'Plantillas legales editables: B2C particular (boda multicultural, cumpleaños temático, aniversarios) + B2B corporate (brand event, embajada, festival gastronómico, planner) con MSA acuerdo marco anual, confidencialidad y propiedad intelectual del menú multi-concepto.' },
      { icon: 'Utensils', title: 'Carta 12 Menús Cocinas del Mundo', desc: 'Boda multicultural premium 7 estaciones + tasting Asia 7 pasos + mexicano Día de Muertos + italiano trattoria + argentino tradicional + peruano Lima + indio Bollywood + griego/turco + vegano premium + BBQ texano + brunch internacional + mariscada gallega.' },
      { icon: 'Flame', title: 'Manual Técnico APPCC Multi-concepto', desc: '7 PCC adaptados a multi-cocina simultánea (cadena frío diferenciada, T° servicio por concepto, alérgenos en multi-station) + cronograma evento 80 pax + layout multi-station + coordinación equipo freelance especializado por concepto.' },
      { icon: 'BookOpen', title: 'Guía Especialización Progresiva', desc: 'Cómo construir tu portafolio de cocinas del mundo: empieza con 1-2 conceptos, añade 1-2/año validando demanda. Roadmap 12 meses para llegar a 6 conceptos. Top 5 mejores conceptos para empezar + 4 sub-explotados (oportunidad). Modelo escalable y validado España 2026.' },
    ],
  },

  testimonials: {
    subtitle:
      'Sushi masters, taqueros, pizzaiolos, asadores argentinos, chefs ceviche peruano, tandoor masters, plant-based premium y BBQ pitmasters que usaron el plan para montar o escalar su catering temático multi-concepto en España',
    items: [
      { name: 'Yuki Tanaka', role: 'Sushi master para eventos premium, Madrid', text: 'El kit me dio el blueprint para escalar de hacer sushi en mi casa a montar 4 estaciones (sushi + ramen + dim sum + bao) en bodas multiculturales premium. Subí ticket de 38 € a 75 €/pax en 8 meses.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Miguel Hernández', role: 'Taquero pro showcooking, Madrid', text: 'Empecé con tacos al pastor en cumpleaños familiares. Tras el plan añadí cochinita pibil + ceviche peruano + barra mezcal y ahora hago corporate brand events de 80-150 pax con 4 estaciones. La guía de especialización progresiva fue clave.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Giuseppe Romano', role: 'Pizzaiolo móvil + trattoria eventos, Toledo', text: 'Tenía un horno de leña móvil y hacía bodas con sólo pizza. El kit me enseñó a integrar pasta fresca + antipasti + dolci en mi servicio. Ahora ofrezco trattoria completa por 65 €/pax y subí volumen 3x.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Diego Ferreyra', role: 'Asador argentino premium, Madrid', text: 'El plan financiero con multi-concepto me convenció de añadir BBQ texano a mi asado argentino. Ahora cubro bodas y corporate outdoor con 2 conceptos potentes. Margen subió del 48 % al 58 %.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Carolina Vega', role: 'Chef ceviche + barra Pisco, Barcelona', text: 'La calculadora pricing dual + el factor multi-concepto me ahorró 6 meses de prueba y error. Hago bodas premium peruano + brunch latino y ya cierro presupuestos en 10 minutos con margen real del 55 %.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Rajesh Patel', role: 'Tandoor master + curry station, Madrid', text: 'Ofrezco tandoor móvil para bodas multiculturales y embajadas. El kit me organizó proveedores premium (Spice Box, TRS Foods) y la matriz de 96 proveedores fue oro. Ticket medio embajadas 110 €/pax.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Carmen Soler', role: 'Catering vegano premium, Madrid', text: 'El catering vegano ESG está explotando para corporate. El plan + la guía de especialización me clarificaron cómo posicionarme premium (45-85 €/pax) y no como alternativa low-cost. Brand events corporate son ahora mi 65 % de ingresos.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sam Williams', role: 'Texas BBQ pitmaster, Madrid', text: 'Slow-smoked BBQ con smoker offset es nicho en España. El plan me dio el dossier B2B y los modelos de contrato MSA — cerré acuerdo marco anual con 2 empresas tech corporate creativo en Madrid.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo del mercado español para montar tu catering temático multi-concepto premium: 11 entregables con 12 cocinas del mundo, 96 proveedores especializados (importadores asiáticos, latinos, italianos, BBQ texano), datos reales 2026 (4.585 M€ catering España, boda media 25.183 €) y anexo regulación 17 CCAA.',
    reasons: [
      { icon: 'Globe', title: 'Único Plan España con Modelo Multi-concepto', desc: 'El ÚNICO plan del mercado español que enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (sushi-bar + pizza al horno de leña + asado argentino simultáneamente), no monoconcepto. Justifica ticket 70-130 €/pax frente a 45-85 €/pax monoconcepto, con márgenes 30-40 % más altos.' },
      { icon: 'BarChart3', title: 'Modelo Dual B2C Bodas Multiculturales + B2B Corporate', desc: 'Mix B2C 35 % (bodas multiculturales, cumpleaños temáticos, aniversarios) + B2B 65 % (corporate brand events, embajadas, wedding planners, festivales gastronómicos, hoteles boutique). Calculadora pricing dual con factor multi-concepto y modelos de contrato para cada canal.' },
      { icon: 'ShieldCheck', title: '96 Proveedores · 12 Cocinas del Mundo', desc: 'Importadores asiáticos premium (EMB Food, Cominport, Garmiko) + latinos/mexicanos (Importaciones Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ texano (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento + plataformas.' },
      { icon: 'Banknote', title: 'Inversión Mínima 5.500 EUR', desc: '5-9x menor que un catering con cocina central (45-120K EUR). Escenario mínimo viable, recomendado 11.500 EUR o premium hasta 35.000 EUR. Break-even 14 eventos/mes año 1. Pago único, sin suscripciones.' },
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
      'Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €114',
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
      a: 'Esos productos son monoconcepto (un único producto/servicio: parrilla, paella o chef privado). Este es el ÚNICO multi-concepto: enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (ejemplo: sushi-bar + pizza al horno de leña + asado argentino simultáneamente). Esto justifica ticket 70-130 €/pax frente a 45-85 €/pax monoconcepto, con márgenes 30-40 % más altos. Pensado para emprendedores que quieren un sistema operativo, no una receta.',
    },
    {
      q: '¿Sirve si nunca he montado mi propio negocio antes?',
      a: 'Sí. El plan está pensado para chefs que arrancan desde cero. Incluye constitución autónomo (tarifa plana 80 EUR/mes primer año), alta IAE 677.9, plan APPCC móvil multi-concepto, RGSEAA, seguro RC profesional eventos con cláusula intoxicación. La guía de especialización progresiva te orienta para empezar con 1-2 conceptos dominados y añadir 1-2/año. El checklist de 6 fases con 110 hitos no se te escapa nada.',
    },
    {
      q: '¿Cuántos conceptos temáticos cubre el plan?',
      a: 'El plan documenta 12 conceptos pre-empaquetados (sushi-bar omakase, tacos al pastor + trompo móvil, trattoria italiana, asado argentino, ceviche peruano, marisquería gallega, tandoor indio, mediterráneo griego/turco, plant-based premium, brasileño rodízio, BBQ texano slow-smoked, brunch internacional). Cada uno con menú propuesto + escandallo + equipamiento clave + ambientación + operativa específica. La guía de especialización te orienta cómo elegir cuáles dominar primero según tu perfil y zona.',
    },
    {
      q: '¿La plantilla de 96 proveedores incluye contactos verificables?',
      a: 'Sí. Cada proveedor lleva web, zona de cobertura y notas operativas. 12 bloques: importadores asiáticos premium (EMB Food, Cominport, Garmiko, Janax) + latinos/mexicanos (Importaciones Cuesta, CMA, Jasa Internacional, Maíz Maya) + italiano/mediterráneo (Caputo Harinas, Italfoods, Galbani) + indio/tandoor (Spice Box, Patak\'s, TRS Foods, Bombay Spices, iCatering Indian) + BBQ texano (ALEXS BBQ, Dame la Brasa, Smokefire) + carniceros premium (Cesáreo Gómez, Discarlux, El Capricho León, Treviño) + pescaderías + vegano + equipamiento (Wokinox, Josper, Pizza Party, Sammic) + vajilla (Pordamsa, Steelite, Schönwald) + plataformas. Verifica con cada uno antes de cerrar acuerdos.',
    },
    {
      q: '¿Cómo cubre el plan la regulación de catering itinerante por CCAA?',
      a: 'Con un anexo dedicado en el Plan de Negocio. Resumen operativo de 17 comunidades autónomas: Registro Sanitario CCAA + RGSEAA, requisitos cocina cliente, normativa transporte alimentos, etiquetado bilingüe (Cataluña, País Vasco), trámites telemáticos vs presenciales y plazos. Plus orientación específica APPCC multi-concepto (cada concepto tiene riesgos distintos: pescado crudo sushi vs cordero asado argentino vs tandoor indio).',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (14 eventos/mes break-even año 1), 3 escenarios inversión (5.500 € mínimo viable / 11.500 € recomendado / 35.000 € premium), mix B2C+B2B desglosado por canal, plan cashflow con estacionalidad bodas + corporate. Formato estándar bancos para microcrédito o ICO emprendedores.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Lanzar tu ',
    headingGold: 'Catering Temático Multi-concepto',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a sushi masters, taqueros, pizzaiolos, asadores argentinos, chefs ceviche y tandoor masters que ya montaron o escalaron su catering temático multi-concepto con un plan adaptado al mercado español premium.',
    items: [
      'Plan de Negocio DOCX 60+ pp. + Plan Financiero Excel 6 hojas',
      'Calculadora Pricing multi-concepto + Plantilla 96 proveedores · 12 cocinas del mundo',
      'Catálogo equipamiento multi-cocina (cuchillería japonesa, horno leña, tandoor, smoker, wok)',
      '12 conceptos pre-empaquetados + Carta 12 menús temáticos cocinas del mundo',
      'Manual técnico APPCC multi-concepto + Modelos contrato B2C + B2B corporate (con MSA)',
      'Guía especialización progresiva — escalar de 1 a 6+ conceptos en portafolio',
      'Checklist apertura 6 fases + anexo regulación 17 CCAA catering itinerante',
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
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'plan-catering-tematico-eventos',
    label: '¿Ya compraste el Plan Catering Temático? Vuelve a entrar al dashboard',
  },
};

export default data;
