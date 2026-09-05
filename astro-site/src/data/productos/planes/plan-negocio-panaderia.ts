// astro-site/src/data/productos/planes/plan-negocio-panaderia.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — Copy VERBATIM de la SPA:
//   · src/pages/PlanNegocioPanaderia.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/plan-negocio-panaderia/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-panaderia.ts (8 testimonios)
//   · CompatibleAppsMarquee variant="tareas" (título/subtítulo constantes de línea, hardcodeados en el template)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA (resuelto en el wrapper .astro).
//
// Divergencias vs. constantes de línea (ver types.ts):
//   · cta.headingPre = 'Es Hora de Hacer Realidad tu ' (patrón de la sub-línea A).
//   · authorBadges se OMITE → cae en el default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],
//     que es EXACTAMENTE el par de este producto.
//   · hero.titlePost se omite (Forma B: titlePre + gold + titleSubtitle en bloque).
//   · images.gridGallery DIFIERE del hero (swap: sale -hero, entra -tienda; distinto orden).
//
// QUIRK VERBATIM: schema.faqs (FAQPage JSON-LD) = 4 preguntas (subconjunto), mientras que faqs on-page
// (acordeón) = 6 preguntas. Cada bloque copiado según su origen en la SPA.
import type { PlanNegocioData } from './types';

