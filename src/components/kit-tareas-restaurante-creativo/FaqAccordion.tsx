import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Las tareas vienen ya rellenadas para restaurante creativo?',
    a: 'Si. Cada checklist viene pre-rellenado con las tareas reales de un restaurante creativo o de autor: I+D de platos, mise en place de degustacion, brigada creativa, sumiller y eventos. Solo tienes que personalizar: ajustar tareas a tu negocio, borrar las que no apliquen y anadir las especificas. Las celdas editables estan marcadas en verde.',
  },
  {
    q: '¿Cubre I+D y desarrollo de menu?',
    a: 'Si. Incluye una plantilla completa de I+D: fichas tecnicas de nuevos platos, pruebas de concepto, evaluacion sensorial, costes de investigacion, registro fotografico y seguimiento de la evolucion de la carta.',
  },
  {
    q: '¿Incluye tareas de sumiller y bodega?',
    a: 'Si. Una plantilla entera dedicada al sumiller: gestion de bodega, carta de vinos, maridajes por pase del menu degustacion, servicio de sumilleria, catas para equipo, temperaturas de servicio y control de stock de referencias premium.',
  },
  {
    q: '¿Es solo para fine dining o sirve para cocina creativa casual?',
    a: 'Sirve para ambos. Las plantillas son escalables: un restaurante con menu degustacion de 12 pases puede usar todas. Un bistro creativo con carta corta puede simplificar y quedarse con apertura/cierre, brigada y periodicas. Adapta lo que necesites.',
  },
  {
    q: '¿En que se diferencia de apps de gestion?',
    a: 'Las apps de gestion cobran €40/mes por local y requieren tablets/moviles. Este kit te da las mismas listas de tareas en Excel por €12, pago unico. Sin suscripcion, sin internet, ilimitado en locales.',
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
