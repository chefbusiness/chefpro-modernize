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
import ImageDisclaimerNote from '@/components/ImageDisclaimerNote';
import { useLanguage } from '@/hooks/useLanguage';
import { ALL_USE_CASES, getUseCasesByType, type UseCase, type UseCaseType, type LangCode } from '@/data/use-cases';
import { getProductsByIds } from '@/data/products-catalog';
import { LinkifyText } from '@/lib/linkify-use-case';
import { ArrowRight, CheckCircle, Sparkles, MessageSquare, X, Check } from 'lucide-react';

const SITE_URL = 'https://aichef.pro';

// URL segments per language. Mirrors App.tsx route definitions and useLanguage.ts.
const SEGMENTS: Record<string, { hub: string; role: string; concept: string; task: string; locale: string; hubLabel: string }> = {
  es: { hub: 'usos',             role: 'rol',    concept: 'concepto', task: 'tarea',   locale: 'es-ES', hubLabel: 'Casos de uso' },
  en: { hub: 'use-cases',        role: 'role',   concept: 'concept',  task: 'task',    locale: 'en-US', hubLabel: 'Use Cases' },
  fr: { hub: 'cas-d-usage',      role: 'role',   concept: 'concept',  task: 'tache',   locale: 'fr-FR', hubLabel: 'Cas d’usage' },
  de: { hub: 'anwendungsfaelle', role: 'rolle',  concept: 'konzept',  task: 'aufgabe', locale: 'de-DE', hubLabel: 'Anwendungsfälle' },
  it: { hub: 'casi-uso',         role: 'ruolo',  concept: 'concetto', task: 'compito', locale: 'it-IT', hubLabel: 'Casi d’uso' },
  pt: { hub: 'casos-uso',        role: 'funcao', concept: 'conceito', task: 'tarefa',  locale: 'pt-PT', hubLabel: 'Casos de uso' },
  nl: { hub: 'use-cases',        role: 'rol',    concept: 'concept',  task: 'taak',    locale: 'nl-NL', hubLabel: 'Use cases' },
};

