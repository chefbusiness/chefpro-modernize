import { Utensils, Calculator, ShieldCheck, RefreshCw } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Utensils,
    title: 'Escrita por un Profesional',
    desc: '29 años en alta hostelería y 15 años de consultoría gastronómica. No es teoría: es experiencia real asesorando aperturas de dark kitchens.',
  },
  {
    icon: Calculator,
    title: 'Números Reales, No Fantasía',
    desc: 'Inversión real (30K-80K€), márgenes después de comisiones de plataformas (25-35%), y punto de equilibrio calculado con datos del mercado español.',
  },
  {
    icon: ShieldCheck,
    title: 'Requisitos Legales Actualizados',
    desc: 'Licencias, APPCC, registro sanitario, seguros — todo actualizado a 2026 para España, con diferencias por comunidad autónoma.',
  },
  {
    icon: RefreshCw,
    title: 'Un Consultor Cobra 3.000€. Esto es 24€',
    desc: 'La misma información que reciben los clientes de consultoría, pero en formato guía por un pago único. Sin suscripción.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/guia-dk-cocina.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
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
