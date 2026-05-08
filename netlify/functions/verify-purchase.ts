import type { Handler } from '@netlify/functions';
import { PRODUCTS_CONFIG, DEFAULT_PRODUCT_ID } from '../../src/data/productos-digitales-config';

// ── Handler ─────────────────────────────────────────────────────
export const handler: Handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ valid: false }) };
  }

  try {
    const { checkoutSessionId, existingJwt, product } = JSON.parse(event.body || '{}');
    const productId = product && PRODUCTS_CONFIG[product] ? product : DEFAULT_PRODUCT_ID;

    // Case 1: Verify new Stripe checkout session
    if (checkoutSessionId) {
      const Stripe = (await import('stripe')).default;
      const jwt = (await import('jsonwebtoken')).default;

      const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { apiVersion: '2024-12-18.acacia' });
      const session = await stripe.checkout.sessions.retrieve(checkoutSessionId);

      if (session.payment_status === 'paid') {
        const email = session.customer_details?.email || session.customer_email || '';
        const token = jwt.sign(
          { email, product: productId },
          process.env.JWT_SECRET!,
          { expiresIn: '365d' }
        );

        // Send access email (log errors but don't block response)
        sendAccessEmail(email, token, productId).catch((err) => {
          console.error('sendAccessEmail failed:', err);
        });

        return {
          statusCode: 200,
          headers,
          body: JSON.stringify({ valid: true, jwt: token }),
        };
      }

      return { statusCode: 403, headers, body: JSON.stringify({ valid: false }) };
    }

    // Case 2: Verify existing JWT (magic link from email)
    if (existingJwt) {
      const jwt = (await import('jsonwebtoken')).default;
      try {
        jwt.verify(existingJwt, process.env.JWT_SECRET!);
        return {
          statusCode: 200,
          headers,
          body: JSON.stringify({ valid: true, jwt: existingJwt }),
        };
      } catch {
        return { statusCode: 403, headers, body: JSON.stringify({ valid: false }) };
      }
    }

    return { statusCode: 400, headers, body: JSON.stringify({ valid: false }) };
  } catch (err) {
    console.error('verify-purchase error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ valid: false }) };
  }
};

// ── Email sender ────────────────────────────────────────────────
async function sendAccessEmail(email: string, token: string, productId: string) {
  if (!email || !process.env.RESEND_API_KEY) return;

  const config = PRODUCTS_CONFIG[productId] || PRODUCTS_CONFIG[DEFAULT_PRODUCT_ID];
  const magicLink = `https://aichef.pro${config.accessPath}?jwt=${token}`;

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
    },
    body: JSON.stringify({
      from: 'AI Chef Pro <noreply@contact.aichef.pro>',
      to: email,
      subject: config.emailSubject,
      html: `
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
          <h1 style="color: #FFD700; font-size: 24px;">${config.emailTitle}</h1>
          <p style="color: #333; line-height: 1.6;">
            ${config.emailBodyPostPurchase}
          </p>
          <div style="text-align: center; margin: 30px 0;">
            <a href="${magicLink}" style="background: #FFD700; color: #000; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 16px;">
              ${config.emailCta}
            </a>
          </div>
          <p style="color: #666; font-size: 14px; line-height: 1.6;">
            Guarda este email. Puedes usar este enlace para acceder en cualquier momento.
          </p>
          <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;" />
          <p style="color: #999; font-size: 12px;">
            AI Chef Pro · <a href="https://aichef.pro" style="color: #FFD700;">aichef.pro</a>
          </p>
        </div>
      `,
    }),
  });

  if (!res.ok) {
    const errorBody = await res.text();
    console.error(`Resend API error (${res.status}):`, errorBody);
    throw new Error(`Resend failed: ${res.status} ${errorBody}`);
  }

  console.log('Email sent successfully to:', email);
}
