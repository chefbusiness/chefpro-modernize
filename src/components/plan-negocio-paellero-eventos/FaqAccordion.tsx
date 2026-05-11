import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Para quién está pensado este plan?',
    a: 'Para profesionales del arroz y la paella — mestres arrossers valencianos, paelleros murcianos, alicantinos, paelleros corporate de cualquier zona o emprendedores españoles con dominio del producto — que quieren montar un servicio premium itinerante de paella para eventos en España. Cubre tanto el cliente final particular (cumpleaños, comuniones, bautizos, bodas íntimas en finca) como el cliente B2B (wedding planners, agencias de eventos, hoteles 4-5 estrellas, ayuntamientos con fiestas populares, empresas que contratan team-building gastronómico).',
  },
  {
    q: '¿Sirve si nunca he montado mi propio negocio antes?',
    a: 'Sí. El plan está pensado para emprendedores que arrancan desde cero. Incluye la constitución como autónomo (tarifa plana 80 EUR/mes primer año), alta IAE 677.9, plan APPCC adaptado a actividad itinerante, RGSEAA, seguro RC profesional eventos con cláusula intoxicación. El checklist de 6 fases con 110 hitos no deja nada al azar.',
  },
  {
    q: '¿Qué diferencia hay con un Plan de Negocio de Restaurante de Arroces con local fijo?',
    a: 'Todo. Modelo itinerante sin local: sin licencia de actividad clasificada (autorizaciones puntuales por evento), sin plantilla fija (ayudantes freelance bajo demanda solo en eventos > 60 pax), inversión 4-7 veces menor (3.500-25.000 EUR según escenario vs 70-130K EUR de un restaurante fijo), ingresos por evento concentrados mayo-octubre + Falles (70-75 % facturación), captación B2B intensiva con wedding planners. El plan modela todos estos pilares.',
  },
  {
    q: '¿Cómo cubre el plan la regulación del fuego al aire libre por CCAA?',
    a: 'Con un anexo dedicado dentro del Plan de Negocio. Resumen operativo de 8 comunidades (Madrid, Cataluña, Baleares, Andalucía, Comunidad Valenciana, País Vasco, Galicia, Castilla y León) con tipo de autorización exigida, restricciones por temporada (planes INFOCA, PATRICOVA, PLADIGA, INFOCYL, IBANAT, SOSDeiak, PIDOM), excepciones para eventos en finca privada con licencia. La Comunidad Valenciana contempla excepciones culturales para Falles y festes tradicionales — vital para paelleros del Levante.',
  },
  {
    q: '¿La plantilla de 88 proveedores incluye contactos verificables?',
    a: 'Sí. Cada proveedor lleva web, zona de cobertura, notas operativas y estado (validado / investigar). Arroceros DO Valencia (Tartana, J. Sendra, Marjal, La Fallera) + arroz Bomba Calasparra DO + carniceros mayoristas (Hidalgo, Casa López Mercamadrid, Tres Jotas Mercabarna), mariscos del Mediterráneo (Pescaderías Coruñesas, Mariscos Linamar, Mariscos Castellet, Mariscos Nardín gamba roja DO Denia), verduras DO Levante (garrofó, ferraura, alcachofa), azafrán DO La Mancha y pimentón DO Vera, equipamiento Garcima/Vaello/GGM, vajilla Pordamsa/Steelite.',
  },
  {
    q: '¿Sirve para presentar al banco si necesito financiación?',
    a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (18-22 eventos break-even año 1), 3 escenarios de inversión (3.500 € mínimo viable / 8.500-12.000 € recomendado / 25.000 € premium), mix B2C+B2B desglosado y plan de cashflow con estacionalidad. Es el formato estándar que piden bancos para microcrédito o ICO emprendedores.',
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
