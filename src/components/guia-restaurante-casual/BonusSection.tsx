import { FileText, BookOpen, ClipboardCheck, CalendarRange, PieChart } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: FileText,
    label: 'BONUS 1',
    title: 'Business Plan Modelo para Bancos',
    value: '49 EUR',
    desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Resumen ejecutivo, proyecciones financieras a 3 años y análisis de mercado.',
    image: '/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
  },
  {
    icon: BookOpen,
    label: 'BONUS 2',
    title: 'Manual de Operaciones',
    value: '39 EUR',
    desc: 'Protocolo completo: apertura, cierre, servicio mediodía y cena, gestión de delivery, terraza, reclamaciones y alérgenos. Para formar a tu equipo desde el día 1.',
    image: '/lovable-uploads/ai-gallery/guia-casual-sala.jpg',
  },
  {
    icon: ClipboardCheck,
    label: 'BONUS 3',
    title: 'Checklist Diseño Sala + Terraza',
    value: '29 EUR',
    desc: '29 ítems: distribución, mobiliario, iluminación regulable, acústica, decoración, terraza completa con sombrillas, estufas y macetas.',
    image: '/lovable-uploads/ai-gallery/guia-casual-terraza.jpg',
  },
  {
    icon: CalendarRange,
    label: 'BONUS 4',
    title: 'Cronograma de Apertura Gantt 12 Meses',
    value: '24 EUR',
    desc: 'Todas las fases: planificación, local, licencias, obra, equipamiento, equipo, marketing, soft opening e inauguración.',
    image: '/lovable-uploads/ai-gallery/guia-casual-cocina.jpg',
  },
  {
    icon: PieChart,
    label: 'BONUS 5',
    title: 'Calculadora Menú Engineering + Menú del Día',
    value: '19 EUR',
    desc: 'Matrix automática Stars/Plowhorses/Puzzles/Dogs + simulador de menú del día con food cost controlado.',
    image: '/lovable-uploads/ai-gallery/guia-casual-plato.jpg',
  },
];

export default function BonusSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-5xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">Bonus <span className="text-[#FFD700]">Incluidos</span></h2>
            <p className="text-gray-400 text-lg">Además de la guía PDF + DOCX, recibes estos 5 recursos — valorados en 160 EUR</p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-5xl mx-auto mb-8">
          {bonuses.slice(0, 3).map(({ icon: Icon, label, title, value, desc, image }, i) => (
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
        <div className="grid md:grid-cols-2 gap-6 max-w-3xl mx-auto mb-12">
          {bonuses.slice(3).map(({ icon: Icon, label, title, value, desc, image }, i) => (
            <FadeIn key={title} delay={(i + 3) * 100}>
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
            <p className="text-gray-400 mb-2">Valor total: guía + 5 bonus</p>
            <p className="text-3xl text-gray-500 line-through mb-1">180 EUR</p>
            <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">65 EUR</p>
            <p className="text-[#FFD700] font-bold text-lg">Ahorra 115 EUR HOY</p>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
