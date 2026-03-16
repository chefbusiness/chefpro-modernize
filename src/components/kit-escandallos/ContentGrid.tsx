import {
  UtensilsCrossed, Wine, CakeSlice, Truck, Coffee,
  BarChart3, Calculator, TrendingDown, ClipboardList, ChefHat, PartyPopper,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: UtensilsCrossed, title: 'Escandallo Estándar', desc: 'Plato a la carta con todos los cálculos' },
  { icon: ChefHat, title: 'Menú Degustación', desc: '5 pases con resumen de coste total' },
  { icon: ClipboardList, title: 'Menú del Día', desc: '3 platos + extras + PVP automático' },
  { icon: Wine, title: 'Cocktails y Bebidas', desc: '4 cocktails con medidas en cl/ml' },
  { icon: CakeSlice, title: 'Pastelería', desc: 'Recetas con mermas de repostería' },
  { icon: PartyPopper, title: 'Catering', desc: 'Coste por persona + presupuesto completo' },
  { icon: Coffee, title: 'Cafetería / Brunch', desc: 'Tostadas, bowls, eggs benedict' },
  { icon: Truck, title: 'Food Truck', desc: 'Burgers, fries, sándwiches rápidos' },
  { icon: TrendingDown, title: 'Control de Mermas', desc: '16 categorías con alertas automáticas' },
  { icon: Calculator, title: 'Calculadora de PVP', desc: 'PVP para 9 tipos de establecimiento' },
  { icon: BarChart3, title: 'Dashboard Mensual', desc: '12 meses con gráfico de food cost' },
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Plantillas Profesionales
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla incluye fórmulas automáticas, mermas precargadas, zona para foto del plato y formato listo para imprimir.
            </p>
          </div>
        </FadeIn>

        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {templates.map(({ icon: Icon, title, desc }, i) => (
            <FadeIn key={title} delay={i * 60}>
              <div className="bg-white/[0.03] border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/30 transition-all group">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 rounded-lg bg-[#FFD700]/15 flex items-center justify-center flex-shrink-0 group-hover:bg-[#FFD700]/25 transition-colors">
                    <Icon className="w-5 h-5 text-[#FFD700]" />
                  </div>
                  <div>
                    <h3 className="text-white font-bold text-sm mb-1">{title}</h3>
                    <p className="text-gray-500 text-xs leading-relaxed">{desc}</p>
                  </div>
                </div>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
