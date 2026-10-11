import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft,
  Calculator, Truck, Wrench, Beef, ScrollText, Sparkles, Flame, Tent,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import ProductChangelog, { ProductVersionBadge } from '@/components/shared/ProductChangelog';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const TEMPLATES = [
  {
    key: 'plan-negocio',
    icon: FileText,
    type: '.docx',
    title: 'Plan de Negocio (Word)',
    desc: 'Word de 10 secciones en A4: resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, equipo, plan financiero, aspectos legales y plan de acción, con un anexo del fuego al aire libre en 8 comunidades.',
  },
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Plan Financiero Excel',
    desc: '9 hojas: supuestos, inversión inicial, cuenta de resultados a 3 años, punto de equilibrio, escenarios, personal, tesorería de 12 meses y financiación con cuadro del préstamo. Con IVA, ayudantes fijos discontinuos y cocina de apoyo autorizada.',
  },
  {
    key: 'calculadora-pricing',
    icon: Calculator,
    type: '.xlsx',
    title: 'Calculadora de Presupuestos por Evento',
    desc: 'De los invitados a la carne cruda, las parrillas, los parrilleros y el carbón, con el precio por invitado sin IVA y con IVA (10 %), cobro y tramos de cancelación para particular o empresa. 3 presupuestos de ejemplo calculados: boda, empresa y fiesta municipal.',
  },
  {
    key: 'plantilla-proveedores',
    icon: Truck,
    type: '.xlsx',
    title: 'Plantilla de 93 Proveedores',
    desc: 'Carniceros mayoristas (Hidalgo, Casa López, Tres Jotas), GGM Gastro (parrillas), Tienda Biomasa (carbón quebracho), Texfire (EPI), Hosply.pro y más. Con web y zona, y una columna de estado que arranca en «Por verificar».',
  },
  {
    key: 'catalogo-equipamiento',
    icon: Wrench,
    type: '.docx',
    title: 'Catálogo Equipamiento + Menaje',
    desc: 'Parrilla GGM KGE1200 709 EUR + Brogas asador cruz + Comander COMPER-M ahumador + cuchillería Arcos + vajilla eventos + EPI Texfire. SKU + URL + precio orientativo.',
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Checklist de Apertura (83 tareas)',
    desc: '6 fases: constitución y fiscalidad · cocina de apoyo autorizada, registro sanitario, APPCC, fuego y permisos, seguros · equipamiento y proveedores · personal y formación · marca y captación · primer evento y primeros 90 días.',
  },
  {
    key: 'carta-cortes',
    icon: Beef,
    type: '.docx',
    title: 'Carta 12 Cortes de Carne',
    desc: 'Argentinos (asado tira, bife chorizo, vacío) + castellanos (cordero a la cruz, cochinillo) + picaña y tomahawk + BBQ texano (brisket, ribs). Técnica + Tº + merma + maridaje.',
  },
  {
    key: 'modelos-contrato',
    icon: ScrollText,
    type: '.docx',
    title: 'Modelos Contrato B2C + B2B',
    desc: 'Plantillas legales editables: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias) con anexo tarifario. IVA al 10 %, cancelación por tramos y fuerza mayor con plan B de gas.',
  },
  {
    key: 'experiencias-tematicas',
    icon: Sparkles,
    type: '.docx',
    title: '10 Experiencias Temáticas',
    desc: 'Asado argentino, asador a la cruz, parrilla uruguaya, BBQ texano, rodizio brasileño, asador criollo, mediterránea, llanera, show de fuego y brunch parrillero corporate.',
  },
  {
    key: 'manual-tecnico',
    icon: Flame,
    type: '.docx',
    title: 'Manual Técnico Parrillero',
    desc: '8 salmueras + 12 marinados + tabla de cocción de 18 cortes con Tº interna y merma + escalado de carne, parrillas, parrilleros y carbón + chimichurri 3 versiones + 5 salsas profesionales. Lo que separa al amateur del profesional.',
  },
  {
    key: 'guia-sistemas',
    icon: Tent,
    type: '.docx',
    title: 'Guía 8 Sistemas + Roadmap Food Truck',
    desc: 'Comparativa parrilla argentina, asador cruz, BBQ pit, caja china, barril llanero, modular inox, brasero, lift-grill. + Roadmap food truck especializado: inversión 30-75K EUR, regulación 8 CCAA.',
  },
];

export default function PlanNegocioParrilleroAsadorEventosDashboard() {
  const { token } = useAuth('plan-negocio-parrillero-asador-eventos-jwt');
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
        <title>Plan de Negocio Parrillero / Asador Eventos — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/plan-negocio-parrillero-asador-eventos" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Plan Parrillero / Asador Eventos</a>
            <div className="flex items-center gap-2"><Flame className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Plan de Negocio <span className="text-[#FFD700]">Parrillero / Asador Eventos</span></h1>
          <div className="mb-3">
            <ProductVersionBadge productId="plan-negocio-parrillero-asador-eventos" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu kit profesional listo para descargar: 11 entregables para montar tu servicio premium itinerante de parrilla y asado en España.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">11 Entregables · Descarga Directa</p>
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
        <ProductChangelog productId="plan-negocio-parrillero-asador-eventos" />
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Completa tu toolkit de parrilla profesional</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/kit-tareas-asador" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Tareas Asador — €14</a>
              <a href="/plan-negocio-cocteleria-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Coctelería Eventos — €55</a>
              <a href="/kit-escandallos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Escandallos — €12</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Plan Parrillero / Asador Eventos · Todos los derechos reservados</p>
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
