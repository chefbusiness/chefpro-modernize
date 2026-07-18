// astro-site/src/data/productos/planes/plan-negocio-paellero-eventos.ts
// LÍNEA PLANES (sub-línea B "planes de eventos") — usa el MISMO template único PlanNegocioLandingPage
// (ver types.ts para el veredicto del diff). Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioPaelleroEventos.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-paellero-eventos/*  (los 10 componentes)
//   · src/data/testimonials-plan-paellero-eventos.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (constante de línea, hardcodeada en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_PAELLERO (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Lanzar tu ' (patrón de la sub-línea B).
//   · hero.checkItems tiene 8 elementos.
//   · authorBadges se OMITE → default ['Consultor Gastronómico', '+29 años en alta hostelería']
//     (= el de este producto, verificado byte a byte contra AuthorSection.tsx).
//   · images.gallery usa extensión .jpg — VERBATIM de la SPA.
//
// QUIRKS VERBATIM:
//   · titlePre / seo.title / schema.productName llevan un '&' literal (la SPA lo escribe '&amp;' en JSX y
//     como '&' en JSON.stringify; aquí se escribe '&' y el template/BaseLayout lo escapan igual en HTML).
//   · schema.faqs (FAQPage JSON-LD) = 5 preguntas (subconjunto VERBATIM del Helmet); faqs on-page
//     (acordeón) = 7, más largas y en orden distinto (schema NO es un prefijo del acordeón).
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-paellero-eventos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_PAELLERO',

  seo: {
    title:
      'Plan de Negocio & Kit Paellero / Paella para Eventos — 11 Entregables | AI Chef Pro',
    description:
      'Plan + kit profesional completo para montar tu servicio premium itinerante de paella y arroces para eventos en España 2026. Modelo híbrido B2C + B2B. 11 entregables: DOCX 60+ pp + Plan Financiero Excel + 88 proveedores DO Valencia + Catálogo equipamiento + Manual técnico del fuego + socarrat + Carta 12 paellas + Modelos contrato B2C/B2B + Guía 8 sistemas + roadmap food truck arrocería. Inversión desde 3.500 EUR. €45.',
    keywords:
      'plan de negocio paellero, paella eventos, arroz para eventos, mestre arrosser, paella valenciana premium, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-paellero-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio & Kit de Paellero / Paella para Eventos — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium itinerante de paella y arroces para eventos en España 2026. Modelo híbrido B2C particular (bodas, comuniones, fiestas del pueblo, cumpleaños) + B2B (wedding planners, agencias, hoteles 4-5*, ayuntamientos, empresas team-building). Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 88 proveedores reales DO Valencia + Calasparra, catálogo equipamiento + menaje, manual técnico paellero (técnica del fuego + socarrat + 6 arroces + 3 caldos + 12 paellas), carta de 12 paellas, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck arrocería y checklist de apertura con anexo CCAA fuego al aire libre y excepción Falles.',
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
        author: 'Vicent Pellicer',
        rating: '5',
        body: 'Llevo 25 años haciendo paellas en fiestas del pueblo y siempre me faltó el plan de negocio para escalar a bodas premium. La calculadora pricing y el modelo contrato B2B me cerraron 4 wedding planners en 2 meses.',
      },
      {
        author: 'Carmen Soler',
        rating: '5',
        body: 'El manual técnico del fuego y el socarrat es oro puro. La tabla de cocción de 12 paellas la imprimí y la tengo plastificada en la furgo. Mis bodas en finca mejoraron en consistencia desde la primera temporada.',
      },
      {
        author: 'Marc Esteve',
        rating: '5',
        body: 'Empecé con 4.200 EUR siguiendo el escenario mínimo viable. En el segundo año ya facturo más de 95.000 EUR. La plantilla de 88 proveedores DO Valencia me ahorró 3 meses de búsqueda.',
      },
    ],
    // FAQPage schema (5 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 7, más largas)
    faqs: [
      {
        q: '¿Para quién está pensado este plan?',
        a: 'Para profesionales del arroz y la paella — mestres arrossers valencianos, paelleros murcianos, alicantinos, paelleros corporate o emprendedores españoles — que quieren montar un servicio premium itinerante para eventos en España. Cubre cliente final particular (bodas íntimas, cumpleaños, comuniones, fiestas del pueblo) y B2B (wedding planners, agencias, hoteles, ayuntamientos, empresas team-building).',
      },
      {
        q: '¿Qué diferencia hay con un Restaurante de Arroces con local fijo?',
        a: 'Modelo itinerante sin local: sin licencia clasificada (autorizaciones puntuales por evento), sin plantilla fija, inversión 4-7x menor (3.500-25.000 EUR vs 70-130K), ingresos concentrados mayo-octubre + Falles (70-75 % facturación), captación B2B intensiva con wedding planners.',
      },
      {
        q: '¿Cómo cubre la regulación del fuego al aire libre por CCAA?',
        a: 'Anexo dedicado con autorización exigida y restricciones (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL, IBANAT, SOSDeiak, PIDOM) en 8 comunidades + excepciones para finca privada y excepción cultural Falles/festes valencianas — vital para paelleros del Levante.',
      },
      {
        q: '¿Sirve para presentar al banco?',
        a: 'Sí. Plan Financiero Excel con P&L 3 años, break-even 18-22 eventos año 1, 3 escenarios de inversión, mix B2C+B2B y plan de cashflow estacional. Formato ICO/microcrédito.',
      },
      {
        q: '¿Cómo funciona la garantía?',
        a: '30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio Paellero / Paella Eventos',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-1.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-3.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-5.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (empieza en -1, termina en -6)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-1.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-3.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-5.jpg',
      '/lovable-uploads/ai-gallery/plan-paellero-eventos-6.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-paellero-eventos-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-paellero-eventos-4.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-paellero-eventos-hero.jpg',
  },

  hero: {
    badge: 'El plan más completo de España para montar tu servicio premium de paella y arroces para eventos',
    titlePre: 'Plan de Negocio & Kit de ',
    titleGold: 'Paellero / Paella',
    titleSubtitle: 'para Eventos — 11 Entregables Profesionales',
    description:
      'El kit profesional para montar tu empresa itinerante de paella y arroces para eventos en España. Modelo híbrido B2C particular (bodas, comuniones, fiestas del pueblo, cumpleaños) + B2B (wedding planners, agencias, hoteles 4-5*, ayuntamientos, empresas team-building), con 88 proveedores reales DO Valencia + Calasparra. Inversión 4-7x menor que un restaurante con local fijo.',
    checkItems: [
      'Plan de negocio DOCX completo (60+ pp.) con marco legal CCAA fuego al aire libre',
      'Plan Financiero Excel con mix B2C 35 % + B2B 65 % y estacionalidad mayo-octubre + Falles',
      'Plantilla 88 proveedores reales (arroceros DO Valencia + Calasparra, mariscos Mediterráneo, Garcima, Pordamsa)',
      'Catálogo equipamiento + utensilios + menaje con SKU + URL + precio actualizado',
      'Manual técnico paellero: técnica del fuego + socarrat + 6 tipos arroz + 3 caldos pro + tabla 12 paellas',
      '10 experiencias temáticas + Guía 8 sistemas de cocción + roadmap food truck arrocería',
      '2 modelos de contrato (B2C particular + B2B profesional con anexo tarifario)',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales con datos reales del mercado de eventos español 2026 para validar la viabilidad de tu servicio premium itinerante de paella y arroces.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026, 10 competidores reales, doble embudo B2C+B2B, marco legal CCAA fuego al aire libre, financiero 3 años, riesgos, roadmap 3 años.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 35 % + B2B 65 %, inversión 3.500-25.000 EUR según escenario, estacionalidad mayo-octubre + Falles, break-even por número de eventos.' },
      { icon: 'Calculator', title: 'Calculadora Pricing Eventos', desc: 'Excel con fórmulas duales B2C particular + B2B planner. Inputs: pax, distancia, tipo de paella, concepto premium, ayudantes ⇒ precio sugerido + margen. 10 ejemplos validados.' },
      { icon: 'Truck', title: 'Plantilla 88 Proveedores Reales', desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Calasparra), carniceros, mariscos Mediterráneo, verduras Levante (garrofó, ferraura), azafrán DO La Mancha, equipamiento Garcima/Vaello, vajilla Pordamsa.' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento + Menaje', desc: 'Paelleras Garcima 60-90-120 cm + paellero Vaello 4 fuegos 50 kW + trípode leña + cuchillería Arcos + vajilla Pordamsa + EPI Texfire. SKU + URL + precio actualizado.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC + RGSEAA) · seguros RC eventos con cláusula intoxicación · equipamiento + arroceros DO · marca y web · captación B2C+B2B · operativa primer evento. 110 hitos.' },
      { icon: 'Utensils', title: 'Carta 12 Paellas y Arroces', desc: 'Valenciana DO + marisco premium + senyoret + arroz negro + mixta + arroz a banda + fideuá + meloso bogavante + caldoso bogavante + montaña + alicantina con costra + vegetal DO. Receta + escandallo + maridaje.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas legales editables: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias, ayuntamientos) con anexo tarifario, briefing y SLA.' },
      { icon: 'Sparkles', title: '10 Experiencias Temáticas', desc: 'Boda en finca · corporate showcooking · fiesta del pueblo popular · bautizo familiar · cumpleaños senyoret · Falles + festes · boda exclusiva 5* · hotel show cooking · vegetal DO inclusive · brunch banda + fideuá.' },
      { icon: 'Flame', title: 'Manual Técnico Paellero', desc: 'Técnica del fuego en 4 fases (sofrito, proteínas, caldo+arroz, socarrat) + 6 tipos arroz Bomba/Sendra/Albufera + 3 caldos pro + salmueras + tabla cocción 12 paellas + 4 salsas + errores frecuentes.' },
      { icon: 'Tent', title: 'Guía 8 Sistemas + Food Truck', desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico inducción, gas industrial, portátil camping, caja china peruana, paellero solar. + Roadmap food truck arrocería: inversión 30-75K EUR, regulación 8 CCAA.' },
    ],
  },

  testimonials: {
    subtitle:
      'Paelleros profesionales, mestres arrossers y wedding planners que usaron el plan para montar o impulsar su empresa premium de paella y arroces para eventos',
    items: [
      { name: 'Vicent Pellicer', role: 'Mestre arrosser valenciano, Sueca', text: 'Llevo 25 años haciendo paellas en fiestas del pueblo y siempre me faltó el plan de negocio para escalar a bodas premium. Este kit me dio todo: la calculadora pricing y el modelo contrato B2B me cerraron 4 wedding planners en 2 meses.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Carmen Soler', role: 'Paellera profesional, finca Toledo', text: 'El manual técnico del fuego y el socarrat es oro puro. La tabla de cocción de 12 paellas la imprimí y la tengo plastificada en la furgo. Mis bodas en finca mejoraron en consistencia desde la primera temporada.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Antonio Rivas', role: 'Paellero murciano, Mar Menor', text: 'Soy de Murcia y llevaba años haciendo paella de marisco en eventos privados sin marca. El plan de negocio y el dossier B2B me posicionaron premium en wedding planners de la zona Levante.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Marc Esteve', role: 'Joven emprendedor arrocero, Valencia', text: 'Empecé con 4.200 EUR siguiendo el escenario mínimo viable. En el segundo año ya facturo más de 95.000 EUR. La plantilla de 88 proveedores DO Valencia me ahorró 3 meses de búsqueda.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Sara Romero', role: 'Paellera corporate, Madrid', text: 'Hago corporate showcooking para empresas en terrazas de Madrid y el catálogo de equipamiento con SKU exactos de Garcima me organizó la inversión inicial sin pasarme. La calculadora pricing B2B es la que más uso.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Don Joan Beltrán', role: 'Asador a la leña tradicional, Castellón', text: 'Soy de la vieja escuela del fuego de leña. Pensaba que no necesitaba un plan, pero el anexo legal CCAA + el modelo de contrato profesional me organizaron el papeleo de la primera boda planner que cerré.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Laura Martín', role: 'Paellera de bodas premium, Levante', text: 'Las 10 experiencias temáticas + la carta de 12 paellas me dieron un catálogo comercial de productos empaquetados. El ticket medio subió un 40 % desde que vendo "experiencias" en lugar de "menús".', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Diego Montes', role: 'Paellero alicantino fideuá, Alicante', text: 'Los dos modelos de contrato (B2C + B2B con anexos) son ya mi base de trabajo. Antes redactaba cláusulas sueltas para cada cliente; ahora copio, edito y firmo en 10 minutos.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo de España para montar tu empresa premium de paella y arroces para eventos: 11 entregables reales con datos del mercado 2026, marco legal CCAA fuego al aire libre y modelo híbrido B2C+B2B.',
    reasons: [
      { icon: 'Flame', title: 'Único Plan España con Marco CCAA Fuego', desc: 'Anexo dedicado con autorización exigida, restricciones por temporada (INFOCA, PATRICOVA, PLADIGA, INFOCYL, IBANAT, SOSDeiak) y excepciones para finca privada en 8 CCAA. Cubre la excepción cultural valenciana de Falles y festes — vital para paelleros del Levante.' },
      { icon: 'BarChart3', title: 'Modelo Híbrido B2C + B2B Validado', desc: 'Mix B2C 35 % (bodas, comuniones, fiestas del pueblo, cumpleaños) + B2B 65 % (wedding planners, agencias, hoteles 4-5*, ayuntamientos, empresas team-building). Calculadora pricing dual y modelos de contrato para cada canal.' },
      { icon: 'ShieldCheck', title: '88 Proveedores Reales Validados', desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Marjal, La Fallera) + Bomba Calasparra DO, mariscos Mediterráneo (Linamar, Castellet, Nardín DO Denia), verduras Levante DO, azafrán DO La Mancha, equipamiento Garcima/Vaello, vajilla Pordamsa/Steelite.' },
      { icon: 'Banknote', title: 'Inversión Mínima 3.500 EUR', desc: '4-7x menor que un restaurante de arroces con local fijo (70-130K EUR). Escenario mínimo viable o full equipment hasta 25K EUR. Break-even 18-22 eventos año 1. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha asesorado a mestres arrossers valencianos, paelleros murcianos y alicantinos, y emprendedores arroceros en el lanzamiento de servicios premium itinerantes de paella y arroces para eventos en España.',
  // authorBadges omitido → default ['Consultor Gastronómico', '+29 años en alta hostelería'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €89',
    items: [
      {
        icon: 'Flame',
        label: 'BONUS 1',
        title: 'Manual Técnico Paellero',
        value: '€40',
        desc: 'Técnica del fuego en 4 fases (sofrito, proteínas, caldo + arroz, socarrat) + 6 tipos de arroz Bomba/J. Sendra/Albufera/Sénia + 3 caldos profesionales + salmueras + tabla de cocción de 12 paellas + 4 salsas. La pieza que separa al paellero amateur del profesional.',
        image: '/lovable-uploads/ai-gallery/plan-paellero-eventos-3.jpg',
      },
      {
        icon: 'Tent',
        label: 'BONUS 2',
        title: 'Guía 8 Sistemas + Roadmap Food Truck',
        value: '€49',
        desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico de inducción, gas industrial, portátil camping, caja china peruana y paellero solar. + Roadmap food truck especializado en paella y arroces: inversión 30-75 K EUR y regulación de venta ambulante en 8 CCAA.',
        image: '/lovable-uploads/ai-gallery/plan-paellero-eventos-5.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  guarantee: {
    text:
      'Si el plan de negocio para tu servicio premium itinerante de paella y arroces para eventos no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (7 preguntas; distinto orden/redacción que schema.faqs)
  faqs: [
    {
      q: '¿Para quién está pensado este plan?',
      a: 'Para profesionales del arroz y la paella — mestres arrossers valencianos, paelleros murcianos, alicantinos, paelleros corporate de cualquier zona o emprendedores españoles con dominio del producto — que quieren montar un servicio premium itinerante de paella para eventos en España. Cubre tanto el cliente final particular (cumpleaños, comuniones, bautizos, bodas íntimas en finca) como el cliente B2B (wedding planners, agencias de eventos, hoteles 4-5 estrellas, ayuntamientos con fiestas populares, empresas que contratan team-building gastronómico).',
    },
    {
      q: '¿Sirve si nunca he montado mi propio negocio antes?',
      a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. Incluye la constitución como autónomo (tarifa plana 80 EUR/mes primer año), alta IAE 677.9, plan APPCC adaptado a actividad itinerante, RGSEAA, seguro RC profesional eventos con cláusula intoxicación. El checklist de 6 fases con 110 hitos no deja nada al azar.',
    },
    {
      q: '¿Qué diferencia hay con un Plan de Negocio de Restaurante de Arroces con local fijo?',
      a: 'Todo. Modelo itinerante sin local: sin licencia de actividad clasificada (autorizaciones puntuales por evento), sin plantilla fija (ayudantes freelance bajo demanda solo en eventos > 60 pax), inversión 4-7 veces menor (3.500-25.000 EUR según escenario vs 70-130K EUR de un restaurante fijo), ingresos por evento concentrados mayo-octubre + Falles (70-75 % facturación), captación B2B intensiva con wedding planners. El plan modela todos estos pilares.',
    },
    {
      q: '¿Cómo cubre el plan la regulación del fuego al aire libre por CCAA?',
      a: 'Con un anexo dedicado dentro del Plan de Negocio. Resumen operativo de 8 comunidades (Madrid, Cataluña, Baleares, Andalucía, Comunidad Valenciana, País Vasco, Galicia, Castilla y León) con tipo de autorización exigida, restricciones por temporada (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL, IBANAT, SOSDeiak, PIDOM), excepciones para eventos en finca privada con licencia. La Comunidad Valenciana contempla excepciones culturales para Falles y festes tradicionales — vital para paelleros del Levante.',
    },
    {
      q: '¿La plantilla de 88 proveedores incluye contactos verificables?',
      a: 'Sí. Cada proveedor lleva web, zona de cobertura, notas operativas y estado (validado / investigar). Arroceros DO Valencia (Tartana, J. Sendra, Marjal, La Fallera) + arroz Bomba Calasparra DO + carniceros mayoristas (Hidalgo, Casa López Mercamadrid, Tres Jotas Mercabarna), mariscos del Mediterráneo (Pescaderías Coruñesas, Mariscos Linamar, Mariscos Castellet, Mariscos Nardín gamba roja DO Denia), verduras DO Levante (garrofó, ferraura, alcachofa), azafrán DO La Mancha y pimentón DO Vera, equipamiento Garcima/Vaello/GGM, vajilla Pordamsa/Steelite.',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (18-22 eventos break-even año 1), 3 escenarios de inversión (3.500 € mínimo viable / 8.500-12.000 € recomendado / 25.000 € premium), mix B2C+B2B desglosado y plan de cashflow con estacionalidad. Es el formato estándar que piden bancos para microcrédito o ICO emprendedores.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Lanzar tu ',
    headingGold: 'Servicio Premium de Paella',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a mestres arrossers, paelleros profesionales y emprendedores arroceros que ya escalaron su servicio itinerante con un plan adaptado al mercado español de eventos.',
    items: [
      'Plan de Negocio DOCX 60+ pp. + Plan Financiero Excel 6 hojas',
      'Calculadora Pricing eventos B2C + B2B + Plantilla 88 proveedores DO Valencia',
      'Catálogo equipamiento + utensilios + menaje (SKU Garcima, Vaello, Pordamsa, Texfire)',
      'Manual técnico paellero + Carta 12 paellas + 10 experiencias temáticas',
      'Modelos contrato B2C + B2B + Guía 8 sistemas + roadmap food truck arrocería',
      'Checklist apertura 6 fases + anexo CCAA fuego al aire libre',
      'Acceso de por vida + 30 días de garantía de devolución',
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

  stickyLabel: 'PLAN PAELLERO EVENTOS — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-parrillero-asador-eventos', label: 'Plan Parrillero Eventos' },
    { href: '/plan-negocio-cocteleria-eventos', label: 'Plan Coctelería Eventos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'plan-negocio-paellero-eventos',
    label: '¿Ya compraste el Plan Paellero / Paella Eventos? Vuelve a entrar al dashboard',
  },
};

export default data;
