// astro-site/src/data/productos/planes/types.ts
// ---------------------------------------------------------------------------
// Tipo de datos de la LÍNEA PLANES (10 productos):
//   Sub-línea A "planes de negocio" (local fijo):
//     plan-negocio-bar-restaurante (REFERENCIA), plan-negocio-tapas-bar,
//     plan-negocio-cafeteria, plan-negocio-panaderia, plan-negocio-food-truck
//   Sub-línea B "planes de eventos" (itinerante):
//     plan-negocio-cocteleria-eventos, plan-negocio-parrillero-asador-eventos,
//     plan-negocio-paellero-eventos, plan-chef-privado-showcooking-eventos,
//     plan-catering-tematico-eventos
//
// VEREDICTO DEL DIFF (evidencia byte a byte, ver handoff): las dos "sub-líneas"
// A y B comparten un ESQUELETO DOM IDÉNTICO — el diff estructural entre bar-restaurante
// (A) y cocteleria-eventos (B), y entre productos dentro de cada sub-línea, es NULO:
// mismo orden de 18 secciones, mismo DOM de cada componente src/components/plan-*/*, mismos
// banners compartidos y los 3 JSON-LD (Product + FAQPage + BreadcrumbList). SOLO difiere el
// CONTENIDO (copy, iconos, imágenes, precios, env var Stripe, longitud de arrays). La única
// diferencia de DOM que varía POR PRODUCTO es el prefijo del H2 del CtaFinal ("...Hacer
// Realidad tu" en la sub-línea A vs "...Lanzar tu" en la B) + su palabra dorada.
// => UN SOLO TEMPLATE (PlanNegocioLandingPage.astro) sirve a las 10 landings.
//
// El template reproduce server-side y parametrizado por `data` la estructura EXACTA de la
// SPA de referencia src/pages/PlanNegocioBarRestaurante.tsx + src/components/
// plan-negocio-bar-restaurante/*. Idéntico scaffold/convenciones que KitExcelLandingPage.astro
// (Icon.astro, .kt-fade + IntersectionObserver, marquee testimonios rAF, AlreadyBought vanilla).
//
// ---------------------------------------------------------------------------
// CONSTANTES DE LÍNEA (hardcodeadas en el template, NO en data — idénticas en las 10):
//   · SaasDiscoveryBanner.
//   · CompatibleAppsMarquee — TODAS usan variant="tareas": título
//       'Imprime, Delega y <gold>Controla</gold>' + subtítulo
//       'Plantillas Excel optimizadas para imprimir en A4. Compatible con Excel, Google
//        Sheets, LibreOffice y Numbers' + las 9 apps (orden de shared/CompatibleAppsMarquee).
//   · ContentGrid  H2: 'Qué Incluye el <gold>Plan de Negocio</gold>'.
//   · Testimonials H2: 'Lo Que Dicen los <gold>Profesionales</gold>'.
//   · WhySection   H2: 'Por Qué Este <gold>Plan de Negocio</gold>'.
//   · AuthorSection: 'Creado por' / 'Chef John Guerrero' / chip dorado 'CEO AI Chef Pro'.
//   · BonusSection H2: 'Bonos <gold>Exclusivos</gold>'.
//   · FreeToolsSection (badge + H2 '8 Herramientas Profesionales Gratuitas' + 8 tarjetas).
//   · GuaranteeSection H2: 'Garantía de Satisfacción <gold>100%</gold>' (SIEMPRE acentuado).
//   · FaqAccordion H2: 'Preguntas <gold>Frecuentes</gold>'.
//   · WorldwideBanner / TryPlatformBanner / WhatsAppProductSupport.
//   · StickyBar: variante DOM única (px-3 max-w-screen-sm, <p text-xs truncate>, CTA 'COMPRAR').
//     (No hay la variante v1 de la línea Kits; la línea Planes usa siempre esta.)
//   · Hero badge: SIEMPRE tono gold (no hay variante 'red' en esta línea).
//   · ContentGrid: SIEMPRE grid-cols-2 md:grid-cols-3 (nunca 4 columnas).
//
// DIVERGENCIAS ENTRE PRODUCTOS (cubiertas por props; el resto = data pura):
//   1. CTA FINAL H2 → cta.headingPre + cta.headingGold (gold al final, sin post):
//        · sub-línea A: 'Es Hora de Hacer Realidad tu ' + <gold>{nicho}</gold>
//        · sub-línea B: 'Es Hora de Lanzar tu ' + <gold>{servicio}</gold>
//   2. HERO H1 → titlePre + <gold>titleGold</gold> + titlePost? (inline, opcional) +
//        titleSubtitle? (bloque <span class="block">). En la práctica todos los productos
//        usan titlePre + titleGold + titleSubtitle (Forma B); titlePost queda opcional por
//        robustez (ningún producto actual lo usa, se omite).
//   3. AUTHOR chips grises → authorBadges? (default ['Consultor Gastronómico',
//        '+29 años en alta hostelería'] = el de bar-restaurante; se sobrescribe VERBATIM si
//        algún producto trae otra pareja).
//   4. Longitud de arrays (hero.checkItems 5→9, grid.templates 9|11, bonus.items, etc.):
//        variable por producto — cada uno copia su array VERBATIM.
//
// QUIRKS VERBATIM (no son errores de transcripción — copiar tal cual la SPA):
//   · La línea mezcla símbolos de precio con formato '€35'/'€120' (sub-línea A y cocteleria)
//     — usar el símbolo EXACTO de cada producto.
//   · schema.faqs (JSON-LD FAQPage) suele ser un SUBCONJUNTO más corto que faqs on-page
//     (bar: 5 en el schema vs 6 en el acordeón). Copiar cada bloque según su origen en la SPA.
// ---------------------------------------------------------------------------

