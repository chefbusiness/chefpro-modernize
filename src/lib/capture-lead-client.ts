/** Cliente del imán y del newsletter. Mismo contrato que `netlify/functions/capture-lead`. */

export const CAPTURE_ENDPOINT = '/.netlify/functions/capture-lead';

export type CaptureSource = 'food-cost-calculator' | 'footer-newsletter';

export type CaptureResult =
  | { ok: true }
  | { ok: false; error: string };

export async function submitCapture(body: {
  email: string;
  lang: string;
  source: CaptureSource;
  consent: boolean;
  /** Honeypot. Debe ir vacío. */
  website?: string;
  page?: string;
}): Promise<CaptureResult> {
  try {
    const res = await fetch(CAPTURE_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    const data = (await res.json().catch(() => ({}))) as { ok?: boolean; error?: unknown };
    if (!res.ok || data.ok !== true) {
      return { ok: false, error: typeof data.error === 'string' ? data.error : 'upstream' };
    }
    return { ok: true };
  } catch {
    return { ok: false, error: 'upstream' };
  }
}
