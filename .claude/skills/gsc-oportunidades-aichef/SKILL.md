---
name: gsc-oportunidades-aichef
description: Versión LOCAL de gsc-oportunidades-seo para aichef.pro (repo chefpro-modernize). Propiedad, comandos, mapa de tipos de página, gotchas del sitio y línea base de la última sesión SEO. Úsala junto con la agnóstica siempre que se revise GSC, posiciones o CTR de aichef.pro.
---

# GSC → arreglos en aichef.pro (skill local)

La metodología vive en `~/.claude/skills/gsc-oportunidades-seo/`. Aquí solo está el «con qué».

## Propiedad y comandos

- Propiedad: `sc-domain:aichef.pro` (incluye los subdominios legacy `blog.aichef.pro` y `enblog.aichef.pro`).
- Volcado completo y análisis:
  ```bash
  ~/mcp-gsc/.venv/bin/python ~/.claude/skills/gsc-oportunidades-seo/scripts/gsc_pull.py \
    --site "sc-domain:aichef.pro" --out <scratchpad>/gsc
  python3 ~/.claude/skills/gsc-oportunidades-seo/scripts/analizar_gsc.py --datos <scratchpad>/gsc \
    --config .claude/skills/gsc-oportunidades-aichef/config-gsc.json --raiz . --out <scratchpad>/informe.md
  ```
- Volúmenes y SERP: `DATAFORSEO_ENV=~/.config/chefbusiness/secrets.env python3 scripts/dataforseo.py vol|serp "kw" --pais <loc> --idioma <lang>`. En el T480 las claves viven en ese fichero. **Fuera de ES, `--pais` e `--idioma` explícitos siempre.**
- ⚠️ El scratchpad está en `/tmp` y se borra al apagar el equipo. Lo que haya que conservar entre sesiones va a `~/recuperacion-*` o al repo.

## Mapa de tipos de página

| Ruta | Fuente | Notas |
|---|---|---|
| `/blog/<slug>` (ES), `/{en,fr,de,it,pt}/blog/<slug>` | `astro-site/src/content/blog/<lang>/*.md` | `title` = H1 y `<title>{title} \| Blog AI Chef Pro` (≤ 42 caracteres). `description` = meta **y entradilla bajo el H1**. NL aún no tiene blog. |
| Glosario ES (`*-concepto-*`) | mismo, categoría `glosario` | Mucho volumen de intención escolar o científica: posición 7-10 y CTR 0,2-0,5 %. |
| Landings de marketing (`/en/restaurant-marketing-ai`…) | copy en `src/i18n/locales/<lang>.json` (raíz de la SPA) + head en `astro-site/src/lib/marketing-heads/*.ts` | La FAQ del JSON alimenta el FAQPage y se pinta como **texto plano**: no lleva enlaces. |
| pSEO `/escandallo-restaurante/<ciudad>` | plantilla Fase 6 | Ya en posición 1,8-4 para «escandallo de costes restaurante (valencia)». |
| `llms.txt` / `llms-full.txt` | `astro-site/public/` (estáticos, a mano) | El `public/llms*.txt` de la raíz es la copia muerta de la SPA. |
| CTA final de cada post | `components/blog/BlogCTA.astro` + `lib/app-url.ts` | Ya manda al workspace de su idioma. |

## Gotchas del sitio

