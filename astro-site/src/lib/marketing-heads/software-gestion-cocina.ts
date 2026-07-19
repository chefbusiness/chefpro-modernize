// Head module server-side para la landing /software-gestion-cocina-ia (y variantes por idioma).
// Origen: src/pages/SoftwareGestionCocina.tsx (island client:only en Astro → su Helmet es no-op,
// por eso el SEO del <head> se emite en build desde aquí).
// Decisiones no obvias: la SPA pasa title/description/keywords EXPLÍCITOS a <SEOHead> (claves
// landingSoftwareGestion.seo.*), así que NO aplica el fallback a seo.* global. No pasa ogImage →
// usa la default /og-image.jpg → se omite el campo. Emite 2 JSON-LD propios (BreadcrumbList + FAQPage);
// se excluyen los 3 globales de SEOHead (Organization/WebSite/SoftwareApplication → layout global).
// LANG_SLUGS y SITE_URL copiados verbatim del componente para reconstruir el canonicalUrl del breadcrumb.
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

// Copiado verbatim de src/pages/SoftwareGestionCocina.tsx
const LANG_SLUGS: Record<string, string> = {
  es: 'software-gestion-cocina-ia',
  en: 'kitchen-management-software-ai',
  fr: 'logiciel-gestion-cuisine-ia',
  de: 'kuechenverwaltung-ki',
  it: 'software-gestione-cucina-ia',
  pt: 'software-gestao-cozinha-ia',
  nl: 'keuken-software-ai',
};

const SITE_URL = 'https://aichef.pro';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const title = t(lang, 'landingSoftwareGestion.seo.title');
  const description = t(lang, 'landingSoftwareGestion.seo.description');
  const keywords = t(lang, 'landingSoftwareGestion.seo.keywords');

  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl = lang === 'es'
    ? `${SITE_URL}/${canonicalSlug}`
    : `${SITE_URL}/${lang}/${canonicalSlug}`;

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingSoftwareGestion.faq');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingSoftwareGestion.breadcrumb'), item: canonicalUrl },
    ],
  };

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map(f => ({
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
