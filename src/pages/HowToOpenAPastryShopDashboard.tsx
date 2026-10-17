import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, ArrowLeft,
  BookOpen, FileText, Building2, Banknote,
  CalendarRange, Calculator, TrendingUp, ClipboardCheck,
  Wrench, Users, GraduationCap, ScrollText, Star,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// How to Open a Pastry Shop (tienda EN) — COPIA TRADUCIDA de GuiaPasteleriaDashboard.tsx (ES), mismas secciones y
// mismo molde de tarjeta; componentes compartidos con lang="en" como FoodCostMenuEngineeringGuideDashboard.tsx.
// Las claves (`key`) son las MISMAS que el ES guia-pasteleria-obrador, salvo el bonus de equivalencias, que es el
// COMÚN de la tienda EN ('equivalents-guide', dl/en-shared/), y coinciden con la entrada `how-to-open-a-pastry-shop`
// de netlify/functions/get-download-urls.ts y de src/data/productos-digitales-config.ts (gate-flujo-postpago.py las
// cruza). Títulos = los de los ficheros EN (SPEC guia-pasteleria-en §2). Venta cruzada: solo productos de la tienda EN.

const SECTIONS = [
  {
    title: 'Main Guide',
    templates: [
      { key: 'guia-pdf', icon: BookOpen, title: 'Complete Guide (PDF)', desc: '20 chapters and a dated US regulatory appendix, with tables built from the Excel tools and from the rules they cite. 113 pages.', ext: '.pdf' },
      { key: 'guia-docx', icon: FileText, title: 'Complete Guide (Editable DOCX)', desc: 'The same content in an editable format to annotate, adapt to your project and take to your meeting with your designer or architect.', ext: '.docx' },
    ],
  },
  {
    title: 'Excel Tools (8)',
    templates: [
      { key: 'capacidad-obrador', icon: Building2, title: 'Kitchen Capacity and Site Visit Checklist', desc: 'Zones and square feet, capacity by equipment, which machine is your bottleneck, pieces a day for the whole kitchen and the site visit checklist with its deal-breakers.', ext: '.xlsx' },
      { key: 'capex-pasteleria', icon: Banknote, title: 'Startup Cost Calculator', desc: 'Startup costs by block and by format, the sales tax column line by line, takeover versus new build over the years of the lease, and the cash cushion.', ext: '.xlsx' },
      { key: 'estacionalidad-picos', icon: CalendarRange, title: 'Seasonal Peaks Planner', desc: 'The six peaks with their share of the year, the capacity gap against your kitchen, the cost of extra staff and the cash the seasonal stock ties up.', ext: '.xlsx' },
      { key: 'carta-escandallo', icon: Calculator, title: 'Opening Menu and Recipe Costing', desc: "Batch costing for 30 items with the production kitchen's hour charged in, mix and average ticket, the menu decision and the egg and TCS decision with its Food Code section.", ext: '.xlsx' },
      { key: 'plan-financiero', icon: TrendingUp, title: '3-Year Financial Plan', desc: 'A P&L with monthly seasonality and a ramp-up, break-even, scenarios, staff with payroll taxes, a 12-month cash flow, financing and margin by channel.', ext: '.xlsx' },
      { key: 'checklist-legal', icon: ClipboardCheck, title: 'Permits and Licenses Checklist', desc: 'Thirty steps in six phases with a progress counter, which permit you need, selling wholesale, the cottage food route, the training log and the timeline with its critical path.', ext: '.xlsx' },
      { key: 'checklist-equipamiento', icon: Wrench, title: 'Equipment and Suppliers Checklist', desc: 'Equipment with a price range, its critical items, a sales tax column and lead times, nine verified suppliers with their link, and what you negotiated against the reference.', ext: '.xlsx' },
      { key: 'turnos-personal', icon: Users, title: 'Staff Schedule and Labor Cost', desc: "Weekly schedule per person, hours and cost by month and year with payroll taxes, workers' comp and benefits included, the cost of peak extra staff and the hiring plan.", ext: '.xlsx' },
    ],
  },
  {
    title: 'Bonuses (2)',
    templates: [
      { key: 'business-plan-docx', icon: ScrollText, title: 'Sample Business Plan for a Pastry Shop (Editable DOCX)', desc: 'The full case in the format a bank or an SBA lender expects: executive summary, market and location, concept and menu, operations, a three-year financial plan, and risks and scenarios.', ext: '.docx' },
      { key: 'bonus-decisiones-pdf', icon: GraduationCap, title: '12 Opening Decisions, Solved (PDF)', desc: 'Each decision with its context, its options, the criterion, the cell in the pack that settles it and the rule that applies when there is one. 39 pages.', ext: '.pdf' },
      { key: 'bonus-decisiones-docx', icon: FileText, title: '12 Opening Decisions, Solved (Editable DOCX)', desc: 'The same bonus in an editable format to work through with your partner, your accountant or your designer.', ext: '.docx' },
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
  { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
  { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
  { href: '/en/digital-products/bakery-business-plan', label: 'Bakery Business Plan Kit' },
];

export default function HowToOpenAPastryShopDashboard() {
  const { token } = useAuth('how-to-open-a-pastry-shop-jwt');
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
        <title>How to Open a Pastry Shop — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/how-to-open-a-pastry-shop" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />How to Open a Pastry Shop</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Your Dashboard</span></div>
            <a href="https://aichef.pro/en" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge lang="en" />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">How to Open a <span className="text-[#FFD700]">Pastry Shop</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="how-to-open-a-pastry-shop" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Your complete guide + 8 Excel tools + both bonuses + the Equivalents Guide, ready to download. Lifetime access — future updates included.</p>
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

        <ProductChangelog productId="how-to-open-a-pastry-shop" lang="en" />
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
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · How to Open a Pastry Shop · All rights reserved</p>
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
