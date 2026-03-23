import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Las tareas vienen ya rellenadas para chef privado?',
    a: 'Sí. Cada checklist viene pre-rellenado con las tareas reales de un chef privado profesional: gestión de clientes, transporte de equipo, APPCC móvil, ejecución de servicio y administración del negocio. Solo tienes que personalizar: ajustar tareas a tu tipo de servicio, borrar las que no apliquen y añadir las específicas.',
  },
  {
    q: '¿Sirve para diferentes tipos de chef privado?',
    a: 'Sí. Las plantillas cubren todos los tipos de servicio: cenas a domicilio, meal prep semanal, eventos privados, chef de yate/villa, clases de cocina y catering corporativo. Adapta lo que necesites según tu especialidad.',
  },
  {
    q: '¿Incluye gestión de alérgenos?',
    a: 'Sí, es una de las partes más críticas. La ficha de cliente incluye registro completo de los 14 alérgenos UE, intolerancias, dietas especiales y restricciones. El APPCC móvil tiene checklist de verificación de alérgenos antes de cada servicio.',
  },
  {
    q: '¿En qué se diferencia de apps de gestión?',
    a: 'Las apps de gestión cobran €40/mes y requieren tablets/móviles. Este kit te da las mismas listas de tareas en Excel por €18, pago único. Sin suscripción, sin internet, ilimitado en clientes.',
  },
  {
    q: '¿Puedo usarlo si trabajo con ayudante?',
    a: 'Sí. Los checklists están pensados para compartir con tu ayudante o segundo chef. El briefing pre-servicio es perfecto para alinear al equipo antes de cada evento.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: '30 días de garantía completa. Si no estás satisfecho, 100% reembolso sin preguntas.',
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
