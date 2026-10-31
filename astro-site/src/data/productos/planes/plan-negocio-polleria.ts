// astro-site/src/data/productos/planes/plan-negocio-polleria.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (noviembre 2026), 35 €.
// Landing NATIVA. Molde: el plan hermano de la línea (sin testimonios, 35 €, local fijo).
// Fuentes: scripts/productos-digitales/plan-polleria/{F1-camino.md (§4, §5), F1-research-polleria.md (§0, §1, §4, §6, §8),
//   cifras_caso_es.json, F2-NOTAS.md}.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Pollería y Asador de Pollos» (H1, schema.productName, catálogo, hub, breadcrumb).
//    En España «pollería» es también la tienda de pollo crudo: el nombre lleva siempre «asador de pollos» y nunca «asador» suelto.
//  · SIN año fijo en title/meta/H1 (AGENTS.md: si algún día lleva año, token {year}).
//  · SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials` (producto recién nacido; la clave
//    `testimonials` se OMITE por completo: la plantilla pinta marquee con 5 estrellas si es un objeto).
//  · Cifras de la landing: SOLO las MEDIDAS del caso (cifras_caso_es.json) y las estables (5 ficheros, 9 hojas, 10 secciones,
//    80 tareas). NADA de DSCR, payback, saldos de tesorería, importe del préstamo ni neto exacto.
//    Calculadora: siempre «estimación del kit, editable». Food cost siempre sobre el precio SIN IVA.
//  · LEGAL (R §1): IAE 677.9; IVA 10 % de la comida; para llevar, alcohol y refrescos azucarados al 21 %; temperaturas = art. 30 del
//    RD 1086/2020 en la redacción del RD 1021/2022; cámara de crudos por el RD 1021/2022. Nada de «sin gluten» prometido.
//  · CRIPTO: nada que tocar (la plantilla monta las puertas si cryptoEnabledFor('plan-negocio-polleria')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ pollería-asador con las espadas del asador girando y el mostrador preparado
//   asador ...... asador de gas de espadas con los pollos dorándose
//   mostrador ... mostrador con pollos asados, patatas y cremas listos para llevar
//   brasa ....... pollo a la brasa en horno de carbón o leña
//   delivery .... bolsas de pollo asado listas para repartir
//   equipo ...... el equipo de la pollería en la línea de servicio
//   plan ........ plan de negocio y hojas de cálculo sobre el mostrador de la pollería
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 9 FAQ (research §6 + patrón de la línea). Una sola fuente: el acordeón de la página y el FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Cuánto cuesta montar una pollería o un asador de pollos?',
    a: 'Depende del local, de la salida de humos, de la potencia eléctrica y del asador, que son las partidas que más mueven la cuenta. En el caso del plan (un local alquilado de 80 m² con 20 plazas, un asador de gas de 12 espadas y el 72 % de las ventas fuera del local) salen unos 93.100 € en partidas de obra y equipos, imprevistos incluidos, y unos 161.600 € de necesidad total de caja una vez sumados la fianza, la renta previa, el fondo de maniobra de tres meses y el IVA de la inversión. Son cifras de ejemplo: el Excel trae la inversión por partidas (obra, conducto de humos, campana, asador, vitrina, freidora, frío, mobiliario, TPV, marca, imprevistos…) todas editables para que pongas las tuyas y veas cuánto necesitas tú.',
  },
  {
    q: '¿Es rentable una pollería? ¿Cuánto deja de ganancia?',
    a: 'No te prometemos rentabilidad: depende de tu local, de tu ticket y de lo que llenes cada día, y un asador vive de los fines de semana y del verano. Lo que sí hace el plan es enseñarte la cuenta con honestidad. En el caso medido por el Excel (77 pedidos al día a 15,80 € por pedido sin IVA, 300 días al año, unos 365.000 € de ventas) el beneficio neto queda en torno al 7-8 % de las ventas, con la plantilla y tu propio sueldo ya dentro, y el equilibrio llega con unos 64-67 pedidos al día. Tienes tres escenarios (el pesimista, con pérdidas, incluido) para ver qué pasa con un año flojo, y todo se recalcula cuando cambias el ticket, los pedidos o el alquiler.',
  },
  {
    q: '¿Cuántos pollos hay que vender a la semana para cubrir gastos?',
    a: 'Con los supuestos del caso (estimación del kit, editable) la pollería vende unos 301 pollos a la semana y cubre sus gastos con unos 250-262, es decir, entre 64 y 67 pedidos al día. No es una cifra universal: depende de cuánto pollo lleve cada pedido y de lo que cueste tu local. El Excel te deja cambiar el ticket, los pedidos y el alquiler y ver al instante en qué punto estás tú, y la calculadora del pollo te enseña a traducir esos pedidos a pollos y a cargas del asador.',
  },
  {
    q: '¿Cuánto pesa un pollo asado y cuánto merma?',
    a: 'Un pollo pierde peso por el camino: el agua y la grasa que suelta al asarse. Con los supuestos del kit (estimación editable) el rendimiento del asado es del 76 %: un pollo de 1,45 kg en canal queda en unos 1,10 kg ya asado. La hoja Pollo de la calculadora hace la cuenta con tus datos (peso en canal, precio por kilo, sazón, rendimiento, sobrantes del cierre) y te da el coste del pollo entero y de la mitad, el cuarto y el octavo. Con los supuestos del caso el pollo entero cuesta unos 4,55 € y, sobre el precio de venta sin IVA, queda en un food cost de alrededor del 38,8 %: por eso el margen está en las patatas, las croquetas y la bebida, no en vender el pollo solo.',
  },
  {
    q: '¿Qué asador necesito y cuántos pollos caben?',
    a: 'Depende de lo que vendas el día que más vendes, que casi siempre es el domingo. Cada espada admite varios pollos (la ficha de los fabricantes habla de cuatro a seis) y el tiempo de asado lo tienes que medir con tu asador. Con los supuestos del kit (estimación editable) un asador de gas de 12 espadas carga unos 60 pollos por tanda y llega a unos 180 antes de las 15:00 del domingo. La hoja Asador de la calculadora hace la cuenta de cargas con tus datos, te dice si te falta o te sobra capacidad en la punta y qué pasa en agosto, y te ahorra comprar un asador pequeño para el domingo o grande para el martes.',
  },
  {
    q: '¿Pollo a la brasa con leña o carbón, o asador de gas?',
    a: 'El caso del plan usa asador de gas, que se instala con campana y conducto a cubierta normales y con una empresa de gas habilitada. El pollo a la brasa peruano de horno de leña o carbón, el venezolano y la churrasqueira portuguesa de carbón (el piri-piri) son otra decisión de producto: dan un sabor propio, pero la ordenanza suele exigir proyecto y filtro de partículas, y los vecinos cuentan. El Word recoge las cinco corrientes del pollo asado (peruana, venezolana, española con el pollo al ast, francesa de rôtisserie y portuguesa piri-piri) y explica qué cambia en cada una; la brasa de carbón o leña se trata como variante del Word, sin hoja de Excel propia. Si te interesa el restaurante peruano completo, tienes la Guía Restaurante Peruano.',
  },
  {
    q: '¿Qué licencias necesito, y qué IVA llevan el pollo y la bebida para llevar?',
    a: 'Una pollería con asador y comida preparada tributa por el IAE en el epígrafe 677.9 (y en el 671 o el 673 si tiene sala), no solo en el 642.5 de la pollería de crudos, que no ampara asar ni vender comida preparada. La apertura se tramita por el régimen municipal (licencia o declaración responsable, según tu ordenanza), a lo que se suman el registro sanitario de tu comunidad autónoma; sin conducto de humos a cubierta, sin trifásica y sin gas por empresa habilitada no hay asador. En cuanto al IVA, la comida va al 10 %, pero para llevar o a domicilio el alcohol y los refrescos con azúcares o edulcorantes añadidos van al 21 %. Las temperaturas tienen su norma: la cámara de aves y el adobado, el RD 1021/2022; el mantenimiento en caliente y el enfriado del sobrante, el art. 30 del RD 1086/2020 en la redacción del RD 1021/2022. El plan lo recoge en un checklist de 80 tareas, pero qué te exigen exactamente en tu municipio, compruébalo con tu ayuntamiento y con tu asesoría antes de firmar el alquiler.',
  },
  {
    q: '¿Y un asador ambulante en un mercadillo o un remolque?',
    a: 'Es otro negocio: un asador sobre ruedas se mueve entre mercadillos, ferias y eventos, con otros permisos, otra cuenta de resultados y otra logística. Este plan es el de una pollería-asador con local fijo y alquilado. Si lo tuyo es el remolque, mira el Plan de Negocio: Food Truck de nuestro catálogo, que parte de la cuenta del vehículo.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Pollería y Asador de Pollos» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, el pollo asado se dice «pollo rostizado» y el local, «rosticería», en México; «rotisería» en Argentina; «pollo a la brasa» y «pollería» en Perú; «asadero» en Colombia. El «chile» se dice «ají» en Argentina, Colombia y Chile, el «camarero» es «mesero» en México y Colombia y «mozo» en Argentina, y el pedido «a domicilio» se dice «delivery» en Argentina, Chile y Perú. Ojo: el marco legal del plan es el español (en México, por ejemplo, el SAT, el RFC o la licencia de funcionamiento no están cubiertos). Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-polleria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_POLLERIA',

  seo: {
    title: 'Plan de Negocio Pollería y Asador de Pollos — Excel, Word y Calculadora | AI Chef Pro',
    description:
      'Plan de negocio para abrir una pollería y asador de pollos: plan financiero en Excel de 9 hojas, plan en Word de 10 secciones, checklist de apertura de 80 tareas y calculadora del pollo, la capacidad del asador y el escandallo. 35 €, pago único.',
    keywords:
      'plan de negocio pollería, plan de negocio asador de pollos, cómo montar una pollería, como montar una polleria, cómo montar un asador de pollos, negocio de pollos asados, pollo a la brasa, pollo asado, pollo al ast, pollo piri piri, rosticería, rotisería, asadero de pollos, cuánto cuesta montar una pollería, es rentable una pollería, rendimiento del pollo asado, escandallo pollo asado, plan financiero pollería excel, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-polleria-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Pollería y Asador de Pollos',
    productDescription:
      'Plan de negocio para abrir una pollería-asador de pollos con asador de gas de espadas, mostrador de encargos, plataforma de reparto y sala, en un local alquilado. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones con las cinco corrientes del pollo asado (peruana, venezolana, española con el pollo al ast, francesa y portuguesa piri-piri), un checklist de apertura de 80 tareas, una calculadora del pollo, la capacidad del asador y el escandallo (rendimiento del asado, cargas del domingo y food cost de cada combo) y la Guía de Equivalencias para Latinoamérica. Caso base de 77 pedidos al día con 15,80 € por pedido sin IVA, 300 días al año y unos 365.000 € de ventas. No es un curso de cocina ni asesoría legal, y no promete rentabilidad.',
    price: '35.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Pollería y Asador de Pollos',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-polleria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-asador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-mostrador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-brasa.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-polleria-mostrador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-asador.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-brasa.jpg',
      '/lovable-uploads/ai-gallery/plan-polleria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-polleria-asador.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-polleria-brasa.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-polleria-hero.jpg',
  },

  hero: {
    badge: 'El asador es el negocio: monta tu pollería sabiendo cuántos pollos caben antes del domingo a las tres',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Pollería y Asador de Pollos',
    titleSubtitle: 'Pollo a la brasa, pollo asado y al ast: Excel, Word, checklist y calculadora del asador',
    description:
      'El plan para abrir una pollería y asador de pollos con asador de gas, mostrador de encargos, plataforma de reparto y sala, en un local alquilado: la inversión por partidas, la salida de humos, el delivery y el escandallo de cada combo. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones con las cinco corrientes del pollo asado, checklist de apertura de 80 tareas, calculadora del pollo y del asador, y la Guía de Equivalencias para Hispanoamérica como bonus.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Calculadora del pollo, el asador y el escandallo: el rendimiento del asado, cuántos pollos caben antes del domingo a las 15:00 y el food cost de cada combo',
      'Plan de negocio en Word (10 secciones) con las cinco corrientes del pollo asado, y checklist de apertura de 80 tareas',
      'Humos, gas y licencia antes de firmar el local, y el IVA del 21 % de la bebida para llevar, con las cuentas hechas',
      'Delivery por plataforma frente a los encargos en el mostrador, con la comisión real',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      'Es el plan de una pollería-asador: sus números, sus trámites y su asador. No es un curso de cocina ni un recetario, y no sustituye a tu asesoría ni al proyecto técnico del local.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias el ticket, los pedidos o el alquiler y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Obra, conducto de humos, campana, asador, vitrina, freidora, frío, mobiliario, TPV, marca de lanzamiento e imprevistos, más la fianza, la renta previa, el fondo de maniobra y el IVA de la inversión. En el caso, unos 93.100 € en partidas y unos 161.600 € de necesidad total de caja; todo editable para tu local.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos pedidos al día necesitas para cubrir costes (en el caso, entre 64 y 67) y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo.' },
      { icon: 'Calculator', title: 'Calculadora del Pollo, el Asador y el Escandallo', desc: 'Cuatro hojas: el pollo (peso en canal, rendimiento del asado, coste del entero, la mitad y el cuarto), el asador (espadas, pollos por tanda y capacidad antes de las 15:00 del domingo), el escandallo de tus combos con su food cost y margen por canal, e instrucciones. En el ejemplo, rendimiento del 76 % y ≈ 4,55 € de coste por pollo entero (≈ 38,8 % de food cost sobre el precio sin IVA): estimación del kit, editable.' },
      { icon: 'Flame', title: 'Humos, Gas y Licencia', desc: 'Sin conducto a cubierta no hay asador ni freidora. Gas o brasa, filtro de partículas si hay leña o carbón, trifásica, instalación de gas por empresa habilitada y consulta urbanística: lo que se decide en la ordenanza de tu ayuntamiento, antes de firmar el local.' },
      { icon: 'Truck', title: 'Delivery y Encargos del Domingo', desc: 'La comisión de la plataforma, las promociones y el envase frente al encargo con hora de recogida en el mostrador, con el techo del 11 % de las ventas del caso. Y el IVA del 21 % del alcohol y los refrescos azucarados cuando van para llevar.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing local, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con las cinco corrientes del pollo asado (peruana, venezolana, española con el pollo al ast, francesa y portuguesa piri-piri), el sobrante convertido en croqueta y los alérgenos del adobo.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución; local, humos y gas; cocina, asador y sanidad; personal y alérgenos; carta, marca y encargos; apertura y primeros 90 días. Con responsable, plazo y nota en cada tarea.' },
      { icon: 'Globe', title: 'Guía de Equivalencias para Hispanoamérica', desc: 'Vocabulario, impuestos, sanidad, normas laborales, licencias y unidades de 20 países, para adaptar el plan a tu mercado. Incluida como bonus.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de una pollería-asador, con su pollo, su asador y su domingo.',
    reasons: [
      { icon: 'Calculator', title: 'El Pollo Es la Unidad del Negocio', desc: 'Cuánto rinde un pollo asado y cuántos caben en el asador antes de la punta del domingo casi nadie lo mide. La calculadora te enseña a medirlo y a ver qué le hace a tu food cost, con supuestos del kit editables.' },
      { icon: 'Flame', title: 'Los Humos Se Deciden Antes del Alquiler', desc: 'No es el BOE quien decide si puedes poner un asador y una freidora: es la ordenanza de tu ayuntamiento (conducto a cubierta, filtro de partículas si hay leña o carbón), la trifásica y la instalación de gas. El plan te lo pone en el checklist antes de firmar el local.' },
      { icon: 'Euro', title: 'El IVA de la Bebida para Llevar', desc: 'Para llevar o a domicilio, el alcohol y los refrescos azucarados tributan al 21 %, no al 10 %. Parece un detalle y se nota en el margen: el Excel lo trae ya partido.' },
      { icon: 'Scale', title: 'Una Cuenta Honesta, no una Promesa', desc: 'Con tu sueldo y la plantilla ya dentro, tres escenarios (el pesimista, con pérdidas) y la plataforma de delivery frente al encargo en el mostrador, con la comisión real. Para decidir con números, no con promesas.' },
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
      'Además del plan financiero, el plan en Word, el checklist y la calculadora del pollo, te llevas un extra — valorado en €15',
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
    headingGold: 'Pollería',
    subtitle:
      'Antes de firmar el local y de encargar el asador, ten las cuentas, los trámites, la capacidad del domingo y el escandallo de cada combo sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes y tres escenarios (pesimista, realista y optimista)',
      'Calculadora del pollo, el asador y el escandallo',
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

  stickyLabel: 'PLAN POLLERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/guia-restaurante-peruano', label: 'Guía Restaurante Peruano' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/pack-appcc', label: 'Pack Plantillas APPCC' },
    { href: '/plan-negocio-taqueria', label: 'Plan de Negocio: Taquería' },
    { href: '/plan-negocio-sushi-bar', label: 'Plan de Negocio: Sushi Bar' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · noviembre 2026',

  alreadyBought: {
    product: 'plan-negocio-polleria',
    label: '¿Ya compraste el Plan de Negocio: Pollería y Asador de Pollos? Vuelve a entrar al dashboard',
  },
};

export default data;
