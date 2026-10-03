// guia-churreria-chocolateria.ts — LÍNEA GUÍAS «Cómo Montar», producto 51 (2026-10-03).
//
// Landing NATIVA en Astro (no hay página SPA de la que portar copy). Fuentes del copy:
//   · scripts/productos-digitales/guia-churreria-SPEC.md (§0 ficha, §5 lista negra,
//     §6 vocabulario, §7.1 salientes, §8.1 fila 1, §8.3 correcciones de la FAQ)
//   · scripts/productos-digitales/auditorias/guia-churreria-RESEARCH-2026-10-03.md
//     (§12 nombre, promesa y vocabulario; §14 las 12 FAQ de compra)
//   · scripts/productos-digitales/guias-v2_0/guion_guia_churreria_chocolateria.py
//     (índice REAL: 17 capítulos, el último el anexo normativo; manda sobre los 19+anexo
//     de la SPEC) y los 8 xlsx de guia-churreria/build/.
//   Molde fichero a fichero: guia-chocolateria-obrador.ts (producto 49).
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · UN SOLO NOMBRE VISIBLE: «Cómo Montar una Churrería-Chocolatería», idéntico en el H1
//    (hero.titlePre + hero.titleGold), en schema.productName, en el name.es de
//    src/data/products-catalog.ts, en la tarjeta del hub y en los footerLinks cruzados.
//  · SIN `priceOld` ni `discountBadge`, SIN `aggregateRating`, SIN `review` y con
//    `testimonials.items: []`: producto nuevo, sin una sola venta. El ancla de precio, si
//    se usa, es SOLO el canon de franquicia publicado de 12.000 € (CUS-M15).
//  · SR-10 — no se han podido releer los anuncios de portales de clasificados: NINGUNA cifra que venga
//    de ahí (ni el curso, ni la renta del local, ni los traspasos) aparece en la ficha.
//    La maquinaria con precio publicado sí (sin IVA, y diciendo qué no incluye).
//  · Las páginas anunciadas de la guía y del bonus 2 son las MEDIDAS con PyMuPDF sobre el PDF
//    final (3-oct-2026); las verifica paginas-gate.py. El business plan es DOCX y NO publica
//    páginas.
//  · Nunca «verificado contra el BOE», «cumple la normativa» ni «quedarás legal»; ni
//    promesas de rentabilidad; ni «prueba gratis». Sin siglas (IAE, RGSEAA, APPCC, CTE) en
//    el hero ni en los titulares de capítulo.
//  · Declaración en negativo ARRIBA: no enseña a freír, no es un recetario ni un curso de
//    churrero y no sustituye al proyecto técnico de la extracción. La bombonería es otro
//    negocio y tiene su guía (/guia-chocolateria-obrador).
//  · §5 lista negra: ninguna temperatura de fritura, ningún tipo de IVA del chocolate a la
//    taza, ningún margen del 85-90 %, ninguna cifra de traspaso, ninguna cuota del IAE.
//  · CRIPTO: nada que tocar aquí. GuiaLandingPage.astro monta las tres puertas de
//    CryptoPayButton solas cuando `cryptoEnabledFor('guia-churreria-chocolateria')` da true.
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-churreria-chocolateria',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_CHURRERIA_CHOCOLATERIA',

  seo: {
    title: 'Cómo Montar una Churrería-Chocolatería | Guía y Excel',
    description: 'Para quien va a abrir una churrería-chocolatería en España: local, humos y aceite, coste de apertura, licencias y escandallo del churro. 16 capítulos, anexo y 8 Excel.',
    keywords: 'montar una churrería, cómo montar una churrería, cuánto cuesta montar una churrería, churrería rentable, licencia de churrería, maquinaria de churrería, churrera y dosificadora, porras, chocolate a la taza, traspaso de churrería, franquicia de churrería, escandallo del churro, aceite de fritura, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-churreria-chocolateria.jpg',
  },

  hero: {
    badge: 'Para quien AÚN no ha abierto: lo que hay que decidir antes de firmar nada',
    titlePre: 'Cómo Montar una ',
    titleGold: 'Churrería-Chocolatería',
    subtitleLine: 'Local, obrador de masa, freidora y números: el dossier completo de apertura de una churrería-chocolatería, con los Excel que hacen tus cuentas',
    description: 'No te enseña a freír. Te dice qué decidir y en qué orden: si ese local admite una freidora, cuánto cuesta abrir de verdad, a cuánto vender la ración y la taza, cuánta madrugada te toca y qué haces en verano. Cubre a fondo la churrería-chocolatería con obrador de masa y sala; el despacho para llevar y la caseta de feria entran como variantes. Si lo tuyo es la bombonería, es otro negocio y tiene su propia guía. El marco legal explicado es el español. Esto no es un recetario ni un curso de churrero, y no sustituye al proyecto técnico de la extracción.',
    checkItems: [
      'Guía completa PDF + DOCX: 16 capítulos y un anexo normativo con fecha de corte (95 páginas)',
      '8 herramientas Excel con fórmulas vivas: producción, hora punta y local; coste de apertura; carta y escandallo del churro; aceite de fritura; temporada, franjas y ferias; plan financiero a 3 años; checklist legal de fritura y licencias; y turnos, plantilla y madrugada',
      'Para quien ya tiene la bombonería en la cabeza: es otro negocio y tiene su guía aparte, la de Chocolatería Boutique & Atelier',
      'El marco legal explicado es el español, con su norma y el día en que se comprobó. Todas las casillas de los Excel son editables',
      'Bonus 1: el business plan modelo, relleno con el caso completo de «El Molinete», en DOCX editable',
      'Bonus 2: 12 decisiones de apertura resueltas (21 páginas)',
    ],
    ctaLabel: 'COMPRAR GUÍA — 65 EUR',
    avatarAltPrefix: 'Professional',
  },

  // Producto nuevo: sin priceOld ni discountBadge (no hay «precio anterior de 30 días»
  // que anclar sin incumplir el art. 20 de la Ley 7/1996).
  pricing: {
    price: '65 EUR',
    heroNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    buyBoxNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    bonusTotalLabel: 'Incluido en el precio: la guía, las 8 herramientas Excel y los dos bonus',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-churreria-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-churreria-1.jpg',
      '/lovable-uploads/ai-gallery/guia-churreria-2.jpg',
      '/lovable-uploads/ai-gallery/guia-churreria-3.jpg',
      '/lovable-uploads/ai-gallery/guia-churreria-4.jpg',
      '/lovable-uploads/ai-gallery/guia-churreria-5.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-churreria-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-churreria-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-churreria-4.jpg',
  },

  grid: {
    countGold: '17',
    headingRest: ' Capítulos + 8 Plantillas + 2 Bonus',
    subtitle: 'Criterio y decisión, no teoría. Cada capítulo se apoya en una de las ocho herramientas Excel del pack y sus tablas salen de las celdas de esos ficheros, no de ejemplos inventados: el caso es «El Molinete», una churrería-chocolatería modelada, sin ciudad ni dueños. Cierra un anexo normativo con fecha de corte, para que sepas qué estaba vigente el día que se escribió y qué fechas ya sabemos que se mueven. Escrito por un chef y consultor gastronómico que lleva desde 2010 acompañando aperturas.',
    chapters: [
      { icon: 'Layers', num: '01', title: 'Qué Negocio Estás Montando: Seis Formatos y Cuál te Toca', desc: 'Las seis formas de montar una churrería-chocolatería comparadas por inversión, metros y régimen de apertura, por qué la bombonería es otro negocio con su propia guía, el mapa de problema a capítulo y a herramienta, y el glosario con las equivalencias de Hispanoamérica.' },
      { icon: 'Users', num: '02', title: 'El Cliente, las Franjas y la Plaza', desc: 'Quién compra churros y a qué hora, cómo se reparte el día entre desayuno, merienda y madrugada del fin de semana, qué se sabe y qué no del número de churrerías que hay en España, y cómo leer la plaza antes de enamorarte de un local.' },
      { icon: 'Cookie', num: '03', title: 'La Carta de Apertura y el IVA de Cada Cosa', desc: 'Cómo se decide un surtido de apertura: churro, porra, chocolate a la taza y venta para llevar, qué papel juega cada familia en el ticket, y el IVA de lo que vendes y de lo que compras explicado una sola vez, para que los Excel de carta y de apertura lo apliquen bien.' },
      { icon: 'DoorOpen', num: '04', title: 'Antes de Firmar: el Formato Decide el Régimen de Apertura, las Obras y el Horario', desc: 'Por qué el despacho para llevar y el local con sala no se abren igual, qué obras necesitan proyecto aunque la actividad no necesite licencia previa, y qué dice la norma del horario de apertura de madrugada. Lo que hay que saber antes de firmar el alquiler.' },
      { icon: 'Wind', num: '05', title: 'Humos, Extracción y Fuego de Aceite: lo que Exige la Norma y lo que Fija el Proyecto', desc: 'Dónde acaba lo que la norma exige y dónde empieza lo que decide el técnico de tu proyecto: potencia de los aparatos, riesgo del local, extinción automática, conducto a cubierta, distancias del filtro y las preguntas exactas que llevarle al ingeniero. No sustituye al proyecto.' },
      { icon: 'Layout', num: '06', title: 'El Local y la Hora Punta: Metros, Conducto, Ficha de Visita y la Cola del Domingo', desc: 'Las zonas de un obrador de masa a la vista, cuántas raciones por hora aguanta tu línea, qué pasa en la cola del domingo y en Navidad y Reyes, y la ficha con la que se visita un local antes de enamorarse de él, con sus eliminatorios en orden.' },
      { icon: 'Wrench', num: '07', title: 'Maquinaria y Proveedores: Churrera, Dosificadora, Freidora, Chocolatera, Harina, Aceite, Envase y Gestor', desc: 'La escalera de equipos de la línea, qué necesita un despacho y qué una sala, cómo pedir presupuestos comparables, y los proveedores de harina o mix, aceite, chocolate, envase y recogida de aceite usado, con las preguntas que separan a quien compra de quien sabe lo que compra.' },
      { icon: 'Banknote', num: '08', title: 'Cuánto Cuesta Abrir, Partida a Partida', desc: 'El modelo que produce TU cifra de apertura: inversión por bloque y por formato, traspaso frente a obra nueva a cinco años, la columna de impuesto línea a línea, las partidas que ninguna fuente publica y cómo presupuestarlas, y el colchón de tesorería como partida y no como propina.' },
      { icon: 'FileText', num: '09', title: 'Alta Fiscal y Sanitaria de Cada Formato: Epígrafe, Código de Actividad y Registro', desc: 'Qué epígrafe te corresponde según vendas para tomar en sala, para llevar o en ferias, la pregunta exacta que hay que hacerle al asesor sobre el código de actividad, y el árbol del registro sanitario según a quién vendas.' },
      { icon: 'Droplets', num: '10', title: 'Aceite de Fritura: Calidad, Cambio, Coste y Gestor', desc: 'Cuánto te cuesta el aceite por ración entre lo que absorbe el producto y lo que tiras al cambiar la cuba, cuándo compensa cambiarlo, qué pasa cuando sube el precio y cómo se gestiona el aceite usado. El registro de calidad del aceite lo lleva tu plan de autocontrol.' },
      { icon: 'ClipboardCheck', num: '11', title: 'Autocontrol, Alérgenos, Acrilamida y el Día de la Inspección', desc: 'La carpeta que hay que tener el día que entra el inspector, los alérgenos de una carta de masa frita y chocolate, qué implica compartir aceite entre productos, dónde está la regulación de la acrilamida y por qué la norma está en revisión, y la formación del equipo.' },
      { icon: 'Calculator', num: '12', title: 'Escandallo del Churro y de la Porra: Rendimiento, Absorción y los Dos Márgenes', desc: 'El coste por kilo de masa, por ración, por docena y por taza; el aceite que absorbe la masa como coste de materia; y por qué dos márgenes que circulan entre churreros no se contradicen, sino que miden cosas distintas. Parte de tu receta y de tus gramos, no de una receta nuestra.' },
      { icon: 'UserCog', num: '13', title: 'El Equipo, los Turnos y la Madrugada', desc: 'Cuántas personas necesitas en la línea en el pico, cómo se cubre una madrugada, la diferencia entre el plus del convenio y el trabajador nocturno del Estatuto, el salto del salario al coste de empresa y cómo identificar el convenio que te toca a ti.' },
      { icon: 'CalendarRange', num: '14', title: 'La Temporada y las Ferias: de Octubre a Marzo, el Verano y las Casetas', desc: 'Cuánto pesa cada mes sobre el año, qué haces en julio y agosto con tres salidas comparadas en euros de contribución, y la caseta de feria como variante: punto muerto por evento, calendario, venta ambulante y cuándo te conviene mejor un food truck.' },
      { icon: 'Scale', num: '15', title: 'Franquicia o Independiente', desc: 'Lo que publican las enseñas de churrerías en canon, inversión y royalty, como orden de magnitud y con su fecha, y la tabla para compararlo con montar por tu cuenta. Sin recomendar marca: te da las preguntas que hay que hacerle a un franquiciador antes de firmar.' },
      { icon: 'Rocket', num: '16', title: 'El Plan Financiero, el Punto de Equilibrio y los Primeros Noventa Días', desc: 'Cuenta de resultados a tres años con estacionalidad mensual, punto de equilibrio en raciones al día con tu personal real, la tesorería con el valle del verano, qué canal paga los fijos y qué se mide en el mes cero y en el mes tres. Los veredictos van en euros, no por ratio.' },
      { icon: 'ScrollText', num: '17', title: 'Anexo Normativo, Actualizado a 3 de Octubre de 2026', desc: 'Qué estaba vigente el día que se escribió la guía, con su norma y su fecha de corte, y las cuestiones que ya sabemos que se mueven: la regulación de la acrilamida en revisión, el convenio, el registro horario y la facturación verificable.' },
    ],
  },

  // Producto recién nacido, sin una sola venta → sin testimonios y sin aggregateRating.
  // El template oculta esta sección con el array vacío.
  testimonials: {
    titleGold: '',
    subtitle: '',
    items: [],
  },

  why: {
    reasons: [
      { icon: 'Shuffle', title: 'Lo Que Se Decide Antes de Abrir', desc: 'Esta guía es todo lo que hay que decidir antes: si ese local admite una freidora, cuánto cuesta abrir de verdad, a cuánto vender la ración y la taza, cuánta madrugada te toca y qué haces en verano. No es una guía de bombonería: si lo tuyo es el bombón, es otro negocio y tiene la suya, con obrador y sin freidora. Y la freidora lo cambia todo: la licencia, los humos, el gas y el aceite.' },
      { icon: 'FileSpreadsheet', title: 'Ocho Herramientas Que Hacen Tus Cuentas', desc: 'Metes TUS metros, TU carta y TU precio de aceite y sale TU cifra, con la hipótesis escrita al lado. La capacidad de la línea y la cola del domingo, el coste del aceite por ración, qué hacer en verano con tres salidas comparadas en euros, y el cuadrante de la madrugada con sus dos figuras de nocturnidad. No existe nada igual en nuestro catálogo, porque ni el Kit de Escandallos ni la guía de Food Cost costean masa frita.' },
      { icon: 'ShieldCheck', title: 'Cada Dato Legal con su Norma y su Fecha', desc: 'Ninguna afirmación normativa va suelta: cada tabla lleva su norma y el día en que se comprobó, y el anexo final tiene fecha de corte con las cuestiones que ya sabemos que se mueven. Donde la norma no da una cifra, la guía no la inventa: te dice a quién preguntarla y con qué palabras. El marco explicado es el español; todas las casillas de los Excel son editables.' },
      { icon: 'AlertTriangle', title: 'Y Lo Que Esta Guía No Hace', desc: 'No te enseña a freír ni a hacer la masa: eso es oficio y se aprende al lado de un maestro. No sustituye al proyecto técnico de la extracción de humos ni a la gestión de licencias, que los firma un técnico. No te garantiza que tu ayuntamiento diga que sí, y no promete clientes ni rentabilidad. Lo que hace es que llegues a cada reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar, y que no firmes un alquiler antes de tiempo.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía en PDF y DOCX, recibes estas 10 piezas: las 8 herramientas Excel con fórmulas vivas y los dos bonus',
    // layout 'single' (rejilla única de 3 columnas con todas las tarjetas del mismo ancho):
    // el 'split' está pensado para 5 ítems (3+2) y con 10 dejaría 3 anchas y 7 estrechas.
    layout: 'single',
    items: [
      {
        icon: 'FileSpreadsheet',
        label: 'HERRAMIENTA 1',
        title: 'Producción, Hora Punta y Local',
        value: 'Incluido en el pack',
        desc: 'Zonas y metros, capacidad de la línea en raciones por hora, cuello de botella, freidoras con su potencia y su riesgo, día tipo y día punta, y ficha de visita al local con sus eliminatorios en orden. Decide si ese local sirve, y si te basta una churrera o necesitas dos.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-hero.jpg',
      },
      {
        icon: 'Banknote',
        label: 'HERRAMIENTA 2',
        title: 'Calculadora del Coste de Apertura',
        value: 'Incluido en el pack',
        desc: 'Inversión por bloque, equipamiento línea a línea, variante del formato (local con sala, despacho, caseta o franquicia), traspaso frente a obra nueva a cinco años y la columna de impuesto con su efecto en la tesorería. Decide cuánto necesitas de verdad y en qué formato.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-3.jpg',
      },
      {
        icon: 'Calculator',
        label: 'HERRAMIENTA 3',
        title: 'Carta de Apertura y Escandallo del Churro',
        value: 'Incluido en el pack',
        desc: 'Escandallo por kilo de masa, aceite absorbido, chocolate a la taza, coste de la hora de obrador, ración frente a docena o kilo, ticket por canal y temporada, y los dos márgenes juntos con su definición. Parte de tu receta y de tus gramos. Decide a cuánto vendes la ración, la docena y la taza.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-2.jpg',
      },
      {
        icon: 'Droplets',
        label: 'HERRAMIENTA 4',
        title: 'Aceite de Fritura: Coste y Cambio',
        value: 'Incluido en el pack',
        desc: 'Consumo y reposición, punto económico de cambio, escenarios de subida del precio del aceite y gestor de aceite usado. Decide cuánto te cuesta el aceite por ración y cuándo lo cambias. No es un registro de autocontrol: para eso están las plantillas del Pack APPCC.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-5.jpg',
      },
      {
        icon: 'CalendarRange',
        label: 'HERRAMIENTA 5',
        title: 'Temporada, Franjas y Ferias',
        value: 'Incluido en el pack',
        desc: 'Peso de cada mes sobre el año, demanda por franja del día, capacidad contra el pico, cola del domingo, refuerzo de Navidad y Reyes, las tres salidas del verano comparadas en euros y punto muerto por evento para ferias. Decide si cierras en verano y a qué ferias vas.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-4.jpg',
      },
      {
        icon: 'TrendingUp',
        label: 'HERRAMIENTA 6',
        title: 'Plan Financiero a 3 Años',
        value: 'Incluido en el pack',
        desc: 'Supuestos, inversión inicial, cuenta de resultados a tres años con estacionalidad mensual, punto de equilibrio en raciones al día, escenarios, personal, tesorería a doce meses, financiación y canales con su punto muerto. Decide si el banco te lo aguanta y qué canal paga los fijos.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-hero.jpg',
      },
      {
        icon: 'ClipboardCheck',
        label: 'HERRAMIENTA 7',
        title: 'Checklist Legal de Fritura y Licencias',
        value: 'Incluido en el pack',
        desc: 'Seis fases con contador de avance, la pregunta de si la extracción necesita proyecto como primera fila, epígrafes por formato, régimen de apertura y horario, licencia, humos y gas, registro sanitario, ferias y venta ambulante, alérgenos, formación y cronograma con ruta crítica. Decide qué papel te toca y en qué orden.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-3.jpg',
      },
      {
        icon: 'UserCog',
        label: 'HERRAMIENTA 8',
        title: 'Turnos, Plantilla y Madrugada',
        value: 'Incluido en el pack',
        desc: 'Cuadrante por franja, las dos figuras de nocturnidad en dos columnas por persona, coste anual por puesto con semáforo contra el salario mínimo, identificación de tu convenio y horas del titular. Decide cuánta gente necesitas y cuánto te cuesta abrir de madrugada. Para el cuadrante semana a semana, el Kit de Gestión de Personal.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-1.jpg',
      },
      {
        icon: 'ScrollText',
        label: 'BONUS 1',
        title: 'Business Plan Modelo, Relleno',
        value: 'Incluido en el pack',
        desc: 'El caso completo de «El Molinete» en el formato que pide un banco o una línea de financiación pública: resumen ejecutivo con el resultado neto y el punto de equilibrio dentro, mercado y plaza, concepto y carta, operaciones con fritura, capacidad y plantilla, plan financiero a tres años, tesorería con el valle del verano y riesgos con escenarios. En DOCX editable, con las cifras cuadradas contra el plan financiero del pack.',
        image: '/lovable-uploads/ai-gallery/guia-churreria-5.jpg',
      },
      {
        icon: 'GraduationCap',
        label: 'BONUS 2',
        title: '12 Decisiones de Apertura Resueltas',
        value: 'Incluido en el pack',
        desc: 'Doce decisiones reales con su contexto, sus opciones, el criterio, la celda del Excel que la resuelve y la norma con su fecha cuando la hay: sala o sólo despacho, traspaso u obra nueva, gas o eléctrico, mix propio o preparado comercial, ración, docena o kilo, abrir antes de las ocho, qué haces en verano, o franquicia o por tu cuenta. En PDF y en DOCX editable (21 páginas).',
        image: '/lovable-uploads/ai-gallery/guia-churreria-4.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te sirve para decidir tu local, tus números y tu papeleo con criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  // Las 12 FAQ de COMPRA del research §14, con las correcciones de SPEC §8.3 y SR-10:
  // la 1 con «ninguna de las que hemos leído»; la 3 sin cifra de curso; la 4 sin cifras de
  // traspaso y con la maquinaria sin IVA y lo que NO incluye; la 5 con los dos márgenes
  // atribuidos; la 6 sobre la receta; la 7 con la condición de obra; la 11 sin la
  // causalidad falsa de Sheets. Las de oficio y las de consumidor quedan fuera.
  faqs: [
    { q: '¿Esto no está gratis en Google?', a: 'Lo suelto sí está, pero las guías gratuitas que hemos leído se copian los mismos tramos, y ninguna de las que hemos leído desglosa el coste de apertura partida a partida, cuantifica la temporada o trata a fondo los humos y el aceite. Lo que no está en Google es el orden en el que se toman las decisiones y ocho Excel donde metes TUS metros, TU carta y TU precio de aceite y sale TU cifra, con la hipótesis escrita al lado.' },
    { q: '¿En qué se diferencia de la guía de Chocolatería Boutique & Atelier? ¿Necesito las dos?', a: 'Aquella es bombonería con obrador y sin freidora; esta es churro frito y chocolate a la taza, con freidora, y la freidora cambia la licencia, los humos, el gas y el aceite. Son dos negocios distintos y cada guía cubre el suyo. Si vas a hacer las dos cosas, se enlazan: cada una te dice dónde acaba y dónde empieza la otra.' },
    { q: '¿Me enseña a hacer churros?', a: 'No, y lo decimos antes de que pagues. Esta guía no es un recetario ni un curso de churrero: eso es oficio y se aprende al lado de un maestro. Para eso hay cursos presenciales de pago en Madrid. Lo que sí hace la guía es ayudarte a elegir uno, a pedir lo que importa en un traspaso con maestro saliente y a que las cuentas de tu churrería salgan antes de abrir.' },
    { q: '¿Cuánto cuesta montar una churrería?', a: 'No te damos un número: te damos el modelo que produce el tuyo, porque depende de tus metros, de tu plaza, del estado del local y de si abres con sala o sólo con despacho. Lo que sí traemos con precio publicado es la maquinaria núcleo: va de unos 4.200 € en un despacho a unos 8.600 € en un local con sala, sin IVA, y no incluye la obra de humos, la cafetera, la vitrina ni el TPV. Esas partidas que nadie publica las presupuestas tú en la calculadora, con las preguntas que hacer y la columna de impuesto línea a línea.' },
    { q: '¿Es rentable una churrería?', a: 'Te lo enseñamos con tus números, no con una promesa. Entre churreros circulan dos márgenes que parecen contradecirse: más del 60 % sobre materia prima, y algo más del 50 % que declara el gestor de La Artesana. No se contradicen, miden cosas distintas, y la guía te los da juntos con su definición. Después viene lo que decide: el punto de equilibrio en raciones al día con tu personal real. Un margen de foro no aguanta una nómina, y por eso el Excel calcula el tuyo.' },
    { q: '¿Los Excel parten de mi receta o de una receta vuestra?', a: 'De la tuya. El libro de escandallo parte de tu receta y de tus gramos por pieza, del precio de tu mix o de tu harina, y del rendimiento que te declare tu proveedor, y te da piezas, raciones y coste por kilo. No damos un «rendimiento de un kilo de harina» como dato, porque no hay una cifra pública fiable y depende de la receta y del gramaje. El caso de «El Molinete» está ahí como ejemplo relleno que sobrescribes con lo tuyo.' },
    { q: '¿Necesito licencia de apertura?', a: 'Depende del formato, y el checklist bifurca por ahí desde la primera fila. La actividad de un despacho para llevar hasta 750 m² va por declaración responsable; pero las obras de la salida de humos, si necesitan proyecto, van con su licencia y su técnico. Con mesas y consumo en el local, manda tu ayuntamiento. La guía no sustituye a la gestión de licencias: te dice qué papel te toca, en qué orden y qué preguntar.' },
    { q: '¿Sirve para un puesto de feria o un food truck?', a: 'La caseta de feria entra como variante, con su capítulo, su checklist y la hoja de punto muerto por evento, pero sin caso cifrado. Si vas a un vehículo-cocina, el Plan de Negocio Food Truck es tu producto, y la guía te remite a él.' },
    { q: 'Tengo una cafetería y quiero meter churros. ¿Me sirve?', a: 'Te sirve el capítulo de lo que cambia al meter una freidora en un local que no la tenía: humos, potencia, aceite y alérgenos. El negocio de cafetería lo cubren su plan de negocio y su kit; esta guía es para quien monta una churrería-chocolatería.' },
    { q: '¿Franquicia o por mi cuenta?', a: 'Hay un capítulo entero con lo que publican las enseñas, de unos pocos miles de euros a más de cien mil de inversión, con canon y royalty, como orden de magnitud y con su fecha, sin recomendar marca. Una de ellas publica un canon de entrada de 12.000 €: la guía cuesta el 0,54 % de ese canon, y con ella llegas a esa conversación sabiendo qué preguntar.' },
    { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí. Y conviene decir por qué, porque la razón que se suele dar es falsa: no es que hayamos recortado funciones para que Sheets las entienda, porque Sheets las entiende perfectamente. Es una convención interna de la casa: no usamos funciones volátiles ni funciones que compliquen el recalculado, no hay ni una referencia de una fórmula a otro fichero, y no hay constantes escondidas dentro de las fórmulas —todos los parámetros viven en celda verde, con su valor por defecto declarado—. El efecto secundario es que lo que ves en Excel se recalcula igual en Google Sheets, en LibreOffice y en Numbers, y como los libros guardan dentro los valores ya calculados, también se leen bien en el móvil.' },
    { q: '¿Sirve si voy a abrir fuera de España, y qué pasa cuando cambie la normativa?', a: 'El marco legal explicado es el español, y lo decimos en la primera pantalla. La estructura económica viaja entera —coste de apertura, capacidad de la línea, escandallo, punto de equilibrio, temporada y tesorería son casillas editables— y el vocabulario lleva su equivalencia de Hispanoamérica en la primera mención. El bloque sanitario y de licencias hay que adaptarlo a tu país, y esa adaptación te la ofrecemos como servicio: escríbenos a info@aichef.pro y te decimos qué cambia y qué cuesta. Sobre la normativa: es pago único con actualizaciones incluidas, entras a tu dashboard y descargas la versión nueva sin pagar nada más. Los parámetros legales viven en celda editable con su nota y su fecha, y el anexo cierra con la fecha de corte y las cuestiones que ya sabemos que se mueven: la acrilamida en revisión, el convenio, el registro horario y la facturación verificable.' },
  ],

  cta: {
    heading: 'Decide Antes de Firmar, No Después',
    subtitle: 'El orden de las decisiones, las herramientas que hacen tus números y los documentos que te piden. Todo lo que hay que resolver antes de abrir una churrería-chocolatería.',
    items: [
      'Guía completa PDF + DOCX: 16 capítulos y anexo normativo con fecha de corte (95 páginas)',
      '8 herramientas Excel con fórmulas vivas y todas las casillas editables',
      'Producción, hora punta y local: si ese local sirve y cuántas raciones por hora aguanta tu línea',
      'Coste de apertura por escenarios, con traspaso frente a obra nueva a cinco años',
      'Escandallo del churro y de la porra con el aceite absorbido y los dos márgenes',
      'Aceite de fritura, temporada y ferias, y plan financiero a 3 años',
      'Bonus: business plan modelo relleno (DOCX) y 12 decisiones de apertura resueltas (21 páginas)',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'CÓMO MONTAR UNA CHURRERÍA-CHOCOLATERÍA — 65 EUR',

  // §7.1: salientes de la landing al siguiente paso del embudo, con
  // utm_source=landing&utm_medium=cross-sell. La hermana (bombonería) va en primer lugar
  // de los cruces: «la bombonería es otro negocio y tiene su guía».
  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/guia-chocolateria-obrador?utm_source=landing&utm_medium=cross-sell', label: 'Cómo Montar una Chocolatería Boutique & Atelier' },
    { href: '/pack-appcc?utm_source=landing&utm_medium=cross-sell', label: 'Pack Plantillas APPCC' },
    { href: '/kit-escandallos?utm_source=landing&utm_medium=cross-sell', label: 'Kit de Escandallos Pro' },
    { href: '/plan-negocio-food-truck?utm_source=landing&utm_medium=cross-sell', label: 'Plan de Negocio: Food Truck' },
    { href: '/plan-negocio-cafeteria?utm_source=landing&utm_medium=cross-sell', label: 'Plan de Negocio: Cafetería' },
    { href: '/kit-gestion-personal?utm_source=landing&utm_medium=cross-sell', label: 'Kit Gestión de Personal y Turnos' },
    { href: '/productos-digitales', label: 'Todos los Productos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Versión 1.0 · octubre 2026',

  alreadyBought: {
    product: 'guia-churreria-chocolateria',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  // Sin aggregateRating y sin review. El template no los emite si no están.
  schema: {
    productName: 'Cómo Montar una Churrería-Chocolatería',
    productDescription: 'Dossier completo de apertura de una churrería-chocolatería en España: 16 capítulos y un anexo normativo con fecha de corte que recorren la elección del local, los humos y el fuego de aceite, la maquinaria, el coste de apertura, el alta fiscal y sanitaria, el aceite de fritura, el escandallo del churro y de la porra, el equipo y la madrugada, la temporada y las ferias, la franquicia y el plan financiero a tres años. Incluye 8 herramientas Excel con fórmulas vivas, un business plan modelo relleno y 12 decisiones de apertura resueltas.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    faqs: [
      { q: '¿Esto no está gratis en Google?', a: 'Lo suelto sí está, pero las guías gratuitas que hemos leído se copian los mismos tramos, y ninguna de las que hemos leído desglosa el coste de apertura partida a partida, cuantifica la temporada o trata a fondo los humos y el aceite. Lo que no está en Google es el orden en el que se toman las decisiones y ocho Excel donde metes TUS metros, TU carta y TU precio de aceite y sale TU cifra.' },
      { q: '¿En qué se diferencia de la guía de Chocolatería Boutique & Atelier? ¿Necesito las dos?', a: 'Aquella es bombonería con obrador y sin freidora; esta es churro frito y chocolate a la taza, con freidora, y la freidora cambia la licencia, los humos, el gas y el aceite. Son dos negocios distintos y cada guía cubre el suyo.' },
      { q: '¿Me enseña a hacer churros?', a: 'No, y lo decimos antes de que pagues: no es un recetario ni un curso de churrero. Lo que hace la guía es ayudarte a elegir un curso, a pedir lo que importa en un traspaso con maestro saliente y a que las cuentas de tu churrería salgan antes de abrir.' },
      { q: '¿Cuánto cuesta montar una churrería?', a: 'No te damos un número: te damos el modelo que produce el tuyo. La maquinaria núcleo con precio publicado va de unos 4.200 € en un despacho a unos 8.600 € en un local con sala, sin IVA, y no incluye la obra de humos, la cafetera, la vitrina ni el TPV; esas partidas las presupuestas tú en la calculadora.' },
      { q: '¿Es rentable una churrería?', a: 'Te lo enseñamos con tus números, no con una promesa: los dos márgenes que circulan entre churreros —más del 60 % sobre materia prima y algo más del 50 % que declara el gestor de La Artesana— miden cosas distintas, y la guía los da juntos con su definición. Lo que decide es el punto de equilibrio en raciones al día con tu personal real.' },
      { q: '¿Los Excel parten de mi receta o de una receta vuestra?', a: 'De la tuya: el libro de escandallo parte de tu receta, de tus gramos por pieza y del precio de tu mix, y te da piezas, raciones y coste por kilo. El caso de «El Molinete» es un ejemplo relleno que sobrescribes con lo tuyo.' },
      { q: '¿Necesito licencia de apertura?', a: 'Depende del formato. La actividad de un despacho para llevar hasta 750 m² va por declaración responsable, pero las obras de la salida de humos, si necesitan proyecto, van con su licencia y su técnico. Con mesas y consumo en el local, manda tu ayuntamiento.' },
      { q: '¿Sirve para un puesto de feria o un food truck?', a: 'La caseta de feria entra como variante, con su checklist y la hoja de punto muerto por evento. Si vas a un vehículo-cocina, el Plan de Negocio Food Truck es tu producto.' },
      { q: 'Tengo una cafetería y quiero meter churros. ¿Me sirve?', a: 'Te sirve el capítulo de lo que cambia al meter una freidora en un local que no la tenía: humos, potencia, aceite y alérgenos. El negocio de cafetería lo cubren su plan de negocio y su kit.' },
      { q: '¿Franquicia o por mi cuenta?', a: 'Hay un capítulo con lo que publican las enseñas, de unos pocos miles de euros a más de cien mil de inversión, con canon y royalty, como orden de magnitud y con su fecha, sin recomendar marca.' },
      { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí, y no porque hayamos recortado funciones: Sheets las entiende perfectamente. Es una convención interna de la casa: no usamos funciones volátiles, no hay ni una referencia de una fórmula a otro fichero y no hay constantes escondidas dentro de las fórmulas, porque todos los parámetros viven en celda verde con su valor por defecto declarado.' },
      { q: '¿Sirve si voy a abrir fuera de España, y qué pasa cuando cambie la normativa?', a: 'El marco legal explicado es el español. La estructura económica viaja entera en casillas editables; el bloque sanitario y de licencias hay que adaptarlo a tu país, y esa adaptación te la ofrecemos como servicio en info@aichef.pro. Es pago único con actualizaciones incluidas y el anexo cierra con la fecha de corte y las cuestiones que ya sabemos que se mueven.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Cómo Montar una Churrería-Chocolatería', item: 'https://aichef.pro/guia-churreria-chocolateria' },
    ],
  },
};

export default data;
