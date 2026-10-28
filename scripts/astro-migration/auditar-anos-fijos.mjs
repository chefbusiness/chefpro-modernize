/**
 * Lista años fijos (20xx) en title, meta description, H1 y og:title
 * de las landings públicas. No modifica nada.
 *
 *   node scripts/astro-migration/auditar-anos-fijos.mjs
 *
 * No entra en scripts/productos-digitales, ni en la zona app (access, library,
 * admin), ni en la SPA de src/pages. Los textos de las landings públicas de
 * producto sí se leen: son los que salen en el HTML.
 *
 * La sugerencia es solo una pista:
 *   evergreen — el año parece de caducidad anual (candidato a {year})
 *   dato real — norma, fecha, hito o no está claro que caduque; no sustituir
 */
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../..', import.meta.url));
const ROOTS = [
  'astro-site/src/pages',
  'astro-site/src/layouts',
  'astro-site/src/components',
  'astro-site/src/data',
  'astro-site/src/lib/marketing-heads',
  'astro-site/src/content/blog',
  'src/i18n/locales',
  'netlify/edge-functions/og-meta.ts',
];
const TEXT_EXT = new Set(['.astro', '.ts', '.tsx', '.mjs', '.js', '.json', '.md']);
const HERO_H1_KEYS = new Set([
  'title',
  'titlePre',
  'titleGold',
  'subtitleLine',
  'v2_title_prefix',
  'v2_title_suffix',
  'title_brand',
]);

function shouldSkip(rel) {
  if (rel.includes('/admin/')) return true;
  if (/(^|\/)(access|library)\.astro$/.test(rel)) return true;
  if (/-(access|library)\.astro$/.test(rel)) return true;
  return false;
}

function walk(abs, rel, acc) {
  let st;
  try {
    st = statSync(abs);
  } catch {
    return;
  }
  if (st.isFile()) {
    acc.push({ abs, rel: rel.replaceAll('\\', '/') });
    return;
  }
  for (const name of readdirSync(abs)) {
    if (name === 'node_modules' || name === 'dist' || name === '.astro') continue;
    const childRel = rel ? `${rel}/${name}` : name;
    if (shouldSkip(childRel)) continue;
    walk(join(abs, name), childRel, acc);
  }
}

const MONTH_NAMES = [
  'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
  'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december',
  'janvier', 'février', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'aout', 'septembre', 'octobre', 'novembre', 'décembre', 'decembre',
  'januar', 'februar', 'märz', 'marz', 'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'dezember',
  'gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre',
  'janeiro', 'fevereiro', 'março', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro',
  'januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december',
].join('|');

function classify(text, year, field) {
  const y = String(year);
  if (new RegExp(`\\b${y}-\\d{2}-\\d{2}\\b`).test(text)) return 'dato real';
  if (new RegExp(`\\b\\d{1,2}[/.-]\\d{1,2}[/.-]${y}\\b`).test(text)) return 'dato real';
  if (new RegExp(`\\b\\d{1,2}\\s+de\\s+(?:${MONTH_NAMES})\\s+de\\s+${y}\\b`, 'i').test(text)) return 'dato real';
  if (new RegExp(`\\b(?:${MONTH_NAMES})\\s+\\d{1,2},?\\s+${y}\\b`, 'i').test(text)) return 'dato real';
  if (new RegExp(`\\b\\d{1,4}/${y}\\b`).test(text)) return 'dato real';
  if (new RegExp(`\\b(RD|R\\.?D\\.?|Ley|Reglamento|Directiva|BOE|ISO|UNE|DOUE)\\b[\\s\\S]{0,48}\\b${y}\\b`, 'i').test(text)) {
    return 'dato real';
  }
  if (new RegExp(`\\b(desde|since|depuis|seit|dal|sinds|desde o|a partir de)\\s+${y}\\b`, 'i').test(text)) {
    return 'dato real';
  }
  if (Number(y) <= 2024) return 'dato real';
  if (new RegExp(`\\b(en|para|in|for|pour|für|nel|em|anno)\\s+${y}\\b`, 'i').test(text)) return 'evergreen';
  if (new RegExp(`\\b(España|Spain|France|Italia|Deutschland|Nederland|Portugal)\\s+${y}\\b`, 'i').test(text)) {
    return 'evergreen';
  }
  if (new RegExp(`\\(${y}\\)`).test(text)) return 'evergreen';
  if (new RegExp(`\\b${y}\\s*[:|—–-]\\s`).test(text) || new RegExp(`[:|—–-]\\s*${y}\\b`).test(text)) return 'evergreen';
  if (new RegExp(`\\b${y}\\s*$`).test(text)) return 'evergreen';
  if (new RegExp(`\\b(guía|guia|guide|mejores|best|beste|besten|meilleures?|migliori|melhores|melhor|checklist|tendencias|trends|actualizado|updated|édition|edizione|editie|comparativa|comparatif|comparativo)\\b[\\s\\S]{0,48}\\b${y}\\b`, 'i').test(text)) {
    return 'evergreen';
  }
  if (new RegExp(`\\b${y}\\b[\\s\\S]{0,48}\\b(guía|guia|guide|mejores|best|beste|besten|meilleures?|migliori|melhores|melhor)\\b`, 'i').test(text)) return 'evergreen';
  if (new RegExp(`©\\s*${y}\\b`).test(text)) return 'evergreen';
  if ((field === 'title' || field === 'h1' || field === 'og:title' || field === 'json-ld headline') && Number(y) >= 2025) {
    return 'evergreen';
  }
  return 'dato real';
}

