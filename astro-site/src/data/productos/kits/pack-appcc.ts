// astro-site/src/data/productos/kits/pack-appcc.ts
// LÍNEA KITS EXCEL — producto pack-appcc. Copy VERBATIM de la SPA:
//   · src/pages/PackAppcc.tsx (Helmet: SEO + 3 JSON-LD, orden de secciones, footer, AlreadyBought)
//   · src/components/pack-appcc/*  (Hero, ContentGrid, WhySection, AuthorSection,
//     BonusSection, BuyBox, GuaranteeSection, FaqAccordion, CtaFinal, StickyBar)
//   · src/data/testimonials-appcc.ts (10 testimonios)
// DINERO: stripeEnvKey = VITE_STRIPE_PAYMENT_LINK_APPCC (resuelto en el wrapper .astro).
//
// Divergencias DOM vs kit-escandallos (todas cubiertas por props opcionales de types.ts):
//   · hero.badgeTone = 'gold' (igual que escandallos)
//   · hero H1 = Forma B (titleSubtitle en <span block>, SIN titlePost)
//   · grid.fourCols = false/omitido (9 tarjetas, md:grid-cols-3) — SPA usa grid-cols-2 md:grid-cols-3 (9)
//   · guarantee.headingPre = default acentuado "Garantía de Satisfacción " (SPA lo usa igual)
//   · stickyVariant = 'v2' (default; SPA usa px-3 max-w-screen-sm, CTA "COMPRAR")
//   · authorBadges = default acentuado ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'] (SPA idéntico)
import type { KitExcelData } from './types';

