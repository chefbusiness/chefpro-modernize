# RESEARCH CONSOLIDADO — «Cómo Montar una Pastelería»
## Producto digital NUEVO nº 4 · AI Chef Pro · línea «Cómo Montar» (hermano de `guia-panaderia-obrador`)

**Fecha:** 2026-09-09 / 2026-09-10 (las lentes trabajaron a caballo de la medianoche; esta síntesis se cierra el 10-sep) · **Estado:** research cerrado, PENDIENTE DEL OK DE JOHN antes de escribir una sola línea de producto.
**Fuentes:** las seis lentes de este mismo directorio (`guia-pasteleria-research-L1-competencia.md`, `-L2-serp-demanda.md`, `-L3-normativa.md`, `-L4-sector-equipamiento.md`, `-L5-cliente.md`, `-L6-assets.md`), leídas enteras, más **verificación propia** contra el repo (`src/data/products-catalog.ts`, `src/data/use-cases-content.es.ts`, `astro-site/public/robots.txt`, `astro-site/public/dl/**`, `astro-site/src/content/blog/es/**`, `scripts/productos-digitales/**`, `CALENDARIO-V2-SEMANAL.md`), una consulta **en vivo a GSC** (`sc-domain:aichef.pro`, 2026-06-11 → 2026-09-09) y **una lectura primaria del BOE** que cierra un bloqueante declarado por L3.
**Regla aplicada:** cada cifra lleva fuente y fecha, o va marcada **«sin fuente»**. Nada de memoria del modelo. Este documento es research y propuesta: **no contiene contenido de producto**.

> ### Trece verificaciones propias — cinco de ellas CORRIGEN o AMPLÍAN a las lentes (detalle en §16)
>
> 1. 🔴 **AMPLIACIÓN GRAVE A L6: no es «la hermana rota», es la LÍNEA ENTERA.** L6 midió sólo `guia-panaderia-obrador`. Medidos hoy con PyMuPDF los 10 PDF de `astro-site/public/dl/guia-*/`: **`guia-panaderia-obrador` 1 pág / 55 palabras · `guia-restaurante-casual`, `-japones`, `-mexicano`, `-nikkei`, `-peruano` 1 pág / 33 palabras cada una · `guia-restaurante-gastronomico` (85 €) 10 págs / 2.488 palabras contra «22 capítulos, 119 páginas»**. Los DOCX van de **2.395 a 6.317 palabras** contra promesas de 60-70+ páginas (≈32.000-37.000 palabras a la densidad medida). **El único «Cómo Montar» que entrega lo que promete es `guia-dark-kitchen` (24 €, 27 págs / 7.023 palabras).** Es decir: **6 de los 8 productos de la franja 65-85 € están vacíos**, no uno. Cambia por completo la pregunta 1 de L6 (§15, decisión D2).
> 2. ✅ **CORRECCIÓN A L6: `documentos.py` YA ESTÁ COMMITEADO.** L6 avisaba de que el arreglo de `repartir_puntos()` estaba sin commitear y con otra sesión editándolo en vivo. Hoy `git status --porcelain` sólo devuelve los **seis .md de las lentes** como no rastreados, y `git log -1 -- documentos.py` da **`3c1444d` «fix(documentos): reparto de `puntos` por tramo…»**. El fichero tiene 2.189 líneas y `repartir_puntos()` está en `:1096`. **La acción urgente de L6 está hecha; no hay nada que rescatar.**
> 3. ✅ **CORRECCIÓN A LA ESCALERA que dan L1, L2, L3 y L6: la franja de 65 € ya no son «6 guías Cómo Montar».** Parseado `src/data/products-catalog.ts` entero: **47 productos** y la franja de 65 € tiene **7**, porque el **Manual del Chef Ejecutivo salió a 65 €**, no a los 55 € que recomendaba su propio research (commit `b056abc`, 6-sep). Es el precedente más reciente, más cercano en el tiempo y el que más pesa: **John sube antes que baja cuando el paquete lo aguanta.**
> 4. 🔴 **CIERRO EL BLOQUEANTE V-01 DE L3 con fuente primaria.** Descargado `https://www.boe.es/buscar/pdf/2025/BOE-A-2025-6597-consolidado.pdf` (43 págs) y extraído con `pypdf`. **Disposición final vigésima, literal:** «La presente ley entrará en vigor el **2 de enero de 2025**. No obstante, la disposición adicional sexta, la disposición derogatoria y las disposiciones finales primera, segunda y séptima a décima, entrarán en vigor el **día siguiente al de la publicación**… **Las medidas obligatorias contenidas en el artículo 6 de esta ley serán aplicadas transcurrido el plazo de un año desde la publicación en el "Boletín Oficial del Estado"**». **El metadato del BOE no estaba mal leído: el error está en la propia ley** (publicada el 02-04-2025 y diciendo que entra en vigor el 02-01-2025). Lo operativo y citable: **art. 6 exigible desde el 2-abr-2026**. Y el **art. 21, literal**: leves **hasta 2.000 €**, graves **2.001-60.000 €**, muy graves **60.001-500.000 €**, con las CCAA pudiendo **incrementar** esos umbrales; prescripción 6 meses / 1 año / 2 años (art. 23). Verificados además, literales, el **art. 6.4.c)** (1.300 m² con la regla de acumulación por mismo CIF), el **6.6** (microempresas excluidas) y el **6.7** (pequeñas explotaciones agrarias fuera de toda la ley).
> 5. ✅ **AMPLIACIÓN A L6: el universo de blog no son 6 posts, son 8.** Censados los 164 posts ES que mencionan pastelería/obrador/repostería y contadas las menciones una a una: faltaban **`libreria-de-prompts-para-panaderia-creativa-ai` (55 menciones)** y **`libreria-de-prompts-para-chocolatero-consultor-pro-ai` (40)**. Los banners de los 8 extraídos y verificados (§13.2).
> 6. 🔴 **AMPLIACIÓN A L6: el miswiring del panadero NO está sólo en la página de rol, también está en el BLOG.** Además de `use-cases-content.es.ts:1153` (`panadero` → `kit-tareas-pasteleria`), **dos posts de panadería llevan `kit-tareas-pasteleria` como primer banner**: `libreria-de-prompts-para-panadero-consultor-pro-ai` y `libreria-de-prompts-para-panaderia-creativa-ai`. Son **tres instancias del mismo defecto**, no una.
> 7. ✅ **Confirmo a L6 en el censo de superficies:** **47** entradas en `products-catalog.ts`, **47** en `netlify/shared/payment-links.ts` y **47** en `netlify/shared/product-prices.ts`. Éste sería el **48** en las tres.
> 8. ✅ **Confirmo a L6 en `robots.txt`:** `Disallow: /guia-*-access` y `/guia-*-library` están en los **5 bloques de user-agent** (líneas 35-36, 53-54, 71-72, 89-90, 107-108). **No hay que tocar nada** con el slug `guia-pasteleria-obrador`.
> 9. ✅ **Confirmo el `comingSoon` en los dos ficheros del hub**, con la descripción literal: `ProductosDigitales.tsx:942` y `ProductosDigitalesHubPage.astro:957`, `phase: 'Mayo 2026'`. **Dato nuevo: el array de `comingSoon` sólo tiene DOS entradas** — Pastelería y Chocolatería (`:943` / `:958`). Al publicar, el hub se queda con una sola tarjeta de «Próximamente».
> 10. ✅ **Calibración medida por mí con PyMuPDF, no heredada:** `manual-chef-ejecutivo.pdf` **96 págs / 52.203 palabras = 544 pal/pág** · `guia-food-cost-ingenieria-menu.pdf` **95 / 50.265 = 529** · bonus **406-464**. Confirma a L6.
> 11. ✅ **GSC en vivo confirma a L2 al dígito:** `/guia-panaderia-obrador` **2 clics / 35 impresiones / posición 7,4** en 90 días, y **toda la línea `guia-*` de aichef.pro: 7 clics / 386 impresiones**. Es el mejor predictor que tenemos y es demoledor.
> 12. ✅ **Los prefijos `PA-` y `PS-` están LIBRES y no colisionan entre sí.** `guias-v2-research-sector.json` tiene hoy **225 entradas** con prefijos MICH 10 · REPS 7 · TURG 5 · SECT 10 · TICK 3 · SMI 3 · CONV 7 · TRAM 12 · ANIS 6 · JORN 4 · FC 36 · MM 59 · **CE 40 · CS 23**. Ni un `PA-` ni un `PS-`. **A diferencia del Chef Ejecutivo (donde L3 y L4 se pisaron 23 ids con el mismo prefijo `CE-`), aquí no hay nada que renombrar.**
> 13. ✅ **AMPLIACIÓN A L6 sobre el kit infravendido:** `kit-tareas-pasteleria` entrega **15 xlsx** (contados) y el hub dice «9 checklists» — pero **esa frase aparece 6 veces** en `ProductosDigitales.tsx`, no una: es un patrón de familia. Contados los ficheros de las 18 verticales: 11 en casi todas, **15 en pastelería**, 19 en hotel, 13 en restaurante-creativo, 9 en chef-privado. **Pastelería es el caso más extremo del catálogo (+67 % de lo anunciado).**

---

## 0. Lo primero: qué demanda hay de verdad y por dónde entra el dinero

**Este es el producto con la demanda de búsqueda más baja de los cuatro del ciclo, y ahora está medido con activos propios en vez de por analogía.** Volúmenes de DataForSEO (Google Ads, búsquedas/mes, España, medidos por L2 el 2026-09-09/10):

| Bloque | Keywords | Vol/mes |
|---|---|---|
| **Genérico de CONSUMIDOR** (no es nuestro) | `pasteleria` 110.000 · `confiteria` 9.900 · `obrador` 9.900 · `chocolateria` 9.900 · `reposteria` 6.600 · `bolleria` 4.400 · `dulceria` 3.600 · `cafeteria pasteleria` 2.900 · `pasteleria sin gluten` 2.400 | — |
| **Apertura, el clúster entero** | ~35 cadenas, 25 de ellas en 10/mes | **~330** |
| Las cuatro con intención pura | `obrador compartido` **50** · `requisitos para montar un obrador en casa` **30** · `requisitos obrador pasteleria` **30** · `montar una pasteleria en casa` **20** · `vender reposteria desde casa españa` **20** | **~150** |
| La keyword del nombre | **`como montar una pasteleria`** | **10** — y **10 en los SIETE mercados** (ES, MX, CO, AR, CL, PE, US-es) |

**Cinco lecturas, y ninguna es cómoda:**

1. **Todo lo que pasa de 300 búsquedas/mes en este nicho lo teclea alguien que quiere COMPRAR UN PASTEL.** Las cuatro SERP grandes están dominadas por **local pack de 12 resultados** y negocios locales. `confiteria` (9.900) es el «qué es un token = criptomonedas» de este nicho.
2. **L2 descubrió y validó un filtro barato en 10 SERP: LOCAL PACK presente + AI OVERVIEW ausente = la consulta NO es nuestra.** Las **cuatro únicas SERP con AI Overview** (`requisitos para montar un obrador en casa`, `montar una pasteleria en casa`, `vender reposteria desde casa españa`, `obrador compartido`) son exactamente las cuatro de intención de apertura, y **ninguna tiene local pack**. Es el clasificador más barato para cualquier keyword nueva del nicho.
3. **⚠️ La anti-recomendación más cara del research: NO escribir «Pastelería sin gluten» (2.400/mes).** Su SERP son 12 resultados de local pack más tiendas (`helmacakes.com`, `nicolina.es`, `pastelerialaorientalsingluten.com`) y **ni un solo PAA**: son celíacos comprando tarta. Quien mire la hoja de volúmenes sin abrir la SERP lo propondrá. Igual con «cafetería pastelería» (2.900) y «confitería» (9.900).
4. **La demanda de apertura no existe en NINGÚN mercado hispano.** Sumando España, México, Colombia, Argentina, Chile, Perú y EE. UU. en español, el clúster **no llega a 500 búsquedas/mes**. No hay un «mercado LATAM» al que escaparse.
5. **Y los activos propios ya lo demuestran, que es lo nuevo.** `/kit-tareas-pasteleria` está en **posición media 4,6** —de las mejores de sus 17 hermanas— con **8 impresiones y 0 clics** en 90 días. `/usos/rol/repostero-pastelero` rankea **1,0** para «la repostería» con **1 impresión**. **Rankear aquí no vale nada porque no hay a quién.**

### 0.1 El mejor predictor que tenemos, verificado por mí en GSC hoy

| Landing | Clics | Impresiones | Posición |
|---|---|---|---|
| `/guia-restaurante-peruano` | 2 | 114 | 5,7 |
| `/guia-restaurante-mexicano` | 2 | 66 | 9,6 |
| `/guia-restaurante-japones` | 1 | 53 | 7,4 |
| **`/guia-panaderia-obrador`** | **2** | **35** | **7,4** |
| `/guia-restaurante-gastronomico` | 0 | 50 | 13,6 |
| `/guia-restaurante-casual` | 0 | 46 | 9,0 |
| `/guia-restaurante-nikkei` | 0 | 10 | 5,7 |
| `/guia-food-cost-ingenieria-menu` | 0 | 7 | 6,9 |
| `/guia-dark-kitchen` | 0 | 4 | 39,2 |
| **TOTAL línea `guia-*`** | **7** | **386** | — |

*(GSC `sc-domain:aichef.pro`, filtro `page contains /guia-`, 2026-06-11 → 2026-09-09, consultado por mí el 2026-09-10.)*

**Siete clics en 90 días es lo que el SEO aporta hoy a la línea de producto más cara del catálogo.** Y al pedir el desglose por consulta de `/guia-panaderia-obrador`, GSC devuelve **cero filas**: ni una keyword identificable la alimenta. **Estimación honesta para la landing del 48: 0-5 clics/mes de SEO en el primer año, con 0-2 ventas atribuibles a búsqueda orgánica. No se debe prometer más.**

> ⚠️ **Trampa del histórico legacy, presente también aquí:** dos de las pocas filas GSC del universo pastelería (`universidad de reposteria`, `chocolate school[s]`, posiciones 85-96) cuelgan de `blog.aichef.pro`, ya 301-eado. Son historia, no un suelo del que arrancar — la misma trampa que el 2026-08-04 decidió mal una consolidación.

### 0.2 Por dónde entra el dinero: siete canales, todos nuestros

| Canal | Estado real hoy (verificado por mí) | Qué hay que hacer |
|---|---|---|
| **El producto está ANUNCIADO en el hub desde mayo, y vencido** | `ProductosDigitales.tsx:942` y `ProductosDigitalesHubPage.astro:957`: `{ name: 'Cómo Montar una Pastelería', desc: 'Guía paso a paso: obrador, vitrina, maquinaria, proveedores, licencias y lanzamiento.', phase: 'Mayo 2026' }`. **Cuatro meses de retraso visible al cliente** | Tarjeta real con badge «Nuevo» + **retirar la entrada de `comingSoon` en LOS DOS ficheros**, o quedarán la tarjeta real y la de «Próximamente · Mayo 2026» a la vez |
| **El BUSCADOR del hub ya invita a teclearlo** | `ProductosDigitalesHubPage.astro:2259`: «montar una pastelería» es uno de los ejemplos animados del placeholder de `placeholderAnimado()`. **El hub lleva meses invitando a buscar un producto que no existe.** Hoy esa consulta cae en la tarjeta `comingSoon` | Al lanzar, cae en el producto real: el ejemplo pasa de promesa a acierto. Añadir el alias de búsqueda (§13.1) |
| **8 posts propios de pastelería/panadería/chocolatería, todos con sus 3 banners** | Verificado post a post (§13.2). El peor encaje actual: `ai-chef-pro-un-chatgpt-para-la-pasteleria-profesional…` vende `guia-restaurante-gastronomico` | **Sustitución quirúrgica** en 3 posts + enlace contextual en el resto |
| **3 páginas `/usos/rol/` del público exacto** | `pasteleria-obrador` (`:2660`), `repostero-pastelero` (`:1996`) y —si entra la variante— `cafeteria-brunch` (`:2217`). Las tres venden hoy los mismos 6 productos, **todos de 9-18 €** | Enlace **bidireccional** + añadir `guia-pasteleria-obrador` a sus `productIds`. Y de paso cerrar el hueco: **`guia-panaderia-obrador` aparece 0 veces en las 51 páginas de rol** |
| **Rotación general de banners** | 325 posts ES con 3 banners y rotación por los 44+ productos (`fase8e-banners-corpus.py`, 2026-08-31) | Entrada **48** en `products-catalog.ts` → entra en la rotación sola |
| **Lista de compradores (Resend)** | Segmentos de `kit-tareas-pasteleria` (12 €), `kit-escandallos` (12 €), `pack-appcc` (14 €), Guía Food Cost (55 €), Manual del Manager (55 €), Manual del Chef Ejecutivo (65 €) | **Broadcast propio** (regla de John del 5-sep, cola de 5 días). Hueco natural **14-oct**, con la trampa del tope de 30 días de Resend (§13.3) |
| **Plataforma (Pickaxe)** | Agentes **«Pastelero Consultor Pro»**, **«Pastelería Creativa»** y **«Hotel Pastry & Bakery Pro»** (este último **en inglés siempre**, es del bloque de hotelería) | Mención desde el agente y desde su librería de prompts |

**Conclusión del bloque, sin adornos:** este producto **no se lanza por volumen de búsqueda** — la keyword de su nombre vale 10/mes en los siete mercados y la línea hermana lleva 7 clics en 90 días. Se lanza porque (a) el hueco de pago está medido producto a producto y hay una franja limpia entre 49 € y 357 € (§7), (b) **lleva anunciado desde mayo en dos ficheros y hasta el buscador del hub lo sugiere**, (c) tenemos siete canales propios y una base de compradores de pastelería que ya pagó por las plantillas, y (d) es el primer «Cómo Montar» que entregaría de verdad lo que promete (§16, verificación 1). **La landing no va a captar por búsqueda y no se debe prometer que lo haga.**

---

## 1. Los tipos de negocio y los conceptos que la guía DEBE fijar

### 1.1 Bloque obligatorio 1 — Los 11 sub-conceptos del nicho (ids `PS-01` a `PS-11`)

**La decisión más cara que toma el lector es qué tipo de pastelería monta, y es la que casi ningún contenido de la SERP le plantea de forma comparada.** El salto entre extremos es de **dos órdenes de magnitud**: de 3.000 € a 250.000 €.

| id | Sub-concepto | Inversión de referencia | Qué cambia estructuralmente |
|---|---|---|---|
| **PS-01** | **Obrador en casa / venta directa** | **3.000-5.000 €** (mínimo viable) · **5.000-8.000 €** arranque · **30.000 €+** profesional completo | 🔴 **Régimen legal PROPIO y muy restrictivo** (art. 13 del RD 1021/2022, PA-29): lista blanca de producto, prohibido congelar, tope de **100 kg/semana**, venta sólo en mercados o reparto dentro de la zona de salud, mención «Elaborado en vivienda particular» |
| **PS-02** | **Obrador solo producción (a puerta cerrada)** | **8.000-12.000 €** mínimo · **15.000-20.000 €** completo | Sin escaparate ni licencia comercial; el cliente es B2B o encargo. **Se juega el umbral del art. 3** (PA-02) |
| **PS-03** | **Local con venta / despacho** | **15.000-25.000 €** mínimo · **30.000-50.000 €+** completo | Aparece la licencia de actividad comercial, la vitrina refrigerada y el mobiliario de venta |
| **PS-04** | **Cafetería-pastelería con obrador** | **60.000-80.000 €** mínimo · **100.000 €+** completo | 🔴 **Salto de categoría legal**: en cuanto hay comidas preparadas entra el **art. 30 del RD 1086/2020** (PA-16), puede cambiar el convenio y cambia el IVA (§2.4) |
| **PS-05** | **Pastelería mediana (obrador + tienda), escenario de consultoría** | **100.000-150.000 €** · escenario tipo de **90 m² = 137.000 €** | Es el escenario «tipo» de la mayoría de las fuentes publicadas. **Es el caso central del producto** |
| **PS-06** | **Punto caliente pequeño** | **60.000-100.000 €** | Regenera producto congelado; **no fabrica** → no puede usar «ELABORACIÓN PROPIA» (PA-17) |
| **PS-07** | **Local céntrico / grande** | **150.000-250.000 €** | El alquiler y la obra dominan la inversión |
| **PS-08** | **Franquicia** | Granier **desde 83.000 €** (100franquicias) o **desde 180.000 €** (franquiciashoy), canon **8.000 €**, royalty 500 €/mes, 100 m² mín. · Levaduramadre **99.000 €** canon incluido · modelo autoempleo de Granier **desde 10.000 €** | Canon + royalty + obligación de compra a central; a cambio, obrador central y marca. ⚠️ **Los portales se contradicen dentro del mismo dato** (§15.1) |
| **PS-09** | **Obrador B2B para hostelería** | «sin fuente» de inversión; en el caso Cientotreinta grados el **30 %** de las ventas es canal restauración | Producción a volumen, ventas a crédito, menos escaparate. **Aquí es donde se rompe el «marginal, localizado y restringido»** |
| **PS-10** | **Pastelería sin gluten / sin alérgenos** | «sin fuente» | Exige obrador separado o protocolo de línea validado **analíticamente ≤20 mg/kg** (PA-23) |
| **PS-11** | **Pastelería sin salida de humos** | Ahorra el conducto de acero inoxidable, que **«puede superar los 6.000 €»** | Sólo hornos 100 % eléctricos + campana de condensación; obliga a desagüe en el punto del horno y condiciona el surtido |

**Fuentes:** PS-01…PS-04, PS-11 → Tamara Viñas, «Cómo montar un negocio de pastelería: guía 2026», **12-jul-2026**, https://pasteleriaparatodos.com/guia-montar-negocio-pasteleria/ (consultada 2026-09-10) · PS-05 → La Hostelera, https://www.lahostelera.com/blog/cuanto-dinero-necesito-para-montar-un-negocio-de-reposteria-o-pasteleria/ (**la página no publica fecha**; comentario más reciente 22-ago-2025) · PS-06/07/08 → plandenegocio.es, **13-abr-2026**, https://plandenegocio.es/cuanto-cuesta-abrir-pasteleria/ · PS-08 Granier → https://www.franquiciashoy.es/franquicias/franquicias-de-panaderias-y-pastelerias/panaderias-pastelerias/granier y https://www.100franquicias.com/franquicias/alimentacion/granier/Franquicia-granier-negocio.htm · PS-08 Levaduramadre → https://www.foodretail.es/retailers/levaduramadre-rozo-los-50-millones-de-facturacion-en-2025-el-16-mas-y-abrio-31-locales.html · PS-09 → Guía Repsol, 25-ene-2024 · PS-11 → Salva Industrial, https://www.salva.es/es/blog/montar-una-panaderia-y-pasteleria-sin-salida-de-humos (**sin fecha**).

**Sin cifra publicada localizable, y por tanto sin número en el producto:** *cake design / tartas por encargo* (decenas de negocios activos, cero cifras), *heladería-pastelería*, *online / delivery puro*. Van como **marco de decisión cualitativo**, nunca como cifra (§15.1).

### 1.2 Los 12 conceptos que la SERP mezcla y que la guía tiene que fijar

Es el equivalente a las 16 distinciones del Manual del Chef Ejecutivo. Aquí son **12**, y el reparto es duro para lo gratuito: **en 6 de ellas lo gratuito afirma algo FALSO**.

