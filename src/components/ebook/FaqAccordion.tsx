import { useState } from 'react';
import { ChevronDown } from 'lucide-react';

const faqs = [
  {
    q: '¿Cómo recibo el acceso después del pago?',
    a: 'Inmediatamente después del pago recibirás un email con tu enlace de acceso personal y único a la Pro Prompts Library, donde encontrarás el eBook descargable y todos los bonos. El enlace es personal e intransferible.',
  },
  {
    q: '¿Funciona solo con AI Chef Pro o con otras IAs?',
    a: 'Los prompts están optimizados para AI Chef Pro pero funcionan perfectamente con ChatGPT, Claude, Perplexity, DeepSeek, Gemini, KIMI y cualquier IA conversacional.',
  },
  {
    q: '¿Qué formato tiene el eBook?',
    a: 'PDF de alta calidad, compatible con todos los dispositivos: móvil, tablet y ordenador.',
  },
  {
    q: '¿Recibiré actualizaciones?',
    a: 'Sí. Todas las actualizaciones futuras son gratuitas. A medida que AI Chef Pro lance nuevas apps, el eBook se actualiza y tú las recibes automáticamente.',
  },
  {
    q: '¿Cómo funciona la garantía?',
    a: 'Tienes 30 días completos para probarlo. Si no estás satisfecho por cualquier motivo, te devolvemos el 100% sin hacer ninguna pregunta.',
  },
  {
    q: '¿Necesito experiencia previa con IA?',
    a: 'Para nada. Los prompts están listos para copiar y pegar. Resultados profesionales desde el primer día, independientemente de tu nivel.',
  },
];

export default function FaqAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-3xl mx-auto">
        <h2 className="text-2xl md:text-4xl font-bold text-white text-center mb-12">
          Preguntas Frecuentes
        </h2>

        <div className="space-y-3">
          {faqs.map((faq, i) => {
            const isOpen = openIndex === i;
            return (
              <div
                key={i}
                className="bg-white/5 border border-white/10 rounded-xl overflow-hidden"
              >
                <button
                  onClick={() => setOpenIndex(isOpen ? null : i)}
                  className="w-full flex items-center justify-between p-5 text-left"
                >
                  <span className="text-white font-medium pr-4">{faq.q}</span>
                  <ChevronDown
                    className={`w-5 h-5 text-[#FFD700] flex-shrink-0 transition-transform duration-300 ${
                      isOpen ? 'rotate-180' : ''
                    }`}
                  />
                </button>
                <div
                  className={`grid transition-all duration-300 ${
                    isOpen ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'
                  }`}
                >
                  <div className="overflow-hidden">
                    <p className="px-5 pb-5 text-gray-400 leading-relaxed">
                      {faq.a}
                    </p>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
