// Head module server-side de la página /generador-textos-carta-restaurante.
// Origen (spec verbatim): src/pages/GeneradorTextosCarta.tsx (SPA). Ese componente emite
// su propio <Helmet> (NO usa <SEOHead>) con title/description/keywords explícitos y un
// único JSON-LD propio (FAQPage). Al montarse como island client:only su Helmet es un
// no-op shim, así que el SEO del <head> se emite en build desde aquí. Decisiones no obvias:
//  - title/description/keywords salen de t('toolMenuCopy.seo', {returnObjects}) → .title /
//    .description / .keywords, es decir claves toolMenuCopy.seo.*; al no usar <SEOHead> NO
//    aplica el fallback global (seo.title/description/keywords).
//  - No pasa og:image custom en su Helmet → ogImage se omite (BaseLayout usa /og-image.jpg).
//  - FAQPage se construye desde toolMenuCopy.faq (array de objetos {q,a}); si está vacío,
//    la SPA no lo emite → schemas: []. Los 3 schemas globales (Organization/WebSite/
//    SoftwareApplication de SEOHead.tsx) NO se emiten aquí, van al layout global en otro slice.
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const faqItems = tObjects<{ q: string; a: string }>(lang, 'toolMenuCopy.faq');

  const schemas: object[] = [];
  if (Array.isArray(faqItems) && faqItems.length > 0) {
    schemas.push({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: faqItems.map((f) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    });
  }

  return {
    title: t(lang, 'toolMenuCopy.seo.title'),
    description: t(lang, 'toolMenuCopy.seo.description'),
    keywords: t(lang, 'toolMenuCopy.seo.keywords'),
    schemas,
  };
}
