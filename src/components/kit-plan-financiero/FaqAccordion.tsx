import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Sirve para un restaurante que ya esta abierto?',
    a: 'Si. El P&L mensual real vs presupuesto, el dashboard de ratios y el cash flow forecast son especialmente utiles para restaurantes en funcionamiento. El plan previsional y el informe de viabilidad son mas para aperturas o expansiones.',
  },
  {
    q: '¿Necesito conocimientos de contabilidad?',
    a: 'No. Las plantillas estan disenadas para hosteleros, no para contables. Solo introduces tus numeros (ventas, costes, inversiones) y las formulas calculan todo automaticamente: ratios, graficos, escenarios.',
  },
  {
    q: '¿El banco aceptara este informe de viabilidad?',
    a: 'Si. El formato sigue la estructura que las entidades financieras esperan ver: resumen ejecutivo, proyecciones a 3 anos, TIR, VAN, payback period y escenarios. Lo hemos validado con asesores financieros.',
  },
  {
    q: '¿Las plantillas se conectan entre si?',
    a: 'Si. Las formulas estan encadenadas: los datos del CAPEX alimentan el cash flow, el plan previsional alimenta el break-even, y los ratios se calculan automaticamente desde el P&L.',
  },
  {
    q: '¿Puedo usarlo para varios restaurantes?',
    a: 'Si. La licencia es personal — puedes usar las plantillas en todos los proyectos que gestiones. Ideal para grupos de restauracion, inversores y consultores.',
  },
  {
    q: '¿Hay garantia de devolucion?',
    a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
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
