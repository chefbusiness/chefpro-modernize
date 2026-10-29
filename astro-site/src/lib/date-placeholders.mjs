/**
 * Placeholders de fecha para landings públicas, resueltos en build.
 *
 * Tokens explícitos (y solo esos):
 *   {year}  → año civil en Europe/Madrid
 *   {month} → nombre del mes en el idioma de la página
 *
 * No reescribe años ya escritos ni precios. `{yearly}`, `{Year}` o `{ year }`
 * se quedan como están.
 *
 * @param {string} str
 * @param {Date} [now]  Instantánea. Por defecto, el momento de la llamada.
 * @param {string} [locale]  Idioma de la página: es, en, fr, de, it, pt, nl
 *   (también acepta un tag BCP-47; se usa el subtag principal).
 * @returns {string}
 */
const LOCALE_MAP = {
  es: 'es-ES',
  en: 'en-US',
  fr: 'fr-FR',
  de: 'de-DE',
  it: 'it-IT',
  pt: 'pt-PT',
  nl: 'nl-NL',
};

const MADRID = 'Europe/Madrid';
const META_FIELD = /\b(?:name|property)\s*=\s*(["'])(description|og:title|og:description|twitter:title|twitter:description)\1/i;

/**
 * @param {string} [locale]
 * @returns {string}
 */
function intlLocale(locale) {
  const raw = (locale || 'es').trim();
  const primary = raw.toLowerCase().split('-')[0];
  return LOCALE_MAP[primary] || raw || 'es-ES';
}

/**
 * @param {Date} date
 * @param {string} [locale]
 * @returns {{ year: string, month: string }}
 */
export function madridCalendar(date, locale) {
  const parts = new Intl.DateTimeFormat(intlLocale(locale), {
    timeZone: MADRID,
    year: 'numeric',
    month: 'long',
  }).formatToParts(date);
  const year = parts.find((part) => part.type === 'year')?.value ?? '';
  const month = parts.find((part) => part.type === 'month')?.value ?? '';
  return { year, month };
}

/**
 * @param {string} str
 * @param {Date} [now]
 * @param {string} [locale]
 * @returns {string}
 */
export function resolveDatePlaceholders(str, now, locale = 'es') {
  if (typeof str !== 'string') return str;
  if (!str.includes('{year}') && !str.includes('{month}')) return str;
  const date = now instanceof Date && !Number.isNaN(now.getTime()) ? now : new Date();
  const { year, month } = madridCalendar(date, locale);
  let out = str;
  if (year) out = out.replaceAll('{year}', year);
  if (month) out = out.replaceAll('{month}', month);
  return out;
}

/**
 * @param {string} html
 * @returns {string}
 */
function localeFromHtml(html) {
  const match = html.match(/<html\b[^>]*\blang\s*=\s*(["'])([A-Za-z]{2,})(?:-[A-Za-z0-9]+)*\1/i);
  return match ? match[2] : 'es';
}

/**
 * @param {string} value
 * @returns {boolean}
 */
function hasToken(value) {
  return typeof value === 'string' && (value.includes('{year}') || value.includes('{month}'));
}

/**
 * Sustituye los tokens solo en los campos SEO del HTML ya generado:
 * `<title>`, meta description, `og:title`, `og:description`, `twitter:title`,
 * `twitter:description`, `<h1>` y `headline` de JSON-LD. El resto del cuerpo no se toca.
 *
 * @param {string} html
 * @param {Date} [now]
 * @returns {string}
 */
export function applyDatePlaceholdersToHtml(html, now) {
  if (typeof html !== 'string' || !hasToken(html)) return html;
  const locale = localeFromHtml(html);
  const apply = (value) => resolveDatePlaceholders(value, now, locale);

  let out = html.replace(/<title(\s[^>]*)?>([\s\S]*?)<\/title>/gi, (_, attrs = '', inner) => {
    return `<title${attrs}>${apply(inner)}</title>`;
  });

  out = out.replace(/<meta\b[^>]*>/gi, (tag) => {
    if (!META_FIELD.test(tag)) return tag;
    return tag.replace(
      /\bcontent\s*=\s*(["'])([\s\S]*?)\1/i,
      (_, quote, value) => `content=${quote}${apply(value)}${quote}`,
    );
  });

  out = out.replace(/<h1(\s[^>]*)?>([\s\S]*?)<\/h1>/gi, (_, attrs = '', inner) => {
    return `<h1${attrs}>${apply(inner)}</h1>`;
  });

  out = out.replace(/"headline"\s*:\s*"((?:\\.|[^"\\])*)"/g, (full, inner) => {
    let decoded;
    try {
      decoded = JSON.parse(`"${inner}"`);
    } catch {
      return full;
    }
    if (typeof decoded !== 'string' || !hasToken(decoded)) return full;
    return `"headline":${JSON.stringify(apply(decoded))}`;
  });

  return out;
}

/**
 * Campos SEO que todavía contienen `{year}` o `{month}`.
 * Sirve para fallar el build si el literal se ha colado.
 *
 * @param {string} html
 * @returns {string[]}
 */
export function findUnresolvedSeoPlaceholders(html) {
  if (typeof html !== 'string' || !hasToken(html)) return [];
  const found = [];
  const consider = (field, value) => {
    if (hasToken(value)) found.push(field);
  };

  for (const match of html.matchAll(/<title(?:\s[^>]*)?>([\s\S]*?)<\/title>/gi)) {
    consider('title', match[1]);
  }
  for (const match of html.matchAll(/<meta\b[^>]*>/gi)) {
    const tag = match[0];
    const kind = tag.match(META_FIELD);
    if (!kind) continue;
    const content = tag.match(/\bcontent\s*=\s*(["'])([\s\S]*?)\1/i);
    if (content) consider(kind[2].toLowerCase(), content[2]);
  }
  for (const match of html.matchAll(/<h1(?:\s[^>]*)?>([\s\S]*?)<\/h1>/gi)) {
    consider('h1', match[1]);
  }
  for (const match of html.matchAll(/"headline"\s*:\s*"((?:\\.|[^"\\])*)"/g)) {
    try {
      consider('headline', JSON.parse(`"${match[1]}"`));
    } catch {
      // JSON-LD malformado: no es un headline que podamos afirmar.
    }
  }
  return found;
}
