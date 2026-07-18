// astro-site/src/data/productos/kits/types.ts
// ---------------------------------------------------------------------------
// Tipo de datos de la LÍNEA KITS EXCEL (kit-escandallos, pack-appcc,
// kit-inventario, kit-gestion-personal, kit-plan-financiero).
//
// Producto de REFERENCIA: kit-escandallos (src/pages/KitEscandallos.tsx +
// src/components/kit-escandallos/*). El ORDEN de las 18 secciones + banners
// compartidos es IDÉNTICO a la línea Tareas (mismo scaffold en el template);
// solo divergen a nivel DOM cinco puntos, cubiertos con props opcionales y
// DOCUMENTADOS abajo (ver "DIVERGENCIAS ESTRUCTURALES").
//
// Para replicar un producto: rellena este objeto con el copy VERBATIM extraído de
// sus componentes React (src/components/<producto>/*) y su página
// src/pages/<Producto>.tsx. Ver INSTRUCCIONES DE EXTRACCIÓN en el handoff.
//
// ---------------------------------------------------------------------------
// DIVERGENCIAS ESTRUCTURALES entre productos de la línea (cubiertas por props):
//   1. HERO H1  → dos formas:
//        · Forma A (escandallos): {titlePre}<gold>{titleGold}</gold>{titlePost}  (post inline, sin subtítulo bloque)
//        · Forma B (appcc/inventario/gestion): {titlePre}<gold>{titleGold}</gold> + <span block>{titleSubtitle}</span>
//        · plan-financiero usa AMBAS (titlePost " para Restaurantes" + titleSubtitle).
//      → hero.titlePost? y hero.titleSubtitle? son opcionales; se renderiza lo que exista.
//   2. HERO BADGE tono: 'gold' (escandallos, appcc) | 'red' (inventario, gestion, plan). → hero.badgeTone.
//   3. CONTENT GRID columnas: escandallos usa lg:grid-cols-4 (11 tarjetas); el resto md:grid-cols-3 (9). → grid.fourCols.
//   4. GUARANTEE heading: acentuado "Garantía de Satisfacción " (escandallos, appcc) vs sin tildes
//      "Garantia de Satisfaccion " (inventario, gestion, plan). El gold "100%" es constante. → guarantee.headingPre.
//   5. STICKY BAR: dos variantes DOM:
//        · 'v1' (SOLO escandallos): px-4, <div><p text-sm></div>, CTA "COMPRAR AHORA" (px-6 whitespace-nowrap).
//        · 'v2' (resto): px-3 max-w-screen-sm, <p text-xs truncate>, CTA "COMPRAR" (px-5 flex-shrink-0).
//      → stickyVariant ('v1' | 'v2'). Default template = 'v2'.
//
// NOTA quirk-tildes: inventario / gestion-personal / plan-financiero están redactados
// mayormente SIN tildes (secciones), pero con MEZCLA (p.ej. sus hero.checkItems SÍ llevan
// tildes). No hay flag global "tilde-free": cada string se copia VERBATIM tal cual la SPA.
// ---------------------------------------------------------------------------

/** Nombre de icono lucide. Debe existir en Icon.astro; si falta, añadirlo
 *  extraído EXACTO de node_modules/lucide-react (misma versión, v0.462.0). */
export type IconName = string;

export interface KitExcelReview {
  author: string;
  rating: string; // "5"
  body: string;
}

export interface KitExcelFaq {
  q: string;
  a: string;
}

export interface KitExcelTemplateItem {
  icon: IconName;
  title: string;
  desc: string;
}

export interface KitExcelReason {
  icon: IconName;
  title: string;
  desc: string;
}

export interface KitExcelBonus {
  icon: IconName;
  label: string; // "BONUS 1"
  title: string;
  value: string; // "€27" / "9 EUR"
  desc: string;
  image: string; // /lovable-uploads/ai-gallery/....jpeg
}

export interface KitExcelTestimonial {
  name: string;
  role: string;
  text: string;
  avatar: string; // /avatars/avatar-1.jpg | /avatars/chef-avatar-1.jpg
}

export interface KitExcelPill {
  label: string;
  highlight?: boolean;
}

export interface KitExcelStat {
  number: string; // "30"
  label: string; // "Días de garantía"
}

export interface KitExcelFooterLink {
  href: string;
  label: string;
}

/** Precios de display (con símbolo/sufijo tal cual la SPA: "€12" o "14 EUR").
 *  Se repiten en hero / buybox / bonus / cta. */
export interface KitExcelPricing {
  priceOld: string; // "€49" / "49 EUR"
  price: string; // "€12" / "14 EUR"
  discountBadge: string; // "-75%"
  heroNote: string; // "Precio especial de lanzamiento. Sube pronto"
  buyBoxNote: string; // "Precio especial de lanzamiento — 75% de descuento"
  bonusTotalLabel: string; // "Valor total del kit completo" / "...del pack completo"
  bonusSaveLine: string; // "¡Ahorra €37 HOY!" / "Ahorra 35 EUR HOY"
}

export interface KitExcelData {
  /** slug de la ruta sin barra inicial: "kit-escandallos" → /kit-escandallos */
  slug: string;

  /** Nombre EXACTO de la env var del payment link Stripe (DINERO: byte a byte
   *  igual que la SPA). Se resuelve en el WRAPPER .astro con acceso ESTÁTICO
   *  —import.meta.env.VITE_STRIPE_PAYMENT_LINK_<X> || '#comprar'— para que Vite lo
   *  inline en build. Aquí solo se DOCUMENTA cuál es. */
  stripeEnvKey: string;

