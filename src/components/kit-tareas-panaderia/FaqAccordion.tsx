import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Incluye control de masas madre y pre-fermentos?',
    a: 'Sí. Control completo de masa madre natural: refresco, temperatura, hidratación y tiempos de fermentación. También pre-fermentos como poolish, biga y esponja con registros de actividad y protocolos de recuperación si la masa pierde fuerza.',
  },
  {
    q: '¿Cómo gestiona el turno de madrugada?',
    a: 'Checklist completo desde las 03:00: encendido y precalentamiento de hornos, preparación de masas del día, división y formado, control de fermentación en cámara y a temperatura ambiente, primera hornada y apertura de tienda. Todo paso a paso.',
  },
  {
    q: '¿Cubre diferentes tipos de horno?',
    a: 'Sí. Protocolos para horno de piso (solera refractaria), horno rotativo y horno de convección con vapor. Incluye temperaturas, tiempos de cocción, uso de vapor, grenado y carga óptima para cada tipo de pan y bollería.',
  },
  {
    q: '¿Sirve también para bollería y panes especiales?',
    a: 'Sí. Además del pan básico, cubre bollería fermentada (croissants, brioches, ensaimadas), panes especiales (centeno, espelta, semillas), panes de temporada y productos de pastelería de obrador. Cada categoría con sus tiempos y temperaturas.',
  },
  {
    q: '¿Funcionan en Google Sheets y otros programas?',
    a: 'Sí. Los archivos son .xlsx estándar. Compatibles con Microsoft Excel, Google Sheets, LibreOffice Calc, Apple Numbers e imprimibles directamente en A4 si prefieres trabajar en papel.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas y sin complicaciones.',
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
