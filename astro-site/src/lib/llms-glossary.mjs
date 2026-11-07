/**
 * Bloque de glosario de llms.txt y llms-full.txt.
 *
 * La fuente son las fichas publicadas de src/content/blog: categoría de
 * glosario de su idioma (la misma lista que blog.ts) y draft distinto de true,
 * igual que getPublishedPosts. La URL es la ruta canónica del fichero
 * (postPath): el slug del nombre y el prefijo de post.data.lang. Un slug
 * escrito en `translations` solo agrupa fichas que existen y están publicadas
 * en el glosario; no se emite si el fichero no está.
 *
 * El frontmatter lo lee js-yaml con `yaml.load`, la misma llamada que
 * `parseFrontmatter` de `@astrojs/markdown-remark` (loader glob del content
 * layer). Los defaults que usa el generador son los del schema: `lang` es
 * `es` si falta y `draft` es false si falta; un `draft` que no sea boolean
 * no se interpreta a mano.
 */
import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { basename, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import yaml from 'js-yaml';

export const SITE = 'https://aichef.pro';

/** Mismo orden que LOCALES en src/i18n/config.ts y que los enlaces del bloque. */
export const LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];

/**
 * Idioma del rótulo y de la definición. El fichero está en inglés: si hay
 * ficha inglesa publicada se usa su definedTerm; si no, el español, y luego
 * el resto. Los enlaces siguen el orden de LANGS.
 */
const TEXT_LANGS = ['en', 'es', 'fr', 'de', 'it', 'pt', 'nl'];

/**
 * Slug de la categoría de glosario por idioma. Tiene que coincidir con
 * BLOG_CATEGORIES_BY_LANG en src/lib/blog.ts. El test lo comprueba.
 */
export const GLOSSARY_CATEGORY_BY_LANG = {
  es: 'glosario',
  en: 'glossary',
  fr: 'glossaire',
  de: 'glossar',
  it: 'glossario',
  pt: 'glossario',
  nl: 'glossarium',
};

/** Segmento de archive. Tiene que coincidir con ROUTE_SEGMENTS de blog.ts. */
export const ROUTE_CATEGORY_SEGMENT = {
  es: 'categoria',
  en: 'category',
  fr: 'categorie',
  de: 'kategorie',
  it: 'categoria',
  pt: 'categoria',
  nl: 'categorie',
};

export const GLOSSARY_START = '<!-- GLOSARIO-START -->';
export const GLOSSARY_END = '<!-- GLOSARIO-END -->';
export const GLOSSARY_LEGACY_START = '<!-- GLOSARIO-TANDA1-START -->';
export const GLOSSARY_LEGACY_END = '<!-- GLOSARIO-TANDA1-END -->';

export const MAILLARD_REDIRECT_NOTE =
  'The old slug maillard-concepto-y-definicion-2 redirects to the Maillard URL.';

const INTRO =
  'The hospitality glossary is no longer Spanish-only. Each language has its own category, native slugs and hreflang across es, en, fr, de, it, pt and nl. Definitions are written for cooks and operators. AI agents are the product positioning: calls to action go to the role page, the food cost calculator or the guest home of the app, never to a single agent URL.';

const HUB_LABEL = {
  es: 'ES',
  en: 'EN',
  fr: 'FR',
  de: 'DE',
  it: 'IT',
  pt: 'PT',
  nl: 'NL',
};

export const blogBase = (lang) => (lang === 'es' ? '/blog' : `/${lang}/blog`);

export const postPath = (slug, lang) => `${blogBase(lang)}/${slug}`;

export const categoryPath = (slug, lang) =>
  `${blogBase(lang)}/${ROUTE_CATEGORY_SEGMENT[lang]}/${slug}`;

export const absolutePostUrl = (post) => `${SITE}${postPath(post.slug, post.lang)}`;

export const glossaryHubUrl = (lang) =>
  `${SITE}${categoryPath(GLOSSARY_CATEGORY_BY_LANG[lang], lang)}`;

export function isPublishedGlossary(post) {
  if (post.draft) return false;
  return post.category === GLOSSARY_CATEGORY_BY_LANG[post.lang];
}

// Misma ancla que extractFrontmatter de @astrojs/markdown-remark: BOM opcional
// o una línea en blanco, y luego la cerca. El blog usa YAML (---), no TOML.
const FRONTMATTER_RE = /(?:^\uFEFF?|^\s*\n)(---|\+\+\+)([\s\S]*?\n)(?:---|\+\+\+)/;

function requireString(value, file, field) {
  if (typeof value !== 'string') throw new Error(`${file}: ${field} tiene que ser string`);
  return value;
}

