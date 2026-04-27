// Edge Function: Auto-detect user language on root "/" and redirect to the
// matching language-prefixed home (e.g. /en, /de, /fr). Runs at the edge so
// the user lands directly on the right URL without flash-of-Spanish.
//
// Priority order:
//   1. URL prefix (e.g. /de, /en) — handled by absence of "/" match, no-op here
//   2. Cookie "preferred-lang" — user already chose, respect it
//   3. Browser Accept-Language header
//   4. Geo-IP country code (provided by Netlify context.geo)
//   5. Default to English (NOT Spanish) for unknown countries
//
// Bots are skipped so Googlebot etc. continue indexing "/" as Spanish canonical.
// Query param ?nolang=1 disables the redirect (escape hatch for debugging).

const SUPPORTED = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as const;
type Lang = typeof SUPPORTED[number];

const COUNTRY_TO_LANG: Record<string, Lang> = {
  // Spanish-speaking
  ES: 'es', MX: 'es', AR: 'es', CO: 'es', PE: 'es', CL: 'es', VE: 'es',
  UY: 'es', EC: 'es', BO: 'es', PY: 'es', CR: 'es', GT: 'es', HN: 'es',
  NI: 'es', PA: 'es', SV: 'es', DO: 'es', CU: 'es', PR: 'es',
  // English
  US: 'en', GB: 'en', CA: 'en', AU: 'en', NZ: 'en', IE: 'en', IN: 'en',
  ZA: 'en', SG: 'en', PH: 'en', MY: 'en', NG: 'en', KE: 'en',
  // French
  FR: 'fr', MC: 'fr', LU: 'fr', SN: 'fr', CI: 'fr',
  // German
  DE: 'de', AT: 'de', LI: 'de',
  // Italian
  IT: 'it', SM: 'it', VA: 'it',
  // Portuguese
  PT: 'pt', BR: 'pt', AO: 'pt', MZ: 'pt', CV: 'pt',
  // Dutch
  NL: 'nl',
};

const BOT_REGEX = /bot|crawler|spider|googlebot|bingbot|baiduspider|yandex|duckduckbot|facebookexternalhit|twitterbot|linkedinbot|whatsapp|slackbot|telegrambot|applebot|chrome-lighthouse|ahrefsbot|semrushbot|mj12bot|petalbot/i;

function parseAcceptLanguage(header: string | null): Lang | null {
  if (!header) return null;
  const parsed = header.split(',').map((part) => {
    const [tag, qPart] = part.trim().split(';');
    const qStr = qPart && qPart.startsWith('q=') ? qPart.slice(2) : '1';
    const q = parseFloat(qStr);
    return { tag: (tag || '').toLowerCase(), q: isNaN(q) ? 1.0 : q };
  }).sort((a, b) => b.q - a.q);

  for (const { tag } of parsed) {
    const base = tag.split('-')[0];
    if ((SUPPORTED as readonly string[]).includes(base)) return base as Lang;
  }
  return null;
}

interface NetlifyContext {
  geo?: {
    country?: {
      code?: string;
      name?: string;
    };
  };
}

export default async (request: Request, context: NetlifyContext) => {
  const url = new URL(request.url);

  // Only act on root "/" — language-prefixed paths (/en, /de, /fr/...) pass through
  if (url.pathname !== '/') return;

  // Skip bots so they keep indexing "/" as Spanish canonical
  const ua = request.headers.get('user-agent') || '';
  if (BOT_REGEX.test(ua)) return;

  // Honor user's persisted choice — if cookie is set, do not redirect
  const cookie = request.headers.get('cookie') || '';
  if (/(?:^|;\s*)preferred-lang=([a-z]{2})/.test(cookie)) return;

  // Escape hatch for QA / debugging
  if (url.searchParams.has('nolang')) return;

  // 1. Browser language (highest priority for users with localized devices)
  let target = parseAcceptLanguage(request.headers.get('accept-language'));

  // 2. Fall back to geo-IP country
  if (!target) {
    const country = (context.geo?.country?.code || '').toUpperCase();
    target = COUNTRY_TO_LANG[country] || 'en';
  }

  // Spanish is served at "/" — no redirect needed
  if (target === 'es') return;

  // 302 (not 301) so search engines do not treat it as permanent canonical change.
  // Vary headers ensure CDN caches respect language and cookie variations.
  return new Response(null, {
    status: 302,
    headers: {
      'Location': `/${target}`,
      'Vary': 'Accept-Language, Cookie',
      'Cache-Control': 'private, no-cache, no-store, must-revalidate',
    },
  });
};
