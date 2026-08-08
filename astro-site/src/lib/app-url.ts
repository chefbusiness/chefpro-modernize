import type { Locale } from '../i18n/config';

/**
 * URL de la plataforma (Pickaxe whitelabel) por idioma.
 *
 * FUENTE ÚNICA. Antes este mapeo estaba copiado a mano en 15 componentes .astro
 * y en src/hooks/useLanguage.ts, con dos consecuencias medidas el 2026-08-08:
 *
 *  1. Las 7 páginas de precios NO lo usaban: tenían `const APP =
 *     'https://app.aichef.pro'` clavado en la línea 22. Resultado en producción:
 *     /it/prezzi emitía 11 enlaces de navegación a itapp.aichef.pro y los
 *     7 botones de COMPRA a la plataforma española. La página de mayor
 *     intención de compra del árbol italiano contradiciéndose a sí misma.
 *  2. Las copias del helper sólo mapeaban en/it/fr/de, así que `pt` y `nl`
 *     caían al default español — pese a que ptapp.aichef.pro y
 *     nlapp.aichef.pro existen y responden (verificado con curl, 307).
 *
 * Los 7 subdominios están vivos. Ojo al matiz: sólo es/en/it están realmente
 * localizados (redirigen a /invitado, /guest y /ospite respectivamente);
 * fr/de/pt/nl responden en inglés sobre su propio subdominio.
 */
const APP_URLS: Record<Locale, string> = {
  es: 'https://app.aichef.pro',
  en: 'https://enapp.aichef.pro',
  fr: 'https://frapp.aichef.pro',
  de: 'https://deapp.aichef.pro',
  it: 'https://itapp.aichef.pro',
  pt: 'https://ptapp.aichef.pro',
  nl: 'https://nlapp.aichef.pro',
};

/** Devuelve la plataforma del idioma; cae al español si llega algo raro. */
export function appUrl(lang: Locale | string): string {
  return APP_URLS[lang as Locale] ?? APP_URLS.es;
}

/** CTA con UTM. `medium` distingue el origen (pricing, hero, banner…). */
export function appCtaUrl(
  lang: Locale | string,
  medium: string,
  content: string,
): string {
  return `${appUrl(lang)}/?utm_source=web&utm_medium=${medium}&utm_content=${content}`;
}
