import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import {
  Calculator, ShieldAlert, Calendar, TrendingUp, FileText,
  Smartphone, Users, Sparkles, ArrowRight, CheckCircle, ChefHat
} from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import HeroSocialProof from '@/components/HeroSocialProof';
import { useLanguage } from '@/hooks/useLanguage';

const APP_URL = 'https://app.aichef.pro';
const SITE_URL = 'https://aichef.pro';

const LANG_SLUGS: Record<string, string> = {
  es: 'herramientas-gratuitas',
  en: 'en/free-tools-restaurants',
  fr: 'fr/outils-gratuits-restaurant',
  de: 'de/kostenlose-tools-restaurant',
  it: 'it/strumenti-gratuiti-ristorante',
  pt: 'pt/ferramentas-gratuitas-restaurante',
  nl: 'nl/gratis-tools-restaurant',
};

// Slug maps for each tool page
const FOOD_COST_SLUGS: Record<string, string> = {
  es: 'calculadora-food-cost-restaurante',
  en: 'en/food-cost-calculator-restaurant',
  fr: 'fr/calculateur-food-cost-restaurant',
  de: 'de/food-cost-rechner-restaurant',
  it: 'it/calcolatore-food-cost-ristorante',
  pt: 'pt/calculadora-food-cost-restaurante',
  nl: 'nl/food-cost-calculator-restaurant',
};

const RENTABILIDAD_SLUGS: Record<string, string> = {
  es: 'simulador-rentabilidad-restaurante',
  en: 'en/restaurant-profit-simulator',
  fr: 'fr/simulateur-rentabilite-restaurant',
  de: 'de/rentabilitaet-simulator-restaurant',
  it: 'it/simulatore-redditivita-ristorante',
  pt: 'pt/simulador-rentabilidade-restaurante',
  nl: 'nl/winstgevendheid-simulator-restaurant',
};

const ALERGENOS_SLUGS: Record<string, string> = {
  es: 'detector-alergenos-restaurante',
  en: 'en/restaurant-allergen-detector',
  fr: 'fr/detecteur-allergenes-restaurant',
  de: 'de/allergen-detektor-restaurant',
  it: 'it/rilevatore-allergeni-ristorante',
  pt: 'pt/detector-alergenos-restaurante',
  nl: 'nl/allergenen-detector-restaurant',
};

const SCORE_SLUGS: Record<string, string> = {
  es: 'test-digitalizacion-restaurante',
  en: 'en/restaurant-digitalization-test',
  fr: 'fr/test-digitalisation-restaurant',
  de: 'de/digitalisierungstest-restaurant',
  it: 'it/test-digitalizzazione-ristorante',
  pt: 'pt/teste-digitalizacao-restaurante',
  nl: 'nl/digitaliseringstest-restaurant',
};

const BRIGADA_SLUGS: Record<string, string> = {
  es: 'calculadora-brigada-restaurante',
  en: 'en/restaurant-brigade-calculator',
  fr: 'fr/calculateur-brigade-restaurant',
  de: 'de/brigaden-rechner-restaurant',
  it: 'it/calcolatore-brigata-ristorante',
  pt: 'pt/calculadora-brigada-restaurante',
  nl: 'nl/brigade-calculator-restaurant',
};

const CALENDARIO_SLUGS: Record<string, string> = {
  es: 'calendario-contenidos-restaurante',
  en: 'en/restaurant-content-calendar',
  fr: 'fr/calendrier-contenu-restaurant',
  de: 'de/content-kalender-restaurant',
  it: 'it/calendario-contenuti-ristorante',
  pt: 'pt/calendario-conteudo-restaurante',
  nl: 'nl/content-kalender-restaurant',
};

const MENUCOPY_SLUGS: Record<string, string> = {
  es: 'generador-textos-carta-restaurante',
  en: 'en/restaurant-menu-copy-generator',
  fr: 'fr/generateur-textes-carte-restaurant',
  de: 'de/speisekarten-text-generator',
  it: 'it/generatore-testi-menu-ristorante',
  pt: 'pt/gerador-textos-cardapio-restaurante',
  nl: 'nl/menukaart-tekst-generator',
};

