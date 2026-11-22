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
//  - CERO cifras de mercado sin fuente revisada. La comparación con el software
//    de haddock y tspoonlab (más de 1.100 €/año) se quitó de la landing el
//    2026-11-22: no se volvió a comprobar.
//  - `95` y `32` son TOKENS: se sustituyen por las páginas MEDIDAS
//    con PyMuPDF cuando el PDF esté construido (D17). No publicar con el token puesto.
import type { GuiaData } from './types';

const faqs: GuiaData['faqs'] = [
    { q: '¿Qué es el food cost de un restaurante?', a: 'Es la parte del precio de un plato que se va en materia prima. Se mira en porcentaje, sobre el precio de venta sin IVA, y en euros de margen por ración. El porcentaje de la casa es una media: cada plato se mira aparte.' },
    { q: '¿Cómo se calcula el food cost de un plato?', a: 'Con esta fórmula: food cost % = coste de materia prima / precio de venta sin IVA × 100. Ejemplo: un coste de 4,50 € y un precio sin IVA de 15,00 € dan un food cost del 30 %. Esos 15,00 € salen de un precio de carta de 16,50 € con un 10 % de IVA de sala (16,50 / 1,10). El tipo del ejemplo es el del servicio en el local; en para llevar y en delivery puede ser otro.' },
    { q: '¿Qué es la ingeniería de menú?', a: 'Clasificar cada plato según cuántas raciones vende y cuánto deja cada una, en euros. El método de Kasavana y Smith cruza popularidad y margen de contribución. Las raciones salen del TPV y el coste, del escandallo.' },
    { q: '¿Qué es la matriz BCG de una carta?', a: 'La matriz BCG original ordena productos por crecimiento del mercado y por cuota. En la carta se usa la misma rejilla de cuatro casillas con otros ejes: popularidad y margen de contribución. Los grupos son estrella, caballo de batalla, puzzle y perro.' },
    { q: '¿Qué se revisa en cada cuadrante?', a: 'La estrella se protege: receta, porción y sitio en la carta. El caballo de batalla se vende mucho y deja poco: se revisan coste, guarnición o precio. El puzzle deja dinero y se pide poco: se revisan nombre, texto y lugar. El perro es candidato a salir, salvo que cumpla otra función en la carta.' },
    { q: '¿Hace falta el escandallo antes de la matriz?', a: 'Sí. El margen de cada plato sale del coste de la ración. En AI Chef Pro ese coste se trabaja en escandallos con IA (aichef.pro/escandallos-restaurante-ia) y la clasificación, en la página de carta e ingeniería de menú (aichef.pro/carta-menu-restaurante-ia). Se usan uno detrás de otro: pasas tú el coste y las ventas de un paso al siguiente.' },
    { q: '¿La guía incluye la suscripción de AI Chef Pro?', a: 'La guía son 55 EUR, un pago único. La suite se contrata aparte: AI Chef Miembro, 10 € al mes y 10.000 créditos; Premium Pro, 25 € y 85.000; Premium Plus, 50 € y 175.000; Premium Max, 95 € al mes o 950 € al año. No hay plan gratis ni prueba. Los precios están en aichef.pro/precios.' },
    { q: '¿Necesito el Kit de Escandallos si compro esta guía?', a: 'Puedes trabajar con la ficha de escandallo y el test de rendimiento que trae la guía. El Kit son 13 plantillas para escandallar por formato de negocio. Si tienes los dos, se solapan esas dos herramientas básicas y el resto es distinto: la guía sigue en el precio, la matriz y la decisión plato a plato.' },
    { q: '¿Cómo afecta el IVA al cálculo del food cost?', a: 'El food cost se calcula sobre la venta neta (la base imponible) y con el coste neto de IVA soportado, porque el IVA de la compra se deduce: es tesorería, no coste. El tipo cambia según vendas en sala, para llevar o por delivery. Calcularlo sobre el precio con IVA mueve el porcentaje y puede llevarte a subir el plato equivocado.' },
    { q: '¿Las bebidas alcohólicas llevan el 21 % en un restaurante?', a: 'Cuando se sirven en sala, el servicio de hostelería para consumir en el acto va al 10 %, alcohol incluido (art. 91.Uno.2.2.º de la Ley 37/1992). El 21 % aparece cuando no hay servicio: una bebida alcohólica vendida para llevar o por delivery es una entrega de bienes y sale del tipo reducido. La guía trae la matriz por canal y tipo de producto, y en los Excel vive en casillas editables.' },
    { q: '¿Cómo calculo el food cost de un plato vendido por delivery?', a: 'Sumando al coste del plato el packaging que le corresponde por pedido y dividiendo entre lo que ingresas: el precio menos la comisión de la plataforma. El simulador de la guía lo hace por plato y marca si el precio necesario cabe bajo el techo de la app.' },
    { q: '¿El objetivo de las bebidas es el mismo que el de la comida?', a: 'La estructura de coste de la bodega es otra: la unidad de venta (copa, media botella, botella) la decides tú y el despiece no pesa igual. El libro de bebidas deja el objetivo de cada categoría en una casilla editable, para que pongas el tuyo.' },
    { q: '¿Con qué frecuencia hay que re-escandallar una receta?', a: 'Cuando cambia la tarifa de un proveedor, la temporada, el formato de compra, la receta o la ración, y en una revisión de la carta completa. El capítulo 18 fija el protocolo.' },
    { q: '¿Kasavana y Smith es el único método de la guía?', a: 'Es el cruce de popularidad y margen de contribución, el de la matriz BCG de la carta. La guía añade Miller, Pavesic y el Goal Value de Hayes y Huffman sobre la misma carta, con una hoja que marca dónde discrepan.' },
    { q: '¿Qué es el prime cost?', a: 'Es la suma del coste de producto y el coste de personal, con su seguridad social. Un food cost bajo puede convivir con un exceso de horas que se come el margen. El cuadro de mando los pinta juntos mes a mes, con el objetivo en una casilla editable.' },
    { q: '¿Incluye actualizaciones?', a: 'El acceso es de por vida. Si cambia un tipo de IVA o una herramienta, la versión nueva se descarga desde el mismo acceso, sin otro pago.' },
    { q: '¿Hay garantía de devolución?', a: '30 días. Si la guía no te sirve, se devuelve el 100 % del pago.' },
    { q: '¿Sirve fuera de España?', a: 'El bloque fiscal está escrito con la normativa española y sus artículos citados. Los tipos de IVA, las comisiones y los objetivos viven en casillas editables de los Excel. Incluye la Guía de Equivalencias (20 países): «escandallo» es «costeo de recetas» en México y «receta estándar» en Colombia; «ración» es «orden» en México y «porción» en Colombia.' },
    { q: '¿Con qué programas funcionan las herramientas Excel?', a: 'Con Microsoft Excel, Google Sheets, LibreOffice y Apple Numbers. Están hechas sin funciones que rompan la compatibilidad y traen los valores calculados guardados en el fichero.' },
  ];

