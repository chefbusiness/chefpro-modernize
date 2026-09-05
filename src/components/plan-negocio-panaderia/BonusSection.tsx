import { Users, ListChecks } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: Users,
    label: 'BONUS 1',
    title: 'Cuadro de Personal Panadero con Cobertura de Horas',
    value: '€19',
    desc: 'Cuadro completo de personal con salarios brutos, Seguridad Social al 33 %, 14 pagas y turno de madrugada, con seis puestos —maestro panadero, oficial, ayudante de obrador, dependienta, extra de fin de semana y suplencias— y la comprobación de que las horas contratadas cubren el horario que declara el plan.',
    image: '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
  },
  {
    icon: ListChecks,
    label: 'BONUS 2',
    title: 'Ratios de Referencia Sector Panadero 2026',
    value: '€19',
    desc: 'Rangos de referencia del sector: coste de mercancía 25-30 % en pan y 32-38 % en bollería, personal 35-42 %, alquiler 10-14 %, merma de pan 5-10 %, margen bruto objetivo >62 %, producción diaria 80-200 kg y ticket medio de 3-6 €.',
    image: '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
  },
];

export default function BonusSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">Bonos <span className="text-[#FFD700]">Exclusivos</span></h2>
            <p className="text-gray-400 text-lg">Además del plan financiero y el checklist de apertura, accedes a estos recursos extra — valorados en €38</p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 gap-6 max-w-3xl mx-auto mb-12">
          {bonuses.map(({ icon: Icon, label, title, value, desc, image }, i) => (
            <FadeIn key={title} delay={i * 100}>
              <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden hover:border-[#FFD700]/40 transition-all group h-full">
                <div className="h-32 overflow-hidden relative">
                  <img src={image} alt="" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" loading="lazy" />
                  <div className="absolute inset-0 bg-gradient-to-b from-transparent to-[#0a0a0a]" />
                  <span className="absolute bottom-3 left-4 text-[#FFD700] text-xs font-bold tracking-wider uppercase">{label}</span>
                </div>
                <div className="p-5">
                  <div className="flex items-center gap-2 mb-2">
                    <Icon className="w-5 h-5 text-[#FFD700]" />
                    <h3 className="text-white font-bold text-base">{title}</h3>
                  </div>
                  <p className="text-gray-500 text-xs mb-2">Valor: {value}</p>
                  <p className="text-gray-400 text-sm leading-relaxed">{desc}</p>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
        <FadeIn>
          <div className="text-center bg-white/5 border border-[#FFD700]/30 rounded-2xl p-8">
            <p className="text-gray-400 mb-2">Valor total del pack completo</p>
            <p className="text-3xl text-gray-500 line-through mb-1">€120</p>
            <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">€35</p>
            <p className="text-[#FFD700] font-bold text-lg">¡Ahorra €85 HOY!</p>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
