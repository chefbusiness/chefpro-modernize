// astro-site/src/data/productos/kits/kit-plan-financiero.ts
// LÍNEA KITS EXCEL — producto kit-plan-financiero. Copy VERBATIM de la SPA:
//   · src/pages/KitPlanFinanciero.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/kit-plan-financiero/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-plan-financiero.ts (8 testimonios)
//   · src/components/shared/CompatibleAppsMarquee.tsx (variant="tareas" → título/subtítulo, IGUAL
//     que kit-gestion-personal — la SPA reutiliza el copy de la línea Tareas para este producto)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_PLAN_FINANCIERO (resuelto en el wrapper .astro).
//
// Divergencias vs. el producto de referencia (kit-escandallos), todas cubiertas por las 5 props
// opcionales documentadas en types.ts:
//   1. Hero H1 usa AMBAS formas: titlePost inline (" para Restaurantes") + titleSubtitle en
//      bloque ("Planifica, Controla y Presenta tus Numeros").
//   2. hero.badgeTone = 'red' (badge = alerta "El 60% de los restaurantes cierra...").
//   3. grid.fourCols = false/omitido (10 plantillas, grid-cols-2 md:grid-cols-3 — NO 4 columnas).
//   4. guarantee.headingPre SIN tildes ("Garantia de Satisfaccion ").
//   5. authorBadges SIN tildes (['Consultor Gastronomico', '+200 aperturas asesoradas']).
//   stickyVariant: se omite (default 'v2', que es el que usa este producto).
//   images.gridGallery: se omite — el ContentGrid de la SPA usa EXACTAMENTE el mismo set y
//   orden de 6 imágenes que el hero (no diverge como en escandallos).
//
// QUIRK VERBATIM (mantener tal cual, NO es error de transcripción):
//   - pricing.discountBadge "-79%" (hero/buyBox) vs pricing.buyBoxNote "72% de descuento" —
//     inconsistencia real de la SPA (mismo patrón ya visto en otros productos de esta línea).
//   - buyBox.ctaLabel / cta.ctaLabel usan "SI" sin tilde ("SI, QUIERO EL KIT FINANCIERO — 39 EUR"),
//     a diferencia de escandallos ("SÍ, QUIERO EL KIT — €12"). Copiado VERBATIM.
//   - schema.faqs (4 preguntas) es un SUBCONJUNTO DISTINTO de faqs on-page (6 preguntas): dos
//     preguntas on-page ("¿Las plantillas se conectan entre si?" y "¿Puedo usarlo para varios
//     restaurantes?") NO están en el FAQPage schema, y las 4 que sí coinciden tienen texto/pregunta
//     más corto en el schema. Ambos bloques VERBATIM, cada uno según su origen en la SPA.
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'kit-plan-financiero',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_FINANCIERO',

  seo: {
    title: 'Kit Plan Financiero para Restaurantes — Plantillas Excel | AI Chef Pro',
    description:
      '10 plantillas Excel con fórmulas automáticas: plan financiero a 3 y 5 años, punto de equilibrio, cash flow, P&L, CAPEX, ratios e informe de viabilidad para bancos. 39 EUR.',
    keywords:
      'plan financiero restaurante, plan de negocio restaurante, punto equilibrio restaurante, cash flow restaurante, P&L hosteleria, viabilidad restaurante, CAPEX restaurante, food cost, abrir restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-plan-financiero.jpg',
  },

  schema: {
    productName: 'Kit Plan Financiero para Restaurantes — Plantillas Excel',
    productDescription:
      '10 plantillas Excel con fórmulas automáticas: plan financiero a 3 y 5 años, punto de equilibrio, cash flow, P&L, CAPEX, ratios e informe de viabilidad para bancos.',
    price: '39.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Ricardo Gomez',
        rating: '5',
        body: 'El plan previsional a 3 anos fue lo que me pidio el banco. Lo presente tal cual y me aprobaron 120.000 EUR.',
      },
      {
        author: 'Ana Beltran',
        rating: '5',
        body: 'Lo uso con todos mis clientes. El simulador de escenarios profesionaliza cualquier proyecto de apertura.',
      },
      {
        author: 'Isabel Campos',
        rating: '5',
        body: 'El dashboard de ratios con benchmarks del sector es exactamente lo que necesitaba para los comites de direccion.',
      },
    ],
    // FAQPage schema (4 preguntas — SUBCONJUNTO DISTINTO de las 6 FAQ on-page, VERBATIM del Helmet)
    faqs: [
      {
        q: '¿Sirve para un restaurante que ya esta abierto?',
        a: 'Si. El P&L mensual, el dashboard de ratios y el cash flow son especialmente utiles para restaurantes en funcionamiento.',
      },
      {
        q: '¿Necesito conocimientos de contabilidad?',
        a: 'No. Solo introduces tus numeros y las formulas calculan todo automaticamente: ratios, graficos, escenarios.',
      },
      {
        q: '¿El banco aceptara este informe?',
        a: 'Si. El formato sigue la estructura que las entidades financieras esperan: TIR, VAN, payback period, escenarios.',
      },
      {
        q: '¿Hay garantia de devolucion?',
        a: '30 dias de garantia completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit Plan Financiero para Restaurantes',
  },

  images: {
    // hero bg (6) — IDÉNTICAS a ContentGrid.galleryImages en la SPA → gridGallery se omite
    gallery: [
      '/lovable-uploads/ai-gallery/plan-financiero-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-financiero-oficina.jpg',
      '/lovable-uploads/ai-gallery/plan-financiero-reunion.jpg',
      '/lovable-uploads/ai-gallery/plan-financiero-graficos.jpg',
      '/lovable-uploads/ai-gallery/plan-financiero-restaurante.jpg',
      '/lovable-uploads/ai-gallery/plan-financiero-analisis.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-financiero-oficina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-financiero-oficina.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-financiero-hero.jpg',
  },

  hero: {
    badgeTone: 'red',
    badge: 'El 60% de los restaurantes cierra en los primeros 3 anos por falta de planificacion financiera',
    titlePre: 'Kit ',
    titleGold: 'Plan Financiero',
    titlePost: ' para Restaurantes',
    titleSubtitle: 'Planifica, Controla y Presenta tus Numeros',
    description:
      '10 plantillas Excel con fórmulas automáticas para crear tu plan financiero, calcular el punto de equilibrio, controlar P&L, gestionar cash flow y presentar un informe de viabilidad profesional al banco.',
    checkItems: [
      'Plan financiero previsional a 3 y 5 años con gráficos automáticos',
      'Calculadora de punto de equilibrio con 3 escenarios',
      'Cash flow forecast 12 meses con alertas de liquidez',
      'P&L mensual real vs presupuesto con semaforo de desviaciones',
      'Informe de viabilidad listo para presentar al banco',
    ],
    ctaLabel: 'COMPRAR AHORA — 39 EUR',
  },

  // variant="tareas" en la SPA (igual que kit-gestion-personal), NO variant="kit"
  compatApps: {
    titleHtml: 'Imprime, Delega y <span class="text-[#FFD700]">Controla</span>',
    subtitleHtml:
      'Plantillas Excel optimizadas para imprimir en A4. Compatible con Excel, Google Sheets, LibreOffice y Numbers',
  },

  grid: {
    countGold: '10',
    headingRest: ' Plantillas de Plan Financiero',
    subtitle:
      'Cada plantilla incluye formulas encadenadas, graficos profesionales y benchmarks reales del sector hostelero espanol.',
    // fourCols omitido (3-col, igual que el resto de la línea salvo escandallos)
    templates: [
      { icon: 'TrendingUp', title: 'Plan Financiero Previsional (3 Años)', desc: 'Proyección de ingresos y gastos a 3 años con desglose mensual. Líneas de ingreso (comedor, barra, delivery, eventos), costes variables/fijos, EBITDA y gráficos automáticos.' },
      { icon: 'TrendingUp', title: 'Plan Financiero Previsional (5 Años)', desc: 'Misma estructura que el plan a 3 años pero con proyección a 5 años. Ideal para presentaciones a bancos, inversores o franquicias que requieren horizontes más largos.' },
      { icon: 'Target', title: 'Calculadora Punto de Equilibrio', desc: 'Calcula ticket medio necesario, comensales/dia minimos y umbral de facturacion. Incluye 3 escenarios (pesimista/realista/optimista) con grafico visual de break-even.' },
      { icon: 'Wallet', title: 'Cash Flow Forecast (12 Meses)', desc: 'Flujo de caja mensual con desfase cobros/pagos, IVA trimestral y estacionalidad. Alerta automatica en rojo cuando el saldo cae por debajo del umbral de seguridad.' },
      { icon: 'Building2', title: 'Presupuesto de Inversion / CAPEX', desc: 'Desglose por partida: obra, equipamiento cocina, mobiliario sala, tecnologia, licencias. Presupuesto vs real con % desviacion. Totales con y sin IVA.' },
      { icon: 'BarChart3', title: 'P&L Mensual Real vs Presupuesto', desc: 'Cada mes compara real vs presupuesto con desviacion % y semaforo (verde <5%, amarillo 5-10%, rojo >10%). Food cost, labor cost y prime cost automaticos.' },
      { icon: 'PieChart', title: 'Dashboard de Ratios Financieros', desc: 'Calcula food cost %, labor cost %, prime cost %, GOP, RevPASH, coste por cubierto. Compara contra benchmarks del sector hostelero espanol.' },
      { icon: 'FileText', title: 'Informe de Viabilidad para Bancos', desc: 'Formato profesional listo para presentar: resumen ejecutivo, proyecciones, TIR, VAN, payback period. Disenado para lo que los bancos realmente piden.' },
      { icon: 'Shuffle', title: 'BONUS: Simulador de Escenarios', desc: 'Modifica ticket medio, ocupacion, food cost y ve impacto instantaneo en rentabilidad. 3 escenarios con comparativa visual lado a lado.' },
      { icon: 'ClipboardList', title: 'BONUS: Checklist Pre-Apertura Financiero', desc: '48 items agrupados en 6 fases: constitucion, financiacion, licencias, proveedores, seguros, tesoreria. Con estado, responsable y fecha limite.' },
    ],
  },

  why: {
    headingPre: '¿Por Que Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas financieras genericas. Son herramientas disenadas por un chef en cocina desde los 17 años y consultor gastronómico desde 2010, asesorando aperturas.',
    reasons: [
      { icon: 'Utensils', title: 'Disenado para Hosteleria', desc: 'Ratios, benchmarks y estructura de costes especificos del sector: food cost, labor cost, prime cost, GOP. No son plantillas financieras genericas.' },
      { icon: 'Calculator', title: 'Formulas Encadenadas', desc: 'Los datos del CAPEX alimentan el cash flow. El plan previsional alimenta el break-even. Los ratios se calculan solos. Todo conectado automaticamente.' },
      { icon: 'ShieldCheck', title: 'Formato Banco-Ready', desc: 'El informe de viabilidad sigue la estructura exacta que las entidades financieras esperan: TIR, VAN, payback, escenarios. Listo para presentar.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 2.000 EUR. Esto es 39 EUR', desc: 'Las mismas herramientas que usan los consultores financieros para preparar planes de negocio, pero en Excel por un pago único. Sin suscripción.' },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de calculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura y el plan financiero de mas de 200 establecimientos hosteleros.',
  authorBadges: ['Consultor Gastronomico', '+200 aperturas asesoradas'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 8 plantillas principales, recibes estos recursos adicionales — valorados en 28 EUR',
    items: [
      {
        icon: 'Shuffle',
        label: 'BONUS 1',
        title: 'Simulador de Escenarios (What-If)',
        value: '14 EUR',
        desc: 'Modifica ticket medio, ocupacion, food cost y ve impacto instantaneo en rentabilidad. Compara 3 escenarios lado a lado: pesimista, realista y optimista.',
        image: '/lovable-uploads/ai-gallery/plan-financiero-graficos.jpg',
      },
      {
        icon: 'ClipboardList',
        label: 'BONUS 2',
        title: 'Checklist Pre-Apertura Financiero',
        value: '14 EUR',
        desc: '48 items agrupados en 6 fases: constitucion, financiacion, licencias, proveedores, seguros, tesoreria. Con estado, responsable y fecha limite para no olvidar nada.',
        image: '/lovable-uploads/ai-gallery/plan-financiero-reunion.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SI, QUIERO EL KIT FINANCIERO — 39 EUR',
  },

  guarantee: {
    // headingPre SIN tildes (variante inventario/gestion/plan): "Garantia de Satisfaccion "
    headingPre: 'Garantia de Satisfaccion ',
    text:
      'Si las plantillas no te ayudan a planificar mejor las finanzas de tu restaurante, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Dias de garantia' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incomodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (6 preguntas, distinto subconjunto/texto que schema.faqs)
  faqs: [
    {
      q: '¿Sirve para un restaurante que ya esta abierto?',
      a: 'Si. El P&L mensual real vs presupuesto, el dashboard de ratios y el cash flow forecast son especialmente utiles para restaurantes en funcionamiento. El plan previsional y el informe de viabilidad son mas para aperturas o expansiones.',
    },
    {
      q: '¿Necesito conocimientos de contabilidad?',
      a: 'No. Las plantillas estan disenadas para hosteleros, no para contables. Solo introduces tus numeros (ventas, costes, inversiones) y las formulas calculan todo automaticamente: ratios, graficos, escenarios.',
    },
    {
      q: '¿El banco aceptara este informe de viabilidad?',
      a: 'Si. El formato sigue la estructura que las entidades financieras esperan ver: resumen ejecutivo, proyecciones a 3 anos, TIR, VAN, payback period y escenarios. Lo hemos validado con asesores financieros.',
    },
    {
      q: '¿Las plantillas se conectan entre si?',
      a: 'Si. Las formulas estan encadenadas: los datos del CAPEX alimentan el cash flow, el plan previsional alimenta el break-even, y los ratios se calculan automaticamente desde el P&L.',
    },
    {
      q: '¿Puedo usarlo para varios restaurantes?',
      a: 'Si. La licencia es personal — puedes usar las plantillas en todos los proyectos que gestiones. Ideal para grupos de restauracion, inversores y consultores.',
    },
    {
      q: '¿Hay garantia de devolucion?',
      a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Abrir o Gestionar Tu Restaurante a Ciegas',
    subtitle:
      '10 plantillas profesionales por menos de lo que cuesta una hora de consultoria financiera.',
    items: [
      'Plan financiero previsional a 3 y 5 años con gráficos',
      'Calculadora de punto de equilibrio con 3 escenarios',
      'Cash flow forecast 12 meses con alertas de liquidez',
      'Presupuesto de inversion CAPEX con desviaciones',
      'P&L mensual real vs presupuesto con semaforo',
      'Dashboard de ratios con benchmarks del sector',
      'Informe de viabilidad listo para bancos (TIR, VAN, payback)',
      'BONUS: Simulador de Escenarios What-If (14 EUR)',
      'BONUS: Checklist Pre-Apertura Financiero (14 EUR)',
    ],
    ctaLabel: 'SI, QUIERO EL KIT FINANCIERO — 39 EUR',
  },

  testimonials: {
    subtitle:
      'Propietarios, inversores y consultores que ya planifican sus finanzas con estas plantillas',
    items: [
      { name: 'Ricardo Gomez', role: 'Propietario, restaurante casual recien abierto', text: 'El plan previsional a 3 anos fue lo que me pidio el banco para el prestamo. Lo presente tal cual, con los graficos y los escenarios. Me aprobaron 120.000 EUR en 2 semanas.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Ana Beltran', role: 'Consultora gastronomica, +15 anos', text: 'Lo uso con todos mis clientes que van a abrir. El simulador de escenarios es brutal: cambias el ticket medio o la ocupacion y ves al instante como afecta a la rentabilidad. Profesionaliza cualquier proyecto.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Javier Morales', role: 'Gerente, grupo de 3 restaurantes en Valencia', text: 'El P&L mensual real vs presupuesto me cambio la vida. Antes me enteraba a final de ano de que algo iba mal. Ahora detecto desviaciones cada mes con el semaforo y corrijo a tiempo.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Isabel Campos', role: 'Directora financiera, cadena de restaurantes', text: 'El dashboard de ratios financieros con benchmarks del sector es exactamente lo que necesitaba para los comites de direccion. Food cost, labor cost, prime cost, GOP — todo automatico.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Fernando Reyes', role: 'Chef emprendedor, primer restaurante', text: 'La calculadora de punto de equilibrio me abrio los ojos. Descubri que necesitaba 45 cubiertos diarios a 22 EUR de ticket medio para ser rentable. Sin eso habria abierto a ciegas.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Maria Herrero', role: 'Asesora fiscal especializada en hosteleria', text: 'El cash flow forecast con alertas de liquidez es lo que mas valoro. Mis clientes ahora ven 3 meses antes cuando van a tener tension de tesoreria. Prevenir es infinitamente mas barato que curar.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pablo Navarro', role: 'Inversor, 2 restaurantes + dark kitchen', text: 'El presupuesto CAPEX con desviacion real vs presupuesto me evito sorpresas en la obra. Cada partida controlada: cocina, mobiliario, tecnologia, licencias. Sabia en todo momento cuanto me quedaba.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Daniel Ortiz', role: 'Director de operaciones, franquicia hostelera', text: 'El informe de viabilidad para bancos es impecable. TIR, VAN, payback period — todo calculado automaticamente. Nuestros franquiciados lo usan para conseguir financiacion sin contratar consultores.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  pricing: {
    priceOld: '190 EUR',
    price: '39 EUR',
    discountBadge: '-79%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    // QUIRK VERBATIM: -79% en hero/buyBox pero "72%" aquí (inconsistencia real de la SPA)
    buyBoxNote: 'Precio especial de lanzamiento — 72% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: 'Ahorra 151 EUR HOY',
  },

  stickyLabel: 'KIT PLAN FINANCIERO — 39 EUR',
  // stickyVariant omitido (default 'v2', el que usa este producto)

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/kit-inventario', label: 'Kit Inventario' },
    { href: '/kit-gestion-personal', label: 'Kit Gestion Personal' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'kit-plan-financiero',
    label: '¿Ya compraste el Kit Plan Financiero? Vuelve a entrar al dashboard',
  },
};

export default data;
