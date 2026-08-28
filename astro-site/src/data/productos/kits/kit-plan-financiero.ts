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
//      bloque ("Planifica, Controla y Presenta tus Números").
//   2. hero.badgeTone = 'red' (badge de alerta). OJO: el badge YA NO cita «El 60% de los restaurantes
//      cierra…» — esa cifra sin fuente se retiró a propósito (COM-24, v2.0); hoy dice «La mayoría de los
//      cierres tempranos se explican por una planificación financiera inexistente». No restaurarla.
//   3. grid.fourCols = false/omitido (10 plantillas, grid-cols-2 md:grid-cols-3 — NO 4 columnas).
//   4. DEROGADO por COM-23 (v2.0, 2026-08-29): guarantee.headingPre iba SIN tildes
//      (las dos palabras sin tilde); ahora es 'Garantía de Satisfacción '.
//   5. DEROGADO por COM-23 (v2.0, 2026-08-29): authorBadges iban SIN tildes; ahora
//      ['Consultor Gastronómico', '+200 aperturas asesoradas'].
//   stickyVariant: se omite (default 'v2', que es el que usa este producto).
//   images.gridGallery: se omite — el ContentGrid de la SPA usa EXACTAMENTE el mismo set y
//   orden de 6 imágenes que el hero (no diverge como en escandallos).
//
// QUIRK VERBATIM (mantener tal cual, NO es error de transcripción):
//   - pricing.discountBadge "-79%" (hero/buyBox) vs pricing.buyBoxNote "72% de descuento" —
//     inconsistencia real de la SPA (mismo patrón ya visto en otros productos de esta línea).
//   - DEROGADO por COM-23 (v2.0, 2026-08-29): buyBox.ctaLabel / cta.ctaLabel usaban "SI" sin
//     tilde; ahora "SÍ, QUIERO EL KIT FINANCIERO — 39 EUR", como en escandallos. Los puntos 4 y 5
//     de arriba y este quirk quedan DEROGADOS: el 2026-08-29 se barrió de tildes y ñ todo el copy
//     de este producto (COM-23 del R1 / BLOQUEO 2 del crítico) en las dos superficies a la vez
//     —este fichero y la SPA (src/components/kit-plan-financiero/*, src/pages/KitPlanFinanciero.tsx,
//     src/pages/KitPlanFinancieroDashboard.tsx, src/data/testimonials-plan-financiero.ts)—, así que
//     el port sigue siendo VERBATIM. Ninguna frase, cifra ni claim cambió: sólo ortografía.
//   - Fix 2026-08-24 (COM-21, independiente de la versión del xlsx): schema.faqs pasa a ser el
//     MISMO array que faqs on-page (6 preguntas) — antes era un subconjunto recortado de 4 y el
//     FAQPage no coincidía con lo que veía el visitante. Esto es una corrección de SEO/schema, no
//     un cambio de contenido del producto: NO implica que el kit ya esté en v2.0 (sigue en v1.1,
//     ver nota más abajo sobre updateNote).
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'kit-plan-financiero',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_FINANCIERO',

  seo: {
    title: 'Kit Plan Financiero para Restaurantes — Plantillas Excel | AI Chef Pro',
    description:
      '10 plantillas Excel con fórmulas automáticas: plan financiero a 3 y 5 años, punto de equilibrio, cash flow, P&L, CAPEX, ratios e informe de viabilidad para bancos. 39 EUR.',
    keywords:
      'plan financiero restaurante, plan de negocio restaurante, punto equilibrio restaurante, cash flow restaurante, P&L hostelería, viabilidad restaurante, CAPEX restaurante, food cost, abrir restaurante, AI Chef Pro',
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
        author: 'Ricardo Gómez',
        rating: '5',
        body: 'El plan previsional a 3 años fue lo que me pidió el banco. Lo presenté tal cual y me aprobaron 120.000 EUR.',
      },
      {
        author: 'Ana Beltrán',
        rating: '5',
        body: 'Lo uso con todos mis clientes. El simulador de escenarios profesionaliza cualquier proyecto de apertura.',
      },
      {
        author: 'Isabel Campos',
        rating: '5',
        body: 'El dashboard de ratios con benchmarks del sector es exactamente lo que necesitaba para los comités de dirección.',
      },
    ],
    // FAQPage schema — v2.0 (COM-21): MISMO array que la FAQ on-page (6 preguntas), no un
    // subconjunto recortado — antes el FAQPage declaraba solo 4 de las 6 preguntas visibles.
    faqs: [
      {
        q: '¿Sirve para un restaurante que ya está abierto?',
        a: 'Sí. El P&L mensual real vs presupuesto, el dashboard de ratios y el cash flow forecast son especialmente útiles para restaurantes en funcionamiento. El plan previsional y el informe de viabilidad son más para aperturas o expansiones.',
      },
      {
        q: '¿Necesito conocimientos de contabilidad?',
        a: 'No. Las plantillas están diseñadas para hosteleros, no para contables. Solo introduces tus números (ventas, costes, inversiones) y las fórmulas calculan todo automáticamente: ratios, gráficos, escenarios.',
      },
      {
        q: '¿El banco aceptará este informe de viabilidad?',
        a: 'Te da la estructura que piden las entidades: resumen ejecutivo, proyecciones a 5 años, ratios de solvencia, TIR, VAN y payback. La aprobación final depende de tu proyecto y del banco.',
      },
      {
        q: '¿Las plantillas se conectan entre sí?',
        a: 'Son coherentes entre sí: mismas categorías de ingreso/gasto, mismos ratios y la misma base sin IVA en 9 de las 10 (la de tesorería va con IVA porque es caja, y lo dice en su portada). Dentro de cada libro sí hay fórmulas encadenadas (mensual, total anual, resumen); entre libros no.',
      },
      {
        q: '¿Puedo usarlo para varios restaurantes?',
        a: 'Sí. La licencia es personal — puedes usar las plantillas en todos los proyectos que gestiones. Ideal para grupos de restauración, inversores y consultores.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. Si no estás satisfecho, 100 % reembolso sin preguntas.',
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
    badge: 'La mayoría de los cierres tempranos se explican por una planificación financiera inexistente',
    titlePre: 'Kit ',
    titleGold: 'Plan Financiero',
    titlePost: ' para Restaurantes',
    titleSubtitle: 'Planifica, Controla y Presenta tus Números',
    description:
      '10 plantillas Excel con fórmulas automáticas para crear tu plan financiero, calcular el punto de equilibrio, controlar P&L, gestionar cash flow y presentar un informe de viabilidad profesional al banco.',
    checkItems: [
      'Plan financiero previsional a 3 y 5 años con gráficos automáticos',
      'Calculadora de punto de equilibrio con 3 escenarios',
      'Cash flow forecast 12 meses con alertas de liquidez',
      'P&L mensual real vs presupuesto con semáforo de desviaciones',
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
      'Las 10 plantillas son coherentes entre sí: mismas categorías de ingreso/gasto, mismos ratios y la misma base sin IVA (salvo la tesorería, que va con IVA porque es caja). Benchmarks reales del sector hostelero español.',
    // fourCols omitido (3-col, igual que el resto de la línea salvo escandallos)
    templates: [
      { icon: 'TrendingUp', title: 'Plan Financiero Previsional (3 Años)', desc: 'Proyección de ingresos y gastos a 3 años con desglose mensual. Líneas de ingreso (comedor, barra, delivery, eventos), costes variables/fijos, EBITDA y gráficos automáticos.' },
      { icon: 'TrendingUp', title: 'Plan Financiero Previsional (5 Años)', desc: 'Misma estructura que el plan a 3 años pero con proyección a 5 años. Ideal para presentaciones a bancos, inversores o franquicias que requieren horizontes más largos.' },
      { icon: 'Target', title: 'Calculadora Punto de Equilibrio', desc: 'Calcula comensales/día mínimos, umbral de facturación y el ticket medio necesario para los cubiertos que preveas, con gráfico de ingresos vs costes. Break-even operativo y de caja, y 3 escenarios: pesimista, realista y optimista.' },
      { icon: 'Wallet', title: 'Cash Flow Forecast (12 Meses)', desc: 'Flujo de caja mensual con desfase cobros/pagos, IVA trimestral y estacionalidad. Alerta automática en rojo cuando el saldo cae por debajo del umbral de seguridad.' },
      { icon: 'Building2', title: 'Presupuesto de Inversión / CAPEX', desc: 'Desglose por partida: obra, equipamiento cocina, mobiliario sala, tecnología, licencias. Presupuesto vs real con % desviación. Totales con y sin IVA.' },
      { icon: 'BarChart3', title: 'P&L Mensual Real vs Presupuesto', desc: 'Cada mes compara real vs presupuesto con desviación % y semáforo (verde <5%, amarillo 5-10%, rojo >10%). Food cost, labor cost y prime cost automáticos.' },
      { icon: 'PieChart', title: 'Dashboard de Ratios Financieros', desc: 'Calcula food cost %, labor cost %, prime cost %, GOP, RevPASH, coste por cubierto. Compara contra benchmarks del sector hostelero español.' },
      { icon: 'FileText', title: 'Informe de Viabilidad para Bancos', desc: 'Formato profesional listo para presentar: resumen ejecutivo, proyecciones, TIR, VAN, payback period. Diseñado para lo que los bancos realmente piden.' },
      { icon: 'Shuffle', title: 'BONUS: Simulador de Escenarios', desc: 'Modifica ticket medio, cubiertos/día, food cost y ve impacto instantáneo en rentabilidad. 3 escenarios con comparativa visual lado a lado.' },
      { icon: 'ClipboardList', title: 'BONUS: Checklist Pre-Apertura Financiero', desc: '54 ítems agrupados en 7 fases: constitución, financiación, licencias, proveedores, seguros, tesorería y obligaciones laborales. Con estado, responsable y fecha límite.' },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas financieras genéricas. Son herramientas diseñadas por un chef en cocina desde los 17 años y consultor gastronómico desde 2010, asesorando aperturas.',
    reasons: [
      { icon: 'Utensils', title: 'Diseñado para Hostelería', desc: 'Ratios, benchmarks y estructura de costes específicos del sector: food cost, labor cost, prime cost, GOP. No son plantillas financieras genéricas.' },
      { icon: 'Calculator', title: 'Plantillas Coherentes Entre Sí', desc: 'Mismas categorías de ingreso/gasto, mismos ratios y la misma base sin IVA en 9 de las 10 (la de tesorería va con IVA porque es caja, y lo dice en su portada). Dentro de cada libro las fórmulas sí están encadenadas: mensual, total anual y resumen.' },
      { icon: 'ShieldCheck', title: 'Formato Banco-Ready', desc: 'El informe de viabilidad sigue la estructura exacta que las entidades financieras esperan: TIR, VAN, payback, escenarios. Listo para presentar.' },
      { icon: 'RefreshCw', title: 'Un Consultor Cobra 2.000 EUR. Esto es 39 EUR', desc: 'Las mismas herramientas que usan los consultores financieros para preparar planes de negocio, pero en Excel por un pago único. Sin suscripción.' },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de cálculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura y el plan financiero de más de 200 establecimientos hosteleros.',
  authorBadges: ['Consultor Gastronómico', '+200 aperturas asesoradas'],

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
        desc: 'Modifica ticket medio, cubiertos/día, food cost y ve impacto instantáneo en rentabilidad. Compara 3 escenarios lado a lado: pesimista, realista y optimista.',
        image: '/lovable-uploads/ai-gallery/plan-financiero-graficos.jpg',
      },
      {
        icon: 'ClipboardList',
        label: 'BONUS 2',
        title: 'Checklist Pre-Apertura Financiero',
        value: '14 EUR',
        desc: '54 ítems agrupados en 7 fases: constitución, financiación, licencias, proveedores, seguros, tesorería y obligaciones laborales. Con estado, responsable y fecha límite para no olvidar nada.',
        image: '/lovable-uploads/ai-gallery/plan-financiero-reunion.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT FINANCIERO — 39 EUR',
  },

  guarantee: {
    // COM-23 (2026-08-29): antes iba SIN tildes, como en las variantes inventario/gestion;
    // corregido a "Garantía de Satisfacción ".
    headingPre: 'Garantía de Satisfacción ',
    text:
      'Si las plantillas no te ayudan a planificar mejor las finanzas de tu restaurante, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (6 preguntas, distinto subconjunto/texto que schema.faqs)
  faqs: [
    {
      q: '¿Sirve para un restaurante que ya está abierto?',
      a: 'Sí. El P&L mensual real vs presupuesto, el dashboard de ratios y el cash flow forecast son especialmente útiles para restaurantes en funcionamiento. El plan previsional y el informe de viabilidad son más para aperturas o expansiones.',
    },
    {
      q: '¿Necesito conocimientos de contabilidad?',
      a: 'No. Las plantillas están diseñadas para hosteleros, no para contables. Solo introduces tus números (ventas, costes, inversiones) y las fórmulas calculan todo automáticamente: ratios, gráficos, escenarios.',
    },
    {
      q: '¿El banco aceptará este informe de viabilidad?',
      a: 'Te da la estructura que piden las entidades: resumen ejecutivo, proyecciones a 5 años, ratios de solvencia, TIR, VAN y payback. La aprobación final depende de tu proyecto y del banco.',
    },
    {
      q: '¿Las plantillas se conectan entre sí?',
      a: 'Son coherentes entre sí: mismas categorías de ingreso/gasto, mismos ratios y la misma base sin IVA en 9 de las 10 (la de tesorería va con IVA porque es caja, y lo dice en su portada). Dentro de cada libro sí hay fórmulas encadenadas (mensual, total anual, resumen); entre libros no, para que puedas mover o abrir cada plantilla por separado sin romper ninguna referencia.',
    },
    {
      q: '¿Puedo usarlo para varios restaurantes?',
      a: 'Sí. La licencia es personal — puedes usar las plantillas en todos los proyectos que gestiones. Ideal para grupos de restauración, inversores y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100 % reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Abrir o Gestionar Tu Restaurante a Ciegas',
    subtitle:
      '10 plantillas profesionales por menos de lo que cuesta una hora de consultoría financiera.',
    items: [
      'Plan financiero previsional a 3 y 5 años con gráficos',
      'Calculadora de punto de equilibrio con 3 escenarios',
      'Cash flow forecast 12 meses con alertas de liquidez',
      'Presupuesto de inversión CAPEX con desviaciones',
      'P&L mensual real vs presupuesto con semáforo',
      'Dashboard de ratios con benchmarks del sector',
      'Informe de viabilidad listo para bancos (TIR, VAN, payback)',
      'BONUS: Simulador de Escenarios What-If (14 EUR)',
      'BONUS: Checklist Pre-Apertura Financiero (14 EUR)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT FINANCIERO — 39 EUR',
  },

  testimonials: {
    subtitle:
      'Propietarios, inversores y consultores que ya planifican sus finanzas con estas plantillas',
    items: [
      { name: 'Ricardo Gómez', role: 'Propietario, restaurante casual recién abierto', text: 'El plan previsional a 3 años fue lo que me pidió el banco para el préstamo. Lo presenté tal cual, con los gráficos y los escenarios. Me aprobaron 120.000 EUR en 2 semanas.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Ana Beltrán', role: 'Consultora gastronómica, +15 años', text: 'Lo uso con todos mis clientes que van a abrir. El simulador de escenarios es brutal: cambias el ticket medio o la ocupación y ves al instante cómo afecta a la rentabilidad. Profesionaliza cualquier proyecto.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Javier Morales', role: 'Gerente, grupo de 3 restaurantes en Valencia', text: 'El P&L mensual real vs presupuesto me cambió la vida. Antes me enteraba a final de año de que algo iba mal. Ahora detecto desviaciones cada mes con el semáforo y corrijo a tiempo.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Isabel Campos', role: 'Directora financiera, cadena de restaurantes', text: 'El dashboard de ratios financieros con benchmarks del sector es exactamente lo que necesitaba para los comités de dirección. Food cost, labor cost, prime cost, GOP — todo automático.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Fernando Reyes', role: 'Chef emprendedor, primer restaurante', text: 'La calculadora de punto de equilibrio me abrió los ojos. Descubrí que necesitaba 45 cubiertos diarios a 22 EUR de ticket medio para ser rentable. Sin eso habría abierto a ciegas.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'María Herrero', role: 'Asesora fiscal especializada en hostelería', text: 'El cash flow forecast con alertas de liquidez es lo que más valoro. Mis clientes ahora ven 3 meses antes cuando van a tener tensión de tesorería. Prevenir es infinitamente más barato que curar.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Pablo Navarro', role: 'Inversor, 2 restaurantes + dark kitchen', text: 'El presupuesto CAPEX con desviación real vs presupuesto me evitó sorpresas en la obra. Cada partida controlada: cocina, mobiliario, tecnología, licencias. Sabía en todo momento cuánto me quedaba.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Daniel Ortiz', role: 'Director de operaciones, franquicia hostelera', text: 'El informe de viabilidad para bancos es impecable. TIR, VAN, payback period — todo calculado automáticamente. Nuestros franquiciados lo usan para conseguir financiación sin contratar consultores.', avatar: '/avatars/avatar-8.jpg' },
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
    { href: '/kit-gestion-personal', label: 'Kit Gestión Personal' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-plan-financiero',
    label: '¿Ya compraste el Kit Plan Financiero? Vuelve a entrar al dashboard',
  },
};

export default data;
