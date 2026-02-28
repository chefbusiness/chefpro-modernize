import { useTranslation } from 'react-i18next';
import { Link } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Calculator, ShieldAlert, Calendar, TrendingUp, FileText,
  Smartphone, Users, Sparkles, ArrowRight,
} from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

const SITE_URL = 'https://aichef.pro';

// ─── Slug maps (must match HerramientasGratuitas.tsx order exactly) ──────────
const TOOL_SLUGS: Record<string, Record<string, string>> = {
  0: { es: 'calculadora-food-cost-restaurante', en: 'en/food-cost-calculator-restaurant', fr: 'fr/calculateur-food-cost-restaurant', de: 'de/food-cost-rechner-restaurant', it: 'it/calcolatore-food-cost-ristorante', pt: 'pt/calculadora-food-cost-restaurante', nl: 'nl/food-cost-calculator-restaurant' },
  1: { es: 'detector-alergenos-restaurante', en: 'en/restaurant-allergen-detector', fr: 'fr/detecteur-allergenes-restaurant', de: 'de/allergen-detektor-restaurant', it: 'it/rilevatore-allergeni-ristorante', pt: 'pt/detector-alergenos-restaurante', nl: 'nl/allergenen-detector-restaurant' },
  2: { es: 'calendario-contenidos-restaurante', en: 'en/restaurant-content-calendar', fr: 'fr/calendrier-contenu-restaurant', de: 'de/content-kalender-restaurant', it: 'it/calendario-contenuti-ristorante', pt: 'pt/calendario-conteudo-restaurante', nl: 'nl/content-kalender-restaurant' },
  3: { es: 'simulador-rentabilidad-restaurante', en: 'en/restaurant-profit-simulator', fr: 'fr/simulateur-rentabilite-restaurant', de: 'de/rentabilitaet-simulator-restaurant', it: 'it/simulatore-redditivita-ristorante', pt: 'pt/simulador-rentabilidade-restaurante', nl: 'nl/winstgevendheid-simulator-restaurant' },
  4: { es: 'generador-textos-carta-restaurante', en: 'en/restaurant-menu-copy-generator', fr: 'fr/generateur-textes-carte-restaurant', de: 'de/speisekarten-text-generator', it: 'it/generatore-testi-menu-ristorante', pt: 'pt/gerador-textos-cardapio-restaurante', nl: 'nl/menukaart-tekst-generator' },
  5: { es: 'test-digitalizacion-restaurante', en: 'en/restaurant-digitalization-test', fr: 'fr/test-digitalisation-restaurant', de: 'de/digitalisierungstest-restaurant', it: 'it/test-digitalizzazione-ristorante', pt: 'pt/teste-digitalizacao-restaurante', nl: 'nl/digitaliseringstest-restaurant' },
  6: { es: 'calculadora-brigada-restaurante', en: 'en/restaurant-brigade-calculator', fr: 'fr/calculateur-brigade-restaurant', de: 'de/brigaden-rechner-restaurant', it: 'it/calcolatore-brigata-ristorante', pt: 'pt/calculadora-brigada-restaurante', nl: 'nl/brigade-calculator-restaurant' },
  7: { es: 'generador-menu-degustacion', en: 'en/tasting-menu-generator', fr: 'fr/generateur-menu-degustation', de: 'de/degustationsmenu-generator', it: 'it/generatore-menu-degustazione', pt: 'pt/gerador-menu-degustacao', nl: 'nl/proefmenu-generator' },
};

const HUB_SLUGS: Record<string, string> = {
  es: 'herramientas-gratuitas',
  en: 'en/free-tools-restaurants',
  fr: 'fr/outils-gratuits-restaurant',
  de: 'de/kostenlose-tools-restaurant',
  it: 'it/strumenti-gratuiti-ristorante',
  pt: 'pt/ferramentas-gratuitas-restaurante',
  nl: 'nl/gratis-tools-restaurant',
};

