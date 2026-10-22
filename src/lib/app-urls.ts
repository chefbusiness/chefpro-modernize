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
 * Home del portal invitado. La raíz de cada subdominio (el CTA de cabecera,
 * utm_medium=header) redirige aquí y muestra el portal. Medido el 2026-10-22
 * con el HTML ya pintado: estas rutas tienen el texto de bienvenida; una ruta
 * de agente (`/gastro-lexicum` → `/invitado/gastro-lexicum`, y lo mismo en
 * `/guest` y `/ospite`) pinta «No content is available yet».
 *
 * itapp usa `/ospite`. El resto de idiomas no españoles usa `/guest`.
 */
export const GUEST_HOME_PATHS: Record<AppLang, string> = {
  es: '/invitado',
  en: '/guest',
  fr: '/guest',
  de: '/guest',
  it: '/ospite',
  pt: '/guest',
  nl: '/guest',
};

/** Ruta de la home de invitado del idioma; cae al español si llega algo raro. */
export function guestHomePath(lang: string): string {
  return GUEST_HOME_PATHS[lang as AppLang] ?? GUEST_HOME_PATHS.es;
}

/**
 * Enlace a la plataforma con el mismo esquema UTM que precios y el CTA del blog:
 * utm_source + utm_medium + utm_content.
 *
 * `path` solo puede ser `/` o la home de invitado de ese idioma.
 * `/` es la raíz del subdominio: la usa la cabecera y Pickaxe la redirige a la
 * home de invitado conservando los UTM. Cualquier otra ruta (slug de agente o
 * de categoría) se sustituye por esa home: el invitado no ve el agente y la
 * página sale vacía. Quien ya ha iniciado sesión lo reconoce Pickaxe al entrar
 * en la home.
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
  const guest = guestHomePath(lang);
  const requested = (path.startsWith('/') ? path : `/${path}`).replace(/\/+$/, '') || '/';
  const clean = requested === '/' || requested === guest ? requested : guest;
  const url = new URL(`${base}${clean === '/' ? '/' : clean}`);
  url.searchParams.set('utm_source', 'web');
  url.searchParams.set('utm_medium', medium);
  url.searchParams.set('utm_content', content);
  return url.toString();
}
