// astro-site/src/data/productos/planes/plan-negocio-pizzeria.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (octubre 2026), 35 €.
// Landing NATIVA. Moldes: plan-negocio-finca-eventos-bodas.ts (sin testimonios) y plan-negocio-heladeria.ts (35 €, local fijo).
// Fuentes: scripts/productos-digitales/plan-pizzeria/{SPEC.md (D1, D2, D11, D12, D17), F1-research-pizzeria.md (§0, §4, §6),
//   cifras_caso_es.json, F2-NOTAS.md}.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Pizzería Napolitana» (H1, schema.productName, catálogo, hub, breadcrumb).
//  · SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials` (producto recién nacido; la clave
//    `testimonials` se OMITE por completo: la plantilla pinta marquee con 5 estrellas si es un objeto).
//  · D11: el producto NO llama «napolitana» a ninguna pizza del caso y NUNCA dice «certificada», «ETG» ni «verace» como sello
//    del lector o del producto. Se explica qué puede poner el lector en su carta y se le manda a la verificación oficial.
//    La AVPN es privada y no sustituye a esa verificación. Sin prometer certificación.
//  · D12: sin «España 2026» como sello, sin «validado», sin neto «15-25 %» como dato propio (solo como lo que «circula»).
//  · Cifras de la landing: SOLO las MEDIDAS del caso (cifras_caso_es.json) y las estables (5 ficheros, 9 hojas, 10 secciones,
//    80 tareas). NADA de DSCR, payback, saldos de tesorería ni importe del préstamo.
//  · CRIPTO: nada que tocar (la plantilla monta las puertas si cryptoEnabledFor('plan-negocio-pizzeria')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ pizzería napolitana con el horno de leña encendido y la sala preparada
//   horno ....... horno de leña de cúpula baja con una pizza entrando
//   masa ........ bolas de masa en reposo sobre la mesa de trabajo
//   sala ........ sala de la pizzería con las mesas puestas
//   delivery .... cajas de pizza listas para repartir
//   equipo ...... el equipo de la pizzería en la línea de montaje
//   plan ........ plan de negocio y hojas de cálculo sobre una mesa de la pizzería
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 8 FAQ (research §6 + SPEC D11/D17). Una sola fuente: el acordeón de la página y el FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Puedo poner «pizza napolitana» en la carta de mi pizzería?',
    a: 'Solo si tu pizza cumple el pliego y pasa la verificación oficial, porque desde diciembre de 2022 «Pizza Napoletana» es una especialidad tradicional garantizada (ETG) con reserva de nombre (Reglamento de Ejecución (UE) 2022/2313), y esa protección alcanza también al nombre traducido, así que «pizza napolitana» no es una etiqueta libre. Para usarlo hay que elaborar la pizza según el pliego (masa del día a temperatura ambiente, estirado a mano, horno de leña, ciertos quesos…) y pasar la verificación oficial antes de vender. La AVPN es una asociación privada y su certificación no sustituye a esa verificación. Qué autoridad la lleva en tu comunidad y qué cuesta, compruébalo antes de imprimir la carta. El plan te explica qué puedes poner mientras tanto («Margherita», «Marinara»…), te deja la ETG como opción razonada en el Word y te avisa de que rótulos como «estilo napolitano» pueden ser evocación: consúltalo antes de usarlos. No prometemos certificación de nada.',
  },
  {
    q: '¿Cuánto cuesta montar una pizzería?',
    a: 'Depende del local, de la salida de humos y del horno, que es la partida que más mueve la cuenta. En el caso del plan (un local alquilado de 50 plazas) salen unos 130.000 € en partidas de obra y equipos, unos 143.000 € contando la fianza y la renta previa, y unos 223.000 € de necesidad total de caja una vez sumados el fondo de maniobra de tres meses y el IVA de la inversión. Son cifras de ejemplo: el Excel trae la inversión por partidas (obra, horno, chimenea, campana, amasadora, mobiliario, TPV, marca, imprevistos…) todas editables para que pongas las tuyas y veas cuánto necesitas tú.',
  },
  {
    q: '¿Qué rentabilidad tiene una pizzería?',
    a: 'No te prometemos rentabilidad: depende de tu local, de tu ticket y de lo que llenes cada día. Lo que sí hace el plan es enseñarte la cuenta con honestidad. En el caso medido por el Excel (66 comensales al día a 19,50 € de ticket sin IVA, 300 días al año, unos 386.000 € de ventas) el beneficio neto sale en un 8,5 % de las ventas el primer año y en torno al 10 % el segundo y el tercero, con la plantilla y tu propio sueldo ya dentro, y el equilibrio, en unos 57 comensales al día. Está muy lejos del «15-25 %» que circula por internet. Tienes tres escenarios (el pesimista, con pérdidas, incluido) para ver qué pasa con un año flojo.',
  },
  {
    q: '¿Cuántas pizzas salen de 1 kg de harina?',
    a: 'Con la receta del pliego (1 litro de agua, 50-55 g de sal, 3 g de levadura y 1.800 g de harina) sale algo más de 1.580 g de masa por cada kilo de harina, es decir, unas 6 bolas de 250 g (o casi 8 de 200 g). La calculadora de masa lo hace por ti: eliges cuántas bolas y de qué peso, la merma y los gramos por litro, y te da los gramos de cada ingrediente, y compara tu masa con los gramajes del pliego («dentro de los gramajes del pliego» o «fuera»; nunca «es napolitana»). Con un segundo bloque, el B, calculas tu masa por porcentaje panadero con tu propia hidratación, sal y levadura; los tiempos de fermentación los fijan tu receta y tu APPCC.',
  },
  {
    q: '¿Horno de leña, de gas o eléctrico?',
    a: 'Cada uno cambia la inversión, la potencia que necesitas, los humos y el nombre que puedes poner en la carta. El de leña da el sabor y es el único que encaja con el pliego de la «Pizza Napoletana», pero necesita chimenea y, según la ordenanza de humos de tu ayuntamiento, un conducto exclusivo a cubierta y filtro de partículas: eso se decide en la ordenanza municipal, no en el BOE, y conviene saberlo antes de firmar el local. El de gas pide instaladora habilitada y revisión periódica, y el eléctrico es el más sencillo de instalar, aunque pide unos 16 kW más en trifásica y también campana y conducto para los vahos. El Excel parte de un horno de leña (con la leña y el mantenimiento como gasto fijo) y el Word compara las tres opciones, con la variante eléctrica incluida.',
  },
  {
    q: '¿Me conviene el delivery por plataforma?',
    a: 'Depende de cuánto te dejen las comisiones. Las plataformas suelen cobrar entre el 25 % y el 35 % más IVA, a lo que se suman las promociones y la caja, y la pizza de masa blanda llega peor a casa. En el caso del plan el reparto por plataforma pesa el 10 % de las ventas, con la comisión al 30 %, y el Word hace la cuenta del reparto propio frente a la plataforma para que decidas con números. Además, para llevar o a domicilio la cerveza, el vino y los refrescos con azúcares o edulcorantes añadidos van al 21 % de IVA (en sala, todo al 10 %). Y si repartes tú, el repartidor es hostelería y lleva contrato laboral; confírmalo con tu asesoría.',
  },
  {
    q: '¿Qué licencias necesito para abrir una pizzería?',
    a: 'La pizzería tributa por el IAE en el grupo 671 (restaurantes) y, si vendes para llevar o a domicilio, en el epígrafe 677.9; la apertura se tramita por el régimen municipal (licencia o declaración responsable, según tu ordenanza), a lo que se suman el registro sanitario de tu comunidad autónoma y, si hay terraza, la autorización correspondiente. Lo que más condiciona el local es la salida de humos. El plan lo recoge en un checklist de 80 tareas, pero qué te exigen exactamente en tu municipio, compruébalo con tu ayuntamiento y con tu asesoría antes de firmar el alquiler.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Pizzería Napolitana» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, la «mozzarella» es «muzzarella» en Argentina, el «camarero» es «mesero» en México y Colombia y «mozo» en Argentina, el pedido «a domicilio» se dice «delivery» en Argentina, Chile y Perú, y ojo con la «pizza napolitana», que en Argentina es otra pizza (con rodajas de tomate y ajo). Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-pizzeria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_PIZZERIA',

  seo: {
    title: 'Plan de Negocio Pizzería Napolitana — Excel, Word y Calculadora de Masa | AI Chef Pro',
    description:
      'Plan de negocio para abrir una pizzería: plan financiero en Excel de 9 hojas, plan en Word de 10 secciones, checklist de apertura de 80 tareas, calculadora de masa y escandallo por pizza, y el nombre de la carta bien resuelto. 35 €, pago único.',
    keywords:
      'plan de negocio pizzería, plan de negocio pizzería napolitana, cómo montar una pizzería, abrir una pizzería, cuánto cuesta montar una pizzería, es rentable una pizzería, horno de leña pizzería, escandallo pizza, food cost pizza, plan financiero pizzería excel, pizza napolitana ETG, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Pizzería Napolitana',
    productDescription:
      'Plan de negocio para abrir una pizzería de horno de leña con sala y servicio para llevar, en un local alquilado. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 80 tareas, una calculadora de masa y escandallo por pizza (masa según los gramajes del pliego o masa de panadero, y escandallo de 8 pizzas) y la Guía de Equivalencias para Latinoamérica. Caso base de 66 comensales al día con un ticket de 19,50 € sin IVA, 300 días al año y unos 386.000 € de ventas. Explica qué se puede poner en la carta tras la reserva del nombre «Pizza Napoletana» (Reglamento de Ejecución (UE) 2022/2313) y no promete certificación. No es un curso de pizzaiolo ni asesoría legal, y no promete rentabilidad.',
    price: '35.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Pizzería Napolitana',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-sala.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-pizzeria-masa.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-sala.jpg',
      '/lovable-uploads/ai-gallery/plan-pizzeria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-pizzeria-horno.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-pizzeria-sala.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-pizzeria-hero.jpg',
  },

  hero: {
    badge: 'Desde 2022, «pizza napolitana» es un nombre reservado: monta tu pizzería sabiendo qué poner en la carta',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Pizzería Napolitana',
    titleSubtitle: 'Plan Financiero en Excel, Plan en Word, Checklist y Calculadora de Masa',
    description:
      'El plan para abrir una pizzería de horno de leña en un local alquilado, con sala y servicio para llevar: la inversión por partidas, la salida de humos, el delivery y el nombre de la carta. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones, checklist de apertura de 80 tareas, calculadora de masa y escandallo por pizza, y la Guía de Equivalencias para Hispanoamérica como bonus.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Calculadora de masa y escandallo por pizza: compara tu masa con los gramajes del pliego y te dice cuánto cuesta cada pizza',
      'Qué puedes poner en tu carta: la «Pizza Napoletana» es un nombre reservado desde 2022',
      'Plan de negocio en Word (10 secciones) y checklist de apertura de 80 tareas',
      'Horno de leña, gas o eléctrico, y el delivery por plataforma frente al reparto propio, con las cuentas hechas',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      'Es el plan de una pizzería: sus números, sus trámites y su horno. No es un curso de pizzaiolo ni un recetario, y no sustituye a tu asesoría, al proyecto técnico ni a la verificación oficial si quieres usar el nombre protegido.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias el ticket, los comensales o el alquiler y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Obra, horno de leña con su chimenea, campana, amasadora, mesa fría, mobiliario, TPV, marca de lanzamiento e imprevistos, más la fianza, la renta previa, el fondo de maniobra y el IVA de la inversión. En el caso, unos 130.000 € en partidas y unos 223.000 € de necesidad total de caja; todo editable para tu local.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos comensales al día necesitas para cubrir costes (en el caso, unos 57) y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo.' },
      { icon: 'Calculator', title: 'Calculadora de Masa y Escandallo por Pizza', desc: 'El bloque A calcula la masa con los gramajes del pliego (agua, harina, sal, levadura, bolas de 180-250 g) y compara la tuya; el B, tu masa por porcentaje panadero. El escandallo de 8 pizzas te da el coste por bola (≈ 0,23 € en el ejemplo) y el food cost de la Margherita (≈ 15 % en el ejemplo), editable.' },
      { icon: 'Flame', title: 'Horno de Leña, Gas o Eléctrico', desc: 'El horno es la partida y la decisión que más pesa: potencia, chimenea, filtro de partículas, leña y mantenimiento como gasto fijo. Y la salida de humos, que se decide en la ordenanza de tu ayuntamiento, antes de firmar el local.' },
      { icon: 'Truck', title: 'Delivery: Plataforma o Recogida', desc: 'La comisión de la plataforma, las promociones y la caja frente a la recogida en el local, con el techo del 10 % de las ventas del caso. Y el IVA del 21 % de la cerveza, el vino y los refrescos azucarados o edulcorados cuando van para llevar.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing local, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con el nombre de la carta, la ordenanza de humos, el sin gluten y la Ley 1/2025 de desperdicio alimentario.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución; local, humos y licencia; cocina, horno y sanidad; personal y prevención; carta, marca y delivery; apertura y primeros 90 días. Con responsable, plazo y nota en cada tarea.' },
      { icon: 'Globe', title: 'Guía de Equivalencias para Hispanoamérica', desc: 'Vocabulario, impuestos, sanidad, normas laborales, licencias y unidades de 20 países, para adaptar el plan a tu mercado. Incluida como bonus.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de una pizzería, con su horno, su masa y su carta.',
    reasons: [
      { icon: 'ShieldCheck', title: '«Pizza Napolitana» Es un Nombre Reservado', desc: 'Desde 2022, «Pizza Napoletana» es una ETG con reserva de nombre (Reglamento de Ejecución (UE) 2022/2313), también traducida. El plan te explica qué puedes poner en tu carta y qué exige la verificación oficial antes de usar el nombre; la AVPN es privada y no la sustituye. Sin prometer certificación.' },
      { icon: 'Flame', title: 'El Horno de Leña se Decide en la Ordenanza', desc: 'No es el BOE quien decide si puedes instalar un horno de leña: es la ordenanza de humos de tu ayuntamiento (conducto a cubierta, filtro de partículas, limpieza). El plan te lo pone en el checklist antes del alquiler y compara leña, gas y eléctrico.' },
      { icon: 'Euro', title: 'El IVA de la Bebida para Llevar', desc: 'Para llevar o a domicilio, la cerveza, el vino y los refrescos azucarados o edulcorados tributan al 21 %, no al 10 %. Parece un detalle y se nota en el margen: el Excel lo trae ya partido.' },
      { icon: 'Scale', title: 'Un Neto Realista, no el «15-25 %»', desc: 'Con las cifras del Excel, el neto sale en un 8,5 % de las ventas el primer año y en torno al 10 % los dos siguientes, con la plantilla y tu sueldo dentro. Y la plataforma de delivery frente a la recogida, con la comisión real. Para decidir con números, no con promesas.' },
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
      'Además del plan financiero, el plan en Word, el checklist y la calculadora de masa, te llevas un extra — valorado en €15',
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
    headingGold: 'Pizzería',
    subtitle:
      'Antes de firmar el local y de encargar el horno, ten las cuentas, los trámites, la masa y el nombre de la carta sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes y tres escenarios (pesimista, realista y optimista)',
      'Calculadora de masa y escandallo por pizza',
      'Qué poner en la carta: el nombre «Pizza Napoletana» está reservado',
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

  stickyLabel: 'PLAN PIZZERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-pizzeria', label: 'Kit de Tareas Recurrentes: Pizzería' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/pack-appcc', label: 'Pack Plantillas APPCC' },
    { href: '/plan-negocio-bar-restaurante', label: 'Plan Bar-Restaurante' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · octubre 2026',

  alreadyBought: {
    product: 'plan-negocio-pizzeria',
    label: '¿Ya compraste el Plan de Negocio: Pizzería Napolitana? Vuelve a entrar al dashboard',
  },
};

export default data;
