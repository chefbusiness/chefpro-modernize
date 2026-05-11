import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Para quién está pensado este plan?',
    a: 'Para chefs profesionales que quieren montar un servicio premium de chef privado y showcooking a domicilio en España. Cubre desde el cliente final particular (cumpleaños, aniversarios, San Valentín, brunch privado, cenas ejecutivas) hasta el cliente B2B (empresas con showcooking corporate, hoteles boutique 4-5 estrellas con servicio in-suite, wedding planners con cenas de ensayo y pre-bodas, agencias de eventos con cooking class team-building y cenas de directiva fin de año).',
  },
  {
    q: '¿Sirve si nunca he montado mi propio negocio antes?',
    a: 'Sí. El plan está pensado para chefs solopreneurs que arrancan desde cero. Incluye constitución como autónomo (tarifa plana 80 EUR/mes primer año), alta IAE 677.9, plan APPCC móvil adaptado a servicio domiciliario, RGSEAA, seguro RC profesional eventos con cláusula intoxicación. El checklist de 6 fases con 108 hitos no deja que se te escape nada.',
  },
  {
    q: '¿Qué diferencia hay con un Personal Chef o un Caterer?',
    a: 'Mucha. El plan incluye una guía dedicada que clarifica las tres figuras: Chef Privado (modelo por evento, ticket 580-2.200 EUR, marca personal, multi-cliente), Personal Chef (recurrente con 1-3 clientes fijos high-net-worth, 1.800-4.500 EUR/mes, exclusividad parcial) y Caterer (escalable con cocina central y plantilla, 8.000-150.000 EUR por evento). El plan recomienda empezar siempre por chef privado y pivotar después si encaja con tu vida y negocio.',
  },
  {
    q: '¿Cómo cubre el plan la regulación de catering itinerante por CCAA?',
    a: 'Con un anexo dedicado dentro del Plan de Negocio. Resumen operativo de 17 comunidades autónomas con: tipo de Registro Sanitario CCAA + RGSEAA, requisitos sobre la cocina del cliente, cumplimiento normativa transporte alimentos, etiquetado bilingüe (Cataluña, País Vasco), trámites telemáticos vs presenciales y plazos por CCAA. Plus orientación regulatoria sobre la cocina del cliente final.',
  },
  {
    q: '¿La plantilla de 96 proveedores incluye contactos verificables?',
    a: 'Sí. Cada proveedor lleva web, zona de cobertura, notas operativas y estado (validado / investigar). Cuchillería japonesa (Tojiro, Yoshihiro Cutlery, Kai Shun, Misono, Sakai Takayuki) + sous-vide Anova/Polyscience/Sammic + vajilla blanca premium (Pordamsa, Steelite, Schönwald, Villeroy & Boch, Rosenthal) + carniceros premium (Cesáreo Gómez, Discarlux, Treviño, El Capricho León) + pescaderías Coruñesas + microbrotes (Aitana, MyHerbs, Petras) + caviar Riofrío + trufa Soria + AOVE DO (Castillo de Canena, Oro Bailén, Núñez de Prado). Verifica con cada uno antes de cerrar acuerdos.',
  },
  {
    q: '¿Sirve para presentar al banco si necesito financiación?',
    a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (9-12 eventos/mes break-even año 1), 3 escenarios de inversión (4.500 € mínimo viable / 11.500 € recomendado / 30.000 € premium), mix B2C+B2B desglosado, plan de cashflow con picos diciembre y verano. Es el formato estándar que piden bancos para microcrédito o ICO emprendedores.',
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
