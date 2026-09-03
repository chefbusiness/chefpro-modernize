# LENTE 4 — Voz del cliente y vocabulario por mercado
## Research para «Guía Food Cost + Ingeniería de Menú» (AI Chef Pro)

Fecha de research: 2026-09-03. Autor: subagente de research (Claude), a partir de WebSearch/WebFetch/curl — sin navegador local ni Playwright, según regla del proyecto.

---

## 0. Nota metodológica — léela antes de usar este informe (importante)

El encargo pedía citas literales de **Reddit (r/hosteleria, r/Cocina), foros de Gastroeconomy, grupos de Facebook, LinkedIn, comentarios de YouTube, Quora/Yahoo, reseñas de Amazon/Udemy**. Se ha intentado acceder a los nueve canales. El resultado real, verificado en esta sesión:

| Canal | Resultado | Evidencia |
|---|---|---|
| Reddit (`reddit.com`, `old.reddit.com`) | **Bloqueado a nivel de herramienta.** WebFetch devuelve «Claude Code is unable to fetch from www.reddit.com» / `old.reddit.com`. WebSearch con `site:reddit.com` no devuelve un solo hilo en español sobre food cost/escandallo (sí devuelve resultados genéricos de Wikipedia u otros dominios) | Búsquedas `site:reddit.com r/hosteleria escandallo food cost`, `site:reddit.com "food cost" restaurante`, `reddit.com/r/AskCulinary…`, todas sin resultados reales |
| Quora | **Bloqueado.** `es.quora.com` devuelve HTTP 403 por curl; WebSearch sólo trae hilos en inglés genéricos, ninguno sobre «escandallo» | curl a `es.quora.com/search?q=escandallo` → 403 |
| Facebook (grupos) | **Parcialmente accesible.** Se localizó un post real de pregunta en un grupo (`Yo Soy Camarer@`) pero WebFetch no pudo extraer los comentarios de respuesta (contenido dinámico tras login); curl devuelve 400 | Ver cita FB-1 más abajo |
| Udemy (reseñas) | **Bloqueado.** HTTP 403 tanto por WebFetch como por curl en las dos páginas de curso probadas | `udemy.com/course/ingenieria-del-menu/` → 403 |
| Amazon (reseñas de libros) | **Accesible vía curl con user-agent de escritorio.** Se extrajeron 2 reseñas reales, con nombre, fecha, estrellas y texto completo, del único libro de la categoría con reseñas (4 libros más del mismo nicho en Amazon.es tienen 0 reseñas) | Ver AMZ-1, AMZ-2 |
| YouTube (comentarios) | **No accesible.** Los comentarios se cargan por API asíncrona; WebFetch sólo devuelve el pie de página estático de la SPA de YouTube | — |
| LinkedIn | **Parcialmente accesible** — un artículo público (`LinkedIn Pulse`) sí se pudo leer completo | Ver LI-1 |
| Prensa/blogs especializados con declaraciones reales de hosteleros | **Vía alternativa que SÍ funcionó bien.** El Español, El Cronista (Argentina), Warocol (Colombia), Panca (Perú), Yo Emprendedora (España) citan por nombre a dueños de negocio reales, con fecha | Ver EL-1 a WA-2 |

**Consecuencia para este informe:** de las 9 fuentes pedidas, 4 estaban bloqueadas por completo (Reddit, Quora, Udemy, YouTube-comentarios) y una parcialmente (Facebook). Para no rellenar el hueco con contenido inventado, este informe combina:

1. **Citas primarias verificadas** (10): personas identificables por nombre/apodo/negocio, con URL y fecha — reseñas de Amazon, prensa, un artículo de LinkedIn, una entrevista de blog y un post de Facebook.
2. **Paráfrasis secundarias documentadas** (14): patrones de queja que NO son una cita de un usuario anónimo de foro, sino contenido publicado por blogs/consultores especializados en food cost que describen — con cifras y ejemplos — el mismo problema que se buscaba en foros. Se marcan explícitamente como «fuente secundaria (blog especializado)» para no hacerlas pasar por voz de foro.
3. Dos estadísticas que aparecían en resúmenes de búsqueda («67 % de los restaurantes no conoce su food cost real», «sólo el 2 % aplica escandallos sistemáticamente») **se descartan de este informe**: al intentar verificarlas en la página fuente exacta, una dio error de pago (402) y la otra no contenía el dato al leer el artículo completo. Ninguna de las dos cifras se usa por debajo, ni en el resumen ejecutivo.