function clip(text) {
  const clean = text.replace(/\s+/g, ' ').trim();
  return clean.length > 220 ? `${clean.slice(0, 217)}...` : clean;
}

function addYears(rows, file, field, text) {
  if (!text || !/\b20\d{2}\b/.test(text)) return;
  const full = text.replace(/\s+/g, ' ').trim();
  const shown = clip(full);
  const seen = new Set();
  for (const match of full.matchAll(/\b(20\d{2})\b/g)) {
    if (seen.has(match[1])) continue;
    seen.add(match[1]);
    const kind = classify(full, match[1], field);
    rows.push({
      file,
      field,
      text: shown,
      suggestion: kind === 'evergreen'
        ? `evergreen — candidato a {year} (aparece ${match[1]})`
        : `dato real — no sustituir (${match[1]})`,
    });
  }
}

function fieldFor(stack, key, rel) {
  if (!key || key.includes(' ')) return null;
  const named = stack.filter(Boolean);
  const parent = named[named.length - 1] ?? null;
  if (key === 'title' && parent === 'seo') return 'title';
  if (key === 'description' && parent === 'seo') return 'meta description';
  if (key === 'seo_title') return 'title';
  if (key === 'seo_description') return 'meta description';
  if (parent === 'hero' && HERO_H1_KEYS.has(key)) return 'h1';
  if (key === 'h1') return 'h1';
  if (key === 'headline') return 'json-ld headline';
  if (rel.endsWith('og-meta.ts') && key === 'title') return 'og:title';
  if (rel.endsWith('og-meta.ts') && key === 'description') return 'meta description';
  if (key === 'og_title' || key === 'ogTitle') return 'og:title';
  return null;
}

function scanStrings(src, rel, rows) {
  let i = 0;
  const keyStack = [];
  let pendingKey = null;

  function skipWsAndComments() {
    while (i < src.length) {
      const c = src[i];
      if (c === ' ' || c === '\n' || c === '\r' || c === '\t') {
        i += 1;
        continue;
      }
      if (c === '/' && src[i + 1] === '/') {
        while (i < src.length && src[i] !== '\n') i += 1;
        continue;
      }
      if (c === '/' && src[i + 1] === '*') {
        i += 2;
        while (i < src.length && !(src[i] === '*' && src[i + 1] === '/')) i += 1;
        i += 2;
        continue;
      }
      break;
    }
  }

  function readQuoted(quote) {
    let out = '';
    i += 1;
    while (i < src.length) {
      if (src[i] === '\\') {
        const next = src[i + 1] ?? '';
        out += next === 'n' ? '\n' : next;
        i += 2;
        continue;
      }
      if (src[i] === quote) {
        i += 1;
        return out;
      }
      out += src[i];
      i += 1;
    }
    return out;
  }

  function readTemplate() {
    let out = '';
    i += 1;
    while (i < src.length) {
      if (src[i] === '\\') {
        out += src[i + 1] ?? '';
        i += 2;
        continue;
      }
      if (src[i] === '`') {
        i += 1;
        return out;
      }
      if (src[i] === '$' && src[i + 1] === '{') {
        i += 2;
        let depth = 1;
        while (i < src.length && depth > 0) {
          if (src[i] === '{') depth += 1;
          else if (src[i] === '}') depth -= 1;
          i += 1;
        }
        continue;
      }
      out += src[i];
      i += 1;
    }
    return out;
  }

  while (i < src.length) {
    skipWsAndComments();
    if (i >= src.length) break;
    const c = src[i];
    if (c === '"' || c === "'" || c === '`') {
      const value = c === '`' ? readTemplate() : readQuoted(c);
      const checkpoint = i;
      skipWsAndComments();
      if (src[i] === ':') {
        pendingKey = value;
        i += 1;
        continue;
      }
      i = checkpoint;
      const field = fieldFor(keyStack, pendingKey, rel);
      if (field) addYears(rows, rel, field, value);
      pendingKey = null;
      continue;
    }
    if (c === '{') {
      keyStack.push(pendingKey);
      pendingKey = null;
      i += 1;
      continue;
    }
    if (c === '}') {
      keyStack.pop();
      pendingKey = null;
      i += 1;
      continue;
    }
    if (c === ',' || c === ';') {
      pendingKey = null;
      i += 1;
      continue;
    }
    const ident = src.slice(i).match(/^[A-Za-z_$][\w$]*/);
    if (ident) {
      const name = ident[0];
      i += name.length;
      const checkpoint = i;
      skipWsAndComments();
      if (src[i] === ':') {
        pendingKey = name;
        i += 1;
      } else {
        i = checkpoint;
      }
      continue;
    }
    i += 1;
  }
}

