import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Incluye los requisitos legales actualizados a 2026?',
    a: 'Sí. La guía cubre licencias de actividad, registro sanitario, alta en Hacienda, APPCC obligatorio, seguros y normativa de plásticos 2026. Actualizada para España con diferencias por CCAA.',
  },
  {
    q: '¿El DOCX es editable? ¿Puedo personalizarlo?',
    a: 'Sí. Recibes dos versiones: el PDF editorial (diseño profesional para leer) y el DOCX editable (para personalizar, añadir notas, adaptar a tu proyecto y presentar a socios o bancos).',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. La calculadora de viabilidad calcula automáticamente el punto de equilibrio, márgenes tras comisiones de plataformas y proyecciones a 12 meses. Los checklists tienen validación de datos y estados.',
  },
  {
    q: '¿Sirve si ya tengo un restaurante y quiero expandir a delivery?',
    a: 'Especialmente para eso. El capítulo 3 explica los modelos de negocio: marca propia, multi-marca desde tu cocina existente, o cocina satélite. Muchos restaurantes usan dark kitchens como extensión.',
  },
  {
    q: '¿Cuánto cuesta montar una dark kitchen?',
    a: 'Entre 30.000€ y 80.000€ dependiendo de la ubicación, equipamiento y número de marcas. La guía desglosa cada partida con costes reales del mercado español en el capítulo 4 y el checklist de equipamiento.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
  },
];

export default function FaqAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <h2 className="text-2xl md:text-4xl font-bold text-white text-center mb-12">Preguntas <span className="text-[#FFD700]">Frecuentes</span></h2>
        </FadeIn>
        <div className="space-y-3">
          {faqs.map((faq, i) => {
            const isOpen = openIndex === i;
            return (
              <FadeIn key={i} delay={i * 50}>
                <div className="bg-white/5 border border-white/10 rounded-xl overflow-hidden">
                  <button onClick={() => setOpenIndex(isOpen ? null : i)} className="w-full flex items-center justify-between p-5 text-left">
                    <span className="text-white font-medium pr-4">{faq.q}</span>
                    <ChevronDown className={`w-5 h-5 text-[#FFD700] flex-shrink-0 transition-transform duration-300 ${isOpen ? 'rotate-180' : ''}`} />
                  </button>
                  <div className={`grid transition-all duration-300 ${isOpen ? 'grid-rows-[1fr]' : 'grid-rows-[0fr]'}`}>
                    <div className="overflow-hidden">
                      <p className="px-5 pb-5 text-gray-400 leading-relaxed">{faq.a}</p>
                    </div>
                  </div>
                </div>
              </FadeIn>
            );
          })}
        </div>
      </div>
    </section>
  );
}
