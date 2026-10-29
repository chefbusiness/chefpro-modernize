// astro-site/src/data/productos/planes/plan-negocio-taqueria.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (noviembre 2026), 35 €.
// Landing NATIVA. Molde: plan-negocio-pizzeria.ts (sin testimonios, 35 €, local fijo).
// Fuentes: scripts/productos-digitales/plan-taqueria/{F1-camino.md (§4, §5), F1-research-taqueria.md (§0, §1, §4, §6, §8),
//   cifras_caso_es.json, F2-NOTAS.md}.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Taquería» (H1, schema.productName, catálogo, hub, breadcrumb).
//  · SIN año fijo en title/meta/H1 (AGENTS.md: si algún día lleva año, token {year}).
//  · SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials` (producto recién nacido; la clave
//    `testimonials` se OMITE por completo: la plantilla pinta marquee con 5 estrellas si es un objeto).
//  · Cifras de la landing: SOLO las MEDIDAS del caso (cifras_caso_es.json) y las estables (5 ficheros, 9 hojas, 10 secciones,
//    80 tareas). NADA de DSCR, payback, saldos de tesorería, importe del préstamo ni neto exacto.
//    Calculadora: siempre «estimación del kit, editable».
//  · LEGAL (R §1): IVA 10 % en sala; para llevar, alcohol y refrescos/aguas frescas azucaradas al 21 %; temperaturas = art. 30 del
//    RD 1086/2020 en la redacción del RD 1021/2022. Nada de «sin gluten» prometido.
//  · CRIPTO: nada que tocar (la plantilla monta las puertas si cryptoEnabledFor('plan-negocio-taqueria')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ taquería con el trompo al pastor girando y el mostrador preparado
//   trompo ...... trompo al pastor con la piña en la punta y el taquero cortando
//   tortilla .... tortillas de maíz en el comal
//   salsas ...... barra de salsas de la taquería
//   delivery .... bolsas de tacos listas para repartir
//   equipo ...... el equipo de la taquería en la línea de servicio
//   plan ........ plan de negocio y hojas de cálculo sobre el mostrador de la taquería
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 8 FAQ (research §6). Una sola fuente: el acordeón de la página y el FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Cuánto cuesta montar una taquería?',
    a: 'Depende del local, de la salida de humos y de la cocina, que son las partidas que más mueven la cuenta. En el caso del plan (un local alquilado de 80 m² con 32 plazas y 16 más de terraza) salen unos 100.000 € en partidas de obra y equipos, imprevistos incluidos, y unos 172.000 € de necesidad total de caja una vez sumados la fianza, la renta previa, el fondo de maniobra de tres meses y el IVA de la inversión. Son cifras de ejemplo: el Excel trae la inversión por partidas (obra, conducto de humos, campana, trompo, plancha, freidora, frío, mobiliario, TPV, marca, imprevistos…) todas editables para que pongas las tuyas y veas cuánto necesitas tú.',
  },
  {
    q: '¿Es rentable una taquería? ¿Cuánto gana el dueño?',
    a: 'No te prometemos rentabilidad: depende de tu local, de tu ticket y de lo que llenes cada día. Lo que sí hace el plan es enseñarte la cuenta con honestidad. En el caso medido por el Excel (77 comensales al día a 15,50 € de ticket sin IVA, 300 días al año, unos 358.000 € de ventas) el beneficio neto queda en torno al 9-10 % de las ventas, con la plantilla y tu propio sueldo ya dentro, y el equilibrio llega con unos 64 comensales al día. Tienes tres escenarios (el pesimista, con pérdidas, incluido) para ver qué pasa con un año flojo, y todo se recalcula cuando cambias el ticket, los comensales o el alquiler.',
  },
  {
    q: '¿Cuál es el margen de un taco?',
    a: 'Depende de lo que pagues por la carne, del gramaje y de lo que se te quede por el camino en el trompo. Con los supuestos del kit (una estimación, editable), el taco al pastor sale a unos 0,61 € de coste y a un food cost de alrededor del 22,5 % sobre el precio de venta del caso (3,00 € con IVA). La calculadora del trompo y escandallo te deja poner tus precios, tus gramos y tu merma y te da el food cost y el margen de cada taco y de cada orden, para que no fijes el precio a ojo.',
  },
  {
    q: '¿Cuántos tacos salen de un trompo?',
    a: 'No hay una cifra única: depende de los kilos del cono, de los gramos que sirvas por taco y, sobre todo, de la merma de cocción y del sobrante del cierre. Con los supuestos del kit (estimación editable: cono de 15 kg, 35 g servidos por taco y un rendimiento del 64,8 %) salen unos 278 tacos por cono. La hoja del trompo de la calculadora hace la cuenta con tus datos y te enseña a medir tu propio rendimiento, que es lo que de verdad te protege el margen. Y si quieres registrarlo cada día, el Kit de Tareas Recurrentes de la taquería trae la hoja para eso.',
  },
  {
    q: '¿Tortilla comprada o nixtamal propio?',
    a: 'Con el volumen de un local como el del caso, comprar la tortilla suele salir mejor que hacerla: el nixtamal propio pide molino, tortilladora y a alguien que se dedique a ello, y solo se paga a partir de un volumen alto. Con los supuestos del kit (estimación, editable) el equilibrio de la tortilla propia está en torno a las 700 tortillas al día. La hoja de la tortilla de la calculadora te deja comparar las dos opciones con tus precios y tu volumen, y el Word explica cuándo tiene sentido dar el salto al nixtamal como decisión de producto y no solo de ahorro.',
  },
  {
    q: '¿Qué licencias necesito y qué pasa con la salida de humos y el gas?',
    a: 'La taquería tributa por el IAE en el grupo 671 (restaurantes) o 673 (cafeterías y bares), y en el epígrafe 677.9 si vendes para llevar o a domicilio; la apertura se tramita por el régimen municipal (licencia o declaración responsable, según tu ordenanza), a lo que se suman el registro sanitario de tu comunidad autónoma y, si hay terraza, su autorización. Lo que más condiciona el local es la salida de humos: sin conducto a cubierta no hay trompo, plancha ni comal, y si cocinas con carbón la ordenanza suele exigir además filtro de partículas. El gas lo instala una empresa habilitada. El plan lo recoge en un checklist de 80 tareas, pero qué te exigen exactamente en tu municipio, compruébalo con tu ayuntamiento y con tu asesoría antes de firmar el alquiler.',
  },
  {
    q: '¿Qué IVA llevan las bebidas y las aguas frescas para llevar?',
    a: 'En sala, comida y bebida van al 10 %. Para llevar o a domicilio, la comida sigue al 10 %, pero el alcohol (cerveza, mezcal, tequila…) y los refrescos y aguas frescas con azúcares o edulcorantes añadidos van al 21 %. Parece un detalle y se nota en el margen: el Excel lo trae ya partido, con la bebida en una línea propia. Lo de las temperaturas del trompo y de la cámara tiene su norma aparte (art. 30 del RD 1086/2020, en la redacción del RD 1021/2022) y el Word la cita tal cual. Confirma tu caso concreto con tu asesoría.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Taquería» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, el «chile» se dice «ají» en Argentina, Colombia y Chile, el «aguacate» es «palta» en Argentina y Chile, el «camarero» es «mesero» en México y Colombia y «mozo» en Argentina, y el pedido «a domicilio» se dice «delivery» en Argentina, Chile y Perú. Ojo: el marco legal del plan es el español (en México, por ejemplo, el SAT, el RFC o la licencia de funcionamiento no están cubiertos). Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-taqueria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_TAQUERIA',

  seo: {
    title: 'Plan de Negocio Taquería — Excel, Word y Calculadora del Trompo | AI Chef Pro',
    description:
      'Plan de negocio para abrir una taquería: plan financiero en Excel de 9 hojas, plan en Word de 10 secciones, checklist de apertura de 80 tareas y calculadora del trompo al pastor y escandallo por taco. 35 €, pago único.',
    keywords:
      'plan de negocio taquería, plan de negocio taqueria, cómo montar una taquería, como montar una taqueria, cómo poner una taquería, abrir taquería, abrir una taqueria, cuánto cuesta montar una taquería, es rentable una taquería, trompo al pastor, rendimiento del trompo, escandallo tacos, food cost taco al pastor, plan financiero taquería excel, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Taquería',
    productDescription:
      'Plan de negocio para abrir una taquería con trompo al pastor, barra de salsas y servicio para llevar, en un local alquilado. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 80 tareas, una calculadora del trompo y escandallo por taco (rendimiento del trompo, coste de la tortilla comprada o con nixtamal propio y escandallo de la carta) y la Guía de Equivalencias para Latinoamérica. Caso base de 77 comensales al día con un ticket de 15,50 € sin IVA, 300 días al año y unos 358.000 € de ventas. No es un curso de cocina mexicana ni asesoría legal, y no promete rentabilidad.',
    price: '35.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Taquería',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-tortilla.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-salsas.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-taqueria-tortilla.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-salsas.jpg',
      '/lovable-uploads/ai-gallery/plan-taqueria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-taqueria-trompo.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-taqueria-salsas.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-taqueria-hero.jpg',
  },

  hero: {
    badge: 'El trompo es el negocio: monta tu taquería sabiendo cuántos tacos te da cada cono',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Taquería',
    titleSubtitle: 'Plan Financiero en Excel, Plan en Word, Checklist y Calculadora del Trompo',
    description:
      'El plan para abrir una taquería con trompo al pastor, barra de salsas y servicio para llevar, en un local alquilado: la inversión por partidas, la salida de humos, el delivery y el escandallo de cada taco. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones, checklist de apertura de 80 tareas, calculadora del trompo y escandallo por taco, y la Guía de Equivalencias para Hispanoamérica como bonus.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Calculadora del trompo y escandallo por taco: el rendimiento del cono, la tortilla comprada o con nixtamal propio y el food cost de cada taco',
      'Plan de negocio en Word (10 secciones) y checklist de apertura de 80 tareas',
      'Humos, gas y licencia antes de firmar el local, y el IVA del 21 % de la bebida para llevar, con las cuentas hechas',
      'Delivery por plataforma frente al reparto propio, con la comisión real',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      'Es el plan de una taquería: sus números, sus trámites y su trompo. No es un curso de cocina mexicana ni un recetario, y no sustituye a tu asesoría ni al proyecto técnico del local.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias el ticket, los comensales o el alquiler y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Obra, conducto de humos, campana, trompo, plancha, freidora, frío, mobiliario, TPV, marca de lanzamiento e imprevistos, más la fianza, la renta previa, el fondo de maniobra y el IVA de la inversión. En el caso, unos 100.000 € en partidas y unos 172.000 € de necesidad total de caja; todo editable para tu local.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos comensales al día necesitas para cubrir costes (en el caso, unos 64) y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo.' },
      { icon: 'Calculator', title: 'Calculadora del Trompo y Escandallo por Taco', desc: 'Cuatro hojas: el trompo (kilos de cono, adobo, merma, gramos por taco y rendimiento), la tortilla (comprada o nixtamal propio, con su punto de equilibrio), el escandallo de tus tacos y las instrucciones. En el ejemplo, ≈ 278 tacos por cono y ≈ 0,61 € de coste por taco al pastor (≈ 22,5 % de food cost): estimación del kit, editable.' },
      { icon: 'Flame', title: 'Humos, Gas y Licencia', desc: 'Sin conducto a cubierta no hay trompo, plancha ni comal. Gas o carbón, filtro de partículas, instalación de gas por empresa habilitada y consulta urbanística: lo que se decide en la ordenanza de tu ayuntamiento, antes de firmar el local.' },
      { icon: 'Truck', title: 'Delivery: Plataforma o Recogida', desc: 'La comisión de la plataforma, las promociones y el envase frente a la recogida en el local, con el techo del 12 % de las ventas del caso. Y el IVA del 21 % del alcohol y de las aguas frescas azucaradas cuando van para llevar.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing local, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con la tortilla comprada frente al nixtamal, el carbón y el gas, la barra de salsas y los alérgenos.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución; local, humos y gas; cocina, trompo y sanidad; personal y alérgenos; carta, marca y delivery; apertura y primeros 90 días. Con responsable, plazo y nota en cada tarea.' },
      { icon: 'Globe', title: 'Guía de Equivalencias para Hispanoamérica', desc: 'Vocabulario, impuestos, sanidad, normas laborales, licencias y unidades de 20 países, para adaptar el plan a tu mercado. Incluida como bonus.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de una taquería, con su trompo, su tortilla y su barra de salsas.',
    reasons: [
      { icon: 'Calculator', title: 'El Trompo Es la Unidad del Negocio', desc: 'Cuántos tacos te da un cono depende de los kilos, del gramaje y de la merma de cocción, y casi nadie lo mide. La calculadora del trompo te enseña a medirlo y a ver qué le hace a tu food cost, con supuestos del kit editables.' },
      { icon: 'Flame', title: 'Los Humos Se Deciden Antes del Alquiler', desc: 'No es el BOE quien decide si puedes poner un trompo, una plancha y un comal: es la ordenanza de tu ayuntamiento (conducto a cubierta, filtro de partículas si hay carbón) y la instalación de gas. El plan te lo pone en el checklist antes de firmar el local.' },
      { icon: 'Euro', title: 'El IVA de la Bebida para Llevar', desc: 'Para llevar o a domicilio, el alcohol y los refrescos y aguas frescas azucaradas tributan al 21 %, no al 10 %. Parece un detalle y se nota en el margen: el Excel lo trae ya partido.' },
      { icon: 'Scale', title: 'Una Cuenta Honesta, no una Promesa', desc: 'Con tu sueldo y la plantilla ya dentro, tres escenarios (el pesimista, con pérdidas) y la plataforma de delivery frente a la recogida, con la comisión real. Y la tortilla comprada frente al nixtamal propio, con su punto de equilibrio. Para decidir con números, no con promesas.' },
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
      'Además del plan financiero, el plan en Word, el checklist y la calculadora del trompo, te llevas un extra — valorado en €15',
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
    headingGold: 'Taquería',
    subtitle:
      'Antes de firmar el local y de encargar el trompo, ten las cuentas, los trámites, la tortilla y el escandallo de cada taco sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes y tres escenarios (pesimista, realista y optimista)',
      'Calculadora del trompo y escandallo por taco',
      'Humos, gas y licencia en el checklist antes de firmar el local',
      'Checklist de apertura con 80 tareas',
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

  stickyLabel: 'PLAN TAQUERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-taqueria', label: 'Kit de Tareas Recurrentes: Taquería Mexicana' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/pack-appcc', label: 'Pack Plantillas APPCC' },
    { href: '/guia-restaurante-mexicano', label: 'Guía Restaurante Mexicano' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · noviembre 2026',

  alreadyBought: {
    product: 'plan-negocio-taqueria',
    label: '¿Ya compraste el Plan de Negocio: Taquería? Vuelve a entrar al dashboard',
  },
};

export default data;
