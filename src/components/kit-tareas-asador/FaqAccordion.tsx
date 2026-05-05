import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Incluye el protocolo del horno Josper?',
    a: 'Sí. Encendido, precalentamiento, zonas de calor, tipos de carbón (encina, quebracho), regulación de compuertas, mantenimiento semanal y limpieza profunda anual. Todo el ciclo del Josper documentado por turno.',
  },
  {
    q: '¿Sirve para mi tipo de asador?',
    a: 'Sí. Cubre asador tradicional, steakhouse, parrilla argentina, gastrobar con Josper y cualquier local con cocina a las brasas. Todo es 100% editable para adaptar a tu carta y formato.',
  },
  {
    q: '¿Incluye control de maduración de carne?',
    a: 'Sí. Fichas de dry-age y wet-age, control de piezas por peso y fecha, temperaturas de cámara (≤4 ºC), humedad y ventilación, más cálculo de mermas reales por pieza. Todo lo necesario para auditar y vender carne premium.',
  },
  {
    q: '¿Qué cortes y puntos de cocción incluye?',
    a: 'Chuletón, entrecot, tomahawk, costillar, solomillo, hamburguesa premium. Con temperaturas internas para blue (45 ºC), rare (50 ºC), medium rare (55 ºC), medium (60 ºC), medium well (65 ºC) y well done (70 ºC).',
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
