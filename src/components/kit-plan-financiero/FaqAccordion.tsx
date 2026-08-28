import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Sirve para un restaurante que ya está abierto?',
    a: 'Sí. El P&L mensual real vs presupuesto, el dashboard de ratios y el cash flow forecast son especialmente útiles para restaurantes en funcionamiento. El plan previsional y el informe de viabilidad son más para aperturas o expansiones.',
  },
  {
    q: '¿Necesito conocimientos de contabilidad?',
    a: 'No. Las plantillas están diseñadas para hosteleros, no para contables. Solo introduces tus números (ventas, costes, inversiones) y las fórmulas calculan todo automáticamente: ratios, gráficos, escenarios.',
  },
  {
    q: '¿El banco aceptará este informe de viabilidad?',
    a: 'Te da la estructura que piden las entidades: resumen ejecutivo, proyecciones a 5 años, ratios de solvencia, TIR, VAN y payback. La aprobación final depende de tu proyecto y del banco.',
  },
  {
    q: '¿Las plantillas se conectan entre sí?',
    a: 'Son coherentes entre sí: mismas categorías de ingreso/gasto, mismos ratios y la misma base sin IVA en 9 de las 10 (la de tesorería va con IVA porque es caja, y lo dice en su portada). Dentro de cada libro sí hay fórmulas encadenadas (mensual, total anual, resumen); entre libros no, para que puedas mover o abrir cada plantilla por separado sin romper ninguna referencia.',
  },
  {
    q: '¿Puedo usarlo para varios restaurantes?',
    a: 'Sí. La licencia es personal — puedes usar las plantillas en todos los proyectos que gestiones. Ideal para grupos de restauración, inversores y consultores.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: '30 días de garantía completa. Si no estás satisfecho, 100 % reembolso sin preguntas.',
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
