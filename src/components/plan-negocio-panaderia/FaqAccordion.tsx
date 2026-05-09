import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Es un plan genérico o específico para panadería?',
    a: 'Es 100 % específico para panadería y obrador artesanal en España. Las partidas de inversión (horno profesional, amasadora, cámara fermentación), los ratios financieros (coste materia prima, merma, margen pan vs bollería), los costes de personal con turno madrugada y los trámites legales (RGSEAA obrador, licencia actividad) están adaptados al modelo panadero.',
  },
  {
    q: '¿Puedo presentar este plan al banco o a inversores?',
    a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años con estacionalidad navideña, punto de equilibrio por kilos diarios, análisis de viabilidad financiera y 3 escenarios. Es exactamente el formato que piden bancos para microcrédito o ICO emprendedores y leasing de equipamiento (horno, amasadora).',
  },
  {
    q: '¿Puedo modificar las cifras del Excel?',
    a: 'Sí, todas las celdas son editables y las fórmulas se recalculan automáticamente. Puedes cambiar el alquiler, los kilos producidos al día, el ticket medio, los salarios del maestro panadero y cualquier partida de inversión. Incluye hoja de instrucciones.',
  },
  {
    q: '¿Qué trámites legales incluye el checklist de apertura?',
    a: 'Más de 60 trámites organizados en 6 fases: constitución de la SL, RGSEAA obrador (Registro General Sanitario), licencias municipales (actividad, expositor en fachada), equipamiento (proyecto técnico, instalación de horno, salida de humos), RRHH (contratos panaderos, Seg. Social, PRL turno madrugada) y primeros 90 días de operación.',
  },
  {
    q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
    a: 'Los planes gratuitos son plantillas genéricas sin datos reales del sector panadero. Este plan incluye cifras del mercado español 2026 (10K+ panaderías, mix consumo barra/bollería/cafetería, tasa de cierre), ratios profesionales (materia prima 22-28 %, merma 3-5 %, margen pan >70 %, bollería >75 %), cuadro de personal con turno madrugada y un checklist de trámites verificado con la legislación obrador vigente.',
  },
  {
    q: '¿Cómo funciona la garantía?',
    a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que abras tu panadería con total confianza.',
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
