import { useState, useEffect } from 'react';
import { Helmet } from 'react-helmet-async';
import {
  Download, Loader2, Globe, FileSpreadsheet, FileText, ClipboardCheck, ArrowLeft,
  Calculator, Truck, Wrench, Utensils, ScrollText, Sparkles, Flame, Tent,
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
    desc: 'Plan de negocio en 10 secciones más un anexo del fuego al aire libre en 8 comunidades (más de 7.000 palabras, A4): resumen ejecutivo, concepto, mercado, competencia, marketing y captación, operaciones, equipo, plan financiero, aspectos legales y plan de acción. Sus cifras son las del caso de ejemplo del Excel: si cambias el Excel, manda el Excel.',
  },
  {
    key: 'plan-financiero',
    icon: FileSpreadsheet,
    type: '.xlsx',
    title: 'Plan Financiero Excel',
    desc: '9 hojas: supuestos, inversión inicial, PyG 3 años, punto de equilibrio (raciones por evento e ingresos), escenarios, personal, tesorería 12 meses, financiación con cuadro del préstamo y DSCR, e instrucciones. Ventas = eventos al año × raciones por evento × precio por ración sin IVA; IVA del 10 %, cocina de apoyo autorizada, sueldo del dueño, amortización y ayudantes fijos discontinuos. Cambia las celdas verdes por tus datos.',
  },
  {
    key: 'calculadora-pricing',
    icon: Calculator,
    type: '.xlsx',
    title: 'Calculadora de Presupuestos por Evento',
    desc: 'Paelleras por diámetro, paelleros, kilos de arroz, litros de caldo y gas; materia prima, menaje, personal con su Seguridad Social y alquileres, al precio por invitado sin IVA y con IVA (10 %). Particular o empresa, desplazamiento a 0,95 €/km, anticipo del 30 %, importes por tramo de cancelación y margen calculado. 3 presupuestos de ejemplo: boda, empresa y fiesta popular.',
  },
  {
    key: 'plantilla-proveedores',
    icon: Truck,
    type: '.xlsx',
    title: 'Plantilla de 88 Proveedores',
    desc: 'Arroceros DO Valencia (Tartana, J. Sendra, Calasparra DO), carniceros mayoristas, mariscos Mediterráneo (Linamar, Castellet, Nardín DO Denia), verduras Levante, azafrán DO La Mancha, Garcima/Vaello, Pordamsa. Con una columna de estado que arranca en «Por verificar».',
  },
  {
    key: 'catalogo-equipamiento',
    icon: Wrench,
    type: '.docx',
    title: 'Catálogo Equipamiento + Menaje',
    desc: 'Paelleras Garcima 60-90-120 cm + paellero Vaello 4 fuegos 50 kW + trípode leña + cuchillería Arcos + vajilla Pordamsa + EPI Texfire. SKU + URL + precio orientativo.',
  },
  {
    key: 'checklist-apertura',
    icon: ClipboardCheck,
    type: '.xlsx',
    title: 'Checklist de Apertura (83 tareas)',
    desc: '83 tareas en 6 fases: constitución y fiscalidad (IAE 677.9, Veri*factu, IVA al 10 %) · cocina de apoyo autorizada, registro sanitario autonómico, APPCC, gas, fuego y permisos · equipamiento y proveedores · personal y formación · marca y captación (ayuntamientos por FACe) · primer evento y primeros 90 días.',
  },
  {
    key: 'carta-paellas',
    icon: Utensils,
    type: '.docx',
    title: 'Carta 12 Paellas y Arroces',
    desc: 'Valenciana DO + marisco premium + senyoret + arroz negro + mixta + arroz a banda + fideuá + meloso bogavante + caldoso bogavante + montaña + alicantina con costra + vegetal DO. Receta + food cost por ración + maridaje, con PVP orientativo por ración.',
  },
  {
    key: 'modelos-contrato',
    icon: ScrollText,
    type: '.docx',
    title: 'Modelos Contrato B2C + B2B',
    desc: 'Plantillas editables y orientativas: B2C particular (cumpleaños, bautizos, bodas íntimas) + B2B profesional (wedding planners y agencias) con anexo tarifario, briefing y SLA, IVA al 10 %, cancelación escalonada y fuerza mayor por alerta de incendios. Revísalas con tu asesor antes de usarlas.',
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
    desc: 'Escalado por paellera (diámetro → raciones → arroz → caldo → quemador) y cómo cubrir 50, 100 o 200 invitados + técnica del fuego en 4 fases, con gas o leña + 6 tipos de arroz + 4 caldos + tabla de cocción de 12 paellas + cronograma del evento + seguridad alimentaria y alérgenos por paella + problemas y soluciones + checklist de material.',
  },
  {
    key: 'guia-sistemas',
    icon: Tent,
    type: '.docx',
    title: 'Guía 8 Sistemas + Roadmap Food Truck',
    desc: 'Comparativa paellero gas profesional, fuego de leña con trípode, paellero leña obra, eléctrico inducción, gas industrial, portátil camping, caja china peruana, paellero solar. + Roadmap food truck arrocería: inversión de 26.000 a 86.000 € según su tabla, regulación 8 CCAA.',
  },
  {
    key: 'guia-equivalencias',
    icon: Globe,
    type: '.docx',
    title: 'Guía de Equivalencias para tu país',
    desc: 'Vocabulario, impuestos, sanidad, normas laborales y unidades de 20 países para adaptar tu producto.',
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
          <div className="mb-3">
            <ProductVersionBadge productId="plan-negocio-paellero-eventos" />
          </div>
          <p className="text-gray-400 text-base md:text-lg max-w-2xl mx-auto">Tu kit profesional listo para descargar: 12 entregables para montar tu servicio premium itinerante de paella y arroces en España.</p>
        </section>
        <section className="pb-16 px-4">
          <div className="max-w-5xl mx-auto">
            <p className="text-[#FFD700] text-sm font-bold uppercase tracking-wider mb-6">12 Entregables · Descarga Directa</p>
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
        <ProductChangelog productId="plan-negocio-paellero-eventos" />
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
