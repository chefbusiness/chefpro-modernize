/** Alta en la audiencia de captación (función Netlify `subscribe`). */

export type SubscribeSource = 'food-cost' | 'newsletter';

export type SubscribeResult =
  | { ok: true }
  | { ok: false; error: string };

export async function subscribeLead(input: {
  email: string;
  lang: string;
  source: SubscribeSource;
  consent: boolean;
  company?: string;
}): Promise<SubscribeResult> {
  try {
    const res = await fetch('/.netlify/functions/subscribe', {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(input),
    });
    const data = (await res.json().catch(() => ({}))) as { ok?: boolean; error?: string };
    if (res.ok && data.ok) return { ok: true };
    return { ok: false, error: typeof data.error === 'string' ? data.error : 'upstream' };
  } catch {
    return { ok: false, error: 'upstream' };
  }
}
