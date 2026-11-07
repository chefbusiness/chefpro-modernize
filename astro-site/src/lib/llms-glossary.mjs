/**
 * Bloque de glosario de llms.txt y llms-full.txt.
 *
 * La fuente son las fichas publicadas de src/content/blog: categoría de
 * glosario de su idioma (la misma lista que blog.ts) y draft distinto de true,
 * igual que getPublishedPosts. La URL es la ruta canónica del fichero
 * (postPath): el slug del nombre y el prefijo de post.data.lang. Un slug
 * escrito en `translations` solo agrupa fichas que existen y están publicadas
 * en el glosario; no se emite si el fichero no está.
 */
import { readdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { basename, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

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

function unquote(raw, file) {
  const value = raw.trim();
  if (value.startsWith('"')) {
    if (value.length < 2 || !value.endsWith('"')) {
      throw new Error(`${file}: cadena sin cerrar (${value.slice(0, 60)})`);
    }
    return value
      .slice(1, -1)
      .replace(/\\n/g, '\n')
      .replace(/\\"/g, '"')
      .replace(/\\\\/g, '\\');
  }
  if (value.startsWith("'")) {
    if (value.length < 2 || !value.endsWith("'")) {
      throw new Error(`${file}: cadena sin cerrar (${value.slice(0, 60)})`);
    }
    return value.slice(1, -1).replace(/''/g, "'");
  }
  return value.replace(/\s+#.*$/, '');
}

function parseFrontmatter(raw, file) {
  if (!raw.startsWith('---\n') && !raw.startsWith('---\r\n')) {
    throw new Error(`Sin frontmatter: ${file}`);
  }
  const end = raw.indexOf('\n---', 3);
  if (end === -1) throw new Error(`Frontmatter sin cierre: ${file}`);
  const body = raw.slice(raw.startsWith('---\r\n') ? 5 : 4, end);
  const data = {
    title: '',
    category: '',
    lang: 'es',
    draft: false,
    translations: {},
    definedTerm: {},
  };
  let section = null;
  for (const line of body.split(/\r?\n/)) {
    if (!line.trim() || line.trimStart().startsWith('#')) continue;
    const indent = line.match(/^ */)[0].length;
    if (indent === 0) {
      const header = line.match(/^([A-Za-z0-9_]+):\s*(.*)$/);
      if (!header) {
        section = null;
        continue;
      }
      const key = header[1];
      const value = header[2].trim();
      const multiline = value === '' || value === '>' || value === '|' || value.startsWith('>') || value.startsWith('|');
      if (multiline) {
        if (key === 'translations' || key === 'definedTerm') {
          if (value !== '') throw new Error(`${file}: ${key} no admite un escalar multilínea`);
          section = key;
          continue;
        }
        if (key === 'title' || key === 'category' || key === 'lang' || key === 'draft') {
          throw new Error(`${file}: ${key} no admite un escalar multilínea`);
        }
        section = null;
        continue;
      }
      section = null;
      if (key === 'title') data.title = unquote(value, file);
      else if (key === 'category') data.category = unquote(value, file);
      else if (key === 'lang') data.lang = unquote(value, file);
      else if (key === 'draft') {
        const flag = unquote(value, file);
        data.draft = flag === 'true' || flag === 'yes' || flag === '1';
      }
      continue;
    }
    if (section === 'translations') {
      const item = line.match(/^\s+(es|en|fr|de|it|pt|nl):\s*(.*)$/);
      if (!item) continue;
      const slug = unquote(item[2].trim(), file);
      if (slug) data.translations[item[1]] = slug;
      continue;
    }
    if (section === 'definedTerm') {
      const item = line.match(/^\s+(name|description):\s*(.*)$/);
      if (!item) continue;
      const value = item[2].trim();
      if (value === '' || value === '>' || value === '|' || value.startsWith('>') || value.startsWith('|')) {
        throw new Error(`${file}: definedTerm.${item[1]} no admite un escalar multilínea`);
      }
      data.definedTerm[item[1]] = unquote(value, file);
    }
  }
  if (!LANGS.includes(data.lang)) throw new Error(`${file}: lang no reconocido (${data.lang})`);
  return data;
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
    const data = parseFrontmatter(readFileSync(file, 'utf8'), file);
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
