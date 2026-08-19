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
  {
    // 8C — Las librerías de prompts por agente. El ES las tiene bajo
    // 'libreria-de-prompts'; en EN el segmento es nativo, no una traducción
    // literal del slug español.
    slug: 'prompt-library',
    name: 'Prompt Library',
    description:
      'Ready-to-use prompt libraries for every AI Chef Pro agent: copy them, adapt them to your operation and get straight to a usable answer instead of staring at a blank chat.',
  },
];

// 2026-08-08 — Blog ITALIANO. Arranca en 0 posts, así que la taxonomía nace
// deliberadamente MÁS CORTA que la española (6 categorías) y algo más ancha que
// la inglesa (3): cuatro cajas que se corresponden con los clústeres que dio el
// keyword research de Google.it, sin fragmentar un blog que aún no tiene con qué
// llenarlas. El hub sólo pinta las categorías que YA tienen posts, así que una
// caja vacía no ensucia nada mientras se llena.
//
// No hay 'glosario' a propósito: en español son 69 posts que vienen del
// histórico de WordPress, no una decisión editorial que replicar de cero.
const CATEGORIES_IT: BlogCategory[] = [
  {
    slug: 'ia-in-gastronomia',
    name: 'IA in Gastronomia',
    description:
      'Come l’intelligenza artificiale sta cambiando le cucine professionali: strumenti che valgono il tuo tempo, confronti onesti, automazioni che reggono un servizio pieno e i numeri dietro ogni decisione.',
  },
  {
    slug: 'gestione-ristorante',
    name: 'Gestione Ristorante',
    description:
      'Il mestiere che non si vede dalla sala: food cost e schede tecniche, margini, HACCP e allergeni, personale, fornitori e tutto quello che decide se il locale chiude l’anno in utile.',
  },
  {
    slug: 'tecnica-e-ricette',
    name: 'Tecnica e Ricette',
    description:
      'Tecnica di cucina professionale spiegata per chi la usa in servizio: cotture, fermentazioni, impasti, mise en place e ricette pensate per essere replicate in brigata, non per la fotografia.',
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Tutto sulla piattaforma: guide agli agenti IA culinari, novità di ogni rilascio e i flussi di lavoro che chef e gestori ci fanno girare davvero ogni giorno.',
  },
];

// 2026-08-16 — Blog FRANCÉS. Mismo criterio que el italiano: nace con 0 posts y
// CUATRO cajas, una por clúster del keyword research de Google.fr
// (ROADMAP_BLOG_FRANCES.md: 6 clústeres medidos, ~185 keywords y 40 SERP), no
// una traducción de la taxonomía española. El hub sólo pinta las categorías que
// YA tienen posts, así que una caja vacía no ensucia nada mientras se llena.
//
// Tampoco hay 'glossaire': los 69 posts de glosario del ES vienen del histórico
// de WordPress, no de una decisión editorial que replicar de cero.
//
// Las descripciones son FRANCÉS NATIVO (redactadas sobre el research, no
// traducidas del ES ni del IT). Apóstrofo RECTO a propósito: es la convención
// del francés de este repo (src/i18n/locales/fr.json usa 566 rectos y 0
// tipográficos), así que las cadenas van entre comillas dobles.
const CATEGORIES_FR: BlogCategory[] = [
  {
    slug: 'ia-en-gastronomie',
    name: 'IA en Gastronomie',
    description:
      "Comment l'intelligence artificielle transforme les cuisines professionnelles : des outils qui méritent votre temps, des comparatifs honnêtes, des automatisations qui tiennent un service complet et les chiffres derrière chaque décision.",
  },
  {
    slug: 'gestion-restaurant',
    name: 'Gestion de Restaurant',
    description:
      "Le métier qu'on ne voit pas depuis la salle : food cost et fiches techniques, marges, HACCP et allergènes, équipe, fournisseurs et tout ce qui décide si l'établissement finit l'année dans le vert.",
  },
  {
    slug: 'technique-et-recettes',
    name: 'Technique et Recettes',
    description:
      "La technique de cuisine professionnelle expliquée pour ceux qui l'utilisent en service : cuissons, fermentations, tailles de découpe, mise en place et des recettes pensées pour être reproduites en brigade, pas pour la photo.",
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Tout sur la plateforme : guides des agents IA culinaires, nouveautés de chaque version et les flux de travail que chefs et gérants font réellement tourner au quotidien.',
  },
];

