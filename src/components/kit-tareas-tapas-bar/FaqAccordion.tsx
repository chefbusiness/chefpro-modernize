import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Sirve para un gastrobar moderno?',
    a: 'Sí. Cubre desde tapas bar clásico hasta gastrobar contemporáneo con cocina de autor en formato tapa. Tapas tradicionales, pinchos, raciones, medias raciones y propuestas creativas. Todo es 100% editable y adaptable a tu formato.',
  },
  {
    q: '¿Incluye control de cerveza de grifo?',
    a: 'Sí. Control completo de grifos: presión, CO2, temperatura, purga diaria, limpieza de líneas semanal, rotación de barriles y control de mermas. Todo con frecuencias y valores de referencia para que el barril no pierda calidad.',
  },
  {
    q: '¿Cubre la terraza?',
    a: 'Sí. Apertura y cierre de terraza, montaje de mesas y sillas, limpieza, eventos en terraza, control de stock terraza y protocolo de cierre por climatología. Importante para locales con terraza temporal o anual.',
  },
  {
    q: '¿Incluye rotación de carta estacional?',
    a: 'Sí. El calendario anual incluye tapas por temporada (gazpacho en verano, guisos en invierno, setas en otoño, espárragos en primavera), eventos gastronómicos, rutas de tapas y fechas clave para planificar la carta.',
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
