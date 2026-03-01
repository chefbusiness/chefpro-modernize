import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';
import { Users, CheckCircle, RotateCcw, ArrowRight } from 'lucide-react';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';
import PricingPlans from '@/components/PricingPlans';

const LANG_SLUGS: Record<string, string> = {
  es: '/calculadora-brigada-restaurante',
  en: '/en/restaurant-brigade-calculator',
  fr: '/fr/calculateur-brigade-restaurant',
  de: '/de/brigaden-rechner-restaurant',
  it: '/it/calcolatore-brigata-ristorante',
  pt: '/pt/calculadora-brigada-restaurante',
  nl: '/nl/brigade-calculator-restaurant',
};

const HUB_SLUGS: Record<string, string> = {
  es: '/herramientas-gratuitas',
  en: '/en/free-tools-restaurants',
  fr: '/fr/outils-gratuits-restaurant',
  de: '/de/kostenlose-tools-restaurant',
  it: '/it/strumenti-gratuiti-ristorante',
  pt: '/pt/ferramentas-gratuitas-restaurante',
  nl: '/nl/gratis-tools-restaurant',
};

// Brigade ratios by service type index (carta, menu, buffet, catering)
// Returns { kitchen staff roles, sala staff roles }
function calculateBrigade(
  covers: number,
  serviceTypeIdx: number,
  servicesPerDay: number,
  hasDelivery: boolean,
  deliveryOrders: number
) {
  // Complexity multiplier per service type
  const complexity = [1.0, 0.7, 0.5, 0.8][serviceTypeIdx] ?? 1.0;

  // Kitchen ratios (covers per cook role)
  const dailyCovers = covers * servicesPerDay;

  // Base kitchen staff
  const headChef = 1;
  const sousChef = dailyCovers > 80 ? 1 : 0;
  const chefPartida = Math.max(1, Math.ceil((covers * complexity) / 30));
  const cocinero = Math.max(0, Math.ceil((covers * complexity) / 20) - chefPartida);
  const ayudante = Math.max(0, Math.ceil(covers / 40));
  const kitchenPorter = Math.max(1, Math.ceil(dailyCovers / 100) + (hasDelivery ? 1 : 0));
  const deliveryBonus = hasDelivery ? Math.ceil(deliveryOrders / 30) : 0;

  const totalKitchen = headChef + sousChef + chefPartida + cocinero + ayudante + kitchenPorter + deliveryBonus;

  // Sala ratios
  // Covers per waiter: carta=12, menu=18, buffet=25, catering=20
  const coversPerWaiter = [12, 18, 25, 20][serviceTypeIdx] ?? 15;
  const camarero = Math.max(1, Math.ceil(covers / coversPerWaiter));
  const maitre = covers > 40 ? 1 : 0;
  const jefeRango = covers > 60 ? Math.ceil(camarero / 3) : 0;
  const ayudanteSala = Math.ceil(camarero * 0.3);
  const totalSala = maitre + jefeRango + camarero + ayudanteSala;

  const ratio = camarero > 0 ? Math.round(covers / camarero) : covers;

  return {
    headChef, sousChef, chefPartida, cocinero, ayudante, kitchenPorter, deliveryBonus,
    totalKitchen,
    maitre, jefeRango, camarero, ayudanteSala,
    totalSala,
    totalStaff: totalKitchen + totalSala,
    ratio,
  };
}

