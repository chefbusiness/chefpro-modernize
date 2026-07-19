// Head module server-side de la landing "Reducir Costes de Restaurante con IA".
// Origen (spec verbatim): src/pages/ReducirCostesRestaurante.tsx — que en Astro se monta como
// island client:only (su react-helmet es un no-op shim), así que TODO lo SEO-relevante del
// <head> debe emitirse en build desde aquí. Replica el <SEOHead title/description/keywords>
// (los 3 se pasan EXPLÍCITOS desde landingCostes.seo.* → sin fallback a seo.* global) y los
// 2 JSON-LD propios de su <Helmet>: BreadcrumbList + FAQPage (mismo orden que la SPA).
// Decisiones no obvias:
//  - ogImage se OMITE: la SPA no pasa `ogImage` a <SEOHead>, usa la default /og-image.jpg.
//  - canonicalUrl se reconstruye con LANG_SLUGS + SITE_URL (copiados verbatim del componente).
//    Los slugs NO llevan prefijo de idioma → el ternario es→raíz `/slug` / otros→`/${lang}/slug`
//    es load-bearing y se conserva tal cual. El breadcrumb item posición 2 apunta a él.
//  - Se EXCLUYEN los 3 schemas globales (Organization/WebSite/SoftwareApplication) de SEOHead.tsx
//    (van al layout global) y los <link hreflang> del <Helmet> (los emite BaseLayout).
//  - La SPA interpola { userCount } en sus claves; ni seo.* ni breadcrumb ni faq contienen el
//    placeholder {{userCount}} (verificado en es.json: solo hero.tagline y cta_section.subtitle,
//    no SEO-relevantes), así que t()/tObjects sin interpolación reproduce el mismo texto.
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

const SITE_URL = 'https://aichef.pro';

// Copiado verbatim de src/pages/ReducirCostesRestaurante.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'reducir-costes-restaurante-ia',
  en: 'reduce-restaurant-costs-ai',
  fr: 'reduire-couts-restaurant-ia',
  de: 'restaurantkosten-senken-ki',
  it: 'ridurre-costi-ristorante-ia',
  pt: 'reduzir-custos-restaurante-ia',
  nl: 'restaurantkosten-verlagen-ai',
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

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingCostes.faq');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingCostes.breadcrumb'), item: canonicalUrl },
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
    title: t(lang, 'landingCostes.seo.title'),
    description: t(lang, 'landingCostes.seo.description'),
    keywords: t(lang, 'landingCostes.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
