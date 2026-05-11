import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Para quién está pensado este plan?',
    a: 'Para chefs y emprendedores en España que quieren montar un servicio premium de catering temático para eventos especializado en cocinas del mundo (japonés, mexicano, italiano, argentino, peruano, indio, vegano, BBQ texano, mediterráneo, etc.). Cubre tanto el cliente B2C (bodas multiculturales, cumpleaños temáticos, aniversarios) como el B2B (corporate brand events, embajadas, wedding planners, agencias eventos, hoteles boutique 4-5 estrellas, festivales gastronómicos). Es el único plan del mercado español enfocado en multi-concepto, no en monoproducto.',
  },
  {
    q: '¿Qué hace este kit diferente del Parrillero, Paellero o Chef Privado?',
    a: 'Esos productos son monoconcepto (un único producto/servicio: parrilla, paella o chef privado). Este es el ÚNICO multi-concepto: enseña a montar 3-5 cocinas del mundo en paralelo en un mismo evento (ejemplo: sushi-bar + pizza al horno de leña + asado argentino simultáneamente). Esto justifica ticket 70-130 €/pax frente a 45-85 €/pax monoconcepto, con márgenes 30-40 % más altos. Pensado para emprendedores que quieren un sistema operativo, no una receta.',
  },
  {
    q: '¿Sirve si nunca he montado mi propio negocio antes?',
    a: 'Sí. El plan está pensado para chefs que arrancan desde cero. Incluye constitución autónomo (tarifa plana 80 EUR/mes primer año), alta IAE 677.9, plan APPCC móvil multi-concepto, RGSEAA, seguro RC profesional eventos con cláusula intoxicación. La guía de especialización progresiva te orienta para empezar con 1-2 conceptos dominados y añadir 1-2/año. El checklist de 6 fases con 110 hitos no se te escapa nada.',
  },
  {
    q: '¿Cuántos conceptos temáticos cubre el plan?',
    a: 'El plan documenta 12 conceptos pre-empaquetados (sushi-bar omakase, tacos al pastor + trompo móvil, trattoria italiana, asado argentino, ceviche peruano, marisquería gallega, tandoor indio, mediterráneo griego/turco, plant-based premium, brasileño rodízio, BBQ texano slow-smoked, brunch internacional). Cada uno con menú propuesto + escandallo + equipamiento clave + ambientación + operativa específica. La guía de especialización te orienta cómo elegir cuáles dominar primero según tu perfil y zona.',
  },
  {
    q: '¿La plantilla de 96 proveedores incluye contactos verificables?',
    a: 'Sí. Cada proveedor lleva web, zona de cobertura y notas operativas. 12 bloques: importadores asiáticos premium (EMB Food, Cominport, Garmiko, Janax) + latinos/mexicanos (Importaciones Cuesta, CMA, Jasa Internacional, Maíz Maya) + italiano/mediterráneo (Caputo Harinas, Italfoods, Galbani) + indio/tandoor (Spice Box, Patak\'s, TRS Foods, Bombay Spices, iCatering Indian) + BBQ texano (ALEXS BBQ, Dame la Brasa, Smokefire) + carniceros premium (Cesáreo Gómez, Discarlux, El Capricho León, Treviño) + pescaderías + vegano + equipamiento (Wokinox, Josper, Pizza Party, Sammic) + vajilla (Pordamsa, Steelite, Schönwald) + plataformas. Verifica con cada uno antes de cerrar acuerdos.',
  },
  {
    q: '¿Cómo cubre el plan la regulación de catering itinerante por CCAA?',
    a: 'Con un anexo dedicado en el Plan de Negocio. Resumen operativo de 17 comunidades autónomas: Registro Sanitario CCAA + RGSEAA, requisitos cocina cliente, normativa transporte alimentos, etiquetado bilingüe (Cataluña, País Vasco), trámites telemáticos vs presenciales y plazos. Plus orientación específica APPCC multi-concepto (cada concepto tiene riesgos distintos: pescado crudo sushi vs cordero asado argentino vs tandoor indio).',
  },
  {
    q: '¿Sirve para presentar al banco si necesito financiación?',
    a: 'Sí. El Plan Financiero Excel incluye P&L previsional 3 años, punto de equilibrio (14 eventos/mes break-even año 1), 3 escenarios inversión (5.500 € mínimo viable / 11.500 € recomendado / 35.000 € premium), mix B2C+B2B desglosado por canal, plan cashflow con estacionalidad bodas + corporate. Formato estándar bancos para microcrédito o ICO emprendedores.',
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
