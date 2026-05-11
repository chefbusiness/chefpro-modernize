import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft,
  Calculator, Truck, Wrench, Utensils, ScrollText, Sparkles, Flame, Tent,
} from 'lucide-react';
import { useAuth } from '@/hooks/useAuth';
import SaasDiscoveryBanner from '@/components/shared/SaasDiscoveryBanner';
import LogoBadge from '@/components/shared/LogoBadge';
import WhatsAppProductSupport from '@/components/shared/WhatsAppProductSupport';

const TEMPLATES = [
  {
    key: 'plan-negocio',
    icon: FileText,
    type: '.docx',
    title: 'Plan de Negocio (Word)',
    desc: 'DOCX completo de 60+ páginas: análisis de mercado España 2026, 10 competidores, doble embudo B2C+B2B, marco legal CCAA fuego al aire libre con excepción Falles, financiero 3 años, riesgos y roadmap.',
  },
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Plan Financiero Excel',
    desc: 'P&L 3 años con mix B2C 35 % + B2B 65 %, inversión 3.500-25.000 EUR según escenario, estacionalidad mayo-octubre + Falles, break-even 18-22 eventos año 1.',
  },
  {
    key: 'calculadora-pricing',
    icon: Calculator,
    type: '.xlsx',
    title: 'Calculadora Pricing Eventos',
    desc: 'Excel con fórmulas duales B2C particular + B2B planner. Inputs: pax, distancia, tipo de paella, concepto, ayudantes ⇒ precio sugerido + margen. Con 10 ejemplos validados.',
  },
  {
    key: 'plantilla-proveedores',
    icon: Truck,
    type: '.xlsx',
    title: 'Plantilla 88 Proveedores Reales',
    desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Calasparra DO), carniceros mayoristas, mariscos Mediterráneo (Linamar, Castellet, Nardín DO Denia), verduras Levante, azafrán DO La Mancha, Garcima/Vaello, Pordamsa.',
  },
  {
    key: 'catalogo-equipamiento',
    icon: Wrench,
    type: '.docx',
    title: 'Catálogo Equipamiento + Menaje',
    desc: 'Paelleras Garcima 60-90-120 cm + paellero Vaello 4 fuegos 50 kW + trípode leña + cuchillería Arcos + vajilla Pordamsa + EPI Texfire. SKU + URL + precio actualizado.',
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Checklist Apertura (6 fases)',
    desc: 'Constitución (autónomo + IAE 677.9 + APPCC + RGSEAA) · seguros RC eventos con cláusula intoxicación · equipamiento + arroceros DO · marca y web · captación B2C+B2B · operativa primer evento. 110 hitos.',
  },
  {
    key: 'carta-paellas',
    icon: Utensils,
    type: '.docx',
    title: 'Carta 12 Paellas y Arroces',
    desc: 'Valenciana DO + marisco premium + senyoret + arroz negro + mixta + arroz a banda + fideuá + meloso bogavante + caldoso bogavante + montaña + alicantina con costra + vegetal DO. Receta + escandallo + maridaje.',
  },
  {
    key: 'modelos-contrato',
    icon: ScrollText,
    type: '.docx',
    title: 'Modelos Contrato B2C + B2B',
    desc: 'Plantillas legales editables: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners, agencias, ayuntamientos) con anexo tarifario, briefing y SLA.',
  },
  {
    key: 'experiencias-tematicas',
    icon: Sparkles,
    type: '.docx',
    title: '10 Experiencias Temáticas',
    desc: 'Boda en finca · corporate showcooking · fiesta del pueblo popular · bautizo familiar · cumpleaños senyoret · Falles + festes · boda exclusiva 5* · hotel show cooking · vegetal DO inclusive · brunch banda + fideuá.',
  },
  {
    key: 'manual-tecnico',
    icon: Flame,
    type: '.docx',
    title: 'Manual Técnico Paellero',
    desc: 'Técnica del fuego en 4 fases (sofrito, proteínas, caldo+arroz, socarrat) + 6 tipos arroz Bomba/Sendra/Albufera + 3 caldos pro + salmueras + tabla cocción 12 paellas + 4 salsas + errores frecuentes.',
  },
  {
    key: 'guia-sistemas',
    icon: Tent,
    type: '.docx',
    title: 'Guía 8 Sistemas + Roadmap Food Truck',
    desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico inducción, gas industrial, portátil camping, caja china peruana, paellero solar. + Roadmap food truck arrocería: inversión 30-75K EUR, regulación 8 CCAA.',
  },
];

export default function PlanNegocioPaelleroEventosDashboard() {
  const { token } = useAuth('plan-negocio-paellero-eventos-jwt');
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
        <title>Plan de Negocio Paellero / Paella Eventos — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/plan-negocio-paellero-eventos" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Plan Paellero / Paella Eventos</a>
            <div className="flex items-center gap-2"><Flame className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Plan de Negocio <span className="text-[#FFD700]">Paellero / Paella Eventos</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu kit profesional listo para descargar: 11 entregables para montar tu servicio premium itinerante de paella y arroces en España 2026.</p>
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
        <section className="py-10 px-4 border-t border-white/10">
          <div className="max-w-3xl mx-auto text-center space-y-4">
            <p className="text-gray-400 text-sm mb-3">Completa tu toolkit de paella profesional</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/plan-negocio-parrillero-asador-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Parrillero Eventos — €45</a>
              <a href="/plan-negocio-cocteleria-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Coctelería Eventos — €55</a>
              <a href="/kit-escandallos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Kit Escandallos — €12</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Plan Paellero / Paella Eventos · Todos los derechos reservados</p>
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
