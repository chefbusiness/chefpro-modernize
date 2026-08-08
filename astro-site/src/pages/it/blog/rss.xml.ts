// Fase 9 (2026-08-08) — Feed RSS del blog IT: /it/blog/rss.xml. Sin dependencias
// externas (mismo conversor que los feeds ES y EN, con las URLs y el <language>
// del árbol IT).
import { SITE } from '../../../i18n/config';
import { blogBase, getPublishedPosts, postPath, postSlug } from '../../../lib/blog';

const esc = (s: string): string =>
  s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

export async function GET() {
  const posts = (await getPublishedPosts('it')).slice(0, 30);
  const items = posts
    .map((p) => {
      const url = `${SITE}${postPath(postSlug(p), 'it')}`;
      return `    <item>
      <title>${esc(p.data.title)}</title>
      <link>${url}</link>
      <guid isPermaLink="true">${url}</guid>
      <description>${esc(p.data.description)}</description>
      <pubDate>${p.data.pubDate.toUTCString()}</pubDate>
    </item>`;
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Blog AI Chef Pro</title>
    <link>${SITE}${blogBase('it')}</link>
    <atom:link href="${SITE}${blogBase('it')}/rss.xml" rel="self" type="application/rss+xml" />
    <description>Intelligenza artificiale per ristoranti e ristorazione: guide, prompt, food cost e tecnica di cucina professionale.</description>
    <language>it</language>
${items}
  </channel>
</rss>`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
}
