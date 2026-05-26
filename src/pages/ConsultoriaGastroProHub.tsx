import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
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
import { getUseCasesByType, type LangCode } from '@/data/use-cases';
import { ArrowRight, Briefcase, Building2, Sparkles, Users, TrendingUp } from 'lucide-react';

const SITE_URL = 'https://aichef.pro';

const SEGMENTS: Record<string, { hub: string; consultor: string; consultorHubSlug: string; locale: string; hubLabel: string }> = {
  es: { hub: 'usos',             consultor: 'consultoria', consultorHubSlug: 'consultoria-gastro-pro',  locale: 'es-ES', hubLabel: 'Casos de uso' },
  en: { hub: 'use-cases',        consultor: 'consultancy', consultorHubSlug: 'gastro-consultancy-pro',   locale: 'en-US', hubLabel: 'Use Cases' },
  fr: { hub: 'cas-d-usage',      consultor: 'conseil',     consultorHubSlug: 'conseil-gastro-pro',       locale: 'fr-FR', hubLabel: 'Cas d’usage' },
  de: { hub: 'anwendungsfaelle', consultor: 'beratung',    consultorHubSlug: 'gastro-beratung-pro',      locale: 'de-DE', hubLabel: 'Anwendungsfälle' },
  it: { hub: 'casi-uso',         consultor: 'consulenza',  consultorHubSlug: 'consulenza-gastro-pro',    locale: 'it-IT', hubLabel: 'Casi d’uso' },
  pt: { hub: 'casos-uso',        consultor: 'consultoria', consultorHubSlug: 'consultoria-gastro-pro',   locale: 'pt-PT', hubLabel: 'Casos de uso' },
  nl: { hub: 'use-cases',        consultor: 'advies',      consultorHubSlug: 'gastro-advies-pro',        locale: 'nl-NL', hubLabel: 'Use cases' },
};

