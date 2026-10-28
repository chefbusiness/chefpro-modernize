import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft,
  Calculator, ScrollText,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const TEMPLATES = [
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Plan Financiero Excel',
    desc: '9 hojas con fórmulas vivas: supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios pesimista/realista/optimista, personal, tesorería mes a mes, financiación con cuadro de amortización e instrucciones.',
  },
  {
    key: 'plan-negocio',
    icon: FileText,
    type: '.docx',
    title: 'Plan de Negocio (Word)',
    desc: 'Documento Word de 10 secciones: resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, organización y personal, plan financiero, aspectos legales y plan de acción, con las tres configuraciones de inversión.',
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Checklist de Apertura (80 tareas)',
    desc: '80 tareas en 6 fases: constitución; vehículo y sanidad; equipo y proveedores; personal y formación; marca y captación; y primer evento y primeros 90 días.',
  },
  {
    key: 'calculadora-pricing',
    icon: Calculator,
    type: '.xlsx',
    title: 'Calculadora de Escandallo y Presupuesto',
    desc: '4 hojas: escandallo de tus bebidas, logística y precio por invitado según los invitados y las horas, cobro y cancelación por tramos, y 3 ejemplos calculados (boda, evento de empresa y feria).',
  },
  {
    key: 'modelos-contrato',
    icon: ScrollText,
    type: '.docx',
    title: 'Modelo de Contrato de Servicio',
    desc: 'Plantilla editable y orientativa (revísala con tu abogado): contrato para particulares y anexo para empresas y organizadores de ferias, con la toma eléctrica, los alérgenos, la señal y la cancelación por tramos.',
  },
  {
    key: 'guia-equivalencias',
    icon: Globe,
    type: '.docx',
    title: 'Guía de Equivalencias para tu país',
    desc: 'Vocabulario, impuestos, sanidad, normas laborales y unidades de 21 países para adaptar tu producto.',
  },
];

export default function PlanNegocioCafeteriaMovilEventosDashboard() {
  const { token } = useAuth('plan-negocio-cafeteria-movil-eventos-jwt');
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
        <title>Plan de Negocio: Cafetería Móvil para Eventos — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/plan-negocio-cafeteria-movil-eventos" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Plan Cafetería Móvil para Eventos</a>
            <div className="flex items-center gap-2"><FileSpreadsheet className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Plan de Negocio <span className="text-[#FFD700]">Cafetería Móvil para Eventos</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="plan-negocio-cafeteria-movil-eventos" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu plan de negocio profesional listo para descargar: plan financiero Excel de 9 hojas con tesorería mes a mes, plan de negocio Word de 10 secciones, checklist de apertura de 80 tareas, calculadora de escandallo y presupuesto, y modelo de contrato de servicio.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">5 Documentos + Bonus · Descarga Directa</p>
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {TEMPLATES.map((tpl, i) => {
                const Icon = tpl.icon;
                const url = files[tpl.key];
                const isPrimary = i === 0;
                return (
                  <div key={tpl.key} className={`rounded-xl p-5 transition-all ${isPrimary ? 'bg-white/5 border-2 border-[#FFD700]/50' : 'bg-white/5 border border-white/10 hover:border-[#FFD700]/30'}`}>
                    <div className="flex items-start gap-3 mb-3">
                      <div className="w-10 h-10 rounded-lg bg-[#FFD700]/10 flex items-center justify-center flex-shrink-0"><Icon className="w-5 h-5 text-[#FFD700]" /></div>
                      <div><h3 className="text-white font-bold text-sm leading-tight">{tpl.title}</h3><p className="text-gray-500 text-xs mt-0.5">{tpl.type}</p></div>
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
              <p className="text-white font-semibold mb-1">Compatibles con Excel, Word, Google Sheets, Google Docs, LibreOffice y Apple Numbers/Pages</p>
              <p className="text-gray-400 text-sm">Descarga los archivos y ábrelos con tu programa favorito. Todas las celdas y textos son editables.</p>
            </div>
          </div>
        </section>
        <ProductChangelog productId="plan-negocio-cafeteria-movil-eventos" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Completa tu toolkit para la barra de café</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-tareas-cafeteria" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Tareas Cafetería — €12</a>
              <a href="/plan-negocio-cafeteria" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan de Negocio Cafetería — €29</a>
              <a href="/plan-negocio-cocteleria-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Coctelería de Eventos — €55</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Plan de Negocio: Cafetería Móvil para Eventos · Todos los derechos reservados</p>
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
