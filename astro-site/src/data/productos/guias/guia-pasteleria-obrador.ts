// guia-pasteleria-obrador.ts — LÍNEA GUÍAS «Cómo Montar», producto 48 (2026-09-10).
//
// Landing NATIVA en Astro (no hay página SPA de la que portar copy). Fuentes del copy:
//   · scripts/productos-digitales/guia-pasteleria-SPEC.md (§0 ficha, §1 decisiones,
//     §2 entregables, §4 índice, §7 canales, §10 Stripe)
//   · scripts/productos-digitales/auditorias/guia-pasteleria-RESEARCH-2026-09-09.md
//     (§12.2 copy, §14 las FAQ de compra)
//
// REGLAS DE COPY QUE ESTE FICHERO CUMPLE (no relajar al editarlo):
//  · D6 — UN SOLO NOMBRE VISIBLE: «Cómo Montar una Pastelería», idéntico en el H1
//    (hero.titlePre + hero.titleGold), en schema.productName, en el name.es de
//    src/data/products-catalog.ts, en la tarjeta del hub, en los footerLinks cruzados
//    de las fichas afines y en el asunto del correo. «con obrador» es SUBTÍTULO, nunca
//    un nombre alternativo. Lo ata scripts/productos-digitales/nombre-gate.py.
//  · D1 — producto nuevo → SIN `priceOld` ni `discountBadge` (no existe «precio anterior
//    de 30 días»: art. 20 de la Ley 7/1996 en la redacción del RDL 24/2021), SIN
//    `aggregateRating`, SIN `review` y con `testimonials.items: []`. No ha vendido una
//    unidad; el template oculta la sección con el array vacío.
//  · D19 — NI UN ENLACE a las otras guías «Cómo Montar» hasta que entreguen lo que
//    prometen (calendario S4-S9). Por eso `footerLinks` sólo cruza a kit-tareas-pasteleria,
//    kit-escandallos, pack-appcc y la Guía Food Cost, y por eso la FAQ 7 del research
//    («¿qué diferencia hay con la Guía de Panadería?») NO entra.
//  · D20 — `__PAGINAS__` y `__PAGINAS_BONUS__` son TOKENS: se sustituyen por las páginas
//    MEDIDAS con PyMuPDF cuando estén construidos el PDF de la guía y el del bonus 2.
//    NO publicar con el token puesto; lo verifica paginas-gate.py --only guia-pasteleria-obrador.
//  · D26 — la FAQ de compatibilidad NO da la razón falsa («las prohibimos para que
//    funcione en Sheets»): Sheets implementa las siete funciones. La razón real es
//    interna (estabilidad del recalculado, caché de fórmulas, volatilidad y legibilidad).
//  · D-copy / §12.3 — sin siglas españolas (RGSEAA, APPCC, BOE) en el hero ni en los
//    titulares de capítulo; el marco legal explicado es el ESPAÑOL y se dice arriba;
//    la FAQ ofrece la adaptación como servicio a quien abre fuera de España.
//  · Declaración en negativo ARRIBA, no en la FAQ: «no es un recetario ni un curso de
//    técnica pastelera, y no sustituye al proyecto técnico visado» (corta devoluciones).
//  · CERO cifras inventadas. Las únicas cifras de mercado admitidas son las verificadas
//    en el research con fuente y fecha: la horquilla 15.000-200.000 € de las fuentes
//    gratuitas (factor 13), el proyecto técnico de obrador a 1.800-2.800 € + IVA y la
//    tramitación desde 1.690 € + IVA en Madrid (estudio-l.es, consultado el 10-09-2026).
//    Los `desc` de los capítulos describen QUÉ SE DECIDE, sin cifras.
//  · D30 — cripto encendida desde el nacimiento: no hay nada que tocar aquí ni en el
//    wrapper. GuiaLandingPage.astro monta las tres puertas de CryptoPayButton solas
//    cuando `cryptoEnabledFor('guia-pasteleria-obrador')` da true (env CRYPTO_PRODUCTS).
import type { GuiaData } from './types';

