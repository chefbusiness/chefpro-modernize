import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, ArrowLeft,
  BookOpen, FileText, Calculator,
  Scale, Users, BarChart3, Calendar,
  ChefHat, ShieldCheck, Wrench, Layout,
  Megaphone, Briefcase, Star, Utensils, Flame,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const SECTIONS = [
  {
    title: 'Guía Principal',
    templates: [
      { key: 'guia-pdf', icon: BookOpen, title: 'Guía Completa (PDF)', desc: '20 capítulos, 60+ páginas. Diseño editorial profesional.', ext: '.pdf' },
      { key: 'guia-docx', icon: FileText, title: 'Guía Completa (DOCX Editable)', desc: 'Mismo contenido en formato editable. Personaliza y presenta.', ext: '.docx' },
    ],
  },
  {
    title: 'Plantillas Excel (9)',
    templates: [
      { key: 'plan-financiero', icon: Calculator, title: 'Plan Financiero 3 Años', desc: 'Inversión, P&L mensual y proyección a 3 años con fórmulas.', ext: '.xlsx' },
      { key: 'calculadora-capex', icon: Calculator, title: 'Calculadora CAPEX', desc: 'Desglose inversión 280K-520K€: obra, cocina nikkei, sala, barra pisco/sake.', ext: '.xlsx' },
      { key: 'pl-mensual', icon: BarChart3, title: 'P&L Mensual con 3 Escenarios', desc: 'Pesimista, realista y optimista con costes fijos y variables.', ext: '.xlsx' },
      { key: 'cash-flow', icon: Calculator, title: 'Cash Flow y Break-Even', desc: '12 meses de cash flow + punto de equilibrio automático.', ext: '.xlsx' },
      { key: 'escandallo-maestro', icon: Flame, title: 'Escandallos: 15 Recetas Nikkei', desc: 'Tiradito, ceviche nikkei, causa, maki acevichado, tataki, anticucho, chaufa mariscos y más.', ext: '.xlsx' },
      { key: 'menu-engineering', icon: BarChart3, title: 'Menú Engineering Matrix', desc: 'Clasificación Stars/Plowhorses/Puzzles/Dogs automática.', ext: '.xlsx' },
      { key: 'calculadora-ticket', icon: Utensils, title: 'Calculadora Ticket Medio', desc: 'Simulador con margen de pisco, sake y coctelería nikkei incluido.', ext: '.xlsx' },
      { key: 'cronograma-gantt', icon: Calendar, title: 'Cronograma Apertura Gantt 12 Meses', desc: '28 tareas con fases específicas (chef nikkei, anisakis, importación peruana).', ext: '.xlsx' },
      { key: 'plantilla-turnos', icon: Users, title: 'Plantilla Turnos Brigada', desc: 'Cuadrante semanal para 16 personas (chef, itamae, robata, cold station, hot kitchen).', ext: '.xlsx' },
    ],
  },
  {
    title: 'Checklists (6)',
    templates: [
      { key: 'checklist-legal', icon: Scale, title: 'Checklist Legal Completo', desc: '42 trámites: licencias, anisakis, importación, registro sanitario.', ext: '.xlsx' },
      { key: 'checklist-equipamiento', icon: Wrench, title: 'Checklist Equipamiento Cocina Nikkei', desc: '36 ítems: vitrina sashimi, robata/josper, wok station, licuadoras leche de tigre, yanagiba, molcajete.', ext: '.xlsx' },
      { key: 'checklist-appcc', icon: ShieldCheck, title: 'Checklist APPCC (Pescado Crudo + Leche de Tigre)', desc: '46 prerrequisitos: anisakis tiraditos, cadena frío leches de tigre, shari, alérgenos.', ext: '.xlsx' },
      { key: 'checklist-sala', icon: Layout, title: 'Checklist Diseño Sala Nikkei', desc: '32 ítems: madera japonesa, textiles peruanos, cerámica Chulucanas, barra tiraditos, barra pisco/sake.', ext: '.xlsx' },
      { key: 'checklist-contratacion', icon: Users, title: 'Checklist Contratación', desc: '31 ítems: chef nikkei, itamae, parrillero robata, cold station, sommelier pisco/sake.', ext: '.xlsx' },
      { key: 'checklist-marketing', icon: Megaphone, title: 'Checklist Marketing Pre-Apertura', desc: '31 acciones: Día del Pisco Sour, Fiestas Patrias Perú, fotos premium, delivery.', ext: '.xlsx' },
    ],
  },
  {
    title: 'Documentos Modelo (2)',
    templates: [
      { key: 'business-plan', icon: Briefcase, title: 'Business Plan Modelo', desc: 'Plantilla rellenable para presentar a bancos e inversores.', ext: '.docx' },
      { key: 'manual-operaciones', icon: ChefHat, title: 'Manual de Operaciones Nikkei', desc: 'Barra tiraditos, cold station leche de tigre, robata, hot kitchen, barra pisco/sake, protocolo anisakis, delivery.', ext: '.docx' },
    ],
  },
];

export default function GuiaRestauranteNikkeiDashboard() {
  const { token } = useAuth('guia-restaurante-nikkei-jwt');
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
        <title>Guía Restaurante Nikkei — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/guia-restaurante-nikkei" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Guía Restaurante Nikkei</a>
            <div className="flex items-center gap-2"><Star className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Restaurante <span className="text-[#FFD700]">Nikkei</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu guía completa + 17 herramientas listas para descargar.</p>
        </section>

        {SECTIONS.map((section) => (
          <section key={section.title} className="pb-12 px-4">
            <div className="max-w-5xl mx-auto">
              <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-4">{section.title}</p>
              <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {section.templates.map((tpl) => {
                  const Icon = tpl.icon;
                  const url = files[tpl.key];
                  return (
                    <div key={tpl.key} className="rounded-xl p-5 bg-white/5 border border-white/10 hover:border-[#FFD700]/30 transition-all">
                      <div className="flex items-start gap-3 mb-3">
                        <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0"><Icon className="w-5 h-5 text-[#FFD700]" /></div>
                        <div><h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3><p className="text-gray-500 text-xs mt-0.5">{tpl.ext}</p></div>
                      </div>
                      <p className="text-gray-400 text-sm mb-4 leading-relaxed">{tpl.desc}</p>
                      {loading ? <Loader2 className="w-5 h-5 text-gray-500 animate-spin" /> : url ? (
                        <a href={url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-bold border border-[#FFD700]/50 text-[#FFD700] hover:bg-[#FFD700]/10 transition-all">
                          <Download className="w-4 h-4" />Descargar
                        </a>
                      ) : <span className="text-gray-500 text-sm">Disponible pronto</span>}
                    </div>
                  );
                })}
              </div>
            </div>
          </section>
        ))}

        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">¿Ya tienes la guía? Completa tu toolkit</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/guia-restaurante-peruano" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Guía Restaurante Peruano — 65 EUR</a>
              <a href="/kit-plan-financiero" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Kit Plan Financiero — 39 EUR</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Guía Restaurante Nikkei · Todos los derechos reservados</p>
          </div>
        </footer>
        <WhatsAppProductSupport />
      </div>
    </>
  );
}