const data: GuiaData = {
  slug: 'guia-food-cost-ingenieria-menu',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_FOOD_COST',

  seo: {
    title: 'Food cost e ingeniería de menú: matriz BCG de carta | AI Chef Pro',
    description: 'Cómo se calcula el food cost de un plato, qué mira la ingeniería de menú y cómo se lee la matriz BCG de la carta. Guía con Excel, 55 EUR. Desde 10 € al mes.',
    keywords: 'food cost, ingeniería de menú, matriz BCG carta, menu engineering, food cost restaurante, margen de contribución, estrella caballo de batalla puzzle perro, kasavana smith, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-food-cost-ingenieria-menu.jpg',
  },

  showCompatibleApps: true,

  hero: {
    badge: 'Guía de pago único para quien ya tiene la carta en marcha',
    titlePre: 'Food cost e ',
    titleGold: 'ingeniería de menú',
    subtitleLine: 'La matriz BCG de la carta, con el cálculo del plato delante',
    description: 'Cómo se saca el food cost de una ración, en qué se separa del margen en euros y cómo cae cada plato en estrella, caballo de batalla, puzzle o perro. La guía trae el método y ocho Excel. El escandallo con IA y la ingeniería de menú de la suite van aparte, agente por agente.',
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
    bonusTotalLabel: 'Incluido en el precio: la guía, las 8 herramientas Excel y los dos bonus: ejercicios resueltos y la Guía de Equivalencias para tu país',
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
    subtitle: 'Cada capítulo se apoya en una de las ocho herramientas Excel del pack. El food cost, el precio y la matriz BCG de la carta se leen con esas hojas. Consultor gastronómico desde 2010.',
    chapters: [
      { icon: 'Users', num: '01', title: 'Para Quién Es Esta Guía (y Qué No Vas a Encontrar Aquí)', desc: 'Nivel de partida, mapa problema → capítulo → herramienta, y el glosario ES/LATAM: escandallo (costeo de recetas), coste (costo), carta (menú).' },
      { icon: 'BarChart3', num: '02', title: 'Las Cuatro Cifras Que Gobiernan tu Carta', desc: 'Food cost %, margen de contribución en euros, prime cost y ticket medio. Cuál manda en cada decisión y por qué mirar solo una engaña.' },
      { icon: 'Scale', num: '03', title: 'IVA, Base Imponible y el Error Que Invalida tu Food Cost', desc: 'La matriz de IVA por canal y tipo de producto, el cálculo sobre venta neta y un plato de ejemplo con y sin impuesto.' },
      { icon: 'Banknote', num: '04', title: 'El Coste Real de Compra: 4 %, 10 % y 21 % en el Mismo Albarán', desc: 'Qué compras van a cada tipo (el aceite de oliva ya no está donde crees), IVA soportado por partida y por qué el IVA de compra es tesorería, no coste.' },
      { icon: 'TrendingDown', num: '05', title: 'Del Bruto al Neto: Merma, Rendimiento y el Test Que Sustituye a la Tabla', desc: 'Despiece, cocción y desperdicio. El protocolo del test de rendimiento con tu proveedor y el coste neto por kilo con subproductos aprovechados.' },
      { icon: 'FileSpreadsheet', num: '06', title: 'La Ficha de Escandallo Que Aguanta una Auditoría', desc: 'Cantidad bruta a partir de la neta y la merma, raciones, coste por ración y precio objetivo. Qué debe llevar una ficha para que nadie la discuta.' },
      { icon: 'Search', num: '07', title: 'Food Cost Teórico vs Real: Dónde Se Escapa el Dinero', desc: 'La fórmula del real con stock inicial, compras y stock final; las cuatro causas de desviación y el protocolo semanal para cazarlas.' },
      { icon: 'Target', num: '08', title: 'Prime Cost: la Métrica Que Mide la Salud del Negocio', desc: 'Producto y personal juntos. Un food cost bajo puede convivir con un coste de personal que se come el margen. El objetivo del formato va en una casilla editable.' },
      { icon: 'Calculator', num: '09', title: 'Cuatro Formas de Poner Precio a un Plato', desc: 'Factor sobre coste, margen en euros, precio de mercado y valor percibido. Cuándo usar cada una y por qué el factor arruina los platos de coste alto.' },
      { icon: 'Sparkles', num: '10', title: 'Psicología de Precios: lo Demostrado y lo Que Es Leyenda', desc: 'Qué se puede usar al poner un precio (anclaje, orden, el plato que hace de referencia) y qué conviene no copiar de oídas.' },
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
    titlePre: '¿Por qué esta guía de ',
    titleGold: 'food cost',
    reasons: [
      { icon: 'Scale', title: 'El IVA, Dentro del Cálculo', desc: 'El food cost se calcula sobre la base imponible, y el tipo cambia según vendas en sala, para llevar o por delivery. Aquí está resuelto con la base legal citada y en casillas editables, no escondido dentro de una fórmula.' },
      { icon: 'Shuffle', title: 'Cuatro métodos sobre la misma carta', desc: 'Kasavana y Smith, Miller, Pavesic y Goal Value, con una hoja que enseña dónde discrepan. Cada método mira una pareja de variables distinta.' },
      { icon: 'FileSpreadsheet', title: 'Ocho Excel con Fórmulas Vivas', desc: 'Metes tus datos y calculan. Compatibles con Excel, Google Sheets y Numbers, con IVA, comisiones y objetivos en casillas editables para trabajar también fuera de España.' },
      { icon: 'Wallet', title: 'Un Pago Único, la Suite Aparte', desc: 'La guía son 55 EUR, una vez, con acceso de por vida. La suite de agentes se contrata en la página de precios: AI Chef Miembro sale a 10 € al mes, con 10.000 créditos. El escandallo y la matriz se usan uno detrás de otro.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. Consultor gastronómico desde 2010.',
    badge3: 'Consultor desde 2010',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX, recibes 8 herramientas Excel con fórmulas vivas y dos bonus: los ejercicios resueltos y la Guía de Equivalencias para tu país',
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
      { icon: 'GraduationCap', label: 'BONUS 1', title: '12 Ejercicios Resueltos', value: 'Incluido en el pack', desc: 'Doce casos con enunciado, datos, resolución paso a paso, tabla y lectura del resultado: merma, IVA por canal, los cuatro métodos de precio, discrepancias entre matrices, delivery, copa contra botella y prime cost.', image: '/lovable-uploads/ai-gallery/guia-foodcost-hero.jpg' },
      { icon: 'Globe', label: 'BONUS 2', title: 'Guía de Equivalencias para tu país', value: 'Incluido en el pack', desc: 'Los términos de tu producto dichos país por país en 20 países, más una ficha de una página por país con impuestos, sanidad, normas laborales, licencias y unidades.', image: '/lovable-uploads/ai-gallery/es-guia-equivalencias.jpg' },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 55 EUR',
  },

  guarantee: {
    text: 'Si la guía no te sirve para poner precios y decidir tu carta con criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  faqs,


  cta: {
    heading: 'La guía de food cost y la matriz de la carta',
    subtitle: 'El método, las herramientas y los ejercicios para decidir tu carta con números delante.',
    items: [
      'Guía completa PDF + DOCX (20 capítulos, 95 páginas)',
      '8 herramientas Excel con fórmulas vivas',
      'Cuatro metodologías de ingeniería de menú y su hoja de discrepancias',
      'Simulador de sala, para llevar y delivery con IVA y comisiones',
      'Cuadro de mando de prime cost y plan de acción de 90 días',
      'Bonus: 12 ejercicios resueltos (32 páginas)',
      'BONUS: Guía de Equivalencias para tu país',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 55 EUR',
  },

  stickyLabel: 'GUÍA FOOD COST + INGENIERÍA DE MENÚ — 55 EUR',

  footerLinks: [
    { label: 'Escandallos con IA', href: '/escandallos-restaurante-ia' },
    { label: 'Carta e ingeniería de menú', href: '/carta-menu-restaurante-ia' },
    { label: 'Calculadora de food cost', href: '/calculadora-food-cost-restaurante' },
    { label: 'Precios', href: '/precios' },
    { label: 'Ingeniería de menú en el blog', href: '/blog/carta-restaurante-rentable-ingenieria-menu-ia' },
    { label: 'Errores de food cost', href: '/blog/8-errores-que-destruyen-el-food-cost-en-tu-restaurante' },
    { label: 'Kit de Escandallos Pro', href: '/kit-escandallos' },
    { label: 'Kit Gestión de Personal', href: '/kit-gestion-personal' },
    { label: 'Guía Restaurante Gastronómico', href: '/guia-restaurante-gastronomico' },
    { label: 'Manual del Manager de Restaurante', href: '/manual-manager-restaurante' },
    { label: 'Manual del Chef Ejecutivo', href: '/manual-chef-ejecutivo' },
    { label: 'Cómo Montar una Pastelería', href: '/guia-pasteleria-obrador' },
    { label: 'Cómo Montar una Chocolatería Boutique & Atelier', href: '/guia-chocolateria-obrador' },
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
    productDescription: 'Guía para calcular el food cost de cada plato, leer la ingeniería de menú y clasificar la carta con la matriz BCG: estrellas, caballos de batalla, puzzles y perros. 20 capítulos, 8 Excel y 12 ejercicios resueltos. Pago único de 55 EUR, aparte de la suscripción de AI Chef Pro.',
    price: '55.00',
    priceValidUntil: '2026-12-31',
    faqs,
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Guía Food Cost + Ingeniería de Menú', item: 'https://aichef.pro/guia-food-cost-ingenieria-menu' },
    ],
  },
};

export default data;
