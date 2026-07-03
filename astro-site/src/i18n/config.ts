export const SITE = 'https://aichef.pro';
export const DEFAULT_LOCALE = 'es' as const;
export const LOCALES = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as const;
export type Locale = (typeof LOCALES)[number];
