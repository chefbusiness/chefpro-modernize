import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Cuánto cuesta montar un restaurante mexicano en España?',
    a: 'Entre 120.000€ y 280.000€ dependiendo de la ubicación, nivel de acabados y si incluyes barra de tequilas premium. La cocina mexicana requiere equipamiento específico (comal, tortillera, ahumador) pero es más económica que otros conceptos.',
  },
  {
    q: '¿Dónde consigo productos mexicanos auténticos en España?',
    a: 'La guía incluye un capítulo completo (cap. 16) con proveedores de importación de chiles secos, masa de maíz, tortillas, tequila, mezcal y más. Hay importadores especializados en Madrid, Barcelona, Valencia y distribución nacional.',
  },
  {
    q: '¿Mexicano auténtico o tex-mex? ¿Qué funciona mejor?',
    a: 'Depende de la zona. En ciudades grandes con comunidad latina, el mexicano auténtico triunfa. En zonas más turísticas, un concepto que mezcle autenticidad con accesibilidad funciona mejor. La guía analiza los 4 modelos en detalle.',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. Las 8 plantillas incluyen fórmulas automáticas: plan financiero, escandallos de 15 platos mexicanos clave (tacos, guacamole, mole), menú engineering, cash flow y más.',
  },
  {
    q: '¿El DOCX es editable?',
    a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas y presentar a socios o inversores.',
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