Esto es exactamente el hueco a comunicar: **no hay verificación cruda de Reddit/Quora/Facebook/Udemy con las herramientas disponibles en este entorno**; sí hay voz real (nombre + negocio + fecha) por otras cuatro vías, y patrones consistentes en el sector confirmados por múltiples fuentes independientes.

---

## 1. Citas y paráfrasis por dolor (24 entradas, todas con URL)

### Dolor A — «No sé qué precio poner» / desconocimiento del coste real

**A1. [PRIMARIA]** Reseña de 1 estrella, «Cliente Amazon», España, 15 de marzo de 2024, sobre el libro *Ingeniería del Menú* (Rodrigo Riquelme Barros):
> «Este libro no aporta mucho más que Revenue Management del mismo autor. A pesar de la promesa y el precio que es significativamente más alto (…) es un exceso, casi un tercio del total de páginas, dedicadas a explicar matrices básicas.»
Fuente: https://www.amazon.es/Ingenier%C3%ADa-del-Men%C3%BA-restaurante-restaurantes/dp/B0CSYX51GG (reseña visible en la ficha del producto, 15-03-2024)

**A2. [PRIMARIA]** Reseña de 5 estrellas, «Max Valdivia», reseñado en Estados Unidos, 21 de junio de 2024, mismo libro:
> «Un libro muy completo sobre el análisis de la ingeniería del menú. Muchas herramientas para evaluar la carta y no quedarse con la típica matriz BCG.»
Fuente: misma URL que A1.

**A3. [PRIMARIA]** Post real de pregunta en el grupo de Facebook «Yo Soy Camarer@» (grupo abierto de profesionales de hostelería):
> «¿Cómo se hace un buen 'escandallo' en hostelería? ¿Qué...» (título del post; no se pudieron extraer las respuestas — contenido dinámico bloqueado tras login parcial de Facebook).
Fuente: https://www.facebook.com/groups/505159727904496/posts/585071929913275/ — evidencia de que la pregunta básica «cómo se hace un escandallo» se sigue haciendo activamente en comunidades profesionales, no sólo por principiantes que buscan en Google.

**A4. [secundaria — blog especializado]** Sobre por qué el food cost varía cada mes: «Si tu receta tiene costes desactualizados, el food cost calculado no refleja la realidad. Actualiza los precios de tus insumos al menos una vez al mes, o cada vez que llega un pedido a un precio distinto.» — patrón confirmado en múltiples blogs de gestión (qamarero.com, purohospitality.com, chejefe.com) al buscar «me sale distinto cada mes».
Fuente representativa: https://qamarero.com/blog/food-cost-restaurante/

**A5. [secundaria — blog especializado]** Sobre la brecha entre food cost teórico y real: «Si tu food cost teórico es del 28 % pero el real sale al 34 %, estás regalando un 6 % de tus ingresos cada mes. En un restaurante que factura 50.000 €/mes, son 3.000 € que desaparecen sin saber dónde.»
Fuente: https://qamarero.com/blog/food-cost-restaurante/

### Dolor B — Estandarización: «cada cocinero hace la receta a su manera»

**B1. [secundaria — blog especializado]** «No puedes costear un plato si cada cocinero añade "un puñado" de cebolla o "un chorro" de aceite (…) si cada cocinero sirve 200 g de proteína cuando la receta pide 175 g, añade un 14 % al coste sin que quede registrado en ningún sitio.»
Fuente: patrón repetido en varios blogs al buscar variabilidad de food cost por falta de estandarización; representativo: https://gastronomadas.com.mx/costeo-de-recetas/

**B2. [secundaria — blog especializado]** Sobre el registro de mermas: «Si cada cocinero limpia el producto de forma distinta, tus costes fluctuarán a diario» — el control de mermas depende de procesos estandarizados, no sólo de fórmulas.
Fuente: https://envanature.com/blog/control-mermas-restaurantes/

### Dolor C — Proveedores que suben precios sin aviso