const UI: Record<string, {
  badge: string;
  h1: string;
  heroSubtitle: string;
  ctaPrimary: string;
  ctaSecondary: string;
  ctaNote: string;
  metricsTitle: string;
  metric1: { value: string; label: string };
  metric2: { value: string; label: string };
  metric3: { value: string; label: string };
  metric4: { value: string; label: string };
  cardsTitle: string;
  cardsSubtitle: string;
  cardCta: string;
  forWhoTitle: string;
  forWho1Title: string;
  forWho1Body: string;
  forWho2Title: string;
  forWho2Body: string;
  forWho3Title: string;
  forWho3Body: string;
  finalH2: string;
  finalBody: string;
  finalCta: string;
  seoTitle: string;
  seoDescription: string;
  seoKeywords: string;
}> = {
  es: {
    badge: 'Consultoría Gastro Pro',
    h1: 'IA para Consultoría Gastronómica Profesional',
    heroSubtitle: 'Descubre cómo AI Chef Pro potencia el trabajo de consultores, asesores y especialistas independientes que trabajan por proyectos para restaurantes, hoteles, grupos de restauración e inversores del sector gastronómico.',
    ctaPrimary: 'Empezar gratis',
    ctaSecondary: 'Ver todos los agentes',
    ctaNote: '5 usos gratis al mes · Sin tarjeta',
    metricsTitle: 'Módulo Consultoría Gastro Pro en AI Chef Pro',
    metric1: { value: '10', label: 'Agentes especializados' },
    metric2: { value: '7', label: 'Idiomas disponibles' },
    metric3: { value: 'HORECA', label: 'Precios en tiempo real' },
    metric4: { value: 'PDF & CSV', label: 'Export profesional' },
    cardsTitle: 'Los 10 Agentes de Consultoría Gastronómica',
    cardsSubtitle: 'Cada perfil es un agente de IA especializado con la profundidad técnica de la disciplina y la visión de negocio que un proyecto de consultoría exige.',
    cardCta: 'Ver caso de uso',
    forWhoTitle: '¿Para Quién es Consultoría Gastro Pro?',
    forWho1Title: 'Consultores independientes',
    forWho1Body: 'Trabaja por proyectos con IA especializada en tu disciplina. Acelera entregables sin perder rigor técnico ni autoridad ante el cliente.',
    forWho2Title: 'Asesores de grupos de restauración',
    forWho2Body: 'Estandariza metodología, replica manuales y acelera procesos de auditoría, formación y onboarding en grupos multi-local.',
    forWho3Title: 'Especialistas sectoriales',
    forWho3Body: 'Profundidad técnica real para masas, fermentaciones, vinos, café, cacao, helados y todas las verticales de alta especialización.',
    finalH2: 'Tu Próximo Proyecto de Consultoría, Acelerado.',
    finalBody: 'Empieza gratis con el onboarding de 2 minutos. 5 usos al mes para probar todos los agentes de Consultoría Gastro Pro. Sin tarjeta.',
    finalCta: 'Probar gratis ahora',
    seoTitle: 'Consultoría Gastro Pro: 10 Agentes de IA para Consultores Gastronómicos | AI Chef Pro',
    seoDescription: 'Módulo de IA especializado para consultores gastronómicos, chefs consultores, sommeliers, bartenders, baristas, pasteleros, panaderos, pizzeros, heladeros y chocolateros que trabajan por proyectos. Empieza gratis.',
    seoKeywords: 'consultor gastronómico IA, chef consultor IA, asesor gastronómico inteligencia artificial, consultoría restaurantes IA, sommelier consultor, bartender consultor, barista consultor, pastelero consultor, panadero consultor, pizzero consultor, heladero consultor, chocolatero consultor, agente IA consultoría hostelería',
  },
  en: {
    badge: 'Gastro Consultancy Pro',
    h1: 'AI for Professional Gastronomic Consulting',
    heroSubtitle: 'See how AI Chef Pro powers the work of consultants, advisors, and independent specialists running project-based engagements for restaurants, hotels, restaurant groups, and food & beverage investors.',
    ctaPrimary: 'Start free',
    ctaSecondary: 'See all agents',
    ctaNote: '5 free uses per month · No credit card',
    metricsTitle: 'Gastro Consultancy Pro module inside AI Chef Pro',
    metric1: { value: '10', label: 'Specialized agents' },
    metric2: { value: '7', label: 'Languages available' },
    metric3: { value: 'HORECA', label: 'Live market pricing' },
    metric4: { value: 'PDF & CSV', label: 'Professional export' },
    cardsTitle: 'The 10 Gastronomic Consultancy Agents',
    cardsSubtitle: 'Every profile is a dedicated AI agent with the technical depth of the discipline and the business sense a consulting project demands.',
    cardCta: 'View use case',
    forWhoTitle: 'Who Is Gastro Consultancy Pro For?',
    forWho1Title: 'Independent consultants',
    forWho1Body: 'Work project by project with AI specialized in your discipline. Speed up deliverables without losing technical rigor or client authority.',
    forWho2Title: 'Restaurant group advisors',
    forWho2Body: 'Standardize methodology, replicate manuals, and accelerate audits, training, and onboarding across multi-location groups.',
    forWho3Title: 'Sector specialists',
    forWho3Body: 'Real technical depth for doughs, fermentations, wines, coffee, cacao, ice cream, and every high-specialization vertical.',
    finalH2: 'Accelerate Your Next Consulting Project.',
    finalBody: 'Start free with our 2-minute onboarding. 5 uses per month to try every Gastro Consultancy Pro agent. No credit card.',
    finalCta: 'Try it free now',
    seoTitle: 'Gastro Consultancy Pro: 10 AI Agents for Gastronomic Consultants | AI Chef Pro',
    seoDescription: 'Specialized AI module for gastronomic consultants, consultant chefs, sommeliers, bartenders, baristas, pastry chefs, bakers, pizza chefs, gelato makers, and chocolatiers running project work. Start free.',
    seoKeywords: 'gastronomic consultant AI, consultant chef AI, hospitality consultant artificial intelligence, restaurant consulting AI, sommelier consultant, bartender consultant, barista consultant, pastry consultant, baker consultant, pizza chef consultant, gelato consultant, chocolatier consultant, AI consultancy agent hospitality',
  },
};

