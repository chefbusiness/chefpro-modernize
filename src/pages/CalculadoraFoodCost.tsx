import { useState } from 'react';
import { Helmet } from 'react-helmet-async';
import { useTranslation } from 'react-i18next';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Calculator, Plus, Trash2, ArrowRight, CheckCircle, ChefHat } from 'lucide-react';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import WhatsAppFloatingButton from '@/components/WhatsAppFloatingButton';
import HeroSocialProof from '@/components/HeroSocialProof';
import { useLanguage } from '@/hooks/useLanguage';

const APP_URL = 'https://app.aichef.pro';
const SITE_URL = 'https://aichef.pro';

const LANG_SLUGS: Record<string, string> = {
  es: 'calculadora-food-cost-restaurante',
  en: 'en/food-cost-calculator-restaurant',
  fr: 'fr/calculateur-food-cost-restaurant',
  de: 'de/food-cost-rechner-restaurant',
  it: 'it/calcolatore-food-cost-ristorante',
  pt: 'pt/calculadora-food-cost-restaurante',
  nl: 'nl/food-cost-calculator-restaurant',
};

interface Ingredient {
  id: number;
  name: string;
  qty: string;   // grams
  cost: string;  // €/kg
}

interface CalcResult {
  totalCost: number;
  costPerPortion: number;
  foodCostPct: number;
  grossMargin: number;
  status: 'ok' | 'warn' | 'bad';
}