| # | Concepto | Qué es exactamente | Con qué se confunde | ¿Lo cubre bien lo gratuito? |
|---|---|---|---|---|
| 1 | **RGSEAA vs registro autonómico** 🔴 | La pastelería minorista que vende al consumidor final **está EXCLUIDA del RGSEAA** (art. 2.2 del RD 191/2011 en la redacción del RD 1021/2022). Lo que hay es una **comunicación o declaración responsable autonómica «que no será habilitante»** | Se vende como que el «Registro Sanitario» es obligatorio siempre | **NO, y es el error nº1 del nicho** (PA-01, E-01). Lo dicen las consultoras que **venden el trámite** |
| 2 | **Cuándo SÍ vuelve el RGSEAA** 🔴 | Los tres requisitos del art. 3 son **ACUMULATIVOS**: marginal (≤25 % anual **o** máx. 500 kg/semana, **incluyendo la venta a consumidor final**), localizado (misma zona de salud, o ≤50 km entre CCAA) y restringido (no suministrar a inscritos en RGSEAA) | Se cree que basta con «vender poco» | **NO.** Vender el 10 % a una cadena inscrita rompe *restringido* y obliga a inscribirse; y **el tope de 500 kg incluye el mostrador**, así que una pastelería que despacha mucho puede pasarse sin haber hecho un solo B2B (PA-02) |
| 3 | **Obrador central + sucursales no consume cuota** | El art. 3.6 exceptúa el flujo del establecimiento central a sus sucursales de misma titularidad: **no se considera suministro entre minoristas** | Se cree que abrir un segundo despacho te mete en el B2B | **NO.** Es una palanca de crecimiento que casi ninguna fuente explica (PA-03) |
| 4 | **La temperatura de la vitrina** 🔴 | Art. 4.1 fila 9: «**Productos de pastelería rellenos (salvo que sean estables a temperatura ambiente) — igual o inferior a 4 °C**». Y el art. 9.3 exige ≤8 °C a lo elaborado con huevo: **en una tarta de crema mandan los 4 °C** | Circula «8 °C y 24 horas» del RD 1254/1991 | **NO, y es peligroso.** El **RD 1254/1991 está DEROGADO** con efectos 22-dic-2022 y sigue citado en páginas de higiene y de proveedores (PA-12, PA-14, E-03) |
| 5 | **Huevo: tres vías legales, no una** 🔴 | Art. 9 del RD 1021/2022: **70 °C/2 s** en el centro · **63 °C/20 s + consumo inmediato** · o **ovoproducto de establecimiento autorizado**. Lo del apartado 1.a) no estable y lo del 2: ≤8 °C, **24 h** y **registro de fecha y hora** | Se cree que «con huevo pasteurizado ya está» o que sigue el decreto de la mayonesa | **NO. Es el corazón técnico de una pastelería**: merengue italiano, crema pastelera, mousse, tiramisú y buttercream caen cada uno en una vía distinta (PA-14, PA-15) |
| 6 | **«Obrador en casa» ≠ «negocio de tartas desde casa»** 🔴 | El art. 13.8 sólo permite en vivienda: comidas preparadas con tratamiento térmico suficiente, **repostería estable a temperatura ambiente**, mermeladas con tratamiento posterior al envasado y conservas con **pH<4,5**. Prohíbe **congelar** (13.5.e), prohíbe **colectividades y eventos** (13.5.b), topa en **100 kg/semana** (13.9) y obliga a la mención «**Elaborado en vivienda particular**» + fecha (13.10) | La SERP entera vende «monta tu negocio de tartas desde casa» | **NO, y es la corrección más brutal del research: la tarta de nata por encargo desde casa NO es legal.** Las galletas decoradas y los bizcochos secos, sí. Ninguna de las páginas medidas lo dice (PA-29, E-04) |
| 7 | **El «carnet de manipulador» no existe** | El **RD 202/2000 fue derogado por el RD 109/2010**, y el RD 1021/2022 (22 artículos, índice leído entero) **no tiene ni un artículo de formación**. La obligación es del empresario, por el Anexo II Cap. XII del Rgto. 852/2004, y hay que **poder acreditarla** | Se vende el carnet como requisito legal | **NO, y lo dicen justamente los que venden el curso** (PA-11, E-02). Cambia el entregable: lo que hace falta es un **registro de formación**, no un curso |
| 8 | **«ELABORACIÓN PROPIA» es voluntaria y tiene exclusiones expresas** | Art. 11 del RD 1021/2022: mención **voluntaria**; quien la usa sólo vende en el establecimiento donde elaboró o en sus sucursales; y **no es elaboración fraccionar o envasar producto de otro fabricante** | Se pone en el escaparate como reclamo sin comprobar si aplica | **NO.** Es una palanca de escaparate verificada frente a quien hornea congelado ajeno (PA-17) |
| 9 | **«Artesano» en pastelería NO tiene definición estatal** | El «pan artesano» del art. 10 del RD 308/2019 **no es extrapolable**. En pastelería es competencia **autonómica**: Cataluña, Decreto 85/2024, con **carné de artesano** y acreditación; Andalucía, Decreto 352/2011; Madrid sólo tiene un **PROYECTO** de decreto | Se usa «artesano» como sinónimo de «hecho a mano» | **NO** (PA-24, PA-26). ⚠️ Nivel B: **verificar el articulado del RD 496/2010 antes de afirmarlo** |
| 10 | **«Sin gluten» es un umbral analítico, no una declaración libre** | Rgto. Ejec. (UE) 828/2014: **≤20 mg/kg** «sin gluten», **≤100 mg/kg** «muy bajo en gluten» | Se anuncia «sin gluten» por usar harina de arroz | **NO.** Un obrador con harina de trigo en el aire **no puede declararlo** sin validar analíticamente. La certificación FACE es voluntaria y **adicional** (PA-23) |
| 11 | **Libertad horaria: la pastelería la tiene POR LEY** | Art. 5.1 de la Ley 1/2004: los establecimientos dedicados **principalmente** a la venta de «pastelería y repostería, pan» tienen «plena libertad para determinar los días y horas en que permanecerán abiertos» | Se cree que hay que consumir uno de los 16 domingos habilitados | **NO, y es un argumento de negocio.** El domingo es el día de la tarta. ⚠️ Matiz: exige que la pastelería sea la actividad **PRINCIPAL** — una cafetería-pastelería con más caja de cafetería podría quedar fuera (PA-39) |
| 12 | **Margen bruto y food cost son la MISMA regla dicha dos veces** | «margen bruto 65-70 % sobre coste» ⇔ «food cost por debajo del 30-35 %» | Se presentan como dos reglas independientes y el lector intenta cumplir las dos | **NO** (PS-55/56). **Trampa de redacción detectada:** el xlsx debe calcular una desde la otra y **nunca pedir las dos** |

**Ese es el índice de criterio de la guía: 12 distinciones, 6 de ellas donde lo gratuito afirma algo falso, y todas comprobables por el lector en un minuto abriendo el BOE.** Es la mejor prueba de criterio que puede dar un producto de pago en un nicho donde las cifras se contradicen por un factor 13.

### 1.3 Los cinco errores de método de lo gratuito, que la guía corrige con autoridad

| Error | Dónde se midió | Qué hace la guía |
|---|---|---|
| **Horquilla de inversión de factor ×3 a ×13 sin decir la hipótesis** | 15.000 € (Tamara Viñas, local con venta) frente a 200.000 € (plandenegocio.es y lexpress). **Ninguna** declara m², plaza, si el local viene vacío o traspasado, ni si incluye fondo de maniobra | **No da un número: da el modelo que produce el número del lector**, con sus m², su plaza y su carta, y declara la hipótesis que lleva dentro |
| **Normativa derogada viva y rankeando** | `emprendedores.es` publica en una URL llamada literalmente `plan-de-negocio-pasteleria` un artículo del **14-abr-2021** que **no contiene ningún plan de negocio** y cita el **RD 2207/1995**, derogado en higiene por el paquete comunitario | Norma + artículo + enlace + **fecha de verificación** en cada afirmación, y un apartado que enseña a abrir la ficha de vigencia del BOE |
| **El punto legal más delicado despachado en una línea** | La guía de obrador en casa de `pasteleriaparatodos` (18-jun-2025) resuelve el RGSEAA en una frase **sin citar reglamento ni autoridad autonómica** — y es justo lo que pregunta el PAA | Capítulo entero con la **lista blanca del art. 13.8** y el árbol de decisión de registro |
| **«Rentabilidad» en el titular y ni un margen en el cuerpo** | `lexpress-franchise.com` (08-abr-2026) titula rentabilidad y no da ninguna | La cifra honesta y poco vendible: **8-12 % neto** (PS-48), con nombre y empresa detrás |
| **Contenido de 2020 rankeando en 2026 sin revisar** | `sillasmesas.es` (sep-2020): cero euros, cero m², cero plazos. Es el catálogo de un proveedor de mobiliario disfrazado de guía | Fecha de edición visible, anexo normativo fechado y actualizaciones incluidas en el precio |

---

## 2. Bloque obligatorio 2 — Regulación España 2026 (ids `PA-*`)

L3 leyó **texto consolidado** en `boe.es` y **extrajo PDF oficiales con `pypdf`** cuando el HTML sólo servía el índice (así se obtuvo el articulado literal del RD 1021/2022 y dos publicaciones del BOCM). Usa tres niveles: **A** = texto literal leído en boletín oficial (citable entrecomillado) · **B** = norma identificada, contenido por fuente oficial indirecta (**no citar entrecomillado**) · **C** = sólo fuente secundaria (**no entra en el producto**).

**Los prefijos `PA-` (normativa) y `PS-` (sector) están libres y no colisionan** — verificado por mí sobre `guias-v2-research-sector.json` (225 entradas). **Nada que renombrar**, a diferencia del Chef Ejecutivo.

### 2.1 El núcleo verificado a nivel A (lo que sostiene el producto)

| id | Tema | Qué dice la norma | Norma y artículo | Nivel |
|---|---|---|---|---|
| **PA-01** 🔴 | **Registro sanitario** | Los establecimientos de comercio al por menor quedan **excluidos del RGSEAA**; se inscriben en el registro autonómico «previa **comunicación o declaración responsable, que no será habilitante**» | RD 191/2011 art. 2.2, en la redacción de la D.F. 1ª del **RD 1021/2022** | **A** |
| **PA-02** 🔴 | **Los tres umbrales acumulativos** | **Marginal**: ≤25 % del volumen anual **o** máx. **500 kg/semana** «incluyendo el suministro a consumidor final». **Localizado**: misma unidad sanitaria local o zona de salud; **≤50 km** entre CCAA. **Restringido**: no suministrar a inscritos en RGSEAA. Y **declaración responsable** + registros de destinatarios, cantidades y fechas | RD 1021/2022, **art. 3.1 a 3.5** | **A** |
| **PA-03** | **Central + sucursales** | «se considerarán una única unidad comercial»; el suministro del central a sus sucursales **no se considera suministro entre minoristas**. Definiciones literales de *obrador* («parte de un establecimiento… **inaccesible al público**»), *establecimiento central* y *sucursales* | RD 1021/2022, art. 3.6 y art. 2.2 | **A** |
| **PA-04** 🔴 | **Madrid acaba de crear su registro** | **DECRETO 26/2026, de 25 de marzo** (BOCM núm. 73 de 27-mar-2026, **leído íntegro**): 11 artículos en 4 capítulos; **sección específica para viviendas privadas** (art. 6.d); comunicación —o declaración responsable en vivienda— **no habilitante** (art. 8.1); presentación **simultánea al inicio de la actividad** (art. 9.1); deroga la Orden 1531/2005; en vigor el **28-mar-2026** con **período transitorio de UN AÑO** para las ya abiertas → vence el **28-mar-2027** | BOCM-20260327-1 | **A** |
| **PA-10** | **APPCC simplificado** | «deberán crear, aplicar y mantener actualizado un procedimiento permanente basado en los principios del APPCC… **debiendo contar con una persona responsable de su aplicación**… **se podrán aplicar de manera simplificada**» conforme a la Comunicación **2020/C 199/01**. Las guías sectoriales son **voluntarias** | RD 1021/2022, **art. 20** | **A** |
| **PA-11** | **El carnet de manipulador no existe** | El índice completo del RD 1021/2022 (22 artículos) **no contiene ningún artículo de formación**. El RD 202/2000 fue **derogado por el RD 109/2010**. La obligación es del operador (Anexo II Cap. XII del Rgto. 852/2004) y hay que **poder acreditarla** | Ausencia confirmada + BOE-A-2010-2696 | **A** (ausencia) / B (derogación) |
| **PA-12** 🔴 | **Temperatura de la vitrina** | Tabla del art. 4.1, **fila 9**: «Productos de pastelería rellenos (salvo que sean estables a temperatura ambiente) — **≤ 4 °C**». Congelados **≤ −18 °C**. Lo no tabulado, «a las temperaturas indicadas en la etiqueta» (4.2); el transporte mantiene esas temperaturas (4.3) | RD 1021/2022, art. 4 | **A** |
| **PA-13** | **Congelación y descongelación** | Equipo con potencia para alcanzar **−18 °C en el centro con descenso ininterrumpido** (→ **un arcón doméstico no vale como abatidor**); **6 registros mínimos** o etiqueta equivalente; descongelación **en refrigeración**; venta de descongelado con la palabra «**descongelado**»; **recongelación prohibida** salvo transformación posterior | RD 1021/2022, art. 5 | **A** |
| **PA-14** 🔴 | **Huevo y ovoproductos** | El **RD 1254/1991 está DEROGADO** con efectos **22-dic-2022** (D.D.ú.d del RD 1021/2022, nota confirmada en el propio BOE). Hoy rige el **art. 9**: **70 °C/2 s** · **63 °C/20 s + consumo inmediato** · o **ovoproducto autorizado**; ≤**8 °C** y **24 h** con **registro de fecha y hora** | RD 1021/2022, art. 9 | **A** |
| **PA-16** | **Zonas de degustación** | «podrán existir zonas de degustación… En el caso de que **elaboren comidas preparadas**, deberán cumplir con lo establecido en el **artículo 30 del RD 1086/2020**… en una **zona separada de la zona de ventas**» | RD 1021/2022, art. 10 y art. 6 | **A** (⚠️ el art. 30 del RD 1086/2020 **no consultado**: V-03) |
| **PA-17** | **«ELABORACIÓN PROPIA» / «ELABORADO POR»** | Menciones **voluntarias**; con «ELABORACIÓN PROPIA» **sólo se puede vender en el establecimiento donde se elaboró o en sus sucursales**; y **«no se considerará elaboración el fraccionamiento o el envasado» de producto de otro fabricante** | RD 1021/2022, art. 11 | **A** |
| **PA-18** | **Recipientes del cliente y doggy bag** | Aceptar el recipiente del cliente es **potestativo**; el comprador responde de su higiene y el vendedor **siempre puede rechazarlo**, quedando **exento de responsabilidad**. El **art. 18.5** obliga a **restauración y hostelería** (no al despacho de pastelería) a facilitar llevarse lo no consumido **sin coste**, salvo bufé libre | RD 1021/2022, art. 18 | **A** |
| **PA-20** | **Venta de producto con defectos** | Se pueden vender productos con **defectos de forma y tamaño** y **defectos gráficos de etiquetado o envasado** (salvo conservas abombadas), informando al consumidor. Es la base legal del «rincón de los feos» | RD 1021/2022, art. 17 | **A** |
| **PA-29** 🔴 | **Obrador en casa: el régimen completo** | Zonas de la vivienda = establecimiento minorista (13.2); **declaración responsable con horario, productos y PLANO de la vivienda** (13.3); venta sólo en mercados ocasionales/periódicos o **reparto a domicilio dentro de la zona de salud** (13.4); **prohibido** consumo in situ, colectividades y eventos, suministro en el propio establecimiento, suministro a otros minoristas y **congelar** (13.5); separación temporal y en su caso espacial del uso doméstico (13.6); **sin personas ajenas ni animales domésticos** (13.7); **lista blanca** de producto (13.8); **≤100 kg/semana demostrables** (13.9); etiqueta «**Elaborado en vivienda particular**» + fecha (13.10) | RD 1021/2022, art. 13 | **A** |
| **PA-32** | **SMI 2026** | **40,70 €/día · 1.221 €/mes · 17.094 €/año** en 14 pagas; **+3,1 %**; vigencia 1-ene a 31-dic-2026; eventuales ≤120 días **57,82 €**/jornada; el art. 3 lo configura como **referencia ANUAL** a efectos de compensación y absorción | **RD 126/2026**, BOE-A-2026-3815 | **A** |
| **PA-33** 🔴 | **Hay convenio PROPIO de pastelería, y en Madrid manda sobre el SMI** | Convenio del Sector de Comercio e Industria de Confitería, Pastelería, Bollería, Repostería, Heladería y Platos Cocinados de la Comunidad de Madrid (código **28001025011981**). Revisión 2026 en **BOCM núm. 50 de 28-feb-2026**, leída íntegra: **+2,9 %**, **15 pagas**, áreas funcionales **OBRADOR / COMERCIO / ADMINISTRACIÓN** y 6 grupos: **1.733,88 · 1.427,89 · 1.376,91 · 1.249,42 · 1.192,42 · 1.192,42 €/mes**. **El grupo más bajo (17.886,30 €/año) supera el SMI anual (17.094 €)** | BOCM-20260228-2 | **A** |
| **PA-39** | **Libertad horaria por ley** | Art. 5.1: los establecimientos dedicados **principalmente** a la venta de «pastelería y repostería, pan»… tienen «plena libertad para determinar los días y horas en que permanecerán abiertos». Art. 3.1: mínimo **90 h** semanales en laborables. Art. 4.1: mínimo **16** domingos y festivos. Art. 2: la regulación concreta es **autonómica** | **Ley 1/2004** (mod. RD-ley 20/2012) | **A** |
| **PA-31** 🔴 | **Ley 1/2025 de desperdicio — RESUELTA POR MÍ HOY** | **D.F. vigésima, literal:** «La presente ley entrará en vigor el **2 de enero de 2025**» (fecha **anterior a su publicación**: el error está en la propia ley) «No obstante, la disposición adicional sexta, la disposición derogatoria y las disposiciones finales primera, segunda y séptima a décima, entrarán en vigor el **día siguiente al de la publicación**» (= **3-abr-2025**) «**Las medidas obligatorias contenidas en el artículo 6… serán aplicadas transcurrido el plazo de un año desde la publicación**» (= **2-abr-2026**). **Art. 6.4.c) literal:** exentas las actividades de transformación, comercio minorista, distribución, hostelería o restauración en establecimientos **≤1.300 m²** (o superficie útil de exposición y venta ≤1.300 m² si hay venta al público); **«En todo caso… quedarán obligados los establecimientos que operen bajo un mismo código de identificación fiscal y que, en su conjunto, superen los 1.300 m²»**. **Art. 6.6:** «Las microempresas quedan excluidas de las obligaciones a las que se refieren los apartados anteriores». **Art. 6.7:** pequeñas explotaciones agrarias, fuera de **toda** la ley. **Art. 21, literal:** leves **apercibimiento o multa de hasta 2.000 €** · graves **entre 2.001 y 60.000 €** · muy graves **entre 60.001 y 500.000 €**, y **las CCAA pueden incrementar esos umbrales**. **Art. 23:** prescripción 6 meses / 1 año / 2 años | Ley 1/2025, PDF consolidado BOE-A-2025-6597, **leído por mí el 2026-09-10** | **A** |

### 2.2 Lo que está a nivel B y NO se puede citar entrecomillado

`PA-05` régimen general de declaración responsable (Directiva 2006/123/CE + Ley 20/2013 + Ley 39/2015 art. 69; **cada municipio tiene su ordenanza**) · `PA-07` salida de humos (CTE **DB-HS 3**: salida en cubierta, ≥3 m de tomas de ventilación, conductos EI 30 a <1,50 m de fachada no EI 30 — ⚠️ **hay que citar el DB-HS oficial, no el PDF de tercero que se leyó**) · `PA-09` las tres novedades del **Rgto. (UE) 2021/382** (Cap. XI bis cultura de seguridad alimentaria, punto de alérgenos en el Cap. IX, Cap. V bis de redistribución) · `PA-21` los 14 alérgenos en no envasado (**RD 126/2015**: obligatorio en no envasado art. 4; carteles o etiquetas art. 6.2; vía oral admisible **con constancia escrita en el establecimiento** art. 6.5.a; **al menos en castellano** art. 10; envasado por el propio minorista sin identificación de lote art. 5) · `PA-23` sin gluten (828/2014) · `PA-24` **RD 496/2010 VIGENTE** con las definiciones legales de confitería / bollería / pastelería y repostería · `PA-25` RD 308/2019 si la pastelería vende pan · `PA-26` artesanía autonómica · `PA-27/28` venta a distancia (**ya dentro de la definición de minorista**, art. 2.2.a; información obligatoria **antes de la compra** y completa **en la entrega**, art. 14 del Rgto. 1169/2011) · `PA-30` envases (Ley 7/2022 y **RD 1055/2022**, con los **5 tramos del art. 9.4**: <120 m² → 1 referencia reutilizable de bebida desde **1-ene-2027**) · `PA-34` registro de jornada (vigente en papel/Excel; **reforma digital en tramitación**, exigibilidad estimada 2027) · `PA-35` **PRL de obrador: la harina es SENSIBILIZANTE** y provoca asma del panadero (INSST, BASEQUIM 030) · `PA-36` IVA · `PA-37` Verifactu · `PA-38` epígrafes de IAE · `PA-40` accesibilidad (**RD 193/2023**, exigibilidad privada **1-ene-2029** nuevos / **1-ene-2030** existentes).

### 2.3 Estado de vigencia a 2026-09-10

| Norma | Estado |
|---|---|
| RD 1021/2022 · RD 191/2011 (mod.) · Rgto. 852/2004 + 2021/382 · Rgto. 1169/2011 + RD 126/2015 · Rgto. Ejec. 828/2014 · **RD 496/2010** · RD 308/2019 · Ley 7/2022 · RD 1055/2022 · Ley 1/2004 · RDLeg 1/2013 + RD 193/2023 | **VIGENTES** |
| **Decreto 26/2026** (Madrid) | **VIGENTE desde 28-mar-2026** · transitorio hasta **28-mar-2027** |
| **Ley 1/2025** | **VIGENTE**; art. 6 exigible desde el **2-abr-2026** (verificado por mí) |
| **RD 126/2026** (SMI) y revisión 2026 del convenio de Madrid | **VIGENTES**, caducan el **31-dic-2026** |
| **RD 1254/1991** (mayonesa/huevo) · **RD 3484/2000** · **RD 1420/2006** | **DEROGADOS** desde el **22-dic-2022** |
| **RD 202/2000** (carnet de manipulador) | **DEROGADO** desde el 20-02-2010 |
| **RD 2207/1995** (el que cita `emprendedores.es`) | Superado en higiene por el paquete comunitario |
| **Verifactu** (RD 1007/2023 + RD-ley 15/2025) | Plazos aplazados a **1-ene-2027** (IS) y **1-jul-2027** (resto). Los fabricantes de software ya obligados desde el **29-jul-2025** |

### 2.4 Qué de esto es argumento de venta, y qué NO se puede decir en el copy

**Sí es argumento (y es honesto):**

1. **El error nº1 del nicho tiene dueño: las consultoras que venden el trámite.** Decir «no necesitas el RGSEAA para una pastelería minorista, y aquí está el artículo» se separa solo, y ahorra dinero real al lector el primer día.
2. **«La tarta de nata por encargo desde casa no es legal».** Es el segmento con más búsqueda del nicho (~120/mes agregado), es donde un competidor vende un producto de **357 €**, y es donde lo gratuito se equivoca de plano. **Es la mejor prueba de criterio del producto entero.**
3. **La libertad horaria por ley** (art. 5.1 de la Ley 1/2004): un dato verificado, poco conocido y directamente convertible en estrategia comercial (el domingo es el día de la tarta).
4. **Las tres vías del huevo** y la resolución del conflicto 4 °C / 8 °C: es la decisión técnica que toma un pastelero cada día y no está resuelta en ningún sitio en español.
5. **El plazo de Madrid vence el 28-mar-2027.** Un producto publicado en otoño de 2026 llega justo a tiempo de avisar a las pastelerías madrileñas ya abiertas. ⚠️ **Tiene fecha de caducidad comercial** (§15.3, R-03).

**NO se puede decir** (además de la lista negra completa del §15):

- ❌ **«Cumple la normativa española»** / «tu pastelería quedará 100 % legal». La responsabilidad es del operador. Fórmula segura: «el mapa normativo completo, con la norma, el artículo y el enlace».
- ❌ **Ninguna cifra de inversión ni de rentabilidad como promesa.** No hay fuente primaria (PA-43): se entrega un modelo, no un número.
- ❌ **Promesas de tráfico SEO.** 10-20 búsquedas/mes para la intención de apertura.
- ❌ **«Válido en toda Hispanoamérica».** Marco español (regla de John del 5-sep); la FAQ ofrece la adaptación **como servicio**.
- ❌ **«Verifactu es obligatorio en 2026»**, **«incluye el carnet de manipulador»**, **«podrás llamarte artesano»**, **«podrás vender tus tartas desde casa»** sin la lista blanca.
- ❌ **«AI Chef Pro tiene plan gratuito»** — no lo tiene desde el 15-ago-2025: «desde 10 €, 10.000 créditos».
- ⚠️ **Y el límite de la regla de John del 5-sep:** en Stripe y en los titulares lideran **los entregables y el beneficio práctico**. «Verificado contra el BOE» se mantiene **dentro** del producto, en la landing larga y en el email — como rigor, nunca como gancho.

### 2.5 Las siete verificaciones que L3 dejó abiertas (una la he cerrado yo)

