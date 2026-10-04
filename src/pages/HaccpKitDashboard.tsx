import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  Thermometer, SprayCan, ClipboardCheck, Truck, Bug,
  AlertTriangle, Droplets, ShieldCheck, UserCheck, GraduationCap,
  Flame, Snowflake, Fish, Gauge,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// HACCP Food Safety Kit Pro (tienda EN) — COPIA TRADUCIDA de PackAppccDashboard.tsx con la maqueta
// de los kits EN hermanos (RestaurantInventoryKitDashboard.tsx): mismos componentes compartidos con
// lang="en". Las claves (`key`) y el ORDEN son los MISMOS que el ES pack-appcc y que la entrada
// `haccp-templates` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza).
// Títulos = los de los xlsx EN (SPEC haccp-kit §2.1, D5). Sin venta cruzada a productos de la
// tienda ES: la cruzada apunta al hub EN.

// ── Template metadata (same order as the files) ─────────────────
const TEMPLATES = [
  { key: 'temp-diario', icon: Thermometer, title: 'Food Temperature Log: Coolers, Freezers & Hot Holding', desc: 'Twice-a-day checks of coolers, freezers, display cases and hot holding, with automatic OK/ALERT in °F.' },
  { key: 'temp-recepcion', icon: Thermometer, title: 'Receiving Temperature Log', desc: 'Delivery temperatures against the receiving limit of each product family, with OK/REJECT.' },
  { key: 'plan-limpieza', icon: SprayCan, title: 'Master Cleaning & Sanitizing Schedule', desc: 'Master plan with 32 pre-filled areas, inside and out, frequencies and a chemicals tab.' },
  { key: 'registro-limpieza', icon: SprayCan, title: 'Daily Cleaning Checklist (AM/PM)', desc: 'Daily checklist by shift with sign-off and initials.' },
  { key: 'recepcion', icon: ClipboardCheck, title: 'Receiving Checklist for Deliveries', desc: 'Temperature, dates, labeling and packaging checks on every delivery.' },
  { key: 'trazabilidad', icon: Truck, title: 'Food Traceability Log (Lots In & Out)', desc: 'Products in and out with lot, vendor and dates.' },
  { key: 'plagas', icon: Bug, title: 'Pest Control Log & Bait Station Map', desc: 'Pest control visits with EPA Reg. No., reports and a bait station map.' },
  { key: 'alergenos', icon: AlertTriangle, title: 'Menu Allergen Matrix (US Big 9 & UK 14)', desc: 'Your menu items × 14 allergens with Y/T/N drop-downs and the US Big 9 marked.' },
  { key: 'aceite', icon: Droplets, title: 'Fryer Oil Log (TPM Tests & Disposal)', desc: 'Total polar materials tests with OK/WATCH/CHANGE alerts and used oil pickups.' },
  { key: 'agua', icon: Droplets, title: 'Water Quality Log (Chlorine & Private Supply)', desc: 'Free chlorine, appearance and lab results.' },
  { key: 'acciones', icon: ClipboardCheck, title: 'Corrective Action Log', desc: 'Incidents with cause, action taken, product disposition and verification.' },
  { key: 'haccp', icon: ShieldCheck, title: 'HACCP Plan Template: Hazard Analysis & CCPs', desc: '21 hazards across 7 process steps with CCPs, critical limits and monitoring.' },
  { key: 'higiene', icon: UserCheck, title: 'Employee Hygiene & Health Checklist', desc: 'Clothing, handwashing, health and conduct rules, ready to print.' },
  { key: 'fichas-alergenos', icon: AlertTriangle, title: 'Allergen Chart & Allergic Reaction Protocol', desc: 'A printable allergen chart and what to do in an allergic reaction.' },
  { key: 'guia-inspeccion', icon: ShieldCheck, title: 'Health Inspection Self-Checklist', desc: 'The 25 points a health inspector looks at, with a self-assessment.' },
  { key: 'coccion', icon: Flame, title: 'Cooking & Reheating Temperature Log', desc: 'Final internal temperature by process with automatic OK/REPEAT.' },
  { key: 'enfriamiento', icon: Snowflake, title: 'Cooling & Thawing Log (2-Stage Cooling)', desc: 'Two-stage cooling (135 → 70 °F in 2 h, → 41 °F in 6 h) and thawing in the walk-in.' },
  { key: 'anisakis', icon: Fish, title: 'Parasite Destruction Log (Fish Served Raw)', desc: 'Freezing record for fish served raw (−4 °F for 168 h or −31 °F for 15 h).' },
  { key: 'termometros', icon: Gauge, title: 'Thermometer Calibration Log', desc: 'Monthly probe check at the ice point or the boiling point, corrected for altitude.' },
  { key: 'bonus-formacion', icon: GraduationCap, title: 'BONUS: Food Safety Training Log', desc: "Your team's food safety training and renewal dates." },
  { key: 'bonus-protocolo', icon: AlertTriangle, title: 'BONUS: Food Recall & Foodborne Illness Response Plan', desc: 'A printable poster with the 7 steps to follow in a recall or a suspected foodborne illness.' },
];

export default function HaccpKitDashboard() {
  const { token } = useAuth('haccp-templates-jwt');
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
        <title>HACCP Food Safety Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/haccp-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              HACCP Food Safety Kit Pro
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
            HACCP Food Safety Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="haccp-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 19 food safety templates + 2 bonuses, ready to download.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              19 Templates + 2 Bonuses · Direct Download
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
                Works with Excel, Google Sheets, LibreOffice and Numbers · Print-ready on US Letter
              </p>
              <p className="text-gray-400 text-sm">
                Download the .xlsx files and open them in your favorite spreadsheet app. Every formula carries over.
              </p>
            </div>
          </div>
        </section>

        <ProductChangelog productId="haccp-templates" lang="en" />
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
              © 2026 AI Chef Pro · HACCP Food Safety Kit Pro · All rights reserved
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
