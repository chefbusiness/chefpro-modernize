// astro-site/src/data/productos/planes/plan-negocio-sushi-bar.ts
// LÍNEA PLANES (sub-línea A "planes de negocio") — producto NUEVO, versión 1.0 (noviembre 2026), 35 €.
// Landing NATIVA. Molde: plan-negocio-polleria.ts (sin testimonios, 35 €, local fijo).
// Fuentes: scripts/productos-digitales/plan-sushi/{F0-mapa-keywords-es-en.md, F1-camino.md (§4, §5), F1-research-sushi.md
//   (§0, §1, §4, §5, §6), cifras_caso_es.json, F2-NOTAS.md (§4, §8), REVISION-FINAL.md}. Cada cifra, contrastada con los
//   entregables de dl/plan-negocio-sushi-bar/ (F3-NOTAS.md §3).
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Plan de Negocio: Sushi Bar» (H1, schema.productName, catálogo, hub, breadcrumb). «Restaurante de
//    sushi» (México 3.600, España 1.900) va en el subtítulo, la meta y las keywords, nunca en el H1.
//  · SIN año fijo en title/meta/H1 (AGENTS.md: si algún día lleva año, token {year}).
//  · SIN `priceOld`, `discountBadge`, `aggregateRating`, `reviews` ni `testimonials` (producto recién nacido; la clave
//    `testimonials` se OMITE por completo: la plantilla pinta marquee con 5 estrellas si es un objeto).
//  · Cifras de la landing: SOLO las MEDIDAS del caso (cifras_caso_es.json y la calculadora de dl/) y las estables (5 ficheros,
//    9 hojas, 10 secciones, 80 tareas, 4 hojas y 14 productos en la calculadora). NADA de DSCR, payback, saldos de tesorería ni
//    importe del préstamo. Calculadora: siempre «estimación del kit, editable». Food cost siempre sobre el precio SIN IVA.
//  · Lo que arregló la revisión de la F2 (REVISION-FINAL.md M1, m10, m13): sin «combinado de 24 + extra = 27 €»; la regla del
//    21 % ENTERA (cerveza, sake, vino y refrescos con azúcares o edulcorantes añadidos que salen del local); lomo comprado a
//    24,16 €/kg útil; plataforma 24 % (no 25-26 %); en plataforma el margen del combinado cae MÁS DE UN CUARTO (no «a la mitad»);
//    food cost teórico 16 % frente al 29 % prudente del plan (no «20-22 %»).
//  · LEGAL (R §1): anisakis = art. 8 del RD 1021/2022 (el RD 1420/2006 solo como DEROGADO; nunca «7 días»; −18 °C solo para
//    decir que no sirve); shari a temperatura ambiente SOLO por el art. 30.5 del RD 1086/2020 (ningún pH ni tiempo legal: el 4,6
//    es el límite crítico del Kit de Tareas); pescado fresco 0-4 °C (art. 4.1 RD 1021/2022); IAE 671/673 y 677.9; IVA 10 % de la
//    comida. Nada de «sin gluten» prometido ni de «sushi grade» como garantía.
//  · CRIPTO: nada que tocar (la plantilla monta las puertas si cryptoEnabledFor('plan-negocio-sushi-bar')).
//
// IMÁGENES (alt descriptivos; la plantilla las pinta con alt=""):
//   hero ........ sushi bar de barrio con la barra de madera, la vitrina refrigerada del pescado, taburetes y mesas
//   barra ....... manos del itamae formando un nigiri de salmón en la barra
//   pescado ..... salmón entero, lomos y bloques de atún en la zona de limpieza del pescado
//   arroz ....... shari aliñándose en el hangiri, con la arrocera y las hojas de nori
//   delivery .... bandejas de sushi cerradas y bolsas listas para recoger y repartir
//   equipo ...... el itamae y el sushiman en la barra durante el servicio, de espaldas
//   plan ........ plan de negocio, portátil y calculadora sobre la barra del sushi bar cerrado
import type { PlanNegocioData, PlanNegocioFaq } from './types';