const data: KitExcelData = {
  slug: 'pack-appcc',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_APPCC',

  seo: {
    title: 'Pack Plantillas APPCC — 17 Registros de Seguridad Alimentaria | AI Chef Pro',
    description:
      '17 plantillas APPCC profesionales para restaurantes: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP. Obligatorio por ley. Solo €14.',
    keywords:
      'plantillas APPCC restaurante, registros APPCC hostelería, control temperaturas restaurante, carta alergenos obligatoria, registro limpieza restaurante, inspección sanidad restaurante, HACCP hostelería, trazabilidad restaurante, control plagas restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-pack-appcc.jpg',
  },

  schema: {
    productName: 'Pack de Plantillas APPCC — 17 Registros de Seguridad Alimentaria',
    productDescription:
      '17 plantillas profesionales de seguridad alimentaria para hostelería: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP, control de plagas. Obligatorio por ley en España.',
    price: '14.00',
    priceValidUntil: '2026-12-31',
    aggregateRating: {
      ratingValue: '4.9',
      reviewCount: '10',
      bestRating: '5',
      worstRating: '1',
    },
    reviews: [
      {
        author: 'Carlos Moreno',
        rating: '5',
        body: 'Pasamos la inspección de Sanidad sin una sola incidencia. Las plantillas cubren todo lo que pide el inspector.',
      },
      {
        author: 'Laura García',
        rating: '5',
        body: 'Gestiono 3 hoteles y estas plantillas me permiten estandarizar los registros APPCC en todos. Imprescindible.',
      },
      {
        author: 'Miguel Torres',
        rating: '5',
        body: 'Antes usaba hojas fotocopiadas de hace 10 años. Ahora tengo registros profesionales con alertas automáticas.',
      },
    ],
    // FAQPage schema (MÁS CORTAS que las FAQ on-page — VERBATIM del Helmet)
    faqs: [
      {
        q: '¿Necesito conocimientos técnicos para usar las plantillas?',
        a: 'No. Todo viene pre-rellenado con datos reales de hostelería. Solo tienes que personalizar con los datos de tu establecimiento.',
      },
      {
        q: '¿Estas plantillas sirven para pasar la inspección de Sanidad?',
        a: 'Sí. Cubren todos los registros que exige la normativa APPCC en España: temperaturas, limpieza, trazabilidad, alérgenos, HACCP, control de plagas, aceite y agua.',
      },
      {
        q: '¿Funcionan con Google Sheets?',
        a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers.',
      },
      {
        q: '¿Puedo personalizar las plantillas para mi restaurante?',
        a: 'Totalmente. Puedes añadir zonas de limpieza, equipos de frío, platos a la matriz de alérgenos, peligros al análisis HACCP. Las celdas editables están marcadas en verde.',
      },
      {
        q: '¿Incluye actualizaciones si cambia la normativa?',
        a: 'Sí. Tienes acceso de por vida al dashboard online. Si hay cambios en la normativa APPCC, actualizaremos las plantillas sin coste adicional.',
      },
      {
        q: '¿Para qué tipo de establecimiento sirven?',
        a: 'Para cualquier negocio de hostelería: restaurantes, bares, cafeterías, hoteles, catering, obradores, food trucks, comedores colectivos.',
      },
    ],
    breadcrumbName: 'Pack Plantillas APPCC',
  },

  images: {
    // hero bg (6) — idéntico al strip del ContentGrid en esta SPA (mismo array reusado, sin gridGallery)
    gallery: [
      '/lovable-uploads/ai-gallery/appcc-control-temperaturas.jpeg',
      '/lovable-uploads/ai-gallery/appcc-limpieza-cocina.jpeg',
      '/lovable-uploads/ai-gallery/appcc-recepcion-mercancias.jpeg',
      '/lovable-uploads/ai-gallery/appcc-alergenos-carta.jpeg',
      '/lovable-uploads/ai-gallery/appcc-inspector-sanidad.jpeg',
      '/lovable-uploads/ai-gallery/appcc-registro-plantilla.jpeg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg',
    buyBoxBg: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg',
    ctaBg: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg',
  },

  hero: {
    badgeTone: 'gold',
    badge: 'Obligatorio por ley — evita sanciones de hasta €60.000',
    titlePre: 'Pack de Plantillas ',
    titleGold: 'APPCC',
    // Forma B: subtítulo en bloque, SIN titlePost
    titleSubtitle: 'Pasa la Inspección de Sanidad con Nota',
    description:
      '17 plantillas profesionales de seguridad alimentaria: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP y más. Todo lo que exige la normativa APPCC, listo para usar en tu restaurante.',
    checkItems: [
      '17 plantillas con fórmulas y alertas automáticas',
      'Matriz de alérgenos con los 14 obligatorios',
      'Análisis de Peligros HACCP pre-rellenado',
      'Guía de los 25 puntos que revisa el inspector',
      'Registros de temperatura con alertas OK/ALERTA',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  compatApps: {
    titleHtml: 'Compatible con <span class="text-[#FFD700]">Excel</span>, Google Sheets y PDF Imprimible',
    subtitleHtml:
      'Descarga, personaliza e imprime. Compatible con Excel, Google Sheets, LibreOffice y Apple Numbers',
  },

  grid: {
    countGold: '17',
    headingRest: ' Plantillas de Seguridad Alimentaria',
    subtitle:
      'Cada plantilla incluye fórmulas automáticas, alertas visuales, datos pre-rellenados y formato listo para imprimir.',
    // fourCols omitido → 9 tarjetas (grid-cols-2 md:grid-cols-3), paridad SPA
    templates: [
      { icon: 'Thermometer', title: 'Control de Temperaturas', desc: '2 plantillas: registro diario (cámaras, congeladores, exposición) con alertas automáticas OK/ALERTA + control en recepción de mercancías con límites por tipo de producto. Las celdas cambian cuando la temperatura sale del rango legal.' },
      { icon: 'SprayCan', title: 'Limpieza y Desinfección', desc: 'Plan maestro L+D con 25+ zonas pre-rellenadas (cocina, sala, baños, almacén) + registro diario por turno con checklist imprimible. Define qué se limpia, cuándo, cómo, con qué producto y quién lo hace.' },
      { icon: 'Truck', title: 'Recepción y Trazabilidad', desc: 'Checklist de recepción con verificación de temperatura, caducidad, etiquetado y estado del envase + registro de trazabilidad completo con lote, proveedor y destino. Localiza cualquier producto en menos de 4 horas.' },
      { icon: 'AlertTriangle', title: 'Alérgenos', desc: 'Matriz de los 14 alérgenos obligatorios × todos los platos de tu carta con desplegables S/T/N (contiene, trazas, no contiene) + fichas imprimibles de cada alérgeno para cocina y sala. Cumple el Reglamento UE 1169/2011.' },
      { icon: 'Droplets', title: 'Aceite y Agua', desc: 'Control de aceite de fritura con test de compuestos polares y alertas (OK/VIGILAR/CAMBIAR) + registro de agua potable con niveles de cloro. Cumple RD 2207/1995 y RD 140/2003.' },
      { icon: 'ClipboardCheck', title: 'HACCP y Acciones Correctivas', desc: 'Análisis de peligros completo pre-rellenado con 13 peligros tipo en 6 fases del proceso (recepción → servicio) + registro de acciones correctivas con causa, medida y verificación.' },
      { icon: 'Bug', title: 'Control de Plagas', desc: 'Registro de actuaciones DDD (desinsectación, desratización, desinfección) con tipo, empresa, productos, zonas y certificados. Calendario de revisiones y espacio para plano de cebos.' },
      { icon: 'ShieldCheck', title: 'Guía de Inspección', desc: 'Los 25 puntos que revisa el inspector de Sanidad con nivel de gravedad (GRAVE/MODERADA/LEVE). Autoevalúa tu establecimiento antes de la inspección. Incluye resumen automático de cumplimiento.' },
      { icon: 'GraduationCap', title: 'Higiene y Formación', desc: 'Checklist de higiene personal imprimible para vestuario + registro de formación del personal en seguridad alimentaria. Normas de indumentaria, lavado de manos, conducta y certificaciones.' },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Pack',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son registros diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      { icon: 'ShieldAlert', title: 'Obligatorio por Ley', desc: 'El sistema APPCC es obligatorio para todos los establecimientos de hostelería en España. Sin estos registros, te expones a sanciones de hasta €60.000 y cierre cautelar.' },
      { icon: 'ClipboardCheck', title: 'Listo para Usar', desc: 'No empieces de cero. Cada plantilla viene pre-rellenada con datos reales de hostelería: zonas de limpieza, peligros HACCP, rangos de temperatura, los 14 alérgenos.' },
      { icon: 'Calculator', title: 'Fórmulas y Alertas Automáticas', desc: 'Las plantillas de temperatura cambian automáticamente entre OK y ALERTA. El control de aceite marca CAMBIAR cuando supera el 25% de compuestos polares.' },
      { icon: 'RefreshCw', title: 'Paga Una Vez, Tuyo Para Siempre', desc: 'Sin suscripciones. Acceso permanente al dashboard con todas las plantillas. Actualizaciones incluidas si cambia la normativa.' },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de cálculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'PDF imprimible' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha diseñado sistemas de seguridad alimentaria y control de costes para cientos de restaurantes.',
  authorBadges: ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años'],

  bonus: {
    headingPre: 'Bonos ',
    headingGold: 'Exclusivos',
    subtitle:
      'Además de las 17 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'GraduationCap',
        label: 'BONUS 1',
        title: 'Registro de Formación en Seguridad Alimentaria',
        value: '€9',
        desc: 'Plantilla para registrar toda la formación de tu equipo: manipulador de alimentos, APPCC, alérgenos, primeros auxilios. El inspector puede pedirlo en cualquier momento.',
        image: '/lovable-uploads/ai-gallery/focaccia-jardin-alta-hidratacion-aichefpro.jpeg',
      },
      {
        icon: 'AlertTriangle',
        label: 'BONUS 2',
        title: 'Protocolo de Actuación ante Alerta Alimentaria',
        value: '€7',
        desc: 'Cartel imprimible con los 7 pasos a seguir ante una alerta alimentaria + teléfonos de emergencia. Identificar → Aislar → Notificar → Documentar → Comunicar → Verificar → Registrar.',
        image: '/lovable-uploads/ai-gallery/hogaza-masa-madre-oreja-perfecta-aichefpro.jpeg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PACK APPCC — €14',
  },

  guarantee: {
    // headingPre por defecto = "Garantía de Satisfacción " (acentuado); pack-appcc usa el default.
    text:
      'Si las plantillas no te ayudan a pasar la inspección de Sanidad con más tranquilidad, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  // FAQ on-page (acordeón) — VERBATIM de FaqAccordion.tsx (más largas que schema.faqs)
  faqs: [
    {
      q: '¿Necesito conocimientos técnicos para usar las plantillas?',
      a: 'No. Todo viene pre-rellenado con datos reales de hostelería. Solo tienes que personalizar con los datos de tu establecimiento: nombre de los platos para la matriz de alérgenos, equipos de frío, zonas de limpieza. Las fórmulas y alertas funcionan automáticamente.',
    },
    {
      q: '¿Estas plantillas sirven para pasar la inspección de Sanidad?',
      a: 'Sí. Cubren todos los registros que exige la normativa APPCC en España: temperaturas, limpieza, trazabilidad, alérgenos, HACCP, control de plagas, aceite y agua. Están diseñadas para cumplir los requisitos del Real Decreto 1021/2022 y el Reglamento UE 1169/2011.',
    },
    {
      q: '¿Funcionan con Google Sheets?',
      a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers. Los documentos imprimibles están optimizados para formato A4.',
    },
    {
      q: '¿Puedo personalizar las plantillas para mi restaurante?',
      a: 'Totalmente. Puedes añadir zonas de limpieza, equipos de frío, platos a la matriz de alérgenos, peligros al análisis HACCP. Las celdas editables están marcadas en verde. Las fórmulas y alertas se adaptan automáticamente.',
    },
    {
      q: '¿Incluye actualizaciones si cambia la normativa?',
      a: 'Sí. Tienes acceso de por vida al dashboard online. Si hay cambios en la normativa APPCC, actualizaremos las plantillas y las tendrás disponibles sin coste adicional.',
    },
    {
      q: '¿Para qué tipo de establecimiento sirven?',
      a: 'Para cualquier negocio de hostelería: restaurantes, bares, cafeterías, hoteles, catering, obradores, food trucks, comedores colectivos. La normativa APPCC es obligatoria para todos.',
    },
  ],

  cta: {
    heading: 'No Esperes a que Venga el Inspector',
    subtitle:
      '17 plantillas profesionales por menos de lo que cuesta una consulta con un asesor de seguridad alimentaria.',
    items: [
      '17 plantillas Excel con fórmulas y alertas automáticas',
      'Matriz de los 14 alérgenos obligatorios',
      'Análisis de Peligros HACCP pre-rellenado con 13 peligros',
      'Plan de Limpieza completo con 25+ zonas',
      'Guía de los 25 puntos que revisa el inspector',
      'BONUS: Registro de Formación del Personal (€9)',
      'BONUS: Protocolo de Alerta Alimentaria (€7)',
      'Garantía de devolución 30 días',
    ],
    ctaLabel: 'SÍ, QUIERO EL PACK APPCC — €14',
  },

  testimonials: {
    subtitle:
      'Hosteleros que ya tienen sus registros APPCC al día con el Pack de Plantillas',
    items: [
      { name: 'Carlos Mendoza', role: 'Chef Ejecutivo, Restaurante Brasa Viva', text: 'Pasamos una inspección de Sanidad con nota gracias a estas plantillas. El inspector comentó que era uno de los registros más completos que había visto. Antes improvisaba con hojas sueltas.', avatar: '/avatars/chef-avatar-1.jpg' },
      { name: 'Laura Castillo', role: 'Directora de Operaciones, Grupo Hotelero Azul', text: 'Tenemos 6 hoteles y necesitábamos estandarizar el APPCC en todos. Con este pack, cada cocina sigue el mismo sistema. La auditoría interna se redujo de 3 días a medio día por centro.', avatar: '/avatars/avatar-2.jpg' },
      { name: 'Marcos Ibáñez', role: 'Dueño, Bar Txoko', text: 'La inspección de Sanidad me quitaba el sueño. Desde que uso las plantillas tengo todo al día: temperaturas, limpieza, trazabilidad. Ahora cuando viene el inspector, le abro la carpeta tranquilo.', avatar: '/avatars/avatar-3.jpg' },
      { name: 'Patricia Roldán', role: 'Consultora de Seguridad Alimentaria', text: 'Uso este pack con todos mis clientes de consultoría. Me ahorra horas de trabajo porque las plantillas ya tienen los campos correctos. Solo personalizo el nombre del establecimiento y listo.', avatar: '/avatars/avatar-4.jpg' },
      { name: 'Javier Esteban', role: 'Director, Catering Eventos del Sur', text: 'En catering, la documentación HACCP es obligatoria para cada evento. Con el registro de trazabilidad y las fichas de alérgenos, genero toda la documentación en 15 minutos por servicio.', avatar: '/avatars/avatar-5.jpg' },
      { name: 'Ana Belén Torres', role: 'Propietaria, Cafetería Miga', text: 'La matriz de alérgenos me salvó. Tenía una clienta celíaca y no tenía los alérgenos documentados correctamente. Ahora cada plato de la carta tiene su ficha con los 14 alérgenos marcados.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Salazar', role: 'Propietario, Trattoria Don Roberto', text: 'Me llegó una inspección sorpresa y gracias al pack tenía todos los registros de los últimos 6 meses impecables. El inspector me dijo que evité una sanción de más de €3.000.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Miguel Ángel Prieto', role: 'Jefe de Cocina, Hotel Montaña', text: 'Llevo 20 años en cocina y siempre usé libretas para apuntar temperaturas. Pasar al Excel con alertas automáticas fue un antes y un después. Si la temperatura sube, lo veo en rojo al instante.', avatar: '/avatars/avatar-8.jpg' },
      { name: 'Daniel Ortega', role: 'Consultor Gastronómico', text: 'Recomiendo este pack a todos mis clientes sin excepción. Es la forma más rápida de poner en orden la seguridad alimentaria de cualquier establecimiento. Se lo he recomendado a más de 40 negocios.', avatar: '/avatars/chef-avatar-5.jpg' },
      { name: 'Ignacio Vargas', role: 'Director de Compras, Hotel Gran Vía Palace', text: 'Los registros de temperatura en recepción de mercancías nos permiten rechazar producto fuera de rango con datos reales. Hemos reducido las incidencias con proveedores un 60% desde que lo usamos.', avatar: '/avatars/avatar-1.jpg' },
    ],
  },

  pricing: {
    priceOld: '€29',
    price: '€14',
    discountBadge: '-52%',
    heroNote: 'Precio especial de lanzamiento. Sube pronto',
    buyBoxNote: 'Precio especial de lanzamiento — 52% de descuento',
    bonusTotalLabel: 'Valor total del pack completo',
    bonusSaveLine: '¡Ahorra €15 HOY!',
  },

  stickyLabel: 'PACK APPCC — €14',
  // stickyVariant omitido → default 'v2' (paridad SPA: px-3 max-w-screen-sm, CTA "COMPRAR")

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos' },
    { href: '/pro-prompts-ebook', label: 'Pro Prompts eBook' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto actualizado · Versión 1.1 · agosto 2026',

  alreadyBought: {
    product: 'pack-appcc',
    label: '¿Ya compraste el Pack APPCC? Vuelve a entrar al dashboard',
  },
};

export default data;
