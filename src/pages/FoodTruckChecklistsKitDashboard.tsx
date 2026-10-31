import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  Truck, Wrench, ShieldCheck, MapPin,
  Users, UserCog, ClipboardList, PartyPopper,
  Calendar, CalendarDays,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Food Truck Checklists Kit Pro (tienda EN) — COPIA TRADUCIDA de KitTareasFoodTruckDashboard.tsx con la maqueta de sus
// hermanos EN (TacoShopChecklistsKitDashboard.tsx): mismos componentes compartidos con lang="en".
// Las claves (`key`), los iconos y el ORDEN son los MISMOS que el ES kit-tareas-food-truck y que la entrada
// `food-truck-checklist-templates` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza); la guía
// ES↔LatAm (`guia-equivalencias`) la sustituye el bonus común EN (`equivalents-guide`).
// Títulos = los de los xlsx EN (SPEC checklists-kit/foodtruck §2). Venta cruzada a la tienda EN (el ES cruza a Kit Tareas
// Restaurante, Kit Tareas Bar y Pack APPCC → Food Truck Business Plan Kit, Restaurant Checklists Kit Pro y HACCP Food
// Safety Kit Pro). Fuera lo que el dashboard ES afirma y el kit EN no trae (vitrina, ITV, «reporting con KPIs»,
// «reservas privadas», «acciones de marketing por estación» como tal: el calendario trae una columna Marketing por mes).
// Molde plano: sin contador, sin instrucciones, sin protección. Sin Google Sheets hasta que el test real lo confirme.

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'setup-teardown', icon: Truck, title: "Food Truck Setup & Teardown Checklist: Arrival, Kitchen, Service & Closing", desc: "Arrival, kitchen, window and teardown: generator, propane, cold equipment, POS, water tanks, leftovers, the cash close-out and the truck secured for the road." },
  { key: 'operaciones-moviles-vehiculo', icon: Wrench, title: "Food Truck Pre-Trip & Vehicle Checklist: Generator, Propane, Water & Waste", desc: "The pre-trip check: fuel, tires, lights, registration, extinguishers, generator, propane leak test, fresh and wastewater tanks and waste." },
  { key: 'appcc-seguridad-alimentaria-movil', icon: ShieldCheck, title: "Food Truck Food Safety & Health Inspection Prep Checklist (FDA Food Code)", desc: "Temperatures in transit and on arrival, cooking and hot holding in °F, handwashing, test strips, the 9 major allergens and the inspector's paperwork." },
  { key: 'permisos-eventos-localizaciones', icon: MapPin, title: "Food Truck Permits, Events & Locations Checklist", desc: "Mobile vending license, health permit, commissary agreement, insurance and COI, sales tax, pre-event checks and 6 event types." },
  { key: 'tareas-manager', icon: Users, title: "Food Truck Manager Checklist: Route, Inventory, Food Cost & Marketing", desc: "Weekly route, event bookings, orders, waste, sales by spot, food cost, ROI per event, cash reconciliation, social media and reviews." },
  { key: 'tareas-perfiles', icon: UserCog, title: "Food Truck Duties by Role: Chef, Prep Cook, Window Staff & Driver", desc: "Food truck chef, prep cook, window staff and driver / tech: 5 tasks each, no overlaps." },
  { key: 'semanales-mensuales', icon: ClipboardList, title: "Food Truck Weekly & Monthly Checklists: Deep Cleaning, Maintenance & Inventory", desc: "Weekly deep clean, hood filters, inventory, fryer oil, propane and water tanks; monthly generator, brakes and tires, logs, food cost and permits." },
  { key: 'eventos-estacionales', icon: PartyPopper, title: "Food Truck Event & Seasonal Checklists: Festivals, Fairs, Markets & Weddings", desc: "The season from spring rallies to the summer peak, plus festivals, farmers and night markets, county fairs, wedding season and New Year's Eve." },
  { key: 'plantilla-personalizable', icon: FileSpreadsheet, title: "Blank Food Truck Checklist Template (Editable)", desc: "A blank checklist with the kit's columns to build lists for your exact truck and menu." },
  { key: 'bonus-briefing-pre-evento', icon: Calendar, title: "BONUS: Food Truck Pre-Event Briefing Template", desc: "15 fields before each event: the event, logistics (power, water, parking, vendor fee), menu and stock, and the crew." },
  { key: 'bonus-calendario-anual', icon: CalendarDays, title: "BONUS: Food Truck Annual Calendar: Events, Menu, Maintenance & Marketing (US)", desc: "12 months of US events, a suggested menu, the truck's maintenance and the month's marketing." },
  { key: 'equivalents-guide', icon: Globe, title: "US · UK · Canada · Australia Equivalents Guide", desc: "Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia." },
];

export default function FoodTruckChecklistsKitDashboard() {
  const { token } = useAuth('food-truck-checklist-templates-jwt');
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
        <title>Food Truck Checklists Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/food-truck-checklist-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Food Truck Checklists Kit Pro
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
            Food Truck Checklists Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="food-truck-checklist-templates" lang="en" />
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

        <ProductChangelog productId="food-truck-checklist-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Complete your food truck management toolkit
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/en/digital-products/food-truck-business-plan"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Food Truck Business Plan Kit
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
              © 2026 AI Chef Pro · Food Truck Checklists Kit Pro · All rights reserved
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
