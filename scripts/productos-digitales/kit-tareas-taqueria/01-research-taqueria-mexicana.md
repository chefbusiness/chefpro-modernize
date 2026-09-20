# Research Fase 1 — «Tareas Recurrentes: Taquería Mexicana»

**Producto**: Kit de Tareas nº 20 de la familia (19 kits LIVE) · pago único · dashboard con 11 ficheros Excel
**Slug previsto**: `kit-tareas-taqueria` · **Fecha del research**: 2026-09-20 · **Máquina**: Mac (solo API, `grep`, `curl`, lecturas)

## Cómo leer las cifras

| Etiqueta | Significa |
|---|---|
| **[medido]** | Dato obtenido hoy de DataForSEO, de Google Search Console o leído en un fichero de este repo (se cita `fichero:línea`) |
| **[fuente]** | Dato externo con URL. Si la URL no es oficial, se dice |
| **[estimado]** | Criterio propio. No es un dato |

Nada de lo que sigue lleva una cifra inventada. Donde una fuente no da el número, se dice que no lo da.

---

## 1. Demanda y mercado

### 1.1 Volúmenes de búsqueda (DataForSEO, Google Ads, 2026-09-20)

**España** (`--pais 2724 --idioma es`, el defecto del helper) **[medido]**:

| Keyword | Vol./mes | Competencia | Últimos 6 meses |
|---|---:|---|---|
| pizza *(control de que la API vive)* | 301.000 | LOW | 450.000, 368.000, 301.000, 301.000, 301.000, 301.000 |
| comida mexicana | 9.900 | LOW | 9.900, 9.900, 9.900, 12.100, 9.900, 12.100 |
| tacos mexicanos | 5.400 | LOW | 6.600, 5.400, 5.400, 5.400, 5.400, 5.400 |
| taqueria | 4.400 | LOW | 5.400, 4.400, 3.600, 4.400, 4.400, 4.400 |
| taco al pastor receta | 480 | LOW | 480, 390, 390, 390, 480, 480 |
| taqueria mexicana | 210 | LOW | 260, 170, 210, 210, 210, 260 |
| **taquería mexicana** *(con tilde)* | **110** | LOW | 260, 170, 140, 110, 70, 70 |
| montar una taqueria | 10 | — | 0, 0, 0, 0, 0, 10 |
| abrir una taqueria | 10 | — | 0, 10, 0, 0, 0, 10 |
| taqueria en españa | 10 | LOW | 10, 10, 10, 10, 10, 10 |
| checklist taqueria | *sin datos* | — | — |
| tareas taqueria | *sin datos* | — | — |
| manual de operaciones taqueria | *sin datos* | — | — |

**México** (`--pais 2484 --idioma es`) **[medido]**:

| Keyword | Vol./mes | Competencia |
|---|---:|---|
| taqueria | 135.000 | LOW |
| trompo al pastor | 1.900 | LOW |
| taco al pastor receta | 880 | LOW |
| taqueria mexicana | 590 | LOW |
| manual de operaciones restaurante | 70 | LOW |
| como poner una taqueria | 30 | LOW |
| montar una taqueria | 10 | — |
| abrir una taqueria | 10 | LOW |
| checklist taqueria · tareas taqueria · manual de operaciones taqueria · control de temperaturas cocina · formatos para taqueria | *sin datos* | — |

**EE. UU. en español** (`--pais 2840 --idioma es`) **[medido]**:

| Keyword | Vol./mes | Competencia |
|---|---:|---|
| taqueria | 201.000 | LOW |
| taco al pastor | 90.500 | LOW |
| taqueria mexicana | 18.100 | LOW |
| como abrir una taqueria | 10 | LOW |
| abrir una taqueria | 10 | — |
| checklist taqueria · lista de tareas restaurante · manual de operaciones para restaurante | *sin datos* | — |

**Tres lecturas que cambian decisiones:**

1. **La grafía con tilde y sin tilde NO devuelve el mismo dato.** En España, `taqueria` = 210/mes y `taquería` = 110/mes, con **series mensuales distintas** (260-170-210-210-210-260 frente a 260-170-140-110-70-70) **[medido]**. No es la misma keyword normalizada: son dos filas. La lección de `chili crisp` vale también al revés — aquí no hay errata, pero **hay que medir las dos grafías antes de decidir el `title` y las `keywords`** de la landing, y probablemente escribir ambas.
2. **La intención operativa tiene volumen cero en los tres mercados.** `checklist taqueria`, `tareas taqueria` y `manual de operaciones taqueria` no devuelven ni una fila en ES, MX ni US-es. Aplica la regla de la casa (`feedback_volumen-cero-no-descalifica-un-producto`): **el kit no se vende por SEO de su keyword, se vende desde el catálogo, desde el hub y desde los contenidos mexicanos**. El volumen que sí existe —`taqueria` 4.400 ES / 135.000 MX / 201.000 US-es— es de gente buscando **dónde comer**, no de compradores.
3. **La API está viva.** `pizza` = 301.000 en España. Los ceros son ceros reales, no un fallo de credenciales.

### 1.2 SERP «montar una taqueria» — España **[medido]**

117 resultados. Bloques: `ai_overview` ×1, `organic` ×17, `people_also_ask` ×1, `video` ×1. **Hay AI Overview.**

| Pos. | Resultado |
|---:|---|
| 1 | lexpress-franchise.com — «Cómo abrir una taquería en España desde cero en 2026» *(único resultado pensado para España)* |
| 2 | Reddit `r/Changarrito` — hilo «Voy a abrir una taquería ¿Consejos?» |
| 3 | olaclick.com (MX) — «¿Cómo montar una taquería paso a paso en México?» |
| 4 | lacanasta.com.mx — equipo y utensilios |
| 5 | joinposter.mx — «Cómo abrir tu taquería, paso a paso» |
| 6 | unileverfoodsolutions.com.mx — «Operación diaria del puesto de tacos · Capacitación del personal» |
| 7 | servinox.com.mx — «¿Vale la pena abrir una taquería?» |
| 8-17 | **Ruido local**: taquerías de Barcelona, Gijón, Valencia, Alicante, Sant Cugat, Parque Warner, un vídeo de YouTube, una noticia de sucesos de Zapopan y dos vídeos de TikTok/Instagram |

**Qué dice esta SERP:** la consulta está **partida**. Google no sabe si «montar una taquería» es una intención de negocio o una intención de «dónde ceno tacos», y rellena la mitad inferior con negocios locales. De los 7 primeros, **6 son contenido mexicano** escrito para México (SAT, RFC, pesos) y sólo 1 habla de España. **No hay ni un operador español con autoridad en esta intención** — y eso incluye a AI Chef Pro.

**People Also Ask (9 preguntas) [medido]:**

- ¿Cuánto dinero necesito para abrir una taquería?
- ¿Cuánto gana un dueño de una taquería?
- ¿Qué se necesita para empezar una taquería?
- ¿Cuál es el margen de ganancia de una taquería?
- ¿Cuánto se cobra una taquiza para 100 personas?
- ¿Cuántos tacos salen de 1 kg de tortilla?
- ¿Cuántos kilos de carne necesito para 100 tacos?
- ¿Cuánto cuesta 1 kg de tortillas?
- ¿Cuánto rinde 1 kilo de carne para tacos?

**Cinco de las nueve son preguntas de RENDIMIENTO** (tacos por kilo de tortilla, kilos de carne por 100 tacos, rendimiento del kilo de carne). Esto es material directo para la FAQ de la landing y, más importante, **un argumento de producto**: una hoja del kit que mida el rendimiento del trompo y de la tortilla responde a lo que la gente ya está preguntando.

### 1.3 SERP «manual de operaciones taqueria» — México **[medido]**

99 resultados. Bloques: `organic` ×19, `ai_overview` ×1, `people_also_ask` ×1. **Hay AI Overview.**

| Pos. | Resultado |
|---:|---|
| 1 | **Scribd** — «Manual de Procedimientos Taquería» (PDF) |
| 2 | **Studocu** — trabajo de la Universidad Autónoma de Chiapas |
| 3 | **CourseHero** — `TAQUERIA.docx` |
| 4 | Facebook (mixmixblog) — «Descarga los manuales para taquería. Son gratis» |
| 5 | **Scribd** — «Manual de Procedimientos Taquería La Unión» |
| 6 | envanature.com — cómo crear el manual de operaciones de un restaurante |
| 7 | **Studocu** — Instituto Tecnológico Superior de Ciudad Hidalgo |
| 8 | clubensayos.com — «Taquería La flamita» |
| 9-13 | **Ruido absoluto**: un vídeo en inglés, el manual de un variador de frecuencia NORD, vídeos sobre coches de transmisión manual y un hilo de Reddit sobre proxies |

