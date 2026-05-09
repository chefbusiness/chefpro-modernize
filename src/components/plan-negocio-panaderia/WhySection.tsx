import { Wheat, BarChart3, ShieldCheck, Banknote } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Wheat,
    title: 'Plan Específico Panadero',
    desc: 'No es plantilla genérica. Adaptado al modelo panadería/obrador: horno profesional, amasadora 40-80 kg, cámara fermentación, mix barra/bollería/cafetería y estacionalidad navideña.',
  },
  {
    icon: BarChart3,
    title: 'Datos Reales Sector 2026',
    desc: 'Materia prima 22-28 %, merma 3-5 %, margen pan >70 %, bollería >75 %, ticket medio €4,50 y break-even por kilos diarios. Cifras del mercado panadero español real.',
  },
  {
    icon: ShieldCheck,
    title: 'RGSEAA Obrador + 60 Trámites',
    desc: 'Panadería con obrador requiere RGSEAA (Registro General Sanitario), licencia clasificada, salida de humos y proyecto técnico. Checklist con 60+ trámites en 6 fases.',
  },
  {
    icon: Banknote,
    title: 'Listo para Banco e Inversores',
    desc: 'P&L 3 años, punto de equilibrio, 3 escenarios y plan de financiación con ICO, ENISA, leasing de horno y subvenciones autonómicas. Pago único, sin suscripciones.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              Por Qué Este <span className="text-[#FFD700]">Plan de Negocio</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No es otra plantilla genérica. Es el plan financiero profesional con datos reales del mercado panadero español para abrir una panadería u obrador con cabeza.
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
