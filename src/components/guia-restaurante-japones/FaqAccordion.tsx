import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Cuánto cuesta montar un restaurante japonés en España?',
    a: 'Entre 250.000€ y 500.000€ dependiendo de la ubicación, nivel de acabados, modelo (sushi-ya, ramen-ya, izakaya, omakase, robatayaki) y equipamiento japonés específico (suihanki, vitrina sashimi, robata, cuchillos yanagiba). Los márgenes en sake premium y whisky japonés (75-85%) ayudan a compensar el coste del pescado fresco.',
  },
  {
    q: '¿Dónde consigo pescado sashimi-grade y productos japoneses en España?',
    a: 'La guía incluye un capítulo completo (cap. 15) con proveedores: Mercamadrid, Mercabarna, lonjas, distribuidores especializados (Japan Sushi Express, Oriental Gourmet, Comercial Minamoto) y importadores directos de pescado premium, arroz Koshihikari, algas nori, sake y whisky japonés.',
  },
  {
    q: '¿Qué normativa debo cumplir para sushi y sashimi (anisakis)?',
    a: 'El RD 1420/2006 OBLIGA a congelar preventivamente todo pescado para consumo crudo a -20°C durante mínimo 24 horas. La guía incluye un PCC específico en el plan APPCC, el checklist de anisakis y el protocolo completo de trazabilidad. Es crítico: un caso positivo puede cerrar tu restaurante.',
  },
  {
    q: '¿Sushi-ya, ramen-ya, izakaya u omakase?',
    a: 'Depende de tu inversión, equipo y zona. Un ramen-ya tiene menor inversión y carta enfocada. Un sushi-ya exige un itamae cualificado pero ofrece máximo prestigio. Un omakase premium tiene ticket 80-180€ pero requiere barra de 8-14 plazas. La guía analiza los 7 modelos en detalle.',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. Las 8 plantillas incluyen fórmulas automáticas: plan financiero, escandallos de 15 platos japoneses (sashimi, ramen, nigiri, yakitori wagyu), menú engineering con coctelería de sake/whisky, cash flow y más.',
  },
  {
    q: '¿El DOCX es editable?',
    a: 'Sí. Recibes dos versiones: el PDF editorial con diseño profesional para leer y consultar, y el DOCX editable para personalizar, añadir notas y presentar a socios o inversores.',
  },
  {
    q: '¿Hay garantía de devolución?',
    a: '30 días de garantía completa. Si no estás satisfecho con el contenido, te devolvemos el 100% de tu dinero. Sin preguntas, sin complicaciones.',
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
