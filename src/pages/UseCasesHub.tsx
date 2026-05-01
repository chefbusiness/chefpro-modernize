import { useState } from 'react';
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
import { getUseCasesByType, hasNativeContent, type LangCode } from '@/data/use-cases';
import { ArrowRight, Briefcase, Building2, Sparkles } from 'lucide-react';

const SITE_URL = 'https://aichef.pro';

const SEGMENTS: Record<string, { hub: string; role: string; concept: string; task: string; locale: string; hubLabel: string }> = {
  es: { hub: 'usos',             role: 'rol',    concept: 'concepto', task: 'tarea',   locale: 'es-ES', hubLabel: 'Casos de uso' },
  en: { hub: 'use-cases',        role: 'role',   concept: 'concept',  task: 'task',    locale: 'en-US', hubLabel: 'Use Cases' },
  fr: { hub: 'cas-d-usage',      role: 'role',   concept: 'concept',  task: 'tache',   locale: 'fr-FR', hubLabel: 'Cas d’usage' },
  de: { hub: 'anwendungsfaelle', role: 'rolle',  concept: 'konzept',  task: 'aufgabe', locale: 'de-DE', hubLabel: 'Anwendungsfälle' },
  it: { hub: 'casi-uso',         role: 'ruolo',  concept: 'concetto', task: 'compito', locale: 'it-IT', hubLabel: 'Casi d’uso' },
  pt: { hub: 'casos-uso',        role: 'funcao', concept: 'conceito', task: 'tarefa',  locale: 'pt-PT', hubLabel: 'Casos de uso' },
  nl: { hub: 'use-cases',        role: 'rol',    concept: 'concept',  task: 'taak',    locale: 'nl-NL', hubLabel: 'Use cases' },
};

