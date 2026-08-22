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
    title: 'Pack Plantillas APPCC — 19 Registros de Seguridad Alimentaria | AI Chef Pro',
    description:
      '19 plantillas APPCC profesionales para restaurantes: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP. Obligatorio por ley. Solo €14.',
    keywords:
      'plantillas APPCC restaurante, registros APPCC hostelería, control temperaturas restaurante, carta alergenos obligatoria, registro limpieza restaurante, inspección sanidad restaurante, HACCP hostelería, trazabilidad restaurante, control plagas restaurante, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-pack-appcc.jpg',
  },

  schema: {
    productName: 'Pack de Plantillas APPCC — 19 Registros de Seguridad Alimentaria',
    productDescription:
      '19 plantillas profesionales de seguridad alimentaria para hostelería: registros de temperatura, limpieza, trazabilidad, alérgenos, HACCP, control de plagas. Obligatorio por ley en España.',
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
        a: 'No. Los planes, el análisis de peligros y las fichas vienen desarrollados; los registros traen 2-3 filas de ejemplo marcadas «(ejemplo)» que te enseñan cómo se rellenan y que borras antes de usarlos.',
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
    badge: 'Obligatorio por ley — las infracciones graves se sancionan con 5.001 a 20.000 € (Ley 17/2011)',
    titlePre: 'Pack de Plantillas ',
    titleGold: 'APPCC',
    // Forma B: subtítulo en bloque, SIN titlePost
    titleSubtitle: 'Pasa la Inspección de Sanidad con Nota',
    description:
      '19 registros profesionales de seguridad alimentaria + 2 bonus: temperatura, cocción, enfriamiento, anisakis, limpieza, trazabilidad, alérgenos, HACCP y más. Todo lo que exige la normativa APPCC, listo para usar en tu restaurante.',
    checkItems: [
      '19 registros con alertas automáticas con semáforo en los registros de medición; planes, checklists y carteles listos para imprimir',
      'Matriz de alérgenos con los 14 obligatorios',
      'Análisis de Peligros HACCP pre-rellenado',
      'Guía de los 25 puntos que revisa el inspector',
      'Registros de temperatura con alertas OK/ALERTA',
    ],
    ctaLabel: 'COMPRAR AHORA — €14',
  },

  compatApps: {
    titleHtml: 'Compatible con <span class="text-[#FFD700]">Excel</span>, Google Sheets y LibreOffice',
    subtitleHtml:
      'Descarga, personaliza e imprime. Compatible con Excel, Google Sheets, LibreOffice y Apple Numbers: los 21 ficheros son .xlsx y salen listos para imprimir en A4 desde la propia hoja',
  },

  grid: {
    countGold: '19',
    headingRest: ' Plantillas de Seguridad Alimentaria',
    subtitle:
      'Los 12 registros de medición traen Estado calculado y semáforo automático; los planes, checklists y carteles llegan desarrollados y listos para imprimir en A4.',
    // fourCols omitido → 10 tarjetas (grid-cols-2 md:grid-cols-3), paridad SPA.
    // La décima (COM-R2-09) nombra los 4 registros nuevos: eran el único motivo
    // por el que la cifra sube de 17 a 19 y no aparecían en NINGÚN punto de la
    // página de venta — sólo en el dashboard, es decir, después de pagar.
    templates: [
      { icon: 'Thermometer', title: 'Control de Temperaturas', desc: '2 plantillas: registro diario (cámaras, congeladores, exposición) con alertas automáticas OK/ALERTA + control en recepción de mercancías con límites por tipo de producto. Las celdas cambian cuando la temperatura sale del rango legal.' },
      { icon: 'SprayCan', title: 'Limpieza y Desinfección', desc: 'Plan maestro L+D con 32 zonas pre-rellenadas (cocina, sala, baños, almacén, vestuarios y exterior: terraza, contenedores y cámara de residuos) + registro diario por turno con checklist imprimible. Define qué se limpia, cuándo, cómo, con qué producto y quién lo hace.' },
      { icon: 'Truck', title: 'Recepción y Trazabilidad', desc: 'Checklist de recepción con verificación de temperatura, caducidad, etiquetado y estado del envase + registro de trazabilidad completo con lote, proveedor y destino, más la pestaña de salida y uso interno. Responde de inmediato a la autoridad: de qué proveedor vino cada lote y en qué elaboración y servicio acabó.' },
      { icon: 'AlertTriangle', title: 'Alérgenos', desc: 'Matriz de los 14 alérgenos obligatorios × todos los platos de tu carta con desplegables S/T/N (contiene, trazas, no contiene) + fichas imprimibles de cada alérgeno para cocina y sala. Cumple el Reglamento UE 1169/2011.' },
      { icon: 'Droplets', title: 'Aceite y Agua', desc: 'Control de aceite de fritura con test de compuestos polares y alertas (OK/VIGILAR/CAMBIAR) + registro de agua potable con niveles de cloro. Cumple la Orden de 26 de enero de 1989 y el RD 3/2023.' },
      { icon: 'ClipboardCheck', title: 'HACCP y Acciones Correctivas', desc: 'Análisis de peligros completo pre-rellenado con 21 peligros tipo en 7 fases del proceso (recepción → servicio), cada uno con su registro del pack detrás + registro de acciones correctivas con causa, medida y verificación.' },
      { icon: 'Bug', title: 'Control de Plagas', desc: 'Registro de actuaciones DDD (desinsectación, desratización, desinfección) con tipo, empresa, productos, zonas y certificados. Calendario de revisiones y espacio para plano de cebos.' },
      { icon: 'ShieldCheck', title: 'Guía de Inspección', desc: 'Los 25 puntos que revisa el inspector de Sanidad con nivel de gravedad (Leve / Grave / Muy grave, Ley 17/2011). Autoevalúa tu establecimiento antes de la inspección. Incluye resumen automático de cumplimiento.' },
      { icon: 'GraduationCap', title: 'Higiene y Formación', desc: 'Checklist de higiene personal imprimible para vestuario + registro de formación del personal en seguridad alimentaria. Normas de indumentaria, lavado de manos, conducta y certificaciones.' },
      { icon: 'Flame', title: 'Cocción, Enfriamiento y Anisakis', desc: '4 registros nuevos que cierran los PCC que el análisis de peligros ya citaba y no tenían ficha detrás: temperatura en el centro del producto (≥75 °C y, en regeneración, en menos de una hora), enfriamiento de 60 a 10 °C en 2 horas, congelación preventiva de anisakis (−20 °C durante 24 h o −35 °C durante 15 h) y verificación mensual de termómetros y sondas.' },
    ],
  },

  why: {
    headingPre: '¿Por Qué Este ',
    headingGold: 'Pack',
    headingPost: '?',
    subtitle:
      'No son plantillas genéricas. Son registros diseñados por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.',
    reasons: [
      { icon: 'ShieldAlert', title: 'Obligatorio por Ley', desc: 'El sistema APPCC es obligatorio para todos los establecimientos de hostelería en España. Sin estos registros, te expones a sanciones de 5.001 a 20.000 € en las graves y hasta 600.000 € en las muy graves (Ley 17/2011).' },
      { icon: 'ClipboardCheck', title: 'Listo para Usar', desc: 'No empieces de cero. Los planes, el análisis de peligros, las fichas de alérgenos y la guía de inspección llegan desarrollados y listos para adaptar (32 zonas de limpieza, 21 peligros HACCP, límites de temperatura por familia, los 14 alérgenos); los registros traen 2-3 filas de ejemplo marcadas «(ejemplo)» que enseñan cómo se rellenan y se borran en un segundo.' },
      { icon: 'Calculator', title: 'Fórmulas y Alertas Automáticas', desc: 'Las plantillas de temperatura cambian automáticamente entre OK y ALERTA. El control de aceite marca VIGILAR a partir del 20 % de compuestos polares y CAMBIAR al llegar al 25 % —el límite legal— o si la fritura ha pasado de 180 °C.' },
      { icon: 'RefreshCw', title: 'Paga Una Vez, Tuyo Para Siempre', desc: 'Sin suscripciones. Acceso permanente al dashboard con todas las plantillas. Actualizaciones incluidas si cambia la normativa.' },
    ],
    compatLabel: 'Compatible con cualquier software de hojas de cálculo:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Google Sheets' },
      { label: 'LibreOffice' },
      { label: 'Listo para imprimir en A4' },
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
      'Además de las 19 plantillas, recibirás estos recursos adicionales — valorados en €16',
    items: [
      {
        icon: 'GraduationCap',
        label: 'BONUS 1',
        title: 'Registro de Formación en Seguridad Alimentaria',
        value: '€9',
        desc: 'Plantilla para registrar toda la formación de tu equipo: manipulador de alimentos, APPCC, alérgenos, primeros auxilios. El inspector puede pedirlo en cualquier momento.',
        image: '/lovable-uploads/ai-gallery/appcc-registro-plantilla.jpeg',
      },
      {
        icon: 'AlertTriangle',
        label: 'BONUS 2',
        title: 'Protocolo de Actuación ante Alerta Alimentaria',
        value: '€7',
        desc: 'Cartel imprimible con los 7 pasos a seguir ante una alerta alimentaria + teléfonos de emergencia. Identificar → Aislar → Notificar → Documentar → Comunicar → Verificar → Registrar.',
        image: '/lovable-uploads/ai-gallery/appcc-inspector-sanidad.jpeg',
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
      a: 'No. Los planes, el análisis de peligros, las fichas de alérgenos y la guía de inspección vienen completos; los registros traen 2-3 filas de ejemplo marcadas «(ejemplo)» para que veas cómo se rellenan y las borres antes de empezar. Solo tienes que personalizar con los datos de tu establecimiento: los platos de tu carta para la matriz de alérgenos, tus equipos de frío, tus zonas de limpieza. El Estado y el semáforo de los registros de medición se calculan solos.',
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
      '19 plantillas profesionales por menos de lo que cuesta una consulta con un asesor de seguridad alimentaria.',
    items: [
      '12 registros Excel con Estado calculado y semáforo automático + 9 planes, checklists y carteles listos para imprimir',
      'Matriz de los 14 alérgenos obligatorios',
      'Análisis de Peligros HACCP pre-rellenado con 21 peligros',
      'Plan de Limpieza completo con 32 zonas, dentro y fuera',
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
      { name: 'Ana Belén Torres', role: 'Propietaria, Cafetería El Trigal', text: 'La matriz de alérgenos me salvó. Tenía una clienta celíaca y no tenía los alérgenos documentados correctamente. Ahora cada plato de la carta tiene su ficha con los 14 alérgenos marcados.', avatar: '/avatars/avatar-6.jpg' },
      { name: 'Roberto Salazar', role: 'Propietario, Trattoria Don Roberto', text: 'Me llegó una inspección sorpresa y gracias al pack tenía todos los registros de los últimos 6 meses impecables. El inspector me dijo que me había ahorrado un buen susto.', avatar: '/avatars/avatar-7.jpg' },
      { name: 'Miguel Ángel Prieto', role: 'Jefe de Cocina, Hotel Montaña', text: 'Llevo 20 años en cocina y siempre usé libretas para apuntar temperaturas. Pasar al Excel con alertas automáticas fue un antes y un después. Si la temperatura sube, lo veo en rojo al instante.', avatar: '/avatars/avatar-8.jpg' },
      { name: 'Daniel Ortega', role: 'Consultor Gastronómico', text: 'Recomiendo este pack a todos mis clientes sin excepción. Es la forma más rápida de poner en orden la seguridad alimentaria de cualquier establecimiento. Se lo he recomendado a más de 40 negocios.', avatar: '/avatars/chef-avatar-5.jpg' },
      { name: 'Ignacio Vargas', role: 'Director de Compras, Hotel Costa Sereno', text: 'Los registros de temperatura en recepción de mercancías nos permiten rechazar producto fuera de rango con datos reales. Desde que lo usamos, las incidencias con proveedores han bajado mucho.', avatar: '/avatars/avatar-1.jpg' },
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
  updateNote: 'Producto actualizado · Versión 2.0 · agosto 2026',

  alreadyBought: {
    product: 'pack-appcc',
    label: '¿Ya compraste el Pack APPCC? Vuelve a entrar al dashboard',
  },
};

export default data;
