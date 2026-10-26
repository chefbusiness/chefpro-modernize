import { SITE } from '../../../i18n/config';
import { blogBase, getPublishedPosts, postPath, postSlug } from '../../../lib/blog';

const esc = (s: string): string =>
  s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');

export async function GET() {
  const posts = (await getPublishedPosts('nl')).slice(0, 30);
  const items = posts
    .map((p) => {
      const url = `${SITE}${postPath(postSlug(p), 'nl')}`;
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
    <link>${SITE}${blogBase('nl')}</link>
    <atom:link href="${SITE}${blogBase('nl')}/rss.xml" rel="self" type="application/rss+xml" />
    <description>AI voor restaurants en horeca: de 14 allergenen, de allergenenlijst, voedselveiligheid en keukentechniek.</description>
    <language>nl</language>
${items}
  </channel>
</rss>`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' },
  });
}
