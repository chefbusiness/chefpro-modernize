// Fase 8B — Content Layer (Astro 5) del blog migrado desde blog.aichef.pro.
// Estructura: src/content/blog/{lang}/{slug}.md — el slug del fichero ES el
// slug público (/blog/{slug}) y se conserva VERBATIM del WP para que el mapa
// 301 del subdominio sea 1:1. El cuerpo es HTML saneado del export de WP
// (Tier B/C) o markdown nuevo de bridge.py (Tier A refresh).
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    modDate: z.coerce.date().optional(),
    /** Slug de categoría destino — ver BLOG_CATEGORIES en src/lib/blog.ts */
    category: z.string(),
    tags: z.array(z.string()).default([]),
    /** Imagen destacada, ruta pública (/blog-assets/YYYY/MM/foo.jpg) */
    image: z.string().optional(),
    imageAlt: z.string().optional(),
    lang: z.enum(['es', 'en', 'fr', 'de', 'it', 'pt', 'nl']).default('es'),
    /** Trazabilidad del export WP (id numérico del post origen) */
    wpId: z.number().optional(),
    /** Tier de migración del análisis (A oro / B autoridad / C consumo) */
    tier: z.enum(['A', 'B', 'C']).optional(),
    faq: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
