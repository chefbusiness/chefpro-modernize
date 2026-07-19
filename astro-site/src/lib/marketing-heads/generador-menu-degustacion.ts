// Head module server-side de la página /generador-menu-degustacion.
// Origen: src/pages/GeneradorMenuDegustacion.tsx (SPA). Ese componente emite su propio
// <Helmet> (NO usa <SEOHead>) con title/description/keywords explícitos y un único
// JSON-LD propio (FAQPage). Decisiones no obvias:
//  - title/description/keywords son literales de la página (claves toolDegustacion.seo.*),
//    así que NO aplica el fallback de SEOHead (seo.title/description/keywords).
//  - No pasa og:image custom en su Helmet → ogImage se omite (BaseLayout usa /og-image.jpg).
//  - FAQPage se construye desde toolDegustacion.faq (array de objetos {q,a}); si está vacío,
//    la SPA no lo emite → schemas: []. Los 3 schemas globales van al layout, no aquí.
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const faqItems = tObjects<{ q: string; a: string }>(lang, 'toolDegustacion.faq');

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
    title: t(lang, 'toolDegustacion.seo.title'),
    description: t(lang, 'toolDegustacion.seo.description'),
    keywords: t(lang, 'toolDegustacion.seo.keywords'),
    schemas,
  };
}
