// Lib de rutas para las 441 URLs de casos de uso (Fase 2 migración Astro).
//
// FUENTE ÚNICA DE VERDAD = los datos de la SPA. NO se copian textos: se importa
// ALL_USE_CASES cross-root por ruta relativa, EXACTAMENTE igual que hace
// translations.ts con los JSON de locales.
//   astro-site/src/lib/  ->  ../../../src/data/use-cases
//   ..      = astro-site/src
//   ../..   = astro-site
//   ../../.. = raíz del repo
import {
  ALL_USE_CASES,
  getUseCasesByType,
  hasNativeContent,
  type UseCase,
  type UseCaseType,
  type LangCode,
} from '../../../src/data/use-cases';
import { LOCALES, type Locale } from '../i18n/config';

// Re-export para que los componentes de contenido tengan una única superficie de import.
export { ALL_USE_CASES, getUseCasesByType, hasNativeContent };
export type { UseCase, UseCaseType, LangCode };

// ─────────────────────────────────────────────────────────────────────────────
// SEGMENTS — COPIADO VERBATIM de src/pages/UseCasePage.tsx (líneas ~23-31).
// URL segments per language. Mirrors App.tsx route definitions and useLanguage.ts.
// ─────────────────────────────────────────────────────────────────────────────
export const SEGMENTS: Record<string, { hub: string; role: string; concept: string; task: string; consultor: string; locale: string; hubLabel: string }> = {
  es: { hub: 'usos',             role: 'rol',    concept: 'concepto', task: 'tarea',   consultor: 'consultoria', locale: 'es-ES', hubLabel: 'Casos de uso' },
  en: { hub: 'use-cases',        role: 'role',   concept: 'concept',  task: 'task',    consultor: 'consultancy', locale: 'en-US', hubLabel: 'Use Cases' },
  fr: { hub: 'cas-d-usage',      role: 'role',   concept: 'concept',  task: 'tache',   consultor: 'conseil',     locale: 'fr-FR', hubLabel: 'Cas d’usage' },
  de: { hub: 'anwendungsfaelle', role: 'rolle',  concept: 'konzept',  task: 'aufgabe', consultor: 'beratung',    locale: 'de-DE', hubLabel: 'Anwendungsfälle' },
  it: { hub: 'casi-uso',         role: 'ruolo',  concept: 'concetto', task: 'compito', consultor: 'consulenza',  locale: 'it-IT', hubLabel: 'Casi d’uso' },
  pt: { hub: 'casos-uso',        role: 'funcao', concept: 'conceito', task: 'tarefa',  consultor: 'consultoria', locale: 'pt-PT', hubLabel: 'Casos de uso' },
  nl: { hub: 'use-cases',        role: 'rol',    concept: 'concept',  task: 'taak',    consultor: 'advies',      locale: 'nl-NL', hubLabel: 'Use cases' },
};

// ─────────────────────────────────────────────────────────────────────────────
// CONSULTOR_HUB — COPIADO VERBATIM de src/pages/UseCasePage.tsx (líneas ~34-42).
// Sub-hub Consultoría Gastro Pro: slug + nombre de marca por idioma.
// ─────────────────────────────────────────────────────────────────────────────
export const CONSULTOR_HUB: Record<string, { slug: string; name: string }> = {
  es: { slug: 'consultoria-gastro-pro',  name: 'Consultoría Gastro Pro' },
  en: { slug: 'gastro-consultancy-pro',  name: 'Gastro Consultancy Pro' },
  fr: { slug: 'conseil-gastro-pro',      name: 'Conseil Gastro Pro' },
  de: { slug: 'gastro-beratung-pro',     name: 'Gastro Beratung Pro' },
  it: { slug: 'consulenza-gastro-pro',   name: 'Consulenza Gastro Pro' },
  pt: { slug: 'consultoria-gastro-pro',  name: 'Consultoria Gastro Pro' },
  nl: { slug: 'gastro-advies-pro',       name: 'Gastro Advies Pro' },
};

// ─────────────────────────────────────────────────────────────────────────────
// Helpers de path
// ─────────────────────────────────────────────────────────────────────────────

/** Prefijo de idioma: '' para es (default locale sin prefijo), '/<lang>' para el resto. */
function langPrefix(lang: Locale): string {
  return lang === 'es' ? '' : `/${lang}`;
}

