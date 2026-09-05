import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Es un plan genérico o específico para panadería?',
    a: 'Es 100 % específico para panadería y obrador artesanal en España. Las partidas de inversión (horno profesional, amasadora, cámara de fermentación), los ratios financieros (coste de mercancía, merma, margen de pan frente a bollería), los costes de personal con turno de madrugada y los trámites legales (registro sanitario autonómico, licencia de actividad clasificada) están adaptados al modelo panadero. El IVA va incluso separado: el pan común al 4 % y la bollería y el café al 10 %.',
  },
  {
    q: '¿Puedo presentar este plan al banco o a inversores?',
    a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años con estacionalidad navideña, tesorería mes a mes, plan de financiación con cuadro de amortización y DSCR, punto de equilibrio en transacciones diarias y 3 escenarios. Es exactamente el formato que piden los bancos para microcrédito o ICO emprendedores y leasing de equipamiento (horno, amasadora).',
  },
  {
    q: '¿Puedo modificar las cifras del Excel?',
    a: 'Sí. Las celdas verdes son las que se teclean y las 737 fórmulas se recalculan solas: cambia el alquiler, las transacciones al día, el ticket medio sin IVA, los salarios del maestro panadero o cualquier partida de inversión. Las hojas van protegidas sin contraseña para que no borres una fórmula sin querer (Revisar → Desproteger hoja). Incluye hoja de instrucciones.',
  },
  {
    q: '¿Qué trámites legales incluye el checklist de apertura?',
    a: '66 trámites organizados en 6 fases: constitución de la SL; local y licencias (registro sanitario de tu Comunidad Autónoma, licencia clasificada, hojas de reclamaciones, gestor de residuos, DDD); equipamiento (proyecto técnico, instalación de horno, salida de humos); personal (contratos, Seguridad Social, registro horario, PRL del turno de madrugada); marketing (incluidos los acuerdos con el canal mayorista y las licencias de música); y primeros 90 días de operación.',
  },
  {
    q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
    a: 'Los planes gratuitos son plantillas genéricas sin un modelo detrás. Este plan trae un caso base calculado y auditado por el propio libro (cinco ratios con semáforo, todos en verde), los rangos de referencia que publica su hoja de instrucciones (coste de mercancía 25-38 %, personal 35-42 %, merma 5-10 %, margen bruto >62 %), tesorería mes a mes con la liquidación de IVA, plan de financiación con DSCR, cuadro de personal con turno de madrugada y auditoría de horas, y un checklist de 66 trámites con la norma citada artículo por artículo.',
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
