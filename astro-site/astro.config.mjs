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
  integrations: [react(), tailwind({ applyBaseStyles: false }), sitemap()],
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
      },
    },
  },
});
