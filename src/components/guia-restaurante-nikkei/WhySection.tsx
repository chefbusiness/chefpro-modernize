import { UtensilsCrossed, Calculator, FileSpreadsheet, RefreshCw } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: UtensilsCrossed,
    title: 'Escrita por un Profesional',
    desc: '29 años en hostelería, 200+ aperturas asesoradas. Incluye proveedores reales de ají peruano, pescado sashimi-grade y pisco en España.',
  },
  {
    icon: Calculator,
    title: 'Números Reales, No Fantasía',
    desc: 'Inversión real (280K-520K€), food cost 32-34%, márgenes pisco/sake/coctelería 75-85%, break-even mes 10-16 y 3 escenarios.',
  },
  {
    icon: FileSpreadsheet,
    title: 'Incluye Plantillas por Valor de 80€+',
    desc: 'Plan financiero, escandallos de tiraditos/ceviches/anticuchos, menú engineering, Gantt y más — todo en Excel.',
  },
  {
    icon: RefreshCw,
    title: 'Un Consultor Cobra 3.000-10.000€',
    desc: 'La misma información que reciben los clientes de consultoría gastronómica, en formato guía por un pago único de 65€.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/guia-restaurante-nikkei-cocina.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
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
