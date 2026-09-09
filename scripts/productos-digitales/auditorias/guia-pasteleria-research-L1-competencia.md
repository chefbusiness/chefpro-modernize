# LENTE 1 — Competencia de pago y contenido gratuito

**Producto en diseño:** «Cómo Montar una Pastelería» (guía premium «Cómo Montar» de AI Chef Pro, producto nº 48 del catálogo).
**Fecha del research:** 2026-09-09 / 2026-09-10 (las consultas se hicieron a caballo de la medianoche; **todas las URLs se consultaron el 2026-09-09 o el 2026-09-10** y así se marcan).
**Autor del informe:** subagente L1 (research adversarial, no contenido de producto).

---

## Método

1. Búsqueda web en español (mercado España) sobre los cinco frentes del encargo: (a) libros, (b) guías/plantillas de pago único, (c) cursos y programas de gestión/emprendimiento pastelero, (d) franquicias con datos económicos publicados, (e) consultoras/ingenierías de apertura.
2. **Verificación de cada precio abriendo la página del vendedor**, no el snippet del buscador. Cuando la página no se pudo abrir (403, 404, 500, contenido vacío) el dato queda marcado **«sin fuente»** y NO se usa como ancla.
3. Para las fuentes gratuitas, lectura de la página completa para extraer: fecha real, cifras concretas, normativa citada y **qué no cubren** (que es donde está el hueco de mercado).
4. Cero cifras de memoria del modelo. Todo lo que aparece aquí tiene URL y fecha de consulta, o el sello «sin fuente».

## Limitaciones declaradas (lo que NO se pudo verificar y por qué)