// Las 10 FAQ (research §6 + la del remolque de la SPEC + la de Latinoamérica). Una sola fuente: el acordeón de la página y el
// FAQPage del JSON-LD deben coincidir.
const FAQS: PlanNegocioFaq[] = [
  {
    q: '¿Cuánto cuesta montar un sushi bar?',
    a: 'Depende del local, de la salida de humos, del frío y de la barra, que son las partidas que más mueven la cuenta. En el caso del plan (un local alquilado de 95 m² con 36 plazas, 8 de ellas en la barra de sushi, y el 24 % de las ventas por plataforma) salen unos 103.400 € en partidas de obra, equipos, licencias, marca y stock inicial, imprevistos incluidos, y unos 185.400 € de necesidad total de caja una vez sumados la fianza, la renta previa, el fondo de maniobra de tres meses y el IVA de la inversión. Son cifras de ejemplo: el Excel trae la inversión por partidas (obra con la barra, conducto de extracción, vitrina refrigerada de sushi, arroceras y hangiri, congelador de −20 °C, cocina caliente, frío, mobiliario, TPV, marca, imprevistos…) todas editables para que pongas las tuyas y veas cuánto necesitas tú. Como referencia, según emprendedores.es, una franquicia de quiosco para llevar pide 39.950 € más la obra y una de restaurante de 180 m², unos 300.000 €.',
  },
  {
    q: '¿Es rentable un sushi bar? ¿Cuánto deja de ganancia?',
    a: 'No te prometemos rentabilidad: depende de tu local, de tu ticket y de lo que llenes cada día. Lo que sí hace el plan es enseñarte la cuenta con honestidad. En el caso medido por el Excel (79 comensales equivalentes al día: unos 45 en sala, y cada pedido para llevar o a domicilio cuenta como 1,6; a 20,00 € de ticket sin IVA, 300 días al año, unos 474.000 € de ventas) el beneficio neto queda en torno al 9-10 % de las ventas, con la plantilla y tu propio sueldo ya dentro, y los costes se cubren con unos 65 comensales al día. El food cost del plan es un 29 % prudente, aunque el escandallo teórico de la calculadora dé un 16 %: la diferencia es la merma de la vitrina, el sobrepeso de neta y de shari, lo que se tira al cierre y las comidas del personal. Tienes tres escenarios (el pesimista, con pérdidas, incluido) para ver qué pasa con un año flojo, y todo se recalcula cuando cambias el ticket, los comensales o el alquiler.',
  },
  {
    q: '¿Cuántos sushis salen con 1 kilo de arroz?',
    a: 'Con los supuestos del kit (estimación editable), un kilo de arroz crudo da unos 2,42 kg de shari, el arroz ya aliñado con vinagre, azúcar y sal, y con 20 g de shari por pieza salen unos 121 nigiris. En los rollos depende del tamaño: un uramaki de 8 piezas lleva unos 120 g de shari y un hosomaki de 6 piezas, unos 70 g. La hoja Arroz de la calculadora hace la cuenta con tus gramos (pesa 10 bolas y usa la media), te da el coste del shari y del nori de cada pieza y te dice cuánto arroz crudo necesitas al día: en el caso, unos 4,9 kg para 79 comensales (5,2 kg contando lo que se tira al cierre).',
  },
  {
    q: '¿Cuánto gana un sushiman?',
    a: 'Las ofertas de sushiman o sushiwoman de los portales de empleo van de 12.000 a 22.000 € brutos al año, muchas a media jornada, y las de un omakase de Ibiza parten de 2.500 € al mes. En el caso del plan, el sushiman cobra 1.650 € brutos al mes en 14 pagas, y tú, como itamae (el jefe de barra) y gerente, 2.200 €. El sueldo depende del convenio provincial de hostelería y de tu ciudad: la hoja Personal te deja poner los tuyos y ver qué le hacen a la cuenta. Y un consejo del plan: contrata al itamae antes de la obra y no dependas de uno solo, porque si falta no abre la barra.',
  },
  {
    q: '¿Qué dice la ley del anisakis?',
    a: 'La norma vigente es el art. 8 del RD 1021/2022 (el RD 1420/2006 está derogado desde el 22 de diciembre de 2022). El pescado que se sirve crudo o casi crudo se congela a −20 °C o menos en la totalidad del producto durante al menos 24 horas, o a −35 °C o menos durante al menos 15 horas, en tu local o antes, con su documento. La acuicultura queda exenta solo si el proveedor acredita por escrito que está libre de parásitos; el pescado salvaje y el atún se congelan. Y hay que informar al cliente en la carta o con un cartel. Un congelador que solo llega a −18 °C no sirve. El checklist lo trae como punto de control crítico, con su registro por lote, y la calculadora te lo recuerda en la hoja Pescado.',
  },
  {
    q: '¿Puedo tener el arroz del sushi a temperatura ambiente?',
    a: 'Solo si lo justificas. Las comidas preparadas siguen el art. 30 del RD 1086/2020, en la redacción del RD 1021/2022, y su apartado 5 deja al operador fijar otras temperaturas si demuestra a la autoridad sanitaria que se basan en evidencias científicas. Esa es la única vía del shari a temperatura ambiente: tu APPCC lo justifica, con el pH de cada tanda y un tiempo máximo, y lo demuestras a sanidad; si no, refrigerado. Ninguna norma española fija un pH ni un tiempo para el arroz de sushi: el pH de 4,6 o menos es el límite crítico del APPCC del Kit de Tareas Recurrentes: Sushi Bar, que trae la hoja para registrarlo, no una cifra legal.',
  },
  {
    q: '¿Qué licencias necesito, y qué IVA lleva el sushi para llevar?',
    a: 'En el IAE, la sala con comedor y servicio de mesa va en el grupo 671 (restaurantes) y la barra sin comedor separado, en el 673; si los pedidos para llevar y a domicilio fueran la actividad principal, sería el 677.9, y eso lo decide tu gestoría. La apertura se tramita por el régimen municipal (licencia o declaración responsable, según tu ordenanza), con la consulta urbanística de la extracción y el aforo antes de firmar, a lo que se suma el registro sanitario de tu comunidad autónoma. En cuanto al IVA, la comida va al 10 %, también para llevar y a domicilio, pero la cerveza, el sake, el vino y los refrescos con azúcares o edulcorantes añadidos que salen del local van al 21 %. Las temperaturas tienen su norma: el pescado fresco, entre 0 y 4 °C (RD 1021/2022, art. 4.1); las comidas preparadas, el art. 30 del RD 1086/2020 en la redacción del RD 1021/2022. El plan lo recoge en un checklist de 80 tareas, pero qué te exigen exactamente en tu municipio, compruébalo con tu ayuntamiento y con tu asesoría antes de firmar el alquiler.',
  },
  {
    q: '¿Y una franquicia de sushi?',
    a: 'Es otra cuenta. Según emprendedores.es, una franquicia de quiosco para llevar como Sushimore pide 39.950 € más la obra; Miss Sushi, desde 200.000 € en 120 m², con un canon de 29.000 €, y Sibuya, unos 300.000 € en 180 m², con un canon de 30.000 € y un 4 % más un 1 % de royalty y publicidad. La franquicia trae marca, proveedores, formación y carta a cambio del canon y la cuota, y suele pedir un local más grande. Este plan es el de una marca propia en un local de 95 m², y el Word razona las dos cuentas para que decidas con números. Las cifras de franquicia sirven para comparar, no para copiarlas en un local de otro tamaño.',
  },
  {
    q: '¿Y un puesto de sushi en un mercadillo o un remolque?',
    a: 'Es otro negocio: un remolque o un puesto en mercados y eventos tiene otros permisos, otra cuenta de resultados y otra logística, y con pescado crudo el frío y el anisakis pesan todavía más. Este plan es el de un sushi bar con local fijo y alquilado. Si lo tuyo es el remolque, mira el Plan de Negocio: Food Truck de nuestro catálogo, que parte de la cuenta del vehículo.',
  },
  {
    q: '¿Sirve en México, Colombia, Argentina y el resto de Latinoamérica?',
    a: 'Sí. Su contenido parte del marco profesional de España, que aporta rigor, y se adapta con facilidad. Con «Plan de Negocio: Sushi Bar» recibes la Guía de Equivalencias para tu país, con 20 países: vocabulario, impuestos, normas sanitarias, aspectos laborales, licencias y unidades. Por ejemplo, el «aguacate» del uramaki es «palta» en Argentina y Chile, el «langostino» de la tempura es «camarón» en México y Colombia, el «camarero» es «mesero» en México y Colombia y «mozo» en Argentina, y el pedido «a domicilio» se dice «delivery» en Argentina, Chile y Perú. Ojo: el marco legal del plan es el español (en México, por ejemplo, el SAT, el RFC o la licencia de funcionamiento no están cubiertos, y la norma del pescado crudo es otra). Si prefieres que lo adaptemos a la normativa de tu país, también lo hacemos como servicio: escríbenos a info@aichef.pro.',
  },
];

