import { Shuffle, ClipboardList } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: Shuffle,
    label: 'BONUS 1',
    title: 'Simulador de Escenarios (What-If)',
    value: '14 EUR',
    desc: 'Modifica ticket medio, ocupacion, food cost y ve impacto instantaneo en rentabilidad. Compara 3 escenarios lado a lado: pesimista, realista y optimista.',
    image: '/lovable-uploads/ai-gallery/plan-financiero-graficos.jpg',
  },
  {
    icon: ClipboardList,
    label: 'BONUS 2',
    title: 'Checklist Pre-Apertura Financiero',
    value: '14 EUR',
    desc: '48 items agrupados en 6 fases: constitucion, financiacion, licencias, proveedores, seguros, tesoreria. Con estado, responsable y fecha limite para no olvidar nada.',
    image: '/lovable-uploads/ai-gallery/plan-financiero-reunion.jpg',
  },
];

export default function BonusSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">Bonos <span className="text-[#FFD700]">Exclusivos</span></h2>
            <p className="text-gray-400 text-lg">Además de las 8 plantillas principales, recibes estos recursos adicionales — valorados en 28 EUR</p>
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
            <p className="text-3xl text-gray-500 line-through mb-1">69 EUR</p>
            <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">19 EUR</p>
            <p className="text-[#FFD700] font-bold text-lg">Ahorra 50 EUR HOY</p>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
