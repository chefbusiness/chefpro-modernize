// Edge Function: Inject correct OG meta tags for social media crawlers
// Runs BEFORE the SPA serves index.html — crawlers get proper meta tags per route

const OG_DATA: Record<string, { title: string; description: string; image: string; price?: string }> = {
  '/guia-dark-kitchen': {
    title: 'Cómo Montar una Dark Kitchen en España — Guía Completa | AI Chef Pro',
    description: 'Guía completa PDF + DOCX: 12 capítulos, requisitos legales, plan financiero, diseño de cocina, tecnología, marketing. 3 checklists Excel + calculadora. 24 EUR.',
    image: 'https://aichef.pro/og-guia-dark-kitchen.jpg',
    price: '24.00',
  },
  '/kit-plan-financiero': {
    title: 'Kit Plan Financiero para Restaurantes — 10 Plantillas Excel | AI Chef Pro',
    description: '10 plantillas Excel: plan financiero a 3 y 5 años, break-even, cash flow, CAPEX, P&L mensual, ratios, informe viabilidad bancos. 39 EUR.',
    image: 'https://aichef.pro/og-kit-plan-financiero.jpg',
    price: '39.00',
  },
  '/kit-inventario': {
    title: 'Kit Control de Inventario y Compras — Plantillas Excel | AI Chef Pro',
    description: '9 plantillas Excel: inventario, proveedores, pedidos, recepción, mermas, FIFO, costes. 14 EUR.',
    image: 'https://aichef.pro/og-kit-inventario.jpg',
    price: '14.00',
  },
  '/kit-gestion-personal': {
    title: 'Kit Gestión de Personal y Turnos — Plantillas Excel | AI Chef Pro',
    description: '9 plantillas Excel: cuadrante turnos, horas extra, coste laboral, onboarding, vacaciones, evaluación. 14 EUR.',
    image: 'https://aichef.pro/og-kit-gestion-personal.jpg',
    price: '14.00',
  },
  '/mega-pack-tareas': {
    title: 'Mega Pack Tareas Recurrentes — 13 Kits, 151 Plantillas | AI Chef Pro',
    description: 'Los 13 kits de tareas recurrentes en un solo pack. 151 plantillas Excel para 13 conceptos de hostelería. 89 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-hotel.jpg',
    price: '89.00',
  },
  '/pro-prompts-ebook': {
    title: 'Gastro Pro Prompts — 300+ Prompts de IA para Hostelería | AI Chef Pro',
    description: '300+ prompts de IA para chefs y restaurantes: cocina creativa, pastelería, catering, gestión, marketing. eBook PDF + Dashboard. 9 EUR.',
    image: 'https://aichef.pro/og-image.jpg',
    price: '9.00',
  },
  '/kit-escandallos': {
    title: 'Kit de Escandallos Pro — 11 Plantillas Excel | AI Chef Pro',
    description: '11 plantillas Excel para calcular food cost, escandallos, PVP, menús y control de mermas. 12 EUR.',
    image: 'https://aichef.pro/og-kit-escandallos.jpg',
    price: '12.00',
  },
  '/pack-appcc': {
    title: 'Pack Plantillas APPCC — 17 Registros Excel | AI Chef Pro',
    description: '17 plantillas Excel APPCC: temperaturas, limpieza, trazabilidad, alérgenos, plagas, aceite, agua. 14 EUR.',
    image: 'https://aichef.pro/og-pack-appcc.jpg',
    price: '14.00',
  },
  '/kit-tareas': {
    title: 'Kit Tareas Recurrentes: Restaurante Casual — Checklists Excel | AI Chef Pro',
    description: '11 checklists Excel editables: apertura/cierre, partidas cocina, manager, perfiles, eventos, negocio, caja. 14 EUR.',
    image: 'https://aichef.pro/og-kit-tareas.jpg',
    price: '14.00',
  },
  '/kit-tareas-cafeteria': {
    title: 'Kit Tareas Recurrentes: Cafetería / Brunch | AI Chef Pro',
    description: '11 checklists Excel para cafeterías y brunch: apertura/cierre, barista, manager, eventos, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-cafeteria.jpg',
    price: '12.00',
  },
  '/kit-tareas-pizzeria': {
    title: 'Kit Tareas Recurrentes: Pizzería | AI Chef Pro',
    description: '11 checklists Excel para pizzerías: apertura/cierre, horno, manager, perfiles, eventos, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-pizzeria.jpg',
    price: '12.00',
  },
  '/kit-tareas-hamburgueseria': {
    title: 'Kit Tareas Recurrentes: Hamburguesería | AI Chef Pro',
    description: '11 checklists Excel para hamburgueserías: apertura/cierre, plancha/grill, manager, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-hamburgueseria.jpg',
    price: '12.00',
  },
  '/kit-tareas-dark-kitchen': {
    title: 'Kit Tareas Recurrentes: Dark Kitchen | AI Chef Pro',
    description: '11 checklists Excel para dark kitchens: apertura/cierre, producción, plataformas, packaging, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-dark-kitchen.jpg',
    price: '12.00',
  },
  '/kit-tareas-pasteleria': {
    title: 'Kit Tareas Recurrentes: Pastelería / Obrador | AI Chef Pro',
    description: '11 checklists Excel para pastelerías: apertura/cierre, producción, manager, obrador, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-pasteleria.jpg',
    price: '12.00',
  },
  '/kit-tareas-bar': {
    title: 'Kit Tareas Recurrentes: Bar / Cocktails | AI Chef Pro',
    description: '11 checklists Excel para bares: apertura/cierre, barra, coctelería, manager, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-bar.jpg',
    price: '12.00',
  },
  '/kit-tareas-catering': {
    title: 'Kit Tareas Recurrentes: Catering / Eventos | AI Chef Pro',
    description: '11 checklists Excel para catering: producción, logística, montaje, desmontaje, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-catering.jpg',
    price: '12.00',
  },
  '/kit-tareas-hotel': {
    title: 'Kit Tareas Recurrentes: Hotel Completo — 19 Checklists | AI Chef Pro',
    description: '19 checklists Excel: F&B, recepción, housekeeping, piscina, spa, mantenimiento, negocio, caja. 18,50 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-hotel.jpg',
    price: '18.50',
  },
  '/kit-tareas-heladeria': {
    title: 'Kit Tareas Recurrentes: Heladería Artesanal | AI Chef Pro',
    description: '11 checklists Excel para heladerías: apertura/cierre, producción, vitrina, manager, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-heladeria.jpg',
    price: '12.00',
  },
  '/kit-tareas-chocolateria': {
    title: 'Kit Tareas Recurrentes: Chocolatería / Bombonería | AI Chef Pro',
    description: '11 checklists Excel para chocolaterías: apertura/cierre, producción, temperado, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-chocolateria.jpg',
    price: '12.00',
  },
  '/kit-tareas-restaurante-creativo': {
    title: 'Kit Tareas Recurrentes: Restaurante Creativo / De Autor | AI Chef Pro',
    description: '13 checklists Excel: mise en place degustación, I+D menú, sumiller, brigada creativa, negocio, caja. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-restaurante-creativo.jpg',
    price: '12.00',
  },
  '/kit-tareas-chef-privado': {
    title: 'Kit Tareas Recurrentes: Chef Privado / Personal Chef | AI Chef Pro',
    description: '9 checklists Excel: ficha cliente, menú, equipo, servicio, fidelización, administración. 18 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-chef-privado.jpg',
    price: '18.00',
  },
  '/productos-digitales': {
    title: 'Productos Digitales para Hostelería — Plantillas Excel, Guías y Checklists | AI Chef Pro',
    description: '21+ productos digitales para hostelería: plantillas Excel, guías, checklists, calculadoras. Desde 9 EUR.',
    image: 'https://aichef.pro/og-image.jpg',
  },
};