| Qué no se pudo verificar | Motivo técnico | Consecuencia |
|---|---|---|
| **Amazon.es** | `https://www.amazon.es/s?k=montar+una+pastelería+negocio` devolvió **contenido vacío** y `https://www.amazon.es/dp/B0CM3JWZPZ` devolvió **HTTP 500**. Amazon bloquea el fetch automatizado. | **Ninguna cifra de Amazon.es entra en este censo.** El censo de libros se apoya en Paraninfo/todostuslibros, Casa del Libro e IC Editorial. |
| **Paraninfo.es (fichas directas)** | `paraninfo.es/catalogo/9788428366564/...` y `.../9788413661230/...` devolvieron **HTTP 403 Forbidden**. | Los precios de Paraninfo se tomaron de **todostuslibros.com** (portal del gremio de librerías), que sí los publica. Precio de tapa, puede diferir del PVP con descuento en tienda. |
| **Certicalia** (`certicalia.com/blog/requisitos-para-abrir-un-obrador-pasteleria`) | **HTTP 403**. | Fuente gratuita descartada del censo. |
| **Precios de Hotmart** | Las fichas de marketplace (`hotmart.com/es/marketplace/productos/...`) **no muestran el precio** sin entrar al checkout. Verificado en 2 fichas. | Los infoproductos de Hotmart entran al censo **sin precio confirmado**, salvo el Pack Técnico de Tamara Viñas (147 €, publicado en su propia web). |
| **ESAH** (Máster en Pastelería Profesional) | La ficha de educaweb dice literalmente **«Consultar precio»**. | Sin ancla de precio. Sí se verificó que **su temario no incluye gestión** (dato útil por sí solo). |
| **Escuela Tábatha** (Madrid) | La página del curso **no publica precio**; remite a WhatsApp. Un snippet de buscador mencionaba «cuatro pagos de 1.500 €». | **«sin fuente»** — no se usa como comparable. |
| **EPGB — Màster Gelateria (2.400 €)** | El snippet de buscador daba la cifra, pero la ficha `escoladepastisseria.cat/m/info_curs.php?id=16` devolvió **HTTP 404** y la home no publica precios. | **«sin fuente»**. |
| **Manolo Bakes** (300.000 € inversión / 50.000 € canon) | Sólo aparece en blogs de terceros (asest.es, conectacuenca.cl). La ficha de ZonaFranquicia consultada dice **«Inversión: Consultar»** y varias fuentes afirman que **ya no franquicia en España** (recompró a sus franquiciados). | **«sin fuente»** y, además, **inservible como ancla**: no hay franquicia que comprar. |
| **hellocash.es** | La página devolvió sólo el cascarón de navegación, sin cuerpo del artículo. | Fuente gratuita descartada del censo. |
| **manipulador-de-alimentos.com/como-montar-una-pasteleria-paso-a-paso/** | El fetch devolvió un artículo **distinto** del solicitado (uno genérico de hostelería del 01-may-2026). | Se anota lo que devolvió, marcado como tal; no se le atribuyen sus cifras al artículo de pastelería. |
| **Precio real pagado vs. precio de lista** | Ninguna plataforma expone descuentos aplicados, cupones ni ventas reales. | El censo mide **precio publicado**, no ticket medio. |
| **Volumen de ventas de la competencia** | Hotmart no publica unidades; Tamara Viñas no publica alumnos. | El censo **no dice cuánto vende nadie**, sólo a cuánto lo ofrece. |

---

## 1. Censo de PAGO — qué puede comprar hoy un español que quiere abrir una pastelería

### (a) Libros en español

| # | Título | Editorial / año | Precio | URL | Consulta | ¿Cubre montar/gestionar el negocio? |
|---|---|---|---|---|---|---|
| P1 | **Administración de establecimientos de producción y venta de productos de pastelería (MF1781_3)** — 502 págs. | Elearning S.L. Editorial, **2015** | **190,00 €** | [casadellibro.com](https://www.casadellibro.com/libro-administracion-de-establecimientos-de-produccion-y-venta-de-produ-ctos-de-pasteleria-mf1781-3/9788416492725/5711015) | 2026-09-09 | **Sí, es el único libro del censo que va de esto.** Manual de certificado de profesionalidad: proyecto de empresa viable, planificación, estructura organizativa, selección y gestión de personal. **Edición de 2015: 11 años de desfase normativo y de precios.** |
| P2 | **Productos de obrador** — Rafael Medina Moreno | Paraninfo, mar. 2022 | **33,50 €** | [todostuslibros.com](https://www.todostuslibros.com/editoriales/ediciones-paraninfo-s-a/coleccion/industrias-alimentarias_2024758) | 2026-09-10 | Parcial. Módulo del ciclo de FP de Panadería/Pastelería. Producción, no apertura. |
| P3 | **Materias primas y procesos en panadería, pastelería y repostería** — Moreno Santacreu / Morales Caraballo | Paraninfo, abr. 2021 | **32,00 €** | [todostuslibros.com](https://www.todostuslibros.com/editoriales/ediciones-paraninfo-s-a/coleccion/industrias-alimentarias_2024758) | 2026-09-10 | No (técnica). |
| P4 | **Elaboraciones de panadería y bollería** — Carrero / Rodríguez | Paraninfo, jun. 2021 | **28,00 €** | [todostuslibros.com](https://www.todostuslibros.com/editoriales/ediciones-paraninfo-s-a/coleccion/industrias-alimentarias_2024758) | 2026-09-10 | No (técnica). |
| P5 | **Presentación y venta de productos de panadería y pastelería** — Rafael Medina Moreno | Paraninfo, may. 2024 | **25,95 €** | [todostuslibros.com](https://www.todostuslibros.com/editoriales/ediciones-paraninfo-s-a/coleccion/industrias-alimentarias_2024758) | 2026-09-10 | Parcial: venta y presentación en vitrina. Es el libro más nuevo de la colección. |
| P6 | **INAD016PO Formación básica en higiene alimentaria: food defense, APPCC, limpieza y desinfección** | Paraninfo, mar. 2025 | **15,00 €** | [todostuslibros.com](https://www.todostuslibros.com/editoriales/ediciones-paraninfo-s-a/coleccion/industrias-alimentarias_2024758) | 2026-09-10 | Sólo APPCC/higiene, no pastelería específica. |
| P7 | **INAD01 Seguridad e higiene en la industria alimentaria** | Paraninfo, feb. 2025 | **15,00 €** | [todostuslibros.com](https://www.todostuslibros.com/editoriales/ediciones-paraninfo-s-a/coleccion/industrias-alimentarias_2024758) | 2026-09-10 | Sólo higiene. |
| P8 | **Aprovisionamiento interno en pastelería. UF0817** — Polo Hernán / Sastre Méndez, 136 págs. | IC Editorial, may. 2022 | **13,47 €** (papel; digital **descatalogado**) | [iceditorial.com](https://www.iceditorial.com/operaciones-basicas-de-pasteleria-hotr0109/9734-aprovisionamiento-interno-en-pasteleria-uf0817-9788411035484.html) | 2026-09-10 | Parcial: aprovisionamiento interno del obrador. |

> **Lectura del bloque (a):** en librería española, la franja de un libro técnico de pastelería es **13-34 €**; el único título que realmente enseña a *administrar* un establecimiento de pastelería cuesta **190 €** y es de **2015**. No existe en el canal librería un libro reciente y asequible sobre **abrir** una pastelería en España.

### (b) Guías, plantillas y manuales de pago único

| # | Producto | Vendedor | Precio | URL | Consulta | Qué incluye |
|---|---|---|---|---|---|---|
| P9 | **Software plan de negocio Pastelería IA** | plandenegocio.es (Stefano Ventura) | **49 €** (antes tachado **147 €**; oferta declarada «válida hasta 13-sep-2026») | [plandenegocio.es](https://plandenegocio.es/plan-de-negocio-pasteleria/) | 2026-09-10 | Business plan integrado, presupuesto económico-financiero a **5 años**, ejemplo precargado de pastelería en España, **dos escenarios**, cálculo automático de **DSCR** e índices bancarios, licencia de por vida, chat 24/7. |
| P10 | **Plan de Negocios Pastelería** (35 págs.) | modelosdeplandenegocios.com | **23 USD** (tachado 39 USD) | [modelosdeplandenegocios.com](https://modelosdeplandenegocios.com/products/plan-de-negocios-pasteleria) | 2026-09-09 | Documento editable en PowerPoint/Keynote/Slides, balance provisional, presupuesto, cuenta de resultados, plan de financiación, punto de equilibrio, DAFO, Business Model Canvas. **Multi-país (16 países), no específico de España.** |
| P11 | **Pack Técnico Completo** (6 cursos de técnica) | Pastelería Para Todos / Hotmart | **147 €** | [pasteleriaparatodos.com/cursos](https://pasteleriaparatodos.com/cursos/) (checkout `pay.hotmart.com/M106768436M`) | 2026-09-09 | 6 cursos técnicos (roscón, bizcochos, donuts, muffins, chocolate, navidad sin gluten). Técnica pura, sin gestión. |
| P12 | **Calculadora de costos y precios para Pastelería y Gastronomía** | Luis Víquez / Hotmart | **sin fuente** (Hotmart no muestra precio) | [hotmart.com](https://hotmart.com/es/marketplace/productos/calculadora-de-precios-pasteleria-y-reposteria/K95490413E) | 2026-09-09 | Excel + Google Sheets, recetas ilimitadas, márgenes, mano de obra y packaging; guía y videotutorial. Valoración 5,0 con 2 reseñas. |
| P13 | **Plantilla de Costos y Precios para Repostería (Excel)** | Clickma Academia / Hotmart | **sin fuente** | [hotmart.com](https://hotmart.com/es/marketplace/productos/plantilla-de-costos-y-precios-para-reposteria-excel/V104956697U) | 2026-09-09 | Escandallo de repostería en Excel. |
| P14 | **Pastelería emprende en casa** (e-book, 200+ págs.) | Gabriela Pascolini / Hotmart | **sin fuente** | [hotmart.com](https://hotmart.com/es/marketplace/productos/pasteleria-emprende-en-casa/U96813761G) | 2026-09-10 | 100 recetas + «estrategias prácticas de negocio» (organización, cálculo de precios, redes, captación). **Es recetario con capa de negocio, no manual de apertura.** |

### (c) Cursos y programas de gestión / emprendimiento pastelero

| # | Programa | Centro | Precio | Duración / modalidad | URL | Consulta | ¿Gestión de negocio? |
|---|---|---|---|---|---|---|---|
| **P15** | **«Monta o mejora tu pastelería» (Formación Negocio Pastelería)** | **Tamara Viñas — Pastelería Para Todos** | **697 €** (o 3 × 232,33 € sin intereses) | 12 semanas, 106 videolecciones + directos, acceso 1 año | [pasteleriaparatodos.com/formacion-crea-tu-negocio](https://pasteleriaparatodos.com/formacion-crea-tu-negocio/) · ficha: [/cursos/crea-tu-negocio/](https://pasteleriaparatodos.com/cursos/crea-tu-negocio/) | 2026-09-09 | **Sí, y es el competidor directo.** 12 módulos: papeles legales, rentabilidad, plan de negocio, **escandallo**, gastos/ingresos, precios, stock, **alérgenos**, calidad, **APPCC**, organización, fiscalidad. **10 plantillas** (APPCC, control de gestión, escandallo, alérgenos…), 6 bonos, Discord privado, **garantía de 30 días**. Declara explícitamente: «no incluye recetas ni técnica». |
| **P16** | **«Obrador en Casa»** | **Tamara Viñas** | **357 €** (o 3 × 119 €) | 7 módulos, 40+ lecciones, acceso de por vida | [pasteleriaparatodos.com/obrador-en-casa](https://pasteleriaparatodos.com/obrador-en-casa/) | 2026-09-09 | **Sí.** 10 bonos: guía de primeros pasos (PDF), **plantilla de escandallo**, plantilla de gastos e ingresos, control de gestión, **carta de alérgenos editable**, **Plan APPCC elaborado**, 6 meses de P&R grupales, sesiones de Instagram/identidad visual. Incluye **asistente IA entrenado con el contenido del programa**. |
| P17 | **Consultoría 1:1 con Tamara Viñas** | Pastelería Para Todos | **250 €/hora** | 1 h | [pasteleriaparatodos.com/consultoria](https://pasteleriaparatodos.com/consultoria/) | 2026-09-09 | Sí (asesoría a medida). |
| P18 | **Máster en Gestión de Alta Pastelería Profesional** | Barcelona Culinary Hub (Martín Berasategui) | **19.200 €** | 15 meses, presencial, inicio nov-2026, título propio + posible Máster de formación permanente UB | [barcelonaculinaryhub.com](https://www.barcelonaculinaryhub.com/programas/master/alta-reposteria-y-pasteleria) | 2026-09-09 | Sí: gestión financiera y control de costes, gestión de equipos y operaciones en obrador, marketing; **TFM = plan de negocio**. |
| P19 | **Máster en Panadería Artesanal y Gestión del Obrador** | Barcelona Culinary Hub | **12.700 €** | 10 meses, presencial, inicio nov-2026 | [barcelonaculinaryhub.com](https://www.barcelonaculinaryhub.com/master-en-panaderia-artesanal-y-gestion-del-obrador) | 2026-09-10 | Sí: «Maquinaria, obradores y establecimientos» + bloque «Negocio del pan» con módulo de plan de negocio, marketing y rentabilidad. |
| P20 | **Pastelería y Repostería Profesional** | Escuela Hofmann (Barcelona) | **7.000 €** (matrícula de 750 € incluida) | 10 meses, presencial | [hofmann-bcn.com](https://www.hofmann-bcn.com/cursos-de-profesionalizacion/curso-de-pasteleria-reposteria-profesional/) | 2026-09-10 | **No.** 100 % técnica (75 % práctica). Ni costes, ni gestión, ni apertura. |
| P21 | **Curso de Repostería y Pastelería** | CEAC (a distancia) | **2.040 € – 2.360 €** (según servicios) | 800 h lectivas + 200 h de prácticas | [ceac.es](https://www.ceac.es/cursos/formacion-tecnica/turismo-y-hosteleria/pasteleria-y-reposteria) | 2026-09-09 | Parcial: «diseño de ofertas gastronómicas» y «cálculo de costes», **escandallos**. No apertura de establecimiento. |
| P22 | **Máster en Pastelería Profesional** | ESAH | **sin fuente** («Consultar precio») | 1.000 h, online | [educaweb.com](https://www.educaweb.com/curso/master-pasteleria-profesional-on-line-323977/) | 2026-09-10 | **No.** Verificado: 7 módulos exclusivamente técnicos + proyecto final. Sin costes, sin escandallo, sin gestión. |
| P23 | **Curso de repostería presencial para emprendedores** | Escuela Tábatha (Madrid) | **sin fuente** (la página no publica precio; remite a WhatsApp) | 2-3 meses intensivo, presencial | [tabathapasteleria.com](https://www.tabathapasteleria.com/curso-de-reposteria-presencial-en-madrid-para-emprendedores-escuela-tabatha/) | 2026-09-09 | Declara cubrir «el paso a paso para tener éxito con un negocio de pastelería», sin detallar temario de gestión. |
| P24 | **Xef de Pastisseria / Alta Pastisseria / Xocolata / Gelateria / Panettone / Bean to Bar** | EPGB — Escola de Pastisseria del Gremi de Barcelona | **sin fuente** (la web no publica precios; la ficha del Màster de Gelateria devolvió 404) | Varias | [escoladepastisseria.cat](https://www.escoladepastisseria.cat/) | 2026-09-10 | **Ninguno menciona gestión de negocio ni apertura** en el contenido público. |

### (d) Franquicias de pastelería/panadería con datos económicos publicados — **anclas de inversión**

| # | Marca | Canon de entrada | Inversión total | Royalty | Publicidad | m² | Contrato | Red | URL | Consulta |
|---|---|---|---|---|---|---|---|---|---|---|
| P25 | **Granier** | **8.000 €** | **desde 83.000 €** (canon incluido) | **0 €** | n/d | desde **60 m²** | 10 años | 320 ES + 20 ext. | [100franquicias.com](https://www.100franquicias.com/franquicias/alimentacion/granier/Franquicia-granier-negocio.htm) | 2026-09-09 |
| P26 | **Santagloria** | **24.000 € + IVA** | **desde 200.000 €** | **5 %** | **1 %** | desde **100 m²** | 12 años | 160 ES | [100franquicias.com](https://www.100franquicias.com/franquicias/hosteleria/SantaGloria/Franquicia-santagloria.htm) | 2026-09-09 |
| P27 | **Chök** | **30.000 €** | **desde 100.000 €** | según ventas | según ventas | **55 m²** | 5 años | 42 | [franquiciashoy.es](https://www.franquiciashoy.es/franquicias/franquicias-de-panaderias-y-pastelerias/panaderias-pastelerias/chok) | 2026-09-09 |
| P28 | **Levaduramadre** (Comess Group) | **18.000 €** | **desde 60.000 €** | **2,5 %** | **1 %** | **60 m²** mín. | 5 años | +130 ES | [mundofranquicia.com](https://www.mundofranquicia.com/franquicia/panaderia-pasteleria/levadura-madre/) | 2026-09-09 |
| P29 | **Panaria** | 18.000 € | desde 120.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| P30 | **Pannus** | 15.000 € | desde 100.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| P31 | **Meraki** | 12.000 € | desde 90.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| P32 | **Las Muns** | 12.000 € | desde 60.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| P33 | **Tort** | 10.000 € | desde 25.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| P34 | **Dunkin' Donuts** | 25.000 € | desde 180.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| P35 | **Empanadas Malvón** | 50.000 € | desde 160.000 € | n/d | n/d | n/d | n/d | n/d | [franquiciashoy.es](https://www.franquiciashoy.es/rankings-detalle/franquicias-dulces-y-rentables-de-panaderias-y-pastelerias) | 2026-09-09 |
| — | **Manolo Bakes** | **sin fuente** | **sin fuente** — la ficha dice **«Consultar»** y hay fuentes que afirman que **ya no franquicia en España** | — | — | — | — | 70+ locales (ES + PT) | [zonafranquicia.com](https://zonafranquicia.com/franquicias/manolo-bakes) | 2026-09-09 |

> ⚠️ **Contradicción de dato registrada, no resuelta.** El **mismo** portal `franquiciashoy.es` publica para **Granier** «inversión desde **180.000 €**» mientras `100franquicias.com` publica «desde **83.000 €**» con canon idéntico de 8.000 €. Y **Levaduramadre** aparece con canon **18.000 €** (mundofranquicia) y **24.000 €** en snippets de otros portales, con inversión «desde 60.000 €» y «desde 99.000 €» según la fuente. **Los portales de franquicia no son fuente primaria**: reproducen fichas comerciales de antigüedad desconocida. Para una cifra que vaya a un producto de pago hay que ir al franquiciador. *(Esto es exactamente el patrón «una cifra repetida no es una cifra verificada».)*

### (e) Consultoras / ingenierías de apertura de obrador

| # | Servicio | Empresa | Precio publicado | URL | Consulta |
|---|---|---|---|---|---|
| P36 | **Licencia de apertura de panadería/pastelería/obrador en Madrid** | estudio LBA | **desde 1.690 € + IVA**; proyecto técnico de obrador completo **1.800 – 2.800 € + IVA**. Publica además un presupuesto total de obrador+despacho de **80 m²** de **97.000 – 184.000 €**. Incluye diseño del obrador con **principio de marcha adelante**, APPCC, registro sanitario y tramitación municipal. | [estudio-l.es](https://www.estudio-l.es/licencia-obrador-panaderia-madrid/) | 2026-09-10 |
| P37 | **Licencia de actividad de obrador de pastelería (Madrid / Barcelona / Valencia)** | Ingenieros Nalba | Presupuesto **gratuito y sin compromiso**; no publica tarifa. Ofrece ingeniería + tramitación + ejecución de obra. | [licenciadeactividadbarcelona.org](https://www.licenciadeactividadbarcelona.org/obrador-de-pasteleria-madrid.html) | 2026-09-09 |
| P38 | **Asesoramiento financiero de apertura** | La Hostelera (Iván Saura) | **1.000 €** dentro de su presupuesto tipo de 137.000 € | [lahostelera.com](https://www.lahostelera.com/blog/cuanto-dinero-necesito-para-montar-un-negocio-de-reposteria-o-pasteleria/) | 2026-09-09 |
| — | Referencia de mercado de licencias | Habitissimo / Cronoshare | Licencia de apertura **~1.600 €** de media incluyendo tasas municipales y proyecto técnico; visado colegial **60-200 €**; honorarios de arquitecto **3-15 % del PEM**. **Cifras de snippet de buscador, no verificadas en página → «sin fuente»** | [habitissimo.es](https://www.habitissimo.es/presupuestos/licencias-de-actividad) | 2026-09-09 |

---

## 2. Censo GRATUITO — qué ya responde a la pregunta sin pagar

| # | Fuente | Fecha real | Qué cubre | Cifras que da | Errores / vaguedades | Qué NO cubre |
|---|---|---|---|---|---|---|
| G1 | **pasteleriaparatodos.com — «Cómo montar un negocio de pastelería: guía 2026»** (Tamara Viñas) · [URL](https://pasteleriaparatodos.com/guia-montar-negocio-pasteleria/) · consultada 2026-09-09 | **12-jul-2026** | **La más completa del censo gratuito.** Rentabilidad, **5 modelos de negocio**, requisitos legales/sanitarios, inversión por modelo, precios y márgenes, errores comunes, FAQ | Margen objetivo **65-70 % sobre coste**; coste de ingredientes **<30-35 %**; beneficio neto **1.200-2.500 €/mes**; inversión: obrador en casa **3.000-5.000 €**, obrador a puerta cerrada **8.000-12.000 €** (completo 15.000-20.000 €), local con venta **15.000-25.000 €** (completo 30.000-50.000 €+), cafetería completa **60.000-80.000 €** (100.000 €+); salida de humos **3.000 €+**; **plan APPCC 700-800 €**; registro sanitario **~200 €**; hornos **400 € – 10.000-12.000 €**; seguro RC **200-500 €/año**; autónomos **80 €** (tarifa plana) → **~200 €/mes**; gastos fijos ejemplo **5.000 €/mes** → facturación necesaria **~7.200 €**; traspasos de obrador **45.000-65.000 €**; subvenciones Andalucía **3.000-5.000 €** | **Mezcla dos bases de margen sin avisar**: «65-70 % sobre coste» y «ingredientes por debajo del 30-35 %» no son la misma métrica y el lector medio las confunde. Las horquillas de inversión son anchísimas (un factor ×2 dentro de cada modelo). El dato de subvención es autonómico y sin URL de convocatoria. Sin desglose de m² por zona | Layout del obrador y **marcha adelante**; escandallo con merma y rendimiento; P&L y cash-flow mes a mes; punto muerto calculado; **14 alérgenos UE en vitrina y venta a granel**; trazabilidad; contrato de arrendamiento; convenio y coste real de personal; calendario de campañas (Navidad, Reyes, Semana Santa) que es donde una pastelería se juega el año |
| G2 | **lahostelera.com — «Cuánto dinero necesito para montar un negocio de repostería o pastelería»** (Iván Saura, CEO) · [URL](https://www.lahostelera.com/blog/cuanto-dinero-necesito-para-montar-un-negocio-de-reposteria-o-pasteleria/) · consultada 2026-09-09 | **actualizado 22-ago-2025** | **El desglose de CAPEX más honesto que hay gratis**, con tres niveles (bajo/medio/alto) sobre un caso real de **90 m² a pie de calle, local vacío** | Asesoramiento financiero **1.000 €**; proyecto técnico **5.000 €**; obra civil **54.000 / 81.000 / 108.000 €** (= **600 / 900 / 1.200 €/m²**); equipamiento **15.000 / 29.000 / 46.000 €**; marketing **5.000 €**; **TOTAL recomendado 137.000 €** | Es el presupuesto de **un** caso (Gijón, 90 m²) presentado como referencia general; el €/m² de obra puede no aplicar en otra plaza. Contenido de un proveedor de servicios de apertura | **Licencias y trámites**, APPCC, personal/nóminas, **P&L**, **cash-flow**, decoración, consumibles iniciales y fondo de maniobra |
| G3 | **plandenegocio.es — «Inversión necesaria para abrir una pastelería en España»** (Stefano Ventura, economista) · [URL](https://plandenegocio.es/cuanto-cuesta-abrir-pasteleria/) · consultada 2026-09-10 | **13-abr-2026** | Inversión inicial, estrategias de reducción, comparativa por modelo, gastos mensuales y rentabilidad, trámites, errores, ayudas públicas, FAQ | Inversión total **60.000-200.000 €+**; reforma **16.000-30.000 €**; equipamiento y vitrinas **30.000-50.000 €**; mobiliario **7.000-15.000 €**; licencias **1.000-5.000 €**; stock **2.000-5.000 €**; fondo de maniobra **10.000-20.000 €**; horno profesional **15.000-35.000 €**; amasadora **4.000-8.000 €**; vitrinas refrigeradas **7.000-15.000 €**; gastos mensuales **5.000-12.000 €** (alquiler 1.200-3.000, suministros 600-1.200, personal 2-5 empleados 2.000-6.000, seguros/gestoría 300-700, marketing 200-500, stock 1.000-2.000); **ROI 18-36 meses**; punto de equilibrio **7.000-15.000 €/mes** | **Es el embudo de un producto de pago** (su software de 49 €): el artículo da los rangos y el cálculo lo vende. Horquillas ×3 en casi todas las partidas. No dice de dónde salen las cifras | El **cómo** calcular: no hay fórmula de punto muerto, ni escandallo, ni modelo financiero. Nada de obrador (layout, flujos, frío), nada de alérgenos ni APPCC operativo |
| G4 | **ayudatpymes.com (Gestron) — «Cómo montar una panadería paso a paso + Costes»** · [URL](https://ayudatpymes.com/gestron/montar-panaderia/) · consultada 2026-09-09 | **2026** (artículo actualizado) | Panadería (adyacente, no pastelería): local, reformas, maquinaria, licencias, stock, trámites | Alquiler **800-3.000 €/mes**; compra de local **150.000-500.000 €+**; reforma despacho de pan **15.000-40.000 €**, obrador completo **40.000-100.000 €+**; maquinaria obrador con horno **23.000-85.000 €**, despacho **7.500-24.500 €**; licencias **2.900-14.900 €**; stock inicial **1.000-3.000 €**; total despacho **28.000-65.000 €**, panadería tradicional con obrador **78.000-177.000 €+** | Es de **panadería**, no de pastelería: el frío, la vitrina y la caducidad corta —que es lo que define una pastelería— no aparecen. Rango de licencias de **2.900 a 14.900 €** (factor ×5) sin explicar de qué depende | Variaciones municipales, formación del personal, seguros, marketing detallado, operación post-apertura |
| G5 | **spigadivulga.es — «Cuánto cuesta montar una panadería artesanal: presupuesto»** (Luis Cuesta) · [URL](https://www.spigadivulga.es/cuanto-cuesta-montar-panaderia-artesanal-presupuesto/) · consultada 2026-09-10 | **2026** | **Tres escenarios cerrados y partida a partida** — micropanadería doméstica, obrador propio, panadería tradicional — más costes fijos mensuales | Doméstica **2.590-7.430 €**; obrador propio **15.400-49.600 €**; tradicional **39.800-131.000 €**. Costes fijos: doméstico **300-700 €/mes**, obrador **850-1.830 €/mes**, tradicional **3.210-6.720 €/mes**. Partidas: horno 2ª mano 800-1.800 €, amasadora espiral 1.200-2.500 €, cámara de fermentación 1.500-4.000 €, permisos 500-1.500 €, colchón 3 meses 2.400-5.000 € / 10.000-22.000 € | Otra vez **panadería**, no pastelería. El «colchón de tesorería» que él mismo reclama (4-6 meses) sólo lo mete a 3 meses en sus propias tablas | Alérgenos, APPCC documental, vitrina y caducidad, encargos y tartas por pedido, campañas estacionales, personal con convenio |
| G6 | **modelosdeplandenegocios.com — «¿Cuánto cuesta abrir una pastelería en España?»** · [URL](https://modelosdeplandenegocios.com/blogs/news/cuanto-cuesta-abrir-pasteleria-espana) · consultada 2026-09-09 | **14-ago-2025** | Desglose de inversión inicial | **41.400 – 101.200 €** total: alquiler 3 meses + fianza **4.000-8.000 €**, licencias **1.000-5.000 €**, obras **5.000-20.000 €**, equipamiento **8.000-18.000 €**, mobiliario **5.000-15.000 €**, materia prima **2.000-5.000 €**, fondo de maniobra 3-6 meses **15.000-25.000 €** | **Es un anzuelo de venta**: promociona su plan de negocio varias veces dentro del artículo. Su rango total (41.400-101.200 €) **contradice** el de plandenegocio.es (60.000-200.000 €) y el de lahostelera (137.000 €) sin que ninguno explique la diferencia | Todo lo operativo. Es sólo una tabla de CAPEX |
| G7 | **lexpress-franchise.com — «Cómo abrir una pastelería en 2026: requisitos clave»** (Esperanza Escribano) · [URL](https://lexpress-franchise.com/es/articulos/abrir-una-pasteleria/) · consultada 2026-09-09 | **pub. 08-abr-2026, act. 11-jun-2026** | 6 tipos de pastelería, 6 fases para montarla, franquicias disponibles, costes, rentabilidad | Local **20.000-80.000 €**; equipamiento **30.000-100.000 €**; licencias **1.000-5.000 €**; materia prima **3.000-10.000 €**; marketing y branding **2.000-8.000 €**; **total 60.000-200.000 €**; Liaopastel 45 locales / capital propio 50.000 €; O'Dreams 130 locales / capital propio 25.000 € | **Es un portal de franquicias**: el artículo existe para derivar a franquiciar, no para abrir por libre. Titula «rentabilidad» y no da ni un margen | Rentabilidad real (% de beneficio, márgenes), **m² del local**, plazos legales, rotación de inventario, gastos mensuales, análisis de competencia por zona |
| G8 | **barcelonaculinaryhub.com/blog — «Requisitos clave para montar una pastelería»** · [URL](https://www.barcelonaculinaryhub.com/blog/requisitos-montar-pasteleria) · consultada 2026-09-10 | **pub. 08-oct-2024, act. 11-jun-2025** | Análisis de mercado, requisitos (presupuesto, permisos, equipamiento), pastelería online, consejos | **Inversión mínima 70.000-100.000 €**. Zonas del local: almacén, área de trabajo, exposición, mostrador | **Una sola cifra en todo el artículo** y sin desglose. Es contenido comercial explícito: empuja al Máster de 19.200 € con formularios de captación | Cálculos financieros, procedimiento de licencias por región, costes desglosados de equipamiento, financiación y ayudas |
| G9 | **pasteleriaparatodos.com — «Montar un obrador de pastelería en casa: guía paso a paso»** · [URL](https://pasteleriaparatodos.com/montar-obrador-pasteleria-casa/) · consultada 2026-09-10 | **18-jun-2025** | El sub-modelo «obrador en casa»: por qué, qué es, requisitos legales, equipamiento, rentabilidad, APPCC, formación, FAQ | Inversión **5.000-8.000 €** (equipo básico) y **30.000 €+** (profesional completo); regla de margen **30-35 %**; **IVA reducido del 10 %** para producto artesanal | **El dato legal más delicado del censo y lo despacha en una línea**: dice que el **RGSEAA** sólo es obligatorio si vendes a otros operadores alimentarios y no al consumidor final. Es la clave de todo el modelo doméstico y no cita ni el reglamento ni la autoridad autonómica que lo resuelve | Licencias por comunidad autónoma, procedimiento de tramitación, punto de equilibrio, **m² mínimos**, marketing digital concreto |
| G10 | **sillasmesas.es — «Cómo montar una pastelería: consejos y requisitos básicos»** · [URL](https://www.sillasmesas.es/blog/proyectos-hosteleria/montar-una-pasteleria/) · consultada 2026-09-10 | **sep-2020** (web actualizada 2026) | Requisitos, trámites, equipamiento y mobiliario, consejos | **Ninguna cifra.** Cero euros, cero m², cero plazos | Es el catálogo de un proveedor de mobiliario disfrazado de guía: la sección de equipamiento enlaza a sus categorías de producto. **Contenido de 2020 que sigue rankeando en 2026** | Todo lo cuantitativo |
| G11 | **emprendedores.es — «Cómo montar tu propia pastelería»** · [URL](https://emprendedores.es/gestion/crear-una-empresa/plan-de-negocio-pasteleria/) · consultada 2026-09-09 | **14-abr-2021** | Oportunidades y amenazas del sector, arrendamiento, requisitos legales | Fianza **2 meses**; contrato mínimo **5 años**; **40-50 m²** para ampliar servicios; **20-25 m²** en competencia desleal; **RD 2207/1995** | **Cinco años de antigüedad** en una URL que se llama literalmente «plan-de-negocio-pasteleria» y **no contiene ningún plan de negocio**. Cita el RD 2207/1995, **derogado** en materia de higiene por el paquete de higiene comunitario (Reglamento CE 852/2004) | Inversión, facturación, márgenes, personal, licencias específicas, costes operativos, rentabilidad, formación |

> **Nota sobre `manipulador-de-alimentos.com`:** la URL `/como-montar-una-pasteleria-paso-a-paso/` devolvió al fetch **un artículo distinto**, genérico de hostelería (01-may-2026): inversión media de restaurante/bar **~20.000 €**, food truck **~15.000 €**, obrador de comida casera **4 m²**, congelación **-18 °C**, y cita **RD 109/2010**, **Reglamento CE 852/2004**, **Ley 1/2025 de desperdicio alimentario**, **RD 199/2010** y el **REM**. No se le atribuyen esas cifras al artículo de pastelería; queda anotado como observación.

---

## 3. Tabla resumen del censo

| Familia | Nº ítems con evidencia | Rango de precio verificado | Ítems «sin fuente» | Lo que revela |
|---|---|---|---|---|
| **(a) Libros** | **8** (P1-P8) | **13,47 € – 190,00 €** | Amazon.es entero (bloqueado) | Sólo **1 de 8** trata de administrar el negocio, y es de **2015** a **190 €** |
| **(b) Guías/plantillas de pago único** | **6** (P9-P14) | **21 € (23 USD) – 147 €**; 3 sin precio público | Precios de Hotmart (3) | **Nadie vende una guía de APERTURA**: venden plan de negocio genérico o escandallo suelto |
| **(c) Cursos y programas** | **10** (P15-P24) | **357 € – 19.200 €** | ESAH, Tábatha, EPGB (3) | El mercado está **partido en dos**: infoproducto de 357-697 € o máster de 12.700-19.200 €. **En medio no hay nada** |
| **(d) Franquicias** | **11 con cifras** (P25-P35) + Manolo Bakes sin cifras | canon **8.000-50.000 €**; inversión **desde 25.000 € hasta 200.000 €** | Manolo Bakes; discrepancias Granier y Levaduramadre | El **canon más barato del sector (8.000 €) es 123 veces** una guía de 65 € |
| **(e) Consultoras/ingenierías** | **3** (P36-P38) | **1.000 € – 2.800 € + IVA** por proyecto/licencia | Nalba (sólo presupuesto a medida); Habitissimo (snippet) | El **papeleo solo** cuesta **1.690 €+IVA**; nadie regala el layout del obrador |
| **Fuentes gratuitas censadas** | **11** (G1-G11) | — | certicalia (403), hellocash (sin cuerpo) | Ver §2 |
| **TOTAL productos de pago censados** | **38 ítems (P1-P38)**, de los cuales **31 con precio confirmado en la página del vendedor** | — | **7 marcados «sin fuente»** | Supera el mínimo de 15 exigido |

---

## 4. Los 5 hallazgos que valen por todo el análisis

### H1 — El competidor real no es un libro ni un máster: es **Tamara Viñas, y ya está posicionada en la SERP que nos interesa**

`pasteleriaparatodos.com` aparece en la SERP de «como montar una pasteleria» **con la guía gratuita** (12-jul-2026) y desde ella embudo a **697 €** («Monta o mejora tu pastelería») y **357 €** («Obrador en Casa»). Es el mismo movimiento que hacemos nosotros —contenido que vende producto— hecho por alguien con **cara, marca y garantía de 30 días**. Y su temario de 12 módulos **solapa punto por punto** con lo que la guía debería cubrir: legal, rentabilidad, plan de negocio, escandallo, precios, stock, alérgenos, APPCC, fiscalidad. Además incluye **10 plantillas** y un **Plan APPCC ya elaborado** — exactamente nuestra munición.
Consecuencia: **no podemos vender «te explico cómo montar una pastelería»**. Eso ya lo vende ella, con acompañamiento humano, por 697 €. Tenemos que vender otra cosa (ver H5).

### H2 — Hay un **agujero de precio de 200-350 €** entre el infoproducto y el máster, y nadie lo ocupa

Ordenado, el mercado verificado es: plantilla de escandallo suelta (~20-50 €) → software de plan de negocio **49 €** → Pack técnico **147 €** → **Obrador en Casa 357 €** → **Formación Negocio 697 €** → CEAC **2.040-2.360 €** → Hofmann **7.000 €** → BCH obrador **12.700 €** → BCH pastelería **19.200 €**.
Entre **49 € y 357 €** sólo hay técnica (147 €) y plantillas sueltas sin precio público. **Un producto documental de 65-85 € cae limpio en ese hueco**, y no compite con nadie de frente: es 7× más caro que un plan de negocio genérico y **5,5× más barato que el programa de Tamara**.

### H3 — Lo gratis da **cifras de CAPEX y se para justo antes del trabajo**

Las 11 fuentes gratuitas cubren bien una sola pregunta —«¿cuánto cuesta?»— y **ninguna** cubre: layout del obrador con **marcha adelante**, escandallo con merma y rendimiento por lote, **P&L y cash-flow mes a mes**, punto muerto calculado sobre datos propios, **los 14 alérgenos UE aplicados a vitrina y venta a granel**, trazabilidad documental, convenio y coste real de personal, y **el calendario estacional** (Reyes, Semana Santa, Navidad) que es donde una pastelería hace la caja del año. Verificado fuente por fuente en la tabla §2: es un **hueco unánime**, no una laguna de una web concreta.

### H4 — Las cifras gratuitas **no coinciden entre sí y ninguna dice de dónde sale**

Para el mismo negocio, en el mismo país, en 12 meses:

| Fuente | Fecha | Inversión total declarada |
|---|---|---|
| modelosdeplandenegocios.com | 14-ago-2025 | **41.400 – 101.200 €** |
| plandenegocio.es | 13-abr-2026 | **60.000 – 200.000 €** |
| lexpress-franchise.com | 08-abr-2026 | **60.000 – 200.000 €** |
| barcelonaculinaryhub.com | act. 11-jun-2025 | **70.000 – 100.000 €** |
| lahostelera.com (90 m², caso real) | act. 22-ago-2025 | **137.000 €** |
| estudio LBA (80 m², obrador+despacho) | consultada 2026-09-10 | **97.000 – 184.000 €** |
| pasteleriaparatodos.com (local con venta) | 12-jul-2026 | **15.000 – 50.000 €** |

Los extremos son **15.000 €** y **200.000 €**: un factor **13**. Ninguna explica la hipótesis (m², plaza, si el local viene vacío o traspasado, si incluye fondo de maniobra). **Esa es nuestra oportunidad más clara**: no dar «un número», sino **el modelo que produce el número del lector** con sus m², su plaza y su carta — y decir explícitamente qué hipótesis lleva dentro.

### H5 — El sector vende **formación**; nadie vende **los entregables**

Nadie del censo vende lo que nosotros sabemos fabricar: **hojas de cálculo que funcionan**. Tamara Viñas regala 10 plantillas *dentro* de un curso de 697 €; Hotmart vende calculadoras de escandallo sueltas (sin precio público) sin contexto de apertura; el software de 49 € da un plan de negocio pero **no da ni escandallo por lote, ni layout, ni APPCC, ni matriz de alérgenos**. Y las ingenierías cobran **1.690 €+IVA** por el papeleo sin entregarte ningún modelo económico.
**El producto que no existe es: el dossier completo de apertura de una pastelería en España, con los Excel que hacen los números y los documentos que pide el inspector, sin tutoría y sin suscripción.** Ese es el ángulo de venta, y encaja con la escalera del catálogo (guías «Cómo Montar» a 65 €) y con los activos que ya tenemos (`guia-panaderia-obrador` como molde, `kit-tareas-pasteleria` como base operativa).

---

## 5. Qué hace bien la competencia y copiamos

| Práctica verificada | Dónde | Cómo la aplicamos |
|---|---|---|
| **Segmentar por MODELO de negocio y poner precio a cada uno** | Tamara Viñas separa «Obrador en Casa» (357 €) de «pastelería completa» (697 €); su guía distingue 5 modelos con inversión propia | La guía debe tener **una ruta por variante** (obrador en casa · obrador a puerta cerrada B2B · pastelería con despacho · pastelería-cafetería · cake design por encargo), cada una con **su** CAPEX, **su** punto muerto y **su** checklist legal. No un único «monta una pastelería» |
| **Declarar en negativo lo que NO incluye** | Tamara: «no incluye recetas ni técnica pastelera» | Decir en la landing y en la primera página: **«esto no es un recetario ni un curso de técnica; es el dossier de apertura»**. Corta devoluciones y posiciona frente al infoproducto |
| **Escenarios bajo / medio / alto, no un número** | lahostelera.com (600/900/1.200 €/m² de obra) y spigadivulga.es (3 escenarios cerrados) | El xlsx de CAPEX debe traer **tres escenarios paramétricos** y el €/m² **en celda verde**, no dentro de la fórmula |
| **Poner el colchón de tesorería como partida propia** | spigadivulga.es lo señala como el error que mata negocios; modelosdeplandenegocios.com lo mete como «fondo de maniobra 3-6 meses» | Partida obligatoria en el CAPEX y ligada al cash-flow: **meses de colchón** como parámetro, con semáforo |
| **Plantillas como argumento de venta, no como bonus escondido** | Tamara enumera las 10 plantillas por su nombre (APPCC, escandallo, alérgenos, control de gestión) | Enumerar los **xlsx uno a uno con lo que calculan** en la landing. Es nuestro punto fuerte medible frente a un PDF |
| **Garantía visible** | Tamara: devolución íntegra a 30 días sin condiciones | Evaluar la política de devolución del catálogo. La competencia directa la publica en portada |
| **Precios y desgloses concretos en el contenido gratuito** | lahostelera.com y spigadivulga.es rankean por dar tablas, no párrafos | Nuestras piezas de captación deben llevar **tablas con cifras fechadas y su fuente** — donde ellos ponen cifras sin origen, nosotros ponemos cifra + URL + fecha |
| **Cubrir explícitamente «desde casa»** | Es la variante con más demanda en el PAA de la SERP («¿Cómo empezar un negocio de repostería desde casa?», «requisitos para montar un obrador en casa», «vender repostería desde casa España») y Tamara le dedica un producto entero de 357 € | **Capítulo propio del obrador doméstico**, con el punto que ella despacha en una línea —cuándo hace falta **RGSEAA** y cuándo basta el registro autonómico— resuelto **con norma citada**. Ahí se gana o se pierde la credibilidad del producto |

**Qué hace mal y NO copiamos:** dar una horquilla de inversión de factor ×3-×13 sin decir la hipótesis (todos); citar normativa derogada (emprendedores.es con el RD 2207/1995); vender «rentabilidad» en el titular y no dar ni un margen (lexpress-franchise); publicar en 2020 y dejarlo rankeando en 2026 sin revisar (sillasmesas); y despachar el punto legal más delicado del modelo doméstico en una frase sin fuente (pasteleriaparatodos, G9).

---

## 6. Ancla de precio argumentada

**Recomendación: 65 €**, igual que `guia-panaderia-obrador` y que las demás «Cómo Montar». Con 85 € defendible **sólo** si el paquete de xlsx supera claramente al de la guía de panadería y se comunica entregable a entregable.

| Comparable verificado | Precio | Qué da por ese dinero | Ratio vs. 65 € | Lectura |
|---|---|---|---|---|
| **«Obrador en Casa» — Tamara Viñas** ([URL](https://pasteleriaparatodos.com/obrador-en-casa/), 2026-09-09) | **357 €** | 7 módulos en vídeo, 40+ lecciones, 6 meses de P&R, 10 bonos (escandallo, gastos/ingresos, control de gestión, alérgenos, **Plan APPCC**), asistente IA | **5,5× más caro** | Es el **techo psicológico** del segmento «quiero abrir desde casa». A 65 € somos el **12 %** de su precio sin tutoría: la comparación es favorable y honesta |
| **«Monta o mejora tu pastelería» — Tamara Viñas** ([URL](https://pasteleriaparatodos.com/formacion-crea-tu-negocio/), 2026-09-09) | **697 €** | 12 semanas, 106 videolecciones, 10 plantillas, Discord, garantía 30 días | **10,7× más caro** | Marca el techo del mercado de infoproducto. Nuestro producto no compite: es el **paso previo** o la alternativa sin acompañamiento |
| **Software plan de negocio Pastelería IA** ([URL](https://plandenegocio.es/plan-de-negocio-pasteleria/), 2026-09-10) | **49 €** (de 147 €) | Business plan + presupuesto a 5 años + 2 escenarios + DSCR, licencia de por vida | **0,75×** | Es el **suelo**. A 65 € estamos apenas un 33 % por encima de un producto que **sólo** hace el plan financiero: si además damos layout de obrador, APPCC, alérgenos, escandallo por lote y checklists, la relación es evidente |
| **Administración de establecimientos de pastelería (MF1781_3)** ([URL](https://www.casadellibro.com/libro-administracion-de-establecimientos-de-produccion-y-venta-de-produ-ctos-de-pasteleria-mf1781-3/9788416492725/5711015), 2026-09-09) | **190,00 €** | 502 págs. de manual de certificado de profesionalidad, **edición de 2015**, sin Excel | **2,9× más caro** | El único libro comparable en tema es **3× nuestro precio y 11 años más viejo**. Argumento limpio de actualidad y formato |
| **Licencia de obrador — estudio LBA** ([URL](https://www.estudio-l.es/licencia-obrador-panaderia-madrid/), 2026-09-10) | **1.690 € + IVA** (proyecto 1.800-2.800 €+IVA) | Sólo la tramitación y el proyecto técnico en Madrid | **26× más caro** | Contexto: **el papeleo de un solo trámite** cuesta 26 guías. Sirve para situar el precio, no para prometer que la guía lo sustituye — **no lo sustituye y hay que decirlo** |
| **Canon de entrada más barato del sector (Granier)** ([URL](https://www.100franquicias.com/franquicias/alimentacion/granier/Franquicia-granier-negocio.htm), 2026-09-09) | **8.000 €** (inversión desde 83.000 €) | Derecho a usar la marca | **123×** | Ancla macro: lo que cuesta *empezar a poder* abrir por la vía franquicia |

**Argumento de precio para la landing (sin cifras inventadas):** un plan de negocio genérico cuesta **49 €** y sólo hace números; el programa que sí enseña a montarla cuesta **357-697 €** y exige 7-12 semanas; el único libro de administración de pastelerías cuesta **190 €** y es de 2015. **65 €, pago único, acceso vitalicio, con los xlsx que hacen los cálculos y los documentos que exige la inspección.**

**Contra el argumento de subir a 85 €:** el comparable más cercano por debajo (49 €) está muy cerca y es agresivo en oferta; y `guia-panaderia-obrador` —la hermana con obrador, la más parecida en alcance— está a 65 €. Subir a 85 € **rompería la coherencia interna del catálogo** y obligaría a justificar por qué la pastelería vale más que la panadería. La única vía honesta a 85 € es que el paquete sea objetivamente mayor (más xlsx, más documentos) **y esté enumerado**.

---

## 7. Limitaciones del censo (además de las de cabecera)

1. **Es un censo de precio publicado, no de mercado real.** Nadie publica unidades vendidas. Que Tamara Viñas cobre 697 € no dice cuánta gente los paga.
2. **Amazon.es queda fuera por bloqueo técnico** (contenido vacío + HTTP 500). Es el mayor canal de libros en español: el bloque (a) está **incompleto por construcción** y podría haber títulos de autopublicación sobre abrir una pastelería que este censo no ve.
3. **Los portales de franquicia no son fuente primaria** y se contradicen entre sí (Granier 83.000 € vs 180.000 €; Levaduramadre canon 18.000 € vs 24.000 €). Las cifras de (d) valen como **orden de magnitud publicado**, no como dato auditado. **No deben entrar en un entregable de producto sin ir al franquiciador.**
4. **Los precios de Hotmart no son públicos** sin llegar al checkout: 3 infoproductos del censo van sin precio. El tamaño real del mercado de plantillas de escandallo en español está **infravalorado** aquí.
5. **Sesgo de idioma y país.** Todo el censo es es-ES. No se ha medido la oferta LATAM (México, Colombia, Argentina), que según el propio DataForSEO del contexto tiene demanda propia («negocio de pasteleria» MX 40/mes) y donde Hotmart es mucho más fuerte.
6. **Las fechas de los artículos gratuitos son las que ellos declaran.** Varios muestran «2026» en el título sin fecha de actualización real verificable (ayudatpymes, spigadivulga). Un título con año no prueba una revisión.
7. **No se ha comprobado si nuestras propias piezas ya rankean** para estas consultas (eso es trabajo de la lente SERP/GSC, no de ésta).
8. **No se ha auditado la calidad interna de los productos de pago**: nadie ha comprado el curso de 697 € ni el software de 49 €. Lo que se compara es **lo que prometen**, no lo que entregan.

---

## 8. Qué tiene que traer nuestra guía para que 65 € tengan sentido frente a lo gratis

Todo lo que sigue está **ausente en las 11 fuentes gratuitas censadas** (verificado columna «Qué NO cubre» de §2) y **no se vende suelto** en el censo de pago:

1. **Modelo de CAPEX paramétrico por variante** (5 modelos), con escenarios bajo/medio/alto, €/m² en celda verde y **fondo de maniobra en meses** como parámetro — la partida que spigadivulga señala como asesina y que lahostelera **no incluye** en sus 137.000 €.
2. **Escandallo por lote de obrador** con merma, rendimiento y coste de mano de obra imputado — no la calculadora de recetas suelta de Hotmart.
3. **P&L a 36 meses y cash-flow mensual** con estacionalidad de pastelería (Reyes, Semana Santa, Navidad, comuniones): **ninguna fuente gratuita lo menciona siquiera**.
4. **Punto muerto calculado sobre los datos del lector**, no un rango «7.000-15.000 €/mes» sin hipótesis.
5. **Layout del obrador con marcha adelante** y zonificación (recepción, almacén seco, frío, elaboración, acabado, expedición, despacho) — lo cobra la ingeniería a 1.800-2.800 €+IVA y no está gratis en ningún sitio.
6. **Matriz de los 14 alérgenos UE aplicada a vitrina y venta a granel** + cartel + etiquetas. Ya lo sabemos hacer (`kit-tareas-pasteleria` lo trae): aquí hay que traerlo **conectado a la carta de apertura**.
7. **El nudo legal del obrador doméstico resuelto con norma citada**: cuándo basta el registro autonómico y cuándo hace falta **RGSEAA**. G9 lo despacha en una línea sin fuente y es lo que más se pregunta en el PAA.
8. **Checklists de trámites por fases** con quién los pide (ayuntamiento / comunidad autónoma / Hacienda / Seguridad Social) — molde B de `guia-panaderia-obrador`, que ya está probado.
9. **Aviso de vocabulario y de ámbito**: normativa española, equivalencias LATAM en primera mención (repostería/pastelería, obrador/taller, escandallo/costeo), y la FAQ «fuera de España» ofreciendo la adaptación como servicio.
10. **Cada cifra del producto con fuente y fecha.** Es literalmente lo que **ninguna** de las 11 fuentes gratuitas hace, y es el único argumento que no puede copiarse con un artículo de blog.

---

*Informe de research. No contiene contenido de producto ni prosa vendible. Todas las URLs consultadas el 2026-09-09 o el 2026-09-10.*
