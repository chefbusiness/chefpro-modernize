import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';
import { Smartphone, CheckCircle, ChevronRight, RotateCcw, ArrowRight } from 'lucide-react';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';

const LANG_SLUGS: Record<string, string> = {
  es: '/test-digitalizacion-restaurante',
  en: '/en/restaurant-digitalization-test',
  fr: '/fr/test-digitalisation-restaurant',
  de: '/de/digitalisierungstest-restaurant',
  it: '/it/test-digitalizzazione-ristorante',
  pt: '/pt/teste-digitalizacao-restaurante',
  nl: '/nl/digitaliseringstest-restaurant',
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

const RESULT_COLORS = [
  { bg: 'bg-slate-50', border: 'border-slate-300', text: 'text-slate-700', bar: 'bg-slate-400' },
  { bg: 'bg-blue-50', border: 'border-blue-300', text: 'text-blue-700', bar: 'bg-blue-400' },
  { bg: 'bg-teal-50', border: 'border-teal-300', text: 'text-teal-700', bar: 'bg-teal-500' },
  { bg: 'bg-emerald-50', border: 'border-emerald-300', text: 'text-emerald-700', bar: 'bg-emerald-500' },
];

export default function TestDigitalizacion() {
  const { t, i18n } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const siteUrl = import.meta.env.VITE_SITE_URL || 'https://aichef.pro';
  const slug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = `${siteUrl}${slug}`;

  const questions: Array<{ id: number; text: string; options: string[] }> = t('toolScore.questions', { returnObjects: true }) as any;
  const results: Array<{ range: [number, number]; level: string; emoji: string; description: string; tips: string[] }> = t('toolScore.results', { returnObjects: true }) as any;
  const tool = t('toolScore.tool', { returnObjects: true }) as any;
  const hero = t('toolScore.hero', { returnObjects: true }) as any;
  const pricing = t('toolScore.pricing', { returnObjects: true }) as any;
  const faqItems: Array<{ q: string; a: string }> = t('toolScore.faq', { returnObjects: true }) as any;
  const ctaSection = t('toolScore.cta_section', { returnObjects: true }) as any;
  const howItWorks = t('toolScore.how_it_works', { returnObjects: true }) as any;
  const benefits = t('toolScore.benefits', { returnObjects: true }) as any;

  const [currentQ, setCurrentQ] = useState(0);
  const [answers, setAnswers] = useState<number[]>([]);
  const [score, setScore] = useState<number | null>(null);
  const [started, setStarted] = useState(false);

  const totalQ = Array.isArray(questions) ? questions.length : 6;

  const handleAnswer = (optionIndex: number) => {
    const newAnswers = [...answers, optionIndex];
    if (currentQ + 1 < totalQ) {
      setAnswers(newAnswers);
      setCurrentQ(currentQ + 1);
    } else {
      // Calculate score: each option = 0,33,66,100 points
      const points = newAnswers.map(a => Math.round((a / 3) * 100));
      const avg = Math.round(points.reduce((s, p) => s + p, 0) / points.length);
      setAnswers(newAnswers);
      setScore(avg);
    }
  };

  const getResult = (s: number) => {
    if (!Array.isArray(results)) return null;
    return results.find(r => s >= r.range[0] && s <= r.range[1]) || results[results.length - 1];
  };

  const reset = () => {
    setCurrentQ(0);
    setAnswers([]);
    setScore(null);
    setStarted(false);
  };

  const result = score !== null ? getResult(score) : null;
  const resultIndex = result ? results.findIndex(r => r === result) : 0;
  const colors = RESULT_COLORS[Math.min(resultIndex, RESULT_COLORS.length - 1)];

  const seoTitle = t('toolScore.seo.title');
  const seoDescription = t('toolScore.seo.description');

  const languages = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];

  return (
    <>
      <Helmet>
        <title>{seoTitle}</title>
        <meta name="description" content={seoDescription} />
        <meta name="keywords" content={t('toolScore.seo.keywords')} />
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
      </Helmet>

      <ModernHeader />

      <main className="min-h-screen bg-white">
        {/* Hero */}
        <section className="bg-gradient-to-br from-teal-50 via-cyan-50 to-white py-16 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <HeroSocialProof />
            <Badge className="bg-teal-100 text-teal-700 border-teal-200 mb-4">{hero.badge}</Badge>
            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{hero.h1}</h1>
            <p className="text-lg text-slate-600 mb-8 max-w-2xl mx-auto">{hero.subtitle}</p>
            {!started && score === null && (
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <Button
                  onClick={() => setStarted(true)}
                  className="bg-teal-600 hover:bg-teal-700 text-white px-8 py-3 text-base"
                >
                  <Smartphone className="w-4 h-4 mr-2" />
                  {hero.cta_tool}
                </Button>
                <Button variant="outline" asChild className="border-teal-300 text-teal-700 hover:bg-teal-50 px-8 py-3 text-base">
                  <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                    {hero.cta_premium} <ArrowRight className="w-4 h-4 ml-1" />
                  </a>
                </Button>
              </div>
            )}
          </div>
        </section>

        {/* Quiz Tool */}
        <section id="tool" className="py-12 px-4">
          <div className="max-w-2xl mx-auto">
            {/* Not started yet */}
            {!started && score === null && (
              <div className="bg-teal-50 border border-teal-200 rounded-2xl p-8 text-center">
                <Smartphone className="w-16 h-16 text-teal-500 mx-auto mb-4" />
                <h2 className="text-xl font-semibold text-slate-800 mb-2">{tool.title}</h2>
                <p className="text-slate-600 mb-6">{totalQ} preguntas · ~2 min</p>
                <Button onClick={() => setStarted(true)} className="bg-teal-600 hover:bg-teal-700 text-white px-8 py-3">
                  {tool.start_btn}
                </Button>
              </div>
            )}

            {/* Active quiz */}
            {started && score === null && Array.isArray(questions) && (
              <div className="bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
                {/* Progress bar */}
                <div className="h-2 bg-slate-100">
                  <div
                    className="h-2 bg-teal-500 transition-all duration-300"
                    style={{ width: `${((currentQ) / totalQ) * 100}%` }}
                  />
                </div>
                <div className="p-8">
                  <p className="text-sm text-teal-600 font-medium mb-2">
                    {tool.question_label.replace('{n}', String(currentQ + 1)).replace('{total}', String(totalQ))}
                  </p>
                  <h2 className="text-xl font-semibold text-slate-800 mb-6">{questions[currentQ]?.text}</h2>
                  <div className="space-y-3">
                    {questions[currentQ]?.options.map((option: string, idx: number) => (
                      <button
                        key={idx}
                        onClick={() => handleAnswer(idx)}
                        className="w-full text-left px-5 py-4 rounded-xl border border-slate-200 hover:border-teal-400 hover:bg-teal-50 transition-all duration-150 text-slate-700 group"
                      >
                        <span className="inline-flex items-center gap-3">
                          <span className="w-7 h-7 rounded-full border-2 border-slate-300 group-hover:border-teal-500 flex items-center justify-center text-xs font-bold text-slate-500 group-hover:text-teal-600 flex-shrink-0">
                            {String.fromCharCode(65 + idx)}
                          </span>
                          {option}
                        </span>
                      </button>
                    ))}
                  </div>
                </div>
              </div>
            )}

            {/* Result */}
            {score !== null && result && (
              <div className={`border-2 ${colors.border} ${colors.bg} rounded-2xl p-8`}>
                <div className="text-center mb-6">
                  <div className="text-5xl mb-3">{result.emoji}</div>
                  <h2 className="text-2xl font-bold text-slate-800 mb-1">{tool.result_title}</h2>
                  <p className={`text-3xl font-bold ${colors.text} mb-2`}>{result.level}</p>
                  <div className="flex items-center justify-center gap-2 mb-4">
                    <span className="text-sm text-slate-500">{tool.score_label}:</span>
                    <span className={`text-2xl font-bold ${colors.text}`}>{score}/100</span>
                  </div>
                  {/* Score bar */}
                  <div className="w-full bg-slate-200 rounded-full h-3 mb-4">
                    <div
                      className={`h-3 rounded-full ${colors.bar} transition-all duration-700`}
                      style={{ width: `${score}%` }}
                    />
                  </div>
                  <p className="text-slate-600">{result.description}</p>
                </div>

                {Array.isArray(result.tips) && result.tips.length > 0 && (
                  <div className="bg-white rounded-xl p-5 mb-6">
                    <h3 className="font-semibold text-slate-800 mb-3">{tool.next_steps_title}</h3>
                    <ul className="space-y-2">
                      {result.tips.map((tip: string, i: number) => (
                        <li key={i} className="flex items-start gap-2 text-slate-600 text-sm">
                          <ChevronRight className={`w-4 h-4 mt-0.5 flex-shrink-0 ${colors.text}`} />
                          {tip}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                <div className="text-center space-y-3">
                  <p className="text-slate-700 font-medium">{tool.cta_after}</p>
                  <div className="flex flex-col sm:flex-row gap-3 justify-center">
                    <Button asChild className="bg-teal-600 hover:bg-teal-700 text-white">
                      <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                        {tool.try_free} <ArrowRight className="w-4 h-4 ml-1" />
                      </a>
                    </Button>
                    <Button variant="outline" onClick={reset} className="border-slate-300 text-slate-600">
                      <RotateCcw className="w-4 h-4 mr-2" />
                      {tool.restart}
                    </Button>
                  </div>
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
                    <div className="w-10 h-10 bg-teal-100 text-teal-700 rounded-full flex items-center justify-center text-lg font-bold mx-auto mb-3">
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
                  <div key={i} className="flex items-start gap-3 p-4 bg-teal-50 rounded-xl">
                    <CheckCircle className="w-5 h-5 text-teal-500 flex-shrink-0 mt-0.5" />
                    <span className="text-slate-700 text-sm">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {/* Pricing CTA */}
        {pricing && (
          <section className="py-12 px-4 bg-gradient-to-br from-teal-600 to-cyan-700 text-white">
            <div className="max-w-3xl mx-auto text-center">
              <h2 className="text-2xl md:text-3xl font-bold mb-4">{pricing.title}</h2>
              <p className="text-teal-100 mb-6 text-lg">{pricing.subtitle}</p>
              <Button asChild size="lg" className="bg-white text-teal-700 hover:bg-teal-50 font-semibold px-8">
                <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                  {pricing.cta} <ArrowRight className="w-4 h-4 ml-2" />
                </a>
              </Button>
              {pricing.note && <p className="text-teal-200 text-sm mt-3">{pricing.note}</p>}
            </div>
          </section>
        )}

        {/* FAQ */}
        {Array.isArray(faqItems) && faqItems.length > 0 && (
          <section className="py-12 px-4 bg-slate-50">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-2xl font-bold text-slate-800 mb-8 text-center">
                {t('toolScore.faq_section.title')}
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

        <OtherFreeTools excludeIndex={5} />

        {/* Final CTA */}
        {ctaSection && (
          <section className="py-16 px-4">
            <div className="max-w-3xl mx-auto text-center">
              <h2 className="text-2xl md:text-3xl font-bold text-slate-900 mb-4">{ctaSection.title}</h2>
              <p className="text-slate-600 mb-8 text-lg">{ctaSection.subtitle}</p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <Button asChild size="lg" className="bg-teal-600 hover:bg-teal-700 text-white px-8">
                  <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                    {ctaSection.cta_primary} <ArrowRight className="w-4 h-4 ml-2" />
                  </a>
                </Button>
                <Button variant="outline" asChild size="lg" className="border-teal-300 text-teal-700 hover:bg-teal-50 px-8">
                  <Link to={HUB_SLUGS[currentLanguage] || '/herramientas-gratuitas'}>
                    {ctaSection.cta_secondary}
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
