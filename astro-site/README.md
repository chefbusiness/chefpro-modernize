# astro-site — Migración de aichef.pro a Astro

Subproyecto de la migración descrita en [`../PLAN_MAESTRO_MIGRACION_ASTRO_2026.md`](../PLAN_MAESTRO_MIGRACION_ASTRO_2026.md) (leer SIEMPRE antes de trabajar aquí).

## Reglas de oro

1. **NUNCA `npm install` / `npm run build` / Playwright en local** (regla térmica). Todo build ocurre en Netlify (staging). Verificación: deploy previews + `curl` con UA Googlebot.
2. **Paridad de URLs 1:1** con la SPA hasta el cutover (D6). Slugs idénticos a `public/sitemap.xml`.
3. El staging lleva `X-Robots-Tag: noindex` (netlify.toml de este directorio). Se quita SOLO en el cutover (Fase 7).
4. Los datos de contenido se **vierten** desde los ficheros existentes de la SPA (`src/data/*`, `src/i18n/locales/*`), no se reescriben.

## Setup del site de staging en Netlify (una vez)

Add new site → Import from Git → este repo → **Base directory: `astro-site`** → build `npm run build` → publish `astro-site/dist`.

## Estructura

- `src/layouts/BaseLayout.astro` — head SEO completo: canonical + hreflang 7 idiomas nativos (el gran gap de la SPA).
- `src/i18n/config.ts` — locales del grupo (es default sin prefijo).
- `tailwind.config.ts` + `src/styles/global.css` — portados verbatim de la SPA para paridad visual.
