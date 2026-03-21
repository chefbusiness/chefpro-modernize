import { ClipboardCheck, Wine, Users, RefreshCw } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: ClipboardCheck,
    title: 'Pre-Rellenadas para Bar',
    desc: 'No empieces de cero. Cada checklist viene con las tareas reales de un bar profesional. Solo ajusta, borra lo que no aplique y añade lo que te falte.',
  },
  {
    icon: Wine,
    title: 'Coctelería y Barra Completa',
    desc: 'Spirits, batches, jarabes, cerveza de grifo, vinos por copa, café espresso. Las tareas que apps genéricas no cubren.',
  },
  {
    icon: Users,
    title: 'Perfiles Específicos',
    desc: 'Checklists para head bartender, bartender, barback y camarero. Cada puesto sabe exactamente qué hacer cada turno.',
  },
  {
    icon: RefreshCw,
    title: 'Trail Cobra €60/mes. Esto es €12',
    desc: 'Las mismas listas de tareas que usan bares con SaaS premium como Trail, pero en Excel por un pago único. Sin suscripción.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              ¿Por Qué Este <span className="text-[#FFD700]">Kit</span>?
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No son plantillas genéricas. Son checklists diseñados por un profesional con 29 años en alta hostelería.
            </p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
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
        <FadeIn>
          <div className="bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8 text-center">
            <p className="text-gray-300 mb-4 text-sm">Compatible con cualquier software de hojas de cálculo:</p>
            <div className="flex flex-wrap justify-center gap-2">
              {[
                { label: 'Excel', highlight: true },
                { label: 'Google Sheets' },
                { label: 'LibreOffice' },
                { label: 'Imprimible A4' },
                { label: 'Apple Numbers' },
              ].map((pill) => (
                <span key={pill.label} className={`px-3 py-1.5 rounded-full text-sm font-medium ${pill.highlight ? 'bg-[#FFD700] text-black' : 'bg-white/10 text-gray-300'}`}>
                  {pill.label}
                </span>
              ))}
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
