import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Cuánto cuesta montar un restaurante gastronómico?',
    a: 'Entre 500.000€ y 900.000€ dependiendo de la ubicación, nivel de acabados, equipamiento de cocina y tamaño de la bodega. La guía desglosa cada partida con costes reales del mercado español en el capítulo 4 y las plantillas Excel.',
  },
  {
    q: '¿Sirve para cualquier tipo de restaurante?',
    a: 'Está diseñada específicamente para restaurantes de alta cocina y fine dining (65 plazas). Dicho esto, la base de planificación financiera, legal y operativa es aplicable a cualquier restaurante de nivel medio-alto que aspire a la excelencia.',
  },
  {
    q: '¿Incluye información sobre cómo aspirar a Estrella Michelin?',
    a: 'Sí. Los capítulos 17, 18 y 19 cubren en detalle cómo aspirar a Estrella Michelin, Sol Repsol y The World\'s 50 Best. Incluye criterios de evaluación, qué buscan los inspectores y un checklist de 45 ítems como bonus.',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. Las 10 plantillas Excel incluyen fórmulas automáticas: plan financiero con P&L y break-even, escandallos por plato, calculadora de menú engineering (matrix Stars/Plowhorses/Puzzles/Dogs), cronograma Gantt y más.',
  },
  {
    q: '¿El DOCX es editable?',
    a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas, adaptar a tu proyecto y presentar a socios o inversores.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
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
