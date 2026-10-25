// astro-site/src/data/productos/planes/plan-negocio-heladeria.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (noviembre 2026), 35 €.
// Landing NATIVA (no hay página SPA de la que portar copy). Molde: plan-negocio-panaderia.ts.
// Fuentes: scripts/productos-digitales/plan-heladeria/{SPEC.md, F1-research-heladeria.md (§0, §1, §4, §5, §6),
//   cifras_caso_es.json, datos_checklist.py, tandas_docx.py (SECCIONES del Word)}.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo; mismas que guia-churreria-chocolateria.ts):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Heladería Artesanal», idéntico en el H1 (hero.titlePre +
//    hero.titleGold), en schema.productName, en el name.es de src/data/products-catalog.ts, en la tarjeta del hub
//    y en el breadcrumb.
//  · SIN `priceOld` ni `discountBadge`, SIN `aggregateRating`, SIN `reviews` y SIN `testimonials`: producto
//    recién nacido, sin una sola venta. OJO: PlanNegocioLandingPage.astro pinta marquee + avatares con 5 estrellas
//    cuando `data.testimonials` es un objeto (aunque `items` esté vacío), así que la clave se OMITE por completo.
//  · Nunca «verificado contra el BOE», «cumple la normativa» ni «quedarás legal»; ni promesas de rentabilidad;
//    ni «España 2026» como sello; ni «prueba gratis» (AI Chef Pro va «desde 10 €»); ni «validado».
//    Lo que la research marca 🟡 se dice como «consúltalo con tu gestoría / tu ayuntamiento / tu inspector».
//  · Sin siglas (IAE, RGSEAA, APPCC, ET…) en el hero ni en los titulares.
//  · Sin cifras movibles: nada de DSCR, payback, saldos ni holguras. Solo las CIFRAS de abajo.
//  · Declaración en negativo ARRIBA (grid.subtitle): no es un curso de heladería ni un recetario y no sustituye a
//    la gestoría, al proyecto técnico del local ni al inspector.
//  · Orden del proceso (SPEC D11): grasas, yemas y emulsionantes ANTES de pasteurizar. Aquí no se detalla; vive en
//    el Word y en el checklist.
//  · CRIPTO: nada que tocar. PlanNegocioLandingPage monta las puertas solas si cryptoEnabledFor('plan-negocio-heladeria').
//
// CIFRAS (cifras_caso_es.json → clave; redondeadas con «≈»; actualizar aquí si el Excel cambia):
//   · ≈ 117.000 € de inversión en partidas ........ INVERSION_PARTIDAS (117.150 €)
//   · ≈ 183.000 € de necesidad total de financiación (con fondo de maniobra e IVA de la inversión) ... NECESIDAD_CAJA (183.170 €)
//   · ≈ 143 clientes al día ........................ CLIENTES_DIA (143)
//   · ticket de 4,90 € sin IVA ..................... TICKET (4,90 €)
//   · 310 días de apertura ......................... DIAS_APERTURA (310)
//   · ≈ 217.000 € de ventas el año 1 ............... VENTAS_A1 (217.217 €)
//   · plantilla de seis puestos .................... PLANTILLA_PERSONAS (6)
//   · 81,6 % del helado en hogares entre abril y septiembre: MAPA, nota de 12-ago-2026 (research §0.6), no del JSON
//   Sin JSON: 9 hojas, 10 secciones del Word, 80 tareas en 6 fases, 19 partidas (SPEC D2/D8/D14/D15).
//
// IMÁGENES: la plantilla pinta todas con alt="" (decorativas). Los alts descriptivos viven aquí, como comentario:
//   hero ........ vitrina de helados artesanos y mostrador listo para abrir
//   obrador ..... obrador con mantecadora y pasteurizador en acero inoxidable
//   vitrina ..... vitrina de cubetas con sabores variados
//   cucurucho ... cucurucho de helado con bolas de dos sabores
//   tarrinas .... tarrinas de helado artesano listas para llevar
//   invierno .... heladería en invierno con chocolate caliente, gofres y tartas heladas
//   plan ........ plan de negocio y hojas de cálculo sobre el mostrador de una heladería
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 8 FAQ (research §6). Una sola fuente: el acordeón de la página y el FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Cuánto cuesta montar una heladería artesanal?',
    a: 'En el caso base del plan, ≈ 117.000 € de inversión en partidas (obra, instalación eléctrica, mantecadora, pasteurizador, abatidor, vitrina, mobiliario…) y ≈ 183.000 € de necesidad total de financiación al sumar el fondo de maniobra y el IVA de la inversión. Tu cifra cambiará con el local, con la obra que necesite el obrador y con si compras la maquinaria nueva o de ocasión. Por eso el Excel es editable: cambias las partidas y ves cuánto necesitas tú de verdad.',
  },
  {
    q: '¿Es rentable una heladería? ¿Cuánto gana un heladero?',
    a: 'No te prometemos rentabilidad, porque depende de tu local, de tu ciudad y de tu verano. Lo que sí hace el plan es enseñarte la cuenta con honestidad: un caso base de ≈ 143 clientes al día con un ticket de 4,90 € sin IVA, el sueldo del titular dentro de la plantilla, tres escenarios (el pesimista incluido) y la tesorería mes a mes. En este negocio el margen es estrecho y las cuentas se deciden en el invierno y en el primer verano; ese es justo el sitio donde el plan te pone los números delante.',
  },
  {
    q: '¿Qué permisos necesito para abrir una heladería?',
    a: 'El plan distingue dos epígrafes del IAE: el 644.4 (fabricar y vender helado en el propio local, que entra en la Ley 12/2012 con declaración responsable hasta 750 m²) y el 676 (consumo en el local, que va por el régimen municipal). La terraza va siempre aparte, con la autorización de ocupación de la vía pública, y el obrador se inscribe en el registro sanitario de tu comunidad autónoma. El checklist te lleva por todo ello tarea a tarea. Qué licencia concreta te pide tu ayuntamiento, consúltalo con tu gestoría o con el propio ayuntamiento antes de firmar el alquiler.',
  },
  {
    q: '¿Qué vendo en invierno? ¿Cierro?',
    a: 'En verano entra la mayor parte de las ventas del año. El caso base abre en marzo y sigue abierto en invierno diversificando (crepes y gofres, chocolate a la taza, tartas y turrón helado por encargo, ventas a otros negocios), con tres semanas de cierre en enero. Los gofres y las crepes dependen de poder sacar humos, así que la consulta urbanística va la primera del checklist; si no se puede, el invierno va de chocolate, tartas y turrón. La alternativa de cerrar de noviembre a febrero se razona en el Word, sin hoja propia; el invierno del caso abierto lo ves mes a mes en la tesorería.',
  },
  {
    q: '¿Puedo poner «artesanal» en el rótulo?',
    a: '«Artesano» como calificación oficial solo se puede usar con la que otorga tu comunidad autónoma, así que confírmalo con ella antes de imprimir el rótulo. La mención segura es «elaboración propia», siempre que el helado se haga de verdad en tu local o en sus sucursales. Las denominaciones del RD 618/1998 (helado crema, mantecado, sorbete…) también tienen requisitos de composición; el Word te las explica.',
  },
  {
    q: '¿Puedo vender helado a restaurantes?',
    a: 'Sí, con límites. El art. 3 del RD 1021/2022 permite suministrar a otros negocios si el suministro es marginal (lo que sirves a otros negocios no pasa del 25 % de lo que vendes en el año, o todo lo que vendes, al público incluido, no pasa de 500 kg a la semana), localizado (tu zona de salud o hasta 50 km entre comunidades) y restringido, con una declaración responsable y un registro de destinatarios, cantidades y fechas. El plan lo incluye como línea de venta y el checklist recoge el trámite. Si tu volumen se acerca a esos umbrales, habla antes con tu autoridad sanitaria.',
  },
  {
    q: '¿Qué IVA lleva el helado y qué convenio aplica?',
    a: 'El helado lleva el 10 % de IVA, y el caso del plan va entero al 10 %. En personal, el convenio es el de hostelería de tu provincia: el ALEH VI nombra expresamente a las heladerías en su art. 4, y la plantilla de temporada va como fijos discontinuos. Qué convenio provincial te toca exactamente, confírmalo con tu gestoría.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Heladería Artesanal» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, la «bola» es «bocha» en Argentina, el «cucurucho» es «cono» en México y Colombia, la «tarrina» es «pote» en Argentina y el «polo» es «paleta» en México (donde la heladería también es «paletería» o «nevería»). Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-heladeria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_HELADERIA',

  seo: {
    title: 'Plan de Negocio: Heladería Artesanal — Excel, Word y Checklist | AI Chef Pro',
    description:
      'Plan de negocio para montar una heladería artesanal: cuánto cuesta, cuándo abrir y cómo pasar el invierno. Plan financiero en Excel de 9 hojas, plan en Word de 10 secciones y checklist de apertura de 80 tareas. 35 €, pago único.',
    keywords:
      'plan de negocio heladería, cómo montar una heladería, cuánto cuesta montar una heladería, plan financiero heladería excel, abrir una heladería artesanal, checklist apertura heladería, AI Chef Pro',
    // No existe og-plan-negocio-heladeria.jpg: se usa la imagen del hero de la landing (ya en producción con el deploy).
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Heladería Artesanal',
    productDescription:
      'Plan de negocio para abrir una heladería artesanal con obrador propio y vitrina. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería de 12 meses empezando en marzo, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 80 tareas en 6 fases y la Guía de Equivalencias para Latinoamérica. Caso base de ≈ 117.000 € de inversión en partidas y ≈ 183.000 € de necesidad total de financiación, con ≈ 143 clientes al día y un ticket de 4,90 € sin IVA. No es un curso de heladería ni un recetario, y no promete rentabilidad.',
    price: '35.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Heladería Artesanal',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-cucurucho.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-tarrinas.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-invierno.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-heladeria-vitrina.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-cucurucho.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-invierno.jpg',
      '/lovable-uploads/ai-gallery/plan-heladeria-tarrinas.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-heladeria-obrador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-heladeria-cucurucho.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-heladeria-hero.jpg',
  },

  hero: {
    badge: 'Para abrir tu heladería con las cuentas claras',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Heladería Artesanal',
    titleSubtitle: 'Plan Financiero en Excel, Plan en Word y Checklist de Apertura',
    description:
      'El plan para montar una heladería artesanal con obrador y vitrina: cuánto cuesta, en qué mes abrir y cómo se aguanta el invierno. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones y checklist de apertura con 80 tareas, desde la consulta urbanística del local hasta la primera temporada.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula',
      'Inversión inicial por partidas (≈ 117.000 €) y necesidad total de financiación (≈ 183.000 €, con fondo de maniobra e IVA)',
      'Caso base de ≈ 143 clientes al día con un ticket de 4,90 € sin IVA, y la tesorería mes a mes con el invierno a la vista',
      'Plan de negocio en Word: 10 secciones para adaptar y presentar',
      'Checklist de apertura: 80 tareas en 6 fases',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      'Es el plan de un negocio de helado: sus números, sus trámites y su calendario. No es un curso de heladería ni un recetario, y no sustituye a tu gestoría, al proyecto técnico del local ni a tu inspector.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería de 12 meses, financiación e instrucciones. Fórmulas vivas: cambias el alquiler, los clientes al día o el ticket y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Las 19 partidas de una heladería con obrador: obra, instalación eléctrica, mantecadora, pasteurizador, abatidor, vitrina, mobiliario, formación e imprevistos. En el caso base, ≈ 117.000 € en partidas y ≈ 183.000 € de necesidad total de financiación al sumar el fondo de maniobra y el IVA de la inversión.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos clientes al día necesitas para cubrir costes, con un caso base de ≈ 143 clientes y un ticket de 4,90 € sin IVA durante 310 días de apertura, y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un verano frío y lluvioso.' },
      { icon: 'CalendarRange', title: 'Tesorería de 12 Meses, Empezando en Marzo', desc: 'El Mes 1 es marzo: abrir en temporada para llegar al primer invierno con la caja del verano. Ves mes a mes la rampa de apertura, el invierno con las ventas bajas y los fijos planos, y la liquidación del IVA.' },
      { icon: 'Users', title: 'Personal de Temporada', desc: 'Una plantilla de seis puestos con fijos discontinuos y convenio de hostelería provincial, y la comprobación de que las horas contratadas cubren el horario de apertura más la producción del obrador.' },
      { icon: 'Banknote', title: 'Plan de Financiación', desc: 'Origen de fondos (recursos propios y préstamo con carencia), comprobación de que lo aportado cubre lo que hace falta y cuadro de amortización del préstamo.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con el plan de invierno, la potencia eléctrica del local y el marketing de temporada.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución y fiscalidad; local y licencia (consulta urbanística, potencia, humos, terraza); obrador y sanidad; personal y control de higiene; marca y carta; apertura y temporada. Con responsable, plazo y nota en cada tarea.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de una heladería, con su estacionalidad, su frío y su normativa propia.',
    reasons: [
      { icon: 'IceCream', title: 'Pensado para el Helado y para tu Local', desc: 'Mantecadora, pasteurizador, abatidor y vitrina de cubetas, con la potencia eléctrica que necesitan: un local monofásico puede dejar de servirte antes de firmar. La consulta urbanística es la primera tarea del checklist.' },
      { icon: 'Snowflake', title: 'El Invierno, con Números', desc: 'El 81,6 % del helado que se consume en los hogares se toma entre abril y septiembre. Por eso el caso abre en marzo y no en otoño, y por eso tienes la tesorería mes a mes con el plan de invierno delante, y razonada en el Word la alternativa de cerrar.' },
      { icon: 'Scale', title: 'Lo que Casi Nadie Cuenta de la Norma', desc: 'El 644.4 frente al 676 y lo que cambia en la apertura. El RD 618/1998 vivo solo en las denominaciones (helado crema, mantecado con al menos un 4 % de yema, sorbete, 430 g por litro). El huevo y la pasteurización: 70 °C durante 2 segundos o un ovoproducto. Cada punto con su norma citada; lo que decide tu comunidad o tu ayuntamiento, te lo marcamos para que lo consultes.' },
      { icon: 'Store', title: 'Vender a Restaurantes y Contratar por Temporada', desc: 'Qué exige el art. 3 del RD 1021/2022 para suministrar helado a otros negocios (marginal, localizado y restringido) y por qué la plantilla de verano va como fijos discontinuos y no por obra o como eventuales.' },
    ],
    compatLabel: 'Compatible con cualquier software ofimático:',
    compatPills: [
      { label: 'Excel', highlight: true },
      { label: 'Word' },
      { label: 'Google Sheets' },
      { label: 'Google Docs' },
      { label: 'LibreOffice' },
      { label: 'Apple Numbers' },
    ],
  },

  authorBio:
    'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha acompañado a emprendedores y a empresas de hostelería en España, combinando experiencia operativa con análisis financiero para que cada decisión de inversión se tome con las cuentas delante.',
  // authorBadges omitido → default ['Consultor Gastronómico desde 2010', 'En cocina desde los 17 años']

  bonus: {
    subtitle:
      'Además del plan financiero, el plan en Word y el checklist de apertura, te llevas un extra — valorado en €15',
    items: [
      {
        icon: 'Globe',
        label: 'BONUS',
        title: 'Guía de Equivalencias para tu país',
        value: '€15',
        desc: 'Los términos de tu producto dichos país por país en 20 países, más una ficha de una página por país con impuestos, sanidad, normas laborales, licencias y unidades.',
        image: '/lovable-uploads/ai-gallery/es-guia-equivalencias.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO EL PLAN — €35',
  },

  guarantee: {
    text:
      'Si el plan de negocio no supera tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones.',
    stats: [
      { number: '30', label: 'Días de garantía' },
      { number: '100%', label: 'Reembolso garantizado' },
      { number: '0', label: 'Preguntas incómodas' },
    ],
  },

  faqs: FAQS,

  cta: {
    headingPre: 'Es Hora de Hacer Realidad tu ',
    headingGold: 'Heladería',
    subtitle:
      'Antes de firmar el alquiler y de comprar la mantecadora, ten las cuentas, los trámites y el calendario de tu heladería sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Inversión inicial por partidas: ≈ 117.000 €, y ≈ 183.000 € de necesidad total de financiación en el caso base',
      'Caso base de ≈ 143 clientes al día con un ticket de 4,90 € sin IVA',
      'Tesorería de 12 meses empezando en marzo, con el invierno a la vista',
      'Tres escenarios financieros (pesimista, realista y optimista)',
      'Checklist de apertura con 80 tareas en 6 fases',
      'Plan de negocio en Word con 10 secciones',
      'BONUS: Guía de Equivalencias para tu país (€15)',
    ],
    ctaLabel: 'SÍ, QUIERO EL PLAN — €35',
  },

  pricing: {
    price: '€35',
    heroNote: 'Pago único. Acceso inmediato y actualizaciones incluidas',
    buyBoxNote: 'Pago único · Acceso inmediato · 30 días de garantía',
    bonusTotalLabel: 'El pack completo, en un solo pago',
  },

  stickyLabel: 'PLAN HELADERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-heladeria', label: 'Kit de Tareas Heladería' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/pack-appcc', label: 'Pack Plantillas APPCC' },
    { href: '/plan-negocio-panaderia', label: 'Plan Panadería' },
    { href: '/plan-negocio-cafeteria', label: 'Plan Cafetería' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · noviembre 2026',

  alreadyBought: {
    product: 'plan-negocio-heladeria',
    label: '¿Ya compraste el Plan de Negocio: Heladería Artesanal? Vuelve a entrar al dashboard',
  },
};

export default data;