**Esto es un hallazgo de posicionamiento, no de tráfico.** La intención «manual de operaciones de taquería» está **ocupada por trabajos de clase subidos a Scribd, Studocu y CourseHero**. No hay un solo producto profesional. Un kit de checklists bien hecho no compite contra nadie: compite contra un PDF de un alumno de Chiapas. Con 70 búsquedas/mes en México para `manual de operaciones restaurante` y cero para la variante de taquería, **no se va a monetizar por SEO** — pero sí soporta el argumento comercial de la landing («lo que circula por ahí son trabajos de clase; esto son las hojas que se firman cada turno»).

**People Also Ask (9 preguntas) [medido]:** ¿Cómo se administra una taquería? · ¿Qué incluye un manual de operaciones? · ¿Qué es el manual de operaciones de un restaurante? · ¿Cuánto genera una taquería al mes? · ¿Cuánto se cobra una taquiza para 100 personas? · ¿Cuántos tacos salen de 1 kg de tortilla? · ¿Cuántos kilos de carne necesito para 100 tacos? · **¿Cuántos tacos salen de un trompo de 10 kilos?** · ¿Cuánto rinde 1 kilo de carne para tacos?

La pregunta del **trompo de 10 kilos** confirma que **el trompo es la unidad mental de rendimiento del formato**. Eso manda sobre el diseño del fichero 02.

### 1.4 Fallos de la API, reportados **[medido]**

- `serp "checklist taqueria" --pais 2484` → `DataForSEO: Task completed with partial results. Some pages could not be retrieved...`
- `serp "checklist para taqueria" --pais 2484` → `DataForSEO: Internal SE Server Error.`

No se reintentaron más veces para no quemar saldo. **No se pudo ver la SERP de «checklist taquería».** Dado que la keyword tiene volumen cero en los tres mercados, la pérdida de información es baja.

---

## 2. Datos propios (Google Search Console, `sc-domain:aichef.pro`, últimos 90 días) **[medido]**

### 2.1 Qué recibe ya la intención mexicana

| Página | Clics | Impr. | CTR | Pos. |
|---|---:|---:|---:|---:|
| `https://aichef.pro/en/use-cases/concept/mexican-restaurant` | 5 | 282 | 1,77 % | 6,7 |
| `https://aichef.pro/guia-restaurante-mexicano` | 3 | 93 | 3,23 % | 8,9 |
| `https://aichef.pro/de/anwendungsfaelle/konzept/mexikanisches-restaurant` | 1 | 3 | 33,33 % | 7,0 |
| `https://blog.aichef.pro/tacos-al-pastor-autenticos-receta-mexicana/` **(URL legacy, 301)** | 0 | 2 | 0 % | 80,0 |

⚠️ **Ojo con la última fila**: es del subdominio **legacy** `blog.aichef.pro`, ya 301-eado. La URL migrada `aichef.pro/blog/tacos-al-pastor-autenticos-receta-mexicana` **no aparece en el top-500 de páginas ni en el top-500 de pares consulta-página**. Es exactamente la trampa documentada en `CLAUDE.md` («las posiciones de GSC suelen ser de la URL legacy»). Conclusión honesta: **ese post no tiene tracción medible**; no es un activo del que colgar el kit.

**No hay ni una sola consulta con «taco», «taquer», «mexic» o «pastor» que traiga clics a un producto.** El único par relevante en 500 filas es `a pastor` → la URL legacy, 2 impresiones, posición 80.

### 2.2 El activo mexicano real: el pSEO de ciudades

| Página | Clics | Impr. | Pos. |
|---|---:|---:|---:|
| `/licencia-restaurante/monterrey` | 24 | 996 | 6,4 |
| `/abrir-restaurante/ciudad-de-mexico` | 23 | 3.383 | 7,1 |
| `/abrir-restaurante/queretaro` | 10 | 547 | 6,1 |
| `/abrir-restaurante/monterrey` | 5 | 96 | 3,7 |
| `/licencia-restaurante/guadalajara` | 4 | 319 | 7,7 |
| `/abrir-restaurante/guadalajara` | 3 | 79 | 3,9 |
| `/licencia-restaurante/ciudad-de-mexico` | 1 | 148 | 8,1 |
| `/licencia-restaurante/queretaro` | 1 | 117 | 7,4 |
| `/plan-negocio-restaurante/ciudad-de-mexico` | 1 | 53 | 8,9 |
| **Total** | **72** | **5.738** | — |

**72 clics y 5.738 impresiones en 90 días de tráfico mexicano ya en casa** — casi tres veces los clics que suma toda la familia de kits de tareas (ver 2.3). Ninguna de esas páginas enlaza hoy a un kit de taquería, porque no existe. **Aquí está el interenlazado de entrada del producto nuevo.**

### 2.3 Cómo se comporta hoy la familia de kits en GSC

| Página | Clics | Impr. | Pos. |
|---|---:|---:|---:|
| `/kit-tareas` (hub/base) | 10 | 349 | 6,8 |
| `/kit-tareas-hotel` | 4 | 137 | 9,4 |
| `/kit-tareas-asador` | 2 | 64 | 23,7 |
| `/kit-tareas-cafeteria` | 2 | 46 | 11,1 |
| `/kit-tareas-food-truck` | 2 | 37 | 9,6 |
| `/kit-tareas-panaderia` | 2 | 17 | 13,5 |
| `/kit-tareas-catering` · `/kit-tareas-chef-privado` · `/kit-tareas-dark-kitchen` · `/kit-tareas-heladeria` · `/kit-tareas-restaurante-creativo` | 1 c/u | 19-55 | 7,2-12,5 |
| **Total familia** | **≈27** | **≈850** | — |

**El hallazgo más accionable de todo el bloque GSC:** la **única consulta no-marca** que engancha a la familia es **`"calendario anual de tareas"` (entre comillas)** **[medido]**:

- → `/kit-tareas`: 0 clics, **20 impresiones**, posición **8,8**
- → `/kit-tareas-dark-kitchen`: 0 clics, 7 impresiones, pos. 10,0
- → `/kit-tareas-cafeteria`: 0 clics, 3 impresiones, pos. 11,0
- → `"calendario anual de tareas" español` → `/kit-tareas`: 0 clics, 5 impresiones, pos. 8,4

Es decir: **lo que Google ya entiende de estos productos es el BONUS-02**, no el kit. 0 clics con posición 8,8 es un problema de título/meta, no de posicionamiento. **Recomendación [estimado]:** que el `BONUS-02-calendario-anual` aparezca en el `title` o en la `description` de la landing de la taquería, o al menos en un `h2`, en lugar de quedar relegado a la sección de bonos.

---

## 3. Canibalización y cross-sell contra lo que está LIVE

### 3.1 La familia: 19 kits, tres escalones de precio

`netlify/shared/product-prices.ts:20-38` **[medido]**:

| Precio | Kits |
|---:|---|
| **12 €** | bar, cafeteria, catering, chocolateria, dark-kitchen, **food-truck**, hamburgueseria, heladeria, **panaderia**, pasteleria, pizzeria, restaurante-creativo *(12 kits)* |
| **14 €** | `kit-tareas` (base, restaurante casual), **asador**, **marisqueria**, **sushi-bar**, **tapas-bar** *(5 kits)* |
| **18 €** | chef-privado |
| **18,5 €** | hotel |

Y `netlify/shared/product-prices.ts:41`: `'mega-pack-tareas': { eur: 89 }`.

### 3.2 `guia-restaurante-mexicano` (65 €) — ¿pisa o complementa?

**Complementa, con un punto de roce acotado.**

- `astro-site/src/data/productos/guias/guia-restaurante-mexicano.ts:39-40` → 180 € tachado / **65 €**.
- `:29-30` → «8 plantillas Excel con fórmulas» + «**6 checklists de apertura**: legal, equipamiento, APPCC, sala, contratación, marketing».
- Los ficheros entregados lo confirman (`astro-site/public/dl/guia-restaurante-mexicano/`) **[medido]**: `checklist-legal.xlsx`, `checklist-equipamiento-cocina-mexicana.xlsx`, `checklist-appcc.xlsx`, `checklist-diseno-sala-mexicana.xlsx`, `checklist-contratacion.xlsx`, `checklist-marketing-preapertura.xlsx`. **Los seis son de PROYECTO (antes de abrir), ninguno es de turno.** El resto son plan financiero, escandallos, Gantt, P&L, cash-flow, business plan y un `manual-operaciones-mexicano.docx`.

