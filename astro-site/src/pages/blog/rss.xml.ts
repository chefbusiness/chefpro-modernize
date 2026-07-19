// Fase 8B — Feed RSS del blog (ES): /blog/rss.xml. Sin dependencias externas.
import { SITE } from '../../i18n/config';
import { getPublishedPosts, postSlug } from '../../lib/blog';

const esc = (s: string): string =>
  s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

export async function GET() {
  const posts = (await getPublishedPosts('es')).slice(0, 30);
  const items = posts
    .map((p) => {
      const url = `${SITE}/blog/${postSlug(p)}`;
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
    <title>Blog de AI Chef Pro</title>
    <link>${SITE}/blog</link>
    <atom:link href="${SITE}/blog/rss.xml" rel="self" type="application/rss+xml" />
    <description>Inteligencia artificial para restaurantes y hostelería: guías, prompts, food cost y técnica culinaria profesional.</description>
    <language>es</language>
${items}
  </channel>
</rss>`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
}
