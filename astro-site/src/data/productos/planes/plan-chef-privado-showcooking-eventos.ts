// astro-site/src/data/productos/planes/plan-chef-privado-showcooking-eventos.ts
// LÍNEA PLANES (sub-línea B "planes de eventos") — mismo template único que bar-restaurante (A) y
// cocteleria-eventos (B): esqueleto DOM IDÉNTICO, solo cambia el copy. Copy VERBATIM de la SPA:
//   · src/pages/PlanChefPrivadoShowcookingEventos.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-chef-privado-showcooking-eventos/*  (los 10 componentes)
//   · src/data/testimonials-plan-chef-privado-showcooking-eventos.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (constante de línea, hardcodeada en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_CHEF_PRIVADO_SHOWCOOKING (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Lanzar tu ' (patrón de la sub-línea B).
//   · hero.checkItems tiene 8 elementos (bar-restaurante tenía 5) — longitud variable, sin impacto estructural.
//   · images.gridGallery DIFIERE de images.gallery: hero usa [hero,1,2,3,4,5], grid usa [1,2,3,4,5,6]
//     (mismo patrón que cocteleria-eventos — el set del ContentGrid excluye el hero e incluye el -6).
//   · authorBadges se OMITE → default ['Consultor Gastronómico', '+29 años en alta hostelería'] (= el de este producto, verbatim).
//   · DIVERGENCIA NUEVA (reportada): WhySection.reasons usa el icono lucide `Home`, que NO existía en
//     Icon.astro (solo estaban Coins/Banknote de la referencia anterior). Añadido aquí mismo: NODES.Home +
//     KEBAB.Home = 'house' (en lucide-react v0.462.0 el componente `Home` es un alias directo de `House` —
//     mismo iconNode y mismo nombre de clase lucide-house — verificado en node_modules/lucide-react/dist/esm/icons/home.js).
//
// QUIRKS VERBATIM:
//   · seo.title / hero.titlePre llevan un '&' literal (la SPA lo escribe '&amp;' en JSX Helmet y '&' en
//     JSON.stringify de los schemas; aquí se escribe '&' y BaseLayout/el template lo escapan igual en HTML).
//   · schema.faqs (FAQPage JSON-LD) = 5 preguntas (subconjunto corto); faqs on-page (acordeón) = 7, más largas.
//   · Todas las imágenes del producto son .jpg (no .jpeg como en cocteleria-eventos).
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-chef-privado-showcooking-eventos',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_CHEF_PRIVADO_SHOWCOOKING',

  seo: {
    title:
      'Plan de Negocio & Kit Chef Privado / Showcooking a Domicilio — 11 Entregables | AI Chef Pro',
    description:
      'Plan + kit profesional completo para montar tu servicio premium de chef privado y showcooking a domicilio en España 2026. Modelo dual B2C íntimo + B2B corporate. 11 entregables: DOCX 60+ pp + Plan Financiero Excel + 96 proveedores premium + Catálogo cuchillería japonesa + Manual técnico APPCC móvil + Carta 12 menús + Modelos contrato B2C/B2B + Guía sistemas Chef Privado vs Personal Chef vs Caterer. Inversión desde 4.500 EUR. €45.',
    keywords:
      'plan de negocio chef privado, showcooking a domicilio, personal chef España, cena privada premium, chef boda boutique, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-chef-privado-showcooking-eventos.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio & Kit de Chef Privado / Showcooking a Domicilio — 11 Entregables',
    productDescription:
      'Plan + kit profesional completo para montar un servicio premium de chef privado y showcooking a domicilio en España 2026. Modelo dual B2C íntimo (cenas en pareja, cumpleaños, aniversarios, brunch privado) + B2B corporate (showcooking empresa, hoteles boutique, wedding planners, cooking class team-building, cena directiva fin de año). Incluye DOCX 60+ pp, Plan Financiero Excel con mix B2C+B2B, Calculadora Pricing dual, plantilla de 96 proveedores premium (cuchillería japonesa, vajilla Pordamsa, AOVE DO, caviar Riofrío), catálogo equipamiento + cuchillería, manual técnico servicio domicilio APPCC móvil con 7 PCC, carta de 12 menús temáticos, modelos de contrato B2C+B2B con confidencialidad y MSA, 10 experiencias temáticas, guía sistemas Chef Privado vs Personal Chef vs Caterer y checklist de apertura con anexo regulación CCAA catering itinerante.',
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
        author: 'David Ramírez',
        rating: '5',
        body: 'Llevaba 3 años haciendo cenas en domicilios con boca-oreja. El plan me dio la marca personal, el portfolio profesional y el dossier B2B. En 4 meses cerré 6 acuerdos con hoteles boutique de Madrid.',
      },
      {
        author: 'Marta Soriano',
        rating: '5',
        body: 'La calculadora pricing dual B2C + B2B me ahorró 6 meses de prueba y error. Antes tiraba precios al aire, ahora cierro presupuestos en 10 minutos con margen real del 60 %.',
      },
      {
        author: 'Carlos Mendieta',
        rating: '5',
        body: 'Las 10 experiencias temáticas se convirtieron en mi catálogo comercial B2B. Subí el ticket medio de showcooking corporate de 1.250 € a 1.850 € en 8 meses sin perder clientes.',
      },
    ],
    // FAQPage schema (5 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 7, más largas)
    faqs: [
      {
        q: '¿Para quién está pensado este plan?',
        a: 'Para chefs profesionales que quieren montar un servicio premium de chef privado y showcooking a domicilio en España. Cubre cliente final particular (cumpleaños, aniversarios, San Valentín, brunch privado) y B2B (showcooking corporate, hoteles boutique 4-5*, wedding planners, agencias con cooking class team-building y cenas directiva fin de año).',
      },
      {
        q: '¿Qué diferencia hay con un Personal Chef o un Caterer?',
        a: 'Mucha. Chef Privado (modelo por evento, ticket 580-2.200 EUR, marca personal, multi-cliente), Personal Chef (recurrente con 1-3 clientes high-net-worth, 1.800-4.500 EUR/mes), Caterer (escalable con cocina central y plantilla, 8.000-150.000 EUR por evento). El plan recomienda empezar siempre por chef privado y pivotar después si encaja con tu vida y negocio.',
      },
      {
        q: '¿Cómo cubre la regulación de catering itinerante por CCAA?',
        a: 'Anexo dedicado con resumen operativo de 17 CCAA: tipo de Registro Sanitario + RGSEAA, requisitos cocina del cliente, normativa transporte alimentos, etiquetado bilingüe Cataluña/País Vasco, trámites telemáticos vs presenciales y plazos por CCAA.',
      },
      {
        q: '¿Sirve para presentar al banco?',
        a: 'Sí. Plan Financiero Excel con P&L 3 años, break-even 9-12 eventos/mes año 1, 3 escenarios de inversión (4.500 / 11.500 / 30.000 EUR), mix B2C+B2B desglosado y plan de cashflow con picos diciembre y verano. Formato ICO/microcrédito.',
      },
      {
        q: '¿Cómo funciona la garantía?',
        a: '30 días de devolución completa sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio Chef Privado / Showcooking',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-1.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-2.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-3.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-4.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-5.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (empieza en -1, termina en -6, sin -hero)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-1.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-2.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-3.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-4.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-5.jpg',
      '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-6.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-4.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-hero.jpg',
  },

  hero: {
    badge: 'El plan más completo de España para montar tu servicio premium de chef privado y showcooking a domicilio',
    titlePre: 'Plan de Negocio & Kit de ',
    titleGold: 'Chef Privado / Showcooking',
    titleSubtitle: 'a Domicilio — 11 Entregables Profesionales',
    description:
      'El kit profesional para montar tu empresa de chef privado y showcooking a domicilio en España. Modelo dual B2C íntimo (cenas en pareja, cumpleaños, aniversarios, brunch privado) + B2B corporate (showcooking empresa, hoteles boutique, wedding planners, cooking class team-building), con 96 proveedores premium validados. Inversión 5-9x menor que un restaurante con local fijo.',
    checkItems: [
      'Plan de negocio DOCX completo (60+ pp.) con anexo regulación CCAA catering itinerante',
      'Plan Financiero Excel: P&L 3 años con mix B2C 40 % + B2B 60 % sin estacionalidad fuerte',
      'Plantilla 96 proveedores reales (cuchillería japonesa, vajilla premium, AOVE DO, microbrotes)',
      'Catálogo equipamiento + cuchillería + vajilla con marcas y modelos validados',
      'Manual técnico servicio domicilio: 7 PCC APPCC móvil + cronograma + estaciones de trabajo',
      '10 experiencias temáticas + Guía sistemas Chef Privado vs Personal Chef vs Caterer',
      '2 modelos de contrato (B2C particular + B2B corporate con confidencialidad y MSA)',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €45',
  },

  grid: {
    subtitle:
      '11 entregables profesionales con datos reales del mercado español 2026 para validar la viabilidad de tu servicio premium de chef privado y showcooking a domicilio.',
    templates: [
      { icon: 'FileText', title: 'Plan de Negocio DOCX (60+ pp.)', desc: 'Análisis mercado España 2026, segmentación dual B2C íntimo + B2B corporate, modelo sin local fijo, anexo regulación CCAA catering itinerante, financiero 3 años, riesgos, roadmap.' },
      { icon: 'Coins', title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L 3 años con mix B2C 40 % + B2B 60 %, inversión 4.500-30.000 EUR según escenario, sin estacionalidad fuerte (picos diciembre + verano), break-even por número de eventos.' },
      { icon: 'Calculator', title: 'Calculadora Pricing B2C + B2B', desc: 'Excel con fórmulas duales B2C cena íntima + B2B corporate showcooking. Inputs: pax, distancia, tipo experiencia, nivel menú (estándar/premium/exclusivo), pairing, branded ⇒ precio sugerido + margen. 10 ejemplos validados.' },
      { icon: 'Truck', title: 'Plantilla 96 Proveedores Reales', desc: 'Cuchillería japonesa (Tojiro, Yoshihiro, Kai Shun) + sous-vide Anova/Polyscience + vajilla Pordamsa/Steelite/Schönwald + carniceros premium (Cesáreo Gómez, Discarlux) + AOVE DO Castillo de Canena + microbrotes + caviar Riofrío + trufa Soria.' },
      { icon: 'Wrench', title: 'Catálogo Equipamiento + Cuchillería', desc: 'Cuchillería japonesa (gyuto, petty, sujihiki) + inducción portátil Vollrath/Iwatani + sous-vide + vajilla blanca premium + cristalería + uniformidad chef + furgoneta. Marcas, modelos y precios validados.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución (autónomo + IAE 677.9 + APPCC móvil + RGSEAA) · seguros RC eventos con cláusula intoxicación · cuchillería + vajilla + proveedores premium · marca y portfolio · captación B2C+B2B · operativa primer evento. 108 hitos.' },
      { icon: 'Utensils', title: 'Carta 12 Menús Temáticos', desc: 'Tasting menu degustación 7 pasos + brunch dominical premium + cena maridajes + mediterránea tradicional + asiático fusión showcooking + mexicano premium + ruta tapas privada + caprice del chef + vegetariano + healthy + mariscada premium + Navidad privada.' },
      { icon: 'ScrollText', title: 'Modelos Contrato B2C + B2B', desc: 'Plantillas legales editables: B2C particular (cumpleaños, aniversarios, San Valentín, Navidad) + B2B corporate (cena directiva, showcooking, hotel, wedding planner) con confidencialidad, MSA y propiedad intelectual del menú.' },
      { icon: 'Sparkles', title: '10 Experiencias Temáticas', desc: 'Cena romántica San Valentín · cumpleaños familiar · aniversario boda · brunch dominical · cena ejecutiva pairing · showcooking corporate 30-80 pax · cooking class team-building · hotel boutique in-suite · cena ensayo pre-boda · cena directiva fin año.' },
      { icon: 'Flame', title: 'Manual Técnico Servicio Domicilio', desc: '7 PCC APPCC móvil (recepción, cadena frío, manipulación, cocción, servicio, alérgenos, limpieza) + cronograma evento 8 pax + estaciones de trabajo en cocina del cliente + coordinación servicio en mesa + documentación obligatoria.' },
      { icon: 'BookOpen', title: 'Guía Sistemas: Chef vs Personal vs Caterer', desc: 'Definición y modelo de cada figura · ticket medio · ICP · margen neto · inversión inicial · cuándo elegir cada figura · modelos híbridos válidos · riesgo de confundir las figuras al posicionarse comercialmente.' },
    ],
  },

  testimonials: {
    subtitle:
      'Chefs privados, showcookers corporate, personal chefs y wedding planners que usaron el plan para montar o impulsar su empresa premium de chef privado a domicilio',
    items: [
      { name: 'David Ramírez', role: 'Chef privado premium, Madrid', text: 'Llevaba 3 años haciendo cenas en domicilios con boca-oreja. El plan me dio la marca personal, el portfolio profesional y el dossier B2B. En 4 meses cerré 6 acuerdos con hoteles boutique de Madrid.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Marta Soriano', role: 'Chef privada para cenas íntimas, Salamanca', text: 'La calculadora pricing dual B2C + B2B me ahorró 6 meses de prueba y error. Antes tiraba precios al aire, ahora cierro presupuestos en 10 minutos con margen real del 60 %.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Mendieta', role: 'Showcooking corporate, Madrid + BCN', text: 'Las 10 experiencias temáticas se convirtieron en mi catálogo comercial B2B. Subí el ticket medio de showcooking corporate de 1.250 € a 1.850 € en 8 meses sin perder clientes.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucía Fernández', role: 'Showcooking premium para bodas, Toledo', text: 'El catálogo de cuchillería japonesa con marcas y precios validados me organizó la inversión inicial. Empecé con cuchillería Tojiro entry-level y subí a Misono y Yoshihiro tras los primeros 6 meses.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Roberto Castillo', role: 'Personal chef high-net-worth, Madrid', text: 'Hago personal chef para 2 familias y eventos puntuales B2B. La guía de sistemas Chef Privado vs Personal Chef vs Caterer me clarificó cómo posicionarme con cada cliente. Vital para no confundir mensajes en LinkedIn y web.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Pablo Iturralde', role: 'Chef hotel boutique 5*, Madrid', text: 'El manual técnico APPCC móvil con los 7 PCC me organizó el protocolo de in-suite room service que vendo al hotel. La cláusula de intoxicación en seguro RC me la puso a primera lectura, antes ni la conocía.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Cristina Vega', role: 'Cooking class team-building, Madrid', text: 'Las experiencias temáticas + el contrato B2B con confidencialidad y MSA cambiaron mi negocio. Empresas que antes me contrataban un evento al año ahora firman acuerdo marco anual de 5-6 sesiones.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Andrés Rivas', role: 'Chef privado experiencias premium, Madrid', text: 'La carta de 12 menús temáticos es lo que ofrezco al cliente para elegir. La sorpresa del chef se ha convertido en mi opción más vendida porque genera fidelidad y referidos. Subí ticket un 30 %.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el único plan completo de España para montar tu empresa premium de chef privado y showcooking a domicilio: 11 entregables reales con datos del mercado 2026, anexo regulación CCAA catering itinerante y modelo dual B2C íntimo + B2B corporate.',
    reasons: [
      { icon: 'Home', title: 'Único Plan España con Anexo CCAA Catering Itinerante', desc: 'Anexo dedicado con resumen operativo de 17 comunidades autónomas: tipo de Registro Sanitario CCAA + RGSEAA, requisitos sobre la cocina del cliente, normativa de transporte de alimentos, etiquetado bilingüe (Cataluña, País Vasco) y plazos de trámites por CCAA.' },
      { icon: 'BarChart3', title: 'Modelo Dual B2C Íntimo + B2B Corporate', desc: 'Mix B2C 40 % (cenas en pareja, cumpleaños, aniversarios, brunch privado) + B2B 60 % (showcooking corporate, hoteles boutique 4-5*, wedding planners, cooking class team-building, cena directiva fin de año). Calculadora pricing dual y modelos de contrato para cada canal.' },
      { icon: 'ShieldCheck', title: '96 Proveedores Premium Validados', desc: 'Cuchillería japonesa (Tojiro, Yoshihiro, Kai Shun, Misono, Sakai Takayuki) + sous-vide Anova/Polyscience/Sammic + vajilla Pordamsa/Steelite/Schönwald + carniceros premium Cesáreo Gómez/Discarlux/El Capricho León + caviar Riofrío + trufa Soria + AOVE DO Castillo de Canena.' },
      { icon: 'Banknote', title: 'Inversión Mínima 4.500 EUR', desc: '5-9x menor que un restaurante con local fijo (70-130K EUR). Escenario mínimo viable, recomendado 11.500 EUR o premium hasta 30.000 EUR. Break-even 9-12 eventos/mes año 1. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. Más de 29 años de carrera profesional en alta hostelería y restauración, y 15 años en consultoría gastronómica. Ha asesorado a chefs privados, personal chefs y showcookers corporate en el lanzamiento de servicios premium a domicilio en España, incluyendo cenas íntimas, eventos corporate, hoteles boutique y wedding planners.',
  // authorBadges omitido → default ['Consultor Gastronómico', '+29 años en alta hostelería'] (= el de este producto, verbatim)

  bonus: {
    subtitle:
      'Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €89',
    items: [
      {
        icon: 'Flame',
        label: 'BONUS 1',
        title: 'Manual Técnico Servicio Domicilio + APPCC Móvil',
        value: '€40',
        desc: '7 PCC (Puntos de Control Crítico) APPCC adaptado a servicio itinerante: recepción, cadena de frío, manipulación, cocción, servicio en mesa, gestión de alérgenos, limpieza. + Cronograma operativo evento 8 pax minuto a minuto + organización de estaciones de trabajo en cocina del cliente + documentación obligatoria. La pieza que te separa del cocinero amateur.',
        image: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-3.jpg',
      },
      {
        icon: 'BookOpen',
        label: 'BONUS 2',
        title: 'Guía Chef Privado vs Personal Chef vs Caterer',
        value: '€49',
        desc: 'Comparativa estratégica de las 3 figuras del segmento: definición y modelo de cada una, ticket medio, ICP, margen neto, inversión inicial, plantilla. + Cuándo elegir cada figura, modelos híbridos válidos y riesgo de confundirlas al posicionarte. Empieza siempre por chef privado y pivota cuando proceda — la guía te dice exactamente cuándo.',
        image: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-5.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €45',
  },

  guarantee: {
    text:
      'Si el plan de negocio para tu servicio premium de chef privado y showcooking a domicilio no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (7 preguntas; más largas que schema.faqs)
  faqs: [
    {
      q: '¿Para quién está pensado este plan?',
      a: 'Para chefs profesionales que quieren montar un servicio premium de chef privado y showcooking a domicilio en España. Cubre desde el cliente final particular (cumpleaños, aniversarios, San Valentín, brunch privado, cenas ejecutivas) hasta el cliente B2B (empresas con showcooking corporate, hoteles boutique 4-5 estrellas con servicio in-suite, wedding planners con cenas de ensayo y pre-bodas, agencias de eventos con cooking class team-building y cenas de directiva fin de año).',
    },
    {
      q: '¿Sirve si nunca he montado mi propio negocio antes?',
      a: 'Sí. El plan está pensado para chefs solopreneurs que arrancan desde cero. Incluye constitución como autónomo (tarifa plana 80 EUR/mes primer año), alta IAE 677.9, plan APPCC móvil adaptado a servicio domiciliario, RGSEAA, seguro RC profesional eventos con cláusula intoxicación. El checklist de 6 fases con 108 hitos no deja que se te escape nada.',
    },
    {
      q: '¿Qué diferencia hay con un Personal Chef o un Caterer?',
      a: 'Mucha. El plan incluye una guía dedicada que clarifica las tres figuras: Chef Privado (modelo por evento, ticket 580-2.200 EUR, marca personal, multi-cliente), Personal Chef (recurrente con 1-3 clientes fijos high-net-worth, 1.800-4.500 EUR/mes, exclusividad parcial) y Caterer (escalable con cocina central y plantilla, 8.000-150.000 EUR por evento). El plan recomienda empezar siempre por chef privado y pivotar después si encaja con tu vida y negocio.',
    },
    {
      q: '¿Cómo cubre el plan la regulación de catering itinerante por CCAA?',
      a: 'Con un anexo dedicado dentro del Plan de Negocio. Resumen operativo de 17 comunidades autónomas con: tipo de Registro Sanitario CCAA + RGSEAA, requisitos sobre la cocina del cliente, cumplimiento normativa transporte alimentos, etiquetado bilingüe (Cataluña, País Vasco), trámites telemáticos vs presenciales y plazos por CCAA. Plus orientación regulatoria sobre la cocina del cliente final.',
    },
    {
      q: '¿La plantilla de 96 proveedores incluye contactos verificables?',
      a: 'Sí. Cada proveedor lleva web, zona de cobertura, notas operativas y estado (validado / investigar). Cuchillería japonesa (Tojiro, Yoshihiro Cutlery, Kai Shun, Misono, Sakai Takayuki) + sous-vide Anova/Polyscience/Sammic + vajilla blanca premium (Pordamsa, Steelite, Schönwald, Villeroy & Boch, Rosenthal) + carniceros premium (Cesáreo Gómez, Discarlux, Treviño, El Capricho León) + pescaderías Coruñesas + microbrotes (Aitana, MyHerbs, Petras) + caviar Riofrío + trufa Soria + AOVE DO (Castillo de Canena, Oro Bailén, Núñez de Prado). Verifica con cada uno antes de cerrar acuerdos.',
    },
    {
      q: '¿Sirve para presentar al banco si necesito financiación?',
      a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (9-12 eventos/mes break-even año 1), 3 escenarios de inversión (4.500 € mínimo viable / 11.500 € recomendado / 30.000 € premium), mix B2C+B2B desglosado, plan de cashflow con picos diciembre y verano. Es el formato estándar que piden bancos para microcrédito o ICO emprendedores.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Lanzar tu ',
    headingGold: 'Servicio Premium de Chef Privado',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a chefs privados, personal chefs y showcookers corporate que ya escalaron su servicio a domicilio con un plan adaptado al mercado español premium.',
    items: [
      'Plan de Negocio DOCX 60+ pp. + Plan Financiero Excel 6 hojas',
      'Calculadora Pricing B2C íntimo + B2B corporate + Plantilla 96 proveedores premium',
      'Catálogo cuchillería japonesa + vajilla + sous-vide (marcas y precios validados)',
      'Manual técnico APPCC móvil + Carta 12 menús temáticos + 10 experiencias',
      'Modelos contrato B2C + B2B + Guía sistemas Chef Privado vs Personal Chef vs Caterer',
      'Checklist apertura 6 fases + anexo regulación CCAA catering itinerante',
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

  stickyLabel: 'PLAN CHEF PRIVADO SHOWCOOKING — €45',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-paellero-eventos', label: 'Plan Paellero Eventos' },
    { href: '/plan-negocio-parrillero-asador-eventos', label: 'Plan Parrillero Eventos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'plan-chef-privado-showcooking-eventos',
    label: '¿Ya compraste el Plan Chef Privado / Showcooking? Vuelve a entrar al dashboard',
  },
};

export default data;
