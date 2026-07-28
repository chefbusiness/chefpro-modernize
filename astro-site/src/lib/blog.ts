// Fase 8B — Taxonomía destino y helpers del blog.
// Las categorías WP se consolidan aquí (los 2 glosarios se fusionan; la slug
// larga 'glosario-y-lexico-cientifico-culinario' se acorta a 'glosario' — el
// mapa 301 del subdominio traduce las archives viejas).
//
// Fase 8B.6 — La taxonomía pasa a estar INDEXADA POR IDIOMA. Cada idioma tiene
// su propia lista: el blog EN (enblog.aichef.pro) no es una traducción del ES,
// es contenido distinto con su propio árbol de URLs. Ojo con 'ai-chef-pro',
// que existe en ES y EN: NO colisionan porque (a) las rutas viven en árboles
// separados (/blog/categoria/… vs /en/blog/category/…) y (b) cada página filtra
// además por post.data.lang antes de agrupar. Nunca resolver una categoría sin
// pasar el idioma.
import { getCollection, type CollectionEntry } from 'astro:content';
import { DEFAULT_LOCALE, type Locale } from '../i18n/config';

export interface BlogCategory {
  slug: string;
  name: string;
  description: string;
}

const CATEGORIES_ES: BlogCategory[] = [
  {
    slug: 'ia-en-gastronomia',
    name: 'IA en Gastronomía',
    description:
      'Inteligencia artificial aplicada a restaurantes y hostelería: herramientas, comparativas, automatización y casos reales.',
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Guías, novedades y trucos para sacar el máximo partido a los agentes de IA culinarios de AI Chef Pro.',
  },
  {
    slug: 'libreria-de-prompts',
    name: 'Librería de Prompts',
    description:
      'Prompts profesionales listos para usar con los agentes de IA culinarios: por rol, por tarea y por tipo de negocio.',
  },
  {
    slug: 'tutoriales',
    name: 'Tutoriales y Técnica',
    description:
      'Técnica culinaria profesional y tutoriales paso a paso: elaboraciones, procesos y guías de cocina con IA.',
  },
  {
    slug: 'recetas',
    name: 'Recetas Profesionales',
    description:
      'Recetas de cocina profesional plato a plato: platos nacionales, alta cocina y elaboraciones creadas con los recetarios de IA de AI Chef Pro.',
  },
  {
    slug: 'glosario',
    name: 'Glosario Culinario',
    description:
      'Léxico científico y técnico de cocina profesional: términos, conceptos y definiciones con rigor.',
  },
];

// Fase 8B.6 — Taxonomía del blog EN. Solo 2 categorías: las 39 piezas que se
// migran de enblog.aichef.pro caen en una de ellas (ver fase8b6-en2md.py:133).
// Las descripciones son NATIVAS, no traducciones de las ES.
const CATEGORIES_EN: BlogCategory[] = [
  {
    slug: 'ai-in-gastronomy',
    name: 'AI in Gastronomy',
    description:
      'How artificial intelligence is reshaping professional kitchens: tools worth your time, honest comparisons, automation that survives a busy service and the numbers behind each decision.',
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Everything about the platform itself: walkthroughs of the culinary AI agents, what is new in each release and the workflows chefs and operators actually run with them.',
  },
];

/** Taxonomía por idioma. Los idiomas sin blog propio devuelven lista vacía. */
export const BLOG_CATEGORIES_BY_LANG: Partial<Record<Locale, BlogCategory[]>> = {
  es: CATEGORIES_ES,
  en: CATEGORIES_EN,
};

/** Categorías de un idioma (vacío si ese idioma aún no tiene blog). */
export const getCategories = (lang: Locale = DEFAULT_LOCALE): BlogCategory[] =>
  BLOG_CATEGORIES_BY_LANG[lang] ?? [];

/**
 * @deprecated Alias de compatibilidad = taxonomía ES. Usa `getCategories(lang)`:
 * a partir de 8B.6 hay más de un idioma y una lista plana miente.
 */
export const BLOG_CATEGORIES: BlogCategory[] = CATEGORIES_ES;

/** Resuelve una categoría DENTRO de su idioma (el slug solo es único por idioma). */
export const getCategory = (
  slug: string,
  lang: Locale = DEFAULT_LOCALE
): BlogCategory | undefined => getCategories(lang).find((c) => c.slug === slug);

