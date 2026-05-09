import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Es un plan genérico o específico para cafetería?',
    a: 'Es 100 % específico para cafetería y brunch en España. Las partidas de inversión, los ratios financieros, los costes de personal y los trámites legales están adaptados al modelo de negocio de cafetería con barra, sala y terraza, incluyendo licencia de actividad inocua y RGSEAA.',
  },
  {
    q: '¿Puedo presentar este plan al banco o a inversores?',
    a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. Es exactamente el formato que piden bancos e inversores para evaluar la financiación de una cafetería.',
  },
  {
    q: '¿Puedo modificar las cifras del Excel?',
    a: 'Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, el número de clientes, el ticket medio, los salarios y cualquier partida de inversión para adaptarlo a tu proyecto concreto. Incluye hoja de instrucciones.',
  },
  {
    q: '¿Qué trámites legales incluye el checklist de apertura?',
    a: 'Más de 65 trámites organizados en 6 fases: constitución de la SL (notaría, registro mercantil, Hacienda), licencias municipales (licencia inocua, RGSEAA, terraza), equipamiento (proyecto técnico, instalaciones), RRHH (contratos, Seg. Social, PRL), marketing pre-apertura y primeros 90 días.',
  },
  {
    q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
    a: 'Los planes gratuitos son plantillas genéricas sin datos reales. Este plan incluye cifras del mercado español 2026, ratios financieros específicos de cafetería (food cost café 25-30 %, ticket medio €8-12), cuadro de personal con Seg. Social y un checklist de 65+ trámites verificado con la legislación vigente.',
  },
  {
    q: '¿Cómo funciona la garantía?',
    a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu cafetería con total confianza.',
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
