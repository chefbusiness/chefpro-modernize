/**
 * Registro de la TIENDA de productos digitales por idioma — ÚNICA fuente de verdad.
 * Plan canónico: scripts/productos-digitales/TIENDA-INTERNACIONAL.md §3.
 *
 * - ES conserva el patrón heredado en la RAÍZ (/kit-escandallos, /kit-escandallos-access,
 *   /kit-escandallos-library). No se toca: hay compras, emails y robots.txt atados a él.
 * - El resto de idiomas cuelgan del hub de su idioma: /en/digital-products/<slug>,
 *   /en/digital-products/<slug>/access y /en/digital-products/<slug>/library.
 *
 * ⚠️ Los `segmento` de aquí se REPITEN en dos sitios que no pueden importar este fichero:
 *   - el filtro del sitemap de astro.config.mjs (dashboards anidados fuera del sitemap);
 *   - robots.txt (dos Disallow por cada tienda ACTIVA que no sea ES).
 *   Gate que comprueba que los tres coinciden: python3 scripts/productos-digitales/tienda-gate.py
 */
import { LOCALES, type Locale } from '../i18n/config';

export interface Tienda {
  /** Ruta del hub de la tienda de ese idioma. */
  hubPath: string;
  /** Segmento de URL del hub (sin prefijo de idioma). */
  segmento: string;
  moneda: 'EUR' | 'USD';
  /** false = la tienda no existe todavía: nadie la enlaza y tiendaHref() devuelve null. */
  activa: boolean;
}

export const TIENDAS: Record<Locale, Tienda> = {
  es: { hubPath: '/productos-digitales', segmento: 'productos-digitales', moneda: 'EUR', activa: true },
  // EN activa desde la fase 0.C (24-sep-2026): el hub /en/digital-products existe.
  en: { hubPath: '/en/digital-products', segmento: 'digital-products', moneda: 'USD', activa: true },
  // FR/DE/IT/PT/NL activas desde el 24-sep-2026: hubs = copias traducidas del hub EN.
  fr: { hubPath: '/fr/produits-numeriques', segmento: 'produits-numeriques', moneda: 'EUR', activa: true },
  de: { hubPath: '/de/digitale-produkte', segmento: 'digitale-produkte', moneda: 'EUR', activa: true },
  it: { hubPath: '/it/prodotti-digitali', segmento: 'prodotti-digitali', moneda: 'EUR', activa: true },
  pt: { hubPath: '/pt/produtos-digitais', segmento: 'produtos-digitais', moneda: 'EUR', activa: true },
  nl: { hubPath: '/nl/digitale-producten', segmento: 'digitale-producten', moneda: 'EUR', activa: true },
};

/** Enlace al hub de la tienda del idioma, o null si ese idioma no tiene tienda activa
 *  (fr nunca enlaza a la tienda ES: sería mandar a un francés a un checkout en español). */
export function tiendaHref(lang: Locale | string): string | null {
  const t = TIENDAS[lang as Locale];
  return t && t.activa ? t.hubPath : null;
}

/** Texto del enlace a la tienda en Header/Footer (y sus gemelos React). Solo idiomas con tienda
 *  activa; el nombre coincide con el H1/breadcrumb del hub (regla: enlace = nombre del destino). */
export const TIENDA_NOMBRE: Partial<Record<Locale, string>> = {
  es: 'Productos Digitales',
  en: 'Digital Products',
  fr: 'Produits numériques',
  de: 'Digitale Produkte',
  it: 'Prodotti Digitali',
  pt: 'Produtos Digitais',
  nl: 'Digitale producten',
};

/** Idiomas con tienda activa, en el orden de LOCALES (el que usa BaseLayout para los hreflang). */
export function hubLocales(): Locale[] {
  return LOCALES.filter((l) => TIENDAS[l].activa);
}

/** lang → hubPath de cada tienda activa. Se pasa como `alternates` a BaseLayout en los 7 hubs:
 *  hreflang recíproco entre todos ellos + x-default al ES (DEFAULT_LOCALE). */
export function hubAlternates(): Partial<Record<Locale, string>> {
  const out: Partial<Record<Locale, string>> = {};
  for (const l of hubLocales()) out[l] = TIENDAS[l].hubPath;
  return out;
}

