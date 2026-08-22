// types.ts — Contrato de datos de la LÍNEA GUÍAS "Cómo Montar" (guia-*).
// Captura TODO el copy variable de la página SPA de referencia
// src/pages/GuiaRestauranteGastronomico.tsx + sus 10 componentes de
// src/components/guia-restaurante-gastronomico/*. Lo CONSTANTE de la línea
// (labels fijos, garantía, badges de autor 1-2, orden de secciones) va literal
// en el template GuiaLandingPage.astro; aquí sólo lo que cambia entre productos.
//
// ── DIVERGENCIAS ESTRUCTURALES de la línea (cubiertas por props opcionales) ──
//  1. showCompatibleApps: sólo guia-dark-kitchen renderiza el <CompatibleAppsMarquee
//     variant="tareas" /> entre Hero y ContentGrid. Los otros 7 NO lo tienen.
//  2. bonus.layout: 'split' (7 productos con 5 bonus → fila de 3 + fila del resto) vs
//     'single' (guia-dark-kitchen con 3 bonus → una fila grid-cols-3 max-w-4xl). El DOM
//     de CADA tarjeta bonus es idéntico; sólo cambia(n) el/los grid contenedor(es).
//  3. schema.breadcrumb: array de 2 (dark-kitchen: AI Chef Pro → guía) o 3 ítems
//     (resto: AI Chef Pro → Productos Digitales → guía). Se emite tal cual, position=idx+1.
//  4. hero.avatarAltPrefix: 'Professional' (default, 7 productos) vs 'Panadero' (panaderia).
//  5. testimonials.titleGold: 'Profesionales' (7) vs 'Panaderos' (panaderia).
// El resto (Hero rojo, ContentGrid con num + lg:grid-cols-4, WhySection SIN subtítulo
// ni pills, AuthorSection label "Autor" + 3 chips, Guarantee 3 stats fijas) es idéntico
// en DOM para los 8: sólo cambia el copy que llega por `data`.

export interface GuiaData {
  /** Slug de la ruta SIN barra. Ej: 'guia-restaurante-gastronomico'. Canonical = SITE/slug. */
  slug: string;
  /** DOC: nombre EXACTO de la env var Stripe que el wrapper resuelve estáticamente.
   *  Ej: 'VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_GASTRONOMICO'. No se lee aquí. */
  stripeEnvKey: string;

  /** SEO → BaseLayout (title/description/keywords/ogImage). robots se OMITE (desviación
   *  cross-cutting sancionada). BaseLayout normaliza head (og:type=website, twitter card,
   *  og:image dims, hreflang es+x-default) igual que en el slice Tareas. */
  seo: {
    title: string;
    description: string;
    keywords: string;
    ogImage: string;
  };

  /** Sólo guia-dark-kitchen = true. Default false. */
  showCompatibleApps?: boolean;

  hero: {
    /** Badge ROJO (danger) del hero. */
    badge: string;
    /** H1: "{titlePre}<gold>{titleGold}</gold>" + bloque "{subtitleLine}". */
    titlePre: string;
    titleGold: string;
    subtitleLine: string;
    description: string;
    checkItems: string[];
    /** CTA del hero. Ej: 'COMPRAR GUÍA — 85 EUR'. */
    ctaLabel: string;
    /** alt de los 8 avatares: `{prefix} {i+1}`. Default 'Professional'; panaderia 'Panadero'. */
    avatarAltPrefix?: string;
  };

  /** Precios/rótulos monetarios compartidos por Hero, BuyBox, Bonus, CtaFinal. */
  pricing: {
    /** Opcional desde 2026-08-21: si se omite, el template no pinta precio tachado. */
    priceOld?: string;       // "220 EUR"  (line-through; mismo valor en hero y caja bonus)
    price: string;           // "85 EUR"
    discountBadge?: string;  // "-61%" (opcional: sin ancla no hay badge)
    heroNote: string;        // "Precio de lanzamiento — ahorra 135 EUR"
    buyBoxNote: string;      // nota del BuyBox (gastro = misma que heroNote)
    bonusTotalLabel: string; // "Valor total: guía + 5 bonus"
    bonusSaveLine?: string;  // "Ahorra 135 EUR HOY" (opcional)
  };

