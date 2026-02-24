import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CheckCircle, ArrowRight, ChefHat, TrendingDown, Clock, Star, Utensils, BarChart3, Megaphone, BookOpen } from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import { useLanguage } from '@/hooks/useLanguage';

const APP_URL = 'https://app.aichef.pro';

const TOOL_ICONS = [
  <BookOpen className="h-7 w-7 text-primary" />,
  <BarChart3 className="h-7 w-7 text-primary" />,
  <TrendingDown className="h-7 w-7 text-primary" />,
  <Utensils className="h-7 w-7 text-primary" />,
  <Megaphone className="h-7 w-7 text-primary" />,
  <ChefHat className="h-7 w-7 text-primary" />,
];

// URL slug per language
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

export default function HerramientasIARestaurantes() {
  const { t } = useTranslation();
  const { currentLanguage } = useLanguage();

  const k = (key: string) => t(`landingRestaurantes.${key}`, { returnObjects: true });
  const s = (key: string) => t(`landingRestaurantes.${key}`) as string;

  const results = k('results') as Array<{ metric: string; label: string }>;
  const tools = k('tools') as Array<{ title: string; description: string; keywords: string[] }>;
  const profiles = k('profiles') as Array<{ title: string; description: string }>;
  const benefits = k('why_section.benefits') as string[];
  const faqs = k('faq') as Array<{ question: string; answer: string }>;

  const canonicalSlug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = currentLanguage === 'es'
    ? `${SITE_URL}/${canonicalSlug}`
    : `${SITE_URL}/${currentLanguage}/${canonicalSlug}`;

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "AI Chef Pro", "item": SITE_URL },
      { "@type": "ListItem", "position": 2, "name": s('breadcrumb'), "item": canonicalUrl }
    ]
  };

  const faqSchema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": faqs.map(f => ({
      "@type": "Question",
      "name": f.question,
      "acceptedAnswer": { "@type": "Answer", "text": f.answer }
    }))
  };

  const plans = [
    { name: "AI Chef Miembro", price: "Gratis", uses: "5 usos/mes", highlight: false },
    { name: "AI Chef Premium Pro", price: "25€/mes", uses: "150 usos/mes", highlight: false },
    { name: "AI Chef Premium Plus", price: "50€/mes", uses: "350 usos/mes", highlight: true },
    { name: "AI Chef Premium Max", price: "95€/mes", uses: "Ilimitado", highlight: false },
  ];

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={s('seo.title')}
        description={s('seo.description')}
        keywords={s('seo.keywords')}
        canonical={canonicalUrl}
      />
      <Helmet>
        {/* Hreflang for all language versions */}
        {Object.entries(LANG_SLUGS).map(([lang, slug]) => {
          const href = lang === 'es' ? `${SITE_URL}/${slug}` : `${SITE_URL}/${lang}/${slug}`;
          return <link key={lang} rel="alternate" hrefLang={lang} href={href} />;
        })}
        <link rel="alternate" hrefLang="x-default" href={`${SITE_URL}/${LANG_SLUGS.es}`} />
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-primary/10 via-background to-secondary/5 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <Badge className="mb-6 text-sm px-4 py-2">{s('hero.badge')}</Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                {s('hero.h1')}
              </h1>
              <p className="text-xl text-muted-foreground mb-4 max-w-3xl mx-auto text-balance">
                {s('hero.subtitle')}
              </p>
              <p className="text-lg font-semibold text-primary mb-10">
                {s('hero.tagline')}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  {s('hero.cta_primary')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button size="lg" variant="outline" onClick={() => window.open(`${APP_URL}/pricing`, '_blank')}>
                  {s('hero.cta_secondary')}
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">{s('hero.no_card')}</p>
            </div>
          </div>
        </section>

        {/* Resultados */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 max-w-5xl mx-auto text-center">
              {results.map((r, i) => (
                <div key={i}>
                  <div className="text-4xl font-bold text-primary mb-2">{r.metric}</div>
                  <div className="text-sm text-muted-foreground">{r.label}</div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Herramientas */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{s('tools_section.title')}</h2>
              <p className="text-lg text-muted-foreground">{s('tools_section.subtitle')}</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
              {tools.map((tool, i) => (
                <Card key={i} className="border shadow-md hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <div className="w-14 h-14 bg-primary/10 rounded-xl flex items-center justify-center mb-4">
                      {TOOL_ICONS[i]}
                    </div>
                    <CardTitle className="text-xl">{tool.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground mb-4">{tool.description}</p>
                    <div className="flex flex-wrap gap-2">
                      {tool.keywords.map((kw, j) => (
                        <Badge key={j} variant="secondary" className="text-xs">{kw}</Badge>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Perfiles */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">{s('profiles_section.title')}</h2>
              <p className="text-lg text-muted-foreground max-w-2xl mx-auto">{s('profiles_section.subtitle')}</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-6xl mx-auto">
              {profiles.map((p, i) => (
                <Card key={i} className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                  <CardHeader>
                    <div className="w-14 h-14 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                      <ChefHat className="h-7 w-7 text-primary" />
                    </div>
                    <CardTitle className="text-lg">{p.title}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground text-sm">{p.description}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Por qué IA */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center max-w-6xl mx-auto">
              <div>
                <h2 className="text-3xl font-bold text-foreground mb-6">{s('why_section.title')}</h2>
                <p className="text-lg text-muted-foreground mb-6">{s('why_section.body')}</p>
                <ul className="space-y-4">
                  {benefits.map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span className="text-muted-foreground">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="bg-muted/30 rounded-2xl p-8">
                <div className="flex items-center gap-1 mb-4">
                  {[...Array(5)].map((_, i) => <Star key={i} className="h-5 w-5 fill-yellow-400 text-yellow-400" />)}
                </div>
                <p className="text-lg italic text-foreground mb-6">
                  "Reducimos nuestras mermas del 14% al 5% en menos de un mes. El ROI fue inmediato: pagamos la suscripción con lo que ahorramos la primera semana."
                </p>
                <div>
                  <p className="font-semibold">Laura García</p>
                  <p className="text-sm text-muted-foreground">Directora de Operaciones, Grupo Gastronómico BCN</p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Precios */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold text-foreground mb-4">{s('pricing_section.title')}</h2>
            <p className="text-lg text-muted-foreground mb-12 max-w-2xl mx-auto">{s('pricing_section.subtitle')}</p>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto mb-10">
              {plans.map((plan, i) => (
                <Card key={i} className={`text-center relative ${plan.highlight ? 'ring-2 ring-primary shadow-xl scale-105' : 'shadow-md'}`}>
                  {plan.highlight && <Badge className="absolute -top-3 left-1/2 -translate-x-1/2">⭐ Más Popular</Badge>}
                  <CardHeader className="pt-6">
                    <CardTitle className="text-lg">{plan.name}</CardTitle>
                    <div className="text-3xl font-bold text-primary">{plan.price}</div>
                    <div className="text-sm text-muted-foreground">{plan.uses}</div>
                  </CardHeader>
                  <CardContent>
                    <Button
                      className={`w-full ${plan.highlight ? 'btn-gold' : ''}`}
                      variant={plan.highlight ? 'default' : 'outline'}
                      onClick={() => window.open(`${APP_URL}/pricing`, '_blank')}
                    >
                      {plan.highlight ? s('hero.cta_primary') : s('hero.cta_secondary')}
                    </Button>
                  </CardContent>
                </Card>
              ))}
            </div>
            <p className="text-sm text-muted-foreground">{s('pricing_section.annual_note')}</p>
          </div>
        </section>

        {/* FAQ */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-12 text-center">{s('faq_section.title')}</h2>
              <div className="space-y-6">
                {faqs.map((item, i) => (
                  <div key={i} className="border-b pb-6">
                    <h3 className="text-lg font-semibold text-foreground mb-3">{item.question}</h3>
                    <p className="text-muted-foreground">{item.answer}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* CTA final */}
        <section className="py-20 bg-gradient-to-r from-primary to-primary/80">
          <div className="container mx-auto px-4 text-center text-primary-foreground">
            <h2 className="text-3xl font-bold mb-4">{s('cta_section.title')}</h2>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">{s('cta_section.subtitle')}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" variant="secondary" className="bg-white text-primary hover:bg-white/90" onClick={() => window.open(APP_URL, '_blank')}>
                {s('cta_section.primary')}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button size="lg" variant="outline" className="border-white text-white hover:bg-white/10" onClick={() => window.open(`${APP_URL}/pricing`, '_blank')}>
                {s('cta_section.secondary')}
              </Button>
            </div>
          </div>
        </section>
      </main>

      <ModernFooter />
      <WhatsAppFloatingButton />
    </div>
  );
}
