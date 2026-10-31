import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  DoorOpen, Flame, ShieldCheck, Wheat,
  Briefcase, Users, ClipboardList, CalendarDays,
  Megaphone, Calendar,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Taco Shop Checklists Kit Pro (tienda EN) — COPIA TRADUCIDA de KitTareasTaqueriaDashboard.tsx con la maqueta de
// sus hermanos EN (PizzaShopChecklistsKitDashboard.tsx): mismos componentes compartidos con lang="en".
// Las claves (`key`), los iconos y el ORDEN son los MISMOS que el ES kit-tareas-taqueria (la 02 es `trompo-plancha-comal`)
// y que la entrada `taco-shop-checklist-templates` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las
// cruza); la guía ES↔LatAm (`guia-equivalencias`) la sustituye el bonus común EN (`equivalents-guide`).
// Títulos = los de los xlsx EN (SPEC checklists-kit/taco §2, D5). Venta cruzada a la tienda EN (el ES cruza a Guía
// Restaurante Mexicano, Kit Tareas Restaurante y Pack APPCC → Taco Shop Business Plan Kit, Restaurant Checklists Kit Pro y
// HACCP Food Safety Kit Pro). Fuera lo que el dashboard ES afirma y el kit EN no trae («arqueo de caja» como hoja: el kit
// no trae libro de caja; RD 1021/2022 y los 14 alérgenos de la UE; «campañas españolas»; «Imprimible A4»).
// Compatibilidad: sin Google Sheets hasta que el test real lo confirme (SPEC checklists-kit §9).

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'apertura-cierre', icon: DoorOpen, title: 'Taco Shop Opening & Closing Checklists: Trompo, Salsa Bar, Tortillas & Counter', desc: 'Opening and closing: temperatures, the trompo and the cone check, the cold salsa bar, guisados, the counter and delivery, leftovers and the cash count.' },
  { key: 'trompo-plancha-comal', icon: Flame, title: 'Trompo, Griddle & Comal Checklists: Al Pastor Marinade, Stacking & Carving', desc: 'Marinade and stacking of the trompo (if applicable), time limit, probe at 145 °F or your county\'s figure, yield, carving, griddle and comal.' },
  { key: 'appcc-salsas-alergenos', icon: ShieldCheck, title: 'Taco Shop Food Safety Checklists: Temperature Logs, Salsa Bar & Allergens', desc: 'Temperature logs and receiving (FDA Food Code), the salsa bar with time on and tossed, and the 9 major allergens.' },
  { key: 'nixtamal-tortilla-guisados', icon: Wheat, title: 'Nixtamal, Masa, Tortilla & Guisados Checklists', desc: 'Nixtamal cooking and milling (if applicable), tortilla machine calibration, guisados in the steam table.' },
  { key: 'manager', icon: Briefcase, title: 'Taqueria Manager Checklist: Daily & Weekly', desc: 'Mexican food distributor orders, supplier prices, beverage inventory, taco costing and time-clock records.' },
  { key: 'perfiles', icon: Users, title: 'Taco Shop Duties by Role: Taquero, Tortilla Maker, Salsa Prep, Griddle, Counter & Driver', desc: 'Taquero on the trompo, tortilla maker, salsa prep cook, griddle and fryer, counter and register, delivery driver.' },
  { key: 'semanales-mensuales', icon: ClipboardList, title: 'Taco Shop Weekly & Monthly Checklists: Deep Cleaning, Inventory & Maintenance', desc: 'Deep cleaning of the corn mill and fryer, trompo and hood filters, gas checks, suppliers and training.' },
  { key: 'eventos-estacionales', icon: CalendarDays, title: 'Taco Shop Event & Seasonal Checklists: Holidays, Busy Days & Seasonal Ingredients', desc: 'Candelaria, Lent Fridays, Cinco de Mayo, chiles en nogada, Mexican Independence Day, Day of the Dead and the posadas.' },
  { key: 'plantilla-personalizable', icon: FileSpreadsheet, title: 'Blank Taco Shop Checklist Template (Editable)', desc: 'A blank template to build checklists for your taqueria (with or without a trompo, with or without a tortilleria).' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Taco Shop Pre-Shift Meeting Template (Huddle Notes)', desc: '5-minute pre-shift meeting: the trompo, guisados and salsas of the day, the allergen notice and 86s.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Taco Shop Annual Calendar: Holidays, Busy Days & Upkeep (US)', desc: '27 dates and yearly tasks: Mexican holidays, US busy days and equipment upkeep, with lead times.' },
  { key: 'equivalents-guide', icon: Globe, title: 'US · UK · Canada · Australia Equivalents Guide', desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.' },
];

export default function TacoShopChecklistsKitDashboard() {
  const { token } = useAuth('taco-shop-checklist-templates-jwt');
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
        <title>Taco Shop Checklists Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/taco-shop-checklist-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Taco Shop Checklists Kit Pro
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
            Taco Shop Checklists Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="taco-shop-checklist-templates" lang="en" />
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

        <ProductChangelog productId="taco-shop-checklist-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Complete your taco shop management toolkit
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/en/digital-products/taco-shop-business-plan"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Taco Shop Business Plan Kit
              </a>
              <a
                href="/en/digital-products/restaurant-checklist-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Restaurant Checklists Kit Pro
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
              © 2026 AI Chef Pro · Taco Shop Checklists Kit Pro · All rights reserved
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
