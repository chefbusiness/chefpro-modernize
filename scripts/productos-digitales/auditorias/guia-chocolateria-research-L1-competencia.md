# LENTE 1 — Competencia de pago y contenido gratuito

**Producto en diseño:** «Cómo Montar una Chocolatería» (guía premium «Cómo Montar» de AI Chef Pro; sería el **producto nº 49** del catálogo).
**Fecha del research:** **2026-09-12**. Todas las URLs de este informe se consultaron el **2026-09-12** salvo indicación expresa.
**Autor:** subagente L1 (research adversarial). **Esto no es contenido de producto**: es censo, evidencia y propuesta.

---

## Método

1. Búsqueda web en español, mercado España, sobre los cinco frentes del encargo: (a) libros, (b) guías/plantillas/manuales de pago único, (c) cursos y programas, (d) franquicias con datos económicos publicados, (e) consultoras y proyectos técnicos.
2. **Verificación abriendo la página del vendedor**, no el snippet del buscador. Cuando la ficha no se pudo abrir (403/404/500/cuerpo vacío) el dato queda marcado **«sin fuente»** y **no se usa como ancla de precio**.
3. Para las fuentes gratuitas, lectura de la página completa buscando: fecha real, cifras concretas, normativa citada, errores y **qué NO cubren**.
4. **Cero cifras de memoria del modelo.** Todo lleva URL + fecha de consulta, o el sello «sin fuente».
5. Térmica: consultas espaciadas con `istats cpu temp` entre tandas. Una pausa real a 67,19 °C (enfriado a 60,75 °C en 45 s) antes de seguir.

## Limitaciones declaradas (qué NO se pudo verificar y por qué)

| Qué no se pudo verificar | Motivo técnico | Consecuencia |
|---|---|---|
| **Amazon.es** | `amazon.es/dp/B08PXFV7ZS` devolvió **HTTP 500**. Amazon bloquea el fetch automatizado (mismo comportamiento que en el research de Pastelería). | **Ninguna cifra de Amazon.es entra en el censo.** El único libro de negocio de chocolatería en español se precia desde **AbeBooks**, en USD. |
| **infofranquicias.com — ficha de Chocolat Factory** | **HTTP 403 Forbidden**. | **Chocolat Factory queda «sin fuente»** pese a ser la franquicia de chocolate artesano más visible de España. No entra como ancla. |
| **EPGB — Màster de Xocolata (3.200 €) y Màster Gelateria (2.400 €)** | La home de `escoladepastisseria.cat` **no publica precios** («No prices or specific dates are published»), y las fichas `info_curs.php?id=14`, `?id=19` y `m/estudis.php?ct=3` devolvieron **HTTP 404**. Las cifras sólo existen en snippets de buscador. | **«sin fuente».** No se usan como comparable. Sí se confirma que **existe** un Màster de Xocolata y una Open Week de Bean to Bar. |
| **Hofmann — Gran Diploma (34.950 €) e Intensivo (4.950 € + 550 € matrícula)** | Sólo snippet de buscador; no se abrieron esas dos fichas. **Sí** se verificó en su web el curso de *Pastelería y Repostería Avanzada*. | Las dos primeras van **«sin fuente»**; el comparable válido de Hofmann es el de 5.525 €. |
| **Hofmann — «Curso 100% Práctico de Chocolate»** | `courses.hofmann-bcn.com/products/curso-practico-chocolate` devolvió **HTTP 404**. | **«sin fuente»**: se sabe que son «8 sesiones» por snippet, no el precio. |
| **silviaguedez.com** | **HTTP 403** al abrir el artículo. | Se anota sólo lo que devolvió el buscador, marcado como tal. |
| **teymas.com** (`abrir-una-tienda-de-chocolates`) | El fetch **falló sin salida** (`Command failed with no output`). | Fuente gratuita **descartada** del censo. |
| **Precios de Hotmart** | Igual que en Pastelería: las fichas de marketplace **no muestran precio** sin entrar al checkout. Verificado en 3 fichas de chocolatería. | Los infoproductos de Hotmart entran **sin precio confirmado**. |
| **ESAH — Chocolate y Pastelería Artística** | Su propia ficha **no publica precio**. | **«sin fuente»**. Sí se verificó el dato más útil: **su temario no tiene ni un módulo de gestión** (8 unidades, todas técnicas). |
| **Consultoras / proyectos técnicos de obrador** | Ninguna de las revisadas (MBW Ingenieros, Madrid Licencias, CIRTEC, Promatec) **publica tarifa**. MBW lo dice explícitamente: los requisitos «pueden variar en función de cada Ayuntamiento». | **No hay ancla de precio verificable en la familia (e).** Es, en sí mismo, un hallazgo. |
| **Precio real pagado vs. precio de lista** | Ninguna plataforma expone descuentos ni cupones aplicados. | El censo mide **precio publicado**, no ticket medio. |
| **Volumen de ventas de la competencia** | Nadie publica unidades. | El censo **no dice cuánto vende nadie**, sólo a cuánto lo ofrece. |
| **Callebaut «Formulación y bombonería 2.0» (900 €)** | La ficha publica **fechas de 14-16 nov 2022**. El precio es real pero la edición está **caducada**. | Se usa sólo como referencia de rango, **no** como oferta viva. |

---

## 1. Censo de PAGO — qué puede comprar hoy un español que quiere abrir una chocolatería

### (a) Libros — separados por TÉCNICA vs. NEGOCIO

