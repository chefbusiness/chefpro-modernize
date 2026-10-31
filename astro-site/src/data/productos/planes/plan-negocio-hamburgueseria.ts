// astro-site/src/data/productos/planes/plan-negocio-hamburgueseria.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (noviembre 2026), 35 €.
// Landing NATIVA. Molde: plan-negocio-sushi-bar.ts (sin testimonios, 35 €, local fijo).
// Fuentes: scripts/productos-digitales/plan-hamburgueseria/{F0-mapa-keywords-es-en.md, F1-camino.md, F1-research-hamburgueseria.md
//   (§0, §1, §4, §6), cifras_caso_es.json, F2-NOTAS.md (§4, §8), REVISION-FINAL.md}. Las cifras son las MEDIDAS de
//   cifras_caso_es.json y de F2-NOTAS §4 y §8, nunca las de la SPEC ni las de R cuando difieren.
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Hamburguesería Smash» (H1, schema.productName, catálogo, hub, breadcrumb).
//    «Cómo montar una hamburguesería» va en el subtítulo, la meta y las keywords. «Franquicia» solo en la FAQ.
//  · SIN año fijo en title/meta/H1. SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials`
//    (producto recién nacido; la clave `testimonials` se OMITE por completo: la plantilla pinta marquee con 5 estrellas si es un objeto).
//  · Cifras de la landing: SOLO las MEDIDAS del caso y las estables (5 ficheros, 9 hojas, 10 secciones, 80 tareas, 4 hojas y
//    14 productos en la calculadora). NADA de DSCR, payback ni saldos de tesorería. Calculadora: «estimación del kit, editable».
//    Food cost siempre sobre el precio SIN IVA. «95 comensales» siempre con «equivalentes» (1 pedido = 1,7).
//  · Lo que arregló la revisión (REVISION-FINAL.md M1-M4, m3, m4, m6, m8): sin temperatura legal de cocción (AESAN: 70 °C o más
//    durante al menos 2 minutos, recomendación; lo decide tu APPCC); la carne madurada más de 15 días solo como prohibición
//    (Madrid Salud, Inf26008); aceite: polares < 25 % y nada ajeno al aceite añadido al baño (no hay que tirarlo por reponerlo);
//    food cost teórico 24,4 % frente al 28 % prudente («unos 4 puntos», sin desglose); la regla del 21 % entera (cerveza y
//    refrescos con azúcares o edulcorantes añadidos, también los zero, que salen del local); plataforma 24 % de las ventas;
//    plancha de 60 a 80 cm; «sin gluten» nunca prometido; sin cifras de franquicia como caso (solo como comparación).
//  · CRIPTO: nada que tocar (la plantilla monta las puertas si cryptoEnabledFor('plan-negocio-hamburgueseria')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ hamburguesería smash de barrio con la plancha a la vista, el mostrador de pedidos y la sala pequeña
//   plancha ..... smash burger aplastándose en la plancha de acero con la prensa
//   carne ....... bolas de carne picada de 100 g porcionadas en la mesa refrigerada
//   patatas ..... cuba de la freidora y raciones de patatas en cucurucho
//   delivery .... bolsas y cajas de hamburguesa listas para recoger y repartir
//   equipo ...... el equipo en la línea de montaje durante el servicio, de espaldas
//   plan ........ plan de negocio, portátil y calculadora sobre el mostrador de la hamburguesería cerrada
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 11 FAQ (research §6 + la del carrito → Plan de Negocio: Food Truck). Una sola fuente: el acordeón de la página y el
// FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Cuánto cuesta montar una hamburguesería?',
    a: 'Depende del local, de la salida de humos y de la plancha, que son las partidas que más mueven la cuenta. En el caso del plan (un local alquilado de 90 m² con 36 plazas y el 24 % de las ventas por plataforma) salen 104.350 € en partidas de obra, equipos, licencias, marca y stock inicial, imprevistos incluidos; 162.144 € de inversión una vez sumados la fianza, la renta previa y el fondo de maniobra de tres meses, y 184.057 € de necesidad total de caja con el IVA de la inversión, cubiertos en el ejemplo con 55.000 € propios y un préstamo de 130.000 €. Son cifras de ejemplo: el Excel trae la inversión por partidas (proyecto técnico, obra, conducto de extracción, plancha, freidoras, mesa refrigerada, campana, mobiliario, TPV, marca, imprevistos…), todas editables para que pongas las tuyas y veas cuánto necesitas tú. Como referencia, según emprendedores.es, una franquicia de hamburguesas como La Pepita pide 250.000 € para un local de 140 m², y las franquicias del sector van de 200.000 a 300.000 €.',
  },
  {
    q: '¿Es rentable el negocio de las hamburguesas?',
    a: 'No te prometemos rentabilidad: depende de tu local, de tu ticket y de lo que llenes cada día. Lo que sí hace el plan es enseñarte la cuenta con honestidad. En el caso medido por el Excel (95 comensales equivalentes al día: unos 53 en sala, y cada pedido para llevar o a domicilio cuenta como 1,7; a 16,00 € por comensal sin IVA, 300 días al año, unos 456.000 € de ventas) el beneficio neto del primer año queda en 46.512 €, el 10,2 % de las ventas, con la plantilla y tu propio sueldo ya dentro, y los costes se cubren con unos 73 comensales equivalentes al día. El food cost del plan es un 28 % prudente, aunque el escandallo teórico de la calculadora dé un 24,4 %: la diferencia, unos 4 puntos, es lo que se pierde entre la receta y la caja. Tienes tres escenarios (el pesimista, con 359.900 € de ventas y 2.441 € de pérdidas, incluido) para ver qué pasa con un año flojo, y todo se recalcula cuando cambias el ticket, los comensales o el alquiler.',
  },
  {
    q: '¿Cuántas hamburguesas salen de 1 kg de carne?',
    a: 'De 1 kg de carne picada salen 10 bolas de 100 g, es decir, 5 hamburguesas dobles (o 11 bolas de 90 g). Con la merma de las bolas que se tiran al cierre, la calculadora cuenta unas 9,7. La hoja Carne hace la cuenta con tus gramos (pesa 10 bolas y usa la media), te da el coste por kilo útil (9,18 € en el ejemplo, estimación del kit, editable), el de cada bola y el de la smash simple, la doble y la triple, y te dice cuánta carne necesitas al día: unos 15,2 kg para los 95 comensales equivalentes del caso. En el escandallo del ejemplo la simple cuesta 1,80 € (el 22,2 % del precio sin IVA) y la doble, 2,90 € (el 26,8 %).',
  },
  {
    q: '¿Qué carne se usa para una smash burger?',
    a: 'Lo habitual en el oficio es un blend de vacuno con una grasa de en torno al 20 %, que es lo que da la costra en la plancha. Puedes comprarlo ya picado o picarlo tú en el local, y la norma cambia según el caso. Si lo compras picado, hazlo a un proveedor autorizado y con su ficha técnica, y recuerda que la carne picada se mantiene a 2 °C o menos. Si picas en el local, el picado se hace con arreglo a las necesidades del despacho diario y no puede conservarse de un día para otro (art. 7.2 del RD 1021/2022), con carne sin recortes y respetando los plazos del Reglamento 853/2004. Y nada de «dry aged burger»: según Madrid Salud (Inf26008), no se puede elaborar carne picada con carne madurada más de quince días. La calculadora compara las dos vías, comprar el blend picado o picar una pieza en el local, y te dice hasta cuántos euros por kilo te compensa limpiar y picar.',
  },
  {
    q: '¿Puedo servir la hamburguesa poco hecha?',
    a: 'En España no existe una temperatura legal de cocción de la hamburguesa. Lo que hay es una recomendación de la AESAN: cocinar los alimentos hechos con carne picada completamente, a una temperatura de 70 °C o más durante al menos 2 minutos. Qué haces tú lo decide tu APPCC, con su punto de control y su sonda, y si la etiqueta de tu proveedor dice que la carne hay que cocinarla, no se usa para consumo crudo. La ventaja del formato es que una bola aplastada de 100 g en una plancha muy caliente sale hecha; el riesgo está en la hamburguesa gruesa «al punto». El checklist lo trae como punto de control con su registro, y la calculadora te lo recuerda en la hoja Instrucciones.',
  },
  {
    q: '¿Qué dice la ley de la freidora y del aceite?',
    a: 'Hay dos normas que sí puedes aplicar. El Reglamento (UE) 2017/2158 (acrilamida) pide para las patatas fritas, en su anexo II parte A, que las temperaturas al freír sean inferiores a 175 °C, que la patata se almacene por encima de 6 °C, que la fresca se deje en remojo y se enjuague, que la congelada se fría con las instrucciones del fabricante y que el personal tenga a la vista una guía de colores. Y la Orden de 26 de enero de 1989 fija que el contenido de componentes polares del aceite sea inferior al 25 % y prohíbe añadir al baño sustancias ajenas al aceite. No obliga a un medidor concreto: tu APPCC elige tiras, un medidor o un cambio por frecuencia. En una hamburguesería lo práctico son dos freidoras, una para las patatas y otra para los rebozados, y no prometer «patatas sin gluten» si comparten aceite. La calculadora incluye el coste del aceite por ración (en el ejemplo, unos 0,05 €).',
  },
  {
    q: '¿Qué licencias necesito?',
    a: 'En el IAE, una hamburguesería con sala va en el grupo 671 (restaurantes) y la que es solo barra y mostrador, en el 673; si los pedidos para llevar y a domicilio fueran la actividad principal, sería el 677.9, y eso lo decide tu gestoría. La apertura se tramita por el régimen municipal (licencia o declaración responsable, según tu ordenanza), con la consulta urbanística previa sobre el uso, la salida de humos a cubierta, la potencia y el aforo antes de firmar, a lo que se suma el registro sanitario de tu comunidad autónoma. Si la plancha es de gas, la instalación la hace una empresa habilitada, con su certificado y su revisión periódica. El plan lo recoge en un checklist de 80 tareas, pero qué te exigen exactamente en tu municipio, compruébalo con tu ayuntamiento y con tu asesoría antes de firmar el alquiler. Y una nota de IVA: la comida va al 10 %, también para llevar y a domicilio, pero la cerveza y los refrescos con azúcares o edulcorantes añadidos, también los zero, que salen del local van al 21 %.',
  },
  {
    q: '¿Cuánto se lleva Glovo, Uber Eats o Just Eat?',
    a: 'Las comisiones publicadas van del 13 al 35 % más IVA según la plataforma y el contrato, y el plan parte de un 30 % editable que ajustas al tuyo. En el caso, la plataforma pesa el 24 % de las ventas y las comisiones suman 32.832 € al año. Por eso el plan trabaja el escandallo por canal: el ticket de una persona en sala es de 17,00 € con IVA, el pedido para recoger en el local sale a 29,10 € y el de la plataforma, con la carta un 15 % más cara, a 33,47 €. En el menú de doble, patatas y bebida, el margen es de 10,83 € en sala, 10,38 € para llevar y 7,41 € en plataforma: casi un tercio menos. La burger viaja bien, las patatas no, y la calculadora lo tiene en cuenta con la caja y la bolsa de cada canal.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Hamburguesería Smash» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, la «carne picada» es «carne molida» en México, Colombia, Perú y Chile, las «patatas fritas» son «papas fritas» o «papas a la francesa», el «batido» es «malteada» en México y Colombia, el «pan de patata» es «pan de papa» en Argentina y Chile, y el pedido «a domicilio» se dice «delivery» en Argentina, Chile y Perú y «domicilios» en Colombia. Ojo: el marco legal del plan es el español (en México, por ejemplo, el SAT, el RFC o la licencia de funcionamiento no están cubiertos, y la norma de la carne picada y la de la fritura son otras). Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
  {
    q: '¿Y una franquicia de hamburguesas?',
    a: 'Es otra cuenta. Según emprendedores.es, La Pepita Burger Bar pide 250.000 € para un local de al menos 140 m², con un canon de entrada de 30.000 € y un 4,5 % más un 1,5 % de royalty y publicidad, y las franquicias del sector se mueven entre 200.000 y 300.000 €. La franquicia trae marca, proveedores, formación y carta a cambio del canon y la cuota, y suele pedir un local más grande. Este plan es el de una marca propia en un local de 90 m², con 162.144 € de inversión en el caso, y el Word razona las dos cuentas para que decidas con números. Las cifras de franquicia sirven para comparar, no para copiarlas en un local de otro tamaño.',
  },
  {
    q: '¿Y un carrito o un food truck de hamburguesas?',
    a: 'Es otro negocio: un remolque, un carrito o un puesto en mercados y eventos tiene otros permisos, otra cuenta de resultados y otra logística. Este plan es el de una hamburguesería con local fijo y alquilado, con su sala, su plancha a la vista y sus pedidos para llevar y a domicilio. Si lo tuyo es el carrito o el food truck de smash, mira el Plan de Negocio: Food Truck de nuestro catálogo, que parte de la cuenta del vehículo.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-hamburgueseria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_HAMBURGUESERIA',

  seo: {
    title: 'Plan de Negocio Hamburguesería Smash — Excel, Word y Calculadora | AI Chef Pro',
    description:
      'Plan de negocio para montar una hamburguesería de smash burgers con sala, para llevar y a domicilio: plan financiero en Excel de 9 hojas, plan en Word de 10 secciones, checklist de apertura de 80 tareas y calculadora de la carne, las patatas y el escandallo por canal. 35 €, pago único.',
    keywords:
      'plan de negocio hamburguesería, cómo montar una hamburguesería, montar una hamburguesería smash, cuánto cuesta montar una hamburguesería, negocio de hamburguesas, hamburguesería smash, smash burger, hamburguesas a domicilio, carne para smash burger, cuántas hamburguesas salen por 1 kg de carne, franquicia hamburguesería, escandallo hamburguesa, plan financiero hamburguesería excel, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Hamburguesería Smash',
    productDescription:
      'Plan de negocio para abrir una hamburguesería de smash burgers de barrio con plancha a la vista, mostrador de pedidos, sala, para llevar y a domicilio, en un local alquilado de 90 m² con 36 plazas. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 80 tareas, una calculadora de la carne, las patatas y el escandallo por canal (coste por kilo útil de la carne, bolas por kilo, patata congelada o fresca y food cost y margen de 14 productos en sala, para llevar y en plataforma) y la Guía de Equivalencias para Latinoamérica. Caso base de 95 comensales equivalentes al día con 16,00 € por comensal sin IVA, 300 días al año y unos 456.000 € de ventas. No es un curso de cocina ni asesoría legal, y no promete rentabilidad.',
    price: '35.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Hamburguesería Smash',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-plancha.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-carne.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-patatas.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-plancha.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-carne.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-patatas.jpg',
      '/lovable-uploads/ai-gallery/plan-hamburgueseria-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-hamburgueseria-carne.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-hamburgueseria-plancha.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-hamburgueseria-hero.jpg',
  },

  hero: {
    badge: 'La carne y el canal son el negocio: monta tu hamburguesería sabiendo cuánto te cuesta cada bola y cuánto te deja cada pedido',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Hamburguesería Smash',
    titleSubtitle: 'Cómo montar una hamburguesería de smash burgers con sala, para llevar y a domicilio',
    description:
      'El plan para abrir una hamburguesería de smash burgers de barrio con plancha a la vista, mostrador de pedidos, sala pequeña, para llevar y a domicilio, en un local alquilado: la inversión por partidas, la carne picada con su norma, la freidora con su norma, el delivery con su comisión y el margen de cada menú por canal. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones, checklist de apertura de 80 tareas, calculadora de la carne, las patatas y el escandallo, y la Guía de Equivalencias para Hispanoamérica como bonus.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Calculadora de la carne, las patatas y el escandallo: cuántas bolas salen de un kilo, el coste de la smash simple y de la doble, la patata congelada o la fresca y el margen de 14 productos en sala, para llevar y en plataforma',
      'Plan de negocio en Word (10 secciones) y checklist de apertura de 80 tareas',
      'La carne picada (RD 1021/2022) y la freidora (acrilamida y aceite), con la norma vigente y sin mitos',
      'Delivery por plataforma frente a la recogida en el local, con una comisión del 30 % editable',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      'Es el plan de una hamburguesería smash: sus números, sus trámites, su carne y su fritura. No es un curso de cocina ni un recetario, y no sustituye a tu asesoría ni al proyecto técnico del local.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias el ticket, los comensales o el alquiler y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Proyecto técnico, obra, conducto de extracción a cubierta, instalaciones, plancha (una de 60 a 80 cm va de unos 771 a 1.399 €), freidoras, mesa refrigerada, campana, utillaje, mobiliario, TPV, licencias, marca, stock inicial e imprevistos, más la fianza, la renta previa, el fondo de maniobra y el IVA de la inversión. En el caso, 104.350 € en partidas, 162.144 € de inversión y 184.057 € de necesidad de caja; todo editable para tu local.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos comensales equivalentes al día necesitas para cubrir costes (en el caso, unos 73 de los 95 previstos) y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo.' },
      { icon: 'Calculator', title: 'Calculadora de la Carne, las Patatas y el Escandallo', desc: 'Cuatro hojas: la carne (coste por kilo útil del blend comprado picado y de la pieza que picas en el local, bolas de 100 g por kilo y kilos al día), las patatas (congelada frente a fresca, con el aceite por ración), el escandallo de 14 productos con su food cost y su margen en sala, para llevar y en plataforma, e instrucciones. En el ejemplo, 10 bolas de 100 g por kilo (5 dobles), la smash doble a 2,90 € y un food cost teórico ponderado del 24,4 % sobre el precio sin IVA: estimación del kit, editable.' },
      { icon: 'Beef', title: 'La Carne Picada, con su Norma', desc: 'Carne picada a 2 °C o menos; si picas en el local, del día y nunca de un día para otro (art. 7.2 del RD 1021/2022); la bola sin sal es carne picada y salada pasa a preparado de carne; y nada de carne madurada más de quince días (Madrid Salud, Inf26008). Sin temperatura legal de cocción: la AESAN recomienda 70 °C o más durante al menos 2 minutos y lo decide tu APPCC.' },
      { icon: 'Flame', title: 'Freidora: Acrilamida y Aceite', desc: 'Patatas fritas por debajo de 175 °C, con la guía de colores a la vista (Reglamento UE 2017/2158), y aceite con menos del 25 % de componentes polares (Orden de 1989). Dos freidoras, una para las patatas y otra para los rebozados, y ninguna promesa de «sin gluten».' },
      { icon: 'Truck', title: 'Delivery y Para Llevar', desc: 'La comisión de la plataforma (un 30 % en el caso), la caja y la bolsa y el recargo de precio frente a la recogida en el local, con el 24 % de las ventas del caso en plataforma. En el menú de doble, patatas y bebida, el margen cae de 10,83 € en sala (10,38 € para llevar) a 7,41 € en plataforma: casi un tercio menos. Y el IVA del 21 % de la cerveza y los refrescos con azúcares o edulcorantes añadidos cuando salen del local.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con las variantes del formato (solo delivery, hamburguesa gourmet con servicio de mesa y carrito), las franquicias frente a la marca propia, los alérgenos de la hamburguesa y los errores más frecuentes.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución; local, humos y gas; carne, fritura y sanidad; personal y alérgenos; carta, marca y delivery; apertura y primeros 90 días. Con responsable, plazo y nota en cada tarea.' },
      { icon: 'Globe', title: 'Guía de Equivalencias para Hispanoamérica', desc: 'Vocabulario, impuestos, sanidad, normas laborales, licencias y unidades de 20 países, para adaptar el plan a tu mercado. Incluida como bonus.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de una hamburguesería smash, con su carne, su plancha y su freidora.',
    reasons: [
      { icon: 'Calculator', title: 'La Bola Es la Unidad del Negocio', desc: 'Cuánto cuesta de verdad una smash simple o una doble, con el kilo útil de la carne, los gramos de la bola y la caja del pedido, casi nadie lo mide. La calculadora te enseña a medirlo bola a bola y canal a canal, con supuestos del kit editables.' },
      { icon: 'Beef', title: 'La Carne Picada y la Freidora, con la Norma Vigente', desc: 'La carne picada tiene norma dentro del restaurante (RD 1021/2022): 2 °C o menos, del día y nunca de un día para otro si la picas tú. Y la freidora tiene dos: menos de 175 °C para la patata y menos del 25 % de polares en el aceite. El plan y el checklist te lo ponen por escrito antes de abrir.' },
      { icon: 'Euro', title: 'El IVA de la Bebida para Llevar', desc: 'Para llevar o a domicilio, la cerveza y los refrescos con azúcares o edulcorantes añadidos, también los zero, tributan al 21 %, no al 10 %. En la cuenta es poco dinero, pero es IVA que Hacienda te reclama si lo cobras al 10 %: el Excel lo trae ya partido.' },
      { icon: 'Scale', title: 'Una Cuenta Honesta, no una Promesa', desc: 'Con tu sueldo y la plantilla ya dentro, un food cost prudente del 28 % (el escandallo teórico da un 24,4 %), tres escenarios (el pesimista, con pérdidas) y la plataforma de delivery frente a la recogida en el local, con una comisión del 30 % que ajustas a tu contrato. Para decidir con números, no con promesas.' },
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
      'Además del plan financiero, el plan en Word, el checklist y la calculadora de la carne y las patatas, te llevas un extra — valorado en €15',
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
    headingGold: 'Hamburguesería',
    subtitle:
      'Antes de firmar el local y de encargar la plancha, ten las cuentas, los trámites, la norma de la carne y el margen de cada menú por canal sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes y tres escenarios (pesimista, realista y optimista)',
      'Calculadora de la carne, las patatas y el escandallo',
      'Consulta urbanística y humos antes de firmar el local; licencia y APPCC, antes de abrir',
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

  stickyLabel: 'PLAN HAMBURGUESERÍA — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-hamburgueseria', label: 'Kit de Tareas Recurrentes: Hamburguesería' },
    { href: '/guia-dark-kitchen', label: 'Guía Cómo Montar una Dark Kitchen' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/plan-negocio-food-truck', label: 'Plan de Negocio: Food Truck' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · noviembre 2026',

  alreadyBought: {
    product: 'plan-negocio-hamburgueseria',
    label: '¿Ya compraste el Plan de Negocio: Hamburguesería Smash? Vuelve a entrar al dashboard',
  },
};

export default data;
