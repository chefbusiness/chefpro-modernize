// guia-food-cost-ingenieria-menu.ts — LÍNEA GUÍAS, producto 45 (2026-09-03).
//
// Primer producto de la línea con landing NATIVA en Astro: no hay página SPA de la que
// portar copy. La fuente del copy es la SPEC firmada
// (scripts/productos-digitales/guia-food-cost-SPEC.md) y el research consolidado
// (scripts/productos-digitales/auditorias/guia-food-cost-RESEARCH-2026-09-03.md).
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  - D2: producto nuevo → SIN `priceOld` ni `discountBadge` (no existe «precio anterior
//    de 30 días»: art. 20 TRLGDCU / RDL 24/2021).
//  - D3: SIN `aggregateRating` y con `testimonials.items: []` — no ha vendido una unidad,
//    así que no hay reseñas. El template oculta la sección cuando el array está vacío.
//  - CERO cifras inventadas. La ÚNICA cifra de mercado admitida es el coste anual del
//    software de food cost (>1.100 € + IVA), tomada de las tarifas públicas de
//    haddock.app y tspoonlab.com consultadas el 2026-09-03 (research §3).
//  - `95` y `32` son TOKENS: se sustituyen por las páginas MEDIDAS
//    con PyMuPDF cuando el PDF esté construido (D17). No publicar con el token puesto.
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-food-cost-ingenieria-menu',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_FOOD_COST',

  seo: {
    title: 'Guía Food Cost + Ingeniería de Menú: Escandallo, Precios y Carta Rentable | AI Chef Pro',
    description: 'Escandallo (costeo de recetas), precios y rentabilidad de tu carta: guía de 95 páginas, 8 Excel con fórmulas y 12 ejercicios resueltos. IVA por canal y delivery. 55 EUR.',
    keywords: 'food cost, escandallo, costeo de recetas, ingeniería de menú, menu engineering, cómo calcular el food cost, precio de venta de un plato, kasavana smith, prime cost, beverage cost, food cost delivery, IVA hostelería, guía food cost, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-food-cost-ingenieria-menu.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'Para quien ya opera: poner precio y decidir la carta con números, no a ojo',
    titlePre: 'Guía Food Cost + ',
    titleGold: 'Ingeniería de Menú',
    subtitleLine: 'Escandallo, precios y rentabilidad de tu carta — con el IVA bien puesto y el delivery dentro de la cuenta',
    description: 'El Kit te dice cuánto te cuesta cada plato. La Guía te dice qué hacer con esa información: qué reformular, qué resubir, qué rediseñar y qué retirar, plato a plato y con el cálculo delante.',
    checkItems: [
      'Guía completa PDF + DOCX editable (20 capítulos, 95 páginas)',
      '8 herramientas Excel con fórmulas vivas: escandallo, mermas, precios, matriz de carta, delivery, bebidas, prime cost y plan de 90 días',
      'Cuatro metodologías de ingeniería de menú sobre la misma carta, y una hoja que enseña dónde discrepan',
      'El IVA por canal (sala, para llevar y delivery) dentro del cálculo, con la base legal citada',
      'Bonus: 12 ejercicios resueltos paso a paso (32 páginas)',
    ],
    ctaLabel: 'COMPRAR GUÍA — 55 EUR',
    avatarAltPrefix: 'Professional',
  },

  pricing: {
    price: '55 EUR',
    heroNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    buyBoxNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    bonusTotalLabel: 'Incluido en el precio: la guía, las 8 herramientas Excel y el bonus de ejercicios',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-cocina.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-bodega.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-delivery.jpg',
      '/lovable-uploads/ai-gallery/guia-foodcost-equipo.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-foodcost-cocina.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 8 Herramientas Excel + 12 Ejercicios Resueltos',
    subtitle: 'Método, no teoría. Cada capítulo se apoya en una de las ocho herramientas Excel del pack y sus tablas salen de las celdas de esos ficheros, no de ejemplos inventados. Escrito por un chef y consultor gastronómico que lleva desde 2010 poniendo precios en cartas reales.',
    chapters: [
      { icon: 'Users', num: '01', title: 'Para Quién Es Esta Guía (y Qué No Vas a Encontrar Aquí)', desc: 'Nivel de partida, mapa problema → capítulo → herramienta, y el glosario ES/LATAM: escandallo (costeo de recetas), coste (costo), carta (menú).' },
      { icon: 'BarChart3', num: '02', title: 'Las Cuatro Cifras Que Gobiernan tu Carta', desc: 'Food cost %, margen de contribución en euros, prime cost y ticket medio. Cuál manda en cada decisión y por qué mirar solo una engaña.' },
      { icon: 'Scale', num: '03', title: 'IVA, Base Imponible y el Error Que Invalida tu Food Cost', desc: 'La matriz de IVA por canal y tipo de producto, el cálculo sobre venta neta y un plato de ejemplo con y sin impuesto.' },
      { icon: 'Banknote', num: '04', title: 'El Coste Real de Compra: 4 %, 10 % y 21 % en el Mismo Albarán', desc: 'Qué compras van a cada tipo (el aceite de oliva ya no está donde crees), IVA soportado por partida y por qué el IVA de compra es tesorería, no coste.' },
      { icon: 'TrendingDown', num: '05', title: 'Del Bruto al Neto: Merma, Rendimiento y el Test Que Sustituye a la Tabla', desc: 'Despiece, cocción y desperdicio. El protocolo del test de rendimiento con tu proveedor y el coste neto por kilo con subproductos aprovechados.' },
      { icon: 'FileSpreadsheet', num: '06', title: 'La Ficha de Escandallo Que Aguanta una Auditoría', desc: 'Cantidad bruta a partir de la neta y la merma, raciones, coste por ración y precio objetivo. Qué debe llevar una ficha para que nadie la discuta.' },
      { icon: 'Search', num: '07', title: 'Food Cost Teórico vs Real: Dónde Se Escapa el Dinero', desc: 'La fórmula del real con stock inicial, compras y stock final; las cuatro causas de desviación y el protocolo semanal para cazarlas.' },
      { icon: 'Target', num: '08', title: 'Prime Cost: la Métrica Que Mide la Salud del Negocio', desc: 'Producto y personal juntos, con los umbrales del sector español según el formato. Un food cost «bueno» puede estar tapando un coste de personal roto.' },
      { icon: 'Calculator', num: '09', title: 'Cuatro Formas de Poner Precio a un Plato', desc: 'Factor sobre coste, margen en euros, precio de mercado y valor percibido. Cuándo usar cada una y por qué el factor arruina los platos de coste alto.' },
      { icon: 'Sparkles', num: '10', title: 'Psicología de Precios: lo Demostrado y lo Que Es Leyenda', desc: 'El efecto señuelo con estudio revisado por pares, los clásicos citados con sus salvedades y lo que circula por el sector sin ninguna evidencia detrás.' },
      { icon: 'LayoutGrid', num: '11', title: 'Ingeniería de Menú I: Kasavana & Smith Bien Hecho', desc: 'La matriz clásica como debe hacerse: umbral de popularidad por familia, margen de contribución y las cuatro categorías con su lectura.' },
      { icon: 'PieChart', num: '12', title: 'Ingeniería de Menú II: lo Que la Matriz Clásica No Ve', desc: 'Miller, Pavesic con margen ponderado y el Goal Value de Hayes y Huffman con su fórmula completa. Tres lecturas que la matriz 2×2 no da.' },
      { icon: 'Shuffle', num: '13', title: 'Cuando los Métodos Discrepan: el Protocolo de Decisión', desc: 'Qué mide realmente cada método, cómo leer la hoja de comparativa y el árbol de decisión: reformular, resubir, rediseñar o retirar.' },
      { icon: 'UtensilsCrossed', num: '14', title: 'Carta Corta, Menú de Precio Fijo, Buffet y Banquete', desc: 'Tamaño de carta y poda; en el precio fijo el margen lo decide el mix. Con epígrafe propio para hotel, buffet, banquete y catering.' },
      { icon: 'Truck', num: '15', title: 'Multicanal: Sala, Para Llevar y Delivery', desc: 'Comisión de plataforma, packaging por pedido, IVA por canal y precio techo en la app. Cuánto hay que subir en cada canal y qué platos no deberían estar.' },
      { icon: 'Wine', num: '16', title: 'Beverage Cost: la Bodega Como Cuenta de Resultados Propia', desc: 'Copa contra botella, barril, destilados y cócteles. Objetivos por categoría y el IVA correcto según se sirva en sala o se venda para llevar.' },
      { icon: 'Croissant', num: '17', title: 'Costeo por Lote en Obrador y Pastelería', desc: 'Rendimiento de tanda, mano de obra por hora, packaging y escalado. El método completo; la plantilla por formato la aporta el Kit de Escandallos.' },
      { icon: 'RefreshCw', num: '18', title: 'Cuando Sube el Proveedor: Protocolo de Re-escandallado', desc: 'Disparadores y calendario de revisión, cómo leer las notas de precios oficiales y cómo subir un precio sin perder al cliente.' },
      { icon: 'ClipboardList', num: '19', title: 'Caso Integral: una Carta Entera, de Principio a Fin', desc: 'Los doce platos de ejemplo del pack recorriendo ficha, matriz, precio objetivo, multicanal y plan de 90 días. Etiquetado como caso modelado.' },
      { icon: 'Cpu', num: '20', title: 'Cuándo tu Excel Se Queda Corto', desc: 'El criterio para saltar de Excel a software y de software a agentes de IA, con lo que gana y lo que cuesta cada salto.' },
    ],
  },

  // D3: producto recién lanzado, sin una sola venta → sin testimonios y sin
  // aggregateRating. El template oculta esta sección con items vacío.
  testimonials: {
    titleGold: '',
    subtitle: '',
    items: [],
  },

  why: {
    reasons: [
      { icon: 'Scale', title: 'El IVA, Dentro del Cálculo', desc: 'El food cost se calcula sobre la base imponible, y el tipo cambia según vendas en sala, para llevar o por delivery. Aquí está resuelto con la base legal citada y en casillas editables, no escondido dentro de una fórmula.' },
      { icon: 'Shuffle', title: 'Cuatro Métodos, No Uno', desc: 'Kasavana & Smith, Miller, Pavesic y Goal Value sobre la misma carta, con una hoja que enseña dónde discrepan y por qué. Cada método mide dos de tres variables: lo interesante no es que coincidan, es que no lo hagan.' },
      { icon: 'FileSpreadsheet', title: 'Ocho Excel con Fórmulas Vivas', desc: 'No son PDF para rellenar a mano: metes tus datos y calculan. Compatibles con Excel, Google Sheets y Numbers, con IVA, comisiones y objetivos en casillas editables para trabajar también fuera de España.' },
      { icon: 'Wallet', title: 'Un Pago Único Frente a una Cuota Mensual', desc: 'Un año de software de food cost cuesta más de 1.100 €, IVA aparte, según las tarifas públicas de haddock.app y tspoonlab.com consultadas el 3 de septiembre de 2026. Esta guía es un pago único con acceso de por vida.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes 8 herramientas Excel con fórmulas vivas y el bonus de ejercicios resueltos',
    layout: 'single',
    items: [
      { icon: 'FileSpreadsheet', label: 'HERRAMIENTA 1', title: 'Ficha de Escandallo Base', value: 'Incluido en el pack', desc: 'Veinte líneas de ingredientes con merma, cantidad bruta calculada, coste por ración y precio de venta objetivo con y sin IVA. El punto de partida de todo lo demás.', image: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg' },
      { icon: 'Scale', label: 'HERRAMIENTA 2', title: 'Rendimiento y Mermas por Producto', value: 'Incluido en el pack', desc: 'Test de rendimiento con subproductos aprovechables, merma de cocción por técnica y tu propia tabla de mermas medidas frente a las de referencia.', image: '/lovable-uploads/ai-gallery/guia-foodcost-cocina.jpg' },
      { icon: 'Calculator', label: 'HERRAMIENTA 3', title: 'Precio Objetivo Multi-Método', value: 'Incluido en el pack', desc: 'Quince platos con los cuatro métodos de fijación de precio en paralelo, el precio elegido según el método y el semáforo del food cost resultante.', image: '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg' },
      { icon: 'PieChart', label: 'HERRAMIENTA 4', title: 'Matriz Multi-Método de Carta', value: 'Incluido en el pack', desc: 'Veinticinco platos clasificados por Kasavana & Smith, Miller, Pavesic y Goal Value, con una hoja de comparativa que marca dónde discrepan y qué hacer.', image: '/lovable-uploads/ai-gallery/guia-foodcost-carta.jpg' },
      { icon: 'Truck', label: 'HERRAMIENTA 5', title: 'Simulador de Repricing Multicanal', value: 'Incluido en el pack', desc: 'Food cost efectivo por canal con comisión y packaging, precio necesario para el objetivo y aviso de si ese precio cabe bajo el techo de la app.', image: '/lovable-uploads/ai-gallery/guia-foodcost-delivery.jpg' },
      { icon: 'Wine', label: 'HERRAMIENTA 6', title: 'Carta de Bebidas y Beverage Cost', value: 'Incluido en el pack', desc: 'Vinos por copa y botella, barriles y botellines, destilados y cócteles con sus ingredientes. Coste, margen y beverage cost ponderado por categoría.', image: '/lovable-uploads/ai-gallery/guia-foodcost-bodega.jpg' },
      { icon: 'Target', label: 'HERRAMIENTA 7', title: 'Cuadro de Mando Prime Cost', value: 'Incluido en el pack', desc: 'Doce meses de food cost y coste de personal con seguridad social, prime cost mensual, semáforo frente a tu objetivo y gráfico de evolución.', image: '/lovable-uploads/ai-gallery/guia-foodcost-equipo.jpg' },
      { icon: 'CalendarRange', label: 'HERRAMIENTA 8', title: 'Plan de Acción 90 Días', value: 'Incluido en el pack', desc: 'Veinte decisiones con responsable, fecha e impacto estimado, calendario de trece semanas y KPI de seguimiento comparados con el mes cero.', image: '/lovable-uploads/ai-gallery/guia-foodcost-equipo.jpg' },
      { icon: 'GraduationCap', label: 'BONUS', title: '12 Ejercicios Resueltos', value: 'Incluido en el pack', desc: 'Doce casos con enunciado, datos, resolución paso a paso, tabla y lectura del resultado: merma, IVA por canal, los cuatro métodos de precio, discrepancias entre matrices, delivery, copa contra botella y prime cost.', image: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 55 EUR',
  },

  guarantee: {
    text: 'Si la guía no te sirve para poner precios y decidir tu carta con criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs: [
    { q: '¿Necesito el Kit de Escandallos si compro esta guía?', a: 'No, pero se complementan. El Kit son 11 plantillas para escandallar por formato de negocio; la Guía es el método y la decisión: qué precio poner, qué método usar y qué hacer con cada plato. La Guía incluye una ficha de escandallo base para que puedas trabajar sin el Kit; si ya lo tienes, no compras nada repetido.' },
    { q: '¿Sirve fuera de España?', a: 'Sí, con un matiz que conviene decir claro: el bloque fiscal está escrito con la normativa española y sus artículos citados. Los tipos de IVA, las comisiones de plataforma y los objetivos viven en casillas editables de los Excel, así que sustituyes los valores por los de tu país y todo se recalcula. El vocabulario incluye las equivalencias de Hispanoamérica (escandallo/costeo de recetas, coste/costo, carta/menú) y los ejemplos de delivery mencionan también las plataformas de México, Argentina, Uruguay y Panamá.' },
    { q: '¿Con qué programas funcionan las herramientas Excel?', a: 'Con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers. Los libros están construidos a propósito sin funciones que rompen la compatibilidad entre programas, y traen los valores calculados guardados dentro del fichero, así que también se ven bien en el móvil y en visores que no recalculan.' },
    { q: '¿Cómo afecta el IVA al cálculo del food cost?', a: 'Más de lo que parece, y es el hueco que casi ninguna fuente gratuita cubre. El food cost se calcula sobre la venta neta (la base imponible), no sobre el precio de la carta, y con el coste neto de IVA soportado, porque ese IVA de compra se deduce: es tesorería, no coste. Calcularlo sobre el precio con IVA infla o desinfla el porcentaje según el canal y te lleva a subir el plato equivocado.' },
    { q: '¿Las bebidas alcohólicas llevan el 21% en un restaurante?', a: 'No cuando se sirven en sala: el servicio de hostelería para consumir en el acto va al 10%, alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992). El 21% aparece cuando no hay servicio: una bebida alcohólica vendida para llevar o por delivery es una entrega de bienes y sale del tipo reducido. La guía trae la matriz completa por canal y tipo de producto, y en los Excel vive en casillas editables.' },
    { q: '¿Cómo calculo el food cost de un plato vendido por delivery?', a: 'Sumando al coste del plato el packaging que le corresponde por pedido y dividiendo entre lo que realmente ingresas, es decir, el precio menos la comisión de la plataforma. El simulador multicanal lo hace por ti para cada plato y además te dice qué precio necesitarías para cumplir tu objetivo y si ese precio cabe bajo el techo que la app te deja poner.' },
    { q: '¿Por qué el objetivo de las bebidas es distinto al de la comida?', a: 'Porque la estructura de coste no se parece: no hay merma de despiece, la unidad de venta se decide (copa, media botella, botella) y la rotación es otra. La guía da los rangos por categoría con su fuente y los deja en casillas editables del libro de bebidas, para que compares tu bodega con la referencia y no con una cifra genérica.' },
    { q: '¿Con qué frecuencia hay que re-escandallar una receta?', a: 'No por calendario ciego, sino por disparadores: cambio de tarifa de un proveedor, cambio de temporada o de formato de compra, cambio de receta o de ración, y una revisión periódica de la carta completa. El capítulo 18 fija el protocolo y explica cómo leer las notas de precios oficiales para anticiparte, en vez de enterarte con la factura.' },
    { q: '¿El método de Kasavana & Smith es el único válido?', a: 'Es el más citado, no el único, y por sí solo se queda corto: cruza popularidad con margen de contribución e ignora el porcentaje de coste. La guía lo hace bien y además añade Miller, Pavesic y el Goal Value de Hayes y Huffman sobre la misma carta, con una hoja que marca dónde discrepan. Ahí es donde suelen estar las decisiones que importan.' },
    { q: '¿Qué es el prime cost y por qué importa más que el food cost solo?', a: 'Es la suma del coste de producto y el coste de personal con su seguridad social. Importa porque son las dos partidas que se mueven con tu operativa, y porque un food cost estupendo puede estar sostenido por un exceso de horas que se come el margen. El cuadro de mando los pinta juntos mes a mes, con el objetivo del formato de tu negocio en una casilla editable.' },
    { q: '¿Incluye actualizaciones?', a: 'Sí, el acceso es de por vida. Si cambia un tipo de IVA o mejoramos una herramienta, entras a tu dashboard y descargas la versión nueva sin pagar nada. En el propio panel verás el historial de cambios de cada versión.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'Deja de Poner Precios a Ojo',
    subtitle: 'El método, las herramientas y los ejercicios para decidir tu carta con números delante.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 95 páginas)',
      '8 herramientas Excel con fórmulas vivas',
      'Cuatro metodologías de ingeniería de menú y su hoja de discrepancias',
      'Simulador de sala, para llevar y delivery con IVA y comisiones',
      'Cuadro de mando de prime cost y plan de acción de 90 días',
      'Bonus: 12 ejercicios resueltos (32 páginas)',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 55 EUR',
  },

  stickyLabel: 'GUÍA FOOD COST + INGENIERÍA DE MENÚ — 55 EUR',

  footerLinks: [
    { label: 'Kit de Escandallos Pro', href: '/kit-escandallos' },
    { label: 'Kit Gestión de Personal', href: '/kit-gestion-personal' },
    { label: 'Guía Restaurante Gastronómico', href: '/guia-restaurante-gastronomico' },
    { label: 'Todos los Productos', href: '/productos-digitales' },
    { label: 'Contacto', href: 'mailto:info@aichef.pro' },
  ],

  updateNote: 'Versión 1.0 · septiembre 2026',

  alreadyBought: {
    product: 'guia-food-cost-ingenieria-menu',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  schema: {
    productName: 'Guía Food Cost + Ingeniería de Menú',
    productDescription: 'Guía técnica de 20 capítulos para escandallar, poner precio y decidir la carta de un negocio de hostelería ya en marcha: IVA por canal, mermas medidas, cuatro metodologías de ingeniería de menú, delivery, beverage cost y prime cost. Incluye 8 herramientas Excel con fórmulas y 12 ejercicios resueltos.',
    price: '55.00',
    priceValidUntil: '2026-12-31',
    faqs: [
      { q: '¿Necesito el Kit de Escandallos si compro esta guía?', a: 'No. El Kit son plantillas para escandallar; la Guía es el método y la decisión, e incluye su propia ficha de escandallo base. Si tienes los dos, no hay contenido repetido.' },
      { q: '¿Sirve fuera de España?', a: 'Sí. El bloque fiscal está escrito con normativa española citada, pero los tipos de IVA, comisiones y objetivos viven en casillas editables de los Excel para adaptarlos a cualquier país.' },
      { q: '¿Con qué programas funcionan las herramientas Excel?', a: 'Con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers. Están construidas sin funciones que rompan la compatibilidad y traen los valores calculados guardados en el fichero.' },
      { q: '¿Cómo afecta el IVA al cálculo del food cost?', a: 'El food cost se calcula sobre la venta neta (base imponible) y con el coste neto de IVA soportado. El tipo cambia según vendas en sala, para llevar o por delivery; la guía trae la matriz por canal y producto.' },
      { q: '¿Cómo calculo el food cost de un plato vendido por delivery?', a: 'Sumando al coste del plato el packaging por pedido y dividiendo entre el precio menos la comisión de la plataforma. El simulador multicanal lo calcula por plato y dice si el precio necesario cabe bajo el techo de la app.' },
      { q: '¿El método de Kasavana & Smith es el único válido?', a: 'No. Cruza popularidad con margen e ignora el porcentaje de coste. La guía añade Miller, Pavesic y el Goal Value de Hayes y Huffman sobre la misma carta, con una hoja que marca dónde discrepan.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Food Cost + Ingeniería de Menú', item: 'https://aichef.pro/guia-food-cost-ingenieria-menu' },
    ],
  },
};

export default data;