const COLOR_THEMES: Record<string, { bg: string; text: string }> = {
  amber: { bg: 'bg-amber-500/10', text: 'text-amber-600' },
  blue: { bg: 'bg-blue-500/10', text: 'text-blue-600' },
  emerald: { bg: 'bg-emerald-500/10', text: 'text-emerald-600' },
  rose: { bg: 'bg-rose-500/10', text: 'text-rose-600' },
  purple: { bg: 'bg-purple-500/10', text: 'text-purple-600' },
  orange: { bg: 'bg-orange-500/10', text: 'text-orange-600' },
  indigo: { bg: 'bg-indigo-500/10', text: 'text-indigo-600' },
  pink: { bg: 'bg-pink-500/10', text: 'text-pink-600' },
  teal: { bg: 'bg-teal-500/10', text: 'text-teal-600' },
  red: { bg: 'bg-red-500/10', text: 'text-red-600' },
};

function getIconComponent(name: string) {
  const Comp = (LucideIcons as unknown as Record<string, LucideIcons.LucideIcon>)[name];
  return Comp || LucideIcons.Sparkles;
}

export default function ConsultoriaGastroProHub() {
  const { currentLanguage, getAppUrl } = useLanguage();
  const lang = currentLanguage as LangCode;
  const APP_URL = getAppUrl(currentLanguage);

  const ui = UI[lang] || UI.es;
  const segs = SEGMENTS[lang] || SEGMENTS.es;
  const langPrefix = lang === 'es' ? '' : `/${lang}`;
  const canonicalUrl = `${SITE_URL}${langPrefix}/${segs.hub}/${segs.consultorHubSlug}`;

  const consultores = getUseCasesByType('consultor');

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${canonicalUrl}#breadcrumb`,
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: segs.hubLabel, item: `${SITE_URL}${langPrefix}/${segs.hub}` },
      { '@type': 'ListItem', position: 3, name: ui.badge },
    ],
  };

  const collectionSchema = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: ui.seoTitle,
    description: ui.seoDescription,
    url: canonicalUrl,
    inLanguage: segs.locale,
    isPartOf: {
      '@type': 'WebSite',
      name: 'AI Chef Pro',
      url: SITE_URL,
    },
    hasPart: consultores.map(uc => {
      const content = uc.content[lang] || uc.content.es;
      const slug = uc.slug[lang] || uc.slug.es;
      return {
        '@type': 'Service',
        name: content.h1,
        url: `${SITE_URL}${langPrefix}/${segs.hub}/${segs.consultor}/${slug}`,
        description: content.heroTagline,
      };
    }),
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={ui.seoTitle}
        description={ui.seoDescription}
        keywords={ui.seoKeywords}
        canonical={canonicalUrl}
        ogImage="https://aichef.pro/og/use-cases/consultoria-gastro-pro-hub.jpg"
      />
      <Helmet>
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
        <script type="application/ld+json">{JSON.stringify(collectionSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-indigo-500/10 via-background to-purple-500/5 py-20 lg:py-28">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2">{ui.badge}</Badge>
              <div className="w-20 h-20 bg-indigo-500/10 rounded-2xl flex items-center justify-center mx-auto mb-6">
                <Briefcase className="h-10 w-10 text-indigo-600" />
              </div>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                {ui.h1}
              </h1>
              <p className="text-xl text-muted-foreground mb-10 max-w-3xl mx-auto text-balance">
                {ui.heroSubtitle}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  {ui.ctaPrimary} <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button asChild size="lg" variant="outline">
                  <a href="#agentes-consultoria"><Users className="mr-2 h-4 w-4" /> {ui.ctaSecondary}</a>
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">{ui.ctaNote}</p>
            </div>
          </div>
        </section>

        {/* Métricas */}
        <section className="py-16 bg-gradient-to-r from-primary/90 to-primary">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-8 max-w-5xl mx-auto text-center">
              {[ui.metric1, ui.metric2, ui.metric3, ui.metric4].map((m, i) => (
                <div key={i}>
                  <div className="text-4xl md:text-5xl font-bold text-white mb-2">{m.value}</div>
                  <div className="text-sm text-primary-foreground/80">{m.label}</div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Cards 10 perfiles */}
        <section id="agentes-consultoria" className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.cardsTitle}</h2>
              <p className="text-muted-foreground">{ui.cardsSubtitle}</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
              {consultores.map(uc => {
                const content = uc.content[lang] || uc.content.es;
                const theme = COLOR_THEMES[uc.colorTheme] || COLOR_THEMES.amber;
                const slug = uc.slug[lang] || uc.slug.es;
                const Icon = getIconComponent(uc.iconKey);
                return (
                  <Link key={uc.id} to={`${langPrefix}/${segs.hub}/${segs.consultor}/${slug}`}>
                    <Card className="h-full border-2 hover:border-primary transition-all hover:shadow-xl">
                      <CardHeader>
                        <div className={`w-14 h-14 ${theme.bg} rounded-xl flex items-center justify-center mb-3`}>
                          <Icon className={`h-7 w-7 ${theme.text}`} />
                        </div>
                        <CardTitle className="text-xl">{content.h1}</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-sm text-muted-foreground mb-4">{content.heroTagline}</p>
                        <div className="flex items-center text-primary text-sm font-semibold">
                          {ui.cardCta} <ArrowRight className="ml-1 h-4 w-4" />
                        </div>
                      </CardContent>
                    </Card>
                  </Link>
                );
              })}
            </div>
          </div>
        </section>

        {/* ¿Para quién? */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-3xl mx-auto">
              <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.forWhoTitle}</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
              <Card className="border-2 border-indigo-200 shadow-md">
                <CardHeader>
                  <div className="w-14 h-14 bg-indigo-500/10 rounded-xl flex items-center justify-center mb-3">
                    <Users className="h-7 w-7 text-indigo-600" />
                  </div>
                  <CardTitle className="text-xl">{ui.forWho1Title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{ui.forWho1Body}</p>
                </CardContent>
              </Card>
              <Card className="border-2 border-purple-200 shadow-md">
                <CardHeader>
                  <div className="w-14 h-14 bg-purple-500/10 rounded-xl flex items-center justify-center mb-3">
                    <Building2 className="h-7 w-7 text-purple-600" />
                  </div>
                  <CardTitle className="text-xl">{ui.forWho2Title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{ui.forWho2Body}</p>
                </CardContent>
              </Card>
              <Card className="border-2 border-amber-200 shadow-md">
                <CardHeader>
                  <div className="w-14 h-14 bg-amber-500/10 rounded-xl flex items-center justify-center mb-3">
                    <TrendingUp className="h-7 w-7 text-amber-600" />
                  </div>
                  <CardTitle className="text-xl">{ui.forWho3Title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{ui.forWho3Body}</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* CTA final */}
        <section className="py-20 bg-gradient-to-br from-indigo-500/10 via-background to-purple-500/5">
          <div className="container mx-auto px-4 text-center">
            <Sparkles className="h-10 w-10 text-indigo-600 mx-auto mb-4" />
            <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">{ui.finalH2}</h2>
            <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">{ui.finalBody}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                {ui.finalCta} <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to={`${langPrefix}/${segs.hub}`}>{segs.hubLabel} <ArrowRight className="ml-2 h-4 w-4" /></Link>
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