**C1. [PRIMARIA]** Agus, hostelero e influencer conocido en redes como @Eldel_Bar (España), citado en El Español, 26 de octubre de 2025:
> «Hace cinco años cobraba la caña a 1,60 euros, ahora a 2 euros, pero el barril me cuesta el doble.»
> «Tenemos que pagar la Seguridad Social, impuestos, el salario de los empleados, a los proveedores, la luz, el agua, los alquileres y una cantidad de cosas tan grande que al final a nosotros se nos queda un sueldo normal.»
Fuente: https://www.elespanol.com/sociedad/20251026/hostelero-estalla-subida-precios-cobraba-cana-ahora-barril-cuesta-doble/1003743982533_0.html (26-10-2025)

**C2. [PRIMARIA]** Dueño de una cervecería, hamburguesería y local vegano en Palermo (Buenos Aires, Argentina), citado en El Cronista, 16 de agosto de 2023:
> «La papelería subió un 27 %; los artículos de limpieza, 26 %; el pollo, 18 %; la carne, 38 %; las hamburguesas, 50 %; los aderezos, 30 %; y las aceitunas... ¡un 100 %!» / «Hoy me voy a sentar a hacer números para decidir cuánto aumentamos.»
Fuente: https://www.cronista.com/negocios/cartas-de-restaurantes-sin-precios-y-subas-de-hasta-el-100-en-insumos-se-termina-el-veranito-de-la-gastronomia/ (16-08-2023)

**C3. [PRIMARIA]** Dueño de una hamburguesería distinta, también en Palermo, mismo artículo:
> «Me parece una locura subir un 100 % la carta. No creo que el mercado esté preparado para eso.»
Ejemplos de subida real que reporta: hamburguesa simple, de $2.200 (mayo) a $3.300 (agosto); papas con queso/panceta, de $2.000 a $3.350 en 3 meses.
Fuente: misma URL que C2.

**C4. [PRIMARIA]** CEO de una cadena de cafeterías, mismo artículo de El Cronista:
> «Es muy difícil precisar los aumentos en este momento, en el que nos llegan desde comienzos de semana dos listas de precios de proveedores» (una por la mañana y otra por la tarde, en función del dólar).
Fuente: misma URL que C2.

**C5. [PRIMARIA]** Luz Stella García, propietaria de un restaurante en el barrio Barranquillita (Barranquilla, Colombia):
> «Subió el salario de los trabajadores, las verduras y, en general, todos los insumos están demasiado caros, especialmente a comienzo del año.»
Fuente: https://warocol.com/blog/como-calcular-el-food-cost

**C6. [PRIMARIA]** Diana Marcela Vélez, cafetería en el barrio 12 de Octubre (Bogotá, Colombia), misma fuente:
> «Todo está muy caro y tengo que sostener el negocio sin echar a ningún empleado.»
Fuente: https://warocol.com/blog/como-calcular-el-food-cost

### Dolor D — Mermas

**D1. [secundaria — blog especializado]** Sobre el ablandado de carnes que infla el coste real: «Una queja constante del sector es la tendencia de los productores a ablandar las carnes, lo que implica inyectar agua, sales o fosfatos, provocando que el producto encoja al cocinarlo — se paga un porcentaje de agua al precio de la carne.»
Fuente: patrón documentado en https://apetitoenlinea.com/mermas-una-indeseable-realidad-en-las-cocinas/

**D2. [secundaria — blog especializado]** «El error más común es comprar por rutina en lugar de por demanda. Es crucial analizar el histórico de ventas antes de hacer el pedido» — el control de mermas se rompe primero en compras, no en cocina.
Fuente: https://lafamigliarestaurantes.com/blog/control-de-mermas-en-un-restaurante/

### Dolor E — La carta demasiado larga

**E1. [secundaria — caso de negocio con cifras]** Restaurante criollo en Miraflores (Lima, Perú), sin nombre publicado, citado como caso en un blog especializado: redujo su carta de **48 platos a 28**, reorganizó la distribución y ajustó precios usando ingeniería de menú. Resultado: el ticket promedio subió de S/ 38 a S/ 44 (**+16 %**) y el food cost bajó del **34 % al 29 %**. «Menos platos, más ganancia.»
Fuente: https://www.panca.pe/blog/como-crear-carta-menu-restaurante-rentable/