// 2026-08-18 — Blog ALEMÁN. Mismo criterio que IT y FR: nace con 0 posts y
// CUATRO cajas, una por clúster del keyword research de Google.de
// (ROADMAP_BLOG_ALEMAN.md: ~224 keywords en 19 tandas y 31 SERP), no una
// traducción de otra taxonomía. El hub sólo pinta las categorías que YA tienen
// posts.
//
// Registro: Sie-Form (decisión 2026-08-16, coherente con los 51 spokes fase10).
// «KI», no «IA»: es la sigla alemana de la inteligencia artificial.
// «Restaurantmanagement» va SOLDADO en el nombre (regla 4 del research: el
// compuesto gana a la forma analítica) pero el slug lleva guion por legibilidad
// de URL — la regla 2 midió que el guion no reparte series.
const CATEGORIES_DE: BlogCategory[] = [
  {
    slug: 'ki-in-der-gastronomie',
    name: 'KI in der Gastronomie',
    description:
      'Wie künstliche Intelligenz Profiküchen verändert: Werkzeuge, die Ihre Zeit verdienen, ehrliche Vergleiche, Automatisierung, die einen vollen Service übersteht, und die Zahlen hinter jeder Entscheidung.',
  },
  {
    slug: 'restaurant-management',
    name: 'Restaurantmanagement',
    description:
      'Das Handwerk, das man vom Gastraum aus nicht sieht: Wareneinsatz und Kalkulation, Margen, HACCP und Allergene, Team, Lieferanten — und alles, was darüber entscheidet, ob der Betrieb das Jahr im Plus beendet.',
  },
  {
    slug: 'technik-und-rezepte',
    name: 'Technik und Rezepte',
    description:
      'Professionelle Küchentechnik für alle, die sie im Service brauchen: Garverfahren, Fermentation, Schnitttechniken, Mise en Place und Rezepte, die für die Brigade gedacht sind, nicht fürs Foto.',
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Alles über die Plattform: Guides zu den kulinarischen KI-Agenten, Neuigkeiten zu jedem Release und die Workflows, mit denen Küchenchefs und Betreiber täglich wirklich arbeiten.',
  },
];

// 2026-08-19 — Blog PORTUGUÉS. Mismo criterio que IT, FR y DE: nace con 0
// posts y CUATRO cajas, una por clúster del keyword research de Google.pt
// (ROADMAP_BLOG_PORTUGUES.md: ~240 keywords + 34 SERP), no una traducción de
// otra taxonomía. El hub sólo pinta las categorías que YA tienen posts.
//
// Registro: PT-PT ESTRICTO (decisión del roadmap: controlo, não controle;
// «restauração», no «restaurantes» a la brasileña; «gastronómico» con ó).
// El slug va sin acentos, como todos los segmentos de URL del sitio.
const CATEGORIES_PT: BlogCategory[] = [
  {
    slug: 'ia-na-gastronomia',
    name: 'IA na Gastronomia',
    description:
      'Como a inteligência artificial está a transformar as cozinhas profissionais: ferramentas que merecem o seu tempo, comparativos honestos, automatização que aguenta um serviço completo e os números por trás de cada decisão.',
  },
  {
    slug: 'gestao-de-restaurantes',
    name: 'Gestão de Restaurantes',
    description:
      'O ofício que não se vê a partir da sala: food cost e fichas técnicas, margens, HACCP e alergénios, equipa, fornecedores e tudo o que decide se o negócio acaba o ano no verde.',
  },
  {
    slug: 'tecnica-e-receitas',
    name: 'Técnica e Receitas',
    description:
      'A técnica de cozinha profissional explicada para quem a usa em serviço: confeções, fermentações, cortes, mise en place e receitas pensadas para serem reproduzidas em brigada, não para a fotografia.',
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Tudo sobre a plataforma: guias dos agentes de IA culinários, novidades de cada versão e os fluxos de trabalho que chefs e gestores realmente usam no dia a dia.',
  },
];

