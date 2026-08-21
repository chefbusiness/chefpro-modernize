// Webhook de Stripe — checkout.session.completed → email de acceso (2026-08-21).
//
// POR QUÉ EXISTE: hasta hoy el email con el magic link sólo salía cuando el cliente
// ATERRIZABA en la página `-access?session_id=…` tras pagar (verify-purchase). Si cerraba la
// pestaña de Stripe al ver «pago completado», o si el Payment Link no tenía bien la URL de
// confirmación, no se enviaba nada y no quedaba rastro (cliente del Kit Pastelería, 16-ago).
// Con el webhook el email sale SIEMPRE que Stripe registra el pago, aterrice o no.
//
// ACTIVACIÓN (dos pasos de John, sin ellos la function es inerte y responde 501):
//   1. Stripe → Developers → Webhooks → Add endpoint:
//        URL     https://aichef.pro/.netlify/functions/stripe-webhook
//        Eventos checkout.session.completed, checkout.session.async_payment_succeeded
//   2. Netlify site aichefpro → env var STRIPE_WEBHOOK_SECRET = whsec_… (scope functions),
//      marcada como secreta. Redeploy no necesario (las functions leen env en runtime).
//
// El producto se deduce del payment_link de la sesión (mapa netlify/shared/payment-links.ts); si el
// link no está mapeado se responde 200 con `ignored` (y se loguea) para que Stripe no reintente
// en bucle. Si el envío del email falla se responde 500 → Stripe reintenta (hasta 3 días).
// Si el cliente además aterriza en `-access`, recibirá un segundo email idéntico: aceptado.
import type { Handler } from '@netlify/functions';
import type Stripe from 'stripe';
import { PRODUCTS, sendAccessEmail } from './verify-purchase';
import { resolveSession } from '../shared/purchase-validation';

const json = (statusCode: number, body: Record<string, unknown>) => ({
  statusCode,
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(body),
});

export const handler: Handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return json(405, { error: 'method_not_allowed' });
  }
  const secret = process.env.STRIPE_WEBHOOK_SECRET;
  if (!secret) {
    console.error('[stripe-webhook] STRIPE_WEBHOOK_SECRET no configurado: endpoint inerte');
    return json(501, { error: 'webhook_not_configured' });
  }
  const sig = event.headers['stripe-signature'] || event.headers['Stripe-Signature'];
  if (!sig) {
    return json(400, { error: 'missing_signature' });
  }
  if (!process.env.STRIPE_SECRET_KEY || !process.env.JWT_SECRET) {
    console.error('[stripe-webhook] faltan STRIPE_SECRET_KEY / JWT_SECRET');
    return json(500, { error: 'misconfigured' });
  }

  const StripeCtor = (await import('stripe')).default;
  const stripe = new StripeCtor(process.env.STRIPE_SECRET_KEY, { apiVersion: '2024-12-18.acacia' });

  // La firma se calcula sobre el cuerpo CRUDO: no parsear antes de verificar.
  const raw = event.isBase64Encoded ? Buffer.from(event.body || '', 'base64') : Buffer.from(event.body || '', 'utf8');
  let evt: Stripe.Event;
  try {
    evt = stripe.webhooks.constructEvent(raw, sig, secret);
  } catch (err) {
    console.warn('[stripe-webhook] firma inválida:', (err as Error).message);
    return json(400, { error: 'invalid_signature' });
  }

  if (evt.type !== 'checkout.session.completed' && evt.type !== 'checkout.session.async_payment_succeeded') {
    return json(200, { ignored: evt.type });
  }

  const session = evt.data.object as Stripe.Checkout.Session;
  if (session.payment_status !== 'paid') {
    // completed pero pendiente (p. ej. SEPA): llegará async_payment_succeeded
    return json(200, { ignored: 'unpaid', payment_status: session.payment_status });
  }

  const email = (session.customer_details?.email || session.customer_email || '').trim();
  const resolved = await resolveSession(stripe, session);
  const productId = resolved.productId;
  if (!productId || !PRODUCTS[productId]) {
    console.error(`[stripe-webhook] sesión ${session.id} pagada con payment_link ${resolved.linkId} (${resolved.url}) SIN producto mapeado — regenerar netlify/shared/payment-links.ts`);
    return json(200, { ignored: 'unknown_product', link: resolved.linkId });
  }
  if (!email) {
    console.error(`[stripe-webhook] sesión ${session.id} (${productId}) sin email`);
    return json(200, { ignored: 'no_email', product: productId });
  }

  const jwt = (await import('jsonwebtoken')).default;
  const token = jwt.sign({ email, product: productId }, process.env.JWT_SECRET, { expiresIn: '365d' });
  try {
    await sendAccessEmail(email, token, productId);
  } catch (err) {
    console.error('[stripe-webhook] sendAccessEmail falló:', err);
    return json(500, { error: 'email_failed', product: productId });
  }
  console.log(`[stripe-webhook] acceso enviado: ${productId} → ${email} (sesión ${session.id})`);
  return json(200, { sent: true, product: productId });
};
