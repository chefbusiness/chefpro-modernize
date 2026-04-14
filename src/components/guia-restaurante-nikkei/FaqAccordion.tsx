import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Cuánto cuesta montar un restaurante nikkei en España?',
    a: 'Entre 280.000€ y 520.000€ para 60 plazas, dependiendo de la ubicación, nivel de acabados y modelo (cevichería nikkei, barra tiraditos, omakase, casual premium). El equipamiento mixto (robata/josper, wok station, licuadoras para leches de tigre, yanagiba, molcajete) y la brigada especializada son los mayores costes. Los márgenes de pisco, sake y coctelería nikkei (75-85%) compensan el food cost del pescado premium.',
  },
  {
    q: '¿Dónde consigo ají amarillo, rocoto, pisco y productos peruanos en España?',
    a: 'La guía incluye directorio completo de importadores peruanos en España (Inkawasi, Latin Products y otros) para ají amarillo, ají limo, rocoto, maíz gigante, choclo, quinoa y salsas nikkei. Para pescado sashimi-grade: Mercamadrid, Mercabarna y Krustagroup. Para arroz Koshihikari, nori, sake: Japan Sushi Express, Oriental Gourmet. Pisco peruano: distribuidores especializados.',
  },
  {
    q: '¿Qué normativa aplica a tiraditos, ceviches nikkei y leches de tigre?',
    a: 'El RD 1420/2006 OBLIGA a congelar preventivamente todo pescado destinado a ser consumido crudo o marinado (tiraditos, ceviches nikkei, sashimi) a -20°C durante mínimo 24 horas. La guía incluye un PCC específico para pescado crudo Y para leches de tigre (cadena de frío), checklist anisakis y protocolo completo de trazabilidad.',
  },
  {
    q: '¿Cevichería nikkei, omakase nikkei o casual premium?',
    a: 'Depende de inversión, equipo y zona. Una cevichería nikkei tiene ticket 45-65€ y alta rotación. Un omakase nikkei tiene ticket 90-150€ pero requiere barra de 10-14 plazas y chef de máximo nivel. Un casual premium de 60 plazas balancea carta amplia y rentabilidad. La guía analiza los 6 modelos en detalle.',
  },
  {
    q: '¿Las plantillas Excel incluyen fórmulas?',
    a: 'Sí. Las 9 plantillas incluyen fórmulas automáticas: plan financiero a 3 años, escandallos de 15 platos nikkei (tiradito, ceviche nikkei, causa, maki acevichado, anticucho, chaufa mariscos), menú engineering con coctelería de pisco y sake, cash flow y break-even.',
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
