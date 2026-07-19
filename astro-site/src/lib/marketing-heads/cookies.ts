// Head module server-side de la página /cookies.
// Origen: src/pages/Cookies.tsx (SPA). Como en Astro se monta client:only con Helmet no-op,
// aquí se reconstruye lo SEO-relevante del head en build.
// Decisiones: title/description/keywords = claves i18n que la SPA pasa a <SEOHead> (pages.cookies.seo_*).
// No pasa ogImage custom -> se omite (usa la default /og-image.jpg del layout). schemas = el único
// JSON-LD propio de la página: el BreadcrumbList de su <Helmet> (name pos.2 = pages.cookies.heading;
// URLs literales verbatim de la SPA). Se EXCLUYEN los 3 schemas globales de SEOHead (Organization/WebSite/SoftwareApplication).
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
        name: t(lang, 'pages.cookies.heading'),
        item: 'https://aichef.pro/cookies',
      },
    ],
  };

  return {
    title: t(lang, 'pages.cookies.seo_title'),
    description: t(lang, 'pages.cookies.seo_description'),
    keywords: t(lang, 'pages.cookies.seo_keywords'),
    schemas: [breadcrumbSchema],
  };
}
