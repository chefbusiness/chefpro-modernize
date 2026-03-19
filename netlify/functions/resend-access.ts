import type { Handler } from '@netlify/functions';

// ── Product config ──────────────────────────────────────────────
interface ProductConfig {
  accessPath: string;
  emailSubject: string;
  emailTitle: string;
  emailBody: string;
  emailCta: string;
}

const PRODUCTS: Record<string, ProductConfig> = {
  'pro-prompts-ebook': {
    accessPath: '/pro-prompts-library-access',
    emailSubject: 'Tu acceso a Pro Prompts Library',
    emailTitle: 'Accede a tu Pro Prompts Library',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard con todos los prompts y descargas:',
    emailCta: 'Acceder a mi Library',
  },
  'kit-escandallos': {
    accessPath: '/kit-escandallos-access',
    emailSubject: 'Tu acceso al Kit de Escandallos Pro',
    emailTitle: 'Accede a tu Kit de Escandallos Pro',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 11 plantillas Excel:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'pack-appcc': {
    accessPath: '/pack-appcc-access',
    emailSubject: 'Tu acceso al Pack de Plantillas APPCC',
    emailTitle: 'Accede a tu Pack de Plantillas APPCC',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 17 plantillas de seguridad alimentaria:',
    emailCta: 'Acceder a mis Plantillas APPCC',
  },
  'kit-tareas': {
    accessPath: '/kit-tareas-access',
    emailSubject: 'Tu acceso al Kit de Tareas Recurrentes',
    emailTitle: 'Accede a tu Kit de Tareas Recurrentes',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
};

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
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    const { email, product } = JSON.parse(event.body || '{}');
    if (!email) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'Email required' }) };
    }

    const productId = product && PRODUCTS[product] ? product : 'pro-prompts-ebook';
    const config = PRODUCTS[productId];

    // Search Stripe for completed checkout sessions with this email
    const Stripe = (await import('stripe')).default;
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { apiVersion: '2024-12-18.acacia' });

    const sessions = await stripe.checkout.sessions.list({
      customer_details: { email },
      limit: 10,
    });

    const paidSession = sessions.data.find((s) => s.payment_status === 'paid');

    if (!paidSession) {
      return { statusCode: 404, headers, body: JSON.stringify({ error: 'No purchase found' }) };
    }

    // Generate new JWT and send email
    const jwt = (await import('jsonwebtoken')).default;
    const token = jwt.sign(
      { email, product: productId },
      process.env.JWT_SECRET!,
      { expiresIn: '365d' }
    );

    const magicLink = `https://aichef.pro${config.accessPath}?jwt=${token}`;

    await fetch('https://api.resend.com/emails', {
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
              ${config.emailBody}
            </p>
            <div style="text-align: center; margin: 30px 0;">
              <a href="${magicLink}" style="background: #FFD700; color: #000; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 16px;">
                ${config.emailCta}
              </a>
            </div>
            <p style="color: #666; font-size: 14px; line-height: 1.6;">
              Guarda este email. Puedes usar este enlace en cualquier momento durante los próximos 12 meses.
            </p>
            <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;" />
            <p style="color: #999; font-size: 12px;">
              AI Chef Pro · <a href="https://aichef.pro" style="color: #FFD700;">aichef.pro</a>
            </p>
          </div>
        `,
      }),
    });

    return { statusCode: 200, headers, body: JSON.stringify({ sent: true }) };
  } catch (err) {
    console.error('resend-access error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'Server error' }) };
  }
};
