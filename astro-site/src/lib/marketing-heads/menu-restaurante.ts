// Head module server-side de la landing "Carta y Menú de Restaurante con IA".
// Origen: src/pages/MenuRestaurante.tsx (SPA). En Astro esa página se monta como
// island client:only, por lo que su <Helmet> es un no-op shim: title/description/
// keywords y sus JSON-LD propios deben emitirse en build desde aquí.
// Decisiones no obvias:
//  - La SPA NO pasa ogImage a <SEOHead> => usa la default /og-image.jpg => se omite aquí.
//  - schemas propios de la página: BreadcrumbList + FAQPage (en ese orden, como en el
//    <Helmet>). Se EXCLUYEN los 3 globales de SEOHead (Organization/WebSite/SoftwareApplication).
//  - LANG_SLUGS y SITE_URL copiados verbatim de la SPA para reconstruir canonicalUrl del breadcrumb.
//  - El userCount que la SPA interpola vía s()/k() no aparece en seo/breadcrumb/faq (verificado), así que no aplica.
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

// Copiados verbatim de src/pages/MenuRestaurante.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'carta-menu-restaurante-ia',
  en: 'restaurant-menu-ai',
  fr: 'carte-menu-restaurant-ia',
  de: 'speisekarte-restaurant-ki',
  it: 'menu-ristorante-ia',
  pt: 'cardapio-restaurante-ia',
  nl: 'restaurantmenu-ai',
};

const SITE_URL = 'https://aichef.pro';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const title = t(lang, 'landingMenu.seo.title');
  const description = t(lang, 'landingMenu.seo.description');
  const keywords = t(lang, 'landingMenu.seo.keywords');

  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl =
    lang === 'es'
      ? `${SITE_URL}/${canonicalSlug}`
      : `${SITE_URL}/${lang}/${canonicalSlug}`;

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingMenu.breadcrumb'), item: canonicalUrl },
    ],
  };

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingMenu.faq');
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
    title,
    description,
    keywords,
    schemas: [breadcrumbSchema, faqSchema],
  };
}