const DEGUSTACION_SLUGS: Record<string, string> = {
  es: 'generador-menu-degustacion',
  en: 'en/tasting-menu-generator',
  fr: 'fr/generateur-menu-degustation',
  de: 'de/degustationsmenu-generator',
  it: 'it/generatore-menu-degustazione',
  pt: 'pt/gerador-menu-degustacao',
  nl: 'nl/proefmenu-generator',
};

const TOOL_ICONS = [
  <Calculator className="h-7 w-7 text-green-600" />,
  <ShieldAlert className="h-7 w-7 text-red-600" />,
  <Calendar className="h-7 w-7 text-purple-600" />,
  <TrendingUp className="h-7 w-7 text-yellow-600" />,
  <FileText className="h-7 w-7 text-blue-600" />,
  <Smartphone className="h-7 w-7 text-teal-600" />,
  <Users className="h-7 w-7 text-orange-600" />,
  <Sparkles className="h-7 w-7 text-indigo-600" />,
];

const TOOL_STYLES = [
  { bg: 'bg-green-50', border: 'border-green-200', badge: 'bg-green-100 text-green-800' },
  { bg: 'bg-red-50', border: 'border-red-200', badge: 'bg-red-100 text-red-800' },
  { bg: 'bg-purple-50', border: 'border-purple-200', badge: 'bg-purple-100 text-purple-800' },
  { bg: 'bg-yellow-50', border: 'border-yellow-200', badge: 'bg-yellow-100 text-yellow-800' },
  { bg: 'bg-blue-50', border: 'border-blue-200', badge: 'bg-blue-100 text-blue-800' },
  { bg: 'bg-teal-50', border: 'border-teal-200', badge: 'bg-teal-100 text-teal-800' },
  { bg: 'bg-orange-50', border: 'border-orange-200', badge: 'bg-orange-100 text-orange-800' },
  { bg: 'bg-indigo-50', border: 'border-indigo-200', badge: 'bg-indigo-100 text-indigo-800' },
];

// Tools with live routes (add 7 when GeneradorMenuDegustacion is built)
const LIVE_TOOLS = new Set([0, 1, 2, 3, 4, 5, 6]);

// Map tool index to its slug map
function getToolSlug(index: number, lang: string): string {
  const maps = [
    FOOD_COST_SLUGS,
    ALERGENOS_SLUGS,
    CALENDARIO_SLUGS,
    RENTABILIDAD_SLUGS,
    MENUCOPY_SLUGS,
    SCORE_SLUGS,
    BRIGADA_SLUGS,
    DEGUSTACION_SLUGS,
  ];
  const slugMap = maps[index];
  const slug = slugMap?.[lang] || slugMap?.['es'] || '';
  return `/${slug}`;
}

