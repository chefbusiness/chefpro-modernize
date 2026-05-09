import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Qué permisos necesito para operar un food truck en España?',
    a: 'Los permisos varían por municipio, pero los principales son: licencia de venta ambulante, autorización sanitaria (registro sanitario RGSEAA), ITV del vehículo adaptado, alta en Hacienda (modelo 036/037), seguro de responsabilidad civil y permiso de ocupación de vía pública. El checklist incluye los 59 trámites organizados por fases y por CCAA.',
  },
  {
    q: '¿Qué requisitos debe cumplir el vehículo del food truck?',
    a: 'El vehículo debe pasar una ITV específica para vehículos adaptados, cumplir la normativa de instalaciones de gas (si aplica), tener depósitos de agua limpia y residual homologados, extracción de humos con filtros, generador eléctrico o conexión a red, y cumplir las medidas de seguridad contra incendios. Todo está detallado en la sección de equipamiento.',
  },
  {
    q: '¿Cuánto cuesta montar un food truck en España?',
    a: 'La inversión inicial oscila entre 45K y 85K EUR dependiendo de si compras un vehículo nuevo o de segunda mano, el nivel de equipamiento de cocina y los permisos de tu municipio. El plan financiero Excel desglosa todas las partidas: vehículo, adaptación, equipamiento cocina, permisos, marketing, stock inicial y fondo de maniobra.',
  },
  {
    q: '¿Cuál es la diferencia con planes de negocio gratuitos?',
    a: 'Los planes gratuitos son plantillas genéricas sin datos reales. Este plan incluye cifras del mercado español de street food 2026, ratios financieros profesionales (food cost 30 %, margen 65 %), cuadro de personal con Seg. Social, punto de equilibrio calculado (27 clientes/día a €12), checklist de 59 trámites verificado y guía de permisos por CCAA.',
  },
  {
    q: '¿Puedo presentar este plan al banco o a inversores?',
    a: 'Sí. El plan financiero Excel incluye P&L previsional a 3 años, punto de equilibrio, análisis de viabilidad financiera y 3 escenarios. El documento DOCX de 10 secciones complementa con análisis de mercado, modelo de negocio y plan operativo. Es el formato profesional que piden bancos y entidades como ICO emprendedores o ENISA.',
  },
  {
    q: '¿Cómo funciona la garantía?',
    a: '30 días. Si el plan de negocio no cumple tus expectativas, te devolvemos el 100 % de tu dinero. Sin preguntas, sin complicaciones. Queremos que montes tu food truck con total confianza.',
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
