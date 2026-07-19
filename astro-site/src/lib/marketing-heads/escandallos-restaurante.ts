// Head module server-side de la página /escandallos-restaurante-ia (y slugs por idioma).
// Origen: src/pages/EscandallosRestaurante.tsx (SPA). Ese componente usa <SEOHead> con
// title/description/keywords EXPLÍCITOS (claves landingEscandallos.seo.*) + un <Helmet>
// propio con DOS JSON-LD: BreadcrumbList y FAQPage. Decisiones no obvias:
//  - Como pasa title/description/keywords, NO aplica el fallback de SEOHead (seo.title/…).
//  - No pasa og:image custom → ogImage se omite (BaseLayout usa /og-image.jpg por defecto).
//  - SITE_URL y LANG_SLUGS se copian verbatim de la SPA; canonicalUrl = `${SITE_URL}/${slug}`
//    (ambas ramas es/no-es de la SPA son idénticas). `s('breadcrumb')` interpola userCount
//    en la SPA, pero la cadena no contiene {{userCount}} → t() plano es equivalente.
//  - Emito los 2 schemas SIEMPRE y en el mismo orden del <Helmet> (breadcrumb, faq); los 3
//    schemas globales (Organization/WebSite/SoftwareApplication) van al layout, no aquí.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

const SITE_URL = 'https://aichef.pro';

const LANG_SLUGS: Record<string, string> = {
  es: 'escandallos-restaurante-ia',
  en: 'en/food-cost-calculator-restaurant-ai',
  fr: 'fr/calcul-food-cost-restaurant-ia',
  de: 'de/food-cost-rechner-restaurant-ki',
  it: 'it/food-cost-ristorante-ia',
  pt: 'pt/escandallo-restaurante-ia',
  nl: 'nl/food-cost-berekening-restaurant-ai',
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

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingEscandallos.faq');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingEscandallos.breadcrumb'), item: canonicalUrl },
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
    title: t(lang, 'landingEscandallos.seo.title'),
    description: t(lang, 'landingEscandallos.seo.description'),
    keywords: t(lang, 'landingEscandallos.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
