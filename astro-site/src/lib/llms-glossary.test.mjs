import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, rmSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';
import {
  GLOSSARY_CATEGORY_BY_LANG,
  GLOSSARY_END,
  GLOSSARY_LEGACY_END,
  GLOSSARY_LEGACY_START,
  GLOSSARY_START,
  LANGS,
  MAILLARD_REDIRECT_NOTE,
  ROUTE_CATEGORY_SEGMENT,
  SITE,
  absolutePostUrl,
  applyGlossaryBlock,
  blogBase,
  categoryPath,
  clusterGlossaryPosts,
  glossaryBlock,
  glossaryEntryUrls,
  glossaryHubUrl,
  isPublishedGlossary,
  loadBlogPosts,
  postPath,
  prepareGlossaryEntries,
  syncLlmsGlossaryFiles,
} from './llms-glossary.mjs';

const ASTRO_ROOT = fileURLToPath(new URL('../..', import.meta.url));
const BLOG_DIR = join(ASTRO_ROOT, 'src/content/blog');
const BLOG_TS = fileURLToPath(new URL('./blog.ts', import.meta.url));

const TANDA1_URLS = [
  'https://aichef.pro/blog/beurre-manie',
  'https://aichef.pro/en/blog/beurre-manie',
  'https://aichef.pro/fr/blog/beurre-manie',
  'https://aichef.pro/de/blog/mehlbutter',
  'https://aichef.pro/it/blog/beurre-manie',
  'https://aichef.pro/pt/blog/beurre-manie',
  'https://aichef.pro/nl/blog/beurre-manie',
  'https://aichef.pro/blog/napar-una-salsa',
  'https://aichef.pro/en/blog/nap-a-sauce',
  'https://aichef.pro/de/blog/nappieren',
  'https://aichef.pro/blog/roux-concepto-y-definicion',
  'https://aichef.pro/en/blog/what-is-a-roux',
  'https://aichef.pro/fr/blog/qu-est-ce-qu-un-roux',
  'https://aichef.pro/blog/demi-glace-concepto-y-definicion',
  'https://aichef.pro/nl/blog/demi-glace',
];

function writePost(dir, lang, slug, fields) {
  const folder = join(dir, lang);
  mkdirSync(folder, { recursive: true });
  const lines = [
    '---',
    `title: "${fields.title ?? slug}"`,
    `category: ${fields.category}`,
    `lang: ${lang}`,
  ];
  if (fields.draft) lines.push('draft: true');
  if (fields.translations) {
    lines.push('translations:');
    for (const [locale, target] of Object.entries(fields.translations)) {
      lines.push(`  ${locale}: "${target}"`);
    }
  }
  if (fields.term) {
    lines.push('definedTerm:');
    lines.push(`  name: "${fields.term}"`);
    lines.push(`  description: "${fields.definition ?? 'Definición.'}"`);
  }
  lines.push('---', '', 'Cuerpo.', '');
  writeFileSync(join(folder, `${slug}.md`), lines.join('\n'));
}

