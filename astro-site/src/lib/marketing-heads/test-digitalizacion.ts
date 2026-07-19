// Head module server-side de la página /test-digitalizacion-restaurante (y slugs por idioma).
// Origen (spec verbatim): src/pages/TestDigitalizacion.tsx — su <Helmet> es un no-op shim al
// montarse como island client:only, así que el SEO del <head> se emite en build desde aquí.
// Decisiones no obvias:
//  - Esta página NO usa <SEOHead>: escribe DIRECTAMENTE en <Helmet> title/description/keywords
//    SIEMPRE explícitos (claves toolScore.seo.*) → no hay fallback a seo.* global que aplicar.
//  - ogImage se OMITE: la página no emite og:image → default /og-image.jpg (BaseLayout).
//  - Único JSON-LD propio = FAQPage (con campos q/a), y SOLO si toolScore.faq es array no vacío
//    (idéntico al ternario faqSchema de la SPA). NO emite BreadcrumbList aunque exista la clave
//    toolScore.breadcrumb — no se añade nada que la SPA no emita. Se EXCLUYEN los 3 schemas
//    globales (Organization/WebSite/SoftwareApplication) de SEOHead.tsx → van al layout global.
import { t, tList, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const faqItems = tObjects<{ q: string; a: string }>(lang, 'toolScore.faq');

  const faqSchema =
    faqItems.length > 0
      ? {
          '@context': 'https://schema.org',
          '@type': 'FAQPage',
          mainEntity: faqItems.map((f) => ({
            '@type': 'Question',
            name: f.q,
            acceptedAnswer: { '@type': 'Answer', text: f.a },
          })),
        }
      : null;

  return {
    title: t(lang, 'toolScore.seo.title'),
    description: t(lang, 'toolScore.seo.description'),
    keywords: t(lang, 'toolScore.seo.keywords'),
    schemas: faqSchema ? [faqSchema] : [],
  };
}