const data: PlanNegocioData = {
  slug: 'plan-negocio-sushi-bar',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_PLAN_SUSHI_BAR',

  seo: {
    title: 'Plan de Negocio Sushi Bar y Restaurante de Sushi — Excel, Word y Calculadora | AI Chef Pro',
    description:
      'Plan de negocio para montar un sushi bar o restaurante de sushi con barra, para llevar y a domicilio: plan financiero en Excel de 9 hojas, plan en Word de 10 secciones, checklist de apertura de 80 tareas y calculadora del pescado, el arroz y el escandallo. 35 €, pago único.',
    keywords:
      'plan de negocio sushi bar, plan de negocio sushi, cómo montar un sushi bar, como montar un sushi bar, montar restaurante de sushi, negocio de sushi, restaurante de sushi, cuánto cuesta abrir un sushi bar, es rentable un negocio de sushi, sushi a domicilio, sushi para llevar, cuántos sushis salen con 1 kilo de arroz, sushiman, itamae, anisakis, escandallo sushi, plan financiero sushi bar excel, AI Chef Pro',
    ogImage: 'https://aichef.pro/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg',
  },

  schema: {
    productName: 'Plan de Negocio: Sushi Bar',
    productDescription:
      'Plan de negocio para abrir un sushi bar de barrio con barra de sushi a la vista, mesas, para llevar y a domicilio, en un local alquilado de 95 m² con 36 plazas. Incluye un plan financiero en Excel de 9 hojas con fórmulas vivas (supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, instrucciones y financiación), un plan de negocio en Word de 10 secciones, un checklist de apertura de 80 tareas, una calculadora del pescado, el arroz y el escandallo (coste por kilo útil del pescado, nigiris por kilo de arroz y food cost y margen por canal de 14 productos) y la Guía de Equivalencias para Latinoamérica. Caso base de 79 comensales equivalentes al día con 20,00 € de ticket sin IVA, 300 días al año y unos 474.000 € de ventas. No es un curso de cocina ni asesoría legal, y no promete rentabilidad.',
    price: '35.00',
    priceValidUntil: '2027-12-31',
    faqs: FAQS,
    breadcrumbName: 'Plan de Negocio: Sushi Bar',
  },

  images: {
    // hero bg (6)
    gallery: [
      '/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-pescado.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-arroz.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-equipo.jpg',
    ],
    // strip del ContentGrid (6) — DIFIERE del hero (sale -hero, entra -plan; distinto orden)
    gridGallery: [
      '/lovable-uploads/ai-gallery/plan-sushi-bar-barra.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-plan.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-pescado.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-delivery.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-arroz.jpg',
      '/lovable-uploads/ai-gallery/plan-sushi-bar-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/plan-sushi-bar-pescado.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/plan-sushi-bar-barra.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/plan-sushi-bar-hero.jpg',
  },

  hero: {
    badge: 'El pescado y el arroz son el negocio: monta tu sushi bar sabiendo cuánto te cuesta cada pieza en cada canal',
    titlePre: 'Plan de Negocio: ',
    titleGold: 'Sushi Bar',
    titleSubtitle: 'Cómo montar un sushi bar o restaurante de sushi con barra, para llevar y a domicilio',
    description:
      'El plan para abrir un sushi bar de barrio con barra de sushi a la vista, mesas, para llevar y a domicilio, en un local alquilado: la inversión por partidas, el anisakis y el shari con su norma, el delivery con su comisión y el coste de cada pieza por canal. Plan financiero en Excel de 9 hojas con fórmulas vivas, plan de negocio en Word de 10 secciones, checklist de apertura de 80 tareas, calculadora del pescado, el arroz y el escandallo, y la Guía de Equivalencias para Hispanoamérica como bonus.',
    checkItems: [
      'Plan financiero en Excel de 9 hojas: cambias un supuesto y todo se recalcula, con la tesorería mes a mes',
      'Calculadora del pescado, el arroz y el escandallo: el kilo útil del salmón y del atún, cuántos nigiris salen de un kilo de arroz y el margen de 14 productos en sala, para llevar y en plataforma',
      'Plan de negocio en Word (10 secciones) y checklist de apertura de 80 tareas',
      'El anisakis (RD 1021/2022, art. 8) y el shari a temperatura ambiente (art. 30.5 del RD 1086/2020), con la norma vigente y sin mitos',
      'Delivery por plataforma frente a la recogida en el local, con una comisión del 30 % editable',
      'Acceso inmediato + actualizaciones de por vida',
    ],
    ctaLabel: 'DESCARGAR PLAN DE NEGOCIO — €35',
  },

  grid: {
    subtitle:
      'Es el plan de un sushi bar: sus números, sus trámites, su pescado y su arroz. No es un curso de sushi ni un recetario, y no sustituye a tu asesoría ni al proyecto técnico del local.',
    templates: [
      { icon: 'FileSpreadsheet', title: 'Plan Financiero en Excel (9 hojas)', desc: 'Supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería mes a mes, financiación e instrucciones. Fórmulas vivas: cambias el ticket, los comensales o el alquiler y el libro se recalcula solo.' },
      { icon: 'Coins', title: 'Inversión Inicial por Partidas', desc: 'Proyecto técnico, obra con la barra de sushi a la vista, conducto de extracción a cubierta, instalaciones, vitrina refrigerada de sushi, arroceras y hangiri, congelador de −20 °C con registrador, cocina caliente, frío, utillaje, mobiliario, TPV, licencias, marca, stock inicial e imprevistos, más la fianza, la renta previa, el fondo de maniobra y el IVA de la inversión. En el caso, unos 103.400 € en partidas y unos 185.400 € de necesidad total de caja; todo editable para tu local.' },
      { icon: 'TrendingUp', title: 'Punto de Equilibrio y Escenarios', desc: 'Cuántos comensales al día necesitas para cubrir costes (en el caso, unos 65 de los 79 previstos) y tres escenarios —pesimista, realista y optimista— para ver qué pasa con un año flojo.' },
      { icon: 'Calculator', title: 'Calculadora del Pescado, el Arroz y el Escandallo', desc: 'Cuatro hojas: el pescado (coste por kilo útil del salmón entero, del lomo comprado limpio y del atún en saku, y si te compensa limpiar el entero), el arroz (shari por kilo de arroz crudo, nigiris por kilo y arroz del día), el escandallo de 14 productos con su food cost y su margen en sala, para llevar y en plataforma, e instrucciones. En el ejemplo, 14,29 € el kilo útil del salmón entero y 24,16 € el del lomo comprado, 121 nigiris por kilo de arroz crudo y un food cost teórico del 16 % sobre el precio sin IVA: estimación del kit, editable.' },
      { icon: 'Fish', title: 'Anisakis y Shari, con su Norma', desc: 'El pescado que se sirve crudo se congela a −20 °C o menos en todo el producto durante al menos 24 horas, o a −35 °C o menos durante al menos 15 (RD 1021/2022, art. 8), salvo la acuicultura con documento escrito del proveedor, y se informa al cliente en la carta o con un cartel. El shari solo puede estar a temperatura ambiente si tu APPCC lo justifica ante sanidad (art. 30.5 del RD 1086/2020); si no, refrigerado. Con la norma vigente, sin mitos y sin «sushi grade».' },
      { icon: 'Truck', title: 'Delivery y Para Llevar', desc: 'La comisión de la plataforma (un 30 % en el caso), el envase y el recargo de precio frente a la recogida en el local, con el techo del 24 % de las ventas del caso. En plataforma, el margen del combinado de 24 piezas cae más de un cuarto: de 22,16 € en sala (21,76 € para llevar) a 16,12 €. Y el IVA del 21 % de la cerveza, el sake, el vino y los refrescos con azúcares o edulcorantes añadidos cuando salen del local.' },
      { icon: 'FileText', title: 'Plan de Negocio en Word (10 secciones)', desc: 'Resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción. Con el itamae (contratarlo antes de la obra), las variantes del formato (solo para llevar, omakase, kaiten y buffet libre), las franquicias frente a la marca propia, los alérgenos del sushi y los trece errores más frecuentes.' },
      { icon: 'ListChecks', title: 'Checklist de Apertura (80 tareas, 6 fases)', desc: 'Constitución; local, frío y extracción; pescado, arroz y sanidad; personal y alérgenos; carta, marca y delivery; apertura y primeros 90 días. Con responsable, plazo y nota en cada tarea.' },
      { icon: 'Globe', title: 'Guía de Equivalencias para Hispanoamérica', desc: 'Vocabulario, impuestos, sanidad, normas laborales, licencias y unidades de 20 países, para adaptar el plan a tu mercado. Incluida como bonus.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → SIN `testimonials` (ver cabecera: la clave se omite entera).

  why: {
    subtitle:
      'No es una plantilla genérica de restaurante. Es el plan de un sushi bar, con su pescado, su arroz y su barra.',
    reasons: [
      { icon: 'Calculator', title: 'La Pieza Es la Unidad del Negocio', desc: 'Cuánto cuesta de verdad un nigiri o un combinado, con el kilo útil del pescado, los gramos de shari y la caja del pedido, casi nadie lo mide. La calculadora te enseña a medirlo pieza a pieza y canal a canal, con supuestos del kit editables.' },
      { icon: 'Fish', title: 'El Anisakis y el Shari, con la Norma Vigente', desc: 'El RD 1420/2006 está derogado: la norma del anisakis es el art. 8 del RD 1021/2022, y el shari a temperatura ambiente solo cabe por el art. 30.5 del RD 1086/2020, si tu APPCC lo justifica. El plan y el checklist te lo ponen por escrito antes de abrir.' },
      { icon: 'Euro', title: 'El IVA de la Bebida para Llevar', desc: 'Para llevar o a domicilio, la cerveza, el sake, el vino y los refrescos con azúcares o edulcorantes añadidos tributan al 21 %, no al 10 %. En la cuenta es poco dinero, pero es IVA que Hacienda te reclama si lo cobras al 10 %: el Excel lo trae ya partido.' },
      { icon: 'Scale', title: 'Una Cuenta Honesta, no una Promesa', desc: 'Con tu sueldo y la plantilla ya dentro, un food cost prudente del 29 % (el escandallo teórico da un 16 %), tres escenarios (el pesimista, con pérdidas) y la plataforma de delivery frente a la recogida en el local, con una comisión del 30 % que ajustas a tu contrato. Para decidir con números, no con promesas.' },
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
      'Además del plan financiero, el plan en Word, el checklist y la calculadora del pescado y el arroz, te llevas un extra — valorado en €15',
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
    headingGold: 'Sushi Bar',
    subtitle:
      'Antes de firmar el local y de encargar la barra, ten las cuentas, los trámites, el anisakis y el coste de cada pieza por canal sobre la mesa.',
    items: [
      'Plan financiero en Excel de 9 hojas con fórmulas vivas',
      'Tesorería mes a mes y tres escenarios (pesimista, realista y optimista)',
      'Calculadora del pescado, el arroz y el escandallo',
      'Consulta urbanística y anisakis antes de firmar el local; licencia y shari, antes de abrir',
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

  stickyLabel: 'PLAN SUSHI BAR — €35',

  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-sushi-bar', label: 'Kit de Tareas Recurrentes: Sushi Bar' },
    { href: '/guia-restaurante-japones', label: 'Guía Restaurante Japonés' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/plan-negocio-taqueria', label: 'Plan de Negocio: Taquería' },
    { href: '/plan-negocio-hamburgueseria', label: 'Plan de Negocio: Hamburguesería Smash' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],
  updateNote: 'Producto nuevo · Versión 1.0 · noviembre 2026',

  alreadyBought: {
    product: 'plan-negocio-sushi-bar',
    label: '¿Ya compraste el Plan de Negocio: Sushi Bar? Vuelve a entrar al dashboard',
  },
};

export default data;
