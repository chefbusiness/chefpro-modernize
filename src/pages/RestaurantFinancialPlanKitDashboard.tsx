import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  TrendingUp, Target, Wallet, Building2, BarChart3,
  PieChart, FileText, Shuffle, ClipboardList,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Restaurant Financial Plan Kit Pro (tienda EN) — COPIA TRADUCIDA de KitPlanFinancieroDashboard.tsx
// con la maqueta de los kits EN hermanos (RestaurantScheduleKitDashboard.tsx): mismos componentes
// compartidos con lang="en". Las claves (`key`) y el ORDEN son los MISMOS que el ES kit-plan-financiero
// y que la entrada `restaurant-financial-plan-templates` de netlify/functions/get-download-urls.ts
// (gate-flujo-postpago.py las cruza). Títulos = los de los xlsx EN (SPEC financial-kit §2.1, D5). Sin
// venta cruzada a productos de la tienda ES: la cruzada apunta al hub EN. Compatibilidad: sin Google
// Sheets hasta que el test real lo confirme (SPEC financial-kit §6 y §9), igual que la landing.

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'plan-previsional', icon: TrendingUp, title: 'Restaurant Financial Projections: 3-Year Pro Forma P&L', desc: '3-year revenue and expense projections with a monthly breakdown and automatic charts.' },
  { key: 'plan-previsional-5', icon: TrendingUp, title: 'Restaurant Financial Projections: 5-Year Pro Forma P&L', desc: 'The same projections over 5 years, for lenders, investors and franchise applications.' },
  { key: 'break-even', icon: Target, title: 'Restaurant Break-Even Calculator', desc: 'Covers per day, break-even revenue, the average check you need and 3 scenarios.' },
  { key: 'cash-flow', icon: Wallet, title: 'Restaurant Cash Flow Forecast (12 Months)', desc: 'Monthly cash flow with quarterly sales tax and low-cash alerts.' },
  { key: 'capex', icon: Building2, title: 'Restaurant Startup Costs & Capex Budget', desc: 'Startup costs line by line, budget vs actual, useful life and depreciation.' },
  { key: 'pyl', icon: BarChart3, title: 'Restaurant P&L Template: Monthly Budget vs Actual', desc: 'Monthly variances with a traffic light and automatic ratios.' },
  { key: 'ratios', icon: PieChart, title: 'Restaurant Financial Ratios & KPI Dashboard', desc: 'Food cost, labor cost, prime cost, GOP, EBITDA and RevPASH against editable benchmarks.' },
  { key: 'viabilidad', icon: FileText, title: 'Restaurant Loan Proposal: Lender & Investor Summary', desc: 'IRR, NPV, payback, loan schedule, DSCR and collateral, in a professional format.' },
  { key: 'bonus-simulador', icon: Shuffle, title: 'BONUS: What-If Scenario Simulator', desc: '3 what-if scenarios compared side by side.' },
  { key: 'bonus-checklist', icon: ClipboardList, title: 'BONUS: Pre-Opening Financial Checklist (54 Tasks)', desc: '54 tasks in 7 phases before opening day.' },
];

export default function RestaurantFinancialPlanKitDashboard() {
  const { token } = useAuth('restaurant-financial-plan-templates-jwt');
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
        <title>Restaurant Financial Plan Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/restaurant-financial-plan-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Restaurant Financial Plan Kit Pro
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
            Restaurant <span className="text-[#FFD700]">Financial Plan</span> Kit Pro
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="restaurant-financial-plan-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 10 financial templates, ready to download. Plan, track and present your numbers.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              8 Templates + 2 Bonuses · Direct Download
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
                        <p className="text-gray-500 text-xs mt-0.5">.xlsx</p>
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
                Works with Excel, LibreOffice and Numbers · Print-ready on US Letter
              </p>
              <p className="text-gray-400 text-sm">
                Download the .xlsx files and open them in your favorite spreadsheet app.
                A planning tool, not financial or tax advice: review your final numbers with your accountant.
              </p>
            </div>
          </div>
        </section>

        <ProductChangelog productId="restaurant-financial-plan-templates" lang="en" />
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
              © 2026 AI Chef Pro · Restaurant Financial Plan Kit Pro · All rights reserved
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
