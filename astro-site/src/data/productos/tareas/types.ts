// astro-site/src/data/productos/tareas/types.ts
// ---------------------------------------------------------------------------
// Tipo de datos de la LÍNEA TAREAS (productos kit-tareas-*).
//
// La estructura de las ~11 secciones + los banners compartidos es IDÉNTICA entre
// productos (variante "lean" canónica = KitTareasAsador.tsx); solo cambian
// copy / props / imágenes / env var de Stripe. Este objeto captura TODO lo
// variable. El resto (banners SaaS/Worldwide/TryPlatform, marquee de apps,
// PaymentBadges, LogoBadge, WhatsApp, cabeceras "constantes") va literal en el
// template KitTareasLandingPage.astro.
//
// Para replicar un producto: rellena este objeto con el copy VERBATIM extraído de
// sus componentes React (src/components/kit-tareas-<x>/*) y su página
// src/pages/KitTareas<X>.tsx. Ver INSTRUCCIONES DE EXTRACCIÓN en el handoff.
// ---------------------------------------------------------------------------

/** Nombre de icono lucide. Debe existir en Icon.astro; si falta, añadirlo
 *  extraído EXACTO de node_modules/lucide-react (misma versión, v0.462.0). */
export type IconName = string;

export interface KitTareasReview {
  author: string;
  rating: string; // "5"
  body: string;
}

export interface KitTareasFaq {
  q: string;
  a: string;
}

export interface KitTareasTemplateItem {
  icon: IconName;
  title: string;
  desc: string;
}

export interface KitTareasReason {
  icon: IconName;
  title: string;
  desc: string;
}

export interface KitTareasBonus {
  icon: IconName;
  label: string; // "BONUS 1"
  title: string;
  value: string; // "€15"
  desc: string;
  image: string; // /lovable-uploads/ai-gallery/....jpg
}

export interface KitTareasTestimonial {
  name: string;
  role: string;
  text: string;
  avatar: string; // /avatars/avatar-1.jpg
}

export interface KitTareasPill {
  label: string;
  highlight?: boolean;
}

export interface KitTareasStat {
  number: string; // "30"
  label: string; // "Días de garantía"
}

export interface KitTareasFooterLink {
  href: string;
  label: string;
}

/** Precios de display (con símbolo €). Se repiten en hero / buybox / bonus / cta. */
export interface KitTareasPricing {
  priceOld: string; // "€69"
  price: string; // "€14"
  discountBadge: string; // "-80%"
  heroNote: string; // "Precio especial de lanzamiento. Sube pronto"
  buyBoxNote: string; // "Precio especial de lanzamiento — 80% de descuento"
  bonusTotalLabel: string; // "Valor total del pack completo"
  bonusSaveLine: string; // "¡Ahorra €55 HOY!"
}

export interface KitTareasData {
  /** slug de la ruta sin barra inicial: "kit-tareas-asador" → /kit-tareas-asador */
  slug: string;

  /** Nombre EXACTO de la env var del payment link Stripe (DINERO: byte a byte
   *  igual que la SPA). Se resuelve en el template: import.meta.env[stripeEnvKey] || '#comprar'. */
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
    price: string; // "14.00" (numérico string para offers.price)
    priceValidUntil: string; // "2026-12-31"
    aggregateRating: {
      ratingValue: string;
      reviewCount: string;
      bestRating: string;
      worstRating: string;
    };
    reviews: KitTareasReview[];
    faqs: KitTareasFaq[]; // FAQPage (OJO: puede diferir de las FAQ on-page)
    breadcrumbName: string; // nombre del item #2 del BreadcrumbList
  };

  // ---- Imágenes reutilizadas por varias secciones ----
  images: {
    /** hero bg (6). En Asador es la misma lista que el grid → gridGallery se omite. */
    gallery: string[];
    /** strip visible del ContentGrid (6). Solo cuando difiere del hero (Kit Tareas); si se omite, el template cae en `gallery`. */
    gridGallery?: string[];
    whyBg: string; // fondo WhySection
    buyBoxBg: string; // fondo BuyBox
    ctaBg: string; // fondo CtaFinal
  };

  // ---- Hero ----
  hero: {
    badge: string;
    titlePre: string; // "Kit de Tareas "
    titleGold: string; // "Recurrentes"
    subtitleLine: string; // "Asador / Parrilla y Horno Josper"
    description: string;
    checkItems: string[];
    ctaLabel: string; // "COMPRAR AHORA — €14"
  };

  // ---- Sticky bar (móvil) ----
  stickyLabel: string; // "KIT TAREAS ASADOR — €14"

  // ---- Content grid ----
  grid: {
    countGold: string; // "11"  (número dorado inicial)
    headingRest: string; // " Checklists Operativos para Asador"
    /** DIVERGENCIA ESTRUCTURAL (solo kit-tareas-hotel): su H2 tiene DOS números dorados
     *  ("46 Checklists en 15 Plantillas — 11 Departamentos"). Si se rellena, el template
     *  renderiza este HTML crudo (con sus <span class="text-[#FFD700]">…</span>) en vez de
     *  countGold+headingRest. Los 18 productos restantes lo dejan sin definir. */
    headingHtml?: string;
    subtitle: string;
    templates: KitTareasTemplateItem[];
  };

  // ---- Why ----
  why: {
    headingPre: string; // "¿Por Qué Este "
    headingGold: string; // "Kit"
    headingPost: string; // "?"
    subtitle: string;
    reasons: KitTareasReason[];
    compatLabel: string; // "Compatible con cualquier software de hojas de cálculo:"
    compatPills: KitTareasPill[];
  };

  // ---- Author (varía la bio) ----
  authorBio: string;
  /** Los DOS chips grises del AuthorSection (el chip dorado "CEO AI Chef Pro" es
   *  constante en toda la línea). Si se omite, el template usa la variante ACENTUADA
   *  ['Consultor Gastronómico', '+29 años en alta hostelería'] que usan ~17 productos.
   *  Productos con el quirk tilde-free (dark-kitchen, restaurante-creativo) pasan aquí
   *  la variante sin tildes VERBATIM de su AuthorSection.tsx. */
  authorBadges?: [string, string];

  // ---- Bonus ----
  bonus: {
    headingPre: string; // "Bonos "
    headingGold: string; // "Exclusivos"
    subtitle: string;
    items: KitTareasBonus[];
  };

  // ---- Buy box ----
  buyBox: {
    ctaLabel: string; // "SÍ, QUIERO EL KIT DE TAREAS ASADOR — €14"
  };

  // ---- Guarantee ----
  guarantee: {
    text: string;
    stats: KitTareasStat[];
  };

  // ---- FAQ on-page (acordeón) ----
  faqs: KitTareasFaq[];

  // ---- CTA final ----
  cta: {
    heading: string;
    subtitle: string;
    items: string[];
    ctaLabel: string;
  };

  // ---- Testimonials (marquee). El título es constante en el template. ----
  testimonials: {
    subtitle: string;
    items: KitTareasTestimonial[];
  };

  // ---- Precios de display ----
  pricing: KitTareasPricing;

  // ---- Footer + gate "¿Ya compraste?" ----
  footerLinks: KitTareasFooterLink[];
  alreadyBought: { product: string; label: string };

  /** Opcional (2026-08-18). Nota de vigencia bajo el precio del hero, p. ej.
   *  «Producto actualizado · Versión 2.0 · agosto 2026». Solo la pintan los kits que
   *  la definen; el resto no cambia. */
  updateNote?: string;
}
