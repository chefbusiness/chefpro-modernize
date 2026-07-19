// Head module server-side de la página /sistema-creditos.
// Origen (spec verbatim): src/pages/SistemaCreditos.tsx — que en Astro se monta como
// island client:only (su react-helmet es un no-op shim), así que TODO lo SEO-relevante
// del <head> debe emitirse en build desde aquí.
//
// Decisiones NO obvias:
//  - A diferencia de los head modules hermanos, esta página NO lee su contenido del i18n
//    JSON: su SEO (seoTitle/seoDescription/seoKeywords) y los datos de sus schemas viven
//    en un módulo TS de la SPA (src/data/sistema-creditos-faq.ts → CREDIT_FAQ_CONTENT).
//    Esas claves NO existen en src/i18n/locales/*.json, por lo que t()/tObjects() no las
//    resolverían. Para ser verbatim y DRY (misma doctrina que translations.ts, que importa
//    los JSON de la SPA como fuente única de verdad) se IMPORTA ese mismo módulo de datos
//    por ruta relativa en lugar de copiar ~700 líneas a mano.
//  - title/description/keywords se pasan EXPLÍCITOS a <SEOHead> → NO aplica el fallback
//    global seo.title/seo.description/seo.keywords.
//  - <SEOHead> se invoca SIN prop ogImage → usa la default /og-image.jpg → se OMITE.
//  - Schemas propios (en su <Helmet>, emitidos SIEMPRE): FAQPage y luego BreadcrumbList
//    (en ese orden). pageUrl se reconstruye verbatim del componente. Los 3 schemas
//    GLOBALES (Organization/WebSite/SoftwareApplication) de SEOHead quedan EXCLUIDOS.
import { CREDIT_FAQ_CONTENT } from '../../../../src/data/sistema-creditos-faq';
import type { Locale } from '../../i18n/config';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  // Mirror del guard de la SPA: Locale ⊆ las claves de CREDIT_FAQ_CONTENT, pero se
  // replica el fallback a 'es' para ser fiel al componente.
  const c = lang in CREDIT_FAQ_CONTENT ? CREDIT_FAQ_CONTENT[lang] : CREDIT_FAQ_CONTENT.es;

  // Reconstruido verbatim de src/pages/SistemaCreditos.tsx.
  const pageUrl =
    lang === 'es'
      ? 'https://aichef.pro/sistema-creditos'
      : `https://aichef.pro/${lang}/sistema-creditos`;

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: c.faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.q,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.a.join('\n\n'),
      },
    })),
  };

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'AI Chef Pro',
        item: 'https://aichef.pro',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: c.breadcrumb,
        item: pageUrl,
      },
    ],
  };

  return {
    title: c.seoTitle,
    description: c.seoDescription,
    keywords: c.seoKeywords,
    schemas: [faqSchema, breadcrumbSchema],
  };
}
