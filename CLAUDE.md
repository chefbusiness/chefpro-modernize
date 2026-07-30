# Instrucciones del proyecto — aichef.pro (chefpro-modernize)

## 🚨 REGLA CAPITAL — Generación de contenidos (BLOQUEANTE)

Aplica a **cualquier** contenido (artículo, landing, ficha de producto, post, página) en este o cualquier proyecto del grupo ChefBusiness. **Antes de escribir la primera línea:**

1. **Keyword research + análisis SERP PRIMERO.** Nunca escribir sin investigar keywords e inspeccionar la SERP de Google del/los mercado(s) objetivo. Lo que dicte la SERP (formatos, People Also Ask, entidades, intención) manda sobre lo que se incluye.
2. **Texto → `bridge.py` (DeepSeek v4).** Motor de redacción (`--task content`/`translation` → `deepseek-v4-pro`). Gotcha: es modelo de razonamiento → usar `--max-tokens` ≥ 8000 o devuelve vacío. **La ruta depende de la máquina** (este repo se trabaja desde el Mac y desde el VPS):
   - VPS: `/root/chefbusiness-ai/bridge.py` — ejecutar con su venv: `/root/chefbusiness-ai/.venv/bin/python`
   - Mac: `/Users/johnguerrero/chefbusiness-ai/bridge.py`
   En el mismo repo están `serp_research.py` (research SERP previo) y `gsc_report.py`.
3. **Imágenes → skill `generate-images` (Gemini "Nano Banana 2").** Todas las imágenes del contenido.
4. **Contenido ENRIQUECIDO obligatorio:** tablas, datos, métricas, citas, listados y comparaciones (cuando apliquen) + sección de **Preguntas Frecuentes (FAQ)** + lo que indique el análisis SERP.
5. **Imágenes dentro del cuerpo: mínimo 2.** Además, una **imagen destacada (featured) ÚNICA** que **no** se repite dentro del contenido.
6. **Ortografía y semántica perfectas; tono amigable y humano** (no corporativo, no robótico).

> Un contenido sin research/SERP previo, o sin tablas/datos/FAQ/≥2 imágenes + destacada única, **no está terminado**.

## Stack y notas operativas

> ⚠️ Actualizado 2026-07-28. **Desde el cutover de Fase 7 (2026-07-19) producción sirve ASTRO**, no la SPA. Lo que se construye y despliega es `astro-site/`; la SPA de la raíz sobrevive sólo como fuente de los islands React de la zona app (decisión D5) y **ya no se construye**. Doc canónico: `PLAN_MAESTRO_MIGRACION_ASTRO_2026.md` (§8 = log por sesión).

- **Stack real**: Astro 5 en `astro-site/` (build `cd astro-site && npm install && npm run build`, publish `astro-site/dist`) + Tailwind + Netlify con auto-deploy desde `main`. La SPA React 18 + Vite de la raíz aporta los componentes cross-root que los islands importan.
- **i18n**: 7 idiomas (es, en, fr, de, it, pt, nl). **El séptimo es NEERLANDÉS, no catalán** (error recurrente en contenidos).
- **Live**: https://aichef.pro · blog ES en https://aichef.pro/blog (322 posts; `blog.aichef.pro` 301-ea desde el cutover 8B.5) · **blog EN en https://aichef.pro/en/blog** (39 posts, Fase 8B.6). El mapa 301 de `enblog.aichef.pro` ya está en `_redirects` pero **no se ejecuta hasta que el subdominio sea alias del site en Netlify + DNS**; mientras tanto ese WordPress sigue vivo. **Tarea pendiente de John, con la trampa de las A records de Hostinger y la batería de verificación: `CUTOVER_ENBLOG_PENDIENTE.md` (recordárselo).**
- **SEO**: meta/hreflang/JSON-LD **nativos server-side** en `BaseLayout.astro` + `SEOHead` de la SPA para los islands. La edge function `netlify/edge-functions/og-meta.ts` está **MUERTA** (no declarada desde Fase 7) y `public/sitemap.xml` ya **no** es la fuente: el sitemap lo genera Astro (`sitemap-index.xml`, 1.091 URLs) con lastmod real por post desde `astro-site/src/lib/blog-lastmod.json`. GSC: `sc-domain:aichef.pro`.
- **Verificación**: gates en `scripts/astro-migration/` (`fase8b-gate.py` blog, `fase6-gate.py <url>` marketing —sin argumento corre modo staging obsoleto—, `fase5-gate-s1-s2.py` zona app) + `fase7-vigilancia.py` (salud de producción post-cutover).
- **Entorno**: el repo se trabaja desde el Mac **y** desde un VPS Linux. En el VPS no aplican las restricciones térmicas del Mac: se pueden hacer builds locales y usar Playwright. Ojo con las rutas absolutas de `~/` que hay en documentos antiguos.

### Gotchas del blog que cuestan dinero

