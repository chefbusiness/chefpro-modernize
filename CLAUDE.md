# Instrucciones del proyecto — aichef.pro (chefpro-modernize)

## 🚨 REGLA CAPITAL — Generación de contenidos (BLOQUEANTE)

Aplica a **cualquier** contenido (artículo, landing, ficha de producto, post, página) en este o cualquier proyecto del grupo ChefBusiness. **Antes de escribir la primera línea:**

1. **Keyword research + análisis SERP PRIMERO.** Nunca escribir sin investigar keywords e inspeccionar la SERP de Google del/los mercado(s) objetivo. Lo que dicte la SERP (formatos, People Also Ask, entidades, intención) manda sobre lo que se incluye.
2. **Texto → `bridge.py`.** Motor de redacción. Desde el **2026-08-08 TODAS las tareas** (`content`, `translation`, `meta`, `social`, `analysis`, `email`, `report`, `quick`, `code`) apuntan a un único slug: **`~deepseek/deepseek-v4-flash-latest`**. La `~` es un alias de OpenRouter que resuelve siempre a la última revisión, así que ya no hay que actualizar el routing a mano. Gotcha: es modelo de razonamiento y verboso → **`--max-tokens` ≥ 8000** o devuelve vacío (el default ya es 8192, y ahora falla con código 3 en vez de escribir un `.txt` vacío). **La ruta depende de la máquina** (este repo se trabaja desde el Mac y desde el VPS):
   - VPS: `/root/chefbusiness-ai/bridge.py` — ejecutar con su venv: `/root/chefbusiness-ai/.venv/bin/python`
   - Mac: `/Users/johnguerrero/chefbusiness-ai/bridge.py`
   En el mismo repo están `serp_research.py` (research SERP previo) y `gsc_report.py`.
3. **Imágenes → skill `generate-images` (Gemini "Nano Banana 2").** Todas las imágenes del contenido.
4. **Contenido ENRIQUECIDO obligatorio:** tablas, datos, métricas, citas, listados y comparaciones (cuando apliquen) + sección de **Preguntas Frecuentes (FAQ)** + lo que indique el análisis SERP.
5. **Imágenes dentro del cuerpo: mínimo 2.** Además, una **imagen destacada (featured) ÚNICA** que **no** se repite dentro del contenido.
6. **Ortografía y semántica perfectas; tono amigable y humano** (no corporativo, no robótico).

> Un contenido sin research/SERP previo, o sin tablas/datos/FAQ/≥2 imágenes + destacada única, **no está terminado**.

### ⚠️ El punto 2 tiene matiz: el MODELO se elige por tipo de contenido (John, 2026-08-08)

`bridge.py` sigue siendo la vía por defecto —es mucho más barato— pero **DeepSeek no vale para todo**, y la decisión de qué motor usar es de criterio, no automática. `bridge.py` acepta `--model` con cualquier slug de OpenRouter, así que cambiar de motor es un parámetro.

**Donde NO vale, medido:** las **librerías de prompts por agente**. Son tablas de 105 prompts que el lector **copia y pega tal cual** en la plataforma, y ahí un desliz no se lee: se ejecuta. Dos defectos reales encontrados el 2026-08-08:

- **Caracteres CJK inyectados en mitad de la frase.** En `fermentus-ai` había **24 inyecciones** —frases chinas enteras—, entre ellas «鬼笔鹅膏菌提取物替代» dentro de un prompt de garum: 鬼笔鹅膏菌 es ***Amanita phalloides***, la seta más venenosa que existe, donde debía decir «en sustitución de la fermentación bacteriana». También «但是 (dulce/animal)» (但是 = «pero») y «历代 (jengibre fresco)» (历代 = «dinastías sucesivas»). Más `consultor-gastronomico` («가스» = gas en coreano) y, en el blog inglés, `customer-retention-strategies-restaurants` («what惊喜 (surprise) might come»). **Los tres estaban vivos en producción.**
- **Fechas caducas:** 41 menciones a años pasados, casi todas «precios HORECA de mayo de 2025» en prompts de escandallo — pidiendo precios de hace 15 meses y contradiciendo al propio agente.

**Qué se hizo, y por qué las dos cosas:** `fase8c-libreria-assemble.py` usa ahora `MODELO = 'anthropic/claude-sonnet-4.6'` (sobreescribible con `--modelo`) **y** tiene `valida()`, que aborta con **cualquier** modelo ante caracteres no latinos o ante un año pasado a menos de 90 caracteres de lenguaje de precios. Cambiar de motor baja la probabilidad; sólo el gate la elimina. Ojo con el gate: su primera versión tumbó el bloque de historia por un «1982» legítimo — por eso mira la **ventana** alrededor del año y no el texto entero.

**Criterio general:** prosa larga y narrativa → `bridge.py` por defecto. Contenido que el usuario **copia y ejecuta** (prompts, comandos, fórmulas, tablas de parámetros) o donde un carácter suelto cambia el significado → modelo bueno + gate automático. Y sea cual sea el motor, **un barrido de caracteres no latinos antes de publicar** cuesta un `grep`.

