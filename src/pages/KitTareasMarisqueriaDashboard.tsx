import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  DoorOpen, Droplets, ShieldCheck, Snowflake,
  Briefcase, Users, ClipboardList, CalendarDays,
  Megaphone, Calendar,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const TEMPLATES = [
  { key: 'apertura-cierre', icon: DoorOpen, title: 'Apertura y Cierre Marisquería', desc: 'Vivero, expositor, cámaras, mise en place de salsas, montaje de sala con cubertería de marisco y cierre completo con arqueo.' },
  { key: 'vivero-lonjas', icon: Droplets, title: 'Vivero, Lonjas y Pescado Fresco', desc: 'Control diario del vivero (temperatura, oxígeno, salinidad, pH, densidad), compras en lonja e indicadores de frescura por especie.' },
  { key: 'trazabilidad-appcc', icon: ShieldCheck, title: 'Trazabilidad y APPCC Marisco', desc: 'Registro de lotes, etiquetado UE 1379/2013, zona FAO, método de captura, alérgenos de crustáceos y moluscos y puntos críticos HACCP.' },
  { key: 'expositor-barra', icon: Snowflake, title: 'Expositor y Barra de Mariscos', desc: 'Montaje del expositor de hielo, rotación FIFO, mantenimiento durante el servicio y apertura segura de ostras, navajas y almejas.' },
  { key: 'manager', icon: Briefcase, title: 'Tareas del Manager', desc: 'Pedidos en lonja, proveedores, food cost por especie, revenue diario, RRHH, administración y reporting semanal de mermas.' },
  { key: 'perfiles', icon: Users, title: 'Perfiles: Mariscador y Equipo', desc: 'Jefe de cocina/mariscador, partida de pescados, partida de mariscos, maître y camarero. Roles sin solapes.' },
  { key: 'semanales-mensuales', icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Limpieza profunda del vivero, inventarios, afilado de cuchillería de pescado, auditoría APPCC y evaluación de proveedores.' },
  { key: 'eventos-estacionales', icon: CalendarDays, title: 'Eventos y Temporadas', desc: 'Temporadas de pesca de España (percebes, gamba roja, centollo, bogavante), Navidad, Nochevieja, San Valentín y vedas oficiales.' },
  { key: 'plantilla-personalizable', icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco para adaptar checklists al concepto de tu marisquería (gallega, mediterránea, restaurante de pescado, gastrobar de mariscos).' },
  { key: 'bonus-briefing', icon: Megaphone, title: 'BONUS: Briefing de Servicio', desc: 'Briefing 5 min: capturas del día, alérgenos activos, reservas VIP, maridajes recomendados, avisos para barra y sala.' },
  { key: 'bonus-calendario', icon: Calendar, title: 'BONUS: Calendario Anual', desc: 'Año completo: temporadas de pesca por mes, vedas, eventos, mantenimientos del vivero, formación, cierres por vacaciones.' },
];

export default function KitTareasMarisqueriaDashboard() {
  const { token } = useAuth('kit-tareas-marisqueria-jwt');
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
        <title>Kit de Tareas Marisquería — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/kit-tareas-marisqueria" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Kit de Tareas Marisquería</a>
            <div className="flex items-center gap-2"><FileSpreadsheet className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Kit de Tareas <span className="text-[#FFD700]">Marisquería</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tus 11 checklists profesionales listos para descargar. Imprime, organiza y profesionaliza tu marisquería con vivero, expositor de hielo y trazabilidad APPCC.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">9 Checklists + 2 Bonus · Descarga Directa</p>
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
              <a href="/kit-tareas-chef-privado" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Tareas Chef Privado — €18</a>
              <a href="/pack-appcc" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Pack APPCC — €14</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Kit de Tareas Marisquería · Todos los derechos reservados</p>
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
