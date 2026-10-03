import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  CalendarDays, Clock, Banknote, UserPlus, Palmtree,
  Star, Users, Megaphone, Calculator,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Restaurant Staff Scheduling Kit Pro (tienda EN) — COPIA TRADUCIDA de KitGestionPersonalDashboard.tsx
// con la maqueta de los kits EN hermanos (RestaurantInventoryKitDashboard.tsx): mismos componentes
// compartidos con lang="en". Las claves (`key`) y el ORDEN son los MISMOS que el ES kit-gestion-personal
// y que la entrada `restaurant-schedule-templates` de netlify/functions/get-download-urls.ts
// (gate-flujo-postpago.py las cruza). Títulos = los de los xlsx EN (SPEC staff-kit §2.1, D5). Icono
// de coste laboral: Banknote en lugar de Euro (tienda en USD, como Food Cost Kit Pro). Sin venta
// cruzada a productos de la tienda ES: la cruzada apunta al hub EN. Compatibilidad: sin Google
// Sheets hasta que el test real lo confirme (SPEC staff-kit §6 y §9), igual que la landing.

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'cuadrante', icon: CalendarDays, title: 'Restaurant Schedule Template: Weekly & Monthly Staff Rota', desc: 'Weekly and monthly schedule with alerts for long shifts, clopenings, 40-hour weeks, days off and minors.' },
  { key: 'horas-extra', icon: Clock, title: 'Overtime Tracker & Time Log (FLSA 40-Hour Week)', desc: 'Overtime over 40 hours a week at 1.5×, an optional daily state rule and the cost of every hour.' },
  { key: 'coste-laboral', icon: Banknote, title: 'Restaurant Labor Cost Calculator (Payroll & Labor %)', desc: 'Labor cost % with a traffic light by type of restaurant and a staffing forecast per service.' },
  { key: 'onboarding', icon: UserPlus, title: 'New Hire Onboarding Checklist', desc: '50 tasks: hiring paperwork, required training, equipment and access.' },
  { key: 'vacaciones', icon: Palmtree, title: 'PTO & Vacation Planner', desc: 'Annual calendar by week, PTO requests and minimum coverage.' },
  { key: 'evaluacion', icon: Star, title: 'Employee Performance Review Form', desc: '10 competencies, scored 1-5, with quarterly history.' },
  { key: 'directorio', icon: Users, title: 'Employee Directory & Expiry Tracker', desc: 'Staff directory with contract, food handler card and alcohol server certificate expiry dates.' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Shift Handover Log (Manager Log Book)', desc: 'Shift handover + cash count against the Z report and temperatures in °F at handover.' },
  { key: 'bonus-calculadora', icon: Calculator, title: 'BONUS: Restaurant Staffing Calculator', desc: 'How many people you need from your covers and days open.' },
];

export default function RestaurantScheduleKitDashboard() {
  const { token } = useAuth('restaurant-schedule-templates-jwt');
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
        <title>Restaurant Staff Scheduling Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/restaurant-schedule-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Restaurant Staff Scheduling Kit Pro
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
            Restaurant Staff Scheduling Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="restaurant-schedule-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 7 templates + 2 bonuses, ready to download.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              7 Templates + 2 Bonuses · Direct Download
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
              </p>
            </div>
          </div>
        </section>

        <ProductChangelog productId="restaurant-schedule-templates" lang="en" />
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
              © 2026 AI Chef Pro · Restaurant Staff Scheduling Kit Pro · All rights reserved
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
