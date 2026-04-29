import type { Handler } from '@netlify/functions';

// Map productId → { accessPath, label } (must match resend-access.ts entries).
// Keep in sync with PRODUCTS in netlify/functions/resend-access.ts.
const PRODUCTS: Record<string, { accessPath: string; label: string }> = {
  'pro-prompts-ebook': { accessPath: '/pro-prompts-library-access', label: 'Pro Prompts eBook' },
  'kit-escandallos': { accessPath: '/kit-escandallos-access', label: 'Kit de Escandallos Pro' },
  'pack-appcc': { accessPath: '/pack-appcc-access', label: 'Pack Plantillas APPCC' },
  'kit-tareas': { accessPath: '/kit-tareas-access', label: 'Kit de Tareas Recurrentes' },
  'kit-tareas-cafeteria': { accessPath: '/kit-tareas-cafeteria-access', label: 'Kit Tareas Cafetería' },
  'kit-tareas-pizzeria': { accessPath: '/kit-tareas-pizzeria-access', label: 'Kit Tareas Pizzería' },
  'kit-tareas-hamburgueseria': { accessPath: '/kit-tareas-hamburgueseria-access', label: 'Kit Tareas Hamburguesería' },
  'kit-tareas-dark-kitchen': { accessPath: '/kit-tareas-dark-kitchen-access', label: 'Kit Tareas Dark Kitchen' },
  'kit-tareas-pasteleria': { accessPath: '/kit-tareas-pasteleria-access', label: 'Kit Tareas Pastelería' },
  'kit-tareas-bar': { accessPath: '/kit-tareas-bar-access', label: 'Kit Tareas Bar' },
  'kit-tareas-catering': { accessPath: '/kit-tareas-catering-access', label: 'Kit Tareas Catering' },
  'kit-tareas-hotel': { accessPath: '/kit-tareas-hotel-completo-access', label: 'Kit Tareas Hotel Completo' },
  'kit-tareas-heladeria': { accessPath: '/kit-tareas-heladeria-access', label: 'Kit Tareas Heladería' },
  'kit-tareas-chocolateria': { accessPath: '/kit-tareas-chocolateria-access', label: 'Kit Tareas Chocolatería' },
  'kit-tareas-restaurante-creativo': { accessPath: '/kit-tareas-restaurante-creativo-access', label: 'Kit Tareas Restaurante Creativo' },
  'kit-tareas-chef-privado': { accessPath: '/kit-tareas-chef-privado-access', label: 'Kit Tareas Chef Privado' },
  'kit-gestion-personal': { accessPath: '/kit-gestion-personal-access', label: 'Kit Gestión de Personal' },
  'kit-inventario': { accessPath: '/kit-inventario-access', label: 'Kit Control de Inventario' },
  'kit-plan-financiero': { accessPath: '/kit-plan-financiero-access', label: 'Kit Plan Financiero' },
  'guia-dark-kitchen': { accessPath: '/guia-dark-kitchen-access', label: 'Guía Dark Kitchen' },
  'guia-restaurante-gastronomico': { accessPath: '/guia-restaurante-gastronomico-access', label: 'Guía Restaurante Gastronómico' },
  'guia-restaurante-casual': { accessPath: '/guia-restaurante-casual-access', label: 'Guía Restaurante Casual' },
  'guia-restaurante-mexicano': { accessPath: '/guia-restaurante-mexicano-access', label: 'Guía Restaurante Mexicano' },
  'guia-restaurante-peruano': { accessPath: '/guia-restaurante-peruano-access', label: 'Guía Restaurante Peruano' },
  'guia-restaurante-japones': { accessPath: '/guia-restaurante-japones-access', label: 'Guía Restaurante Japonés' },
  'guia-restaurante-nikkei': { accessPath: '/guia-restaurante-nikkei-access', label: 'Guía Restaurante Nikkei' },
  'mega-pack-tareas': { accessPath: '/mega-pack-tareas-access', label: 'Mega Pack Tareas' },
};

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
    const config = PRODUCTS[product];
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
          subject: `Tu acceso a ${config.label}`,
          html: `
            <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 40px 20px;">
              <h1 style="color: #FFD700; font-size: 24px;">Tu enlace de acceso a ${config.label}</h1>
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
