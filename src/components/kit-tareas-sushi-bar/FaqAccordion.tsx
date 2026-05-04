import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Incluye el protocolo de anisakis obligatorio por ley?',
    a: 'Sí. El kit incluye un checklist específico con registro de congelación a -20 ºC durante 7 días por lote y proveedor, control de temperaturas y trazabilidad completa del pescado. Cumple con el RD 1420/2006 vigente y te deja todo documentado para auditorías de Sanidad.',
  },
  {
    q: '¿Sirve para mi tipo de restaurante japonés?',
    a: 'Sí. Las plantillas cubren sushi bar tradicional, restaurante japonés con cocina caliente, nikkei (fusión peruano-japonesa), kaiten, omakase y cualquier local que sirva pescado crudo. Todo es 100% editable para adaptar a tu carta y formato.',
  },
  {
    q: '¿Incluye preparación de arroz sushi profesional?',
    a: 'Sí. Protocolo completo de arroz: lavado, cocción, sazonado con sushi-zu, control de pH obligatorio (≤4.6 según APPCC), tiempos de descarte y temperaturas de servicio. Es lo que diferencia un sushi bar profesional de uno amateur.',
  },
  {
    q: '¿Qué es la vitrina neta case?',
    a: 'Es la vitrina refrigerada de la barra de sushi donde se exponen las piezas de pescado a la vista del cliente. El kit incluye checklist específico de montaje, rotación FIFO por lotes, control de temperatura (2-4 ºC) y exposición máxima de 2 horas.',
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
