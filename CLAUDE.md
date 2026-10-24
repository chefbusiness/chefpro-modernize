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

### 🔴 Matiz del 2026-09-04 (John): `bridge.py` NO se usa para PRODUCTOS DIGITALES

Guías, bonus, planes, manuales y ejercicios: el texto lo escriben **subagentes Anthropic** (sonnet por defecto) a
partir del guion; el método (`dump_prompts.py` → un agente por bloque → `check_bloque.py`) y el motivo están en la
skill **`productos-digitales-aichef`**. **El blog y las landings de captación siguen con bridge.py.**

## Stack y notas operativas

> ⚠️ Actualizado 2026-07-28. **Desde el cutover de Fase 7 (2026-07-19) producción sirve ASTRO**, no la SPA. Lo que se construye y despliega es `astro-site/`; la SPA de la raíz sobrevive sólo como fuente de los islands React de la zona app (decisión D5) y **ya no se construye**. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (§8 = log por sesión).

- **Stack real**: Astro 5 en `astro-site/` (build y publish en `netlify.toml`) + Tailwind + Netlify con auto-deploy desde `main`. La SPA React 18 + Vite de la raíz aporta los componentes cross-root que los islands importan.
- **i18n**: 7 idiomas (es, en, fr, de, it, pt, nl). **El séptimo es NEERLANDÉS, no catalán** (error recurrente en contenidos).
- **Live**: https://aichef.pro · blog ES en https://aichef.pro/blog (`blog.aichef.pro` 301-ea desde el cutover 8B.5) · **blog EN en https://aichef.pro/en/blog**. El mapa 301 de `enblog.aichef.pro` ya está en `_redirects` pero **no se ejecuta hasta que el subdominio sea alias del site en Netlify + DNS**; mientras tanto ese WordPress sigue vivo. **Tarea pendiente de John, con la trampa de las A records de Hostinger y la batería de verificación: `CUTOVER_ENBLOG_PENDIENTE.md` (recordárselo).**
- **SEO**: meta/hreflang/JSON-LD **nativos server-side** en `BaseLayout.astro` + `SEOHead` de la SPA para los islands. La edge function `netlify/edge-functions/og-meta.ts` está **MUERTA** (no declarada desde Fase 7) y `public/sitemap.xml` ya **no** es la fuente: el sitemap lo genera Astro (`sitemap-index.xml`) con lastmod real por post desde `astro-site/src/lib/blog-lastmod.json`. GSC: `sc-domain:aichef.pro`.
- **Verificación**: gates en `scripts/astro-migration/` (`fase8b-gate.py` blog, `fase6-gate.py <url>` marketing —sin argumento corre modo staging obsoleto—, `fase5-gate-s1-s2.py` zona app) + `fase7-vigilancia.py` (salud de producción post-cutover).
- **Entorno**: el repo se trabaja desde el Mac **y** desde un VPS Linux. En el VPS no aplican las restricciones térmicas del Mac: se pueden hacer builds locales y usar Playwright. Ojo con las rutas absolutas de `~/` que hay en documentos antiguos.

## 📚 Detalle bajo demanda (movido el 2026-10-12 con /doctor)

Para no cargar ~14k tokens en cada sesión, el detalle de tres áreas vive ahora fuera de este fichero, **copiado literal**. Los no negociables siguen aquí, en una línea cada uno. **Los gotchas nuevos de estas áreas se añaden en su destino, no aquí** (si solo es un «nunca», una línea más abajo).

- **Blog, SEO y contenidos web** → skill local **`blog-aichef`** (`.claude/skills/blog-aichef/SKILL.md`): elección de motor en bridge, gotchas del blog, moldes HTML, bloques congelados de WordPress, banners, robots.txt, research SEO. **Cargarla SIEMPRE antes de crear, ampliar, traducir, parchear o borrar posts, o de tocar `_redirects`, `robots.txt`, sitemap, FAQ o banners del blog.**
  - Contenido que el lector copia y ejecuta (prompts, fórmulas, comandos) → modelo bueno + gate. Y, sea cual sea el motor, barrido de caracteres no latinos (CJK, cirílico, hangul…) antes de publicar.
  - Al borrar posts o tocar el FRONTMATTER: `rm -rf astro-site/.astro astro-site/dist` antes de construir, y verificar el JSON-LD en el `dist`, no en el `.md`.
  - NUNCA volver a correr un ensamblador (`fase8c-libreria-assemble.py`, `fase8d-ampliar-glosario.py`) sobre un post publicado: reconstruye el cuerpo y pisa las ediciones manuales. Banners en lo publicado → `fase8e-banners-corpus.py`.
  - Tocar `_redirects` → `fase8b-auditar-301.py`. Tocar `robots.txt` o nacer una familia de producto → `robots-gate.py`.
  - Antes de borrar o consolidar por datos de GSC: comparar ENCABEZADOS y comprobar que la posición no es de la URL legacy (`blog.aichef.pro`).