export default function CalculadoraFoodCost() {
  const { t } = useTranslation();
  const { currentLanguage, getAppUrl } = useLanguage();

  const k = (key: string) => t(`toolFoodCost.${key}`, { returnObjects: true });
  const s = (key: string) => t(`toolFoodCost.${key}`) as string;

  const lang = currentLanguage;
  const canonicalSlug = LANG_SLUGS[lang] || LANG_SLUGS.es;
  const canonicalUrl = lang === 'es'
    ? `${SITE_URL}/${canonicalSlug}`
    : `${SITE_URL}/${canonicalSlug}`;

  // Calculator state
  const [dishName, setDishName] = useState('');
  const [portions, setPortions] = useState('4');
  const [salePrice, setSalePrice] = useState('');
  const [ingredients, setIngredients] = useState<Ingredient[]>([
    { id: 1, name: '', qty: '', cost: '' },
    { id: 2, name: '', qty: '', cost: '' },
    { id: 3, name: '', qty: '', cost: '' },
  ]);
  const [result, setResult] = useState<CalcResult | null>(null);

  const addIngredient = () => {
    setIngredients(prev => [
      ...prev,
      { id: Date.now(), name: '', qty: '', cost: '' }
    ]);
  };

  const removeIngredient = (id: number) => {
    setIngredients(prev => prev.filter(i => i.id !== id));
  };

  const updateIngredient = (id: number, field: keyof Ingredient, value: string) => {
    setIngredients(prev => prev.map(i => i.id === id ? { ...i, [field]: value } : i));
  };

  const calculate = () => {
    const p = parseFloat(portions) || 1;
    const sp = parseFloat(salePrice) || 0;

    let totalCost = 0;
    for (const ing of ingredients) {
      const qty = parseFloat(ing.qty) || 0;   // grams
      const cost = parseFloat(ing.cost) || 0;  // €/kg
      totalCost += (qty / 1000) * cost;
    }

    const costPerPortion = p > 0 ? totalCost / p : 0;
    const foodCostPct = sp > 0 ? (costPerPortion / sp) * 100 : 0;
    const grossMargin = sp - costPerPortion;

    let status: 'ok' | 'warn' | 'bad' = 'ok';
    if (foodCostPct > 35) status = 'bad';
    else if (foodCostPct > 30) status = 'warn';

    setResult({ totalCost, costPerPortion, foodCostPct, grossMargin, status });
  };

  const reset = () => {
    setDishName('');
    setPortions('4');
    setSalePrice('');
    setIngredients([
      { id: 1, name: '', qty: '', cost: '' },
      { id: 2, name: '', qty: '', cost: '' },
      { id: 3, name: '', qty: '', cost: '' },
    ]);
    setResult(null);
  };

  const steps = k('how_it_works.steps') as Array<{ step: string; title: string; description: string }>;
  const benefits = k('benefits.items') as string[];
  const faqs = k('faq') as Array<{ question: string; answer: string }>;
  const plans = k('pricing.plans') as Array<{ name: string; price: string; uses: string; highlight: boolean }>;

  const statusText = result
    ? result.status === 'ok'
      ? s('tool.status_ok')
      : result.status === 'warn'
      ? s('tool.status_warn')
      : s('tool.status_bad')
    : '';

  const statusColor = result
    ? result.status === 'ok'
      ? 'bg-green-50 border-green-200 text-green-800'
      : result.status === 'warn'
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
        <section className="relative overflow-hidden bg-gradient-to-br from-green-50 via-background to-emerald-50/30 py-16 lg:py-24">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <HeroSocialProof />
              <Badge className="mb-6 text-sm px-4 py-2 bg-green-100 text-green-800 border-green-200">
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
                  className="bg-green-600 hover:bg-green-700 text-white"
                  onClick={() => document.getElementById('herramienta')?.scrollIntoView({ behavior: 'smooth' })}
                >
                  <Calculator className="mr-2 h-5 w-5" />
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
            <div className="max-w-2xl mx-auto">
              <Card className="border-2 border-green-200 shadow-lg">
                <CardHeader className="bg-green-50 border-b border-green-100">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-green-100 rounded-xl flex items-center justify-center">
                      <Calculator className="h-5 w-5 text-green-700" />
                    </div>
                    <CardTitle className="text-xl text-green-900">{s('tool.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent className="p-6 space-y-6">
                  {/* Dish name + portions + sale price */}
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div className="sm:col-span-1">
                      <label className="text-sm font-medium text-foreground block mb-1">
                        {s('tool.dish_name_label')}
                      </label>
                      <Input
                        value={dishName}
                        onChange={e => setDishName(e.target.value)}
                        placeholder={s('tool.dish_name_placeholder')}
                      />
                    </div>
                    <div>
                      <label className="text-sm font-medium text-foreground block mb-1">
                        {s('tool.portions_label')}
                      </label>
                      <Input
                        type="number"
                        min="1"
                        value={portions}
                        onChange={e => setPortions(e.target.value)}
                        placeholder="4"
                      />
                    </div>
                    <div>
                      <label className="text-sm font-medium text-foreground block mb-1">
                        {s('tool.sale_price_label')}
                      </label>
                      <Input
                        type="number"
                        min="0"
                        step="0.01"
                        value={salePrice}
                        onChange={e => setSalePrice(e.target.value)}
                        placeholder="12.00"
                      />
                    </div>
                  </div>

                  {/* Ingredients */}
                  <div>
                    <h3 className="text-sm font-semibold text-foreground mb-3">{s('tool.ingredients_title')}</h3>
                    <div className="space-y-2">
                      <div className="grid grid-cols-12 gap-2 text-xs text-muted-foreground px-1 mb-1">
                        <span className="col-span-5">{s('tool.ingredient_name')}</span>
                        <span className="col-span-3">{s('tool.ingredient_qty')}</span>
                        <span className="col-span-3">{s('tool.ingredient_cost')}</span>
                        <span className="col-span-1"></span>
                      </div>
                      {ingredients.map(ing => (
                        <div key={ing.id} className="grid grid-cols-12 gap-2 items-center">
                          <Input
                            className="col-span-5 h-9 text-sm"
                            value={ing.name}
                            onChange={e => updateIngredient(ing.id, 'name', e.target.value)}
                            placeholder="Ej: Arroz"
                          />
                          <Input
                            className="col-span-3 h-9 text-sm"
                            type="number"
                            min="0"
                            value={ing.qty}
                            onChange={e => updateIngredient(ing.id, 'qty', e.target.value)}
                            placeholder="200"
                          />
                          <Input
                            className="col-span-3 h-9 text-sm"
                            type="number"
                            min="0"
                            step="0.01"
                            value={ing.cost}
                            onChange={e => updateIngredient(ing.id, 'cost', e.target.value)}
                            placeholder="2.50"
                          />
                          <Button
                            variant="ghost"
                            size="icon"
                            className="col-span-1 h-9 w-9 text-muted-foreground hover:text-red-500"
                            onClick={() => removeIngredient(ing.id)}
                          >
                            <Trash2 className="h-4 w-4" />
                          </Button>
                        </div>
                      ))}
                    </div>
                    <Button
                      variant="outline"
                      size="sm"
                      className="mt-3 text-green-700 border-green-300 hover:bg-green-50"
                      onClick={addIngredient}
                    >
                      <Plus className="h-4 w-4 mr-1" />
                      {s('tool.add_ingredient')}
                    </Button>
                  </div>

                  {/* Buttons */}
                  <div className="flex gap-3">
                    <Button
                      className="flex-1 bg-green-600 hover:bg-green-700 text-white"
                      onClick={calculate}
                    >
                      <Calculator className="mr-2 h-4 w-4" />
                      {s('tool.calculate')}
                    </Button>
                    {result && (
                      <Button variant="outline" onClick={reset} className="px-4">
                        {s('tool.reset')}
                      </Button>
                    )}
                  </div>

                  {/* Result */}
                  {result && (
                    <div className="space-y-4 pt-2">
                      <div className={`rounded-xl border-2 p-4 ${statusColor}`}>
                        <p className="font-semibold text-sm">{statusText}</p>
                      </div>

                      <div className="grid grid-cols-2 gap-3">
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.total_cost_label')}</p>
                          <p className="text-xl font-bold text-foreground">€{result.totalCost.toFixed(2)}</p>
                        </div>
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.cost_per_portion_label')}</p>
                          <p className="text-xl font-bold text-foreground">€{result.costPerPortion.toFixed(2)}</p>
                        </div>
                        <div className={`rounded-xl p-3 text-center border-2 ${
                          result.status === 'ok' ? 'bg-green-50 border-green-200' :
                          result.status === 'warn' ? 'bg-yellow-50 border-yellow-200' :
                          'bg-red-50 border-red-200'
                        }`}>
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.food_cost_pct_label')}</p>
                          <p className={`text-2xl font-bold ${
                            result.status === 'ok' ? 'text-green-700' :
                            result.status === 'warn' ? 'text-yellow-700' :
                            'text-red-700'
                          }`}>{result.foodCostPct.toFixed(1)}%</p>
                        </div>
                        <div className="bg-muted/40 rounded-xl p-3 text-center">
                          <p className="text-xs text-muted-foreground mb-1">{s('tool.gross_margin_label')}</p>
                          <p className={`text-xl font-bold ${result.grossMargin >= 0 ? 'text-emerald-600' : 'text-red-600'}`}>
                            €{result.grossMargin.toFixed(2)}
                          </p>
                        </div>
                      </div>

                      <p className="text-xs text-muted-foreground bg-green-50 rounded-lg p-3 border border-green-100">
                        {s('tool.tip')}
                      </p>

                      <div className="text-center pt-2">
                        <p className="text-sm text-muted-foreground mb-3">{s('tool.cta_after')}</p>
                        <Button
                          className="bg-green-600 hover:bg-green-700 text-white"
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
                  <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <span className="text-xl font-bold text-green-700">{step.step}</span>
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
                        <CheckCircle className="h-5 w-5 text-green-500 mt-0.5 flex-shrink-0" />
                        <span className="text-muted-foreground">{item}</span>
                      </li>
                    ))}
                  </ul>
                </div>
                <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-8 border border-green-100">
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

        {/* CTA Final */}
        <section className="py-20 bg-gradient-to-br from-green-600 via-green-500 to-emerald-400">
          <div className="container mx-auto px-4 text-center text-white">
            <ChefHat className="h-12 w-12 mx-auto mb-6 opacity-80" />
            <h2 className="text-3xl font-bold mb-4">{s('cta_section.title')}</h2>
            <p className="text-lg opacity-90 mb-8 max-w-2xl mx-auto">{s('cta_section.subtitle')}</p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button
                size="lg"
                className="bg-white text-green-700 hover:bg-green-50"
                onClick={() => window.open(getAppUrl(lang), '_blank')}
              >
                {s('cta_section.primary')}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-white text-white hover:bg-white/20"
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
