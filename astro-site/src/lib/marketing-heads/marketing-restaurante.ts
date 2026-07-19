// Head module server-side de la landing "Marketing para Restaurantes con IA".
// Origen (spec verbatim): src/pages/MarketingRestaurante.tsx — que en Astro se monta como
// island client:only (su react-helmet es un no-op shim), así que TODO lo SEO-relevante del
// <head> debe emitirse en build desde aquí. Replica el <SEOHead title/description/keywords>
// (los 3 se pasan EXPLÍCITOS desde landingMarketing.seo.* → sin fallback a seo.* global) y
// los 2 JSON-LD propios de su <Helmet>: BreadcrumbList + FAQPage.
// Decisiones no obvias:
//  - ogImage se OMITE: la SPA no pasa `ogImage` a <SEOHead>, usa la default /og-image.jpg.
//  - canonicalUrl se reconstruye con LANG_SLUGS + SITE_URL (copiados verbatim del
//    componente). Aquí los slugs NO llevan prefijo de idioma, así que el ternario es→raíz /
//    otros→`/${lang}/…` es load-bearing y se conserva tal cual (NO se colapsa). El breadcrumb
//    item posición 2 apunta a él.
//  - Se EXCLUYEN los 3 schemas globales (Organization/WebSite/SoftwareApplication) de
//    SEOHead.tsx; van al layout global en otro slice. También se excluyen los <link hreflang>
//    del <Helmet> (los emite BaseLayout).
//  - La SPA interpola { userCount } en todas sus claves; ni seo.* ni breadcrumb contienen
//    el placeholder {{userCount}} (verificado en es.json), así que t()/tObjects sin
//    interpolación reproduce el mismo texto.
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

const SITE_URL = 'https://aichef.pro';

// Copiado verbatim de src/pages/MarketingRestaurante.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'marketing-restaurante-ia',
  en: 'restaurant-marketing-ai',
  fr: 'marketing-restaurant-ia',
  de: 'restaurant-marketing-ki',
  it: 'marketing-ristorante-ia',
  pt: 'marketing-restaurante-ia-pt',
  nl: 'restaurant-marketing-ai-nl',
};

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl =
    lang === 'es'
      ? `${SITE_URL}/${canonicalSlug}`
      : `${SITE_URL}/${lang}/${canonicalSlug}`;

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingMarketing.faq');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingMarketing.breadcrumb'), item: canonicalUrl },
    ],
  };

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((f) => ({
      '@type': 'Question',
      name: f.question,
      acceptedAnswer: { '@type': 'Answer', text: f.answer },
    })),
  };

  return {
    title: t(lang, 'landingMarketing.seo.title'),
    description: t(lang, 'landingMarketing.seo.description'),
    keywords: t(lang, 'landingMarketing.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
