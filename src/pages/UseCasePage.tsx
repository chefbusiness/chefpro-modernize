import { Helmet } from 'react-helmet-async';
import { useParams, Link } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import * as LucideIcons from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import HeroSocialProof from '@/components/HeroSocialProof';
import { useLanguage } from '@/hooks/useLanguage';
import { ALL_USE_CASES, getUseCasesByType, type UseCase, type UseCaseType, type LangCode } from '@/data/use-cases';
import { getProductsByIds } from '@/data/products-catalog';
import { ArrowRight, CheckCircle, Sparkles, MessageSquare, X, Check } from 'lucide-react';

const SITE_URL = 'https://aichef.pro';

const COLOR_THEMES: Record<string, { bg: string; text: string; border: string; gradient: string }> = {
  amber: { bg: 'bg-amber-500/10', text: 'text-amber-600', border: 'border-amber-200', gradient: 'from-amber-500/10 via-background to-amber-500/5' },
  blue: { bg: 'bg-blue-500/10', text: 'text-blue-600', border: 'border-blue-200', gradient: 'from-blue-500/10 via-background to-blue-500/5' },
  emerald: { bg: 'bg-emerald-500/10', text: 'text-emerald-600', border: 'border-emerald-200', gradient: 'from-emerald-500/10 via-background to-emerald-500/5' },
  rose: { bg: 'bg-rose-500/10', text: 'text-rose-600', border: 'border-rose-200', gradient: 'from-rose-500/10 via-background to-rose-500/5' },
  purple: { bg: 'bg-purple-500/10', text: 'text-purple-600', border: 'border-purple-200', gradient: 'from-purple-500/10 via-background to-purple-500/5' },
  orange: { bg: 'bg-orange-500/10', text: 'text-orange-600', border: 'border-orange-200', gradient: 'from-orange-500/10 via-background to-orange-500/5' },
  indigo: { bg: 'bg-indigo-500/10', text: 'text-indigo-600', border: 'border-indigo-200', gradient: 'from-indigo-500/10 via-background to-indigo-500/5' },
  pink: { bg: 'bg-pink-500/10', text: 'text-pink-600', border: 'border-pink-200', gradient: 'from-pink-500/10 via-background to-pink-500/5' },
  teal: { bg: 'bg-teal-500/10', text: 'text-teal-600', border: 'border-teal-200', gradient: 'from-teal-500/10 via-background to-teal-500/5' },
  red: { bg: 'bg-red-500/10', text: 'text-red-600', border: 'border-red-200', gradient: 'from-red-500/10 via-background to-red-500/5' },
};

interface UseCasePageProps {
  type: UseCaseType;
}

function getIconComponent(name: string) {
  const Comp = (LucideIcons as unknown as Record<string, LucideIcons.LucideIcon>)[name];
  return Comp || LucideIcons.Sparkles;
}