const UI: Record<string, {
  badge: string;
  h1: string;
  heroSubtitle: string;
  ctaPrimary: string;
  ctaSecondary: string;
  ctaNote: string;
  tabRole: string;
  tabConcept: string;
  tabRoleDesc: string;
  tabConceptDesc: string;
  cardCta: string;
  finalH2: string;
  finalBody: string;
  finalSecondary: string;
  h1StripPrefix: RegExp;
  seoTitle: string;
  seoDescription: string;
  seoKeywords: string;
}> = {
  es: {
    badge: 'Casos de uso',
    h1: 'IA para Cada Rol y Cada Concepto de Hostelería',
    heroSubtitle: 'Descubre cómo AI Chef Pro se adapta a tu perfil profesional y a tu concepto de negocio. Plantillas, agentes y guías diseñadas para tu día a día.',
    ctaPrimary: 'Empezar gratis',
    ctaSecondary: 'Ver productos',
    ctaNote: '5 usos gratis al mes · Sin tarjeta',
    tabRole: 'Por Rol Profesional',
    tabConcept: 'Por Concepto de Negocio',
    tabRoleDesc: 'Descubre cómo usar AI Chef Pro según tu rol profesional en el equipo o en el negocio.',
    tabConceptDesc: 'Descubre cómo encaja AI Chef Pro en tu tipo concreto de negocio gastronómico.',
    cardCta: 'Ver caso de uso',
    finalH2: '¿No Ves Tu Caso? AI Chef Pro Se Adapta',
    finalBody: 'Empieza gratis y descubre cómo encaja en tu día a día. Sin tarjeta, 5 usos al mes para probar todas las herramientas.',
    finalSecondary: 'Ver productos digitales',
    h1StripPrefix: /^IA para /,
    seoTitle: 'Casos de uso de AI Chef Pro: por rol profesional y concepto de negocio',
    seoDescription: 'Descubre cómo usar AI Chef Pro según tu perfil profesional o tu concepto de hostelería: chef ejecutivo, propietario, gerente, pizzería, dark kitchen, catering, hotel, heladería y más.',
    seoKeywords: 'casos de uso AI Chef Pro, IA hostelería por perfil, IA restaurante por concepto, software hostelería profesional',
  },
  en: {
    badge: 'Use Cases',
    h1: 'AI for Every Role and Every Hospitality Concept',
    heroSubtitle: 'Discover how AI Chef Pro adapts to your professional profile and to your business concept. Templates, agents, and guides built for your day-to-day.',
    ctaPrimary: 'Start free',
    ctaSecondary: 'See products',
    ctaNote: '5 free uses per month · No credit card',
    tabRole: 'By Professional Role',
    tabConcept: 'By Business Concept',
    tabRoleDesc: 'See how AI Chef Pro fits your professional role on the team or in the business.',
    tabConceptDesc: 'See how AI Chef Pro fits your specific type of hospitality business.',
    cardCta: 'View use case',
    finalH2: 'Don\'t See Your Case? AI Chef Pro Adapts',
    finalBody: 'Start free and discover how it fits your day-to-day. No credit card. 5 uses per month to try every tool.',
    finalSecondary: 'See digital products',
    h1StripPrefix: /^AI for /,
    seoTitle: 'AI Chef Pro Use Cases: by professional role and business concept',
    seoDescription: 'See how to use AI Chef Pro by professional profile or hospitality concept: executive chef, owner, manager, pizzeria, dark kitchen, catering, hotel, ice cream shop, and more.',
    seoKeywords: 'AI Chef Pro use cases, hospitality AI by profile, restaurant AI by concept, professional hospitality software',
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

export default function UseCasesHub() {
  const [activeTab, setActiveTab] = useState<'role' | 'concept'>('role');
  const { currentLanguage, getAppUrl } = useLanguage();
  const lang = currentLanguage as LangCode;
  const APP_URL = getAppUrl(currentLanguage);

  const ui = UI[lang] || UI.es;
  const segs = SEGMENTS[lang] || SEGMENTS.es;
  const langPrefix = lang === 'es' ? '' : `/${lang}`;
  const canonicalUrl = `${SITE_URL}${langPrefix}/${segs.hub}`;

  const productsHref = `${langPrefix}/productos-digitales`;

  // Only show cards with a real translation in the current language. `uc.content[lang]`
  // is always truthy because makeContent backfills with ES — use hasNativeContent to detect
  // the actual presence of a translation in the EN/etc. content map.
  const allRoles = getUseCasesByType('role');
  const allConcepts = getUseCasesByType('concept');
  const roles = lang === 'es' ? allRoles : allRoles.filter(uc => hasNativeContent(uc.id, lang));
  const concepts = lang === 'es' ? allConcepts : allConcepts.filter(uc => hasNativeContent(uc.id, lang));

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    '@id': `${canonicalUrl}#breadcrumb`,
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: segs.hubLabel },
    ],
  };

  const items = activeTab === 'role' ? roles : concepts;
  const typeSegment = activeTab === 'role' ? segs.role : segs.concept;

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title={ui.seoTitle}
        description={ui.seoDescription}
        keywords={ui.seoKeywords}
        canonical={canonicalUrl}
      />
      <Helmet>
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-primary/10 via-background to-secondary/5 py-20 lg:py-28">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2">{ui.badge}</Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                {ui.h1}
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-3xl mx-auto text-balance">
                {ui.heroSubtitle}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  {ui.ctaPrimary} <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button asChild size="lg" variant="outline">
                  <Link to={productsHref}>{ui.ctaSecondary} <ArrowRight className="ml-2 h-4 w-4" /></Link>
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">{ui.ctaNote}</p>
            </div>
          </div>
        </section>

        {/* Tabs */}
        <section className="py-12 border-b">
          <div className="container mx-auto px-4">
            <div className="flex flex-col sm:flex-row justify-center items-stretch sm:items-center gap-3 mb-3 max-w-2xl mx-auto">
              <Button
                variant={activeTab === 'role' ? 'default' : 'outline'}
                size="lg"
                onClick={() => setActiveTab('role')}
                className={`w-full sm:w-auto ${activeTab === 'role' ? 'btn-gold' : ''}`}
              >
                <Briefcase className="mr-2 h-4 w-4 flex-shrink-0" />
                <span className="truncate">{ui.tabRole}</span>
                <Badge variant="secondary" className="ml-2">{roles.length}</Badge>
              </Button>
              <Button
                variant={activeTab === 'concept' ? 'default' : 'outline'}
                size="lg"
                onClick={() => setActiveTab('concept')}
                className={`w-full sm:w-auto ${activeTab === 'concept' ? 'btn-gold' : ''}`}
              >
                <Building2 className="mr-2 h-4 w-4 flex-shrink-0" />
                <span className="truncate">{ui.tabConcept}</span>
                <Badge variant="secondary" className="ml-2">{concepts.length}</Badge>
              </Button>
            </div>
            <p className="text-center text-sm text-muted-foreground px-4">
              {activeTab === 'role' ? ui.tabRoleDesc : ui.tabConceptDesc}
            </p>
          </div>
        </section>

        {/* Cards grid */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
              {items.map(uc => {
                const content = uc.content[lang] || uc.content.es;
                const theme = COLOR_THEMES[uc.colorTheme] || COLOR_THEMES.amber;
                const slug = uc.slug[lang] || uc.slug.es;
                const Icon = getIconComponent(uc.iconKey);
                return (
                  <Link key={uc.id} to={`${langPrefix}/${segs.hub}/${typeSegment}/${slug}`}>
                    <Card className="h-full border-2 hover:border-primary transition-all hover:shadow-xl">
                      <CardHeader>
                        <div className={`w-14 h-14 ${theme.bg} rounded-xl flex items-center justify-center mb-3`}>
                          <Icon className={`h-7 w-7 ${theme.text}`} />
                        </div>
                        <CardTitle className="text-xl">{content.h1.replace(ui.h1StripPrefix, '')}</CardTitle>
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

        {/* pSEO Cities cross-link (ES only) */}
        {lang === 'es' && (
          <section className="py-16 bg-muted/30">
            <div className="container mx-auto px-4 max-w-5xl">
              <div className="text-center mb-8">
                <h2 className="text-2xl lg:text-3xl font-bold mb-3">
                  ¿Buscas Recursos por Ciudad?
                </h2>
                <p className="text-muted-foreground max-w-2xl mx-auto">
                  Costes reales, licencias específicas, salarios sectoriales y mejores barrios para 15 ciudades de España y LATAM.
                </p>
              </div>
              <div className="flex flex-wrap justify-center gap-2 mb-6">
                {['madrid', 'barcelona', 'ciudad-de-mexico', 'bogota', 'medellin', 'buenos-aires', 'santiago'].map((slug) => (
                  <Link
                    key={slug}
                    to={`/abrir-restaurante/${slug}`}
                    className="px-4 py-2 bg-background hover:bg-accent/15 hover:text-accent rounded-full text-sm font-medium transition-colors border border-border"
                  >
                    Abrir restaurante en {slug === 'ciudad-de-mexico' ? 'CDMX' : slug === 'buenos-aires' ? 'Buenos Aires' : slug.charAt(0).toUpperCase() + slug.slice(1)}
                  </Link>
                ))}
              </div>
              <div className="text-center">
                <Button asChild variant="outline" size="lg">
                  <Link to="/seo-restaurantes-por-ciudad">
                    Ver todas las ciudades + 5 recursos <ArrowRight className="ml-2 h-4 w-4" />
                  </Link>
                </Button>
              </div>
            </div>
          </section>
        )}

        {/* CTA */}
        <section className="py-20 bg-gradient-to-br from-primary/10 via-background to-secondary/5">
          <div className="container mx-auto px-4 text-center">
            <Sparkles className="h-10 w-10 text-primary mx-auto mb-4" />
            <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">
              {ui.finalH2}
            </h2>
            <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
              {ui.finalBody}
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                {ui.ctaPrimary} <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to={productsHref}>{ui.finalSecondary}</Link>
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