| # | Qué falta | Estado |
|---|---|---|
| **V-01** | Fecha de entrada en vigor y sanciones de la **Ley 1/2025** | ✅ **CERRADA POR MÍ** (§16, verificación 4): art. 6 exigible desde el **2-abr-2026**; sanciones 2.000 / 60.000 / 500.000 € leídas literales |
| **V-02** | **Art. 91 de la Ley 37/1992 literal** (10 % / 4 % / hostelería / bebidas azucaradas) | 🔴 **ABIERTA y bloqueante para el capítulo de precios.** «Pastelería al 10 %» es hoy una **inferencia** del régimen general vía la Resolución DGT de 24-feb-2025, que **sólo trata del pan**. Y falta el tipo de los **servicios de hostelería**: la misma tarta puede llevar tipo distinto para llevar y en mesa |
| **V-03** | **Art. 30 del RD 1086/2020** (comidas preparadas) | 🔴 **ABIERTA.** Es la puerta de toda la variante pastelería-cafetería. **No escribir ese capítulo sin leerlo** |
| **V-04** | Articulado del **RD 496/2010** y confirmación de que NO regula «artesano/artesanal/casero» | ABIERTA. Es un dato de valor comercial: cerrarlo con `grep` sobre el PDF consolidado |
| **V-05** | **RD 1055/2022:** ¿una pastelería que envasa es «productor de producto»? | 🔴 ABIERTA. **La duda de mayor impacto económico del bloque de envases**: es la diferencia entre un trámite anual y ninguno |
| **V-06** | **Venta online a toda España**: ¿rompe algún requisito sanitario o exige RGSEAA? | ABIERTA. El art. 3 regula el suministro **a otros establecimientos**, no al consumidor final, pero la hipótesis hay que refutarla expresamente |
| **V-07** | **Decreto 13/2025** (C. Valenciana) y **Decreto 85/2024** (Cataluña) en su boletín | ABIERTA (`noticias.juridicas.com` dio error de certificado TLS dos veces) |

**Verificaciones menores pendientes:** RD 919/2006 / RITE para horno de gas (PA-08) · Ley 37/2003 del Ruido y ordenanza municipal (PA-42, **bloque entero sin investigar**) · DB-SUA de accesibilidad · actualización de 27-feb-2026 del RD 308/2019 · convenios de Barcelona 2026, Valencia y Sevilla · redacción vigente de las tarifas del IAE · Rgto. 852/2004 consolidado en EUR-Lex para citar literalmente el Cap. XI bis y el Cap. XII.

> **Recomendación de método (decisión D8):** V-02, V-03 y V-05 son **bloqueantes de capítulo**, no del producto. La forma barata de cerrarlos es la que ya funcionó: **descargar el PDF consolidado del BOE y extraerlo con `pypdf`** — es lo que me ha permitido cerrar V-01 en dos minutos cuando el HTML del BOE sólo servía el índice.

---

## 3. Bloque obligatorio 5 — El sector y el modelo de negocio (ids `PS-*`)

### 3.1 Rentabilidad y márgenes: el bloque más valioso de todo el research

| id | Métrica | Valor | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-48** 🔴 | **Rentabilidad NETA de una pastelería «yendo bien»** | **8-12 %** | **Matías (Maties) Pomar Oliver**, gerente de **Pastelerías Pomar** (4.ª generación, 1902), El Español/Cocinillas **21-nov-2025** | **ALTA** (declaración con nombre y empresa) |
| **PS-49** | **Coste de montar un obrador** | **«200.000, 300.000 y más» €** | Misma | **ALTA** |
| **PS-50** | **Coste de abrir una tienda** | **100.000 €** («y es abrir una tienda, no estamos hablando de hacer un punto de fabricación») | Misma | **ALTA** |
| **PS-51** | Margen del turrón | **~40 %** | Misma | ALTA |
| **PS-52** | Punto de equilibrio por producto | «vender **8 unidades** para empatar; la **novena** empieza a ganar» | Misma | ALTA (ilustrativo, **no extrapolable**) |
| **PS-53** | Estructura de cobro | **95 %** venta directa · **5 %** a crédito a 30-60 días | Misma | ALTA |
| **PS-54** | Plantilla | **47 personas**, 10 de ellas familiares | Misma | ALTA |
| **PS-55/56** | **Regla de margen (UNA sola, dos lecturas)** | margen bruto **65-70 %** ⇔ food cost **<30-35 %** | Tamara Viñas, 12-jul-2026 | MEDIA-ALTA |
| **PS-57** | Beneficio neto de un obrador unipersonal bien tarificado | **1.200-2.500 €/mes** | Misma | MEDIA |
| **PS-58** | Ejemplo de break-even | fijos de **5.000 €/mes** ⇒ facturación **~7.200 €/mes** | Misma | MEDIA |
| **PS-59** | Packaging sobre el coste del producto | **5-15 %** | Pleko (resumen de búsqueda) | BAJA-MEDIA |
| **PS-60** | Escenarios de break-even | pequeña **5.000 → 7.000 €** · mediana **8.000 → 10.000 €** · grande **12.000 → 15.000 €** | plandenegocio.es, 13-abr-2026 | MEDIA (⚠️ **el artículo no cita fuente primaria**: escenario editable, nunca benchmark) |
| **PS-61** | Desglose de fijos mensuales | alquiler **1.200-3.000** · suministros **600-1.200** · personal 2-5 empleados **2.000-6.000** · seguros y gestoría **300-700** · marketing **200-500** · reposición **1.000-2.000** → **5.000-12.000 €/mes** | Misma | MEDIA |
| **PS-62** | ROI declarado | **18-36 meses** | Misma | MEDIA |
| **PS-63** | Ticket medio de **restauración** en España | **~21 €** (2024); Baleares 35 €, Álava 16,5 € | CaixaBank Research vía Campus CaixaBankLab | MEDIA-ALTA — ⚠️ **es restauración, NO pastelería** |
| **PS-64** | **Ticket medio de PASTELERÍA** | **«sin fuente» — no existe dato público localizable** | — | — |

> ⚠️ **La trampa de redacción más peligrosa del bloque:** PS-55 y PS-56 **no son dos reglas, son la misma restricción expresada dos veces** (65 % de margen ⇔ 35 % de food cost). Si el guion las presenta como reglas distintas, el xlsx pedirá dos parámetros que se contradicen entre sí. **El libro 4 calcula una desde la otra y nunca pide las dos.**

### 3.2 El tamaño del mercado y el competidor real

| id | Dato | Valor | Fuente | Fiabilidad |
|---|---|---|---|---|
| **PS-26c/d/f/i** 🔴 | **La bollería y pastelería CONGELADA es el competidor real del obrador** | Producción 2025 **233.856 t** (+0,17 %); facturación del sector **2.001,63 M€** (+3,20 %, primera vez por encima de 2.000 M€); facturación de bollería y pastelería **+4,43 %**; **producción de pastelería +31,10 % entre 2018 y 2025** | **ASEMAC**, nota propia, **28-abr-2026** | **ALTA** (patronal, fuente primaria) |
| **PS-33** | Sólo **~1 de cada 20 euros** de bollería y pastelería pasa por el comercio especializado (~**5,4 %**, frente al **74 %** del supermercado, datos 2023) | — | Statista (muro de pago, leído en resumen) | **BAJA-MEDIA** |
| **PS-28** | Consumo en hogares 2025 de bollería y pastelería | **274,2 millones de kg** · **1.917,6 M€** · **5,85 kg/persona/año** (+5,3 % volumen, +5,6 % valor) | Panel de Consumo del **MAPA 2025** vía El Independiente 17-ago-2026 y Sweetpress 30-jul-2026 (⚠️ **el PDF oficial de 28,7 MB no se abrió por la restricción térmica**) | ALTA-MEDIA |
| **PS-29** | Brecha por renta | renta **baja 8,26 kg** vs renta **alta 4,39 kg** — casi el doble | Misma | ALTA-MEDIA |
| **PS-31** | Chocolates, cacaos y derivados 2025 | **2,84 kg/persona** · **33,88 €/persona** · **11,93 €/kg** (volumen −6,5 %, valor +10,4 %) | Sweetpress, 30-jul-2026 | ALTA-MEDIA |
| **PS-12** | Empresas del grupo CNAE **107** | **11.778** a **1-ene-2020** (serie 2013-2020 completa) | INE, DIRCE, tabla **298**, CSV descargado | **ALTA** pero **CADUCA**: la tabla es histórica y se detiene en 2020 |

> 🔴 **No existe un dato oficial de «cuántas pastelerías hay en España».** El CNAE mezcla panadería y pastelería en **1071** (fabricación) y en **4724** (minorista). **Toda cifra redonda que circule es una estimación de tercero**, y la guía debe decirlo en vez de repetirla (§15.1, N-1 y N-13).
>
> **Y la tesis de negocio sale sola de PS-33 + PS-26i:** el obrador **no compite en volumen con el supermercado y no debe intentarlo**. Compite en fresco, encargo y temporada.

### 3.3 Estacionalidad: la única palanca de caja con cifras — y el hallazgo que justifica un xlsx entero

| id | Dato | Valor | Fuente |
|---|---|---|---|
| **PS-41** 🔴 | **El pico de temporada multiplica la producción por 5-10×, no por 1,5×** | Pomar: ensaimadas de **25-30/día → 150-200/día**; individuales **50-60 → 500-600**; **7.000-8.000 barras de turrón** en Navidad | El Español, 21-nov-2025 |
| **L5-D9** 🔴 | Confirmación independiente con **el mismo equipo** | Paloma Silvestrin (Doble Uve, Madrid): «Somos un equipo pequeño, de cinco panaderos. El año pasado con este personal hacíamos **100 roscones** y este año estamos haciendo **casi 400 por día**» | Infobae, **04-ene-2026** |
| **PS-35** | Roscón de Reyes, campaña 2025/26 | **~30 millones de unidades** en España | Estimación de **ASEMAC** vía Infobae/EFE, 2-ene-2026 |
| **PS-36/37** | Madrid | **>2,9 millones** de roscones; **57 %** elige relleno (nata o trufa) | **Asempas** vía Libertad Digital, 2-ene-2026 |
| **PS-38** | Referencias de escala | El Corte Inglés **850.000** roscones · Viena Capellanes **72.000** | Infobae/EFE, 2-ene-2026 |
| **PS-43** | **Un solo producto puede ser el 30 % de la caja** | Hofmann: croissant de mascarpone, **~3.000 uds/semana ≈ 30 % de la facturación** de la pastelería; pastel de pistacho hasta **1.800 uds/mes** | The New Barcelona Post, 12-feb-2026 |
| **PS-46** | El supermercado entra en el pico | roscones de supermercado premiados a **9 €** | La Ciutat / Directo al Paladar, 2026 |

**Lo que enseña este bloque y que ninguna fuente de la SERP explica: el cuello de botella de una pastelería no es la demanda, es la capacidad de obrador y el plan de producción.** Eso condiciona el dimensionado del horno, del abatidor y de la plantilla eventual, y es **el riesgo nº 1 del formato**.

### 3.4 Las dos materias primas que hay que MODELAR, no fijar

**PS-66 — Mantequilla.** Cotización UE (Milk Market Observatory de la Comisión Europea, vía prensa especializada): **386 €/100 kg** en la 4.ª semana de junio 2026 (−2,8 % en 4 semanas) y **405 €/100 kg** en la 2.ª semana de junio (+2,3 %). Antes de 2026 llegó a **duplicarse de ~4.000 a ~8.000 €/t**. Leche en España **52,23 €/100 kg** en feb-2026 (+10,5 % interanual). ⚠️ **Es cotización de COMMODITY A GRANEL, no el precio de la mantequilla de hoja 82-84 % que compra un obrador** — que es sensiblemente superior. **No mezclar las dos en la misma tabla.**

**PS-67 — Cacao: contradicción NO resuelta.** Cuatro cifras distintas para 2026 según mes y mercado: **3.300** (ICCO abr-2026), **4.000** (futuros Londres/NY), **5.000** (ICCO ene-2026) y **6.205 USD/t** (cierre de agosto, leído sólo en resumen). **Ninguna cifra puntual de cacao entra en la guía.** Lo que sí entra es el **patrón, triplemente confirmado**: máximos históricos en 2024-2025, caída fuerte en 2026, y **el precio minorista no baja al ritmo del commodity** (Infobae 15-mar-2026: cacao **−54 %** y azúcar **−21 %** en 12 meses, «pero las torrijas y los huevos de Pascua cuestan más»). **La guía enseña a modelar volatilidad —celda de precio de cobertura + análisis de sensibilidad—, no a fijar un precio.**

### 3.5 El traspaso: el hallazgo más diferencial del research, y no lo cubre nadie

**PS-69 — Milanuncios, traspasos de obrador/pastelería en Barcelona** (consultado 2026-09-10):

| Negocio | m² | Traspaso | Renta/mes |
|---|---|---|---|
| Pastelería-repostería, Gràcia | 85 | **43.000 €** | **1.250 €** |
| Pastelería take away, Poblenou | 69 | **80.000 €** | **850 €** |
| Obrador Sant Antoni (sin venta al público) | 80 | **25.000 €** | **1.050 €** |
| Panadería-pastelería, Pg. Maragall | 63 | **18.000 €** | **1.300 €** |
| Pastelería artesanal, Sant Andreu | 63 | **19.000 €** | **1.300 €** |

**PS-70 — negociosenventa.es, España** (consultado 2026-09-09/10): Sevilla **6.000 €** · Valencia (despacho de pan) **15.500 €** · Valencia (Benimaclet) **18.000 €** · Madrid (obrador pequeño) **20.000 €** · Madrid (sin obrador, 25+ años) **19.500 €** · Almería (repostería creativa) **25.000 €** · Barcelona **50.000 €** · Barcelona por jubilación **75.000 €** · Gran Canaria **65.000 €** · Lleida (pastelería-cafetería, 36+ años) **100.000 €**.

> **Tres lecturas que valen un capítulo y una hoja de xlsx:**
> 1. **Traspasar sale entre 3 y 10 veces más barato que montar de cero.** Frente a los 100.000-250.000 € de obra nueva, la mediana de estos traspasos ronda **25.000-50.000 €** con maquinaria y licencia incluidas.
> 2. **La renta mata el negocio, no el traspaso.** Un traspaso de **18.000 € con 1.300 €/mes** es peor negocio que uno de **80.000 € con 850 €/mes**: en cuatro años la diferencia de renta se come el ahorro. **Ese cálculo debe ser una hoja.**
> 3. **«Por jubilación» es la etiqueta más repetida** — coherente con la falta de relevo generacional del oficio.
>
> ⚠️ **Son precios PEDIDOS, no pagados.** Debe decirse en la propia tabla del producto.

---

## 4. Bloques obligatorios 3 y 4 — Equipamiento crítico con marcas y precios, y proveedores reales

### 4.1 Hornos: 20 modelos con precio visible en un distribuidor español

**PS-72.** La Hostelera, categoría «Hornos profesionales para panadería, repostería y pastelería» (consultado **2026-09-10**; **precios CON IVA** según la propia página). Extremos y referencias del rango: **UNOX Roberta XF003** (3 bandejas) **605,61 €** · **UNOX Anna XF023** 698,78 € · **ROMAGSA Maxiplus** 703,01 € · **FM Industrial RXL 304** 719,29 € · **SMEG ALFA43X** 791,95 € · **UNOX Domenica XF043** 1.229,84 € · **INFRICO HE604Plus** 1.593,21 € · **SMEG ALFA420E1HDS** 2.513,41 € · **Nerone NEMID-5** 2.922,15 € · **EKA KF 1001 G (gas)** 3.210,13 € · **UNOX XB693 Bakerlux** (6 bandejas) 3.354,12 € · **SMEG ALFA1035HR-2** (10) 3.896,20 € · **UNOX XB893** (10) 4.844,84 € · **UNOX XEBC-06EU-E1RM** 5.450,45 € · **UNOX XB813G (gas, 10)** 6.288,98 € · **UNOX XEBC-06EU-EPRM** 7.453,60 € · **UNOX XEBC-10EU-GPRM (gas, 10)** **11.275,71 €**. Fiabilidad **ALTA**.

**PS-73 — Hornos de pisos (deck) y rotativos.** **Salva Industrial** fabrica hornos de pisos eléctricos modulares de **1 a 5 módulos**, 1 o 2 puertas, cámaras de **200 o 300 mm**, para 2, 3, 4 o 6 bandejas de 60×40 o 76×46 cm, con variación **<±5 ºC**. **Precio «sin fuente»** — vende por distribuidor y presupuesto. Otras marcas de referencia del segmento: **Bongard, Wiesheu, Miwe, Sveba Dahlen**.

**PS-74.** Referencia declarada por un profesional en activo: «un horno profesional puede costar **más de 20.000 o 30.000 euros**», igual que un congelador profesional — Matías Pomar, 21-nov-2025.

### 4.2 Frío, laminación, atemperado y vitrinas

| id | Equipo | Marca / modelo | Precio | IVA | Fuente |
|---|---|---|---|---|---|
| **PS-76** | **Vitrina expositora pastelera refrigerada curva** | **Docriluc VEPD-9-15-C** (1505×900×1305 mm, 452 L, 0,93 m² de exposición, R-290) | **2.284,10 €** (PVP tachado 3.263 €, −30 %) | **SIN IVA** | Gavinox, 2026-09-10 |
| **PS-77** | Accesorio: puertas correderas traseras | Docriluc | 120,40 € | sin IVA | Misma |
| **PS-78** | **Abatidor de temperatura** | **Irinox**, 4 bandejas (gama Multifresh, de +85 ºC a −40 ºC) | **desde 10.037 €** | + IVA | EquipoH (resumen) — MEDIA |
| **PS-79** | **Laminadora automática** | **Sammic DF-40** (hasta 40 cm) | **1.215,00 €** sin IVA / 1.470,15 € con IVA | ambos | Alimaq (resumen) — MEDIA |
| **PS-80** | Laminadora profesional de obrador | **RONDO** (Rondostar 5000); **Sermont** es distribuidor oficial en España | **«sin fuente (precio)»** | — | rondo-online.com |
| **PS-81** | **Batidora planetaria 20 L** | **Sammic BP-20** (900 W, 95-392 rpm) | **desde 595,04 €** | no declarado | HostelShopping — MEDIA |
| **PS-82** | **Atemperadora de chocolate** | **Selmi One 12 kg** | **7.400,00 €** | + IVA | Chocosolutions (resumen) — MEDIA |
| **PS-83** | Cámara de fermentación controlada / roll-in | — | rango de categoría **hasta 19.438 €+** | con IVA | La Hostelera — MEDIA |
| **PS-84** | Conducto de extracción de acero inoxidable | — | **puede superar los 6.000 €** | no declarado | Salva — MEDIA |

**Marcas de referencia SIN precio publicado localizable** (todas «sin fuente (precio)», mencionables sin cifra): hornos **Wiesheu, Miwe, Sveba Dahlen** · batidoras **Bear Varimixer, Sinmag** · laminadoras **Fritsch** · abatidores **Coldline, Infrico** · armarios y cámaras **Infrico, Salva** · vitrinas **Tecnodom, Bakermac** · atemperadoras **Chocovision, ICB**.

### 4.3 Obra, instalaciones y la validación cruzada que da credibilidad al producto

| id | Concepto | Cifra | Fuente |
|---|---|---|---|
| **PS-85a/b/c** | Obra civil sobre local de referencia de **90 m²** | **54.000 / 81.000 / 108.000 €** = **600 / 900 / 1.200 €/m²** | La Hostelera |
| **PS-85d** | Equipamiento, tres niveles | **15.000 / 29.000 / 46.000 €** | Misma |
| **PS-85e/f/g** | Proyecto técnico **5.000 €** · asesoramiento **1.000 €** · marketing **5.000 €** | — | Misma |
| **PS-85h** | **Total del escenario recomendado por la fuente** | **137.000 €** | Misma |
| **PS-86a** | **Potencia eléctrica SOLO para los hornos** | **20-80 kW** | Estudio LBA, act. abr-2026 |
| **PS-86c/d/e** | Salida de humos **hasta cubierta, 1 m por encima de la cumbrera**; **7 zonas obligatorias** (venta, obrador, almacén de materia prima, cámara, almacén de producto terminado, vestuarios/aseos de personal, almacén de residuos) con **principio de MARCHA ADELANTE**; superficies lisas, lavables e impermeables, **encuentros pared-suelo redondeados**, lavamanos no manual por zona | — | Misma |
| **P36** | El papeleo por separado | licencia de obrador/panadería en Madrid **desde 1.690 € + IVA**; proyecto técnico de obrador completo **1.800-2.800 € + IVA**; presupuesto publicado de obrador+despacho de 80 m²: **97.000-184.000 €** | estudio-l.es, 2026-09-10 |

> 🟢 **La validación cruzada más fuerte del research (PS-85 / §4.4 de L4):** la dotación tipo montada con **precios reales verificados** suma **≈29.683 €** de maquinaria, y coincide casi exactamente con el nivel «equipamiento medio **29.000 €**» que La Hostelera publica de forma **independiente**. Con obra media (81.000 €) y proyecto (5.000 €) el total ronda **116.000 €**, dentro del rango de PS-05 (100.000-150.000 €) y por debajo de los 137.000 € del escenario de equipamiento alto. **Dos fuentes independientes cuadrando es el mejor argumento de credibilidad que tiene este producto.**
>
> ⚠️ **Y la trampa que va con ello:** los precios **mezclan CON y SIN IVA según distribuidor** (La Hostelera con IVA; Gavinox, Irinox, Selmi y Sammic sin IVA) y algunos llevan descuento de campaña que caduca (la vitrina Docriluc va con −30 %). **Cada línea del xlsx necesita columna «¿lleva IVA?» o el CAPEX saldrá un 21 % desviado.**
>
> **Lo que falta para cerrar el CAPEX** (fermentación, frío de conservación, mobiliario, TPV, packaging, fianza, fondo de maniobra) **no tiene precio verificado** y va al xlsx como **líneas en blanco con celda verde**. Nunca rellenadas a ojo.

### 4.4 Proveedores reales: 9 verificados con URL, 22 descartados

| id | Categoría | Proveedor | Qué vende | Verificación |
|---|---|---|---|---|
| **PS-87** | Ingredientes premium / técnicos | **Sosa Ingredients** (Cataluña, 1967, +80 países) | Ingredientes para pastelería y gastronomía moderna | **ALTA** |
| **PS-88** | Panadería / pastelería / chocolate | **Puratos** | Masas madre, mejorantes, mixes, rellenos, chocolate | **ALTA** |
| **PS-89** | Chocolate y coberturas | **Barry Callebaut** (marcas **Callebaut**, **Cacao Barry**, **Chocovic**) | Coberturas y servicio técnico | MEDIA-ALTA (⚠️ verificar la web ES antes de publicar) |
| **PS-90** | Chocolate premium | **Valrhona** | Coberturas y formación; distribuye Sosa como marca socia | **ALTA** |
| **PS-91** | Mantequilla y nata profesional | **Debic** (FrieslandCampina) | Mantequillas de punto de fusión fijo para hojaldre y bollería | **ALTA** |
| **PS-92** | Mantequilla profesional | **Elle & Vire Professionnel** | Mantequilla seca **84 % MG** de laminado | **ALTA** |
| **PS-93** | Harinas | **Ylla 1878** | Harinas profesionales de pastelería, bollería, churrería | **ALTA** |
| **PS-94** | Harinas | **Farinera Coromina** (Girona, 1897) | Harinas especiales, a la piedra, ecológicas, «a la carta» | MEDIA-ALTA (⚠️ verificar dominio propio) |
| **PS-95** | Distribución | **Cospan** | Materias primas de panadería y pastelería | MEDIA |

**Los 22 proveedores que citaba el encargo y NO se pudieron verificar → «sin fuente», no publicar:** Harinas Polo, Molí de Picó, Harinera Vilafranquina, Dawn Foods, Zeelandia, Bakels, Ravifruit, Boiron, Ovopack, Pascual Ovoproductos, García de Pou, Selfpackaging, Sanilus, Cadibe, Silikomart, Matfer, De Buyer, Martellato, Pavoni, Chocolates Torras, Makro (existe como distribuidor HORECA, pero **no se verificó su catálogo de pastelería**).

> **Marca hermana:** **Hosply.pro** («Directorio de Proveedores HORECA», del grupo ChefBusiness) apareció de forma natural en la búsqueda de proveedores. Es una oportunidad de enlace interno legítima desde el capítulo 11 — **decisión de John** (D11).

---

## 5. Bloque obligatorio 6 — Casos de éxito reales, con cifras públicas