// ─────────────────────────────────────────────────────────────────────────────
// Rutas del blog por idioma
//
// DECISIÓN (8B.6) — segmentos NATIVOS en inglés: /en/blog/category/{slug} y
// /en/blog/page/{n}, no el espejo literal /categoria//pagina/.
//   · El ES usa 'categoria'/'pagina' porque hereda el historial de WordPress:
//     hay 301 vivos en public/_redirects apuntando a /blog/categoria/… y esas
//     URLs ya están indexadas. Ahí no se toca nada.
//   · Las URLs EN son NUEVAS (enblog.aichef.pro solo tenía /{slug}; su mapa 301
//     se escribe ahora, así que no hay nada que preservar) y una URL inglesa con
//     la palabra 'categoria' es ruido para usuario y para el motor.
// Todo el que construya un enlace del blog debe usar estos helpers: son la única
// fuente de verdad del esquema de URLs por idioma.
// ─────────────────────────────────────────────────────────────────────────────
const ROUTE_SEGMENTS: Partial<Record<Locale, { category: string; page: string }>> = {
  es: { category: 'categoria', page: 'pagina' },
  en: { category: 'category', page: 'page' },
};
const segments = (lang: Locale) => ROUTE_SEGMENTS[lang] ?? ROUTE_SEGMENTS.en!;

/** Raíz del blog: '/blog' en ES (sin prefijo, paridad 1:1 con WP), '/{lang}/blog' en el resto. */
export const blogBase = (lang: Locale = DEFAULT_LOCALE): string =>
  lang === DEFAULT_LOCALE ? '/blog' : `/${lang}/blog`;

/** Ruta de un artículo. */
export const postPath = (slug: string, lang: Locale = DEFAULT_LOCALE): string =>
  `${blogBase(lang)}/${slug}`;

/** Ruta de la archive de una categoría. */
export const categoryPath = (slug: string, lang: Locale = DEFAULT_LOCALE): string =>
  `${blogBase(lang)}/${segments(lang).category}/${slug}`;

/** Ruta de la página n del listado (n<=1 → el hub, que NO tiene /page/1). */
export const listPagePath = (n: number, lang: Locale = DEFAULT_LOCALE): string =>
  n <= 1 ? blogBase(lang) : `${blogBase(lang)}/${segments(lang).page}/${n}`;

/** Home del idioma, para migas de pan (ES sin prefijo). */
export const homePath = (lang: Locale = DEFAULT_LOCALE): string =>
  lang === DEFAULT_LOCALE ? '/' : `/${lang}`;

export type BlogPost = CollectionEntry<'blog'>;

/** Slug público del post (basename del id — la carpeta de idioma no cuenta). */
export const postSlug = (post: BlogPost): string =>
  post.id.split('/').pop()!.replace(/\.md$/, '');

/** Posts publicados de un idioma, más recientes primero. */
export async function getPublishedPosts(lang: Locale = 'es'): Promise<BlogPost[]> {
  const posts = await getCollection(
    'blog',
    (p) => p.data.lang === lang && !p.data.draft
  );
  return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

/** Minutos de lectura estimados a partir del HTML/markdown del cuerpo. */
export function readingTime(body: string): number {
  const words = body
    .replace(/<[^>]+>/g, ' ')
    .split(/\s+/)
    .filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}

const MONTHS_ES = [
  'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
  'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
];

/** "17 de febrero de 2026" — sin depender del locale del runtime de build. */
export function formatDateEs(d: Date): string {
  return `${d.getUTCDate()} de ${MONTHS_ES[d.getUTCMonth()]} de ${d.getUTCFullYear()}`;
}

const MONTHS_EN = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December',
];

/** "February 17, 2026" — mismo criterio que formatDateEs: UTC, sin Intl. */
export function formatDateEn(d: Date): string {
  return `${MONTHS_EN[d.getUTCMonth()]} ${d.getUTCDate()}, ${d.getUTCFullYear()}`;
}

/** Fecha larga en el idioma del post (fallback: formato ES). */
export function formatDate(d: Date, lang: Locale = DEFAULT_LOCALE): string {
  return lang === 'en' ? formatDateEn(d) : formatDateEs(d);
}

export const POSTS_PER_PAGE = 24;
