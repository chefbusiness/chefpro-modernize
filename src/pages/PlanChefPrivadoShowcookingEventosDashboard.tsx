import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft,
  Calculator, Truck, Wrench, Utensils, ScrollText, Sparkles, Flame, BookOpen,
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
    desc: 'DOCX completo de 60+ páginas: análisis mercado España 2026, segmentación dual B2C íntimo + B2B corporate, modelo sin local fijo, anexo regulación CCAA catering itinerante, financiero 3 años, riesgos y roadmap.',
  },
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Plan Financiero Excel',
    desc: 'P&L 3 años con mix B2C 40 % + B2B 60 %, inversión 4.500-30.000 EUR según escenario, sin estacionalidad fuerte, break-even 9-12 eventos/mes año 1.',
  },
  {
    key: 'calculadora-pricing',
    icon: Calculator,
    type: '.xlsx',
    title: 'Calculadora Pricing B2C + B2B',
    desc: 'Excel con fórmulas duales B2C cena íntima + B2B corporate showcooking. Inputs: pax, distancia, experiencia, nivel menú, pairing ⇒ precio sugerido + margen. 10 ejemplos validados.',
  },
  {
    key: 'plantilla-proveedores',
    icon: Truck,
    type: '.xlsx',
    title: 'Plantilla 96 Proveedores Premium',
    desc: 'Cuchillería japonesa (Tojiro, Yoshihiro, Kai Shun) + sous-vide Anova + vajilla Pordamsa/Steelite/Schönwald + carniceros Cesáreo Gómez/Discarlux + AOVE DO + caviar Riofrío + trufa Soria + microbrotes.',
  },
  {
    key: 'catalogo-equipamiento',
    icon: Wrench,
    type: '.docx',
    title: 'Catálogo Equipamiento + Cuchillería',
    desc: 'Cuchillería japonesa (gyuto, petty, sujihiki) + inducción portátil Vollrath/Iwatani + sous-vide + vajilla blanca premium + cristalería + uniformidad chef + furgoneta. Marcas y modelos validados.',
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Checklist Apertura (6 fases)',
    desc: 'Constitución (autónomo + IAE 677.9 + APPCC móvil + RGSEAA) · seguros RC con cláusula intoxicación · cuchillería + vajilla + proveedores premium · marca y portfolio · captación B2C+B2B · operativa primer evento. 108 hitos.',
  },
  {
    key: 'carta-menus',
    icon: Utensils,
    type: '.docx',
    title: 'Carta 12 Menús Temáticos',
    desc: 'Tasting menu degustación 7 pasos + brunch dominical premium + cena maridajes + mediterránea + asiático fusión + mexicano premium + ruta tapas privada + caprice del chef + vegetariano + healthy + mariscada + Navidad privada.',
  },
  {
    key: 'modelos-contrato',
    icon: ScrollText,
    type: '.docx',
    title: 'Modelos Contrato B2C + B2B',
    desc: 'Plantillas legales editables: B2C particular (cumpleaños, aniversarios, San Valentín, Navidad) + B2B corporate (cena directiva, showcooking, hotel, wedding planner) con confidencialidad, MSA y propiedad intelectual del menú.',
  },
  {
    key: 'experiencias-tematicas',
    icon: Sparkles,
    type: '.docx',
    title: '10 Experiencias Temáticas',
    desc: 'Cena romántica San Valentín · cumpleaños familiar · aniversario boda · brunch dominical · cena ejecutiva pairing · showcooking corporate 30-80 pax · cooking class team-building · hotel boutique in-suite · cena ensayo pre-boda · cena directiva fin año.',
  },
  {
    key: 'manual-tecnico',
    icon: Flame,
    type: '.docx',
    title: 'Manual Técnico Servicio Domicilio',
    desc: '7 PCC APPCC móvil (recepción, cadena frío, manipulación, cocción, servicio, alérgenos, limpieza) + cronograma evento 8 pax + estaciones de trabajo en cocina del cliente + coordinación servicio + documentación.',
  },
  {
    key: 'guia-sistemas',
    icon: BookOpen,
    type: '.docx',
    title: 'Guía Chef vs Personal vs Caterer',
    desc: 'Definición y modelo de cada figura · ticket medio · ICP · margen neto · inversión inicial · cuándo elegir cada una · modelos híbridos válidos · riesgo de confundirlas al posicionarte comercialmente.',
  },
];

export default function PlanChefPrivadoShowcookingEventosDashboard() {
  const { token } = useAuth('plan-chef-privado-showcooking-eventos-jwt');
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
        <title>Plan de Negocio Chef Privado / Showcooking — Dashboard | AI Chef Pro</title>
        <meta name="robots" content="noindex, nofollow" />
      </Helmet>
      <div className="min-h-screen bg-[#0a0a0a]">
        <SaasDiscoveryBanner />
        <header className="sticky top-0 z-50 bg-[#0a0a0a]/95 backdrop-blur-sm border-b border-white/10">
          <div className="max-w-6xl mx-auto px-4 h-14 flex items-center justify-between">
            <a href="/plan-chef-privado-showcooking-eventos" className="flex items-center gap-2 text-gray-400 hover:text-white transition-colors text-sm"><ArrowLeft className="w-4 h-4" />Plan Chef Privado / Showcooking</a>
            <div className="flex items-center gap-2"><Flame className="w-5 h-5 text-[#FFD700]" /><span className="text-white font-bold text-sm">Tu Dashboard</span></div>
            <a href="https://aichef.pro" className="text-gray-500 hover:text-[#FFD700] text-sm transition-colors">aichef.pro</a>
          </div>
        </header>
        <section className="py-12 md:py-16 px-4 text-center">
          <LogoBadge />
          <h1 className="text-3xl md:text-5xl font-extrabold text-white mb-3 mt-4">Plan de Negocio <span className="text-[#FFD700]">Chef Privado / Showcooking</span></h1>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu kit profesional listo para descargar: 11 entregables para montar tu servicio premium de chef privado y showcooking a domicilio en España 2026.</p>
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
              <a href="/plan-negocio-paellero-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Paellero Eventos — €45</a>
              <a href="/plan-negocio-parrillero-asador-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Parrillero Eventos — €45</a>
              <a href="/plan-negocio-cocteleria-eventos" className="inline-block px-6 py-3 border border-[#FFD700]/50 text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700]/10 transition-all text-sm">Ver Plan Coctelería Eventos — €55</a>
            </div>
          </div>
        </section>
        <footer className="py-8 px-4 border-t border-white/10">
          <div className="max-w-4xl mx-auto text-center">
            <p className="text-gray-500 text-sm mb-2">© 2026 AI Chef Pro · Plan Chef Privado / Showcooking a Domicilio · Todos los derechos reservados</p>
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
