import { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const faqs = [
  {
    q: '¿Sirve para cualquier tipo de restaurante?',
    a: 'Si. Las 10 categorias estan pre-cargadas para hosteleria en general: carnicos, pescados, lacteos, verduras/frutas, secos/granos, congelados, bebidas alcoholicas, bebidas no alcoholicas, limpieza y otros. Solo elimina las que no apliquen a tu negocio y anade las que falten.',
  },
  {
    q: '¿Las plantillas se conectan entre si?',
    a: 'Son nueve ficheros independientes y a proposito: no se enlazan entre si, porque un Excel enlazado se rompe en cuanto mueves un fichero de carpeta y verias #!REF!. Lo que si comparten es el idioma: las mismas 10 categorias en las 9 plantillas y las mismas unidades en las 8 de producto. En el inventario, la columna "A Pedir" te dice cuanto reponer cuando el stock baja del par level, y el desplegable de proveedores del pedido sale de la hoja Proveedores del propio fichero de pedidos, que rellenas una vez.',
  },
  {
    q: '¿Cumple con los requisitos de APPCC?',
    a: 'Te ayudan a documentar los registros de recepcion y trazabilidad que pide tu plan APPCC; no sustituyen al plan ni a un asesor. La plantilla de recepcion incluye control de temperaturas por familia de producto y la de FIFO/FEFO gestiona caducidades con alertas por colores, utiles para tus registros e inspecciones. Si necesitas el plan APPCC completo, revisa el Pack APPCC.',
  },
  {
    q: '¿En que se diferencia del software de inventario?',
    a: 'El software de inventario cobra entre 50 y 100 EUR/mes por restaurante. Este kit cuesta 14 EUR, pago unico, sin suscripcion ni limite de productos. Y puedes personalizar todo al 100%.',
  },
  {
    q: '¿Puedo usarlo en varios restaurantes?',
    a: 'Si. Licencia personal para tu negocio — puedes usar las plantillas en todos tus locales. ¿Eres consultor y quieres usarlas con tus clientes? Escribenos a info@aichef.pro.',
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
