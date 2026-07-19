import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

// Fase 6 — sitemap nativo con paridad EXACTA vs el sitemap.xml de la SPA:
// lastmod por URL (snapshot de prod vía scripts/astro-migration/fase6-lastmod-map.py)
// y exclusiones = zona app + legales + rutas alias (igual que en prod, donde
// legales y alias nunca estuvieron en el sitemap).
const LASTMOD = JSON.parse(
  readFileSync(new URL('./src/lib/sitemap-lastmod.json', import.meta.url), 'utf8')
);
const MARKETING = JSON.parse(
  readFileSync(new URL('./src/lib/marketing-pages.json', import.meta.url), 'utf8')
);
const SITEMAP_EXCLUDE = new Set(
  MARKETING.flatMap((e) => {
    const alias = e.aliasRoutes ?? [];
    if (e.kind !== 'legal') return alias;
    const bp = e.basePath;
    return [bp, ...['en', 'fr', 'de', 'it', 'pt', 'nl'].map((l) => `/${l}${bp}`), ...alias];
  })
);
// Fecha de alta para URLs que NO estaban en el sitemap de la SPA (hoy: las 45
// de productos digitales, incorporadas al sitemap en Fase 6). Si en fases
// posteriores se añaden páginas nuevas, actualizar esta constante o el mapa.
const NEW_URLS_LASTMOD = '2026-07-19';

// PLAN_MAESTRO_MIGRACION_ASTRO_2026.md — D6: paridad de URLs 1:1 con la SPA actual.
// Esquema de rutas idéntico: es sin prefijo, resto de idiomas con prefijo.
export default defineConfig({
  site: 'https://aichef.pro',
  trailingSlash: 'never',
  // format 'file': en/index.astro → /en.html → Netlify sirve /en con 200 SIN barra final,
  // igual que la SPA y el sitemap (D6). Con el default 'directory', /en devolvía 301 → /en/.
  build: { format: 'file' },
  integrations: [
    react(),
    tailwind({ applyBaseStyles: false }),
    sitemap({
      // Fase 5: la zona app post-pago (gates -access, dashboards -library,
      // /admin) NUNCA entra en el sitemap — URLs privadas de dinero, noindex.
      // Fase 6: + legales y rutas alias (paridad: tampoco están en el de prod).
      filter: (page) => {
        const path = new URL(page).pathname.replace(/\/$/, '') || '/';
        return !(
          path.endsWith('-access') ||
          path.endsWith('-library') ||
          path.startsWith('/admin') ||
          SITEMAP_EXCLUDE.has(path)
        );
      },
      // Fase 6: lastmod por URL (paridad con prod; URLs nuevas → fecha de alta).
      // NOTA paridad aceptada: el sitemap de prod lleva xhtml:link alternates en
      // 521/658 URLs; aquí NO se emiten porque el hreflang va nativo en el HTML
      // de TODAS las páginas (cobertura superior; Google acepta cualquiera de
      // las dos vías y no exige ambas).
      serialize: (item) => {
        const path = new URL(item.url).pathname.replace(/\/$/, '') || '/';
        item.lastmod = LASTMOD[path] ?? NEW_URLS_LASTMOD;
        return item;
      },
    }),
  ],
  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'],
    routing: { prefixDefaultLocale: false },
  },
  vite: {
    resolve: {
      alias: {
        // Los ficheros cross-root de la SPA (src/data/apps.ts) importan lucide-react,
        // pero en el build de Netlify (base = astro-site) el node_modules de la raíz
        // NO existe: se resuelve al paquete instalado en astro-site.
        'lucide-react': fileURLToPath(
          new URL('./node_modules/lucide-react/dist/esm/lucide-react.js', import.meta.url)
        ),
        // Fase 5 (zona app islands): los gates/dashboards de la SPA se importan
        // cross-root TAL CUAL (fuente de verdad única, cero copias). Sus imports
        // internos '@/x' apuntan al src/ de la RAÍZ del repo (no a astro-site/src;
        // astro-site no usa '@/' en ningún fichero propio — verificado 2026-07-19).
        // Nota: el find '@' solo matchea '@' exacto o '@/...' — los paquetes
        // scoped tipo @astrojs/* NO se ven afectados (semántica @rollup/plugin-alias).
        '@': fileURLToPath(new URL('../src', import.meta.url)),
        // react-router-dom y react-helmet-async NO están instalados en astro-site:
        // se resuelven a shims mínimos (los islands no tienen Router ni HelmetProvider).
        'react-router-dom': fileURLToPath(
          new URL('./src/islands/shims/react-router-dom.tsx', import.meta.url)
        ),
        'react-helmet-async': fileURLToPath(
          new URL('./src/islands/shims/react-helmet-async.tsx', import.meta.url)
        ),
      },
    },
  },
});