function frontmatterFromYaml(raw, file) {
  const match = FRONTMATTER_RE.exec(raw);
  if (!match) throw new Error(`Sin frontmatter: ${file}`);
  if (match[1] !== '---') throw new Error(`${file}: el frontmatter no es YAML`);
  let data;
  try {
    data = yaml.load(match[2]);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    throw new Error(`${file}: frontmatter YAML inválido (${message})`);
  }
  if (data == null) data = {};
  if (typeof data !== 'object' || Array.isArray(data)) {
    throw new Error(`${file}: el frontmatter no es un objeto`);
  }
  const lang = data.lang === undefined ? 'es' : data.lang;
  if (typeof lang !== 'string' || !LANGS.includes(lang)) {
    throw new Error(`${file}: lang no reconocido (${String(lang)})`);
  }
  const title = requireString(data.title, file, 'title');
  const category = requireString(data.category, file, 'category');
  let draft = false;
  if (data.draft !== undefined) {
    if (typeof data.draft !== 'boolean') throw new Error(`${file}: draft tiene que ser boolean`);
    draft = data.draft;
  }
  const translations = {};
  if (data.translations != null) {
    if (typeof data.translations !== 'object' || Array.isArray(data.translations)) {
      throw new Error(`${file}: translations tiene que ser un objeto`);
    }
    for (const code of LANGS) {
      const slug = data.translations[code];
      if (slug == null || slug === '') continue;
      translations[code] = requireString(slug, file, `translations.${code}`);
    }
  }
  const definedTerm = {};
  if (data.definedTerm != null) {
    if (typeof data.definedTerm !== 'object' || Array.isArray(data.definedTerm)) {
      throw new Error(`${file}: definedTerm tiene que ser un objeto`);
    }
    if (data.definedTerm.name != null) {
      definedTerm.name = requireString(data.definedTerm.name, file, 'definedTerm.name');
    }
    if (data.definedTerm.description != null) {
      definedTerm.description = requireString(
        data.definedTerm.description,
        file,
        'definedTerm.description',
      );
    }
  }
  return { title, category, lang, draft, translations, definedTerm };
}

function walkMd(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    const full = join(dir, name);
    if (statSync(full).isDirectory()) walkMd(full, acc);
    else if (name.endsWith('.md')) acc.push(full);
  }
  return acc;
}

/** Todas las fichas del blog, publicadas o no. El slug es el del fichero. */
export function loadBlogPosts(dir) {
  const posts = [];
  const seen = new Set();
  for (const file of walkMd(dir).sort()) {
    const data = frontmatterFromYaml(readFileSync(file, 'utf8'), file);
    const slug = basename(file, '.md');
    const id = `${data.lang}:${slug}`;
    if (seen.has(id)) throw new Error(`Slug repetido en ${data.lang}: ${slug}`);
    seen.add(id);
    posts.push({
      id,
      file,
      slug,
      lang: data.lang,
      category: data.category,
      draft: data.draft,
      title: data.title,
      translations: data.translations,
      definedTerm: data.definedTerm,
    });
  }
  return posts;
}

function plain(value) {
  return value.replace(/\s+/g, ' ').trim().normalize('NFC');
}

function labelFor(byLang) {
  for (const lang of TEXT_LANGS) {
    const name = byLang.get(lang)?.definedTerm?.name;
    if (name && plain(name)) return plain(name);
  }
  for (const lang of TEXT_LANGS) {
    const title = byLang.get(lang)?.title;
    if (!title || !plain(title)) continue;
    const head = plain(title).split(':')[0].trim();
    return head || plain(title);
  }
  const sample = [...byLang.values()][0];
  throw new Error(`Ficha de glosario sin título: ${sample?.id ?? '?'}`);
}

function findRoot(parent, id) {
  let root = id;
  while (parent.get(root) !== root) root = parent.get(root);
  let cursor = id;
  while (parent.get(cursor) !== root) {
    const next = parent.get(cursor);
    parent.set(cursor, root);
    cursor = next;
  }
  return root;
}

/**
 * Agrupa fichas ya filtradas (solo glosario publicado). Una arista existe solo
 * si `translations` nombra el slug de otra ficha de ese conjunto.
 */