test('las rutas salen de blog.ts, no de un slug inventado', () => {
  const blogTs = readFileSync(BLOG_TS, 'utf8');
  assert.match(blogTs, /lang === DEFAULT_LOCALE \? '\/blog' : `\/\$\{lang\}\/blog`/);
  assert.match(blogTs, /\$\{blogBase\(lang\)\}\/\$\{slug\}/);
  assert.match(
    blogTs,
    /\$\{blogBase\(lang\)\}\/\$\{segments\(lang\)\.category\}\/\$\{slug\}/,
  );
  const names = {
    es: 'CATEGORIES_ES',
    en: 'CATEGORIES_EN',
    it: 'CATEGORIES_IT',
    fr: 'CATEGORIES_FR',
    de: 'CATEGORIES_DE',
    pt: 'CATEGORIES_PT',
    nl: 'CATEGORIES_NL',
  };
  const markers = [...Object.values(names), 'BLOG_CATEGORIES_BY_LANG'];
  for (const [lang, name] of Object.entries(names)) {
    const start = blogTs.indexOf(`const ${name}`);
    assert.ok(start > 0, name);
    let end = blogTs.length;
    for (const marker of markers) {
      if (marker === name) continue;
      const index = blogTs.indexOf(marker, start + name.length);
      if (index !== -1 && index < end) end = index;
    }
    const slice = blogTs.slice(start, end);
    assert.match(slice, new RegExp(`slug:\\s*'${GLOSSARY_CATEGORY_BY_LANG[lang]}'`));
    assert.match(
      blogTs,
      new RegExp(`${lang}:\\s*\\{\\s*category:\\s*'${ROUTE_CATEGORY_SEGMENT[lang]}'`),
    );
    assert.equal(blogBase(lang), lang === 'es' ? '/blog' : `/${lang}/blog`);
    assert.equal(postPath('beurre-manie', lang), `${blogBase(lang)}/beurre-manie`);
    assert.equal(
      categoryPath(GLOSSARY_CATEGORY_BY_LANG[lang], lang),
      `${blogBase(lang)}/${ROUTE_CATEGORY_SEGMENT[lang]}/${GLOSSARY_CATEGORY_BY_LANG[lang]}`,
    );
  }
  assert.deepEqual(LANGS, ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']);
});

test('un borrador, una categoría ajena y un slug sin ficha no entran', () => {
  const dir = mkdtempSync(join(tmpdir(), 'llms-glosario-'));
  try {
    writePost(dir, 'es', 'vivo', {
      category: 'glosario',
      term: 'Vivo',
      translations: { es: 'otro-slug', en: 'borrador', fr: 'no-existe', de: 'otra-categoria' },
    });
    writePost(dir, 'es', 'borrador', { category: 'glosario', draft: true, term: 'Borrador' });
    writePost(dir, 'en', 'borrador', { category: 'glossary', draft: true, term: 'Draft' });
    writePost(dir, 'de', 'otra-categoria', { category: 'technik-und-rezepte', term: 'No' });
    writePost(dir, 'en', 'mal-categoria', { category: 'glosario', term: 'Mal' });
    writePost(dir, 'fr', 'suelto', { category: 'glossaire', term: 'Seul', definition: 'Une définition.' });
    const posts = loadBlogPosts(dir);
    const published = posts.filter(isPublishedGlossary);
    const slugs = published.map((post) => post.id).sort();
    assert.deepEqual(slugs, ['es:vivo', 'fr:suelto']);
    const { entries, unresolved } = clusterGlossaryPosts(published);
    assert.equal(entries.length, 2);
    const vivo = entries.find((entry) => entry.byLang.has('es'));
    assert.equal(absolutePostUrl(vivo.byLang.get('es')), `${SITE}/blog/vivo`);
    assert.equal(vivo.byLang.size, 1);
    const missed = new Set(unresolved.map((item) => `${item.lang}:${item.slug}`));
    assert.ok(missed.has('en:borrador'));
    assert.ok(missed.has('fr:no-existe'));
    assert.ok(missed.has('de:otra-categoria'));
    assert.ok(missed.has('es:otro-slug'));
    const block = applyGlossaryBlock(
      `${GLOSSARY_LEGACY_START}\nviejo\n${GLOSSARY_LEGACY_END}\n`,
      entries,
      'index',
    );
    const urls = glossaryEntryUrls(block);
    assert.deepEqual(urls.sort(), [`${SITE}/blog/vivo`, `${SITE}/fr/blog/suelto`].sort());
    assert.equal(urls.includes(`${SITE}/blog/otro-slug`), false);
    assert.equal(urls.includes(`${SITE}/en/blog/borrador`), false);
    assert.equal(urls.includes(`${SITE}/en/blog/mal-categoria`), false);
    assert.equal(urls.includes(`${SITE}/de/blog/otra-categoria`), false);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test('dos fichas del mismo idioma unidas por translations abortan', () => {
  const posts = [
    {
      id: 'es:a',
      slug: 'a',
      lang: 'es',
      title: 'A',
      translations: { en: 'en-a' },
      definedTerm: { name: 'A' },
    },
    {
      id: 'es:b',
      slug: 'b',
      lang: 'es',
      title: 'B',
      translations: { en: 'en-a' },
      definedTerm: { name: 'B' },
    },
    {
      id: 'en:en-a',
      slug: 'en-a',
      lang: 'en',
      title: 'A',
      translations: { es: 'a' },
      definedTerm: { name: 'A' },
    },
  ];
  assert.throws(() => clusterGlossaryPosts(posts), /Dos fichas publicadas/);
});

test('el bloque generado no toca el texto manual y la segunda pasada no cambia nada', () => {
  const posts = [
    {
      id: 'es:real-es',
      slug: 'real-es',
      lang: 'es',
      title: 'Real',
      translations: { es: 'slug-distinto', en: 'real-en' },
      definedTerm: { name: 'Real', description: 'Definición publicada.' },
    },
    {
      id: 'en:real-en',
      slug: 'real-en',
      lang: 'en',
      title: 'Real',
      translations: { es: 'real-es', en: 'real-en' },
      definedTerm: { name: 'Real', description: 'Published definition.' },
    },
  ];
  const entries = prepareGlossaryEntries(posts);
  const source = [
    '# manual before',
    'keep-this-url https://aichef.pro/precios',
    '',
    GLOSSARY_LEGACY_START,
    'Batch 1, sauces.',
    MAILLARD_REDIRECT_NOTE,
    GLOSSARY_LEGACY_END,
    '',
    '# manual after',
    '',
  ].join('\n');
  const once = applyGlossaryBlock(source, entries, 'full');
  const twice = applyGlossaryBlock(once, entries, 'full');
  assert.equal(twice, once);
  assert.match(once, /^# manual before\nkeep-this-url https:\/\/aichef\.pro\/precios\n\n/);
  assert.match(once, /\n# manual after\n$/);
  assert.equal(once.includes('Batch 1, sauces.'), false);
  assert.equal(once.includes(`${SITE}/blog/slug-distinto`), false);
  assert.match(once, new RegExp(`\\[es\\]\\(${SITE}/blog/real-es\\)`));
  assert.match(once, new RegExp(`\\[en\\]\\(${SITE}/en/blog/real-en\\)`));
  const start = once.indexOf(GLOSSARY_START);
  const end = once.indexOf(GLOSSARY_END);
  assert.equal(once.slice(start, end).includes(MAILLARD_REDIRECT_NOTE), false);
  assert.equal(once.split(MAILLARD_REDIRECT_NOTE).length, 2);
  assert.match(once, new RegExp(`${GLOSSARY_END}\n\n${MAILLARD_REDIRECT_NOTE}\n`));
  assert.match(once, / {2}en: Published definition\./);
});

test('las fichas publicadas del glosario coinciden con los dos llms y el resto queda fuera', () => {
  const all = loadBlogPosts(BLOG_DIR);
  const published = all.filter(isPublishedGlossary);
  const { entries, unresolved } = clusterGlossaryPosts(published);
  assert.ok(published.length > 12);
  assert.ok(entries.length >= 12);
  const rendered = [];
  for (const name of ['llms.txt', 'llms-full.txt']) {
    const text = readFileSync(join(ASTRO_ROOT, 'public', name), 'utf8');
    const again = applyGlossaryBlock(text, entries, name === 'llms.txt' ? 'index' : 'full');
    assert.equal(again, text, name);
    rendered.push(text);
  }
  const [indexText, fullText] = rendered;
  for (const text of rendered) {
    assert.equal(text.includes(GLOSSARY_LEGACY_START), false);
    assert.equal(text.split(GLOSSARY_START).length, 2);
    assert.equal(text.split(GLOSSARY_END).length, 2);
    const block = glossaryBlock(text);
    assert.equal(block.includes(MAILLARD_REDIRECT_NOTE), false);
    assert.equal(text.split(MAILLARD_REDIRECT_NOTE).length, 2);
    assert.ok(text.indexOf(MAILLARD_REDIRECT_NOTE) > text.indexOf(GLOSSARY_END));
    for (const lang of LANGS) {
      const hub = glossaryHubUrl(lang);
      assert.equal(block.split(hub).length, 2, hub);
    }
  }
  assert.match(
    indexText.slice(0, indexText.indexOf(GLOSSARY_START)),
    /\[Sitemap\]\(https:\/\/aichef\.pro\/sitemap-index\.xml\)\n\n$/,
  );
  assert.match(
    fullText.slice(0, fullText.indexOf(GLOSSARY_START)),
    /Translating Madrid into another country would publish invented local law\.\n\n$/,
  );
  const indexUrls = glossaryEntryUrls(glossaryBlock(indexText));
  const fullUrls = glossaryEntryUrls(glossaryBlock(fullText));
  assert.deepEqual(fullUrls, indexUrls);
  assert.equal(indexUrls.length, published.length);
  assert.equal(new Set(indexUrls).size, published.length);
  const urlSet = new Set(indexUrls);
  for (const post of all) {
    const url = absolutePostUrl(post);
    assert.equal(urlSet.has(url), isPublishedGlossary(post), url);
  }
  for (const miss of unresolved) {
    assert.equal(urlSet.has(`${SITE}${postPath(miss.slug, miss.lang)}`), false);
  }
  for (const url of TANDA1_URLS) assert.ok(urlSet.has(url), url);
  const reduction = entries.find((entry) => entry.byLang.get('es')?.slug === 'reduccion-concepto-definicion');
  assert.ok(reduction);
  assert.deepEqual(
    LANGS.map((lang) => reduction.byLang.get(lang)?.slug),
    [
      'reduccion-concepto-definicion',
      'what-is-reduction-in-cooking',
      'reduction-en-cuisine',
      'reduktion-kochen',
      'riduzione-in-cucina',
      'reducao-na-cozinha',
      'reduceren-koken',
    ],
  );
  for (const lang of LANGS) {
    assert.equal(
      absolutePostUrl(reduction.byLang.get(lang)),
      `${SITE}${postPath(reduction.byLang.get(lang).slug, lang)}`,
    );
  }
  const indexLines = glossaryBlock(indexText).split('\n').filter((line) => line.startsWith('- '));
  const fullLines = glossaryBlock(fullText).split('\n').filter((line) => line.startsWith('- '));
  assert.deepEqual(fullLines, indexLines);
  assert.match(glossaryBlock(fullText), / {2}en: /);
  assert.equal(/\n {2}en: /.test(glossaryBlock(indexText)), false);
  const synced = syncLlmsGlossaryFiles({ astroRoot: ASTRO_ROOT, write: true });
  assert.equal(synced.results.every((result) => result.changed === false), true);
});