export default function CalculadoraBrigada() {
  const { t } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const siteUrl = import.meta.env.VITE_SITE_URL || 'https://aichef.pro';
  const slug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = `${siteUrl}${slug}`;

  const tool = t('toolBrigada.tool', { returnObjects: true }) as any;
  const hero = t('toolBrigada.hero', { returnObjects: true }) as any;
  const faqItems: Array<{ q: string; a: string }> = t('toolBrigada.faq', { returnObjects: true }) as any;
  const ctaSection = t('toolBrigada.cta_section', { returnObjects: true }) as any;
  const howItWorks = t('toolBrigada.how_it_works', { returnObjects: true }) as any;
  const benefits = t('toolBrigada.benefits', { returnObjects: true }) as any;

  const serviceTypes: string[] = Array.isArray(tool?.service_types) ? tool.service_types : [];
  const servicesOptions: string[] = Array.isArray(tool?.services_options) ? tool.services_options : [];

  const [covers, setCovers] = useState('50');
  const [serviceTypeIdx, setServiceTypeIdx] = useState(0);
  const [servicesPerDayIdx, setServicesPerDayIdx] = useState(1);
  const [hasDelivery, setHasDelivery] = useState(false);
  const [deliveryOrders, setDeliveryOrders] = useState('20');
  const [result, setResult] = useState<ReturnType<typeof calculateBrigade> | null>(null);

  const calculate = () => {
    const c = parseInt(covers) || 0;
    const spd = servicesPerDayIdx + 1;
    const d = parseInt(deliveryOrders) || 0;
    if (c <= 0) return;
    setResult(calculateBrigade(c, serviceTypeIdx, spd, hasDelivery, d));
  };

  const reset = () => {
    setCovers('50');
    setServiceTypeIdx(0);
    setServicesPerDayIdx(1);
    setHasDelivery(false);
    setDeliveryOrders('20');
    setResult(null);
  };

  const seoTitle = t('toolBrigada.seo.title');
  const seoDescription = t('toolBrigada.seo.description');
  const languages = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];

  const faqSchema = Array.isArray(faqItems) && faqItems.length > 0
    ? {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: faqItems.map(f => ({
          '@type': 'Question',
          name: f.q,
          acceptedAnswer: { '@type': 'Answer', text: f.a },
        })),
      }
    : null;

  return (
    <>
      <Helmet>
        <title>{seoTitle}</title>
        <meta name="description" content={seoDescription} />
        <meta name="keywords" content={t('toolBrigada.seo.keywords')} />
        <link rel="canonical" href={canonicalUrl} />
        <html lang={currentLanguage} />
        {languages.map(lang => (
          <link key={lang} rel="alternate" hrefLang={lang} href={`${siteUrl}${LANG_SLUGS[lang]}`} />
        ))}
        <link rel="alternate" hrefLang="x-default" href={`${siteUrl}${LANG_SLUGS.es}`} />
        <meta property="og:title" content={seoTitle} />
        <meta property="og:description" content={seoDescription} />
        <meta property="og:url" content={canonicalUrl} />
        <meta property="og:type" content="website" />
        <meta name="robots" content="index,follow" />
        {faqSchema && (
          <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
        )}
      </Helmet>

      <ModernHeader />

      <main className="min-h-screen bg-white">
        {/* Hero */}
        <section className="bg-gradient-to-br from-orange-50 via-amber-50 to-white py-16 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <HeroSocialProof />
            <Badge className="bg-orange-100 text-orange-700 border-orange-200 mb-4">{hero.badge}</Badge>
            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{hero.h1}</h1>
            <p className="text-lg text-slate-600 mb-8 max-w-2xl mx-auto">{hero.subtitle}</p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button asChild className="bg-orange-600 hover:bg-orange-700 text-white px-8 py-3 text-base">
                <a href="#tool">
                  <Users className="w-4 h-4 mr-2" />
                  {hero.cta_tool}
                </a>
              </Button>
              <Button variant="outline" asChild className="border-orange-300 text-orange-700 hover:bg-orange-50 px-8 py-3 text-base">
                <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                  {hero.cta_premium} <ArrowRight className="w-4 h-4 ml-1" />
                </a>
              </Button>
            </div>
          </div>
        </section>

        {/* Tool */}
        <section id="tool" className="py-12 px-4">
          <div className="max-w-2xl mx-auto">
            <div className="bg-white border border-slate-200 rounded-2xl shadow-sm p-6 md:p-8">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 bg-orange-100 rounded-xl flex items-center justify-center">
                  <Users className="w-5 h-5 text-orange-600" />
                </div>
                <h2 className="text-xl font-bold text-slate-800">{tool.title}</h2>
              </div>

              <div className="space-y-5">
                {/* Covers */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{tool.covers_label}</label>
                  <p className="text-xs text-slate-500 mb-2">{tool.covers_hint}</p>
                  <input
                    type="number"
                    value={covers}
                    onChange={e => setCovers(e.target.value)}
                    min={1}
                    max={500}
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-orange-400 focus:border-transparent"
                  />
                </div>

                {/* Service type */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">{tool.service_type_label}</label>
                  <div className="grid grid-cols-2 gap-2">
                    {serviceTypes.map((st: string, i: number) => (
                      <button
                        key={i}
                        onClick={() => setServiceTypeIdx(i)}
                        className={`px-3 py-2.5 rounded-xl border text-sm font-medium transition-all ${
                          serviceTypeIdx === i
                            ? 'border-orange-500 bg-orange-50 text-orange-700'
                            : 'border-slate-200 text-slate-600 hover:border-orange-300 hover:bg-orange-50'
                        }`}
                      >
                        {st}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Services per day */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">{tool.services_per_day_label}</label>
                  <div className="space-y-2">
                    {servicesOptions.map((opt: string, i: number) => (
                      <button
                        key={i}
                        onClick={() => setServicesPerDayIdx(i)}
                        className={`w-full text-left px-4 py-3 rounded-xl border text-sm transition-all ${
                          servicesPerDayIdx === i
                            ? 'border-orange-500 bg-orange-50 text-orange-700 font-medium'
                            : 'border-slate-200 text-slate-600 hover:border-orange-300'
                        }`}
                      >
                        {opt}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Delivery toggle */}
                <div>
                  <label className="flex items-center gap-3 cursor-pointer">
                    <div
                      onClick={() => setHasDelivery(!hasDelivery)}
                      className={`relative w-11 h-6 rounded-full transition-colors ${hasDelivery ? 'bg-orange-500' : 'bg-slate-300'}`}
                    >
                      <div className={`absolute top-1 w-4 h-4 bg-white rounded-full shadow transition-transform ${hasDelivery ? 'translate-x-6' : 'translate-x-1'}`} />
                    </div>
                    <span className="text-sm font-medium text-slate-700">{tool.has_delivery_label}</span>
                  </label>
                  {hasDelivery && (
                    <div className="mt-3">
                      <label className="block text-sm text-slate-600 mb-1">{tool.delivery_volume_label}</label>
                      <input
                        type="number"
                        value={deliveryOrders}
                        onChange={e => setDeliveryOrders(e.target.value)}
                        min={1}
                        className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-orange-400 focus:border-transparent"
                      />
                    </div>
                  )}
                </div>
              </div>

              <Button
                onClick={calculate}
                disabled={!covers || parseInt(covers) <= 0}
                className="w-full mt-6 bg-orange-600 hover:bg-orange-700 text-white py-3 disabled:opacity-50"
              >
                <Users className="w-4 h-4 mr-2" />
                {tool.calculate}
              </Button>
            </div>

            {/* Results */}
            {result && (
              <div className="mt-6 bg-white border border-slate-200 rounded-2xl shadow-sm p-6 md:p-8">
                <h2 className="text-lg font-bold text-slate-800 mb-6">{tool.result_title}</h2>

                <div className="grid md:grid-cols-2 gap-6 mb-6">
                  {/* Kitchen */}
                  <div className="bg-orange-50 border border-orange-200 rounded-xl p-5">
                    <h3 className="font-bold text-orange-800 mb-4 text-base">{tool.kitchen_title}</h3>
                    <div className="space-y-2">
                      {[
                        [tool.head_chef, result.headChef],
                        [tool.sous_chef, result.sousChef],
                        [tool.chef_partida, result.chefPartida],
                        [tool.cocinero, result.cocinero],
                        [tool.ayudante, result.ayudante],
                        [tool.kitchen_porter, result.kitchenPorter],
                        ...(result.deliveryBonus > 0 ? [['+ Delivery', result.deliveryBonus]] : []),
                      ].filter(([, v]) => (v as number) > 0).map(([label, val], i) => (
                        <div key={i} className="flex justify-between items-center text-sm">
                          <span className="text-slate-600">{label as string}</span>
                          <span className="font-bold text-orange-700 w-8 text-center bg-white rounded-lg py-0.5">{val as number}</span>
                        </div>
                      ))}
                      <div className="pt-2 border-t border-orange-200 flex justify-between items-center font-bold">
                        <span className="text-slate-700">{tool.total_kitchen}</span>
                        <span className="text-orange-700 text-lg">{result.totalKitchen}</span>
                      </div>
                    </div>
                  </div>

                  {/* Sala */}
                  <div className="bg-amber-50 border border-amber-200 rounded-xl p-5">
                    <h3 className="font-bold text-amber-800 mb-4 text-base">{tool.sala_title}</h3>
                    <div className="space-y-2">
                      {[
                        [tool.maitre, result.maitre],
                        [tool.jefe_rango, result.jefeRango],
                        [tool.camarero, result.camarero],
                        [tool.ayudante_sala, result.ayudanteSala],
                      ].filter(([, v]) => (v as number) > 0).map(([label, val], i) => (
                        <div key={i} className="flex justify-between items-center text-sm">
                          <span className="text-slate-600">{label as string}</span>
                          <span className="font-bold text-amber-700 w-8 text-center bg-white rounded-lg py-0.5">{val as number}</span>
                        </div>
                      ))}
                      <div className="pt-2 border-t border-amber-200 flex justify-between items-center font-bold">
                        <span className="text-slate-700">{tool.total_sala}</span>
                        <span className="text-amber-700 text-lg">{result.totalSala}</span>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Totals */}
                <div className="bg-slate-800 rounded-xl p-4 mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
                  <div className="text-center flex-1">
                    <p className="text-slate-400 text-xs uppercase tracking-wide mb-1">{tool.total_staff}</p>
                    <p className="text-3xl font-bold text-white">{result.totalStaff}</p>
                  </div>
                  <div className="hidden sm:block w-px h-10 bg-slate-600" />
                  <div className="text-center flex-1">
                    <p className="text-slate-400 text-xs uppercase tracking-wide mb-1">{tool.ratio_label}</p>
                    <p className="text-3xl font-bold text-orange-400">1:{result.ratio}</p>
                  </div>
                </div>

                <div className="flex flex-col sm:flex-row gap-3">
                  <Button onClick={reset} variant="outline" className="border-slate-300 text-slate-600 flex-1">
                    <RotateCcw className="w-4 h-4 mr-2" />
                    {tool.reset}
                  </Button>
                  <Button asChild className="bg-orange-600 hover:bg-orange-700 text-white flex-1">
                    <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                      {tool.cta_after} <ArrowRight className="w-4 h-4 ml-1" />
                    </a>
                  </Button>
                </div>
              </div>
            )}
          </div>
        </section>

        {/* How it works */}
        {howItWorks && (
          <section className="py-12 px-4 bg-slate-50">
            <div className="max-w-4xl mx-auto">
              <h2 className="text-2xl font-bold text-center text-slate-800 mb-8">{howItWorks.title}</h2>
              <div className="grid md:grid-cols-3 gap-6">
                {Array.isArray(howItWorks.steps) && howItWorks.steps.map((step: { step: string; title: string; description: string }, i: number) => (
                  <div key={i} className="bg-white rounded-xl p-6 text-center shadow-sm">
                    <div className="w-10 h-10 bg-orange-100 text-orange-700 rounded-full flex items-center justify-center text-lg font-bold mx-auto mb-3">
                      {step.step}
                    </div>
                    <h3 className="font-semibold text-slate-800 mb-2">{step.title}</h3>
                    <p className="text-sm text-slate-600">{step.description}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {/* Benefits */}
        {benefits && (
          <section className="py-12 px-4">
            <div className="max-w-4xl mx-auto">
              <h2 className="text-2xl font-bold text-center text-slate-800 mb-8">{benefits.title}</h2>
              <div className="grid md:grid-cols-2 gap-4">
                {Array.isArray(benefits.items) && benefits.items.map((item: string, i: number) => (
                  <div key={i} className="flex items-start gap-3 p-4 bg-orange-50 rounded-xl">
                    <CheckCircle className="w-5 h-5 text-orange-500 flex-shrink-0 mt-0.5" />
                    <span className="text-slate-700 text-sm">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        <PricingPlans toolKey="toolBrigada" />

        {/* FAQ */}
        {Array.isArray(faqItems) && faqItems.length > 0 && (
          <section className="py-12 px-4 bg-slate-50">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-2xl font-bold text-slate-800 mb-8 text-center">
                {t('toolBrigada.faq_section.title')}
              </h2>
              <div className="space-y-4">
                {faqItems.map((item, i) => (
                  <div key={i} className="bg-white rounded-xl p-6 shadow-sm">
                    <h3 className="font-semibold text-slate-800 mb-2">{item.q}</h3>
                    <p className="text-slate-600 text-sm">{item.a}</p>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        <OtherFreeTools excludeIndex={6} />

        {/* Final CTA */}
        {ctaSection && (
          <section className="py-16 px-4">
            <div className="max-w-3xl mx-auto text-center">
              <h2 className="text-2xl md:text-3xl font-bold text-slate-900 mb-4">{ctaSection.title}</h2>
              <p className="text-slate-600 mb-8 text-lg">{ctaSection.subtitle}</p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <Button asChild size="lg" className="bg-orange-600 hover:bg-orange-700 text-white px-8">
                  <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                    {ctaSection.primary} <ArrowRight className="w-4 h-4 ml-2" />
                  </a>
                </Button>
                <Button variant="outline" asChild size="lg" className="border-orange-300 text-orange-700 hover:bg-orange-50 px-8">
                  <Link to={HUB_SLUGS[currentLanguage] || '/herramientas-gratuitas'}>
                    {ctaSection.secondary}
                  </Link>
                </Button>
              </div>
            </div>
          </section>
        )}
      </main>

      <ModernFooter />
    </>
  );
}