/** Segmento de tipo (rol/concepto/tarea/consultoria …) según type + idioma. */
function typeSegment(type: UseCaseType, lang: Locale): string {
  const seg = SEGMENTS[lang];
  const map: Record<UseCaseType, string> = {
    role: seg.role,
    concept: seg.concept,
    task: seg.task,
    consultor: seg.consultor,
  };
  return map[type];
}

/** Slug nativo por idioma con el MISMO fallback que la SPA: slug[lang] || slug.es. */
function ucSlug(uc: UseCase, lang: Locale): string {
  return uc.slug[lang as LangCode] || uc.slug.es;
}

/** Path de un spoke SIN dominio, con prefijo /<lang> salvo es.
 *  Ej: /usos/rol/propietario-restaurante · /en/use-cases/role/restaurant-owner */
export function useCasePath(uc: UseCase, lang: Locale): string {
  return `${langPrefix(lang)}/${SEGMENTS[lang].hub}/${typeSegment(uc.type, lang)}/${ucSlug(uc, lang)}`;
}

/** alternates para BaseLayout: path nativo del spoke en cada uno de los 7 idiomas. */
export function alternatesFor(uc: UseCase): Record<Locale, string> {
  const out = {} as Record<Locale, string>;
  for (const l of LOCALES) out[l] = useCasePath(uc, l);
  return out;
}

/** Path del hub principal de casos de uso. Ej: /usos · /en/use-cases */
export function hubPath(lang: Locale): string {
  return `${langPrefix(lang)}/${SEGMENTS[lang].hub}`;
}

/** alternates del hub principal en los 7 idiomas. */
export function hubAlternates(): Record<Locale, string> {
  const out = {} as Record<Locale, string>;
  for (const l of LOCALES) out[l] = hubPath(l);
  return out;
}

/** Path del sub-hub Consultoría Gastro Pro.
 *  Ej: /usos/consultoria-gastro-pro · /en/use-cases/gastro-consultancy-pro */
export function consultorHubPath(lang: Locale): string {
  return `${langPrefix(lang)}/${SEGMENTS[lang].hub}/${CONSULTOR_HUB[lang].slug}`;
}

/** alternates del sub-hub consultor en los 7 idiomas. */
export function consultorHubAlternates(): Record<Locale, string> {
  const out = {} as Record<Locale, string>;
  for (const l of LOCALES) out[l] = consultorHubPath(l);
  return out;
}

// ─────────────────────────────────────────────────────────────────────────────
// getStaticPaths de los catch-all [...rest]
// ─────────────────────────────────────────────────────────────────────────────

export interface SpokeParams {
  /** Parte de la URL DESPUÉS de /<lang?>/<hub>/ — puede contener barra.
   *  Spoke:         '<typeSegment>/<slug>'  ej. 'rol/propietario-restaurante'
   *  Hub consultor: '<CONSULTOR_HUB.slug>'  ej. 'consultoria-gastro-pro'          */
  rest: string;
}

/** Props que recibe el catch-all: o un spoke (uc) o el hub consultor. */
export type SpokeProps =
  | { uc: UseCase; consultorHub?: false }
  | { consultorHub: true };

/**
 * Rutas del catch-all /<lang?>/<hub>/[...rest] para un idioma.
 * Devuelve 62 entradas: 61 spokes (19 rol + 24 concepto + 8 tarea + 10 consultor)
 * + 1 hub consultor (ConsultoriaGastroProHubPage).
 *
 * El hub consultor se emite como `{ params: { rest: CONSULTOR_HUB[lang].slug }, props: { consultorHub: true } }`;
 * el catch-all discrimina por `props.consultorHub` (variante de SpokeProps) para renderizar
 * ConsultoriaGastroProHubPage en lugar de UseCasePageContent.
 *
 * Total del sitio = 7 idiomas × (1 hub principal + 62) = 7 × 63 = 441 URLs.
 */
export function spokeStaticPaths(lang: Locale): Array<{ params: SpokeParams; props: SpokeProps }> {
  const entries: Array<{ params: SpokeParams; props: SpokeProps }> = ALL_USE_CASES.map((uc) => ({
    params: { rest: `${typeSegment(uc.type, lang)}/${ucSlug(uc, lang)}` },
    props: { uc },
  }));
  entries.push({
    params: { rest: CONSULTOR_HUB[lang].slug },
    props: { consultorHub: true },
  });
  return entries;
}