**E2. [secundaria — blog especializado]** «Una cocina que gestiona 35 platos es notablemente más eficiente que una con 80: menos desperdicio de preparación, menos ingredientes especializados, servicio más rápido y menor coste de mano de obra por cliente.»
Fuente: https://intermenu.io/es/blog/reducir-platos-carta-es

### Dolor F — El delivery se come el margen

**F1. [secundaria — blog especializado, con ejemplo numérico]** «Un comisión del 25 % al 30 % por pedido puede convertir un plato rentable en uno que apenas cubre costes. Ejemplo concreto: un restaurante peruano vendía Lomo Saltado a S/ 38 en sala con 62 % de margen, pero el mismo precio en Rappi dejaba sólo 19 % de margen; al ajustar a S/ 45 en la app, el margen subió a 38 %.»
Fuente: https://gestionrestoba.com/la-trampa-de-las-apps-de-delivery-como-calcular-si-realmente-ganas-dinero-tras-la-comision-del-20-30/

**F2. [secundaria — blog especializado, México]** «Es común que un restaurante venda mucho por Uber Eats y a fin de mes no le quede nada: hizo el volumen, ensució la cocina, pagó los insumos, y la comisión se quedó con la ganancia. Si cada pedido te dejaba un 20 % de ganancia limpia, una comisión del 28 % no reduce tu ganancia un 28 %: puede borrarla por completo.»
Fuente: https://olaclick.com/es/pos/comisiones-de-rappi-y-uber-eats-en-mexico-cuanto-pierde-tu-restaurante/

### Dolor G — Pastelería / obrador

**G1. [PRIMARIA]** Ana Aboli, repostera y fundadora de «Confeti En Los Bolsillos» (España), entrevistada en Yo Emprendedora:
> «Aún no puedo vivir de Confeti y tengo que seguir compaginándolo con lo que me da de comer.»
> «Valórate más y valora tu trabajo. Si regalas tu trabajo, ni te valoras a ti, ni valoras lo que haces.»
Fuente: https://yoemprendedora.es/entrevista-confetienlosbolsillos-yoemprendedora/

**G2. [PRIMARIA]** @adiercakes, negocio de tortas/pasteles personalizados (cifras en soles → mercado peruano/latinoamericano), en el pie de un vídeo tutorial de TikTok sobre costeo:
> «Si no sabes cómo sacar el costo de tus pasteles, esta es una explicación básica y rápida para que puedas estar seguro de que no estás perdiendo y tampoco estás dando un costo elevado (…) cuando tengas todo esto, le sumarás los gastos extras como empaque, caja, base y el delivery, teniendo la suma total de todo, le agregas lo que tú crees que vale tu trabajo.»
Fuente: https://www.tiktok.com/@adiercakes/video/7414535018447523077

**G3. [secundaria — blog especializado]** «Un problema común es que no sabes si ganas o pierdes con tus productos y cobras precios "al ojo" o porque viste a otra repostera ponerlos así. Cuando no haces escandallos, sueles pensar que estás ganando… pero en realidad estás subsidiando a tus clientes con tu tiempo y tu bolsillo.»
Fuente: https://dianaverdu.com/escandallo-reposteria-como-hacerlo/

### Dolor H — Bar / cócteles

**H1. [secundaria — blog especializado, Argentina]** Sobre el costeo de tragos: «Costear: cómo, para qué y una planilla mágica» — el propio título del blog especializado en coctelería confirma que el problema («no sé cuánto me cuesta un trago») es lo bastante habitual en el gremio como para justificar un recurso propio.
Fuente: https://chicasbarra.com/2016/05/17/635/

**H2. [secundaria — patrón de fórmula heredada, no verificada como buena práctica]** Regla del "multiplica por 3, 4 o 5" para fijar precio de bebidas — se repite en múltiples blogs de bar como atajo mental para no tener que hacer el escandallo completo del cóctel, lo que indica que muchos bares fijan precios sin costear cada trago individualmente.
Fuente representativa: https://www.reyesgrupo.com/blog/blog-1/como-fijar-el-precio-de-un-coctel-1554

### Dolor I — Falta de tiempo / el Excel se queda corto