// ─── Icons & styles (same order as hub) ──────────────────────────────────────
const TOOL_ICONS = [
  <Calculator className="h-6 w-6 text-green-600" />,
  <ShieldAlert className="h-6 w-6 text-red-600" />,
  <Calendar className="h-6 w-6 text-purple-600" />,
  <TrendingUp className="h-6 w-6 text-yellow-600" />,
  <FileText className="h-6 w-6 text-blue-600" />,
  <Smartphone className="h-6 w-6 text-teal-600" />,
  <Users className="h-6 w-6 text-orange-600" />,
  <Sparkles className="h-6 w-6 text-indigo-600" />,
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

// ─── Tools with live routes (add 7 when GeneradorMenuDegustacion is built) ────
const LIVE_TOOLS = new Set([0, 1, 2, 3, 4, 5, 6]);

// ─── Component ────────────────────────────────────────────────────────────────

interface OtherFreeToolsProps {
  /** Index of the current tool (0–7) to exclude from the grid */
  excludeIndex: number;
}

export default function OtherFreeTools({ excludeIndex }: OtherFreeToolsProps) {
  const { t } = useTranslation();
  const { currentLanguage } = useLanguage();
  const lang = currentLanguage;

  const tools = t('toolHub.tools', { returnObjects: true }) as Array<{
    title: string;
    description: string;
    badge: string;
  }>;
  const sectionTitle = t('toolHub.other_tools_title') as string;
  const seeAllText = t('toolHub.see_all_tools') as string;

  const hubSlug = `/${HUB_SLUGS[lang] || HUB_SLUGS.es}`;

  const visibleTools = Array.isArray(tools)
    ? tools
        .map((tool, i) => ({ tool, i }))
        .filter(({ i }) => LIVE_TOOLS.has(i) && i !== excludeIndex)
    : [];

  return (
    <section className="py-16 bg-slate-50">
      <div className="container mx-auto px-4">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-center justify-between mb-8">
            <h2 className="text-2xl font-bold text-slate-900">{sectionTitle}</h2>
            <Link
              to={hubSlug}
              className="text-sm font-medium text-slate-600 hover:text-slate-900 flex items-center gap-1 transition-colors"
            >
              {seeAllText}
              <ArrowRight className="w-4 h-4" />
            </Link>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {visibleTools.map(({ tool, i }) => {
              const slugMap = TOOL_SLUGS[i];
              const slug = slugMap?.[lang] || slugMap?.['es'] || '';
              const href = `/${slug}`;

              return (
                <Link key={i} to={href} className="block group">
                  <Card
                    className={`h-full border-2 ${TOOL_STYLES[i]?.border ?? 'border-border'} shadow-sm hover:shadow-md transition-all duration-200 group-hover:-translate-y-0.5`}
                  >
                    <CardHeader className="pb-2 pt-4 px-4">
                      <div
                        className={`w-10 h-10 ${TOOL_STYLES[i]?.bg ?? 'bg-primary/10'} rounded-lg flex items-center justify-center mb-2`}
                      >
                        {TOOL_ICONS[i]}
                      </div>
                      <div className="flex items-start justify-between gap-2">
                        <CardTitle className="text-sm leading-tight">{tool.title}</CardTitle>
                        <span
                          className={`text-xs px-2 py-0.5 rounded-full font-medium flex-shrink-0 ${TOOL_STYLES[i]?.badge ?? 'bg-muted text-muted-foreground'}`}
                        >
                          {tool.badge}
                        </span>
                      </div>
                    </CardHeader>
                    <CardContent className="px-4 pb-4">
                      <p className="text-xs text-muted-foreground mb-2 leading-relaxed">
                        {tool.description}
                      </p>
                      <span className="text-xs font-medium text-primary flex items-center gap-1 group-hover:gap-2 transition-all">
                        <ArrowRight className="w-3 h-3" />
                      </span>
                    </CardContent>
                  </Card>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
