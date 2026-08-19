import type { Locale } from '../i18n/config';
import { APP_URLS as SHARED_APP_URLS } from '../../../src/lib/app-urls';

/**
 * Helper de la plataforma (Pickaxe whitelabel) para el árbol Astro. El mapa
 * en sí vive en src/lib/app-urls.ts (compartido con el getAppUrl de los
 * islands; astro-site puede importar de la SPA pero no al revés).
 *
 * Historia: este mapeo estuvo copiado a mano en 15 componentes .astro y en
 * src/hooks/useLanguage.ts, con dos consecuencias medidas el 2026-08-08:
 *
 *  1. Las 7 páginas de precios NO lo usaban: tenían `const APP =
 *     'https://app.aichef.pro'` clavado en la línea 22. Resultado en producción:
 *     /it/prezzi emitía 11 enlaces de navegación a itapp.aichef.pro y los
 *     7 botones de COMPRA a la plataforma española. La página de mayor
 *     intención de compra del árbol italiano contradiciéndose a sí misma.
 *  2. Las copias del helper sólo mapeaban en/it/fr/de, así que `pt` y `nl`
 *     caían al default español. Se erradicaron las 14 copias restantes el
 *     2026-08-19, el día que John lanzó en Pickaxe las plataformas PT y NL
 *     localizadas.
 */
const APP_URLS: Record<Locale, string> = SHARED_APP_URLS;

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