**ACTUALIZACIÓN de esa misma tarde: el culpable era `deepseek-v4-pro`, y ya no está.** Las inyecciones CJK salían de `--task content`, que enrutaba a `deepseek-v4-pro` — el snapshot del **24-abr-2026**. Todo `bridge.py` pasó a **`~deepseek/deepseek-v4-flash-latest`** (hoy `flash-0731`, del 31-jul, *re-post-trained*). Contraintuitivo pero medido en Artificial Analysis: **flash puntúa 52 en el Intelligence Index y pro 45** (#3 y #6 de 101), va a 115,3 tok/s frente a 71,0 y cuesta $0.09/$0.18 contra $0.435/$0.87 — pese a tener 284B parámetros (13B activos) frente a los 1,6T (49B activos) de pro. **Lo más nuevo le gana a lo más grande; no dar por hecho que «pro» > «flash».**

**Y el gate bajó al bridge.** `bridge.py` trae ahora `guard_idioma()`: escanea el output buscando CJK, cirílico, hangul, árabe, hebreo y tailandés, avisa por stderr con el fragmento alrededor y aborta con código 2 si se pasa `--strict-lang`. La instrucción de pureza de idioma va en el system prompt **también en español** — las inyecciones de la Amanita aparecieron en contenido ES, no en una traducción. Verificado que no da falso positivo con `perché/è/più/già/così/può` ni con `¿`/`ñ`. **Esto no sustituye al `valida()` de `fase8c-libreria-assemble.py`**, que sigue con `anthropic/claude-sonnet-4.6`: esa decisión no se ha revertido.

**Contrapartida aceptada:** `deepseek-v4-flash` es **text-only**. El `google/gemini-3.5-flash` que servía `analysis`/`email` aceptaba imagen, vídeo, audio y ficheros. Ningún script mandaba imágenes, pero si hace falta analizar una captura, el override es `--model ~google/gemini-flash-latest`.

**El volumen puede estar midiendo una FALTA DE ORTOGRAFÍA.** `chile-crisp` figuraba en el roadmap con 10 búsquedas/mes, casi descartable. El término real es «**chili crisp**» con i: **480/mes en España** y 49.500 en EE.UU. en español — 48 veces más. El post escribe «chile crisp» diez veces y «chili» **cero**, así que competía por una cadena que nadie teclea. Cazado el 2026-08-02: **antes de sentenciar por volumen, probar las variantes de grafía del término**.

**Un censo del roadmap es una hipótesis, no un hecho.** En la tanda 3 de 8D el research refutó **3 de los 4** posts del censo: el descartable era el más rentable (`yuzu-kosho`, ya en pos. 9,7-11,7), el «canibalizado» no canibalizaba (`coccion-a-baja-temperatura`: solape de SERP 2/17 y PAA cero frente a sous-vide) y el de volumen cero lo tenía por una errata. Los censos se escriben con los datos de ese día.

**Ojo al leer posiciones en GSC: suelen ser de la URL LEGACY.** El histórico de `mise-en-place` (posiciones 46-94) colgaba entero de `blog.aichef.pro/mise-en-place/`, ya 301-eada; la URL migrada no aparecía en ninguna fila. Confundirlas hace creer que hay un suelo donde se arranca de cero.

**Y esa trampa ya ha decidido mal una consolidación.** El 2026-08-04 el roadmap mandaba 301-ear `tecnicas-de-coccion-al-vacio-sous-vide` «porque pierde 85,6 contra 40,3». Las dos posiciones eran del subdominio legacy; las URLs migradas del clúster sumaban **8 impresiones y 0 clics en 90 días** (comprobado el 2026-08-08; en su día escribí 4, que era una lectura mal filtrada — los 0 clics sí eran correctos y son lo que sostiene la decisión). Comparando encabezados uno a uno, el duplicado real era otro (`sous-vide-avanzado`, el mismo guion que el pilar escrito dos veces) y **el post condenado era el único con contenido propio** — se habría borrado la taxonomía LTLT/HTST y dos infografías en PDF que no enlazaba nadie más. Regla: **antes de borrar, comparar los ENCABEZADOS de los candidatos**; una posición de GSC no dice quién duplica a quién, y menos si es de una URL que ya no existe.

**Antes de AMPLIAR un post existente, comprobar canibalización.** El research no solo dice qué escribir: a veces dice que NO escribas. El 2026-08-01, ampliar `que-es-el-food-pairing` parecía obvio (421 palabras, 590 búsquedas/mes) hasta ver que existe un `manual-del-food-pairing` de 3.643 palabras cuyo primer `<h2>` es literalmente «¿Qué es el Food Pairing?» — y que **el glosario corto rankea MEJOR que el manual largo** (pos. 41 y 9 frente a 84). Inflarlo habría enfrentado dos páginas propias por la misma keyword. Se amplió como página de DEFINICIÓN, cediendo la profundidad al manual con enlace explícito. El chequeo son dos consultas: `ls` de posts con el término en el slug, y GSC agrupando por `page,query`.

Referencia de longitud medida en el blog (2026-08-01): **mediana del glosario 1.285 palabras**, mediana del resto **2.661**. Por debajo de ~400 el post no compite ni siendo glosario.

## Stack y notas operativas

> ⚠️ Actualizado 2026-07-28. **Desde el cutover de Fase 7 (2026-07-19) producción sirve ASTRO**, no la SPA. Lo que se construye y despliega es `astro-site/`; la SPA de la raíz sobrevive sólo como fuente de los islands React de la zona app (decisión D5) y **ya no se construye**. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (§8 = log por sesión).

- **Stack real**: Astro 5 en `astro-site/` (build `cd astro-site && npm install && npm run build`, publish `astro-site/dist`) + Tailwind + Netlify con auto-deploy desde `main`. La SPA React 18 + Vite de la raíz aporta los componentes cross-root que los islands importan.
- **i18n**: 7 idiomas (es, en, fr, de, it, pt, nl). **El séptimo es NEERLANDÉS, no catalán** (error recurrente en contenidos).
- **Live**: https://aichef.pro · blog ES en https://aichef.pro/blog (322 posts; `blog.aichef.pro` 301-ea desde el cutover 8B.5) · **blog EN en https://aichef.pro/en/blog** (**65 posts**: los 39 de la Fase 8B.6 más 26 de las tandas 8C del 2026-08-01; contados en el sitemap de producción el 2026-08-08). El mapa 301 de `enblog.aichef.pro` ya está en `_redirects` pero **no se ejecuta hasta que el subdominio sea alias del site en Netlify + DNS**; mientras tanto ese WordPress sigue vivo. **Tarea pendiente de John, con la trampa de las A records de Hostinger y la batería de verificación: `CUTOVER_ENBLOG_PENDIENTE.md` (recordárselo).**
- **SEO**: meta/hreflang/JSON-LD **nativos server-side** en `BaseLayout.astro` + `SEOHead` de la SPA para los islands. La edge function `netlify/edge-functions/og-meta.ts` está **MUERTA** (no declarada desde Fase 7) y `public/sitemap.xml` ya **no** es la fuente: el sitemap lo genera Astro (`sitemap-index.xml`, 1.091 URLs) con lastmod real por post desde `astro-site/src/lib/blog-lastmod.json`. GSC: `sc-domain:aichef.pro`.
- **Verificación**: gates en `scripts/astro-migration/` (`fase8b-gate.py` blog, `fase6-gate.py <url>` marketing —sin argumento corre modo staging obsoleto—, `fase5-gate-s1-s2.py` zona app) + `fase7-vigilancia.py` (salud de producción post-cutover).
- **Entorno**: el repo se trabaja desde el Mac **y** desde un VPS Linux. En el VPS no aplican las restricciones térmicas del Mac: se pueden hacer builds locales y usar Playwright. Ojo con las rutas absolutas de `~/` que hay en documentos antiguos.

### Medición: Google Ads y consentimiento (desde 2026-08-03)

- **Hasta esta fecha el sitio no tenía NINGÚN tag** —ni analítica ni publicidad—.
  Ahora `AW-17829651892` con **Consent Mode v2** (denegado por defecto) y banner
  de cookies en los 7 idiomas: `astro-site/src/components/GoogleTag.astro` y
  `CookieConsent.astro`, montados en `BaseLayout.astro`. El bloque de
  consentimiento va **síncrono y ANTES** del loader async de gtag.js; invertirlo
  sembraría cookies publicitarias antes de leer el default denegado.
- **La decisión de consentimiento va en COOKIE sobre `.aichef.pro`, no en
  `localStorage`**, que está aislado por origen: lo aceptado en `aichef.pro` no
  se leería en `app.aichef.pro` y el visitante llegaría a Pickaxe como si no
  hubiera decidido nada, justo donde se mide la conversión.
- **La conversión se mide en Pickaxe, no aquí.** `app.aichef.pro` es Pickaxe
  whitelabeleado (sobre Vercel). El alta es un **modal**: NO existe «confirmation
  page» en el registro gratuito, así que el evento va en el campo **Body** del
  workspace. Y `?success=login` **no distingue registro de login** — lo que sí lo
  distingue es que el modal de alta es el único con **dos campos de contraseña**.
- No hace falta cross-domain linker: `aichef.pro` y `app.aichef.pro` comparten
  dominio registrable, así que `_gcl_aw` viaja sola.
- Docs: `GOOGLE_ADS_PICKAXE.md` (instalación) y `GOOGLE_ADS_GESTION.md` (gestión,
  qué NO tocar, y cómo montar un MCC para las otras marcas del grupo).
- ⚠️ **Antes de dar por buena cualquier campaña**: Objetivos → Conversiones →
  Resumen, y mirar el *Estado* de las acciones **principales**. La de aichef.pro
  llevaba tiempo optimizando hacia una **inactiva con 0,00 conversiones**.

### Gotchas del blog que cuestan dinero

- **Al BORRAR posts hay que limpiar `astro-site/.astro/` antes de construir.** La content collection de Astro 5 se cachea ahí y **sigue emitiendo el HTML de posts cuyo `.md` ya no existe**: tras consolidar 24 posts con 301, el build seguía generando 1.198 páginas y metiéndolos en el sitemap. Con `rm -rf astro-site/.astro astro-site/dist` bajó a 1.173, que es lo correcto. Cazado el 2026-07-28.
- **Y no cachea sólo la existencia del fichero: cachea el FRONTMATTER.** El 2026-08-04, fundir dos preguntas del `faq:` de un post dejó el `.md` con 11 y el `dist` **siguió emitiendo el `FAQPage` con las 12 viejas**, con el build en verde y sin un solo aviso. Las ediciones del CUERPO sí se veían en el mismo build, así que el fallo es especialmente traicionero: parece que el cambio se aplicó. Regla ampliada: **purgar `.astro` siempre que se toque el frontmatter** (`faq`, `title`, `description`, `image`…), no sólo al borrar posts. Y verificar el JSON-LD en el `dist`, no el `.md`.
- Tras CADA refresh de posts: `python3 scripts/astro-migration/fase8b-regen-lastmod.py` (el ensamblador actualiza el `modDate` del .md pero **no** toca `blog-lastmod.json`, del que vive el sitemap).
- **Los ensambladores RECONSTRUYEN el cuerpo entero desde el `.txt` de bridge, así que volver a correrlos sobre un post ya publicado PISA las ediciones manuales posteriores.** Aplica a `fase8d-ampliar-glosario.py` y a `fase8c-libreria-assemble.py`. Regenerar `cocina-molecular` para arreglarle las viñetas se llevó por delante los 2 enlaces internos que se le habían añadido a mano después, y el diff no canta: son dos líneas de párrafo que siguen ahí, sólo que sin el `<a>`. Antes de regenerar algo publicado: `diff <(git show HEAD:<fichero> | grep -o 'https://aichef\.pro/blog/[a-z0-9-]*' | sort) <(grep -o …)`. Cazado el 2026-08-01.
- Reglas nuevas en `astro-site/public/_redirects`: Netlify resuelve por **primera coincidencia**. Cualquier regla del subdominio `blog.aichef.pro` debe insertarse ANTES de la genérica `/:slug → /blog/:slug` (línea marcada con `# Genérica`), o no se ejecuta nunca.
- **La genérica `/:slug` se traga TODO lo que llegue con un solo segmento**, no sólo los posts. Cada familia de un segmento que no sea un post (archives de categoría —ese WP tiene la base vacía y las sirve en la raíz—, las 7 páginas del WordPress, sitemaps hijos, `robots.txt`, `favicon.ico`, archives de año) necesita su regla ANTES o se convierte en un **301 a un 404**. Pasó: 17 familias rotas descubiertas el 2026-07-28, 9 días después del cutover. Gate para que no vuelva a colarse: `python3 scripts/astro-migration/fase8b-auditar-301.py --sitio es|en` (simula el motor de Netlify contra el censo del export del WP y exige que el destino final exista en el `dist`; necesita build reciente). **Correrlo siempre que se toque `_redirects`.**
- Los commits de slices deben incluir `astro-site/public/blog-assets/`: los productores generan imágenes nuevas y un `git add` quirúrgico de `content/` las deja fuera → 404 en producción.
- **Nombres de agentes: la fuente autorizada es la PLATAFORMA, no el repo.** `src/lib/linkify-use-case.tsx`, `src/data/apps.ts` y el sitemap de la app son **vistas parciales** y contienen nombres desactualizados. El catálogo real (86 agentes ES / 77 EN, listados de Pickaxe el 2026-08-01) está volcado en `scripts/astro-migration/fase8c-agentes/catalogo-hub.json` y `agentes-en.json`.
- **Los CTA a Pickaxe no se verifican por código de estado: `ptapp`/`itapp`/etc. NO devuelven 404.** Un slug inventado (`/este-agente-no-existe-zzz99-pt`) sirve **200** con el mismo shell de la SPA y casi el mismo tamaño que uno real. La verificación válida es **buscar el nombre del agente dentro del HTML**. Y de paso: ese HTML trae **el catálogo completo embebido** —`formid`, `formtitle` y `formdescription` de todos los agentes—, que es mejor fuente que cualquier `.txt` de nombres. Volcado del portugués (53 agentes) en `.work/ptapp-agentes.json`. Cazado el 2026-08-22 verificando el CTA de la tanda 3 del blog PT.
- ⚠️ **Corrección de una afirmación que estuvo aquí y era falsa**: los recetarios del mundo SÍ se llaman `Cocina Mexicana`, `Cocina Peruana`… (no `Mexicana` a secas). Fiarme de esta línea me llevó a publicar 27 nombres mal en el hub. Ante la duda, pedir el listado de la plataforma.
- Enlaces internos del blog: la convención establecida es **absoluta** (`https://aichef.pro/blog/<slug>`), 2.278 usos frente a 28 relativos.
- **El blog es MULTI-IDIOMA desde 8B.6 y sus URLs sólo salen de los helpers de `astro-site/src/lib/blog.ts`** (`postPath`, `categoryPath`, `listPagePath`, `blogBase`). El ES va sin prefijo y con segmentos heredados de WP (`/blog/categoria/…`); el EN va con prefijo y segmentos nativos (`/en/blog/category/…`). Las categorías se resuelven SIEMPRE con idioma (`getCategory(slug, lang)`): `ai-chef-pro` existe en los dos.
- **En Header/Footer/Hero —que se pintan en los 7 idiomas— el hub del blog es `blogHubHref(lang)`, nunca `blogBase(lang)`**: sólo ES e EN tienen blog, así que `blogBase('fr')` daría `/fr/blog`, que es un 404. `blogHubHref` cae al ES para los idiomas sin blog propio.
- **El hub de LIBRERÍAS DE PROMPTS tiene su propio helper, `promptHubHref(lang)`** (`/libreria-de-prompts` · `/en/prompt-libraries`), y **no es la categoría del blog del mismo nombre**. El parecido ya costó un enlace roto: el footer inglés enseñaba la categoría `prompt-library` y el hub inglés estaba **huérfano** —nada en todo el sitio lo enlazaba— porque sólo vivía en la rama ES del componente. Por eso `Footer.astro` excluye esa categoría de la lista: con el hub presente serían dos entradas contiguas homónimas apuntando a sitios distintos. Recordar el plural de `prompt-libraries` (el filtro del sitemap se come todo lo acabado en `-library`).
- **El nombre del enlace debe coincidir con el de la página de destino.** El footer decía «Biblioteca de Prompts» apuntando a `/libreria-de-prompts`, y en inglés «Prompt Library» apuntando a «Prompt Libraries». Lo cazó John el 2026-08-03. Los textos salen de `src/i18n/locales/*.json` (**la SPA es la fuente única**: `astro-site/src/i18n/translations.ts` los importa por ruta relativa, no hay copia), así que se tocan ahí y valen para los dos footers.
- **⚠️ Un `<a>` dentro de una celda de tabla NO funciona: `html_tabla` escapa el HTML de las celdas** y el enlace se imprime literal (`<a href="…">roner</a>`) en mitad de la tabla. Bridge devuelve enlaces ahí de vez en cuando y **el diff no canta**. Los enlaces internos van en párrafos o viñetas; en la celda, texto plano. Cazado el 2026-08-04.
- **Los `.md` ensamblados llevan ESPACIO FINO (U+202F) antes de las unidades y GUION NO SEPARABLE (U+2011) en los rangos.** Cualquier script que los parchee tiene que referenciarlos **por escape** (`N = '\u202f'`, `G = '\u2011'`), nunca escribiendo el carácter: al pasar por un heredoc del shell degeneran en espacio y guion normales y **ninguna sustitución encuentra su patrón**. Si un parche «no encuentra» un texto que ves en el fichero, es esto.

### El catálogo de productos vendía la MITAD (2026-08-30)

Orden de John: el catálogo es la herramienta para vender los productos en los
contenidos, y **los banners tienen que cubrirlos todos, no siempre los mismos**.
Medido sobre los 198 banners publicados: **sólo 19 productos distintos de 44**;
`kit-escandallos` se llevaba 60 (el 30 %) y los cuatro primeros el 61 %.

Tres causas encadenadas, **ninguna daba error**:

1. **`src/data/products-catalog.ts` tenía 22 entradas y hay 44 landings vivas.**
   Los otros 22 eran imposibles de poner en un banner (el ensamblador aborta con
   «producto inexistente en el catálogo»). La fuente autorizada de nombre y
   precio de cada producto es su ficha en `astro-site/src/data/productos/`.
2. **⚠️ El parser del catálogo perdía entradas EN SILENCIO.**
   `fase8c-libreria-assemble.py` lee el `.ts` con un regex a mano.
   `kit-gestion-personal` lleva **comentarios entre `description: {` y `es:`**;
   el patrón exigía sólo espacios ahí, no casaba, y el `.*?` saltaba al
   `description:` de la **entrada siguiente**. Doble daño invisible: esa entrada
   se quedaba con la descripción de la siguiente, y **la siguiente desaparecía
   del catálogo**. Así llevaba `kit-inventario` invisible e invendible, y un
   banner nuevo de Gestión de Personal habría descrito el Kit de Inventario.
   Arreglado tolerando comentarios y prohibiendo cruzar al siguiente producto,
   **más un gate que aborta si el parser ve menos productos de los declarados**.
3. La elección era manual en cada config, y siempre caían los mismos.

**Ahora:** `rotar_productos()` permite **fijar** por relevancia temática (van
primero) y rellena el resto **rotando por todo el catálogo**, sembrado con el
slug del post → determinista, reejecutar no ensucia el diff. Simulado sobre los
325 posts ES: **44/44 cubiertos, el más usado del 30,3 % al 3,7 %**.

**La lección transversal: un parser hecho a mano sobre un fichero que otros
editan pierde datos en silencio.** No falla, no avisa, y lo que desaparece es
dinero que no se factura. Cualquier parser así necesita un **gate de recuento
contra la fuente**.

### La política de 3 banners sólo la cumplía el 12 % del blog (2026-08-31)

Arreglar el catálogo el 30-ago dejó la rotación **en el generador**, no en el
blog. Medido sobre el `dist`: **39 de 325 posts ES** tenían banners; **286 no
tenían ninguno**, y el reparto publicado seguía siendo el viejo — 19 productos
de 44 con `kit-escandallos` en el 29,9 %. Un arreglo en el generador **no
retroactúa sobre lo ya publicado**: hay que pasar algo por el corpus.

**Y ese algo NO puede ser el ensamblador**: `fase8c-libreria-assemble.py`
reconstruye el cuerpo desde el `.txt` de bridge y pisa lo publicado. El
insertador quirúrgico es **`scripts/astro-migration/fase8e-banners-corpus.py`**
(dry-run por defecto, `--lang es|en`, `--informe`): sólo inserta, y lo demuestra
con un gate que **quita del resultado exactamente lo insertado y compara con el
original byte a byte**. Reutiliza `catalogo_productos()`, `rotar_productos()` y
`banner()` importando el ensamblador, para no duplicar su gate de recuento.

Resultado: ES **325/325 posts con 3 banners**, 44/44 productos, el más usado del
29,9 % al 7,1 %. EN 64/66. Enlaces internos a las landings huérfanas: de 3 a 24.

**Dos trampas que costaron una iteración cada una:**

- **Repartir por la longitud BRUTA coloca mal los banners.** Los bloques
  congelados de WordPress son hasta el 21 % del HTML, así que el «85 %» bruto
  puede caer detrás de todo el texto real. Se reparte por longitud **útil**
  (descontando esos tramos).
- **Una línea en blanco dentro de un `<div>` corta el bloque HTML de Markdown**
  y el resto se escaparía como texto. Por eso se exige balance 0 de
  contenedores en el punto de inserción. Esa guarda es también la red contra
  los bloques congelados que no conocemos.

**Hay un CUARTO molde, y está en el blog inglés.** `ai-restaurant-management-software`
y `ai-food-cost-calculator-reduce-costs` traen el cuerpo entero envuelto en
`<div class="hero">` / `<header class="post-header">`: no hay ni un punto a
nivel superior. Quedan **sin banners a propósito**, marcados por el script.

### ⚠️ `scripts/dataforseo.py` mide ESPAÑA por defecto y no lo dice

`LOC_ES, LANG_ES = 2724, 'es'`. Investigando el blog PT, la primera pasada dio
`garum` = 12.100 y `fermentação` = 10 — **un término del idioma objetivo con
volumen ridículo al lado de uno latino enorme es la firma de estar midiendo el
mercado equivocado**. El dato real en Portugal es 1.300: factor 9. **Para
cualquier blog que no sea el ES, `--pais` y `--idioma` explícitos, siempre.**

### `bridge.py` puede devolver VACÍO, y subir tokens no siempre lo arregla

La FAQ del post del garum volvió vacía con `--max-tokens 24000` **y otra vez con
48000** (21 minutos para decirlo); la del otro post de la misma tanda, mismo
formato, salió a la primera con 24000. **No es un umbral, es el prompt**: el del
garum llevaba umbrales regulatorios, taxonomía latina y dos reglamentos, y el
modelo de razonamiento se atasca. Se resolvió con
`--model anthropic/claude-sonnet-4.6` y **8192 tokens**, en menos de dos minutos.
**Si bridge devuelve vacío dos veces, no dupliques el presupuesto una tercera:
cambia de motor.**

### Tres gotchas de conteo que engañan (todos vistos el 30-ago)

- **`grep -o '<loc>' dist/sitemap-*.xml` cuenta también el `sitemap-index.xml`**,
  que tiene su propio `<loc>`. Daba 1190 donde había 1189.
- **`grep -c` en el sitemap servido cuenta LÍNEAS**, y el XML va en una sola:
  devolvía `1`. Ocurrencias = `grep -o … | wc -l`.
- **Un `grep -o -E "[^<>]{0,60}(A|B|C)[^<>]{0,60}"`** sobre un HTML de 13 KB
  agota los 120 s por backtracking catastrófico. Para sacar contexto alrededor
  de una aguja, Python con `re.finditer` y rebanadas.

### Nombres de agentes: el bloque de hotelería va en inglés SIEMPRE

- Los 12 agentes de hotelería (Hotel Staff Meal Planner, Room Service Menu Designer, Banquet Event Order AI, F&B Reporting Assistant, Buffet Master AI, In-Room Dining Optimizer, Outlet Concept Developer, Hotel F&B Cost Controller, Mini-Bar & Amenities AI, Hotel Pastry & Bakery Pro, Hotel Menu Engineering Pro, Hotel Bar & Lounge Menu AI) **se llaman igual en español que en inglés**. El inglés es la lengua franca del F&B hotelero premium; un director de A&B en España usa ese vocabulario a diario. **No traducirlos.**
- El resto de agentes SÍ tiene nombre propio por idioma y NO coinciden: `ID Alérgenos`→`Allergen ID`, `Mermas GenCal`→`Waste GenCal`, `Comida de Personal`→`Staff Meal`, `Cocina Creativa`→`Avant-garde Cuisine`, `Heladero Consultor Pro`→`Gelato & Ice Cream Consultant`… El mapa completo (26 pares) está en `scripts/astro-migration/fase8c-agentes/agentes-en.json`. **Usar el nombre del idioma que se publica**: un post inglés que hable de «ID Alérgenos» describe un agente que el lector no encuentra en su interfaz.
- `Chef Privado Pro` **no existe todavía en inglés** (pendiente de crear): no tiene versión EN.

### El corpus del blog tiene TRES moldes de HTML, no uno

Cazado el 2026-08-01 depurando por qué falló el piloto inglés. Cualquier script que parsee un `.md` del blog tiene que contar con esto o devolverá silencio (o basura, que es peor):

- **Molde nuevo** — lo que emite `fase8c-libreria-assemble.py`: etiquetas separadas por `\n`, FAQ en el **frontmatter**. Son 2 posts.
- **Molde WordPress** — los 25 heredados del export: etiquetas **pegadas** (`</h3><p>`), párrafos con `class="wp-block-paragraph"`, tips como `<h3>` + `<ul><li>`, y la FAQ **solo en el cuerpo** (`<h2>Preguntas Frecuentes…`), nunca en el frontmatter.
- **Molde WordPress antiguo** — 5 posts (`burger-pro-ai`, `catering-ai`, `food-pairing-ai`, `mermas-gencal`, `recetario-cocina-creativa-ai`): sin intro ni «Cómo utilizar» por bloque, tips en `<ul>` suelto o inexistentes, y 12-16 imágenes en el cuerpo en vez de 2.

**Dos trampas concretas, las dos con dinero detrás:**

1. **Un regex de sección SIN acotar la zona no falla: acierta en el sitio equivocado.** `<h3>(.*?)</h3><p>(.*?)</p>` lanzado sobre la sección de tips del molde WordPress no encuentra par ahí (los tips van en `<ul>`), así que `.*?` sigue 30 KB hacia abajo y caza el primer par **de la FAQ**. Devuelve 10 resultados, parece que funciona, y lo que alimenta al modelo es la FAQ disfrazada de tips. **Acotar siempre por sección antes de buscar dentro.**
2. **Un `<h1>` incrustado en el cuerpo esconde contenido.** 6 posts ES lo tienen (doble H1 con el del layout). En `recetario-cocina-creativa-ai` hay un bloque entero de 15 prompts bajo `<h1>`, y en `burger-pro-ai` es el encabezado de los tips: cualquier parser que trocee por `<h2>` los pierde sin avisar.

**El molde WordPress antiguo (5 posts) acumula además cinco peculiaridades**, todas descubiertas depurando una a una: el `<h2>Cómo utilizar` (en lugar de `<h3>`) que parte el bloque en dos, el `&nbsp;` pegado al final de ese encabezado, la variante en que ni siquiera es encabezado sino una entradilla en negrita **dentro** del párrafo, la FAQ como bloque de **Rank Math** (con un `<div>` entre pregunta y respuesta) y los tips colgando de un `<p><strong>` sin `<h3>`. Un regex por caso; no hay atajo.

**⚠️ Bloque «También te puede interesar» congelado dentro del cuerpo.** Esos mismos 5 posts llevan incrustado en MITAD del artículo un widget de relacionados heredado de WordPress: **el 20-25 % del HTML**, 7-9 imágenes y **siete `<h2>` falsos** que son títulos de posts (uno repetido cinco veces, apuntando a páginas pSEO de ciudades). `BlogPost.astro` ya pinta sus propios relacionados de la misma categoría, así que es **duplicación pura y además obsoleta**. Envenena cualquier censo: por su culpa estos posts parecían tener 12-16 imágenes cuando las suyas son 2-9. El generador inglés lo recorta con `_sin_relacionados()`; **en los posts ES sigue ahí**.

Gate: `python3 scripts/astro-migration/fase8c-libreria-en-gate.py --todos` compara el post inglés **contra el español** (paridad de prompts/tablas/imágenes, banners y UTM, hreflang recíproco en los dos lados, restos de español en cuerpo **y frontmatter**). Correrlo siempre antes de dar por buena una tanda.

Gate de H1: `python3 scripts/astro-migration/fase8c-h1-unico.py` (dry-run por defecto). El layout ya pinta el `title` como `<h1>`; el del cuerpo llega por **dos vías** —HTML crudo y Markdown `# `— y en **los dos idiomas**. Mirar una sola vía o una sola carpeta da falso verde: así se me escaparon 20 de 26.

Gate de enlaces: `python3 scripts/astro-migration/fase8c-enlaces-vivos.py` pregunta a producción por los ~195 destinos internos únicos del blog (4.100 enlaces deduplicados). **No se ven desde el repo**: son URLs absolutas a `aichef.pro` dentro del HTML de los posts. Cazó 10 rotos el 2026-08-01.

Gate de FAQ duplicadas: `python3 scripts/astro-migration/fase8d-faq-duplicadas.py --lang es|en|todos`. **Cada `q:` del frontmatter es una `Question` del `FAQPage`, y en un rich result cada una aparece SOLA**: dos formulaciones de la misma pregunta no sólo inflan el schema, es que sus respuestas están escritas para leerse en secuencia y una de las dos se queda sin decir nada. `chili-crisp` llegó a publicarse con **cuatro** variantes de «qué es» y una respuesta que abría con «Es exactamente lo mismo». Comparar por igualdad de cadena no sirve —los duplicados vienen de recoger varias formulaciones del **People Also Ask**, que difieren en tildes, artículos, orden y hasta en la grafía del término—, así que normaliza y cruza Jaccard con ratio de secuencia, en tres niveles (IDENTICA / DEFINICION / PARECIDA) porque el ruido es alto: dos preguntas del mismo tema comparten casi todo el vocabulario sin ser la misma. **Ojo, el `faq:` del frontmatter sólo lo tienen 93 de los 322 posts ES**; los otros 149 la llevan en el cuerpo (molde WordPress, en `<h3>` o en `<p><strong>`) y 80 no tienen FAQ. El script lee las dos vías y marca cuál emite schema. Corpus barrido y limpio el 2026-08-04.

### El export de WordPress dejó bloques CONGELADOS en el cuerpo — van tres familias

Bloques que en WordPress eran dinámicos y al exportar quedaron serializados como HTML muerto dentro del `.md`. No son contenido: son mobiliario del CMS anterior, y **cada uno se descubrió por casualidad investigando otra cosa**.

| Familia | Alcance | Qué hacía |
|---|---|---|
| `wp-block-blocksy-query` («También te puede interesar») | 15 posts | Duplicaba los relacionados del layout, 7-8 `<h2>` falsos, 3 destinos 404. En 4 posts, **sin título ninguno** |
| `wp-block-jetpack-donations` | **35 posts** | «Haz una donación única/mensual/anual» en el blog de un SaaS, con botones «Donar» **sin `href`**. 105 encabezados falsos |
| CTA de newsletter | 1 post | A un `/newsletter` que da 404, afirmando «+2.500 chefs ya reciben nuestro contenido exclusivo» — y el formulario del pie está **desconectado** en el código (`Footer.astro`: «no wired») |
| `wp-block-group` «CHEFBUSINESS GROUP» | **62 posts** | Enlaces a las marcas hermanas (GastroSEO, GastroLocal, Hosply, Ingredients Index…), 1.809 bytes fijos. **NO es basura** —son marcas de John, con UTM— y por eso **no se toca sin su visto bueno**. Pero **infla los censos de palabras**: en los glosarios delgados es hasta el **21 % del HTML** (`chile-crisp` tiene 263 palabras reales, no 331). Y **`ingredientsindex.pro` tiene el TLS roto**, así que esos 62 posts enlazan a un aviso de seguridad |

**Asume que hay una quinta.** Cuando algo no cuadre (un censo de imágenes desmadrado, encabezados repetidos, palabras que no aparecen en pantalla), `grep -rl "wp-block-" astro-site/src/content/blog/` antes que nada. Gates: `fase8c-quitar-relacionados.py` y `fase8c-restos-wordpress.py`, los dos con dry-run por defecto.

**Se delimitan por firma ESTRUCTURAL, nunca adivinando dónde acaban.** El primer intento cortaba «hasta la siguiente sección conocida» y se tragó la FAQ entera de `que-es-el-food-pairing`, que escribe «Preguntas **f**recuentes» en minúscula. Lo que ata principio y fin es el `data-id` del `<div>` con su `<style>` de cierre.

### Dos trampas del `BaseLayout` y del sitemap

- **`basePath` va SIN el prefijo de idioma.** `urlFor()` ya antepone `/${lang}` a los idiomas no por defecto, así que pasar `/en/prompt-library` da un canonical `/en/en/prompt-library`. Se pasa `/prompt-libraries` y el layout compone.
- **El filtro del sitemap excluye las rutas de la zona de pago (`-access`, `-library`)**, que nunca deben indexarse. Hasta el 2026-08-27 el test era un `endsWith()` a secas y una página pública cuyo slug acabase así **desaparecía del sitemap sin un solo aviso** — le pasó al hub inglés, que nació como `/en/prompt-library` y se renombró a `/en/prompt-libraries`, y después a la categoría `/en/blog/category/prompt-library`. Ahora el test es `/^\/[^/]+-(access|library)$/`: la zona app es SIEMPRE de un solo segmento en la raíz, así que el blog ya no puede caer dentro.

### ⚠️ El comodín de `robots.txt` no significa «acaba en» — borró 26 posts ingleses

Cazado el **2026-08-27** revisando en GSC por qué los posts ingleses de librerías de prompts no aparecían. `astro-site/public/robots.txt` protegía la zona app con `Disallow: /*-access` y `Disallow: /*-library`. **En robots.txt un patrón SIN `$` casa por PREFIJO una vez expandido el comodín**: `/*-library` no quiere decir «rutas que acaban en `-library`», sino «`/` + lo que sea + `-library` + lo que venga después». Casaba con `/en/blog/prompt-library-barista-consulting` y con los otros 25, más la categoría `/en/blog/category/prompt-library`.

Resultado, medido en GSC: **27 URLs sin poder rastrearse desde el 1 de agosto** («Blocked by robots.txt» en la que Google llegó a intentar, «URL is unknown to Google» / «Discovered - currently not indexed» en el resto, *last crawled: Never* en las 26), mientras sus **gemelas españolas estaban indexadas**. El sitemap las declaraba correctamente y el build salía verde: **un bloqueo de robots.txt no rompe nada, no sale en ningún diff y no da ningún aviso**.

- Las reglas van ahora ancladas al **prefijo de cada familia de producto** (`/kit-*-library`, `/guia-*-access`…): ninguna URL del blog empieza por `/kit-` ni `/guia-`, así que no puede volver a rozarlas. Las 88 páginas de la zona app son de un solo segmento y empiezan por `guia- kit- mega- pack- plan- pro-`; **si nace una familia con otro prefijo hay que añadir sus dos líneas**. Sin ancla final `$` a propósito: con ella se escapaban `/kit-escandallos-library/` y `?x=1`.
- La protección de verdad de esas 88 no es el `robots.txt`: es el **`noindex` del HTML** (las 88 lo llevan) más la exclusión del sitemap. Bloquear por robots impide justamente que Google lea el `noindex`.
- Gate: **`python3 scripts/astro-migration/robots-gate.py`** — implementa la spec de Google (comodín, `$`, gana el path más largo y en empate Allow; validado contra Protego en 6.445 decisiones) y comprueba, para cada user-agent del fichero, que **toda URL del `dist/` es rastreable** y que **toda ruta de la zona app está bloqueada**. Con el `robots.txt` viejo canta las 27; con el nuevo, cero. **Correrlo siempre que se toque `robots.txt` o nazca una familia de producto.**
- Regla general: **al publicar contenido nuevo, comprobar que su URL no cae en ningún patrón de `robots.txt`**. Cuesta un comando y aquí ha costado casi un mes de indexación de 26 posts.

### El widget de WhatsApp lo pinta el LAYOUT, no cada página (2026-09-03)

John lo cazó a ojo: estaba en las home y en poco más. Medido sobre el `dist`:
**655 de 1.312 páginas**. Faltaba en el **blog entero** (ES + EN), `/precios`,
`/contacto`, el hub de librerías, los legales y los **44 gates de acceso** — o
sea, justo donde llega el tráfico de SEO. No fallaba nada: cada página lo
montaba **a mano** y a nadie se le ocurrió que faltase.

Ahora lo pinta `BaseLayout.astro` para todo el sitio. Lo que hay que saber antes
de tocarlo es que **existen TRES implementaciones del mismo botón** y por eso el
riesgo al centralizarlo no era la falta, era el **duplicado**:

| Implementación | Dónde | Por qué es distinta |
|---|---|---|
| `components/WhatsAppFloatingButton.astro` | **global, en `BaseLayout`** | `aria-label` del i18n (7 idiomas), `bottom-6` |
| `<a>` inline en las 7 plantillas de landing | 45 landings de producto | mensaje **prerellenado** de soporte + `bottom-20` en móvil para no quedar debajo de su barra sticky |
| `WhatsAppProductSupport` (React) | 44 dashboards `-library` | va dentro de un island `client:only`, **no está en el HTML** |

Esas 89 páginas pasan **`whatsapp={false}`** a `BaseLayout` o saldrían **dos
botones superpuestos**, con doble animación y sin un solo aviso en el build.
La plantilla de `fase5-generate-zona-app.py` ya lo emite (los `-library` son
generados: editar el generador, no el fichero).

**Y el banner de cookies lo tapaba.** Es `fixed bottom-0` a lo ancho con
z-index 100, así que en la primera visita se comía el botón de la esquina — en
todo el sitio, no sólo donde acababa de aparecer. `CookieConsent.astro` publica
ahora su **altura real** en `--aichef-cookie-h` (medida, no un número fijo: son
~90 px en escritorio y ~190 px en móvil, y cambia con el idioma) y `global.css`
aparta con `transform` **todos** los flotantes de WhatsApp. Se desplaza en vez de
reescribir `bottom` porque las tres variantes tienen anclajes distintos y un
desplazamiento relativo respeta el de cada una; al decidir vuelven a su sitio.

**Gate: `python3 scripts/astro-migration/whatsapp-gate.py`** — exige exactamente
1 botón flotante por página del `dist` y que las únicas 44 sin él sean los
dashboards. Correrlo al tocar el layout, las landings o la zona app. Probado
contra 4 defectos inyectados a mano: los caza los 4 (uno de ellos sólo tras
arreglar que `fr.html` se leía como española — con `build.format: 'file'` la
portada de cada idioma **no** es `fr/index.html`).

### Banners de productos digitales: política obligatoria

- **Todo contenido que se genere lleva MÍNIMO 3 banners de productos digitales, a tres alturas del artículo.** Instrucción de John (2026-07-31): es la línea de negocio más desatendida y hay que desplegarla.
- Son **pago único con acceso vitalicio** a un dashboard, no la suscripción recurrente del SaaS. El banner lo dice explícitamente: es lo que los diferencia.
- Datos **siempre** desde `src/data/products-catalog.ts` (**44 productos**, 9-89 €). Nunca duplicar nombre o precio en el contenido: los precios cambian.
- Elegir por **relevancia temática** con el post. Paleta `accent` (el CTA de la app usa `primary`) para que no se confundan, y UTM `utm_source=blog&utm_medium=banner&utm_content=<slug>` para poder medir qué post vende.
- El generador `fase8c-libreria-assemble.py` aborta si la config trae menos de 3 productos.

### Librerías de prompts por agente: qué son y qué NO son

- Son **valor agregado de producto** para quien **ya usa AI Chef Pro** (de pago o gratuito) y entra al blog a sacarle más partido. **No se miden por tráfico SEO.** Criterio de John, 2026-07-31.
- Medido con DataForSEO: la intención "prompts" tiene **volumen cero** en España. Con la vara del SEO estos posts parecerían inútiles y alguien podría proponer podarlos: sería un error de criterio.
- Prioridad: **cobertura** (que cada agente tenga la suya) y **utilidad real** de los prompts, por delante de las keywords. El research sigue valiendo para el título y para nutrir la FAQ con preguntas reales.
- Su canal de distribución es **interno**: el hub `/libreria-de-prompts` (que nunca se migró) y los enlaces desde la plataforma. Por eso importa la tarea pendiente de exponer públicamente los agentes nuevos.
- Las piezas de **captación** son otro tipo de contenido y sí se miden por tráfico (ejemplo detectado: `reglamento 1169/2011`, 1.600 búsquedas/mes, competencia baja, sin dueño en el grupo).

### Stack de research SEO (estado a 2026-07-31)

- **DataForSEO** es la fuente contratada para volúmenes y SERP. Basic Auth: `DATAFORSEO_LOGIN` (email) + `DATAFORSEO_PASSWORD` (la *API password* del panel), en `/root/chefbusiness-ai/.env` (permisos 600, gitignorado, fuera del repo público). **Ninguna credencial se commitea aquí.** Helper en el repo: `python3 scripts/dataforseo.py vol "kw1" "kw2"` y `python3 scripts/dataforseo.py serp "kw"` (resuelve el `.env` en Mac y VPS, marca si hay AI Overview y saca el People Also Ask, que es el guion de la FAQ).
- **El volumen sin SERP engaña.** «Qué es un token» son 1.600/mes… de **criptomonedas**: BBVA, Wikipedia, Fortinet y Kraken copan el top y la acepción de IA sólo asoma en las posiciones 10 y 13. Escribir para el volumen sin mirar la intención habría producido un post que no puede rankear jamás. Correr siempre `serp` antes de decidir el enfoque, no sólo `vol`.
- **MUERTAS**, comprobado: **Keywords Everywhere** devuelve volumen 0 hasta para "recetas" o "pizza" (la cuenta no sirve datos de GKP) y la **API de Brave** da `422 token inválido`. No perder tiempo con ellas sin renovarlas antes.
- **Empezar siempre por los datos propios**: GSC vía el MCP `gscServer` (`sc-domain:aichef.pro`). Antes de buscar demanda fuera, mirar qué activo propio ya posiciona para esa intención — es lo que evita canibalizar (en ID Alérgenos había uno en posición 9,1 al que no se podía pisar).
- Si no hay volúmenes fiables, **no se inventan cifras**: se trabaja con SERP directa + GSC y se dice qué no se pudo medir.

### ⚠️ Material propietario — ESTE REPO ES PÚBLICO

- `chefbusiness/chefpro-modernize` es **público**. Los **prompts core de los agentes** (el system prompt de Pickaxe que da vida a cada uno) son el producto en sí: **no se commitean aquí, ni en el contenido del blog, ni en un `.astro`**.
- John los comparte en la conversación como material de trabajo: sirven para entender a qué se dedica el agente, cómo lo hace y qué no hace, y desde ahí generar el listado de prompts del usuario final. **No se almacenan** en ningún repo.
- En las páginas y en los posts se explica **qué hace el agente y cómo aprovecharlo**; **el prompt core no se publica jamás**.

### Reglas de marca (John, 2026-07-30)

- **YouTube oficial: `https://youtube.com/@aichefpro`** — nunca el canal personal de John (el pie enlazaba a una playlist suya; corregido en `Footer.astro` y en el gemelo `ModernFooter.tsx` de la SPA).
- **Toda mención con nombre de John enlaza a `https://johnguerrero.es`** con `target="_blank" rel="noopener noreferrer author"`. En JSON-LD, el `Person` lleva `url` = su marca personal y `sameAs` con marca + canal. Los `alt` de imagen no se enlazan.
- Las páginas de agente (8C) incrustarán **vídeos demo de Loom** cuando estén; no bloquean el arranque.
- Gotcha de `faq.astro`: el campo `a` se pinta como TEXTO PLANO y alimenta el FAQPage; el HTML con enlaces va en `aHtml` (plantilla con backticks). Meter markup en `a` lo escupe literal en la página.