export default function HerramientasGratuitas() {
  const { t } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();

  const k = (key: string) => t(`toolHub.${key}`, { returnObjects: true });
  const s = (key: string) => t(`toolHub.${key}`) as string;

  const tools = k('tools') as Array<{ title: string; description: string; badge: string; color: string }>;
  const whyItems = k('why.items') as string[];

  const lang = currentLanguage;
  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl = lang === 'es'
    ? `${SITE_URL}/${canonicalSlug}`
    : `${SITE_URL}/${canonicalSlug}`;

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: s('breadcrumb'), item: canonicalUrl },
    ],
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
        {Object.entries(LANG_SLUGS).map(([l, slug]) => {
          const href = `${SITE_URL}/${slug}`;
          return <link key={l} rel="alternate" hrefLang={l} href={href} />;
        })}
        <link rel="alternate" hrefLang="x-default" href={`${SITE_URL}/${LANG_SLUGS.es}`} />
        <script type="application/ld+json">{JSON.stringify(breadcrumbSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-amber-50 via-background to-orange-50/30 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2 bg-amber-100 text-amber-800 border-amber-200">
                {s('hero.badge')}
              </Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl lg:text-6xl mb-6 text-balance">
                {s('hero.h1')}
              </h1>
              <p className="text-xl text-muted-foreground mb-6 max-w-3xl mx-auto text-balance">
                {s('hero.subtitle')}
              </p>
              <p className="text-base text-amber-700 font-medium mb-10">
                {s('hero.tagline')}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button
                  size="lg"
                  className="btn-gold"
                  onClick={() => window.open(`${getAppUrl(lang)}/pricing`, '_blank')}
                >
                  {s('cta.primary')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <Button
                  size="lg"
                  variant="outline"
                  onClick={() => window.open(getAppUrl(lang), '_blank')}
                >
                  {s('cta.secondary')}
                </Button>
              </div>
            </div>
          </div>
        </section>

        {/* 8 Tool Cards */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-7xl mx-auto">
              {tools.map((tool, i) => {
                const isLive = LIVE_TOOLS.has(i);
                const cardContent = (
                  <Card className={`h-full border-2 ${TOOL_STYLES[i]?.border ?? 'border-border'} shadow-md transition-all duration-200 ${isLive ? 'hover:shadow-xl group-hover:-translate-y-1' : 'opacity-60'}`}>
                    <CardHeader className="pb-3">
                      <div className={`w-12 h-12 ${TOOL_STYLES[i]?.bg ?? 'bg-primary/10'} rounded-xl flex items-center justify-center mb-3`}>
                        {TOOL_ICONS[i]}
                      </div>
                      <div className="flex items-start justify-between gap-2">
                        <CardTitle className="text-base leading-tight">{tool.title}</CardTitle>
                        <span className={`text-xs px-2 py-0.5 rounded-full font-medium flex-shrink-0 ${isLive ? (TOOL_STYLES[i]?.badge ?? 'bg-muted text-muted-foreground') : 'bg-gray-100 text-gray-500'}`}>
                          {isLive ? tool.badge : 'Próximamente'}
                        </span>
                      </div>
                    </CardHeader>
                    <CardContent className="pb-4">
                      <p className="text-sm text-muted-foreground mb-3">{tool.description}</p>
                      {isLive && (
                        <span className="text-sm font-medium text-primary flex items-center gap-1 group-hover:gap-2 transition-all">→</span>
                      )}
                    </CardContent>
                  </Card>
                );
                return isLive ? (
                  <a key={i} href={getToolSlug(i, lang)} className="block group">
                    {cardContent}
                  </a>
                ) : (
                  <div key={i} className="block cursor-default">
                    {cardContent}
                  </div>
                );
              })}
            </div>
          </div>
        </section>

        {/* Why Free */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center max-w-6xl mx-auto">
              <div>
                <h2 className="text-3xl font-bold text-foreground mb-6">{s('why.title')}</h2>
                <p className="text-lg text-muted-foreground mb-8">{s('why.body')}</p>
                <ul className="space-y-4">
                  {whyItems.map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-amber-500 mt-0.5 flex-shrink-0" />
                      <span className="text-muted-foreground">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div className="bg-gradient-to-br from-amber-50 to-orange-50 rounded-2xl p-8 border border-amber-100 text-center">
                <div className="w-16 h-16 bg-amber-100 rounded-full flex items-center justify-center mx-auto mb-6">
                  <ChefHat className="h-8 w-8 text-amber-600" />
                </div>
                <p className="text-4xl font-bold text-amber-700 mb-2">5.000+</p>
                <p className="text-muted-foreground mb-6">profesionales de la hostelería ya las usan</p>
                <Button
                  size="lg"
                  className="btn-gold w-full"
                  onClick={() => window.open(`${getAppUrl(lang)}/pricing`, '_blank')}
                >
                  {s('cta.primary')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <p className="text-xs text-muted-foreground mt-3">{s('cta.subtitle')}</p>
              </div>
            </div>
          </div>
        </section>

        {/* CTA Final */}
        <section className="py-20 bg-gradient-to-br from-amber-500 via-amber-400 to-yellow-300">
          <div className="container mx-auto px-4 text-center text-amber-950">
            <h2 className="text-3xl font-bold mb-4">{s('cta.title')}</h2>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">{s('cta.subtitle')}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button
                size="lg"
                className="bg-amber-950 text-amber-50 hover:bg-amber-900"
                onClick={() => window.open(`${getAppUrl(lang)}/pricing`, '_blank')}
              >
                {s('cta.primary')}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-amber-900 text-amber-900 bg-white/30 hover:bg-white/50"
                onClick={() => window.open(getAppUrl(lang), '_blank')}
              >
                {s('cta.secondary')}
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
