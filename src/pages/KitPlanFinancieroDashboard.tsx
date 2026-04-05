import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  TrendingUp, Target, Wallet, Building2, BarChart3,
  PieChart, FileText, Shuffle, ClipboardList,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const TEMPLATES = [
  { key: 'plan-previsional', icon: TrendingUp, title: 'Plan Financiero Previsional (3 Años)', desc: 'Proyección ingresos y gastos a 3 años con gráficos automáticos.' },
  { key: 'plan-previsional-5', icon: TrendingUp, title: 'Plan Financiero Previsional (5 Años)', desc: 'Proyección a 5 años — ideal para bancos, inversores y franquicias.' },
  { key: 'break-even', icon: Target, title: 'Calculadora Punto de Equilibrio', desc: 'Ticket medio, comensales/día y 3 escenarios.' },
  { key: 'cash-flow', icon: Wallet, title: 'Cash Flow Forecast (12 Meses)', desc: 'Flujo de caja con alertas de liquidez.' },
  { key: 'capex', icon: Building2, title: 'Presupuesto de Inversion / CAPEX', desc: 'Desglose por partida con desviacion real vs presupuesto.' },
  { key: 'pyl', icon: BarChart3, title: 'P&L Mensual Real vs Presupuesto', desc: 'Desviaciones con semaforo y ratios automaticos.' },
  { key: 'ratios', icon: PieChart, title: 'Dashboard de Ratios Financieros', desc: 'Food cost, labor cost, prime cost, GOP, RevPASH.' },
  { key: 'viabilidad', icon: FileText, title: 'Informe de Viabilidad para Bancos', desc: 'TIR, VAN, payback period. Formato profesional.' },
  { key: 'bonus-simulador', icon: Shuffle, title: 'BONUS: Simulador de Escenarios', desc: 'What-if con 3 escenarios comparados.' },
  { key: 'bonus-checklist', icon: ClipboardList, title: 'BONUS: Checklist Pre-Apertura', desc: '48 items en 6 fases financieras.' },
];

export default function KitPlanFinancieroDashboard() {
  const { token } = useAuth('kit-plan-financiero-jwt');
  const [files, setFiles] = useState<Record<string, string>>({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    fetch('/.netlify/functions/get-download-urls', { headers: { Authorization: `Bearer ${token}` } })
      .then((r) => r.json())
      .then((data) => { if (data.files) setFiles(data.files); })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, [token]);

  return (
    <>
      <Helmet>
        <title>Kit Plan Financiero para Restaurantes — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/kit-plan-financiero" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Kit Plan Financiero</a>
            <div className="flex items-center gap-2"><FileSpreadsheet className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Plan <span className="text-[#FFD700]">Financiero</span> para Restaurantes</h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tus 10 plantillas financieras listas para descargar. Planifica, controla y presenta.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">8 Plantillas + 2 Bonus · Descarga Directa</p>
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {TEMPLATES.map((tpl, i) => {
                const Icon = tpl.icon;
                const url = files[tpl.key];
                const isPrimary = i === 0;
                return (
                  <div key={tpl.key} className={`rounded-xl p-5 transition-all ${isPrimary ? 'bg-white/5 border-2 border-[#FFD700]/50' : 'bg-white/5 border border-white/10 hover:border-[#FFD700]/30'}`}>
                    <div className="flex items-start gap-3 mb-3">
                      <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0"><Icon className="w-5 h-5 text-[#FFD700]" /></div>
                      <div><h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3><p className="text-gray-500 text-xs mt-0.5">.xlsx</p></div>
                    </div>
                    <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>
                    {loading ? <Loader2 className="w-5 h-5 text-gray-500 animate-spin" /> : url ? (
                      <a href={url} target="_blank" rel="noopener noreferrer" className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold transition-all ${isPrimary ? 'bg-[#FFD700] text-black hover:bg-[#FFD700]/90' : 'border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10'}`}>
                        <Download className="w-4 h-4" />Descargar
                      </a>
                    ) : <span className="text-gray-500 text-sm">Disponible pronto</span>}
                  </div>
                );
              })}
            </div>
            <div className="mt-8 bg-white/5 border border-white/10 rounded-xl p-6 text-center">
              <p className="text-white font-semibold mb-1">Compatibles con Excel, Google Sheets, LibreOffice, Numbers + Imprimible A4</p>
              <p className="text-gray-400 text-sm">Descarga los archivos .xlsx y abrelos con tu programa favorito.</p>
            </div>
          </div>
        </section>
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Completa tu toolkit de gestion hostelera</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-escandallos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit de Escandallos — 12 EUR</a>
              <a href="/kit-inventario" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Inventario — 14 EUR</a>
              <a href="/kit-gestion-personal" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Gestion Personal — 14 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Kit Plan Financiero · Todos los derechos reservados</p>
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
