import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  UtensilsCrossed, Wine, CakeSlice, Truck, Coffee,
  BarChart3, Calculator, TrendingDown, ClipboardList, ChefHat, PartyPopper,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

// ── Template metadata (matches ContentGrid order) ───────────────
const TEMPLATES = [
  { key: 'estandar', icon: UtensilsCrossed, title: 'Escandallo Estándar', desc: 'Plantilla completa para platos a la carta con fórmulas automáticas.' },
  { key: 'degustacion', icon: ChefHat, title: 'Menú Degustación', desc: 'Para menús de 5 a 9 pases con resumen de coste global.' },
  { key: 'menu-dia', icon: ClipboardList, title: 'Menú del Día', desc: 'Primer plato, segundo, postre y extras con rotación semanal.' },
  { key: 'cocktails', icon: Wine, title: 'Cocktails y Bebidas', desc: 'Escandallos de cocktails con medidas exactas y merma de destilados.' },
  { key: 'pasteleria', icon: CakeSlice, title: 'Pastelería', desc: 'Mermas reales de pastelería y rendimiento por receta.' },
  { key: 'catering', icon: PartyPopper, title: 'Catering', desc: 'Materia prima + personal + logística en un solo presupuesto.' },
  { key: 'cafeteria', icon: Coffee, title: 'Cafetería / Brunch', desc: 'Food cost objetivo 25-30% con ejemplos reales de cafetería.' },
  { key: 'food-truck', icon: Truck, title: 'Food Truck', desc: 'Street food con punto de equilibrio diario incluido.' },
  { key: 'mermas', icon: TrendingDown, title: 'Control de Mermas', desc: 'Registro semanal de mermas en 16 categorías de producto.' },
  { key: 'calculadora-pvp', icon: Calculator, title: 'Calculadora de PVP', desc: 'PVP recomendado para 9 tipos de establecimiento.' },
  { key: 'dashboard', icon: BarChart3, title: 'Dashboard Mensual', desc: 'Seguimiento de food cost durante 12 meses consecutivos.' },
  { key: 'bonus-mermas', icon: TrendingDown, title: 'BONUS: Mermas + Inventario', desc: 'Plantilla avanzada de control de mermas con inventario integrado.' },
];

export default function KitEscandallosDashboard() {
  const { token } = useAuth('kit-escandallos-jwt');
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
        <title>Kit de Escandallos Pro — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>

      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        {/* ── Top bar ────────────────────────────────────────── */}
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/kit-escandallos" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm">
              <ArrowLeft className="w-4 h-4" />
              Kit de Escandallos
            </a>
            <div className="flex items-center gap-2">
              <FileSpreadsheet className="w-5 h-5 text-[#FFD700]" />
              <span className="text-white font-bold text-sm">Tu Dashboard</span>
            </div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">
              aichef.pro
            </a>
          </div>
        </header>

        {/* ── Hero ───────────────────────────────────────────── */}
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">
            Kit de Escandallos <span className="text-[#FFD700]">Pro</span>
          </h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">
            Tus 11 plantillas Excel profesionales listas para descargar.
            Acceso de por vida — incluye futuras actualizaciones.
          </p>
        </section>

        {/* ── Downloads grid ────────────────────────────────── */}
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">
              11 Plantillas + 1 Bonus · Descarga Directa
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
                        Descargar
                      </a>
                    ) : (
                      <span className="text-gray-500 text-sm">Disponible pronto</span>
                    )}
                  </div>
                );
              })}
            </div>

            {/* ── Tip banner ───────────────────────────────── */}
            <div className="mt-8 bg-white/5 border border-white/10 rounded-xl p-6 text-center">
              <p className="text-white font-semibold mb-1">
                Compatibles con Excel, Google Sheets, LibreOffice y Numbers
              </p>
              <p className="text-gray-400 text-sm">
                Descarga los archivos .xlsx y ábrelos con tu programa favorito. Todas las fórmulas se mantienen.
              </p>
            </div>
          </div>
        </section>

        {/* ── Cross-sell banner ─────────────────────────────── */}
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center">
            <p className="text-gray-400 text-sm mb-3">
              Domina la IA en hostelería con 300+ prompts curados
            </p>
            <a
              href="/pro-prompts-ebook"
              className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm"
            >
              Ver Pro Prompts eBook — €9
            </a>
          </div>
        </section>

        {/* ── Footer ───────────────────────────────────────── */}
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">
              © 2026 AI Chef Pro · Kit de Escandallos Pro · Todos los derechos reservados
            </p>
            <div className="flex flex-wrap items-center justify-center gap-2 md:gap-4 text-sm">
              <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">aichef.pro</a>
              <span className="text-gray-700 hidden md:inline">·</span>
              <a href="mailto:info@aichef.pro" className="text-gray-500 hover:text-[#FFD700] transition-colors">Contacto</a>
            </div>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
