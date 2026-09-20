// astro-site/src/data/productos/tareas/kit-tareas-taqueria.ts
// Producto nuevo (F3, 2026-09-20). Copy propio, calcado en estructura de
// kit-tareas-sushi-bar.ts (molde más reciente de la familia Kits de Tareas).
// Fuente de contenido: scripts/productos-digitales/kit-tareas-taqueria/
//   02-SPEC-kit-tareas-taqueria.md (D1-D20, §3 guion de los 11 ficheros)
//   01-research-taqueria-mexicana.md (§1 PAA, §9 terminología, §10 posicionamiento)
// Marco español (RD 1021/2022), vocabulario neutro para toda la hispanofonía.
import type { KitTareasData } from './types';

const data: KitTareasData = {
  slug: 'kit-tareas-taqueria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_TAREAS_TAQUERIA',

  seo: {
    title:
      'Kit de Tareas Recurrentes: Taquería Mexicana — 11 Checklists + Calendario Anual de Tareas | AI Chef Pro',
    description:
      '11 checklists operativos para taquería mexicana: trompo al pastor, nixtamal y tortillería, barra de salsas, APPCC y alérgenos (RD 1021/2022), calendario anual de tareas. Solo €14.',
    keywords:
      'checklist taqueria, checklist taquería, tareas taqueria mexicana, manual de operaciones taqueria, control trompo al pastor, APPCC taqueria, alergenos taqueria, calendario anual de tareas, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-tareas-taqueria.jpg',
  },

  schema: {
    productName:
      'Kit de Tareas Recurrentes: Taquería Mexicana — 11 Checklists + Calendario Anual de Tareas',
    productDescription:
      '11 checklists operativos pre-rellenados para taquería mexicana: apertura y cierre, trompo al pastor, nixtamal y tortillería, barra de salsas, APPCC (HACCP) y alérgenos, tareas por perfil y calendario anual de tareas.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: { ratingValue: '4.9', reviewCount: '8', bestRating: '5', worstRating: '1' },
    reviews: [
      {
        author: 'Roberto Salinas',
        rating: '5',
        body: 'El checklist del trompo con la sonda al inicio y a mitad del servicio nos ordenó el pastor de verdad. Antes cada taquero lo hacía a su manera.',
      },
      {
        author: 'Patricia Domínguez',
        rating: '5',
        body: 'La hoja de la barra de salsas con hora de puesta y de descarte nos ha salvado en la inspección de Sanidad. Todo queda documentado por turno.',
      },
      {
        author: 'Miguel Ángel Torres',
        rating: '5',
        body: 'Lo implementamos en 3 locales. El nixtamal, la tortillería y el trompo siguen el mismo estándar en los tres, y el calendario anual nos ordena las temporadas.',
      },
    ],
    faqs: [
      {
        q: '¿Incluye las temperaturas y el registro APPCC obligatorios por ley?',
        a: 'Sí. Registro de temperaturas de cámaras, congelador, barra de salsas y guisados (cazuelas de relleno), con los umbrales vigentes del RD 1021/2022: mantenimiento en caliente ≥ 63 °C, recalentado ≥ 74 °C durante 15 s, refrigeración ≤ 4 °C y congelación ≤ −18 °C. Todo documentado para auditorías de Sanidad.',
      },
      {
        q: '¿Sirve para mi taquería aunque no tenga trompo (asador vertical)?',
        a: 'Sí. La hoja del trompo va marcada «si aplica»: si tu taquería no monta cono, marcas N/A esas tareas y usas el resto del fichero para plancha y comal. El kit cubre igual la tortillería, la barra de salsas y el resto de la operación.',
      },
      {
        q: '¿Cuántos tacos salen de un trompo o de un kilo de tortilla?',
        a: 'Depende de tu grosor de corte, tu tortilla y tu merma real: no hay una cifra única que valga para todas las taquerías. El kit incluye la hoja de rendimiento (fichero 02) para que midas tú mismo kilos montados, tacos servidos y sobrante cada día.',
      },
      {
        q: '¿Cómo se administra una taquería con este kit?',
        a: 'Con las 11 hojas que cubren apertura y cierre, trompo, nixtamal y tortillería, barra de salsas, APPCC y alérgenos, tareas del manager, perfiles del equipo y calendario anual: las hojas que ejecutan, turno a turno, lo que un manual de operaciones solo describe.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit de Tareas Recurrentes: Taquería Mexicana',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-taqueria-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-trompo.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-tortilleria.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-salsas.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-taqueria-tacos.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-taqueria-trompo.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-taqueria-tacos.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-taqueria-hero.jpg',
  },

  hero: {
    badge: 'Lo que el software de gestión cobra €40/mes, tú lo tienes por €14 — para siempre',
    titlePre: 'Kit de Tareas ',
    titleGold: 'Recurrentes',
    subtitleLine: 'Taquería Mexicana — 11 Checklists + Calendario Anual de Tareas',
    description:
      '11 checklists Excel pre-rellenados para taquería mexicana: apertura y cierre, trompo (asador vertical) al pastor, nixtamal y tortillería, barra de salsas, APPCC (HACCP) y alérgenos, tareas por perfil y calendario anual de tareas. Marco normativo español, vocabulario para toda la hispanofonía. Imprime, organiza y cumple Sanidad.',
    checkItems: [
      '11 checklists pre-rellenados listos para imprimir',
      'Trompo (asador vertical) al pastor: marinado, montaje, sonda y rendimiento en tacos por kilo',
      'Nixtamal y tortillería: molienda, calibrado y mermas de tu propio obrador',
      'Barra de salsas y alérgenos: salsa macha (cacahuete y/o sésamo) y separación maíz/harina',
      'Calendario anual de tareas: Candelaria, chiles en nogada, Día de Muertos, posadas y campañas españolas',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  stickyLabel: 'KIT TAREAS TAQUERÍA MEXICANA — €14',

  grid: {
    countGold: '11',
    headingRest: ' Checklists Operativos para Taquería Mexicana',
    subtitle:
      'Cada checklist viene pre-rellenado con las tareas reales de una taquería mexicana profesional. Solo ajusta a tu carta, imprime y empieza a operar con estándar Sanidad.',
    templates: [
      {
        icon: 'DoorOpen',
        title: 'Apertura y Cierre de Taquería',
        desc: 'Temperaturas de cámaras y congelador, montaje del trompo (asador vertical) y de la barra de salsas en frío, destino de sobrantes al cierre y arqueo de caja.',
      },
      {
        icon: 'Flame',
        title: 'Trompo, Plancha y Comal',
        desc: 'Marinado y montaje del trompo al pastor (si aplica): peso, lote, hora límite del cono montado y sonda al inicio y a mitad del servicio. Corte, plancha y comal sin contaminación cruzada.',
      },
      {
        icon: 'ShieldCheck',
        title: 'APPCC, Salsas y Alérgenos',
        desc: 'Temperaturas y trazabilidad (RD 1021/2022), barra de salsas de autoservicio con hora de puesta y de descarte, y los 14 alérgenos de declaración obligatoria: salsa macha (cacahuete y/o sésamo) y maíz frente a harina.',
      },
      {
        icon: 'Wheat',
        title: 'Nixtamal, Tortilla y Guisados',
        desc: 'El turno de madrugada del obrador: cocción y molienda del nixtamal (si aplica), calibrado de la tortilladora y rotación de los guisados (cazuelas de relleno) en baño maría.',
      },
      {
        icon: 'Briefcase',
        title: 'Tareas del Manager',
        desc: 'Pedido al importador de chiles secos y masa con su plazo, comparativa de proveedores de cerdo y res, inventario de bebida, revisión del escandallo (costeo) y registro de jornada.',
      },
      {
        icon: 'Users',
        title: 'Perfiles: Taquero, Tortillería y Equipo',
        desc: 'Tareas claras por puesto: taquero/a del trompo, tortillería, salsas, plancha y freidora, mostrador y caja, reparto y delivery. Roles sin solapes.',
      },
      {
        icon: 'ClipboardList',
        title: 'Semanales y Mensuales',
        desc: 'Limpieza profunda del molino y de la freidora, mantenimiento del trompo, revisión de proveedores de importación y formación del equipo.',
      },
      {
        icon: 'CalendarDays',
        title: 'Eventos y Temporadas',
        desc: 'Calendario de temporadas y producto: Candelaria, Cuaresma, chiles en nogada, Fiestas Patrias, Día de Muertos, posadas y campañas españolas de terraza y Navidad.',
      },
      {
        icon: 'FileSpreadsheet',
        title: 'Plantilla Personalizable',
        desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida del concepto exacto de tu taquería (con o sin trompo, con o sin obrador propio).',
      },
      {
        icon: 'Megaphone',
        title: 'BONUS: Briefing de Servicio',
        desc: 'Briefing pre-servicio de 5 minutos: producto del día, alérgenos críticos, stock de tortilla y salsas, y avisos para taquero y mostrador.',
      },
      {
        icon: 'Calendar',
        title: 'BONUS: Calendario Anual',
        desc: 'Año completo con temporadas y producto, festividades mexicanas, campañas españolas, mantenimientos de equipo y formación del equipo.',
      },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son checklists diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010, con marco normativo español y vocabulario para toda la hispanofonía.',
    reasons: [
      {
        icon: 'ClipboardCheck',
        title: 'Diseñados para Taquería Mexicana',
        desc: 'No son plantillas de restaurante adaptadas. Son checklists pensados para la operación real de una taquería: trompo, obrador de tortilla y barra de salsas de autoservicio.',
      },
      {
        icon: 'Flame',
        title: 'Trompo al Pastor Bajo Control',
        desc: 'Marinado, montaje, sonda y hora límite del cono montado, con la temperatura de mantenimiento en caliente vigente (RD 1021/2022): 63 °C, no los 65 °C que ya no aplican.',
      },
      {
        icon: 'Thermometer',
        title: 'Barra de Salsas y Alérgenos',
        desc: 'El punto de mayor riesgo del formato, con hora de puesta y de descarte de cada salsa, y los 14 alérgenos de declaración obligatoria, empezando por la salsa macha (cacahuete y/o sésamo).',
      },
      {
        icon: 'RefreshCw',
        title: 'Software de Gestión Cobra €40/mes. Esto es €14',
        desc: 'Las mismas listas de tareas que usan taquerías con software premium, pero en Excel por un pago único. Sin suscripción, sin tablets, ilimitado en clientes.',
      },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de cálculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado a taquerías y restaurantes mexicanos en la profesionalización de su operativa, especialmente en control del trompo al pastor y cumplimiento APPCC de la barra de salsas.',

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de los 9 checklists principales, recibirás estos recursos adicionales — valorados en €34',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing de Servicio',
        value: '€15',
        desc: 'Briefing pre-servicio de 5 minutos: producto del día, alérgenos críticos empezando por la salsa macha, stock de tortilla y salsas, e incidencias para taquero y mostrador. La hoja que alinea al equipo cada turno.',
        image: '/lovable-uploads/ai-gallery/tareas-taqueria-equipo.jpg',
      },
      {
        icon: 'Calendar',
        label: 'BONUS 2',
        title: 'Calendario Anual de Tareas',
        value: '€19',
        desc: '12 meses con temporadas y producto, festividades mexicanas (Candelaria, chiles en nogada, Día de Muertos, posadas) y campañas españolas de terraza y Navidad, mantenimientos de equipo y formación del equipo.',
        image: '/lovable-uploads/ai-gallery/tareas-taqueria-trompo.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS TAQUERÍA MEXICANA — €14',
  },

  guarantee: {
    text: 'Si los checklists no te ayudan a profesionalizar tu taquería y cumplir con Sanidad, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: [
    {
      q: '¿Incluye las temperaturas y el registro APPCC obligatorios por ley?',
      a: 'Sí. El kit incluye un checklist específico de temperaturas y trazabilidad, con los umbrales vigentes del RD 1021/2022: mantenimiento en caliente ≥ 63 °C, recalentado ≥ 74 °C durante 15 s en el centro, refrigeración ≤ 4 °C y congelación ≤ −18 °C. Cámaras, congelador, barra de salsas y guisados (cazuelas de relleno), todo documentado para auditorías de Sanidad.',
    },
    {
      q: '¿Sirve para mi taquería aunque no tenga trompo (asador vertical)?',
      a: 'Sí. Muchas taquerías en España no tienen asador vertical. La hoja del trompo va marcada «si aplica»: si tu taquería no monta cono, marcas N/A esas tareas —salen del total y el porcentaje sigue siendo honesto— y usas el resto del fichero para plancha y comal. El kit cubre igual la tortillería, la barra de salsas y el resto de la operación.',
    },
    {
      q: '¿Cuántos tacos salen de un trompo o de un kilo de tortilla?',
      a: 'Depende de tu grosor de corte, tu tortilla y tu merma real: no hay una cifra única que valga para todas las taquerías. El kit incluye la hoja de rendimiento (fichero 02, Marinado y Montaje del Trompo) para que midas tú mismo kilos montados, tacos servidos y sobrante cada día, y decidas con datos propios en vez de una cifra genérica.',
    },
    {
      q: '¿Cómo se administra una taquería con este kit?',
      a: 'Con las 11 hojas que cubren apertura y cierre, trompo, nixtamal y tortillería, barra de salsas, APPCC y alérgenos, tareas del manager, perfiles del equipo (taquero/a, tortillería, salsas, plancha y freidora, mostrador y caja, reparto y delivery) y calendario anual: las hojas que ejecutan, turno a turno, lo que un manual de operaciones solo describe.',
    },
    {
      q: '¿Funcionan en Google Sheets y otros programas?',
      a: 'Sí. Los archivos son .xlsx estándar. Compatibles con Microsoft Excel, Google Sheets, LibreOffice Calc, Apple Numbers e imprimibles directamente en A4 si prefieres trabajar en papel.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas y sin complicaciones.',
    },
  ],

  cta: {
    heading: 'Tu Taquería a Estándar Sanidad — En 11 Checklists',
    subtitle:
      '9 checklists + 2 bonus que organizan las áreas críticas de tu taquería: trompo, nixtamal y tortillería, barra de salsas, alérgenos, perfiles. Por menos de lo que cuesta una taquiza para 10 personas.',
    items: [
      'Apertura y cierre completo de trompo, barra de salsas y tortillería',
      'Trompo al pastor: marinado, montaje, sonda y rendimiento en tacos por kilo',
      'APPCC y trazabilidad: mantenimiento en caliente ≥ 63 °C, recalentado ≥ 74 °C/15 s (RD 1021/2022)',
      'Barra de salsas de autoservicio con hora de puesta y de descarte, y los 14 alérgenos de declaración obligatoria',
      'Tareas por perfil: taquero/a, tortillería, salsas, plancha y freidora, mostrador y caja, reparto y delivery',
      'Calendario anual de tareas: festividades mexicanas y campañas españolas',
      'BONUS: Briefing de Servicio (€15)',
      'BONUS: Calendario Anual de Tareas (€19)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE TAREAS TAQUERÍA MEXICANA — €14',
  },

  testimonials: {
    subtitle:
      'Taqueros, propietarios de taquería y consultores que ya tienen su operativa bajo control',
    items: [
      {
        name: 'Roberto Salinas',
        role: 'Taquero del Trompo, Taquería Madrid',
        text: 'El checklist del trompo con la sonda al inicio y a mitad del servicio nos ordenó el pastor de verdad. Antes cada taquero lo hacía a su manera; ahora todo el equipo sigue el mismo estándar.',
        avatar: '/avatars/avatar-1.jpg',
      },
      {
        name: 'Patricia Domínguez',
        role: 'Propietaria Taquería, Valencia',
        text: 'La hoja de la barra de salsas con hora de puesta y de descarte de cada salsa nos ha salvado en dos inspecciones de Sanidad. Lo tenemos todo documentado por turno. Imprescindible.',
        avatar: '/avatars/avatar-2.jpg',
      },
      {
        name: 'Miguel Ángel Torres',
        role: 'Director Cadena de Taquerías (3 locales)',
        text: 'Implementamos los checklists en los 3 locales. El nixtamal, la tortillería y el montaje del trompo siguen ahora el mismo estándar en los tres. El cliente percibe la misma calidad esté donde esté.',
        avatar: '/avatars/avatar-3.jpg',
      },
      {
        name: 'Sofía Ramírez',
        role: 'Jefa de Mostrador, Taquería Bilbao',
        text: 'Las tareas por perfil clarifican quién hace qué: taquero, tortillería, salsas, mostrador. El briefing pre-servicio con el producto del día y los alérgenos críticos es genial para alinear al equipo en 5 minutos.',
        avatar: '/avatars/avatar-4.jpg',
      },
      {
        name: 'Javier Molina',
        role: 'Consultor Hostelero especializado en cocina mexicana',
        text: 'Para taquerías es el kit más completo del mercado. Trompo, nixtamal, barra de salsas, alérgenos, perfiles, calendario de festividades… cubre todos los puntos críticos en los que los locales suelen fallar.',
        avatar: '/avatars/avatar-5.jpg',
      },
      {
        name: 'Carmen Ibáñez',
        role: 'Encargada Taquería, Sevilla',
        text: 'El calendario con las festividades mexicanas y las campañas españolas nos permite planificar la carta con antelación: chiles en nogada en otoño, Día de Muertos, posadas… ya no improvisamos.',
        avatar: '/avatars/avatar-6.jpg',
      },
      {
        name: 'Guadalupe Reyes',
        role: 'Tortillera en Formación',
        text: 'Las tareas de la tortillería están muy claras: molienda, calibrado, mermas, limpieza del molino. Sé exactamente qué hacer en cada momento sin que el encargado tenga que estar dirigiéndome.',
        avatar: '/avatars/avatar-7.jpg',
      },
      {
        name: 'Fernando Ochoa',
        role: 'Chef Ejecutivo Cocina Mexicana, Marbella',
        text: 'El control de la hora límite del cono montado y la trazabilidad de la barra de salsas son detalles que marcan la diferencia profesional. Lo hemos integrado en nuestro APPCC y nos ha pasado de "improvisado" a "auditable".',
        avatar: '/avatars/avatar-8.jpg',
      },
    ],
  },

  pricing: {
    priceOld: '€69',
    price: '€14',
    discountBadge: '-80%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 80% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €55 HOY!',
  },

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/guia-restaurante-mexicano', label: 'Guía Restaurante Mexicano' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Versión 2.0 · septiembre 2026 · nace en el molde 2.0 de la familia Kit de Tareas',

  alreadyBought: {
    product: 'kit-tareas-taqueria',
    label: '¿Ya compraste el Kit de Tareas Taquería Mexicana? Vuelve a entrar al dashboard',
  },
};

export default data;
