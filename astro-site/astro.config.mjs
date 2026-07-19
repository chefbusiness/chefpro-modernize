import { fileURLToPath } from 'node:url';
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';

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
      filter: (page) => {
        const path = new URL(page).pathname.replace(/\/$/, '');
        return !(
          path.endsWith('-access') ||
          path.endsWith('-library') ||
          path.startsWith('/admin')
        );
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
