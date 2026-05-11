import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft,
  Calculator, Truck, Wrench, LayoutGrid, Utensils, ScrollText, Flame, BookOpen,
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
    desc: 'DOCX completo de 60+ páginas: análisis mercado España 2026 (4.585 M€ catering, 25.183 € boda media), top 14 conceptos temáticos validados, modelo multi-concepto sin local fijo, anexo regulación 17 CCAA, financiero 3 años, riesgos y roadmap progresivo.',
  },
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Plan Financiero Excel',
    desc: 'P&L 3 años con mix B2C 35 % + B2B 65 %, inversión 5.500-35.000 EUR según escenario, estacionalidad bodas mayo-octubre + corporate diciembre, break-even 14 eventos/mes año 1.',
  },
  {
    key: 'calculadora-pricing',
    icon: Calculator,
    type: '.xlsx',
    title: 'Calculadora Pricing Multi-concepto',
    desc: 'Excel con fórmulas duales B2C bodas + B2B corporate + factor multi-concepto. Inputs: pax, distancia, número conceptos (1-5+), nivel calidad, pairing, branded experience ⇒ precio sugerido + margen.',
  },
  {
    key: 'plantilla-proveedores',
    icon: Truck,
    type: '.xlsx',
    title: 'Plantilla 96 Proveedores · 12 Cocinas',
    desc: 'Importadores asiáticos (EMB Food, Cominport, Garmiko) + latinos (Imp. Cuesta, CMA, Jasa, Maíz Maya) + italiano (Caputo, Italfoods) + indio (Spice Box, Patak\'s, TRS) + BBQ (ALEXS, Smokefire) + carniceros premium + pescaderías + vegano + equipamiento.',
  },
  {
    key: 'catalogo-equipamiento',
    icon: Wrench,
    type: '.docx',
    title: 'Catálogo Equipamiento Multi-cocina',
    desc: 'Cuchillería japonesa sushi (Tojiro, Yoshihiro) + horno leña pizza (Pizza Party, Ooni Pro) + parrilla argentina + trompo pastor + tandoor portátil + smoker offset texano + wok pro (Wokinox) + sous-vide + vajilla premium.',
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Checklist Apertura (6 fases)',
    desc: 'Constitución (autónomo + IAE 677.9 + APPCC móvil multi-concepto + RGSEAA) · seguros RC eventos con cláusula intoxicación · proveedores especializados 12 cocinas · marca multi-concepto · captación B2C+B2B · operativa primer evento multi-station. 110 hitos.',
  },
  {
    key: '12-conceptos',
    icon: LayoutGrid,
    type: '.docx',
    title: '12 Conceptos Temáticos Pre-empaquetados',
    desc: 'Sushi-bar omakase + tacos al pastor + trattoria italiana + asado argentino + ceviche peruano + marisquería gallega + tandoor indio + mediterráneo + vegano premium + brasileño rodízio + BBQ texano + brunch internacional. Cada uno con menú + ambientación + equipamiento + operativa.',
  },
  {
    key: 'carta-menus',
    icon: Utensils,
    type: '.docx',
    title: 'Carta 12 Menús Cocinas del Mundo',
    desc: 'Boda multicultural premium 7 estaciones + tasting Asia 7 pasos + mexicano Día de Muertos + italiano trattoria + argentino tradicional + peruano Lima + indio Bollywood + griego/turco + vegano premium + BBQ texano + brunch internacional + mariscada gallega.',
  },
  {
    key: 'modelos-contrato',
    icon: ScrollText,
    type: '.docx',
    title: 'Modelos Contrato B2C + B2B',
    desc: 'Plantillas legales editables: B2C particular (boda multicultural, cumpleaños temático, aniversarios) + B2B corporate (brand event, embajada, festival gastronómico, planner) con MSA acuerdo marco anual, confidencialidad y propiedad intelectual del menú multi-concepto.',
  },
  {
    key: 'manual-tecnico',
    icon: Flame,
    type: '.docx',
    title: 'Manual Técnico APPCC Multi-concepto',
    desc: '7 PCC adaptados a multi-cocina simultánea (cadena frío diferenciada, T° servicio por concepto, alérgenos en multi-station) + cronograma evento 80 pax + layout multi-station + coordinación equipo freelance especializado por concepto.',
  },
  {
    key: 'guia-especializacion',
    icon: BookOpen,
    type: '.docx',
    title: 'Guía Especialización Progresiva',
    desc: 'Hoja de ruta para construir tu portafolio de cocinas del mundo: empieza con 1-2 conceptos, añade 1-2/año validando demanda. Top 5 mejores conceptos + 4 sub-explotados (oportunidad). Roadmap 12 meses para llegar a 6 conceptos en producción.',
  },
];

export default function PlanCateringTematicoEventosDashboard() {
  const { token } = useAuth('plan-catering-tematico-eventos-jwt');
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
        <title>Plan de Negocio Catering Temático Eventos — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/plan-catering-tematico-eventos" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Plan Catering Temático Eventos</a>
            <div className="flex items-center gap-2"><LayoutGrid className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Plan de Negocio <span className="text-[#FFD700]">Catering &amp; Kit Temático Eventos</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu kit profesional listo para descargar: 11 entregables para montar tu catering temático multi-concepto premium con 12 cocinas del mundo en portafolio.</p>
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
            <p className="text-gray-400 text-sm mb-3">Completa tu toolkit de eventos premium</p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <a href="/plan-chef-privado-showcooking-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Chef Privado / Showcooking — €45</a>
              <a href="/plan-negocio-paellero-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Paellero Eventos — €45</a>
              <a href="/plan-negocio-cocteleria-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Coctelería Eventos — €55</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Plan Catering Temático Eventos · Todos los derechos reservados</p>
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