| id | Marca | Modelo | Datos públicos con fuente | Lección para la guía |
|---|---|---|---|---|
| **PS-97** 🔴 | **Pastelerías Pomar** (Mallorca) | Obrador familiar + tiendas, 4.ª generación (1902) | **47 empleados** (10 familiares) · rentabilidad **8-12 %** · obrador **200.000-300.000 €+** · tienda **100.000 €** · **95/5** venta directa/crédito · margen del turrón **~40 %** · picos ×5-10 | **El caso más útil de todo el research**: un profesional en activo dando la rentabilidad y la inversión reales. ALTA |
| **PS-96** | **Hofmann** (Barcelona, 1983) | Escuela + pastelería de autor + obrador central | **>150 profesionales**; nuevo centro de I+D y producción en **Badalona: 1.200 m², >700.000 €** de inversión, operativo desde enero de 2026, **duplica capacidad** y prevé **+40 %** de producción en 2026; **>200.000 alumnos** formados; 2 tiendas + expansión a Dubái; turnos de **5:00 a 18:00 de lunes a domingo** | **Un solo producto puede ser el 30 % de la caja** (PS-43), y el obrador centralizado es lo que permite escalar sin multiplicar tiendas. ALTA |
| **PS-98** | **Cientotreinta grados** (Madrid) | Obrador de barrio + café de especialidad + B2B | Hermanos **Alberto y Guido Miragoli**; abrió en Chamberí en **2017**, mejor pan de Madrid en 2020, obrador nuevo en Prosperidad en oct-2023. **320 m²** entre dos locales, **~600 kg/día** con capacidad para **1.200 kg**. **~70 %** particulares / **~30 %** restauración | El obrador de barrio moderno **crece por producción, no por m² de tienda**. MEDIA-ALTA |
| **PS-99** | **Manolo Bakes** (Madrid) | Cadena propia — **abandonó la franquicia** | **33,5 M€** en 2024 (+40 %) y 1 M€ de beneficio neto; **>50 locales**, objetivo 100; **>25 millones de «manolitos»/año**; compró los derechos de «Los Manolitos» por **2,5 M€** (jul-2025) | Un producto icónico monoproducto puede sostener una cadena entera — **y la franquicia no siempre es el final del camino: recompró sus franquicias**. MEDIA-ALTA |
| **PS-100** | **Levaduramadre** (Comess Group) | Franquicia panadería-cafetería con obrador propio | **49,3 M€** en 2025 (+16 %), **31 aperturas**, cierre en **167 tiendas**; objetivo 2026: 60 M€ y 60 tiendas. Inversión **99.000 €** canon incluido; **no requiere salida de humos** | **«Sin salida de humos» es una ventaja de negocio, no un detalle técnico**: amplía los locales candidatos y baja el alquiler. MEDIA-ALTA |
| **PS-101** | **Granier** (Consupan SL, 2010) | Franquicia panadería-cafetería | **318 establecimientos** en ficha oficial. Inversión **desde 180.000 €**, canon **8.000 €**, royalty **500 €/mes**, sin canon de publicidad, contrato 10 años, local **mínimo 100 m²**. Modelo **autoempleo desde 10.000 €** con cesión de 1.000 €/mes y royalty del 2 % | **Dos modelos de entrada con un orden de magnitud de diferencia en la misma enseña.** MEDIA-ALTA |
| **PS-102** | **Viena Capellanes** (Madrid) | Pastelería + catering + corners de empresa | **276 empleados** y facturación +12,33 % interanual; **22 establecimientos** + tienda online + **>70 «Viena Corner»** en empresas; **72.000 roscones** en 2025/26 | **El canal B2B (corners, catering) desestacionaliza la caja.** MEDIA |

**Casos de oficio mencionables SIN ninguna cifra** (no se pudieron documentar): Escribà · Bubó · Oriol Balaguer · La Pastisseria · Moulin Chocolat · Pastelería Mallorca · La Duquesita · Totel (Paco Torreblanca) · Nunos · Cristina Torrent · Santagloria.

> 🚨 **Dos refutaciones al propio encargo, verificadas:**
> - «**Cientotreinta grados**, franquicia de Oriol Balaguer, 250 k€ + 30 k€ de canon» es **FALSO**: la marca es de los hermanos Miragoli y no consta como franquicia (Guía Repsol, 25-ene-2024). Lista negra N-3.
> - «**Manolo Bakes** entre los casos de franquicia»: **recompró sus franquicias y ya no franquicia en España**. El «~300.000 € de inversión» que circula vende una franquicia que no existe. Lista negra N-4.

---

## 6. Voz del cliente: dolores, personas, objeciones y vocabulario

### 6.1 Aviso de honestidad que hay que leer antes que la tabla

**Reddit, YouTube, Facebook, Forocoches, Burbuja, Mediavida, fororeposteria.com y dianaverdu.com quedaron inaccesibles** (dominio bloqueado para el user-agent, comentarios por JavaScript, o 403). **Ninguna cita de este research viene de ahí.** El corpus leíble (~25 fuentes) está **sesgado hacia foros de arquitectura e ingeniería** (Sólo Arquitectura, Habitissimo) y hacia prensa. Eso **infla** el peso de «licencias y humos» y **desinfla** los dolores emocionales. El orden por frecuencia es frecuencia **dentro del corpus**, no una medición de mercado.

### 6.2 Los 10 dolores con evidencia, y dónde los resuelve el producto

| # | Dolor | Evidencia literal (la mejor de cada bloque) | Dónde lo resuelve |
|---|---|---|---|
| **1** | **«¿Qué licencia necesito, y me la darán en ESTE local?»** (10/25 fuentes) | Estefania (Sabadell): «Quiero montar una pasteleria en sabadell y **necesito un presupuesto sobre la gestion de las licencias preceptivas**». Y la respuesta del técnico: «no en todos los locales se puede hacer lo que uno desea» | Libro 1 (`Ficha de Visita a Local`) + libro 7 (trámites) + cap. 6 |
| **2** | **La salida de humos: el requisito que tumba proyectos** (7/25) | loverpets (30-01-2019): «El ingeniero del ayuntamiento me ha dicho que para la salida de humos no se indica diámetro mínimo, pero **sigo teniendo mis dudas**» | Ficha de «prueba de humos» en el libro 1 + partida específica de conducto + comunidad + refuerzo en el libro 2 |
| **3** | **«¿Cuánto cuesta de verdad?» y la horquilla imposible** (7/25) | La misma gestión de licencias presupuestada entre **350 €** (VERITAS, local ≤100 m²) y **18.000 €** (David Velasco, Grupo VMA), con un tercer técnico avisando: «**desconfíe de presupuestos ridículos**» | Libro 2 (CAPEX por escenarios y por variante) + cap. 4 |
| **4** | **«¿Puedo hacerlo en la cocina de mi casa?»** (6/25) — **el de más búsqueda** | Anónimo (2011): «¿podemos hacer esto o alguno de nosotros necesita un titulo de pastelero? El tiene un carnet de manipulador, ¿con eso valdría? **Pueden demandarnos y si lo hacen, ¿qué consecuencias tendría?**» | Cap. 9 + hoja «Ruta doméstica» del libro 7 con la **lista blanca del art. 13.8** y el contador de 100 kg/semana |
| **5** | **Precios: «me da miedo subir y creo que estoy regalando el trabajo»** (6/25) | Marta (Escuela de Obradores): «con la mitad vivo y estoy cobrando lo mismo, **haciendo las 2 subidas de precios**». Anita: «Hacía tartas de fondant que me llevaban horas **y jamás cobré**» · «**Las cookies tienen un 35 % de margen. Las tartas, la mitad**» | Libro 4 (escandallo por tanda **con coste de mano de obra**) + cap. 12 |
| **6** | **Facturar mucho y no ganar** (5/25) | Noelia Tomé: «El último año que estuvimos aquí facturamos 500.000 euros. **Pero al final, de beneficio quedaban 15.000 o 20.000 euros**». Anita: «En más de 11 años hemos cometido muchos errores. **El mayor fue no tener los números como prioridad**» | Libro 5 (P&L + punto muerto + tesorería) **con el sueldo del propietario como renglón propio** + cap. 18 |
| **7** | **Personal: no se encuentra y cuesta más de lo que pensabas** (5/25) | Matías Pomar: «el mayor problema que hay es que **es complicado encontrar personal que quiera trabajar en este oficio**» · «es un trabajo de fines de semana, de festivos y de **levantarse pronto cuando los demás disfrutan**» | Libro 10 (turnos + coste con SS) + caps. 13 y 14 |
| **8** | **El madrugón y la vida que se te va** (4/25) | Noelia Tomé: «Nosotros llegamos a ser 15 trabajadores y **a mí se me hizo mundo**» · «**Desarrollé muchísima ansiedad**, cosa que nunca había tenido en mi vida» · «Ahora que estoy sola gano más dinero que cuando éramos 15» | Cap. 14 + el plan de producción del kit citado como **herramienta de horario del dueño**. **Vender «vas a trabajar menos horas» es más honesto y más fuerte que «vas a facturar más»** |
| **9** | **Estacionalidad y encargos: el año se juega en cuatro picos** (4/25) | Paloma Silvestrin: «Somos un equipo pequeño, de cinco panaderos… hacíamos 100 roscones y este año estamos haciendo **casi 400 por día**». Anita: «Hemos llegado a hacer **17.000 euros solo vendiendo cookies**» en un mes punta | **Libro 3** (capacidad vs demanda del pico, refuerzo y tesorería) + cap. 15 |
| **10** | **«Y luego, ¿quién me compra?»: industria y traspasos** (4/25) | Matías Pomar: «para competir con las grandes industrias **estás perdido**»; y su consejo, es más fácil adquirir un traspaso de un negocio que cierra | Hoja `Traspaso vs Obra Nueva` del libro 2 + cap. 6. **No lo cubre ninguna guía de la competencia** |

**Dolores que el corpus NO sostiene (honestidad):** **mermas de vitrina** (cero citas de un pastelero español quejándose; el kit ya lo cubre, pero **no se puede vender como «lo que más te duele»**) · **maquinaria de segunda mano** (sólo oferta comercial, ninguna voz de comprador) · **formación técnica vs gestión** (sostenido sólo por material comercial de escuelas: quien lo dice, vende formación).

### 6.3 Las cinco buyer personas

| Persona | Perfil y capital | Miedo principal | Frase literal | Qué compra |
|---|---|---|---|---|
| **A — «La repostera de casa que quiere legalizarse»** *(el segmento con más búsqueda)* | Mujer, 28-45. Vende por encargo desde su cocina, con clientela por WhatsApp/Instagram. Capital **[inferencia]** 3.000-10.000 € | Que lo que ya hace sea ilegal y le caiga una sanción | «**Pueden demandarnos y si lo hacen, ¿qué consecuencias tendría?**» | La ruta legal paso a paso y el escandallo que le diga cuánto cobrar |
| **B — «La que ya vende y no se atreve a dar el salto al local»** | 30-50, con oficio, demanda validada, sin experiencia de gestión. Capital **[inferencia]** 8.000-25.000 € | Firmar un alquiler y una maquinaria que luego no pueda pagar | «Tengo experiencia y cursos… **Pero no me atrevo a lanzarme a ponerme en un local, comprar maquinaria, etc.**» | **Es el comprador natural de una guía de 65 €**: CAPEX por escenarios + punto muerto + checklist de local |
| **C — «El/la que cambia de vida»** | 25-40, empleo que no le gusta, sin oficio o con formación reciente. Capital **[inferencia]** 5.000-20.000 € | No saber por dónde se empieza | «Tengo **27 años**… mi intención es **montar mi propia pastelería**» (Edurne, Rankia 2017) | El orden de decisión completo, y ayudas/subvenciones como interés secundario real |
| **D — «El promotor con local, a por el proyecto y la licencia»** | 35-55, ya tiene local o traspaso a la vista; su problema es administrativo y técnico | Que el ayuntamiento le pare la apertura o que la salida de humos sea imposible | «Estoy buscando un local para abrir un obrador de Pasteleria en Madrid capital. **Solo seria obrar**…» | El cribado de local y el mapa de trámites. **Es quien más rápido ve que 65 € son baratos frente a 350-18.000 € de honorarios** |
| **E — «El/la profesional que ya factura y se le ha ido de las manos»** | 30-50, ya abierto. Facturaciones reales de 30.000-90.000 €/mes | Trabajar 12 horas para que no quede beneficio | «facturamos 500.000 euros. **Pero al final, de beneficio quedaban 15.000 o 20.000**» | ⚠️ **NO es de esta guía**: es de Food Cost / Manual del Manager / kits. **La ficha debe decir explícitamente «para quien AÚN no ha abierto»** |

> **[Inferencia] Personas del brief que el corpus NO respalda:** «emprendedor sin oficio que contrata pastelero» y «heredero de negocio familiar» no aparecieron ni una vez. El relevo familiar aparece **por su ausencia**: «Hay una falta de relevo generacional en las familias» (Pomar). **No incluirlas en el copy sin más evidencia.**

### 6.4 Las ocho objeciones, con la respuesta honesta

1. **«Esto está gratis en Google».** Sí, la información suelta está. **Lo que no está es el orden de decisión ni los números en un Excel que puedas rellenar con TU local.** Y está demostrado: los blogs de la SERP dan horquillas de 15.000 a 200.000 € **sin decir de qué dependen**. No prometer «información exclusiva»: prometer **estructura, plantillas y criterio**.
2. **«65 € por un PDF me parece caro».** El mismo comprador va a pagar **350-18.000 €** sólo por la gestión de licencias y **700-800 €** por un plan APPCC externo. **El anclaje correcto no es «otro ebook», es una hora de asesoría.** Y hay que decir sin adornos qué NO sustituye: **no sustituye al proyecto técnico visado**.
3. **«¿Me sirve si voy a empezar en casa?»** Sí **si** el producto trae la ruta doméstica completa. Si sólo hablara de local con obrador, **hay que decirlo en la ficha**: es el segmento con más búsqueda y el que peor se lleva una decepción.
4. **«Mi ayuntamiento es distinto / yo estoy en Canarias».** Verdad, y es lo primero que dicen todos los técnicos citados. La guía **no puede dar la ordenanza de 8.131 municipios**; da **el mapa de qué preguntar, a quién y en qué orden**, más los umbrales estatales y autonómicos verificados. Prometer otra cosa es mentir. *(Sin respuesta perfecta — decisión D9.)*
5. **«No tengo oficio de pastelero, esto no es para mí».** La guía es de **negocio**, no de recetas, y hay que decirlo en la ficha. Contrapunto real: Anita empezó «con 10.000 euros ahorrados» y un horno doméstico. Pero también el aviso de Pomar: sin oficio, o lo contratas o lo aprendes.
6. **«¿Y esto quién lo firma?»** Se responde **mostrando el índice y una muestra**, no exhibiendo credenciales. (Regla de la casa: sin ratings ni testimonios inventados en producto nuevo.)
7. **«Prefiero un curso con acompañamiento».** Existen y son **el competidor real** para la persona A (Escuela de Obradores: «más de 1.000 mujeres reposteras», «más de 100 descargables», «en 3 meses tu obrador en marcha»). **La guía no compite en acompañamiento: compite en precio, en inmediatez y en que te llevas los Excel para siempre.** Decirlo así vende más que fingir que es lo mismo.
8. **«¿Sirve si estoy en México/Colombia/EE. UU.?»** El marco normativo es español; **la estructura económica (CAPEX, escandallo, punto muerto, plan de producción) es universal y el marco sanitario hay que adaptarlo**. La FAQ ofrece la adaptación **como servicio**.

### 6.5 Vocabulario: cómo lo dicen ellos, y las equivalencias LATAM

**Lo que escriben ellos** (todo tomado de citas reales, no inventado): «**montar**» una pastelería (no «abrir») · «**obrar**» / «solo seria obrar» · «obrador **a puerta cerrada**» · «**la salida de humos**» (nadie dice «evacuación de gases») · «papeleos», «burocracias», «los sanitarios» · «las **licencias preceptivas**» · «**me da miedo subir los precios**» · «**no me atrevo a lanzarme**» · «tartas **por encargo**» · «**ración**» como unidad de precio de la tarta · «**por no poder atender**» (fórmula estándar de los traspasos) · «**el ingeniero del ayuntamiento**» · «**bakery**» · y la joya de Noelia Tomé: «**a mí se me hizo mundo**».

**Equivalencias para la PRIMERA mención** (español de España como base; luego el término de España):

