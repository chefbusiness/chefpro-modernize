import type { Locale } from '../i18n/config';

/**
 * Ruta de la página de precios por idioma. Antes vivía sólo dentro de
 * Header.astro; desde el CRO de la home (Keak, 20-sep-2026) la usan también el
 * hero («See plans & pricing») y la sección de Herramientas Business («See plans
 * that unlock all 6 tools»), así que se saca a un helper. Ver CRO_HOME_KEAK_2026-09-20.md.
 */
export const PRICING_PATHS: Record<Locale, string> = {
  es: '/precios',
  en: '/en/pricing',
  fr: '/fr/tarifs',
  de: '/de/preise',
  it: '/it/prezzi',
  pt: '/pt/precos',
  nl: '/nl/prijzen',
};

export function pricingHref(lang: Locale | string): string {
  return PRICING_PATHS[lang as Locale] ?? PRICING_PATHS.es;
}
