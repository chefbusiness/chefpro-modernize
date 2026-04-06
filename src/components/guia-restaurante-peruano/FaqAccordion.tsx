import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Cuánto cuesta montar un restaurante peruano en España?',
    a: 'Entre 130.000€ y 300.000€ dependiendo de la ubicación, nivel de acabados y si incluyes barra de piscos premium. La estación de ceviche refrigerada y la importación de productos peruanos añaden coste, pero los márgenes en coctelería (pisco sour 78%) lo compensan.',
  },
  {
    q: '¿Dónde consigo productos peruanos auténticos en España?',
    a: 'La guía incluye un capítulo completo (cap. 16) con proveedores de importación de ají amarillo, rocoto, maíz morado, pisco, chicha morada y más. Hay importadores especializados en Madrid, Barcelona y distribución nacional.',
  },
  {
    q: '¿Cevichería pura o restaurante peruano completo?',
    a: 'Depende de la zona y el ticket. Una cevichería pura tiene menor inversión y carta más enfocada. Un peruano completo (criollo + Nikkei + ceviches) tiene ticket más alto y mayor atracción. La guía analiza los 6 modelos en detalle.',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. Las 8 plantillas incluyen fórmulas automáticas: plan financiero, escandallos de 15 platos peruanos clave (ceviche, lomo saltado, causa), menú engineering con coctelería de pisco, cash flow y más.',
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
