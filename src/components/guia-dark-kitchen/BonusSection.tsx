import { ClipboardList, Wrench, Calculator } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: ClipboardList,
    label: 'BONUS 1',
    title: 'Checklist de Apertura Legal',
    value: '24 EUR',
    desc: '35 trámites organizados por categoría: constitución, licencias municipales, sanidad, seguros, Hacienda, protección de datos y APPCC. Con estado, responsable y fecha límite.',
    image: '/lovable-uploads/ai-gallery/guia-dk-tablets.jpg',
  },
  {
    icon: Wrench,
    label: 'BONUS 2',
    title: 'Checklist de Equipamiento y Obra',
    value: '24 EUR',
    desc: '40 ítems con presupuesto real: obra civil, instalaciones, cocina caliente, cocina fría, almacenamiento, expedición y tecnología. Presupuesto vs real con % de desviación.',
    image: '/lovable-uploads/ai-gallery/guia-dk-cocina.jpg',
  },
  {
    icon: Calculator,
    label: 'BONUS 3',
    title: 'Calculadora de Viabilidad Financiera',
    value: '19 EUR',
    desc: 'Inversión inicial, P&L mensual con comisiones de plataformas y punto de equilibrio automático con 3 escenarios (pesimista, realista, optimista).',
    image: '/lovable-uploads/ai-gallery/guia-dk-plano.jpg',
  },
];

export default function BonusSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">Bonus <span className="text-[#FFD700]">Incluidos</span></h2>
            <p className="text-gray-400 text-lg">Además de la guía PDF + DOCX, recibes estos 3 recursos Excel — valorados en 47 EUR</p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-3 gap-6 max-w-4xl mx-auto mb-12">
          {bonuses.map(({ icon: Icon, label, title, value, desc, image }, i) => (
            <FadeIn key={title} delay={i * 100}>
              <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden hover:border-[#FFD700]/40 transition-all group h-full">
                <div className="h-28 overflow-hidden relative">
                  <img src={image} alt="" className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" loading="lazy" />
                  <div className="absolute inset-0 bg-gradient-to-b from-transparent to-[#0a0a0a]" />
                  <span className="absolute bottom-3 left-4 text-[#FFD700] text-xs font-bold tracking-wider uppercase">{label}</span>
                </div>
                <div className="p-4">
                  <div className="flex items-center gap-2 mb-2">
                    <Icon className="w-5 h-5 text-[#FFD700]" />
                    <h3 className="text-white font-bold text-sm">{title}</h3>
                  </div>
                  <p className="text-gray-500 text-xs mb-2">Valor: {value}</p>
                  <p className="text-gray-400 text-xs leading-relaxed">{desc}</p>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
        <FadeIn>
          <div className="text-center bg-white/5 border border-[#FFD700]/30 rounded-2xl p-8">
            <p className="text-gray-400 mb-2">Valor total: guía + 3 bonus</p>
            <p className="text-3xl text-gray-500 line-through mb-1">90 EUR</p>
            <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">24 EUR</p>
            <p className="text-[#FFD700] font-bold text-lg">Ahorra 66 EUR HOY</p>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
