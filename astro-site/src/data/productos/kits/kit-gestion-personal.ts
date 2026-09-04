// astro-site/src/data/productos/kits/kit-gestion-personal.ts
// LÍNEA KITS EXCEL — producto kit-gestion-personal.
//
// ⚠ RC-15 · ESTE FICHERO ES LA FUENTE DEL COPY, NO UNA COPIA DE LA SPA.
// Nació como copy VERBATIM de src/pages/KitGestionPersonal.tsx y de
// src/components/kit-gestion-personal/*, y hasta la v2.0 lo fue. Desde la v2.0
// (2026-08-24) el copy se corrige AQUÍ y se PORTA a la SPA en el mismo commit
// —las tres afirmaciones legales falsas del hero, la FAQ y el JSON-LD de la
// SPA sobrevivieron una versión entera justamente por describir la relación al
// revés—. Si vuelven a divergir, la referencia es este fichero. Los gemelos:
//   · src/pages/KitGestionPersonal.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/kit-gestion-personal/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-gestion-personal.ts (8 testimonios)
//   · src/components/shared/CompatibleAppsMarquee.tsx (variant="tareas" → título/subtítulo)
//   · src/pages/ProductosDigitales.tsx y astro-site/.../ProductosDigitalesHubPage.astro (tarjeta del hub)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_GESTION_PERSONAL (resuelto en el wrapper .astro).
//
// Divergencias vs. el producto de referencia (kit-escandallos), todas cubiertas por las props
// opcionales documentadas en types.ts:
//   1. Hero H1 Forma B (titleSubtitle en bloque, SIN titlePost inline).
//   2. grid.fourCols = false/omitido (9 plantillas, md:grid-cols-3 — NO 4 columnas).
//   stickyVariant: se omite (default 'v2', que es el que usa este producto).
//   images.gridGallery: se omite — el ContentGrid de la SPA usa EXACTAMENTE el mismo set y
//   orden de 6 imágenes que el hero (no diverge como en escandallos).
// Retiradas en la v2.0: `hero.badgeTone = 'red'` (RC-13: el badge ya no amenaza),
// `guarantee.headingPre` sin tildes (RC-14) y la nota de `authorBadges` «SIN tildes»,
// que además se contradecía a sí misma citando dos badges QUE SÍ LAS LLEVAN.
// Requirió añadir 3 iconos nuevos a Icon.astro (Euro, UserPlus, Palmtree), extraídos EXACTOS
// de node_modules/lucide-react v0.462.0 (Palmtree es alias de TreePalm → kebab "tree-palm").
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'kit-gestion-personal',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GESTION_PERSONAL',

  seo: {
    title: 'Kit Gestión de Personal y Turnos — Plantillas Excel para Hostelería | AI Chef Pro',
    description:
      '9 plantillas Excel con fórmulas automáticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluación de equipo en hostelería. Solo 14 EUR.',
    keywords:
      'gestión personal restaurante, cuadrante turnos hostelería, control horario restaurante, coste laboral hostelería, plantilla turnos excel, onboarding empleado restaurante, evaluación desempeño hostelería, vacaciones restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-gestion-personal.jpg',
  },

  schema: {
    productName: 'Kit Gestión de Personal y Turnos — Plantillas Excel para Hostelería',
    productDescription:
      '9 plantillas Excel con fórmulas automáticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluación de equipo en hostelería.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '8',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'David Ruiz',
        rating: '5',
        body: 'El cuadrante de turnos me ha cambiado la vida. Las alertas de 12 h de descanso entre jornadas y de las horas que tiene contratadas cada uno me avisan automáticamente.',
      },
      {
        author: 'Carmen Delgado',
        rating: '5',
        body: 'La plantilla de onboarding es brutal. El tiempo de incorporación bajó de 2 semanas a 4 días en todas las unidades.',
      },
      {
        author: 'Marta Jiménez',
        rating: '5',
        body: 'Lo recomiendo a todos mis clientes. Las plantillas cumplen con la normativa vigente: descansos, jornada máxima, vacaciones.',
      },
    ],
    // FAQPage schema (MÁS CORTAS que las FAQ on-page — VERBATIM del Helmet)
    faqs: [
      {
        q: '¿Incluye registro horario digital?',
        a: 'No. El registro de jornada es obligatorio en España desde 2019 (RD-ley 8/2019, art. 34.9 ET) y no tenerlo es infracción grave: de 751 a 7.500 EUR por centro de trabajo (art. 7.5 LISOS). Este kit es para planificación de turnos, control de costes laborales, onboarding y gestión de equipo.',
      },
      {
        q: '¿Las fórmulas calculan horas extra automáticamente?',
        a: 'Sí. La plantilla calcula automáticamente el coste de cada hora extra según el recargo de tu convenio colectivo, que ajustas en una celda editable.',
      },
      {
        q: '¿En qué se diferencia del software de RRHH?',
        a: 'El software de RRHH cobra entre 30 y 60 EUR/mes. Este kit cuesta 14 EUR, pago único, sin suscripción.',
      },
      {
        q: '¿Hay garantía de devolución?',
        a: '30 días de garantía completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit Gestión de Personal y Turnos',
  },

  images: {
    // hero bg (6) — el ContentGrid usa EXACTAMENTE el mismo set/orden → gridGallery se omite.
    gallery: [
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-hero.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-turnos.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-cocina.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-equipo.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-oficina.jpg',
      '/lovable-uploads/ai-gallery/tareas-gestion-personal-servicio.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/tareas-gestion-personal-oficina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/tareas-gestion-personal-turnos.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/tareas-gestion-personal-hero.jpg',
  },

  hero: {
    // RC-13 · el badge dejó de amenazar («multas hasta 10.000 EUR/empleado»,
    // que además era falso) y conservaba el tono ROJO diseñado para esa
    // amenaza: quedaba una píldora de alarma diciendo algo que no alarma. Y
    // pasaba de 67 a 110 caracteres arrastrando una promesa genérica que el
    // H1 y la descripción ya dicen. Se queda la cláusula que informa.
    badgeTone: 'gold',
    badge: 'Registro de jornada obligatorio en España desde 2019 — art. 34.9 ET',
    titlePre: 'Kit Gestión de ',
    titleGold: 'Personal y Turnos',
    // sin titlePost (Forma B: subtítulo en bloque, no inline)
    titleSubtitle: 'Planifica, Controla Costes Laborales y Gestiona tu Equipo',
    description:
      '9 plantillas Excel con fórmulas automáticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluación de tu equipo de hostelería. Planifica como un profesional.',
    checkItems: [
      'Cuadrante de turnos semanal y mensual con alertas de cumplimiento',
      'Control de horas extra con cálculo automático de coste',
      'Ratio de coste laboral con semáforo: verde, amarillo, rojo',
      'Onboarding completo: documentación, formación, equipamiento',
      'Vacaciones, evaluación de desempeño y directorio de plantilla',
    ],
    ctaLabel: 'COMPRAR AHORA — 14 EUR',
  },

  compatApps: {
    titleHtml: 'Imprime, Delega y <span class="text-[#FFD700]">Controla</span>',
    subtitleHtml:
      'Plantillas Excel optimizadas para imprimir en A4. Compatible con Excel, Google Sheets, LibreOffice y Numbers',
  },

  grid: {
    countGold: '9',
    headingRest: ' Plantillas de Gestión de Personal',
    subtitle:
      'Cada plantilla incluye fórmulas automáticas y está diseñada para la realidad de la hostelería. Solo ajusta a tu negocio y empieza a planificar.',
    // fourCols omitido (3-col, md:grid-cols-3 — igual que la SPA)
    templates: [
      { icon: 'CalendarDays', title: 'Cuadrante de Turnos', desc: 'Planificación semanal y mensual con las 4 alertas reales: descanso mínimo de 12h entre jornadas (art. 34.3 ET), descanso semanal, jornada diaria máxima y horas sobre lo contratado.' },
      { icon: 'Clock', title: 'Control de Horas Extra', desc: 'Registro de horas extra por empleado con cálculo automático de coste según el recargo de tu convenio (celda editable). Alerta al superar el tope legal de 80h/año.' },
      { icon: 'Euro', title: 'Coste Laboral Mensual', desc: 'Ratio coste laboral/ventas con semáforo por tipo de negocio (fast casual, casual, fine dining, catering...). Previsión de plantilla por servicio y comparativa mensual.' },
      { icon: 'UserPlus', title: 'Onboarding Nuevo Empleado', desc: '50 tareas organizadas en cinco bloques: documentación legal, formación APPCC, prevención de riesgos, uniforme, formación de puesto, sistemas y accesos. Cada una con su plazo en días desde el alta.' },
      { icon: 'Palmtree', title: 'Planificación Vacaciones', desc: 'Calendario anual por semanas con saldo real de vacaciones. Solicitudes, aprobaciones, cobertura mínima por puesto y aviso en temporada alta.' },
      { icon: 'Star', title: 'Evaluación de Desempeño', desc: '10 competencias clave para hostelería con scoring 1-5. Histórico trimestral, objetivos por periodo y plan de desarrollo individual.' },
      { icon: 'Users', title: 'Directorio de Plantilla', desc: 'Base de datos completa: datos personales, puesto, convenio aplicable, vencimiento de contrato, carnets (manipulador, PRL) y aviso de menores de edad.' },
      { icon: 'Megaphone', title: 'BONUS: Briefing Cambio de Turno', desc: 'Traspaso entre turnos: incidencias, reservas VIP, tareas pendientes, stock bajo, ausencias y cambios de personal, ARQUEO DE CAJA con lectura Z y descuadre, y TEMPERATURAS al relevo (APPCC) con mínimo y máximo por equipo.' },
      { icon: 'Calculator', title: 'BONUS: Calculadora Plantilla Óptima', desc: 'Calcula cuántos empleados necesitas según covers por servicio, ratio empleado/cubierto, días de apertura y picos de demanda.' },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas de RRHH. Son herramientas diseñadas por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      { icon: 'Utensils', title: 'Diseñadas para Hostelería', desc: 'No son plantillas de RRHH genéricas. Están pensadas para restaurantes, hoteles y catering: turnos partidos, servicios, cocina, sala, extras de fin de semana.' },
      { icon: 'Calculator', title: 'Fórmulas Reales', desc: 'Cálculo automático de coste laboral, horas extra según convenio, ratios covers/empleado y previsión de plantilla por servicio. No es teoría: son números.' },
      { icon: 'ShieldCheck', title: 'Cumplimiento Legal, con Cita Exacta', desc: 'El registro de jornada es obligatorio en España desde 2019 (RD-ley 8/2019, art. 34.9 ET). Estas plantillas aplican los artículos reales: descanso de 12h entre jornadas (art. 34.3 ET), descanso semanal (art. 37.1 ET) y el tope de 80h/año en horas extra (art. 35.2 ET).' },
      { icon: 'RefreshCw', title: 'Software de Gestión Cobra 30-60 EUR/mes. Esto es 14 EUR', desc: 'Las mismas herramientas de planificación que usan el software de RRHH premium, pero en Excel por un pago único. Sin suscripción.' },
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
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Especialista en gestión de equipos en restaurantes y hoteles, ha diseñado sistemas de planificación de personal para cientos de establecimientos.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 7 plantillas principales, recibes estos recursos adicionales — valorados en 18 EUR',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Cambio de Turno',
        value: '9 EUR',
        desc: 'La plantilla que garantiza que ningún turno empiece a ciegas. Incidencias, reservas VIP, tareas pendientes, stock bajo, ausencias de personal, arqueo de caja (fondo, efectivo contado y ventas del TPV) y temperaturas al relevo, que es el punto exacto en que el APPCC cambia de responsable.',
        image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-equipo.jpg',
      },
      {
        icon: 'Calculator',
        label: 'BONUS 2',
        title: 'Calculadora Plantilla Óptima',
        value: '9 EUR',
        desc: 'Calcula cuántos empleados necesitas según tus covers por servicio, días de apertura, ratio empleado/cubierto y picos de demanda. Deja de tener plantilla de más o de menos.',
        image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-oficina.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL KIT DE GESTIÓN — 14 EUR',
  },

  guarantee: {
    // RC-14 · la divergencia «sin tildes» se documentó cuando TODO el fichero
    // iba sin ellas. Con el resto ya acentuado, mantenerla era lo que
    // producía la incoherencia: «Garantia de Satisfaccion» encabezando un
    // párrafo que dice «gestión» y una cifra que dice «Días de garantía».
    headingPre: 'Garantía de Satisfacción ',
    text:
      'Si las plantillas no te ayudan a mejorar la gestión de personal de tu restaurante, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (más largas que schema.faqs)
  faqs: [
    {
      q: '¿Incluye registro horario digital?',
      a: 'No. El registro de jornada es obligatorio en España desde el 12-05-2019 (RD-ley 8/2019, art. 34.9 ET), y no tenerlo implantado es infracción grave: de 751 a 7.500 EUR por centro de trabajo (art. 7.5 LISOS). Este kit no es ese sistema de fichaje: es para PLANIFICACIÓN de turnos, control de costes laborales, onboarding y gestión de equipo. Es el complemento perfecto a cualquier software de registro de jornada.',
    },
    {
      q: '¿Las fórmulas calculan horas extra automáticamente?',
      a: 'Sí. La plantilla de control de horas extra calcula automáticamente el coste de cada hora extra según el recargo de tu convenio colectivo (una celda editable, 1,25x por defecto). Solo introduces las horas trabajadas y el sistema hace el resto.',
    },
    {
      q: '¿Sirve para cualquier tipo de restaurante?',
      a: 'Sí. Las plantillas están diseñadas para hostelería en general: restaurante casual, fine dining, fast casual, hotel, catering, cadenas. Los ratios y fórmulas se adaptan a cualquier formato.',
    },
    {
      q: '¿En qué se diferencia del software de RRHH?',
      a: 'El software de gestión de personal cobra entre 30 y 60 EUR/mes por establecimiento. Este kit cuesta 14 EUR, pago único, sin suscripción. Tienes las mismas herramientas de planificación en Excel, que puedes personalizar al 100%.',
    },
    {
      q: '¿Puedo usarlo en varios restaurantes?',
      a: 'Sí. La licencia es personal — puedes usar las plantillas en todos los establecimientos que gestiones. Ideal para grupos de restauración, multi-unidades y consultores.',
    },
    {
      q: '¿Hay garantía de devolución?',
      a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Improvisar la Gestión de Tu Equipo',
    subtitle:
      '9 plantillas profesionales para gestionar personal por menos de lo que cuesta una hora de consultoría laboral.',
    items: [
      'Cuadrante de turnos semanal y mensual con alertas legales',
      'Control de horas extra con cálculo automático de coste',
      'Ratio de coste laboral mensual con semáforo',
      'Onboarding nuevo empleado: 50 tareas con su plazo legal',
      'Planificación de vacaciones con cobertura mínima',
      'Evaluación de desempeño: 10 competencias, scoring 1-5',
      'Directorio de plantilla con vencimientos y carnets',
      'BONUS: Briefing Cambio de Turno (9 EUR)',
      'BONUS: Calculadora Plantilla Óptima (9 EUR)',
    ],
    ctaLabel: 'SÍ, QUIERO EL KIT DE GESTIÓN — 14 EUR',
  },

  testimonials: {
    subtitle:
      'Gerentes, directores de RRHH y propietarios que ya gestionan su equipo con estas plantillas',
    items: [
      { name: 'David Ruiz', role: 'Gerente, restaurante casual (45 cubiertos)', text: 'El cuadrante de turnos me ha cambiado la vida. Antes lo hacía a mano y siempre había errores con los descansos. Ahora las alertas de 12 h entre jornadas y de las horas que tiene contratadas cada uno me avisan automáticamente.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Carmen Delgado', role: 'Directora RRHH, grupo hostelero (6 restaurantes)', text: 'La plantilla de onboarding es brutal. 50 tareas organizadas: documentación, APPCC, PRL, formación, accesos. El tiempo de incorporación bajó de 2 semanas a 4 días en todas las unidades.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Francisco Torres', role: 'Propietario, 2 restaurantes en Madrid', text: 'Cierro el mes y en cinco minutos sé mi coste laboral: la cotización de empresa y el recargo de mi convenio están en celdas que edito yo, y el semáforo usa el umbral de MI tipo de negocio, no un 30 % genérico.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucía Navarro', role: 'Jefa de cocina, restaurante mediterráneo', text: 'El control de horas extra es justo lo que necesitaba. Calcula automáticamente el coste según nuestro convenio y me avisa cuando un cocinero está cerca del límite legal. Nos hemos ahorrado 3 sanciones.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Alberto Méndez', role: 'Director de operaciones, cadena de restaurantes', text: 'La planificación de vacaciones con cobertura mínima por puesto es genial. Ya no tenemos agosto con 3 cocineros cuando necesitamos 6. Planificamos desde enero con visión completa.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Marta Jiménez', role: 'Consultora laboral especializada en hostelería', text: 'Lo recomiendo a todos mis clientes. Las plantillas cumplen con la normativa vigente: descansos, jornada máxima, vacaciones. Es la mejor forma de prevenir sanciones de Inspección de Trabajo.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Sánchez', role: 'Chef ejecutivo, hotel 5* (120 empleados)', text: 'La evaluación de desempeño con 10 competencias y scoring 1-5 nos ha profesionalizado las revisiones trimestrales. El histórico permite ver la evolución real de cada miembro del equipo.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Enrique Vidal', role: 'Gerente, restaurante gastronómico (2 estrellas)', text: 'La calculadora de plantilla óptima fue reveladora. Con los cubiertos del día PICO nos dijo que ese servicio necesita 2 personas de refuerzo, y que no hacía falta subir la plantilla fija. El ratio cubiertos/empleado lo explica todo.', avatar: '/avatars/avatar-8.jpg' },
    ],
  },

  pricing: {
    priceOld: '49 EUR',
    price: '14 EUR',
    discountBadge: '-71%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 71% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: 'Ahorra 35 EUR HOY',
  },

  stickyLabel: 'KIT GESTIÓN PERSONAL — 14 EUR',
  // stickyVariant omitido (default 'v2' — coincide con la SPA)

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: '/manual-manager-restaurante', label: 'Manual del Manager de Restaurante' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'kit-gestion-personal',
    label: '¿Ya compraste el Kit de Gestión de Personal? Vuelve a entrar al dashboard',
  },
};

export default data;
