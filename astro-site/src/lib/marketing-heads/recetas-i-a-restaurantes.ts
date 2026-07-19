// Head module server-side de la página /recetas-ia-restaurantes (y slugs por idioma).
// Origen: src/pages/RecetasIARestaurantes.tsx (SPA). Ese componente usa <SEOHead> con
// title/description/keywords explícitos (claves landingRecetas.seo.*) + un <Helmet> con
// dos JSON-LD propios en este orden: BreadcrumbList y luego FAQPage. Decisiones no obvias:
//  - title/description/keywords son literales de la página → NO aplica el fallback de
//    SEOHead (seo.title/description/keywords).
//  - No pasa og:image custom → ogImage se omite (BaseLayout usa /og-image.jpg).
//  - VERBATIM (la SPA es la spec): en este componente los LANG_SLUGS de los idiomas != es
//    YA incluyen el prefijo de idioma (p.ej. 'fr/recettes-ia-restaurants'), y aun así la
//    página antepone otro `/<lang>/` al construir canonicalUrl. Se replica tal cual, así que
//    el item[2] del breadcrumb queda con doble prefijo (…/fr/fr/…) para fr/de/it/pt/nl. Es
//    reproducción fiel del comportamiento de la SPA, no un error de este módulo.
//  - Los `{{userCount}}` sólo viven en results/cta_section (no head) → sin interpolación aquí.
//  - Excluidos los 3 schemas globales (Organization/WebSite/SoftwareApplication) de SEOHead:
//    van al layout global. schemas = [BreadcrumbList, FAQPage], mismo orden que la SPA.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

// Copiados verbatim del componente RecetasIARestaurantes.tsx.
const LANG_SLUGS: Record<string, string> = {
  es: 'recetas-ia-restaurantes',
  en: 'ai-recipes-for-restaurants',
  fr: 'fr/recettes-ia-restaurants',
  de: 'de/ki-rezepte-restaurants',
  it: 'it/ricette-ia-ristoranti',
  pt: 'pt/receitas-ia-restaurantes',
  nl: 'nl/ai-recepten-restaurants',
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
      { '@type': 'ListItem', position: 2, name: t(lang, 'landingRecetas.breadcrumb'), item: canonicalUrl },
    ],
  };

  const faqs = tObjects<{ question: string; answer: string }>(lang, 'landingRecetas.faq');
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
    title: t(lang, 'landingRecetas.seo.title'),
    description: t(lang, 'landingRecetas.seo.description'),
    keywords: t(lang, 'landingRecetas.seo.keywords'),
    schemas: [breadcrumbSchema, faqSchema],
  };
}
