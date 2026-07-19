// Head module server-side de la página Privacy (SPA: src/pages/Privacy.tsx).
// En Astro esa página se monta como island client:only (su Helmet es un no-op),
// así que todo el <head> SEO se emite en build desde aquí.
// Decisiones no obvias: la SPA pasa title/description/keywords EXPLÍCITOS a <SEOHead>
// (claves pages.privacy.seo_*), por lo que NO aplica el fallback seo.*; no pasa ogImage
// (usa la default /og-image.jpg) → se omite. Único schema propio: BreadcrumbList (verbatim
// de la SPA): "Home" es literal (no i18n) y el 2º crumb usa t(lang,'pages.privacy.heading')
// con item literal 'https://aichef.pro/privacidad'. Los 3 schemas globales de SEOHead
// (Organization/WebSite/SoftwareApplication) van al layout global, no aquí.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'Home',
        item: 'https://aichef.pro',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: t(lang, 'pages.privacy.heading'),
        item: 'https://aichef.pro/privacidad',
      },
    ],
  };

  return {
    title: t(lang, 'pages.privacy.seo_title'),
    description: t(lang, 'pages.privacy.seo_description'),
    keywords: t(lang, 'pages.privacy.seo_keywords'),
    schemas: [breadcrumbSchema],
  };
}
