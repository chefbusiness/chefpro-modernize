import { FileSpreadsheet, BarChart3, ShieldCheck, Banknote } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: FileSpreadsheet,
    title: 'Plan Financiero Profesional',
    desc: 'No es una plantilla genérica. Es un plan financiero Excel con P&L previsional a 3 años, fórmulas activas y celdas editables. Cambias el alquiler o el ticket medio y todo se recalcula automáticamente.',
  },
  {
    icon: BarChart3,
    title: 'Datos Reales España 2026',
    desc: '81K+ restaurantes activos en España, ticket medio por comunidad autónoma, inversión media por tipo de local y tasa de cierre del sector en los primeros 3 años. No supuestos: cifras del mercado real.',
  },
  {
    icon: ShieldCheck,
    title: 'Checklist Apertura Completo',
    desc: 'Más de 50 trámites organizados en 6 fases: constitución SL, licencias hostelería, obra, RRHH, marketing pre-apertura y primeros 90 días. No te dejas nada pendiente.',
  },
  {
    icon: Banknote,
    title: 'Listo para Banco e Inversores',
    desc: 'Es exactamente el formato que pide un banco para evaluar la financiación: P&L 3 años, punto de equilibrio, 3 escenarios, ratios financieros y plan de financiación. Pago único, sin suscripciones.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/plan-bar-restaurante-cocina.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              Por Qué Este <span className="text-[#FFD700]">Plan de Negocio</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado español para abrir un bar-restaurante con cabeza.
            </p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {reasons.map(({ icon: Icon, title, desc }, i) => (
            <FadeIn key={title} delay={i * 100}>
              <div className="text-center">
                <div className="w-14 h-14 rounded-2xl bg-[#FFD700]/20 flex items-center justify-center mx-auto mb-4">
                  <Icon className="w-7 h-7 text-[#FFD700]" />
                </div>
                <h3 className="text-white font-bold mb-2">{title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
        <FadeIn>
          <div className="bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8 text-center">
            <p className="text-gray-300 mb-4 text-sm">Compatible con cualquier software ofimático:</p>
            <div className="flex flex-wrap justify-center gap-2">
              {[
                { label: 'Excel', highlight: true },
                { label: 'Word' },
                { label: 'Google Sheets' },
                { label: 'Google Docs' },
                { label: 'LibreOffice' },
                { label: 'Apple Numbers' },
              ].map((pill) => (
                <span key={pill.label} className={`px-3 py-1.5 rounded-full text-sm font-medium ${pill.highlight ? 'bg-[#FFD700] text-black' : 'bg-white/10 text-gray-300'}`}>
                  {pill.label}
                </span>
              ))}
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
