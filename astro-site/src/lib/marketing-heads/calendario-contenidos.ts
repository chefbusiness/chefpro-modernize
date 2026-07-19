// Head module SSR de la página /calendario-contenidos-restaurante (herramienta gratuita).
// Origen: src/pages/CalendarioContenidos.tsx (island client:only en Astro → su <Helmet> es no-op shim).
// Decisiones no obvias:
//  - La SPA NO usa <SEOHead>: su propio <Helmet> pasa title/description/keywords directos desde
//    toolCalendario.seo.{title,description,keywords} → sin fallback a seo.* (las 3 claves existen en es.json).
//  - Único JSON-LD propio de la página = FAQPage construido desde toolCalendario.faq (array de {q,a});
//    se emite solo si hay items (mismo guard `faqItems.length > 0` de la SPA), si no schemas: [].
//  - No hay og:image custom en su Helmet → se omite ogImage (usa la default /og-image.jpg del layout).
//  - Excluidos por contrato: robots/canonical/hreflang/og:*/twitter:* (BaseLayout) y los 3 schemas
//    globales Organization/WebSite/SoftwareApplication (SEOHead → layout global).
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  const faqItems = tObjects<{ q: string; a: string }>(lang, 'toolCalendario.faq');

  const schemas: object[] =
    faqItems.length > 0
      ? [
          {
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            mainEntity: faqItems.map((f) => ({
              '@type': 'Question',
              name: f.q,
              acceptedAnswer: { '@type': 'Answer', text: f.a },
            })),
          },
        ]
      : [];

  return {
    title: t(lang, 'toolCalendario.seo.title'),
    description: t(lang, 'toolCalendario.seo.description'),
    keywords: t(lang, 'toolCalendario.seo.keywords'),
    schemas,
  };
}