const data: GuiaData = {
  slug: 'guia-pasteleria-obrador',
  stripeEnvKey: 'VITE_STRIPE_PAYMENT_LINK_GUIA_PASTELERIA_OBRADOR',

  seo: {
    title: 'Cómo Montar una Pastelería | Obrador, Licencias y Números',
    description: 'Para quien va a abrir una pastelería en España: local, inversión, licencias y registro sanitario, escandallo, campañas y plan financiero. 20 capítulos y 8 Excel.',
    keywords: 'montar una pastelería, cómo montar una pastelería, obrador de pastelería, requisitos obrador pastelería, obrador en casa, obrador compartido, licencia de obrador, maquinaria de pastelería, escandallo de pastelería, plan de negocio pastelería, traspaso de pastelería, abrir una pastelería, pastelería artesanal, AI Chef Pro',
    ogImage: 'https://aichef.pro/og-guia-pasteleria-obrador.jpg',
  },

  hero: {
    badge: 'Para quien AÚN no ha abierto: lo que hay que decidir antes de firmar nada',
    titlePre: 'Cómo Montar una ',
    titleGold: 'Pastelería',
    subtitleLine: 'Obrador, licencias y números: el dossier completo de apertura',
    description: 'No te enseña a hacer pasteles. Te dice qué decidir y en qué orden: si ese local sirve, cuánto necesitas de verdad, qué te pide cada administración, cuánto tienes que cobrar y si aguantas Reyes. Esto no es un recetario ni un curso de técnica pastelera, y no sustituye al proyecto técnico visado.',
    checkItems: [
      'Guía completa PDF + DOCX editable: 20 capítulos y un anexo normativo con fecha de corte (__PAGINAS__ páginas)',
      '8 herramientas Excel con fórmulas vivas: capacidad de obrador y ficha de visita al local, coste de apertura, campañas del año, carta y escandallo, plan financiero a 3 años, licencias, equipamiento y proveedores, y turnos con coste de personal',
      'El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes',
      'El marco legal explicado es el español, con su norma, su artículo y el día en que se comprobó. Todas las casillas de los Excel son editables',
      'Bonus 1: el business plan modelo, relleno con el caso completo, en DOCX editable',
      'Bonus 2: 12 decisiones de apertura resueltas (__PAGINAS_BONUS__ páginas)',
    ],
    ctaLabel: 'COMPRAR GUÍA — 65 EUR',
    avatarAltPrefix: 'Professional',
  },

  // D1: sin priceOld ni discountBadge. Producto nuevo: no hay «precio anterior».
  pricing: {
    price: '65 EUR',
    heroNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    buyBoxNote: 'Pago único · acceso vitalicio · actualizaciones incluidas',
    bonusTotalLabel: 'Incluido en el precio: la guía, las 8 herramientas Excel y los dos bonus',
  },

  images: {
    gallery: [
      '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-1.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-2.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-3.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-4.jpg',
      '/lovable-uploads/ai-gallery/guia-pasteleria-5.jpg',
    ],
    whyBg: '/lovable-uploads/ai-gallery/guia-pasteleria-2.jpg',
    buyBoxBg: '/lovable-uploads/ai-gallery/guia-pasteleria-hero.jpg',
    ctaBg: '/lovable-uploads/ai-gallery/guia-pasteleria-4.jpg',
  },

  grid: {
    countGold: '20',
    headingRest: ' Capítulos + 8 Plantillas + 2 Bonus',
    subtitle: 'Criterio y decisión, no teoría. Cada capítulo se apoya en una de las ocho herramientas Excel del pack y sus tablas salen de las celdas de esos ficheros, no de ejemplos inventados. Cierra un anexo normativo con fecha de corte, para que sepas qué estaba vigente el día que se escribió y qué fechas ya sabemos que se mueven. Escrito por un chef y consultor gastronómico que lleva desde 2010 acompañando aperturas.',
    chapters: [
      { icon: 'Layers', num: '01', title: 'Qué Negocio Estás Montando: las 11 Variantes y Cuál te Toca', desc: 'Las once formas de vender pastelería comparadas por inversión, metros y personal, el mapa de problema a capítulo y a herramienta, qué es cross-sell y qué no vas a encontrar aquí, y el glosario con sus equivalencias de Hispanoamérica.' },
      { icon: 'Users', num: '02', title: 'El Cliente y la Plaza: Quién Compra Pastelería y Cuándo', desc: 'Contra quién compites de verdad, qué parte del gasto en dulce pasa por el comercio especializado y por qué un obrador no debería intentar competir en volumen.' },
      { icon: 'CakeSlice', num: '03', title: 'La Carta de Apertura: 30 Referencias y Por Qué Esas', desc: 'Cómo se decide un surtido de apertura con criterio de margen, qué papel juega cada familia de producto y por qué el margen no se reparte igual entre ellas.' },
      { icon: 'Banknote', num: '04', title: 'Cuánto Cuesta Abrir: el Coste de Apertura, Partida a Partida', desc: 'Por qué las cifras publicadas se contradicen y qué hipótesis lleva cada una, los tres escenarios de obra, la columna de impuesto que descuadra el presupuesto si falta, y el colchón de tesorería como partida y no como propina.' },
      { icon: 'Layout', num: '05', title: 'El Local: Metros, Zonas y la Ficha de Visita', desc: 'Las siete zonas obligatorias y el principio de marcha adelante, qué pide el reglamento en superficies y lavamanos, la potencia que se llevan los hornos, la altura libre y la carga del forjado.' },
      { icon: 'DoorOpen', num: '06', title: 'Antes de Firmar el Alquiler: el Capítulo Que Ahorra el Dinero', desc: 'El cribado eliminatorio del local, la salida de humos hasta cubierta y la comunidad de propietarios como riesgo real, qué preguntar en el ayuntamiento, y las tres puertas: local nuevo, traspaso o franquicia con la renta a cinco años.' },
      { icon: 'Snowflake', num: '07', title: 'El Obrador por Dentro: Frío, Calor y Flujo de Trabajo', desc: 'Por qué la pastelería gira sobre el frío negativo y no sobre el horno, qué papel juegan abatidor, fermentación controlada y congelación, y cuál de tus equipos marca el ritmo de todo lo demás.' },
      { icon: 'Wrench', num: '08', title: 'Maquinaria: Qué Compras, Qué Alquilas y Qué Esperas a Tener', desc: 'Precios reales por gama con marca y modelo, la trampa de comparar precios publicados con y sin impuesto, cuándo la segunda mano compensa y qué plazos de entrega mueven tu fecha de apertura.' },
      { icon: 'ShieldCheck', num: '09', title: 'Licencias, Sanidad y Registro: el Camino Completo', desc: 'Qué trámite te toca según a quién vendas, cuándo basta la vía autonómica y cuándo aparece el registro estatal, qué pasa con la central y sus sucursales, el cuadro de cuatro comunidades como ejemplo y la ruta desde casa con su lista blanca.' },
      { icon: 'ClipboardCheck', num: '10', title: 'Seguridad Alimentaria, Alérgenos y Formación: Qué Pide la Inspección', desc: 'La carpeta que hay que tener el día que entra el inspector: plan de autocontroles con responsable designado por su nombre, registro de formación del equipo, alérgenos de obrador frente a los de vitrina y qué exige de verdad decir «sin gluten».' },
      { icon: 'Truck', num: '11', title: 'Proveedores: Materia Prima, Packaging y Plazos', desc: 'Los proveedores verificados por categoría con su enlace, cómo pedir tres presupuestos comparables, cuánto pesa el packaging en el coste y cómo modelar la volatilidad de la mantequilla y el cacao en vez de fijar un precio que caduca.' },
      { icon: 'Calculator', num: '12', title: 'Escandallo y Precios: Por Qué la Mano de Obra Manda', desc: 'La unidad de costeo es la tanda, no la pieza. Coste de la hora de obrador imputado por pieza, margen y precio por ración en la tarta por encargo, y el antídoto numérico al miedo a subir precios.' },
      { icon: 'UserCog', num: '13', title: 'El Equipo: Cuántos, Qué Perfiles y Qué Cuestan', desc: 'Los grupos del convenio y sus áreas funcionales, cuándo manda el convenio sobre el salario mínimo, el salto de bruto a coste de empresa con la seguridad social dentro, y el problema estructural de encontrar personal.' },
      { icon: 'Clock', num: '14', title: 'Turnos de Madrugada y Jornada Legal', desc: 'Cómo se registra hoy la jornada y qué se está tramitando, el turno de obrador frente al de despacho y cómo se solapan en el pico, la prevención de riesgos del obrador, y el horario del dueño como decisión de vida.' },
      { icon: 'CalendarRange', num: '15', title: 'Los Seis Picos del Año', desc: 'Cuánto multiplica cada campaña con el mismo equipo, cuánto pesa sobre el año, qué déficit de capacidad te deja, qué refuerzo necesitas y cuánta tesorería inmoviliza el stock de temporada.' },
      { icon: 'PartyPopper', num: '16', title: 'Encargos y Comuniones Como Línea de Negocio', desc: 'Captación y demanda validada, anticipo y señal, calendario de entrega y riesgo de anulación, y qué encargos se aceptan y cuáles no cuando todavía no tienes histórico.' },
      { icon: 'Store', num: '17', title: 'Canales: Mostrador, Venta a Empresas, Online y Envío', desc: 'Cuánto cobras al contado y cuánto a crédito, en qué momento vender a otros comercios cambia tu obligación de registro, qué información hay que dar antes de la compra en la venta a distancia y qué producto viaja y cuál no.' },
      { icon: 'TrendingUp', num: '18', title: 'El Plan Financiero y el Dinero Hasta el Punto de Equilibrio', desc: 'Cuenta de resultados a tres años con estacionalidad mensual y rampa de arranque, punto muerto con una sola regla de margen, el sueldo del propietario como renglón propio y la rentabilidad honesta del sector.' },
      { icon: 'Wallet', num: '19', title: 'Financiación, Impuestos, Envases y Tesorería del Arranque', desc: 'Servicio de deuda, qué tipo impositivo le toca a cada familia de producto, las fechas de la facturación verificable que ya están puestas en el calendario, la obligación de envases y de qué estás exento exactamente en la ley de desperdicio.' },
      { icon: 'Rocket', num: '20', title: 'Cronograma, Apertura y los Primeros 90 Días', desc: 'Ruta crítica y fecha de apertura, por qué conviene abrir fuera de pico y llegar rodado a Reyes, la libertad de horarios como decisión comercial del día uno, y qué se mide en el mes cero y en el mes tres con responsable y fecha.' },
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
      { icon: 'Shuffle', title: 'Lo Que Se Decide Antes de Abrir', desc: 'El Kit de Tareas Pastelería te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes: si ese local sirve, cuánto necesitas de verdad, qué papel te toca y a cuánto tienes que vender. No se pisan: aquí no encontrarás ni el plan de producción semanal ni el registro de encargos, porque ya existen y se citan por su nombre.' },
      { icon: 'FileSpreadsheet', title: 'Tres Herramientas Que No Están en Ningún Otro Sitio', desc: 'La capacidad del obrador (cuántas piezas al día permite el equipo que estás a punto de comprar), el comparador de traspaso frente a obra nueva con la renta a cinco años, y la economía de las campañas: cuánto pesa cada pico, qué refuerzo pide y cuánta caja inmoviliza. No están en el resto del catálogo ni en la competencia de pago que hemos revisado producto a producto.' },
      { icon: 'ShieldCheck', title: 'Cada Dato Legal con su Artículo y su Fecha', desc: 'Ninguna afirmación normativa va suelta: cada celda y cada tabla llevan la norma, el artículo, el enlace y el día en que se comprobó, y el anexo final tiene fecha de corte con las cuatro fechas que ya sabemos que se mueven. El marco explicado es el español; todas las casillas de los Excel son editables.' },
      { icon: 'AlertTriangle', title: 'Y Lo Que Esta Guía No Hace', desc: 'No sustituye al proyecto técnico visado ni a la gestión de licencias: eso lo firma un técnico, y aquí verás cuánto cuesta. No te garantiza que tu ayuntamiento diga que sí, y no promete clientes ni visibilidad. Lo que hace es que llegues a cada reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar, y que no firmes un alquiler antes de tiempo.' },
    ],
  },

  author: {
    bio: 'CEO de AI Chef Pro y fundador de ChefBusiness Group. En cocina desde los 17 años y consultor gastronómico desde 2010. Ha asesorado la apertura de más de 200 establecimientos, incluyendo restaurantes con Estrella Michelin y Soles Repsol en España y Europa.',
    badge3: '+200 aperturas',
  },

  bonus: {
    subtitle: 'Además de la guía PDF + DOCX y de las 8 herramientas Excel con fórmulas vivas, el pack incluye estos dos documentos',
    layout: 'single',
    items: [
      {
        icon: 'FileText',
        label: 'BONUS 1',
        title: 'Business Plan Modelo, Relleno',
        value: 'Incluido en el pack',
        desc: 'El caso completo de la pastelería de ejemplo escrito en el formato que pide un banco o una línea de financiación pública: resumen ejecutivo, mercado y plaza, concepto y carta, plan de operaciones con obrador, capacidad y plantilla, plan financiero a tres años y análisis de riesgos con escenarios. En DOCX editable y con las cifras cuadradas contra el plan financiero del pack, celda a celda.',
        image: '/lovable-uploads/ai-gallery/guia-pasteleria-3.jpg',
      },
      {
        icon: 'GraduationCap',
        label: 'BONUS 2',
        title: '12 Decisiones de Apertura Resueltas',
        value: 'Incluido en el pack',
        desc: 'Doce decisiones reales con su contexto, sus opciones, el criterio, la celda del Excel que la resuelve y la norma con su fecha cuando la hay: local con obrador o obrador aparte, comprar el abatidor o esperar, abrir con veinte referencias o con cuarenta, empezar en casa dentro de la legalidad, aceptar el primer encargo de comunión sin histórico, el primer contrato con otro comercio, o qué hacer con lo que no se vende hoy. En PDF y en DOCX editable (__PAGINAS_BONUS__ páginas).',
        image: '/lovable-uploads/ai-gallery/guia-pasteleria-5.jpg',
      },
    ],
  },

  buyBox: {
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  guarantee: {
    text: 'Si la guía no te sirve para decidir tu local, tus números y tu papeleo con criterio, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones. Tienes 30 días para decidir.',
  },

  // Las 12 FAQ de COMPRA del research §14, menos la 7 («¿qué diferencia hay con la Guía
  // de Panadería?»), que NO entra por D19: no se menciona ninguna guía hermana hasta que
  // entreguen lo que prometen. En su lugar, la de garantía, que es la que cierra la
  // familia. Las de oficio y las de empleo quedan fuera: no son nuestras.
  faqs: [
    { q: '¿Esto no está gratis en Google?', a: 'La información suelta sí está, y por eso se contradice: las fuentes gratuitas que hemos revisado una a una dan entre 15.000 € y 200.000 € para el mismo negocio —un factor 13— y ninguna dice de qué depende ese número, ni cuántos metros, ni qué plaza, ni si el local viene vacío o traspasado. Lo que no está en Google es el orden en el que se toman las decisiones y ocho Excel donde metes TUS metros, TU plaza y TU carta y sale TU cifra, con la hipótesis escrita al lado.' },
    { q: '¿Me sirve si quiero empezar desde casa?', a: 'Sí, y es donde más aporta: hay un capítulo entero y una hoja dedicada a la ruta doméstica, con la lista de lo que la norma estatal permite elaborar en una vivienda, el contador de kilos por semana y el aviso de que tu comunidad autónoma puede haber ampliado esa lista. Y se dice lo que casi nadie dice: hay producto que por defecto NO puedes vender desde casa, empezando por la tarta rellena de nata. Mejor saberlo antes que después de una inspección.' },
    { q: '¿En qué se diferencia del Kit de Tareas Pastelería de 12 €? ¿Necesito los dos?', a: 'El Kit te dice qué hacer cada día cuando ya has abierto: producción, encargos, alérgenos de vitrina, temperaturas, apertura y cierre. Esta guía es todo lo que hay que decidir antes de abrir: el local, la inversión, el papeleo, la carta y los números. Si ya estás abierto, el Kit te vale y esta guía no te hace falta. Si vas a abrir, la guía es lo primero y el Kit es lo que usarás desde el día uno.' },
    { q: '¿Y si ya tengo la pastelería abierta?', a: 'Entonces éste no es tu producto, y preferimos decirlo antes de que pagues. Lo tuyo es la Guía Food Cost + Ingeniería de Menú para los precios y la carta, o los kits operativos para el día a día. Esta guía está escrita para quien AÚN no ha abierto, y la mitad de su valor está en decisiones que tú ya has tomado.' },
    { q: '¿Sustituye al proyecto técnico o a la gestión de licencias?', a: 'No, y hay que decirlo arriba. El proyecto técnico de un obrador cuesta entre 1.800 € y 2.800 € más impuestos, y la tramitación arranca en 1.690 € más impuestos en Madrid (tarifas públicas de estudio-l.es consultadas el 10 de septiembre de 2026): eso lo firma un técnico y no hay atajo. Lo que hace la guía es que llegues a esa reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar, y que no hayas firmado un alquiler antes de saberlo.' },
    { q: 'Mi ayuntamiento es distinto. ¿Me sirve igual?', a: 'Es la primera objeción que pone cualquier técnico, y tiene razón: no existe ninguna guía que dé la ordenanza de los más de ocho mil municipios que hay en España. Lo que da ésta es el marco estatal y autonómico verificado con su artículo y su enlace, un cuadro con cuatro comunidades como ejemplo y cómo encontrar la tuya, y la lista exacta de qué preguntar en tu ayuntamiento y en qué orden. Prometer otra cosa sería mentirte.' },
    { q: '¿Necesito el Pack de Plantillas APPCC si compro esta guía?', a: 'Son cosas distintas y se notan en el momento en que las usas. La guía te da el criterio y el checklist de puesta en marcha: qué tienes que tener preparado el día que venga la inspección. El Pack te da los registros que hay que rellenar y firmar cada día a partir de entonces. La guía no construye ni un registro de autocontrol a propósito, para que no pagues dos veces por lo mismo.' },
    { q: '¿Y el Kit de Escandallos?', a: 'El Kit trae el escandallo unitario de tres elaboraciones de pastelería. La guía trae la carta de apertura completa de treinta referencias con el coste de la hora de obrador imputado, que es lo que decide tu precio de verdad cuando el trabajo pesa más que la materia prima. Las tres primeras coinciden a propósito, para que no veas dos costes distintos del mismo croissant.' },
    { q: '¿Los Excel funcionan en Google Sheets y en Numbers?', a: 'Sí. No usamos fórmulas volátiles ni funciones que dependan del motor de cálculo, y no hay referencias entre libros: lo que ves en Excel se recalcula igual en Google Sheets, en LibreOffice y en Numbers. Todos los parámetros van en celda verde, sin constantes escondidas dentro de las fórmulas, y los libros guardan dentro los valores ya calculados, así que también se leen bien en el móvil y en visores que no recalculan.' },
    { q: '¿Sirve si voy a abrir fuera de España?', a: 'El marco legal explicado es el español, y lo decimos en la primera pantalla. La estructura económica viaja entera —coste de apertura, capacidad de obrador, escandallo, punto muerto, campañas y tesorería son casillas editables— y el vocabulario lleva su equivalencia de Hispanoamérica en la primera mención. El bloque sanitario y de licencias hay que adaptarlo a tu país, y esa adaptación te la ofrecemos como servicio: escríbenos a info@aichef.pro y te decimos qué cambia y qué cuesta.' },
    { q: '¿Qué pasa cuando cambie la normativa?', a: 'Pago único con actualizaciones incluidas: entras a tu dashboard y descargas la versión nueva sin pagar nada. Además, los parámetros legales viven en celda editable con su nota y su fecha, la guía cierra con un anexo normativo con fecha de corte y hay un apartado que enseña a comprobar la vigencia de una norma en un minuto. Y las fechas que ya sabemos que se mueven están escritas: el salario mínimo y el convenio caducan a final de 2026, y el plazo transitorio de Madrid vence en marzo de 2027.' },
    { q: '¿Hay garantía de devolución?', a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.' },
  ],

  cta: {
    heading: 'Decide Antes de Firmar, No Después',
    subtitle: 'El orden de las decisiones, las herramientas que hacen tus números y los documentos que te piden. Todo lo que hay que resolver antes de abrir.',
    items: [
      'Guía completa PDF + DOCX: 20 capítulos y anexo normativo con fecha de corte (__PAGINAS__ páginas)',
      '8 herramientas Excel con fórmulas vivas y todas las casillas editables',
      'Capacidad de obrador y ficha de visita: si ese local sirve y cuántas piezas al día aguanta',
      'Coste de apertura por escenarios, con traspaso frente a obra nueva a cinco años',
      'Licencias y registro sanitario en árbol de decisión, con cronograma y ruta crítica',
      'Carta de apertura de 30 referencias con la hora de obrador imputada, y plan financiero a 3 años',
      'Bonus: business plan modelo relleno y 12 decisiones de apertura resueltas (__PAGINAS_BONUS__ páginas)',
    ],
    ctaLabel: 'SÍ, QUIERO LA GUÍA — 65 EUR',
  },

  stickyLabel: 'CÓMO MONTAR UNA PASTELERÍA — 65 EUR',

  // D19: NINGÚN enlace a las guías hermanas «Cómo Montar» hasta que entreguen lo que
  // prometen. Los cuatro cross-sell son bidireccionales (los mismos cuatro productos
  // enlazan de vuelta a esta guía desde sus propios footerLinks).
  footerLinks: [
    { href: 'https://aichef.pro', label: 'aichef.pro' },
    { href: '/kit-tareas-pasteleria', label: 'Kit Tareas Pastelería' },
    { href: '/kit-escandallos', label: 'Kit de Escandallos Pro' },
    { href: '/pack-appcc', label: 'Pack Plantillas APPCC' },
    { href: '/guia-food-cost-ingenieria-menu', label: 'Guía Food Cost + Ingeniería de Menú' },
    { href: '/productos-digitales', label: 'Todos los Productos' },
    { href: 'mailto:info@aichef.pro', label: 'Contacto' },
  ],

  updateNote: 'Versión 1.0 · septiembre 2026',

  alreadyBought: {
    product: 'guia-pasteleria-obrador',
    label: '¿Ya compraste la guía? Vuelve a entrar al dashboard',
  },

  // D1: sin aggregateRating y sin review. El template no los emite si no están.
  schema: {
    productName: 'Cómo Montar una Pastelería',
    productDescription: 'Dossier completo de apertura de una pastelería con obrador en España: 20 capítulos y un anexo normativo con fecha de corte que recorren la elección del local, el coste de apertura, la maquinaria, las licencias y el registro sanitario, la carta y el escandallo con la mano de obra dentro, el equipo y el convenio, las campañas del año y el plan financiero a tres años. Incluye 8 herramientas Excel con fórmulas vivas, un business plan modelo relleno y 12 decisiones de apertura resueltas.',
    price: '65.00',
    priceValidUntil: '2026-12-31',
    faqs: [
      { q: '¿En qué se diferencia del Kit de Tareas Pastelería de 12 €?', a: 'El Kit te dice qué hacer cada día cuando ya has abierto: producción, encargos, alérgenos de vitrina y temperaturas. Esta guía es todo lo que hay que decidir antes de abrir: el local, la inversión, el papeleo, la carta y los números.' },
      { q: '¿Sustituye al proyecto técnico o a la gestión de licencias?', a: 'No. El proyecto técnico de un obrador y la tramitación de la licencia los firma un técnico, y la guía dice lo que cuestan. Lo que hace es que llegues a esa reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar, y que no firmes un alquiler antes.' },
      { q: '¿Sirve si voy a abrir fuera de España?', a: 'El marco legal explicado es el español. La estructura económica viaja entera en casillas editables y el vocabulario lleva su equivalencia de Hispanoamérica; el bloque sanitario y de licencias hay que adaptarlo, y esa adaptación la ofrecemos como servicio.' },
    ],
    breadcrumb: [
      { name: 'AI Chef Pro', item: 'https://aichef.pro' },
      { name: 'Productos Digitales', item: 'https://aichef.pro/productos-digitales' },
      { name: 'Cómo Montar una Pastelería', item: 'https://aichef.pro/guia-pasteleria-obrador' },
    ],
  },
};

export default data;
