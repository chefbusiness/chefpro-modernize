import { FileText, BookOpen, ClipboardCheck, CalendarRange, PieChart } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const bonuses = [
  {
    icon: FileText,
    label: 'BONUS 1',
    title: 'Business Plan Modelo para Bancos',
    value: '49 EUR',
    desc: 'Plantilla rellenable con estructura profesional para presentar a bancos e inversores. Incluye sección específica de cocina nikkei premium y proveedores peruanos en España.',
    image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
  },
  {
    icon: BookOpen,
    label: 'BONUS 2',
    title: 'Manual de Operaciones Nikkei',
    value: '39 EUR',
    desc: 'Protocolo completo: barra de tiraditos, cold station leche de tigre, robata, cocina caliente (chaufa/anticuchos), barra pisco/sake, anisakis, delivery y alérgenos.',
    image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-sala.jpg',
  },
  {
    icon: ClipboardCheck,
    label: 'BONUS 3',
    title: 'Checklist Equipamiento Cocina Nikkei',
    value: '29 EUR',
    desc: '36 ítems específicos: vitrina sashimi, robata/josper, wok station, licuadoras leche de tigre, cuchillos yanagiba/deba, molcajete, teppanyaki.',
    image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-cocina.jpg',
  },
  {
    icon: CalendarRange,
    label: 'BONUS 4',
    title: 'Cronograma de Apertura Gantt 12 Meses',
    value: '24 EUR',
    desc: 'Fases específicas nikkei: búsqueda del chef nikkei, contacto importadores de ají peruano y pescado sashimi-grade, formación, soft opening.',
    image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-barra.jpg',
  },
  {
    icon: PieChart,
    label: 'BONUS 5',
    title: 'Escandallos: 15 Recetas Base Nikkei',
    value: '19 EUR',
    desc: 'Fichas técnicas con food cost real: tiradito clásico, ceviche nikkei, causa nikkei, maki acevichado, tataki de atún, anticucho, chaufa de mariscos.',
    image: '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-plato.jpg',
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
