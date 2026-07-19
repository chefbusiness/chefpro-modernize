// Head module server-side de la landing "Herramientas de IA para Restaurantes".
// Origen (spec verbatim): src/pages/HerramientasIARestaurantes.tsx — que en Astro se
// monta como island client:only (su react-helmet es un no-op shim), así que TODO lo
// SEO-relevante del <head> debe emitirse en build desde aquí.
//
// Decisiones no obvias:
// - title/description/keywords: la página SÍ los pasa EXPLÍCITOS a <SEOHead> vía
//   s('seo.title'|'seo.description'|'seo.keywords') = t('landingRestaurantes.seo.*')
//   → NO aplica ningún fallback a seo.title/seo.description/seo.keywords globales.
// - ogImage: <SEOHead> se invoca SIN prop ogImage → usa la default /og-image.jpg → se OMITE.
// - schemas propios de la página (en su <Helmet>): BreadcrumbList + FAQPage, ambos
//   emitidos SIN condicional en la SPA → se replican SIEMPRE. LANG_SLUGS y SITE_URL
//   se copian VERBATIM del componente para reconstruir canonicalUrl (usado en el
//   breadcrumb) idéntico a la SPA. Los 3 schemas GLOBALES (Organization/WebSite/
//   SoftwareApplication) que inyecta SEOHead quedan EXCLUIDOS (van al layout global).
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

// Copiado verbatim de src/pages/HerramientasIARestaurantes.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'herramientas-ia-para-restaurantes',
  en: 'ai-tools-for-restaurants',
  fr: 'outils-ia-restaurant',
  de: 'ki-tools-restaurant',
  it: 'strumenti-ia-ristorante',
  pt: 'ferramentas-ia-restaurante',
  nl: 'ai-tools-restaurant',
};

const SITE_URL = 'https://aichef.pro';

interface FaqItem {
  question: string;
  answer: string;
}

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  // Claves explícitas pasadas a <SEOHead> (sin fallback global).
  const title = t(lang, 'landingRestaurantes.seo.title');
  const description = t(lang, 'landingRestaurantes.seo.description');
  const keywords = t(lang, 'landingRestaurantes.seo.keywords');

  // canonicalUrl reconstruido idéntico a la SPA (usado por el BreadcrumbList).
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
      {
        '@type': 'ListItem',
        position: 2,
        name: t(lang, 'landingRestaurantes.breadcrumb'),
        item: canonicalUrl,
      },
    ],
  };

  const faqs = tObjects<FaqItem>(lang, 'landingRestaurantes.faq');
  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((f) => ({
      '@type': 'Question',
      name: f.question,
      acceptedAnswer: { '@type': 'Answer', text: f.answer },
    })),
  };

  return { title, description, keywords, schemas: [breadcrumbSchema, faqSchema] };
}
