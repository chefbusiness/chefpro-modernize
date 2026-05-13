import { FileText, BookOpen, FlaskConical, Wind, FileSpreadsheet } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: FileText,
    label: 'BONUS 1',
    title: 'Business Plan Modelo para Bancos',
    value: '49 EUR',
    desc: 'Plantilla rellenable con estructura profesional para presentar a bancos. Resumen ejecutivo, proyecciones financieras a 3 años específicas panadería, análisis de mercado con datos sector 2026.',
    image: '/lovable-uploads/ai-gallery/guia-panaderia-hero.jpg',
  },
  {
    icon: BookOpen,
    label: 'BONUS 2',
    title: 'Manual del Obrador (Operaciones Completo)',
    value: '39 EUR',
    desc: 'Protocolo completo: refresco masa madre, recetario maestro (baguette, hogaza, croissant, panettone), planes de limpieza diaria/semanal/mensual, trazabilidad lotes harina.',
    image: '/lovable-uploads/ai-gallery/guia-panaderia-3.jpg',
  },
  {
    icon: FlaskConical,
    label: 'BONUS 3',
    title: 'Plan de Fermentación + Escandallos Harina',
    value: '29 EUR',
    desc: 'Excel completo con tiempos, hidrataciones, masa madre %, plegados para 15 tipos de pan. Calculadora de escandallos por harina T55/T65/T80/T110/espelta/centeno/sin gluten.',
    image: '/lovable-uploads/ai-gallery/guia-panaderia-2.jpg',
  },
  {
    icon: Wind,
    label: 'BONUS 4',
    title: 'Checklist Salida de Humos + Licencia Clasificada',
    value: '24 EUR',
    desc: 'Killer #1 de aperturas frustradas. 28 ítems pre-alquiler + proyecto técnico + licencia municipal + ejecución. Ahorra 4-6 meses de retraso.',
    image: '/lovable-uploads/ai-gallery/guia-panaderia-4.jpg',
  },
  {
    icon: FileSpreadsheet,
    label: 'BONUS 5',
    title: 'Calculadora CAPEX + Cronograma Gantt',
    value: '19 EUR',
    desc: 'Desglose inversión 120K-200K€ por categoría (obrador + tienda + licencias + maniobra) + cronograma Gantt 6 meses con fases críticas (proyecto humos → licencia → equipamiento).',
    image: '/lovable-uploads/ai-gallery/guia-panaderia-1.jpg',
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