**I1. [secundaria — blog especializado]** «Cuando los restaurantes dependen de Excel para la gestión de costes, los datos se duplican, los inventarios se desactualizan y los informes financieros tardan demasiado en generarse (…) Excel puede funcionar bien para operaciones pequeñas, pero muchas enfrentan límites cuando las ventas, los proveedores o las sucursales aumentan.»
Fuente: https://blog.zetalatam.com/de-excel-a-un-software-inteligente-como-digitalizar-la-administracion-de-tu-restaurante/

### Dolor J — Ingeniería de menú a nivel profesional / hotelero

**J1. [PRIMARIA]** Angelo Vassallo, Director de Alimentos y Bebidas del Fairmont Rey Juan Carlos I (España), en un artículo publicado en LinkedIn Pulse:
> «(…) es aún más importante cuidar bien la rentabilidad de nuestra carta y oferta gastronómica.»
> «Un restaurante es una empresa, es un negocio. El propietario no sólo es un cocinero.»
Define el menu engineering como herramienta para «analizar y diseñar estratégicamente nuestro menú con la finalidad de maximizar la rentabilidad del restaurante», sobre la base de margen de contribución y popularidad de cada plato.
Fuente: https://www.linkedin.com/pulse/cuidar-la-rentabilidad-de-nuestra-carta-el-menu-angelo-vassallo — nota: el artículo hace referencia a la incertidumbre causada por «el virus», así que es de la era pandémica (circa 2020-2021); se cita por ser una voz profesional real y con cargo verificable, no por su actualidad.

---

## 2. Glosario ES ↔ MX/AR/CO ↔ inglés

| Concepto | 🇪🇸 España | 🇲🇽 México | 🇦🇷 Argentina | 🇨🇴 Colombia | 🇬🇧 Inglés | Recomendación para la guía y la landing |
|---|---|---|---|---|---|---|
| Cálculo del coste de un plato | **Escandallo** | **Costeo de recetas** / ficha técnica de costos | **Costeo** / ficha de costos | **Ficha técnica de costos** / costeo de platos | Recipe costing / plate cost | Usar **«Escandallo (costeo de recetas)»** en el título y la primera mención de cada capítulo — cubre a España sin dejar fuera a LATAM, que reconoce «costeo» de inmediato. |
| % del coste de materia prima sobre el precio de venta | **Food cost** (anglicismo ya asentado) | **Food cost** / costo de alimentos y bebidas (CyB) | **Food cost** / CMV (Costo de Mercadería Vendida — término contable, usado en informes financieros más que en cocina) | **Food cost** | Food cost | «Food cost» funciona igual en los 4 mercados — es el término de mayor volumen de búsqueda en todos ellos (ver Lente de datos). Mencionar **CMV** una vez en Argentina para lectores con perfil administrativo/contable. |
| Documento con ingredientes, cantidades y coste unificado de una receta | **Ficha técnica** | **Receta estándar** | **Receta estándar** | **Ficha técnica** | Standard recipe | Usar **«receta estándar / ficha técnica»** juntos la primera vez que aparece el concepto. |
| Precio final al cliente | **PVP** (precio de venta al público) | **Precio de venta** | **Precio de venta** | **Precio de venta** | Menu price / selling price | «PVP» es jerga de España; en LATAM se entiende pero no se usa activamente — preferir «precio de venta» como término principal y usar «PVP» sólo como sinónimo entre paréntesis. |
| Pérdida de producto (pelado, corte, cocción, deterioro) | **Merma** | **Merma** | **Merma** / desperdicio | **Merma** | Waste / yield loss | «Merma» es universal en los 4 mercados — no hace falta adaptar. |
| Documento con los platos y precios del restaurante | **Carta** | **Menú** (y **carta** también se entiende) | **Carta** / menú | **Carta** / menú | Menu | En España «carta» es dominante; en México «menú» es más frecuente en el habla cotidiana aunque «carta» también se usa en gastronomía formal. Usar ambos como sinónimos explícitos en el glosario de la guía. |
| Un plato del menú | **Plato** | **Platillo** (muy usado; «plato» sonaría a plato físico, no al preparado) | **Plato** | **Plato** | Dish | **No usar «platillo» como término por defecto** (sonaría raro en España y Argentina) — usar «plato», que se entiende en México sin sonar forzado, y mencionar «platillo» una vez como aclaración regional en el glosario. |
| Análisis de rentabilidad + popularidad de cada plato | **Ingeniería de menú** (también se ve «menu engineering» sin traducir en contenido de hoteles/consultoras) | **Ingeniería de menú** | **Ingeniería de menú** | **Ingeniería de menú** | Menu engineering | El término ya está unificado en español en los 4 mercados (confirmado por el research SERP): usar **«Ingeniería de Menú»** como término principal del producto, con «(menu engineering)» entre paréntesis en la primera mención para SEO y para lectores que buscan directamente en inglés. |
| Impuesto sobre el precio | **IVA** (hostelería: distinto tipo para bebida en barra vs. mesa — ver nota de la guía gastronómica ya publicada) | **IVA** (impuesto al valor agregado) | **IVA** | **IVA** | VAT | Mismo acrónimo en los 4 mercados — pero **el % y las reglas varían por país**; la guía debe dejar la casilla de IVA vacía/editable y no fijar un porcentaje único, tal y como ya se corrigió en la guía gastronómica v2.0 (IVA bebida en sala al 10 % en España, que no aplica igual en LATAM). |
| Comisión de las apps de reparto | **Delivery** / comisión de plataformas | **Comisión de Rappi/Uber Eats/DiDi Food** | **Delivery** | **Domicilios** / comisión de plataformas | Delivery commission | «Delivery» se entiende en los 4 mercados como anglicismo ya instalado — no hace falta traducir. En México, mencionar Rappi/DiDi Food explícitamente porque son las plataformas dominantes citadas en las fuentes (F2). |

