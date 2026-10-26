/**
 * Banners de productos digitales en el blog y el glosario.
 *
 * Se eligen en build (un plan para todo el corpus) y un plugin de remark los
 * inserta en el árbol, sin reescribir el Markdown. Las piezas nuevas entran
 * solas en el siguiente build.
 *
 * Reglas (John, 2026-10-26):
 *   · 2 o 3 banners por pieza, 4 si es larga, siempre antes de la FAQ.
 *   · Los banners de producto que ya estaban se quedan y cuentan para el cupo.
 *   · Los CTA de trial («+75 agentes», bloques de la app) no se tocan.
 *   · ES vende el catálogo ES. El resto de idiomas vende el EN hasta que
 *     CATALOGUE_BY_LANG apunte a un catálogo propio.
 *   · Primero un producto que encaja con el tema, si no se sale de la banda
 *     de reparto; el resto rota por lo menos usado, de forma determinista.
 *   · Título, precio e imagen salen del catálogo. Sin claims inventados.
 */
import { createHash } from 'node:crypto';
import { readFileSync, readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const CATALOGUE_PATH = fileURLToPath(new URL('../data/digital-products-catalogue.json', import.meta.url));
const BLOG_DIR = fileURLToPath(new URL('../content/blog', import.meta.url));

/**
 * Catálogo que vende cada idioma del blog.
 * Cuando un idioma tenga fichero propio en el JSON, basta con cambiar su valor
 * (por ejemplo `fr: 'fr'`) y los posts de ese idioma pasan solos a ese catálogo.
 */
export const CATALOGUE_BY_LANG = {
  es: 'es',
  en: 'en',
  fr: 'en',
  de: 'en',
  it: 'en',
  pt: 'en',
  nl: 'en',
};

/** Categorías de glosario. El UTM usa la palabra `glosario` en todos los idiomas. */
export const GLOSSARY_CATEGORIES = new Set([
  'glosario',
  'glossary',
  'glossario',
  'glossaire',
  'glossar',
  'glossarium',
]);

const CHROME = {
  es: { tag: 'Producto digital', cta: 'Ver producto →' },
  en: { tag: 'Digital product', cta: 'View product →' },
};

const LOGO = '/email-assets/aichef-pro-logo-white.png';

/**
 * Grupos de tema. Un producto entra por su TÍTULO (no por la lista de
 * «también sirve para» de los tags, que metería el kit de food cost en
 * todas las pizzerías). Una pieza entra por slug, título, tags y h2.
 */
const TOPICS = [
  ['pizza', 'pizzeria', 'pizzería', 'napolitana'],
  ['heladeria', 'heladería', 'helado', 'ice cream', 'gelato', 'eisdiele'],
  ['chocolate', 'chocolateria', 'chocolatería', 'chocolatier', 'churreria', 'churrería', 'churro'],
  ['pasteleria', 'pastelería', 'pastry', 'patisserie', 'pâtisserie', 'pasticceria', 'brioche', 'viennoiserie'],
  ['panaderia', 'panadería', 'bakery', 'boulangerie', 'bäckerei', 'padaria', 'panadero', 'sourdough'],
  ['food cost', 'escandallo', 'escandallos', 'menu engineering', 'ingenieria de menu', 'ingeniería de menú', 'wareneinsatz', 'recipe cost', 'recipe costing', 'kalkulation', 'portion', 'porcion', 'porciones', 'portionsgroessen', 'portionsgrosse'],
  ['haccp', 'appcc', 'alergeno', 'alergenos', 'alérgeno', 'alérgenos', 'allergen', 'allergene', 'alergenio', 'hygiene', 'higiene', 'seguridad alimentaria', 'food safety'],
  ['inventario', 'inventory'],
  ['turnos', 'turno', 'scheduling', 'staff', 'brigada', 'brigade', 'brigata'],
  ['financiero', 'financial', 'rentabilidad', 'profit margin'],
  ['coctel', 'cóctel', 'cocktail', 'cocteleria', 'coctelería', 'mixologia', 'mixología', 'bartender', 'barra movil', 'mobile bar', 'bares'],
  ['bar'],
  ['cafeteria', 'cafetería', 'coffee', 'cafe', 'café', 'brunch', 'barista'],
  ['food truck', 'foodtruck', 'street food'],
  ['catering', 'banquet'],
  ['hotel', 'hoteleria', 'hotelería'],
  ['sushi', 'japones', 'japonés', 'japanese', 'nikkei', 'umami'],
  ['asador', 'parrilla', 'parrillero', 'bbq', 'barbecue', 'grill', 'josper'],
  ['marisco', 'marisqueria', 'marisquería', 'pescado', 'fish', 'seafood', 'poisson', 'pesce', 'fisch', 'fumet', 'fumetto', 'visfumet', 'fischfond'],
  ['tapas', 'gastrobar', 'gastropub'],
  ['taqueria', 'taquería', 'mexicano', 'mexicana', 'mexican', 'taco'],
  ['peruano', 'peruana', 'peruvian'],
  ['dark kitchen', 'ghost kitchen', 'cloud kitchen'],
  ['paella'],
  ['chef ejecutivo', 'executive chef'],
  ['manager', 'gerente'],
  ['chef privado', 'personal chef', 'showcooking'],
  ['finca', 'bodas'],
  ['prompt', 'prompts', 'chefgpt', 'chatgpt'],
  ['hamburguesa', 'hamburgueseria', 'hamburguesería', 'burger'],
];

const rawCatalogue = JSON.parse(readFileSync(CATALOGUE_PATH, 'utf8'));

function fold(s) {
  return String(s || '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase();
}

function decodeBasic(s) {
  return String(s || '')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;|&#160;/gi, ' ')
    .replace(/&amp;|&#038;|&#38;/gi, '&')
    .replace(/&#x26;/gi, '&')
    .replace(/&quot;|&#34;/gi, '"')
    .replace(/&#8217;|&rsquo;|&#8216;/gi, "'")
    .replace(/&#8211;|&ndash;/gi, '-')
    .replace(/&#8220;|&#8221;|&ldquo;|&rdquo;/gi, '"')
    .replace(/\s+/g, ' ')
    .trim();
}

function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function hash32(s) {
  return createHash('sha256').update(s).digest().readUInt32BE(0);
}

function slugFromHref(href) {
  const clean = String(href || '').replace(/&amp;/g, '&').split('?')[0];
  try {
    const u = clean.startsWith('http') ? new URL(clean) : new URL(clean, 'https://aichef.pro');
    const parts = u.pathname.replace(/\/$/, '').split('/').filter(Boolean);
    return parts[parts.length - 1] || '';
  } catch {
    return '';
  }
}

function productId(url) {
  return slugFromHref(url);
}

function loadProducts(catalogueKey) {
  const list = rawCatalogue[catalogueKey] || [];
  return list.map((p) => {
    const id = productId(p.url);
    const title = p.title;
    const topics = topicsIn(title);
    return {
      id,
      title,
      price: p.price,
      image: p.image,
      url: p.url,
      tags: p.tags || '',
      catalogue: catalogueKey,
      topics,
    };
  });
}

const PRODUCTS = {
  es: loadProducts('es'),
  en: loadProducts('en'),
};

const PRODUCT_BY_SLUG = {
  es: new Map(PRODUCTS.es.map((p) => [p.id, p])),
  en: new Map(PRODUCTS.en.map((p) => [p.id, p])),
};

function catalogueKeyFor(lang) {
  const want = CATALOGUE_BY_LANG[lang] || 'en';
  if (PRODUCTS[want]?.length) return want;
  return 'en';
}

function topicsIn(text) {
  const hay = ` ${fold(text).replace(/[^a-z0-9]+/g, ' ')} `;
  const hit = [];
  for (const group of TOPICS) {
    const ok = group.some((phrase) => {
      const p = fold(phrase).replace(/[^a-z0-9]+/g, ' ').trim();
      if (!p) return false;
      return hay.includes(` ${p} `);
    });
    if (ok) hit.push(group[0]);
  }
  return hit;
}

function isFaq(text) {
  const t = fold(decodeBasic(text));
  return /preguntas frecuentes|frequently asked|questions frequentes|haufig gestellte|domande frequenti|perguntas frequentes|veelgestelde|^faq\b|\bfaq$/.test(t);
}

function parseFrontmatter(raw) {
  if (!raw.startsWith('---')) return { fm: '', body: raw, data: {} };
  const end = raw.indexOf('\n---', 3);
  if (end === -1) return { fm: '', body: raw, data: {} };
  const fm = raw.slice(3, end);
  const body = raw.slice(end + 4).replace(/^\s*\n/, '');
  const field = (key) => {
    const m = fm.match(new RegExp(`^${key}:\\s*(.*)$`, 'm'));
    return m ? m[1].trim() : '';
  };
  const unquote = (s) => s.replace(/^["']|["']$/g, '');
  let tags = [];
  const tagsLine = field('tags');
  if (tagsLine.startsWith('[')) {
    try { tags = JSON.parse(tagsLine); } catch { tags = []; }
  } else {
    const block = fm.match(/^tags:\s*\n((?:[ \t]+-\s+.*\n?)*)/m);
    if (block) {
      tags = block[1]
        .split('\n')
        .map((l) => l.replace(/^\s*-\s*/, '').trim())
        .filter(Boolean)
        .map(unquote);
    }
  }
  return {
    fm,
    body,
    data: {
      title: unquote(field('title')),
      lang: unquote(field('lang')) || 'es',
      category: unquote(field('category')),
      draft: field('draft') === 'true',
      tags,
    },
  };
}

function headingMatches(body) {
  const found = [];
  const push = (index, level, text) => {
    const clean = decodeBasic(text);
    const faq = isFaq(clean);
    if (level === 2 || faq) found.push({ index, level, text: clean, faq });
  };
  const md = /^(#{2,3})\s+(.+)$/gm;
  let m;
  while ((m = md.exec(body))) {
    push(m.index, m[1].length, m[2]);
  }
  const html = /<h([23])\b[^>]*>([\s\S]*?)<\/h\1>/gi;
  while ((m = html.exec(body))) {
    push(m.index, Number(m[1]), m[2]);
  }
  found.sort((a, b) => a.index - b.index);
  // El mismo encabezado puede casar por Markdown y por HTML; nos quedamos con el primero.
  const dedup = [];
  for (const h of found) {
    if (dedup.some((d) => Math.abs(d.index - h.index) < 4)) continue;
    dedup.push(h);
  }
  return dedup;
}

function wordsBeforeFaq(body) {
  const headings = headingMatches(body);
  const faq = headings.find((h) => h.faq);
  const slice = faq ? body.slice(0, faq.index) : body;
  return slice
    .replace(/<[^>]+>/g, ' ')
    .replace(/[#>*_\[\]()`]/g, ' ')
    .split(/\s+/)
    .filter(Boolean).length;
}

export function targetCount(words, sections) {
  // 4 si la pieza es larga. 2 si es corta (pocas secciones, o muy breve).
  // El resto, 3. Un glosario con varias secciones no baja a 2 solo por
  // quedarse cerca de las 1 000 palabras.
  if (words >= 2500 || sections >= 12) return 4;
  if (sections <= 4 || words < 700) return 2;
  return 3;
}

function isProductAside(block) {
  const flat = block.replace(/&amp;/g, '&');
  if (/dp-banner/.test(block)) return true;
  if (/border-accent/.test(block)) return true;
  if (/utm_medium=banner/.test(flat)) return true;
  const hrefs = [...flat.matchAll(/href="([^"]+)"/g)].map((m) => m[1]);
  return hrefs.some((href) => {
    const id = slugFromHref(href);
    return PRODUCT_BY_SLUG.es.has(id) || PRODUCT_BY_SLUG.en.has(id);
  });
}

function productFromHref(href) {
  const id = slugFromHref(href);
  if (!id) return null;
  const path = String(href).replace(/&amp;/g, '&');
  if (/\/(digital-products|produits-numeriques|digitale-produkte|prodotti-digitali|produtos-digitais|digitale-producten)\//.test(path)) {
    return PRODUCT_BY_SLUG.en.get(id) || PRODUCT_BY_SLUG.es.get(id) || null;
  }
  return PRODUCT_BY_SLUG.es.get(id) || PRODUCT_BY_SLUG.en.get(id) || null;
}

function existingBanners(body) {
  const re = /<aside\b[^>]*>[\s\S]*?<\/aside>/gi;
  const out = [];
  let m;
  while ((m = re.exec(body))) {
    if (!isProductAside(m[0])) continue;
    const href = /href="([^"]+)"/.exec(m[0].replace(/&amp;/g, '&'));
    const product = href ? productFromHref(href[1]) : null;
    out.push({ product, index: m.index });
  }
  return out;
}

function mediumFor(category) {
  return GLOSSARY_CATEGORIES.has(category) ? 'glosario' : 'blog';
}

export function bannerHref(productUrl, medium, slug) {
  const u = new URL(productUrl);
  u.searchParams.set('utm_source', 'aichef');
  u.searchParams.set('utm_medium', medium);
  u.searchParams.set('utm_campaign', 'productos-digitales');
  u.searchParams.set('utm_content', slug);
  return u.toString();
}

export function renderProductBanner(product) {
  const chrome = CHROME[product.catalogue] || CHROME.en;
  const href = product.href || product.url;
  return (
    `<aside class="dp-banner not-prose" data-product="${esc(product.id)}">` +
    `<img class="dp-banner__photo" src="${esc(product.image)}" alt="${esc(product.title)}" loading="lazy" decoding="async" />` +
    `<div class="dp-banner__body">` +
    `<div class="dp-banner__top">` +
    `<p class="dp-banner__tag">${esc(chrome.tag)}</p>` +
    `<img class="dp-banner__logo" src="${LOGO}" alt="AI Chef Pro" />` +
    `</div>` +
    `<p class="dp-banner__title">${esc(product.title)}</p>` +
    `<p class="dp-banner__price">${esc(product.price)}</p>` +
    `<a class="dp-banner__cta" href="${esc(href)}">${esc(chrome.cta)}</a>` +
    `</div></aside>`
  );
}

function score(postTopics, product) {
  let n = 0;
  for (const t of product.topics) if (postTopics.has(t)) n += 1;
  return n;
}

function assignCatalogue(posts, products) {
  const counts = Object.fromEntries(products.map((p) => [p.id, 0]));
  for (const post of posts) {
    for (const id of post.existingIds) {
      if (counts[id] != null) counts[id] += 1;
    }
  }

  const needOf = new Map(posts.map((p) => [p.key, p.need]));
  const chosen = new Map(posts.map((p) => [p.key, []]));

  const byScore = [...posts].filter((p) => p.need > 0).sort((a, b) => {
    const ds = b.bestScore - a.bestScore;
    if (ds) return ds;
    return a.key.localeCompare(b.key);
  });

  for (const post of byScore) {
    let topicSlots = 0;
    if (post.need === 1) topicSlots = 1;
    else if (post.need >= 2) topicSlots = post.need >= 3 ? Math.min(2, post.need - 1) : 1;
    const used = new Set(post.existingIds);
    for (let s = 0; s < topicSlots; s += 1) {
      const min = minCount(products, counts, used);
      if (min == null) break;
      // El producto de tema gana si sigue cerca del suelo (min+2). Más arriba
      // ya está cubierto y el hueco pasa a la rotación, para no apilar el
      // mismo título en todas las piezas del tema.
      const band = products.filter((p) => !used.has(p.id) && counts[p.id] <= min + 2 && score(post.topics, p) > 0);
      if (!band.length) break;
      band.sort((a, b) => {
        const ds = score(post.topics, b) - score(post.topics, a);
        if (ds) return ds;
        if (counts[a.id] !== counts[b.id]) return counts[a.id] - counts[b.id];
        return a.id.localeCompare(b.id);
      });
      const pick = band[0];
      chosen.get(post.key).push(pick);
      used.add(pick.id);
      counts[pick.id] += 1;
      needOf.set(post.key, needOf.get(post.key) - 1);
    }
  }

  const bySlug = [...posts].filter((p) => needOf.get(p.key) > 0).sort((a, b) => a.key.localeCompare(b.key));
  for (const post of bySlug) {
    const used = new Set([...post.existingIds, ...chosen.get(post.key).map((p) => p.id)]);
    let left = needOf.get(post.key);
    let guard = 0;
    while (left > 0 && guard < 8) {
      guard += 1;
      const min = minCount(products, counts, used);
      if (min == null) break;
      const band = products
        .filter((p) => !used.has(p.id) && counts[p.id] === min)
        .sort((a, b) => a.id.localeCompare(b.id));
      if (!band.length) break;
      const i = hash32(`${post.slug}:${left}:${band.length}`) % band.length;
      const pick = band[i];
      chosen.get(post.key).push(pick);
      used.add(pick.id);
      counts[pick.id] += 1;
      left -= 1;
    }
  }

  return { counts, chosen };
}

function minCount(products, counts, used) {
  let min = null;
  for (const p of products) {
    if (used.has(p.id)) continue;
    if (min == null || counts[p.id] < min) min = counts[p.id];
  }
  return min;
}

function readPosts() {
  const posts = [];
  for (const lang of readdirSync(BLOG_DIR)) {
    const dir = path.join(BLOG_DIR, lang);
    let files = [];
    try { files = readdirSync(dir); } catch { continue; }
    for (const file of files) {
      if (!file.endsWith('.md')) continue;
      const raw = readFileSync(path.join(dir, file), 'utf8');
      const { body, data } = parseFrontmatter(raw);
      if (data.draft) continue;
      const slug = file.slice(0, -3);
      const catalogue = catalogueKeyFor(data.lang || lang);
      const headings = headingMatches(body);
      const faqAt = headings.findIndex((h) => h.faq);
      const content = (faqAt === -1 ? headings : headings.slice(0, faqAt)).filter((h) => h.level === 2 && !h.faq);
      const words = wordsBeforeFaq(body);
      const sections = content.length;
      const target = targetCount(words, sections);
      const existing = existingBanners(body);
      const existingIds = existing.map((e) => e.product?.id).filter((id) => id && PRODUCT_BY_SLUG[catalogue].has(id));
      const topicText = [
        slug.replace(/-/g, ' '),
        data.title,
        (data.tags || []).join(' '),
        GLOSSARY_CATEGORIES.has(data.category) ? '' : data.category,
        content.map((h) => h.text).join(' '),
      ].join(' ');
      const topics = new Set(topicsIn(topicText));
      const products = PRODUCTS[catalogue];
      let bestScore = 0;
      for (const p of products) bestScore = Math.max(bestScore, score(topics, p));
      const need = Math.max(0, target - existing.length);
      posts.push({
        key: `${lang}/${slug}`,
        lang,
        slug,
        category: data.category,
        title: data.title,
        catalogue,
        medium: mediumFor(data.category),
        words,
        sections,
        target,
        existing: existing.length,
        existingIds,
        topics,
        bestScore,
        need,
      });
    }
  }
  return posts;
}

let cached = null;

export function getPlan() {
  if (cached) return cached;
  const posts = readPosts();
  const byCatalogue = { es: [], en: [] };
  for (const post of posts) byCatalogue[post.catalogue].push(post);

  const assigned = {};
  const totals = {};
  for (const key of ['es', 'en']) {
    const { counts, chosen } = assignCatalogue(byCatalogue[key], PRODUCTS[key]);
    assigned[key] = chosen;
    totals[key] = counts;
  }

  const byKey = new Map();
  for (const post of posts) {
    const picks = assigned[post.catalogue].get(post.key) || [];
    const add = picks.map((p) => ({
      id: p.id,
      title: p.title,
      price: p.price,
      image: p.image,
      url: p.url,
      catalogue: p.catalogue,
      href: bannerHref(p.url, post.medium, post.slug),
    }));
    byKey.set(post.key, { ...post, add });
  }

  cached = { byKey, totals, products: PRODUCTS };
  return cached;
}

export function resetPlanForTests() {
  cached = null;
}

function textOf(node) {
  if (!node) return '';
  if (node.type === 'text' || node.type === 'inlineCode') return node.value || '';
  if (node.type === 'html') return decodeBasic(node.value || '');
  if (Array.isArray(node.children)) return node.children.map(textOf).join('');
  return '';
}

function nodeRaw(node) {
  if (!node) return '';
  if (node.type === 'html') return node.value || '';
  if (node.type === 'text') return node.value || '';
  if (node.type === 'heading') return textOf(node);
  if (Array.isArray(node.children)) return node.children.map(nodeRaw).join('\n');
  return node.value || '';
}

/**
 * Encabezados del árbol en orden de lectura: h2 y, si es la FAQ, también h3.
 * Así el corte «antes de la FAQ» vale igual en Markdown y en HTML de WordPress.
 */
export function collectHeadings(tree) {
  const out = [];
  const kids = tree.children || [];
  for (let i = 0; i < kids.length; i += 1) {
    const node = kids[i];
    if (node.type === 'heading' && (node.depth === 2 || node.depth === 3)) {
      const text = decodeBasic(textOf(node));
      const faq = isFaq(text);
      if (node.depth === 2 || faq) {
        out.push({ kind: 'md', parent: tree, index: i, level: node.depth, text, faq });
      }
    } else if (node.type === 'html' && /<h[23]\b/i.test(node.value || '')) {
      const re = /<h([23])\b[^>]*>([\s\S]*?)<\/h\1>/gi;
      let m;
      let local = 0;
      while ((m = re.exec(node.value))) {
        const level = Number(m[1]);
        const text = decodeBasic(m[2]);
        const faq = isFaq(text);
        if (level === 2 || faq) {
          out.push({
            kind: 'html',
            node,
            local,
            level,
            text,
            faq,
            start: m.index,
            end: m.index + m[0].length,
          });
        }
        local += 1;
      }
    }
  }
  return out;
}

function sectionSlice(tree, headings, i) {
  const h = headings[i];
  const next = headings[i + 1];
  if (h.kind === 'html') {
    if (next && next.kind === 'html' && next.node === h.node) {
      return h.node.value.slice(h.end, next.start);
    }
    let s = h.node.value.slice(h.end);
    const startIdx = tree.children.indexOf(h.node) + 1;
    const endIdx = next
      ? (next.kind === 'md' ? next.index : tree.children.indexOf(next.node))
      : tree.children.length;
    for (let j = startIdx; j < endIdx; j += 1) s += `\n${nodeRaw(tree.children[j])}`;
    return s;
  }
  const from = h.index + 1;
  const to = next
    ? (next.kind === 'md' ? next.index : tree.children.indexOf(next.node))
    : tree.children.length;
  return tree.children.slice(from, Math.max(from, to)).map(nodeRaw).join('\n');
}

function pickSlots(sections, k) {
  if (!k || !sections.length) return [];
  const freeIdx = [];
  sections.forEach((s, i) => { if (!s.occupied) freeIdx.push(i); });
  const pool = freeIdx.length >= k ? freeIdx : sections.map((_, i) => i);
  const n = pool.length;
  const want = Math.min(k, n);
  const used = new Set();
  const chosen = [];
  for (let i = 1; i <= want; i += 1) {
    let idx = Math.round((i * n) / (want + 1)) - 1;
    idx = Math.max(0, Math.min(n - 1, idx));
    let guard = 0;
    while (used.has(idx) && guard < n) {
      idx = (idx + 1) % n;
      guard += 1;
    }
    used.add(idx);
    chosen.push(pool[idx]);
  }
  return chosen.sort((a, b) => a - b);
}

/**
 * Inserta los banners del plan en el árbol. No reparsea el artículo, así que
 * no deshace smartypants ni las tablas. Devuelve cuántos ha metido.
 */
export function applyProductBanners(tree, entry) {
  const products = entry?.add || [];
  if (!products.length) return 0;
  const headings = collectHeadings(tree);
  const faqAt = headings.findIndex((h) => h.faq);
  const content = (faqAt === -1 ? headings : headings.slice(0, faqAt)).filter((h) => h.level === 2 && !h.faq);
  if (!content.length) {
    // Sin h2: al final del cuerpo, que sigue estando antes de la FAQ del layout y del CTA.
    tree.children.push({ type: 'html', value: products.map(renderProductBanner).join('\n') });
    return products.length;
  }
  const sections = content.map((h) => {
    const abs = headings.indexOf(h);
    return { h, abs, occupied: productAsideIn(sectionSlice(tree, headings, abs)) };
  });
  const slots = pickSlots(sections, products.length);
  const htmlEdits = [];
  const siblingEdits = [];
  slots.forEach((si, k) => {
    const html = renderProductBanner(products[k]);
    const h = sections[si].h;
    const next = headings[sections[si].abs + 1];
    if (h.kind === 'html' && next && next.kind === 'html' && next.node === h.node) {
      htmlEdits.push({ node: h.node, pos: next.start, html });
    } else if (h.kind === 'html' && !next) {
      htmlEdits.push({ node: h.node, pos: h.node.value.length, html });
    } else if (next && next.kind === 'md') {
      siblingEdits.push({ index: next.index, html });
    } else if (next && next.kind === 'html') {
      siblingEdits.push({ index: tree.children.indexOf(next.node), html });
    } else if (h.kind === 'md') {
      siblingEdits.push({ index: tree.children.length, html });
    } else {
      siblingEdits.push({ index: tree.children.indexOf(h.node) + 1, html });
    }
  });

  const byNode = new Map();
  for (const edit of htmlEdits) {
    if (!byNode.has(edit.node)) byNode.set(edit.node, []);
    byNode.get(edit.node).push(edit);
  }
  for (const edits of byNode.values()) {
    edits.sort((a, b) => b.pos - a.pos);
    for (const edit of edits) {
      const node = edit.node;
      node.value = `${node.value.slice(0, edit.pos)}\n${edit.html}\n${node.value.slice(edit.pos)}`;
    }
  }
  siblingEdits.sort((a, b) => b.index - a.index);
  for (const edit of siblingEdits) {
    const at = edit.index < 0 ? tree.children.length : edit.index;
    tree.children.splice(at, 0, { type: 'html', value: edit.html });
  }
  return slots.length;
}

function productAsideIn(slice) {
  const re = /<aside\b[^>]*>[\s\S]*?<\/aside>/gi;
  let m;
  while ((m = re.exec(slice))) {
    if (isProductAside(m[0])) return true;
  }
  return false;
}

export function remarkProductBanners() {
  const plan = getPlan();
  return function transformer(tree, file) {
    if (tree.data?.dpBannersApplied) return;
    const key = keyFromVFile(file);
    if (!key) return;
    const entry = plan.byKey.get(key);
    if (!entry?.add?.length) return;
    applyProductBanners(tree, entry);
    tree.data = tree.data || {};
    tree.data.dpBannersApplied = true;
  };
}

function keyFromVFile(file) {
  const candidates = [file?.path, ...(file?.history || [])].filter(Boolean);
  for (const p of candidates) {
    const m = String(p).match(/content\/blog\/([a-z]{2})\/([^/]+)\.md$/);
    if (m) return `${m[1]}/${m[2]}`;
  }
  const fm = file?.data?.astro?.frontmatter;
  const stem = file?.stem;
  if (fm?.lang && stem) return `${fm.lang}/${stem}`;
  return null;
}

export function appearanceRows() {
  const plan = getPlan();
  const rows = [];
  for (const catalogue of ['es', 'en']) {
    const added = Object.fromEntries(PRODUCTS[catalogue].map((p) => [p.id, 0]));
    const pieces = Object.fromEntries(PRODUCTS[catalogue].map((p) => [p.id, 0]));
    for (const entry of plan.byKey.values()) {
      if (entry.catalogue !== catalogue) continue;
      const seen = new Set();
      for (const id of entry.existingIds) {
        if (added[id] == null) continue;
        seen.add(id);
      }
      for (const p of entry.add) {
        added[p.id] += 1;
        seen.add(p.id);
      }
      for (const id of seen) pieces[id] += 1;
    }
    for (const p of PRODUCTS[catalogue]) {
      const existing = plan.totals[catalogue][p.id] - added[p.id];
      rows.push({
        catalogue,
        id: p.id,
        title: p.title,
        price: p.price,
        url: p.url,
        existing,
        added: added[p.id],
        total: existing + added[p.id],
        pieces: pieces[p.id],
      });
    }
  }
  return rows;
}
