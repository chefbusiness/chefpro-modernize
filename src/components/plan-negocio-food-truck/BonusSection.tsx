import { Map, ListChecks } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: Map,
    label: 'BONUS 1',
    title: 'Guía Permisos Food Truck por CCAA',
    value: '€19',
    desc: 'Guía de permisos de venta ambulante: por qué la licencia es municipal e intransferible, qué documentación pide el ayuntamiento, plazos reales de 1 a 3 meses y qué cambia según la comunidad autónoma (sección 9 del documento y fase 2 del checklist). No incluye los formularios de cada CCAA.',
    image: '/lovable-uploads/ai-gallery/plan-food-truck-mercado.jpg',
  },
  {
    icon: ListChecks,
    label: 'BONUS 2',
    title: 'Ratios Referencia Street Food 2026',
    value: '€19',
    desc: 'Tabla de referencia del sector dentro del libro: food cost de comida 28-33 %, de bebida 22-28 %, packaging 3-5 %, personal 25-32 %, margen bruto > 62 %, ticket 10-15 €, 40-80 clientes por servicio y 4-6 días operativos por semana, cada dato con su fuente y con una nota que dice dónde se aparta tu plan.',
    image: '/lovable-uploads/ai-gallery/plan-food-truck-cola.jpg',
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
            <p className="text-3xl text-gray-500 line-through mb-1">€99</p>
            <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">€29</p>
            <p className="text-[#FFD700] font-bold text-lg">¡Ahorra €70 HOY!</p>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