function scanAssignments(src, rel, rows) {
  if (!/\/(pages|layouts)\//.test(rel)) return;
  const specs = [
    [/title/g, 'title'],
    [/description/g, 'meta description'],
  ];
  for (const [nameRe, field] of specs) {
    const re = new RegExp(`(?:const|let)\\s+${nameRe.source}\\s*=\\s*(['"])([\\s\\S]*?)\\1`, 'g');
    for (const match of src.matchAll(re)) addYears(rows, rel, field, match[2]);
  }
}

function withoutComments(src) {
  return src
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/^\s*\/\/.*$/gm, '')
    .replace(/<!--[\s\S]*?-->/g, '');
}

function scanH1(src, rel, rows) {
  const visible = withoutComments(src);
  for (const match of visible.matchAll(/<h1\b[^>]*>[\s\S]*?<\/h1>/gi)) {
    const text = match[0].replace(/<[^>]+>/g, ' ').replace(/\{[^}]*\}/g, ' ');
    addYears(rows, rel, 'h1', text);
  }
}

function scanMeta(src, rel, rows) {
  for (const match of withoutComments(src).matchAll(/<meta\b[^>]*>/gi)) {
    const tag = match[0];
    const kind = tag.match(/\b(?:name|property)\s*=\s*(["'])(description|og:title|twitter:title)\1/i);
    if (!kind) continue;
    const content = tag.match(/\bcontent\s*=\s*(["'])([\s\S]*?)\1/i);
    if (!content) continue;
    const field = kind[2].toLowerCase() === 'description' ? 'meta description' : kind[2].toLowerCase();
    addYears(rows, rel, field, content[2]);
  }
}

function scanFrontmatter(src, rel, rows) {
  const fm = src.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fm) return;
  const lines = fm[1].split(/\r?\n/);
  for (let i = 0; i < lines.length; i += 1) {
    const match = lines[i].match(/^(title|description):\s*(.*)$/);
    if (!match) continue;
    let val = match[2].trim();
    if (val === '>' || val === '|' || val === '>-' || val === '|-') {
      const acc = [];
      let j = i + 1;
      for (; j < lines.length; j += 1) {
        if (/^\s+\S/.test(lines[j])) acc.push(lines[j].trim());
        else break;
      }
      val = acc.join(' ');
      i = j - 1;
    }
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
      val = val.slice(1, -1);
    }
    addYears(rows, rel, match[1] === 'title' ? 'title' : 'meta description', val);
  }
}

function scanJson(src, rel, rows) {
  let data;
  try {
    data = JSON.parse(src);
  } catch {
    return;
  }
  const walkJson = (value, stack) => {
    if (typeof value === 'string') {
      const field = fieldFor(stack.slice(0, -1), stack[stack.length - 1], rel);
      if (field) addYears(rows, rel, field, value);
      return;
    }
    if (Array.isArray(value)) {
      for (const item of value) walkJson(item, stack);
      return;
    }
    if (value && typeof value === 'object') {
      for (const [key, child] of Object.entries(value)) walkJson(child, stack.concat(key));
    }
  };
  walkJson(data, []);
}

function extOf(rel) {
  const dot = rel.lastIndexOf('.');
  return dot === -1 ? '' : rel.slice(dot);
}

const files = [];
for (const rel of ROOTS) walk(join(ROOT, rel), rel, files);

const rows = [];
for (const file of files) {
  const ext = extOf(file.rel);
  if (!TEXT_EXT.has(ext)) continue;
  const src = readFileSync(file.abs, 'utf8');
  if (ext === '.md') {
    scanFrontmatter(src, file.rel, rows);
    continue;
  }
  if (ext === '.json') {
    scanJson(src, file.rel, rows);
    continue;
  }
  scanStrings(src, file.rel, rows);
  scanAssignments(src, file.rel, rows);
  if (ext === '.astro' || ext === '.tsx') {
    scanH1(src, file.rel, rows);
    scanMeta(src, file.rel, rows);
  }
}

const seen = new Set();
const unique = rows.filter((row) => {
  const key = `${row.file}\t${row.field}\t${row.text}\t${row.suggestion}`;
  if (seen.has(key)) return false;
  seen.add(key);
  return true;
});
unique.sort((a, b) => a.file.localeCompare(b.file) || a.field.localeCompare(b.field) || a.text.localeCompare(b.text));

const evergreen = unique.filter((row) => row.suggestion.startsWith('evergreen')).length;
const real = unique.length - evergreen;
console.log(`Resumen: ${unique.length} hallazgos. Evergreen: ${evergreen}. Dato real: ${real}.`);
console.log('La auditoría no modifica ficheros.');
console.log('');
console.log(['archivo', 'campo', 'texto', 'sugerencia'].join('\t'));
for (const row of unique) {
  console.log([row.file, row.field, row.text, row.suggestion].join('\t'));
}
