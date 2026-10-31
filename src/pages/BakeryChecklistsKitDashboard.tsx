import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  Sunrise, Wheat, Flame, Store,
  Users, UserCog, ClipboardList, Gift,
  Calendar, CalendarDays,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Bakery Checklists Kit Pro (tienda EN) — COPIA TRADUCIDA de KitTareasPanaderiaDashboard.tsx con la maqueta de sus
// hermanos EN (TacoShopChecklistsKitDashboard.tsx): mismos componentes compartidos con lang="en".
// Las claves (`key`), los iconos y el ORDEN son los MISMOS que el ES kit-tareas-panaderia y que la entrada
// `bakery-checklist-templates` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza); la guía
// ES↔LatAm (`guia-equivalencias`) la sustituye el bonus común EN (`equivalents-guide`).
// Títulos = los de los xlsx EN (SPEC checklists-kit/bakery §2). Venta cruzada a la tienda EN (el ES cruza a Kit Tareas
// Restaurante, Kit Tareas Pastelería y Pack APPCC → Bakery Business Plan Kit, Pastry Shop Checklists Kit Pro y HACCP Food
// Safety Kit Pro). Fuera lo que el dashboard ES afirma y el kit EN no trae (horno de convección, «protocolos para recuperar
// masas», «gestión de cola», «reporting con KPIs», calibración de termómetros, San Juan, «marketing por estación»).
// Molde plano: sin contador, sin instrucciones, sin protección. Sin Google Sheets hasta que el test real lo confirme.

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'apertura-cierre', icon: Sunrise, title: "Bakery Opening & Closing Checklist: Overnight Bake Shift, Production & Shop", desc: "The overnight bake shift from 3:00 AM, fermentation and baking, the shop opening and the close, each task with a time and who does it." },
  { key: 'masas-madre-fermentacion', icon: Wheat, title: "Sourdough Starter & Fermentation Checklist: Starter, Bulk, Retard & Preferments", desc: "Starter feeding, pH, temperature, float test and log; dough temperature, bulk, retard and final proof; yeast, poolish and biga." },
  { key: 'hornos-coccion', icon: Flame, title: "Bakery Oven Checklist: Deck & Rack Ovens, Steam and Bake Times", desc: "Deck and rack ovens: preheating, steam, the damper and loading, plus a bake table in °F for 7 breads." },
  { key: 'expositor-venta', icon: Store, title: "Bakery Display & Counter Checklist: Bread Case, Labels & Customer Service", desc: "The display with FIFO, labels and allergens, TCS items, gluten-free and organic, customer service, special orders and the shop close." },
  { key: 'tareas-manager', icon: Users, title: "Bakery Manager Checklist: Production Planning, Flour Orders, Waste & Food Cost", desc: "Daily production plan, flour orders and quality, waste, food cost, prices, the overnight shift schedule and training." },
  { key: 'tareas-perfiles', icon: UserCog, title: "Bakery Duties by Role: Head Baker, Baker, Bakery Assistant & Counter Staff", desc: "Head baker, baker, bakery assistant and counter staff: clear tasks, no overlaps." },
  { key: 'semanales-mensuales', icon: ClipboardList, title: "Bakery Weekly & Monthly Checklists: Deep Cleaning, Maintenance & Inventory", desc: "Weekly deep cleaning, scale calibration and inventory; monthly oven and mixer maintenance, log reviews, food cost and pest control." },
  { key: 'eventos-estacionales', icon: Gift, title: "Bakery Seasonal & Holiday Checklist: Seasonal Breads, Holiday Orders & Specialties", desc: "Breads by season, the holidays, Easter, Valentine's Day, World Bread Day and Thanksgiving, and the specialty trends." },
  { key: 'plantilla-personalizable', icon: FileSpreadsheet, title: "Blank Bakery Checklist Template (Editable)", desc: "A blank checklist with the kit's columns to build lists for your exact bakery." },
  { key: 'bonus-briefing-produccion', icon: Calendar, title: "BONUS: Bakery Daily Production Sheet (Pre-Shift Briefing)", desc: "13 fields to start the day: today's production, the starter and preferments, ovens and equipment, and the team." },
  { key: 'bonus-calendario-anual', icon: CalendarDays, title: "BONUS: Bakery Annual Calendar: Seasonal Breads, Orders, Maintenance & Training (US)", desc: "12 months of seasonal breads, US events and orders, maintenance and team training." },
  { key: 'equivalents-guide', icon: Globe, title: "US · UK · Canada · Australia Equivalents Guide", desc: "Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia." },
];

export default function BakeryChecklistsKitDashboard() {
  const { token } = useAuth('bakery-checklist-templates-jwt');
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
        <title>Bakery Checklists Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/bakery-checklist-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Bakery Checklists Kit Pro
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
            Bakery Checklists Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="bakery-checklist-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 11 templates, ready to download. Print, delegate and keep control.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              9 Checklists + 3 Bonuses · Direct Download
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
                        <p className="text-gray-500 text-xs mt-0.5">{tpl.key === 'equivalents-guide' ? '.docx' : '.xlsx'}</p>
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
              </p>
            </div>
          </div>
        </section>

        <ProductChangelog productId="bakery-checklist-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Complete your bakery management toolkit
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/en/digital-products/bakery-business-plan"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Bakery Business Plan Kit
              </a>
              <a
                href="/en/digital-products/pastry-shop-checklist-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Pastry Shop Checklists Kit Pro
              </a>
              <a
                href="/en/digital-products/haccp-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See HACCP Food Safety Kit Pro
              </a>
            </div>
          </div>
        </section>

        {/* ── Footer ───────────────────────────────────────── */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Bakery Checklists Kit Pro · All rights reserved
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
