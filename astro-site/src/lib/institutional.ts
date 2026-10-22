// Rutas institucionales con slug NATIVO por mercado. No son calcos del español:
// el segmento sale de cómo se nombra la página en ese idioma (kontakt, contatti,
// vragen, a-propos), y BaseLayout antepone el prefijo de idioma salvo en es.
//
// El hreflang es recíproco: las siete URLs de una misma pieza se declaran en
// todas. El contenido está localizado (moneda EUR, normativa, tono), pero la
// intención de la página es la misma, así que el par es verdadero.
import { DEFAULT_LOCALE, LOCALES, type Locale } from '../i18n/config';

export type InstitutionalKey = 'contact' | 'faq' | 'about' | 'training';

/** Ruta absoluta (con prefijo de idioma salvo es). */
export const INSTITUTIONAL_PATHS: Record<InstitutionalKey, Record<Locale, string>> = {
  contact: {
    es: '/contacto',
    en: '/en/contact',
    fr: '/fr/contact',
    de: '/de/kontakt',
    it: '/it/contatti',
    pt: '/pt/contacto',
    nl: '/nl/contact',
  },
  faq: {
    es: '/faq',
    en: '/en/faq',
    fr: '/fr/questions-frequentes',
    de: '/de/haeufige-fragen',
    it: '/it/domande-frequenti',
    pt: '/pt/perguntas-frequentes',
    nl: '/nl/veelgestelde-vragen',
  },
  about: {
    es: '/sobre-nosotros',
    en: '/en/about',
    fr: '/fr/a-propos',
    de: '/de/ueber-uns',
    it: '/it/chi-siamo',
    pt: '/pt/sobre',
    nl: '/nl/over-ons',
  },
  training: {
    es: '/formacion-presencial',
    en: '/en/in-person-ai-training',
    fr: '/fr/formation-ia-restauration',
    de: '/de/praesenzschulung-ki-gastronomie',
    it: '/it/formazione-ia-ristorazione',
    pt: '/pt/formacao-ia-restauracao',
    nl: '/nl/ai-training-horeca',
  },
};

/**
 * Hubs de prompts de fr/de/it/pt/nl. El plural evita el filtro del sitemap que
 * excluye cualquier ruta de un solo segmento acabada en `-library` (dashboards
 * de pago). ES (`/libreria-de-prompts`) y EN (`/en/prompt-libraries`) NO entran
 * en este mapa: su catálogo publicado es distinto (decisión ya documentada en
 * la página inglesa) y un hreflang entre un índice de 26 librerías y una
 * puerta de entrada sería falso.
 */
export const PROMPT_HUB_PATHS = {
  fr: '/fr/bibliotheques-de-prompts',
  de: '/de/prompt-bibliotheken',
  it: '/it/librerie-di-prompt',
  pt: '/pt/bibliotecas-de-prompts',
  nl: '/nl/promptbibliotheken',
} as const;

export type PromptHubLocale = keyof typeof PROMPT_HUB_PATHS;

export const alternatesFor = (key: InstitutionalKey): Record<Locale, string> =>
  INSTITUTIONAL_PATHS[key];

/** basePath que espera BaseLayout: sin el prefijo /en|/fr|… */
export function basePathFor(key: InstitutionalKey, lang: Locale): string {
  const full = INSTITUTIONAL_PATHS[key][lang];
  if (lang === DEFAULT_LOCALE) return full;
  const stripped = full.replace(new RegExp(`^/${lang}`), '');
  return stripped || '/';
}

export function promptHubBasePath(lang: PromptHubLocale): string {
  return PROMPT_HUB_PATHS[lang].replace(new RegExp(`^/${lang}`), '');
}

export const PROMPT_HUB_LOCALES = ['fr', 'de', 'it', 'pt', 'nl'] as const;

export function formacionHref(lang: Locale): string {
  return INSTITUTIONAL_PATHS.training[lang];
}

/** Todos los idiomas, para el prop `locales` de BaseLayout. */
export const ALL_LOCALES: readonly Locale[] = LOCALES;