/** Nombre de icono lucide. Debe existir en Icon.astro; si falta, añadirlo
 *  extraído EXACTO de node_modules/lucide-react (misma versión, v0.462.0). */
export type IconName = string;

export interface PlanNegocioReview {
  author: string;
  rating: string; // "5"
  body: string;
}

export interface PlanNegocioFaq {
  q: string;
  a: string;
}

export interface PlanNegocioTemplateItem {
  icon: IconName;
  title: string;
  desc: string;
}

export interface PlanNegocioReason {
  icon: IconName;
  title: string;
  desc: string;
}

export interface PlanNegocioBonus {
  icon: IconName;
  label: string; // "BONUS 1"
  title: string;
  value: string; // "€19"
  desc: string;
  image: string; // /lovable-uploads/ai-gallery/....jpg
}

export interface PlanNegocioTestimonial {
  name: string;
  role: string;
  text: string;
  avatar: string; // /avatars/avatar-1.jpg (import → ruta pública en Astro)
}

export interface PlanNegocioPill {
  label: string;
  highlight?: boolean;
}

export interface PlanNegocioStat {
  number: string; // "30"
  label: string; // "Días de garantía"
}

export interface PlanNegocioFooterLink {
  href: string;
  label: string;
}

/** Precios de display (con símbolo tal cual la SPA: "€35"). Se repiten en
 *  hero / buyBox / bonus / cta. */
export interface PlanNegocioPricing {
  priceOld: string; // "€120"
  price: string; // "€35"
  discountBadge: string; // "-71%"
  heroNote: string; // hero: "Precio especial de lanzamiento. Sube pronto"
  buyBoxNote: string; // buyBox: "Precio especial de lanzamiento — 71 % de descuento"
  bonusTotalLabel: string; // "Valor total del pack completo"
  bonusSaveLine: string; // "¡Ahorra €85 HOY!"
}