// Social media bot user agents
const SOCIAL_BOTS = [
  'telegrambot',
  'whatsapp',
  'facebookexternalhit',
  'facebot',
  'twitterbot',
  'linkedinbot',
  'slackbot',
  'discordbot',
  'pinterestbot',
  'skypeuripreview',
];

function isSocialBot(userAgent: string): boolean {
  const ua = userAgent.toLowerCase();
  return SOCIAL_BOTS.some(bot => ua.includes(bot));
}

export default async (request: Request) => {
  const url = new URL(request.url);
  const path = url.pathname.replace(/\/$/, '') || '/';
  const userAgent = request.headers.get('user-agent') || '';

  // Only intercept for social media bots on known product pages
  if (!isSocialBot(userAgent) || !OG_DATA[path]) {
    return;
  }

  const og = OG_DATA[path];

  const html = `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <title>${og.title}</title>
  <meta name="description" content="${og.description}" />
  <meta property="og:title" content="${og.title}" />
  <meta property="og:description" content="${og.description}" />
  <meta property="og:image" content="${og.image}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:url" content="https://aichef.pro${path}" />
  <meta property="og:type" content="product" />
  <meta property="og:site_name" content="AI Chef Pro" />
  <meta property="og:locale" content="es_ES" />
  ${og.price ? `<meta property="product:price:amount" content="${og.price}" />
  <meta property="product:price:currency" content="EUR" />` : ''}
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="${og.title}" />
  <meta name="twitter:description" content="${og.description}" />
  <meta name="twitter:image" content="${og.image}" />
  <link rel="canonical" href="https://aichef.pro${path}" />
</head>
<body>
  <h1>${og.title}</h1>
  <p>${og.description}</p>
  <a href="https://aichef.pro${path}">Ver producto</a>
</body>
</html>`;

  return new Response(html, {
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'cache-control': 'public, max-age=3600',
    },
  });
};

export const config = {
  path: "/*",
};
