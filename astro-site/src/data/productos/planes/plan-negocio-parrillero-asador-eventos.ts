// astro-site/src/data/productos/planes/plan-negocio-parrillero-asador-eventos.ts
// LÍNEA PLANES (sub-línea B "planes de eventos") — usa el MISMO template único PlanNegocioLandingPage
// (ver types.ts para el veredicto del diff). Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioParrilleroAsadorEventos.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-parrillero-asador-eventos/*  (los 10 componentes)
//   · src/data/testimonials-plan-parrillero-asador-eventos.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (constante de línea, hardcodeada en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_PARRILLERO (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Lanzar tu ' (patrón de la sub-línea B).
//   · hero.checkItems tiene 8 elementos.
//   · authorBadges se OMITE → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años']
//     (= el de este producto, verificado byte a byte contra AuthorSection.tsx).
//   · images.gallery usa extensión .jpg (no .jpeg como cocteleria-eventos) — VERBATIM de la SPA.
//
// QUIRKS VERBATIM:
//   · titlePre / seo.title / schema.productName llevan un '&' literal (la SPA lo escribe '&amp;' en JSX y
//     como '&' en JSON.stringify; aquí se escribe '&' y el template/BaseLayout lo escapan igual en HTML).
//   · schema.faqs (FAQPage JSON-LD) = 5 preguntas (subconjunto VERBATIM del Helmet); faqs on-page
//     (acordeón) = 7, más largas y en orden distinto (schema NO es un prefijo del acordeón).
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-parrillero-asador-eventos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_PARRILLERO',

  seo: {
    title:
      'Plan de Negocio & Kit Parrillero / Asador para Eventos — 11 Entregables | AI Chef Pro',
    description:
      'Plan + kit profesional completo para montar tu servicio premium itinerante de parrilla y asado para eventos en España. Modelo híbrido para particulares y empresas. 11 entregables: plan de negocio en Word de 10 secciones con anexo del fuego al aire libre + plan financiero Excel de 9 hojas + calculadora de presupuestos por evento + checklist de apertura de 83 tareas + 93 proveedores + catálogo de equipamiento + manual técnico del parrillero + carta de 12 cortes + contratos B2C/B2B + guía de 8 sistemas y roadmap de food truck. €45.',
    keywords:
      'plan de negocio parrillero, parrilla eventos, asador a la cruz, BBQ pitmaster España, parrilla itinerante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-parrillero-asador-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio & Kit de Parrillero / Asador para Eventos — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium itinerante de parrilla y asado para eventos en España. Modelo híbrido B2C particular (bodas, cumpleaños, bautizos) + B2B (wedding planners, agencias, hoteles, empresas, restaurantes show cooking). Incluye plan de negocio en Word de 10 secciones con anexo del fuego al aire libre en 8 comunidades, plan financiero Excel de 9 hojas, calculadora de presupuestos por evento con IVA, escalado y tramos de cancelación, plantilla de 93 proveedores, catálogo de equipamiento + menaje, manual técnico del parrillero (8 salmueras + 12 marinados + 18 cortes + escalado), carta de 12 cortes, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck y checklist de apertura de 83 tareas.',
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
        author: 'Mariano Rodríguez',
        rating: '5',
        body: 'Llevaba 12 años de empleado en parrilla y este plan me dio la hoja de ruta para independizarme. Las 10 experiencias y la calculadora de pricing son lo que más uso ahora.',
      },
      {
        author: 'Lucía Sanz',
        rating: '5',
        body: 'El manual técnico de salmueras y la tabla de cocción de 18 cortes vale el plan entero. Mis bodas mejoraron en consistencia desde la primera temporada con esta guía.',
      },
      {
        author: 'Diego López',
        rating: '5',
        body: 'El roadmap del food truck especializado en parrilla es brutal. Invertí 30.000 EUR siguiendo el blueprint y arranqué con eventos corporate en 6 meses.',
      },
    ],
    // FAQPage schema (5 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 7, más largas)
    faqs: [
      {
        q: '¿Para quién está pensado este plan?',
        a: 'Para profesionales de la parrilla — argentinos, uruguayos, colombianos, asadores castellanos o emprendedores españoles — que quieren montar un servicio premium itinerante para eventos en España. Cubre cliente final particular (bodas, cumpleaños, bautizos) y B2B (wedding planners, agencias, hoteles, restaurantes show cooking).',
      },
      {
        q: '¿Qué diferencia hay con un Plan de Asador con local fijo?',
        a: 'Modelo itinerante sin local propio: trabajas desde una cocina de apoyo autorizada y pides los permisos de cada evento. Ayudantes contratados como fijos discontinuos, ingresos concentrados en la temporada de bodas y fiestas y captación con wedding planners y empresas. El Excel calcula tu caso: inversión, punto de equilibrio y tesorería mes a mes.',
      },
      {
        q: '¿Cómo cubre la regulación del fuego al aire libre por CCAA?',
        a: 'Anexo dedicado en el plan de negocio para 8 comunidades: su plan de incendios forestales, la época de peligro, la franja alrededor del monte y la autorización que se pide. En terreno forestal o en esa franja la restricción se aplica aunque la finca tenga licencia, y los contratos llevan fuerza mayor con plan B.',
      },
      {
        q: '¿Sirve para presentar al banco?',
        a: 'Sí. Plan financiero Excel de 9 hojas con cuenta de resultados a 3 años, punto de equilibrio, escenarios pesimista y optimista, tesorería de 12 meses y financiación con préstamo, cuadro de amortización y DSCR. La aprobación siempre depende de la entidad.',
      },
      {
        q: '¿Cómo funciona la garantía?',
        a: '30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio Parrillero / Asador Eventos',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-1.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-3.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-5.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (empieza en -1, termina en -6)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-1.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-3.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-4.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-5.jpg',
      '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-6.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-4.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-hero.jpg',
  },

  hero: {
    badge: 'El plan más completo para montar tu servicio premium de parrilla itinerante',
    titlePre: 'Plan de Negocio & Kit de ',
    titleGold: 'Parrillero / Asador',
    titleSubtitle: 'para Eventos — 11 Entregables Profesionales',
    description:
      'El kit profesional para montar tu servicio premium itinerante de parrilla y asado para eventos en España. Modelo híbrido B2C particular (bodas, cumpleaños, bautizos) + B2B (wedding planners, agencias, hoteles, empresas, restaurantes show cooking). Con el caso calculado en un Excel de 9 hojas.',
    checkItems: [
      'Plan de negocio en Word de 10 secciones con anexo del fuego al aire libre en 8 comunidades',
      'Plan financiero Excel de 9 hojas: cuenta de resultados, IVA, préstamo y tesorería de 12 meses',
      'Plantilla de 93 proveedores (carniceros mayoristas, GGM, Tienda Biomasa, Texfire) y checklist de 83 tareas',
      'Catálogo equipamiento + utensilios + menaje con SKU + URL + precio orientativo',
      'Manual técnico parrillero: 8 salmueras + 12 marinados + tabla de cocción de 18 cortes + escalado',
      '10 experiencias temáticas + Guía 8 sistemas de parrilla + roadmap food truck',
      'Calculadora de presupuestos + 2 modelos de contrato (B2C particular + B2B profesional)',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales para calcular y poner en marcha tu servicio premium itinerante de parrilla y asado para eventos en España.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 Secciones + Anexo)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, equipo, plan financiero, aspectos legales y plan de acción, más un anexo del fuego al aire libre en 8 comunidades: en A4 y con las cifras del Excel.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (9 Hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio (en invitados por evento y en ingresos; el plan en Word lo traduce a eventos al año), escenarios, personal, tesorería de 12 meses y financiación con cuadro del préstamo. Con IVA, cocina de apoyo autorizada, sueldo del dueño, amortización y ayudantes fijos discontinuos.' },
      { icon: 'Calculator', title: 'Calculadora de Presupuestos por Evento', desc: 'De los invitados a la carne cruda, las parrillas, los parrilleros y el carbón que necesitas, con el precio por invitado sin IVA y con IVA (10 %), cobro y tramos de cancelación para particular o empresa. 3 presupuestos de ejemplo calculados: boda de 110 invitados, evento de empresa de 70 y fiesta municipal de 300.' },
      { icon: 'Truck', title: 'Plantilla de 93 Proveedores', desc: 'Carniceros mayoristas (Hidalgo, Casa López, Tres Jotas), GGM Gastro (parrillas), Tienda Biomasa (carbón quebracho), Texfire (EPI), Hosply.pro y más. Con web y zona, y una columna de estado que arranca en «Por verificar».' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento + Menaje', desc: 'Parrilla GGM KGE1200 709 EUR + Brogas asador cruz + Comander COMPER-M ahumador + cuchillería Arcos + vajilla eventos + EPI Texfire. SKU + URL + precio orientativo.' },
      { icon: 'ShieldCheck', title: 'Checklist de Apertura (83 Tareas)', desc: 'Seis fases: constitución y fiscalidad (SL o autónomo, IAE, IVA al 10 %) · cocina de apoyo autorizada, registro sanitario, APPCC, fuego y permisos, seguros · equipamiento y proveedores · personal y formación · marca y captación · primer evento y primeros 90 días.' },
      { icon: 'Beef', title: 'Carta 12 Cortes de Carne', desc: 'Argentinos (asado tira, bife chorizo, vacío) + castellanos (cordero a la cruz, cochinillo) + picaña y tomahawk + BBQ texano (brisket, ribs). Técnica + Tº + merma + maridaje.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas editables y orientativas (revísalas con tu asesor): B2C particular (cumpleaños, bautizos, bodas) + B2B profesional (wedding planners, agencias) con anexo tarifario. IVA al 10 %, cancelación por tramos, sin derecho de desistimiento en un servicio con fecha y fuerza mayor con plan B de gas.' },
      { icon: 'Sparkles', title: '10 Experiencias Temáticas', desc: 'Asado argentino, asador a la cruz, parrilla uruguaya, BBQ texano, rodizio brasileño, asador criollo, mediterránea, llanera, show de fuego y brunch parrillero corporate.' },
      { icon: 'Flame', title: 'Manual Técnico Parrillero', desc: '8 salmueras + 12 marinados + tabla de cocción de 18 cortes con Tº interna y merma + escalado de carne cruda, parrillas, parrilleros y carbón de 40 a 300 invitados + chimichurri 3 versiones + 5 salsas profesionales. Lo que separa al amateur del profesional.' },
      { icon: 'Tent', title: 'Guía 8 Sistemas + Food Truck', desc: 'Comparativa parrilla argentina, asador cruz, BBQ pit, caja china, barril llanero, modular inox, brasero, lift-grill. + Roadmap food truck especializado: inversión 30-75K EUR, regulación 8 CCAA.' },
    ],
  },

  testimonials: {
    subtitle:
      'Parrilleros, asadores castellanos, BBQ pitmasters y emprendedores latinos que usaron el plan para montar o escalar su servicio itinerante de parrilla',
    items: [
      { name: 'Mariano Rodríguez', role: 'Parrillero argentino, Madrid', text: 'Llevaba 12 años de empleado en parrilla y este plan me dio la hoja de ruta para independizarme. Las 10 experiencias y la calculadora de pricing son lo que más uso ahora.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Lucía Sanz', role: 'Parrillera profesional, Barcelona', text: 'El manual técnico de salmueras y la tabla de cocción de 18 cortes vale el plan entero. Mis bodas mejoraron en consistencia desde la primera temporada con esta guía.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Don Tomás García', role: 'Asador castellano, finca rural Toledo', text: 'Pensaba que ya lo sabía todo del cordero a la cruz, pero la sección de marco legal CCAA y el modelo de contrato profesional me organizaron todo el papeleo de la primera boda planner.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Diego López', role: 'BBQ pitmaster, Madrid corporate', text: 'El roadmap del food truck especializado en parrilla es brutal. Invertí 30.000 EUR siguiendo el blueprint y arranqué con eventos corporate en 6 meses.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Andrés Camacho', role: 'Asador llanero colombiano, Madrid', text: 'Aporta lo que ningún plan español ofrece: cubre el barril llanero y el asado tradicional latino. Diferencial total en bodas con familia LATAM.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Federico Aguirre', role: 'Asador uruguayo, Costa del Sol', text: 'La plantilla de 93 proveedores me ahorró meses de búsqueda. Con web y zona de cada uno, ya tenía por dónde empezar a llamar. Tienda Biomasa para el quebracho fue el hallazgo del año.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Marcos Pérez', role: 'Joven emprendedor parrillero, Valencia', text: 'En el segundo año ya facturo más de 100.000 EUR. El plan financiero realista es lo que me ancla cada decisión.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sandra Vera', role: 'Parrillera latina freelance, Bilbao', text: 'Los dos modelos de contrato (B2C + B2B) son oro puro. Antes redactaba cláusulas sueltas para cada cliente; ahora copio, edito y firmo en 10 minutos.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es un plan completo para montar tu servicio premium itinerante de parrilla, con el caso calculado en Excel y el marco del fuego al aire libre por comunidades.',
    reasons: [
      { icon: 'Flame', title: 'Anexo del Fuego en 8 Comunidades', desc: 'Anexo en el plan de negocio con la autorización que se pide, la época de peligro y la franja alrededor del monte en 8 comunidades. En terreno forestal o en esa franja la restricción se aplica aunque la finca tenga licencia; por eso los contratos llevan fuerza mayor con plan B.' },
      { icon: 'BarChart3', title: 'Modelo Híbrido B2C + B2B', desc: 'Particulares (bodas, cumpleaños, bautizos) y empresas (wedding planners, agencias, hoteles, show cooking). La calculadora tiene selector particular / empresa con los tramos de cancelación de cada canal, y hay modelos de contrato para cada uno.' },
      { icon: 'ShieldCheck', title: '93 Proveedores para Empezar', desc: 'Carniceros mayoristas (Hidalgo, Casa López, Tres Jotas), Tienda Biomasa (quebracho), GGM Gastro España, Brogas 1958, Texfire EPI, Hiscox/Mapfre. Con web y zona, y su estado en «Por verificar» para que lleves tu seguimiento.' },
      { icon: 'Banknote', title: 'Caso Calculado, sin Local Propio', desc: 'El caso de ejemplo necesita unos 77.000 € de inversión total, fondo de maniobra incluido, y alcanza el punto de equilibrio en torno a 80 eventos al año, trabajando desde una cocina de apoyo autorizada. Cambia los supuestos y el Excel recalcula tu caso. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a parrilleros argentinos, asadores castellanos, BBQ pitmasters y emprendedores latinos en el lanzamiento de servicios premium itinerantes de parrilla en España.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €89',
    items: [
      {
        icon: 'Flame',
        label: 'BONUS 1',
        title: 'Manual Técnico Parrillero',
        value: '€40',
        desc: '8 salmueras + 12 marinados + tabla de cocción para 18 cortes con Tº interna y merma + escalado de carne cruda, parrillas, parrilleros y carbón de 40 a 300 invitados + chimichurri en 3 versiones + 5 salsas profesionales. La pieza que separa al parrillero amateur del profesional.',
        image: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-3.jpg',
      },
      {
        icon: 'Tent',
        label: 'BONUS 2',
        title: 'Guía 8 Sistemas + Roadmap Food Truck',
        value: '€49',
        desc: 'Comparativa parrilla argentina, asador a la cruz, BBQ pit, caja china peruana, barril llanero, modular inox, brasero y lift-grill. + Roadmap food truck especializado en parrilla: inversión 30-75K EUR y regulación de venta ambulante en 8 CCAA.',
        image: '/lovable-uploads/ai-gallery/plan-parrillero-asador-eventos-5.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  guarantee: {
    text:
      'Si el plan de negocio para tu servicio premium de parrilla itinerante no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
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
      a: 'Para profesionales de la parrilla — argentinos, uruguayos, colombianos, asadores castellanos o emprendedores españoles con dominio del producto — que quieren montar un servicio premium itinerante de parrilla para eventos en España. Cubre tanto el cliente final particular (cumpleaños, bautizos, bodas en finca) como el cliente B2B (wedding planners, agencias de eventos, hoteles, empresas, restaurantes que contratan show cooking en directo).',
    },
    {
      q: '¿Sirve si nunca he montado mi propio negocio antes?',
      a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. El checklist de apertura reúne 83 tareas en 6 fases: SL o autónomo (con la cuota reducida de inicio de actividad, si te aplica), alta en el IAE, IVA al 10 %, cocina de apoyo autorizada, registro sanitario de tu comunidad autónoma, APPCC, gas, extintores y permisos de fuego, y seguro de responsabilidad civil. Cada tarea, con responsable, plazo y nota.',
    },
    {
      q: '¿Qué diferencia hay con un Plan de Negocio de Asador con local fijo?',
      a: 'Todo. Modelo itinerante sin local propio: la mise en place y el almacén van en una cocina de apoyo autorizada (compartida por horas u obrador) y cada evento lleva sus permisos. Ayudantes contratados como fijos discontinuos, nunca como autónomos que te facturan; ingresos concentrados en la temporada de bodas y fiestas; captación con wedding planners y empresas. El Excel modela todo eso: el caso de ejemplo necesita unos 77.000 € de inversión total, con el fondo de maniobra incluido.',
    },
    {
      q: '¿Cómo cubre el plan la regulación del fuego al aire libre por CCAA?',
      a: 'Con un anexo dedicado dentro del plan de negocio, una guía de partida para 8 comunidades (Madrid, Cataluña, Baleares, Andalucía, Valencia, País Vasco, Galicia y Castilla y León): su plan de incendios forestales, la época de peligro, la franja alrededor del terreno forestal y la autorización que se pide. Ojo: en terreno forestal o en esa franja la restricción se aplica aunque la finca tenga licencia, y en los niveles de alerta máximos pueden quedar sin efecto las autorizaciones. Por eso los contratos llevan cláusula de fuerza mayor y plan B de gas.',
    },
    {
      q: '¿Qué incluye la plantilla de 93 proveedores?',
      a: 'Cada proveedor lleva web, zona de cobertura y notas operativas, y una columna de estado que arranca en «Por verificar» para que lleves tu seguimiento. Carniceros mayoristas (Hidalgo, Casa López Mercamadrid, Tres Jotas Mercabarna), proveedores de carbón quebracho (Tienda Biomasa, Ricosan Carborec), GGM Gastro España, Brogas 1958, Texfire EPI y seguros Hiscox/Mapfre.',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El plan financiero Excel tiene 9 hojas: inversión inicial, cuenta de resultados a 3 años, punto de equilibrio en invitados por evento y en ingresos (el plan en Word lo traduce a eventos al año), escenarios pesimista y optimista, personal, tesorería de 12 meses con el IVA trimestral y financiación con recursos propios, préstamo con carencia, cuadro de amortización y DSCR. Sirve para presentarlo al banco, aunque la aprobación siempre depende de la entidad.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Lanzar tu ',
    headingGold: 'Servicio Premium de Parrilla',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a parrilleros, asadores y BBQ pitmasters que ya escalaron su servicio itinerante con un plan profesional adaptado al mercado español.',
    items: [
      'Plan de negocio en Word de 10 secciones + Plan financiero Excel de 9 hojas',
      'Calculadora de presupuestos por evento + Plantilla de 93 proveedores',
      'Catálogo equipamiento + utensilios + menaje (SKU GGM, Brogas, Texfire)',
      'Manual técnico parrillero + Carta 12 cortes + 10 experiencias temáticas',
      'Modelos contrato B2C + B2B + Guía 8 sistemas + roadmap food truck',
      'Checklist de apertura de 83 tareas + anexo del fuego al aire libre',
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

  stickyLabel: 'PLAN PARRILLERO EVENTOS — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-cocteleria-eventos', label: 'Plan Coctelería Eventos' },
    { href: '/kit-tareas-asador', label: 'Kit Tareas Asador' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.2 · octubre 2026',

  alreadyBought: {
    product: 'plan-negocio-parrillero-asador-eventos',
    label: '¿Ya compraste el Plan Parrillero / Asador Eventos? Vuelve a entrar al dashboard',
  },
};

export default data;
