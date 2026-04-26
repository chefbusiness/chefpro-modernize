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
import { getUseCasesByType, type LangCode } from '@/data/use-cases';
import { ArrowRight, Briefcase, Building2, Sparkles } from 'lucide-react';

const SITE_URL = 'https://aichef.pro';

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

  const roles = getUseCasesByType('role');
  const concepts = getUseCasesByType('concept');

  const langPrefix = lang === 'es' ? '' : `/${lang}`;
  const canonicalUrl = `${SITE_URL}${langPrefix}/usos`;

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'Casos de uso', item: canonicalUrl },
    ],
  };

  const items = activeTab === 'role' ? roles : concepts;
  const typeSegment = activeTab === 'role' ? 'rol' : 'concepto';

  return (
    <div className="min-h-screen bg-background">
      <SEOHead
        title="Casos de uso de AI Chef Pro: por rol profesional y concepto de negocio"
        description="Descubre cómo usar AI Chef Pro según tu perfil profesional o tu concepto de hostelería: chef ejecutivo, propietario, gerente, pizzería, dark kitchen, catering, hotel, heladería y más."
        keywords="casos de uso AI Chef Pro, IA hostelería por perfil, IA restaurante por concepto, software hostelería profesional"
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
              <Badge className="mb-6 text-sm px-4 py-2">Casos de uso</Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                IA para Cada Rol y Cada Concepto de Hostelería
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-3xl mx-auto text-balance">
                Descubre cómo AI Chef Pro se adapta a tu perfil profesional y a tu concepto de negocio. Plantillas, agentes y guías diseñadas para tu día a día.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                  Empezar gratis <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button asChild size="lg" variant="outline">
                  <Link to="/productos-digitales">Ver productos <ArrowRight className="ml-2 h-4 w-4" /></Link>
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">5 usos gratis al mes · Sin tarjeta</p>
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
                <span className="truncate">Por Rol Profesional</span>
                <Badge variant="secondary" className="ml-2">{roles.length}</Badge>
              </Button>
              <Button
                variant={activeTab === 'concept' ? 'default' : 'outline'}
                size="lg"
                onClick={() => setActiveTab('concept')}
                className={`w-full sm:w-auto ${activeTab === 'concept' ? 'btn-gold' : ''}`}
              >
                <Building2 className="mr-2 h-4 w-4 flex-shrink-0" />
                <span className="truncate">Por Concepto de Negocio</span>
                <Badge variant="secondary" className="ml-2">{concepts.length}</Badge>
              </Button>
            </div>
            <p className="text-center text-sm text-muted-foreground px-4">
              {activeTab === 'role'
                ? 'Descubre cómo usar AI Chef Pro según tu rol profesional en el equipo o en el negocio.'
                : 'Descubre cómo encaja AI Chef Pro en tu tipo concreto de negocio gastronómico.'}
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
                  <Link key={uc.id} to={`${langPrefix}/usos/${typeSegment}/${slug}`}>
                    <Card className="h-full border-2 hover:border-primary transition-all hover:shadow-xl">
                      <CardHeader>
                        <div className={`w-14 h-14 ${theme.bg} rounded-xl flex items-center justify-center mb-3`}>
                          <Icon className={`h-7 w-7 ${theme.text}`} />
                        </div>
                        <CardTitle className="text-xl">{content.h1.replace(/^IA para /, '')}</CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-sm text-muted-foreground mb-4">{content.heroTagline}</p>
                        <div className="flex items-center text-primary text-sm font-semibold">
                          Ver caso de uso <ArrowRight className="ml-1 h-4 w-4" />
                        </div>
                      </CardContent>
                    </Card>
                  </Link>
                );
              })}
            </div>
          </div>
        </section>

        {/* CTA */}
        <section className="py-20 bg-gradient-to-br from-primary/10 via-background to-secondary/5">
          <div className="container mx-auto px-4 text-center">
            <Sparkles className="h-10 w-10 text-primary mx-auto mb-4" />
            <h2 className="text-3xl lg:text-4xl font-bold text-foreground mb-4 text-balance">
              ¿No Ves Tu Caso? AI Chef Pro Se Adapta
            </h2>
            <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
              Empieza gratis y descubre cómo encaja en tu día a día. Sin tarjeta, 5 usos al mes para probar todas las herramientas.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" className="btn-gold" onClick={() => window.open(APP_URL, '_blank')}>
                Empezar gratis <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button asChild size="lg" variant="outline">
                <Link to="/productos-digitales">Ver productos digitales</Link>
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
