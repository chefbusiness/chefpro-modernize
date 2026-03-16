import { Calculator, FileSpreadsheet, TrendingDown, RefreshCw } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Calculator,
    title: 'Fórmulas Reales, No Valores Fijos',
    desc: 'Cambias un ingrediente y todo se recalcula: coste, merma, food cost % y PVP sugerido. Sin errores manuales.',
  },
  {
    icon: FileSpreadsheet,
    title: 'Para Todo Tipo de Establecimiento',
    desc: 'Restaurante, catering, pastelería, bar, food truck, cafetería. Cada plantilla adaptada a su formato real.',
  },
  {
    icon: TrendingDown,
    title: 'Mermas Estándar Precargadas',
    desc: '16 categorías de ingredientes con la merma típica de la industria. Editable para ajustar a tu realidad.',
  },
  {
    icon: RefreshCw,
    title: 'Paga Una Vez, Tuyo Para Siempre',
    desc: 'Sin suscripciones. Acceso permanente al dashboard con todas las plantillas. Nuevas plantillas sin coste adicional.',
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
              ¿Por Qué Este <span className="text-[#FFD700]">Kit</span>?
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No son plantillas genéricas. Son escandallos diseñados por un profesional con 29 años en alta hostelería.
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
                { label: 'Microsoft Excel', highlight: true },
                { label: 'Google Sheets' },
                { label: 'LibreOffice Calc' },
                { label: 'Apple Numbers' },
                { label: 'WPS Office' },
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
