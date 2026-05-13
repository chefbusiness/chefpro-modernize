import { Wheat, Calculator, FileSpreadsheet, FlaskConical } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Wheat,
    title: 'Escrita para Panadería Real',
    desc: 'Recetario maestro masa madre, fermentaciones 18-72h, escandallos por tipo de harina T55/T65/T80. No es una guía genérica.',
  },
  {
    icon: Calculator,
    title: 'Números Reales del Sector 2026',
    desc: 'Inversión 120K-200K€, food cost 18-22%, EBITDA 15-22%, break-even mes 8-14. Casos Levaduramadre, Panic, Crustó.',
  },
  {
    icon: FileSpreadsheet,
    title: 'Plantillas por Valor de 80€+',
    desc: 'Plan financiero, escandallos por pan, calculadora harinas, plan fermentación, Gantt apertura, turnos madrugada — todo Excel.',
  },
  {
    icon: FlaskConical,
    title: 'Técnica + Negocio en un mismo Documento',
    desc: 'Lo único que combina recetario técnico (masa madre + croissant + panettone) con plan de negocio + APPCC obrador + salida humos.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/guia-panaderia-3.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              ¿Por Qué Esta <span className="text-[#FFD700]">Guía</span>?
            </h2>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
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
      </div>
    </section>
  );
}
