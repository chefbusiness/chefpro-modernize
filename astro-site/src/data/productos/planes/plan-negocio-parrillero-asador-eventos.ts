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
      'Plan + kit profesional completo para montar tu servicio premium itinerante de parrilla y asado para eventos en España 2026. Modelo híbrido B2C + B2B. 11 entregables: DOCX 60+ pp + Plan Financiero Excel + 96 proveedores + Catálogo equipamiento + Manual técnico + Carta 12 cortes + Modelos contrato B2C/B2B + Guía 8 sistemas + roadmap food truck. Inversión desde 3.500 EUR. €45.',
    keywords:
      'plan de negocio parrillero, parrilla eventos, asador a la cruz, BBQ pitmaster España, parrilla itinerante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-parrillero-asador-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio & Kit de Parrillero / Asador para Eventos — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium itinerante de parrilla y asado para eventos en España 2026. Modelo híbrido B2C particular (bodas, cumpleaños, bautizos) + B2B (wedding planners, agencias, hoteles, empresas, restaurantes show cooking). Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 96 proveedores reales, catálogo equipamiento + menaje, manual técnico parrillero (8 salmueras + 12 marinados + 18 cortes), carta de 12 cortes, modelos de contrato B2C+B2B, 10 experiencias temáticas, guía de 8 sistemas + roadmap food truck y checklist de apertura con anexo CCAA fuego al aire libre.',
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
        a: 'Para profesionales de la parrilla — argentinos, uruguayos, colombianos, asadores castellanos o emprendedores españoles — que quieren montar un servicio premium itinerante para eventos en España. Cubre cliente final particular (bodas íntimas, cumpleaños, bautizos) y B2B (wedding planners, agencias, hoteles, restaurantes show cooking).',
      },
      {
        q: '¿Qué diferencia hay con un Plan de Asador con local fijo?',
        a: 'Modelo itinerante sin local: sin licencia clasificada (autorizaciones puntuales por evento), sin plantilla fija (ayudantes freelance), inversión 4-7x menor (3.500 EUR mínimo viable vs 70-130K), ingresos por evento concentrados mayo-septiembre + diciembre, captación B2B intensiva con wedding planners.',
      },
      {
        q: '¿Cómo cubre la regulación del fuego al aire libre por CCAA?',
        a: 'Anexo dedicado con autorización exigida y restricciones (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL) en 8 comunidades + excepciones para finca privada. El dolor real que ningún competidor ayuda a resolver.',
      },
      {
        q: '¿Sirve para presentar al banco?',
        a: 'Sí. Plan Financiero Excel con P&L 3 años, break-even 8-10 eventos año 1, 3 escenarios, mix B2C+B2B y plan de cashflow estacional. Formato ICO/microcrédito.',
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
    badge: 'El plan más completo de España para montar tu servicio premium de parrilla itinerante',
    titlePre: 'Plan de Negocio & Kit de ',
    titleGold: 'Parrillero / Asador',
    titleSubtitle: 'para Eventos — 11 Entregables Profesionales',
    description:
      'El kit profesional para montar tu servicio premium itinerante de parrilla y asado para eventos en España. Modelo híbrido B2C particular (bodas, cumpleaños, bautizos) + B2B (wedding planners, agencias, hoteles, empresas, restaurantes show cooking). Inversión desde 3.500 EUR.',
    checkItems: [
      'Plan de negocio DOCX completo (60+ pp.) con marco legal CCAA fuego al aire libre',
      'Plan Financiero Excel con mix B2C 40 % + B2B 60 % y estacionalidad mayo-septiembre',
      'Plantilla 96 proveedores reales (carniceros mayoristas, GGM, Tienda Biomasa, Texfire)',
      'Catálogo equipamiento + utensilios + menaje con SKU + URL + precio actualizado',
      'Manual técnico parrillero: 8 salmueras + 12 marinados + tabla cocción 18 cortes',
      '10 experiencias temáticas + Guía 8 sistemas de parrilla + roadmap food truck',
      '2 modelos de contrato (B2C particular + B2B profesional con anexo tarifario)',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales con datos reales del mercado de eventos español 2026 para validar la viabilidad de tu servicio premium itinerante de parrilla y asado.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026, 10 competidores reales, doble embudo B2C+B2B, marco legal CCAA fuego, financiero 3 años, riesgos, roadmap 3 años.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 40 % + B2B 60 %, inversión 3.500-25.000 EUR según escenario, estacionalidad mayo-septiembre 70 %, break-even 8-10 eventos año 1.' },
      { icon: 'Calculator', title: 'Calculadora Pricing Eventos', desc: 'Excel con fórmulas duales B2C particular + B2B planner. Inputs: pax, distancia, concepto, ayudantes ⇒ precio sugerido + margen. Con 10 ejemplos validados.' },
      { icon: 'Truck', title: 'Plantilla 96 Proveedores Reales', desc: 'Carniceros mayoristas (Hidalgo, Casa López, Tres Jotas), GGM Gastro (parrillas), Tienda Biomasa (carbón quebracho), Texfire (EPI), Hosply.pro y más.' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento + Menaje', desc: 'Parrilla GGM KGE1200 709 EUR + Brogas asador cruz + Comander COMPER-M ahumador + cuchillería Arcos + vajilla eventos + EPI Texfire. SKU + URL + precio.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC) · seguros RC eventos · equipamiento + carniceros · marca y web · captación B2C+B2B · operativa primer evento.' },
      { icon: 'Beef', title: 'Carta 12 Cortes de Carne', desc: 'Argentinos (asado tira, bife chorizo, vacío) + castellanos (cordero a la cruz, cochinillo) + ibéricos (pluma, secreto) + BBQ texano (brisket, ribs). Técnica + Tº + merma + maridaje.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas legales editables: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias) con anexo tarifario y SLA.' },
      { icon: 'Sparkles', title: '10 Experiencias Temáticas', desc: 'Asado argentino, asador a la cruz, parrilla uruguaya, BBQ texano, rodizio brasileño, asador criollo, mediterránea, llanera, show de fuego y brunch parrillero corporate.' },
      { icon: 'Flame', title: 'Manual Técnico Parrillero', desc: '8 salmueras + 12 marinados + tabla cocción 18 cortes con Tº interna y merma + chimichurri 3 versiones + 5 salsas profesionales. Lo que separa al amateur del profesional.' },
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
      { name: 'Federico Aguirre', role: 'Asador uruguayo, Costa del Sol', text: 'La plantilla de 96 proveedores me ahorró meses de búsqueda. Validados, con teléfonos y notas reales. Tienda Biomasa para el quebracho fue el hallazgo del año.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Marcos Pérez', role: 'Joven emprendedor parrillero, Valencia', text: 'Empecé con 3.800 EUR siguiendo el escenario mínimo viable. En el segundo año ya facturo más de 100.000 EUR. El plan financiero realista es lo que me ancla cada decisión.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Sandra Vera', role: 'Parrillera latina freelance, Bilbao', text: 'Los dos modelos de contrato (B2C + B2B) son oro puro. Antes redactaba cláusulas sueltas para cada cliente; ahora copio, edito y firmo en 10 minutos.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo de España para montar tu servicio premium itinerante de parrilla con datos reales del mercado eventos 2026 y marco legal CCAA del fuego al aire libre.',
    reasons: [
      { icon: 'Flame', title: 'Único Plan España con Marco CCAA Fuego', desc: 'Anexo dedicado con autorización exigida, restricciones por temporada (INFOCA, PATRICOVA, PLADIGA, INFOCYL) y excepciones para finca privada en 8 CCAA. Es el dolor real que ningún competidor ayuda a resolver.' },
      { icon: 'BarChart3', title: 'Modelo Híbrido B2C + B2B Validado', desc: 'Mix B2C 40 % (bodas íntimas, cumpleaños, bautizos) + B2B 60 % (wedding planners, agencias, hoteles, restaurantes show cooking). Calculadora pricing dual y modelos de contrato para cada canal.' },
      { icon: 'ShieldCheck', title: '96 Proveedores Reales Validados', desc: 'Carniceros mayoristas (Hidalgo, Casa López, Tres Jotas, El Capricho León), Tienda Biomasa (quebracho), GGM Gastro España, Brogas 1958, Texfire EPI, Hiscox/Mapfre. Web, contacto, cobertura y notas verificadas.' },
      { icon: 'Banknote', title: 'Inversión Mínima 3.500 EUR', desc: '4-7x menor que un asador con local fijo (70-130K EUR). Escenario mínimo viable o full equipment hasta 25K EUR. Break-even en 8-10 eventos año 1. Pago único, sin suscripciones.' },
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
        desc: '8 salmueras + 12 marinados + tabla de cocción para 18 cortes con Tº interna y merma + chimichurri en 3 versiones + 5 salsas profesionales. La pieza que separa al parrillero amateur del profesional.',
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
      a: 'Para profesionales de la parrilla — argentinos, uruguayos, colombianos, asadores castellanos o emprendedores españoles con dominio del producto — que quieren montar un servicio premium itinerante de parrilla para eventos en España. Cubre tanto el cliente final particular (cumpleaños, bautizos, bodas íntimas en finca) como el cliente B2B (wedding planners, agencias de eventos, hoteles, empresas, restaurantes que contratan show cooking en directo).',
    },
    {
      q: '¿Sirve si nunca he montado mi propio negocio antes?',
      a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. Incluye la constitución como autónomo (tarifa plana 80 EUR/mes el primer año), alta IAE 677.9, plan APPCC adaptado a actividad itinerante y seguro RC profesional eventos. El checklist de 6 fases con 80-120 ítems no deja nada al azar.',
    },
    {
      q: '¿Qué diferencia hay con un Plan de Negocio de Asador con local fijo?',
      a: 'Todo. Modelo itinerante sin local: sin licencia de actividad clasificada (autorizaciones puntuales por evento), sin plantilla fija (ayudantes freelance bajo demanda), inversión 4-7 veces menor (3.500-5.000 EUR mínimo viable vs 70-130K EUR de un asador fijo), ingresos por evento concentrados mayo-septiembre + diciembre (65-75 % facturación), captación B2B intensiva con wedding planners. El plan modela todos estos pilares.',
    },
    {
      q: '¿Cómo cubre el plan la regulación del fuego al aire libre por CCAA?',
      a: 'Con un anexo dedicado dentro del Plan de Negocio. Resumen operativo de 8 comunidades (Madrid, Cataluña, Baleares, Andalucía, Valencia, País Vasco, Galicia, Castilla y León) con tipo de autorización exigida, restricciones por temporada (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL) y excepciones para eventos en finca privada con licencia. Es el dolor real que ningún competidor ayuda a resolver.',
    },
    {
      q: '¿La plantilla de 96 proveedores incluye contactos verificables?',
      a: 'Sí. Cada proveedor lleva web, zona de cobertura, notas operativas, score y estado (validado / investigar). Carniceros mayoristas (Hidalgo, Casa López Mercamadrid, Tres Jotas Mercabarna, El Capricho León), proveedores de carbón quebracho (Tienda Biomasa, Ricosan Carborec), GGM Gastro España, Brogas 1958, Texfire EPI y seguros Hiscox/Mapfre.',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (8-10 eventos break-even año 1), 3 escenarios de inversión, mix B2C+B2B desglosado y plan de cashflow con estacionalidad. Es el formato estándar que piden bancos para microcrédito o ICO emprendedores.',
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
      'Plan de Negocio DOCX 60+ pp. + Plan Financiero Excel 6 hojas',
      'Calculadora Pricing eventos B2C + B2B + Plantilla 96 proveedores',
      'Catálogo equipamiento + utensilios + menaje (SKU GGM, Brogas, Texfire)',
      'Manual técnico parrillero + Carta 12 cortes + 10 experiencias temáticas',
      'Modelos contrato B2C + B2B + Guía 8 sistemas + roadmap food truck',
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

  stickyLabel: 'PLAN PARRILLERO EVENTOS — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-cocteleria-eventos', label: 'Plan Coctelería Eventos' },
    { href: '/kit-tareas-asador', label: 'Kit Tareas Asador' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'plan-negocio-parrillero-asador-eventos',
    label: '¿Ya compraste el Plan Parrillero / Asador Eventos? Vuelve a entrar al dashboard',
  },
};

export default data;
