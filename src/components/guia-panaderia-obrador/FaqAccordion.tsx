import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Cuánto cuesta montar una panadería con obrador en España?',
    a: 'Entre 120.000€ y 200.000€ para un local de 60-90 m² con obrador propio. La guía desglosa cada partida en el capítulo 4 y en la calculadora CAPEX incluida (Excel): 40% equipamiento obrador, 20% obra + salida humos, 15% tienda + branding, 25% fondo maniobra + licencias.',
  },
  {
    q: '¿Sirve para cualquier modelo de panadería?',
    a: 'Sí. La guía cubre los 4 modelos principales: obrador propio + tienda (modelo principal), despacho con horno de regeneración, panadería-bistró (cross-sell con brunch), y boutique especializada (solo masa madre / solo ecológico / solo sin gluten). El capítulo 3 ayuda a elegir el modelo correcto para tu zona.',
  },
  {
    q: '¿Incluye recetario maestro de masa madre?',
    a: 'Sí. El manual de operaciones incluye recetario técnico con hidrataciones, masa madre %, plegados y tiempos de fermentación para baguette tradition, hogaza T80 masa madre, croissant clásico mantequilla, brioche, panettone y más. Incluye también el protocolo de refresco diario de masa madre líquida y sólida.',
  },
  {
    q: '¿Cubre el problema de la salida de humos y licencia clasificada?',
    a: 'Sí. Es el capítulo 5 + un checklist específico de 28 ítems. La salida de humos es el killer #1 de las aperturas de panadería en España. La guía te enseña a verificar la viabilidad ANTES de alquilar, qué proyectos técnicos necesitas (1.500-4.000€), y cómo resolverlo con la comunidad de vecinos.',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. Las 9 plantillas Excel incluyen fórmulas automáticas: plan financiero 3 años, P&L 3 escenarios, cash flow + break-even, calculadora CAPEX, escandallo maestro con food cost por tipo de pan, plan de fermentación, calculadora ticket medio, cronograma Gantt apertura y plantilla turnos brigada con control horario.',
  },
  {
    q: '¿Cubre línea sin gluten certificada?',
    a: 'Sí. El capítulo 6 (APPCC y alérgenos cruzados) y el checklist APPCC obrador detallan los requisitos para ofrecer línea sin gluten con certificación FACE (Espiga Barrada): separación física del obrador, utensilios exclusivos, etiquetado y procedimientos.',
  },
  {
    q: '¿El DOCX es editable?',
    a: 'Sí. Recibes dos versiones: el PDF editorial profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas, adaptar a tu proyecto concreto y presentar a socios o inversores.',
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
