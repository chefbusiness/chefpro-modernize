import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Para quién está pensado este plan?',
    a: 'Para profesionales de la parrilla — argentinos, uruguayos, colombianos, asadores castellanos o emprendedores españoles con dominio del producto — que quieren montar un servicio premium itinerante de parrilla para eventos en España. Cubre tanto el cliente final particular (cumpleaños, bautizos, bodas íntimas en finca) como el cliente B2B (wedding planners, agencias de eventos, hoteles, empresas, restaurantes que contratan show cooking en directo).',
  },
  {
    q: '¿Sirve si nunca he montado mi propio negocio antes?',
    a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. Incluye la constitución como autónomo (tarifa plana 80 EUR/mes el primer año), alta IAE 677.9, plan APPCC adaptado a actividad itinerante y seguro RC profesional eventos. El checklist de 6 fases con 80-120 ítems no deja nada al azar.',
  },
  {
    q: '¿Qué diferencia hay con un Plan de Negocio de Asador con local fijo?',
    a: 'Todo. Modelo itinerante sin local: sin licencia de actividad clasificada (autorizaciones puntuales por evento), sin plantilla fija (ayudantes freelance bajo demanda), inversión 4-7 veces menor (3.500-5.000 EUR mínimo viable vs 70-130K EUR de un asador fijo), ingresos por evento concentrados mayo-septiembre + diciembre (65-75 % facturación), captación B2B intensiva con wedding planners. El plan modela todos estos pilares.',
  },
  {
    q: '¿Cómo cubre el plan la regulación del fuego al aire libre por CCAA?',
    a: 'Con un anexo dedicado dentro del Plan de Negocio. Resumen operativo de 8 comunidades (Madrid, Cataluña, Baleares, Andalucía, Valencia, País Vasco, Galicia, Castilla y León) con tipo de autorización exigida, restricciones por temporada (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL) y excepciones para eventos en finca privada con licencia. Es el dolor real que ningún competidor ayuda a resolver.',
  },
  {
    q: '¿La plantilla de 96 proveedores incluye contactos verificables?',
    a: 'Sí. Cada proveedor lleva web, zona de cobertura, notas operativas, score y estado (validado / investigar). Carniceros mayoristas (Hidalgo, Casa López Mercamadrid, Tres Jotas Mercabarna, El Capricho León), proveedores de carbón quebracho (Tienda Biomasa, Ricosan Carborec), GGM Gastro España, Brogas 1958, Texfire EPI y seguros Hiscox/Mapfre.',
  },
  {
    q: '¿Sirve para presentar al banco si necesito financiación?',
    a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (8-10 eventos break-even año 1), 3 escenarios de inversión, mix B2C+B2B desglosado y plan de cashflow con estacionalidad. Es el formato estándar que piden bancos para microcrédito o ICO emprendedores.',
  },
  {
    q: '¿Cómo funciona la garantía?',
    a: '30 días de devolución completa. Si el plan no cumple tus expectativas, te devolvemos el 100 % del importe sin preguntas. Los 11 entregables son tuyos para siempre + actualizaciones gratuitas.',
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
