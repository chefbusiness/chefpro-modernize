import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft, Calculator, Globe,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Sushi Restaurant Business Plan Kit (tienda EN) — COPIA del dashboard EN gemelo de la familia Planes
// (RotisserieChickenRestaurantBusinessPlanDashboard.tsx) con los textos del sushi restaurant; edición inglesa de
// PlanNegocioSushiBarDashboard.tsx. Mismos componentes compartidos con lang="en". Claves (`key`) = las del ES
// plan-negocio-sushi-bar: 'plan-negocio', 'plan-financiero', 'checklist-apertura', 'calculadora-sushi' y el bonus común
// 'equivalents-guide' (el ES lo llama 'guia-equivalencias'; la familia EN usa 'equivalents-guide'); son las de la entrada
// `sushi-restaurant-business-plan` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza). Títulos =
// los de los ficheros EN; el Word va primero. 4 ficheros + la guía → rejilla de 2 columnas. Compatibilidad: solo
// Microsoft Excel y Word. Venta cruzada: Restaurant Checklists, Food Cost y HACCP (no hay checklists de sushi EN), y el hub EN.

// ── Template metadata (matches the landing grid order) ─────────
const TEMPLATES = [
  {
    key: 'plan-negocio',
    icon: FileText,
    type: '.docx',
    title: 'Sushi Restaurant Business Plan (10 Sections)',
    desc: "A complete Word plan with 10 sections for a neighborhood sushi restaurant with a sushi bar, tables, take-out and delivery: executive summary, concept and value proposition, market analysis, competitive analysis, marketing plan, operations plan, management and staffing, financial plan, legal requirements, permits and licenses (Type I hood, raw-fish freezing rules, sushi rice, health permit, beer and wine license), and conclusions with an action plan.",
  },
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Sushi Restaurant Financial Projections: 3-Year P&L, Cash Flow & Financing',
    desc: "9 sheets: assumptions, startup costs, 3-year P&L, break-even in covers per day, pessimistic / base / optimistic scenarios, staffing, 12-month cash flow, financing with a loan schedule and DSCR, and instructions. Type in the green cells; the rest recalculates.",
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Sushi Restaurant Startup Checklist (80 Tasks)',
    desc: "80 tasks in 6 phases: business setup (zoning check, LLC, EIN, business license, sales tax permit), hood and permits (plan review, building permit, fire suppression, certificate of occupancy), raw fish and health (parasite letters, freezer log, consumer advisory, sushi rice TPHC or variance), staff and allergens, menu, brand and delivery, and opening day plus your first 90 days.",
  },
  {
    key: 'calculadora-sushi',
    icon: Calculator,
    type: '.xlsx',
    title: 'Sushi Fish, Rice & Costing Calculator',
    desc: "Fish yield (cost per usable lb of whole salmon, fillet and tuna saku, per slice and per roll, and whether the whole fish pays off), sushi rice (lb of sushi rice per lb of raw rice, nigiri per lb, rice to cook a day) and the food cost, suggested price and margin by channel of 14 products, in pounds and ounces. The starting values are kit estimates: replace them with your own.",
  },
  {
    key: 'equivalents-guide',
    icon: Globe,
    type: '.docx',
    title: "US · UK · Canada · Australia Equivalents Guide",
    desc: "Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.",
  },
];

const CROSS_SELL = [
  { href: '/en/digital-products/restaurant-checklist-templates', label: 'Restaurant Checklists Kit Pro' },
  { href: '/en/digital-products/food-cost-templates', label: 'Food Cost Kit Pro' },
  { href: '/en/digital-products/haccp-templates', label: 'HACCP Food Safety Kit Pro' },
];

export default function SushiRestaurantBusinessPlanDashboard() {
  const { token } = useAuth('sushi-restaurant-business-plan-jwt');
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
        <title>Sushi Restaurant Business Plan Kit — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/sushi-restaurant-business-plan" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Sushi Restaurant Business Plan Kit
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
            Sushi Restaurant <span className="text-[#FFD700]">Business Plan</span> Kit
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="sushi-restaurant-business-plan" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your sushi restaurant business plan, ready to download: a 10-section Word plan, Excel financial projections with a 3-year P&L, cash flow and financing, a fish, sushi rice and costing calculator, and an 80-task startup checklist. Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              5 Files · Direct Download
            </p>

            <div className="grid sm:grid-cols-2 gap-4">
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
                        <p className="text-gray-500 text-xs mt-0.5">{tpl.type}</p>
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
                Microsoft Excel and Word files · Print-ready on US Letter
              </p>
              <p className="text-gray-400 text-sm">
                In the Excel model, the green cells are the ones you type; the rest have formulas and are protected so
                they don't break. To change one: Review → Unprotect Sheet (no password). A planning tool, not financial,
                tax or legal advice: review your final numbers with your accountant.
              </p>
            </div>
          </div>
        </section>

        <ProductChangelog productId="sushi-restaurant-business-plan" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">
              Complete your toolkit before opening day
            </p>
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

        {/* ── Footer ───────────────────────────────────────── */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Sushi Restaurant Business Plan Kit · All rights reserved
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
