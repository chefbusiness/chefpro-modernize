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
// Fase 8B: lastmod real (modDate del frontmatter) de los posts del blog,
// generado por scripts/astro-migration/fase8b-wp2md.py en cada conversión.
const BLOG_LASTMOD = JSON.parse(
  readFileSync(new URL('./src/lib/blog-lastmod.json', import.meta.url), 'utf8')
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
          // Las 88 páginas de la zona app son SIEMPRE de un único segmento en
          // la raíz (/kit-escandallos-library, /guia-dark-kitchen-access…).
          // Antes esto era un endsWith() que no miraba la profundidad y se
          // llevaba por delante /en/blog/category/prompt-library —una
          // categoría PÚBLICA del blog—, que desaparecía del sitemap sin un
          // solo aviso. Cazado el 2026-08-27, junto al mismo fallo de patrón
          // en robots.txt, que además bloqueaba los 26 posts de la categoría.
          /^\/[^/]+-(access|library)$/.test(path) ||
          // '/admin' o '/admin/...' — NO startsWith('/admin') a secas, que
          // excluiría por error futuras rutas tipo /administracion-... (BAJA
          // del revisor adversarial de Fase 6).
          path === '/admin' ||
          path.startsWith('/admin/') ||
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
        item.lastmod = LASTMOD[path] ?? BLOG_LASTMOD[path] ?? NEW_URLS_LASTMOD;
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
    ssr: {
      // Desde 2026-08-01 las 119 páginas de marketing pasan por SSR, así que sus
      // dependencias se cargan también en Node. jspdf y xlsx (y fflate, que
      // arrastra jspdf) son CommonJS con una forma de export que el loader ESM
      // de Node rechaza: «does not provide an export named 'default'». Con
      // noExternal las empaqueta Vite, que sí hace el interop.
      // Solo se usan dentro de handlers de exportación; nunca durante el render.
      noExternal: ['jspdf', 'xlsx', 'fflate'],
    },
    plugins: [
      {
        // Fase 6: en el pipeline de Astro, importar .jpg/.svg devuelve un objeto
        // ImageMetadata — pero los componentes de la SPA (cross-root, D5: no se
        // tocan) esperan la semántica de Vite puro: un STRING con la URL
        // (<img src={logo}>). Sin esto, el DOM emite src="[object Object]"
        // (visto en staging: logo y avatares rotos, request a /[object%20Object]).
        // Se fuerza ?url SOLO para imágenes que resuelven al src/ de la RAÍZ.
        name: 'cross-root-assets-as-url',
        enforce: 'pre',
        async resolveId(source, importer, options) {
          if (!importer || !/\.(jpe?g|png|svg|webp|gif)$/.test(source)) return null;
          const resolved = await this.resolve(source, importer, {
            skipSelf: true,
            ...options,
          });
          const rootSrc = fileURLToPath(new URL('../src/', import.meta.url));
          if (resolved && resolved.id.startsWith(rootSrc) && !resolved.id.includes('?')) {
            return `${resolved.id}?url`;
          }
          return resolved;
        },
      },
    ],
    resolve: {
      alias: {
        // Los ficheros cross-root de la SPA (src/data/apps.ts) importan lucide-react,
        // pero en el build de Netlify (base = astro-site) el node_modules de la raíz
        // NO existe: se resuelve al paquete instalado en astro-site.
        'lucide-react': fileURLToPath(
          new URL('./node_modules/lucide-react/dist/esm/lucide-react.js', import.meta.url)
        ),
        // Fase 6: MISMO gotcha para todo el grafo cross-root de marketing/legales
        // (Node resuelve subiendo desde el fichero importador → /opt/build/repo/
        // node_modules, que NO existe en Netlify). Cada paquete bare del cierre de
        // imports (censo fase6-import-walker, 56 ficheros) se apunta al node_modules
        // de astro-site. Un find string solo matchea exacto o con '/' — 'i18next'
        // NO captura 'i18next-browser-languagedetector'. react/react-dom no van
        // aquí: los dedupe-a @astrojs/react.
        ...Object.fromEntries(
          [
            'i18next',
            'i18next-browser-languagedetector',
            'react-i18next',
            'xlsx',
            'jspdf',
            'class-variance-authority',
            'clsx',
            'tailwind-merge',
            '@radix-ui/react-accordion',
            '@radix-ui/react-avatar',
            '@radix-ui/react-collapsible',
            '@radix-ui/react-dialog',
            '@radix-ui/react-dropdown-menu',
            '@radix-ui/react-navigation-menu',
            '@radix-ui/react-scroll-area',
            '@radix-ui/react-separator',
            '@radix-ui/react-slot',
          ].map((p) => [p, fileURLToPath(new URL(`./node_modules/${p}`, import.meta.url))])
        ),
        // Fase 5 (zona app islands): los gates/dashboards de la SPA se importan
        // cross-root TAL CUAL (fuente de verdad única, cero copias). Sus imports
        // internos '@/x' apuntan al src/ de la RAÍZ del repo (no a astro-site/src).
        // ⚠️ Desde Fase 6, BaseLayout.astro también usa '@/hooks/useLiveUserCount'
        // A PROPÓSITO (fichero cross-root de la SPA). Si algún día se crea
        // astro-site/src/hooks/*, recordar que '@/' SIEMPRE resuelve a la raíz.
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
