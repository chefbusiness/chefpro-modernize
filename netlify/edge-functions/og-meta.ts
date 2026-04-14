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
  '/guia-restaurante-gastronomico': {
    title: 'Cómo Montar un Restaurante Gastronómico 65 Plazas — Guía España (Michelin · Sol Repsol) | AI Chef Pro',
    description: 'Guía premium 80+ págs: 22 capítulos, plan financiero, diseño cocina, brigada, bodega, Michelin, Repsol. 10 plantillas Excel + 8 checklists + business plan. 85 EUR.',
    image: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-gastro-hero.jpg',
    price: '85.00',
  },
  '/guia-restaurante-casual': {
    title: 'Cómo Montar un Restaurante Casual 80 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium 60+ págs: 20 capítulos, plan financiero, delivery, terraza, menú del día. 8 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    image: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
    price: '65.00',
  },
  '/guia-restaurante-mexicano': {
    title: 'Cómo Montar un Restaurante Mexicano 80 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium 60+ págs: 20 capítulos, proveedores mexicanos, barra tequilas, escandallos tacos. 9 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    image: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg',
    price: '65.00',
  },
  '/guia-restaurante-peruano': {
    title: 'Cómo Montar un Restaurante Peruano 80 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium 60+ págs: 20 capítulos, cevichería, Nikkei, barra piscos, proveedores peruanos. 9 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    image: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-peruano-hero.jpg',
    price: '65.00',
  },
  '/guia-restaurante-japones': {
    title: 'Cómo Montar un Restaurante Japonés 60 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium 60+ págs: 20 capítulos, sushi-ya, ramen-ya, izakaya, omakase, robatayaki, pescado sashimi-grade, sake y whisky japonés. 9 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    image: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg',
    price: '65.00',
  },
  '/guia-restaurante-nikkei': {
    title: 'Cómo Montar un Restaurante Nikkei 60 Plazas — Guía Completa España | AI Chef Pro',
    description: 'Guía premium 60+ págs: 20 capítulos, fusión peruano-japonesa, tiraditos, ceviches nikkei, omakase, barra de pisco y sake. 9 plantillas Excel + 6 checklists + business plan. 65 EUR.',
    image: 'https://aichef.pro/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
    price: '65.00',
  },
  '/productos-digitales': {
    title: 'Productos Digitales para Hostelería — Plantillas Excel, Guías y Checklists | AI Chef Pro',
    description: '21+ productos digitales para hostelería: plantillas Excel, guías, checklists, calculadoras. Desde 9 EUR.',
    image: 'https://aichef.pro/og-image.jpg',
  },

  // ── Homepage ──
  '/': {
    title: 'AI Chef Pro — Suite de IA para Profesionales de Hostelería',
    description: '55+ herramientas de inteligencia artificial para chefs, cocineros y profesionales de hostelería. Recetas, escandallos, marketing, gestión de cocina y más. Empieza gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },

  // ── Content / SEO Landing Pages ──
  '/herramientas-ia-para-restaurantes': {
    title: 'Herramientas de IA para Restaurantes | AI Chef Pro',
    description: '55+ herramientas de inteligencia artificial para dueños de restaurantes. Controla costes, diseña carta, gestiona alérgenos y automatiza el marketing. Empieza gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/reducir-costes-restaurante-ia': {
    title: 'Reducir Costes Restaurante con IA | AI Chef Pro',
    description: 'Reduce hasta un 35% las mermas y costes de tu restaurante con inteligencia artificial. Escandallo automático, control de food cost y optimización de carta en tiempo real.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/carta-menu-restaurante-ia': {
    title: 'Carta y Menú de Restaurante con IA | AI Chef Pro',
    description: 'Crea la carta de tu restaurante con inteligencia artificial. Diseño de menú, ingeniería de carta, descripciones atractivas y gestión de alérgenos. Prueba gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/marketing-restaurante-ia': {
    title: 'Marketing para Restaurantes con IA | AI Chef Pro',
    description: 'Automatiza el marketing de tu restaurante con inteligencia artificial. Redes sociales, Google My Business, respuestas a reseñas y campañas en minutos. Prueba gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/chatgpt-para-restaurantes': {
    title: 'ChatGPT para Restaurantes: la IA especializada | AI Chef Pro',
    description: 'ChatGPT para restaurantes vs AI Chef Pro: descubre por qué la IA entrenada en gastronomía da mejores resultados que un modelo genérico. Prueba gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/software-gestion-cocina-ia': {
    title: 'Software Gestión de Cocina con IA | AI Chef Pro',
    description: 'Software de gestión de cocina con IA: escandallos, inventario, recetas y alérgenos en un solo lugar. Más de 5.000 restaurantes ya lo usan. Empieza gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/recetas-ia-restaurantes': {
    title: 'Recetas con IA para Restaurantes | AI Chef Pro',
    description: 'Genera recetas profesionales con IA: 25 cocinas del mundo, menús de temporada, fichas técnicas y escalado automático. Más de 5.000 restaurantes ya lo usan.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/escandallos-restaurante-ia': {
    title: 'Escandallos Restaurante con IA: Food Cost Automático | AI Chef Pro',
    description: 'Calcula escandallos y food cost de tu restaurante con IA en 2 minutos. Control de mermas, precio de venta óptimo y análisis de rentabilidad por plato. Empieza gratis.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/mentoria-online': {
    title: 'Mentoría Online AI Chef Pro | Consultoría Personalizada',
    description: 'Sesiones estratégicas 1:1 con expertos en gastronomía e IA. Acelera resultados en tu negocio gastronómico con asesoría especializada.',
    image: 'https://aichef.pro/og-image.jpg',
  },

  // ── Free Tools ──
  '/herramientas-gratuitas': {
    title: '8 Herramientas Gratuitas de IA para Restaurantes | AI Chef Pro',
    description: 'Herramientas gratuitas de IA para restaurantes: calculadora food cost, simulador de rentabilidad, detector alérgenos, generador de menú y más. Sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/calculadora-food-cost-restaurante': {
    title: 'Calculadora Food Cost Restaurante Gratis | AI Chef Pro',
    description: 'Calcula el food cost de tus platos gratis: ingredientes, gramajes y precio de venta. Resultado instantáneo con semáforo de rentabilidad. Sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/simulador-rentabilidad-restaurante': {
    title: 'Simulador Rentabilidad Restaurante Gratis | AI Chef Pro',
    description: 'Calcula si tu restaurante es rentable: introduce comensales, ticket medio y costes. Beneficio neto y punto de equilibrio al instante. Gratis, sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/test-digitalizacion-restaurante': {
    title: 'Test Digitalización Restaurante Gratis | AI Chef Pro',
    description: 'Descubre en qué nivel de digitalización está tu restaurante en 2 minutos. 6 preguntas, resultado inmediato con plan de acción personalizado. Gratis, sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/detector-alergenos-restaurante': {
    title: 'Detector Alérgenos Restaurante Gratis | AI Chef Pro',
    description: 'Detecta los 14 alérgenos de declaración obligatoria en cualquier plato al instante. Introduce los ingredientes y obtén la ficha de alérgenos. Gratis, sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/calculadora-brigada-restaurante': {
    title: 'Calculadora Brigada Cocina Gratis | AI Chef Pro',
    description: 'Calcula cuántos empleados necesitas en cocina y sala según tu volumen de servicio. Gratis, sin registro. Basado en estándares reales de hostelería.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/calendario-contenidos-restaurante': {
    title: 'Calendario de Contenidos Restaurante Gratis | AI Chef Pro',
    description: 'Genera un calendario editorial de 30 días para tu restaurante gratis. Ideas de posts para Instagram, TikTok y Facebook personalizadas para tu local. Sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/generador-textos-carta-restaurante': {
    title: 'Generador Textos Carta Restaurante Gratis | AI Chef Pro',
    description: 'Genera 3 versiones de descripción para cada plato de tu carta: clásica, emocional y km0. Gratis, sin registro. Mejora tu carta y atrae más clientes.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/generador-menu-degustacion': {
    title: 'Generador Menú Degustación Gratis | AI Chef Pro',
    description: 'Crea un menú degustación completo con IA: nombre poético, descripción sensorial, técnica y maridaje para cada pase. Gratis, sin registro.',
    image: 'https://aichef.pro/og-image.jpg',
  },

  // ── Legal Pages ──
  '/legales': {
    title: 'Aviso Legal | AI Chef Pro',
    description: 'Aviso legal, condiciones de uso e información corporativa de AI Chef Pro.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/cookies': {
    title: 'Política de Cookies | AI Chef Pro',
    description: 'Política de cookies de AI Chef Pro. Información sobre el uso de cookies en nuestra plataforma.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/privacidad': {
    title: 'Política de Privacidad | AI Chef Pro',
    description: 'Política de privacidad de AI Chef Pro. Cómo tratamos y protegemos tus datos personales.',
    image: 'https://aichef.pro/og-image.jpg',
  },
  '/terminos': {
    title: 'Términos y Condiciones | AI Chef Pro',
    description: 'Términos y condiciones de uso de AI Chef Pro y sus productos digitales.',
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
  <meta property="og:type" content="${og.price ? 'product' : 'website'}" />
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
