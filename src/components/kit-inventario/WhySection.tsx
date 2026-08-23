import { Utensils, Calculator, ShieldCheck, RefreshCw } from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const reasons = [
  {
    icon: Utensils,
    title: 'Disenadas para Hosteleria',
    desc: 'Las 10 categorias canonicas de la hosteleria pre-cargadas en las 9 plantillas, con desplegable: carnicos, pescados, lacteos, verduras/frutas, secos/granos, congelados, bebidas alcoholicas, bebidas no alcoholicas, limpieza y otros. No son plantillas genericas de almacen.',
  },
  {
    icon: Calculator,
    title: 'Formulas que Ahorran Dinero',
    desc: 'Par levels con alertas, coste de mermas automatico, variacion de precios entre proveedores y reparto del gasto por categoria. El food cost sobre consumo y el coste por cubierto, en el dashboard de KPIs. Los numeros trabajan por ti.',
  },
  {
    icon: ShieldCheck,
    title: 'Registros para tu Plan APPCC',
    desc: 'Te ayuda a documentar los registros de recepcion y trazabilidad que pide tu plan APPCC: control de temperaturas, trazabilidad FIFO/FEFO, registro de caducidades y mapa de almacen. No sustituye al plan ni a un asesor.',
  },
  {
    icon: RefreshCw,
    title: 'Software de Gestión Cobra 50-100 EUR/mes. Esto es 14 EUR',
    desc: 'Para controlar stock, proveedores y mermas sin pagar una suscripcion, esto es suficiente: en Excel, por un pago unico y sin usuarios que pagar. Vienen preparadas 100 referencias de inventario, 100 lineas de merma al mes, 50 lotes de FIFO y 30 lineas de pedido; ampliables desprotegiendo la hoja (no lleva contrasena).',
  },
];

export default function WhySection() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.04]">
        <img src="/lovable-uploads/ai-gallery/inventario-almacen.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/95" />
      <div className="relative max-w-6xl mx-auto z-10">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              ¿Por Que Este <span className="text-[#FFD700]">Kit</span>?
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              No son plantillas genericas de almacen. Son herramientas disenadas por un chef en cocina desde los 17 años y consultor gastronómico desde 2010.
            </p>
          </div>
        </FadeIn>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {reasons.map(({ icon: Icon, title, desc }, i) => (
            <FadeIn key={title} delay={i * 100}>
              <div className="text-center">
                <div className="w-14 h-14 rounded-2xl bg-[#FFD700]/20 flex items-center justify-center mx-auto mb-4">
                  <Icon className="w-7 h-7 text-[#FFD700]" />
                </div>
                <h3 className="text-white font-bold mb-2">{title}</h3>
                <p className="text-gray-400 text-sm leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
        <FadeIn>
          <div className="bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8 text-center">
            <p className="text-gray-300 mb-4 text-sm">Compatible con cualquier software de hojas de calculo:</p>
            <div className="flex flex-wrap justify-center gap-2">
              {[
                { label: 'Excel', highlight: true },
                { label: 'Google Sheets' },
                { label: 'LibreOffice' },
                { label: 'Imprimible A4' },
                { label: 'Apple Numbers' },
              ].map((pill) => (
                <span key={pill.label} className={`px-3 py-1.5 rounded-full text-sm font-medium ${pill.highlight ? 'bg-[#FFD700] text-black' : 'bg-white/10 text-gray-300'}`}>
                  {pill.label}
                </span>
              ))}
            </div>
          </div>
        </FadeIn>
      </div>
    </section>
  );
}
