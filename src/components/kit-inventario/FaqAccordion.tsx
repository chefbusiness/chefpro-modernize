import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Sirve para cualquier tipo de restaurante?',
    a: 'Si. Las categorias estan pre-cargadas para hosteleria en general: carnicos, pescados, lacteos, verduras, secos, congelados, bebidas, limpieza. Solo elimina las que no apliquen a tu negocio y anade las que falten.',
  },
  {
    q: '¿Las plantillas se conectan entre si?',
    a: 'Si. Los niveles de stock alimentan automaticamente las sugerencias de pedido. Las fichas de proveedores se enlazan con los pedidos de compra. El control de mermas calcula el coste en tiempo real.',
  },
  {
    q: '¿Cumple con los requisitos de APPCC?',
    a: 'Si. La plantilla de recepcion incluye control de temperaturas y la de FIFO gestiona caducidades con alertas por colores. Ambas son trazables y auditables para inspecciones.',
  },
  {
    q: '¿En que se diferencia de apps de inventario?',
    a: 'Las apps de inventario cobran entre 50 y 100 EUR/mes por restaurante. Este kit cuesta 14 EUR, pago unico, sin suscripcion ni limite de productos. Y puedes personalizar todo al 100%.',
  },
  {
    q: '¿Puedo usarlo en varios restaurantes?',
    a: 'Si. La licencia es personal — puedes usar las plantillas en todos los establecimientos que gestiones. Ideal para grupos de restauracion, multi-unidades y consultores.',
  },
  {
    q: '¿Hay garantia de devolucion?',
    a: '30 dias de garantia completa. Si no estas satisfecho, 100% reembolso sin preguntas.',
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
