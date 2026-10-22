/**
 * Captación de email (calculadora de food cost y newsletter del footer).
 *
 * Destino: un segmento de Resend POR IDIOMA, distinto de las listas de
 * producto «AI Chef Pro ES/EN» (esas son broadcasts de la tienda). El nombre
 * estable es `aichef.pro captacion <lang>`. Si existe
 * `RESEND_CAPTURE_SEGMENT_<LANG>` se usa ese id y no se crea nada.
 *
 * `RESEND_API_KEY` es la misma que ya usan `resend-access` y `verify-purchase`.
 * Si falta, la función responde `misconfigured` y no guarda nada.
 */

export const CAPTURE_LANGS = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as const;
export type CaptureLang = (typeof CAPTURE_LANGS)[number];

export const CAPTURE_SOURCES = ['food-cost-calculator', 'footer-newsletter'] as const;
export type CaptureSource = (typeof CAPTURE_SOURCES)[number];

export const CONSENT_VERSION = 'gdpr-2026-10-22';

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const MAX_EMAIL = 254;
const MAX_PAGE = 200;

export interface CaptureInput {
  email: string;
  lang: CaptureLang;
  source: CaptureSource;
  page?: string;
}

export type ParseResult =
  | { ok: true; honeypot: true }
  | { ok: true; honeypot: false; value: CaptureInput }
  | { ok: false; error: 'invalid_json' | 'invalid_email' | 'invalid_lang' | 'invalid_source' | 'consent_required' };

export function segmentName(lang: CaptureLang): string {
  return `aichef.pro captacion ${lang}`;
}

export function segmentEnvKey(lang: CaptureLang): string {
  return `RESEND_CAPTURE_SEGMENT_${lang.toUpperCase()}`;
}

export function parseCaptureBody(raw: unknown): ParseResult {
  if (!raw || typeof raw !== 'object') return { ok: false, error: 'invalid_json' };
  const body = raw as Record<string, unknown>;

  if (typeof body.website === 'string' && body.website.trim() !== '') {
    return { ok: true, honeypot: true };
  }

  if (body.consent !== true) return { ok: false, error: 'consent_required' };

  if (typeof body.email !== 'string') return { ok: false, error: 'invalid_email' };
  const email = body.email.trim().toLowerCase();
  if (email.length < 3 || email.length > MAX_EMAIL || !EMAIL_RE.test(email)) {
    return { ok: false, error: 'invalid_email' };
  }

  if (typeof body.lang !== 'string' || !(CAPTURE_LANGS as readonly string[]).includes(body.lang)) {
    return { ok: false, error: 'invalid_lang' };
  }

  if (typeof body.source !== 'string' || !(CAPTURE_SOURCES as readonly string[]).includes(body.source)) {
    return { ok: false, error: 'invalid_source' };
  }

  let page: string | undefined;
  if (typeof body.page === 'string' && body.page.trim()) {
    page = body.page.trim().slice(0, MAX_PAGE);
  }

  return {
    ok: true,
    honeypot: false,
    value: {
      email,
      lang: body.lang as CaptureLang,
      source: body.source as CaptureSource,
      page,
    },
  };
}

export function originAllowed(origin: string | undefined | null): boolean {
  if (!origin) return true;
  let url: URL;
  try {
    url = new URL(origin);
  } catch {
    return false;
  }
  const host = url.hostname;
  if (host === 'localhost' || host === '127.0.0.1') return url.protocol === 'http:' || url.protocol === 'https:';
  if (url.protocol !== 'https:') return false;
  if (host === 'aichef.pro' || host.endsWith('.aichef.pro')) return true;
  if (host === 'aichefpro.netlify.app' || host.endsWith('--aichefpro.netlify.app')) return true;
  return false;
}

type FetchLike = typeof fetch;

interface ResendOk {
  ok: true;
  status: number;
  json: Record<string, unknown>;
}
interface ResendFail {
  ok: false;
  status: number;
  json: Record<string, unknown>;
}

