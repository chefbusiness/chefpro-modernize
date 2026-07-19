// Head module server-side de la página de marketing "Calculadora Food Cost".
// Origen (spec verbatim): src/pages/CalculadoraFoodCost.tsx — su <Helmet> es un no-op
// shim al montarse como island client:only, así que el SEO del <head> se emite en build
// desde aquí. Replica el <SEOHead title/description/keywords> (todos con clave propia
// toolFoodCost.seo.*, la página SIEMPRE los pasa → sin fallback a seo.* global) y los 2
// JSON-LD propios de su <Helmet>: BreadcrumbList + FAQPage.
// Decisiones no obvias:
//  - ogImage se OMITE: la SPA no pasa `ogImage` a <SEOHead>, usa la default /og-image.jpg.
//  - canonicalUrl se reconstruye con LANG_SLUGS (copiado verbatim del componente): el
//    breadcrumb item de posición 3 apunta a él; el ternario de la SPA es redundante
//    (ambas ramas dan `${SITE_URL}/${canonicalSlug}`), se colapsa a esa expresión.
//  - Se EXCLUYEN los 3 schemas globales (Organization/WebSite/SoftwareApplication) de
//    SEOHead.tsx; van al layout global en otro slice.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

const SITE_URL = 'https://aichef.pro';

// Copiado verbatim de src/pages/CalculadoraFoodCost.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'calculadora-food-cost-restaurante',
  en: 'en/food-cost-calculator-restaurant',
  fr: 'fr/calculateur-food-cost-restaurant',
  de: 'de/food-cost-rechner-restaurant',
  it: 'it/calcolatore-food-cost-ristorante',
  pt: 'pt/calculadora-food-cost-restaurante',
  nl: 'nl/food-cost-calculator-restaurant',
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

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'toolFoodCost.faq');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'Herramientas Gratuitas', item: `${SITE_URL}/herramientas-gratuitas` },
      { '@type': 'ListItem', position: 3, name: t(lang, 'toolFoodCost.breadcrumb'), item: canonicalUrl },
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
    title: t(lang, 'toolFoodCost.seo.title'),
    description: t(lang, 'toolFoodCost.seo.description'),
    keywords: t(lang, 'toolFoodCost.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
