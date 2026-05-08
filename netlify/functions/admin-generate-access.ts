import type { Handler } from '@netlify/functions';
import { PRODUCTS_CONFIG } from '../../src/data/productos-digitales-config';

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
    const { adminPassword, email, product, sendEmail } = JSON.parse(event.body || '{}');

    if (!process.env.ADMIN_PASSWORD) {
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'ADMIN_PASSWORD not configured' }) };
    }
    if (!adminPassword || adminPassword !== process.env.ADMIN_PASSWORD) {
      return { statusCode: 401, headers, body: JSON.stringify({ error: 'Unauthorized' }) };
    }
    if (!email || !product) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'email and product required' }) };
    }
    const config = PRODUCTS_CONFIG[product];
    if (!config) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: `Unknown product: ${product}` }) };
    }

    const jwt = (await import('jsonwebtoken')).default;
    const token = jwt.sign({ email, product }, process.env.JWT_SECRET!, { expiresIn: '365d' });
    const magicLink = `https://aichef.pro${config.accessPath}?jwt=${token}`;

    let emailSent = false;
    if (sendEmail && process.env.RESEND_API_KEY) {
      const res = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
        },
        body: JSON.stringify({
          from: 'AI Chef Pro <noreply@contact.aichef.pro>',
          to: email,
          subject: `Tu acceso a ${config.name}`,
          html: `
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
              <h1 style="color: #FFD700; font-size: 24px;">Tu enlace de acceso a ${config.name}</h1>
              <p style="color: #333; line-height: 1.6;">
                Hemos generado manualmente tu acceso al producto. Haz clic en el botón para entrar a tu dashboard:
              </p>
              <div style="text-align: center; margin: 30px 0;">
                <a href="${magicLink}" style="background: #FFD700; color: #000; padding: 14px 32px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 16px;">
                  Acceder a mi producto
                </a>
              </div>
              <p style="color: #666; font-size: 14px; line-height: 1.6;">
                Guarda este email. El enlace es válido durante 12 meses.
              </p>
              <hr style="border: none; border-top: 1px solid #eee; margin: 30px 0;" />
              <p style="color: #999; font-size: 12px;">
                AI Chef Pro · <a href="https://aichef.pro" style="color: #FFD700;">aichef.pro</a>
              </p>
            </div>
          `,
        }),
      });
      emailSent = res.ok;
      if (!res.ok) {
        const errBody = await res.text();
        console.error(`Resend error (${res.status}):`, errBody);
      }
    }

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify({ magicLink, emailSent, product, email }),
    };
  } catch (err) {
    console.error('admin-generate-access error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'Server error' }) };
  }
};
