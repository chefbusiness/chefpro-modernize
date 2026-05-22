import { Helmet } from 'react-helmet-async';
import { Coins } from 'lucide-react';
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import { useLanguage } from '@/hooks/useLanguage';
import {
  CREDIT_FAQ_CONTENT,
  SUPPORT_EMAIL,
  type FaqLang,
} from '@/data/sistema-creditos-faq';

/** Renders a paragraph, turning any occurrence of the support email into a mailto link. */
const renderParagraph = (text: string, key: number) => {
  const parts = text.split(SUPPORT_EMAIL);
  if (parts.length === 1) {
    return <p key={key}>{text}</p>;
  }
  return (
    <p key={key}>
      {parts.flatMap((part, i) =>
        i === 0
          ? [part]
          : [
              <a
                key={`mail-${i}`}
                href={`mailto:${SUPPORT_EMAIL}`}
                className="text-primary font-medium hover:underline"
              >
                {SUPPORT_EMAIL}
              </a>,
              part,
            ]
      )}
    </p>
  );
};

const SistemaCreditos = () => {
  const { currentLanguage } = useLanguage();
  const lang = (currentLanguage as FaqLang) in CREDIT_FAQ_CONTENT
    ? (currentLanguage as FaqLang)
    : 'es';
  const c = CREDIT_FAQ_CONTENT[lang];

  const pageUrl =
    lang === 'es'
      ? 'https://aichef.pro/sistema-creditos'
      : `https://aichef.pro/${lang}/sistema-creditos`;

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: c.faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.q,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.a.join('\n\n'),
      },
    })),
  };

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'AI Chef Pro',
        item: 'https://aichef.pro',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: c.breadcrumb,
        item: pageUrl,
      },
    ],
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={c.seoTitle}
        description={c.seoDescription}
        keywords={c.seoKeywords}
        canonical={pageUrl}
      />
      <Helmet>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
        <script type="application/ld+json">
          {JSON.stringify(breadcrumbSchema)}
        </script>
      </Helmet>
      <ModernHeader />
      <main className="py-16 md:py-24">
        <div className="container mx-auto px-4">
          <div className="max-w-3xl mx-auto">
            {/* Hero */}
            <div className="text-center mb-12">
              <div className="inline-flex items-center gap-2 rounded-full border border-primary/30 bg-primary/10 px-4 py-1.5 text-sm font-medium text-primary mb-6">
                <Coins className="h-4 w-4" />
                {c.badge}
              </div>
              <h1 className="text-3xl md:text-5xl font-bold text-foreground mb-4 text-balance">
                {c.h1}
              </h1>
              <p className="text-lg text-muted-foreground leading-7 text-balance">
                {c.intro}
              </p>
            </div>

            {/* FAQ */}
            <Accordion type="single" collapsible className="w-full">
              {c.faqs.map((faq, index) => (
                <AccordionItem key={index} value={`item-${index}`}>
                  <AccordionTrigger className="text-left text-base md:text-lg font-semibold hover:no-underline">
                    {faq.q}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground leading-7 space-y-3 pb-5">
                    {faq.a.map((paragraph, i) => renderParagraph(paragraph, i))}
                  </AccordionContent>
                </AccordionItem>
              ))}
            </Accordion>

            {/* Support CTA */}
            <div className="mt-12 rounded-2xl border border-border bg-muted/40 p-8 text-center">
              <h2 className="text-xl md:text-2xl font-bold text-foreground mb-2">
                {c.supportTitle}
              </h2>
              <p className="text-muted-foreground mb-5">{c.supportText}</p>
              <a
                href={`mailto:${SUPPORT_EMAIL}`}
                className="inline-flex items-center justify-center rounded-lg bg-primary px-6 py-3 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90"
              >
                {c.supportCta.replace('{email}', SUPPORT_EMAIL)}
              </a>
            </div>
          </div>
        </div>
      </main>
      <ModernFooter />
    </div>
  );
};

export default SistemaCreditos;
