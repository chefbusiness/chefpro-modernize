// Head module server-side de la página /legales (Aviso Legal).
// Origen SPA: src/pages/Legal.tsx (montada en Astro como island client:only → su Helmet es no-op shim).
// title/description/keywords: la SPA los pasa EXPLÍCITOS a <SEOHead> (claves pages.legal.seo_*),
//   por lo que NO aplica el fallback a seo.* de SEOHead.tsx. ogImage: la SPA no pasa custom → default /og-image.jpg → omitido.
// schemas: el único JSON-LD propio de la página es el BreadcrumbList que emite en su <Helmet>
//   (name "Home" es literal en el componente, no i18n; item URL literal '.../legales'; name del 2º ítem = pages.legal.heading).
//   Se EXCLUYEN los 3 schemas globales (Organization/WebSite/SoftwareApplication) que inyecta SEOHead → van al layout global.
import { t } from '../../i18n/translations';
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
        name: t(lang, 'pages.legal.heading'),
        item: 'https://aichef.pro/legales',
      },
    ],
  };

  return {
    title: t(lang, 'pages.legal.seo_title'),
    description: t(lang, 'pages.legal.seo_description'),
    keywords: t(lang, 'pages.legal.seo_keywords'),
    schemas: [breadcrumbSchema],
  };
}