- **Productos digitales** → skill local **`productos-digitales-aichef`** (complementa la agnóstica `digital-product-launch`). Cargarla antes de crear, actualizar o lanzar un producto. Siempre vigente: 3 fases con gate + commit y techo S ≤ 2,5 M · M ≤ 5 M · L ≤ 10 M tokens; el Mac redacta y orquesta, el VPS genera Excel, ensambla y pasa gates; todo producto nuevo nace con Stripe + NOWPayments (3 puertas cripto); un correo de Resend por producto nuevo o actualizado, en cola de 5 días.
- **Medición, layout y widgets del sitio** (Google Ads + consentimiento, DataFast, botón de WhatsApp, tarjeta de Miselup, integraciones) → **`astro-site/CLAUDE.md`**, que se carga al trabajar con ficheros de `astro-site/`. Siempre vigente: para apartar un `position: fixed`, margen y no `transform` (en móvil tiembla).

### ⚠️ Material propietario — ESTE REPO ES PÚBLICO

- `chefbusiness/chefpro-modernize` es **público**. Los **prompts core de los agentes** (el system prompt de Pickaxe que da vida a cada uno) son el producto en sí: **no se commitean aquí, ni en el contenido del blog, ni en un `.astro`**.
- John los comparte en la conversación como material de trabajo: sirven para entender a qué se dedica el agente, cómo lo hace y qué no hace, y desde ahí generar el listado de prompts del usuario final. **No se almacenan** en ningún repo.
- En las páginas y en los posts se explica **qué hace el agente y cómo aprovecharlo**; **el prompt core no se publica jamás**.

### Reglas de marca (John, 2026-07-30)

- **YouTube oficial: `https://youtube.com/@aichefpro`** — nunca el canal personal de John (el pie enlazaba a una playlist suya; corregido en `Footer.astro` y en el gemelo `ModernFooter.tsx` de la SPA).
- **Toda mención con nombre de John enlaza a `https://johnguerrero.es`** con `target="_blank" rel="noopener noreferrer author"`. En JSON-LD, el `Person` lleva `url` = su marca personal y `sameAs` con marca + canal. Los `alt` de imagen no se enlazan.
- **Correos (John, 2026-09-21): NUNCA saludar «Hola, chef».** La lista es transversal (dueños, managers, panaderos, pasteleros, chocolateros, bartenders, consultores): saludo abierto «Hola, colegas / amigos / comunidad» y su equivalente en cada idioma (EN «Hi everyone,» · FR «Bonjour à tous,» · DE «Hallo zusammen,» · IT «Ciao a tutti,» · PT «Olá a todos,» · NL «Hallo allemaal,»). Los moldes de `scripts/productos-digitales/emails/` ya van corregidos; detalle en la skill local `resend-aichef`.
- Las páginas de agente (8C) incrustarán **vídeos demo de Loom** cuando estén; no bloquean el arranque.

### 🔴 Otros idiomas = DUPLICAR lo español y adaptar, NUNCA reconstruir (John, 24-sep-2026)

El español lleva **siempre** la delantera: cada producto se construye desde cero **solo en español**. Para inglés y
para cada idioma futuro se **duplican** su landing, su dashboard y sus ficheros (xlsx, pdf, docx, md…) —y los hubs— y
se **traducen**, adaptando las variables del mercado nativo (terminología, moneda, impuestos, unidades, normativa o
anexos, benchmarks, ejemplos). **Diseño, estructura, maquetación y componentes son los mismos**: `cp` del componente
ES y traducir encima; ninguna plantilla ni página nueva. Si una adaptación obliga a cambiar la estructura **del diseño**
(landing, dashboard, componentes, maquetación), preguntar antes. Origen, lo que ya está decidido DENTRO de un
entregable y qué significa «nativo» → skill **`productos-digitales-aichef`**.

### 🔴🔴 PROPORCIONALIDAD: el recurso escaso es el TIEMPO de John (3-oct-2026) — manda sobre todo lo de abajo

John, tras parar la Churrería-Chocolatería (día y medio y ≈ 10,5 M tokens para una guía de 65 € con ~150 búsquedas/mes
de apertura): «Lo que me preocupa, lo que me jode, es el TIEMPO. A ti te sobra el tiempo, pero a mí no». Y: «lo que vayas a
desarrollar, investigar y proponer tiene que ser proporcional al producto». Los ~50 productos anteriores llevaron **3-6
horas** cada uno; los últimos 3-4 se fueron a 1-2 días con el mismo proceso pesado (5-6 lentes de research, verificación
legal cita a cita, SPEC de cientos de líneas, refutaciones en cadena, decenas de agentes Opus) y además obligaron a John a
vigilar la sesión para que no se gastara la suscripción.

- **Objetivo: producto terminado y listo para el Payment Link en 3-6 horas, sin que John tenga que supervisar.**
- **Antes de elegir el producto**: cuenta corta de coste (horas + tokens) frente a retorno (demanda, precio). Si no se paga,
  se recorta (p. ej. kit de Excel en vez de guía) o se elige otro.
- **Research en UNA pasada** (un agente, las lentes en un solo prompt), **SPEC corta**, **un implementador** por pieza,
  **gates de script** y **UNA sola comprobación adversarial final** (que no haya errores y que los ficheros no estén corruptos).
  Nada de rondas encadenadas ni de verificar cada cita por separado salvo en lo legal que el producto afirma.
- Reutilizar lo hecho (generadores, guiones y fichas de la hermana) cambiando datos; no rediseñar.
- UltraCode **no** autoriza nada de esto a crecer: si un paso va a pasar de una hora o de ~1 M tokens, se recorta antes de lanzarlo.
