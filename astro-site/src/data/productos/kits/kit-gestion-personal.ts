// astro-site/src/data/productos/kits/kit-gestion-personal.ts
// LÍNEA KITS EXCEL — producto kit-gestion-personal. Copy VERBATIM de la SPA:
//   · src/pages/KitGestionPersonal.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/kit-gestion-personal/*  (HeroSection, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-gestion-personal.ts (8 testimonios)
//   · src/components/shared/CompatibleAppsMarquee.tsx (variant="tareas" → título/subtítulo)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_GESTION_PERSONAL (resuelto en el wrapper .astro).
//
// Divergencias vs. el producto de referencia (kit-escandallos), todas cubiertas por las 5 props
// opcionales documentadas en types.ts:
//   1. Hero H1 Forma B (titleSubtitle en bloque, SIN titlePost inline).
//   2. hero.badgeTone = 'red'.
//   3. grid.fourCols = false/omitido (9 plantillas, md:grid-cols-3 — NO 4 columnas).
//   4. guarantee.headingPre SIN tildes ("Garantia de Satisfaccion ").
//   5. authorBadges SIN tildes (['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años']).
//   stickyVariant: se omite (default 'v2', que es el que usa este producto).
//   images.gridGallery: se omite — el ContentGrid de la SPA usa EXACTAMENTE el mismo set y
//   orden de 6 imágenes que el hero (no diverge como en escandallos).
// Requirió añadir 3 iconos nuevos a Icon.astro (Euro, UserPlus, Palmtree), extraídos EXACTOS
// de node_modules/lucide-react v0.462.0 (Palmtree es alias de TreePalm → kebab "tree-palm").
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'kit-gestion-personal',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GESTION_PERSONAL',

  seo: {
    title: 'Kit Gestion de Personal y Turnos — Plantillas Excel para Hosteleria | AI Chef Pro',
    description:
      '9 plantillas Excel con formulas automaticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluacion de equipo en hosteleria. Solo 14 EUR.',
    keywords:
      'gestion personal restaurante, cuadrante turnos hosteleria, control horario restaurante, coste laboral hosteleria, plantilla turnos excel, onboarding empleado restaurante, evaluacion desempeno hosteleria, vacaciones restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-kit-gestion-personal.jpg',
  },

  schema: {
    productName: 'Kit Gestion de Personal y Turnos — Plantillas Excel para Hosteleria',
    productDescription:
      '9 plantillas Excel con formulas automaticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluacion de equipo en hosteleria.',
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
        body: 'El cuadrante de turnos me ha cambiado la vida. Las alertas de 11h entre turnos y maximo 40h/semana me avisan automaticamente.',
      },
      {
        author: 'Carmen Delgado',
        rating: '5',
        body: 'La plantilla de onboarding es brutal. El tiempo de incorporacion bajo de 2 semanas a 4 dias en todas las unidades.',
      },
      {
        author: 'Marta Jimenez',
        rating: '5',
        body: 'Lo recomiendo a todos mis clientes. Las plantillas cumplen con la normativa vigente: descansos, jornada maxima, vacaciones.',
      },
    ],
    // FAQPage schema (MÁS CORTAS que las FAQ on-page — VERBATIM del Helmet)
    faqs: [
      {
        q: '¿Incluye registro horario digital?',
        a: 'No. El registro/fichaje horario digital requiere un software homologado. Este kit es para planificacion de turnos, control de costes laborales, onboarding y gestion de equipo.',
      },
      {
        q: '¿Las formulas calculan horas extra automaticamente?',
        a: 'Si. La plantilla calcula automaticamente el coste de cada hora extra segun el porcentaje de tu convenio colectivo.',
      },
      {
        q: '¿En que se diferencia del software de RRHH?',
        a: 'El software de RRHH cobra entre 30 y 60 EUR/mes. Este kit cuesta 14 EUR, pago unico, sin suscripcion.',
      },
      {
        q: '¿Hay garantia de devolucion?',
        a: '30 dias de garantia completa. 100% reembolso sin preguntas.',
      },
    ],
    breadcrumbName: 'Kit Gestion de Personal y Turnos',
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
    badgeTone: 'red',
    badge: 'Control horario obligatorio 2026 — multas hasta 10.000 EUR/empleado',
    titlePre: 'Kit Gestion de ',
    titleGold: 'Personal y Turnos',
    // sin titlePost (Forma B: subtítulo en bloque, no inline)
    titleSubtitle: 'Planifica, Controla Costes Laborales y Gestiona tu Equipo',
    description:
      '9 plantillas Excel con formulas automaticas para gestionar turnos, horas extra, coste laboral, onboarding, vacaciones y evaluacion de tu equipo de hosteleria. Planifica como un profesional.',
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
    headingRest: ' Plantillas de Gestion de Personal',
    subtitle:
      'Cada plantilla incluye formulas automaticas y esta disenada para la realidad de la hosteleria. Solo ajusta a tu negocio y empieza a planificar.',
    // fourCols omitido (3-col, md:grid-cols-3 — igual que la SPA)
    templates: [
      { icon: 'CalendarDays', title: 'Cuadrante de Turnos', desc: 'Planificacion semanal y mensual con alertas automaticas: descanso minimo 11h entre turnos, maximo 40h/semana, libranzas y rotacion de turnos.' },
      { icon: 'Clock', title: 'Control de Horas Extra', desc: 'Registro de horas extra por empleado con calculo automatico de coste segun convenio colectivo. Alertas cuando se superan limites legales.' },
      { icon: 'Euro', title: 'Coste Laboral Mensual', desc: 'Ratio coste laboral/ventas con semaforo (verde <30%, amarillo 30-35%, rojo >35%). Prevision por servicio y comparativa mensual.' },
      { icon: 'UserPlus', title: 'Onboarding Nuevo Empleado', desc: '40+ tareas organizadas: documentacion legal, formacion APPCC, prevencion riesgos, uniforme, formacion de puesto, sistemas y accesos.' },
      { icon: 'Palmtree', title: 'Planificacion Vacaciones', desc: 'Calendario anual de vacaciones por empleado. Solicitudes, aprobaciones, cobertura minima por puesto y periodos de maxima demanda.' },
      { icon: 'Star', title: 'Evaluacion de Desempeno', desc: '10 competencias clave para hosteleria con scoring 1-5. Historico trimestral, objetivos por periodo y plan de desarrollo individual.' },
      { icon: 'Users', title: 'Directorio de Plantilla', desc: 'Base de datos completa: datos personales, puesto, convenio, vencimiento contrato, carnets (manipulador, PRL), tallas de uniforme.' },
      { icon: 'Megaphone', title: 'BONUS: Briefing Cambio de Turno', desc: 'Plantilla de traspaso de informacion entre turnos: incidencias, reservas VIP, tareas pendientes, stock bajo, avisos de mantenimiento.' },
      { icon: 'Calculator', title: 'BONUS: Calculadora Plantilla Optima', desc: 'Calcula cuantos empleados necesitas segun covers por servicio, ratio empleado/cubierto, dias de apertura y picos de demanda.' },
    ],
  },

  why: {
    headingPre: '¿Por Que Este ',
    headingGold: 'Kit',
    headingPost: '?',
    subtitle:
      'No son plantillas genericas de RRHH. Son herramientas disenadas por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      { icon: 'Utensils', title: 'Disenadas para Hosteleria', desc: 'No son plantillas de RRHH genericas. Estan pensadas para restaurantes, hoteles y catering: turnos partidos, servicios, cocina, sala, extras de fin de semana.' },
      { icon: 'Calculator', title: 'Formulas Reales', desc: 'Calculo automatico de coste laboral, horas extra segun convenio, ratios covers/empleado y prevision de plantilla por servicio. No es teoria: son numeros.' },
      { icon: 'ShieldCheck', title: 'Cumplimiento Legal 2026', desc: 'El control horario digital es obligatorio en Espana desde 2026. Estas plantillas te ayudan a planificar turnos, descansos y vacaciones segun la normativa vigente.' },
      { icon: 'RefreshCw', title: 'Software de Gestión Cobra 40 EUR/mes. Esto es 14 EUR', desc: 'Las mismas herramientas de planificacion que usan el software de RRHH premium, pero en Excel por un pago unico. Sin suscripcion.' },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de calculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Imprimible A4' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Especialista en gestion de equipos en restaurantes y hoteles, ha disenado sistemas de planificacion de personal para cientos de establecimientos.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Ademas de las 7 plantillas principales, recibes estos recursos adicionales — valorados en 18 EUR',
    items: [
      {
        icon: 'Megaphone',
        label: 'BONUS 1',
        title: 'Briefing Cambio de Turno',
        value: '9 EUR',
        desc: 'La plantilla que garantiza que ningun turno empiece a ciegas. Incidencias, reservas VIP, tareas pendientes, stock bajo, avisos de mantenimiento y notas del turno saliente.',
        image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-equipo.jpg',
      },
      {
        icon: 'Calculator',
        label: 'BONUS 2',
        title: 'Calculadora Plantilla Optima',
        value: '9 EUR',
        desc: 'Calcula cuantos empleados necesitas segun tus covers por servicio, dias de apertura, ratio empleado/cubierto y picos de demanda. Deja de tener plantilla de mas o de menos.',
        image: '/lovable-uploads/ai-gallery/tareas-gestion-personal-oficina.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SI, QUIERO EL KIT DE GESTION — 14 EUR',
  },

  guarantee: {
    headingPre: 'Garantia de Satisfaccion ',
    text:
      'Si las plantillas no te ayudan a mejorar la gestion de personal de tu restaurante, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Dias de garantia' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incomodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (más largas que schema.faqs)
  faqs: [
    {
      q: '¿Incluye registro horario digital?',
      a: 'No. El registro/fichaje horario digital requiere un software homologado (obligatoria en Espana desde 2026). Este kit es para PLANIFICACION de turnos, control de costes laborales, onboarding y gestion de equipo. Es el complemento perfecto a cualquier software de fichaje.',
    },
    {
      q: '¿Las formulas calculan horas extra automaticamente?',
      a: 'Si. La plantilla de control de horas extra calcula automaticamente el coste de cada hora extra segun el porcentaje de tu convenio colectivo. Solo introduces las horas trabajadas y el sistema hace el resto.',
    },
    {
      q: '¿Sirve para cualquier tipo de restaurante?',
      a: 'Si. Las plantillas estan disenadas para hosteleria en general: restaurante casual, fine dining, fast casual, hotel, catering, cadenas. Los ratios y formulas se adaptan a cualquier formato.',
    },
    {
      q: '¿En que se diferencia del software de RRHH?',
      a: 'El software de gestion de personal cobra entre 30 y 60 EUR/mes por establecimiento. Este kit cuesta 14 EUR, pago unico, sin suscripcion. Tienes las mismas herramientas de planificacion en Excel, que puedes personalizar al 100%.',
    },
    {
      q: '¿Puedo usarlo en varios restaurantes?',
      a: 'Si. La licencia es personal — puedes usar las plantillas en todos los establecimientos que gestiones. Ideal para grupos de restauracion, multi-unidades y consultores.',
    },
    {
      q: '¿Hay garantia de devolucion?',
      a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
    },
  ],

  cta: {
    heading: 'Deja de Improvisar la Gestion de Tu Equipo',
    subtitle:
      '9 plantillas profesionales para gestionar personal por menos de lo que cuesta una hora de consultoria laboral.',
    items: [
      'Cuadrante de turnos semanal y mensual con alertas legales',
      'Control de horas extra con calculo automatico de coste',
      'Ratio de coste laboral mensual con semaforo',
      'Onboarding nuevo empleado: 40+ tareas',
      'Planificacion de vacaciones con cobertura minima',
      'Evaluacion de desempeno: 10 competencias, scoring 1-5',
      'Directorio de plantilla con vencimientos y carnets',
      'BONUS: Briefing Cambio de Turno (9 EUR)',
      'BONUS: Calculadora Plantilla Optima (9 EUR)',
    ],
    ctaLabel: 'SI, QUIERO EL KIT DE GESTION — 14 EUR',
  },

  testimonials: {
    subtitle:
      'Gerentes, directores de RRHH y propietarios que ya gestionan su equipo con estas plantillas',
    items: [
      { name: 'David Ruiz', role: 'Gerente, restaurante casual (45 cubiertos)', text: 'El cuadrante de turnos me ha cambiado la vida. Antes lo hacia a mano y siempre habia errores con los descansos. Ahora las alertas de 11h entre turnos y maximo 40h/semana me avisan automaticamente.', avatar: '/avatars/avatar-1.jpg' },
      { name: 'Carmen Delgado', role: 'Directora RRHH, grupo hostelero (6 restaurantes)', text: 'La plantilla de onboarding es brutal. 40+ tareas organizadas: documentacion, APPCC, PRL, formacion, accesos. El tiempo de incorporacion bajo de 2 semanas a 4 dias en todas las unidades.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Francisco Torres', role: 'Propietario, 2 restaurantes en Madrid', text: 'Por fin controlo el coste laboral en tiempo real. El semaforo verde/amarillo/rojo me dice al momento si estoy por encima del 30% sobre ventas. Antes me enteraba a final de mes.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Lucia Navarro', role: 'Jefa de cocina, restaurante mediterraneo', text: 'El control de horas extra es justo lo que necesitaba. Calcula automaticamente el coste segun nuestro convenio y me avisa cuando un cocinero esta cerca del limite legal. Nos hemos ahorrado 3 sanciones.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Alberto Mendez', role: 'Director de operaciones, cadena de restaurantes', text: 'La planificacion de vacaciones con cobertura minima por puesto es genial. Ya no tenemos agosto con 3 cocineros cuando necesitamos 6. Planificamos desde enero con vision completa.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Marta Jimenez', role: 'Consultora laboral especializada en hosteleria', text: 'Lo recomiendo a todos mis clientes. Las plantillas cumplen con la normativa vigente: descansos, jornada maxima, vacaciones. Es la mejor forma de prevenir sanciones de Inspeccion de Trabajo.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Sanchez', role: 'Chef ejecutivo, hotel 5* (120 empleados)', text: 'La evaluacion de desempeno con 10 competencias y scoring 1-5 nos ha profesionalizado las revisiones trimestrales. El historico permite ver la evolucion real de cada miembro del equipo.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Enrique Vidal', role: 'Gerente, restaurante gastronomico (2 estrellas)', text: 'La calculadora de plantilla optima fue reveladora. Descubrimos que necesitabamos 2 personas mas en servicio de viernes y sabado y una menos entre semana. El ratio covers/empleado lo explica todo.', avatar: '/avatars/avatar-8.jpg' },
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

  stickyLabel: 'KIT GESTION PERSONAL — 14 EUR',
  // stickyVariant omitido (default 'v2' — coincide con la SPA)

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas', label: 'Kit Tareas Restaurante' },
    { href: '/kit-escandallos', label: 'Kit Escandallos' },
    { href: '/pack-appcc', label: 'Pack APPCC' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  alreadyBought: {
    product: 'kit-gestion-personal',
    label: '¿Ya compraste el Kit de Gestion de Personal? Vuelve a entrar al dashboard',
  },
};

export default data;