export function clusterGlossaryPosts(posts) {
  const index = new Map(posts.map((post) => [`${post.lang}:${post.slug}`, post]));
  const parent = new Map(posts.map((post) => [post.id, post.id]));
  const unresolved = [];
  for (const post of posts) {
    for (const lang of LANGS) {
      const slug = post.translations[lang];
      if (!slug) continue;
      const target = index.get(`${lang}:${slug}`);
      if (!target) {
        unresolved.push({ from: post.id, lang, slug });
        continue;
      }
      if (target.id === post.id) continue;
      const left = findRoot(parent, post.id);
      const right = findRoot(parent, target.id);
      if (left !== right) parent.set(right, left);
    }
  }
  const groups = new Map();
  for (const post of posts) {
    const root = findRoot(parent, post.id);
    if (!groups.has(root)) groups.set(root, []);
    groups.get(root).push(post);
  }
  const entries = [];
  for (const group of groups.values()) {
    const byLang = new Map();
    for (const post of group) {
      const previous = byLang.get(post.lang);
      if (previous) {
        throw new Error(
          `Dos fichas publicadas de glosario en ${post.lang} quedaron unidas: ${previous.slug} y ${post.slug}`,
        );
      }
      byLang.set(post.lang, post);
    }
    entries.push({ byLang, label: labelFor(byLang) });
  }
  entries.sort((a, b) => {
    const byLabel = a.label.localeCompare(b.label, 'en', { sensitivity: 'base', numeric: true });
    if (byLabel !== 0) return byLabel;
    return clusterKey(a).localeCompare(clusterKey(b));
  });
  const folded = new Map();
  for (const entry of entries) {
    const key = entry.label.toLocaleLowerCase('en');
    folded.set(key, (folded.get(key) ?? 0) + 1);
  }
  for (const entry of entries) {
    const key = entry.label.toLocaleLowerCase('en');
    if ((folded.get(key) ?? 0) < 2) {
      entry.display = entry.label;
      continue;
    }
    const slug = entry.byLang.get('es')?.slug ?? [...entry.byLang.values()][0].slug;
    entry.display = `${entry.label} (${slug})`;
  }
  return { entries, unresolved };
}

function clusterKey(entry) {
  return LANGS.filter((lang) => entry.byLang.has(lang))
    .map((lang) => `${lang}:${entry.byLang.get(lang).slug}`)
    .join('|');
}

export function prepareGlossaryEntries(posts) {
  return clusterGlossaryPosts(posts).entries;
}

function countsLine(entries) {
  const perLang = Object.fromEntries(LANGS.map((lang) => [lang, 0]));
  let posts = 0;
  for (const entry of entries) {
    for (const lang of entry.byLang.keys()) {
      perLang[lang] += 1;
      posts += 1;
    }
  }
  const bits = LANGS.map((lang) => `${lang} ${perLang[lang]}`).join(', ');
  return `Published entries: ${posts} posts (${bits}), ${entries.length} terms. A language is listed only when that glossary post is published.`;
}

function entryLine(entry) {
  if (entry.display.includes('](') || entry.display.includes('[')) {
    throw new Error(`El rótulo del glosario rompería el enlace: ${entry.display}`);
  }
  const links = LANGS.filter((lang) => entry.byLang.has(lang))
    .map((lang) => `[${lang}](${absolutePostUrl(entry.byLang.get(lang))})`)
    .join(' ');
  return `- ${entry.display}: ${links}`;
}

function definitionLine(entry) {
  for (const lang of TEXT_LANGS) {
    const description = entry.byLang.get(lang)?.definedTerm?.description;
    if (!description || !plain(description)) continue;
    return `  ${lang}: ${plain(description)}`;
  }
  return '';
}

export function renderGlossaryBlock(entries, variant) {
  if (variant !== 'index' && variant !== 'full') {
    throw new Error(`Variante de llms desconocida: ${String(variant)}`);
  }
  const hubs = LANGS.map((lang) => `[${HUB_LABEL[lang]}](${glossaryHubUrl(lang)})`).join(' · ');
  const lines = [
    '## Culinary glossary (7 languages)',
    '',
    INTRO,
    '',
    `Glossary hubs: ${hubs}.`,
    '',
    countsLine(entries),
  ];
  if (variant === 'index') {
    lines.push('One-line definitions of these entries are in llms-full.txt.');
  }
  lines.push('');
  for (const entry of entries) {
    lines.push(entryLine(entry));
    if (variant === 'full') {
      const definition = definitionLine(entry);
      if (definition) lines.push(definition);
    }
  }
  return lines.join('\n');
}

