// 301 de blog.aichef.pro/{en,fr,de,it,pt,nl}/… al post del mismo idioma en
// aichef.pro, o al índice de ese blog si no hay equivalente.
//
// Corre ANTES que _redirects. En aichef.pro (y en cualquier otro host) no hace
// nada: el path /en/* del sitio real sigue sirviendo el blog inglés.
// El mapa lo genera scripts/astro-migration/legacy-subdominios-301.py.
// La red de seguridad, si esta función no llega a correr, está en _redirects
// y manda cada prefijo al índice de su idioma — no al blog en español.

import { LEGACY_LANG_EXACT } from './legacy-blog-lang-map.ts';

const HUB: Record<string, string> = {
  en: 'https://aichef.pro/en/blog',
  fr: 'https://aichef.pro/fr/blog',
  de: 'https://aichef.pro/de/blog',
  it: 'https://aichef.pro/it/blog',
  pt: 'https://aichef.pro/pt/blog',
  nl: 'https://aichef.pro/nl/blog',
};

/** Misma normalización que legacy-subdominios-301.py (hay un test cruzado). */
export function normalizePath(pathname: string): string {
  let path = pathname;
  try {
    path = decodeURIComponent(pathname);
  } catch {
    path = pathname;
  }
  path = path.replace(/\u00a0|\u202f/g, ' ');
  path = path.normalize('NFKD').replace(/[\u0300-\u036f]/g, '');
  path = path.toLowerCase().split('?')[0].split('#')[0];
  if (!path.startsWith('/')) path = `/${path}`;
  path = path
    .replace(/[^a-z0-9/]+/g, '-')
    .replace(/-+/g, '-')
    .replace(/-\//g, '/')
    .replace(/\/-/g, '/');
  path = path.replace(/\/+$/, '');
  return path || '/';
}

export function destinoLegacy(hostname: string, pathname: string): string | null {
  if (hostname !== 'blog.aichef.pro') return null;
  const limpio = normalizePath(pathname);
  const lang = limpio.split('/').filter(Boolean)[0];
  if (!lang || !(lang in HUB)) return null;
  return LEGACY_LANG_EXACT[limpio] || HUB[lang];
}

export default async (request: Request) => {
  const url = new URL(request.url);
  const dest = destinoLegacy(url.hostname, url.pathname);
  if (!dest) return;
  return new Response(null, {
    status: 301,
    headers: {
      Location: dest,
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
