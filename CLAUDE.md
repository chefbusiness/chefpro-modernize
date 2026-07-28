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
- **Live**: https://aichef.pro · blog en https://aichef.pro/blog (346 posts; `blog.aichef.pro` 301-ea desde el cutover 8B.5).
- **SEO**: meta/hreflang/JSON-LD **nativos server-side** en `BaseLayout.astro` + `SEOHead` de la SPA para los islands. La edge function `netlify/edge-functions/og-meta.ts` está **MUERTA** (no declarada desde Fase 7) y `public/sitemap.xml` ya **no** es la fuente: el sitemap lo genera Astro (`sitemap-index.xml`, 1.073 URLs) con lastmod real por post desde `astro-site/src/lib/blog-lastmod.json`. GSC: `sc-domain:aichef.pro`.
- **Verificación**: gates en `scripts/astro-migration/` (`fase8b-gate.py` blog, `fase6-gate.py <url>` marketing —sin argumento corre modo staging obsoleto—, `fase5-gate-s1-s2.py` zona app) + `fase7-vigilancia.py` (salud de producción post-cutover).
- **Entorno**: el repo se trabaja desde el Mac **y** desde un VPS Linux. En el VPS no aplican las restricciones térmicas del Mac: se pueden hacer builds locales y usar Playwright. Ojo con las rutas absolutas de `~/` que hay en documentos antiguos.

### Gotchas del blog que cuestan dinero

- Tras CADA refresh de posts: `python3 scripts/astro-migration/fase8b-regen-lastmod.py` (el ensamblador actualiza el `modDate` del .md pero **no** toca `blog-lastmod.json`, del que vive el sitemap).
- Los commits de slices deben incluir `astro-site/public/blog-assets/`: los productores generan imágenes nuevas y un `git add` quirúrgico de `content/` las deja fuera → 404 en producción.
- Nombres de agentes/apps: catálogo canónico en `src/lib/linkify-use-case.tsx` y `src/data/apps.ts` (los recetarios del mundo se llaman `Mexicana`, `Peruana`…, **no** "Cocina Mexicana AI": ese nombre es un adorno editorial heredado de WordPress y no existe como producto).
- Enlaces internos del blog: la convención establecida es **absoluta** (`https://aichef.pro/blog/<slug>`), 2.278 usos frente a 28 relativos.
