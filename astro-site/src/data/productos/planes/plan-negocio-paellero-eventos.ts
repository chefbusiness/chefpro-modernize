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
//   · authorBadges se OMITE → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años']
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
      'Plan + kit profesional completo para montar tu servicio premium itinerante de paella y arroces para eventos en España 2026. Modelo híbrido para particulares, empresas y ayuntamientos. 11 entregables: plan de negocio en Word de 10 secciones con anexo del fuego al aire libre + plan financiero Excel de 9 hojas + calculadora de presupuestos por evento + checklist de apertura de 83 tareas + 88 proveedores DO Valencia + catálogo de equipamiento + manual técnico del fuego y el socarrat + carta de 12 paellas + contratos B2C/B2B + guía de 8 sistemas y roadmap de food truck arrocero. €45.',
    keywords:
      'plan de negocio paellero, paella eventos, arroz para eventos, mestre arrosser, paella valenciana premium, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-paellero-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio & Kit de Paellero / Paella para Eventos — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium itinerante de paella y arroces para eventos en España 2026. Modelo híbrido para particulares (bodas, comuniones, cumpleaños, peñas) y empresas (wedding planners, agencias, hoteles 4-5*, empresas team-building y ayuntamientos con fiestas populares). Incluye plan de negocio en Word de 10 secciones con anexo del fuego al aire libre en 8 comunidades, plan financiero Excel de 9 hojas (PyG 3 años, punto de equilibrio, escenarios, personal, tesorería 12 meses y financiación), calculadora de presupuestos por evento con IVA al 10 %, checklist de apertura de 83 tareas en 6 fases, plantilla de 88 proveedores DO Valencia + Calasparra, catálogo de equipamiento y menaje, manual técnico paellero (técnica del fuego + socarrat + 6 arroces + 4 caldos + 12 paellas), carta de 12 paellas, modelos de contrato B2C + B2B, 10 experiencias temáticas y guía de 8 sistemas con roadmap de food truck arrocero.',
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
        body: 'En el segundo año ya facturo más de 95.000 EUR. La plantilla de 88 proveedores DO Valencia me ahorró 3 meses de búsqueda.',
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
        a: 'Modelo itinerante sin local propio: trabajas desde una cocina de apoyo autorizada (compartida por horas u obrador) y pides los permisos de cada evento. Ayudantes contratados como fijos discontinuos, ingresos concentrados de mayo a octubre y captación con wedding planners, empresas y ayuntamientos. El Excel calcula tu caso: inversión, punto de equilibrio y tesorería mes a mes.',
      },
      {
        q: '¿Cómo cubre la regulación del fuego al aire libre por CCAA?',
        a: 'Con un anexo del plan de negocio para 8 comunidades: su plan de incendios forestales (INFOMA, INFOCAT, INFOBAL, INFOCA, PLADIGA, INFOCAL y los planes valenciano y vasco), la época de peligro, la franja alrededor del monte y la autorización que se pide. En terreno forestal o en esa franja la restricción se aplica aunque la finca tenga licencia, y los contratos llevan cláusula de fuerza mayor y plan B.',
      },
      {
        q: '¿Sirve para presentar al banco?',
        a: 'Sí. Plan financiero Excel de 9 hojas con PyG a 3 años, punto de equilibrio, escenarios pesimista y optimista, tesorería de 12 meses y financiación con préstamo, carencia, cuadro de amortización y DSCR. El plan de negocio en Word cuenta las mismas cifras. La aprobación siempre depende de la entidad.',
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
      'El kit profesional para montar tu empresa itinerante de paella y arroces para eventos en España. Modelo híbrido para particulares (bodas, comuniones, cumpleaños, peñas) y empresas (wedding planners, agencias, hoteles 4-5*, empresas team-building y ayuntamientos con fiestas populares), con 88 proveedores DO Valencia + Calasparra. Sin local propio: el modelo trabaja desde una cocina de apoyo autorizada, compartida por horas u obrador.',
    checkItems: [
      'Plan de negocio en Word: 10 secciones + anexo del fuego al aire libre en 8 CCAA (más de 7.000 palabras), con las mismas cifras que el Excel',
      'Plan financiero Excel de 9 hojas: eventos × raciones por evento × precio por ración, PyG 3 años, tesorería y financiación',
      'Calculadora de presupuestos: paelleras por diámetro, arroz, gas, kilómetros, IVA, anticipo del 30 % y margen calculado',
      'Checklist de apertura de 83 tareas en 6 fases: cocina de apoyo, gas, fuego, permisos y factura a ayuntamientos por FACe',
      'Plantilla de 88 proveedores (arroceros DO Valencia + Calasparra, mariscos Mediterráneo, Garcima, Pordamsa)',
      'Manual técnico paellero: escalado por paellera + técnica del fuego + socarrat + 6 tipos de arroz + 4 caldos + tabla de 12 paellas + alérgenos',
      'Catálogo de equipamiento + carta de 12 paellas + 10 experiencias temáticas + guía de 8 sistemas y roadmap de food truck',
      '2 modelos de contrato (particular + profesional) con fuerza mayor por alerta de incendios',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales, con la fiscalidad y los trámites de España, para montar tu servicio premium itinerante de paella y arroces para eventos.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 Secciones + Anexo)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, equipo, plan financiero, aspectos legales y plan de acción, más un anexo del fuego al aire libre en 8 comunidades: más de 7.000 palabras en A4, con las cifras del Excel. Caso de ejemplo: 105 eventos al año con una media de 94 raciones a 16 € por ración sin IVA, que salen de mezclar bodas, comidas de empresa, fiestas privadas y fiestas populares.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (9 Hojas)', desc: 'Supuestos, inversión inicial, PyG 3 años, punto de equilibrio (en raciones por evento y en ingresos; el plan en Word lo traduce a eventos al año), escenarios, personal, tesorería 12 meses, financiación con cuadro del préstamo y DSCR, e instrucciones. Ventas = eventos al año × raciones por evento × precio por ración sin IVA, con IVA del 10 %, cocina de apoyo autorizada, sueldo del dueño, amortización, ayudantes fijos discontinuos y la estacionalidad de bodas y fiestas.' },
      { icon: 'Calculator', title: 'Calculadora de Presupuestos por Evento', desc: 'De los invitados y el diámetro de paellera a las paelleras y los paelleros que necesitas, los kilos de arroz, los litros de caldo y el gas. Suma materia prima, menaje, personal con su Seguridad Social y alquileres, y da el precio por invitado sin IVA y con IVA (10 %), el desplazamiento a 0,95 €/km, el anticipo del 30 %, los importes por tramo de cancelación y el margen calculado. 3 presupuestos de ejemplo: boda, empresa y fiesta popular.' },
      { icon: 'Truck', title: 'Plantilla de 88 Proveedores', desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Calasparra), carniceros, mariscos Mediterráneo, verduras Levante (garrofó, ferraura), azafrán DO La Mancha, equipamiento Garcima/Vaello, vajilla Pordamsa. Con web, zona y una columna de estado que arranca en «Por verificar».' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento + Menaje', desc: 'Paelleras Garcima 60-90-120 cm + paellero Vaello 4 fuegos 50 kW + trípode leña + cuchillería Arcos + vajilla Pordamsa + EPI Texfire. SKU + URL + precio orientativo.' },
      { icon: 'ShieldCheck', title: 'Checklist de Apertura (83 Tareas)', desc: 'Seis fases: constitución y fiscalidad (IAE 677.9, Veri*factu, IVA al 10 %) · cocina de apoyo autorizada, registro sanitario autonómico, APPCC, gas y extintores, época de peligro de incendios, seguros y permisos · equipamiento y proveedores · personal y formación en higiene alimentaria · marca y captación, con los ayuntamientos por contrato menor y factura por FACe · primer evento y primeros 90 días.' },
      { icon: 'Utensils', title: 'Carta 12 Paellas y Arroces', desc: 'Valenciana DO + marisco premium + senyoret + arroz negro + mixta + arroz a banda + fideuá + meloso bogavante + caldoso bogavante + montaña + alicantina con costra + vegetal DO. Receta + food cost por ración + maridaje, con PVP orientativo por ración y precios de fiesta popular por volumen.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas editables y orientativas (revísalas con tu asesor): B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias, ayuntamientos) con anexo tarifario, briefing y SLA. IVA al 10 %, anticipo del 30 %, cancelación escalonada y fuerza mayor si una alerta de incendios prohíbe el fuego o el gas.' },
      { icon: 'Sparkles', title: '10 Experiencias Temáticas', desc: 'Boda en finca · corporate showcooking · fiesta del pueblo popular · bautizo familiar · cumpleaños senyoret · Falles + festes · boda exclusiva 5* · hotel show cooking · vegetal DO inclusive · brunch banda + fideuá.' },
      { icon: 'Flame', title: 'Manual Técnico Paellero', desc: 'Escalado por paellera (diámetro → raciones → arroz → caldo → quemador) y cómo cubrir 50, 100 o 200 invitados + técnica del fuego en 4 fases, con gas o leña + 6 tipos de arroz + 4 caldos + tabla de cocción de 12 paellas + cronograma del evento + seguridad alimentaria y alérgenos por paella + problemas y soluciones + checklist de material.' },
      { icon: 'Tent', title: 'Guía 8 Sistemas + Food Truck', desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico inducción, gas industrial, portátil camping, caja china peruana, paellero solar. + Roadmap food truck arrocería: inversión de 26.000 a 86.000 € según su tabla, regulación 8 CCAA.' },
    ],
  },

  testimonials: {
    subtitle:
      'Paelleros profesionales, mestres arrossers y wedding planners que usaron el plan para montar o impulsar su empresa premium de paella y arroces para eventos',
    items: [
      { name: 'Vicent Pellicer', role: 'Mestre arrosser valenciano, Sueca', text: 'Llevo 25 años haciendo paellas en fiestas del pueblo y siempre me faltó el plan de negocio para escalar a bodas premium. Este kit me dio todo: la calculadora pricing y el modelo contrato B2B me cerraron 4 wedding planners en 2 meses.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Carmen Soler', role: 'Paellera profesional, finca Toledo', text: 'El manual técnico del fuego y el socarrat es oro puro. La tabla de cocción de 12 paellas la imprimí y la tengo plastificada en la furgo. Mis bodas en finca mejoraron en consistencia desde la primera temporada.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Antonio Rivas', role: 'Paellero murciano, Mar Menor', text: 'Soy de Murcia y llevaba años haciendo paella de marisco en eventos privados sin marca. El plan de negocio y el dossier B2B me posicionaron premium en wedding planners de la zona Levante.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Marc Esteve', role: 'Joven emprendedor arrocero, Valencia', text: 'En el segundo año ya facturo más de 95.000 EUR. La plantilla de 88 proveedores DO Valencia me ahorró 3 meses de búsqueda.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Sara Romero', role: 'Paellera corporate, Madrid', text: 'Hago corporate showcooking para empresas en terrazas de Madrid y el catálogo de equipamiento con SKU exactos de Garcima me organizó la inversión inicial sin pasarme. La calculadora pricing B2B es la que más uso.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Don Joan Beltrán', role: 'Asador a la leña tradicional, Castellón', text: 'Soy de la vieja escuela del fuego de leña. Pensaba que no necesitaba un plan, pero el anexo legal CCAA + el modelo de contrato profesional me organizaron el papeleo de la primera boda planner que cerré.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Laura Martín', role: 'Paellera de bodas premium, Levante', text: 'Las 10 experiencias temáticas + la carta de 12 paellas me dieron un catálogo comercial de productos empaquetados. El ticket medio subió un 40 % desde que vendo "experiencias" en lugar de "menús".', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Diego Montes', role: 'Paellero alicantino fideuá, Alicante', text: 'Los dos modelos de contrato (B2C + B2B con anexos) son ya mi base de trabajo. Antes redactaba cláusulas sueltas para cada cliente; ahora copio, edito y firmo en 10 minutos.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo de España para montar tu empresa premium de paella y arroces para eventos: 11 entregables, un plan financiero de 9 hojas con la fiscalidad española, un checklist de apertura de 83 tareas, el anexo del fuego al aire libre por comunidad y un modelo híbrido para particulares, empresas y ayuntamientos.',
    reasons: [
      { icon: 'Flame', title: 'Único Plan España con Marco CCAA Fuego', desc: 'Anexo para 8 comunidades con su plan de incendios forestales (INFOMA, INFOCAT, INFOBAL, INFOCA, PLADIGA, INFOCAL y los planes valenciano y vasco), la época de peligro y la autorización que se pide. En terreno forestal o en su franja, la restricción se aplica aunque la finca tenga licencia; las paellas de Fallas y de las fiestas patronales en la calle dependen del bando de cada municipio. Vital para paelleros del Levante.' },
      { icon: 'BarChart3', title: 'Modelo Híbrido: Particulares, Empresas y Ayuntamientos', desc: 'Caso de ejemplo con 105 eventos al año: 15 bodas, 30 comidas de empresa, 50 fiestas privadas (cumpleaños, comuniones, peñas) y 10 fiestas populares de ayuntamiento. Calculadora con selector particular / empresa (tramos de cancelación de cada canal) y modelos de contrato para cada uno; los ayuntamientos, por contrato menor y factura electrónica por FACe.' },
      { icon: 'ShieldCheck', title: '88 Proveedores DO Valencia y Calasparra', desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Marjal, La Fallera) + Bomba Calasparra DO, mariscos Mediterráneo (Linamar, Castellet, Nardín DO Denia), verduras Levante DO, azafrán DO La Mancha, equipamiento Garcima/Vaello, vajilla Pordamsa/Steelite. Cada uno con web y zona, y su estado en «Por verificar» para que lleves tu seguimiento.' },
      { icon: 'Banknote', title: 'Caso Calculado, sin Local Propio', desc: 'El caso de ejemplo factura 157.920 € sin IVA el primer año: 105 eventos con una media de 94 raciones a 16 € por ración sin IVA, la media de 28 € en bodas, 24 € en empresas, 18 € en fiestas privadas y 5 € en fiestas populares de 400 raciones. Alcanza el punto de equilibrio en torno a 90 eventos al año. Unos 63.000 € de inversión total, fondo de maniobra incluido: furgoneta isoterma, paelleras, quemadores, equipo de gas y seguridad y lanzamiento, trabajando desde una cocina de apoyo autorizada. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a mestres arrossers valencianos, paelleros murcianos y alicantinos, y emprendedores arroceros en el lanzamiento de servicios premium itinerantes de paella y arroces para eventos en España.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €89',
    items: [
      {
        icon: 'Flame',
        label: 'BONUS 1',
        title: 'Manual Técnico Paellero',
        value: '€40',
        desc: 'El manual de cocina del evento: escalado por paellera y número de invitados, técnica del fuego en 4 fases con gas o leña, 6 tipos de arroz Bomba/J. Sendra/Albufera/Sénia, 4 caldos, tabla de cocción de 12 paellas, cronograma hora a hora, seguridad alimentaria, alérgenos por paella y tabla de problemas y soluciones. La pieza que separa al paellero amateur del profesional.',
        image: '/lovable-uploads/ai-gallery/plan-paellero-eventos-3.jpg',
      },
      {
        icon: 'Tent',
        label: 'BONUS 2',
        title: 'Guía 8 Sistemas + Roadmap Food Truck',
        value: '€49',
        desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico de inducción, gas industrial, portátil camping, caja china peruana y paellero solar. + Roadmap food truck especializado en paella y arroces: inversión de 26.000 a 86.000 € según su tabla y regulación de venta ambulante en 8 CCAA.',
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
      a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. El checklist de apertura reúne 83 tareas en 6 fases: SL o autónomo (con la cuota reducida de inicio de actividad, si te aplica), alta en el epígrafe 677.9 del IAE, facturación Veri*factu, IVA al 10 %, cocina de apoyo autorizada (para eventos no se puede preparar en casa, RD 1021/2022), registro sanitario de tu comunidad autónoma, APPCC, gas y extintores, época de peligro de incendios y seguro de responsabilidad civil con cobertura de intoxicación alimentaria. Cada tarea, con responsable, plazo y nota.',
    },
    {
      q: '¿Qué diferencia hay con un Plan de Negocio de Restaurante de Arroces con local fijo?',
      a: 'Todo. Modelo itinerante sin local propio: la mise en place, los caldos y el almacén de paelleras y bombonas van en una cocina de apoyo autorizada (compartida por horas u obrador), y cada evento lleva sus permisos (ayuntamiento o recinto y, en época de peligro, el uso del fuego). Ayudantes contratados como fijos discontinuos, nunca como autónomos que te facturan; ingresos concentrados de mayo a octubre; captación con wedding planners, empresas y ayuntamientos. El Excel modela todo eso: el caso de ejemplo necesita unos 63.000 € de inversión total, con el fondo de maniobra incluido, y alcanza el punto de equilibrio en torno a 90 eventos al año.',
    },
    {
      q: '¿Cómo cubre el plan la regulación del fuego al aire libre por CCAA?',
      a: 'Con un anexo dedicado dentro del plan de negocio, una guía de partida para 8 comunidades (Madrid, Cataluña, Baleares, Andalucía, Comunidad Valenciana, País Vasco, Galicia y Castilla y León): su plan de incendios forestales (INFOMA, INFOCAT, INFOBAL, INFOCA, el plan valenciano, el vasco, PLADIGA e INFOCAL), la época de peligro, la franja alrededor del terreno forestal y la autorización que se pide. Ojo: en terreno forestal o en esa franja, la restricción se aplica aunque la finca tenga licencia, y en los niveles de alerta máximos quedan sin efecto las autorizaciones (algunas alertas prohíben también el gas). Las paellas de Fallas y de las fiestas patronales en la calle se rigen por el bando de cada municipio. Por eso los contratos llevan una cláusula de fuerza mayor y el checklist, un plan B. Confirma siempre con el ayuntamiento y con la comunidad antes de cada evento.',
    },
    {
      q: '¿Qué incluye la plantilla de 88 proveedores?',
      a: 'Cada proveedor lleva web, zona de cobertura y notas operativas, y una columna de estado que arranca en «Por verificar» para que lleves tu seguimiento. Arroceros DO Valencia (Tartana, J. Sendra, Marjal, La Fallera) + arroz Bomba Calasparra DO + carniceros mayoristas (Hidalgo, Casa López Mercamadrid, Tres Jotas Mercabarna), mariscos del Mediterráneo (Pescaderías Coruñesas, Mariscos Linamar, Mariscos Castellet, Mariscos Nardín gamba roja DO Denia), verduras DO Levante (garrofó, ferraura, alcachofa), azafrán DO La Mancha y pimentón DO Vera, equipamiento Garcima/Vaello/GGM, vajilla Pordamsa/Steelite. Confirma disponibilidad y condiciones con cada uno antes de pedir.',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El plan financiero Excel tiene 9 hojas: inversión inicial, PyG previsional a 3 años, punto de equilibrio en raciones por evento y en ingresos (el plan en Word lo traduce a eventos al año), escenarios pesimista y optimista, personal, tesorería de 12 meses con el IVA trimestral y financiación con recursos propios, préstamo con carencia, cuadro de amortización y DSCR. El plan de negocio en Word cuenta las mismas cifras. Sirve para presentarlo al banco, aunque la aprobación siempre depende de la entidad.',
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
      'Plan de negocio en Word (10 secciones + anexo del fuego) + Plan financiero Excel de 9 hojas',
      'Calculadora de presupuestos por evento + Plantilla de 88 proveedores DO Valencia',
      'Catálogo equipamiento + utensilios + menaje (SKU Garcima, Vaello, Pordamsa, Texfire)',
      'Manual técnico paellero + Carta 12 paellas + 10 experiencias temáticas',
      'Modelos contrato B2C + B2B + Guía 8 sistemas + roadmap food truck arrocería',
      'Checklist de apertura: 83 tareas en 6 fases, con los trámites españoles',
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
  updateNote: 'Producto actualizado · Versión 2.2 · octubre 2026',

  alreadyBought: {
    product: 'plan-negocio-paellero-eventos',
    label: '¿Ya compraste el Plan Paellero / Paella Eventos? Vuelve a entrar al dashboard',
  },
};

export default data;
