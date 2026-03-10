import { Globe, BookOpen, FileText } from 'lucide-react';

const bonuses = [
  {
    icon: Globe,
    label: 'BONUS 1',
    title: 'Mega Pack Cocinas del Mundo',
    value: '€47',
    desc: '50 prompts adicionales exclusivos para las 25 cocinas internacionales de AI Chef Pro: francesa, japonesa, italiana, peruana, mexicana y más.',
  },
  {
    icon: BookOpen,
    label: 'BONUS 2',
    title: 'Guía de Prompt Engineering Gastronómico',
    value: '€27',
    desc: 'Aprende a crear tus propios prompts gastronómicos perfectos desde cero con el método AI Chef Pro.',
  },
  {
    icon: FileText,
    label: 'BONUS 3',
    title: 'Cheat Sheet Descargable',
    value: '€23',
    desc: 'Resumen rápido de los 30 mejores prompts para hostelería para tener siempre a mano en tu negocio.',
  },
];

export default function BonusSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-5xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
            Bonos Exclusivos
          </h2>
          <p className="text-gray-400 text-lg">
            Además del eBook, recibirás estos bonos GRATIS valorados en €97
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mb-12">
          {bonuses.map(({ icon: Icon, label, title, value, desc }) => (
            <div
              key={title}
              className="bg-white/5 border border-white/10 rounded-xl p-6 hover:border-[#FFD700]/40 transition-all"
            >
              <div className="flex items-center gap-2 mb-4">
                <Icon className="w-6 h-6 text-[#FFD700]" />
                <span className="text-[#FFD700] text-xs font-bold tracking-wider uppercase">
                  {label}
                </span>
              </div>
              <h3 className="text-white font-bold text-lg mb-1">{title}</h3>
              <p className="text-gray-500 text-sm mb-3">Valor: {value}</p>
              <p className="text-gray-400 text-sm leading-relaxed">{desc}</p>
            </div>
          ))}
        </div>

        {/* Total value box */}
        <div className="text-center bg-white/5 border border-[#FFD700]/30 rounded-2xl p-8">
          <p className="text-gray-400 mb-2">Valor total</p>
          <p className="text-3xl text-gray-500 line-through mb-1">€194</p>
          <p className="text-5xl md:text-6xl font-extrabold text-[#FFD700] mb-2">€9</p>
          <p className="text-[#FFD700] font-bold text-lg">¡Ahorra €185 HOY!</p>
        </div>
      </div>
    </section>
  );
}