**El único roce real** está en `guia-restaurante-mexicano.ts:124` **[medido]**:

> BONUS 2 · «Manual de Operaciones Mexicano» (39 €) — *«Protocolo completo: apertura, cierre, servicio, preparación de salsas, barra de tequilas, gestión de delivery y eventos temáticos (Día de Muertos, Cinco de Mayo)»*

Es un `.docx` **narrativo** («protocolo»), no una rejilla de fichaje con firma. El kit nuevo es la **ejecución diaria** de eso. Riesgo de canibalización: **bajo**, y se neutraliza con posicionamiento explícito (ver §11, pregunta 3).

**Cross-sell natural, con dinero detrás**: guía 65 € (abrir) → kit 12/14 € (operar). Y al revés: quien compre el kit de taquería por 14 € es el candidato perfecto a la guía de 65 €. `src/data/use-cases-content.es.ts:3580` ya define la cesta del caso de uso `restaurante-mexicano` (`:3542`) con `['guia-restaurante-mexicano', 'kit-escandallos', 'pack-appcc', 'kit-inventario', 'kit-gestion-personal', 'pro-prompts-ebook']` **[medido]** — **ahí falta el kit nuevo**.

### 3.3 `kit-tareas-food-truck` — ¿solapa por los tacos?

**No. Cero solape.** Una sola aparición de «tacos» en las 376 líneas de ficha:

`astro-site/src/data/productos/tareas/kit-tareas-food-truck.ts:159` **[medido]**:
> `desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu food truck (tacos, hamburguesas, fusión, dulce, café, etc.).'`

Es la descripción del fichero `09-plantilla-personalizable`, donde «tacos» es un ejemplo de concepto entre cinco. Sus ficheros propios son `01-setup-teardown-food-truck`, `02-operaciones-moviles-vehiculo`, `03-appcc-seguridad-alimentaria-movil`, `04-permisos-eventos-localizaciones` **[medido]** — todo gira alrededor del **vehículo y los permisos de evento**, no de la cocina mexicana. Una taquería de local fijo no tiene nada que hacer ahí.

### 3.4 `kit-tareas-sushi-bar` — el molde (376 líneas)

`astro-site/src/data/productos/tareas/kit-tareas-sushi-bar.ts` es la referencia de la ficha. Bloques obligatorios, en orden **[medido]**: `slug` · `stripeEnvKey` · `seo{title,description,keywords,ogImage}` · `schema{productName,productDescription,price,priceValidUntil,aggregateRating,reviews[3],faqs[5],breadcrumbName}` · `images{gallery[6],whyBg,buyBoxBg,ctaBg}` · `hero{badge,titlePre,titleGold,subtitleLine,description,checkItems[5],ctaLabel}` · `stickyLabel` · `grid{countGold:'11',headingRest,subtitle,templates[11]}` · `why{…,reasons[4],compatPills[5]}` · `authorBio` · `bonus{items[2]}` · `buyBox` · `guarantee{text,stats[3]}` · `faqs[6]` · `cta{heading,subtitle,items[8],ctaLabel}` · `testimonials{items[8]}` · `pricing{priceOld:'€69',price:'€14',discountBadge:'-80%',…}` · `footerLinks[6]` · `updateNote` · `alreadyBought`.

Detalles del molde que hay que calcar **[medido]**:

- El `badge` del hero es un ancla de precio: *«Lo que el software de gestión cobra €40/mes, tú lo tienes por €14 — para siempre»* (`:90`).
- El `bonus.subtitle` valora los dos bonus en **34 €** (BONUS 1 = 15 €, BONUS 2 = 19 €) (`:222-246`).
- El escalón de 14 € usa **`priceOld: '€69'`** (`:353`); el de 12 € usa **`priceOld: '€39'`** (`kit-tareas-food-truck.ts:353`). **No se pueden mezclar.**
- `aggregateRating` 4,9 con 8 reseñas y 8 testimonios con avatar. La capa comercial se mantiene intacta por decisión de John (memoria `project_capa-comercial-honesta-decision-2026-08-29`).

### 3.5 Lo que ya está publicado sobre este producto

`astro-site/src/components/pages/ProductosDigitalesHubPage.astro:993` **[medido]**:

> `{ iconName: 'UtensilsCrossed', name: 'Tareas Recurrentes: Taquería Mexicana', desc: 'Rutinas de plancha, salsas y tortilla, turnos y cierre para una taquería que funciona sola.', tags: ['plantillas','excel','restaurante'], phase: 'Q4 2026' }`

**La descripción publicada no menciona el trompo**, que es la señal de identidad del formato y el que aparece en el People Also Ask («¿cuántos tacos salen de un trompo de 10 kilos?»). Al publicar el producto, esa tarjeta sale de `comingSoon` — y si se reutiliza el texto, se pierde el gancho.

### 3.6 Mega Pack: dice 13, hay 19

- `src/data/products-catalog.ts:516` **[medido]**: `es: 'Los 13 kits de tareas de hostelería en un solo pack.'`
- `src/pages/MegaPackTareas.tsx:20-33` **[medido]** lista exactamente 13: restaurante casual, cafetería, pizzería, hamburguesería, dark kitchen, pastelería, bar, catering, **hotel (19 plantillas)**, heladería, chocolatería, **restaurante creativo (13)**, **chef privado (9)**.
- `src/pages/MegaPackTareasDashboard.tsx` entrega esos mismos 13 **[medido]**.
- Quedan **fuera**: sushi-bar, asador, marisquería, tapas-bar, food-truck y panadería.
- La decisión ya está anotada como pendiente en `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md:311` **[medido]**: *«antes de la primera [réplica], decidir si el Mega Pack (89 €, "13 kits") pasa a incluir los nuevos (hoy ya hay 19 kits LIVE fuera de esa cifra)»*.

**Conclusión del bloque 3: el kit COMPLEMENTA. No pisa nada.** El único ajuste de copy necesario es diferenciarlo del BONUS 2 de la guía mexicana.

---

## 4. Tipos de taquería que debe cubrir un solo juego de ficheros

Seis formatos. La clave es que **los seis comparten el 01, el 05, el 06, el 07, el 09 y los dos BONUS**; lo que cambia es el peso que le dan al 02, 03 y 04.

| Tipo | Qué es | Qué cambia operativamente | Ficheros que carga |
|---|---|---|---|
| **1. De barrio / de guisados** | Carta corta, cazuelas en baño maría, alta rotación, ticket bajo | La tarea crítica es la **rotación de guisados**: hora de elaboración, hora de entrada en baño maría, hora límite y merma. Sin trompo, o con trompo pequeño | 04 (guisados), 01 |
| **2. Gourmet / contemporánea** | Carta de autor, maridaje mezcal, reservas, emplatado | Aparecen **fichas de emplatado**, briefing con plato del día, control de mermas de producto caro y gestión de reservas | BONUS-01, 05 |
| **3. Con trompo al pastor** | El asador vertical es el centro del negocio | **Marinado 12-24 h → montaje con peso y hora → sonda antes de cada tanda de corte → rendimiento del trompo.** Es el formato con más carga de registro | 02, 03 |
| **4. Con tortillería propia (nixtamal)** | Nixtamaliza y muele en el local | **Turno de madrugada completo**: cocción con cal, reposo, lavado, molienda, prensado. La limpieza del molino es punto crítico. Rendimiento kg maíz → kg masa → nº de tortillas | 04, 07 |
| **5. Con barra de salsas de autoservicio** | El cliente se sirve | **El punto de mayor riesgo del formato**: salsas crudas ≤4 °C, reposición por tandas en recipiente limpio (nunca rellenar encima), utensilio por salsa, cartel de alérgenos (la macha lleva cacahuete y/o sésamo) | 03 |
| **6. Taquería-cantina** | Taquería + barra de bebida | **Dos negocios**: doble cierre (cocina y barra), mermas de barra, inventario de mezcal/tequila, control de cola y aforo en horario de copas | 05, 07 |

