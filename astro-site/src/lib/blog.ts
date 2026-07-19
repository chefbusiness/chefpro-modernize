// Fase 8B — Taxonomía destino y helpers del blog.
// Las categorías WP se consolidan aquí (los 2 glosarios se fusionan; la slug
// larga 'glosario-y-lexico-cientifico-culinario' se acorta a 'glosario' — el
// mapa 301 del subdominio traduce las archives viejas).
import { getCollection, type CollectionEntry } from 'astro:content';
import type { Locale } from '../i18n/config';

export interface BlogCategory {
  slug: string;
  name: string;
  description: string;
}

export const BLOG_CATEGORIES: BlogCategory[] = [
  {
    slug: 'ia-en-gastronomia',
    name: 'IA en Gastronomía',
    description:
      'Inteligencia artificial aplicada a restaurantes y hostelería: herramientas, comparativas, automatización y casos reales.',
  },
  {
    slug: 'ai-chef-pro',
    name: 'AI Chef Pro',
    description:
      'Guías, novedades y trucos para sacar el máximo partido a los agentes de IA culinarios de AI Chef Pro.',
  },
  {
    slug: 'libreria-de-prompts',
    name: 'Librería de Prompts',
    description:
      'Prompts profesionales listos para usar con los agentes de IA culinarios: por rol, por tarea y por tipo de negocio.',
  },
  {
    slug: 'tutoriales',
    name: 'Tutoriales y Técnica',
    description:
      'Técnica culinaria profesional y tutoriales paso a paso: elaboraciones, procesos y guías de cocina con IA.',
  },
  {
    slug: 'recetas',
    name: 'Recetas Profesionales',
    description:
      'Recetas de cocina profesional plato a plato: platos nacionales, alta cocina y elaboraciones creadas con los recetarios de IA de AI Chef Pro.',
  },
  {
    slug: 'glosario',
    name: 'Glosario Culinario',
    description:
      'Léxico científico y técnico de cocina profesional: términos, conceptos y definiciones con rigor.',
  },
];

export const getCategory = (slug: string): BlogCategory | undefined =>
  BLOG_CATEGORIES.find((c) => c.slug === slug);

export type BlogPost = CollectionEntry<'blog'>;

/** Slug público del post (basename del id — la carpeta de idioma no cuenta). */
export const postSlug = (post: BlogPost): string =>
  post.id.split('/').pop()!.replace(/\.md$/, '');

/** Posts publicados de un idioma, más recientes primero. */
export async function getPublishedPosts(lang: Locale = 'es'): Promise<BlogPost[]> {
  const posts = await getCollection(
    'blog',
    (p) => p.data.lang === lang && !p.data.draft
  );
  return posts.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

/** Minutos de lectura estimados a partir del HTML/markdown del cuerpo. */
export function readingTime(body: string): number {
  const words = body
    .replace(/<[^>]+>/g, ' ')
    .split(/\s+/)
    .filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}

const MONTHS_ES = [
  'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
  'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
];

/** "17 de febrero de 2026" — sin depender del locale del runtime de build. */
export function formatDateEs(d: Date): string {
  return `${d.getUTCDate()} de ${MONTHS_ES[d.getUTCMonth()]} de ${d.getUTCFullYear()}`;
}

export const POSTS_PER_PAGE = 24;