**Recomendación de fondo:** no crear una versión distinta por país (coincide con la decisión ya tomada por John de «tienda única, sin páginas por país»). El vocabulario recomendado para el título y los H2 de la guía y la landing es: **«Food Cost» + «Ingeniería de Menú» + «Escandallo (costeo de recetas)»** — combinación que un lector de España y uno de México reconocen igual de bien, sin que ninguno de los dos sienta que el contenido «no es para él».

---

## 3. Cinco perfiles de comprador (buyer personas)

### Persona 1 — Carlos, dueño-chef de restaurante independiente (España, 38-55 años)
- **Contexto:** lleva la cocina y la caja a la vez. Hace el escandallo «a mano» o en un Excel que se le queda corto (patrón I1). Ya sabe lo que es un escandallo — lo que no tiene es tiempo ni criterio para decidir qué hacer con los datos (paralelo directo con la reseña A1: rechaza pagar por «lo que ya explica cualquier blog»).
- **Objetivo con la guía:** un capítulo que vaya directo al grano por problema («mi carta pierde dinero en X plato, ¿qué hago»), no una introducción larga a qué es un escandallo.
- **Lo que le convence:** la matriz de ingeniería de menú aplicada con un ejemplo de carta real (tipo Kasavana & Smith, ya presente en la Guía Restaurante Gastronómico) + el caso de Miraflores (E1: -20 platos, +16 % ticket, food cost -5 puntos) como prueba de que reducir carta funciona.

### Persona 2 — Marisol, gerente/socia de un restaurante familiar de comida típica (México, 30-45 años)
- **Contexto:** usa «costeo de recetas» y «platillo», no «escandallo». Le pega directo la subida de insumos (C5, C6, F2) y la comisión de Rappi/DiDi Food, que en México se lleva buena parte del margen si no ajusta precio en la app (F2).
- **Objetivo con la guía:** quiere una plantilla con fórmulas ya listas en pesos mexicanos, no una teoría larga — coincide con el patrón de decepción de A1 («un tercio del libro en explicar matrices básicas»).
- **Lo que le convence:** un capítulo específico de precios diferenciados delivery vs. sala (evita el error de F1/F2: vender con el mismo precio en Rappi que en sala y perder margen sin darse cuenta).

### Persona 3 — Javier, Director de Alimentos y Bebidas de un hotel o grupo de restauración (España/LATAM, 35-55 años)
- **Perfil real de referencia:** Angelo Vassallo (J1) — ya conoce la teoría de la matriz BCG y del menu engineering, pero necesita una herramienta actualizada y aplicable rápido a una carta de decenas de referencias (buffet, room service, banquetes).
- **Objetivo con la guía:** el capítulo avanzado — matrices más allá de la básica 2x2, caso de un F&B hotelero, gestión de mermas a escala.
- **Lo que le convence:** que la guía no se quede en «qué es un escandallo» (la queja de A1 aplica el doble a este perfil, que ya lo sabe) — necesita profundidad, no una introducción.

