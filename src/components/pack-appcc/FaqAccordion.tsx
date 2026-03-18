import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Necesito conocimientos técnicos para usar las plantillas?',
    a: 'No. Todo viene pre-rellenado con datos reales de hostelería. Solo tienes que personalizar con los datos de tu establecimiento: nombre de los platos para la matriz de alérgenos, equipos de frío, zonas de limpieza. Las fórmulas y alertas funcionan automáticamente.',
  },
  {
    q: '¿Estas plantillas sirven para pasar la inspección de Sanidad?',
    a: 'Sí. Cubren todos los registros que exige la normativa APPCC en España: temperaturas, limpieza, trazabilidad, alérgenos, HACCP, control de plagas, aceite y agua. Están diseñadas para cumplir los requisitos del Real Decreto 1021/2022 y el Reglamento UE 1169/2011.',
  },
  {
    q: '¿Funcionan con Google Sheets?',
    a: 'Sí. Puedes importar los archivos .xlsx directamente a Google Sheets y todas las fórmulas se mantienen. También son compatibles con LibreOffice Calc y Apple Numbers. Los documentos imprimibles están optimizados para formato A4.',
  },
  {
    q: '¿Puedo personalizar las plantillas para mi restaurante?',
    a: 'Totalmente. Puedes añadir zonas de limpieza, equipos de frío, platos a la matriz de alérgenos, peligros al análisis HACCP. Las celdas editables están marcadas en verde. Las fórmulas y alertas se adaptan automáticamente.',
  },
  {
    q: '¿Incluye actualizaciones si cambia la normativa?',
    a: 'Sí. Tienes acceso de por vida al dashboard online. Si hay cambios en la normativa APPCC, actualizaremos las plantillas y las tendrás disponibles sin coste adicional.',
  },
  {
    q: '¿Para qué tipo de establecimiento sirven?',
    a: 'Para cualquier negocio de hostelería: restaurantes, bares, cafeterías, hoteles, catering, obradores, food trucks, comedores colectivos. La normativa APPCC es obligatoria para todos.',
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
