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
  'kit-tareas-cafeteria': {
    accessPath: '/kit-tareas-cafeteria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Cafetería / Brunch',
    emailTitle: 'Accede a tu Kit de Tareas: Cafetería / Brunch',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pizzeria': {
    accessPath: '/kit-tareas-pizzeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pizzería',
    emailTitle: 'Accede a tu Kit de Tareas: Pizzería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hamburgueseria': {
    accessPath: '/kit-tareas-hamburgueseria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Hamburguesería',
    emailTitle: 'Accede a tu Kit de Tareas: Hamburguesería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-dark-kitchen': {
    accessPath: '/kit-tareas-dark-kitchen-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Dark Kitchen',
    emailTitle: 'Accede a tu Kit de Tareas: Dark Kitchen',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-pasteleria': {
    accessPath: '/kit-tareas-pasteleria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Pastelería / Obrador',
    emailTitle: 'Accede a tu Kit de Tareas: Pastelería / Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos + 2 bonus:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-bar': {
    accessPath: '/kit-tareas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Bar / Cocktails',
    emailTitle: 'Accede a tu Kit de Tareas: Bar / Cocktails',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-catering': {
    accessPath: '/kit-tareas-catering-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Catering / Eventos',
    emailTitle: 'Accede a tu Kit de Tareas: Catering / Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-hotel': {
    accessPath: '/kit-tareas-hotel-completo-access',
    emailSubject: 'Tu acceso al Kit Tareas Recurrentes: Hotel Completo — 46 Checklists',
    emailTitle: 'Accede a tu Kit Tareas: Hotel Completo',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 15 plantillas con 46 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-heladeria': {
    accessPath: '/kit-tareas-heladeria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Heladería Artesanal',
    emailTitle: 'Accede a tu Kit de Tareas: Heladería Artesanal',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chocolateria': {
    accessPath: '/kit-tareas-chocolateria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chocolatería / Obrador de Chocolate',
    emailTitle: 'Accede a tu Kit de Tareas: Chocolatería',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-restaurante-creativo': {
    accessPath: '/kit-tareas-restaurante-creativo-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Restaurante Creativo / De Autor',
    emailTitle: 'Accede a tu Kit de Tareas: Restaurante Creativo',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-chef-privado': {
    accessPath: '/kit-tareas-chef-privado-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Chef Privado / Personal Chef',
    emailTitle: 'Accede a tu Kit de Tareas: Chef Privado',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 checklists profesionales:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-gestion-personal': {
    accessPath: '/kit-gestion-personal-access',
    emailSubject: 'Tu acceso al Kit de Gestión de Personal y Turnos',
    emailTitle: 'Accede a tu Kit de Gestión de Personal',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de gestión de personal:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'kit-inventario': {
    accessPath: '/kit-inventario-access',
    emailSubject: 'Tu acceso al Kit Control de Inventario y Compras',
    emailTitle: 'Accede a tu Kit Control de Inventario',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas de control de inventario:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'guia-dark-kitchen': {
    accessPath: '/guia-dark-kitchen-access',
    emailSubject: 'Tu acceso a la Guía: Cómo Montar una Dark Kitchen',
    emailTitle: 'Accede a tu Guía Dark Kitchen',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 3 checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-gastronomico': {
    accessPath: '/guia-restaurante-gastronomico-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Gastronómico 65 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Gastronómico',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 20 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-casual': {
    accessPath: '/guia-restaurante-casual-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Casual 80 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Casual',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 16 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-mexicano': {
    accessPath: '/guia-restaurante-mexicano-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Mexicano 80 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Mexicano',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-peruano': {
    accessPath: '/guia-restaurante-peruano-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Peruano 80 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Peruano',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-japones': {
    accessPath: '/guia-restaurante-japones-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Japonés 60 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Japonés',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'guia-restaurante-nikkei': {
    accessPath: '/guia-restaurante-nikkei-access',
    emailSubject: 'Tu acceso a la Guía: Restaurante Nikkei 60 Plazas',
    emailTitle: 'Accede a tu Guía Restaurante Nikkei',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel:',
    emailCta: 'Acceder a mi Guía',
  },
  'mega-pack-tareas': {
    accessPath: '/mega-pack-tareas-access',
    emailSubject: 'Tu acceso al Mega Pack Tareas Recurrentes — 13 Kits',
    emailTitle: 'Accede a tu Mega Pack Tareas Recurrentes',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 151 plantillas:',
    emailCta: 'Acceder a mis 13 Kits',
  },
  'kit-plan-financiero': {
    accessPath: '/kit-plan-financiero-access',
    emailSubject: 'Tu acceso al Kit Plan Financiero para Restaurantes',
    emailTitle: 'Accede a tu Kit Plan Financiero',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar las 9 plantillas financieras:',
    emailCta: 'Acceder a mis Plantillas',
  },
  'kit-tareas-sushi-bar': {
    accessPath: '/kit-tareas-sushi-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Sushi Bar',
    emailTitle: 'Accede a tu Kit de Tareas: Sushi Bar',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos con protocolo anisakis APPCC:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-asador': {
    accessPath: '/kit-tareas-asador-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Asador / Parrilla y Josper',
    emailTitle: 'Accede a tu Kit de Tareas: Asador / Parrilla y Josper',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos del horno Josper, brasas y maduración:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-marisqueria': {
    accessPath: '/kit-tareas-marisqueria-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Marisquería con Vivero y APPCC',
    emailTitle: 'Accede a tu Kit de Tareas: Marisquería con Vivero y APPCC',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos del vivero, expositor de hielo y trazabilidad APPCC marisco:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-tapas-bar': {
    accessPath: '/kit-tareas-tapas-bar-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Tapas Bar / Gastrobar',
    emailTitle: 'Accede a tu Kit de Tareas: Tapas Bar / Gastrobar',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos de barra de pinchos, cocina de raciones, cerveza grifo, vinos por copa y vermut:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-food-truck': {
    accessPath: '/kit-tareas-food-truck-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Food Truck',
    emailTitle: 'Accede a tu Kit de Tareas: Food Truck',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos de setup, teardown, APPCC móvil, permisos y eventos:',
    emailCta: 'Acceder a mis Checklists',
  },
  'kit-tareas-panaderia': {
    accessPath: '/kit-tareas-panaderia-access',
    emailSubject: 'Tu acceso al Kit de Tareas: Panadería / Obrador',
    emailTitle: 'Accede a tu Kit de Tareas: Panadería / Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 checklists operativos de turno madrugada, masas madre, hornos, expositor y campañas estacionales:',
    emailCta: 'Acceder a mis Checklists',
  },
  'guia-panaderia-obrador': {
    accessPath: '/guia-panaderia-obrador-access',
    emailSubject: 'Tu acceso a la Guía: Panadería con Obrador',
    emailTitle: 'Accede a tu Guía Panadería con Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar la guía PDF + DOCX + 17 plantillas y checklists Excel + manual del obrador:',
    emailCta: 'Acceder a mi Guía',
  },
  'plan-negocio-bar-restaurante': {
    accessPath: '/plan-negocio-bar-restaurante-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Bar-Restaurante',
    emailTitle: 'Accede a tu Plan de Negocio: Bar-Restaurante',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-tapas-bar': {
    accessPath: '/plan-negocio-tapas-bar-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Tapas Bar / Gastrobar',
    emailTitle: 'Accede a tu Plan de Negocio: Tapas Bar / Gastrobar',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el documento DOCX, el plan financiero Excel y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cafeteria': {
    accessPath: '/plan-negocio-cafeteria-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Cafetería / Brunch',
    emailTitle: 'Accede a tu Plan de Negocio: Cafetería / Brunch',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-panaderia': {
    accessPath: '/plan-negocio-panaderia-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Panadería / Obrador',
    emailTitle: 'Accede a tu Plan de Negocio: Panadería / Obrador',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el plan financiero Excel, el plan de negocio Word y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-food-truck': {
    accessPath: '/plan-negocio-food-truck-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Food Truck',
    emailTitle: 'Accede a tu Plan de Negocio: Food Truck',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar el documento DOCX, el plan financiero Excel y el checklist de apertura:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-cocteleria-eventos': {
    accessPath: '/plan-negocio-cocteleria-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Coctelería de Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Coctelería de Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 9 entregables del kit de coctelería de eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-parrillero-asador-eventos': {
    accessPath: '/plan-negocio-parrillero-asador-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Parrillero / Asador para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Parrillero / Asador para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 entregables del kit de parrillero / asador para eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-negocio-paellero-eventos': {
    accessPath: '/plan-negocio-paellero-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Paellero / Paella para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Paellero / Paella para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 entregables del kit de paellero / paella para eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-chef-privado-showcooking-eventos': {
    accessPath: '/plan-chef-privado-showcooking-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Chef Privado / Showcooking a Domicilio',
    emailTitle: 'Accede a tu Plan de Negocio: Chef Privado / Showcooking a Domicilio',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 entregables del kit de chef privado y showcooking a domicilio:',
    emailCta: 'Acceder a mi Plan de Negocio',
  },
  'plan-catering-tematico-eventos': {
    accessPath: '/plan-catering-tematico-eventos-access',
    emailSubject: 'Tu acceso al Plan de Negocio: Catering & Kit Temático para Eventos',
    emailTitle: 'Accede a tu Plan de Negocio: Catering & Kit Temático para Eventos',
    emailBody: 'Haz clic en el botón para acceder a tu dashboard y descargar los 11 entregables del kit de catering temático multi-concepto para eventos:',
    emailCta: 'Acceder a mi Plan de Negocio',
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

    // Reject an explicitly-provided but unknown product (avoid silent fallback to pro-prompts-ebook).
    // Legacy callers that omit `product` (undefined/null) keep the pro-prompts-ebook fallback.
    if (product != null && !PRODUCTS[product]) {
      return { statusCode: 400, headers, body: JSON.stringify({ error: 'unknown_product' }) };
    }

    const productId = product && PRODUCTS[product] ? product : 'pro-prompts-ebook';
    const config = PRODUCTS[productId];

    // Search Stripe for completed checkout sessions with this email
    const Stripe = (await import('stripe')).default;
    const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, { apiVersion: '2024-12-18.acacia' });

    // El cliente teclea el email a mano en "¿Ya compraste?": normalizar espacios/mayúsculas y
    // consultar Stripe con la variante normalizada Y la literal (bug "email case-sensitive",
    // catalogado en CB PRODUCTOS-DIGITALES-ROADMAP §2). Se conserva la literal para no romper
    // a quien pagó con mayúsculas si el filtro de Stripe resultara sensible a ellas.
    const emailNorm = String(email).trim().toLowerCase();
    const variants = emailNorm === email ? [email] : [emailNorm, email];
    const results = await Promise.all(
      variants.map((e) => stripe.checkout.sessions.list({ customer_details: { email: e }, limit: 10 }))
    );
    const allSessions = results.flatMap((r) => r.data);

    const paidSession = allSessions.find((s) => s.payment_status === 'paid');

    if (!paidSession) {
      return { statusCode: 404, headers, body: JSON.stringify({ error: 'No purchase found' }) };
    }

    // Generate new JWT and send email
    const jwt = (await import('jsonwebtoken')).default;
    const token = jwt.sign(
      { email: emailNorm, product: productId },
      process.env.JWT_SECRET!,
      { expiresIn: '365d' }
    );

    const magicLink = `https://aichef.pro${config.accessPath}?jwt=${token}`;

    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
      },
      body: JSON.stringify({
        from: 'AI Chef Pro <noreply@contact.aichef.pro>',
        to: emailNorm,
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

    if (!res.ok) {
      const errorBody = await res.text();
      console.error(`Resend API error (${res.status}):`, errorBody);
      return { statusCode: 500, headers, body: JSON.stringify({ error: `Email send failed: ${res.status}` }) };
    }

    console.log('Resend-access email sent to:', email);
    return { statusCode: 200, headers, body: JSON.stringify({ sent: true }) };
  } catch (err) {
    console.error('resend-access error:', err);
    return { statusCode: 500, headers, body: JSON.stringify({ error: 'Server error' }) };
  }
};
