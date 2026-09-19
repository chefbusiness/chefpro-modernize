// guia-chocolateria-obrador.ts — LÍNEA GUÍAS «Cómo Montar», producto 49 (2026-09-19).
//
// Landing NATIVA en Astro (no hay página SPA de la que portar copy). Fuentes del copy:
//   · scripts/productos-digitales/guia-chocolateria-SPEC.md (§0 ficha, §1 decisiones
//     D1-D53, §2 entregables, §4 índice, §5 lista negra, §6 vocabulario, §7 canales,
//     §8.1 ficheros a tocar)
//   · scripts/productos-digitales/guia-chocolateria-DECISIONES-2026-09-12.md (D1-D18 + D17-bis)
//   · scripts/productos-digitales/auditorias/guia-chocolateria-RESEARCH-2026-09-12.md
//     (§6 voz del cliente, §12 copy, §14 las 12 FAQ de compra, §15 lista negra)
//   Molde fichero a fichero: guia-pasteleria-obrador.ts (producto 48, commit 8457077 +
//   8b35fd9 para el layout del bonus).
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · D17 / D17-bis — UN SOLO NOMBRE VISIBLE: «Cómo Montar una Chocolatería Boutique &
//    Atelier», idéntico en el H1 (hero.titlePre + hero.titleGold), en schema.productName,
//    en el name.es de src/data/products-catalog.ts, en la tarjeta del hub, en los
//    footerLinks cruzados de las fichas afines y en el asunto del correo. El «&» va
//    LITERAL en las cadenas fuente (Astro escapa el HTML solo). «con obrador» es
//    SUBTÍTULO, nunca un nombre alternativo. Lo ata scripts/productos-digitales/nombre-gate.py.
//  · D1 (§0 «Ancla») — producto nuevo → SIN `priceOld` ni `discountBadge` (no existe
//    «precio anterior de 30 días»: art. 20 de la Ley 7/1996 en la redacción del RDL
//    24/2021, NO el TRLGDCU), SIN `aggregateRating`, SIN `review` y con
//    `testimonials.items: []`. No ha vendido una unidad; el template oculta la sección
//    con el array vacío.
//  · §7.1 — NI UN ENLACE a las otras guías «Cómo Montar» mientras no entreguen lo que
//    anuncian. Por eso `footerLinks` sólo cruza a kit-tareas-chocolateria,
//    kit-escandallos, pack-appcc y la Guía Food Cost, más las tres páginas de rol
//    /usos/ del nicho (enlace bidireccional).
//  · PÁGINAS = TOKENS. `111` (guía), `34` (bonus 2) y
//    (el business plan NO publica páginas: es DOCX y no se mide, precedente Pastelería) se sustituyen por las páginas MEDIDAS con PyMuPDF
//    cuando estén construidos los documentos. NO publicar con el token puesto; lo
//    verifica paginas-gate.py --only guia-chocolateria-obrador (exit 1 si queda alguno).
//  · §2.3 / D26 de Pastelería — la FAQ de compatibilidad NO da la razón falsa («las
//    prohibimos para que funcione en Sheets»): Sheets implementa esas funciones. La
//    razón real es interna (estabilidad del recalculado, caché de fórmulas, volatilidad
//    y legibilidad).
//  · §12.3 — sin siglas españolas (RGSEAA, APPCC, BOE, EUDR) en el hero ni en los
//    titulares de capítulo; el marco legal explicado es el ESPAÑOL y se dice arriba; la
//    FAQ ofrece la adaptación como servicio a quien abre fuera de España. Y nada de
//    «verificado contra el BOE» como gancho (regla de John del 5-sep).
//  · D1 (alcance) — aviso de alcance EN LA PRIMERA PANTALLA: se cubre a fondo la
//    bombonería artesanal con obrador; la chocolatería de taza y churros entra como
//    variante y se dice antes de comprar (antídoto contra la devolución por expectativa).
//  · Declaración en negativo ARRIBA, no en la FAQ: «no es un recetario ni un curso de
//    técnica del chocolate, y no sustituye al proyecto técnico visado».
//  · §6 vocabulario — «artesanal», NUNCA «artesana». «templado», NUNCA «temperado».
//    «dulcería» no aparece en ninguna parte (en México es la tienda de golosinas al
//    mayoreo). «trufa» y «praliné» no se usan como sinónimos de bombón: son tipos.
//  · CERO cifras inventadas. Las únicas cifras admitidas son las verificadas con id y
//    fuente: el núcleo de máquina como RANGO y con etiqueta de BASE MIXTA de impuestos
//    (D23c: ≈5.700-5.900 € y ≈24.000-24.300 €, nunca restados ni comparados
//    aritméticamente), el cacao de CHS-24a (4.956 €/t el 2-ene-2026 frente a más de
//    10.300 €/t el 2-ene-2025) y la subida del chocolate de CHS-23 (17,7 % en 2025).
//    PROHIBIDAS `N-1`…`N-20` de §5.2, empezando por «una chocolatería artesanal premium
//    requiere 80.000-250.000 €» (que es NUESTRA, use-cases-content.es.consultor.ts:393).
//    Los `desc` de los capítulos describen QUÉ SE DECIDE, sin cifras.
//  · D16 — cripto encendida desde el nacimiento: no hay nada que tocar aquí ni en el
//    wrapper. GuiaLandingPage.astro monta las tres puertas de CryptoPayButton solas
//    cuando `cryptoEnabledFor('guia-chocolateria-obrador')` da true (env CRYPTO_PRODUCTS).
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-chocolateria-obrador',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_CHOCOLATERIA_OBRADOR',

  seo: {
    title: 'Cómo Montar una Chocolatería Boutique & Atelier | Obrador',
    description: 'Para quien va a abrir una chocolatería en España: local, clima del obrador, coste de apertura, licencias y escandallo del cacao. 20 capítulos y 9 Excel.',
    keywords: 'montar una chocolatería, cómo montar una chocolatería, obrador de chocolate, bombonería artesanal, chocolatería artesanal, templado de chocolate, atemperadora, cámara de chocolate, escandallo de chocolate, bean-to-bar, licencia de obrador, traspaso de chocolatería, abrir una chocolatería, denominaciones legales del cacao, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-chocolateria-obrador.jpg',
  },

  hero: {
    badge: 'Para quien AÚN no ha abierto: lo que hay que decidir antes de firmar nada',
    titlePre: 'Cómo Montar una ',
    titleGold: 'Chocolatería Boutique & Atelier',
    subtitleLine: 'Obrador, denominaciones legales y números: el dossier completo de apertura de una bombonería con obrador',
    description: 'No te enseña a templar. Te dice qué decidir y en qué orden: si ese local sirve, cuánto necesitas de verdad, cómo puedes llamar legalmente a lo que vendes, cuánto tienes que cobrar cuando sube el cacao y de qué vives en agosto. Cubre a fondo la chocolatería artesanal con obrador —bombones, tabletas y cajas—; si lo que quieres es una chocolatería de taza y churros, aquí tienes el capítulo que te dice qué cambia, pero ése es otro negocio. El marco legal explicado es el español. Esto no es un recetario ni un curso de técnica del chocolate, y no sustituye al proyecto técnico visado.',
    checkItems: [
      'Guía completa PDF + DOCX editable: 20 capítulos y un anexo normativo con fecha de corte (111 páginas)',
      '9 herramientas Excel con fórmulas vivas: capacidad de obrador y clima, coste de apertura, sensibilidad al precio del cacao, carta y escandallo con merma de templado, vida útil de los rellenos, campañas y valle del año, plan financiero a 3 años, licencias, y equipamiento y proveedores de cobertura y cacao',
      'El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes',
      'El marco legal explicado es el español, con su norma, su artículo y el día en que se comprobó. Todas las casillas de los Excel son editables',
      'Bonus 1: el business plan modelo, relleno con el caso completo, en DOCX editable',
      'Bonus 2: 12 decisiones de apertura resueltas (34 páginas)',
    ],
    ctaLabel: 'COMPRAR GUÍA — 65 EUR',
    avatarAltPrefix: 'Professional',
  },

  // D1 (§0 «Ancla»): sin priceOld ni discountBadge. Producto nuevo: no hay «precio
  // anterior de 30 días» que anclar sin incumplir el art. 20 de la Ley 7/1996.
  pricing: {
    price: '65 EUR',
    heroNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    buyBoxNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    bonusTotalLabel: 'Incluido en el precio: la guía, las 9 herramientas Excel y los dos bonus',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-chocolateria-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-chocolateria-1.jpg',
      '/lovable-uploads/ai-gallery/guia-chocolateria-2.jpg',
      '/lovable-uploads/ai-gallery/guia-chocolateria-3.jpg',
      '/lovable-uploads/ai-gallery/guia-chocolateria-4.jpg',
      '/lovable-uploads/ai-gallery/guia-chocolateria-5.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-chocolateria-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-chocolateria-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-chocolateria-4.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 9 Plantillas + 2 Bonus',
    subtitle: 'Criterio y decisión, no teoría. Cada capítulo se apoya en una de las nueve herramientas Excel del pack y sus tablas salen de las celdas de esos ficheros, no de ejemplos inventados. Cierra un anexo normativo con fecha de corte, para que sepas qué estaba vigente el día que se escribió y qué fechas ya sabemos que se mueven. Escrito por un chef y consultor gastronómico que lleva desde 2010 acompañando aperturas.',
    chapters: [
      { icon: 'Layers', num: '01', title: 'Qué Negocio Estás Montando: las Doce Variantes y Cuál te Toca', desc: 'Las doce formas de vender chocolate comparadas por inversión, metros y personal, por qué la chocolatería de taza y churros es otro negocio, el mapa de problema a capítulo y a herramienta, y el glosario con sus equivalencias de Hispanoamérica.' },
      { icon: 'Users', num: '02', title: 'El Cliente y la Plaza: Quién Compra Chocolate, Cuándo y a Qué Precio', desc: 'Contra quién compites de verdad: un mercado que crece en euros y se encoge en kilos, qué peso tiene el bombón dentro de la categoría, por qué el consumidor ya paga más por menos, y por qué no existe un número oficial de chocolaterías en España ni conviene fingir que sí.' },
      { icon: 'Cookie', num: '03', title: 'La Carta de Apertura: las Referencias, las Familias y la Caja como Unidad', desc: 'Cómo se decide un surtido de apertura con criterio de margen, qué papel juega cada una de las cinco familias, por qué la caja y no la unidad es la verdadera unidad de venta, y qué aporta el chocolate a la taza como familia de invierno que sube el ticket.' },
      { icon: 'Banknote', num: '04', title: 'Cuánto Cuesta Abrir: el Coste de Apertura, Partida a Partida', desc: 'Por qué las cifras publicadas varían por un factor diez y qué hipótesis lleva cada una, la columna de impuesto que descuadra el presupuesto si falta, las partidas que ninguna fuente publica y cómo presupuestarlas, y el colchón de tesorería como partida y no como propina.' },
      { icon: 'Layout', num: '05', title: 'El Local: Metros, Zonas y la Ficha de Visita', desc: 'Las zonas de un obrador de chocolate, que no son las de una pastelería, el principio de marcha adelante, la cámara climatizada como zona propia, la potencia que de verdad hace falta, y la ficha con la que se visita un local antes de enamorarse de él.' },
      { icon: 'DoorOpen', num: '06', title: 'Antes de Firmar: el Obrador sin Humos Cambia la Conversación de la Licencia', desc: 'El chocolate no fríe ni hornea, y eso cambia la conversación: qué norma de evacuación no te regula, qué te sigue regulando por la climatización, hasta qué superficie ninguna administración puede exigirte licencia previa de actividad, y las tres puertas de local nuevo, traspaso o franquicia.' },
      { icon: 'Thermometer', num: '07', title: 'El Clima del Obrador: por Qué el Chocolate Manda sobre el Local', desc: 'Sala y cámara son dos cosas distintas y conviene no confundirlas. Ninguna norma fija la temperatura de tu obrador: la declaras tú y la justificas. De dónde salen el fat bloom y el sugar bloom, y exactamente qué hay que preguntarle al instalador antes de pedirle presupuesto.' },
      { icon: 'Wrench', num: '08', title: 'Maquinaria: Atemperadora, Enrobadora y Moldes', desc: 'La escalera de atemperadoras y el cruce de kilos por semana con máquina, la trampa de comparar precios publicados con impuesto y sin él, por qué la vitrina de chocolate no es la de pastelería, y los plazos de entrega y la segunda mano que mueven tu fecha de apertura.' },
      { icon: 'ShieldCheck', num: '09', title: 'Licencias, Sanidad y Registro: el Camino Completo', desc: 'Una chocolatería minorista no va al registro sanitario estatal, y tener obrador no te saca de minorista: cuándo sí vuelve y con qué tres condiciones acumulativas, la central y sus sucursales, la ruta desde casa con las cinco letras de la lista, y dónde se pide la artesanía alimentaria.' },
      { icon: 'FileText', num: '10', title: 'Cómo Puedes Llamar a lo Que Vendes: las Denominaciones Legales del Cacao', desc: 'La tabla de mínimos y sus dos bases de cálculo, por qué bombón y praliné son el mismo punto de la norma, cuándo la mención del porcentaje de cacao es obligatoria y cuándo no, qué calificativos de calidad autoriza la norma sin dar lista de palabras, y dónde acaba el chocolate y empieza el sucedáneo.' },
      { icon: 'Leaf', num: '11', title: 'Cacao, Cadmio y Deforestación: Qué te Pide la Norma y Qué le Pides a tu Proveedor', desc: 'El cadmio sube con el porcentaje de cacao y castiga al negro premium, lo que es chocolate para la denominación no lo es para los contaminantes, qué cambia el reglamento de deforestación según compres cobertura o grano, y qué papeles hay que pedirle exactamente a cada proveedor.' },
      { icon: 'ClipboardCheck', num: '12', title: 'Autocontrol, Alérgenos y Formación: Qué Tener el Día de la Inspección', desc: 'La carpeta que hay que tener el día que entra el inspector: autocontrol simplificado con responsable designado por su nombre, los peligros propios de un obrador de chocolate, los ocho alérgenos de una bombonería, cuándo el lote es obligatorio y cuándo no, y qué exige de verdad decir «sin gluten».' },
      { icon: 'Truck', num: '13', title: 'Proveedores: Cobertura, Cacao, Packaging y Plazos', desc: 'Los proveedores verificados por categoría con su enlace, cómo pedir tres presupuestos comparables de verdad, las dos preguntas que separan a quien compra de quien sabe lo que compra, y qué pasa con el impuesto al plástico si traes los estuches de fuera de España.' },
      { icon: 'Calculator', num: '14', title: 'Escandallo del Chocolate: la Merma de Templado, el Recorte Que Vuelve y la Caja', desc: 'La unidad de costeo es el molde y la tanda, no la pieza. El chocolate limpio se refunde y el que lleva ganache o fruta va a residuo, así que hay dos mermas y no una. Coste de la hora de obrador imputado por pieza, y margen bruto y food cost como la misma regla dicha dos veces.' },
      { icon: 'Coins', num: '15', title: 'El Precio del Cacao: Qué Haces Cuando Sube y Quién Paga la Subida', desc: 'El cacao cayó a la mitad en un año y el chocolate siguió subiendo: la cobertura no baja cuando baja la bolsa. El ciclo real de revisión de precios, los cuatro caminos con su número —precio, gramaje, cobertura o margen— y cómo se comunica una subida sin perder al cliente.' },
      { icon: 'Droplets', num: '16', title: 'Vida Útil del Relleno: Actividad de Agua, Vitrina y Tamaño de Lote', desc: 'Entre la ganache fresca y la estabilizada hay un factor de tres a cinco, y eso es una decisión de modelo de negocio, no de técnica. La vida útil la declaras tú y consta en tu plan de autocontrol; envasado con etiqueta y a granel no son el mismo régimen; y de cuánto conviene hacer cada lote.' },
      { icon: 'UserCog', num: '17', title: 'El Equipo: Cuántos, Qué Perfiles y Qué Cuestan', desc: 'Los tres perfiles del obrador y qué hace cada uno, el salto del bruto al coste de empresa con la seguridad social dentro, por qué no existe un convenio estatal del chocolate y qué sí existe en su lugar, y cómo identificar en el registro público el convenio que te toca a ti.' },
      { icon: 'CalendarRange', num: '18', title: 'Las Campañas y el Valle: de Navidad a Agosto', desc: 'Cuánto pesa un solo evento como San Valentín, por qué la Navidad se produce y se paga en octubre y se cobra en diciembre, por qué las comuniones son una campaña propia que sostiene tres meses, y qué es exactamente lo que para en agosto: el obrador, no la caja.' },
      { icon: 'Store', num: '19', title: 'Canales: Mostrador, Envío, Hostelería, Corporativo y Talleres', desc: 'Los canales que se salen de la nota de tu epígrafe y la pregunta exacta que hay que llevarle al asesor, cuándo vender a empresas te obliga a inscribirte, por qué vender online sigue siendo minorista pero te responsabiliza de la temperatura en el camión, y los talleres como la única línea que funciona en agosto.' },
      { icon: 'Rocket', num: '20', title: 'El Plan Financiero y los Primeros Noventa Días', desc: 'Cuenta de resultados a tres años con estacionalidad mensual y rampa de arranque, punto muerto con una sola regla de margen, el sueldo del propietario como renglón propio, la facturación verificable y la libertad de horarios como decisión comercial del día uno, y qué se mide en el mes cero y en el mes tres.' },
    ],
  },

  // D1: producto recién nacido, sin una sola venta → sin testimonios y sin
  // aggregateRating. El template oculta esta sección con el array vacío.
  testimonials: {
    titleGold: '',
    subtitle: '',
    items: [],
  },

  why: {
    reasons: [
      { icon: 'Shuffle', title: 'Lo Que Se Decide Antes de Abrir', desc: 'El Kit de Tareas Chocolatería te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes: si ese local sirve, qué clima necesita tu obrador, cuánto necesitas de verdad, cómo puedes llamar a lo que vendes y a cuánto tienes que venderlo. No se pisan: aquí no encontrarás las curvas de templado ni el parte de producción, porque ya existen y se citan por su nombre.' },
      { icon: 'FileSpreadsheet', title: 'Tres Herramientas Que No Están en Ningún Otro Sitio', desc: 'La sensibilidad al precio del cacao (qué precio tienes que poner cuando la cobertura sube, y cuál de tus referencias se rompe primero), el clima del obrador con su ficha de preguntas al instalador y su semáforo contra la temperatura exterior de agosto de tu ciudad, y la vida útil de los rellenos con el lote económico y la merma por caducidad en euros al año. No están en el resto del catálogo ni en la competencia de pago que hemos revisado producto a producto.' },
      { icon: 'ShieldCheck', title: 'Cada Dato Legal con su Artículo y su Fecha', desc: 'Ninguna afirmación normativa va suelta: cada celda y cada tabla llevan la norma, el artículo, el enlace y el día en que se comprobó, y el anexo final tiene fecha de corte con las fechas que ya sabemos que se mueven. Es el capítulo que más falta hace en este nicho, donde la guía gratuita más leída sigue pidiendo un requisito que dejó de existir en 2010. El marco explicado es el español; todas las casillas de los Excel son editables.' },
      { icon: 'AlertTriangle', title: 'Y Lo Que Esta Guía No Hace', desc: 'No te enseña a templar ni a formular una ganache: eso es oficio y se aprende en un obrador. No sustituye al proyecto técnico visado ni a la gestión de licencias, que los firma un técnico. No te garantiza que tu ayuntamiento diga que sí, y no promete clientes ni rentabilidad. Lo que hace es que llegues a cada reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar, y que no firmes un alquiler antes de tiempo.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía en PDF y DOCX, recibes estas 11 piezas: las 9 herramientas Excel con fórmulas vivas y los dos bonus',
    // layout 'single' (una sola rejilla de 3 columnas, todas las tarjetas del mismo
    // ancho) y no 'split': el split de la línea reparte slice(0,3) en una rejilla
    // max-w-5xl y slice(3) en OTRA de 2 columnas y max-w-3xl — está pensado para 5
    // ítems (3+2) y con 11 dejaría 3 tarjetas anchas y 8 estrechas. Mismo criterio que
    // guia-pasteleria-obrador.ts (8b35fd9) y guia-food-cost-ingenieria-menu.ts.
    layout: 'single',
    items: [
      {
        icon: 'FileSpreadsheet',
        label: 'HERRAMIENTA 1',
        title: 'Capacidad de Obrador y Clima',
        value: 'Incluido en el pack',
        desc: 'Zonas y metros cuadrados, capacidad por equipo, cuello de botella, clima del obrador con su ficha de preguntas al instalador, y ficha de visita al local con semáforo eliminatorio. Decide si ese local sirve y cuántos bombones al día aguanta el equipo que estás a punto de comprar.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-hero.jpg',
      },
      {
        icon: 'Banknote',
        label: 'HERRAMIENTA 2',
        title: 'Calculadora del Coste de Apertura',
        value: 'Incluido en el pack',
        desc: 'Inversión por bloque, variante del formato, traspaso frente a obra nueva a cinco años, y la columna de impuesto línea a línea con su efecto en la tesorería. Decide cuánto necesitas de verdad y si te sale mejor coger un traspaso o montarlo desde cero.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-3.jpg',
      },
      {
        icon: 'Coins',
        label: 'HERRAMIENTA 3',
        title: 'Sensibilidad al Precio del Cacao',
        value: 'Incluido en el pack',
        desc: 'Coste de cobertura por referencia en sus dos bases de impuesto, escenarios de subida, repercusión al precio de venta y semanas de stock. Decide qué haces cuando la cobertura sube: subir precio, cambiar gramaje, cambiar cobertura o aceptar menos margen. No existe nada igual en el catálogo.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-1.jpg',
      },
      {
        icon: 'Calculator',
        label: 'HERRAMIENTA 4',
        title: 'Carta de Apertura y Escandallo',
        value: 'Incluido en el pack',
        desc: 'Escandallo por molde y por tanda, merma de templado con el recorte que vuelve a la cuba y el que va a residuo, coste de la hora de obrador, unidad frente a caja, mix y ticket medio, y la denominación legal de cada referencia. Decide qué vendes, a cuánto y cómo puedes llamarlo.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-2.jpg',
      },
      {
        icon: 'Droplets',
        label: 'HERRAMIENTA 5',
        title: 'Vida Útil de los Rellenos y Rotación',
        value: 'Incluido en el pack',
        desc: 'Tipo de relleno y actividad de agua, vida útil que declaras tú, régimen de etiquetado o granel, temperatura y vitrina con su semáforo, y lote económico con la merma por caducidad en euros al año. Decide cuánto dura cada bombón, en qué vitrina va y de cuánto haces cada lote.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-5.jpg',
      },
      {
        icon: 'CalendarRange',
        label: 'HERRAMIENTA 6',
        title: 'Campañas y Valle del Año',
        value: 'Incluido en el pack',
        desc: 'Calendario de campañas mes a mes, peso de cada una sobre el año, capacidad frente a demanda del pico, refuerzo y tesorería inmovilizada en moldes y packaging, y el agosto real: obrador parado y mostrador vivo con otro mix. Decide si aguantas Navidad y de qué vives en julio.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-4.jpg',
      },
      {
        icon: 'TrendingUp',
        label: 'HERRAMIENTA 7',
        title: 'Plan Financiero a 3 Años',
        value: 'Incluido en el pack',
        desc: 'Supuestos, inversión inicial, cuenta de resultados a tres años con estacionalidad mensual, punto de equilibrio, escenarios, personal con seguridad social, tesorería mes a mes, financiación, margen por canal y la economía de los talleres y el regalo corporativo. Decide si el negocio se sostiene.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-hero.jpg',
      },
      {
        icon: 'ClipboardCheck',
        label: 'HERRAMIENTA 8',
        title: 'Checklist Legal, Licencias y Cacao',
        value: 'Incluido en el pack',
        desc: 'Seis fases con contador de avance, árbol de registro sanitario, árbol del suministro a otros minoristas, ruta desde casa, cadmio y analíticas, el árbol del reglamento de deforestación, registro de formación, y cronograma con ruta crítica. Decide qué papel te toca, en qué orden y cuándo abres.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-3.jpg',
      },
      {
        icon: 'Wrench',
        label: 'HERRAMIENTA 9',
        title: 'Equipamiento y Proveedores de Cobertura y Cacao',
        value: 'Incluido en el pack',
        desc: 'Equipamiento con horquilla, prioridad, impuesto y plazo de entrega; variante del formato; el árbol que clasifica a cada proveedor y te dice qué papel pedirle; la tabla de clientes a los que suministras; y la desviación contra tu presupuesto. Decide qué compras, a quién y con qué papeles.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-1.jpg',
      },
      {
        icon: 'ScrollText',
        label: 'BONUS 1',
        title: 'Business Plan Modelo, Relleno',
        value: 'Incluido en el pack',
        desc: 'El caso completo de la bombonería de ejemplo en el formato que pide un banco o una línea de financiación pública: resumen ejecutivo con el resultado neto y el punto de equilibrio dentro, mercado y plaza, concepto y carta, plan de operaciones con obrador y clima, plan financiero a tres años y riesgos con escenarios. En DOCX editable, con las cifras cuadradas contra el plan financiero del pack, celda a celda.',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-5.jpg',
      },
      {
        icon: 'GraduationCap',
        label: 'BONUS 2',
        title: '12 Decisiones de Apertura Resueltas',
        value: 'Incluido en el pack',
        desc: 'Doce decisiones reales con su contexto, sus opciones, el criterio, la celda del Excel que la resuelve y la norma con su fecha cuando la hay: bombonería o bean-to-bar, comprar la atemperadora continua o empezar con la de sobremesa, abrir con quince referencias o con veintiocho, vender la caja o la unidad, parar el obrador en agosto o no, o empezar en casa dentro de la legalidad. En PDF y en DOCX editable (34 páginas).',
        image: '/lovable-uploads/ai-gallery/guia-chocolateria-4.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te sirve para decidir tu local, tus números y tu papeleo con criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  // Las 12 FAQ de COMPRA del research §12/§14, REESCRITAS según §8.1 fila 1 de la SPEC:
  // la 3 con la letra e) del art. 13.8 (D21), la 4 sin totales cerrados y con la etiqueta
  // de base mixta (D23c), la 6 con «operador ≠ operador posterior» y el número de
  // declaración sólo si el proveedor es operador (D5, D48), la 7 con el límite de la nota
  // del epígrafe 644.5 dentro (D19) y la 11 sin la causalidad falsa de Sheets (§2.3).
  // Las de oficio («¿cómo se templa?») y las definicionales del PAA («¿cuáles son los 3
  // tipos de chocolate?») quedan fuera: no son de compra (D39).
  faqs: [
    { q: '¿Esto no está gratis en Google?', a: 'La información suelta sí está, y por eso se contradice. Las fuentes gratuitas que hemos revisado una a una dan cifras de arranque que se separan por un factor diez para el mismo negocio y ninguna dice de qué depende ese número; media página de resultados en español es de México y de Estados Unidos, con pesos y con dólares; y la única guía española de 2026 exige un requisito legal que dejó de existir en 2010. Lo que no está en Google es el orden en el que se toman las decisiones y nueve Excel donde metes TUS metros, TU carta y TU precio de cobertura y sale TU cifra, con la hipótesis escrita al lado.' },
    { q: '¿En qué se diferencia del Kit de Tareas Chocolatería de 12 €? ¿Necesito los dos?', a: 'El Kit te dice qué hacer cada día cuando ya has abierto: templado, moldeado, vitrina, campañas y caja. Esta guía es todo lo que hay que decidir antes de abrir: el local, el clima del obrador, la inversión, el papeleo, cómo puedes llamar a lo que vendes y los números. Si ya estás abierto, el Kit te vale y esta guía no te hace falta. Si vas a abrir, la guía es lo primero y el Kit es lo que usarás desde el día uno. Y no se pisan a propósito: donde la guía necesita un dato que el Kit ya publica —los plazos orientativos de vida útil por familia, por ejemplo—, lo cita por su fichero y su hoja en vez de reescribirlo con otros números.' },
    { q: '¿Me sirve si quiero empezar desde casa?', a: 'Sí, y es donde más aporta, aunque la respuesta no sea la que esperabas. El artículo 13.8 del Real Decreto 1021/2022 lista cinco letras de alimentos que pueden elaborarse en una vivienda particular, y el chocolate no aparece por defecto en ninguna de ellas. Pero la quinta letra dice literalmente «otros alimentos que las autoridades competentes de las comunidades autónomas permitan en sus territorios», así que la puerta no está cerrada: está en tu comunidad. La fórmula correcta no es «hacer bombones en casa para vender es ilegal en España», sino «no entra en el régimen estatal salvo que tu comunidad lo haya añadido». La guía te dice cómo preguntarlo, a quién y con qué palabras, y el checklist legal trae una hoja dedicada a esa ruta con la casilla de tu comunidad y el enlace a su registro.' },
    { q: '¿Cuánto cuesta montar una chocolatería de verdad?', a: 'No te damos un número: te damos el modelo que produce el tuyo, porque el coste de abrir depende de tus metros, de tu plaza, del estado del local y de con qué máquina arrancas, y ninguna de esas cuatro cosas la sabemos nosotros. Lo que sí te damos verificado, proveedor a proveedor y con su fecha, es el núcleo de máquina: del orden de 5.700 a 5.900 € si arrancas con una atemperadora de sobremesa, y del orden de 24.000 a 24.300 € con una continua. Los dos son rangos de BASE MIXTA de impuestos —hay líneas publicadas con el impuesto dentro y otras sin él, y así van etiquetadas—, así que sirven para dimensionar la compra de maquinaria y no son un presupuesto de apertura ni una cifra fiscal. Las partidas que ninguna fuente publica las presupuestas tú en la calculadora, con la columna de impuesto línea a línea para que el total no te salga un veintiuno por ciento desviado.' },
    { q: '¿Qué pasa cuando sube el cacao?', a: 'Hay un libro de Excel entero para eso, y es el que no existe en ninguna otra parte. El cacao cotizaba por encima de 10.300 €/t el 2 de enero de 2025 y a 4.956 €/t el 2 de enero de 2026, y sin embargo el precio del chocolate subió un 17,7 % durante 2025: la cobertura no baja cuando baja la bolsa, y conviene saberlo antes de fijar la carta. El precio de tu cobertura vive en celda verde, la hoja de sensibilidad te dice qué pasa con cada escenario de subida y cuál de tus referencias se rompe primero, y el capítulo te da los cuatro caminos con su número: subir precio, bajar gramaje, cambiar de cobertura o aceptar menos margen. Con el guion de cómo se comunica una subida, que también hace falta.' },
    { q: '¿Y el reglamento europeo de deforestación? ¿Me afecta si compro cobertura europea?', a: 'Sí, y no como te lo han contado. Hay que separar dos figuras que la norma distingue: el «operador», que es quien introduce el producto en el mercado de la Unión, y el «operador posterior» del artículo 2, punto 15 ter, que es quien lo comercializa después. Si tu cobertura llega ya comercializada en la Unión y amparada por una declaración de diligencia debida, eres operador posterior, y el aplazamiento del artículo 38.3 —que está redactado para operadores establecidos como tales a 31 de diciembre de 2024— no te alcanza: tu fecha es el 30 de diciembre de 2026. Si tu cobertura no está amparada, la calificación deja de ser automática y hay que revisarla. Lo decimos con esa cautela a propósito, porque ese último paso es una inferencia nuestra y va declarada como tal, no vendida como certeza. En la práctica: guardas los datos de tus proveedores y de tus clientes, y pides el número de referencia de la declaración únicamente a los proveedores que sean operadores. El Excel trae el árbol que lo resuelve proveedor a proveedor.' },
    { q: '¿Cubre la chocolatería de taza y churros, tipo San Ginés?', a: 'Como variante, no a fondo, y preferimos decirlo antes de que pagues. Es otro negocio: fríe, y con la freidora vuelven la salida de humos, el gas y las comidas preparadas. La propia norma los separa: el anexo de la Ley 12/2012 incluye el epígrafe 644.5, «comercio al por menor de bombones y caramelos», y no incluye ningún grupo de la agrupación 67, donde vive la chocolatería de taza. Ese epígrafe te faculta para fabricar bombones y caramelos en tu propio establecimiento siempre que los vendas en tus propias dependencias de venta; en el momento en que sirves a otros comercios, a empresas o envías fuera, eso cambia, y la guía te dice cuándo y qué hay que preguntarle exactamente a tu asesor. Lo que cubrimos a fondo es la chocolatería artesanal con obrador; para la de taza y churros tienes el epígrafe del capítulo 1 que te dice qué cambia y una columna de escenario en la calculadora y en la cuenta de resultados.' },
    { q: '¿Y si quiero hacer bean-to-bar?', a: 'Entra como variante, con su propia columna de inversión, su epígrafe en el capítulo de cacao y dos frentes normativos que la bombonería corriente no tiene. El primero: partiendo del grano eres operador a efectos del reglamento de deforestación, con diligencia debida completa, no operador posterior. El segundo: tostar el grano obliga a mirar el catálogo de actividades potencialmente contaminadoras de la atmósfera, cuyo epígrafe habla del tostado «del café o similares» —una calificación que hay que consultar con tu comunidad, no dar por hecha—, y la nota que sube de grupo la actividad empieza por los núcleos de población, no por los espacios protegidos. Lo que no te damos es un precio del tren bean-to-bar: no existe precio público verificable, y en lugar de inventarlo te damos la lista de la compra y las preguntas que hay que hacerle a cada fabricante.' },
    { q: '¿Sustituye al proyecto técnico o a la gestión de licencias?', a: 'No, y hay que decirlo arriba. Eso lo firma un técnico y no hay atajo. Aquí tampoco vas a encontrar un precio de proyecto: ninguna de las ingenierías que revisamos publica su tarifa, y preferimos dejar el hueco a rellenarlo con un número inventado. Lo que hace la guía es que llegues a esa reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar, que sepas qué parte del expediente depende de ti y cuál del técnico, y que no hayas firmado un alquiler antes de saberlo.' },
    { q: 'Mi ayuntamiento es distinto. ¿Me sirve igual?', a: 'Es la primera objeción que pone cualquier técnico, y tiene razón: no existe ninguna guía que dé la ordenanza de los más de ocho mil municipios que hay en España, y ésta tampoco la da. No hemos abierto ninguna ordenanza municipal, y por eso no verás aquí escrito «en tu ciudad el trámite es tal». Lo que sí da es el marco estatal y europeo verificado con su norma, su artículo y su enlace, más la lista exacta de qué preguntar en tu ayuntamiento y en qué orden. Y un dato estatal que cambia la conversación: el artículo 3.1 de la Ley 12/2012 impide a las administraciones exigir licencia previa de instalación, de funcionamiento o de actividad hasta 750 m², y su anexo incluye expresamente el epígrafe del comercio al por menor de bombones y caramelos. Prometer más que eso sería mentirte.' },
    { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí. Y conviene decir por qué, porque la razón que se suele dar es falsa: no es que hayamos recortado funciones para que Sheets las entienda, porque Sheets las entiende perfectamente. Es una convención interna de la casa: no usamos funciones volátiles ni funciones que compliquen el recalculado, no hay ni una referencia de una fórmula a otro fichero, y no hay constantes escondidas dentro de las fórmulas —todos los parámetros viven en celda verde, con su valor por defecto declarado—. El efecto secundario es que lo que ves en Excel se recalcula igual en Google Sheets, en LibreOffice y en Numbers, y como los libros guardan dentro los valores ya calculados, también se leen bien en el móvil y en visores que no recalculan.' },
    { q: '¿Sirve si voy a abrir fuera de España, y qué pasa cuando cambie la normativa?', a: 'El marco legal explicado es el español, y lo decimos en la primera pantalla. La estructura económica viaja entera —coste de apertura, capacidad de obrador, sensibilidad al cacao, escandallo, punto muerto, campañas y tesorería son casillas editables— y el vocabulario lleva su equivalencia de Hispanoamérica en la primera mención. El bloque sanitario y de licencias hay que adaptarlo a tu país, y esa adaptación te la ofrecemos como servicio: escríbenos a info@aichef.pro y te decimos qué cambia y qué cuesta. Sobre la normativa: es pago único con actualizaciones incluidas, entras a tu dashboard y descargas la versión nueva sin pagar nada más. Los parámetros legales viven en celda editable con su nota y su fecha, la guía cierra con un anexo normativo con fecha de corte, y las fechas que ya sabemos que se mueven están escritas: el reglamento de deforestación el 30 de diciembre de 2026, el salario mínimo y el convenio a final de 2026, la facturación verificable en enero y julio de 2027 y la obligación del envase reutilizable en enero de 2027.' },
  ],

  cta: {
    heading: 'Decide Antes de Firmar, No Después',
    subtitle: 'El orden de las decisiones, las herramientas que hacen tus números y los documentos que te piden. Todo lo que hay que resolver antes de abrir una bombonería con obrador.',
    items: [
      'Guía completa PDF + DOCX: 20 capítulos y anexo normativo con fecha de corte (111 páginas)',
      '9 herramientas Excel con fórmulas vivas y todas las casillas editables',
      'Capacidad y clima del obrador: si ese local sirve, qué aire necesita y cuántos bombones al día aguanta',
      'Coste de apertura por escenarios, con traspaso frente a obra nueva a cinco años',
      'Denominaciones legales del cacao y escandallo por molde con la merma de templado dentro',
      'Sensibilidad al precio del cacao, campañas y valle del año, y plan financiero a 3 años',
      'Bonus: business plan modelo relleno y 12 decisiones de apertura resueltas (34 páginas)',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'CÓMO MONTAR UNA CHOCOLATERÍA BOUTIQUE & ATELIER — 65 EUR',

  // §7.1: NINGÚN enlace a las guías hermanas «Cómo Montar» mientras no entreguen lo que
  // anuncian. Los cuatro cross-sell son bidireccionales (los mismos cuatro productos
  // enlazan de vuelta a esta guía desde sus propios footerLinks, con el label EXACTO que
  // exige nombre-gate.py). Las tres páginas de rol /usos/ del nicho también enlazan de
  // vuelta con el slug en primera posición de sus productIds.
  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-chocolateria', label: 'Kit Tareas Chocolatería' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/pack-appcc', label: 'Pack Plantillas APPCC' },
    { href: '/guia-food-cost-ingenieria-menu', label: 'Guía Food Cost + Ingeniería de Menú' },
    { href: '/usos/rol/chocolatero-bombonero', label: 'IA para Chocolatero y Bombonero' },
    { href: '/usos/concepto/chocolateria-bomboneria', label: 'IA para Chocolatería y Bombonería' },
    { href: '/usos/consultoria/chocolatero-consultor', label: 'IA para Chocolatero Consultor Pro' },
    { href: '/productos-digitales', label: 'Todos los Productos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Versión 1.0 · septiembre 2026',

  alreadyBought: {
    product: 'guia-chocolateria-obrador',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  // D1: sin aggregateRating y sin review. El template no los emite si no están.
  schema: {
    productName: 'Cómo Montar una Chocolatería Boutique & Atelier',
    productDescription: 'Dossier completo de apertura de una chocolatería artesanal con obrador en España: 20 capítulos y un anexo normativo con fecha de corte que recorren la elección del local, el clima del obrador, el coste de apertura, la maquinaria de templado, las licencias y el registro sanitario, las denominaciones legales del cacao, el escandallo por molde con la merma de templado, la vida útil de los rellenos, el precio del cacao, las campañas del año y el plan financiero a tres años. Incluye 9 herramientas Excel con fórmulas vivas, un business plan modelo relleno y 12 decisiones de apertura resueltas.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    faqs: [
      { q: '¿Esto no está gratis en Google?', a: 'La información suelta sí está, y por eso se contradice: las fuentes gratuitas que hemos revisado una a una dan cifras de arranque que se separan por un factor diez para el mismo negocio, y la única guía española de 2026 exige un requisito legal que dejó de existir en 2010. Lo que no está en Google es el orden en el que se toman las decisiones y nueve Excel donde metes TUS metros, TU carta y TU precio de cobertura y sale TU cifra, con la hipótesis escrita al lado.' },
      { q: '¿En qué se diferencia del Kit de Tareas Chocolatería de 12 €? ¿Necesito los dos?', a: 'El Kit te dice qué hacer cada día cuando ya has abierto: templado, moldeado, vitrina, campañas y caja. Esta guía es todo lo que hay que decidir antes de abrir: el local, el clima del obrador, la inversión, el papeleo, cómo puedes llamar a lo que vendes y los números. Si vas a abrir, la guía es lo primero y el Kit es lo que usarás desde el día uno.' },
      { q: '¿Me sirve si quiero empezar desde casa?', a: 'Sí, y es donde más aporta. El artículo 13.8 del Real Decreto 1021/2022 lista cinco letras de alimentos que pueden elaborarse en una vivienda particular y el chocolate no aparece por defecto en ninguna, pero la quinta dice «otros alimentos que las autoridades competentes de las comunidades autónomas permitan en sus territorios»: la puerta no está cerrada, está en tu comunidad. La guía te dice cómo preguntarlo, a quién y con qué palabras, y el checklist legal trae una hoja dedicada a esa ruta con la casilla de tu comunidad.' },
      { q: '¿Cuánto cuesta montar una chocolatería de verdad?', a: 'No te damos un número: te damos el modelo que produce el tuyo, porque depende de tus metros, de tu plaza, del estado del local y de con qué máquina arrancas. Lo que sí traemos verificado, proveedor a proveedor y con su fecha, es el núcleo de máquina: del orden de 5.700 a 5.900 € con una atemperadora de sobremesa y de 24.000 a 24.300 € con una continua, los dos como rangos de BASE MIXTA de impuestos, útiles para dimensionar la compra de maquinaria y no como presupuesto de apertura ni cifra fiscal. Las demás partidas las presupuestas tú en la calculadora, con la columna de impuesto línea a línea.' },
      { q: '¿Qué pasa cuando sube el cacao?', a: 'Hay un libro de Excel entero para eso: el cacao cotizaba por encima de 10.300 €/t el 2 de enero de 2025 y a 4.956 €/t el 2 de enero de 2026, y aun así el precio del chocolate subió un 17,7 % durante 2025 — la cobertura no baja cuando baja la bolsa. El precio de tu cobertura vive en celda verde, la hoja de sensibilidad te dice qué escenario rompe primero cada referencia, y el capítulo te da los cuatro caminos con su número: subir precio, bajar gramaje, cambiar de cobertura o aceptar menos margen.' },
      { q: '¿Y el reglamento europeo de deforestación? ¿Me afecta si compro cobertura europea?', a: 'Sí, y hay que separar dos figuras que la norma distingue: el «operador», que introduce el producto en el mercado de la Unión, y el «operador posterior» del artículo 2, punto 15 ter, que lo comercializa después. Si tu cobertura llega ya comercializada en la Unión y amparada por una declaración de diligencia debida eres operador posterior, y el aplazamiento del artículo 38.3 no te alcanza: tu fecha es el 30 de diciembre de 2026. En la práctica guardas los datos de tus proveedores y de tus clientes y pides el número de referencia de la declaración únicamente a los proveedores que sean operadores; el Excel trae el árbol que lo resuelve proveedor a proveedor.' },
      { q: '¿Cubre la chocolatería de taza y churros, tipo San Ginés?', a: 'Como variante, no a fondo, y preferimos decirlo antes de que pagues: es otro negocio, porque fríe, y con la freidora vuelven la salida de humos, el gas y las comidas preparadas. El anexo de la Ley 12/2012 incluye el epígrafe 644.5, «comercio al por menor de bombones y caramelos», que te faculta para fabricar bombones y caramelos en tu propio establecimiento siempre que los vendas en tus propias dependencias de venta. Lo que cubrimos a fondo es la chocolatería artesanal con obrador; para la de taza tienes el epígrafe del capítulo 1 y una columna de escenario en la calculadora y en la cuenta de resultados.' },
      { q: '¿Y si quiero hacer bean-to-bar?', a: 'Entra como variante, con su columna de inversión, su epígrafe en el capítulo de cacao y dos frentes normativos que la bombonería corriente no tiene: partiendo del grano eres operador a efectos del reglamento de deforestación, con diligencia debida completa, y tostar el grano obliga a mirar el catálogo de actividades potencialmente contaminadoras de la atmósfera, una calificación que hay que consultar con tu comunidad y no dar por hecha. Lo que no te damos es un precio del tren bean-to-bar: no existe precio público verificable, así que en su lugar tienes la lista de la compra y las preguntas que hay que hacerle a cada fabricante.' },
      { q: '¿Sustituye al proyecto técnico o a la gestión de licencias?', a: 'No, y hay que decirlo arriba: eso lo firma un técnico y no hay atajo. Tampoco encontrarás aquí un precio de proyecto, porque ninguna de las ingenierías que revisamos publica su tarifa y preferimos dejar el hueco antes que rellenarlo con un número inventado. Lo que hace la guía es que llegues a esa reunión sabiendo qué pedir, qué preguntar y qué parte del expediente depende de ti, y que no hayas firmado un alquiler antes de saberlo.' },
      { q: 'Mi ayuntamiento es distinto. ¿Me sirve igual?', a: 'No existe ninguna guía que dé la ordenanza de los más de ocho mil municipios que hay en España, y ésta tampoco la da: no hemos abierto ninguna ordenanza municipal. Lo que sí da es el marco estatal y europeo verificado con su norma, su artículo y su enlace, más la lista exacta de qué preguntar en tu ayuntamiento y en qué orden. Y un dato estatal que cambia la conversación: el artículo 3.1 de la Ley 12/2012 impide a las administraciones exigir licencia previa de instalación, de funcionamiento o de actividad hasta 750 m², y su anexo incluye el epígrafe del comercio al por menor de bombones y caramelos.' },
      { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí, y no porque hayamos recortado funciones: Sheets las entiende perfectamente. Es una convención interna de la casa: no usamos funciones volátiles, no hay ni una referencia de una fórmula a otro fichero y no hay constantes escondidas dentro de las fórmulas, porque todos los parámetros viven en celda verde con su valor por defecto declarado. El efecto secundario es que lo que ves en Excel se recalcula igual en Google Sheets, en LibreOffice y en Numbers, y como los libros guardan dentro los valores ya calculados también se leen bien en el móvil.' },
      { q: '¿Sirve si voy a abrir fuera de España, y qué pasa cuando cambie la normativa?', a: 'El marco legal explicado es el español, y lo decimos en la primera pantalla. La estructura económica viaja entera en casillas editables y el vocabulario lleva su equivalencia de Hispanoamérica en la primera mención; el bloque sanitario y de licencias hay que adaptarlo a tu país, y esa adaptación te la ofrecemos como servicio en info@aichef.pro. Sobre la normativa: es pago único con actualizaciones incluidas, los parámetros legales viven en celda editable con su nota y su fecha, y las fechas que ya sabemos que se mueven están escritas — el reglamento de deforestación el 30 de diciembre de 2026 y la obligación del envase reutilizable en enero de 2027.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Cómo Montar una Chocolatería Boutique & Atelier', item: 'https://aichef.pro/guia-chocolateria-obrador' },
    ],
  },
};

export default data;
