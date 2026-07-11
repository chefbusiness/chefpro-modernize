// i18n para los componentes .astro de la home.
//
// FUENTE ÚNICA DE VERDAD = los JSON de la SPA (src/i18n/locales/*.json).
// No se copian textos a mano: se importan por ruta relativa desde este directorio.
//   astro-site/src/i18n/  ->  ../../../src/i18n/locales/<lang>.json
//   ..      = astro-site/src
//   ../..   = astro-site
//   ../../.. = raíz del repo
import es from '../../../src/i18n/locales/es.json';
import en from '../../../src/i18n/locales/en.json';
import fr from '../../../src/i18n/locales/fr.json';
import de from '../../../src/i18n/locales/de.json';
import it from '../../../src/i18n/locales/it.json';
import pt from '../../../src/i18n/locales/pt.json';
import nl from '../../../src/i18n/locales/nl.json';

import { DEFAULT_LOCALE, type Locale } from './config';

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const DICTS: Record<Locale, any> = { es, en, fr, de, it, pt, nl };

// Resolución por dot-path. Soporta claves numéricas de objetos ("features.0")
// igual que hace react-i18next en la SPA.
// eslint-disable-next-line @typescript-eslint/no-explicit-any
function resolve(obj: any, path: string): any {
  return path.split('.').reduce((acc, k) => (acc == null ? undefined : acc[k]), obj);
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function lookup(lang: Locale, key: string): any {
  const dict = DICTS[lang] ?? DICTS[DEFAULT_LOCALE];
  const v = resolve(dict, key);
  if (v !== undefined) return v;
  // Fallback a español (idéntico comportamiento de fallbackLng: 'es' en la SPA)
  return resolve(DICTS[DEFAULT_LOCALE], key);
}

/** Traducción string. Devuelve la propia clave si no existe en ningún idioma. */
export function t(lang: Locale, key: string): string {
  const v = lookup(lang, key);
  return v === undefined || v === null ? key : String(v);
}

/** Traducción de arrays (p.ej. hero.business_types con returnObjects). */
export function tList(lang: Locale, key: string): string[] {
  const v = lookup(lang, key);
  return Array.isArray(v) ? (v as string[]) : [];
}

/** Traducción de arrays de objetos (equivalente a returnObjects: true en la SPA). */
export function tObjects<T = Record<string, unknown>>(lang: Locale, key: string): T[] {
  const v = lookup(lang, key);
  return Array.isArray(v) ? (v as T[]) : [];
}