### Persona 4 — Ana, repostera/pastelera emprendedora con obrador pequeño (España/LATAM, 25-40 años)
- **Perfil real de referencia:** Ana Aboli (G1) y la creadora de @adiercakes (G2) — negocio que empezó por pasión, todavía no vive 100 % de él, y no tiene la certeza de si cada torta le deja margen o le está costando dinero (G3: «piensa que está ganando… pero está subsidiando a sus clientes con su tiempo y su bolsillo»).
- **Objetivo con la guía:** un capítulo de costeo específico de pastelería/obrador que incluya packaging, mano de obra por hora y delivery — no sólo materia prima (tal y como pide G2).
- **Lo que le convence:** el mensaje de «valórate y valora tu trabajo» (cita G1) traducido a una herramienta concreta, no sólo a una frase motivacional.

### Persona 5 — Diana, dueña de bar/coctelería (Argentina/Colombia/España, 28-45 años)
- **Contexto:** fija el precio del trago con la «regla del multiplicar por 3-5 el coste del licor» (H2) en vez de escandallar cada cóctel — y no tiene forma sistemática de medir la merma por goteo/derrame en barra.
- **Objetivo con la guía:** un capítulo de escandallo de bebidas y cócteles (el Kit de Escandallos Pro ya tiene una plantilla de cocktails — esta guía debería explicar el criterio detrás, no repetir la plantilla).
- **Lo que le convence:** ejemplos concretos con cifras de coctelería, no sólo de cocina — el research encontró blogs dedicados en exclusiva a «costear tragos» (H1), señal de que el dolor es real y específico del canal bar.

---

## 4. Objeciones de compra probables y cómo responderlas con honestidad

