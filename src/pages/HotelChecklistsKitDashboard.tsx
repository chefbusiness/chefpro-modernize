import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, ArrowLeft,
  Sunrise, ConciergeBell, ClipboardList, UtensilsCrossed,
  PartyPopper, Megaphone, Calendar, Bed, Building2, Waves,
  Sun, Wrench, BarChart3, Sparkles, Users, Wallet,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// Hotel Checklists Kit Pro (tienda EN) — COPIA TRADUCIDA de KitTareasHotelDashboard.tsx con la maqueta de sus hermanos EN
// (IceCreamShopChecklistsKitDashboard.tsx): mismos componentes compartidos con lang="en". Las claves (`key`), los iconos
// y el ORDEN son los MISMOS que el ES kit-tareas-hotel y que la entrada `hotel-checklist-templates` de
// netlify/functions/get-download-urls.ts (gate-flujo-postpago.py las cruza); la guía ES↔LatAm (`guia-equivalencias`) la
// sustituye el bonus común EN (`equivalents-guide`). Títulos = los de los xlsx EN (SPEC checklists-kit/hotel §2, D5). El
// ES cruza a Kit Tareas Restaurante, Catering y Escandallos → Restaurant Checklists, Catering Checklists y Food Cost Kit
// Pro. Fuera lo que el dashboard ES afirma y el kit no trae ("20 fechas clave": son 24). Compatibilidad: sin Google
// Sheets hasta que el test real lo confirme (SPEC checklists-kit §9).

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'fb-buffet-desayuno', icon: Sunrise, title: 'Hotel Breakfast Buffet Checklists: Setup, Service & Closing', desc: 'Breakfast buffet opening and closing: kitchen start-up, setup, restocking and breakdown.' },
  { key: 'fb-buffet-comida-cena', icon: UtensilsCrossed, title: 'Hotel Lunch & Dinner Buffet Checklists', desc: 'Lunch and dinner buffet: station setup, restocking, show cooking, temperatures and closing.' },
  { key: 'fb-restaurante-carte', icon: ClipboardList, title: 'Hotel Restaurant Opening & Closing Checklists (À la Carte)', desc: 'Opening (reservations, setup, briefing) and closing.' },
  { key: 'fb-outlets', icon: ConciergeBell, title: 'Hotel Bar & Outlet Checklists: Pool Bar, Lobby Bar & Grab-and-Go', desc: 'Pool bar, lobby bar and lounge, and snack bar and grab-and-go.' },
  { key: 'fb-room-service-minibar', icon: ConciergeBell, title: 'In-Room Dining (Room Service) & Minibar Checklists', desc: 'Order to delivery to pickup, plus minibar restocking.' },
  { key: 'fb-banquetes-eventos', icon: PartyPopper, title: 'Hotel Banquet & Event Checklist: From BEO to Breakdown', desc: 'Weddings, conferences and galas: BEO, room setup, AV, service timing and breakdown.' },
  { key: 'recepcion-turnos', icon: Building2, title: 'Hotel Front Desk Checklists: AM, PM & Night Audit Shifts, Check-In & Check-Out', desc: 'AM, PM and night audit shifts, plus the check-in and check-out procedure.' },
  { key: 'guest-services', icon: Users, title: 'Concierge & Guest Experience Checklists', desc: 'Concierge, VIP arrivals, reviews and loyalty.' },
  { key: 'housekeeping', icon: Bed, title: 'Hotel Housekeeping Checklists: Checkout & Stayover Room Cleaning, Turndown, Deep Cleaning & Linen', desc: 'Checkout and stayover cleaning, turndown service, weekly deep cleaning and linen control.' },
  { key: 'areas-publicas', icon: Building2, title: 'Hotel Public Area Cleaning Checklists: Lobby, Corridors & Elevators, Restrooms & Parking', desc: 'Lobby, corridors and elevators, public restrooms and parking.' },
  { key: 'piscina', icon: Waves, title: 'Hotel Pool Checklists: Daily Opening & Closing, Weekly Maintenance & Towel Service', desc: 'Daily opening and closing, weekly maintenance and towel service.' },
  { key: 'terraza', icon: Sun, title: 'Hotel Patio & Terrace Checklists: Seasonal Setup & Daily Service', desc: 'Seasonal setup plus daily service: furniture, umbrellas, cleaning and menu.' },
  { key: 'mantenimiento', icon: Wrench, title: 'Hotel Preventive Maintenance Checklists: Daily Rounds to Annual, HVAC, Plumbing & Electrical', desc: 'Daily, weekly, monthly, quarterly and annual rounds, plus HVAC, plumbing and electrical.' },
  { key: 'administracion', icon: BarChart3, title: 'Hotel Back-Office Checklists: Revenue Management, Reservations, Accounting & HR', desc: 'Revenue management, reservations, accounting and HR operations.' },
  { key: 'spa-wellness', icon: Sparkles, title: 'Hotel Spa & Wellness Checklists: Opening, Closing, Treatment Rooms & Locker Rooms', desc: 'Opening and closing, treatment rooms and locker rooms.' },
  { key: 'apertura-negocio', icon: Building2, title: 'Hotel Daily Opening & Closing Rounds: F&B Outlets & Public Areas', desc: 'Opening and closing rounds for the F&B outlets and public areas, with who does it and due-by times.' },
  { key: 'apertura-caja', icon: Wallet, title: 'Cash Drawer Opening & Closing: Count Sheet, Z Report & Over/Short Log', desc: 'Starting bank, cash count, over/short against the Z report and the monthly log.' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Hotel Daily F&B Briefing Template (Stand-Up Notes)', desc: 'Daily stand-up template: occupancy, VIPs, the menu of the day, the team and allergens.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Hotel F&B Calendar: 24 Key Dates & Seasons (US)', desc: '24 key US dates and seasons for hotel F&B, with the recommended lead time.' },
  { key: 'equivalents-guide', icon: Globe, title: 'US · UK · Canada · Australia Equivalents Guide', desc: 'Bonus: terms, taxes, food safety, staff rules, alcohol and units for using this kit in the US, UK, Canada and Australia.' },
];

export default function HotelChecklistsKitDashboard() {
  const { token } = useAuth('hotel-checklist-templates-jwt');
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
        <title>Hotel Checklists Kit Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner lang="en" />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/en/digital-products/hotel-checklist-templates" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Hotel Checklists Kit Pro
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
            Hotel Checklists Kit <span className="text-[#FFD700]">Pro</span>
          </h1>
          <div className="mb-3">
            <ProductVersionBadge productId="hotel-checklist-templates" lang="en" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Your 19 templates, ready to download. Print, delegate and keep control.
            Lifetime access — future updates included.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              17 Checklists + 2 Bonuses + Guide · Direct Download
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

        <ProductChangelog productId="hotel-checklist-templates" lang="en" />
        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Complete your hotel management toolkit
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a
                href="/en/digital-products/catering-checklist-templates"
                className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
              >
                See Catering Checklists Kit Pro
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
              © 2026 AI Chef Pro · Hotel Checklists Kit Pro · All rights reserved
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
