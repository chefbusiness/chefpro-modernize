import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';
import { Calendar, Copy, CheckCircle, RotateCcw, ArrowRight, Download } from 'lucide-react';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';
import PricingPlans from '@/components/PricingPlans';

const LANG_SLUGS: Record<string, string> = {
  es: '/calendario-contenidos-restaurante',
  en: '/en/restaurant-content-calendar',
  fr: '/fr/calendrier-contenu-restaurant',
  de: '/de/content-kalender-restaurant',
  it: '/it/calendario-contenuti-ristorante',
  pt: '/pt/calendario-conteudo-restaurante',
  nl: '/nl/content-kalender-restaurant',
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

// Gastro special dates per month (1-indexed) — universal/factual, stays in JS
const GASTRO_DATES: Record<number, Array<{ day: number; name: string }>> = {
  1: [{ day: 17, name: 'Día Mundial de la Tarta' }, { day: 20, name: 'Día Internacional del Chef' }],
  2: [{ day: 9, name: 'Día Internacional de la Pizza' }, { day: 14, name: 'San Valentín' }],
  3: [{ day: 19, name: 'San José / Día del Padre (ES)' }, { day: 21, name: 'Inicio de Primavera' }],
  4: [{ day: 7, name: 'Día Mundial de la Salud' }, { day: 22, name: 'Día de la Tierra' }],
  5: [{ day: 18, name: 'Día Internacional del Sushi' }, { day: 25, name: 'Día de la Cuchara' }],
  6: [{ day: 1, name: 'Día Internacional de la Leche' }, { day: 21, name: 'Día Mundial de la Ensalada' }],
  7: [{ day: 7, name: 'Día Mundial del Chocolate' }, { day: 28, name: 'Día Mundial del Helado' }],
  8: [{ day: 19, name: 'Día Mundial de la Fotografía' }, { day: 20, name: 'Día del Salmón Ahumado' }],
  9: [{ day: 25, name: 'Día Nacional del Arroz' }, { day: 27, name: 'Día Mundial del Turismo' }],
  10: [{ day: 16, name: 'Día Mundial de la Alimentación' }, { day: 31, name: 'Halloween' }],
  11: [{ day: 11, name: 'San Martín — caza y setas' }, { day: 25, name: 'Black Friday' }],
  12: [{ day: 24, name: 'Nochebuena' }, { day: 25, name: 'Navidad' }, { day: 31, name: 'Nochevieja' }],
};

// Hashtag seeds per network
const NETWORK_HASHTAGS: Record<string, string[]> = {
  Instagram: ['#foodphotography', '#instafood', '#foodie', '#restaurante', '#gastronomia'],
  TikTok: ['#foodtok', '#restaurantetiktok', '#cheftok', '#comida', '#gastro'],
  Facebook: ['#restaurante', '#gastronomia', '#food', '#hosteleria', '#chef'],
  Pinterest: ['#recetas', '#foodie', '#gastronomia', '#restaurante', '#cocina'],
};

interface CalendarEntry {
  day: number;
  network: string;
  typeEmoji: string;
  typeName: string;
  idea: string;
  hashtags: string[];
  isSpecial: boolean;
  specialName?: string;
}

function generateCalendar(
  monthIdx: number,
  frequencyIdx: number,
  selectedNetworks: string[],
  ideas: string[],
  contentTypes: Array<{ emoji: string; name: string }>
): CalendarEntry[] {
  const year = new Date().getFullYear();
  const daysInMonth = new Date(year, monthIdx + 1, 0).getDate();
  const specialDates = GASTRO_DATES[monthIdx + 1] || [];
  const networks = selectedNetworks.length > 0 ? selectedNetworks : ['Instagram'];

  // Determine posting days
  let postingDays: number[] = [];
  if (frequencyIdx === 0) {
    for (let i = 1; i <= daysInMonth; i++) postingDays.push(i);
  } else if (frequencyIdx === 1) {
    // ~3x/week: days 1,3,5 of each week
    for (let week = 0; week < 5; week++) {
      [1, 3, 5].forEach(offset => {
        const day = week * 7 + offset;
        if (day >= 1 && day <= daysInMonth) postingDays.push(day);
      });
    }
  } else {
    // Weekly: every 7 days starting day 1
    for (let d = 1; d <= daysInMonth; d += 7) postingDays.push(d);
  }

  return postingDays.map((day, i) => {
    const specialDate = specialDates.find(sd => sd.day === day);
    const typeIdx = i % contentTypes.length;
    const ideaIdx = specialDate ? (i + 5) % ideas.length : i % ideas.length;
    const network = networks[i % networks.length];
    const baseHashtags = NETWORK_HASHTAGS[network] || NETWORK_HASHTAGS['Instagram'];

    return {
      day,
      network,
      typeEmoji: contentTypes[typeIdx].emoji,
      typeName: contentTypes[typeIdx].name,
      idea: ideas[ideaIdx],
      hashtags: baseHashtags,
      isSpecial: !!specialDate,
      specialName: specialDate?.name,
    };
  });
}

export default function CalendarioContenidos() {
  const { t, i18n } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const siteUrl = import.meta.env.VITE_SITE_URL || 'https://aichef.pro';
  const slug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = `${siteUrl}${slug}`;

  const hero = t('toolCalendario.hero', { returnObjects: true }) as any;
  const tool = t('toolCalendario.tool', { returnObjects: true }) as any;
  const faqItems: Array<{ q: string; a: string }> = t('toolCalendario.faq', { returnObjects: true }) as any;
  const ctaSection = t('toolCalendario.cta_section', { returnObjects: true }) as any;
  const howItWorks = t('toolCalendario.how_it_works', { returnObjects: true }) as any;
  const benefits = t('toolCalendario.benefits', { returnObjects: true }) as any;

  const ideas: string[] = Array.isArray(tool?.ideas) ? tool.ideas : [];
  const contentTypes: Array<{ emoji: string; name: string }> = Array.isArray(tool?.content_types) ? tool.content_types : [];
  const venueTypes: string[] = Array.isArray(tool?.venue_types) ? tool.venue_types : [];
  const networks: string[] = Array.isArray(tool?.networks) ? tool.networks : ['Instagram', 'TikTok', 'Facebook'];
  const months: string[] = Array.isArray(tool?.months) ? tool.months : [];
  const frequencies: string[] = Array.isArray(tool?.frequencies) ? tool.frequencies : [];

  const [venueTypeIdx, setVenueTypeIdx] = useState(0);
  const [selectedNetworks, setSelectedNetworks] = useState<string[]>(['Instagram']);
  const [monthIdx, setMonthIdx] = useState(new Date().getMonth());
  const [frequencyIdx, setFrequencyIdx] = useState(1);
  const [calendar, setCalendar] = useState<CalendarEntry[] | null>(null);
  const [copiedIdx, setCopiedIdx] = useState<number | null>(null);
  const [copiedAll, setCopiedAll] = useState(false);

  const toggleNetwork = (net: string) => {
    setSelectedNetworks(prev =>
      prev.includes(net) ? prev.filter(n => n !== net) : [...prev, net]
    );
  };

  const handleGenerate = () => {
    const result = generateCalendar(monthIdx, frequencyIdx, selectedNetworks, ideas, contentTypes);
    setCalendar(result);
    setCopiedIdx(null);
    setCopiedAll(false);
  };

  const copyEntry = (entry: CalendarEntry, idx: number) => {
    const text = [
      `Día ${entry.day} — ${entry.network}`,
      `${entry.typeEmoji} ${entry.typeName}`,
      entry.isSpecial ? `📅 ${entry.specialName}` : '',
      entry.idea,
      entry.hashtags.join(' '),
    ].filter(Boolean).join('\n');
    navigator.clipboard.writeText(text).then(() => {
      setCopiedIdx(idx);
      setTimeout(() => setCopiedIdx(null), 2000);
    });
  };

  const copyAll = () => {
    if (!calendar) return;
    const lines = calendar.map(entry =>
      [
        `📅 Día ${entry.day} — ${entry.network} — ${entry.typeEmoji} ${entry.typeName}`,
        entry.isSpecial ? `   (${entry.specialName})` : '',
        `   ${entry.idea}`,
        `   ${entry.hashtags.join(' ')}`,
        '',
      ].filter(l => l !== null).join('\n')
    );
    navigator.clipboard.writeText(lines.join('\n')).then(() => {
      setCopiedAll(true);
      setTimeout(() => setCopiedAll(false), 2500);
    });
  };

  const reset = () => {
    setCalendar(null);
    setCopiedIdx(null);
    setCopiedAll(false);
  };

  const languages = ['es', 'en', 'fr', 'de', 'it', 'pt', 'nl'];
  const seoTitle = t('toolCalendario.seo.title');
  const seoDescription = t('toolCalendario.seo.description');

  const networkColors: Record<string, string> = {
    Instagram: 'bg-purple-100 text-purple-700',
    TikTok: 'bg-slate-900 text-white',
    Facebook: 'bg-blue-100 text-blue-700',
    Pinterest: 'bg-red-100 text-red-700',
  };

  return (
    <>
      <Helmet>
        <title>{seoTitle}</title>
        <meta name="description" content={seoDescription} />
        <meta name="keywords" content={t('toolCalendario.seo.keywords')} />
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
        <section className="bg-gradient-to-br from-purple-50 via-violet-50 to-white py-16 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <HeroSocialProof />
            <Badge className="bg-purple-100 text-purple-700 border-purple-200 mb-4">{hero?.badge}</Badge>
            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{hero?.h1}</h1>
            <p className="text-lg text-slate-600 mb-8 max-w-2xl mx-auto">{hero?.subtitle}</p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button asChild className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 text-base">
                <a href="#tool">
                  <Calendar className="w-4 h-4 mr-2" />
                  {hero?.cta_tool}
                </a>
              </Button>
              <Button variant="outline" asChild className="border-purple-300 text-purple-700 hover:bg-purple-50 px-8 py-3 text-base">
                <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                  {hero?.cta_premium} <ArrowRight className="w-4 h-4 ml-1" />
                </a>
              </Button>
            </div>
          </div>
        </section>

        {/* Tool */}
        <section id="tool" className="py-12 px-4">
          <div className="max-w-3xl mx-auto">
            <div className="bg-white border border-slate-200 rounded-2xl shadow-sm p-6 md:p-8">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 bg-purple-100 rounded-xl flex items-center justify-center">
                  <Calendar className="w-5 h-5 text-purple-600" />
                </div>
                <h2 className="text-xl font-bold text-slate-800">{tool?.title}</h2>
              </div>

              <div className="grid md:grid-cols-2 gap-4 mb-6">
                {/* Venue type */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{tool?.venue_type_label}</label>
                  <select
                    value={venueTypeIdx}
                    onChange={e => setVenueTypeIdx(Number(e.target.value))}
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-purple-400 focus:border-transparent bg-white"
                  >
                    {venueTypes.map((vt, i) => (
                      <option key={i} value={i}>{vt}</option>
                    ))}
                  </select>
                </div>

                {/* Month */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{tool?.month_label}</label>
                  <select
                    value={monthIdx}
                    onChange={e => setMonthIdx(Number(e.target.value))}
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-purple-400 focus:border-transparent bg-white"
                  >
                    {months.map((m, i) => (
                      <option key={i} value={i}>{m}</option>
                    ))}
                  </select>
                </div>

                {/* Frequency */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{tool?.frequency_label}</label>
                  <select
                    value={frequencyIdx}
                    onChange={e => setFrequencyIdx(Number(e.target.value))}
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-purple-400 focus:border-transparent bg-white"
                  >
                    {frequencies.map((f, i) => (
                      <option key={i} value={i}>{f}</option>
                    ))}
                  </select>
                </div>

                {/* Networks */}
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">{tool?.networks_label}</label>
                  <div className="flex flex-wrap gap-2">
                    {networks.map(net => (
                      <button
                        key={net}
                        onClick={() => toggleNetwork(net)}
                        className={`px-3 py-1.5 rounded-lg text-sm font-medium border transition-all ${
                          selectedNetworks.includes(net)
                            ? 'border-purple-400 bg-purple-100 text-purple-700'
                            : 'border-slate-300 bg-white text-slate-600 hover:border-purple-300'
                        }`}
                      >
                        {net}
                      </button>
                    ))}
                  </div>
                </div>
              </div>

              <Button
                onClick={handleGenerate}
                disabled={selectedNetworks.length === 0}
                className="w-full bg-purple-600 hover:bg-purple-700 text-white py-3 disabled:opacity-50"
              >
                <Calendar className="w-4 h-4 mr-2" />
                {tool?.generate}
              </Button>
            </div>

            {/* Results */}
            {calendar && calendar.length > 0 && (
              <div className="mt-6 bg-white border border-slate-200 rounded-2xl shadow-sm overflow-hidden">
                <div className="p-6 border-b border-slate-100 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
                  <div>
                    <h2 className="text-lg font-bold text-slate-800">{tool?.result_title}</h2>
                    <p className="text-sm text-slate-500">{calendar.length} {tool?.posts_label || 'publicaciones'} · {months[monthIdx]}</p>
                  </div>
                  <div className="flex gap-2">
                    <Button
                      onClick={copyAll}
                      variant="outline"
                      size="sm"
                      className="border-slate-300 text-slate-700 hover:bg-slate-50"
                    >
                      {copiedAll
                        ? <><CheckCircle className="w-4 h-4 mr-1 text-green-500" /> {tool?.copied}</>
                        : <><Copy className="w-4 h-4 mr-1" /> {tool?.copy_all}</>
                      }
                    </Button>
                    <Button onClick={reset} variant="outline" size="sm" className="border-slate-300 text-slate-600">
                      <RotateCcw className="w-4 h-4 mr-1" />
                      {tool?.reset}
                    </Button>
                  </div>
                </div>

                <div className="divide-y divide-slate-100">
                  {calendar.map((entry, i) => (
                    <div
                      key={i}
                      className={`p-4 hover:bg-slate-50 transition-colors ${entry.isSpecial ? 'bg-amber-50 hover:bg-amber-100' : ''}`}
                    >
                      <div className="flex items-start gap-3">
                        <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center flex-shrink-0 text-purple-700 font-bold text-sm">
                          {entry.day}
                        </div>
                        <div className="flex-1 min-w-0">
                          <div className="flex flex-wrap items-center gap-2 mb-1">
                            <span className={`text-xs px-2 py-0.5 rounded-full font-medium ${networkColors[entry.network] || 'bg-slate-100 text-slate-700'}`}>
                              {entry.network}
                            </span>
                            <span className="text-xs text-slate-500">{entry.typeEmoji} {entry.typeName}</span>
                            {entry.isSpecial && (
                              <span className="text-xs bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full">
                                📅 {entry.specialName}
                              </span>
                            )}
                          </div>
                          <p className="text-sm text-slate-700 mb-1">{entry.idea}</p>
                          <p className="text-xs text-slate-400">{entry.hashtags.join(' ')}</p>
                        </div>
                        <button
                          onClick={() => copyEntry(entry, i)}
                          className="flex-shrink-0 text-slate-400 hover:text-purple-600 transition-colors p-1"
                          title={tool?.copy_entry || 'Copiar'}
                        >
                          {copiedIdx === i
                            ? <CheckCircle className="w-4 h-4 text-green-500" />
                            : <Copy className="w-4 h-4" />
                          }
                        </button>
                      </div>
                    </div>
                  ))}
                </div>

                <div className="p-6 border-t border-slate-100 text-center">
                  <p className="text-slate-700 font-medium mb-3">{tool?.cta_after}</p>
                  <Button asChild className="bg-purple-600 hover:bg-purple-700 text-white">
                    <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                      AI Chef Pro Premium <ArrowRight className="w-4 h-4 ml-1" />
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
                {Array.isArray(howItWorks.steps) && howItWorks.steps.map((step: { number: string; title: string; description: string }, i: number) => (
                  <div key={i} className="bg-purple-50 rounded-xl p-6 text-center">
                    <div className="w-10 h-10 bg-purple-100 text-purple-700 rounded-full flex items-center justify-center text-lg font-bold mx-auto mb-3">
                      {step.number}
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
                  <div key={i} className="flex items-start gap-3 p-4 bg-white rounded-xl shadow-sm border border-slate-100">
                    <CheckCircle className="w-5 h-5 text-purple-500 flex-shrink-0 mt-0.5" />
                    <span className="text-slate-700 text-sm">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        <PricingPlans toolKey="toolCalendario" />

        {/* FAQ */}
        {Array.isArray(faqItems) && faqItems.length > 0 && (
          <section className="py-12 px-4 bg-slate-50">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-2xl font-bold text-slate-800 mb-8 text-center">
                {t('toolCalendario.faq_section.title')}
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

        <OtherFreeTools excludeIndex={2} />

        {/* Final CTA */}
        {ctaSection && (
          <section className="py-16 px-4">
            <div className="max-w-3xl mx-auto text-center">
              <h2 className="text-2xl md:text-3xl font-bold text-slate-900 mb-4">{ctaSection.title}</h2>
              <p className="text-slate-600 mb-8 text-lg">{ctaSection.subtitle}</p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <Button asChild size="lg" className="bg-purple-600 hover:bg-purple-700 text-white px-8">
                  <a href="#tool">
                    {ctaSection.cta_primary} <ArrowRight className="w-4 h-4 ml-2" />
                  </a>
                </Button>
                <Button variant="outline" asChild size="lg" className="border-purple-300 text-purple-700 hover:bg-purple-50 px-8">
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
