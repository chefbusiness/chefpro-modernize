import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import { Link } from 'react-router-dom';
import jsPDF from 'jspdf';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';
import { ShieldAlert, Copy, CheckCircle, RotateCcw, ArrowRight, FileDown } from 'lucide-react';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';
import PricingPlans from '@/components/PricingPlans';

const LANG_SLUGS: Record<string, string> = {
  es: '/detector-alergenos-restaurante',
  en: '/en/restaurant-allergen-detector',
  fr: '/fr/detecteur-allergenes-restaurant',
  de: '/de/allergen-detektor-restaurant',
  it: '/it/rilevatore-allergeni-ristorante',
  pt: '/pt/detector-alergenos-restaurante',
  nl: '/nl/allergenen-detector-restaurant',
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

interface Allergen {
  id: string;
  name: string;
  emoji: string;
  description: string;
  keywords: string[];
}

export default function DetectorAlergenos() {
  const { t, i18n } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();
  const siteUrl = import.meta.env.VITE_SITE_URL || 'https://aichef.pro';
  const slug = LANG_SLUGS[currentLanguage] || LANG_SLUGS.es;
  const canonicalUrl = `${siteUrl}${slug}`;

  const allergens: Allergen[] = t('toolAlergenos.allergens', { returnObjects: true }) as any;
  const tool = t('toolAlergenos.tool', { returnObjects: true }) as any;
  const hero = t('toolAlergenos.hero', { returnObjects: true }) as any;
  const faqItems: Array<{ q: string; a: string }> = t('toolAlergenos.faq', { returnObjects: true }) as any;
  const ctaSection = t('toolAlergenos.cta_section', { returnObjects: true }) as any;
  const howItWorks = t('toolAlergenos.how_it_works', { returnObjects: true }) as any;
  const benefits = t('toolAlergenos.benefits', { returnObjects: true }) as any;
  const allergensSection = t('toolAlergenos.allergens_section', { returnObjects: true }) as any;

  const [ingredients, setIngredients] = useState('');
  const [dishName, setDishName] = useState('');
  const [detected, setDetected] = useState<Allergen[] | null>(null);
  const [copied, setCopied] = useState(false);

  const detect = () => {
    if (!ingredients.trim()) return;
    const normalized = ingredients.toLowerCase();
    const found = (allergens || []).filter((allergen: Allergen) =>
      allergen.keywords.some((kw: string) => normalized.includes(kw.toLowerCase()))
    );
    setDetected(found);
    setCopied(false);
  };

  const reset = () => {
    setIngredients('');
    setDishName('');
    setDetected(null);
    setCopied(false);
  };

  const copySheet = () => {
    if (!detected) return;
    const lines = [
      dishName ? `Ficha de Alérgenos: ${dishName}` : 'Ficha de Alérgenos',
      `Ingredientes: ${ingredients}`,
      '',
      detected.length === 0
        ? tool.no_allergens
        : `${tool.allergens_found}: ${detected.map((a: Allergen) => `${a.emoji} ${a.name}`).join(', ')}`,
      '',
      tool.legal_note,
      tool.warning,
    ];
    navigator.clipboard.writeText(lines.join('\n')).then(() => {
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    });
  };

  const downloadPDF = () => {
    if (!detected) return;

    const doc = new jsPDF({ unit: 'mm', format: 'a4' });
    const W = 210; // page width
    const margin = 14;
    const col = W - margin * 2;
    let y = 0;

    const today = new Date().toLocaleDateString(currentLanguage, {
      year: 'numeric', month: '2-digit', day: '2-digit',
    });

    // ── HEADER ──────────────────────────────────────────────────────────
    doc.setFillColor(185, 28, 28); // red-700
    doc.rect(0, 0, W, 28, 'F');
    doc.setTextColor(255, 255, 255);
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.text(tool.pdf_title, margin, 11);
    doc.setFontSize(8);
    doc.setFont('helvetica', 'normal');
    doc.text(tool.pdf_subtitle, margin, 18);
    doc.setFontSize(9);
    doc.text('AI Chef Pro — aichef.pro', W - margin, 11, { align: 'right' });
    y = 36;

    // ── DISH + DATE ──────────────────────────────────────────────────────
    doc.setTextColor(30, 30, 30);
    doc.setFillColor(254, 242, 242); // red-50
    doc.roundedRect(margin, y, col, 18, 3, 3, 'F');
    doc.setFontSize(9);
    doc.setFont('helvetica', 'bold');
    doc.text(tool.pdf_dish_label + ':', margin + 4, y + 7);
    doc.setFont('helvetica', 'normal');
    doc.text(dishName || '—', margin + 30, y + 7);
    doc.setFont('helvetica', 'bold');
    doc.text(tool.pdf_date_label + ':', margin + 4, y + 14);
    doc.setFont('helvetica', 'normal');
    doc.text(today, margin + 30, y + 14);
    y += 25;

    // ── INGREDIENTS ──────────────────────────────────────────────────────
    doc.setFontSize(8);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(185, 28, 28);
    doc.text(tool.pdf_ingredients_label, margin, y);
    y += 5;
    doc.setFont('helvetica', 'normal');
    doc.setTextColor(60, 60, 60);
    const ingLines = doc.splitTextToSize(ingredients, col);
    doc.text(ingLines, margin, y);
    y += ingLines.length * 4.5 + 6;

    // ── DETECTED ALLERGENS ───────────────────────────────────────────────
    doc.setFontSize(8);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(185, 28, 28);
    doc.text(tool.pdf_detected_label, margin, y);
    y += 5;

    if (detected.length === 0) {
      doc.setFillColor(240, 253, 244);
      doc.roundedRect(margin, y, col, 10, 2, 2, 'F');
      doc.setFont('helvetica', 'normal');
      doc.setTextColor(22, 101, 52);
      doc.text(tool.pdf_no_allergens, margin + 3, y + 6.5);
      y += 16;
    } else {
      const perRow = 3;
      const boxW = col / perRow - 2;
      const boxH = 12;
      detected.forEach((a, i) => {
        const col_x = margin + (i % perRow) * (boxW + 3);
        const row_y = y + Math.floor(i / perRow) * (boxH + 3);
        doc.setFillColor(254, 226, 226); // red-100
        doc.roundedRect(col_x, row_y, boxW, boxH, 2, 2, 'F');
        doc.setTextColor(153, 27, 27);
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(7);
        doc.text(a.name, col_x + boxW / 2, row_y + 7.5, { align: 'center' });
      });
      const rows = Math.ceil(detected.length / perRow);
      y += rows * (boxH + 3) + 6;
    }

    // ── 14 ALLERGENS TABLE ───────────────────────────────────────────────
    if (y > 220) { doc.addPage(); y = 14; }

    doc.setFontSize(8);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(185, 28, 28);
    doc.text(tool.pdf_table_label, margin, y);
    y += 5;

    const detectedIds = new Set(detected.map(a => a.id));
    const tableColW = col / 2 - 1;
    const rowH = 8;

    allergens.forEach((a: Allergen, i: number) => {
      const isPresent = detectedIds.has(a.id);
      const col_x = margin + (i % 2) * (tableColW + 2);
      const row_y = y + Math.floor(i / 2) * rowH;

      if (isPresent) {
        doc.setFillColor(254, 226, 226);
      } else {
        doc.setFillColor(i % 2 === 0 ? 250 : 245, 250, 250);
      }
      doc.roundedRect(col_x, row_y, tableColW, rowH - 1, 1, 1, 'F');

      doc.setFontSize(7);
      doc.setFont('helvetica', 'normal');
      doc.setTextColor(40, 40, 40);
      doc.text(a.name, col_x + 3, row_y + 5);

      if (isPresent) {
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(185, 28, 28);
        doc.text(tool.pdf_present, col_x + tableColW - 3, row_y + 5, { align: 'right' });
      } else {
        doc.setTextColor(150, 150, 150);
        doc.text(tool.pdf_not_detected, col_x + tableColW - 3, row_y + 5, { align: 'right' });
      }
    });

    y += Math.ceil(allergens.length / 2) * rowH + 8;

    // ── WARNING ───────────────────────────────────────────────────────────
    if (y > 255) { doc.addPage(); y = 14; }
    doc.setFillColor(255, 251, 235); // amber-50
    doc.roundedRect(margin, y, col, 12, 2, 2, 'F');
    doc.setFontSize(7);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(146, 64, 14);
    doc.text(tool.pdf_warning, margin + 3, y + 8);
    y += 18;

    // ── FOOTER ────────────────────────────────────────────────────────────
    doc.setFillColor(185, 28, 28);
    doc.rect(0, 282, W, 15, 'F');
    doc.setFontSize(7);
    doc.setFont('helvetica', 'normal');
    doc.setTextColor(255, 255, 255);
    doc.text(tool.pdf_generated_by, W / 2, 291, { align: 'center' });

    const filename = `${tool.pdf_filename}-${(dishName || 'plato').toLowerCase().replace(/\s+/g, '-').slice(0, 25)}-${today.replace(/\//g, '-')}.pdf`;
    doc.save(filename);
  };

  const seoTitle = t('toolAlergenos.seo.title');
  const seoDescription = t('toolAlergenos.seo.description');
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
        <meta name="keywords" content={t('toolAlergenos.seo.keywords')} />
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
        <section className="bg-gradient-to-br from-rose-50 via-red-50 to-white py-16 px-4">
          <div className="max-w-3xl mx-auto text-center">
            <HeroSocialProof />
            <Badge className="bg-red-100 text-red-700 border-red-200 mb-4">{hero.badge}</Badge>
            <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{hero.h1}</h1>
            <p className="text-lg text-slate-600 mb-8 max-w-2xl mx-auto">{hero.subtitle}</p>
            <div className="flex flex-col sm:flex-row gap-3 justify-center">
              <Button asChild className="bg-red-600 hover:bg-red-700 text-white px-8 py-3 text-base">
                <a href="#tool">
                  <ShieldAlert className="w-4 h-4 mr-2" />
                  {hero.cta_tool}
                </a>
              </Button>
              <Button variant="outline" asChild className="border-red-300 text-red-700 hover:bg-red-50 px-8 py-3 text-base">
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
                <div className="w-10 h-10 bg-red-100 rounded-xl flex items-center justify-center">
                  <ShieldAlert className="w-5 h-5 text-red-600" />
                </div>
                <h2 className="text-xl font-bold text-slate-800">{tool.title}</h2>
              </div>

              <div className="space-y-4 mb-6">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{tool.dish_name_label}</label>
                  <input
                    type="text"
                    value={dishName}
                    onChange={e => setDishName(e.target.value)}
                    placeholder={tool.dish_name_placeholder}
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-red-400 focus:border-transparent"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{tool.input_label}</label>
                  <textarea
                    value={ingredients}
                    onChange={e => setIngredients(e.target.value)}
                    placeholder={tool.input_placeholder}
                    rows={4}
                    className="w-full border border-slate-300 rounded-xl px-4 py-3 text-slate-700 focus:outline-none focus:ring-2 focus:ring-red-400 focus:border-transparent resize-none"
                  />
                </div>
              </div>

              <Button
                onClick={detect}
                disabled={!ingredients.trim()}
                className="w-full bg-red-600 hover:bg-red-700 text-white py-3 disabled:opacity-50"
              >
                <ShieldAlert className="w-4 h-4 mr-2" />
                {tool.detect}
              </Button>
            </div>

            {/* Results */}
            {detected !== null && (
              <div className="mt-6 bg-white border border-slate-200 rounded-2xl shadow-sm p-6 md:p-8">
                <h2 className="text-lg font-bold text-slate-800 mb-4">{tool.result_title}</h2>

                {detected.length === 0 ? (
                  <div className="flex items-center gap-3 bg-green-50 border border-green-200 rounded-xl p-4 mb-4">
                    <CheckCircle className="w-6 h-6 text-green-500 flex-shrink-0" />
                    <span className="text-green-800 font-medium">{tool.no_allergens}</span>
                  </div>
                ) : (
                  <>
                    <p className="text-sm text-slate-500 mb-3">{tool.allergens_found}: <strong className="text-red-700">{detected.length}</strong></p>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
                      {detected.map((a: Allergen) => (
                        <div key={a.id} className="flex items-start gap-3 bg-red-50 border border-red-200 rounded-xl p-3">
                          <span className="text-2xl flex-shrink-0">{a.emoji}</span>
                          <div>
                            <p className="font-semibold text-red-800 text-sm">{a.name}</p>
                            <p className="text-xs text-slate-500">{a.description}</p>
                          </div>
                        </div>
                      ))}
                    </div>
                  </>
                )}

                <div className="bg-amber-50 border border-amber-200 rounded-xl p-3 mb-4 text-xs text-amber-800">
                  {tool.warning}<br />
                  <span className="text-slate-500">{tool.legal_note}</span>
                </div>

                <div className="flex flex-col sm:flex-row gap-3">
                  <Button
                    onClick={copySheet}
                    variant="outline"
                    className="border-slate-300 text-slate-700 hover:bg-slate-50 flex-1"
                  >
                    {copied ? <CheckCircle className="w-4 h-4 mr-2 text-green-500" /> : <Copy className="w-4 h-4 mr-2" />}
                    {copied ? tool.copied : tool.copy}
                  </Button>
                  <Button onClick={reset} variant="outline" className="border-slate-300 text-slate-600 flex-1">
                    <RotateCcw className="w-4 h-4 mr-2" />
                    {tool.reset}
                  </Button>
                </div>

                <Button
                  onClick={downloadPDF}
                  className="w-full bg-red-700 hover:bg-red-800 text-white font-semibold mt-1"
                >
                  <FileDown className="w-4 h-4 mr-2" />
                  {tool.pdf_download}
                </Button>

                <div className="mt-6 pt-6 border-t border-slate-100 text-center">
                  <p className="text-slate-700 font-medium mb-3">{tool.cta_after}</p>
                  <Button asChild className="bg-red-600 hover:bg-red-700 text-white">
                    <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                      {tool.try_free} <ArrowRight className="w-4 h-4 ml-1" />
                    </a>
                  </Button>
                </div>
              </div>
            )}
          </div>
        </section>

        {/* Allergen reference list */}
        <section className="py-12 px-4 bg-slate-50">
          <div className="max-w-4xl mx-auto">
            <h2 className="text-2xl font-bold text-slate-800 mb-2 text-center">
              {allergensSection?.title}
            </h2>
            <p className="text-center text-slate-500 text-sm mb-8">{allergensSection?.subtitle}</p>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-3">
              {Array.isArray(allergens) && allergens.map((a: Allergen) => (
                <div key={a.id} className="bg-white rounded-xl p-3 text-center shadow-sm border border-slate-100">
                  <div className="text-2xl mb-1">{a.emoji}</div>
                  <p className="text-xs font-semibold text-slate-700">{a.name}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* How it works */}
        {howItWorks && (
          <section className="py-12 px-4">
            <div className="max-w-4xl mx-auto">
              <h2 className="text-2xl font-bold text-center text-slate-800 mb-8">{howItWorks.title}</h2>
              <div className="grid md:grid-cols-3 gap-6">
                {Array.isArray(howItWorks.steps) && howItWorks.steps.map((step: { step: string; title: string; description: string }, i: number) => (
                  <div key={i} className="bg-red-50 rounded-xl p-6 text-center">
                    <div className="w-10 h-10 bg-red-100 text-red-700 rounded-full flex items-center justify-center text-lg font-bold mx-auto mb-3">
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
          <section className="py-12 px-4 bg-slate-50">
            <div className="max-w-4xl mx-auto">
              <h2 className="text-2xl font-bold text-center text-slate-800 mb-8">{benefits.title}</h2>
              <div className="grid md:grid-cols-2 gap-4">
                {Array.isArray(benefits.items) && benefits.items.map((item: string, i: number) => (
                  <div key={i} className="flex items-start gap-3 p-4 bg-white rounded-xl shadow-sm">
                    <CheckCircle className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                    <span className="text-slate-700 text-sm">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        <PricingPlans toolKey="toolAlergenos" />

        {/* FAQ */}
        {Array.isArray(faqItems) && faqItems.length > 0 && (
          <section className="py-12 px-4 bg-slate-50">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-2xl font-bold text-slate-800 mb-8 text-center">
                {t('toolAlergenos.faq_section.title')}
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

        <OtherFreeTools excludeIndex={1} />

        {/* Final CTA */}
        {ctaSection && (
          <section className="py-16 px-4">
            <div className="max-w-3xl mx-auto text-center">
              <h2 className="text-2xl md:text-3xl font-bold text-slate-900 mb-4">{ctaSection.title}</h2>
              <p className="text-slate-600 mb-8 text-lg">{ctaSection.subtitle}</p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <Button asChild size="lg" className="bg-red-600 hover:bg-red-700 text-white px-8">
                  <a href={getAppUrl()} target="_blank" rel="noopener noreferrer">
                    {ctaSection.primary} <ArrowRight className="w-4 h-4 ml-2" />
                  </a>
                </Button>
                <Button variant="outline" asChild size="lg" className="border-red-300 text-red-700 hover:bg-red-50 px-8">
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
