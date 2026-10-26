/**
 * Reparto de banners de producto en el blog y el glosario.
 * No toca los Markdown: lee el mismo plan que el plugin de remark.
 *
 *   node scripts/astro-migration/product-banner-report.mjs [csv-out]
 */
import { writeFileSync } from 'node:fs';
import { appearanceRows, getPlan } from '../../astro-site/src/lib/product-banners.mjs';

const plan = getPlan();
const rows = appearanceRows();
const out = process.argv[2];

const header = ['catalogue', 'id', 'title', 'price', 'existing', 'added', 'total', 'pieces', 'url'];
const lines = [header.join(',')];
for (const row of rows) {
  const cells = header.map((key) => {
    const value = String(row[key] ?? '');
    return /[",\n]/.test(value) ? `"${value.replace(/"/g, '""')}"` : value;
  });
  lines.push(cells.join(','));
}
const csv = `${lines.join('\n')}\n`;
if (out) writeFileSync(out, csv);

for (const catalogue of ['es', 'en']) {
  const subset = rows.filter((row) => row.catalogue === catalogue);
  const totals = subset.map((row) => row.total).sort((a, b) => a - b);
  const sum = (key) => subset.reduce((acc, row) => acc + row[key], 0);
  console.log(
    `${catalogue} products=${subset.length} min=${totals[0]} median=${totals[Math.floor(totals.length / 2)]} max=${totals.at(-1)} existing=${sum('existing')} added=${sum('added')} total=${sum('total')}`,
  );
}
const quota = {};
for (const entry of plan.byKey.values()) {
  const got = entry.existing + entry.add.length;
  const key = `${entry.lang} ${got}/${entry.target}`;
  quota[key] = (quota[key] || 0) + 1;
}
console.log('posts', plan.byKey.size);
console.log(quota);
if (out) console.log('csv', out);
