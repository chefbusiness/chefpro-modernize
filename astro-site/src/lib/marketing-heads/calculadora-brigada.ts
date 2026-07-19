// Head module server-side de la Calculadora de Brigada (herramienta gratuita).
// Origen (spec verbatim): src/pages/CalculadoraBrigada.tsx — que en Astro se monta
// como island client:only (su react-helmet es un no-op shim), así que TODO lo
// SEO-relevante del <head> debe emitirse en build desde aquí.
//
// Decisiones no obvias:
// - La página NO usa <SEOHead>: emite su propio <Helmet> con title/description/
//   keywords EXPLÍCITOS → no aplica ningún fallback a seo.title/seo.description/
//   seo.keywords. Se replican las mismas claves toolBrigada.seo.*.
// - No emite <meta og:image> propio → usa la default /og-image.jpg → ogImage se OMITE.
// - Único JSON-LD propio de la página: el FAQPage construido desde toolBrigada.faq
//   (returnObjects → array de {q,a}). Sin BreadcrumbList/HowTo/WebApplication.
//   Solo se incluye si hay ≥1 item (mismo condicional que la SPA), y NO contiene URLs.
// - Los 3 schemas GLOBALES (Organization/WebSite/SoftwareApplication) los inyecta
//   SEOHead en la SPA → EXCLUIDOS aquí (van al layout global en otro slice).
import { t, tObjects } from '../../i18n/translations';
import type { Locale } from '../../i18n/config';

interface FaqItem {
  q: string;
  a: string;
}

export function head(lang: Locale): {
  title: string;
  description: string;
  keywords: string;
  ogImage?: string;
  schemas: object[];
} {
  // Título / descripción / keywords: claves explícitas de la SPA (sin fallback SEOHead).
  const title = t(lang, 'toolBrigada.seo.title');
  const description = t(lang, 'toolBrigada.seo.description');
  const keywords = t(lang, 'toolBrigada.seo.keywords');

  // Único schema propio: FAQPage desde toolBrigada.faq (condicional a que haya items).
  const faqItems = tObjects<FaqItem>(lang, 'toolBrigada.faq');
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

  return { title, description, keywords, schemas };
}
