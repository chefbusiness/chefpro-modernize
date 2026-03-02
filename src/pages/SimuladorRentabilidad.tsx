import { useState } from 'react';
import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import * as XLSX from 'xlsx';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { TrendingUp, ArrowRight, CheckCircle, ChefHat, Download } from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import HeroSocialProof from '@/components/HeroSocialProof';
import OtherFreeTools from '@/components/OtherFreeTools';
import { useLanguage } from '@/hooks/useLanguage';

const SITE_URL = 'https://aichef.pro';

const LANG_SLUGS: Record<string, string> = {
  es: 'simulador-rentabilidad-restaurante',
  en: 'en/restaurant-profit-simulator',
  fr: 'fr/simulateur-rentabilite-restaurant',
  de: 'de/rentabilitaet-simulator-restaurant',
  it: 'it/simulatore-redditivita-ristorante',
  pt: 'pt/simulador-rentabilidade-restaurante',
  nl: 'nl/winstgevendheid-simulator-restaurant',
};

interface SimResult {
  monthlyRevenue: number;
  variableCosts: number;
  totalCosts: number;
  netProfit: number;
  profitMargin: number;
  breakEvenCovers: number;
  status: 'profitable' | 'breakeven' | 'loss';
}

export default function SimuladorRentabilidad() {
  const { t } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();

  const k = (key: string) => t(`toolRentabilidad.${key}`, { returnObjects: true });
  const s = (key: string) => t(`toolRentabilidad.${key}`) as string;

  const lang = currentLanguage;
  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl = lang === 'es'
    ? `${SITE_URL}/${canonicalSlug}`
    : `${SITE_URL}/${canonicalSlug}`;

  // Simulator state
  const [covers, setCovers] = useState('');
  const [ticket, setTicket] = useState('');
  const [fixedCosts, setFixedCosts] = useState('');
  const [variablePct, setVariablePct] = useState('');
  const [result, setResult] = useState<SimResult | null>(null);

  const calculate = () => {
    const c = parseFloat(covers) || 0;
    const t = parseFloat(ticket) || 0;
    const fc = parseFloat(fixedCosts) || 0;
    const vp = parseFloat(variablePct) || 0;

    const monthlyRevenue = c * t;
    const variableCosts = monthlyRevenue * (vp / 100);
    const totalCosts = fc + variableCosts;
    const netProfit = monthlyRevenue - totalCosts;
    const profitMargin = monthlyRevenue > 0 ? (netProfit / monthlyRevenue) * 100 : 0;

    // Break-even: fc / (ticket * (1 - vp/100))
    const contributionPerCover = t * (1 - vp / 100);
    const breakEvenCovers = contributionPerCover > 0 ? Math.ceil(fc / contributionPerCover) : 0;

    let status: 'profitable' | 'breakeven' | 'loss' = 'profitable';
    if (netProfit < 0) status = 'loss';
    else if (profitMargin < 3) status = 'breakeven';

    setResult({ monthlyRevenue, variableCosts, totalCosts, netProfit, profitMargin, breakEvenCovers, status });
  };

  const reset = () => {
    setCovers('');
    setTicket('');
    setFixedCosts('');
    setVariablePct('');
    setResult(null);
  };

  const downloadExcel = () => {
    if (!result) return;

    const today = new Date().toLocaleDateString(lang, { year: 'numeric', month: '2-digit', day: '2-digit' });
    const coversVal   = parseFloat(covers)      || 0;
    const ticketVal   = parseFloat(ticket)      || 0;
    const fixedVal    = parseFloat(fixedCosts)  || 0;
    const varPctVal   = parseFloat(variablePct) || 0;

    // Fixed row positions (1-indexed)
    const ROW_COVERS   = 5;   // B5 — editable
    const ROW_TICKET   = 6;   // B6 — editable
    const ROW_FIXED    = 7;   // B7 — editable
    const ROW_VARPCT   = 8;   // B8 — editable

    const RES_HEADER   = 10;
    const ROW_REVENUE  = 11;  // =B5*B6
    const ROW_VARCOSTS = 12;  // =B11*(B8/100)
    const ROW_TOTAL    = 13;  // =B7+B12
    const ROW_PROFIT   = 14;  // =B11-B13
    const ROW_MARGIN   = 15;  // =IF(B11>0,(B14/B11)*100,0)
    const ROW_BREAKEVEN= 16;  // =IF(B6*(1-B8/100)>0,CEILING(B7/(B6*(1-B8/100)),1),0)

    const SCEN_HEADER  = 18;
    const SCEN_COLS    = 19;
    const SCEN_LOW     = 20;  // −20%
    const SCEN_BASE    = 21;  // actual
    const SCEN_MID     = 22;  // +20%
    const SCEN_HIGH    = 23;  // +40%
    const FOOTER_ROW   = 25;

    // Build worksheet as array-of-arrays for initial population
    const rows: (string | number)[][] = [
      // Row 1: title
      ['AI Chef Pro — ' + s('tool.title')],
      // Row 2: URL
      ['aichef.pro'],
      // Row 3: empty
      [],
      // Row 4: inputs section header
      [s('tool.export_inputs_label')],
      // Row 5: covers
      [s('tool.covers_label'), coversVal],
      // Row 6: ticket
      [s('tool.ticket_label'), ticketVal],
      // Row 7: fixed costs
      [s('tool.fixed_costs_label'), fixedVal],
      // Row 8: variable %
      [s('tool.variable_pct_label'), varPctVal],
      // Row 9: empty
      [],
      // Row 10: results section header
      [s('tool.export_results_label')],
      // Row 11: monthly revenue
      [s('tool.monthly_revenue_label'), result.monthlyRevenue],
      // Row 12: variable costs
      [s('tool.variable_costs_label'), result.variableCosts],
      // Row 13: total costs
      [s('tool.total_costs_label'), result.totalCosts],
      // Row 14: net profit
      [s('tool.net_profit_label'), result.netProfit],
      // Row 15: profit margin
      [s('tool.profit_margin_label'), result.profitMargin],
      // Row 16: break-even
      [s('tool.breakeven_label'), result.breakEvenCovers],
      // Row 17: empty
      [],
      // Row 18: scenarios section header
      [s('tool.export_scenarios_label')],
      // Row 19: column headers
      [s('tool.export_scenario_header'), s('tool.export_scenario_covers'), s('tool.export_scenario_revenue'), s('tool.export_scenario_profit'), s('tool.export_scenario_margin')],
      // Rows 20-23: scenario data (placeholder, replaced by formulas)
      [s('tool.export_scenario_low'),  0, 0, 0, 0],
      [s('tool.export_scenario_base'), 0, 0, 0, 0],
      [s('tool.export_scenario_mid'),  0, 0, 0, 0],
      [s('tool.export_scenario_high'), 0, 0, 0, 0],
      // Row 24: empty
      [],
      // Row 25: footer
      [s('tool.export_date_label') + ': ' + today + ' | ' + s('tool.export_generated_by')],
    ];

    const ws = XLSX.utils.aoa_to_sheet(rows);

    // --- Inject formulas into results section ---
    // Revenue: B11 = B5 * B6
    ws[`B${ROW_REVENUE}`]  = { t: 'n', v: result.monthlyRevenue,   f: `=B${ROW_COVERS}*B${ROW_TICKET}` };
    // Variable costs: B12 = B11 * (B8/100)
    ws[`B${ROW_VARCOSTS}`] = { t: 'n', v: result.variableCosts,    f: `=B${ROW_REVENUE}*(B${ROW_VARPCT}/100)` };
    // Total costs: B13 = B7 + B12
    ws[`B${ROW_TOTAL}`]    = { t: 'n', v: result.totalCosts,       f: `=B${ROW_FIXED}+B${ROW_VARCOSTS}` };
    // Net profit: B14 = B11 - B13
    ws[`B${ROW_PROFIT}`]   = { t: 'n', v: result.netProfit,        f: `=B${ROW_REVENUE}-B${ROW_TOTAL}` };
    // Profit margin %: B15 = IF(B11>0,(B14/B11)*100,0)
    ws[`B${ROW_MARGIN}`]   = { t: 'n', v: result.profitMargin,     f: `=IF(B${ROW_REVENUE}>0,(B${ROW_PROFIT}/B${ROW_REVENUE})*100,0)` };
    // Break-even covers: B16
    ws[`B${ROW_BREAKEVEN}`]= { t: 'n', v: result.breakEvenCovers,  f: `=IF(B${ROW_TICKET}*(1-B${ROW_VARPCT}/100)>0,CEILING(B${ROW_FIXED}/(B${ROW_TICKET}*(1-B${ROW_VARPCT}/100)),1),0)` };

    // --- Inject scenario formulas ---
    // Each scenario: covers (C), revenue (D=C*B6), variable costs (E=D*(B8/100)), total (F=B7+E), profit (G=D-F), margin (H=IF(D>0,(G/D)*100,0))
    // But we only have 5 columns (A-E) → A=label, B=covers, C=revenue, D=profit, E=margin
    const scenRows: { row: number; factor: string }[] = [
      { row: SCEN_LOW,  factor: '0.8'  },
      { row: SCEN_BASE, factor: '1'    },
      { row: SCEN_MID,  factor: '1.2'  },
      { row: SCEN_HIGH, factor: '1.4'  },
    ];

    for (const { row, factor } of scenRows) {
      // B = covers scenario
      const bRef = `ROUND(B${ROW_COVERS}*${factor},0)`;
      // C = revenue = covers * ticket
      const cRef = `${bRef}*B${ROW_TICKET}`;
      // var costs = revenue * (B8/100)
      // total = B7 + varCosts
      // profit = revenue - total = revenue - B7 - revenue*(B8/100) = revenue*(1-B8/100) - B7
      const profitF = `(${cRef})*(1-B${ROW_VARPCT}/100)-B${ROW_FIXED}`;
      const marginF = `IF((${cRef})>0,(${profitF})/(${cRef})*100,0)`;

      const scenCovers  = Math.round(coversVal * parseFloat(factor));
      const scenRevenue = scenCovers * ticketVal;
      const scenProfit  = scenRevenue * (1 - varPctVal / 100) - fixedVal;
      const scenMargin  = scenRevenue > 0 ? (scenProfit / scenRevenue) * 100 : 0;

      ws[XLSX.utils.encode_cell({ r: row - 1, c: 1 })] = { t: 'n', v: scenCovers,  f: bRef };
      ws[XLSX.utils.encode_cell({ r: row - 1, c: 2 })] = { t: 'n', v: scenRevenue, f: cRef };
      ws[XLSX.utils.encode_cell({ r: row - 1, c: 3 })] = { t: 'n', v: scenProfit,  f: profitF };
      ws[XLSX.utils.encode_cell({ r: row - 1, c: 4 })] = { t: 'n', v: scenMargin,  f: marginF };
    }

    // Column widths
    ws['!cols'] = [{ wch: 32 }, { wch: 18 }, { wch: 18 }, { wch: 20 }, { wch: 14 }];

    // Update range to include all rows
    ws['!ref'] = XLSX.utils.encode_range({ s: { r: 0, c: 0 }, e: { r: FOOTER_ROW - 1, c: 4 } });

    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, s('tool.export_sheet_name'));

    const date = new Date().toISOString().slice(0, 10);
    XLSX.writeFile(wb, `${s('tool.export_filename')}-${date}.xlsx`);
  };

  const steps = k('how_it_works.steps') as Array<{ step: string; title: string; description: string }>;
  const benefits = k('benefits.items') as string[];
  const faqs = k('faq') as Array<{ question: string; answer: string }>;
  const plans = k('pricing.plans') as Array<{ name: string; price: string; uses: string; highlight: boolean }>;

  const statusText = result
    ? result.status === 'profitable'
      ? s('tool.status_profitable')
      : result.status === 'breakeven'
      ? s('tool.status_breakeven')
      : s('tool.status_loss')
    : '';

  const statusColor = result
    ? result.status === 'profitable'
      ? 'bg-green-50 border-green-200 text-green-800'
      : result.status === 'breakeven'
      ? 'bg-yellow-50 border-yellow-200 text-yellow-800'
      : 'bg-red-50 border-red-200 text-red-800'
    : '';

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: 'AI Chef Pro', item: SITE_URL },
      { '@type': 'ListItem', position: 2, name: 'Herramientas Gratuitas', item: `${SITE_URL}/herramientas-gratuitas` },
      { '@type': 'ListItem', position: 3, name: s('breadcrumb'), item: canonicalUrl },
    ],
  };

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map(f => ({
      '@type': 'Question',
      name: f.question,
      acceptedAnswer: { '@type': 'Answer', text: f.answer },
    })),
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
        <script type="application/ld+json">{JSON.stringify(faqSchema)}</script>
      </Helmet>

      <ModernHeader />

      <main>
        {/* Hero */}
        <section className="relative overflow-hidden bg-gradient-to-br from-yellow-50 via-background to-amber-50/30 py-16 lg:py-24">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2 bg-yellow-100 text-yellow-800 border-yellow-200">
                {s('hero.badge')}
              </Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl mb-4 text-balance">
                {s('hero.h1')}
              </h1>
              <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto text-balance">
                {s('hero.subtitle')}
              </p>
              <div className="flex flex-col sm:flex-row gap-3 justify-center">
                <Button
                  size="lg"
                  className="bg-yellow-500 hover:bg-yellow-600 text-white"
                  onClick={() => document.getElementById('herramienta')?.scrollIntoView({ behavior: 'smooth' })}
                >
                  <TrendingUp className="mr-2 h-5 w-5" />
                  {s('hero.cta_tool')}
                </Button>
                <Button
                  size="lg"
                  variant="outline"
                  onClick={() => window.open(`${getAppUrl(lang)}/pricing`, '_blank')}
                >
                  {s('hero.cta_premium')}
                </Button>
              </div>
            </div>
          </div>
        </section>

        {/* TOOL SECTION */}
        <section id="herramienta" className="py-16 bg-muted/20">
          <div className="container mx-auto px-4">
            <div className="max-w-xl mx-auto">
              <Card className="border-2 border-yellow-200 shadow-lg">
                <CardHeader className="bg-yellow-50 border-b border-yellow-100">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-yellow-100 rounded-xl flex items-center justify-center">
                      <TrendingUp className="h-5 w-5 text-yellow-700" />
                    </div>
                    <CardTitle className="text-xl text-yellow-900">{s('tool.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent className="p-6 space-y-5">
                  {/* Covers */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label className="text-sm font-medium text-foreground block mb-1">
                        {s('tool.covers_label')}
                      </label>
                      <Input
                        type="number"
                        min="0"
                        value={covers}
                        onChange={e => setCovers(e.target.value)}
                        placeholder="300"
                      />
                    </div>
                    <div>
                      <label className="text-sm font-medium text-foreground block mb-1">
                        {s('tool.ticket_label')}
                      </label>
                      <Input
                        type="number"
                        min="0"
                        step="0.50"
                        value={ticket}
                        onChange={e => setTicket(e.target.value)}
                        placeholder="28.00"
                      />
                    </div>
                  </div>

                  {/* Fixed costs */}
                  <div>
                    <label className="text-sm font-medium text-foreground block mb-1">
                      {s('tool.fixed_costs_label')}
                    </label>
                    <Input
                      type="number"
                      min="0"
                      value={fixedCosts}
                      onChange={e => setFixedCosts(e.target.value)}
                      placeholder="4500"
                    />
                    <p className="text-xs text-muted-foreground mt-1">{s('tool.fixed_costs_hint')}</p>
                  </div>

                  {/* Variable costs */}
                  <div>
                    <label className="text-sm font-medium text-foreground block mb-1">
                      {s('tool.variable_pct_label')}
                    </label>
                    <div className="flex items-center gap-2">
                      <Input
                        type="number"
                        min="0"
                        max="100"
                        value={variablePct}
                        onChange={e => setVariablePct(e.target.value)}
                        placeholder="35"
                        className="flex-1"
                      />
                      <span className="text-sm font-medium text-muted-foreground">%</span>
                    </div>
                    <p className="text-xs text-muted-foreground mt-1">{s('tool.variable_pct_hint')}</p>
                  </div>

                  {/* Buttons */}
                  <div className="flex gap-3">
                    <Button
                      className="flex-1 bg-yellow-500 hover:bg-yellow-600 text-white"
                      onClick={calculate}
                    >
                      <TrendingUp className="mr-2 h-4 w-4" />
                      {s('tool.calculate')}
                    </Button>
                    {result && (
                      <Button variant="outline" onClick={reset} className="px-4">
                        {s('tool.reset')}
                      </Button>
                    )}
                  </div>

                  {/* Download Excel — shown only after calculation */}
                  {result && (
                    <Button
                      className="w-full bg-amber-600 hover:bg-amber-700 text-white font-semibold"
                      onClick={downloadExcel}
                    >
                      <Download className="mr-2 h-4 w-4" />
                      {s('tool.export_excel')}
                    </Button>
                  )}

                  {/* Result */}
                  {result && (
                    <div className="space-y-4 pt-2">
                      <div className={`rounded-xl border-2 p-4 ${statusColor}`}>
                        <p className="font-semibold text-sm">{statusText}</p>
                      </div>

                      <div className="grid grid-cols-2 gap-3">
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.monthly_revenue_label')}</p>
                          <p className="text-xl font-bold text-foreground">€{result.monthlyRevenue.toLocaleString('es', { minimumFractionDigits: 0 })}</p>
                        </div>
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.variable_costs_label')}</p>
                          <p className="text-xl font-bold text-foreground">€{result.variableCosts.toLocaleString('es', { minimumFractionDigits: 0 })}</p>
                        </div>
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.total_costs_label')}</p>
                          <p className="text-xl font-bold text-foreground">€{result.totalCosts.toLocaleString('es', { minimumFractionDigits: 0 })}</p>
                        </div>
                        <div className={`rounded-xl p-3 text-center border-2 ${
                          result.status === 'profitable' ? 'bg-green-50 border-green-200' :
                          result.status === 'breakeven' ? 'bg-yellow-50 border-yellow-200' :
                          'bg-red-50 border-red-200'
                        }`}>
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.net_profit_label')}</p>
                          <p className={`text-2xl font-bold ${
                            result.netProfit >= 0 ? 'text-green-700' : 'text-red-700'
                          }`}>
                            {result.netProfit >= 0 ? '+' : ''}€{result.netProfit.toLocaleString('es', { minimumFractionDigits: 0 })}
                          </p>
                        </div>
                      </div>

                      {/* Margin + Break-even */}
                      <div className="grid grid-cols-2 gap-3">
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.profit_margin_label')}</p>
                          <p className={`text-xl font-bold ${result.profitMargin >= 0 ? 'text-foreground' : 'text-red-700'}`}>
                            {result.profitMargin.toFixed(1)}%
                          </p>
                        </div>
                        <div className="bg-amber-50 border-2 border-amber-200 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.breakeven_label')}</p>
                          <p className="text-xl font-bold text-amber-700">{result.breakEvenCovers.toLocaleString()}</p>
                          <p className="text-xs text-muted-foreground mt-0.5">{s('tool.breakeven_suffix')}</p>
                        </div>
                      </div>

                      <div className="text-center pt-2">
                        <p className="text-sm text-muted-foreground mb-3">{s('tool.cta_after')}</p>
                        <Button
                          className="bg-yellow-500 hover:bg-yellow-600 text-white"
                          onClick={() => window.open(getAppUrl(lang), '_blank')}
                        >
                          {s('cta_section.primary')}
                          <ArrowRight className="ml-2 h-4 w-4" />
                        </Button>
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Cómo funciona */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12 max-w-2xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">{s('how_it_works.title')}</h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
              {steps.map((step, i) => (
                <div key={i} className="text-center">
                  <div className="w-12 h-12 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <span className="text-xl font-bold text-yellow-700">{step.step}</span>
                  </div>
                  <h3 className="font-semibold text-foreground mb-2">{step.title}</h3>
                  <p className="text-sm text-muted-foreground">{step.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Beneficios */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                <div>
                  <h2 className="text-3xl font-bold text-foreground mb-8">{s('benefits.title')}</h2>
                  <ul className="space-y-4">
                    {benefits.map((item, i) => (
                      <li key={i} className="flex items-start gap-3">
                        <CheckCircle className="h-5 w-5 text-yellow-500 mt-0.5 flex-shrink-0" />
                        <span className="text-muted-foreground">{item}</span>
                      </li>
                    ))}
                  </ul>
                </div>
                <div className="bg-gradient-to-br from-yellow-50 to-amber-50 rounded-2xl p-8 border border-yellow-100">
                  <div className="flex items-center gap-1 mb-4">
                    {[...Array(5)].map((_, i) => (
                      <svg key={i} className="h-5 w-5 text-yellow-400 fill-yellow-400" viewBox="0 0 20 20">
                        <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                      </svg>
                    ))}
                  </div>
                  <p className="text-lg italic text-foreground mb-6">"{s('testimonial.quote')}"</p>
                  <div>
                    <p className="font-semibold">{s('testimonial.name')}</p>
                    <p className="text-sm text-muted-foreground">{s('testimonial.role')}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Pricing */}
        <section className="py-20 bg-gradient-to-b from-muted/20 to-muted/50">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold text-foreground mb-4">{s('pricing.title')}</h2>
            <p className="text-lg text-muted-foreground mb-12 max-w-2xl mx-auto">{s('pricing.subtitle')}</p>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto mb-10">
              {plans.map((plan, i) => (
                <Card key={i} className={`text-center relative ${plan.highlight ? 'ring-2 ring-amber-400 shadow-2xl scale-105 bg-gradient-to-b from-amber-50 to-white' : 'shadow-md bg-card'}`}>
                  {plan.highlight && <Badge className="absolute -top-3 left-1/2 -translate-x-1/2 bg-amber-400 text-amber-950 border-0">⭐ Popular</Badge>}
                  <CardHeader className="pt-6">
                    <CardTitle className={`text-lg ${plan.highlight ? 'text-amber-900' : ''}`}>{plan.name}</CardTitle>
                    <div className={`text-3xl font-bold ${plan.highlight ? 'text-amber-600' : 'text-primary'}`}>{plan.price}</div>
                    <div className="text-sm text-muted-foreground">{plan.uses}</div>
                  </CardHeader>
                  <CardContent>
                    <Button
                      className={`w-full ${plan.highlight ? 'btn-gold' : ''}`}
                      variant={plan.highlight ? 'default' : 'outline'}
                      onClick={() => window.open(`${getAppUrl(lang)}/pricing`, '_blank')}
                    >
                      {plan.highlight ? s('cta_section.primary') : s('cta_section.secondary')}
                    </Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* FAQ */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-12 text-center">{s('faq_section.title')}</h2>
              <div className="space-y-6">
                {faqs.map((item, i) => (
                  <div key={i} className="border-b pb-6">
                    <h3 className="text-lg font-semibold text-foreground mb-3">{item.question}</h3>
                    <p className="text-muted-foreground">{item.answer}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        <OtherFreeTools excludeIndex={3} />

        {/* CTA Final */}
        <section className="py-20 bg-gradient-to-br from-amber-500 via-amber-400 to-yellow-300">
          <div className="container mx-auto px-4 text-center text-amber-950">
            <ChefHat className="h-12 w-12 mx-auto mb-6 opacity-70" />
            <h2 className="text-3xl font-bold mb-4">{s('cta_section.title')}</h2>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">{s('cta_section.subtitle')}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button
                size="lg"
                className="bg-amber-950 text-amber-50 hover:bg-amber-900"
                onClick={() => window.open(getAppUrl(lang), '_blank')}
              >
                {s('cta_section.primary')}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-amber-900 text-amber-900 bg-white/30 hover:bg-white/50"
                onClick={() => window.open(`${getAppUrl(lang)}/pricing`, '_blank')}
              >
                {s('cta_section.secondary')}
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