**[estimado]** Un solo juego de 11 ficheros los cubre todos si —y sólo si— el fichero 02 se titula por **la función** («trompo y plancha») y no por el equipo. Una taquería española sin asador vertical (muy común) debe seguir usando ese fichero para plancha y comal, o se queda con 10 ficheros útiles de 11.

---

## 5. Regulación española 2026 aplicada a las CHECKLISTS

Esto **no** es un capítulo legal: es la lista de los datos que cada hoja tiene que pedir. Pero las cifras tienen que estar bien, porque van impresas en una hoja que se firma.

### 5.1 🔴 La norma marco cambió, y la cifra que todo el mundo repite es la vieja

**Real Decreto 1021/2022, de 13 de diciembre** (BOE-A-2022-21681), *«por el que se regulan determinados requisitos en materia de higiene de la producción y comercialización de los productos alimenticios en establecimientos de comercio al por menor»* **[fuente: https://www.boe.es/buscar/act.php?id=BOE-A-2022-21681]**.

Su **disposición derogatoria única** derogó, con efectos de 22-dic-2022 **[fuente, misma URL]**:

- RD 1254/1991 (mayonesa de elaboración propia)
- **RD 3484/2000** (comidas preparadas)
- **RD 1376/2003** (carnes frescas en establecimientos minoristas)
- RD 1420/2006 (anisakis)

**Artículo 30 — temperaturas de comidas preparadas [fuente: BOE, art. 30]:**

| Concepto | Valor vigente | Valor VIEJO que sigue circulando |
|---|---|---|
| Mantenimiento en **caliente** | **≥ 63 °C** | 65 °C (RD 3484/2000, derogado) |
| **Refrigeración**, vida útil > 24 h | **≤ 4 °C** | igual |
| **Refrigeración**, vida útil ≤ 24 h | **≤ 8 °C** | igual |
| **Congelación** | **≤ −18 °C** | igual |
| **Recalentado** | **≥ 74 °C durante ≥ 15 s en el centro, en el término de 1 hora** | «≥65 °C en el centro» |

⚠️ **Esto es dinero.** Casi toda la documentación de hostelería en castellano —y buena parte de la que hay en el propio blog— sigue diciendo «65 °C en caliente» y «recalentar a 65 °C». **Son las cifras derogadas.** Las hojas del kit deben imprimir **63 °C** y **74 °C/15 s**. El kit de sushi-bar ya cita correctamente este RD (`kit-tareas-sushi-bar.ts:63`), así que la familia tiene precedente.

**Artículo 8 — congelación preventiva de productos de la pesca [fuente: BOE, art. 8]:** **−20 °C durante un mínimo de 24 h** o **−35 °C durante un mínimo de 15 h**, para pescado destinado a consumirse crudo, en escabeche o en salazón.

**Aplica a la taquería**, aunque no lo parezca: **aguachiles, ceviches, tostadas de atún y camarón crudo** son carta habitual. Si la taquería los sirve, necesita el mismo registro de congelación por lote que un sushi bar. Si no los sirve, la hoja se queda vacía y no pasa nada.

### 5.2 El trompo al pastor: mismo perfil de riesgo que el döner

No hay norma específica española del trompo. Lo que existe es la guía de buenas prácticas del asador vertical, publicada por la **Agència Catalana de Seguretat Alimentària (ACSA)**, *«Buenas prácticas en la elaboración de kebab»* **[fuente: https://acsa.gencat.cat/es/Publicacions/guies-i-documents-de-bones-practiques/documents-de-bones-practiques/bones-practiques-en-lelaboracio-de-kebab/index.html]**, resumida en **[fuente: https://higieneambiental.com/higiene-alimentaria-kebab]**:

- Recepción y conservación del cono: **≤ −18 °C** si congelado, **≤ 4 °C** si refrigerado.
- Salsas y vegetales crudos, en nevera y en expositor: **≤ 4 °C**.
- **Termómetro sonda obligatorio** para comprobar cocción y mantenimiento, **como mínimo al inicio y a mitad del servicio**.
- Evitar que la carne cruda toque, directa o indirectamente, alimentos listos para el consumo.
- Los vegetales se lavan bajo agua corriente y pueden desinfectarse con lejía de uso alimentario.

**Honestidad sobre lo que la fuente NO dice [fuente]:** ni la ficha de ACSA ni el resumen fijan **un tiempo máximo de cono montado** ni **una vida útil de la carne ya fileteada**. Esos dos números los fija el operador en su propio APPCC y los valida. **El kit debe pedir el dato, no inventarlo**: la hoja lleva una casilla «hora de montaje» y otra «hora límite definida en tu APPCC: ____», no un «máximo 4 h» sacado de la manga.

**Temperatura de cocinado [fuente: AESAN, Informe del Comité Científico sobre combinaciones tiempo-temperatura, https://www.aesan.gob.es/AECOSAN/docs/documentos/seguridad_alimentaria/evaluacion_riesgos/informes_comite/TIEMPO-TEMPERATURA.pdf]:** **70 °C durante ≥1 s en el centro** para carne; **74 °C durante ≥1 s** para aves. El trompo se corta por capas: la superficie que se rebana tiene que haber alcanzado esa temperatura, y el interior sigue crudo hasta que le toca.

**[estimado]** Traducción a tareas: sondar la superficie de corte antes de cada tanda; cortar sólo la capa cocinada; la carne cortada que no se sirve al momento va a mantenimiento **≥63 °C** (art. 30), nunca a ambiente; y cuchillo y tabla del trompo no tocan producto listo para consumo.

### 5.3 Salsas crudas, pico de gallo y guacamole

No hay una norma que les ponga nombre: entran como **comidas preparadas sin tratamiento térmico** del art. 30 → **≤4 °C** si la vida útil supera 24 h, **≤8 °C** si no llega **[fuente: BOE, RD 1021/2022, art. 30]**. La guía del kebab exige además **≤4 °C en el expositor** para salsas y vegetales crudos **[fuente: ACSA]**.

**[estimado]** Lo que de verdad falla en una barra de salsas de autoservicio, y por tanto lo que tiene que ir en la hoja:

1. **Rellenar encima del resto anterior** (mezcla lotes y reinicia el reloj de forma falsa) → la tarea es «cambiar recipiente, no rellenar».
2. **Hora de puesta en barra sin hora de descarte** → dos casillas, siempre las dos.
3. **Una cuchara compartida** entre la macha (cacahuete/sésamo) y el resto → utensilio por salsa, y cambio por turno registrado.
4. **El cliente metiendo la mano** → revisión visual por turno.

### 5.4 Nixtamal, masa y tortilla

**No existe normativa española específica** de masa nixtamalizada. Lo que hay es literatura técnica **[fuente: http://www.fcb.uanl.mx/IDCyTA/files/volume3/4/1/4.pdf y https://www.alanrevista.org/ediciones/1995/2/art-8/]** que concluye que **la refrigeración es lo que inhibe el crecimiento microbiano en la tortilla** y que hay que controlar **la limpieza del molino** y **la temperatura de almacenamiento de la masa**. Las vidas útiles que dan esos estudios son de laboratorio y con conservadores (propionato sódico, sorbato) — **no sirven como cifra para una hoja de trabajo**.

**[estimado]** Por tanto: la hoja 04 no imprime «la masa dura X horas». Imprime las casillas de **hora de molienda**, **temperatura de conservación**, **hora límite definida por el operador** y **limpieza del molino antes y después** (que es el punto crítico real). Y, si la taquería compra la tortilla en vez de hacerla, la misma hoja sirve como registro de recepción: proveedor, lote, fecha y temperatura.

### 5.5 Alérgenos — la trampa específica de una taquería

**Reglamento (UE) 1169/2011** + **Real Decreto 126/2015** (BOE-A-2015-2293) para alimentos sin envasar: los **14 alérgenos** de declaración obligatoria, información **gratuita y accesible** al consumidor, por carta, recetario o de forma oral con soporte escrito verificable **[fuente: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2015-2293]**.

Los cuatro puntos donde una taquería se cae, y que tienen que ser tarea:

| Alérgeno | Dónde se esconde en una taquería |
|---|---|
| **Cereales con gluten** | La **tortilla de harina de trigo**. La de maíz nixtamalizado no lleva — y esa diferencia es justo la que el cliente celíaco pregunta. También la cerveza |
| **Cacahuetes** y **granos de sésamo** | La **salsa macha** (cacahuete y/o sésamo), servida a granel en la barra de autoservicio. Es el punto de contacto más peligroso del formato |
| **Frutos de cáscara** | Los **moles** (almendra, nuez, cacahuete según receta) y la **nogada** |
| **Leche y derivados** | Crema, queso fresco, quesadillas, queso fundido, chile con queso |

**[estimado]** Tareas derivadas: separación física de la freidora/pinzas/superficie entre tortilla de maíz y de harina; cartel de alérgenos visible en la barra de salsas con la macha marcada; y **revisión de la ficha de alérgenos cada vez que cambia un proveedor o una receta** (el fallo más frecuente: se cambia el proveedor de mole y nadie toca la ficha).

### 5.6 Registro de jornada — ⚠️ NO decir «obligatorio en digital desde 2026»

- **Lo que sí es cierto:** el registro diario de jornada es obligatorio para todas las empresas desde 2019 por el **art. 34.9 del Estatuto de los Trabajadores** (introducido por el **RD-ley 8/2019**), y no tenerlo es infracción **grave**. El propio repo ya lo dice bien en `src/pages/KitGestionPersonal.tsx:70` **[medido]**: *«de 751 a 7.500 EUR por centro de trabajo (art. 7.5 LISOS)»*.
- **Lo que NO es cierto todavía:** el Real Decreto que impondría el **registro horario DIGITAL** (prohibiendo papel y Excel) **seguía sin publicarse en el BOE a mediados de 2026**. Pasó consulta pública en octubre de 2025 y recibió el dictamen del Consejo de Estado el 23 de marzo de 2026, con reparos; el Consejo mencionó **expresamente a la hostelería** como sector que necesitaría tratamiento diferenciado **[fuente: https://mifichajelegal.com/blog/real-decreto-registro-horario-digital-mayo-2026-estado-tramitacion-pymes/ — medio especializado, NO oficial]**.

⚠️ **Verificar en el BOE antes de publicar la landing.** Y ojo: hay copy vivo que ya afirma lo contrario — `astro-site/src/data/productos/guias/guia-panaderia-obrador.ts:75` vende *«Requisitos Legales España 2026: … + control horario digital»* y `:105` un testimonio que habla de *«el control horario digital 2026»* **[medido]**. No es del alcance de este producto, pero es un riesgo del corpus (§11).

**[estimado]** En el kit, la hoja 05 pide «registro de jornada cerrado y firmado» como tarea del manager, sin adjetivos. Un kit de Excel no puede prometer que resuelve un registro que quizá deje de poder hacerse en Excel.

---

## 6. Equipamiento y ciclo productivo (de aquí salen las hojas 01-04)

### 6.1 Equipamiento que dicta tareas

| Equipo | Tareas que genera |
|---|---|
| **Trompo / asador vertical de gas** (1-3 quemadores) | Encendido y verificación de llama · montaje con peso y hora · sonda de superficie antes de cada tanda · desengrase de la bandeja de grasas · revisión de la instalación de gas (mensual) |
| **Plancha de acero** | Calibración por zonas (alta/media) · rascado y engrase en caliente al cierre |
| **Comal** | Temperatura de trabajo · limpieza · mermas de tortilla |
| **Tortilladora / prensa** | Calibración de grosor y peso por pieza · limpieza a fondo (semanal) |
| **Nixtamalizadora y molino** | Cocción con cal (proporción y hora) · reposo · lavado · molienda · **limpieza del molino antes y después: punto crítico** |
| **Baño maría de guisados** | ≥63 °C con dos lecturas por turno · hora de entrada y hora límite por cazuela |
| **Mesa/barra fría de salsas** | ≤4 °C · reposición por tandas · utensilio por salsa · hora de descarte |
| **Freidora** (tacos dorados, flautas, totopos) | Filtrado y cambio de aceite · control de punto de humo · separación tortilla maíz/harina por alérgenos |
| **Cámaras y congelador** | Registro de temperaturas 2×turno · trazabilidad de lote y proveedor · registro de congelación para crudos (art. 8) |
| **Licuadora industrial / molcajete** | Molienda de chiles · limpieza y desinfección entre salsas (contaminación cruzada de alérgenos) |
| **Campana y extracción** | Desengrase semanal · limpieza de filtros y registro (mensual) |

### 6.2 El ciclo, y cuándo ocurre cada cosa

```
D-1 tarde    Marinado del pastor: pesar carne + adobo (achiote, chiles), 12-24 h a ≤4 °C
D  madrugada Nixtamal (si hay tortillería): cocción con cal → reposo → lavado → molienda
D  pre-apert. Montaje del trompo (capas, grasa, piña, cebolla) + encendido del asador
             Mise en place de salsas (cocidas y crudas) y de guisados a baño maría
D  servicio  Corte por capas del trompo · plancha · comal · reposición de barra de salsas
D  cierre    Retirada del trompo (destino registrado) · descarte de salsas crudas ·
             abatimiento del guisado apto · limpieza de bandeja de grasas, comal y molino ·
             arqueo de caja y cierre de delivery
```

**El marinado empieza el día anterior y el nixtamal de madrugada.** Eso significa que **la hoja de apertura no puede ser la primera hoja cronológica del kit**: hay tareas que ocurren antes de que la taquería abra, y hay quien las hace en otro turno. Esto es lo que justifica que el 02 (trompo) y el 04 (nixtamal) sean ficheros propios y no secciones del 01.

---

## 7. Perfiles, manager y estacionalidad

### 7.1 Perfiles (→ hoja 06)

| Perfil | Núcleo de sus tareas |
|---|---|
| **Taquero (trompo)** | Marinado y montaje del trompo · sonda antes de cada tanda · corte por capas · ritmo de corte según cola · limpieza del asador y de la bandeja |
| **Tortillera/o** | Nixtamal, molienda, prensado y comal · mermas · limpieza del molino · recepción de tortilla comprada |
| **Salsero/a** *(responsable de salsas)* | Molienda de chiles · salsas cocidas y crudas · reposición por tandas · etiquetado, hora de puesta y hora de descarte · cartel de alérgenos |
| **Plancha y freidora** | Tacos dorados, quesadillas, totopos · filtrado y cambio de aceite · separación maíz/harina |
| **Mostrador y caja** | Comanda · **información de alérgenos al cliente** · cobro · gestión de cola · entrega de delivery |
| **Delivery** *(si aplica)* | Preparación y sellado del pedido · control de tiempos · temperatura de salida · incidencias |

**[estimado]** Son 6 perfiles frente a los 4 del sushi-bar (`06-tareas-perfiles.xlsx` → `Itamae (Chef Sushi)` / `Ayudante Sushi` / `Cocina Caliente` / `Sala y Servicio`) **[medido]**. El molde admite una hoja por perfil sin problema. Si se quiere mantener el paralelismo con la familia, «Plancha y freidora» y «Mostrador y caja» se pueden fundir, pero **el taquero, la tortillera y el salsero son tres oficios distintos y no deben compartir hoja**.

### 7.2 Tareas del manager (→ hoja 05)

**Diarias:** arqueo y cuadre de caja + reparto de propinas · revisión de la hoja de temperaturas firmada · tiempos y incidencias de delivery · **rendimiento del trompo del día** (kg montados → tacos servidos → ticket medio) · respuesta a reseñas.

**Semanales:** pedido a **importador de chiles secos, masa y producto mexicano** (con su plazo de entrega, que es el cuello de botella real en España) · comparativa de precio de cerdo y res · inventario de bebida, mezcal y tequila · revisión de escandallos de los 5 tacos más vendidos · planificación de turnos y cierre del registro de jornada.

**[estimado]** El «pedido a importador» es una diferencia de fondo con cualquier otro kit de la familia: una taquería española depende de importación para el chile seco, la masa y buena parte del producto seco, con plazos que no son los de un proveedor local. Esa tarea merece su propia fila con columna de plazo.

### 7.3 Estacionalidad (→ hoja 08 y BONUS-02)

| Fecha | Qué es | Nota |
|---|---|---|
| **6 de enero** | Día de Reyes — rosca | Compartido con España |
| **2 de febrero** | **Día de la Candelaria** — tamales | Quien sacó la figurita de la rosca pone los tamales **[fuente: https://calendariodemexico.com/chiles-en-nogada-historia-temporada/]** |
| **Cuaresma / Vigilia** (feb-abr) | Tacos de pescado, capeados, nopales, romeritos | Pico de demanda de pescado; enlaza con el art. 8 del RD 1021/2022 si se sirve crudo |
| **5 de mayo** | **Cinco de Mayo** | ⚠️ **Es una fiesta sobre todo ESTADOUNIDENSE.** En México se celebra en Puebla, no es fiesta nacional. Vale como excusa comercial en España y EE. UU.; **no** se puede presentar como «la gran fiesta mexicana» sin quedar mal ante un comprador mexicano |
| **15 de julio → finales de septiembre** | **Temporada de chiles en nogada** | La fecha de la Feria del Chile en Nogada 2026 va del **15 de julio a finales de septiembre**; agosto es el mes de mayor disponibilidad. Depende de la cosecha de granada roja, nuez de Castilla, manzana panochera, pera lechera, durazno criollo y chile poblano **[fuente: https://www.excelsior.com.mx/recetas/cuando-empieza-temporada-chiles-nogada-2026 y https://www.milenio.com/consejos/temporada-chiles-en-nogada-cuando-empieza-termina]** |
| **15-16 de septiembre** | **Grito e Independencia** | El pico comercial del año para una taquería fuera de México. Pozole, chiles en nogada, mezcal |
| **1-2 de noviembre** | **Día de Muertos** | Pan de muerto, calabaza en tacha. Muy fuerte también en España |
| **Diciembre** | Posadas y Navidad | Bacalao, romeritos, ponche |

**[fuente]** El encadenado lo resume bien la prensa gastronómica mexicana: *«los chiles en nogada son el pistoletazo de salida de la temporada gastronómica más rica de México: de ahí al pozole de las fiestas patrias, al pan de muerto y la calabaza en tacha de noviembre, al bacalao y los romeritos de Navidad, y a la rosca y los tamales de la Candelaria»* **[https://www.7canibales.com/mundo-canibal/chiles-en-nogada/]**.

**[estimado]** La hoja 08 debe llevar **dos pestañas**: `Calendario de Eventos` (lo de arriba, con columna «aplica en ES / MX / US-es») y `Temporadas y Producto` (aguacate, chile seco por campaña, cerdo para pastor, maíz). El sushi-bar hace exactamente eso: `Temporadas Pescado Espana` + `Eventos Especiales` **[medido]**.

---

## 8. Propuesta de los 11 ficheros

### 8.0 El molde, medido

`astro-site/public/dl/kit-tareas-sushi-bar/` **[medido]**: `01-apertura-cierre-sushi` · `02-preparacion-arroz-pescado` · `03-seguridad-anisakis-appcc` · `04-barra-sushi-neta-case` · `05-tareas-manager` · `06-tareas-perfiles` · `07-semanales-mensuales` · `08-eventos-estacionales` · `09-plantilla-personalizable` · `BONUS-01-briefing-servicio` · `BONUS-02-calendario-anual`.

Es decir: **01 fijo, 02-03-04 propios del concepto, 05-09 y BONUS fijos.**

**Estructura interna de cada `.xlsx` [medido, leyendo el XML con `unzip -p`, sin abrir Excel]:**

- Toda hoja de cálculo abre con una pestaña **`Instrucciones`** y luego 1-4 pestañas de contenido.
- Ejemplos reales: `01` → `Apertura Barra Sushi` / `Cierre Barra Sushi`; `05` → `Tareas Diarias Manager` / `Tareas Semanales Manager`; `06` → una hoja **por perfil**; `08` → `Temporadas Pescado Espana` / `Eventos Especiales`; `BONUS-02` → una sola hoja `Calendario Anual`.
- Cabecera de cada hoja de checklist: `Fecha: ___/___/______    Turno: ☐ Almuerzo  ☐ Cena    Responsable: _________________________`
- Columnas: **`Nº | Tarea | Zona | Responsable | Hora Limite | ✓ Completada | Firma`**
- Las tareas se agrupan bajo **secciones en mayúsculas** («  TEMPERATURAS Y EQUIPOS», «  PREPARACION ARROZ SUSHI»), con dos espacios de sangría.
- 🔴 **El texto de las celdas va SIN TILDES** (`Camara`, `Hora Limite`, `PREPARACION`, `Verificar temperatura camara pescado crudo`) y los símbolos van como entidades: `&#186;`=º, `&#176;`=°, `&#10003;`=✓, `&#9744;`=☐. **Verificado idéntico en `kit-tareas-asador`** **[medido]**. Es la convención de la familia; si el generador de la taquería emite tildes, el kit cantará distinto al resto y cualquier gate de paridad lo marcará.
- Volumen: la hoja de apertura del sushi-bar contiene 113 cadenas de texto en 4 columnas de texto → **≈30 tareas por hoja [estimado]**.

### 8.1 Los 11 ficheros propuestos

| # | Fichero | Hojas | Tareas de ejemplo (3-5 por hoja) |
|---:|---|---|---|
| **01** | `01-apertura-cierre-taqueria.xlsx` | `Instrucciones` · `Apertura Taqueria` · `Cierre Taqueria` | **Apertura** — *TEMPERATURAS Y EQUIPOS*: Verificar camara de carne marinada ≤4 °C y registrar en hoja APPCC · Encender asador vertical y comprobar llama uniforme en los quemadores · *TROMPO Y PLANCHA*: Montar el trompo del dia (capas, grasa, pina, cebolla), anotar peso y hora de montaje · Calibrar plancha y comal por zonas · *SALSAS Y GUARNICIONES*: Sacar salsas a barra fria y comprobar ≤4 °C en las crudas · Verificar cartel de alergenos de la barra (macha = cacahuete/sesamo) visible.<br>**Cierre** — Apagar asador, retirar carne sobrante del trompo y registrar destino (abatimiento / descarte) · Vaciar, lavar y desinfectar la bandeja de grasas · Descartar salsas crudas del dia y anotar merma · Limpiar comal y plancha en caliente, rascado y engrase · Arqueo de caja, cierre de delivery y corte de propinas |
| **02** | `02-trompo-pastor-plancha-comal.xlsx` | `Instrucciones` · `Marinado y Montaje del Trompo` · `Corte, Plancha y Comal` | **Marinado/Montaje** — Pesar carne y adobo por lote; anotar nº de lote y hora de inicio del marinado (12-24 h a ≤4 °C) · Remover el lote a mitad del marinado y registrar temperatura de camara · Montar el trompo: orden de capas, grasa, pina y cebolla; anotar peso total y hora de montaje · Esperar a que la capa exterior este cocinada antes del primer corte · Anotar peso sobrante al cierre y calcular rendimiento (tacos por kilo).<br>**Corte** — Sondar la capa exterior antes de cada tanda y registrar la lectura (≥70 °C) · Cortar solo la capa cocinada; no rebanar hacia el interior crudo · La carne cortada que no se sirve al momento pasa a mantenimiento ≥63 °C, nunca a ambiente · Limpiar cuchillo y tabla entre el trompo y cualquier producto listo para consumo |
| **03** | `03-appcc-salsas-crudas-alergenos.xlsx` | `Instrucciones` · `Temperaturas y Trazabilidad` · `Barra de Salsas` · `Alergenos y Contaminacion Cruzada` | **Temperaturas** — Registrar camaras, congelador, bano maria (≥63 °C) y barra fria (≤4 °C), dos veces por turno · Anotar lote y proveedor de carne de pastor, masa/tortilla y chiles secos importados · Registrar recepcion: temperatura, envase, caducidad y albaran · Verificar congelacion de pescado para tostadas/aguachiles: −20 °C/24 h o −35 °C/15 h por lote (RD 1021/2022, art. 8) · Recalentado de guisados: ≥74 °C durante 15 s en el centro, en menos de 1 hora (art. 30).<br>**Barra de salsas** — Reponer por tandas pequenas en recipiente limpio; PROHIBIDO rellenar sobre el resto anterior · Anotar hora de puesta en barra y hora de descarte de cada salsa cruda · Medir temperatura de pico de gallo, guacamole y crudas (≤4 °C) · Cambiar cucharas y pinzas por turno y registrarlo.<br>**Alérgenos** — Marcar la salsa macha como CACAHUETE y/o SESAMO y separarla fisicamente · Separar tortilla de maiz (sin gluten) de tortilla de harina: freidora, pinzas y superficie distintas · Revisar fichas de alergenos de los moles (frutos de cascara, sesamo) · Registrar cada cambio de proveedor o de receta que altere la ficha |
| **04** | `04-nixtamal-tortilla-guisados.xlsx` | `Instrucciones` · `Nixtamal y Molienda` · `Tortilla y Comal` · `Guisados y Rotacion` | **Nixtamal** — Pesar maiz y cal, anotar proporcion y hora de inicio de la coccion · Registrar tiempo de reposo y hora de lavado · Limpiar y desinfectar el molino antes y despues de cada molienda (punto critico) · Anotar rendimiento: kg de maiz → kg de masa → nº de tortillas.<br>**Tortilla** — Calibrar la tortilladora (grosor y peso por pieza) al arranque · Anotar mermas de tortilla por turno · Recepcion de tortilla comprada: proveedor, lote, fecha y temperatura.<br>**Guisados** — Anotar hora de elaboracion, hora de entrada en bano maria y hora limite de cada guisado · Verificar ≥63 °C con dos lecturas por turno · Etiquetar y abatir el sobrante apto, descartar el no apto y anotar merma |
| **05** | `05-tareas-manager.xlsx` | `Instrucciones` · `Tareas Diarias Manager` · `Tareas Semanales Manager` | **Diarias** — Arqueo y cuadre de caja y reparto de propinas · Revisar la hoja de temperaturas firmada del turno anterior · Medir rendimiento del trompo del dia (kg montados → tacos servidos → ticket) · Revisar tiempos e incidencias de delivery · Responder resenas.<br>**Semanales** — Pedido al importador de chiles secos, masa y producto mexicano (con plazo de entrega) · Comparar precios de cerdo y res · Inventario de bebida, mezcal y tequila · Revisar escandallos de los 5 tacos mas vendidos · Planificar turnos y cerrar el registro de jornada |
| **06** | `06-tareas-perfiles.xlsx` | `Instrucciones` · `Taquero (Trompo)` · `Tortillera/o` · `Salsero/a` · `Plancha y Freidora` · `Mostrador y Caja` | Una hoja por perfil, con el núcleo de §7.1. Ej. **Salsero/a**: Tostar y moler chiles del dia · Elaborar salsas cocidas y etiquetar con hora · Montar barra de salsas y comprobar ≤4 °C · Reponer por tandas, con recipiente limpio · Descartar crudas al cierre y anotar merma |
| **07** | `07-semanales-mensuales.xlsx` | `Instrucciones` · `Tareas Semanales` · `Tareas Mensuales` | **Semanales** — Desengrase profundo del asador vertical y de la campana · Afilado de cuchillos de corte · Limpieza a fondo del molino y de la tortilladora · Inventario de chiles secos y control de plagas en almacen seco · Formacion de 15 minutos al equipo.<br>**Mensuales** — Revision de la instalacion de gas del asador y del comal · Calibracion de sondas y termometros · Revision del plan APPCC y de las fichas de alergenos · Auditoria de proveedores de importacion · Limpieza de filtros de extraccion, con registro |
| **08** | `08-eventos-estacionales.xlsx` | `Instrucciones` · `Calendario de Eventos` · `Temporadas y Producto` | **Eventos** — Candelaria (2-feb, tamales) · Cuaresma y Vigilia (tacos de pescado, capeados) · Cinco de Mayo (**fiesta sobre todo de EE. UU.**) · Grito e Independencia (15-16 sep) · Dia de Muertos (1-2 nov) · Posadas y Navidad.<br>**Temporadas** — Chiles en nogada (15-jul a finales de sep) · Campana de chile seco · Precio y disponibilidad del aguacate · Cerdo para pastor |
| **09** | `09-plantilla-personalizable.xlsx` | `Instrucciones` · `Plantilla en Blanco` | Misma rejilla `Nº / Tarea / Zona / Responsable / Hora Limite / ✓ / Firma`, vacía, para que el comprador cree checklists del formato exacto de su taqueria (de barrio, gourmet, con tortilleria, cantina) |
| **B1** | `BONUS-01-briefing-servicio.xlsx` | `Instrucciones` · `Briefing Pre-Servicio` | Trompo del dia: peso montado, hora de montaje y prevision de cortes · Guisados del dia y hora limite de cada uno · Salsas del dia, nivel de picante y **aviso de alergenos (macha = cacahuete/sesamo)** · Roturas de stock y «86» (sin tortilla de harina, sin cochinita...) · Reservas, grupos y prevision de delivery |
| **B2** | `BONUS-02-calendario-anual.xlsx` | `Instrucciones` · `Calendario Anual` | 12 meses con eventos (§7.3), temporadas de producto, mantenimientos (gas del asador, campana, molino, sondas), formacion del equipo y cierres por vacaciones |

### 8.2 Variante considerada y descartada

**Alternativa:** `02-trompo`, `03-nixtamal-tortilla`, `04-salsas-guisados-appcc`.
**Descartada [estimado]** porque el fichero regulatorio quedaría el último y mezclado con producción, mientras que en el molde del sushi-bar el APPCC ocupa el **03** (`03-seguridad-anisakis-appcc`). Mantener el APPCC en el 03 conserva el paralelismo de la familia y deja la **barra de salsas —el punto de mayor riesgo del formato— dentro del fichero que el inspector pide primero**.

---

## 9. Marco español, mercado hispano: vocabulario

**Regla de la casa** (`feedback_productos-marco-espanol-mercado-hispano`): la base normativa es **española** (RD 1021/2022, RD 126/2015, ET art. 34.9); el comprador puede estar en España, México, EE. UU. hispano o Colombia y adapta. El vocabulario, por tanto, tiene que ser **neutro con glosa**, no mexicano cerrado ni español cerrado.

### 9.1 Términos que hay que glosar la primera vez

| Término | Problema | Cómo escribirlo |
|---|---|---|
| **trompo** | En España no se entiende; se asocia a la peonza | **«trompo (asador vertical)»** la primera vez, luego «trompo» |
| **tortillería** | En España se lee «sitio donde hacen tortilla de patata» | **«tortillería (obrador de tortilla de maíz)»** |
| **guisados** | En México son los rellenos de cazuela; en España «guiso» es otra cosa | **«guisados (cazuelas de relleno)»** |
| **nixtamal / masa nixtamalizada** | Desconocido fuera de México | Glosar una vez en la hoja `Instrucciones` del 04 |
| **salsero/a** | Puesto claro en México, borroso en España | **«salsero/a (responsable de salsas)»** |
| **macha** | Nombre de salsa que oculta un alérgeno | Siempre **«salsa macha (cacahuete y/o sésamo)»** en cualquier hoja de alérgenos |
| **APPCC** | En LATAM se dice HACCP | **«APPCC (HACCP)»** la primera vez de cada fichero |
| **escandallo** | En MX/LATAM es «costeo» | **«escandallo (costeo)»** |

### 9.2 Mexicanismos que SÍ se dejan tal cual

`taquero`, `comal`, `pastor`, `al pastor`, `trompo` (ya glosado), `aguachile`, `cochinita`, `carnitas`, `suadero`, `mole`, `pico de gallo`, `86` (la voz de «se acabó»). **Son el producto.** Traducirlos sería como traducir «itamae» en el kit de sushi.

### 9.3 Qué NO decir

- **«tex-mex»** — insulta al comprador mexicano y es un concepto distinto. Ni en la landing ni en los ficheros.
- **«gyro»** para el trompo — es griego. Sirve como comparación pedagógica para el lector español («funciona como un kebab o un gyro»), **nunca como sinónimo**.
- **«burrito» o «nachos» como plato central de taquería** — no lo son; son el estereotipo estadounidense.
- **«Cinco de Mayo» como fiesta nacional mexicana** — es principalmente estadounidense (ver §7.3).
- **«tortilla» a secas** en un texto para España — sin «de maíz» o «de harina» se lee tortilla de patata, y además la distinción es el **alérgeno**.
- **Importes en pesos** — el kit no lleva dinero, sólo tareas. Si en algún momento apareciera una cifra monetaria, va en euros.
- **«prueba gratis» / «plan gratuito» de AI Chef Pro** — el plan gratuito murió el 15-ago (memoria `feedback_aichef-pro-sin-plan-gratis-desde-10-euros`).

---

## 10. Precio y posicionamiento: 12 € frente a 14 €

### 10.1 Lo que dice cada fuente

- **Calendario**: `scripts/productos-digitales/CALENDARIO-V2-SEMANAL.md:281` → *«Tareas Recurrentes: Taquería Mexicana | Kits de tareas | 12 € | Q4 2026»* **[medido]**.
- **Precios vivos**: `netlify/shared/product-prices.ts:20-38` **[medido]** — 12 kits a 12 €, 5 a 14 €.

### 10.2 Qué separa de verdad los dos escalones

No es «étnico contra no étnico». Mirando los cuatro kits de 14 € distintos del base:

| Kit 14 € | Ficheros 02-03-04 propios | Capa técnica/regulatoria exclusiva |
|---|---|---|
| sushi-bar | `preparacion-arroz-pescado` · `seguridad-anisakis-appcc` · `barra-sushi-neta-case` | Anisakis (art. 8) + pH del arroz ≤4,6 |
| asador | `horno-josper-brasas` · `maduracion-despiece-carne` · `parrilla-pescados-verduras` | Maduración y despiece |
| marisquería | — | Molusco vivo, vivero, trazabilidad |
| tapas-bar | `barra-tapas-pinchos` · `cocina-raciones-platos` · `bebidas-cerveza-vino-vermut` | Barra de exposición + bebida |

Los de 12 € (cafetería, pizzería, hamburguesería, dark kitchen, food truck…) tienen operativa de restaurante **estándar**: lo específico es el equipo, no un proceso de obrador ni un riesgo sanitario propio.

### 10.3 Dónde cae la taquería

**Tres capas propias, no una:**

1. **Trompo** — perfil de riesgo del asador vertical (ACSA), sonda antes de cada tanda, la carne cortada a ≥63 °C.
2. **Nixtamal y tortillería** — un **obrador dentro del local**, con turno de madrugada y un punto crítico propio (el molino).
3. **Barra de salsas de autoservicio** — el mayor riesgo higiénico del formato **y** el punto de contacto del alérgeno cacahuete/sésamo.

Es **la misma carga técnica que el sushi-bar**, no la de una hamburguesería.

### 10.4 Recomendación **[estimado]**

**14 €.** Razones, en orden:

1. **Coherencia del escalón.** Dejar la taquería a 12 € al lado de `tapas-bar` a 14 € invita a la pregunta incómoda «¿por qué el de tapas vale más que el que lleva trompo, nixtamal y barra de salsas?». El escalón tiene una lógica legible (capa técnica propia) y la taquería está claramente dentro.
2. **Coste de producción.** El fichero 02 (trompo), el 03 (APPCC + salsas + alérgenos) y el 04 (nixtamal) son **tres ficheros nuevos de verdad**, no adaptaciones. No hay ahorro que justifique bajar.
3. **El delta es irrelevante para el comprador y no lo es para el catálogo.** Sobre un producto de 12-14 €, 2 € no mueven la conversión; sí mueven la percepción de que los kits tienen escalones con criterio.

**Si John prefiere respetar el calendario y dejarlo en 12 €**, el contenido **no se recorta**: la carga de trabajo es idéntica. Sólo hay que acordarse de que el par de precio tachado cambia: **14 € va con `priceOld: '€69'`** (`kit-tareas-sushi-bar.ts:353`) y **12 € va con `priceOld: '€39'`** (`kit-tareas-food-truck.ts:353`) **[medido]**. Mezclarlos rompe el `-80 %` del badge.

### 10.5 Posicionamiento de la landing **[estimado]**

- **Ángulo**: «el manual de operaciones de una taquería, pero en hojas que se firman cada turno». La SERP mexicana de `manual de operaciones taqueria` está ocupada por trabajos de clase en Scribd (§1.3): ese contraste es el argumento.
- **Gancho medible**: el **rendimiento del trompo**. Cinco de las nueve preguntas del People Also Ask son de rendimiento (§1.2), y una es literalmente «¿cuántos tacos salen de un trompo de 10 kilos?».
- **Meter el BONUS-02 arriba**: `"calendario anual de tareas"` es la única consulta no-marca que ya posiciona a la familia (pos. 8,8, 0 clics) (§2.3).
- **Entradas de enlace obligatorias** (regla de cero huérfanas): hub `/productos-digitales` (convertir la tarjeta `comingSoon` de `ProductosDigitalesHubPage.astro:993`) · `/kit-tareas` y las fichas hermanas · `/guia-restaurante-mexicano` (cross-sell descendente) · el caso de uso `restaurante-mexicano` (`src/data/use-cases-content.es.ts:3580`, donde hoy no está) · las páginas pSEO mexicanas con tráfico real (`/abrir-restaurante/ciudad-de-mexico`, `/licencia-restaurante/monterrey`, `/abrir-restaurante/queretaro`) · banners en los posts `tacos-al-pastor-autenticos-receta-mexicana.md` y `23-moles-regionales-mexicanos-con-ia-guia-definitiva-con-cocina-mexicana-ai.md` **[medido]**.

---

## 11. Riesgos y preguntas para John

1. **¿12 € o 14 €?** El calendario dice 12 (`CALENDARIO-V2-SEMANAL.md:281`), pero la taquería tiene tres capas técnicas propias (trompo, nixtamal, barra de salsas) y el escalón de 14 € es justo el de los kits con capa propia: sushi-bar, asador, marisquería, tapas-bar. **Recomiendo 14 €** (§10). Sea cual sea, hay que emparejar el `priceOld` correcto (€69 / €39).

2. **¿La taquería entra en el Mega Pack?** Hoy el Mega Pack vende «13 kits» (`src/data/products-catalog.ts:516`, `src/pages/MegaPackTareas.tsx:43-134`) y hay **19 LIVE**: ya hay 6 kits fuera (sushi-bar, asador, marisquería, tapas-bar, food-truck, panadería). Si entra la taquería, hay que decidir qué pasa con esos 6, y actualizar precio, copy, JSON-LD, `sticky` y dashboard. La decisión ya estaba anotada como pendiente en `CALENDARIO-V2-SEMANAL.md:311`.

3. **¿Cómo se diferencia del BONUS 2 de la Guía Restaurante Mexicano?** Ese bonus se llama «Manual de Operaciones Mexicano» (39 €) y promete «apertura, cierre, servicio, preparación de salsas, delivery y eventos temáticos» (`guia-restaurante-mexicano.ts:124`). Es un `.docx` narrativo y el kit son hojas de turno, pero **el copy se solapa**. Propuesta: posicionar el kit como «las hojas que ejecutan ese manual» y cross-linkear en las dos fichas. ¿OK, o prefieres tocar el bonus?

4. **¿El fichero 02 asume trompo?** Muchas taquerías en España no tienen asador vertical. Si el 02 se llama sólo «trompo al pastor», a esa mitad de la clientela le sobra un fichero de 11. **Recomiendo `02-trompo-pastor-plancha-comal`**, de forma que quien no tenga trompo siga usando la hoja para plancha y comal. ¿Conforme?

5. **Riesgo de corpus, fuera del alcance de este producto**: el registro horario **digital NO es obligatorio todavía** (el RD seguía sin publicarse en el BOE a mediados de 2026, §5.6), y hay copy vivo que ya lo afirma: `guia-panaderia-obrador.ts:75` («Requisitos Legales España 2026: … + control horario digital») y el testimonio de `:105` («el control horario digital 2026»). ¿Lo barremos en una sesión aparte?

---

## Anexo — Comandos ejecutados (reproducibles)

```bash
# Volúmenes
DATAFORSEO_ENV=/Users/johnguerrero/chefbusiness-astro/.env /usr/bin/python3 \
  scripts/dataforseo.py vol "taqueria mexicana" "taquería mexicana" "montar una taqueria" \
  "abrir una taqueria" "checklist taqueria" "tareas taqueria" "manual de operaciones taqueria" \
  "taqueria en españa" "taco al pastor receta" "taqueria" "tacos mexicanos" "comida mexicana" "pizza"
#   … --pais 2484 --idioma es   (México)
#   … --pais 2840 --idioma es   (EE. UU. en español)

# SERP
… scripts/dataforseo.py serp "montar una taqueria"
… scripts/dataforseo.py serp "manual de operaciones taqueria" --pais 2484 --idioma es

# Estructura de los xlsx sin abrir Excel (Mac con restricción térmica)
unzip -p astro-site/public/dl/kit-tareas-sushi-bar/01-apertura-cierre-sushi.xlsx xl/workbook.xml
unzip -p astro-site/public/dl/kit-tareas-sushi-bar/01-apertura-cierre-sushi.xlsx xl/worksheets/sheet2.xml
```

**Nota de entorno:** `openpyxl` **no está instalado** en el `/usr/bin/python3` del Mac. La inspección de los `.xlsx` se hizo con `unzip -p` sobre el XML interno, que además es más ligero térmicamente.
