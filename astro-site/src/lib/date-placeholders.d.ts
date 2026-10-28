export function madridCalendar(date: Date, locale?: string): { year: string; month: string };

/** Sustituye `{year}` y `{month}` (mes en `locale`). El resto de la cadena no cambia. */
export function resolveDatePlaceholders(str: string, now?: Date, locale?: string): string;

/** Sustituye los tokens en title, meta description, og:title, twitter:title, h1 y headline. */
export function applyDatePlaceholdersToHtml(html: string, now?: Date): string;

/** Campos SEO del HTML que aún contienen el placeholder literal. */
export function findUnresolvedSeoPlaceholders(html: string): string[];