**1. «Ya hay plantillas Excel gratis, ¿para qué pago por esto?»**
Objeción real y bien fundada: existen decenas de plantillas Excel gratuitas de escandallo publicadas por blogs del sector (ej. https://cashtrainers.com/plantilla-excel-calculo-escandallos-costes-y-rentabilidad-de-restaurantes, https://www.elcoladorchino.com/plantilla-excel-costes-restaurante/). No se puede negar esto de forma honesta.
**Respuesta honesta:** no vender la guía como «la única forma de tener una plantilla» — el valor real es el **criterio para leer esos números y decidir** (qué hacer cuando el food cost real se dispara, cómo priorizar qué plato reformular, cómo aplicar la matriz de ingeniería de menú a una carta completa), más un caso trabajado de principio a fin. Sin esto, la guía compite mal contra lo gratuito.

**2. «Esto ya lo sé / lo puedo leer gratis en cualquier blog de food cost.»**
Objeción confirmada literalmente por la reseña 1★ de Amazon (A1): un lector pagó por un libro del mismo nicho y sintió que un tercio del contenido era «explicar matrices básicas» que ya conocía.
**Respuesta honesta:** el research de la Lente de SERP (documento hermano) ya muestra que «qué es un escandallo» y «qué es la ingeniería de menú» están sobre-cubiertos por decenas de blogs gratuitos — la guía **no puede competir ahí**. Tiene que empezar donde termina el contenido gratuito: casos con cifras reales, ejercicios resueltos (hay demanda de «menú engineering ejercicios resueltos», ver Lente de datos), y los capítulos específicos por canal (delivery, pastelería, bar) que ningún blog genérico cubre con la misma profundidad.

**3. «El precio me parece alto.»**
También confirmada por A1: el lector cuestionó pagar «un precio significativamente más alto» por un libro que sentía repetía contenido de otro libro del mismo autor.
**Respuesta honesta:** no ocultar el precio ni compararlo sólo contra lo gratuito — compararlo explícitamente contra el **Kit de Escandallos Pro (12 €)**, que ya existe: si la guía no aporta claramente más que ese kit + su bono de 17 páginas, la objeción de precio es legítima y hay que resolverla con contenido, no con marketing.

**4. «No tengo tiempo para leer una guía larga.»**
Patrón que aparece de forma indirecta en varias fuentes (A1: quejarse de "exceso" de páginas; C4: los propios hosteleros describen no tener tiempo ni para revisar precios de proveedores a diario).
**Respuesta honesta:** estructurar la guía por **capítulos autoconclusivos y accionables** (uno por dolor: mermas, delivery, carta larga, pastelería, bar), de forma que el lector pueda ir directo al suyo sin leer los demás — no prometer que se lee «en una tarde» si el documento es largo por diseño (documento técnico premium, no un folleto).

**5. «Ya tengo el Kit de Escandallos, no quiero comprar dos veces lo mismo.»**
Riesgo real de canibalización dentro del propio catálogo: el Kit de Escandallos Pro (12 €) ya incluye 11 plantillas Excel + un bono PDF de 17 páginas sobre food cost, y la Guía Restaurante Gastronómico (85 €) ya incluye `escandallo-maestro.xlsx` y `menu-engineering-matrix.xlsx` completos.
**Respuesta honesta:** la landing y la propia guía deben decir explícitamente qué añade sobre esos dos productos hermanos (más profundidad teórica + casos por canal + ejercicios resueltos, no plantillas nuevas que dupliquen las del Kit) y ofrecer un mensaje claro de progresión: Kit de Escandallos (herramienta operativa) → esta Guía (criterio técnico avanzado) → Guía Restaurante Gastronómico (todo el negocio). Sin esta jerarquía explícita, el propio catálogo se hace la competencia a sí mismo.

**6. «Mi negocio es muy específico (food truck / catering / hotel) para que esto me sirva.»**
El Kit de Escandallos Pro ya tiene plantillas separadas por formato (food truck, catering, cafetería/brunch, pastelería) — señal de que el catálogo ya reconoce que un formato único no convence a todos los perfiles.
**Respuesta honesta:** la guía no puede ser sólo de «restaurante a la carta clásico» — necesita al menos un ejemplo o mención explícita por formato (sala, delivery, bar, obrador, hotel) para que las 5 personas del apartado 3 se sientan representadas, sin llegar a fragmentar el documento en 5 guías distintas.

**7. «No me fío de comprar un documento digital sin poder probarlo antes.»**
Objeción genérica de comercio de infoproductos — **sin fuente específica encontrada en este research** (no se localizó una queja textual sobre esto en las fuentes revisadas); se incluye porque es la objeción estándar de cualquier producto digital de pago único, y el propio catálogo de AI Chef Pro ya la resuelve con el mismo mecanismo (páginas de producto con detalle del contenido, capturas de las plantillas, sin necesidad de research adicional para confirmar que existe).

---

## 5. Huecos de este research (léase junto con el resumen)

- **Reddit, Quora, Udemy y comentarios de YouTube quedaron fuera por completo**: bloqueo técnico de las herramientas disponibles en este entorno (confirmado con errores HTTP explícitos, no por falta de intento). Si se necesita esa voz específica, hace falta una vía con sesión autenticada (extensión de Chrome/Playwright), que las reglas del proyecto no permiten usar en este momento por la restricción térmica del Mac — sería tarea para VPS o para una sesión con el navegador de Windows, según la regla 2bis del CLAUDE.md global.
- **Facebook**: se confirmó que el dolor se pregunta activamente en grupos reales (A3), pero no se pudieron extraer respuestas/comentarios — sólo el título del post.
- **Dos estadísticas de adopción de escandallos** que aparecían en resúmenes de búsqueda (`67 %` y `2 %`) se descartaron al no poder verificar el texto exacto en la página fuente — no se han usado en ningún punto de este informe ni deben citarse en el producto final sin una fuente verificada aparte.
- **Sin voz directa de México** más allá de patrones de blog (no se encontró una cita textual atribuida a un restaurantero mexicano con nombre, pese a varios intentos de búsqueda dirigida) — el research de México se apoya en blogs especializados (gastronomadas.com.mx, PoloTab, Pleko) y en la cita colombiana de comisión de delivery (F2), no en voz mexicana propia.
- Las 14 entradas marcadas «secundarias» son paráfrasis fieles de contenido publicado (con URL y, cuando el blog lo indica, cifras concretas) — no son citas literales de un usuario anónimo de foro. Se han mantenido separadas de las 10 «primarias» en todo el documento para que no se confundan al redactar el producto.
