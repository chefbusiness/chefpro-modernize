import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Las tareas vienen ya rellenadas para hamburguesería?',
    a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de una hamburguesería. Solo tienes que personalizar: ajustar tareas a tu local, borrar las que no apliquen y añadir las específicas de tu negocio. Las celdas editables están marcadas en verde.',
  },
  {
    q: '¿Incluye tareas de plancha, grill y smash burger?',
    a: 'Sí. Las tareas de plancha y grill cubren encendido, limpieza de superficie, control de temperatura, técnica smash burger (peso de bola, presión, tiempo), punto de carne (rare a well done) y limpieza entre turnos.',
  },
  {
    q: '¿Incluye tareas de freidora y control de aceite?',
    a: 'Sí. Hay tareas específicas para encendido y apagado de freidora, test polares del aceite, filtrado diario, cambio de aceite programado y control de temperatura para patatas, aros de cebolla y otros acompañamientos.',
  },
  {
    q: '¿En qué se diferencia de Trail u otras apps?',
    a: 'Trail cobra €60-75 al mes por local y requiere tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €12, pago único. Sin suscripción, sin internet, ilimitado en locales.',
  },
  {
    q: '¿Puedo usarlo en varias hamburgueserías?',
    a: 'Sí. La licencia es personal — puedes usar los checklists en todos los establecimientos que gestiones. Ideal para cadenas de hamburgueserías y consultores.',
  },
  {
    q: '¿Incluye tareas de delivery y packaging de burger?',
    a: 'Sí. Las tareas cubren packaging correcto de burger (que no se desmonte), control de tiempos de entrega, gestión de riders, etiquetado, preparación de pedidos y cierre de plataformas de delivery.',
  },
];

export default function FaqAccordion() {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-3xl mx-auto">
        <FadeIn>
          <h2 className="text-2xl md:text-4xl font-bold text-white text-center mb-12">
            Preguntas <span className="text-[#FFD700]">Frecuentes</span>
          </h2>
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