export type TiendaKind = 'landing' | 'access' | 'library';

/** Ruta de una página de producto. ES = patrón raíz heredado; resto = anidado bajo el hub. */
export function tiendaProductoPath(lang: Locale | string, slug: string, kind: TiendaKind = 'landing'): string {
  if (lang === 'es' || !TIENDAS[lang as Locale]) {
    return kind === 'landing' ? `/${slug}` : `/${slug}-${kind}`;
  }
  const base = `${TIENDAS[lang as Locale].hubPath}/${slug}`;
  return kind === 'landing' ? base : `${base}/${kind}`;
}

/** Un mismo producto en varios idiomas. `vivo: false` = reservado (slug decidido, página aún no
 *  publicada): no emite hreflang ni enlaces cruzados hasta que pase a true. */
export interface FamiliaProducto {
  familia: string;
  productos: Partial<Record<Locale, { slug: string; vivo: boolean }>>;
}

export const FAMILIAS: FamiliaProducto[] = [
  {
    familia: 'kit-escandallos',
    productos: {
      es: { slug: 'kit-escandallos', vivo: true },
      en: { slug: 'food-cost-templates', vivo: true },
    },
  },
  {
    familia: 'kit-inventario',
    productos: {
      es: { slug: 'kit-inventario', vivo: true },
      en: { slug: 'restaurant-inventory-templates', vivo: true },
    },
  },
  {
    familia: 'pack-appcc',
    productos: {
      es: { slug: 'pack-appcc', vivo: true },
      en: { slug: 'haccp-templates', vivo: true },
    },
  },
  {
    familia: 'kit-gestion-personal',
    productos: {
      es: { slug: 'kit-gestion-personal', vivo: true },
      en: { slug: 'restaurant-schedule-templates', vivo: true },
    },
  },
  {
    familia: 'kit-plan-financiero',
    productos: {
      es: { slug: 'kit-plan-financiero', vivo: true },
      en: { slug: 'restaurant-financial-plan-templates', vivo: true },
    },
  },
  {
    // Tienda EN (4-oct-2026): Food Truck Business Plan Kit (SPEC business-plans-en D1).
    familia: 'plan-negocio-food-truck',
    productos: {
      es: { slug: 'plan-negocio-food-truck', vivo: true },
      en: { slug: 'food-truck-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (4-oct-2026): Coffee Shop Business Plan Kit (SPEC business-plans-en D1).
    familia: 'plan-negocio-cafeteria',
    productos: {
      es: { slug: 'plan-negocio-cafeteria', vivo: true },
      en: { slug: 'coffee-shop-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (4-oct-2026): Restaurant Business Plan Kit (SPEC business-plans-en-2 D30).
    familia: 'plan-negocio-bar-restaurante',
    productos: {
      es: { slug: 'plan-negocio-bar-restaurante', vivo: true },
      en: { slug: 'restaurant-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (4-oct-2026): Bakery Business Plan Kit (SPEC business-plans-en-2 D30).
    familia: 'plan-negocio-panaderia',
    productos: {
      es: { slug: 'plan-negocio-panaderia', vivo: true },
      en: { slug: 'bakery-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (11-oct-2026): Bar Business Plan Kit (SPEC business-plans-en-3 D48).
    familia: 'plan-negocio-tapas-bar',
    productos: {
      es: { slug: 'plan-negocio-tapas-bar', vivo: true },
      en: { slug: 'bar-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (11-oct-2026): Catering Business Plan Kit (SPEC business-plans-en-4 D66).
    familia: 'plan-catering-tematico-eventos',
    productos: {
      es: { slug: 'plan-catering-tematico-eventos', vivo: true },
      en: { slug: 'catering-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (13-oct-2026): Mobile Bar Business Plan Kit (SPEC business-plans-en-5 D81).
    familia: 'plan-negocio-cocteleria-eventos',
    productos: {
      es: { slug: 'plan-negocio-cocteleria-eventos', vivo: true },
      en: { slug: 'mobile-bar-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (24-oct-2026): BBQ Catering Business Plan Kit (SPEC business-plans-en-6 D96). vivo: true en la rama, que
    // se fusiona cuando existe el Payment Link (mismo criterio que el Catering y el Mobile Bar Business Plan Kit).
    familia: 'plan-negocio-parrillero-asador-eventos',
    productos: {
      es: { slug: 'plan-negocio-parrillero-asador-eventos', vivo: true },
      en: { slug: 'bbq-catering-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (24-oct-2026): Paella Catering Business Plan Kit (SPEC business-plans-en-7 D114). vivo: true en la rama, que
    // se fusiona cuando existe el Payment Link (mismo criterio que el Catering, el Mobile Bar y el BBQ Catering Business Plan Kit).
    familia: 'plan-negocio-paellero-eventos',
    productos: {
      es: { slug: 'plan-negocio-paellero-eventos', vivo: true },
      en: { slug: 'paella-catering-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (25-oct-2026): Pizza Shop Business Plan Kit (SPEC business-plans-en-8 D133/D152). vivo: true en la rama, que
    // se fusiona cuando existe el Payment Link (mismo criterio que el Paella, el BBQ y el Mobile Bar Business Plan Kit).
    familia: 'plan-negocio-pizzeria',
    productos: {
      es: { slug: 'plan-negocio-pizzeria', vivo: true },
      en: { slug: 'pizza-shop-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (29-oct-2026): Taco Shop Business Plan Kit (SPEC business-plans-en-12 / plan-taqueria F1-camino §6). vivo: true en la
    // rama, que se fusiona cuando existe el Payment Link (mismo criterio que el resto de planes EN de la tienda).
    familia: 'plan-negocio-taqueria',
    productos: {
      es: { slug: 'plan-negocio-taqueria', vivo: true },
      en: { slug: 'taco-shop-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (29-oct-2026): Rotisserie Chicken Restaurant Business Plan Kit (SPEC business-plans-en-13 / plan-polleria F1-camino §6-§7). vivo: true en la
    // rama, que se fusiona cuando existe el Payment Link (mismo criterio que el resto de planes EN de la tienda).
    familia: 'plan-negocio-polleria',
    productos: {
      es: { slug: 'plan-negocio-polleria', vivo: true },
      en: { slug: 'rotisserie-chicken-restaurant-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (31-oct-2026): Sushi Restaurant Business Plan Kit (SPEC business-plans-en-14 / plan-sushi F1-camino §6-§7). vivo: true en la
    // rama, que se fusiona cuando existe el Payment Link (mismo criterio que el resto de planes EN de la tienda).
    familia: 'plan-negocio-sushi-bar',
    productos: {
      es: { slug: 'plan-negocio-sushi-bar', vivo: true },
      en: { slug: 'sushi-restaurant-business-plan', vivo: true },
    },
  },
  {
    // Hamburguesería Smash (31-oct-2026): ES vivo; Burger Restaurant Business Plan Kit (EN) reservado (vivo: false) hasta que nazca la edición inglesa.
    familia: 'plan-negocio-hamburgueseria',
    productos: {
      es: { slug: 'plan-negocio-hamburgueseria', vivo: true },
      en: { slug: 'burger-restaurant-business-plan', vivo: false },
    },
  },
  {
    // Tienda EN (27-oct-2026): Ice Cream Shop Business Plan Kit (SPEC business-plans-en-10 D186/D205). vivo: true en la rama,
    // que se fusiona cuando existe el Payment Link (mismo criterio que el Pizza Shop, el Paella y el BBQ Business Plan Kit).
    familia: 'plan-negocio-heladeria',
    productos: {
      es: { slug: 'plan-negocio-heladeria', vivo: true },
      en: { slug: 'ice-cream-shop-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (27-oct-2026): Wedding Venue Business Plan Kit (SPEC business-plans-en-9 D156/D176). vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que el Pizza Shop, el Ice Cream Shop y el BBQ Business Plan Kit).
    familia: 'plan-negocio-finca-eventos-bodas',
    productos: {
      es: { slug: 'plan-negocio-finca-eventos-bodas', vivo: true },
      en: { slug: 'wedding-venue-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (28-oct-2026): Coffee Cart Business Plan Kit (SPEC business-plans-en-11 D216). vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que el Pizza Shop, el Wedding Venue y el Ice Cream Shop Business Plan Kit).
    familia: 'plan-negocio-cafeteria-movil-eventos',
    productos: {
      es: { slug: 'plan-negocio-cafeteria-movil-eventos', vivo: true },
      en: { slug: 'coffee-cart-business-plan', vivo: true },
    },
  },
  {
    // Tienda EN (15-oct-2026): Food Cost + Menu Engineering Guide, primera guía de la tienda EN
    // (SPEC guia-food-cost-en D1). vivo: true en la rama, que se fusiona cuando existe el Payment Link.
    familia: 'guia-food-cost-ingenieria-menu',
    productos: {
      es: { slug: 'guia-food-cost-ingenieria-menu', vivo: true },
      en: { slug: 'food-cost-menu-engineering-guide', vivo: true },
    },
  },
  {
    // Tienda EN (17-oct-2026): How to Open a Pastry Shop, segunda guía de la tienda EN (SPEC guia-pasteleria-en D1).
    // vivo: true en la rama, que se fusiona cuando existe el Payment Link.
    familia: 'guia-pasteleria-obrador',
    productos: {
      es: { slug: 'guia-pasteleria-obrador', vivo: true },
      en: { slug: 'how-to-open-a-pastry-shop', vivo: true },
    },
  },
  {
    // Tienda EN (17-oct-2026): Restaurant Checklists Kit Pro, primer producto EN de la línea Tareas
    // (SPEC checklists-kit D1/D3). Gemelo del Kit de Tareas Recurrentes (restaurante casual, la ficha base
    // de la línea); las otras 19 verticales ES no tienen gemelo EN. vivo: true en la rama, que se fusiona
    // cuando existe el Payment Link (mismo criterio que la guía de pastelería).
    familia: 'kit-tareas',
    productos: {
      es: { slug: 'kit-tareas', vivo: true },
      en: { slug: 'restaurant-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (18-oct-2026): Bar Checklists Kit Pro, primer hermano vertical del Restaurant Checklists Kit
    // Pro (SPEC checklists-kit/bar D1-D4). Gemelo del Kit de Tareas para Bar. vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que el Restaurant Checklists Kit Pro).
    familia: 'kit-tareas-bar',
    productos: {
      es: { slug: 'kit-tareas-bar', vivo: true },
      en: { slug: 'bar-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (18-oct-2026): Coffee Shop Checklists Kit Pro, segundo hermano vertical del Restaurant Checklists
    // Kit Pro (SPEC checklists-kit/cafe D1-D4). Gemelo del Kit de Tareas para Cafetería. vivo: true en la rama, que
    // se fusiona cuando existe el Payment Link (mismo criterio que el Restaurant y el Bar Checklists Kit Pro).
    familia: 'kit-tareas-cafeteria',
    productos: {
      es: { slug: 'kit-tareas-cafeteria', vivo: true },
      en: { slug: 'coffee-shop-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (18-oct-2026): Catering Checklists Kit Pro, tercer hermano vertical del Restaurant Checklists Kit Pro
    // (SPEC checklists-kit/catering D1-D4). Gemelo del Kit de Tareas para Catering. vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que el Restaurant, el Bar y el Coffee Shop Checklists Kit Pro).
    familia: 'kit-tareas-catering',
    productos: {
      es: { slug: 'kit-tareas-catering', vivo: true },
      en: { slug: 'catering-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (18-oct-2026): Pizza Shop Checklists Kit Pro, cuarto hermano vertical del Restaurant Checklists Kit Pro
    // (SPEC checklists-kit/pizza D1-D4). Gemelo del Kit de Tareas para Pizzería. vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que el Restaurant, el Bar, el Coffee Shop y el Catering
    // Checklists Kit Pro).
    familia: 'kit-tareas-pizzeria',
    productos: {
      es: { slug: 'kit-tareas-pizzeria', vivo: true },
      en: { slug: 'pizza-shop-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (18-oct-2026): Burger Joint Checklists Kit Pro, quinto hermano vertical del Restaurant Checklists Kit
    // Pro (SPEC checklists-kit/burger D1-D4). Gemelo del Kit de Tareas para Hamburguesería. vivo: true en la rama, que
    // se fusiona cuando existe el Payment Link (mismo criterio que el Restaurant, el Bar, el Coffee Shop, el Catering y
    // el Pizza Shop Checklists Kit Pro).
    familia: 'kit-tareas-hamburgueseria',
    productos: {
      es: { slug: 'kit-tareas-hamburgueseria', vivo: true },
      en: { slug: 'burger-joint-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (18-oct-2026): Ghost Kitchen Checklists Kit Pro, sexto hermano vertical del Restaurant Checklists Kit
    // Pro (SPEC checklists-kit/ghost D1-D4). Gemelo del Kit de Tareas para Dark Kitchen. vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que el Restaurant, el Bar, el Coffee Shop, el Catering, el
    // Pizza Shop y el Burger Joint Checklists Kit Pro).
    familia: 'kit-tareas-dark-kitchen',
    productos: {
      es: { slug: 'kit-tareas-dark-kitchen', vivo: true },
      en: { slug: 'ghost-kitchen-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (24-oct-2026): Ice Cream Shop Checklists Kit Pro, séptimo hermano vertical del Restaurant Checklists Kit
    // Pro (SPEC checklists-kit/icecream D1-D4). Gemelo del Kit de Tareas Heladería. vivo: true en la rama, que se fusiona
    // cuando existe el Payment Link (mismo criterio que el Restaurant, el Bar, el Coffee Shop, el Catering, el Pizza
    // Shop, el Burger Joint y el Ghost Kitchen Checklists Kit Pro).
    familia: 'kit-tareas-heladeria',
    productos: {
      es: { slug: 'kit-tareas-heladeria', vivo: true },
      en: { slug: 'ice-cream-shop-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (27-oct-2026): Hotel Checklists Kit Pro, décimo hermano vertical del Restaurant Checklists Kit Pro (SPEC
    // checklists-kit/hotel D1-D4). Gemelo del Kit de Tareas Hotel Completo (/kit-tareas-hotel). vivo: true en la rama,
    // que se fusiona cuando existe el Payment Link (mismo criterio que los demás Checklists Kit Pro).
    familia: 'kit-tareas-hotel',
    productos: {
      es: { slug: 'kit-tareas-hotel', vivo: true },
      en: { slug: 'hotel-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (31-oct-2026): Taco Shop Checklists Kit Pro, undécimo hermano vertical del Restaurant Checklists Kit Pro
    // (SPEC checklists-kit/taco D1-D4). Gemelo del Kit de Tareas Recurrentes: Taquería Mexicana (/kit-tareas-taqueria).
    // vivo: true en la rama, que se fusiona cuando existe el Payment Link (mismo criterio que los demás Checklists Kit Pro).
    familia: 'kit-tareas-taqueria',
    productos: {
      es: { slug: 'kit-tareas-taqueria', vivo: true },
      en: { slug: 'taco-shop-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (2026-10-31): Food Truck Checklists Kit Pro, duodécimo hermano vertical del Restaurant Checklists Kit Pro y primero del molde PLANO
    // (SPEC checklists-kit/foodtruck D1-D4, $15). Gemelo del Kit de Tareas Recurrentes: Food Truck (/kit-tareas-food-truck).
    // vivo: true en la rama, que se fusiona cuando existe el Payment Link (mismo criterio que los demás Checklists Kit Pro).
    familia: 'kit-tareas-food-truck',
    productos: {
      es: { slug: 'kit-tareas-food-truck', vivo: true },
      en: { slug: 'food-truck-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (2026-10-31): Bakery Checklists Kit Pro, decimotercer hermano vertical del Restaurant Checklists Kit Pro y segundo del molde PLANO
    // (SPEC checklists-kit/bakery D1-D4, $15). Gemelo del Kit de Tareas Recurrentes: Panadería / Obrador (/kit-tareas-panaderia).
    // vivo: true en la rama, que se fusiona cuando existe el Payment Link (mismo criterio que los demás Checklists Kit Pro).
    familia: 'kit-tareas-panaderia',
    productos: {
      es: { slug: 'kit-tareas-panaderia', vivo: true },
      en: { slug: 'bakery-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (2026-10-31): Seafood Restaurant Checklists Kit Pro, decimocuarto hermano vertical del Restaurant Checklists Kit Pro y tercero y último del molde PLANO
    // (SPEC checklists-kit/seafood D1-D4, $15). Gemelo del Kit de Tareas Recurrentes: Marisquería con Vivero y APPCC (/kit-tareas-marisqueria).
    // vivo: true en la rama, que se fusiona cuando existe el Payment Link (mismo criterio que los demás Checklists Kit Pro).
    familia: 'kit-tareas-marisqueria',
    productos: {
      es: { slug: 'kit-tareas-marisqueria', vivo: true },
      en: { slug: 'seafood-restaurant-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (2026-10-31): Fine Dining Checklists Kit Pro, decimoquinto hermano vertical del Restaurant Checklists Kit Pro y molde v2.0 híbrido como el hotel
    // (SPEC checklists-kit/finedining D1-D4, $19). Gemelo del Kit de Tareas Recurrentes: Restaurante Creativo / De Autor (/kit-tareas-restaurante-creativo).
    // vivo: true en la rama, que se fusiona cuando existe el Payment Link (mismo criterio que los demás Checklists Kit Pro).
    familia: 'kit-tareas-restaurante-creativo',
    productos: {
      es: { slug: 'kit-tareas-restaurante-creativo', vivo: true },
      en: { slug: 'fine-dining-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (24-oct-2026): Chocolate Shop Checklists Kit Pro, octavo hermano vertical del Restaurant Checklists Kit
    // Pro (SPEC checklists-kit/chocolate D1-D4). Gemelo del Kit de Tareas Chocolatería. vivo: true en la rama, que se
    // fusiona cuando existe el Payment Link (mismo criterio que los siete hermanos anteriores).
    familia: 'kit-tareas-chocolateria',
    productos: {
      es: { slug: 'kit-tareas-chocolateria', vivo: true },
      en: { slug: 'chocolate-shop-checklist-templates', vivo: true },
    },
  },
  {
    // Tienda EN (24-oct-2026): Pastry Shop Checklists Kit Pro, noveno hermano vertical (SPEC checklists-kit/pastry
    // D1-D4). Gemelo del Kit de Tareas Pastelería. vivo: true en la rama, que se fusiona con el Payment Link y con los 15
    // xlsx de la F2 en dl/ (mismo criterio).
    familia: 'kit-tareas-pasteleria',
    productos: {
      es: { slug: 'kit-tareas-pasteleria', vivo: true },
      en: { slug: 'pastry-shop-checklist-templates', vivo: true },
    },
  },
  {
    // ES con el patrón heredado: landing /pro-prompts-ebook, gate /pro-prompts-library-access y
    // dashboard /pro-prompts-library (quirk documentado en zona-app.ts). Aquí solo cuenta la
    // landing, que es lo único que usa alternatesFamilia(); los slugs de acceso no salen de aquí.
    familia: 'pro-prompts-ebook',
    productos: {
      es: { slug: 'pro-prompts-ebook', vivo: true },
      en: { slug: 'ai-prompts-for-restaurants', vivo: true },
    },
  },
];

/** hreflang de la landing de una familia: SOLO los idiomas con producto vivo. Mientras EN no
 *  esté vivo, las páginas ES reciben exactamente locales ['es'] y alternates vacío → su HTML
 *  no cambia. Uso: <BaseLayout locales={r.locales} alternates={r.alternates} …>. */
export function alternatesFamilia(familia: string): {
  locales: Locale[];
  alternates: Partial<Record<Locale, string>>;
} {
  const f = FAMILIAS.find((x) => x.familia === familia);
  const locales: Locale[] = [];
  const alternates: Partial<Record<Locale, string>> = {};
  if (!f) return { locales, alternates };
  for (const [lang, p] of Object.entries(f.productos) as [Locale, { slug: string; vivo: boolean }][]) {
    if (!p || !p.vivo) continue;
    locales.push(lang);
    // Con un solo idioma vivo no hay a quién apuntar: sin override (BaseLayout usa basePath).
    alternates[lang] = tiendaProductoPath(lang, p.slug, 'landing');
  }
  if (locales.length < 2) return { locales, alternates: {} };
  return { locales, alternates };
}
