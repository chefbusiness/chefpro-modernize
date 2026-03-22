import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  Sunrise, ConciergeBell, ClipboardList, UtensilsCrossed,
  PartyPopper, Megaphone, Calendar, Bed, Building2, Waves,
  Sun, Wrench, BarChart3, Sparkles, Users,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const TEMPLATES = [
  { key: 'fb-buffet-desayuno', icon: Sunrise, title: 'Buffet Desayuno', desc: 'Apertura y cierre completo del buffet de desayuno.' },
  { key: 'fb-buffet-comida-cena', icon: UtensilsCrossed, title: 'Buffet Almuerzo / Cena', desc: 'Montaje, reposición, show cooking, cierre.' },
  { key: 'fb-restaurante-carte', icon: ClipboardList, title: 'Restaurante À la Carte', desc: 'Apertura (reservas, montaje, briefing) y cierre.' },
  { key: 'fb-outlets', icon: ConciergeBell, title: 'Pool Bar · Lobby · Snack', desc: 'Checklists para pool bar, lobby bar y snack bar.' },
  { key: 'fb-room-service-minibar', icon: ConciergeBell, title: 'Room Service + Minibar', desc: 'Pedido→entrega→recogida + minibar reposición.' },
  { key: 'fb-banquetes-eventos', icon: PartyPopper, title: 'Banquetes y Eventos', desc: 'Bodas, convenciones, galas, BEO, desmontaje.' },
  { key: 'recepcion-turnos', icon: Building2, title: 'Recepción — 3 Turnos', desc: 'Mañana, tarde, noche + check-in/out protocolo.' },
  { key: 'guest-services', icon: Users, title: 'Guest Services', desc: 'Conserjería + guest experience / fidelización.' },
  { key: 'housekeeping', icon: Bed, title: 'Housekeeping', desc: 'Checkout, estancia, turndown, deep clean, lencería.' },
  { key: 'areas-publicas', icon: Building2, title: 'Áreas Públicas', desc: 'Lobby, pasillos, baños públicos, parking.' },
  { key: 'piscina', icon: Waves, title: 'Piscina', desc: 'Apertura/cierre, mantenimiento semanal, toallas.' },
  { key: 'terraza', icon: Sun, title: 'Terraza', desc: 'Montaje temporada + servicio diario.' },
  { key: 'mantenimiento', icon: Wrench, title: 'Mantenimiento', desc: 'Diario, semanal, mensual, HVAC, fontanería, electricidad.' },
  { key: 'administracion', icon: BarChart3, title: 'Administración', desc: 'Revenue, reservas, contabilidad, RRHH.' },
  { key: 'spa-wellness', icon: Sparkles, title: 'Spa / Wellness', desc: 'Apertura/cierre, cabinas, vestuarios.' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Briefing Diario F&B', desc: 'Ocupación, VIPs, menú del día, equipo, incidencias.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Calendario Anual', desc: '20 fechas clave F&B hotelero con antelación.' },
];

export default function KitTareasHotelDashboard() {
  const { token } = useAuth('kit-tareas-hotel-jwt');
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
        <title>Kit de Tareas Hotel F&B — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/kit-tareas-hotel" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Kit de Tareas Hotel</a>
            <div className="flex items-center gap-2"><FileSpreadsheet className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Kit de Tareas <span className="text-[#FFD700]">Hotel F&B / Buffet</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tus 46 checklists en 15 plantillas + 2 bonus listos para descargar. Imprime, delega y controla.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">15 Plantillas + 2 Bonus · 46 Checklists · Descarga Directa</p>
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
              <p className="text-gray-400 text-sm">Descarga los archivos .xlsx y ábrelos con tu programa favorito.</p>
            </div>
          </div>
        </section>
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Completa tu toolkit de gestión hostelera</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-tareas" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Tareas Restaurante — €14</a>
              <a href="/kit-tareas-catering" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Tareas Catering — €12</a>
              <a href="/kit-escandallos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit de Escandallos Pro — €12</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Kit de Tareas Hotel F&B · Todos los derechos reservados</p>
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
