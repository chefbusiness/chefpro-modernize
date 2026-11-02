// Head module server-side de la página /simulador-rentabilidad-restaurante (y slugs por idioma).
// Origen (spec verbatim): src/pages/SimuladorRentabilidad.tsx — su <Helmet> es un no-op shim al
// montarse como island client:only, así que el SEO del <head> se emite en build desde aquí.
// La SPA pasa a <SEOHead> title/description/keywords EXPLÍCITOS (claves toolRentabilidad.seo.*) →
// NO aplica el fallback a seo.title/description/keywords globales de SEOHead.tsx.
// Decisiones no obvias:
//  - ogImage se OMITE: la SPA no pasa `ogImage` a <SEOHead> → default /og-image.jpg (BaseLayout).
//  - LANG_SLUGS copiado verbatim; canonicalUrl = `${SITE_URL}/${slug}` (las dos ramas es/no-es
//    del ternario de la SPA son idénticas → se colapsan). El breadcrumb item 3 apunta a él.
//  - `s('breadcrumb')` = t(lang, 'toolRentabilidad.breadcrumb') plano (sin interpolación).
//  - Emito los 2 JSON-LD propios en el mismo orden de su <Helmet>: BreadcrumbList + FAQPage.
//    Se EXCLUYEN los 3 schemas globales (Organization/WebSite/SoftwareApplication) de SEOHead.tsx.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

const SITE_URL = 'https://aichef.pro';

// Copiado verbatim de src/pages/SimuladorRentabilidad.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'simulador-rentabilidad-restaurante',
  en: 'en/restaurant-profit-simulator',
  fr: 'fr/simulateur-rentabilite-restaurant',
  de: 'de/rentabilitaet-simulator-restaurant',
  it: 'it/simulatore-redditivita-ristorante',
  pt: 'pt/simulador-rentabilidade-restaurante',
  nl: 'nl/winstgevendheid-simulator-restaurant',
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

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'toolRentabilidad.faq');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'Herramientas Gratuitas', item: `${SITE_URL}/herramientas-gratuitas` },
      { '@type': 'ListItem', position: 3, name: t(lang, 'toolRentabilidad.breadcrumb'), item: canonicalUrl },
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
    title: t(lang, 'toolRentabilidad.seo.title'),
    description: t(lang, 'toolRentabilidad.seo.description'),
    keywords: t(lang, 'toolRentabilidad.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