  // ---- SEO (→ BaseLayout vía wrapper .astro) ----
  seo: {
    title: string; // <title>
    description: string;
    keywords: string;
    ogImage: string; // URL absoluta: https://aichef.pro/og-....jpg
  };

  // ---- JSON-LD (Product + FAQPage + BreadcrumbList) ----
  schema: {
    productName: string;
    productDescription: string;
    price: string; // "12.00" (numérico string para offers.price)
    priceValidUntil: string; // "2026-12-31"
    aggregateRating: {
      ratingValue: string;
      reviewCount: string; // OJO: puede diferir del nº de reviews (SPA: 10 con 3 reviews)
      bestRating: string;
      worstRating: string;
    };
    reviews: KitExcelReview[];
    faqs: KitExcelFaq[]; // FAQPage — OJO: en esta línea SON MÁS CORTAS que las FAQ on-page
    breadcrumbName: string; // nombre del item #2 del BreadcrumbList
  };

  // ---- Imágenes reutilizadas por varias secciones ----
  images: {
    /** hero bg (6). */
    gallery: string[];
    /** strip visible del ContentGrid (6). En escandallos DIFIERE del hero → obligatorio.
     *  Si un producto usa el mismo set que el hero, puede omitirse (cae en `gallery`). */
    gridGallery?: string[];
    whyBg: string; // fondo WhySection (opacity .04)
    buyBoxBg: string; // fondo BuyBox (opacity .06)
    ctaBg: string; // fondo CtaFinal (opacity .06)
  };

  // ---- Hero ----
  hero: {
    /** tono del badge superior. 'gold' = escandallos/appcc · 'red' = inventario/gestion/plan. */
    badgeTone: 'gold' | 'red';
    badge: string;
    titlePre: string; // texto antes del gold (incluye su espacio final si aplica)
    titleGold: string; // <span class="text-[#FFD700]">…</span>
    /** texto INLINE tras el gold (incluye su espacio inicial). Forma A/plan-financiero. Opcional. */
    titlePost?: string;
    /** subtítulo en <span class="block …">. Forma B. Opcional (escandallos NO lo tiene). */
    titleSubtitle?: string;
    description: string;
    checkItems: string[];
    ctaLabel: string; // "COMPRAR AHORA — €12"
  };

  // ---- CompatibleAppsMarquee (título/subtítulo varían por variant kit/appcc/tareas;
  //      la lista de apps es CONSTANTE). Se guardan como HTML crudo porque el subtítulo
  //      de la variante 'kit' contiene un <a>. ----
  compatApps: {
    titleHtml: string; // p.ej. 'Compatible con las <span class="text-[#FFD700]">Herramientas</span> que Ya Usas'
    subtitleHtml: string;
  };

  // ---- Content grid ----
  grid: {
    countGold: string; // "11"  (número dorado inicial)
    headingRest: string; // " Plantillas Profesionales"
    subtitle: string;
    /** true → grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 (SOLO escandallos, 11 tarjetas).
     *  false/omitido → grid grid-cols-2 md:grid-cols-3 (9 tarjetas). */
    fourCols?: boolean;
    templates: KitExcelTemplateItem[];
  };

  // ---- Why ----
  why: {
    headingPre: string; // "¿Por Qué Este " / "¿Por Que Este " (varía tilde)
    headingGold: string; // "Kit" / "Pack"
    headingPost: string; // "?"
    subtitle: string;
    reasons: KitExcelReason[];
    compatLabel: string; // "Compatible con cualquier software de hojas de cálculo:" (varía tilde)
    compatPills: KitExcelPill[];
  };

  // ---- Author ----
  authorBio: string;
  /** Los DOS chips grises del AuthorSection (el chip dorado "CEO AI Chef Pro" es constante).
   *  Default = variante acentuada ['Consultor Gastronómico', '+29 años en alta hostelería']
   *  (= escandallos/appcc). inventario/gestion pasan la variante sin tildes; plan-financiero
   *  pasa ['Consultor Gastronomico', '+200 aperturas asesoradas']. */
  authorBadges?: [string, string];

  // ---- Bonus ----
  bonus: {
    headingPre: string; // "Bonos " (constante; se deja parametrizado por robustez)
    headingGold: string; // "Exclusivos"
    subtitle: string;
    items: KitExcelBonus[];
  };

  // ---- Buy box ----
  buyBox: {
    ctaLabel: string; // "SÍ, QUIERO EL KIT — €12"
  };

  // ---- Guarantee ----
  guarantee: {
    /** heading antes del gold "100%". Default "Garantía de Satisfacción " (acentuado).
     *  inventario/gestion/plan pasan "Garantia de Satisfaccion ". */
    headingPre?: string;
    text: string;
    stats: KitExcelStat[];
  };

  // ---- FAQ on-page (acordeón). OJO: más largas que schema.faqs. ----
  faqs: KitExcelFaq[];

  // ---- CTA final (heading en texto plano, sin gold) ----
  cta: {
    heading: string;
    subtitle: string;
    items: string[];
    ctaLabel: string;
  };

  // ---- Testimonials (marquee). El título "Lo Que Dicen los Profesionales" es constante. ----
  testimonials: {
    subtitle: string;
    items: KitExcelTestimonial[];
  };

  // ---- Precios de display ----
  pricing: KitExcelPricing;

  // ---- Sticky bar (móvil) ----
  stickyLabel: string; // "KIT ESCANDALLOS — €12"
  /** 'v1' = variante DOM antigua (SOLO escandallos) · 'v2' = variante actual (resto). Default 'v2'. */
  stickyVariant?: 'v1' | 'v2';

  // ---- Footer + gate "¿Ya compraste?" ----
  footerLinks: KitExcelFooterLink[];
  alreadyBought: { product: string; label: string };
}
