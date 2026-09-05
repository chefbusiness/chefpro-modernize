import { Wheat, BarChart3, ShieldCheck, Banknote } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Wheat,
    title: 'Plan Específico Panadero',
    desc: 'No es plantilla genérica. Adaptado al modelo panadería/obrador: horno profesional, amasadora espiral 25-50 kg, cámara de fermentación, mix de pan, bollería y café, canal mayorista a restaurantes y estacionalidad navideña.',
  },
  {
    icon: BarChart3,
    title: 'Datos Reales Sector 2026',
    desc: 'Coste de mercancía 25-38 % según la línea, personal 35-42 %, merma de pan 5-10 %, margen bruto objetivo >62 %, ticket medio de 5,50 € sin IVA y break-even en transacciones diarias. Los rangos con los que el propio libro se audita.',
  },
  {
    icon: ShieldCheck,
    title: 'Registro Sanitario + 66 Trámites',
    desc: 'Una panadería con obrador que vende al consumidor final se inscribe en el Registro Sanitario de su Comunidad Autónoma, no en el RGSEAA estatal (art. 2.2 del RD 191/2011), y necesita licencia clasificada, salida de humos y proyecto técnico. Checklist con 66 trámites en 6 fases, con aviso de cuándo el canal mayorista sí puede obligar al RGSEAA.',
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