  images: {
    /** 6 imgs: fondo del hero (grid 3/6) Y galería de ContentGrid (mismas 6). */
    gallery: string[];
    whyBg: string;    // fondo tenue WhySection
    buyBoxBg: string; // fondo tenue BuyBox
    ctaBg: string;    // fondo tenue CtaFinal
  };

  /** ContentGrid — "N Capítulos + …" + galería + tarjetas de capítulo (num + icon). */
  grid: {
    countGold: string;   // "22"
    headingRest: string; // " Capítulos + 10 Plantillas + 8 Checklists + 2 Documentos"
    subtitle: string;
    chapters: { icon: string; num: string; title: string; desc: string }[];
  };

  testimonials: {
    /** Palabra dorada del H2 "Lo Que Dicen los <gold>{titleGold}</gold>". */
    titleGold: string;
    subtitle: string;
    /** avatar = ruta pública '/avatars/avatar-N.jpg'. */
    items: { name: string; role: string; text: string; avatar: string }[];
  };

  /** WhySection — H2 fijo "¿Por Qué Esta Guía?"; sólo varían las 4 razones. */
  why: {
    reasons: { icon: string; title: string; desc: string }[];
  };

  /** AuthorSection — label "Autor" fijo; badges 1-2 fijos (CEO AI Chef Pro / Consultor
   *  Gastronómico); sólo varían la bio y el 3er chip. */
  author: {
    bio: string;
    badge3: string; // "+200 aperturas"
  };

  bonus: {
    subtitle: string;            // "Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR"
    layout?: 'split' | 'single'; // default 'split' (5 bonus); 'single' para 3 bonus (dark-kitchen)
    items: { icon: string; label: string; title: string; value: string; desc: string; image: string }[];
  };

  buyBox: {
    ctaLabel: string; // "SÍ, QUIERO LA GUÍA — 85 EUR"
  };

  guarantee: {
    /** Sólo el párrafo varía; las 3 stats (30 / 100% / 0) son fijas en el template. */
    text: string;
  };

  /** FAQ en página (acordeón). OJO: distinto y más largo que schema.faqs (JSON-LD). */
  faqs: { q: string; a: string }[];

  cta: {
    heading: string;
    subtitle: string;
    items: string[];
    ctaLabel: string;
  };

  /** Rótulo de la barra sticky móvil. Ej: 'GUÍA RESTAURANTE GASTRONÓMICO — 85 EUR'. */
  stickyLabel: string;

  footerLinks: { label: string; href: string }[];

  alreadyBought: {
    product: string; // product EXACTO → /.netlify/functions/resend-access. Ej 'guia-restaurante-gastronomico'
    label: string;   // "¿Ya compraste la guía? Vuelve a entrar al dashboard"
  };

  /** JSON-LD ÍNTEGROS: Product (SIN review[] ni seller — la SPA de la línea NO los emite,
   *  a diferencia del slice Tareas) + FAQPage + BreadcrumbList. */
  schema: {
    productName: string;
    productDescription: string;
    price: string;          // "85.00"
    priceValidUntil: string; // "2026-12-31"
    /** Opcional desde 2026-08-21: sin sistema real de reseñas NO se emite (riesgo de acción
     *  manual de Google por reseñas autoeditadas). Si se omite, el Product schema va sin él. */
    aggregateRating?: { ratingValue: string; reviewCount: string; bestRating: string; worstRating: string };
    /** FAQPage (3 Q en gastro) — NO confundir con las faqs de la página. */
    faqs: { q: string; a: string }[];
    /** BreadcrumbList completo tal cual la SPA (2 o 3 ítems). position = índice + 1. */
    breadcrumb: { name: string; item: string }[];
  };

  /** Opcional (2026-08-18). Nota de vigencia bajo el precio del hero, p. ej.
   *  «Producto actualizado · Versión 2.0 · agosto 2026». Solo la pintan los kits que
   *  la definen; el resto no cambia. */
  updateNote?: string;
}
