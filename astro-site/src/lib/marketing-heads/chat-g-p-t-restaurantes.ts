// Head module server-side de la página /chatgpt-para-restaurantes (y slugs por idioma).
// Origen: src/pages/ChatGPTRestaurantes.tsx (SPA). Ese componente usa <SEOHead> con
// title/description/keywords explícitos + un <Helmet> con dos JSON-LD propios
// (BreadcrumbList y luego FAQPage). Decisiones no obvias:
//  - title/description/keywords son literales de la página (claves landingChatGPT.seo.*),
//    así que NO aplica el fallback de SEOHead (seo.title/description/keywords).
//  - No pasa og:image custom → ogImage se omite (BaseLayout usa /og-image.jpg).
//  - El item[2] del breadcrumb usa el canonicalUrl que la propia página calcula desde
//    LANG_SLUGS + SITE_URL (copiados verbatim); ES sin prefijo de idioma, resto con /<lang>/.
//  - Los `{{userCount}}` sólo viven en results/cta_section (no head) → sin interpolación aquí.
//  - Excluidos los 3 schemas globales (Organization/WebSite/SoftwareApplication) de SEOHead:
//    van al layout global. schemas = [BreadcrumbList, FAQPage], en el mismo orden que la SPA.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

// Copiados verbatim del componente ChatGPTRestaurantes.tsx.
const LANG_SLUGS: Record<string, string> = {
  es: 'chatgpt-para-restaurantes',
  en: 'chatgpt-for-restaurants',
  fr: 'chatgpt-pour-restaurants',
  de: 'chatgpt-fuer-restaurants',
  it: 'chatgpt-per-ristoranti',
  pt: 'chatgpt-para-restaurantes',
  nl: 'chatgpt-voor-restaurants',
};

const SITE_URL = 'https://aichef.pro';

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

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingChatGPT.breadcrumb'), item: canonicalUrl },
    ],
  };

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingChatGPT.faq');
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
    title: t(lang, 'landingChatGPT.seo.title'),
    description: t(lang, 'landingChatGPT.seo.description'),
    keywords: t(lang, 'landingChatGPT.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
