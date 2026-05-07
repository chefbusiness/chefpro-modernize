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
  '/kit-tareas-sushi-bar': {
    title: 'Kit Tareas Recurrentes: Sushi Bar — Protocolo Anisakis APPCC | AI Chef Pro',
    description: '11 checklists Excel: barra sushi, arroz con control pH, anisakis APPCC (RD 1420/2006), neta case, itamae, omakase. 14 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-sushi-bar.jpg',
    price: '14.00',
  },
  '/kit-tareas-asador': {
    title: 'Kit Tareas Recurrentes: Asador / Parrilla y Horno Josper | AI Chef Pro',
    description: '11 checklists Excel: encendido y mantenimiento Josper, maduración dry-age, despiece, temperaturas por corte, pescados y verduras a la brasa. 14 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-asador.jpg',
    price: '14.00',
  },
  '/kit-tareas-marisqueria': {
    title: 'Kit Tareas Recurrentes: Marisquería con Vivero y APPCC | AI Chef Pro',
    description: '11 checklists Excel: control vivero (oxígeno, salinidad), expositor de hielo, trazabilidad APPCC marisco (UE 1379/2013), alérgenos, lonjas y temporadas de pesca. 14 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-marisqueria.jpg',
    price: '14.00',
  },
  '/kit-tareas-tapas-bar': {
    title: 'Kit Tareas Recurrentes: Tapas Bar / Gastrobar — Checklists Operativos | AI Chef Pro',
    description: '11 checklists Excel: barra de pinchos, cocina raciones, cerveza grifo, vinos, vermut, terraza y rotación carta estacional. 14 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-tapas-bar.jpg',
    price: '14.00',
  },
  '/kit-tareas-food-truck': {
    title: 'Kit Tareas Recurrentes: Food Truck — Setup, APPCC Móvil y Permisos | AI Chef Pro',
    description: '11 checklists Excel: setup y teardown, operaciones móviles, APPCC móvil, permisos por evento, vehículo, generador y calendario anual. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-food-truck.jpg',
    price: '12.00',
  },
  '/kit-tareas-panaderia': {
    title: 'Kit Tareas Recurrentes: Panadería / Obrador — Masas Madre, Hornos y Turno Madrugada | AI Chef Pro',
    description: '11 checklists Excel: turno madrugada desde las 03:00, masas madre y pre-fermentos, hornos de piso y rotativo, expositor, campañas estacionales y calendario anual. 12 EUR.',
    image: 'https://aichef.pro/og-kit-tareas-panaderia.jpg',
    price: '12.00',
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

  // ── Use Cases Hub ──
  '/usos': {
    title: 'Casos de uso de AI Chef Pro: por rol y por concepto | AI Chef Pro',
    description: 'Descubre cómo usar AI Chef Pro según tu perfil profesional o tipo de negocio: chef ejecutivo, propietario, gerente, pizzería, dark kitchen, hotel, catering y más.',
    image: 'https://aichef.pro/og/use-cases/hub.jpg',
  },

  // ── Use Cases — Roles ──
  '/usos/rol/propietario-restaurante': {
    title: 'IA para propietarios de restaurante | AI Chef Pro',
    description: 'Toma mejores decisiones: escandallos, plan financiero, APPCC y marketing con IA especializada en hostelería.',
    image: 'https://aichef.pro/og/use-cases/propietario-restaurante.jpg',
  },
  '/usos/rol/gerente-restaurante': {
    title: 'IA para gerentes y managers de restaurante | AI Chef Pro',
    description: 'Optimiza turnos, inventario, APPCC y reporting con IA. Caja de herramientas digital para managers.',
    image: 'https://aichef.pro/og/use-cases/gerente-restaurante.jpg',
  },
  '/usos/rol/director-operaciones-grupo-restauracion': {
    title: 'IA para directores de operaciones de grupos de restauración | AI Chef Pro',
    description: 'Estandariza procesos, consolida KPIs y replica manuales operativos en grupos multi-local con IA.',
    image: 'https://aichef.pro/og/use-cases/director-operaciones-grupo.jpg',
  },
  '/usos/rol/chef-ejecutivo-corporativo': {
    title: 'IA para chef ejecutivo y corporativo | AI Chef Pro',
    description: 'Estandariza recetas, calcula escandallos y crea manuales replicables en múltiples unidades con IA gastronómica.',
    image: 'https://aichef.pro/og/use-cases/chef-ejecutivo.jpg',
  },
  '/usos/rol/chef-jefe-cocina': {
    title: 'IA para chef de cocina y jefe de cocina | AI Chef Pro',
    description: 'Escandallos, fichas técnicas, APPCC y formación de equipo con IA gastronómica profesional.',
    image: 'https://aichef.pro/og/use-cases/chef-cocina.jpg',
  },
  '/usos/rol/sous-chef': {
    title: 'IA para sous chef | AI Chef Pro',
    description: 'Mise en place, fichas técnicas, APPCC y formación con IA pensada para sous chef en cocina profesional.',
    image: 'https://aichef.pro/og/use-cases/sous-chef.jpg',
  },
  '/usos/rol/chef-catering': {
    title: 'IA para chef de catering | AI Chef Pro',
    description: 'Escandallos por evento, producción a escala, APPCC fuera de local y diseño de menús con IA gastronómica.',
    image: 'https://aichef.pro/og/use-cases/chef-catering.jpg',
  },
  '/usos/rol/propietario-empresa-catering': {
    title: 'IA para propietarios de empresa de catering | AI Chef Pro',
    description: 'Rentabilidad por evento, producción a escala, gestión de equipos eventuales y plan financiero para catering.',
    image: 'https://aichef.pro/og/use-cases/propietario-catering.jpg',
  },

  // ── Use Cases — Conceptos ──
  '/usos/concepto/restaurante-casual': {
    title: 'IA para restaurante casual | AI Chef Pro',
    description: 'Escandallos, APPCC, cuadrantes y marketing con IA para restaurantes casuales. Más control, menos papeleo.',
    image: 'https://aichef.pro/og/use-cases/restaurante-casual.jpg',
  },
  '/usos/concepto/cafeteria-brunch': {
    title: 'IA para cafetería y brunch | AI Chef Pro',
    description: 'Escandallos, APPCC, listas de turno y marketing con IA para cafeterías de especialidad y locales de brunch.',
    image: 'https://aichef.pro/og/use-cases/cafeteria-brunch.jpg',
  },
  '/usos/concepto/pizzeria': {
    title: 'IA para pizzería | AI Chef Pro',
    description: 'Escandallos por pizza, control de delivery, APPCC y marketing con IA especializada en pizzería profesional.',
    image: 'https://aichef.pro/og/use-cases/pizzeria.jpg',
  },
  '/usos/concepto/hamburgueseria': {
    title: 'IA para hamburguesería | AI Chef Pro',
    description: 'Escandallos por burger, control de carne y delivery, APPCC y marketing con IA especializada.',
    image: 'https://aichef.pro/og/use-cases/hamburgueseria.jpg',
  },
  '/usos/concepto/dark-kitchen': {
    title: 'IA para dark kitchen | AI Chef Pro',
    description: 'Escandallos multi-marca, gestión de plataformas, APPCC y branding para dark kitchens con IA especializada.',
    image: 'https://aichef.pro/og/use-cases/dark-kitchen.jpg',
  },
  '/usos/concepto/pasteleria-obrador': {
    title: 'IA para pastelería y obrador | AI Chef Pro',
    description: 'Escandallos por pieza, APPCC, trazabilidad y branding para pastelerías y obradores con IA especializada.',
    image: 'https://aichef.pro/og/use-cases/pasteleria-obrador.jpg',
  },
  '/usos/concepto/bar-cocktails': {
    title: 'IA para bar y coctelería | AI Chef Pro',
    description: 'Escandallos de cócteles, cartas, APPCC y branding con IA especializada en bar y coctelería profesional.',
    image: 'https://aichef.pro/og/use-cases/bar-cocktails.jpg',
  },
  '/usos/concepto/catering-eventos': {
    title: 'IA para catering y eventos | AI Chef Pro',
    description: 'Escandallos por evento, producción a escala, APPCC fuera de local y propuestas comerciales con IA.',
    image: 'https://aichef.pro/og/use-cases/catering-eventos.jpg',
  },
  '/usos/concepto/hotel-completo-fb': {
    title: 'IA para hotel completo (F&B y housekeeping) | AI Chef Pro',
    description: 'Gestiona F&B completo: desayunos, restaurante, bar, room service y banquetes con IA pensada para F&B Manager.',
    image: 'https://aichef.pro/og/use-cases/hotel-completo.jpg',
  },
  '/usos/concepto/heladeria-artesanal': {
    title: 'IA para heladería artesanal | AI Chef Pro',
    description: 'Escandallos por sabor, control de obrador, vitrina y APPCC con IA especializada en heladería artesanal.',
    image: 'https://aichef.pro/og/use-cases/heladeria.jpg',
  },
  '/usos/concepto/chocolateria-bomboneria': {
    title: 'IA para chocolatería y bombonería | AI Chef Pro',
    description: 'Escandallos por pieza, producción estacional, APPCC y branding con IA especializada en chocolatería.',
    image: 'https://aichef.pro/og/use-cases/chocolateria.jpg',
  },
  '/usos/concepto/restaurante-creativo-autor': {
    title: 'IA para restaurante creativo y de autor | AI Chef Pro',
    description: 'Brainstorming, escandallos, fichas técnicas y storytelling para restaurantes de autor con IA gastronómica.',
    image: 'https://aichef.pro/og/use-cases/restaurante-creativo.jpg',
  },
  '/usos/concepto/restaurante-gastronomico-michelin': {
    title: 'IA para restaurante gastronómico (Michelin/Repsol) | AI Chef Pro',
    description: 'Escandallos premium, menús degustación, brigada y comunicación con IA especializada en alta gastronomía.',
    image: 'https://aichef.pro/og/use-cases/restaurante-gastronomico.jpg',
  },

  // ── Use Cases EN — Hub ──
  '/en/use-cases': {
    title: 'AI Chef Pro Use Cases: by professional role and business concept | AI Chef Pro',
    description: 'See how to use AI Chef Pro by professional profile or hospitality concept: executive chef, owner, manager, pizzeria, dark kitchen, hotel, catering, and more.',
    image: 'https://aichef.pro/og/use-cases/hub.jpg',
  },

  // ── Use Cases EN — Roles ──
  '/en/use-cases/role/restaurant-owner': {
    title: 'AI for Restaurant Owners | AI Chef Pro',
    description: 'Make better decisions: recipe costing, financial plan, HACCP, and marketing with AI built for hospitality.',
    image: 'https://aichef.pro/og/use-cases/en/restaurant-owner.jpg',
  },
  '/en/use-cases/role/restaurant-manager': {
    title: 'AI for Restaurant Managers | AI Chef Pro',
    description: 'Optimize shifts, inventory, HACCP, and reporting with AI. Digital toolbox for managers.',
    image: 'https://aichef.pro/og/use-cases/en/restaurant-manager.jpg',
  },
  '/en/use-cases/role/operations-director-restaurant-group': {
    title: 'AI for Multi-Unit Operations Directors | AI Chef Pro',
    description: 'Standardize processes, consolidate KPIs, and replicate operational manuals across multi-unit groups with AI.',
    image: 'https://aichef.pro/og/use-cases/en/operations-director-restaurant-group.jpg',
  },
  '/en/use-cases/role/executive-corporate-chef': {
    title: 'AI for Executive & Corporate Chefs | AI Chef Pro',
    description: 'Standardize recipes, calculate plate costs, and build replicable manuals across multiple units with culinary AI.',
    image: 'https://aichef.pro/og/use-cases/en/executive-corporate-chef.jpg',
  },
  '/en/use-cases/role/head-chef': {
    title: 'AI for Head Chefs | AI Chef Pro',
    description: 'Recipe costing, spec sheets, HACCP, and team training with professional culinary AI.',
    image: 'https://aichef.pro/og/use-cases/en/head-chef.jpg',
  },
  '/en/use-cases/role/sous-chef': {
    title: 'AI for Sous Chefs | AI Chef Pro',
    description: 'Mise en place, spec sheets, HACCP, and training with AI built for sous chefs in professional kitchens.',
    image: 'https://aichef.pro/og/use-cases/en/sous-chef.jpg',
  },
  '/en/use-cases/role/catering-chef': {
    title: 'AI for Catering Chefs | AI Chef Pro',
    description: 'Per-event recipe costing, production at scale, off-site HACCP, and menu design with culinary AI.',
    image: 'https://aichef.pro/og/use-cases/en/catering-chef.jpg',
  },
  '/en/use-cases/role/catering-business-owner': {
    title: 'AI for Catering Company Owners | AI Chef Pro',
    description: 'Per-event profitability, production at scale, temporary-team management, and financial plan for catering.',
    image: 'https://aichef.pro/og/use-cases/en/catering-business-owner.jpg',
  },
  '/en/use-cases/role/bartender-mixologist': {
    title: 'AI for Bartenders & Mixologists | AI Chef Pro',
    description: 'Cocktail menu costing, signature drinks with storytelling, pairings, and bar HACCP with culinary AI.',
    image: 'https://aichef.pro/og/use-cases/en/bartender-mixologist.jpg',
  },
  '/en/use-cases/role/pizzaiolo': {
    title: 'AI for Pizzaiolos & Pizza Chefs | AI Chef Pro',
    description: 'Doughs and fermentations, per-pizza costing, oven technique, and HACCP with professional Italian-cooking AI.',
    image: 'https://aichef.pro/og/use-cases/en/pizzaiolo.jpg',
  },
  '/en/use-cases/role/artisan-baker': {
    title: 'AI for Artisan Bakers | AI Chef Pro',
    description: 'Sourdough and pre-ferments, per-piece costing with production-kitchen labor cost, and HACCP for artisan baking.',
    image: 'https://aichef.pro/og/use-cases/en/artisan-baker.jpg',
  },
  '/en/use-cases/role/chocolatier': {
    title: 'AI for Chocolatiers | AI Chef Pro',
    description: 'Bonbons, tempering, per-piece costing, seasonal planning, and HACCP for signature artisan chocolate making.',
    image: 'https://aichef.pro/og/use-cases/en/chocolatier.jpg',
  },
  '/en/use-cases/role/private-personal-chef': {
    title: 'AI for Private & Personal Chefs | AI Chef Pro',
    description: 'Personalized menus, per-dinner costing, in-home mise, and signature branding for professional private chefs.',
    image: 'https://aichef.pro/og/use-cases/en/private-personal-chef.jpg',
  },
  '/en/use-cases/role/hotel-fb-manager': {
    title: 'AI for Hotel F&B Managers | AI Chef Pro',
    description: 'Coordinate restaurants, banquets, room service, breakfast, and bars with cross-outlet recipe costing and integrated branding.',
    image: 'https://aichef.pro/og/use-cases/en/hotel-fb-manager.jpg',
  },
  '/en/use-cases/role/maitre-d-head-waiter': {
    title: 'AI for Maîtres & Floor Managers | AI Chef Pro',
    description: 'Floor service, premium reservations, pairings, and team training with culinary AI for fine-dining service.',
    image: 'https://aichef.pro/og/use-cases/en/maitre-d-head-waiter.jpg',
  },
  '/en/use-cases/role/sommelier': {
    title: 'AI for Sommeliers | AI Chef Pro',
    description: 'Wine list, food-science pairings, cellar traceability, and wine-driven branding for professional sommellerie.',
    image: 'https://aichef.pro/og/use-cases/en/sommelier.jpg',
  },
  '/en/use-cases/role/master-grillmaster': {
    title: 'AI for Master Grill Chefs & Asadores | AI Chef Pro',
    description: 'Fire technique, butchering, dry-aged, per-cut recipe costing, and fire-driven branding for professional grill cooking.',
    image: 'https://aichef.pro/og/use-cases/en/master-grillmaster.jpg',
  },
  '/en/use-cases/role/master-gelato-maker': {
    title: 'AI for Master Ice Cream Makers & Gelatieri | AI Chef Pro',
    description: 'Technical balance of bases, per-flavor costing, seasonal planning, and artisan branding for professional ice cream making.',
    image: 'https://aichef.pro/og/use-cases/en/master-gelato-maker.jpg',
  },
  '/en/use-cases/role/pastry-chef': {
    title: 'AI for Pastry Chefs & Pâtissiers | AI Chef Pro',
    description: 'Advanced pastry technique, per-piece costing with production-kitchen labor cost, and seasonal planning for signature pastry.',
    image: 'https://aichef.pro/og/use-cases/en/pastry-chef.jpg',
  },

  // ── Use Cases EN — Concepts ──
  '/en/use-cases/concept/casual-restaurant': {
    title: 'AI for Casual Restaurants | AI Chef Pro',
    description: 'Recipe costing, HACCP, scheduling, and marketing with AI for casual restaurants. More control, less paperwork.',
    image: 'https://aichef.pro/og/use-cases/en/casual-restaurant.jpg',
  },
  '/en/use-cases/concept/cafe-brunch': {
    title: 'AI for Coffee Shops & Brunch | AI Chef Pro',
    description: 'Recipe costing, HACCP, shift checklists, and marketing with AI for specialty coffee shops and brunch spots.',
    image: 'https://aichef.pro/og/use-cases/en/cafe-brunch.jpg',
  },
  '/en/use-cases/concept/pizzeria': {
    title: 'AI for Pizzerias | AI Chef Pro',
    description: 'Per-pizza recipe costing, delivery control, HACCP, and marketing with AI specialized in professional pizzeria.',
    image: 'https://aichef.pro/og/use-cases/en/pizzeria.jpg',
  },
  '/en/use-cases/concept/burger-restaurant': {
    title: 'AI for Burger Joints | AI Chef Pro',
    description: 'Per-burger recipe costing, meat and delivery control, HACCP, and marketing with specialized AI.',
    image: 'https://aichef.pro/og/use-cases/en/burger-restaurant.jpg',
  },
  '/en/use-cases/concept/dark-kitchen': {
    title: 'AI for Dark Kitchens | AI Chef Pro',
    description: 'Multi-brand recipe costing, platform management, HACCP, and branding for dark kitchens with specialized AI.',
    image: 'https://aichef.pro/og/use-cases/en/dark-kitchen.jpg',
  },
  '/en/use-cases/concept/bakery-pastry-shop': {
    title: 'AI for Pastry Shops & Production Kitchens | AI Chef Pro',
    description: 'Per-piece costing, HACCP, traceability, and branding for pastry shops and production kitchens with specialized AI.',
    image: 'https://aichef.pro/og/use-cases/en/bakery-pastry-shop.jpg',
  },
  '/en/use-cases/concept/bar-cocktails': {
    title: 'AI for Bars & Cocktails | AI Chef Pro',
    description: 'Cocktail recipe costing, menus, HACCP, and branding with AI specialized in professional bar and mixology.',
    image: 'https://aichef.pro/og/use-cases/en/bar-cocktails.jpg',
  },
  '/en/use-cases/concept/catering-events': {
    title: 'AI for Catering & Events | AI Chef Pro',
    description: 'Per-event recipe costing, production at scale, off-site HACCP, and commercial proposals with AI.',
    image: 'https://aichef.pro/og/use-cases/en/catering-events.jpg',
  },
  '/en/use-cases/concept/hotel-fb-complete': {
    title: 'AI for Full-Service Hotels (F&B + Housekeeping) | AI Chef Pro',
    description: 'Manage full F&B: breakfast, restaurant, bar, room service, and banquets with AI built for F&B Managers.',
    image: 'https://aichef.pro/og/use-cases/en/hotel-fb-complete.jpg',
  },
  '/en/use-cases/concept/artisan-ice-cream-shop': {
    title: 'AI for Artisan Ice Cream Shops | AI Chef Pro',
    description: 'Per-flavor recipe costing, production kitchen control, display, and HACCP with specialized AI for artisan ice cream.',
    image: 'https://aichef.pro/og/use-cases/en/artisan-ice-cream-shop.jpg',
  },
  '/en/use-cases/concept/chocolate-shop': {
    title: 'AI for Chocolate Shops & Bonbon Shops | AI Chef Pro',
    description: 'Per-piece costing, seasonal production, HACCP, and branding with AI specialized in chocolate making.',
    image: 'https://aichef.pro/og/use-cases/en/chocolate-shop.jpg',
  },
  '/en/use-cases/concept/creative-signature-restaurant': {
    title: 'AI for Creative & Signature Restaurants | AI Chef Pro',
    description: 'Brainstorming, recipe costing, spec sheets, and storytelling for signature restaurants with culinary AI.',
    image: 'https://aichef.pro/og/use-cases/en/creative-signature-restaurant.jpg',
  },
  '/en/use-cases/concept/fine-dining-michelin': {
    title: 'AI for Fine Dining (Michelin / Repsol) | AI Chef Pro',
    description: 'Premium recipe costing, tasting menus, brigade, and communication with AI specialized in fine dining.',
    image: 'https://aichef.pro/og/use-cases/en/fine-dining-michelin.jpg',
  },
  '/en/use-cases/concept/mexican-restaurant': {
    title: 'AI for Mexican Restaurants | AI Chef Pro',
    description: 'Salsas, per-taco recipe costing, holiday planning, branding, and HACCP with AI specialized in authentic Mexican cuisine.',
    image: 'https://aichef.pro/og/use-cases/en/mexican-restaurant.jpg',
  },
  '/en/use-cases/concept/peruvian-restaurant': {
    title: 'AI for Peruvian Restaurants | AI Chef Pro',
    description: 'Ceviches, per-dish costing, holiday planning, branding, and HACCP with AI specialized in authentic Peruvian cuisine.',
    image: 'https://aichef.pro/og/use-cases/en/peruvian-restaurant.jpg',
  },
  '/en/use-cases/concept/japanese-restaurant': {
    title: 'AI for Japanese Restaurants | AI Chef Pro',
    description: 'Sushi, per-piece recipe costing, ferments, holiday planning, and minimalist branding for professional Japanese cooking.',
    image: 'https://aichef.pro/og/use-cases/en/japanese-restaurant.jpg',
  },
  '/en/use-cases/concept/nikkei-restaurant': {
    title: 'AI for Nikkei Restaurants | AI Chef Pro',
    description: 'Tiraditos, fusion sushi, per-dish costing, and branding with AI specialized in authentic Peruvian-Japanese fusion.',
    image: 'https://aichef.pro/og/use-cases/en/nikkei-restaurant.jpg',
  },
  '/en/use-cases/concept/plant-based-vegan-restaurant': {
    title: 'AI for Plant-Based & Vegan Restaurants | AI Chef Pro',
    description: 'Plant-based menus, per-bowl costing, vegetable ferments, and fresh branding for professional plant-based cooking.',
    image: 'https://aichef.pro/og/use-cases/en/plant-based-vegan-restaurant.jpg',
  },
  '/en/use-cases/concept/steakhouse-grill': {
    title: 'AI for Steakhouses, Grills & Asadores | AI Chef Pro',
    description: 'Per-cut recipe costing, dry-aged management, fire technique, and branding for professional fire cooking.',
    image: 'https://aichef.pro/og/use-cases/en/steakhouse-grill.jpg',
  },
  '/en/use-cases/concept/specialty-coffee-shop': {
    title: 'AI for Specialty Coffee Shops | AI Chef Pro',
    description: 'Per-drink recipe costing, in-house pastry, third-wave technique, and minimalist branding for specialty coffee.',
    image: 'https://aichef.pro/og/use-cases/en/specialty-coffee-shop.jpg',
  },
  '/en/use-cases/concept/sushi-bar': {
    title: 'AI for Sushi Bars | AI Chef Pro',
    description: 'Itamae technique, per-nigiri recipe costing, signature omakase, and minimalist branding for professional sushi bars.',
    image: 'https://aichef.pro/og/use-cases/en/sushi-bar.jpg',
  },
  '/en/use-cases/concept/gastrobar-tapas-bar': {
    title: 'AI for Gastrobars & Tapas Bars | AI Chef Pro',
    description: 'Per-tapa recipe costing, vermouth and wines by the glass, pairings, and HACCP with AI specialized in Spanish cuisine.',
    image: 'https://aichef.pro/og/use-cases/en/gastrobar-tapas-bar.jpg',
  },
  '/en/use-cases/concept/food-truck': {
    title: 'AI for Food Trucks | AI Chef Pro',
    description: 'Compact menu, per-dish recipe costing, event planning, viral branding, and HACCP for professional food-truck operations.',
    image: 'https://aichef.pro/og/use-cases/en/food-truck.jpg',
  },
  '/en/use-cases/concept/italian-restaurant': {
    title: 'AI for Italian Restaurants | AI Chef Pro',
    description: 'Fresh pasta, per-dish recipe costing, traditional sauces, Italian wines, and trattoria branding for professional Italian cooking.',
    image: 'https://aichef.pro/og/use-cases/en/italian-restaurant.jpg',
  },

  // ── Use Cases EN — Tasks ──
  '/en/use-cases/task/recipe-costing-with-ai': {
    title: 'How to Do Recipe Costing with AI | AI Chef Pro',
    description: 'Calculate real per-dish cost, food cost %, and suggested price in minutes with culinary AI. Recipe + costing CSV with production-kitchen labor cost.',
    image: 'https://aichef.pro/og/use-cases/en/recipe-costing-with-ai.jpg',
  },
  '/en/use-cases/task/tasting-menu-with-ai': {
    title: 'How to Design a Tasting Menu with AI | AI Chef Pro',
    description: 'Tasting menus with coherent sequence, validated total recipe costing, food-science pairings, and floor storytelling.',
    image: 'https://aichef.pro/og/use-cases/en/tasting-menu-with-ai.jpg',
  },
  '/en/use-cases/task/technical-recipe-sheets-with-ai': {
    title: 'How to Create Spec Sheets with AI | AI Chef Pro',
    description: 'Document every dish with a professional spec sheet: ingredients, gram weights, technique, automatic allergens, food cost, and storytelling.',
    image: 'https://aichef.pro/og/use-cases/en/technical-recipe-sheets-with-ai.jpg',
  },
  '/en/use-cases/task/wine-pairings-with-ai': {
    title: 'How to Validate Pairings with AI | AI Chef Pro',
    description: 'Pairings with food-science backing: acidity, tannin, structure, intensity, and harmony. AI suite with professional sommelier technique.',
    image: 'https://aichef.pro/og/use-cases/en/wine-pairings-with-ai.jpg',
  },
  '/en/use-cases/task/reduce-food-waste-with-ai': {
    title: 'How to Reduce Kitchen Shrinkage with AI | AI Chef Pro',
    description: 'Identify, measure, and reduce per-process shrinkage with real data integrated into recipe costing. AI suite specialized in zero-waste operations.',
    image: 'https://aichef.pro/og/use-cases/en/reduce-food-waste-with-ai.jpg',
  },
  '/en/use-cases/task/digital-haccp-with-ai': {
    title: 'How to Manage Digital HACCP with AI | AI Chef Pro',
    description: 'Replace scattered printed paper with mobile HACCP using professional templates: temperatures, cleaning, traceability, allergens, pests, oil, and water.',
    image: 'https://aichef.pro/og/use-cases/en/digital-haccp-with-ai.jpg',
  },
  '/en/use-cases/task/seasonal-menu-with-ai': {
    title: 'How to Design a Seasonal Menu with AI | AI Chef Pro',
    description: 'Seasonal menu with local in-season product, professional recipe costing, advance planning, and producer storytelling.',
    image: 'https://aichef.pro/og/use-cases/en/seasonal-menu-with-ai.jpg',
  },
  '/en/use-cases/task/food-photography-with-ai': {
    title: 'How to Do Food Photography with AI | AI Chef Pro',
    description: 'Generate a professional reference image of the dish before cooking to validate plating, palette, and composition. Then take the final photo of the real dish.',
    image: 'https://aichef.pro/og/use-cases/en/food-photography-with-ai.jpg',
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

  // Detect language from path prefix. ES is the default; other supported locales use a /xx/ prefix.
  const langCode = (() => {
    const m = path.match(/^\/(en|fr|de|it|pt|nl)(\/|$)/);
    return m ? m[1] : 'es';
  })();
  const ogLocale = ({
    es: 'es_ES',
    en: 'en_US',
    fr: 'fr_FR',
    de: 'de_DE',
    it: 'it_IT',
    pt: 'pt_PT',
    nl: 'nl_NL',
  } as const)[langCode] ?? 'es_ES';
  const viewLink = ({
    es: 'Ver',
    en: 'View',
    fr: 'Voir',
    de: 'Anzeigen',
    it: 'Vedi',
    pt: 'Ver',
    nl: 'Bekijken',
  } as const)[langCode] ?? 'Ver';

  const html = `<!DOCTYPE html>
<html lang="${langCode}">
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
  <meta property="og:locale" content="${ogLocale}" />
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
  <a href="https://aichef.pro${path}">${viewLink}</a>
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
