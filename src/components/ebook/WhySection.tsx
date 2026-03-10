import { Globe, FlaskConical, Clock, RefreshCw } from 'lucide-react';

const reasons = [
  {
    icon: Globe,
    title: 'Para todo el sector, no solo la cocina',
    desc: 'Da igual que seas chef, gerente, pastelero, bartender o dueño de restaurante. Cada prompt está diseñado para tu rol específico dentro del negocio.',
  },
  {
    icon: FlaskConical,
    title: 'Prompts Probados en AI Chef Pro',
    desc: 'Cada prompt ha sido testeado en la plataforma para garantizar resultados consistentes y de calidad profesional en hostelería real.',
  },
  {
    icon: Clock,
    title: 'Ahorra Horas de Trabajo',
    desc: 'Deja de experimentar con la IA. Obtén resultados de calidad en segundos, ya sea para una receta, un presupuesto de catering o un post de Instagram.',
  },
  {
    icon: RefreshCw,
    title: 'Actualizaciones Gratuitas',
    desc: 'A medida que AI Chef Pro crece con nuevas apps para toda la hostelería, el eBook se actualiza. Tú las recibes sin coste adicional.',
  },
];

const compatPills = [
  { label: 'AI Chef Pro', highlight: true },
  { label: 'ChatGPT' },
  { label: 'Claude' },
  { label: 'Perplexity' },
  { label: 'DeepSeek' },
  { label: 'Gemini' },
  { label: 'KIMI' },
  { label: 'Copilot' },
  { label: '+ cualquier chatbot' },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
            ¿Por Qué Este eBook?
          </h2>
          <p className="text-gray-400 text-lg max-w-3xl mx-auto">
            No es solo una lista de prompts. Es un sistema completo para dominar la IA en tu negocio de hostelería.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {reasons.map(({ icon: Icon, title, desc }) => (
            <div key={title} className="text-center">
              <div className="w-14 h-14 rounded-2xl bg-[#FFD700]/20 flex items-center justify-center mx-auto mb-4">
                <Icon className="w-7 h-7 text-[#FFD700]" />
              </div>
              <h3 className="text-white font-bold mb-2">{title}</h3>
              <p className="text-gray-400 text-sm leading-relaxed">{desc}</p>
            </div>
          ))}
        </div>

        {/* Compatibility banner */}
        <div className="bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8 text-center">
          <p className="text-gray-300 mb-4 text-sm">
            Diseñado para AI Chef Pro. También funciona perfectamente con cualquier IA conversacional:
          </p>
          <div className="flex flex-wrap justify-center gap-2">
            {compatPills.map((pill) => (
              <span
                key={pill.label}
                className={`px-3 py-1.5 rounded-full text-sm font-medium ${
                  pill.highlight
                    ? 'bg-[#FFD700] text-black'
                    : 'bg-white/10 text-gray-300'
                }`}
              >
                {pill.label}
              </span>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