- **Posiciones de URLs legacy:** GSC sigue mostrando `blog.aichef.pro/<slug>/`, que ya devuelve 301. Filtra por `https://aichef.pro/` antes de concluir nada.
- **Un «baile» entre dos URLs no siempre es canibalización.** «chef gpt» pasó de `/blog/chef-gpt` (hasta el 10-sep-2026) a `/blog/chef-gpt-espanol` (desde el 11-sep), siempre en posición ~6 y con una sola URL a la vez. La causa probable era que `chef-gpt` tenía **0 enlaces internos entrantes**. Antes de fusionar, mira el enlazado.
- **Clon parcial (blobless + sparse):** NO ejecutes `git fsck`, ni `sparse-checkout add astro-site/public` ni otras carpetas de imágenes: descarga cientos de MB de blobs. Para editar un fichero fuera del sparse, cópialo y luego `git add --sparse`.
- **El build se verifica en el deploy preview de Netlify** (PR → `deploy-preview-N--aichefpro.netlify.app`). Si se toca frontmatter, el `.astro` cacheado puede servir el viejo en un build local (ver CLAUDE.md).
- **Banners de producto en posts EN:** la otra sesión (tienda EN) los reapunta a `/en/digital-products/*` al lanzar cada producto EN. No los toques sin coordinarte con ella.
- **Cifras por idioma:** la web dice «75+ agentes» en ES/EN y «50+» en FR/DE/IT/PT. Los hubs EN aún dicen «55+ apps» (inconsistencia previa).

## Línea base — sesión del 2026-10-04 (PR #112), medir hacia el 25-oct

GSC del 20-jul al 3-oct-2026:

| Página | Impr. | Clics | Pos. | Qué se tocó |
|---|---|---|---|---|
| /blog/homogeneizacion-concepto-definicion | 28.465 | 60 | 7,2 | title + description |
| /blog/hidrolisis-concepto-definicion | 25.520 | 67 | 9,5 | title + description |
| /blog/demi-glace-concepto-y-definicion | 10.313 | 32 | 7,9 | title + description |
| /blog/maceracion-concepto-definicion | 10.181 | 47 | 8,3 | title + description |
| /blog/emulsion-concepto-definicion | 9.577 | 24 | 10,3 | title + description |
| /blog/reduccion-concepto-definicion | 9.227 | 29 | 8,5 | title + description |
| /blog/roux-concepto-y-definicion | 6.557 | 27 | 9,1 | title + description |
| /blog/salsa-veloute-concepto-y-definicion | 6.399 | 34 | 7,7 | title + description |
| /blog/mandolina-concepto-definicion | 6.290 | 21 | 7,9 | title + description |
| /blog/fondo-blanco-concepto-y-definicion | 3.728 | 24 | 6,1 | title + description |
| /blog/gelificacion-concepto-definicion | 3.453 | 41 | 9,0 | title + description |
| /blog/salsa-espanola-concepto-y-definicion | 2.400 | 21 | 8,4 | title + description |
| /blog/chef-gpt + /blog/chef-gpt-espanol | 4.243 + 1.785 | 45 + 18 | 6,0 / 6,1 | 4 enlaces entrantes a chef-gpt |
| /en/restaurant-marketing-ai (90 d) | 721 | 5 | 17-25 | title/meta/H1/FAQ |
| /en/kitchen-management-software-ai (90 d) | 814 | 1 | 7-15 | title/meta/H1/FAQ |
| /fr/calcul-food-cost-restaurant-ia (90 d) | 367 | 0 | 24-34 | title/meta/H1/H2/FAQ «logiciel food cost» |

Papillote, oxidación, flambeado y liofilización también se retitularon (volumen menor; liofilización está en pos. 17-36, así que el snippet solo no basta).

## Pendientes y descartes

- Descartado: las landings ES `/simulador-rentabilidad-restaurante` y `/escandallo-restaurante/*`. Suman 60-180 impresiones en 90 días y ya están en el top 5 para lo suyo.
- Pendiente: el H2 «Hidrólisis ácida → ceviche» del post de hidrólisis es incorrecto (en el ceviche hay desnaturalización, no hidrólisis). Necesita un refresh con revisión Opus.
- Pendiente: la cifra «5 % et 15 % de bénéfice potentiel» de la landing FR no tiene fuente; también los testimonios y números previos de las landings EN/FR.
- Plan de contenidos del trimestre: `PLAN_CONTENIDOS_Q4_2026.md` (raíz).
