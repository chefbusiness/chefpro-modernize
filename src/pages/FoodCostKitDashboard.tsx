import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  UtensilsCrossed, Wine, CakeSlice, Truck, Coffee,
  BarChart3, Calculator, TrendingDown, ClipboardList, ChefHat, PartyPopper, BookOpen,
  Scale, ReceiptText,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Food Cost Kit Pro (tienda EN) — COPIA TRADUCIDA de KitEscandallosDashboard.tsx: mismo diseño y
// mismos componentes compartidos, que reciben lang="en" (el ES no cambia).
// Las claves (`key`) son las MISMAS que la entrada `food-cost-templates` de
// netlify/functions/get-download-urls.ts (el gate gate-flujo-postpago.py las cruza).
// Títulos = los de los xlsx EN (SPEC recipe-costing-kit, D9 bis). Sin promesa de Google Sheets
// (D16) y sin venta cruzada a productos de la tienda ES: la cruzada apunta al hub EN.

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'estandar', icon: UtensilsCrossed, title: 'Recipe Cost Card & Plate Cost Calculator', desc: 'The full recipe cost card for menu dishes, with automatic formulas and your actual food cost.' },
  { key: 'degustacion', icon: ChefHat, title: 'Tasting Menu Costing', desc: 'For tasting menus of 5 to 9 courses, with an overall cost summary.' },
  { key: 'menu-dia', icon: ClipboardList, title: 'Prix Fixe & Set Menu Costing', desc: 'Starter, main, dessert and extras, with a weekly rotation.' },
  { key: 'cocktails', icon: Wine, title: 'Pour Cost Calculator (Cocktails & Drinks)', desc: 'Cocktail pour cost with standard US pours and bottle-to-liter pricing.' },
  { key: 'pasteleria', icon: CakeSlice, title: 'Bakery & Cake Pricing Calculator', desc: 'Pastry trim losses and yield per batch, with cost and price per unit.' },
  { key: 'catering', icon: PartyPopper, title: 'Catering Pricing Calculator & Quote', desc: 'Food + staff + rentals + transport in a single quote per guest.' },
  { key: 'cafeteria', icon: Coffee, title: 'Café & Brunch Menu Costing', desc: '25-30% target food cost with real café examples.' },
  { key: 'food-truck', icon: Truck, title: 'Food Truck Menu Pricing & Break-Even', desc: 'Street food with a daily break-even included.' },
  { key: 'mermas', icon: TrendingDown, title: 'Food Waste Log', desc: 'Weekly waste log for 16 product families, with a traffic light and a trend chart.' },
  { key: 'calculadora-pvp', icon: Calculator, title: 'Menu Pricing Calculator', desc: 'Recommended menu price for 10 venue types.' },
  { key: 'dashboard', icon: BarChart3, title: 'Food Cost Percentage Tracker', desc: 'Track your food cost over 12 consecutive periods.' },
  { key: 'test-rendimiento', icon: Scale, title: 'Yield Test (Butcher & Cooking Loss)', desc: 'Butcher yield and cooking loss: weigh the cut and get the real trim loss for your cost card.' },
  { key: 'lista-precios', icon: ReceiptText, title: 'Ingredient Price Tracker', desc: 'Your supplier prices in one sheet, with an alert when an ingredient goes up.' },
  { key: 'bonus-mermas', icon: TrendingDown, title: 'BONUS: Actual vs Theoretical Food Cost (Inventory & Waste)', desc: 'Inventory and waste control that compares actual and theoretical usage.' },
  { key: 'bonus-guia', icon: BookOpen, title: 'BONUS: How to Reduce Food Cost in 30 Days', desc: 'A step-by-step PDF guide (23 pages) to bring your food cost down in a month.' },
];

export default function FoodCostKitDashboard() {
  const { token } = useAuth('food-cost-templates-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then((data) => {
        if (data.files) setFiles(data.files);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <>
      <Helmet>
        <title>Food Cost Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/food-cost-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Food Cost Kit Pro
            </a>
            <div className="flex items-center gap-2">
              <FileSpreadsheet className="w-5 h-5 text-[#FFD700]" />
              <span className="text-white font-bold text-sm">Your Dashboard</span>
            </div>
            <a href="https://aichef.pro/en" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">
              aichef.pro
            </a>
          </div>
        </header>

        {/* ── Hero ───────────────────────────────────────────── */}
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge lang="en" />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">
            Food Cost Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="food-cost-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 13 templates + 2 bonuses, ready to download.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              13 Templates + 2 Bonuses · Direct Download
            </p>

            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {TEMPLATES.map((tpl, i) => {
                const Icon = tpl.icon;
                const url = files[tpl.key];
                const isPrimary = i === 0;

                return (
                  <div
                    key={tpl.key}
                    className={`rounded-xl p-5 transition-all ${
                      isPrimary
                        ? 'bg-white/5 border-2 border-[#FFD700]/50'
                        : 'bg-white/5 border border-white/10 hover:border-[#FFD700]/30'
                    }`}
                  >
                    <div className="flex items-start gap-3 mb-3">
                      <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0">
                        <Icon className="w-5 h-5 text-[#FFD700]" />
                      </div>
                      <div>
                        <h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3>
                        <p className="text-gray-500 text-xs mt-0.5">{tpl.key === 'bonus-guia' ? '.pdf' : '.xlsx'}</p>
                      </div>
                    </div>
                    <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>

                    {loading ? (
                      <Loader2 className="w-5 h-5 text-gray-500 animate-spin" />
                    ) : url ? (
                      <a
                        href={url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition-all ${
                          isPrimary
                            ? 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90'
                            : 'border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10'
                        }`}
                      >
                        <Download className="w-4 h-4" />
                        Download
                      </a>
                    ) : (
                      <span className="text-gray-500 text-sm">Coming soon</span>
                    )}
                  </div>
                );
              })}
            </div>

            {/* ── Tip banner ───────────────────────────────── */}
            <div className="mt-8 bg-white/5 border border-white/10 rounded-xl p-6 text-center">
              <p className="text-white font-semibold mb-1">
                Works with Excel, Google Sheets, LibreOffice and Numbers
              </p>
              <p className="text-gray-400 text-sm">
                Download the .xlsx files and open them in your favorite spreadsheet app. Every formula carries over.
              </p>
            </div>
          </div>
        </section>

        <ProductChangelog productId="food-cost-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              More templates, guides and AI prompts for your restaurant
            </p>
            <a
              href="/en/digital-products"
              className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
            >
              See all Digital Products
            </a>
          </div>
        </section>

        {/* ── Footer ───────────────────────────────────────── */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Food Cost Kit Pro · All rights reserved
            </p>
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
