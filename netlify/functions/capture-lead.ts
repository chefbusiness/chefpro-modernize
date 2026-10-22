import type { Handler } from '@netlify/functions';
import { originAllowed, parseCaptureBody, saveCapture } from '../shared/capture-lead';

/**
 * POST /.netlify/functions/capture-lead
 *
 * Guarda un email con consentimiento en el segmento de captación del idioma
 * (Resend). Lo usan la calculadora de food cost y el newsletter del footer.
 *
 * Variable obligatoria (ya presente en el site Netlify `aichefpro` para los
 * correos de producto; si en un entorno no está, la respuesta es 503
 * `misconfigured` y el navegador no descarga el Excel):
 *   RESEND_API_KEY
 *
 * Opcional, un id por idioma. Si falta, la función busca o crea el segmento
 * `aichef.pro captacion <lang>` con esa misma key:
 *   RESEND_CAPTURE_SEGMENT_ES
 *   RESEND_CAPTURE_SEGMENT_EN
 *   RESEND_CAPTURE_SEGMENT_FR
 *   RESEND_CAPTURE_SEGMENT_DE
 *   RESEND_CAPTURE_SEGMENT_IT
 *   RESEND_CAPTURE_SEGMENT_PT
 *   RESEND_CAPTURE_SEGMENT_NL
 *
 * No envía un correo de bienvenida y no toca las listas de producto.
 */

const MAX_BODY = 4000;

const headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'Cache-Control': 'no-store',
};

function json(statusCode: number, body: Record<string, unknown>) {
  return { statusCode, headers, body: JSON.stringify(body) };
}

export const handler: Handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }
  if (event.httpMethod !== 'POST') {
    return json(405, { ok: false, error: 'method' });
  }
  if (!originAllowed(event.headers.origin || event.headers.Origin)) {
    return json(403, { ok: false, error: 'origin' });
  }
  if ((event.body || '').length > MAX_BODY) {
    return json(400, { ok: false, error: 'invalid_json' });
  }

  let raw: unknown;
  try {
    raw = event.body ? JSON.parse(event.body) : null;
  } catch {
    return json(400, { ok: false, error: 'invalid_json' });
  }

  const parsed = parseCaptureBody(raw);
  if (!parsed.ok) return json(400, { ok: false, error: parsed.error });
  if (parsed.honeypot) return json(200, { ok: true });

  const saved = await saveCapture(parsed.value, {
    apiKey: process.env.RESEND_API_KEY,
    env: process.env,
  });
  if (!saved.ok) {
    const status = saved.error === 'misconfigured' ? 503 : 502;
    return json(status, { ok: false, error: saved.error });
  }
  return json(200, { ok: true });
};