export interface PlanNegocioData {
  /** slug de la ruta sin barra inicial: "plan-negocio-bar-restaurante". */
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
    price: string; // "35.00" (numérico string para offers.price)
    priceValidUntil: string; // "2026-12-31"
    aggregateRating: {
      ratingValue: string;
      reviewCount: string; // OJO: puede diferir del nº de reviews
      bestRating: string;
      worstRating: string;
    };
    reviews: PlanNegocioReview[];
    faqs: PlanNegocioFaq[]; // FAQPage — OJO: suele ser SUBCONJUNTO más corto que faqs on-page
    breadcrumbName: string; // nombre del item #2 del BreadcrumbList
  };

  // ---- Imágenes reutilizadas por varias secciones ----
  images: {
    /** hero bg (6). */
    gallery: string[];
    /** strip visible del ContentGrid (6). Difiere del hero en esta línea → obligatorio.
     *  Si un producto usa el mismo set que el hero, puede omitirse (cae en `gallery`). */
    gridGallery?: string[];
    whyBg: string; // fondo WhySection (opacity .04)
    buyBoxBg: string; // fondo BuyBox (opacity .06)
    ctaBg: string; // fondo CtaFinal (opacity .06)
  };

  // ---- Hero (badge SIEMPRE gold; H1 = titlePre + gold + titlePost? + titleSubtitle?) ----
  hero: {
    badge: string;
    titlePre: string; // texto antes del gold (incluye su espacio final si aplica)
    titleGold: string; // <span class="text-[#FFD700]">…</span>
    /** texto INLINE tras el gold (incluye su espacio inicial). Opcional (ningún producto lo usa hoy). */
    titlePost?: string;
    /** subtítulo en <span class="block …">. Todos los productos actuales lo llevan. */
    titleSubtitle?: string;
    description: string;
    checkItems: string[];
    ctaLabel: string; // "DESCARGAR PLAN DE NEGOCIO — €35"
  };

  // ---- Content grid (H2 constante 'Qué Incluye el Plan de Negocio'; solo varía subtítulo + tarjetas) ----
  grid: {
    subtitle: string;
    templates: PlanNegocioTemplateItem[];
  };

  // ---- Why (H2 constante 'Por Qué Este Plan de Negocio'; solo varía subtítulo/razones/compat) ----
  why: {
    subtitle: string;
    reasons: PlanNegocioReason[];
    compatLabel: string; // "Compatible con cualquier software ofimático:"
    compatPills: PlanNegocioPill[];
  };

  // ---- Author (heading/chip dorado constantes; solo bio + 2 chips grises varían) ----
  authorBio: string;
  /** Los DOS chips grises del AuthorSection (el chip dorado 'CEO AI Chef Pro' es constante).
   *  Default = el de bar-restaurante ['Consultor Gastronómico', '+29 años en alta hostelería']. */
  authorBadges?: [string, string];

  // ---- Bonus (H2 constante 'Bonos Exclusivos'; solo varía subtítulo + items) ----
  bonus: {
    subtitle: string;
    items: PlanNegocioBonus[];
  };

  // ---- Buy box ----
  buyBox: {
    ctaLabel: string; // "SÍ, QUIERO EL PLAN — €35"
  };

  // ---- Guarantee (H2 constante 'Garantía de Satisfacción 100%'; solo varía texto + stats) ----
  guarantee: {
    text: string;
    stats: PlanNegocioStat[];
  };

  // ---- FAQ on-page (acordeón). OJO: puede ser MÁS larga que schema.faqs. ----
  faqs: PlanNegocioFaq[];

  // ---- CTA final (H2 = headingPre + <gold>headingGold</gold>, la única divergencia de DOM por producto) ----
  cta: {
    headingPre: string; // "Es Hora de Hacer Realidad tu " (A) | "Es Hora de Lanzar tu " (B)
    headingGold: string; // "Bar-Restaurante" | "Barra Móvil de Coctelería"
    subtitle: string;
    items: string[];
    ctaLabel: string;
  };

  // ---- Testimonials (marquee). El título 'Lo Que Dicen los Profesionales' es constante. ----
  testimonials: {
    subtitle: string;
    items: PlanNegocioTestimonial[];
  };

  // ---- Precios de display ----
  pricing: PlanNegocioPricing;

  // ---- Sticky bar (móvil) ----
  stickyLabel: string; // "PLAN BAR-RESTAURANTE — €35"

  // ---- Footer + gate "¿Ya compraste?" ----
  footerLinks: PlanNegocioFooterLink[];
  alreadyBought: { product: string; label: string };
}