const data: PlanNegocioData = {
  slug: 'plan-negocio-panaderia',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_PANADERIA',

  seo: {
    title:
      'Plan de Negocio: Panadería / Obrador — Plan Financiero Excel + Checklist Apertura | AI Chef Pro',
    description:
      'Plan de negocio completo para abrir una panadería u obrador artesanal en España 2026. Plan financiero Excel de 9 hojas con P&L 3 años + estacionalidad navideña, tesorería mes a mes, plan de financiación con DSCR, inversión inicial y punto de equilibrio en transacciones diarias, plan de negocio en Word de 10 secciones y checklist de apertura con 66 trámites, incluida la inscripción en el registro sanitario autonómico. €35.',
    keywords:
      'plan de negocio panadería, plan financiero obrador artesanal, abrir panadería España, RGSEAA obrador, horno pisos rotativo, masa madre, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-plan-negocio-panaderia.jpg',
  },

  schema: {
    productName:
      'Plan de Negocio: Panadería / Obrador — Plan Financiero Excel, Inversión Inicial y Checklist Apertura',
    productDescription:
      'Plan de negocio completo para abrir una panadería u obrador artesanal en España. Incluye plan financiero Excel de 9 hojas con P&L previsional a 3 años con estacionalidad navideña, inversión inicial detallada (101.600 € de CAPEX y 145.215 € con el colchón de caja), punto de equilibrio en 162 transacciones diarias con ticket medio de 5,50 € sin IVA, escenarios financieros, tesorería mes a mes con liquidación de IVA, plan de financiación con cuadro de amortización francés y DSCR, cuadro de personal panadero de 6 puestos con turno de madrugada y auditoría de horas, checklist de apertura con 66 trámites incluida la inscripción en el registro sanitario de tu Comunidad Autónoma, equipamiento específico (horno de pisos o rotativo, amasadora espiral 25-50 kg, cámara de fermentación) y los rangos de referencia del sector panadero español 2026.',
    price: '35.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Alejandro Ruiz',
        rating: '5',
        body: 'Presenté el plan al banco y me aprobaron 65K EUR de financiación con leasing del horno. La proyección a 3 años con estacionalidad navideña fue clave.',
      },
      {
        author: 'María López',
        rating: '5',
        body: 'El checklist con 60+ trámites me salvó del laberinto del RGSEAA y la licencia de obrador. Hubiera tardado el doble.',
      },
      {
        author: 'Carlos Méndez',
        rating: '5',
        body: 'El break-even por kilos de pan diarios y el mix bollería son exactamente los ratios que necesito ver.',
      },
    ],
    // FAQPage schema (4 preguntas — subconjunto VERBATIM del Helmet; on-page tiene 6)
    faqs: [
      {
        q: '¿Es un plan genérico o específico para panadería?',
        a: 'Es 100% específico para panadería y obrador artesanal en España. Las partidas de inversión, ratios financieros, costes de personal con turno madrugada y trámites legales (registro sanitario autonómico, licencia de actividad) están adaptados al modelo panadero.',
      },
      {
        q: '¿Puedo presentar este plan al banco o a inversores?',
        a: 'Sí. Incluye P&L a 3 años con estacionalidad navideña, tesorería mes a mes, plan de financiación con cuadro de amortización y DSCR año a año, punto de equilibrio en transacciones diarias y 3 escenarios. Es el formato que piden los bancos para microcrédito ICO y leasing de horno y amasadora.',
      },
      {
        q: '¿Qué trámites legales incluye el checklist?',
        a: '66 trámites en 6 fases: constitución de la SL, local y licencias (registro sanitario autonómico, licencia clasificada, salida de humos), equipamiento, personal (turno de madrugada, PRL, registro horario), marketing y primeros 90 días.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Plan de Negocio: Panadería / Obrador',
  },

  images: {
    // hero bg (6) — HeroSection.heroImages
    gallery: [
      '/lovable-uploads/ai-gallery/plan-panaderia-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-masa.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -tienda)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-panaderia-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-masa.jpg',
      '/lovable-uploads/ai-gallery/plan-panaderia-tienda.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-panaderia-hero.jpg',
  },

  hero: {
    badge: 'El plan de negocio más completo para abrir tu panadería u obrador',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Panadería / Obrador',
    titleSubtitle: 'Plan Financiero Excel, Inversión Inicial y Checklist de Apertura',
    description:
      'El plan de negocio completo para abrir una panadería u obrador artesanal en España. Plan financiero Excel de 9 hojas con P&L a 3 años y estacionalidad navideña, tesorería mensual, plan de financiación, inversión inicial detallada, punto de equilibrio en transacciones diarias y checklist de apertura con 66 trámites, incluidos el registro sanitario autonómico y la salida de humos.',
    checkItems: [
      'Plan financiero Excel de 9 hojas: P&L 3 años, tesorería mensual y financiación',
      'Inversión inicial detallada por partidas (101.600 € de CAPEX; 145.215 € con el colchón de caja)',
      'Punto de equilibrio en 162 transacciones diarias con ticket medio de 5,50 € sin IVA',
      'Checklist de apertura: 66 trámites en 6 fases, con el registro sanitario autonómico',
      'Plan de negocio en Word: 10 secciones listas para presentar',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      '9 secciones profesionales con datos reales del mercado panadero español para construir la viabilidad financiera de tu panadería u obrador y presentarla a banco o inversores.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero Excel (9 hojas)', desc: 'Supuestos, inversión inicial, P&L previsional a 3 años con estacionalidad navideña, punto de equilibrio, escenarios, personal con cobertura de horas, tesorería 12 meses con liquidación de IVA, plan de financiación con DSCR e instrucciones. Las celdas verdes son las que se teclean y las 733 fórmulas se recalculan solas.' },
      { icon: 'Coins', title: 'Inversión Inicial Detallada', desc: 'Local, horno profesional de pisos o rotativo, amasadora espiral 25-50 kg, divisora y boleadora, cámara de fermentación controlada, vitrina expositor, mobiliario y fondo de maniobra: 101.600 € de CAPEX más 43.615 € de colchón de caja, 145.215 € en total.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio (Break-Even)', desc: 'Cálculo en transacciones diarias con ticket medio de 5,50 € sin IVA: 162 al día para cubrir costes y 155 en términos de caja, con holgura sobre el equilibrio año a año y tabla de sensibilidad al ticket y al coste variable.' },
      { icon: 'BarChart3', title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes de producción y mix barra/bollería/cafetería para presentar a banco e inversores.' },
      { icon: 'Users', title: 'Cuadro de Personal Panadero', desc: 'Seis puestos —maestro panadero, oficial, ayudante de obrador, dependienta, extra de fin de semana y suplencias de vacaciones y descansos— con salarios brutos, Seguridad Social al 33 %, 14 pagas, turno de madrugada y comprobación de que las horas contratadas cubren el horario declarado.' },
      { icon: 'ShieldCheck', title: 'Checklist Apertura (6 fases)', desc: 'Constitución de la SL, local y licencias (registro sanitario de tu Comunidad Autónoma, licencia clasificada), equipamiento (proyecto técnico, salida de humos), personal, marketing y primeros 90 días.' },
      { icon: 'Wrench', title: 'Equipamiento Específico Panadería', desc: 'Horno de pisos o rotativo, amasadora espiral 25-50 kg, divisora y boleadora, cámara de fermentación controlada, laminadora y vitrina expositor, cada uno con su importe orientativo en la hoja de inversión.' },
      { icon: 'ListChecks', title: 'Ratios de Referencia Panadería', desc: 'Coste de mercancía 25-30 % en pan y 32-38 % en bollería, personal 35-42 %, alquiler 10-14 %, merma de pan 5-10 % y margen bruto objetivo por encima del 62 %. Los mismos rangos contra los que el libro se audita a sí mismo.' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'Hoja «Financiación» con origen de fondos —recursos propios, préstamo bancario, línea ICO, ENISA, business angels y subvenciones autonómicas—, comprobación de que lo aportado cubre lo que hace falta, cuadro de amortización francés con carencia y DSCR año a año.' },
    ],
  },

  testimonials: {
    subtitle:
      'Maestros panaderos, propietarios de obrador artesanal e inversores que abrieron su panadería con un plan financiero profesional',
    items: [
      { name: 'Alejandro Ruiz', role: 'Maestro Panadero Madrid', text: 'Presenté el plan al banco y me aprobaron 65K EUR de financiación con leasing del horno. La proyección a 3 años con estacionalidad navideña fue clave para que confiaran en el proyecto.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'María López', role: 'Emprendedora Obrador Barcelona', text: 'El checklist con 60+ trámites me salvó del laberinto del RGSEAA y la licencia de obrador. Hubiera tardado el doble sin esta guía organizada por fases.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Carlos Méndez', role: 'Inversor Sector Alimentación', text: 'Uso este plan para evaluar proyectos de panadería en mi cartera. El break-even por kilos de pan diarios y el mix bollería son exactamente los ratios que necesito ver.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Laura Fernández', role: 'Propietaria Panadería Artesanal Sevilla', text: 'El cuadro de personal con turno madrugada y plus nocturnidad me abrió los ojos. Antes calculaba mal los costes del maestro panadero. Ahora margen real superior al 25 %.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'David Torres', role: 'Consultor Hostelería y Obradores', text: 'Lo recomiendo a todos mis clientes panaderos. Es el plan más completo del mercado español con datos reales del sector: ratios materia prima, mermas y márgenes por categoría.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana García', role: 'Propietaria Panadería con Cafetería Valencia', text: 'Los ratios — coste materia prima 22-28 %, merma 3-5 %, margen bollería >75 % — me ayudaron a renegociar precios con el molino harinero. Ahorré 800 EUR al mes.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pedro Gutiérrez', role: 'Ex Corporativo, Abrió Obrador Pan', text: 'Venía del mundo financiero y no sabía nada de licencias de obrador ni RGSEAA. El checklist con las 6 fases me guió paso a paso. Abrí en 4 meses sin retrasos legales.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Fernando Delgado', role: 'Socio Cadena 3 Panaderías', text: 'Hemos usado el plan financiero Excel para nuestras 3 aperturas. Solo cambias las cifras del local y mix de producción y tienes business plan profesional listo para inversores.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  why: {
    subtitle:
      'No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado panadero español para abrir una panadería u obrador con cabeza.',
    reasons: [
      { icon: 'Wheat', title: 'Plan Específico Panadero', desc: 'No es plantilla genérica. Adaptado al modelo panadería/obrador: horno profesional, amasadora espiral 25-50 kg, cámara de fermentación, mix de pan, bollería y café, canal mayorista a restaurantes y estacionalidad navideña.' },
      { icon: 'BarChart3', title: 'Datos Reales Sector 2026', desc: 'Coste de mercancía 25-38 % según la línea, personal 35-42 %, merma de pan 5-10 %, margen bruto objetivo >62 %, ticket medio de 5,50 € sin IVA y break-even en transacciones diarias. Los rangos con los que el propio libro se audita.' },
      { icon: 'ShieldCheck', title: 'Registro Sanitario + 66 Trámites', desc: 'Una panadería con obrador que vende al consumidor final se inscribe en el Registro Sanitario de su Comunidad Autónoma, no en el RGSEAA estatal (art. 2.2 del RD 191/2011), y necesita licencia clasificada, salida de humos y proyecto técnico. Checklist con 66 trámites en 6 fases, con aviso de cuándo el canal mayorista sí puede obligar al RGSEAA.' },
      { icon: 'Banknote', title: 'Listo para Banco e Inversores', desc: 'P&L 3 años, punto de equilibrio, 3 escenarios y plan de financiación con ICO, ENISA, leasing de horno y subvenciones autonómicas. Pago único, sin suscripciones.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a maestros panaderos, propietarios de obrador artesanal y cadenas de panaderías en España, combinando experiencia operativa con análisis financiero profesional para garantizar la viabilidad y rentabilidad del negocio panadero.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (= el de este producto)

  bonus: {
    subtitle:
      'Además del plan financiero y el checklist de apertura, accedes a estos recursos extra — valorados en €38',
    items: [
      {
        icon: 'Users',
        label: 'BONUS 1',
        title: 'Cuadro de Personal Panadero con Cobertura de Horas',
        value: '€19',
        desc: 'Cuadro completo de personal con salarios brutos, Seguridad Social al 33 %, 14 pagas y turno de madrugada, con seis puestos —maestro panadero, oficial, ayudante de obrador, dependienta, extra de fin de semana y suplencias— y la comprobación de que las horas contratadas cubren el horario que declara el plan.',
        image: '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
      },
      {
        icon: 'ListChecks',
        label: 'BONUS 2',
        title: 'Ratios de Referencia Sector Panadero 2026',
        value: '€19',
        desc: 'Rangos de referencia del sector: coste de mercancía 25-30 % en pan y 32-38 % en bollería, personal 35-42 %, alquiler 10-14 %, merma de pan 5-10 %, margen bruto objetivo >62 %, producción diaria 80-200 kg y ticket medio de 3-6 €.',
        image: '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €35',
  },

  guarantee: {
    text:
      'Si el plan de negocio no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (6 preguntas; distinto subconjunto/texto que schema.faqs)
  faqs: [
    {
      q: '¿Es un plan genérico o específico para panadería?',
      a: 'Es 100 % específico para panadería y obrador artesanal en España. Las partidas de inversión (horno profesional, amasadora, cámara de fermentación), los ratios financieros (coste de mercancía, merma, margen de pan frente a bollería), los costes de personal con turno de madrugada y los trámites legales (registro sanitario autonómico, licencia de actividad clasificada) están adaptados al modelo panadero. El IVA va incluso separado: el pan común al 4 % y la bollería y el café al 10 %.',
    },
    {
      q: '¿Puedo presentar este plan al banco o a inversores?',
      a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años con estacionalidad navideña, tesorería mes a mes, plan de financiación con cuadro de amortización y DSCR, punto de equilibrio en transacciones diarias y 3 escenarios. Es exactamente el formato que piden los bancos para microcrédito o ICO emprendedores y leasing de equipamiento (horno, amasadora).',
    },
    {
      q: '¿Puedo modificar las cifras del Excel?',
      a: 'Sí. Las celdas verdes son las que se teclean y las 733 fórmulas se recalculan solas: cambia el alquiler, las transacciones al día, el ticket medio sin IVA, los salarios del maestro panadero o cualquier partida de inversión. Las hojas van protegidas sin contraseña para que no borres una fórmula sin querer (Revisar → Desproteger hoja). Incluye hoja de instrucciones.',
    },
    {
      q: '¿Qué trámites legales incluye el checklist de apertura?',
      a: '66 trámites organizados en 6 fases: constitución de la SL; local y licencias (registro sanitario de tu Comunidad Autónoma, licencia clasificada, hojas de reclamaciones, gestor de residuos, DDD); equipamiento (proyecto técnico, instalación de horno, salida de humos); personal (contratos, Seguridad Social, registro horario, PRL del turno de madrugada); marketing (incluidos los acuerdos con el canal mayorista y las licencias de música); y primeros 90 días de operación.',
    },
    {
      q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
      a: 'Los planes gratuitos son plantillas genéricas sin un modelo detrás. Este plan trae un caso base calculado y auditado por el propio libro (cinco ratios con semáforo, todos en verde), los rangos de referencia que publica su hoja de instrucciones (coste de mercancía 25-38 %, personal 35-42 %, merma 5-10 %, margen bruto >62 %), tesorería mes a mes con la liquidación de IVA, plan de financiación con DSCR, cuadro de personal con turno de madrugada y auditoría de horas, y un checklist de 66 trámites con la norma citada artículo por artículo.',
    },
    {
      q: '¿Cómo funciona la garantía?',
      a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu panadería con total confianza.',
    },
  ],

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Panadería',
    subtitle:
      'No dejes pasar esta oportunidad. Únete a maestros panaderos y emprendedores que ya abrieron su panadería u obrador artesanal con un plan financiero profesional.',
    items: [
      'Plan financiero Excel de 9 hojas: P&L 3 años, tesorería y financiación',
      'Inversión inicial detallada: 101.600 € de CAPEX y 145.215 € con el colchón de caja',
      'Punto de equilibrio en 162 transacciones diarias con ticket de 5,50 € sin IVA',
      '3 escenarios financieros (pesimista/realista/optimista)',
      'Checklist de apertura con 66 trámites, incluido el registro sanitario autonómico',
      'Equipamiento específico panadería + ratios sectoriales',
      'Plan de negocio en Word con 10 secciones listas para presentar',
      'BONUS: Cuadro de Personal Panadero con cobertura de horas (€19)',
      'BONUS: Ratios Referencia Sector Panadero 2026 (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €35',
  },

  pricing: {
    priceOld: '€120',
    price: '€35',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71 % de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €85 HOY!',
  },

  stickyLabel: 'PLAN PANADERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: '/kit-tareas-panaderia', label: 'Kit Tareas Panadería' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.2 · septiembre 2026',

  alreadyBought: {
    product: 'plan-negocio-panaderia',
    label: '¿Ya compraste el Plan de Negocio Panadería? Vuelve a entrar al dashboard',
  },
};

export default data;
