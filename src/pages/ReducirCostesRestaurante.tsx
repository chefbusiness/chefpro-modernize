import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { CheckCircle, ArrowRight, ChefHat, TrendingDown, ShoppingCart, Users, BarChart3, PieChart } from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import HeroSocialProof from '@/components/HeroSocialProof';
import { useLanguage } from '@/hooks/useLanguage';
import { useLiveUserCount } from '@/hooks/useLiveUserCount';

const TOOL_CARDS = [
  { icon: <TrendingDown className="h-7 w-7 text-red-600" />, bg: 'bg-red-50', border: 'border-red-200' },
  { icon: <PieChart className="h-7 w-7 text-blue-600" />, bg: 'bg-blue-50', border: 'border-blue-200' },
  { icon: <BarChart3 className="h-7 w-7 text-emerald-600" />, bg: 'bg-emerald-50', border: 'border-emerald-200' },
  { icon: <ShoppingCart className="h-7 w-7 text-orange-600" />, bg: 'bg-orange-50', border: 'border-orange-200' },
  { icon: <ChefHat className="h-7 w-7 text-purple-600" />, bg: 'bg-purple-50', border: 'border-purple-200' },
  { icon: <Users className="h-7 w-7 text-amber-600" />, bg: 'bg-amber-50', border: 'border-amber-200' },
];

const PROFILE_COLORS = [
  { bg: 'bg-red-100', icon: 'text-red-700' },
  { bg: 'bg-blue-100', icon: 'text-blue-700' },
  { bg: 'bg-emerald-100', icon: 'text-emerald-700' },
  { bg: 'bg-purple-100', icon: 'text-purple-700' },
];

// URL slug per language
const LANG_SLUGS: Record<string, string> = {
  es: 'reducir-costes-restaurante-ia',
  en: 'reduce-restaurant-costs-ai',
  fr: 'reduire-couts-restaurant-ia',
  de: 'restaurantkosten-senken-ki',
  it: 'ridurre-costi-ristorante-ia',
  pt: 'reduzir-custos-restaurante-ia',
  nl: 'restaurantkosten-verlagen-ai',
};

const SITE_URL = 'https://aichef.pro';

export default function ReducirCostesRestaurante() {
  const { t } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const APP_URL = getAppUrl(currentLanguage);

  const { formatted: userCount } = useLiveUserCount(currentLanguage);

  const k = (key: string) => t(`landingCostes.${key}`, { returnObjects: true, userCount });
  const s = (key: string) => t(`landingCostes.${key}`, { userCount }) as string;

  const results = k('results') as Array<{ metric: string; label: string }>;
  const tools = k('tools') as Array<{ title: string; description: string; keywords: string[] }>;
  const profiles = k('profiles') as Array<{ title: string; description: string }>;
  const benefits = k('why_section.benefits') as string[];
  const faqs = k('faq') as Array<{ question: string; answer: string }>;

  const canonicalSlug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = currentLanguage === 'es'
    ? `${SITE_URL}/${canonicalSlug}`
    : `${SITE_URL}/${currentLanguage}/${canonicalSlug}`;

  const plans = [
    { name: 'AI Chef Miembro', price: 'Gratis', uses: '5 usos/mes', highlight: false },
    { name: 'AI Chef Premium Pro', price: '25€/mes', uses: '150 usos/mes', highlight: false },
    { name: 'AI Chef Premium Plus', price: '50€/mes', uses: '350 usos/mes', highlight: true },
    { name: 'AI Chef Premium Max', price: '95€/mes', uses: 'Ilimitado', highlight: false },
  ];

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: s('breadcrumb'), item: canonicalUrl },
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

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={s('seo.title')}
        description={s('seo.description')}
        keywords={s('seo.keywords')}
        canonical={canonicalUrl}
      />
      <Helmet>
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
        <section className="relative overflow-hidden bg-gradient-to-br from-red-50 via-background to-orange-50/30 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
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
        <section className="py-16 bg-gradient-to-r from-red-600/90 to-red-500">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 max-w-5xl mx-auto text-center">
              {results.map((r, i) => (
                <div key={i}>
                  <div className="text-4xl font-bold text-white mb-2">{r.metric}</div>
                  <div className="text-sm text-red-100">{r.label}</div>
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
                <Card key={i} className={`border-2 ${TOOL_CARDS[i]?.border ?? 'border-border'} shadow-md hover:shadow-lg transition-shadow`}>
                  <CardHeader>
                    <div className={`w-14 h-14 ${TOOL_CARDS[i]?.bg ?? 'bg-primary/10'} rounded-xl flex items-center justify-center mb-4`}>
                      {TOOL_CARDS[i]?.icon}
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
                    <div className={`w-14 h-14 ${PROFILE_COLORS[i]?.bg ?? 'bg-primary/10'} rounded-full flex items-center justify-center mx-auto mb-4`}>
                      <ChefHat className={`h-7 w-7 ${PROFILE_COLORS[i]?.icon ?? 'text-primary'}`} />
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

        {/* Por qué */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center max-w-6xl mx-auto">
              <div>
                <h2 className="text-3xl font-bold text-foreground mb-6">{s('why_section.title')}</h2>
                <p className="text-lg text-muted-foreground mb-6">{s('why_section.body')}</p>
                <ul className="space-y-4">
                  {benefits.map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-emerald-500 mt-0.5 flex-shrink-0" />
                      <span className="text-muted-foreground">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl p-8 border border-red-100">
                <div className="flex items-center gap-1 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <svg key={i} className={`h-5 w-5 ${i < 4 ? 'text-yellow-400 fill-yellow-400' : 'text-yellow-300 fill-yellow-300'}`} viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                  ))}
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
        <section className="py-20 bg-gradient-to-b from-muted/20 to-muted/50">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold text-foreground mb-4">{s('pricing_section.title')}</h2>
            <p className="text-lg text-muted-foreground mb-12 max-w-2xl mx-auto">{s('pricing_section.subtitle')}</p>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto mb-10">
              {plans.map((plan, i) => (
                <Card key={i} className={`text-center relative ${plan.highlight ? 'ring-2 ring-amber-400 shadow-2xl scale-105 bg-gradient-to-b from-amber-50 to-white' : 'shadow-md bg-card'}`}>
                  {plan.highlight && <Badge className="absolute -top-3 left-1/2 -translate-x-1/2 bg-amber-400 text-amber-950 border-0">⭐ Más Popular</Badge>}
                  <CardHeader className="pt-6">
                    <CardTitle className={`text-lg ${plan.highlight ? 'text-amber-900' : ''}`}>{plan.name}</CardTitle>
                    <div className={`text-3xl font-bold ${plan.highlight ? 'text-amber-600' : 'text-primary'}`}>{plan.price}</div>
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
        <section className="py-20 bg-gradient-to-br from-amber-500 via-amber-400 to-yellow-300">
          <div className="container mx-auto px-4 text-center text-amber-950">
            <h2 className="text-3xl font-bold mb-4">{s('cta_section.title')}</h2>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">{s('cta_section.subtitle')}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="bg-amber-950 text-amber-50 hover:bg-amber-900" onClick={() => window.open(APP_URL, '_blank')}>
                {s('cta_section.primary')}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button size="lg" variant="outline" className="border-amber-900 text-amber-900 bg-white/30 hover:bg-white/50" onClick={() => window.open(`${APP_URL}/pricing`, '_blank')}>
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
