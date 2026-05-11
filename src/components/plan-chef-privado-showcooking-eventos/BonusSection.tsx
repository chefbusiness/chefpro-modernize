import { Flame, BookOpen } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: Flame,
    label: 'BONUS 1',
    title: 'Manual Técnico Servicio Domicilio + APPCC Móvil',
    value: '€40',
    desc: '7 PCC (Puntos de Control Crítico) APPCC adaptado a servicio itinerante: recepción, cadena de frío, manipulación, cocción, servicio en mesa, gestión de alérgenos, limpieza. + Cronograma operativo evento 8 pax minuto a minuto + organización de estaciones de trabajo en cocina del cliente + documentación obligatoria. La pieza que te separa del cocinero amateur.',
    image: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-3.jpg',
  },
  {
    icon: BookOpen,
    label: 'BONUS 2',
    title: 'Guía Chef Privado vs Personal Chef vs Caterer',
    value: '€49',
    desc: 'Comparativa estratégica de las 3 figuras del segmento: definición y modelo de cada una, ticket medio, ICP, margen neto, inversión inicial, plantilla. + Cuándo elegir cada figura, modelos híbridos válidos y riesgo de confundirlas al posicionarte. Empieza siempre por chef privado y pivota cuando proceda — la guía te dice exactamente cuándo.',
    image: '/lovable-uploads/ai-gallery/plan-chef-privado-showcooking-5.jpg',
  },
];

export default function BonusSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">Bonos <span className="text-[#FFD700]">Exclusivos</span></h2>
            <p className="text-gray-400 text-lg">Además del plan financiero y los 9 entregables principales, accedes a estos recursos diferenciales — valorados en €89</p>
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
            <p className="text-3xl text-gray-500 line-through mb-1">€165</p>
            <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">€45</p>
            <p className="text-[#FFD700] font-bold text-lg">¡Ahorra €120 HOY!</p>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