| Concepto | España | LATAM (primera mención) | Nota verificada |
|---|---|---|---|
| El oficio y la tienda | **pastelería** | **repostería** | `pasteleria` gana en los 7 mercados; `reposteria` es fuerte en MX (22.200) y AR (9.900) |
| El espacio de producción | **obrador** | **taller** · **laboratorio** (AR/UY/CL) · **planta de producción** | **DLE**: «*Taller artesanal, especialmente el de confitería y repostería*» (https://dle.rae.es/obrador, consultado 2026-09-09). En España 9.900/mes; **fuera de España la palabra apenas se usa** (10/mes) |
| Coste unitario de receta | **escandallo** | **costeo** | `costeo de pasteles` **sin dato en ningún mercado**: el vocabulario LATAM sirve para que se entienda, **no** para captar tráfico |
| Mueble de exposición | **vitrina** · **mostrador** | **exhibidor** · **vitrina exhibidora** | ⚠️ **la preposición cambia por mercado**: `vitrina DE pasteleria` en España, `vitrina PARA pasteleria` en LATAM |
| Producto | **tarta** | **pastel** (MX) · **torta** (AR/CO/CL/PE/UY) | ⚠️ **Es la palabra más peligrosa del producto**: triple divergencia, y en México «torta» es un bocadillo |
| Pedido de cliente | **encargo** | **pedido** · **orden** (MX) | `tartas por encargo` 210/mes en España |
| Forma «artesanal» | **artesanal** (480) | artesanal | ⚠️ `artesana` sólo 260 (×0,54): **usar «artesanal» como forma principal** |
| Modelo sin local propio | **obrador compartido** (50) | **cocina compartida** · **cocina colaborativa** | SERP 100 % institucional (ACSA/Gencat, Diputació de Barcelona) |

> 🚨 **FALSO AMIGO, y es el que más engaña porque tiene volumen: «dulcería».** Vale **110.000/mes en México** y **14.800 en EE. UU. en español** (frente a 3.600 en España). **Pero en México una dulcería es la tienda de golosinas y el mostrador de dulces del cine, NO una pastelería.** El DLE la da como sinónimo de obrador en España, pero el uso mexicano manda en México. **No se usa como sinónimo en ninguna parte del producto.**

---

## 7. Bloque obligatorio 8 (parte 1) — La competencia de pago: el hueco, confirmado producto a producto

### 7.1 El censo: 38 productos de pago, 31 con precio confirmado en la página del vendedor

| Familia | Ítems con evidencia | Rango verificado | Lo que revela |
|---|---|---|---|
| **(a) Libros en español** | **8** | **13,47 € – 190,00 €** | **Sólo 1 de 8 trata de administrar el negocio**, y es de **2015** a **190 €** («Administración de establecimientos de producción y venta de productos de pastelería, MF1781_3», Elearning S.L., 502 págs.) |
| **(b) Guías y plantillas de pago único** | **6** (3 sin precio público) | **21 € – 147 €** | **Nadie vende una guía de APERTURA**: venden plan de negocio genérico (49 €, plandenegocio.es) o escandallo suelto |
| **(c) Cursos y programas** | **10** (3 sin precio) | **357 € – 19.200 €** | El mercado está **partido en dos**: infoproducto de 357-697 € o máster de 12.700-19.200 €. **En medio no hay nada** |
| **(d) Franquicias con cifras** | **11** | canon **8.000-50.000 €** · inversión **desde 25.000 hasta 200.000 €** | El **canon más barato del sector (Granier, 8.000 €) es 123 veces** una guía de 65 € |
| **(e) Consultoras / ingenierías** | **3** | **1.000 € – 2.800 € + IVA** | **El papeleo solo cuesta 1.690 € + IVA**; nadie regala el layout del obrador |
| **Fuentes gratuitas censadas** | **11** | — | Ver §7.3 |

### 7.2 Los cinco hallazgos que valen por todo el análisis

**H1 — El competidor real no es un libro ni un máster: es Tamara Viñas, y YA está en la SERP que nos interesa.** `pasteleriaparatodos.com` aparece en la SERP de «como montar una pasteleria» **con una guía gratuita del 12-jul-2026** y desde ella embudo a **«Monta o mejora tu pastelería» (697 €, o 3×232,33 €)** y **«Obrador en Casa» (357 €, o 3×119 €)**. Es **nuestro mismo movimiento —contenido que vende producto— hecho por alguien con cara, marca, Discord privado y garantía de 30 días**. Su temario de 12 módulos **solapa punto por punto**: legal, rentabilidad, plan de negocio, escandallo, precios, stock, alérgenos, calidad, APPCC, organización, fiscalidad. Y regala **10 plantillas** y un **Plan APPCC ya elaborado** — exactamente nuestra munición. Además, **`obrador-en-casa` ocupa la POSICIÓN 1 de «montar una pasteleria en casa»**, la 2.ª de «requisitos para montar un obrador en casa» y la 3.ª de «vender reposteria desde casa españa».

> 🔴 **Consecuencia comercial, sin adornos: no podemos vender «te explico cómo montar una pastelería».** Eso ya lo vende ella, con acompañamiento humano, por 697 €. **El ángulo que queda libre es el DOSSIER DE ENTREGABLES** (los xlsx que hacen los números y los documentos que pide la inspección), pago único, sin tutoría y sin suscripción.
>
> ⚠️ **Y esto contradice parcialmente al brief:** el brief daba por hecho que la venta entra por canales propios *porque el SEO es mínimo*. Se confirma el volumen bajo, **pero aparece un competidor que SÍ monetiza esa SERP diminuta con un embudo de 357-697 €**. **Volumen bajo no significa competidor ausente.**

**H2 — Hay un agujero de precio limpio entre 49 € y 357 €, y nadie lo ocupa.** El mercado verificado, ordenado: plantilla de escandallo suelta (~20-50 €) → **software de plan de negocio 49 €** → Pack técnico 147 € → **Obrador en Casa 357 €** → **Formación Negocio 697 €** → CEAC 2.040-2.360 € → Hofmann 7.000 € → BCH obrador 12.700 € → BCH pastelería 19.200 €. **Entre 49 € y 357 € sólo hay técnica y plantillas sueltas. Un producto documental de 65 € cae limpio y no compite con nadie de frente.**

**H3 — Lo gratis da cifras de CAPEX y se para justo antes del trabajo.** Verificado columna a columna en las 11 fuentes: **ninguna** cubre layout del obrador con **marcha adelante**, escandallo por lote con merma y rendimiento, **P&L y cash-flow mes a mes**, punto muerto sobre datos propios, **los 14 alérgenos UE aplicados a vitrina y venta a granel**, trazabilidad documental, convenio y coste real de personal, ni **el calendario estacional** donde la pastelería hace la caja del año. **Es un hueco unánime, no la laguna de una web concreta.**

**H4 — Las cifras gratuitas no coinciden entre sí y ninguna dice de dónde sale.** Para el mismo negocio, en el mismo país, en 12 meses: **41.400-101.200 €** (modelosdeplandenegocios, 14-ago-2025) · **60.000-200.000 €** (plandenegocio.es 13-abr-2026 y lexpress 08-abr-2026) · **70.000-100.000 €** (BCH) · **137.000 €** (lahostelera, caso real de 90 m²) · **97.000-184.000 €** (estudio LBA, 80 m²) · **15.000-50.000 €** (Tamara Viñas, local con venta). **Los extremos son 15.000 y 200.000: un factor 13.** Ninguna explica la hipótesis. **Ésa es nuestra oportunidad más clara: no dar «un número», sino el modelo que produce el número del lector — y decir qué hipótesis lleva dentro.**

**H5 — El sector vende FORMACIÓN; nadie vende los ENTREGABLES.** Tamara regala 10 plantillas *dentro* de un curso de 697 €; Hotmart vende calculadoras de escandallo sueltas sin contexto de apertura; el software de 49 € hace el plan financiero pero **no da escandallo por lote, ni layout, ni APPCC, ni matriz de alérgenos**; y las ingenierías cobran 1.690 €+IVA por el papeleo **sin entregar ningún modelo económico**. **El producto que no existe es: el dossier completo de apertura de una pastelería en España, con los Excel que hacen los números y los documentos que pide el inspector, sin tutoría y sin suscripción.**

### 7.3 Qué hace bien la competencia y copiamos

| Práctica verificada | Dónde | Cómo la aplicamos |
|---|---|---|
| **Segmentar por MODELO y poner precio a cada uno** | Tamara separa «Obrador en Casa» (357 €) de «pastelería completa» (697 €) | **Una ruta por variante**, cada una con **su** CAPEX, **su** punto muerto y **su** checklist legal. No un único «monta una pastelería» |
| **Declarar en negativo lo que NO incluye** | Tamara: «no incluye recetas ni técnica pastelera» | Decirlo en la landing y en la primera página: **«esto no es un recetario ni un curso de técnica; es el dossier de apertura»**. Corta devoluciones |
| **Escenarios bajo / medio / alto, no un número** | lahostelera (600/900/1.200 €/m²) y spigadivulga (3 escenarios cerrados) | El CAPEX trae **tres escenarios paramétricos** y el €/m² **en celda verde**, nunca dentro de la fórmula |
| **El colchón de tesorería como partida propia** | spigadivulga lo señala como el error que mata negocios; lahostelera **no lo incluye** en sus 137.000 € | **Meses de colchón como parámetro**, ligado al cash-flow, con semáforo |
| **Plantillas como argumento de venta, no como bonus escondido** | Tamara enumera las 10 por su nombre; Escuela de Obradores vende «**más de 100 descargables**» | **Enumerar los 10 xlsx uno a uno con lo que calculan** en la landing. Es nuestro punto fuerte medible frente a un PDF |
| **Garantía visible** | Tamara publica «devolución íntegra a 30 días sin condiciones» **en portada** | Evaluar la política de devolución (decisión D10) |
| **Tablas con cifras, no párrafos** | lahostelera y spigadivulga rankean por dar tablas | Donde ellos ponen cifras sin origen, **nosotros ponemos cifra + URL + fecha** |

**Qué hace mal y NO copiamos:** horquillas de factor ×3-×13 sin hipótesis (todos) · citar normativa derogada (`emprendedores.es` con el RD 2207/1995) · vender «rentabilidad» en el titular y no dar ni un margen (`lexpress-franchise`) · publicar en 2020 y dejarlo rankeando en 2026 (`sillasmesas`) · y **despachar el punto legal más delicado del modelo doméstico en una frase sin fuente** (`pasteleriaparatodos`, G9).

### 7.4 Limitaciones declaradas del censo

1. **Es censo de precio publicado, no de mercado real.** Nadie publica unidades vendidas.
2. **Amazon.es queda FUERA por bloqueo técnico** (contenido vacío + HTTP 500). Es el mayor canal de libros en español: **el bloque de libros está incompleto por construcción**.
3. **Los portales de franquicia no son fuente primaria y se contradicen entre sí** (Granier 83.000 € vs 180.000 € con canon idéntico; Levaduramadre canon 18.000 € vs 24.000 €). Valen como **orden de magnitud publicado**, nunca como dato auditado.
4. **Los precios de Hotmart no son públicos** sin llegar al checkout: 3 infoproductos sin precio. **El mercado de plantillas de escandallo en español está infravalorado aquí.**
5. **Sesgo de idioma y país:** el censo es 100 % es-ES. **No se midió la oferta LATAM**, donde Hotmart es mucho más fuerte.
6. **Las fechas de los artículos gratuitos son las que ellos declaran.** Varios muestran «2026» en el título sin fecha de actualización verificable. **Un año en el título no prueba una revisión.**
7. **No se auditó la calidad interna de ningún producto de pago**: se compara **lo que prometen**, no lo que entregan.

---

## 8. Lo que ya vendemos y la FRONTERA: qué se cita y qué se construye

> **La conclusión del inventario, en una frase:** el catálogo resuelve muy bien **OPERAR** una pastelería (el kit de 12 € es exhaustivo: producción, encargos, alérgenos de vitrina, temperaturas, caja) y no resuelve **ABRIRLA** en absoluto. La línea es limpia porque el kit es completo en lo suyo.

### 8.1 Frontera con `kit-tareas-pasteleria` (12 €, 15 xlsx) — la más peligrosa, y seis reglas numeradas

L6 abrió los 15 libros uno a uno con `openpyxl`; yo he confirmado el recuento de ficheros.

| # | Riesgo | Por qué es real (medido) | **Regla de no-solape** |
|---|---|---|---|
| **R1** | **Plan de producción** | `10-plan-produccion-semanal.xlsx` ya trae **Plan Semanal 56×11 + Producido vs Vendido 261×12 + Resumen por Partida con Merma % y Coste merma €** | La guía **no emite ninguna hoja de plan de producción semanal**. El cap. 7 **cita el libro 10 por su nombre de fichero**. Lo que sí construye es **capacidad de obrador** (cuántas piezas/día permite el equipo que estás comprando): es una decisión de compra, no de operación |
| **R2** | **Encargos** | `11-control-encargos.xlsx`: Ficha 51×4 · Registro 48×15 · Agenda Entregas 19×8 · Encargos de Hoy 24×7 | **Prohibido rehacer.** La guía cubre **el modelo de negocio de encargos** (comuniones: captación, anticipo, calendario, riesgo de anulación) y remite al libro 11 para la herramienta |
| **R3** | **Alérgenos de vitrina** | `12-control-alergenos-vitrina.xlsx`: **Matriz 57×22** + Carta + Cartel + Etiquetas de los 14 UE. Y `pack-appcc/08` trae otra matriz 214×19 | **Prohibido rehacer, y prohibido duplicar con el pack.** La guía lleva **una fila de checklist legal** («matriz de alérgenos publicada antes de abrir») y **la matriz de OBRADOR**, que es otra cosa (materias primas × alérgenos × **orden de elaboración**, PA-22). *(Misma regla D5 del Manual del Chef: nunca dos declaraciones completas de alérgenos en el mismo catálogo.)* |
| **R4** | **Temperaturas y vidas útiles** | `13-registro-temperaturas-recepcion.xlsx`: Temperaturas 45×15 · Recepción 44×11 · Etiquetas 50×6 · **Vidas Útiles 28×4** (crema pastelera 48-72 h, nata montada 24 h, ganache 5-7 días) | **Prohibido rehacer.** La guía cita el libro 13 y el `pack-appcc`. Lo que sí construye es la **hoja de decisión del huevo** (art. 9: 70 °C/2 s · 63 °C/20 s · ovoproducto) y la clasificación **relleno vs estable a temperatura ambiente** (art. 4.1 fila 9), que **no está en ningún fichero del catálogo** |
| **R5** | **Calendario de picos** | `BONUS-02-calendario-anual-tareas.xlsx` ya lista las 6 campañas con producción y antelación; `06-eventos-festivos.xlsx` las desarrolla tarea a tarea | La guía **no repite el calendario**. Construye **la ECONOMÍA del pico**: % de facturación anual, capacidad necesaria, refuerzo de plantilla y tesorería inmovilizada. **El bonus dice cuándo y qué; la guía dice cuánto y si aguantas** |
| **R6** | **Perfiles de puesto** | `04-tareas-perfiles.xlsx`: Jefe Pastelero · Pastelero · Ayudante · Dependiente Vitrina, con sus tareas | La guía **no rehace las fichas de tarea**. Construye el **dimensionado** (cuántas personas de cada perfil, con bruto de convenio y SS) y el **plan de contratación** con plazos |

**Regla transversal (equivalente a la D4/D5 del Manual del Chef):** *cero fórmulas entre libros y cero duplicación de tabla operativa; cuando la guía necesita un dato que vive en el kit, lleva una **celda verde** con la nota «cópialo de tu `10-plan-produccion-semanal.xlsx`».*

> **Y esto es también el argumento de venta cruzada más honesto que tenemos:** la guía de 65 € puede decir, con verdad, «**la operativa del día 1 ya está resuelta en el Kit de Tareas Pastelería de 12 €; esta guía es lo que hay que decidir antes**». Son productos complementarios de verdad, no solapados.

### 8.2 Frontera con `guia-panaderia-obrador` (65 €) — mismo molde, contenido propio

**Se comparte (ESTRUCTURA, no contenido):** las 6 familias de checklist (legal, equipamiento, APPCC, contratación, marketing preapertura, salida de humos) · el gantt de apertura · la calculadora de CAPEX · el ticket medio · el P&L de 3 escenarios · el cash-flow / break-even · la estructura de 20 capítulos · los dos bonus.

**Es contenido propio de pastelería, y no se hereda:**

1. **Frío, no calor.** La panadería gira sobre horno, fermentación y masa madre; la pastelería gira sobre **frío negativo y abatimiento**: abatidor, cámara de fermentación controlada, congelación de entremets a −18 °C, glaseado sobre pieza congelada. **El CAPEX y la capacidad cambian por completo.**
2. **Estacionalidad extrema.** La panadería vende pan todos los días; la pastelería concentra en **6 picos** y multiplica por 5-10 (PS-41). **La panadería no tiene ese problema y su guía no lo modela.**
3. **Encargos y comuniones** como línea de negocio con anticipo, calendario y riesgo de anulación. En panadería es marginal.
4. **Vitrina y merma de exposición.** El producto caduca en 24-72 h y se vende a la vista.
5. **El huevo y el art. 9** (tres vías legales) y **la fila 9 del art. 4.1** (4 °C al relleno). **La panadería no tiene ninguno de los dos.**
6. **Las variantes del formato**, que la panadería no tiene: pastelería-cafetería · sin obrador · B2B/online · boutique de autor · cake design · **obrador en casa** (que **no es un apéndice: es un capítulo**).

> 🔴 **El riesgo mayor, y ahora es mucho más grande de lo que L6 creía:** no se puede lanzar la Guía de Pastelería enlazando a la de Panadería como hermana mientras **la de Panadería entrega un PDF de 1 página / 55 palabras** contra «20 capítulos, 70+ páginas». **Y medido por mí, no es sólo panadería: son 6 de los 8 productos de la franja 65-85 €** (§16, verificación 1). Tres salidas, y hay que elegir **antes** de escribir el copy — decisión **D2**.

### 8.3 Frontera con el resto del catálogo: qué se CITA y no se construye

| Ya existe en | Decisión |
|---|---|
| **`plan-negocio-panaderia` (35 €)** | ❌ **Se cita.** El plan responde «¿sale la cuenta y qué le enseño al banco?»; la guía responde «¿qué hago, en qué orden, con qué proveedor y qué me juego si me equivoco?». La guía **contiene** un plan financiero, y por eso la escalera 35 → 65 es coherente. **No existe `plan-negocio-pasteleria`** (verificado: los 10 planes son cafetería, food-truck, bar-restaurante, panadería, tapas-bar, catering, chef privado, paellero, parrillero y coctelería) → **no hay canibalización real hoy** |
| **`pack-appcc` (14 €, 21 xlsx)** | ❌ **Se cita entero.** La guía **no construye ni un registro APPCC**; construye el **checklist de puesta en marcha del sistema** (qué hay que tener el día de la inspección), que es otra cosa. *No aplican a pastelería: `09` aceite de fritura, `16` cocción-regeneración, `18` anisakis* |
| **`kit-escandallos` (12 €), hoja `05-pasteleria.xlsx`** | ❌ **Se cita** para el escandallo unitario. Verificado por mí: Instrucciones 66×2 · **Tarta Chocolate 38×13 · Croissants 37×13 · Macarons 37×13** · Conversiones 37×3 · Mermas 25×4. **Le falta, para quien abre:** son **3 elaboraciones**, no una carta; **no incorpora coste hora de obrador**; y no ayuda a **decidir el surtido**. La guía construye esa capa |
| **Guía Food Cost (55 €), cap. 17 «Costeo por Lote en Obrador y Pastelería»** | ❌ **Se cita el MÉTODO.** Son 1.400 palabras y 4 epígrafes, y su propio guion ya remite: «*Para el negocio que quiera la plantilla de costeo por lote lista, está en el Kit de Escandallos; aquí se da el método*». **La guía de pastelería no explica ingeniería de menú** (eso es Food Cost, caps. 1-16) |
| **`kit-tareas-chocolateria` (12 €)** | ❌ **Se cita** si la guía cubre la variante con línea de bombonería: aporta `02-partidas-produccion.xlsx` con hojas **Templado** y **Moldeado** |

### 8.4 El pipeline se reutiliza al 100 %, sin tocar una línea de código

- **`documentos.py`** carga el guion **por convención** (`guion_{pid.replace("-","_")}.py` + `importlib`) y ya parametriza `categoria_doc` / `tipo_doc`; **para una «Guía Cómo Montar» los valores por defecto son los correctos**. `GUIA['gates']` acepta `paginas_prometidas`, `palabras_objetivo`, `min_palabras_cap`, `cifras_extra`, `erratas_permitidas`, `erratas_forzadas`. **Cero cambios de código.**
- ✅ **`repartir_puntos()` está en `:1096` y COMMITEADO** (`3c1444d`) — verificado por mí. Acepta **`puntos_por_epigrafe`** (forma preferida, aborta si una clave no es epígrafe del capítulo) o reparto posicional. **Ningún guion existente lo usa** (grep: 0 de 4): **el de pastelería debe nacer con él.**
- **`dump_prompts.py`** y **`check_bloque.py`** son genéricos por `--producto <pid>`. `MODELO_FALLBACK = 'anthropic/claude-sonnet-4.6'` ya está.
- **`robots.txt`:** nada que tocar (verificado en los 5 bloques).
- **A crear:** la SPEC · `guias-v2_0/guion_guia_pasteleria_obrador.py` con su `NO_COMUN` propio · `scripts/productos-digitales/guia-pasteleria/` con 10 `gen_*.py` + `datos_ejemplo.py` + `verificar_guion.py` (copiado de `manual-chef-ejecutivo/`, que valida que las N referencias a celda existen **antes** de gastar tokens de redacción).
- 🔴 **Ordenación crítica:** `documentos.py` lee `xlsx_dir = DL/<pid>/`. **Los 10 libros tienen que estar copiados en `astro-site/public/dl/guia-pasteleria-obrador/` ANTES de lanzar la redacción**, porque el guion cita cifras por `fichero.xlsx!Hoja!Celda` y el pipeline las resuelve con openpyxl para meter **el número** en el prompt. **Invertir el orden hace que el guion no pueda escribirse.**
- ⚠️ **`guias-v2-SPEC.md` §5.3 y la cabecera de `documentos.py` siguen diciendo «texto largo SIEMPRE con bridge.py» y están DESACTUALIZADAS.** Manda la regla de John del 2026-09-04: los productos digitales los escriben **subagentes Anthropic**.

---

## 9. Bloque obligatorio 7 — La lista DEFINITIVA de entregables

### 9.1 El juego de datos único: la pastelería «La Clara»

Patrón obligado (`guia-food-cost/datos_ejemplo.py`): **un solo `datos_ejemplo.py`** del que beben los 10 generadores, el guion y los dos bonus. *Si un número cambia, cambia ahí y se regeneran los libros.*

| Campo | Propuesta | Por qué |
|---|---|---|
| Nombre | Pastelería de ejemplo **«La Clara»** | Neutro, sin marca real. Paralelo a «La Encina» de Food Cost y del Manual del Manager |
| Formato | **Obrador propio + despacho a calle**, ciudad media española (PS-05) | Es el caso central; las demás variantes se tratan como **desviaciones sobre él** |
| Superficie | **~110 m²**: obrador ~55 · despacho ~25 · cámara/almacén ~15 · aseos y vestuario ~15 | Coherente con el «mínimo 80 m²: obrador + tienda» del checklist F2 de `plan-negocio-panaderia`, subido por el frío de pastelería. ⚠️ **Es PROPUESTA, no medición** |
| Plantilla | Jefe pastelero · 1 oficial · 1 ayudante · 2 dependientes (1 a tiempo parcial) | **Coincide exactamente con los 4 perfiles del `04-tareas-perfiles.xlsx`** del kit → el cross-sell es literal. Y encaja con los grupos del convenio de Madrid (PA-33) |
| Carta | **30 referencias** en 5 familias: bollería · pastelería individual · tartas y entremets · panes de acompañamiento · temporada | Las 3 primeras deben incluir croissant, pain au chocolat y napolitana de crema: son las que el `10-plan-produccion-semanal.xlsx` y el `12-control-alergenos-vitrina.xlsx` **ya traen precargadas** |
| **Coherencia externa obligatoria** | Tarta de chocolate 70 %, croissants y macarons con **el mismo escandallo** que `kit-escandallos/05-pasteleria.xlsx` | Un cliente con los dos productos vería **dos costes distintos del mismo croissant**. **Copia declarada, nunca vínculo entre libros** |

**Restricciones de familia, no negociables:** helpers de `motor.py` (`f()`, `val()`, `verde()`, `dv_lista()`, `semaforo_isnumber()`, `version_line()`, `hoja_instrucciones()`) · hoja «Instrucciones» primero con «celdas verdes = editables», línea de versión, bio anclada y nota de desproteger · **cero constantes tecleadas dentro de una fórmula** · `IFERROR(...;"")` y `ISNUMBER` en semáforos · «sin dato» = `""`, nunca `0` · **prohibidos `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET`, `LAMBDA` y las referencias entre libros** (`COUNTIF` sí, lo usan los checklists del molde B) · formatos `#,##0.00 €` / `0.0 %` / `dd/mm/yyyy` · A4 con `print_setup` · metadata `author='AI Chef Pro'` · **cada celda con dato legal lleva nota «Verificado el 09-09-2026 · norma · URL»** · al final, `inject_cache.py` + verificación `data_only` de cada fórmula + `mapa-<libro>.json`.

### 9.2 Los 10 libros de Excel — evaluación de la propuesta de L6 y propuesta final

**Confirmo los 10 libros de L6 y los corrijo en cuatro puntos**, con la misma lógica del research anterior: (a) el bloque legal más diferencial consigue herramienta **sin añadir un libro 11**; (b) el hallazgo que ninguna competencia cubre entra como hoja del libro que le toca; (c) el libro financiero cambia de molde; (d) la variante doméstica deja de ser un párrafo y pasa a ser una hoja con contador.

| # | Libro | Hojas | Entradas (celda verde) | Salidas por fórmula | Qué decisión permite | Frontera |
|---|---|---|---|---|---|---|
| **1** | **`capacidad-obrador-y-local.xlsx`** ⭐ | Instrucciones · Parámetros · Zonas y m² · Capacidad por Equipo · Cuello de Botella · **Ficha de Visita a Local** (con la prueba de humos) | m² por zona, litros de amasadora, bandejas de horno, m³ de cámara y de abatidor, horas de turno, potencia instalada | m² totales y % obrador/venta, piezas/día por equipo, **el equipo que limita**, piezas/día del conjunto, ¿aguanta el pico?, **semáforo eliminatorio del local** | **Nada equivalente en el catálogo.** El kit organiza la producción en el obrador que ya tienes. Cubre los dolores 1 y 2 (los dos más frecuentes del corpus) |
| **2** | **`calculadora-capex-pasteleria.xlsx`** ✏️ *recargado* | Instrucciones · Parámetros · CAPEX por Bloque · Variante del Formato · **Traspaso vs Obra Nueva** · IVA y Tesorería · Resumen | importe por partida (mín/máx/tuyo), variante elegida, **columna «¿lleva IVA?» y tipo por línea**, precio de traspaso, renta mensual, años de horizonte, meses de colchón | total por bloque y total CAPEX, **IVA soportado y cuándo se recupera**, CAPEX por variante, **coste a 5 años de traspaso+renta contra obra nueva+renta** | ✏️ **Mi corrección nº1 a L6:** el comparador **traspaso vs obra nueva** era el hallazgo más diferencial de L4/L5 (§3.5) y L6 no lo incluía. Entra como **hoja**, no como libro 11. **No existe en ninguna guía de la competencia** y es literalmente el consejo del pastelero con 47 empleados |
| **3** | **`estacionalidad-y-picos.xlsx`** ⭐ | Instrucciones · Parámetros · Calendario de 6 Picos · Peso sobre el Año · **Capacidad vs Demanda del Pico** · Refuerzo y Tesorería | ventas estimadas por pico, precio y unidades, personal de refuerzo, antelación de compra | % de facturación de cada pico sobre el año, **déficit de capacidad en el pico** (contra el libro 1), coste del refuerzo, **tesorería inmovilizada en stock de temporada** | **El libro más propio de todo el producto.** Ni panadería ni ningún restaurante lo tienen. Frontera R5: el `BONUS-02` del kit da fechas; éste da euros. Lo justifica solo el 100 → 400 roscones/día con el mismo equipo |
| **4** | **`carta-de-apertura-y-escandallo.xlsx`** ⭐ ✏️ *recargado* | Instrucciones · Parámetros (coste hora obrador) · Escandallo por Tanda (30 refs) · Coste Hora y Mano de Obra · **Decisión de Huevo y Temperatura** · Mix y Ticket Medio · Decisión de Surtido | precios de compra, gramaje, tanda, minutos de mano de obra, PVP, mix %, **vía legal del huevo por elaboración** | coste materia por pieza, **coste de mano de obra por pieza**, coste total, food cost %, margen €, aporte al ticket medio, semáforo de surtido, **temperatura de conservación y vida útil resultantes de la vía elegida** | ✏️ **Mi corrección nº2 a L6:** la hoja `Decisión de Huevo y Temperatura` materializa **PA-14 + PA-12 + PA-15** — las tres vías del art. 9 (70 °C/2 s · 63 °C/20 s + consumo inmediato · ovoproducto) y la resolución del conflicto **4 °C vs 8 °C**. Es **el corazón técnico-legal de una pastelería, no existe en ningún producto del catálogo ni de la competencia**, y evita un libro 11. ⚠️ **Aquí manda la regla única de margen** (PS-55/56): el libro calcula una desde la otra y **nunca pide las dos** |
| **5** | **`plan-financiero-3-anos-pasteleria.xlsx`** ⭐ | 0. Supuestos · Inversión Inicial · PyG 3 Años · Punto de Equilibrio · Escenarios · Personal · **Tesorería 12 meses** · Financiación · Instrucciones | tickets/día, ticket medio sin IVA, días de apertura, **estacionalidad mensual**, rampa de arranque, brutos de convenio, % de SS, condiciones de deuda | P&L, punto muerto, 3 escenarios, coste de personal con SS, tesorería mes a mes, servicio de deuda | ✏️ **Mi corrección nº3, firmada con L6:** se construye con el **molde de `planes-v2_0` (motor 2.2)**, verificado por mí en `plan-negocio-panaderia/plan-financiero-panaderia.xlsx` (9 hojas, `Tesorería 12 meses` 70×15 con rampa 0,55→1,00, `Personal` con SS a cargo de la empresa, columnas «¿Lleva IVA?» y «Tipo de IVA de la línea»), **NO con el `plan-financiero-3-anos.xlsx` de la guía de panadería** (25×5, 21 fórmulas, sin tesorería, sin IVA, sin financiación). **Si no, la guía de 65 € entregaría un plan peor que el del plan de negocio de 35 €.** Es la **fuente única de cifras del texto** |
| **6** | **`mix-de-canales-y-punto-muerto.xlsx`** | Instrucciones · Parámetros · Mostrador · Encargos · B2B · Online y Envío · Punto Muerto por Canal | ventas y margen por canal, coste de servir cada canal, comisión de plataforma | margen de contribución por canal, **punto muerto con y sin B2B**, canal que sostiene el negocio | Nada equivalente. Aquí se juegan las variantes PS-02, PS-09 y la online. Conecta con PS-53 (95/5) y con PS-102 (el B2B desestacionaliza) |
| **7** | **`checklist-legal-y-licencias.xlsx`** ✏️ *recargado, y es el libro más diferencial del bloque legal* | Instrucciones · 6 fases (F1-F6) con contador · **Árbol de Registro Sanitario** · **Control de Suministro B2B (25 % / 500 kg / 50 km)** · **Ruta Doméstica (lista blanca + contador de 100 kg/semana)** · Registro de Formación | ✓/☐/N/A, fecha, responsable, coste; CCAA; kg suministrados por destinatario y semana; kg elaborados en vivienda; formación por persona | contador por fase y % de avance; **veredicto «te basta la comunicación autonómica» / «te toca RGSEAA»**; **semáforo de los tres umbrales acumulativos**; **alerta al superar 100 kg/semana**; caducidad de la formación | ✏️ **Mi corrección nº4 a L6:** su libro 7 era un checklist de fases a secas. **Recargado con PA-01/02/03 y PA-29 pasa a ser la pieza que corrige el error nº1 del nicho y la que sirve a la buyer persona A** (la de más búsqueda). ⚠️ **El epígrafe de IAE (644.1 / 419.1 / 419.2) NO se copia de la guía de panadería sin verificar** (V del §2.5) |
| **8** | **`checklist-equipamiento-y-proveedores.xlsx`** | Instrucciones · Equipamiento (mín/máx, prioridad, **¿lleva IVA?**) · Variante del Formato · Proveedores · Contador | ✓, precio real negociado, proveedor, **plazo de entrega** | contador, **desviación contra el CAPEX del libro 2**, **plazo crítico** | Molde B de `checklist-equipamiento`. **La columna de PLAZO es nueva**: una laminadora a 8 semanas mueve la fecha de apertura. Se siembra con los **9 proveedores verificados** (§4.4) y con los precios de §4.1-4.2, **cada línea con su columna de IVA** |
| **9** | **`cronograma-apertura-gantt.xlsx`** | Instrucciones · Gantt (hitos × meses) · Ruta Crítica · Fecha de Apertura | fecha de inicio, duración de cada hito | mes de cada hito, **ruta crítica**, fecha de apertura estimada, **aviso si cae fuera de pico** | Molde `cronograma-apertura-gantt` de panadería, que hoy tiene **0 fórmulas**: aquí **con** fórmulas. La estacionalidad hace que **la fecha de apertura sea una decisión de dinero** |
| **10** | **`plantilla-turnos-y-coste-personal.xlsx`** | Instrucciones · Parámetros (convenio, % SS) · Turnos Semanales · Horas y Coste · Plan de Contratación | horas por persona y día, bruto de convenio, % de SS, fecha de alta | horas semanales por persona y total, **coste mes y año con SS**, aviso si se pasa de jornada, coste del refuerzo de pico | El molde `plantilla-turnos-brigada` de panadería **tiene 0 fórmulas**: no calcula ni horas ni coste. **La SS se olvida y hunde el P&L.** Se siembra con **los 6 grupos del convenio de Madrid (PA-33) en celda verde**, sustituibles por el convenio del lector |

**Cobertura de la promesa publicada en el hub desde mayo** («obrador, vitrina, maquinaria, proveedores, licencias y lanzamiento»): obrador → 1, 3 · vitrina → 4, 6 (+ el libro 12 del kit) · maquinaria → 2, 8 · proveedores → 8 · licencias → 7 · lanzamiento → 9. **Los seis sustantivos quedan cubiertos.**

### 9.3 Los dos bonus — y uno que se descarta con argumento

**BONUS 1 — `business-plan-modelo-pasteleria.docx` (RELLENO).** El caso completo de «La Clara» con cifras: resumen ejecutivo, mercado, concepto, plan de operaciones, plan financiero y análisis de riesgos con escenarios. **Objetivo ≥3.500 palabras y ≥8 tablas**, todas coherentes con el libro 5. **Justificación medida:** es el formato que pide un banco o una línea ENISA, y **la versión de panadería son 796 palabras y 0 tablas** contra una landing que promete «resumen ejecutivo, proyecciones financieras a 3 años y análisis de mercado» — **no entrega ninguno de los tres**. Las versiones de casual (287 pal.), gastronómico (300), mexicano (360), peruano (388), japonés (400) y nikkei (463) están igual o peor (medido por mí).

**BONUS 2 — «12 decisiones de apertura resueltas» (PDF + DOCX).** ~25-30 páginas ≈ **10.500-12.500 palabras**. Molde probado **dos veces** (`BONUS-12-situaciones-resueltas-cocina`: 34 págs / 15.762 palabras, medido). Cada decisión con **contexto · opciones · criterio · la celda del libro que la resuelve · y la norma con su id `PA-*` y su fecha de verificación** cuando la hay. Las doce:

1. Local con obrador vs obrador aparte. · 2. Comprar el abatidor o esperar. · 3. Abrir con 20 referencias o con 40. · 4. Producto de terceros al arrancar: cuándo sí (y qué te prohíbe decir en el escaparate, PA-17). · 5. Cuánto roscón produzco el primer año. · 6. Aceptar el primer encargo de comunión sin histórico. · 7. El primer contrato B2B: a qué precio, **y en qué momento te obliga el RGSEAA** (PA-02). · 8. Contratar oficial o tirar de ayudante. · 9. Abrir en septiembre o en febrero. · 10. **Empezar en casa dentro de la legalidad: qué puedo vender y qué no** (PA-29). · 11. Envío a domicilio: qué producto viaja y cuál no. · 12. Qué hago con lo que no se vende hoy (PA-20 y Ley 1/2025).

**BONUS 3 (recetario de escandallos base de 20 referencias) — 🔴 DESCARTADO como pieza independiente.** Un recetario con gramajes y costes que **nadie ha cocinado** es exactamente el patrón de cifra inventada que la casa prohíbe, y **no hay forma de citar fuente para el gramaje de una receta propia**. **Alternativa sin riesgo:** las 30 referencias viven **dentro del libro 4** como datos de ejemplo declarados como tales, con las 3 primeras coincidiendo con `kit-escandallos/05-pasteleria.xlsx`. Se gana coherencia y se pierde un riesgo.

### 9.4 Resumen del paquete

**1 guía (PDF + DOCX) de 20 capítulos · 2 bonus (business plan relleno + 12 decisiones resueltas) · 10 libros de Excel con fórmulas vivas.** Pago único, acceso vitalicio al dashboard, actualizaciones incluidas.

> **Es, con diferencia, el paquete más grande de los cuatro productos nuevos del ciclo:** Food Cost entregó 8 xlsx, el Manual del Manager 7 y el Manual del Chef Ejecutivo **7** (contados por mí: 7 `gen_*.py` en `scripts/productos-digitales/manual-chef-ejecutivo/`). Aquí son **10**, y **tres no tienen molde previo** (capacidad de obrador, estacionalidad, mix de canales). Eso es lo que sostiene el precio y lo que dispara el presupuesto (§15.4).

---

## 10. Índice propuesto: 20 capítulos, con presupuesto de palabras calibrado

**Calibración MEDIDA por mí con PyMuPDF sobre los PDF que se venden hoy** (no estimada): cuerpo **529-544 palabras/página** · bonus **406-464**. Y la lección de los dos productos anteriores: **el guion se sobrepasa siempre en ~+30 %**.

| Entregable | Presupuesto de guion | Salida realista (con el +30 % medido) | Gate interno | Qué publica la landing |
|---|---|---|---|---|
| **Guía, 20 capítulos** | 1.700-1.850 palabras/cap. (los 3 legales —9, 10, 19— a 2.100) ≈ **37.000 palabras** | **42.000-46.000 palabras → 78-86 páginas** | `paginas_prometidas: 70` · `min_palabras_cap: 1.300` | **La cifra MEDIDA tras construir** (decisión D17 de la familia). Nunca la prometida |
| **Bonus 2, 12 decisiones** | 800-900 palabras/decisión + 1 tabla ≈ **10.500 palabras** | **12.000-13.500 palabras → 28-32 páginas** | `paginas_prometidas: 25` · `min_palabras_cap: 600` | Ídem |
| **Bonus 1, business plan** | ≈ **3.500 palabras + 8 tablas** | 3.500-4.500 palabras | ≥8 `<w:tbl>` verificadas descomprimiendo `word/document.xml` | «Business plan modelo relleno con el caso completo» |

**Cada capítulo con `puntos_por_epigrafe`** (la forma preferida de `repartir_puntos()`, que **ningún guion usa todavía**). **Ninguna cifra entra si no sale de una celda de xlsx o de un id `PA-*` / `PS-*`.**

| # | Capítulo | Contenido obligatorio | Libro / tabla | ids |
|---|---|---|---|---|
| **01** | **Qué negocio estás montando: las 11 variantes y cuál te toca** | La matriz comparada de los 11 sub-conceptos con inversión, m² y personal; **la frontera con el Kit de Tareas y con el plan de negocio en la primera página**; mapa «problema → capítulo → herramienta»; y qué **NO** vas a encontrar aquí (no es un recetario, no es un curso de técnica, no sustituye al proyecto técnico visado) | `capacidad-obrador-y-local!Parámetros` | PS-01 a PS-11 |
| **02** | **El cliente y la plaza: quién compra pastelería y cuándo** | Consumo en hogares y la **brecha por renta** (8,26 vs 4,39 kg); **sólo ~1 de cada 20 euros pasa por el comercio especializado**; el competidor real es la masa congelada (+31,1 % de producción 2018-2025); por qué el obrador **no compite en volumen y no debe intentarlo** | `estacionalidad-y-picos!Peso sobre el Año` | PS-28, PS-29, PS-33, PS-26 |
| **03** | **La carta de apertura: 30 referencias y por qué esas** | Cómo se decide el surtido de apertura; familias y su papel; **un solo producto puede ser el 30 % de la caja** (Hofmann); margen por familia (la galleta rinde el doble que la tarta) | `carta-de-apertura-y-escandallo!Decisión de Surtido` | PS-43, L5-D5 |
| **04** | **Cuánto cuesta abrir: el CAPEX real, partida a partida** | **Por qué las cifras publicadas se contradicen por un factor 13** y qué hipótesis lleva cada una; los tres escenarios de obra (600/900/1.200 €/m²); **el colchón de tesorería como partida, no como propina**; y el aviso del IVA por línea | `calculadora-capex-pasteleria!CAPEX por Bloque` | PS-85, PS-05, ⛔ nada de §15.1 |
| **05** | **El local: metros, zonas y la ficha de visita** | Las **7 zonas obligatorias** y el principio de **marcha adelante**; superficies, encuentros redondeados, lavamanos no manual; **20-80 kW sólo para los hornos**; altura libre y carga de forjado | `capacidad-obrador-y-local!Zonas y m²` | PS-86 |
| **06** | **Antes de firmar el alquiler (el capítulo que ahorra el dinero)** | El checklist de cribado eliminatorio; **la salida de humos hasta cubierta y 1 m sobre la cumbrera**, con la comunidad de propietarios como riesgo real; la pregunta al ayuntamiento («¿mi actividad es comercio o industria artesanal en el planeamiento?»); **y las tres puertas de entrada: local nuevo, traspaso o franquicia**, con el cálculo de renta a 5 años | `calculadora-capex-pasteleria!Traspaso vs Obra Nueva` + `…!Ficha de Visita a Local` | PA-06, PA-07, PS-69, PS-70 |
| **07** | **El obrador por dentro: frío, calor y flujo de trabajo** | Por qué la pastelería gira sobre **frío negativo**, no sobre horno; abatidor, cámara de fermentación controlada, congelación de entremets; **un arcón doméstico no vale como abatidor** (art. 5); capacidad por equipo y **cuál es tu cuello de botella** | `capacidad-obrador-y-local!Capacidad por Equipo` | PA-13 |
| **08** | **Maquinaria: qué compras, qué alquilas y qué esperas a tener** | Precios reales por gama con marca y modelo; **la trampa del IVA** (unos distribuidores publican con y otros sin); **«sin salida de humos» como ventaja de negocio**, no como detalle técnico; segunda mano y plazos de entrega | `checklist-equipamiento-y-proveedores!Equipamiento` | PS-72 a PS-84, PS-11, PS-100 |
| **09** | **Licencias, sanidad y registro: el camino completo** 🔴 | **El error nº1 del nicho: la pastelería minorista NO va al RGSEAA**; la comunicación o declaración responsable autonómica **que no habilita**; **los tres umbrales acumulativos** del art. 3 y el aviso de que los 500 kg **incluyen el mostrador**; central + sucursales; el cuadro por CCAA con Madrid y su **plazo del 28-mar-2027**; y **la ruta doméstica con su lista blanca** | `checklist-legal-y-licencias!Árbol de Registro Sanitario` + `…!Ruta Doméstica` | **PA-01, PA-02, PA-03, PA-04, PA-05, PA-29** |
| **10** | **APPCC, alérgenos y formación: qué hay que tener el día de la inspección** | APPCC **simplificado es legal** y exige **persona responsable designada con nombre**; las guías sectoriales son **voluntarias**; **el carnet de manipulador no existe** desde 2010 → lo que hace falta es un **registro de formación**; alérgenos de **obrador** (equipos, recipientes, orden de elaboración) frente a alérgenos de **vitrina** (que ya resuelve el kit); «sin gluten» ≤20 mg/kg | `checklist-legal-y-licencias!Registro de Formación` *(cita `pack-appcc` y el libro 12 del kit)* | PA-09, PA-10, PA-11, PA-21, PA-22, PA-23 |
| **11** | **Proveedores: materia prima, packaging y plazos** | Los 9 proveedores verificados por categoría; cómo pedir **tres presupuestos comparables**; **packaging al 5-15 % del coste**; y **cómo modelar la volatilidad de mantequilla y cacao** en vez de fijar un precio | `checklist-equipamiento-y-proveedores!Proveedores` | PS-87 a PS-95, PS-59, PS-66, ⛔ PS-67 sin cifra |
| **12** | **Escandallo y precios: por qué la mano de obra manda** | La unidad de costeo es **la tanda, no la pieza**; **coste hora de obrador imputado por pieza**; **margen bruto y food cost son la misma regla dicha dos veces**; precio por **ración** en la tarta por encargo; y el miedo a subir precios con su antídoto numérico | `carta-de-apertura-y-escandallo!Coste Hora y Mano de Obra` *(cita Food Cost cap. 17 y `kit-escandallos/05`)* | PS-55, PS-56, L5-D5 |
| **13** | **El equipo: cuántos, qué perfiles y qué cuestan** | Los **6 grupos del convenio de Madrid** y sus áreas funcionales OBRADOR / COMERCIO / ADMINISTRACIÓN; **el convenio manda sobre el SMI** (el grupo más bajo, 17.886,30 €/año, supera los 17.094 € del SMI); bruto → **coste empresa con SS**; y el problema estructural: no se encuentra personal | `plantilla-turnos-y-coste-personal!Horas y Coste` *(cita el libro 04 del kit)* | PA-32, PA-33, PS-104-106 |
| **14** | **Turnos de madrugada y jornada legal** | El registro de jornada hoy (papel o Excel valen) y **la reforma digital en tramitación**; el turno de obrador contra el de despacho; **el horario del dueño** como decisión de vida, con la evidencia de Noelia Tomé | `plantilla-turnos-y-coste-personal!Turnos Semanales` | PA-34 |
| **15** | **Los seis picos del año: Reyes, San Valentín, Padre/Madre, Semana Santa, comuniones, Todos los Santos** 🔴 | El pico multiplica por **5-10** con el mismo equipo; **cuánto pesa cada campaña sobre el año**; el déficit de capacidad y el refuerzo; **la tesorería inmovilizada en stock de temporada**; y la desestacionalización | `estacionalidad-y-picos!Capacidad vs Demanda del Pico` | PS-41, PS-35, PS-36, PS-38, PS-44 |
| **16** | **Encargos y comuniones como línea de negocio** | Captación, **anticipo y señal**, calendario de entrega y riesgo de anulación; precio por ración; qué se acepta y qué no sin histórico | `mix-de-canales-y-punto-muerto!Encargos` *(cita el libro 11 del kit)* | L5-D9 |
| **17** | **Canales: mostrador, B2B, online y envío** | El **95/5** de cobro directo y a crédito; **cuándo el B2B te obliga a inscribirte en el RGSEAA**; venta a distancia (ya es minorista) y la información obligatoria **antes de la compra**; qué producto viaja | `mix-de-canales-y-punto-muerto!Punto Muerto por Canal` | PS-53, PA-02, PA-27, PA-28 |
| **18** | **El plan financiero y el dinero hasta el break-even** | P&L a 3 años con **estacionalidad mensual y rampa de arranque**; punto muerto; **el sueldo del propietario como renglón propio**; y la cifra honesta: **rentabilidad neta real del 8-12 %**, con la frase de Noelia Tomé («de 500.000 quedaban 15.000-20.000») | `plan-financiero-3-anos-pasteleria!PyG 3 Años` | PS-48, PS-58, PS-60, PS-62 |
| **19** | **Financiación, IVA, envases y tesorería del arranque** | Financiación y servicio de deuda; **IVA por familia de producto** ⚠️ (sólo cuando esté verificado, V-02); **Verifactu: 1-ene-2027 y 1-jul-2027**, y el software que compres hoy ya debe cumplir; envases (**1 referencia reutilizable de bebida desde 1-ene-2027 si tienes <120 m²**) y la duda del «productor de producto»; **desperdicio: art. 6 exigible desde el 2-abr-2026, y por qué tu pastelería está exenta del plan** | `plan-financiero-3-anos-pasteleria!Financiación` + `…!IVA y Tesorería` | PA-36, PA-37, PA-30, **PA-31** |
| **20** | **Cronograma, apertura y los primeros 90 días** | Ruta crítica y fecha de apertura; **abrir fuera de pico y llegar rodado a Reyes**; la libertad horaria por ley como decisión comercial del día 1; qué se mide en el mes 0 y en el mes 3, con responsable y fecha | `cronograma-apertura-gantt!Ruta Crítica` *(cita todo el kit de tareas)* | PA-39 |

---

## 11. Bloque obligatorio 8 (parte 2) — Precio y ancla

### 11.1 La escalera real del catálogo (47 productos, parseada por mí hoy)

| Franja | Nº | Productos |
|---|---|---|
| 9 € | 1 | eBook Pro Prompts |
| **12 €** | **13** | Kit de Escandallos + 12 kits de tareas por concepto (incl. **`kit-tareas-pasteleria`** y `kit-tareas-chocolateria`) |
| **14 €** | **8** | Kit de Tareas, Pack APPCC, Kit de Inventario, Kit de Gestión de Personal + 4 kits de tareas |
| 18 / 18,50 € | 2 | `kit-tareas-chef-privado` · `kit-tareas-hotel` |
| 24 € | 1 | **Guía Dark Kitchen** *(la única «Cómo Montar» que no está a 65 €)* |
| 29 € | 2 | plan-negocio-cafeteria · plan-negocio-food-truck |
| 35 € | 3 | plan-negocio-bar-restaurante · **plan-negocio-panaderia** · plan-negocio-tapas-bar |
| **39 €** | 1 | Kit Plan Financiero |
| 45 € | 4 | 4 planes de eventos |
| **55 €** | **3** | Guía Food Cost + Ingeniería de Menú · Manual del Manager de Restaurante · Plan Coctelería |
| **65 €** | **7** | 6 guías «Cómo Montar» (casual, **panadería-obrador**, japonés, mexicano, nikkei, peruano) **+ Manual del Chef Ejecutivo** |
| 85 € | 1 | Guía Restaurante Gastronómico |
| 89 € | 1 | Mega Pack de Tareas |

### 11.2 Recomendación: **65 €**

**Seis argumentos, uno por línea:**

1. **La hermana directa está a 65 € y comparte molde, estructura y comprador.** `guia-panaderia-obrador` es el paralelo exacto: obrador, humos, APPCC, CAPEX, checklists, business plan. Separarse obligaría a explicar por qué la pastelería vale distinto que la panadería.
2. **El precedente más reciente empuja hacia arriba, no hacia abajo.** Verificado por mí: **el Manual del Chef Ejecutivo salió a 65 €** (commit `b056abc`, 6-sep) cuando su propio research recomendaba 55 €. **La franja de 65 € es hoy la franja de los productos grandes del catálogo**, no sólo la de las guías.
3. **El paquete es objetivamente mayor que el de cualquier producto nuevo anterior: 10 libros de Excel frente a 7-8**, más 2 bonus. Es exactamente la condición que L1 ponía para no bajar («la única vía honesta a otro precio es que el paquete sea mayor **y esté enumerado**»).
4. **El hueco de mercado está entre 49 € y 357 € y no lo ocupa nadie.** A 65 € somos **1,33×** el software de plan de negocio (49 €) dando además layout de obrador, APPCC, alérgenos de obrador, escandallo con mano de obra, estacionalidad y checklists; y el **12 %** de «Obrador en Casa» (357 €).
5. **Las anclas externas aguantan sin retórica:** el único libro de administración de pastelerías cuesta **190 € y es de 2015** (2,9×) · la gestión de licencias va de **350 € a 18.000 €** por lo mismo · un **plan APPCC externo, 700-800 €** (11×) · la licencia de obrador en Madrid, **1.690 € + IVA** (**26 guías**) · el canon de franquicia más barato del sector, **8.000 €** (**123×**).
6. **Y el argumento de valor más limpio de todo el research, medido:** «**un plan APPCC por técnico externo cuesta 700-800 €; esta guía entera cuesta 65 €**». No hace falta inflarlo.

**Sin `priceOld` ni `discountBadge`** (decisión D2 de la familia: producto nuevo, sin «precio anterior de 30 días» que sostenga un tachado — art. 20 TRLGDCU / RDL 24/2021). **Sin `aggregateRating`, sin `review` en el JSON-LD y sin testimonios inventados** (D3): la sección de testimonios se oculta con `items: []`, que `GuiaLandingPage.astro` ya soporta. **Nace con NOWPayments** además de Stripe (regla de John del 6-sep).

### 11.3 Las alternativas, con su coste honesto

- **85 €** — es la opción que L1 deja abierta «sólo si el paquete de xlsx supera claramente al de la guía de panadería **y se comunica entregable a entregable**». Y objetivamente lo supera: **10 libros frente a 15 plantillas de v1.0 sin fórmulas** (tres de los 15 de panadería tienen **cero** fórmulas). **Su coste:** colisiona con la **Guía Restaurante Gastronómico (85 €)**, que hoy promete 119 páginas y **entrega 10** — sería el vecino de precio más incómodo posible; rompe la paridad con la hermana directa; y obliga a justificar por qué la pastelería vale más que la panadería. **No lo recomiendo hasta que la línea esté arreglada.**
- **55 €** — es lo que sugería la voz del cliente por prudencia. **Su coste:** lo pondría **por debajo del Manual del Chef Ejecutivo con un paquete mayor** (10 xlsx frente a 7), desaprovecha las anclas de 190/700/1.690 €, y **rompe la lectura de la franja**: el hub enseña las «Cómo Montar» juntas y la de pastelería aparecería como la barata de la familia.
- **49 € — VETADO**: es el precio tachado del Kit de Escandallos y chocarían en el hub (misma razón que en los tres productos anteriores).

> **Lo que se deja sobre la mesa, dicho en voz alta:** con 65 € renunciamos al margen que el paquete de 10 libros justificaría. Se hace **a cambio de coherencia con la hermana directa y de no tocar la franja de 85 €** mientras el producto que la ocupa entregue 10 páginas de 119. **Si John prefiere el margen, 85 € es defendible con el recuento de entregables en la mano — pero entonces la Guía Gastronómica debería arreglarse antes** (decisión D2 + D3).

---

## 12. Nombre, slug, subtítulo, promesa y vocabulario

### 12.1 Nombre y slug

**Titular / H1: «Cómo Montar una Pastelería».** No es una preferencia: **es el nombre con el que el producto lleva anunciado en el hub desde mayo**, en los dos ficheros y con su descripción publicada, y **es el ejemplo que el buscador del hub sugiere al visitante** (`ProductosDigitalesHubPage.astro:2259`). Cambiarlo rompe una promesa que ya está en producción.

**Nombre de catálogo, banner y email: «Guía Pastelería con Obrador»** — calca la ficha de la hermana (`products-catalog.ts`: `name: { es: 'Guía Panadería con Obrador', en: 'Guide: Bakery with Production Room' }`). Inglés propuesto: **«Guide: Pastry Shop with Production Room»**.

**Slug recomendado: `guia-pasteleria-obrador`** → `https://aichef.pro/guia-pasteleria-obrador`, `-access`, `-library`.

| Alternativa evaluada | Veredicto |
|---|---|
| **`guia-pasteleria-obrador`** | ✅ **Recomendado.** Calca el patrón del hermano; incluye «obrador», que en España tiene 9.900/mes de reconocimiento de marca-categoría y es la palabra que usa el propio anuncio del hub; **cubierto por `robots.txt` en los 5 bloques sin tocar nada** (verificado por mí) |
| `guia-pasteleria` | ❌ Rompe el paralelismo y pierde «obrador», que es lo que distingue este producto de un curso de repostería. Y **colisiona visualmente con `kit-tareas-pasteleria`**: dos slugs casi homónimos de productos distintos invitan al error que ya costó el enlace roto del hub de librerías |
| `guia-como-montar-pasteleria` | ❌ Mete en el slug una keyword de **10/mes** que no compra nada, rompe el patrón de los 9 slugs `guia-*` existentes y es el más largo de la línea |

⚠️ **Y un aviso de nomenclatura que ya costó dinero en este repo:** el nombre del enlace debe coincidir con el de la página de destino. Si el hub dice «Cómo Montar una Pastelería» y la landing se titula «Guía Pastelería con Obrador», **el H1 y el título del hub tienen que decir lo mismo** o repetimos el defecto de «Biblioteca de Prompts» → `/libreria-de-prompts`.

### 12.2 Copy

| Elemento | Propuesta | Nota |
|---|---|---|
| **H1** | **«Cómo Montar una Pastelería»** | Es la promesa publicada desde mayo |
| **Title** (≤60) | **«Cómo Montar una Pastelería \| Obrador, Licencias y Números»** (58) | Alternativa: «Guía Pastelería con Obrador \| Abrir Paso a Paso» (52) |
| **Subtítulo del hero** | **«El dossier completo de apertura: los diez Excel que hacen tus números y los documentos que te pide la inspección.»** | Es el ángulo libre que deja el competidor (§7.2, H1 y H5): **no vendemos «te explico», vendemos los entregables** |
| **Promesa honesta** | **«No te enseña a hacer pasteles. Te dice qué decidir y en qué orden: si ese local sirve, cuánto necesitas de verdad, qué te pide cada administración, cuánto tienes que cobrar y si aguantas Reyes.»** | Responde de frente a las objeciones 1, 3 y 5 |
| **Declaración en negativo, arriba y no en la FAQ** | **«Esto no es un recetario ni un curso de técnica pastelera, y no sustituye al proyecto técnico visado.»** | Copiado de lo que hace bien el competidor. **Corta devoluciones** |
| **Description** (~155) | **«Para quien va a abrir una pastelería en España: viabilidad del local, CAPEX por escenarios, licencias y registro sanitario, escandallo con mano de obra, campañas y plan financiero. 20 capítulos y 10 Excel.»** (recortar a 155) | — |
| **Keywords** (para el cuerpo y los H2, **no para el slug ni el title**) | montar una pastelería · obrador de pastelería · requisitos obrador pastelería · obrador en casa · obrador compartido · licencia de obrador · maquinaria de pastelería · escandallo de pastelería · plan de negocio pastelería · traspaso de pastelería | ⚠️ **Usar «artesanal», no «artesana»** (480 vs 260). **Nunca «dulcería» como sinónimo** |
| **Frase de frontera para la landing** | *«El Kit de Tareas te dice qué hacer cada día cuando ya has abierto. Esta guía es todo lo que hay que decidir antes.»* | Va **arriba**, no en la FAQ |

### 12.3 Límite del copy, escrito en la primera pantalla

**El marco legal explicado es el ESPAÑOL.** Las herramientas tienen todas las casillas editables, el vocabulario lleva su equivalencia LATAM en la primera mención y el método viaja entero — pero **no se promete cobertura normativa de ningún otro país**. Se dice en el hero, en la FAQ y en el email. Y, según la regla de John del 5-sep, la FAQ **ofrece la adaptación como servicio** para quien esté fuera de España, en vez de fingir que el producto ya la trae. **Sin siglas españolas en los titulares** (RGSEAA, APPCC y BOE van dentro, no en el hero).

---

## 13. Canales, interenlazado y piezas de captación

### 13.1 Entrantes (regla capital: cero páginas huérfanas)

| Origen | Acción | Fichero |
|---|---|---|
| **Hub `/productos-digitales`** (Astro **y** SPA) | Tarjeta real con badge «Nuevo» + **retirar la entrada de `comingSoon` en LOS DOS ficheros**, o quedarán la tarjeta real y la de «Próximamente · Mayo 2026» a la vez. Los contadores del hero se recalculan solos | `src/pages/ProductosDigitales.tsx:942` · `astro-site/src/components/pages/ProductosDigitalesHubPage.astro:957` |
| **Buscador del hub** | **Un alias nuevo**, porque el índice se construye con `indiceBusqueda([name, description, features, tags, tagLabel, slug, ALIAS_BUSQUEDA[slug]])` y normaliza sin acentos: `"/guia-pasteleria-obrador": "abrir montar una pasteleria obrador reposteria pasteleria en casa cake design tartas por encargo vitrina licencia maquinaria traspaso"`. **Verificado por mí: hoy `sinonimos-buscador.json` no menciona pastelería, obrador ni montar**, así que no se dispara el gate de grupos huérfanos | `astro-site/src/lib/sinonimos-buscador.json` |
| **3 posts con banner FIJADO** (sustitución quirúrgica) | Ver §13.2 | `astro-site/src/content/blog/es/` |
| **5 posts más con enlace contextual** | Los otros 5 del universo de 8 | Ídem |
| **3 páginas `/usos/rol/`** | Añadir `'guia-pasteleria-obrador'` a los `productIds` de **`pasteleria-obrador` (:2698)**, **`repostero-pastelero` (:2034)** y —si entra la variante— **`cafeteria-brunch` (:2217)**. Enlace **bidireccional** | `src/data/use-cases-content.es.ts` |
| **`footerLinks` cruzados** | Desde `guia-panaderia-obrador.ts`, `kit-tareas-pasteleria`, `kit-escandallos` y `pack-appcc` | `astro-site/src/data/productos/**` |
| **Rotación general de banners** | Entrada **48** en `products-catalog.ts` → `fase8e-banners-corpus.py` lo reparte solo por los 325 posts | — |
| **Lista de compradores (Resend)** | Broadcast propio (§13.3) | — |
| **Plataforma (Pickaxe)** | Agentes **«Pastelero Consultor Pro»**, **«Pastelería Creativa»** y **«Hotel Pastry & Bakery Pro»** (⚠️ **el bloque de hotelería va en inglés siempre**). **Comprobar los nombres contra `fase8c-agentes/catalogo-hub.json` antes de escribirlos** | — |

**Salientes de la landing:** `kit-tareas-pasteleria` (12 €), `kit-escandallos` (12 €), `pack-appcc` (14 €), Guía Food Cost (55 €), `plan-negocio-panaderia` (35 €) y la plataforma — con `utm_source=landing&utm_medium=cross-sell` para poder medir quién compra dos. ⚠️ **`guia-panaderia-obrador` NO entra en el cross-sell hasta que entregue lo que promete** (decisión D2).

### 13.2 Los 8 posts del universo y qué banner sustituye a cuál

Extraídos por mí, banner a banner, de `astro-site/src/content/blog/es/`. **Los 8 tienen exactamente 3 banners: hay que SUSTITUIR, no añadir.**

| Post | Menciones | Banners hoy | Sustituir |
|---|---|---|---|
| `libreria-de-prompts-para-pastelero-consultor-pro-ai` | **258** | kit-tareas-pasteleria · kit-plan-financiero · kit-escandallos | **`kit-plan-financiero`** → el plan financiero está **dentro** de la guía |
| `libreria-de-prompts-para-pasteleria-creativa-ai` | 110 | kit-tareas-pasteleria · kit-escandallos · pro-prompts-ebook | **`pro-prompts-ebook`** (el menos ligado al negocio de pastelería) |
| `ai-chef-pro-un-chatgpt-para-la-pasteleria-profesional-usos-y-aplicaciones` | 72 | kit-tareas-pasteleria · kit-tareas-panaderia · **guia-restaurante-gastronomico** | **`guia-restaurante-gastronomico`** → **es el peor encaje de los ocho**: un post de pastelería vendiendo una guía de restaurante gastronómico |
| `libreria-de-prompts-para-panadero-consultor-pro-ai` | 90 | ⚠️ **kit-tareas-pasteleria** · kit-plan-financiero · kit-escandallos | **NO es para el 48.** Es un **miswiring**: post de panadería con el kit de pastelería. El hueco natural es `kit-tareas-panaderia` y `guia-panaderia-obrador` |
| `libreria-de-prompts-para-panaderia-creativa-ai` | 55 | ⚠️ **kit-tareas-pasteleria** · kit-escandallos · pro-prompts-ebook | **NO es para el 48.** Mismo miswiring |
| `libreria-de-prompts-para-chocolateria-creativa-ai` | 45 | kit-tareas-chocolateria · kit-escandallos · pro-prompts-ebook | Sólo si la guía cubre bombonería |
| `libreria-de-prompts-para-chocolatero-consultor-pro-ai` | 40 | kit-tareas-chocolateria · kit-plan-financiero · kit-escandallos | Ídem |
| `ia-para-panaderias` | 18 | kit-tareas-panaderia · kit-plan-financiero · **plan-catering-tematico-eventos** | **NO es para el 48**: el hueco es de `guia-panaderia-obrador` (catering temático en un post de panadería no encaja) |

**Ganancia neta para el 48: 3 banners** en los tres posts de pastelería.

⚠️ **Herramienta:** `fase8e-banners-corpus.py` **sólo inserta, no sustituye**. Para cambiar un banner ya publicado hace falta una pasada quirúrgica del estilo `fase8h` (la que se usó con el Manual del Chef Ejecutivo), **con gate de reversibilidad byte a byte**. **PROHIBIDO reejecutar `fase8c-libreria-assemble.py`**: reconstruye el cuerpo desde el `.txt` de bridge y **pisa las ediciones manuales**.

⚠️ **A la lista `NUNCA` del script:** `kit-tareas-pasteleria`, `kit-escandallos`, `pack-appcc` y `guia-food-cost-ingenieria-menu` — son cross-sell de la guía; sustituirlos sería quitarse ventas propias (regla heredada de la D16 del Manual del Manager).

### 13.3 Resend: dónde cabe el correo de lanzamiento, y la trampa

Cola documentada en `CALENDARIO-V2-SEMANAL.md` §0-ter (regla de John del 5-sep: **último `scheduled_at` + 5 días, 08:00 UTC / 10:00 Madrid**), verificada por mí:

| Fecha | Correo | Estado |
|---|---|---|
| 14-sep | Manual del Chef Ejecutivo (lanzamiento) | programado |
| 19-sep | Bar-restaurante 2.1 | programado |
| 24-sep | Cafetería 2.2 | programado |
| 29-sep | Tapas-bar 2.2 | programado |
| 4-oct | Panadería 2.2 | programado |
| 9-oct | Food truck 2.2 | **BORRADOR** (Resend no admite > 30 días vista) |
| **14-oct** | **← hueco natural de la Guía de Pastelería** | libre |

⚠️ **El 14-oct está a 34 días del 10-sep, fuera del tope de 30 días de Resend: no se puede programar todavía.** Queda como borrador y se programa a partir del **14-sep**. Y al recrear cualquier correo: **leer el asunto ANTES de borrar** y `json.loads(strict=False)` — la lección del 6-sep, en la que se borraron cuatro correos a ciegas.

> **Alternativa que merece plantearse (decisión D12):** un lanzamiento **anunciado desde mayo con cuatro meses de retraso** compite mal con un aviso de versión. **El precedente existe y es de hace cuatro días:** la D28 del Manual del Chef Ejecutivo **adelantó el lanzamiento y desplazó un hueco las cinco actualizaciones de planes**, con este argumento literal: *«un lanzamiento anunciado desde mayo vende más que un aviso de versión»*. Si se repite, la pastelería saldría el **19-sep** o el **24-sep** y todo lo demás corre un hueco.

### 13.4 Las piezas de captación de blog que salen de este research

**No son este producto y no bloquean el lanzamiento**, pero salen gratis y son las **únicas cuatro SERP del nicho sin local pack, con AI Overview y con PAA de apertura**. Se escriben con `bridge.py` (regla capital: los productos no, el blog sí).

| # | Pieza | Volumen ES | Por qué | Riesgo |
|---|---|---|---|---|
| **1** | **El obrador compartido: cómo abrir una pastelería sin montar obrador propio** | `obrador compartido` **50** | 🟢 **El hueco más limpio del research.** SERP **100 % institucional** (ACSA/Gencat, Diputació de Barcelona, grupos LEADER, `cooccio.com`) y **cero piezas comerciales**. Nadie lo explica como vía de entrada con CAPEX mínimo | Bajo |
| **2** | **¿Es legal vender repostería desde casa en España? Requisitos, licencia y multas** | ~**120/mes agregado** (30+30+20+20+20) | El clúster mejor definido, con PAA listo para FAQ: «¿Es legal…?», «**¿Cuál es la multa por vender comida sin permiso en España?**». **Y es donde podemos decir lo que nadie dice: la tarta de nata desde casa no es legal** (art. 13.8) | ⚠️ **Medio-alto: `pasteleriaparatodos.com` ocupa la POSICIÓN 1** con un producto de pago de 357 €, más `escueladeobradores.com`. **No es un hueco vacío: es un hueco disputado por productos, no por medios** |
| **3** | **Cuánto cuesta montar una pastelería en España: desglose real** | 10+10+10, **pero es PAA inyectado** en SERP de 2.900 y de 40/mes | Volumen ridículo, conversión altísima: quien busca esto compra. Y nuestro diferencial es dar **la hipótesis** que ninguna de las 11 fuentes gratuitas declara | Bajo |
| **4** | **Franquicia de pastelería vs marca propia: qué te dan y qué te quitan** | `franquicias de pasteleria` **40** + `franquicia pasteleria` **40** (el término tiene ~80/mes repartido en dos grafías) | Intención comercial confirmada | ⚠️ SERP de **directorios verticales con años de autoridad**. Rankear es improbable; el valor es de **contenido de decisión** para quien ya nos lee |

> ❌ **Anti-recomendación (repetida aquí porque es donde se decide):** **NO escribir «Pastelería sin gluten» (2.400), «Cafetería pastelería» (2.900) ni «Confitería» (9.900)** como piezas de captación. Los tres volúmenes son de consumidor comprando producto, con SERP de 12 resultados de local pack.

---

## 14. FAQ de COMPRA — 12 preguntas

Las de **oficio** («¿cómo se hace un roscón?», «¿qué escuela de pastelería elijo?») y las de **empleo** («¿cuánto cobra un pastelero?») **quedan fuera**: no son nuestras. Estas 12 son de compra.

| # | Pregunta | Cómo se responde |
|---|---|---|
| 1 | **¿Esto no está gratis en Google?** | **La primera, por la objeción nº1 medida.** Sí, la información suelta está — y **se contradice por un factor 13**: las mismas 11 fuentes dan de 15.000 € a 200.000 € para el mismo negocio y ninguna dice de qué depende. Lo que no está en Google es **el orden de decisión y diez Excel donde metes TUS metros, TU plaza y TU carta**. Se responde con una tabla, no con adjetivos |
| 2 | **¿Me sirve si quiero empezar desde casa?** | Sí, y es donde más aporta: hay un capítulo entero y una hoja con la **lista blanca legal del art. 13** del RD 1021/2022 y el contador de los 100 kg/semana. **Y se dice lo que casi nadie dice: hay producto que NO puedes vender desde casa** (empezando por la tarta rellena de nata). Mejor saberlo antes que después de una inspección |
| 3 | **¿En qué se diferencia del Kit de Tareas Pastelería de 12 €? ¿Necesito los dos?** | **El kit te dice qué hacer cada día cuando ya has abierto** (producción, encargos, alérgenos de vitrina, temperaturas, caja). **Esta guía es todo lo que hay que decidir antes de abrir.** Si ya estás abierto, el kit te vale y esta guía no te hace falta |
| 4 | **¿Y si ya tengo la pastelería abierta?** | **Entonces éste no es tu producto**, y se dice claro: lo tuyo es la Guía Food Cost, el Manual del Manager o los kits. Esta guía es **para quien AÚN no ha abierto** |
| 5 | **¿Sustituye al proyecto técnico o a la gestión de licencias?** | **No, y hay que decirlo arriba.** El proyecto técnico de un obrador cuesta **1.800-2.800 € + IVA** y la tramitación **desde 1.690 € + IVA** en Madrid: eso lo firma un técnico. Lo que hace la guía es que **llegues a esa reunión sabiendo qué pedir, qué preguntar y qué te van a cobrar** — y que no firmes un alquiler antes |
| 6 | **Mi ayuntamiento es distinto. ¿Me sirve igual?** | **Verdad, y es lo primero que dicen todos los técnicos.** No existe una guía que dé la ordenanza de 8.131 municipios. Lo que da ésta es **el marco estatal y autonómico verificado con su artículo y su enlace**, más **la lista exacta de qué preguntar en tu ayuntamiento y en qué orden**. Prometer otra cosa sería mentir |
| 7 | **¿Qué diferencia hay con la Guía de Panadería con Obrador?** | ⚠️ **Depende de la decisión D2.** Si la de panadería sigue como está, **esta pregunta NO entra en la FAQ** y la guía no la menciona. Si se arregla antes: la panadería gira sobre horno, fermentación y masa madre; la pastelería sobre **frío negativo, vitrina, encargos y campañas**, con dos bloques legales que la panadería no tiene (huevo y temperatura del producto relleno) |
| 8 | **¿Necesito el Pack APPCC si compro esta guía?** | Son cosas distintas: la guía te da **el criterio y el checklist de puesta en marcha** (qué tienes que tener el día que venga la inspección); el Pack te da **los 21 registros que hay que rellenar y firmar cada día** después. La guía **no construye ni un registro APPCC** a propósito |
| 9 | **¿Y el Kit de Escandallos?** | El kit trae el escandallo unitario de **3 elaboraciones** (tarta de chocolate, croissants, macarons). La guía trae **la carta de apertura completa de 30 referencias con el coste de la hora de obrador imputado**, que es lo que decide tu precio de verdad. **Las tres primeras coinciden a propósito**, para que no veas dos costes distintos del mismo croissant |
| 10 | **¿Los Excel funcionan en Google Sheets y en Numbers?** | Sí: nuestras convenciones **prohíben `INDIRECT`, `COUNTA`, `PMT`, `OFFSET`, `XLOOKUP`, `LET` y `LAMBDA`** justamente por eso, y no hay referencias entre libros. Todos los parámetros van en **celda verde**, sin constantes escondidas dentro de fórmulas |
| 11 | **¿Sirve si voy a abrir fuera de España?** | **El marco legal explicado es el español**, y se dice en la primera pantalla. **La estructura económica viaja entera** (CAPEX, capacidad de obrador, escandallo, punto muerto, campañas, tesorería): son celdas editables. El bloque sanitario y de licencias hay que adaptarlo — **y esa adaptación la ofrecemos como servicio** |
| 12 | **¿Qué pasa cuando cambie la normativa?** | Pago único con **actualizaciones incluidas**. Los parámetros legales viven en celda editable con su nota y su fecha, hay un **anexo normativo con fecha de corte** y un apartado que enseña a comprobar la vigencia en el BOE. **Y hay tres fechas que ya sabemos que se mueven: el SMI y el convenio caducan el 31-dic-2026, y el plazo de Madrid vence el 28-mar-2027** |

**JSON-LD:** `Product` (con `offers`, `priceValidUntil`, `availability`, `seller`) **sin `aggregateRating` ni `review`** + `FAQPage` con las 12 + `BreadcrumbList`. Se pasa `clasifica()` de `fase8d-faq-duplicadas.py` sobre la FAQ final: **cero pares PARECIDA/DEFINICION**. ⚠️ **Ojo con los pares 3/4 y 8/9**, que son los que más se parecen entre sí.

---

## 15. LISTA NEGRA, riesgos, presupuesto y decisiones

### 15.1 Cifras que NO pueden entrar en el producto

Va literalmente al `NO_COMUN` del guion como `cifras_ignorar` + `prohibido`, y el gate de coherencia de cifras de `documentos.py` lo hace cumplir.

| # | Cifra prohibida | Por qué se rechaza |
|---|---|---|
| **N-1** | «**11.729 pastelerías y panaderías en España en 2025, +2,11 % sobre 2023**» (recipok.com) | Blog **sin fuente primaria**; el INE **no publica ese desglose**. Precisión falsa: cuatro dígitos para un censo que no existe |
| **N-2** | 🚨 «**Facturación media anual por pastelería: 1,08 millones de euros**» (modelosdeplandenegocios.com) | **La más peligrosa del research.** Contradice a PS-48/57/60 por un factor de **6 a 12** (un obrador artesano factura 84.000-180.000 €/año). **Un lector que planifique sobre 1,08 M€ quiebra.** Contenido de granja de IA |
| **N-3** | «Cientotreinta grados, **franquicia de Oriol Balaguer**, 250 k€ + 30 k€ de canon» | **Refutado**: la marca es de los hermanos Miragoli y **no consta como franquicia** |
| **N-4** | «Franquicia **Manolo Bakes**, ~300.000 € de inversión» | **Manolo Bakes recompró sus franquicias y ya no franquicia en España.** Vender una inversión en una franquicia que no existe |
| **N-5** | «Chocolate cobertura 18-22 €/kg · vainilla 600-800 €/kg · frutos secos 15-35 €/kg · mantequilla 9-12 €/kg» | Sin fecha, sin formato (granel/minorista), sin proveedor. Los commodities de 2026 se mueven **±50 %** |
| **N-6** | «**68,2 % super / 12,5 % hiper / 10,6 % tienda tradicional**» presentado como reparto de la **bollería** | Es el reparto del **total de la compra alimentaria** en 2025, no de bollería (que es ~74 % / ~5,4 % especializado). **Error de atribución que exagera el peso del canal del obrador** |
| **N-7** | «**El cacao cotiza a X USD/t**» — cualquier valor puntual | **Cuatro cifras distintas para 2026** (3.300 / 4.000 / 5.000 / 6.205). Sin consenso ⇒ **sin cifra**; sólo el patrón |
| **N-8** | «Horno modular Salva, **1.499 €** sin impuestos» | Precio de un listado antiguo para un equipo cuyo fabricante **vende a presupuesto**. Induciría a presupuestar un horno de pisos por el precio de uno de convección |
| **N-9** | «Mercado sin gluten **+18 %** entre 2022 y 2025» | Un proveedor de pan sin gluten dando el tamaño de su propio mercado, sin citar estudio |
| **N-10** | «Los pasteleros esperan vender un **4 % más** por Todos los Santos» | La página devolvió **403** y no se pudo fechar. Una cifra de campaña sin año no vale nada |
| **N-11** | Cualquier «**ticket medio de pastelería**» | **No existe dato público.** Va como parámetro en celda verde **con el valor por defecto declarado explícitamente como supuesto**, y la guía enseña a medirlo con el TPV en dos semanas |
| **N-12** | Cualquier «**reparto de ventas por día de la semana**» | **No se encontró fuente.** Mismo tratamiento que N-11 |
| **N-13** | «**12.751 empresas y 1.789 M€** en el CNAE 4724» presentado como censo | Sólo cubre sociedades que depositan cuentas: **excluye a los autónomos, que son la mayoría del sector** |
| **N-14** | «**4 €/ración cuando el coste real mínimo son 6,71 €**» | Apareció sólo en el resumen de un hilo que devolvió **403**. **No verificado** |
| **N-15** | Los **umbrales de 7,5 kW / 10 kW / 55 m² / Anexo III.2** de Habitissimo | Son respuestas de técnicos en un foro **de hace 8-11 años**. Valen como retrato de la duda, **jamás como regla vigente** |
| **N-16** | «**846 M€** en 2024» y «más aperturas que cierres en el 1S-2025» (recipok) | Sin citar organismo |
| **N-17** | Los costes de `lahostelera.com` (proyecto 5.000 €, obra 81.000 €, equipamiento 46.000 €, marketing 5.000 €, total 137.000 €) **como dato general** | **La página no publica fecha** y es el presupuesto de **un** caso (90 m², Gijón). Entran **sólo** como «escenario publicado de La Hostelera», nunca como «lo que cuesta montar una pastelería» |
| **N-18** | Cualquier cifra de **franquicia** como dato auditado | Los portales **se contradicen entre sí dentro del mismo dato** (Granier 83.000 vs 180.000 € con canon idéntico). Valen como «orden de magnitud publicado por el portal X en la fecha Y» |

### 15.2 Afirmaciones normativas falsas o caducas, y errores de método

**Normativas (todas vivas en la SERP medida):**

- «Necesitas el **RGSEAA** para abrir tu obrador» — **no**, si vendes al consumidor final: es comunicación autonómica no habilitante (PA-01).
- «Con vender **poco** a otras tiendas no pasa nada» — los tres requisitos del art. 3 son **acumulativos**, y los 500 kg **incluyen el mostrador** (PA-02).
- «Los alimentos con huevo, a **8 °C y 24 horas** por el **RD 1254/1991**» — **derogado el 22-dic-2022**; y para un producto de pastelería relleno la temperatura es **4 °C**, no 8 (PA-12, PA-14).
- «Hay que sacarse el **carnet de manipulador**» — **no existe desde el 20-02-2010** (PA-11).
- «Puedes montar tu **negocio de tartas** desde casa» — sólo repostería **estable a temperatura ambiente**; prohibido congelar; máximo 100 kg/semana (PA-29).
- «**Verifactu** es obligatorio en 2026» — **1-ene-2027** (IS) y **1-jul-2027** (resto).
- «Las temperaturas las fija el **RD 3484/2000**» y «el anisakis, el **RD 1420/2006**» — **los dos derogados** el 22-dic-2022.
- «Se aplica el **RD 2207/1995**» (lo que sigue citando `emprendedores.es`) — superado por el paquete de higiene comunitario.
- «Poner **"elaboración propia"** es obligatorio» / «puedo ponerlo si fraccionó o envaso producto de otro» — **es voluntario** y esos supuestos están **expresamente excluidos** (PA-17).
- «Con harina de arroz ya puedo poner **sin gluten**» — es un umbral analítico de **20 mg/kg** (PA-23).
- «Podrás llamarte **artesano**» — depende de la CCAA; en Cataluña hay **carné y acreditación**, en Madrid sólo hay un **proyecto** de decreto (PA-26).
- «La **Ley 1/2025** te obliga a un plan de prevención» — **no** si eres microempresa o ≤1.300 m² (PA-31), **y su art. 6 no era exigible hasta el 2-abr-2026**.
- «Una pastelería tiene que **pedir permiso para abrir en domingo**» — tiene **libertad horaria por ley** (PA-39).

**Errores de método:**

- **Dar un número de inversión en vez del modelo que lo produce.** Es lo que hacen las 11 fuentes gratuitas y por lo que se contradicen en un factor 13.
- **Presentar «margen 65-70 %» y «food cost <30-35 %» como dos reglas.** Son la misma.
- **Mezclar precios CON y SIN IVA en la misma tabla de CAPEX** → desviación del 21 %.
- **Mezclar la cotización de commodity de la mantequilla con el precio de la mantequilla de hoja 82-84 %** que compra un obrador.
- **Confundir el reparto de canal del total alimentario con el de bollería** (N-6).
- **Usar «dulcería» como sinónimo de pastelería en el copy LATAM** — en México es la tienda de golosinas.
- **Escribir «artesana» en vez de «artesanal»** — deja fuera la mitad del término.
- **Copiar redacciones legales de otros kits sin verificar.** Precedente medido: `kit-tareas-sushi-bar/03` y `kit-tareas-marisqueria/03` citan el **RD 1420/2006 derogado**, y el de marisquería además da **−20 °C/7 días** (criterio de la FDA) donde lo español son **24 h**. La guía de pastelería no toca anisakis, así que **no hereda el defecto — pero la lección aplica a todo el bloque legal**.
- **Prometer tráfico SEO.** 10-20 búsquedas/mes para la intención de apertura.

### 15.3 Riesgos, incluidos los de caducidad

| # | Riesgo | Evidencia | Mitigación |
|---|---|---|---|
| **1** | 🔴 **La línea de 65 € entrega un 5-13 % de lo que promete** | Medido por mí: 6 de 8 PDF de la franja son de **1 página**; el gastronómico de 85 € da **10 págs de 119 prometidas** | Decisión **D2**. Mientras no se arregle, **el copy y el `emailBody` de pastelería no mencionan a ninguna hermana de la línea** |
| **2** | **Competidor de pago en la posición 1 de nuestras mejores SERP** | `pasteleriaparatodos.com/obrador-en-casa/` (357 €) es **el nº 1 de «montar una pasteleria en casa»**, el 2.º de «requisitos…» y el 3.º de «vender reposteria desde casa» | **No competir en «te explico cómo montar»**: vender el **dossier de entregables** (§7.2, H5). Y en la pieza de captación nº 2, entrar por donde ella no puede: **la norma citada** |
| **3** | **Canibalización con `kit-tareas-pasteleria` (12 €)** | El kit resuelve producción, encargos, alérgenos de vitrina, temperaturas y caja | Las **6 reglas R1-R6 del §8.1**, verificadas hoja a hoja, y el cap. 01 con la tabla «qué incluye el pack / qué es cross-sell» |
| **4** | **Un error en el bloque legal cuesta más que un error de food cost** | Sanciones de seguridad alimentaria (Ley 17/2011: hasta **600.000 €** y cierre de 5 años) y de desperdicio (Ley 1/2025: hasta **500.000 €**, verificado literal) | **Verificador legal independiente obligatorio** (agente sonnet, patrón del verificador fiscal de la Guía Food Cost) **antes** de escribir los caps. 9, 10 y 19, **contra las fuentes primarias, no contra L3** |
| **5** | **Tres verificaciones normativas siguen abiertas y son de capítulo** | V-02 (art. 91 IVA), V-03 (art. 30 del RD 1086/2020), V-05 (¿la pastelería que envasa es «productor de producto»?) | **No escribir esos epígrafes sin cerrarlas.** El método barato ya está probado: **PDF consolidado del BOE + `pypdf`** |
| **6** | **Cinco dolores centrales con corpus sesgado o sin voz** | Reddit, YouTube, Facebook, Forocoches, Burbuja y Mediavida **inaccesibles**; cero reseñas negativas del nicho | **Pedirle a John 5-10 minutos de voz** sobre precios, mermas de vitrina, encargos y el madrugón (decisión **D13**) |
| **7** | **Vender profundidad LATAM que no tenemos** | El bloque legal es **exclusivamente español**; y la demanda LATAM medida es de 10/mes | Casillas editables + vocabulario con equivalencia + **la landing lo dice en la primera pantalla** + la FAQ ofrece la adaptación como servicio |
| **R-01** | **SMI 2026 (RD 126/2026)** | Todo el libro 10 y los ejemplos de nómina | **Caduca el 31-dic-2026.** Vive en celda verde y en el anexo fechado, nunca en la prosa |
| **R-02** | **Revisión 2026 del convenio de Madrid** | Las 6 filas de la tabla salarial | **Caduca el 31-dic-2026** |
| **R-03** | **Decreto 26/2026 de Madrid: transitorio de 1 año** | La frase «tienes de plazo hasta…» | **Vence el 28-mar-2027.** Es oro comercial **con fecha de caducidad** |
| **R-04** | **RD 1055/2022 art. 9.4** — 1 referencia de bebida reutilizable en <300 m² | Un requisito que hoy es futuro pasa a presente | **1-ene-2027** |
| **R-05** | **Verifactu** | El capítulo de TPV y facturación. **Ya se ha aplazado dos veces**: probabilidad real de una tercera | 1-ene-2027 / 1-jul-2027 |
| **R-06** | **Registro horario digital** | La recomendación de herramienta | Estimado 2027 |
| **R-08** | **RD 496/2010** — norma de calidad de confitería y pastelería | Definiciones legales y denominaciones de venta. **Es de 2010 y el pan ya se actualizó en 2019** | Riesgo medio, sin fecha |
| **R-09** | **Art. 91 de la Ley 37/1992 (IVA)** | Tipos por familia de producto | Cada Ley de Presupuestos |
| **R-10** | **Registros sanitarios autonómicos** | El cuadro por CCAA. **Madrid legisló en 2026 y Valencia en 2025: las CCAA se están adaptando al RD 1021/2022 ahora mismo** | Continuo. En los próximos 24 meses saldrán más decretos |

> **Consecuencia de diseño, no de contenido:** todo lo de R-01 a R-10 debe vivir en **celda de parámetro o en un anexo fechado**, nunca cosido en la prosa de un capítulo. Un «**Anexo normativo — actualizado a <fecha>**» de 6-8 páginas permite reeditar el producto cambiando un fichero. **Decisión D7.**

### 15.4 Presupuesto estimado por fase

| Fase | Trabajo | Modelo | Estimación |
|---|---|---|---|
| **A — research** (esta sesión) | 6 lentes + esta síntesis | opus / sonnet | **Cerrada.** ~1,5-2,0 M |
| **A2 — verificación + SPEC + guion** | Cerrar V-02, V-03, V-05 con PDF del BOE · SPEC con las decisiones firmadas · `guion_guia_pasteleria_obrador.py` de 20 caps con `puntos_por_epigrafe` · `verificar_guion.py` en verde | opus (SPEC) + sonnet (guion) | **1,5-2,0 M** |
| **B1 — los 10 libros** | `datos_ejemplo.py` (opus) → 4 constructores (libros 1-2-3 · 4-5 · 6-7 · 8-9-10) → 1 refutador opus de los xlsx → fixer sonnet → `inject_cache` + verificación `data_only` + `mapa-*.json` | opus + sonnet | **2,5-3,5 M** |
| **B2 — documentos** | `dump_prompts.py` → **~44 redactores sonnet** (20 caps × 2 bloques + 2 bonus) con `check_bloque.py` → **1 verificador legal sonnet contra fuentes primarias** (caps. 9, 10, 19) → `documentos.py` ensambla → 1 refutador opus → fixer → gates (páginas con PyMuPDF, no latinos, coherencia de cifras, paridad PDF↔DOCX, metadata `author='AI Chef Pro'`) | sonnet en paralelo + opus | **5,5-7,0 M** |
| **C — capa de producto y lanzamiento** | Landing sobre `GuiaData`, dashboard (Guía 2 · Herramientas 10 · Bonus 4), 4 functions + config, Payment Link (John), catálogo 48, hub ×2 con el `comingSoon` retirado, alias del buscador, changelog, imágenes, sustitución quirúrgica de 3 banners, `productIds` de 3 páginas de rol, `robots-gate.py`, `whatsapp-gate.py`, `gate-flujo-postpago.py`, `censo-entregables.py --fail`, gate LIVE, broadcast en Resend | sonnet + Fable en lo crítico | **1,0-1,5 M** |
| **TOTAL** | | | **12,0-16,0 M** |

🔴 **Aviso explícito, y es la decisión D14:** el techo de John es **~15 % de la cuota semanal** y «una semana normal debe quedarse por debajo de 1,5 M». Los cuatro productos nuevos anteriores ya lo rompieron (**9,7 / 10,5 / ~17 M**) y el del Chef fue **una sesión dedicada autorizada expresamente**. **Este producto es el más caro de la serie por entregables** —10 libros frente a los 7 del Chef, y **tres sin molde previo**— aunque mi estimación queda ligeramente por debajo de la de L6 (13,5-17,5 M) porque **el pipeline ya no necesita arreglos**: `repartir_puntos()` está commiteado y `documentos.py` no se toca. **No arrancar la construcción sin luz verde explícita, y probablemente en dos sesiones**: (A2+B1) y (B2+C).

### 15.5 Decisiones que sólo puede tomar John

| # | Decisión | Mi recomendación | Su coste |
|---|---|---|---|
| **D1** | **Precio: 65 €, 85 € o 55 €** | **65 €.** Paridad con la hermana directa, coherencia con el precedente del Chef Ejecutivo (que salió a 65 € pudiendo salir a 55) y hueco de mercado limpio entre 49 € y 357 € | Renunciamos al margen que 10 libros justificarían. **85 € sería defendible con el recuento en la mano, pero choca con la Guía Gastronómica de 85 € mientras ésta entregue 10 páginas de 119** |
| **D2** | 🔴 **La línea rota. No es una hermana: son 6 de 8 productos de la franja 65-85 €** (medido por mí). ¿Se arregla **antes**, **después**, o el copy de pastelería **no menciona a ninguna** hasta que estén? | **La tercera: no mencionar ninguna guía de la línea en el copy ni en el `emailBody`**, y cruzar sólo con `kit-tareas-pasteleria`, `kit-escandallos`, `pack-appcc` y Food Cost. **El calendario ya tiene el arreglo planificado**: S4 casual, S5 mexicano, S6 peruano, S7 japonés, S8 nikkei, **S9 panadería (26-oct–1-nov)** | Lanzar sin cross-sell de línea deja ventas cruzadas sobre la mesa. La alternativa —arreglar antes— **retrasa el lanzamiento meses**, porque son 6 productos |
| **D3** | ¿El producto 48 se lanza **antes** o **después** de arreglar la línea? | **Antes.** Es el único de la franja que nacería entregando lo que promete, y **lleva 4 meses anunciado**. Además marca el listón para los arreglos | Durante unas semanas convivirán en el hub una guía llena y seis vacías |
| **D4** | **Alcance de las variantes.** ¿Entran las 11 (o al menos las 6 del brief) o el producto se centra en obrador+tienda? | **Obrador+tienda como caso central (el juego de datos «La Clara»), con capítulo propio para el obrador en casa** —es el segmento con más búsqueda y donde podemos corregir a todo el mundo— y las demás como **desviaciones tabuladas** en el cap. 01 y en el libro 6 | La **pastelería-cafetería** abre un frente entero (art. 30 del RD 1086/2020, otro convenio, otro IVA) y puede añadir 1,5-2 M de tokens. **Recomiendo tratarla como variante, no como segundo caso modelado** |
| **D5** | **Canibalización con `kit-tareas-pasteleria`:** ¿confirmas las 6 reglas R1-R6 (la guía NO repite plan de producción, encargos, alérgenos de vitrina, temperaturas, calendario de picos ni fichas de perfil) y hace upsell al kit? | **Sí.** Es el reparto más limpio del catálogo: **el kit resuelve operar, la guía resuelve abrir** | Ninguno. La guía es autosuficiente en su eje |
| **D6** | **Cobertura territorial de los cuadros por CCAA.** ¿Las 4 de ejemplo (Madrid, Cataluña, Andalucía, C. Valenciana) o las 17? | **Las 4, declaradas como ejemplos**, más «cómo encontrar el tuyo» | Las 17 son ~2 días más de verificación y **multiplican el coste de mantenimiento**: las CCAA se están adaptando al RD 1021/2022 ahora mismo (R-10) |
| **D7** | **¿Anexo normativo fechado como pieza separada** o integrado en el cuerpo? | **Separado.** Permite reeditar cuando caduquen el SMI, el convenio, Verifactu o el plazo de Madrid **cambiando un fichero**, no capítulos | Una pieza más que mantener (pero mucho más barata que reescribir capítulos) |
| **D8** | **¿Segunda pasada de verificación ANTES del guion** (V-02 IVA, V-03 comidas preparadas, V-05 envases) o se escribe y se refuta después? | **Antes, y es barata**: los tres se cierran con `curl` del PDF consolidado + `pypdf`, que es exactamente como cerré V-01 en dos minutos | ~0,2 M de tokens y media hora. **Escribir primero y refutar después sale mucho más caro** |
| **D9** | **La objeción «mi ayuntamiento es distinto» no tiene respuesta perfecta.** ¿Se asume explícitamente en la ficha que la guía da el MAPA de trámites y no la ordenanza municipal? | **Sí, y arriba.** Es lo primero que dicen todos los técnicos citados; fingir lo contrario genera devoluciones | Suena menos ambicioso. **Vende mejor que una promesa que no se cumple** |
| **D10** | **Garantía de devolución.** La competencia directa publica «devolución íntegra a 30 días sin condiciones» **en portada** | **Evaluarlo para este producto y para el resto del catálogo** | Es una decisión de negocio, no de research. La FAQ 12 asume hoy la política actual |
| **D11** | **¿Se enlaza a `Hosply.pro`** (marca hermana, directorio de proveedores HORECA) desde el capítulo de proveedores, con UTM? | **Sí, con UTM.** Encaja de forma natural y es tráfico para una marca del grupo | ⚠️ **Comprobar antes el TLS**: `ingredientsindex.pro` tiene el certificado roto y 62 posts del blog enlazan a un aviso de seguridad. **Verificar que Hosply no está igual** |
| **D12** | **Slot de Resend.** ¿Se deja como **borrador para el 14-oct**, o se **adelanta el lanzamiento** (19-sep o 24-sep) desplazando un hueco las actualizaciones de planes? | **Adelantarlo**, con el precedente literal de la D28 del Chef Ejecutivo (6-sep): «un lanzamiento anunciado desde mayo vende más que un aviso de versión» | Desplaza cinco correos un hueco. **Es exactamente lo que ya decidiste hace cuatro días** |
| **D13** | **¿Nos das 5-10 minutos de voz** sobre precios (el miedo a subir), mermas de vitrina, encargos y el madrugón? | **Sí.** Es el hueco declarado de L5 (Reddit, YouTube y foros bloqueados) y **tu experiencia es la fuente más autorizada que existe** para llenarlo | 10 minutos tuyos |
| **D14** | **¿Se parte la construcción en DOS sesiones** (A2+B1 · B2+C)? | **Sí.** 12-16 M no caben en una semana bajo el techo del 15 % | Alarga el lanzamiento una semana. **Decidirlo antes, no a mitad** |
| **D15** | **Los tres defectos colaterales de dos líneas.** (a) La página de rol `panadero` (`:1153`) vende `kit-tareas-pasteleria` en vez de `kit-tareas-panaderia`. (b) `guia-panaderia-obrador` **no aparece en ninguna** de las 51 páginas de rol. (c) **Dos posts de panadería llevan `kit-tareas-pasteleria` como primer banner** | **Arreglar (a) y (b) en el mismo commit** (son dos líneas). **(c) se arregla en la misma pasada quirúrgica de banners** que hace falta para el 48 | Ninguno. Es trabajo que ya hay que hacer |
| **D16** | **El kit infravendido.** `kit-tareas-pasteleria` entrega **15 xlsx** y el hub dice «**9 checklists**» — y esa frase aparece **6 veces** en el fichero, no una | **Actualizar la descripción de pastelería en los dos ficheros del hub** al tocarlos para el 48; el resto de la familia, a una sesión impar | Ampliar a las 6 sería salirse del alcance de esta sesión |
| **D17** | **Cripto.** ¿El 48 nace con NOWPayments activado aunque el pago real de prueba siga pendiente? | **Sí** (regla del 6-sep). Si para entonces se aplicó la réplica a los 47 y `CRYPTO_PRODUCTS=all`, no hay que hacer nada | Ninguno |
| **D18** | **Nombre.** ¿«Cómo Montar una Pastelería» como H1 + «Guía Pastelería con Obrador» como nombre de catálogo, o se unifican? | **Los dos**, como propone L2: el titular es la promesa publicada; el nombre de catálogo calca al hermano | Dos nombres para lo mismo exige cuidado en el hub y en el footer (§12.1) |

---

## 16. Lo que este research NO pudo verificar (y lo que SÍ comprobé yo)

**L1 — competencia**
- **Amazon.es bloqueado** (contenido vacío + HTTP 500): el censo de libros está **incompleto por construcción**.
- **Paraninfo (403), Certicalia (403), hellocash (sin cuerpo), Escuela Tábatha, EPGB y ESAH sin precio publicado.** Los precios de Paraninfo vienen de `todostuslibros.com` (precio de tapa).
- **Los precios de Hotmart no son públicos** sin llegar al checkout: 3 infoproductos sin precio.
- **El censo es 100 % es-ES.** No se midió la oferta LATAM.

**L2 — SERP y demanda**
- **No se pudo leer el TEXTO de los AI Overviews**: DataForSEO los devuelve como `asynchronous_ai_overview: true` con `markdown: null`. **Se sabe en qué 4 consultas existen, no qué dicen ni a quién citan.** Requiere el endpoint asíncrono (coste extra) o inspección manual.
- **DataForSEO devuelve `None`, no `0`**, para keywords sin dato. **`None` ≠ cero búsquedas.**
- **Bug de herramienta GSC con riesgo de conclusión falsa:** `get_search_by_page_query` devolvió «No search data found» para `/guia-panaderia-obrador` mientras `get_advanced_search_analytics` con `page contains` devuelve 2 clics / 35 impresiones. **Fiarse del primero habría hecho concluir que la landing hermana no existe en Google.**

**L3 — normativa**
- **V-02 (art. 91 del IVA), V-03 (art. 30 del RD 1086/2020), V-04 (articulado del RD 496/2010), V-05 (RD 1055/2022, «productor de producto»), V-06 (venta online a toda España) y V-07 (decretos valenciano y catalán) siguen ABIERTAS.** Ninguna puede entrar en el producto tal cual está.
- **`noticias.juridicas.com` y `supercontable.com` dieron error de certificado TLS**; la sede de la AEAT, 404.
- **Bloques enteros sin investigar:** ruido y contaminación acústica (PA-42), horno de gas / RITE (PA-08), DB-SUA de accesibilidad.

**L4 — sector y equipamiento**
- **`servicioswcf.ine.es` no resuelve DNS**; `pasteleros.org` (escala salarial 2026), `andaluciainformacion.es` y `makro.es` dieron **403**; Iberinform/eInforma/Axesor son de pago; **el PDF del MAPA 2025 (28,7 MB) no se abrió por la restricción térmica**.
- **21 proveedores del encargo NO verificados** y **11 casos de oficio sin cifras públicas**.
- **No existe dato oficial de «nº de pastelerías en España»**, ni **ticket medio de pastelería**, ni **reparto de ventas por día de la semana**.

**L5 — voz del cliente**
- **Reddit bloqueado por completo** para el user-agent; **comentarios de YouTube inaccesibles** (JavaScript); Facebook e Instagram requieren sesión; **Forocoches, Burbuja, Mediavida, fororeposteria y dianaverdu dieron 403**.
- **Cero reseñas negativas de un producto formativo del nicho.** Las encontradas son de plataformas genéricas de cursos y se descartaron a propósito.
- **Dos dolores del brief sin evidencia:** mermas de vitrina y maquinaria de segunda mano.
- **Un comentario llegó traducido al inglés** por la herramienta: se reporta como paráfrasis, nunca como cita.

**L6 — assets**
- ❌ **Ampliado y corregido por mí:** midió sólo la guía de panadería. **Son 6 de 8 productos de la franja 65-85 €** (verificación 1).
- ❌ **Corregido por mí:** daba `documentos.py` por **sin commitear**. Está en `3c1444d` (verificación 2).
- ❌ **Ampliado por mí:** el universo de blog son **8 posts, no 6** (verificación 5), y el miswiring del panadero está **también en el blog** (verificación 6).
- **Ninguna fórmula de los 10 libros se ha verificado con pycel**: son diseño, no ficheros.
- **No se abrió producción ni se corrió ningún gate LIVE** (no hay `dist/` y la regla térmica prohíbe builds locales): la afirmación sobre `robots.txt` es por **lectura de la regla**, no por simulación.
- **No se abrió el panel de Resend**: la cola sale del calendario escrito, no de la API.

**Verificaciones propias de esta síntesis (lo que SÍ comprobé)**
- ✅ **47** productos en `products-catalog.ts`, **47** en `payment-links.ts`, **47** en `product-prices.ts` · escalera de precios completa parseada · ✅ `robots.txt` con `guia-*` en los **5 bloques** · ✅ `comingSoon` en los dos ficheros del hub, y el array sólo tiene **2 entradas** · ✅ **los 10 PDF y los 24 DOCX de `dl/guia-*/` medidos con PyMuPDF y descomprimiendo `word/document.xml`** · ✅ **calibración 529-544 pal/pág** medida, no heredada · ✅ **8 posts de blog censados sobre 164** y sus 24 banners extraídos · ✅ `use-cases-content.es.ts`: **51 bloques `productIds`**, los tres de pastelería/panadería idénticos, y **`guia-panaderia-obrador` con 0 apariciones** · ✅ `git status` y `git log` de `documentos.py`; `repartir_puntos()` en `:1096`; **0 de 4 guiones usan `puntos_por_epigrafe`** · ✅ `guias-v2-research-sector.json` con **225 entradas** y los prefijos `PA-`/`PS-` **libres** · ✅ **GSC en vivo** (90 días) para toda la línea `guia-*` · ✅ `plan-financiero-panaderia.xlsx` (9 hojas) y `kit-escandallos/05-pasteleria.xlsx` (6 hojas) abiertos con openpyxl · ✅ **15 ficheros** en `kit-tareas-pasteleria` frente a «9 checklists» del hub, y el recuento de las 18 verticales · ✅ **Ley 1/2025 leída en su PDF consolidado del BOE**: D.F. vigésima, art. 6.4.c), 6.6, 6.7, art. 21 y art. 23.
- ❌ **No repetí los fetches de precios de L1 ni de L4**: las cifras de cursos, franquicias, maquinaria y proveedores se toman de esas lentes con su fecha de consulta.
- ❌ **No consulté Resend**: el hueco del 14-oct es una previsión sobre lo documentado en el calendario, **no un hueco confirmado**.
- ❌ **No verifiqué ninguna otra norma con mis propias manos** más allá de la Ley 1/2025: el resto del bloque legal se apoya en L3 con sus niveles A/B/C declarados. **Antes de escribir los caps. 9, 10 y 19, el verificador legal debe abrir el RD 1021/2022 y el Decreto 26/2026.**

**Térmica:** `istats cpu temp` medido entre tandas durante toda la sesión. Registro real: **45,0 → 45,4 → 45,4 → 44,5 → 44,8 → 44,8 → 44,6 °C**. Nunca se acercó a los 65 °C. Sin builds, sin Playwright, sin navegador; los xlsx y los PDF se abrieron **un fichero cada vez**, con `close()` y `gc.collect()`.

---

**Estado: research cerrado, PENDIENTE DEL OK DE JOHN.**

**Via: Claude Code**