// UI strings (fields rendered in JSX, not the per-spoke content). ES + EN are first-class;
// other languages fall back to ES until full translation lands.
const UI: Record<string, {
  notFoundTitle: string;
  notFoundLink: string;
  ctaPrimary: string;
  ctaSeePlans: string;
  ctaFreeUses: string;
  onboardingBadge: string;
  defaultAppsTitle: string;
  appsSubtitle: string;
  seeAllAppsBtn: string;
  beforeAfterTitle: string;
  productsSubtitle: string;
  productCardCta: string;
  seeAllProductsBtn: string;
  siblingHeadingRole: string;
  siblingHeadingConcept: string;
  siblingHeadingTask: string;
  finalCtaSeeAllUseCases: string;
  galleryAltSuffix: string;
  serviceTypeRole: string;
  serviceTypeConcept: string;
  serviceTypeTask: string;
}> = {
  es: {
    notFoundTitle: 'Caso de uso no encontrado',
    notFoundLink: 'Ver todos los casos de uso',
    ctaPrimary: 'Empezar gratis',
    ctaSeePlans: 'Ver planes',
    ctaFreeUses: '5 usos gratis al mes · Sin tarjeta',
    onboardingBadge: 'Onboarding · ¿Quién Soy?',
    defaultAppsTitle: 'Apps especializadas que vas a usar',
    appsSubtitle: 'Agentes IA reales del catálogo de AI Chef Pro, organizados por categoría oficial de la plataforma.',
    seeAllAppsBtn: 'Ver todas las apps en la plataforma',
    beforeAfterTitle: 'El Antes y el Después',
    productsSubtitle: 'Plantillas, kits y guías diseñadas para este caso de uso. Listas para descargar y usar.',
    productCardCta: 'Ver detalle',
    seeAllProductsBtn: 'Ver todos los productos',
    siblingHeadingRole: 'También Útil Para',
    siblingHeadingConcept: 'Otros Conceptos Similares',
    siblingHeadingTask: 'Otras Tareas Relacionadas',
    finalCtaSeeAllUseCases: 'Ver todos los casos de uso',
    galleryAltSuffix: 'imagen %N de referencia generada con IA',
    serviceTypeRole: 'Software de IA para hostelería por rol profesional',
    serviceTypeConcept: 'Software de IA para hostelería por concepto de negocio',
    serviceTypeTask: 'Software de IA para hostelería por tarea operativa',
  },
  en: {
    notFoundTitle: 'Use case not found',
    notFoundLink: 'See all use cases',
    ctaPrimary: 'Start free',
    ctaSeePlans: 'See plans',
    ctaFreeUses: '5 free uses per month · No credit card',
    onboardingBadge: 'Onboarding · Who Am I?',
    defaultAppsTitle: 'Specialist apps you’ll be using',
    appsSubtitle: 'Real AI agents from the AI Chef Pro catalog, grouped by their official platform category.',
    seeAllAppsBtn: 'See all apps on the platform',
    beforeAfterTitle: 'Before & After',
    productsSubtitle: 'Templates, kits and guides built for this use case. Ready to download and use.',
    productCardCta: 'See details',
    seeAllProductsBtn: 'See all products',
    siblingHeadingRole: 'Also Useful For',
    siblingHeadingConcept: 'Similar Concepts',
    siblingHeadingTask: 'Related Tasks',
    finalCtaSeeAllUseCases: 'See all use cases',
    galleryAltSuffix: 'reference image %N generated with AI',
    serviceTypeRole: 'AI software for hospitality by professional role',
    serviceTypeConcept: 'AI software for hospitality by business concept',
    serviceTypeTask: 'AI software for hospitality by operational task',
  },
};

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
  const ui = UI[lang] || UI.es;
  const segs = SEGMENTS[lang] || SEGMENTS.es;
  const typeSegment = type === 'role' ? segs.role : type === 'concept' ? segs.concept : segs.task;
  const hubPath = `/${segs.hub}`;

  const useCase: UseCase | undefined = ALL_USE_CASES.find(
    uc => uc.type === type && Object.values(uc.slug).includes(slug || '')
  );

  if (!useCase) {
    const notFoundHubHref = lang === 'es' ? hubPath : `/${lang}${hubPath}`;
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-3xl font-bold mb-4">{ui.notFoundTitle}</h1>
          <Link to={notFoundHubHref} className="text-primary underline">{ui.notFoundLink}</Link>
        </div>
      </div>
    );
  }

  const content = useCase.content[lang] || useCase.content.es;
  const theme = COLOR_THEMES[useCase.colorTheme] || COLOR_THEMES.amber;
  const HeroIcon = getIconComponent(useCase.iconKey);
  const products = getProductsByIds(content.productIds, lang);

  const langPrefix = lang === 'es' ? '' : `/${lang}`;
  const canonicalSlug = useCase.slug[lang] || useCase.slug.es;
  const canonicalUrl = `${SITE_URL}${langPrefix}/${segs.hub}/${typeSegment}/${canonicalSlug}`;

  const siblingUseCases = getUseCasesByType(type)
    .filter(uc => uc.id !== useCase.id)
    .slice(0, 3);

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${canonicalUrl}#breadcrumb`,
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: segs.hubLabel, item: `${SITE_URL}${langPrefix}/${segs.hub}` },
      { '@type': 'ListItem', position: 3, name: content.h1 },
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

  const serviceSchema = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: content.h1,
    description: content.seo.description,
    provider: {
      '@type': 'Organization',
      name: 'AI Chef Pro',
      url: SITE_URL,
      logo: `${SITE_URL}/og-image.jpg`,
    },
    areaServed: lang === 'en' ? ['US', 'UK', 'CA', 'AU', 'EU'] : ['ES', 'EU', 'LATAM'],
    serviceType: type === 'role' ? ui.serviceTypeRole : type === 'concept' ? ui.serviceTypeConcept : ui.serviceTypeTask,
    audience: {
      '@type': 'Audience',
      audienceType: content.badge,
    },
    url: canonicalUrl,
    image: content.seo.ogImage,
    offers: {
      '@type': 'AggregateOffer',
      priceCurrency: 'EUR',
      lowPrice: '0',
      highPrice: '95',
      offerCount: '4',
      availability: 'https://schema.org/InStock',
    },
  };

  const webPageSchema = {
    '@context': 'https://schema.org',
    '@type': 'WebPage',
    name: content.seo.title,
    description: content.seo.description,
    url: canonicalUrl,
    inLanguage: segs.locale,
    isPartOf: {
      '@type': 'WebSite',
      name: 'AI Chef Pro',
      url: SITE_URL,
    },
    primaryImageOfPage: {
      '@type': 'ImageObject',
      url: content.galleryImages?.[0] ? `${SITE_URL}${content.galleryImages[0]}` : content.seo.ogImage,
    },
    breadcrumb: { '@id': `${canonicalUrl}#breadcrumb` },
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={content.seo.title}
        description={content.seo.description}
        keywords={content.seo.keywords}
        canonical={canonicalUrl}
        disableAutoHreflang
      />
      <Helmet>
        {(['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'] as LangCode[]).map(l => {
          const altSegs = SEGMENTS[l];
          const altSlug = useCase.slug[l];
          const altType = type === 'role' ? altSegs.role : type === 'concept' ? altSegs.concept : altSegs.task;
          const altPrefix = l === 'es' ? '' : `/${l}`;
          const href = `${SITE_URL}${altPrefix}/${altSegs.hub}/${altType}/${altSlug}`;
          return <link key={l} rel="alternate" hrefLang={l} href={href} />;
        })}
        <link rel="alternate" hrefLang="x-default" href={`${SITE_URL}/${SEGMENTS.es.hub}/${SEGMENTS.es[type]}/${useCase.slug.es}`} />
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(serviceSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(webPageSchema)}</script>
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
                <LinkifyText text={content.heroSubtitle} appUrl={APP_URL} />
              </p>
              <p className={`text-lg font-semibold ${theme.text} mb-10`}>
                {content.heroTagline}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  {ui.ctaPrimary} <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button size="lg" variant="outline" onClick={() => window.open(`${APP_URL}/pricing`, '_blank')}>
                  {ui.ctaSeePlans}
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">{ui.ctaFreeUses}</p>
            </div>
          </div>
        </section>

        {/* Gallery — opcional, mini galería de 6 imágenes de referencia */}
        {content.galleryImages && content.galleryImages.length > 0 && (
          <section className="py-20 bg-muted/30">
            <div className="container mx-auto px-4">
              <div className="text-center mb-10 max-w-3xl mx-auto">
                {content.galleryTitle && <h2 className="text-3xl font-bold text-foreground mb-3">{content.galleryTitle}</h2>}
                {content.gallerySubtitle && <p className="text-muted-foreground">{content.gallerySubtitle}</p>}
              </div>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 max-w-6xl mx-auto">
                {content.galleryImages.map((src, i) => (
                  <div key={i} className="relative aspect-[16/10] overflow-hidden rounded-xl shadow-md hover:shadow-xl transition-shadow group">
                    <img
                      src={src}
                      alt={`${content.h1} — ${ui.galleryAltSuffix.replace('%N', String(i + 1))}`}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                      loading={i < 3 ? 'eager' : 'lazy'}
                    />
                  </div>
                ))}
              </div>
            </div>
            <ImageDisclaimerNote variant="gallery" lang={lang} />
          </section>
        )}

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
                        <Badge className="mb-3 text-xs">{ui.onboardingBadge}</Badge>
                        <h2 className="text-2xl md:text-3xl font-bold text-foreground mb-4 text-balance">{content.personalizationTitle}</h2>
                        <p className="text-base md:text-lg text-muted-foreground leading-relaxed">
                          <LinkifyText text={content.personalizationBody!} appUrl={APP_URL} />
                        </p>
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
                      <CardTitle className="text-xl">
                        <LinkifyText text={feature.title} appUrl={APP_URL} />
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-muted-foreground">
                        <LinkifyText text={feature.description} appUrl={APP_URL} />
                      </p>
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
                <h2 className="text-3xl font-bold text-foreground mb-4">{content.appsTitle || ui.defaultAppsTitle}</h2>
                <p className="text-muted-foreground">{ui.appsSubtitle}</p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 max-w-6xl mx-auto">
                {content.apps.map((app, i) => (
                  <a
                    key={i}
                    href={APP_URL}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block group"
                  >
                    <Card className={`h-full border-l-4 ${theme.border} shadow-sm hover:shadow-lg hover:border-primary transition-all`} style={{ borderLeftColor: 'currentColor' }}>
                      <CardContent className="pt-5 pb-5">
                        <div className="flex items-start justify-between gap-3 mb-2">
                          <h3 className={`font-bold text-base leading-tight ${theme.text} group-hover:underline`}>{app.name}</h3>
                          <ArrowRight className={`h-4 w-4 ${theme.text} flex-shrink-0 mt-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-transform`} />
                        </div>
                        <Badge variant="secondary" className="text-xs mb-2">{app.category}</Badge>
                        <p className="text-sm text-muted-foreground leading-snug">
                          <LinkifyText text={app.description} appUrl={APP_URL} />
                        </p>
                      </CardContent>
                    </Card>
                  </a>
                ))}
              </div>
              <div className="text-center mt-10">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  {ui.seeAllAppsBtn} <ArrowRight className="ml-2 h-4 w-4" />
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
                    <p className="text-foreground pt-1">
                      <LinkifyText text={step} appUrl={APP_URL} />
                    </p>
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
                <h2 className="text-3xl font-bold text-foreground mb-4">{ui.beforeAfterTitle}</h2>
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
                          <span><LinkifyText text={item} appUrl={APP_URL} /></span>
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
                          <span><LinkifyText text={item} appUrl={APP_URL} /></span>
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
              <p className="text-muted-foreground">{ui.productsSubtitle}</p>
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
                        {ui.productCardCta} <ArrowRight className="ml-1 h-4 w-4" />
                      </div>
                    </CardContent>
                  </Card>
                </Link>
              ))}
            </div>
            <div className="text-center mt-12">
              <Button asChild variant="outline" size="lg">
                <Link to={lang === 'es' ? '/productos-digitales' : `/${lang}/productos-digitales`}>
                  {ui.seeAllProductsBtn} <ArrowRight className="ml-2 h-4 w-4" />
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
                    <p className="text-muted-foreground">
                      <LinkifyText text={faq.a} appUrl={APP_URL} />
                    </p>
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
                  {type === 'role' ? ui.siblingHeadingRole : type === 'concept' ? ui.siblingHeadingConcept : ui.siblingHeadingTask}
                </h2>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
                {siblingUseCases.map(sib => {
                  const sibContent = sib.content[lang] || sib.content.es;
                  const sibTheme = COLOR_THEMES[sib.colorTheme] || COLOR_THEMES.amber;
                  const sibSlug = sib.slug[lang] || sib.slug.es;
                  const SibIcon = getIconComponent(sib.iconKey);
                  return (
                    <Link key={sib.id} to={`${langPrefix}/${segs.hub}/${typeSegment}/${sibSlug}`}>
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
                {ui.ctaPrimary} <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to={`${langPrefix}/${segs.hub}`}><CheckCircle className="mr-2 h-4 w-4" /> {ui.finalCtaSeeAllUseCases}</Link>
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