export default function UseCasePage({ type }: UseCasePageProps) {
  const { slug } = useParams<{ slug: string }>();
  const { currentLanguage, getAppUrl } = useLanguage();
  const lang = currentLanguage as LangCode;
  const APP_URL = getAppUrl(currentLanguage);

  const useCase: UseCase | undefined = ALL_USE_CASES.find(
    uc => uc.type === type && Object.values(uc.slug).includes(slug || '')
  );

  if (!useCase) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-4">Caso de uso no encontrado</h1>
          <Link to="/usos" className="text-primary underline">Ver todos los casos de uso</Link>
        </div>
      </div>
    );
  }

  const content = useCase.content[lang] || useCase.content.es;
  const theme = COLOR_THEMES[useCase.colorTheme] || COLOR_THEMES.amber;
  const HeroIcon = getIconComponent(useCase.iconKey);
  const products = getProductsByIds(content.productIds);

  const langPrefix = lang === 'es' ? '' : `/${lang}`;
  const typeSegment = type === 'role' ? 'rol' : 'concepto';
  const canonicalSlug = useCase.slug[lang] || useCase.slug.es;
  const canonicalUrl = `${SITE_URL}${langPrefix}/usos/${typeSegment}/${canonicalSlug}`;

  const siblingUseCases = getUseCasesByType(type)
    .filter(uc => uc.id !== useCase.id)
    .slice(0, 3);

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'Casos de uso', item: `${SITE_URL}${langPrefix}/usos` },
      { '@type': 'ListItem', position: 3, name: content.h1, item: canonicalUrl },
    ],
  };

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: content.faqs.map(f => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: f.a },
    })),
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={content.seo.title}
        description={content.seo.description}
        keywords={content.seo.keywords}
        canonical={canonicalUrl}
      />
      <Helmet>
        {(['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as LangCode[]).map(l => {
          const altSlug = useCase.slug[l];
          const altPrefix = l === 'es' ? '' : `/${l}`;
          const href = `${SITE_URL}${altPrefix}/usos/${typeSegment}/${altSlug}`;
          return <link key={l} rel="alternate" hrefLang={l} href={href} />;
        })}
        <link rel="alternate" hrefLang="x-default" href={`${SITE_URL}/usos/${typeSegment}/${useCase.slug.es}`} />
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className={`relative overflow-hidden bg-gradient-to-br ${theme.gradient} py-20 lg:py-32`}>
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2">{content.badge}</Badge>
              <div className={`w-20 h-20 ${theme.bg} rounded-2xl flex items-center justify-center mx-auto mb-6`}>
                <HeroIcon className={`h-10 w-10 ${theme.text}`} />
              </div>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                {content.h1}
              </h1>
              <p className="text-xl text-muted-foreground mb-4 max-w-3xl mx-auto text-balance">
                {content.heroSubtitle}
              </p>
              <p className={`text-lg font-semibold ${theme.text} mb-10`}>
                {content.heroTagline}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  Empezar gratis <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button size="lg" variant="outline" onClick={() => window.open(`${APP_URL}/pricing`, '_blank')}>
                  Ver planes
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">5 usos gratis al mes · Sin tarjeta</p>
            </div>
          </div>
        </section>

        {/* Personalization (¿Quién Soy?) — opcional */}
        {content.personalizationTitle && content.personalizationBody && (
          <section className={`py-16 bg-gradient-to-br ${theme.gradient} border-b`}>
            <div className="container mx-auto px-4">
              <div className="max-w-4xl mx-auto">
                <Card className={`border-2 ${theme.border} shadow-xl`}>
                  <CardContent className="pt-10 pb-10 px-8 md:px-12">
                    <div className="flex items-start gap-6">
                      <div className={`hidden md:flex w-16 h-16 ${theme.bg} rounded-2xl items-center justify-center flex-shrink-0`}>
                        <MessageSquare className={`h-8 w-8 ${theme.text}`} />
                      </div>
                      <div>
                        <Badge className="mb-3 text-xs">Onboarding · ¿Quién Soy?</Badge>
                        <h2 className="text-2xl md:text-3xl font-bold text-foreground mb-4 text-balance">{content.personalizationTitle}</h2>
                        <p className="text-base md:text-lg text-muted-foreground leading-relaxed">{content.personalizationBody}</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>
          </section>
        )}

        {/* Métricas — opcional */}
        {content.metrics && content.metrics.length > 0 && (
          <section className="py-16 bg-gradient-to-r from-primary/90 to-primary">
            <div className="container mx-auto px-4">
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 max-w-5xl mx-auto text-center">
                {content.metrics.map((m, i) => (
                  <div key={i}>
                    <div className="text-4xl md:text-5xl font-bold text-white mb-2">{m.value}</div>
                    <div className="text-sm text-primary-foreground/80">{m.label}</div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {/* Pains */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{content.painsTitle}</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
              {content.pains.map((pain, i) => (
                <Card key={i} className={`border-2 ${theme.border} shadow-md`}>
                  <CardContent className="pt-6 flex items-start gap-3">
                    <div className={`w-8 h-8 ${theme.bg} rounded-lg flex items-center justify-center flex-shrink-0`}>
                      <span className={`font-bold ${theme.text}`}>{i + 1}</span>
                    </div>
                    <p className="text-foreground">{pain}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Features */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{content.featuresTitle}</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
              {content.features.map((feature, i) => {
                const Icon = getIconComponent(feature.icon);
                return (
                  <Card key={i} className="border-none shadow-lg hover:shadow-xl transition-shadow">
                    <CardHeader>
                      <div className={`w-14 h-14 ${theme.bg} rounded-xl flex items-center justify-center mb-4`}>
                        <Icon className={`h-7 w-7 ${theme.text}`} />
                      </div>
                      <CardTitle className="text-xl">{feature.title}</CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-muted-foreground">{feature.description}</p>
                    </CardContent>
                  </Card>
                );
              })}
            </div>
          </div>
        </section>

        {/* Apps destacadas — opcional */}
        {content.apps && content.apps.length > 0 && (
          <section className="py-20">
            <div className="container mx-auto px-4">
              <div className="text-center mb-12 max-w-3xl mx-auto">
                <h2 className="text-3xl font-bold text-foreground mb-4">{content.appsTitle || 'Apps especializadas que vas a usar'}</h2>
                <p className="text-muted-foreground">Agentes IA reales del catálogo de AI Chef Pro, organizados por categoría oficial de la plataforma.</p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-w-6xl mx-auto">
                {content.apps.map((app, i) => (
                  <Card key={i} className={`border-l-4 ${theme.border} shadow-sm hover:shadow-md transition-shadow`} style={{ borderLeftColor: 'currentColor' }}>
                    <CardContent className="pt-5 pb-5">
                      <div className="flex items-start justify-between gap-3 mb-2">
                        <h3 className="font-bold text-foreground text-base leading-tight">{app.name}</h3>
                      </div>
                      <Badge variant="secondary" className="text-xs mb-2">{app.category}</Badge>
                      <p className="text-sm text-muted-foreground leading-snug">{app.description}</p>
                    </CardContent>
                  </Card>
                ))}
              </div>
              <div className="text-center mt-10">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  Ver todas las apps en la plataforma <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              </div>
            </div>
          </section>
        )}

        {/* Workflow */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{content.workflowTitle}</h2>
            </div>
            <div className="max-w-3xl mx-auto space-y-4">
              {content.workflow.map((step, i) => (
                <Card key={i} className="border-l-4 shadow-sm" style={{ borderLeftColor: 'currentColor' }}>
                  <CardContent className="pt-6 flex items-start gap-4">
                    <div className={`w-10 h-10 rounded-full ${theme.bg} flex items-center justify-center font-bold ${theme.text} flex-shrink-0`}>
                      {i + 1}
                    </div>
                    <p className="text-foreground pt-1">{step}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Antes vs Después — opcional */}
        {content.beforeAfter && (
          <section className="py-20 bg-muted/30">
            <div className="container mx-auto px-4">
              <div className="text-center mb-12 max-w-3xl mx-auto">
                <h2 className="text-3xl font-bold text-foreground mb-4">El antes y el después</h2>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto">
                <Card className="border-2 border-red-200 shadow-md">
                  <CardHeader>
                    <CardTitle className="text-xl flex items-center gap-2 text-red-700">
                      <X className="h-5 w-5" /> {content.beforeAfter.beforeTitle}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <ul className="space-y-3">
                      {content.beforeAfter.beforeItems.map((item, i) => (
                        <li key={i} className="flex items-start gap-2 text-sm text-muted-foreground">
                          <X className="h-4 w-4 text-red-500 flex-shrink-0 mt-0.5" />
                          <span>{item}</span>
                        </li>
                      ))}
                    </ul>
                  </CardContent>
                </Card>
                <Card className="border-2 border-emerald-200 shadow-md">
                  <CardHeader>
                    <CardTitle className="text-xl flex items-center gap-2 text-emerald-700">
                      <Check className="h-5 w-5" /> {content.beforeAfter.afterTitle}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <ul className="space-y-3">
                      {content.beforeAfter.afterItems.map((item, i) => (
                        <li key={i} className="flex items-start gap-2 text-sm text-foreground">
                          <Check className="h-4 w-4 text-emerald-600 flex-shrink-0 mt-0.5" />
                          <span>{item}</span>
                        </li>
                      ))}
                    </ul>
                  </CardContent>
                </Card>
              </div>
            </div>
          </section>
        )}

        {/* Productos recomendados */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{content.productsTitle}</h2>
              <p className="text-muted-foreground">Plantillas, kits y guías diseñadas para este caso de uso. Listas para descargar y usar.</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
              {products.map(p => (
                <Link key={p.id} to={p.url} className="block">
                  <Card className="h-full border-2 hover:border-primary transition-colors shadow-md hover:shadow-lg">
                    <CardHeader>
                      <div className="flex justify-between items-start mb-2">
                        <CardTitle className="text-lg">{p.name}</CardTitle>
                        <Badge variant="secondary" className="ml-2">{p.price}</Badge>
                      </div>
                    </CardHeader>
                    <CardContent>
                      <p className="text-muted-foreground text-sm mb-4">{p.description}</p>
                      <div className="flex items-center text-primary text-sm font-semibold">
                        Ver detalle <ArrowRight className="ml-1 h-4 w-4" />
                      </div>
                    </CardContent>
                  </Card>
                </Link>
              ))}
            </div>
            <div className="text-center mt-12">
              <Button asChild variant="outline" size="lg">
                <Link to="/productos-digitales">
                  Ver todos los productos <ArrowRight className="ml-2 h-4 w-4" />
                </Link>
              </Button>
            </div>
          </div>
        </section>

        {/* Testimonio */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <Card className={`max-w-3xl mx-auto border-2 ${theme.border} shadow-xl`}>
              <CardContent className="pt-10 pb-10 text-center">
                <Sparkles className={`h-10 w-10 ${theme.text} mx-auto mb-4`} />
                <p className="text-xl text-foreground italic mb-6 text-balance">"{content.testimonialQuote}"</p>
                <div>
                  <p className="font-bold text-foreground">{content.testimonialAuthor}</p>
                  <p className="text-sm text-muted-foreground">{content.testimonialRole}</p>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* FAQ */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{content.faqTitle}</h2>
            </div>
            <div className="max-w-3xl mx-auto space-y-4">
              {content.faqs.map((faq, i) => (
                <Card key={i} className="shadow-sm">
                  <CardContent className="pt-6">
                    <h3 className="font-bold text-lg text-foreground mb-2">{faq.q}</h3>
                    <p className="text-muted-foreground">{faq.a}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Spokes hermanos */}
        {siblingUseCases.length > 0 && (
          <section className="py-20">
            <div className="container mx-auto px-4">
              <div className="text-center mb-12">
                <h2 className="text-2xl font-bold text-foreground mb-2">
                  {type === 'role' ? 'También útil para' : 'Otros conceptos similares'}
                </h2>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
                {siblingUseCases.map(sib => {
                  const sibContent = sib.content[lang] || sib.content.es;
                  const sibTheme = COLOR_THEMES[sib.colorTheme] || COLOR_THEMES.amber;
                  const sibSlug = sib.slug[lang] || sib.slug.es;
                  const SibIcon = getIconComponent(sib.iconKey);
                  return (
                    <Link key={sib.id} to={`${langPrefix}/usos/${typeSegment}/${sibSlug}`}>
                      <Card className="h-full hover:shadow-lg transition-shadow">
                        <CardHeader>
                          <div className={`w-12 h-12 ${sibTheme.bg} rounded-xl flex items-center justify-center mb-3`}>
                            <SibIcon className={`h-6 w-6 ${sibTheme.text}`} />
                          </div>
                          <CardTitle className="text-lg">{sibContent.h1}</CardTitle>
                        </CardHeader>
                        <CardContent>
                          <p className="text-sm text-muted-foreground">{sibContent.heroTagline}</p>
                        </CardContent>
                      </Card>
                    </Link>
                  );
                })}
              </div>
            </div>
          </section>
        )}

        {/* CTA final */}
        <section className={`py-20 bg-gradient-to-br ${theme.gradient}`}>
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{content.ctaTitle}</h2>
            <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">{content.ctaSubtitle}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                Empezar gratis <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to="/usos"><CheckCircle className="mr-2 h-4 w-4" /> Ver todos los casos de uso</Link>
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