- **Al BORRAR posts hay que limpiar `astro-site/.astro/` antes de construir.** La content collection de Astro 5 se cachea ahí y **sigue emitiendo el HTML de posts cuyo `.md` ya no existe**: tras consolidar 24 posts con 301, el build seguía generando 1.198 páginas y metiéndolos en el sitemap. Con `rm -rf astro-site/.astro astro-site/dist` bajó a 1.173, que es lo correcto. Cazado el 2026-07-28.
- Tras CADA refresh de posts: `python3 scripts/astro-migration/fase8b-regen-lastmod.py` (el ensamblador actualiza el `modDate` del .md pero **no** toca `blog-lastmod.json`, del que vive el sitemap).
- Reglas nuevas en `astro-site/public/_redirects`: Netlify resuelve por **primera coincidencia**. Cualquier regla del subdominio `blog.aichef.pro` debe insertarse ANTES de la genérica `/:slug → /blog/:slug` (línea marcada con `# Genérica`), o no se ejecuta nunca.
- **La genérica `/:slug` se traga TODO lo que llegue con un solo segmento**, no sólo los posts. Cada familia de un segmento que no sea un post (archives de categoría —ese WP tiene la base vacía y las sirve en la raíz—, las 7 páginas del WordPress, sitemaps hijos, `robots.txt`, `favicon.ico`, archives de año) necesita su regla ANTES o se convierte en un **301 a un 404**. Pasó: 17 familias rotas descubiertas el 2026-07-28, 9 días después del cutover. Gate para que no vuelva a colarse: `python3 scripts/astro-migration/fase8b-auditar-301.py --sitio es|en` (simula el motor de Netlify contra el censo del export del WP y exige que el destino final exista en el `dist`; necesita build reciente). **Correrlo siempre que se toque `_redirects`.**
- Los commits de slices deben incluir `astro-site/public/blog-assets/`: los productores generan imágenes nuevas y un `git add` quirúrgico de `content/` las deja fuera → 404 en producción.
- Nombres de agentes/apps: catálogo canónico en `src/lib/linkify-use-case.tsx` y `src/data/apps.ts` (los recetarios del mundo se llaman `Mexicana`, `Peruana`…, **no** "Cocina Mexicana AI": ese nombre es un adorno editorial heredado de WordPress y no existe como producto).
- Enlaces internos del blog: la convención establecida es **absoluta** (`https://aichef.pro/blog/<slug>`), 2.278 usos frente a 28 relativos.
- **El blog es MULTI-IDIOMA desde 8B.6 y sus URLs sólo salen de los helpers de `astro-site/src/lib/blog.ts`** (`postPath`, `categoryPath`, `listPagePath`, `blogBase`). El ES va sin prefijo y con segmentos heredados de WP (`/blog/categoria/…`); el EN va con prefijo y segmentos nativos (`/en/blog/category/…`). Las categorías se resuelven SIEMPRE con idioma (`getCategory(slug, lang)`): `ai-chef-pro` existe en los dos.
- **En Header/Footer/Hero —que se pintan en los 7 idiomas— el hub del blog es `blogHubHref(lang)`, nunca `blogBase(lang)`**: sólo ES e EN tienen blog, así que `blogBase('fr')` daría `/fr/blog`, que es un 404. `blogHubHref` cae al ES para los idiomas sin blog propio.

### ⚠️ Material propietario — ESTE REPO ES PÚBLICO

- `chefbusiness/chefpro-modernize` es **público**. Nunca entra aquí material propietario: los **prompts core de los agentes** (el system prompt de Pickaxe que da vida a cada uno) son el producto en sí.
- Van al repo **privado** `chefbusiness/aichef-blog` → carpeta `agentes-core-prompts/` (clon estable en el VPS: `/root/aichef-blog-repo/`). Un `.md` por agente, con el slug del catálogo canónico; ahí está la plantilla y la convención.
- Son la fuente de verdad de la Fase 8C: de cada core salen el trabajo que hace el agente, cómo lo hace y qué NO hace. En las páginas se explica **qué hace y cómo aprovecharlo**; **el prompt no se publica jamás**.

### Reglas de marca (John, 2026-07-30)

- **YouTube oficial: `https://youtube.com/@aichefpro`** — nunca el canal personal de John (el pie enlazaba a una playlist suya; corregido en `Footer.astro` y en el gemelo `ModernFooter.tsx` de la SPA).
- **Toda mención con nombre de John enlaza a `https://johnguerrero.es`** con `target="_blank" rel="noopener noreferrer author"`. En JSON-LD, el `Person` lleva `url` = su marca personal y `sameAs` con marca + canal. Los `alt` de imagen no se enlazan.
- Las páginas de agente (8C) incrustarán **vídeos demo de Loom** cuando estén; no bloquean el arranque.
- Gotcha de `faq.astro`: el campo `a` se pinta como TEXTO PLANO y alimenta el FAQPage; el HTML con enlaces va en `aHtml` (plantilla con backticks). Meter markup en `a` lo escupe literal en la página.
