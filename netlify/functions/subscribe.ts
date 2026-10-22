import type { Handler } from '@netlify/functions';

/**
 * Alta de captación (imán de la calculadora de food cost y newsletter del footer).
 *
 * Guarda el email en Resend, en un segmento por idioma (las «audiencias» de
 * Resend pasaron a llamarse segmentos en noviembre de 2025; el endpoint
 * /audiences está deprecado). No es el segmento de compradores «AI Chef Pro ES/EN»:
 * es una lista de captación, para no mezclar leads con los broadcasts de producto.
 *
 * Variables (scope functions en Netlify):
 *   RESEND_API_KEY            — obligatoria. Ya la usan verify-purchase y el resto.
 *                               Si falta, esta función responde 503 not_configured
 *                               y no guarda nada.
 *   RESEND_AUDIENCE_ES … _NL — id del segmento de captación de ese idioma.
 *                               Si falta, la función busca o crea un segmento
 *                               llamado «Captación XX» (ES, EN, FR, DE, IT, PT, NL).
 *
 * No registra IP ni user-agent. El consentimiento tiene que llegar en true.
 */

const LOCALES = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as const;
type Locale = (typeof LOCALES)[number];

const SOURCES = ['food-cost', 'newsletter'] as const;

const SEGMENT_NAME: Record<Locale, string> = {
  es: 'Captación ES',
  en: 'Captación EN',
  fr: 'Captación FR',
  de: 'Captación DE',
  it: 'Captación IT',
  pt: 'Captación PT',
  nl: 'Captación NL',
};

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const MAX_PER_MINUTE = 8;

const hits = new Map<string, number[]>();
const segmentCache = new Map<string, string>();

function json(status: number, body: Record<string, unknown>) {
  return {
    statusCode: status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
    body: JSON.stringify(body),
  };
}

function limited(key: string): boolean {
  const now = Date.now();
  const windowStart = now - 60_000;
  const prev = (hits.get(key) ?? []).filter((t) => t > windowStart);
  if (prev.length >= MAX_PER_MINUTE) {
    hits.set(key, prev);
    return true;
  }
  prev.push(now);
  hits.set(key, prev);
  return false;
}

async function resend(path: string, init: RequestInit = {}): Promise<Response> {
  const key = process.env.RESEND_API_KEY;
  if (!key) throw new Error('no-key');
  return fetch(`https://api.resend.com${path}`, {
    ...init,
    headers: {
      Authorization: `Bearer ${key}`,
      'Content-Type': 'application/json',
      ...(init.headers ?? {}),
    },
  });
}

async function segmentId(lang: Locale): Promise<string> {
  const envName = `RESEND_AUDIENCE_${lang.toUpperCase()}`;
  const fromEnv = process.env[envName]?.trim();
  if (fromEnv) return fromEnv;
  const cached = segmentCache.get(lang);
  if (cached) return cached;

  const wanted = SEGMENT_NAME[lang];
  const listed = await resend('/segments?limit=100');
  if (listed.ok) {
    const payload = (await listed.json()) as { data?: { id?: string; name?: string }[] };
    const found = payload.data?.find((s) => s.name === wanted && s.id);
    if (found?.id) {
      segmentCache.set(lang, found.id);
      return found.id;
    }
  }

  const created = await resend('/segments', {
    method: 'POST',
    body: JSON.stringify({ name: wanted }),
  });
  if (created.ok) {
    const payload = (await created.json()) as { id?: string };
    if (payload.id) {
      segmentCache.set(lang, payload.id);
      return payload.id;
    }
  }

  throw new Error('segment');
}

async function saveContact(email: string, segment: string): Promise<void> {
  const created = await resend('/contacts', {
    method: 'POST',
    body: JSON.stringify({
      email,
      unsubscribed: false,
      segments: [{ id: segment }],
    }),
  });
  if (created.ok) return;

  // Contacto ya existente: se añade al segmento sin reactivar una baja global.
  if (created.status === 409 || created.status === 422) {
    const added = await resend(
      `/contacts/${encodeURIComponent(email)}/segments/${encodeURIComponent(segment)}`,
      { method: 'POST' },
    );
    if (added.ok || added.status === 409) return;
  }
  throw new Error('contact');
}

export const handler: Handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, body: '' };
  }
  if (event.httpMethod !== 'POST') {
    return json(405, { ok: false, error: 'method' });
  }

  const raw = event.headers ?? {};
  const ip =
    raw['x-nf-client-connection-ip'] ||
    raw['x-forwarded-for']?.split(',')[0]?.trim() ||
    'unknown';
  if (limited(ip)) {
    return json(429, { ok: false, error: 'rate_limited' });
  }

  let body: Record<string, unknown>;
  try {
    body = JSON.parse(event.body || '');
  } catch {
    return json(400, { ok: false, error: 'invalid_json' });
  }

  // Honeypot: los bots rellenan `company`. Respondemos ok y no guardamos.
  if (typeof body.company === 'string' && body.company.trim() !== '') {
    return json(200, { ok: true });
  }

  const email = typeof body.email === 'string' ? body.email.trim().toLowerCase() : '';
  const lang = typeof body.lang === 'string' ? body.lang : '';
  const source = typeof body.source === 'string' ? body.source : '';

  if (!LOCALES.includes(lang as Locale)) {
    return json(400, { ok: false, error: 'invalid_lang' });
  }
  if (!SOURCES.includes(source as (typeof SOURCES)[number])) {
    return json(400, { ok: false, error: 'invalid_source' });
  }
  if (!email || email.length > 320 || !EMAIL_RE.test(email)) {
    return json(400, { ok: false, error: 'invalid_email' });
  }
  if (body.consent !== true) {
    return json(400, { ok: false, error: 'consent_required' });
  }
  if (!process.env.RESEND_API_KEY) {
    console.error('[subscribe] falta RESEND_API_KEY');
    return json(503, { ok: false, error: 'not_configured' });
  }

  try {
    const segment = await segmentId(lang as Locale);
    await saveContact(email, segment);
    console.log(`[subscribe] ok lang=${lang} source=${source}`);
    return json(200, { ok: true });
  } catch (err) {
    console.error('[subscribe] upstream', err instanceof Error ? err.message : 'error');
    return json(502, { ok: false, error: 'upstream' });
  }
};
