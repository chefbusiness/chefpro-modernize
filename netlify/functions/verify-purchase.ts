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
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Pro Prompts Library</strong> está listo. Haz clic en el botón para acceder a tus prompts y descargas:',
    emailCta: 'Acceder a mi Library',
  },
  'kit-escandallos': {
    accessPath: '/kit-escandallos-access',
    emailSubject: 'Tu acceso al Kit de Escandallos Pro',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Escandallos Pro</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 11 plantillas Excel:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'pack-appcc': {
    accessPath: '/pack-appcc-access',
    emailSubject: 'Tu acceso al Pack de Plantillas APPCC',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Pack de Plantillas APPCC</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 17 plantillas de seguridad alimentaria:',
    emailCta: 'Acceder a mis Plantillas APPCC',
  },
  'kit-tareas': {
    accessPath: '/kit-tareas-access',
    emailSubject: 'Tu acceso al Kit de Tareas Recurrentes',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes Pro</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-cafeteria': {
    accessPath: '/kit-tareas-cafeteria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Cafetería / Brunch',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Cafetería / Brunch</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pizzeria': {
    accessPath: '/kit-tareas-pizzeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pizzería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Pizzería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hamburgueseria': {
    accessPath: '/kit-tareas-hamburgueseria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Hamburguesería',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Hamburguesería</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-dark-kitchen': {
    accessPath: '/kit-tareas-dark-kitchen-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Dark Kitchen',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Dark Kitchen</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pasteleria': {
    accessPath: '/kit-tareas-pasteleria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pastelería / Obrador',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Pastelería / Obrador</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-bar': {
    accessPath: '/kit-tareas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Bar / Cocktails',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Bar / Cocktails</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-catering': {
    accessPath: '/kit-tareas-catering-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Catering / Eventos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Catering / Eventos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hotel': {
    accessPath: '/kit-tareas-hotel-completo-access',
    emailSubject: 'Tu acceso al Kit Tareas Recurrentes: Hotel Completo — 46 Checklists',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit Tareas Recurrentes: Hotel Completo — 46 Checklists</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 15 plantillas con 46 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-heladeria': {
    accessPath: '/kit-tareas-heladeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Heladería Artesanal',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Heladería Artesanal</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chocolateria': {
    accessPath: '/kit-tareas-chocolateria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chocolatería / Obrador de Chocolate',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Chocolatería / Obrador de Chocolate</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-restaurante-creativo': {
    accessPath: '/kit-tareas-restaurante-creativo-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Restaurante Creativo / De Autor',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Restaurante Creativo / De Autor</strong> esta listo. Haz clic en el boton para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chef-privado': {
    accessPath: '/kit-tareas-chef-privado-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chef Privado / Personal Chef',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Tareas Recurrentes: Chef Privado / Personal Chef</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists profesionales:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-gestion-personal': {
    accessPath: '/kit-gestion-personal-access',
    emailSubject: 'Tu acceso al Kit de Gestión de Personal y Turnos',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit de Gestión de Personal y Turnos</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de gestión de personal:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'kit-inventario': {
    accessPath: '/kit-inventario-access',
    emailSubject: 'Tu acceso al Kit Control de Inventario y Compras',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit Control de Inventario y Compras</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de control de inventario:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'guia-dark-kitchen': {
    accessPath: '/guia-dark-kitchen-access',
    emailSubject: 'Tu acceso a la Guía: Cómo Montar una Dark Kitchen',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar una Dark Kitchen</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 3 checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-gastronomico': {
    accessPath: '/guia-restaurante-gastronomico-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Gastronómico 65 Plazas',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso a la <strong>Guía Cómo Montar un Restaurante Gastronómico</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 20 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'mega-pack-tareas': {
    accessPath: '/mega-pack-tareas-access',
    emailSubject: 'Tu acceso al Mega Pack Tareas Recurrentes — 13 Kits',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Mega Pack Tareas Recurrentes (13 Kits)</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 151 plantillas:',
    emailCta: 'Acceder a mis 13 Kits',
  },
  'kit-plan-financiero': {
    accessPath: '/kit-plan-financiero-access',
    emailSubject: 'Tu acceso al Kit Plan Financiero para Restaurantes',
    emailTitle: '¡Gracias por tu compra!',
    emailBody: 'Tu acceso al <strong>Kit Plan Financiero para Restaurantes</strong> está listo. Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas financieras:',
    emailCta: 'Acceder a mis Plantillas',
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
    return { statusCode: 405, headers, body: JSON.stringify({ valid: false }) };
  }

  try {
    const { checkoutSessionId, existingJwt, product } = JSON.parse(event.body || '{}');
    const productId = product && PRODUCTS[product] ? product : 'pro-prompts-ebook';

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

  const config = PRODUCTS[productId] || PRODUCTS['pro-prompts-ebook'];
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
            ${config.emailBody}
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