function locateBlock(text) {
  const starts = [];
  for (const marker of [GLOSSARY_START, GLOSSARY_LEGACY_START]) {
    let from = 0;
    while (from < text.length) {
      const index = text.indexOf(marker, from);
      if (index === -1) break;
      starts.push({ marker, index });
      from = index + marker.length;
    }
  }
  if (starts.length !== 1) {
    throw new Error(`Se esperaba un único bloque de glosario y hay ${starts.length}`);
  }
  const start = starts[0];
  const endMarker = start.marker === GLOSSARY_START ? GLOSSARY_END : GLOSSARY_LEGACY_END;
  const end = text.indexOf(endMarker, start.index + start.marker.length);
  if (end === -1) throw new Error('Falta el cierre del bloque de glosario');
  if (text.indexOf(endMarker, end + endMarker.length) !== -1) {
    throw new Error('Cierre de glosario duplicado');
  }
  return {
    start: start.index,
    startLength: start.marker.length,
    end,
    endLength: endMarker.length,
    interior: text.slice(start.index + start.marker.length, end),
  };
}

/**
 * Sustituye el bloque generado y deja el resto del fichero igual.
 * La frase del 301 de Maillard, si estaba dentro del bloque viejo, pasa
 * a continuación del cierre para no perderla ni repetir sus URLs.
 */
export function applyGlossaryBlock(text, entries, variant) {
  const block = locateBlock(text);
  const before = text.slice(0, block.start);
  let after = text.slice(block.end + block.endLength);
  if (
    block.interior.includes(MAILLARD_REDIRECT_NOTE) &&
    !before.includes(MAILLARD_REDIRECT_NOTE) &&
    !after.includes(MAILLARD_REDIRECT_NOTE)
  ) {
    const rest = after.replace(/^\n/, '');
    after = `\n\n${MAILLARD_REDIRECT_NOTE}\n${rest}`;
  }
  let next = `${before}${GLOSSARY_START}\n${renderGlossaryBlock(entries, variant)}\n${GLOSSARY_END}${after}`;
  if (!next.endsWith('\n')) next += '\n';
  return next;
}

/** URLs de ficha dentro de las viñetas del bloque (no los hubs ni el resto del fichero). */
export function glossaryEntryUrls(blockText) {
  const urls = [];
  for (const line of blockText.split('\n')) {
    if (!line.startsWith('- ')) continue;
    const re = /\[(es|en|fr|de|it|pt|nl)\]\((https:\/\/aichef\.pro[^)]+)\)/g;
    let match = re.exec(line);
    while (match) {
      urls.push(match[2]);
      match = re.exec(line);
    }
  }
  return urls;
}

export function glossaryBlock(text) {
  const start = text.indexOf(GLOSSARY_START);
  const end = text.indexOf(GLOSSARY_END);
  if (start === -1 || end === -1 || end < start) {
    throw new Error('El fichero no tiene el bloque GLOSARIO');
  }
  return text.slice(start, end + GLOSSARY_END.length);
}

const LLMS_FILES = [
  ['llms.txt', 'index'],
  ['llms-full.txt', 'full'],
];

export function syncLlmsGlossaryFiles({ astroRoot, write = true } = {}) {
  const posts = loadBlogPosts(join(astroRoot, 'src/content/blog')).filter(isPublishedGlossary);
  const { entries, unresolved } = clusterGlossaryPosts(posts);
  const results = [];
  for (const [name, variant] of LLMS_FILES) {
    const file = join(astroRoot, 'public', name);
    const current = readFileSync(file, 'utf8');
    const next = applyGlossaryBlock(current, entries, variant);
    if (write && next !== current) writeFileSync(file, next);
    results.push({ file, variant, changed: next !== current });
  }
  return { posts, entries, unresolved, results };
}

function runCli() {
  const astroRoot = fileURLToPath(new URL('../..', import.meta.url));
  const check = process.argv.includes('--check');
  const { posts, entries, unresolved, results } = syncLlmsGlossaryFiles({
    astroRoot,
    write: !check,
  });
  const perLang = Object.fromEntries(LANGS.map((lang) => [lang, 0]));
  for (const post of posts) perLang[post.lang] += 1;
  console.log(
    `glosario publicado: ${posts.length} fichas, ${entries.length} términos (${LANGS.map((lang) => `${lang} ${perLang[lang]}`).join(', ')})`,
  );
  if (unresolved.length) {
    console.log(`traducciones sin ficha de glosario publicada: ${unresolved.length}`);
  }
  const dirty = results.filter((result) => result.changed);
  if (check && dirty.length) {
    console.error(`desactualizados: ${dirty.map((result) => result.file).join(', ')}`);
    process.exitCode = 1;
    return;
  }
  if (!check && dirty.length === 0) console.log('sin cambios');
}

const invokedDirectly =
  process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href;

if (invokedDirectly) runCli();
