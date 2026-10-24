import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  DoorOpen, Croissant, ClipboardList, Users,
  CalendarDays, PartyPopper, FileEdit, Megaphone, Calendar, Building2, Wallet,
  CalendarRange, Cake, ShieldAlert, Thermometer,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Pastry Shop Checklists Kit Pro (tienda EN) — COPIA TRADUCIDA de KitTareasPasteleriaDashboard.tsx con la maqueta
// de sus hermanos EN (PastryShopChecklistsKitDashboard.tsx): mismos componentes compartidos con lang="en".
// Las claves (`key`), los iconos y el ORDEN son los MISMOS que el ES kit-tareas-pasteleria (13 plantillas: la 02 es
// `partidas`; 10-13 = plan-produccion, encargos, alergenos, temperaturas) y que la entrada
// `pastry-shop-checklist-templates` de netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza); la
// guía ES↔LatAm (`guia-equivalencias`) la sustituye el bonus común EN (`equivalents-guide`). Títulos = los de los xlsx
// EN (SPEC checklists-kit/pastry §2, D5). Sin la marca «NUEVO v2.0» del ES (es la primera edición inglesa). Venta
// cruzada a la tienda EN (el ES cruza a Kit Tareas Restaurante, Kit Tareas Cafetería y Kit Escandallos → Chocolate Shop
// Checklists, How to Open a Pastry Shop y Food Cost Kit Pro: el hermano de postre más cercano —muchas pastelerías hacen
// bombones—, la guía EN de la misma familia y el gemelo EN de Escandallos; el Coffee Shop y el Ice Cream Shop quedan en
// el pie de la landing). Compatibilidad: sin Google Sheets hasta que el test real lo confirme (SPEC checklists-kit §9).

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'apertura-cierre', icon: DoorOpen, title: 'Pastry Kitchen & Bakery Case Opening and Closing Checklists', desc: '2 checklists (kitchen opening and closing) with 6 blocks and 42 tasks: equipment, kitchen setup and the bakery case.' },
  { key: 'partidas', icon: Croissant, title: 'Pastry Kitchen Production Checklists: Doughs, Creams & Fillings, Decorating', desc: 'Doughs and fermentation, creams and fillings, decorating and the bakery case.' },
  { key: 'manager', icon: ClipboardList, title: 'Pastry Shop Manager Checklist: Daily, Weekly, Monthly & Shift Handover', desc: 'Daily, weekly and monthly + a shift handover.' },
  { key: 'perfiles', icon: Users, title: 'Pastry Chef Duties by Role: Head Pastry Chef, Pastry Cook, Assistant & Counter', desc: 'Head pastry chef, pastry cook, pastry assistant and counter associate.' },
  { key: 'periodicas', icon: CalendarDays, title: 'Bakery Cleaning Schedule, Equipment Maintenance & Weekly Inventory', desc: 'Weekly deep clean, FIFO, oven and mixer maintenance and a weekly inventory.' },
  { key: 'eventos', icon: PartyPopper, title: 'Pastry Shop Holiday & Event Checklists: Holidays, Valentine\'s, Easter, Mother\'s Day, Celebration Cakes & Thanksgiving', desc: 'Holiday season and Three Kings Day, Valentine\'s Day, Easter, Mother\'s and Father\'s Day, celebration cakes and Thanksgiving, each with its wrap-up.' },
  { key: 'personalizable', icon: FileEdit, title: 'Blank Pastry Shop Checklist Template (Editable)', desc: '3 blank templates to build your own.' },
  { key: 'apertura-negocio', icon: Building2, title: 'Pastry Shop Opening & Closing Checklist (Whole Shop)', desc: 'Shop and bakery case: case temperatures, labels, today\'s custom orders, leftovers and final checks.' },
  { key: 'apertura-caja', icon: Wallet, title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log', desc: 'Starting bank, cash count by denomination, over/short against the Z report and a monthly cash log.' },
  { key: 'plan-produccion', icon: CalendarRange, title: 'Bakery Production Schedule & Waste Log: Weekly Plan, Made vs. Sold & Summary', desc: 'Planned units by item and day (Mon–Sun), made vs. sold, waste in % and in your currency, and a weekly summary.' },
  { key: 'encargos', icon: Cake, title: 'Cake Order Form & Custom Order Log: Order Form, Log, Pickups & Today\'s Orders', desc: 'Printable cake order form with allergens, deposit and balance due, a monthly order log and a pickup schedule.' },
  { key: 'alergenos', icon: ShieldAlert, title: 'Bakery Allergen Chart (9 Major Allergens, UK 14): Matrix, Chart, Case Sign & Labels', desc: 'Starter matrix with 43 items (to check against your recipes and spec sheets), allergen chart, case sign and case labels.' },
  { key: 'temperaturas', icon: Thermometer, title: 'Food Temperature Log, Receiving Log, Prep Labels & Shelf Life Chart', desc: 'Monthly temperature log by unit, receiving log with rejection criteria, prep labels and a shelf-life chart in °F.' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Pastry Shop Pre-Shift Meeting Template (Huddle Notes)', desc: 'Pre-shift huddle template for the pastry kitchen.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Pastry Shop Holiday & Events Calendar (US)', desc: '17 key dates and occasions for a US pastry shop.' },
  { key: 'equivalents-guide', icon: Globe, title: 'US · UK · Canada · Australia Equivalents Guide', desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.' },
];

export default function PastryShopChecklistsKitDashboard() {
  const { token } = useAuth('pastry-shop-checklist-templates-jwt');
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
        <title>Pastry Shop Checklists Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/pastry-shop-checklist-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Pastry Shop Checklists Kit Pro
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
            Pastry Shop Checklists Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="pastry-shop-checklist-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 13 templates + 3 bonuses, ready to download. Print, delegate and keep control.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              13 Templates + 3 Bonuses · Direct Download
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

        <ProductChangelog productId="pastry-shop-checklist-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Complete your pastry shop management toolkit
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/en/digital-products/chocolate-shop-checklist-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Chocolate Shop Checklists Kit Pro
              </a>
              <a
                href="/en/digital-products/how-to-open-a-pastry-shop"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See How to Open a Pastry Shop
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
              © 2026 AI Chef Pro · Pastry Shop Checklists Kit Pro · All rights reserved
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
