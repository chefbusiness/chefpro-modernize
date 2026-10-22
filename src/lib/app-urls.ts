/**
 * URL de la plataforma (Pickaxe whitelabel) por idioma — FUENTE ÚNICA REAL.
 *
 * Vive aquí (SPA) y no en astro-site/ porque la dependencia sólo puede ir en
 * ese sentido: astro-site importa fuentes de la SPA (igual que hace con
 * src/i18n/locales/*.json), pero la SPA no puede importar de astro-site.
 * Consumidores: astro-site/src/lib/app-url.ts (helper appUrl/appCtaUrl de
 * todo el árbol Astro) y src/hooks/useLanguage.ts (getAppUrl de los islands).
 *
 * Los 7 subdominios están vivos y LOCALIZADOS (verificado en vivo el
 * 2026-08-19: cada uno sirve su html lang y su UI traducida — ptapp
 * «Experimente grátis», nlapp «Probeer het gratis»). PT y NL los lanzó John
 * en Pickaxe ese mismo día. Ojo: el path del redirect de la raíz NO es prueba
 * de localización — app→/invitado e itapp→/ospite, pero enapp/frapp/deapp/
 * ptapp/nlapp van todos a /guest; para verificar hay que mirar el contenido.
 */
export const APP_URLS = {
  es: 'https://app.aichef.pro',
  en: 'https://enapp.aichef.pro',
  fr: 'https://frapp.aichef.pro',
  de: 'https://deapp.aichef.pro',
  it: 'https://itapp.aichef.pro',
  pt: 'https://ptapp.aichef.pro',
  nl: 'https://nlapp.aichef.pro',
} as const;

export type AppLang = keyof typeof APP_URLS;

/**
 * Enlace a la plataforma con el mismo esquema UTM que precios y el CTA del blog:
 * utm_source + utm_medium + utm_content. `path` es la ruta dentro del subdominio
 * (por defecto la raíz).
 *
 * Sin cross-domain linker. aichef.pro y los subdominios *app comparten dominio
 * registrable: gtag guarda `_gcl_aw` en `.aichef.pro` y el subdominio la lee
 * sola (GoogleTag.astro). Añadir `linker` reescribiría el clic y puede pisar
 * esa cookie. Estas URLs solo añaden query string; no tocan gtag ni el banner.
 */
export function appCtaUrl(
  lang: string,
  medium: string,
  content: string,
  path = '/',
): string {
  const base = (APP_URLS[lang as AppLang] ?? APP_URLS.es).replace(/\/$/, '');
  const clean = path.startsWith('/') ? path : `/${path}`;
  const url = new URL(`${base}${clean === '/' ? '/' : clean}`);
  url.searchParams.set('utm_source', 'web');
  url.searchParams.set('utm_medium', medium);
  url.searchParams.set('utm_content', content);
  return url.toString();
}
