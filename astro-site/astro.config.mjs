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
});
