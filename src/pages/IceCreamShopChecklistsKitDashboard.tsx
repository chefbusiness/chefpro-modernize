import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  IceCream, Beaker, ClipboardList, Users,
  CalendarDays, Sun, FileEdit, Megaphone, Calendar, Building2, Wallet,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Ice Cream Shop Checklists Kit Pro (tienda EN) — COPIA TRADUCIDA de KitTareasHeladeriaDashboard.tsx con la maqueta
// de sus hermanos EN (GhostKitchenChecklistsKitDashboard.tsx): mismos componentes compartidos con lang="en".
// Las claves (`key`), los iconos y el ORDEN son los MISMOS que el ES kit-tareas-heladeria (la 02 es `partidas`) y que
// la entrada `ice-cream-shop-checklist-templates` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py
// las cruza); la guía ES↔LatAm (`guia-equivalencias`) la sustituye el bonus común EN (`equivalents-guide`). Títulos =
// los de los xlsx EN (SPEC checklists-kit/icecream §2, D5). Venta cruzada a la tienda EN (el ES cruza a Kit Tareas
// Restaurante, Kit Tareas Bar y Kit Escandallos → Coffee Shop Checklists, Restaurant Checklists y Food Cost Kit Pro:
// el Coffee Shop es el hermano más cercano, mostrador y vitrina con helado y café, en lugar del Bar). Fuera lo que el
// dashboard ES afirma y el kit no trae («inventario» semanal: son comprobaciones de stock; «15 fechas clave»: el
// calendario son 12 meses). Compatibilidad: sin Google Sheets hasta que el test real lo confirme (SPEC checklists-kit §9).

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'apertura-cierre', icon: IceCream, title: 'Ice Cream Shop Opening & Closing Checklists: Dipping Cabinets, Toppings & Counter', desc: '2 checklists: opening and closing, with the dipping cabinets, toppings, the counter and the cash count.' },
  { key: 'partidas', icon: Beaker, title: 'Ice Cream & Gelato Production Checklists: Pasteurizing, Aging & Batch Freezing', desc: 'Pasteurizing and batch freezing, with temperatures in °F and a shelf-life table.' },
  { key: 'manager', icon: ClipboardList, title: 'Ice Cream Shop Manager Checklist: Daily, Weekly & Monthly', desc: 'Daily, weekly and monthly, food cost included.' },
  { key: 'perfiles', icon: Users, title: 'Ice Cream Shop Duties by Role: Ice Cream Maker, Scooper & Shift Lead', desc: 'Ice cream maker, scooper and shift lead.' },
  { key: 'periodicas', icon: CalendarDays, title: 'Ice Cream Shop Cleaning Checklist & Maintenance Schedule', desc: 'Weekly deep clean, weekly upkeep and stock, monthly tasks and a quarterly and annual sheet.' },
  { key: 'eventos', icon: Sun, title: 'Ice Cream Shop Seasonal Checklists: Peak Season, Off-Season & Ice Cream Catering', desc: 'Peak season, off-season and ice cream catering.' },
  { key: 'personalizable', icon: FileEdit, title: 'Blank Ice Cream Shop Checklist Template (Editable)', desc: '3 blank templates: by area, by shift and by role.' },
  { key: 'apertura-negocio', icon: Building2, title: 'Ice Cream Parlor Opening & Closing Checklist (Whole Shop)', desc: 'The complete checklist to open and close the whole shop.' },
  { key: 'apertura-caja', icon: Wallet, title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log', desc: 'Starting bank, cash count, over/short against the Z report and the bank deposit.' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Ice Cream Shop Pre-Shift Meeting Template (Huddle Notes)', desc: 'Pre-shift huddle template: flavors to make, flavors running low, special orders, the team on shift and allergens.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Ice Cream Shop Seasonal Calendar & Flavor Planner (US)', desc: '12 months with key US dates, featured flavors and the season.' },
  { key: 'equivalents-guide', icon: Globe, title: 'US · UK · Canada · Australia Equivalents Guide', desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.' },
];

export default function IceCreamShopChecklistsKitDashboard() {
  const { token } = useAuth('ice-cream-shop-checklist-templates-jwt');
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
        <title>Ice Cream Shop Checklists Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/ice-cream-shop-checklist-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Ice Cream Shop Checklists Kit Pro
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
            Ice Cream Shop Checklists Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="ice-cream-shop-checklist-templates" lang="en" />
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

        <ProductChangelog productId="ice-cream-shop-checklist-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Complete your ice cream shop management toolkit
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/en/digital-products/coffee-shop-checklist-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Coffee Shop Checklists Kit Pro
              </a>
              <a
                href="/en/digital-products/restaurant-checklist-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Restaurant Checklists Kit Pro
              </a>
              <a
                href="/en/digital-products/food-cost-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Food Cost Kit Pro
              </a>
            </div>
          </div>
        </section>

        {/* ── Footer ───────────────────────────────────────── */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Ice Cream Shop Checklists Kit Pro · All rights reserved
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