async function resend(
  doFetch: FetchLike,
  apiKey: string,
  method: string,
  path: string,
  body?: unknown,
): Promise<ResendOk | ResendFail> {
  const res = await doFetch(`https://api.resend.com${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      'User-Agent': 'aichef-pro-capture/1.0',
    },
    body: body === undefined ? undefined : JSON.stringify(body),
  });
  const json = (await res.json().catch(() => ({}))) as Record<string, unknown>;
  return res.ok ? { ok: true, status: res.status, json } : { ok: false, status: res.status, json };
}

const segmentCache = new Map<string, string>();

function rowsOf(json: Record<string, unknown>): Array<Record<string, unknown>> {
  const data = json.data;
  if (Array.isArray(data)) return data.filter((row) => row && typeof row === 'object') as Array<Record<string, unknown>>;
  return [];
}

async function findSegmentId(
  doFetch: FetchLike,
  apiKey: string,
  name: string,
): Promise<string | null> {
  let after = '';
  for (let page = 0; page < 5; page++) {
    const qs = after ? `?limit=100&after=${encodeURIComponent(after)}` : '?limit=100';
    const listed = await resend(doFetch, apiKey, 'GET', `/segments${qs}`);
    if (!listed.ok) {
      throw new Error(`resend_list_segments_${listed.status}`);
    }
    const rows = rowsOf(listed.json);
    const hit = rows.find((row) => row.name === name && typeof row.id === 'string');
    if (hit && typeof hit.id === 'string') return hit.id;
    if (listed.json.has_more !== true || rows.length === 0) return null;
    const last = rows[rows.length - 1];
    if (typeof last.id !== 'string') return null;
    after = last.id;
  }
  return null;
}

async function resolveSegmentId(
  doFetch: FetchLike,
  apiKey: string,
  lang: CaptureLang,
  env: Record<string, string | undefined>,
): Promise<string> {
  const fromEnv = env[segmentEnvKey(lang)]?.trim();
  if (fromEnv) return fromEnv;
  const cached = segmentCache.get(lang);
  if (cached) return cached;
  const name = segmentName(lang);
  const existing = await findSegmentId(doFetch, apiKey, name);
  if (existing) {
    segmentCache.set(lang, existing);
    return existing;
  }
  const created = await resend(doFetch, apiKey, 'POST', '/segments', { name });
  if (!created.ok || typeof created.json.id !== 'string') {
    const again = await findSegmentId(doFetch, apiKey, name);
    if (again) {
      segmentCache.set(lang, again);
      return again;
    }
    throw new Error(`resend_create_segment_${created.ok ? 'no_id' : created.status}`);
  }
  segmentCache.set(lang, created.json.id);
  return created.json.id;
}

function propertyError(result: ResendFail): boolean {
  if (result.status !== 400 && result.status !== 422) return false;
  const blob = JSON.stringify(result.json).toLowerCase();
  return blob.includes('propert');
}

export interface SaveDeps {
  fetch?: FetchLike;
  apiKey: string | undefined;
  env?: Record<string, string | undefined>;
  now?: () => string;
}

export type SaveResult =
  | { ok: true }
  | { ok: false; error: 'misconfigured' | 'upstream' };

export async function saveCapture(input: CaptureInput, deps: SaveDeps): Promise<SaveResult> {
  if (!deps.apiKey) return { ok: false, error: 'misconfigured' };
  const doFetch = deps.fetch ?? fetch;
  const env = deps.env ?? {};
  const now = deps.now ?? (() => new Date().toISOString());

  let segmentId: string;
  try {
    segmentId = await resolveSegmentId(doFetch, deps.apiKey, input.lang, env);
  } catch (err) {
    console.error('[capture-lead] segmento', err instanceof Error ? err.message : 'error');
    return { ok: false, error: 'upstream' };
  }

  const properties: Record<string, string> = {
    capture_source: input.source,
    capture_lang: input.lang,
    consent_at: now(),
    consent_version: CONSENT_VERSION,
  };
  if (input.page) properties.capture_page = input.page;

  const created = await resend(doFetch, deps.apiKey, 'POST', '/contacts', {
    email: input.email,
    unsubscribed: false,
    segments: [{ id: segmentId }],
    properties,
  });

  if (created.ok) return { ok: true };

  let createResult: ResendOk | ResendFail = created;
  if (!created.ok && propertyError(created)) {
    const retry = await resend(doFetch, deps.apiKey, 'POST', '/contacts', {
      email: input.email,
      unsubscribed: false,
      segments: [{ id: segmentId }],
    });
    if (retry.ok) return { ok: true };
    createResult = retry;
  }

  if (createResult.ok || createResult.status !== 409) {
    console.error('[capture-lead] alta', createResult.ok ? 'unexpected' : createResult.status);
    return { ok: false, error: 'upstream' };
  }

  const added = await resend(
    doFetch,
    deps.apiKey,
    'POST',
    `/contacts/${encodeURIComponent(input.email)}/segments/${segmentId}`,
  );
  if (!added.ok && added.status !== 409) {
    console.error('[capture-lead] segmento-contacto', added.status);
    return { ok: false, error: 'upstream' };
  }

  // Consentimiento nuevo y explícito: si el contacto existía dado de baja,
  // esta casilla es una alta nueva. No reabrimos bajas sin esa casilla
  // (parseCaptureBody ya exigió consent === true).
  const patched = await resend(doFetch, deps.apiKey, 'PATCH', `/contacts/${encodeURIComponent(input.email)}`, {
    unsubscribed: false,
  });
  if (!patched.ok) {
    console.error('[capture-lead] patch consentimiento', patched.status);
  }
  return { ok: true };
}

/** Solo para tests: el caché de ids vive en el módulo. */
export function clearSegmentCache(): void {
  segmentCache.clear();
}
