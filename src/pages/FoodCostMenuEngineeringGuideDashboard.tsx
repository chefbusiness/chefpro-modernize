import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  BookOpen, FileText, Calculator, BarChart3,
  Scale, Wine, Truck, Target, CalendarRange,
  GraduationCap, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Food Cost + Menu Engineering Guide (tienda EN) — COPIA TRADUCIDA de GuiaFoodCostDashboard.tsx (ES), mismas
// secciones y mismo molde de tarjeta; componentes compartidos con lang="en" como MobileBarBusinessPlanDashboard.tsx.
// Las claves (`key`) son las MISMAS que el ES guia-food-cost-ingenieria-menu, salvo el bonus de equivalencias, que es
// el COMÚN de la tienda EN ('equivalents-guide', dl/en-shared/), y coinciden con la entrada
// `food-cost-menu-engineering-guide` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza).
// Títulos = los de los ficheros EN (SPEC guia-food-cost-en §2). Venta cruzada: solo productos de la tienda EN.

const SECTIONS = [
  {
    title: 'Main Guide',
    templates: [
      { key: 'guia-pdf', icon: BookOpen, title: 'Complete Guide (PDF)', desc: '20 chapters, 94 pages, with tables built from the Excel tools.', ext: '.pdf' },
      { key: 'guia-docx', icon: FileText, title: 'Complete Guide (Editable DOCX)', desc: 'The same content in an editable format to annotate and adapt.', ext: '.docx' },
    ],
  },
  {
    title: 'Excel Tools (8)',
    templates: [
      { key: 'ficha-escandallo', icon: FileSpreadsheet, title: 'Recipe Cost Card', desc: 'Plate cost with trim loss line by line, target menu price with tax and an invoice & tax check.', ext: '.xlsx' },
      { key: 'rendimiento-mermas', icon: Scale, title: 'Yield and Trim Loss', desc: 'Yield test, cooking loss test and your own trim loss table.', ext: '.xlsx' },
      { key: 'precio-objetivo', icon: Calculator, title: 'Menu Pricing Calculator', desc: 'Four ways to set the menu price of each dish, and the food cost each one gives you.', ext: '.xlsx' },
      { key: 'matriz-multimetodo', icon: BarChart3, title: 'Menu Engineering Matrix', desc: 'Kasavana-Smith, Miller, Pavesic and Goal Value, with a comparison sheet that shows where they disagree.', ext: '.xlsx' },
      { key: 'simulador-multicanal', icon: Truck, title: 'Multichannel Repricing Simulator', desc: 'Dine-in, takeout and third-party delivery with commission, packaging and tax by channel.', ext: '.xlsx' },
      { key: 'carta-bebidas', icon: Wine, title: 'Beverage Menu and Beverage Cost', desc: 'Wines, beers, spirits and cocktails with cost per serving and margin.', ext: '.xlsx' },
      { key: 'cuadro-prime-cost', icon: Target, title: 'Prime Cost Dashboard', desc: 'Food cost and labor cost month by month, with a traffic light against your target.', ext: '.xlsx' },
      { key: 'plan-90-dias', icon: CalendarRange, title: '90-Day Action Plan', desc: 'Decisions with an owner and a date, a 13-week calendar and tracking KPIs.', ext: '.xlsx' },
    ],
  },
  {
    title: 'Bonus (2)',
    templates: [
      { key: 'bonus-pdf', icon: GraduationCap, title: '12 Solved Exercises (PDF)', desc: 'The problem with its data, a step-by-step solution, a table and what the result means. 31 pages.', ext: '.pdf' },
      { key: 'bonus-docx', icon: FileText, title: '12 Solved Exercises (Editable DOCX)', desc: 'The same bonus in an editable format to work through with your team.', ext: '.docx' },
    ],
  },
  {
    title: 'International Bonus',
    templates: [
      { key: 'equivalents-guide', icon: Globe, title: 'US · UK · Canada · Australia Equivalents Guide', desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this guide in the US, UK, Canada and Australia.', ext: '.docx' },
    ],
  },
];

const CROSS_SELL = [
  { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
  { href: '/en/digital-products/restaurant-schedule-templates', label: 'Restaurant Staff Scheduling Kit Pro' },
];

export default function FoodCostMenuEngineeringGuideDashboard() {
  const { token } = useAuth('food-cost-menu-engineering-guide-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', { headers: { Authorization: `Bearer ${token}` } })
      .then((r) => r.json())
      .then((data) => { if (data.files) setFiles(data.files); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <>
      <Helmet>
        <title>Food Cost + Menu Engineering Guide — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/food-cost-menu-engineering-guide" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Food Cost + Menu Engineering Guide</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Your Dashboard</span></div>
            <a href="https://aichef.pro/en" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge lang="en" />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Food Cost + <span className="text-[#FFD700]">Menu Engineering</span> Guide</h1>
          <div className="mb-3">
            <ProductVersionBadge productId="food-cost-menu-engineering-guide" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Your complete guide + 8 Excel tools + the solved exercises bonus + the Equivalents Guide, ready to download. Lifetime access — future updates included.</p>
        </section>

        {SECTIONS.map((section) => (
          <section key={section.title} className="pb-12 px-4">
            <div className="max-w-5xl mx-auto">
              <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-4">{section.title}</p>
              <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {section.templates.map((tpl) => {
                  const Icon = tpl.icon;
                  const url = files[tpl.key];
                  return (
                    <div key={tpl.key} className="rounded-xl p-5 bg-white/5 border border-white/10 hover:border-[#FFD700]/30 transition-all">
                      <div className="flex items-start gap-3 mb-3">
                        <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0"><Icon className="w-5 h-5 text-[#FFD700]" /></div>
                        <div><h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3><p className="text-gray-500 text-xs mt-0.5">{tpl.ext}</p></div>
                      </div>
                      <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>
                      {loading ? <Loader2 className="w-5 h-5 text-gray-500 animate-spin" /> : url ? (
                        <a href={url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10 transition-all">
                          <Download className="w-4 h-4" />Download
                        </a>
                      ) : <span className="text-gray-500 text-sm">Coming soon</span>}
                    </div>
                  );
                })}
              </div>
            </div>
          </section>
        ))}

        <ProductChangelog productId="food-cost-menu-engineering-guide" lang="en" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Already have the guide? Complete your toolkit</p>
            <div className="flex flex-col sm:flex-row flex-wrap items-center justify-center gap-4">
              {CROSS_SELL.map((c) => (
                <a
                  key={c.href}
                  href={c.href}
                  className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
                >
                  See {c.label}
                </a>
              ))}
            </div>
            <a href="/en/digital-products" className="inline-block text-gray-400 hover:text-[#FFD700] text-sm transition-colors">
              See all Digital Products
            </a>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Food Cost + Menu Engineering Guide · All rights reserved</p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro/en" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contact</a>
            </div>
          </div>
        </footer>
        <WhatsAppProductSupport lang="en" />
      </div>
    </>
  );
}