/** Taxonomía por idioma. Los idiomas sin blog propio devuelven lista vacía. */
export const BLOG_CATEGORIES_BY_LANG: Partial<Record<Locale, BlogCategory[]>> = {
  es: CATEGORIES_ES,
  en: CATEGORIES_EN,
  it: CATEGORIES_IT,
  fr: CATEGORIES_FR,
  de: CATEGORIES_DE,
  pt: CATEGORIES_PT,
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
//   · El IT usa 'categoria'/'pagina' porque son las palabras ITALIANAS, que se
//     escriben igual que las españolas. No es un copy-paste del ES: sin esta
//     entrada caería al fallback inglés y serviría /it/blog/category/…, que en
//     una URL italiana es ruido igual que 'categoria' lo sería en una inglesa.
//   · El FR usa 'categorie'/'page', que son las palabras FRANCESAS. Mismo
//     criterio nativo que en/it, con dos matices propios: 'categorie' va SIN
//     acento porque es un segmento de URL (la forma acentuada obligaría a
//     percent-encoding, %C3%A9, y ninguna URL del sitio lo hace), y 'page' se
//     escribe igual que en inglés — coincidencia, no fallback: sin esta entrada
//     el francés caería al ROUTE_SEGMENTS.en y serviría /fr/blog/category/…,
//     que en una URL francesa es ruido.
//   · El DE usa 'kategorie'/'seite', las palabras ALEMANAS. Mismo criterio
//     nativo: sin esta entrada caería al fallback inglés y serviría
//     /de/blog/category/…. 'kategorie' va en minúscula y sin adornos (los
//     sustantivos alemanes se capitalizan en prosa, no en un segmento de URL:
//     ninguna URL del sitio lleva mayúsculas).
//   · El PT usa 'categoria'/'pagina', las palabras PORTUGUESAS — que se
//     escriben como las españolas ('página' pierde el acento porque es un
//     segmento de URL, como 'categorie' francés perdió el suyo). No es un
//     copy-paste del ES: sin esta entrada caería al fallback inglés y
//     serviría /pt/blog/category/…, ruido en una URL portuguesa.
const ROUTE_SEGMENTS: Partial<Record<Locale, { category: string; page: string }>> = {
  es: { category: 'categoria', page: 'pagina' },
  en: { category: 'category', page: 'page' },
  it: { category: 'categoria', page: 'pagina' },
  fr: { category: 'categorie', page: 'page' },
  de: { category: 'kategorie', page: 'seite' },
  pt: { category: 'categoria', page: 'pagina' },
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

/** Idiomas que TIENEN blog propio (los que declaran taxonomía). Hoy: es, en, it, fr. */
export const hasBlog = (lang: Locale): boolean =>
  (BLOG_CATEGORIES_BY_LANG[lang]?.length ?? 0) > 0;

/**
 * Hub del blog para la navegación global (Header/Footer/Hero), que se pinta en
 * los 7 idiomas. OJO: no vale `blogBase(lang)` a secas — /nl/blog no existe
 * todavía y sería un 404. Los idiomas sin blog propio caen al ES, que es el
 * comportamiento que ya tenían antes de 8B.6. (El FR tiene árbol propio desde
 * el 2026-08-16, el DE desde el 2026-08-18 y el PT desde el 2026-08-19, así
 * que ya no caen; sólo queda el NL.)
 */
export const blogHubHref = (lang: Locale): string =>
  hasBlog(lang) ? blogBase(lang) : blogBase(DEFAULT_LOCALE);

/**
 * Hub de las LIBRERÍAS DE PROMPTS, mismo patrón que `blogHubHref`: sólo hay
 * versión nativa en es y en, y los demás idiomas caen al español.
 *
 * OJO, no confundirlo con la CATEGORÍA del blog del mismo nombre. Son cosas
 * distintas y el parecido ha costado un enlace roto: en inglés existe a la vez
 * la categoría `prompt-library` (/en/blog/category/prompt-library) y este hub
 * (/en/prompt-libraries), y el footer inglés enseñaba la categoría porque el
 * hub se le caía de la lista. Un lector que buscaba el catálogo de librerías
 * aterrizaba en un listado de posts del blog.
 *
 * Y el slug inglés es `prompt-libraries` en PLURAL a propósito: el filtro del
 * sitemap excluye toda ruta acabada en `-library` (así se llaman los dashboards
 * de pago), así que `/en/prompt-library` desaparecía del sitemap sin un aviso.
 */
export const promptHubHref = (lang: Locale): string =>
  lang === 'en' ? '/en/prompt-libraries' : '/libreria-de-prompts';

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

const MONTHS_IT = [
  'gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno',
  'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre',
];

/**
 * "17 febbraio 2026" — en italiano NO se intercalan preposiciones («17 de
 * febrero de 2026» sería un calco del español), y el mes va en minúscula.
 * Mismo criterio que las otras dos: UTC y sin Intl, para que el resultado no
 * dependa del locale de la máquina que construye.
 */
export function formatDateIt(d: Date): string {
  return `${d.getUTCDate()} ${MONTHS_IT[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
}

const MONTHS_FR = [
  'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
  'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre',
];

/**
 * "17 août 2026" — como en italiano, el francés NO intercala preposiciones y
 * escribe el mes en minúscula. Mismo criterio que las otras tres: UTC y sin
 * Intl, para que el resultado no dependa del locale de la máquina que construye.
 *
 * Única excepción: el día 1 se escribe "1er" ("1er août 2026"). Es la norma en
 * francés y la única fecha del mes que la lleva; el resto son cardinales.
 */
export function formatDateFr(d: Date): string {
  const day = d.getUTCDate();
  return `${day === 1 ? '1er' : day} ${MONTHS_FR[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
}

const MONTHS_DE = [
  'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
  'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember',
];

/**
 * "17. August 2026" — el alemán escribe el día como ORDINAL (número + punto) y
 * el mes con MAYÚSCULA inicial, como todo sustantivo. Mismo criterio que las
 * otras cuatro: UTC y sin Intl, para que el resultado no dependa del locale de
 * la máquina que construye.
 */
export function formatDateDe(d: Date): string {
  return `${d.getUTCDate()}. ${MONTHS_DE[d.getUTCMonth()]} ${d.getUTCFullYear()}`;
}

const MONTHS_PT = [
  'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
  'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',
];

/**
 * "17 de agosto de 2026" — el portugués SÍ intercala «de» como el español, y
 * el mes va en minúscula. Mismo criterio que las demás: UTC y sin Intl, para
 * que el resultado no dependa del locale de la máquina que construye.
 */
export function formatDatePt(d: Date): string {
  return `${d.getUTCDate()} de ${MONTHS_PT[d.getUTCMonth()]} de ${d.getUTCFullYear()}`;
}

/** Fecha larga en el idioma del post (fallback: formato ES). */
export function formatDate(d: Date, lang: Locale = DEFAULT_LOCALE): string {
  if (lang === 'en') return formatDateEn(d);
  if (lang === 'it') return formatDateIt(d);
  if (lang === 'fr') return formatDateFr(d);
  if (lang === 'de') return formatDateDe(d);
  if (lang === 'pt') return formatDatePt(d);
  return formatDateEs(d);
}

export const POSTS_PER_PAGE = 24;
