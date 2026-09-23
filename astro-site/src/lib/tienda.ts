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
import type { Locale } from '../i18n/config';

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
  // Reservados (sin fecha). Se fijan ya para que ningún slug nuevo los pise.
  fr: { hubPath: '/fr/produits-numeriques', segmento: 'produits-numeriques', moneda: 'EUR', activa: false },
  de: { hubPath: '/de/digitale-produkte', segmento: 'digitale-produkte', moneda: 'EUR', activa: false },
  it: { hubPath: '/it/prodotti-digitali', segmento: 'prodotti-digitali', moneda: 'EUR', activa: false },
  pt: { hubPath: '/pt/produtos-digitais', segmento: 'produtos-digitais', moneda: 'EUR', activa: false },
  nl: { hubPath: '/nl/digitale-producten', segmento: 'digitale-producten', moneda: 'EUR', activa: false },
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
};

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
      en: { slug: 'recipe-costing-kit', vivo: false },
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