| # | Título | Autor / editorial / año | Precio | URL | Consulta | **¿Técnica o negocio?** |
|---|---|---|---|---|---|---|
| C1 | **The Chocolatier's Shop** — 160 págs., inglés | Callebaut, **2023** | **49,90 €** | [booksforchefs.com](https://www.booksforchefs.com/es/chocolate/838-the-chocolatier-s-shop-callebaut.html) | 2026-09-12 | **NEGOCIO.** Literalmente «a guide for chocolatiers and confectioners who want to **start or grow their chocolate shop**»: marca, surtido, personal, clientes, equipamiento esencial, control de inventario + 25 chocolateros contando su experiencia. **Es el competidor de pago más directo que existe.** Pero: **en inglés, sin España, sin normativa, sin un solo Excel.** |
| C2 | **The Chocolatier's Kitchen** (volumen 1, +200 recetas) | Callebaut | **sin fuente** | [booksforchefs.com](https://www.booksforchefs.com/en/) | 2026-09-12 | TÉCNICA (bombonería por vida útil). |
| C3 | **Chocolate** — 416 págs., bilingüe ES/EN, 6ª ed. | Ramon Morató / **Grupo Vilbo** | **99,00 €** | [restorhome.es](https://www.restorhome.es/biblioteca-restorhome/11109-libro-chocolate-de-ramon-morato.html) | 2026-09-12 | **TÉCNICA.** +200 recetas: atemperado, variedades, bombones, piezas. La referencia del oficio en España. Cero gestión. |
| C4 | **Offbeat** — bombones de vanguardia | Andrey Dubovik | **99,00 €** | [booksforchefs.com](https://www.booksforchefs.com/es/91-chocolate) | 2026-09-12 | TÉCNICA. |
| C5 | **Cómo crear tu negocio de chocolatería: Paso a Paso** — 221 págs., español | Daniel Rojas Rivero, **autoeditado ("Independently published"), 2020** | **18,85–31,33 USD** (usado/nuevo) | [abebooks.com](https://www.abebooks.com/9798578061042/C%C3%B3mo-crear-negocio-chocolater%C3%ADa-Paso/plp) (ISBN 9798578061042) | 2026-09-12 | **NEGOCIO.** El **único** libro en español dedicado a montar una chocolatería. Autor **venezolano**; estructura Canvas (identidad, canales, ingresos, recursos, costes, precios, márgenes). **Sin marco legal español, autoeditado, de 2020.** |

> **Lectura del bloque (a): en toda la librería profesional española no existe un solo libro sobre el NEGOCIO de una chocolatería en España.** Lo que hay es (1) un libro de negocio de Callebaut de 49,90 € **en inglés**, (2) un autoeditado en español de 2020 escrito desde Venezuela, y (3) técnica pura a 99 €. La sección «Chocolatería» de Books for Chefs llegó a devolver **«There are no products»** el día de la consulta.

### (b) Guías, plantillas y manuales de pago único

| # | Producto | Vendedor | Precio | URL | Consulta | Qué incluye |
|---|---|---|---|---|---|---|
| C6 | **Software plan de negocio Chocolatería (IA)** | plandenegocio.es | **49 €** (antes tachado **147 €**; oferta «válida hasta el 13-sep-2026») | [plandenegocio.es](https://plandenegocio.es/plan-de-negocio-chocolateria/) | 2026-09-12 | Business plan integrado + presupuesto económico-financiero **a 5 años** «conforme a los requisitos bancarios», **dos escenarios**, cálculo automático de **DSCR**, ejemplo precargado de chocolatería para España, licencia vitalicia, chat 24/7. **Es el mismo motor que ya vendía para pastelería**: producto genérico con un ejemplo cambiado. |
| C7 | **Plantilla de costes de repostería (Excel)** | magnifiquereposteria (Gumroad) | **3 USD** | [gumroad](https://magnifiquereposteria.gumroad.com/l/Plantilla) | 2026-09-12 | Cálculo automático de gastos fijos, variables y packaging. Repostería, no chocolate. |
| C8 | **Production Cost (plantilla)** | excelwave (Gumroad) | **10 USD** | [gumroad](https://excelwave.gumroad.com/l/wuojm) | 2026-09-12 | Genérica. |
| C9 | **Cake Cost Calculator — Home Bakery Excel & Google Sheets** | HoneyPeachCo (Etsy) | **sin fuente** (Etsy no devolvió precio al fetch) | [etsy.com](https://www.etsy.com/es/listing/1650828129/calculadora-de-costos-de-pasteles) | 2026-09-12 | Escandallo de repostería casera. Listado el 01-jul-2026. |
| C10 | **Chocolatería en Casa como Negocio** | MasterClasses.La (Hotmart) | **sin fuente** | [hotmart.com](https://hotmart.com/es/marketplace/productos/chocolateria-en-casa-como-negocio/V60359052J) | 2026-09-12 | Masterclass: bombones desde cero «para crear tu propio negocio desde casa». LATAM. |
| C11 | **El negocio rentable de las fresas con chocolate** | Jorge Luis Junco Villadiego (Hotmart) | **sin fuente** | [hotmart.com](https://hotmart.com/es/marketplace/productos/curso-online-el-negocio-rentable-de-las-fresas-con-chocolate/Q96452481J) | 2026-09-12 | Cálculo de costes y fijación de precios de un solo producto. LATAM. |

> **Lectura del bloque (b):** el hueco es brutal. **Nadie vende en España una plantilla de escandallo, CAPEX o plan financiero pensada para un obrador de chocolate.** Lo que hay son escandallos de repostería a 3-10 USD y un generador de business plans genérico a 49 €.

### (c) Cursos y programas

| # | Programa | Centro | Precio | Duración / formato | URL | Consulta | **¿Gestión del negocio?** |
|---|---|---|---|---|---|---|---|
| C12 | **Bombonería** (11-13 may 2026) | **Callebaut Chocolate Academy™ España** (Gurb, Barcelona) | **790,00 €** | 3 días presencial, máx. 14 alumnos, desayuno y comida incl. | [callebaut.com](https://www.callebaut.com/es-ES/callebaut-chocolate-academy/courses/in-person-courses/bomboneria-1) | 2026-09-12 | **No.** Bombón moldeado y cortado, ganaches, pralinés, enrobadora. |
| C13 | **Chocolate The One 2026** (25 may – 11 jun 2026) | Callebaut Chocolate Academy™ | **4.500 €** | **17 días / 100 h** (70 % práctica), máx. 12, incluye comidas, material, uniforme y diploma | [callebaut.com](https://www.callebaut.com/en-US/callebaut-chocolate-academy/courses/in-person-courses/chocolate-one-2026-17-dias-de-curso) | 2026-09-12 | **No.** Del cacao al chocolate, bean-to-bar, atemperado, tabletas, bombonería, piezas artísticas, visita a la fábrica Chocovic. Verificado: «does not explicitly address business or management topics». |
| C14 | **Formulación y bombonería 2.0** | Callebaut Chocolate Academy™ | **900,00 €** (⚠️ **ficha con fechas de nov-2022**) | 3 días, máx. 12 | [callebaut.com](https://www.callebaut.com/es-ES/courses/in-person-courses/formulacion-y-bomboneria-20) | 2026-09-12 | **No**, pero es el único que enseña **aw, pH y estabilidad** — lo más cercano a vida útil. |
| C15 | **Curso Bean to Bar presencial** (Madrid) | Helen Chocolate / Escuela de Chocolate de Madrid | **900 €** (rebajado; la ficha figura **agotada**) | 6 h, 1 jornada, en pareja | [helenchocolate.es](https://helenchocolate.es/producto/curso-bean-to-bar/) | 2026-09-12 | **Parcial.** Su propia ficha promete «conceptos básicos del **emprendimiento**», packaging, proveedores y nuevos mercados… **en las pausas del café.** |
| C16 | **Curso de Bean to Bar by Jacob Torreblanca** | Escuela Torreblanca | **180 €** | 6 h, **online (Zoom)**, incluye uniforme, dosier PDF, diploma y grabación | [escuelatorreblanca.com](https://escuelatorreblanca.com/cursos-de-pasteleria-online/curso-de-bean-to-bar-by-jacob-torreblanca/) | 2026-09-12 | **No.** Verificado: «focuses on technical production skills rather than business development, pricing strategies, or operational management». |
| C17 | **Pastelería y Repostería Avanzada** | **Escuela Hofmann** (Barcelona) | **5.525 €** (matrícula **750 €** incluida) | **6 meses**, viernes 16:30-21:30 | [hofmann-bcn.com](https://www.hofmann-bcn.com/cursos-de-profesionalizacion/curso-de-pasteleria-y-reposteria-avanzada/) | 2026-09-12 | **Muy parcial.** Incluye «gestión profesional del chocolate: atemperado, cristalización, moldeo… bombonería fina» y «organización y planificación del trabajo en obrador». **Organizar el obrador ≠ montar la empresa.** |
| C18 | **Máster en Gestión en Alta Pastelería Profesional** | **Barcelona Culinary Hub** (título Universidad de Barcelona) | **19.200 €** | **15 meses**, 90 ECTS, presencial, inicio nov-2026 | [barcelonaculinaryhub.com](https://www.barcelonaculinaryhub.com/programas/master/alta-reposteria-y-pasteleria) | 2026-09-12 | **Sí**, el único del censo: Bloque 3 «Dirección y gestión del negocio gastronómico» (15 ECTS) + módulo «Chocolate y bombonería». **A 19.200 € y 15 meses.** |
| C19 | **Diploma de Pastelería** | **Le Cordon Bleu Madrid** | **21.150 €** nacional (1.500 € matrícula + 19.650 €) · **23.500 €** internacional | Programa completo (certificados Básico/Intermedio/Superior sueltos entre **7.830 y 8.700 €**) | [cordonbleu.edu](https://www.cordonbleu.edu/madrid/tuition-fees/en) | 2026-09-12 | **No** en la ficha de tarifas; el chocolate aparece como técnica de escultura. ⚠️ Un snippet de buscador daba **41.580 €**: **falso para este diploma**, corresponde a otro programa. Vale la cifra de la página de tarifas. |
| C20 | **Chocolate y Pastelería Artística** | **ESAH** (100 % online) | **precio no publicado** («sin fuente»; ESAH declara rango general 1.000-2.700 € sin atribuirlo a este curso) | **150 h** online | [estudiahosteleria.com](https://www.estudiahosteleria.com/pasteleria/curso-chocolate-pasteleria-artistica) | 2026-09-12 | **No. Cero.** 8 unidades: historia, cacao, subproductos, atemperado, cremas, masas, bombones, chocolate artístico. **Ni un módulo de gestión.** |
| C21 | **Màster de Xocolata** + **Bean to Bar 100% Open Week** | **EPGB — Escola de Pastisseria del Gremi de Barcelona** | **sin fuente** (la web no publica precios; fichas 404) | — | [escoladepastisseria.cat](https://www.escoladepastisseria.cat/) | 2026-09-12 | Desconocido. Existen, no se puede precisar precio ni temario. |
| C22 | **Curso online chocolatería y bombonería** | Escuela Mundo Pastel | **2 cuotas de 50 USD** (no publica precio en €) | 8 clases de 2 h, online en directo | [escuelamundopastel.com](https://escuelamundopastel.com/producto/curso-online-chocolateria-y-bomboneria/) | 2026-09-12 | Marketing hacia emprendedores; **contenido 100 % técnico**. Argentina. |
| C23 | **Iniciación al Bean to Bar** | Club del Chocolate | **sin fuente** (snippet: 300 € para 2 personas) | 2 sesiones de 4 h | [clubdelchocolate.com](https://www.clubdelchocolate.com/en/1710-curso-level-0-chocolate-maker-para-2-personas.html) | 2026-09-12 | Desconocido. |

> **Lectura del bloque (c): el mercado formativo español de chocolate enseña a HACER chocolate, no a VENDERLO.** Verificado uno por uno: Callebaut The One (100 h, 4.500 €) **no toca negocio**; ESAH (150 h) **no tiene ni un módulo de gestión**; Torreblanca lo dice en su ficha. El único con dirección de empresa de verdad —BCH— cuesta **19.200 €** y dura **15 meses**, y es de pastelería, no de chocolatería.

### (d) Franquicias — el ancla de inversión que publica el propio franquiciador

| # | Marca | Inversión total | Canon de entrada | Royalty | Publicidad | Local | Red | URL | Consulta |
|---|---|---|---|---|---|---|---|---|---|
| C24 | **Chocolates Valor** | **150.000 €** | **24.000 €** | **5 %** | «No facilitado» | **150 m²**, mín. 100.000 hab. o zona turística, contrato 10 años | 7 propios + **28 franquiciados** | [lafranquicia.es](https://www.lafranquicia.es/franquicia/valor-chocolates/) | 2026-09-12 |
| C25 | **Chök The Chocolate Kitchen** | **200.000 €** | **30.000 € + IVA** | «Fijo, 6 meses de carencia» | «No hay» | **70-120 m²**, mín. 60.000 hab. | 5 propios + 12 franq. + 5 internacionales | [lafranquicia.es](https://www.lafranquicia.es/franquicia/chok/) | 2026-09-12 |
| C26 | **Maestro Churrero** (churrería-chocolatería) | **desde 115.000 €** | **15.000 €** | **5 %** | **1 %** | **100 m² mín.**, contrato 10 años, exclusividad | 2 en España (expansión desde 2021) | [mundofranquicia.com](https://www.mundofranquicia.com/franquicia/restauracion/cafeteria-heladeria-chocolateria/maestro-churrero/) | 2026-09-12 |
| C27 | **Chocolat-Box** | **60.000-70.000 €** (+600 €/m² si hay reforma) | **5.000 €** | **0 %** los 2 primeros ejercicios, 3 % desde el 3.º | **1.500 €/año** | **100-200 m²** | 3 franquiciadas + 2 propias | [franquicias.es](https://www.franquicias.es/sectores-espana/alimentacion/chocolat-box) | 2026-09-12 |
| C28 | **Fábrica di Chocolate** | **60.000 €** | **15.000 €** | «Fijo» | **200 €** | **isla de 10 m²** | 4 en España + 49 en el extranjero (origen Brasil) | [100franquicias.com](https://www.100franquicias.com/franquicias/alimentacion/fabrica-di-chocolate/Franquicia-fabrica-di-chocolate-negocio.htm) | 2026-09-12 |
| C29 | **Sven Belgian Chocolate** (bombonería) | **33.000 €** | **5.000 €** | 2 % s/ventas **desde el 5.º año** | 3 % s/ventas desde el 5.º año | mín. 100.000 hab. | 3 propias + 1 franquiciada | [lafranquicia.es](https://www.lafranquicia.es/franquicia/bomboneria-sven/) | 2026-09-12 |
| — | **Chocolat Factory** | **sin fuente** (infofranquicias **403**) | — | — | — | — | — | — | 2026-09-12 |

> **Lectura del bloque (d):** el sector **sí** publica cifras — pero sólo cuando te vende una franquicia. **El canon de entrada más barato del censo son 5.000 € (Sven, Chocolat-Box)**: eso es lo que cuesta hoy, en el mercado español, que alguien te dé el método de una chocolatería empaquetado. Y ninguna de las seis te lo vende **sin** obligarte a llevar su marca.

### (e) Consultoras, ingenierías y proyectos técnicos

| # | Proveedor | Servicio | Precio | URL | Consulta |
|---|---|---|---|---|---|
| C30 | **MBW Ingenieros** (Barcelona) | Licencia de actividad de pastelería/obrador: proyecto con memoria y planos, tramitación, tasas | **No publica precio.** Advierte que el trámite «puede variar en función de cada Ayuntamiento» | [mbwingenieros.es](https://mbwingenieros.es/licencia-de-actividad-de-pasteleria-con-obrador/) | 2026-09-12 |
| C31 | **Madrid Licencias** | Licencia de tienda de alimentación **con obrador** (declara que hacen falta **las dos**: tienda + obrador) | **No publica precio** | [madridlicencias.com](https://www.madridlicencias.com/blog/licencia-de-actividad-y-apertura-para-tienda-de-alimentacion-con-obrador/) | 2026-09-12 |
| C32 | **CIRTEC Ingeniería** / **Promatec** | Proyectos de licencia de apertura para alimentación con obrador | **No publican precio** | [cirtec-ingenieria.es](https://www.cirtec-ingenieria.es/licencia-de-apertura/) · [licenciasyproyectospromatec.es](https://www.licenciasyproyectospromatec.es/) | 2026-09-12 |

> **Lectura del bloque (e): no hay ni una tarifa pública.** El emprendedor no puede presupuestar la partida «licencias» sin llamar por teléfono. Es exactamente el tipo de hueco que un Excel de CAPEX con escenarios resuelve.

---

## 2. Censo GRATUITO — las fuentes mejor posicionadas, auditadas una a una

| # | Fuente | Fecha real | Cifras que da | Errores / vaguedades | **Qué NO cubre** |
|---|---|---|---|---|---|
| G1 | **plandenegocio.es — «Guía práctica para abrir una chocolatería en España en 2026»** · [URL](https://plandenegocio.es/como-abrir-una-chocolateria/) | **14/04/2026** (declarada en el artículo) | Inversión **20.000-30.000 €** (artesana media) y **50.000-250.000 €+** (obrador con producción propia). Desglose: local y reformas **5.000-10.000 €**, equipamiento **7.000-12.000 €**, stock inicial **2.000-4.000 €**, licencias **1.000-2.000 €**. Umbral de **750 m²** para trámite simplificado. Plazo de trámites **2-4 meses** | 🔴 **«Carnet de manipulador de alimentos: obligatorio»** — el error clásico: el carnet oficial **no existe desde el RD 109/2010**; lo que obliga el Rgto. (CE) 852/2004 es **formación acreditada por la empresa**. Confirmado en el fetch. Además el desglose **no suma**: 5.000+7.000+2.000+1.000 = 15.000 €, no 20.000 | **Ni una palabra de RD 1055/2003** (definiciones legales de chocolate, % mínimos, grasas vegetales, «chocolate a la taza»), **ni de EUDR/2023-1115**, ni de cadmio (Rgto. 2023/915), ni de cámara de chocolate y clima del obrador, ni de escandallo por lote, ni de estacionalidad, ni de aw/vida útil, ni de APPCC real, ni de variación autonómica, ni de coste de seguros |
| G2 | **maxima.com — «7 cosas que necesita para abrir una chocolatería»** · [URL](https://maxima.com/es/blogs/maxima/todo-lo-necesario-para-abrir-una-chocolateria-en/) | **05/04/2023** | **NINGUNA.** Cero precios, cero m², cero inversión (verificado en el fetch) | **Es el blog de un vendedor de maquinaria**, con enlaces a sus propias categorías de producto. Los «7 pasos» son genéricos: ubicación, plan de negocio, inversores, ingredientes, equipo, personal, marketing | Permisos españoles, seguros, plantilla, superficie, proveedores, procedimientos operativos |
| G3 | **maestrochurrero.com — «3 razones por las que abrir una chocolatería…»** · [URL](https://www.maestrochurrero.com/abrir-una-chocolateria/) | **Sin fecha** (copyright 2026) | Consumo: Suiza **8,8 kg/persona (2017)**; España **186 M kg en 2020** (+24 M sobre 2019) | **Post promocional de su propia franquicia**: «si quieres abrir una chocolatería de éxito debes contar con nosotros». Datos de consumo de hace 5-9 años | Costes de arranque, licencias, competencia, inventario, salarios, proveedores |
| G4 | **cursosgastronomia.com.mx** · [URL](https://www.cursosgastronomia.com.mx/blog/montar-una-chocolateria/) | **ago-2018** (actualizado «hace 1 año») | **200.000-400.000 MXN** de arranque; hasta **300.000 MXN** de maquinaria | 🔴 **Es MÉXICO y son PESOS.** Rankea en la SERP española y sus cifras no aplican | Licencias españolas, procedimientos, personal, marketing |
| G5 | **expocafe.mx — «5 Tips para Abrir una Chocolatería Exitosa»** · [URL](https://www.expocafe.mx/5-tips-para-abrir-una-chocolateria-exitosa/) | **24/04/2024** | **NINGUNA** (la única cifra de la página son sus 198 «me gusta») | México. Cinco consejos de concepto, diferenciación, carta, calidad y experiencia | Capital, proyecciones, licencias, cadena de suministro, personal, ubicación, TPV |
| G6 | **gempages.net/es — «Cómo Iniciar una Tienda de Chocolates»** · [URL](https://gempages.net/es/blogs/shopify/chocolate-business) | **25/08/2025** | **3.000-8.000 USD** de arranque; mercado global 133.600 M USD (2024) | 🔴 **Traducido de contenido estadounidense**: cita la **FDA** y la **SBA**. Es un embudo hacia Shopify («$1/mes») y su propio constructor de páginas | Verificado en el fetch: **no menciona obrador, ni escandallo, ni licencias españolas, ni normativa europea** |
| G7 | **emprender-facil.com — «Tipos de chocolate y su plan de negocios»** · [URL](https://www.emprender-facil.com/tipos-de-chocolate/) | **Sin fecha** | **La mejor desglosada del censo gratuito:** ~**36.600 €** por tienda, **80 m²**; acondicionamiento **18.000 €**, mobiliario **4.800 €**, stock **5.500 €**, informática **1.800 €**; gastos mensuales **6.000-7.000 €** | Sin fecha = sin poder saber si los precios son de 2019 o de ayer. Proveedores sugeridos (Godiva, Torreblanca, Cacao Sampaka) mezclan marca de lujo con obrador | **Ni RD 1055/2003, ni escandallo, ni proyecciones financieras, ni fiscalidad, ni higiene/seguridad alimentaria** (verificado) |
| G8 | **silviaguedez.com — «Mi Top 10 de consejos para iniciarse en el negocio de la chocolatería»** · [URL](https://silviaguedez.com/mi-top-10-de-consejos-para-iniciarse-en-el-negocio-de-la-chocolateria/) | **Sin verificar (HTTP 403)** | Ninguna en lo devuelto por el buscador | Consejos de actitud: «asegúrate de que te gusta», «haz un Canvas», «no dejes tu trabajo», «empieza en casa», «haz un piloto». **Sensatos y ciertos, pero no accionables.** «Montar el espacio en casa» es, además, jurídicamente delicado en España y el artículo no lo matiza | Todo lo cuantitativo y todo lo legal |
| G9 | **mundodelchocolate.co — «Tips para abrir tu negocio de chocolates»** · [URL](http://www.mundodelchocolate.co/tips-para-abrir-tu-negocio-de-chocolates/) | Sin fecha | — | Dominio **.co (Colombia)**. Otra fuente LATAM ocupando SERP española | Marco español completo |
| G10 | **Asociación Chocolate Bean to Bar España — censo de asociados** · [URL](https://www.chocolatebeantobar.com/asociados/) | Consultada 2026-09-12 | **~40+ makers** asociados (Utopick, Kaitxo, Pangea, Casa Cacao Girona, Chocolates Artesanos Isabel, Lurka, Origen, Relieve, Kankel…) | **No es una guía**: es un directorio. No publica cuota ni formación | Todo el «cómo». Pero es **la mejor fuente gratuita de benchmark competitivo** del segmento bean-to-bar |
| *(bonus)* | **losfoodistas.com — reportaje de Utopick** · [URL](https://losfoodistas.com/utopick-pioneros-bean-to-bar-en-espana/) | **13/01/2021** | **35.000 € de inversión inicial (2014)** para el primer bean-to-bar de España | Cifra de hace 12 años, en un reportaje, sin desglose | Todo lo demás |

### Contraste que resume el bloque

Las tres cifras de inversión que un español encuentra hoy gratis para el mismo negocio son **20.000-30.000 €** (plandenegocio.es), **36.600 €** (emprender-facil.com, sin fecha) y **3.000-8.000 USD** (gempages, EE. UU.). **No se puede planificar una apertura con un rango que varía ×10 según qué resultado de Google abras**, y ninguna de las tres explica de qué depende la diferencia.

---

## 3. Tabla resumen del censo

| Familia | Ítems con **precio confirmado + URL** | Rango de precio verificado | ¿Alguno enseña a MONTAR una chocolatería **en España**? |
|---|---|---|---|
| (a) Libros | **4** de 5 | **18,85 USD – 99 €** | **No.** El único de negocio (49,90 €) está en inglés y sin marco español; el único en español es un autoeditado venezolano de 2020 |
| (b) Guías / plantillas | **3** de 6 | **3 USD – 49 €** | **No.** Un generador de business plan genérico (49 €) y escandallos de repostería |
| (c) Cursos | **8** de 12 | **180 € – 21.150 €** | **No.** Uno solo tiene gestión de empresa (BCH, **19.200 €**, 15 meses) y es de pastelería |
| (d) Franquicias | **6** de 7 | Inversión **33.000 – 200.000 €** · canon **5.000 – 30.000 €** | **Sí, pero comprando su marca.** Y el método no se vende suelto |
| (e) Consultoras | **0** de 3 | **Ninguna publica tarifa** | Hacen el proyecto técnico; no enseñan a decidir |
| **TOTAL de pago censado** | **21 con precio confirmado** (+11 sin precio verificable) | — | — |
| Fuentes gratuitas auditadas | **10 + 1 bonus** | — | **Una sola declara escribir para España en 2026 (G1) y su primer requisito legal es falso** |

---

## 4. Los 5 hallazgos que valen por todo el análisis

**H1 — El único libro del mundo sobre el negocio de una chocolatería cuesta 49,90 €, está en inglés y lo publica un fabricante de cobertura.**
*The Chocolatier's Shop* (Callebaut, 2023, 160 págs.) es literalmente «una guía para chocolateros que quieren **empezar o hacer crecer su tienda de chocolate**»: marca, surtido, personal, equipamiento, inventario, más 25 chocolateros contando qué les salió mal. Es un producto excelente y es **nuestro competidor conceptual**. Lo que no tiene: español, normativa española, un solo Excel, un solo número de un local de Madrid. Y el que sí está en español —Rojas Rivero, 221 págs., ~19-31 USD— es **autoeditado, de 2020 y escrito desde Venezuela**. *Consecuencia de diseño:* no competimos contra el vacío, competimos contra un buen libro en inglés — y ganamos por marco legal + hojas de cálculo, no por «contenido».

**H2 — Toda la formación española de chocolate enseña a HACER chocolate; ninguna enseña a VENDERLO.** Verificado ficha por ficha: Callebaut *Chocolate The One* son **100 h y 4.500 €** y su propia descripción «no aborda explícitamente temas de negocio o gestión»; **ESAH** son **150 h online** con **ocho unidades, todas técnicas** y **cero módulos de gestión**; **Torreblanca** lo admite en su ficha. El **único** programa del censo con dirección de empresa de verdad es el Máster de **Barcelona Culinary Hub**: **19.200 € y 15 meses**, y es de alta pastelería. *Consecuencia:* nuestro comprador no es alguien que necesite aprender a atemperar — probablemente ya sabe, o va a un curso de 790 €. Es alguien que sabe atemperar y **no sabe si le salen los números**. La guía no debe enseñar técnica.

**H3 — El error del «carnet de manipulador» está vivo en la única guía española de 2026, y es el hilo del que tirar.** `plandenegocio.es` (14-abr-2026) lista como requisito obligatorio el **carnet de manipulador de alimentos**, suprimido en España por el **RD 109/2010**; lo que exige el Rgto. (CE) 852/2004 es formación acreditada por la propia empresa. Y su desglose **no cuadra**: las cuatro partidas suman **15.000 €** frente a los **20.000-30.000 €** que titula. Si la fuente mejor posicionada de España falla en el requisito legal más elemental y en una suma, **la promesa «verificado contra el BOE, con las cuentas cuadradas» es defendible con evidencia** — sin decirlo en el titular comercial (regla del 5-sep).

**H4 — La mitad de la SERP española es LATAM o traducción de EE. UU., y eso se paga en dinero equivocado.** De las 10 fuentes gratuitas auditadas, **cuatro** (G4 México, G5 México, G6 EE. UU., G9 Colombia) están posicionadas en España con **pesos mexicanos, dólares, FDA y SBA**. Alguien que teclee «montar una chocolatería» en Madrid recibe hoy **200.000-400.000 MXN**, **3.000-8.000 USD** y **20.000-30.000 €** como respuestas al mismo problema. *Y confirma el patrón de los cuatro productos anteriores:* con «como montar una chocolateria» a **10 búsquedas/mes**, **la venta no entra por SEO** — entra por hub, lista de compradores, blog y plataforma. No prometer tráfico en ninguna parte.

**H5 — El mercado ya pone precio al método: 5.000 € de canon mínimo, y ninguna consultora publica tarifa.** Las seis franquicias verificadas van de **33.000 a 200.000 €** de inversión con **5.000-30.000 €** de canon de entrada: eso es lo que cuesta hoy que alguien te dé un obrador de chocolate empaquetado — **atado a su marca**. En el otro extremo, **ninguna** de las cuatro ingenierías revisadas publica el precio del proyecto técnico de licencia, así que el emprendedor **no puede ni presupuestar esa partida** sin llamar por teléfono. Entre «5.000 € y tu marca es de otro» y «gratis pero con una cifra falsa», **no hay absolutamente nada**. Ese es el hueco, y cabe un producto de 65 €.

---

## 5. Qué hace bien la competencia y copiamos

| Qué hace bien | Quién | Cómo lo aplicamos |
|---|---|---|
| **Contar fracasos, no sólo casos de éxito** | *The Chocolatier's Shop* (C1): 25 chocolateros narrando «experiencias exitosas **y las dificultades encontradas**» | El bonus de la familia («**12 decisiones de apertura resueltas**», molde de Pastelería) es exactamente esta forma. Cada decisión debe **enseñar el escenario que sale mal**, con la cifra a la que se rompe |
| **Dos escenarios + DSCR calculado automáticamente** | plandenegocio.es (C6), que lo vende a 49 € como su argumento principal | Ya lo tenemos y mejor: el **Kit Plan Financiero** y la Guía de Pastelería traen P&L, tesorería a 12 meses y DSCR **antes de deuda**. Hay que **enseñarlo en la landing**, porque el competidor lo usa como titular |
| **Publicar la estructura económica completa, sin vaguedades** | Las fichas de franquicia (C24-C29): inversión, canon, royalty, publicidad, m², población mínima, años de contrato | El xlsx de **CAPEX por escenarios** debe traer una columna «**franquicia vs. independiente**» con estas seis cifras reales citadas: es el único benchmark público y honesto del sector |
| **Formulación con aw, pH y estabilidad como materia propia** | Callebaut *Formulación y bombonería 2.0* (C14) — 900 € por enseñarlo | **Vida útil y aw del bombón relleno** tiene que ser un capítulo con tabla, no una nota al pie. Es lo que separa un obrador que vende en tienda de uno que envía por mensajería |
| **El Canvas como puerta de entrada emocional** | Rojas Rivero (C5) y silviaguedez.com (G8) | Un capítulo 1 corto de «¿es esto para ti?» con **criterios de descarte numéricos**, no con ánimo |
| **Directorio sectorial como prueba de mercado** | Asociación Chocolate Bean to Bar España (G10), ~40 makers | Capítulo de **benchmark competitivo**: quién hay, en qué ciudad, con qué modelo. Gratis, verificable y nadie lo ha convertido en tabla |
| **Empezar pequeño y escalar la máquina** | KM0Chocolate: «primero una atemperadora y una bañadora, y más adelante molinos, conchadoras, prensas o túneles» | El CAPEX debe tener **fases**, no una sola lista de compra |

---

## 6. Ancla de precio argumentada

**Recomendación: 65 €**, el mismo escalón que sus dos hermanas (`guia-pasteleria-obrador`, `guia-panaderia-obrador`) y que el Manual del Chef Ejecutivo. **No subir a 85 €** (reservado al gastronómico) y **no bajar a 55 €**.

**Comparables verificados (los cuatro con URL y precio confirmado en este informe):**

| Comparable | Precio verificado | Qué da por ese dinero | Qué NO da |
|---|---|---|---|
| **The Chocolatier's Shop** (Callebaut, 2023) | **49,90 €** | 160 págs. sobre el negocio de una chocolatería + 25 testimonios reales | **Inglés. Sin normativa española. Sin un solo Excel. Sin cifras de un local español.** |
| **plandenegocio.es — plan de negocio de chocolatería** | **49 €** (de 147 €) | Business plan + financiero a 5 años + DSCR + 2 escenarios | **Cero contenido: es un formulario.** No explica el obrador, el local, la estacionalidad ni la ley. Su propia guía gratuita tiene un requisito legal falso |
| **Callebaut — Bombonería (3 días, Gurb)** | **790,00 €** | 3 días presenciales de técnica con enrobadora | **Nada de negocio.** 12× nuestro precio por 0 % de gestión |
| **Franquicia Sven Belgian Chocolate** — canon de entrada | **5.000 €** | El método completo de una bombonería, empaquetado | **Atado a su marca, su surtido y su royalty desde el 5.º año** |

**El argumento, en una línea:** 65 € es **1,30×** el único libro de negocio del sector (49,90 €, en inglés y sin España), **0,36×** el curso técnico presencial más barato del censo (180 €) y **el 1,3 %** del canon de entrada más barato del mercado (5.000 €) — y es el único de todos ellos que llega con **normativa española verificada + libros de Excel calculados**.

**El ancla defensiva, para la landing:** «un solo mes de alquiler del local que vas a firmar» y «el 0,2 % de la inversión mínima de la franquicia más barata (33.000 €)». Las dos cifras son **verificables y están en este informe**; ninguna promete un retorno.

**Lo que justifica 65 € y no 49 €** —y hay que poder demostrarlo en el entregable, no en el copy—: el marco legal propio del chocolate (**RD 1055/2003**, cadmio, **EUDR**) que **ninguna fuente del censo menciona**, los libros de Excel (CAPEX por fases, escandallo con coste hora de obrador, estacionalidad Navidad/San Valentín/Pascua, plan financiero a 3 años), y el bonus de decisiones resueltas. Sin eso, 65 € no se sostienen frente a un libro de 49,90 €.

---

## 7. Decisión que hay que elevar a John: ¿qué se hace con la chocolatería de taza y churros?

**El censo dice que son dos negocios distintos, y la evidencia de este informe apunta a mantener el alcance (a) y tratar (b) como capítulo de variante corto.** Tres razones, todas con dato en este informe:

1. **La demanda de (b) es de consumidor, no de emprendedor.** «chocolate a la taza» 4.400/mes y «chocolateria churreria» 1.000/mes son búsquedas de quien quiere merendar (la SERP devuelve **Franquicia Valor** y **Valor chocolate** como relacionadas). Quien quiere *montarla* teclea «montar una churreria»: **50/mes**.
2. **El modelo (b) ya tiene quien se lo venda empaquetado.** **Maestro Churrero: 115.000 €, canon 15.000 €, royalty 5 %, publicidad 1 %, 100 m² mínimo** (C26). Competir con eso desde una guía de 65 € es otro producto.
3. **Rompería el xlsx.** Un obrador de bombonería **no tiene freidora ni salida de humos** — y eso es justo lo que cambia la licencia, la campana, el seguro y el CAPEX. Un obrador de churros sí. **Meter los dos en la misma hoja de CAPEX obliga a duplicar el concepto «obrador», que es exactamente el defecto que la refutación de Pastelería marcó como alto** (el mismo concepto calculado de dos maneras → UNA fuente por concepto).

**Propuesta:** alcance (a) **chocolatería artesana / bombonería con obrador**, con las variantes rentables dentro (boutique de autor, obrador B2B y regalo corporativo, venta online con envío, talleres y catas, chocolatería-pastelería, bean-to-bar). La chocolatería de taza y churros entra como **un capítulo corto de variante** que dice qué cambia (licencia con humos, estacionalidad invernal invertida, ticket y rotación distintos) **y remite a la franquicia como alternativa real**, más un aviso explícito de alcance en la landing y en la FAQ. Decisión de John.

---

## 8. Limitaciones del censo (resumen)

- **Amazon.es e infofranquicias.com bloquean el fetch (500 y 403).** Faltan por tanto el precio español del único libro de negocio en español y todos los datos de **Chocolat Factory**, la franquicia de chocolate artesano más visible del país.
- **EPGB no publica precios en su web** y tres de sus fichas dan 404: su Màster de Xocolata y su Open Week de Bean to Bar quedan sin precio verificable, pese a ser probablemente el competidor formativo más relevante de Barcelona.
- **Hotmart no muestra precio sin checkout**: tres infoproductos de chocolatería-negocio quedan censados sin cifra.
- **Ninguna consultora de licencias publica tarifa**: la familia (e) no aporta ancla de precio, sólo la constatación de la opacidad.
- **El censo mide precio publicado, no ticket medio ni unidades vendidas.** Nadie publica ventas.
- **No se ha verificado en esta lente el estado real del EUDR (Rgto. UE 2023/1115) ni el RD 1055/2003 ni la crisis del cacao**: aquí sólo se constata que **ninguna fuente del censo los menciona**. Su verificación normativa corresponde a la lente legal (L3) y es **bloqueante antes de escribir una línea**.
- **Dos fuentes gratuitas se perdieron por fallo técnico** (silviaguedez.com 403, teymas.com sin salida): el censo gratuito son 10 fuentes auditadas, no 12.
- **Le Cordon Bleu:** se descarta activamente la cifra de 41.580 € que devolvió el buscador y se usa la de su página oficial de tarifas (21.150 €). Es un recordatorio de que **el snippet no es la fuente**.
