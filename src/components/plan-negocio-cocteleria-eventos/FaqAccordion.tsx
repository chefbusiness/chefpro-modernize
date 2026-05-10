import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Es válido si nunca he montado una empresa de eventos antes?',
    a: 'Sí. El plan está pensado precisamente para emprendedores que arrancan desde cero. Incluye desde la constitución como autónomo (1 día, tarifa plana 80 EUR/mes el primer año) hasta los primeros 90 días de operación. El checklist de 71 trámites organizados en 6 fases no deja nada al azar.',
  },
  {
    q: '¿Qué diferencia hay con un Plan de Negocio para un bar fijo?',
    a: 'Todo. Modelo itinerante: sin licencia de actividad clasificada (autorizaciones puntuales por evento), sin plantilla fija (bartenders freelance bajo demanda), inversión 4-7x menor, ingresos por evento (no diarios), estacionalidad agresiva (mayo-septiembre + diciembre = 60-70 % facturación), captación B2B intensiva con wedding planners. El plan refleja todos estos pilares.',
  },
  {
    q: '¿La plantilla de 96 proveedores incluye contactos reales?',
    a: 'Sí. Cada proveedor lleva web/contacto, cobertura, precio orientativo, plazo y notas. Distribuidores oficiales como Damm (Fever-Tree), Disbesa (Schweppes HORECA), Latin Hotel (Spiegelau) y SERHS Equipments (Hoshizaki). Verifica con cada uno antes de cerrar acuerdos.',
  },
  {
    q: '¿Sirve para presentar al banco si necesito financiación?',
    a: 'Sí. El Plan Financiero Excel incluye P&L previsional a 3 años, punto de equilibrio (31 eventos/año break-even), escenarios pesimista/realista/optimista y cuadro de personal freelance. Es el formato que piden bancos para microcrédito o ICO emprendedores.',
  },
  {
    q: '¿Puedo personalizar la Carta de 15 Cocktails para mi marca?',
    a: 'Sí, el DOCX es totalmente editable. Cada cocktail incluye receta, escandallo, escalado por nº de invitados (50/100/200), glasería recomendada y consejo pro. Puedes usarlo como base y crear tu carta signature en pocas horas.',
  },
  {
    q: '¿Cómo funciona la garantía?',
    a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 9 entregables son tuyos para siempre + actualizaciones gratuitas.',
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
