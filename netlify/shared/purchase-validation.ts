// Validación producto ↔ sesión de Checkout (2026-08-21).
//
// PROBLEMA que cierra: verify-purchase acuñaba el JWT del producto que pidiera el cliente
// con CUALQUIER sesión pagada, y resend-access encontraba CUALQUIER compra de ese email.
// Quien pagó el eBook de 9 € podía pedirse el enlace de la guía de 85 €.
//
// CÓMO: todas las compras entran por Payment Links. La sesión trae `payment_link` (plink_…);
// `stripe.paymentLinks.retrieve(id).url` es la URL pública https://buy.stripe.com/… — la misma
// que Vite inlina en la landing y que congela netlify/shared/payment-links.ts
// (generado desde las env VITE_STRIPE_PAYMENT_LINK_* del site, que NO existen en runtime).
//
// MODOS (env PURCHASE_VALIDATION, por defecto `soft`):
//   off    → no se consulta nada (comportamiento anterior).
//   soft   → se comprueba y se LOGUEA el desajuste, pero se concede el acceso (para revisar
//            los logs de Netlify unos días antes de cerrar la puerta).
//   strict → desajuste = 403 / 404. Una sesión SIN payment_link o un producto SIN entrada en el
//            mapa cuentan como «unknown» y se dejan pasar (fail-open): no es un ataque posible
//            desde fuera, es un hueco del mapa, y se loguea.
import type Stripe from 'stripe';
import { PAYMENT_LINKS, PRODUCT_BY_LINK } from './payment-links';

export type ValidationMode = 'off' | 'soft' | 'strict';
export type Verdict = 'match' | 'mismatch' | 'unknown';

export interface ResolvedSession {
  linkId: string | null;
  url: string | null;
  /** productId según el mapa, o null si el link no está mapeado. */
  productId: string | null;
}

export function validationMode(): ValidationMode {
  const m = String(process.env.PURCHASE_VALIDATION || 'soft').trim().toLowerCase();
  return m === 'strict' || m === 'off' ? m : 'soft';
}

/** https://buy.stripe.com/xxx?locale=es#foo → https://buy.stripe.com/xxx */
export function normalizeLink(url: string | null | undefined): string | null {
  if (!url) return null;
  return url.split('#')[0].split('?')[0].replace(/\/+$/, '');
}

const NORMALIZED_LINKS: Record<string, string> = Object.fromEntries(
  Object.entries(PAYMENT_LINKS).map(([pid, url]) => [pid, normalizeLink(url)!]),
);
const PRODUCT_BY_NORMALIZED: Record<string, string> = Object.fromEntries(
  Object.entries(PRODUCT_BY_LINK).map(([url, pid]) => [normalizeLink(url)!, pid]),
);

// Caché por instancia de la function (un Payment Link no cambia de URL).
const linkUrlCache = new Map<string, string | null>();

/** Resuelve el Payment Link de una sesión y, con el mapa, el productId que pagó. */
export async function resolveSession(stripe: Stripe, session: Stripe.Checkout.Session): Promise<ResolvedSession> {
  const pl = session.payment_link as string | Stripe.PaymentLink | null | undefined;
  const linkId = typeof pl === 'string' ? pl : pl?.id ?? null;
  if (!linkId) return { linkId: null, url: null, productId: null };
  let url: string | null | undefined = typeof pl === 'object' && pl?.url ? pl.url : linkUrlCache.get(linkId);
  if (url === undefined) {
    try {
      const link = await stripe.paymentLinks.retrieve(linkId);
      url = link.url ?? null;
    } catch (err) {
      console.error('[purchase-validation] paymentLinks.retrieve falló', linkId, err);
      url = null;
    }
    linkUrlCache.set(linkId, url);
  }
  const norm = normalizeLink(url);
  return { linkId, url: norm, productId: norm ? PRODUCT_BY_NORMALIZED[norm] ?? null : null };
}

/** ¿La sesión resuelta corresponde al producto que se está pidiendo? */
export function verdictFor(resolved: ResolvedSession, productId: string): Verdict {
  const expected = NORMALIZED_LINKS[productId];
  if (!expected) return 'unknown'; // producto sin Payment Link en el mapa → regenerar payment-links.ts
  if (!resolved.url) return 'unknown'; // sesión sin payment_link (no creada por Payment Link)
  return resolved.url === expected ? 'match' : 'mismatch';
}

/** Atajo: resuelve + veredicto + log homogéneo. */
export async function validatePurchase(
  stripe: Stripe,
  session: Stripe.Checkout.Session,
  productId: string,
  origin: string,
): Promise<{ verdict: Verdict; mode: ValidationMode; resolved: ResolvedSession }> {
  const mode = validationMode();
  if (mode === 'off') return { verdict: 'unknown', mode, resolved: { linkId: null, url: null, productId: null } };
  const resolved = await resolveSession(stripe, session);
  const verdict = verdictFor(resolved, productId);
  if (verdict !== 'match') {
    console.warn(
      `[purchase-validation] ${origin}: sesión ${session.id} → ${verdict} (modo ${mode}); ` +
        `pidió ${productId}, pagó ${resolved.productId ?? 'desconocido'} (${resolved.url ?? 'sin payment_link'})`,
    );
  }
  return { verdict, mode, resolved };
}
