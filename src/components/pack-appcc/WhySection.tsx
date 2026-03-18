import { ShieldAlert, ClipboardCheck, Calculator, RefreshCw } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: ShieldAlert,
    title: 'Obligatorio por Ley',
    desc: 'El sistema APPCC es obligatorio para todos los establecimientos de hostelería en España. Sin estos registros, te expones a sanciones de hasta €60.000 y cierre cautelar.',
  },
  {
    icon: ClipboardCheck,
    title: 'Listo para Usar',
    desc: 'No empieces de cero. Cada plantilla viene pre-rellenada con datos reales de hostelería: zonas de limpieza, peligros HACCP, rangos de temperatura, los 14 alérgenos.',
  },
  {
    icon: Calculator,
    title: 'Fórmulas y Alertas Automáticas',
    desc: 'Las plantillas de temperatura cambian automáticamente entre OK y ALERTA. El control de aceite marca CAMBIAR cuando supera el 25% de compuestos polares.',
  },
  {
    icon: RefreshCw,
    title: 'Paga Una Vez, Tuyo Para Siempre',
    desc: 'Sin suscripciones. Acceso permanente al dashboard con todas las plantillas. Actualizaciones incluidas si cambia la normativa.',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/cochinillo-asado.jpeg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />

      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              ¿Por Qué Este <span className="text-[#FFD700]">Pack</span>?
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No son plantillas genéricas. Son registros diseñados por un profesional con 29 años en alta hostelería.
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
            <p className="text-gray-300 mb-4 text-sm">
              Compatible con cualquier software de hojas de cálculo:
            </p>
            <div className="flex flex-wrap justify-center gap-2">
              {[
                { label: 'Excel', highlight: true },
                { label: 'Google Sheets' },
                { label: 'LibreOffice' },
                { label: 'PDF imprimible' },
                { label: 'Apple Numbers' },
              ].map((pill) => (
                <span
                  key={pill.label}
                  className={`px-3 py-1.5 rounded-full text-sm font-medium ${
                    pill.highlight ? 'bg-[#FFD700] text-black' : 'bg-white/10 text-gray-300'
                  }`}
                >
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
