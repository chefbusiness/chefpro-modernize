import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Necesito Excel avanzado para usar las plantillas?',
    a: 'No. Las plantillas vienen con todo configurado: fórmulas, mermas, validaciones. Solo introduces tus ingredientes, cantidades y precios. Todo se calcula automáticamente.',
  },
  {
    q: '¿Funcionan con Google Sheets?',
    a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers.',
  },
  {
    q: '¿Los datos de merma son fiables?',
    a: 'Sí. Son los estándares utilizados en hostelería profesional y en consultoría gastronómica. Cubren 16 categorías de ingredientes con mermas mínimas, máximas y típicas. Puedes ajustarlas a tu realidad.',
  },
  {
    q: '¿Puedo personalizar las plantillas?',
    a: 'Totalmente. Puedes añadir ingredientes, modificar precios, ajustar mermas, cambiar el food cost objetivo y añadir tus propias fotos de platos. Las celdas editables están marcadas en verde.',
  },
  {
    q: '¿Incluye actualizaciones futuras?',
    a: 'Sí. Tienes acceso de por vida al dashboard online. Cuando añadamos nuevas plantillas o mejoras, las recibirás sin coste adicional.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: 'Sí. 30 días de garantía completa. Si las plantillas no te ayudan a controlar tu food cost, te devolvemos el 100% sin hacer ninguna pregunta.',
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
