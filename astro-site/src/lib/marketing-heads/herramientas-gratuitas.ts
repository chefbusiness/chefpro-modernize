// Head module server-side de la página /herramientas-gratuitas (hub de herramientas gratuitas).
// Origen: src/pages/HerramientasGratuitas.tsx (SPA). En Astro esa página se monta como island
// client:only, cuyo <Helmet> es un no-op shim; por eso todo lo SEO-relevante del head sale de aquí en build.
// Decisiones no obvias: (1) title/description/keywords se pasan EXPLÍCITOS a SEOHead con las claves
// toolHub.seo.* → sin fallback a seo.*. (2) La página NO pasa ogImage → usa la default /og-image.jpg → se omite.
// (3) Único schema propio = BreadcrumbList (dentro de su <Helmet>); los 3 globales (Organization/WebSite/
// SoftwareApplication) los inyecta SEOHead y van al layout global, NO aquí. (4) LANG_SLUGS + SITE_URL copiados
// verbatim del componente para reconstruir canonicalUrl (ambas ramas del ternario original son idénticas).

import { t } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

const SITE_URL = 'https://aichef.pro';

const LANG_SLUGS: Record<string, string> = {
  es: 'herramientas-gratuitas',
  en: 'en/free-tools-restaurants',
  fr: 'fr/outils-gratuits-restaurant',
  de: 'de/kostenlose-tools-restaurant',
  it: 'it/strumenti-gratuiti-ristorante',
  pt: 'pt/ferramentas-gratuitas-restaurante',
  nl: 'nl/gratis-tools-restaurant',
};

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl = `${SITE_URL}/${canonicalSlug}`;

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'toolHub.breadcrumb'), item: canonicalUrl },
    ],
  };

  return {
    title: t(lang, 'toolHub.seo.title'),
    description: t(lang, 'toolHub.seo.description'),
    keywords: t(lang, 'toolHub.seo.keywords'),
    schemas: [breadcrumbSchema],
  };
}
