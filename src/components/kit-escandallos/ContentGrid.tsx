import {
  UtensilsCrossed, Wine, CakeSlice, Truck, Coffee,
  BarChart3, Calculator, TrendingDown, ClipboardList, ChefHat, PartyPopper,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: UtensilsCrossed, title: 'Escandallo Estándar', desc: 'Para platos a la carta. Calcula coste, merma, food cost % y PVP sugerido con fórmulas automáticas.' },
  { icon: ChefHat, title: 'Menú Degustación', desc: '5 pases con escandallo individual + hoja resumen que suma el coste total del menú completo.' },
  { icon: ClipboardList, title: 'Menú del Día', desc: 'Primer plato, segundo, postre + extras (pan, bebida, café). PVP automático del menú completo.' },
  { icon: Wine, title: 'Cocktails y Bebidas', desc: '4 cocktails detallados con medidas en cl/ml. Food cost de bar al 20%. Ideal para bartenders.' },
  { icon: CakeSlice, title: 'Pastelería', desc: 'Tarta de chocolate, croissants, macarons. Con mermas específicas de repostería y rendimiento por receta.' },
  { icon: PartyPopper, title: 'Catering', desc: 'Coste por persona + presupuesto completo del evento: personal, logística, menaje y margen objetivo.' },
  { icon: Coffee, title: 'Cafetería / Brunch', desc: 'Tostada de aguacate, açaí bowl, eggs benedict. Con food cost adaptado a cafetería (28%).' },
  { icon: Truck, title: 'Food Truck', desc: 'Smash burger, loaded fries, pulled pork. Recetas simples con foco en velocidad y márgenes altos.' },
  { icon: TrendingDown, title: 'Control de Mermas', desc: 'Registro semanal de mermas reales vs estándar en 16 categorías. Con alertas automáticas de desviación.' },
  { icon: Calculator, title: 'Calculadora de PVP', desc: 'Introduce el coste de tu plato y obtén el PVP sugerido para 9 tipos de establecimiento diferentes.' },
  { icon: BarChart3, title: 'Dashboard Mensual', desc: 'Seguimiento de food cost durante 12 meses. Compras, ventas, % food cost real vs objetivo con gráfico.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-garibaldi-fermentado.jpeg',
  '/lovable-uploads/ai-gallery/milhojas-vertical-de-vainilla-con-frambuesas-aichefpro-2.jpeg',
  '/lovable-uploads/ai-gallery/carpaccio-gambas.jpeg',
  '/lovable-uploads/ai-gallery/torrija-caramelizada-con-helado.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-tepache-pina-asada.jpeg',
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

        {/* Gallery strip */}
        <FadeIn>
          <div className="grid grid-cols-3 md:grid-cols-6 gap-2 mb-12 rounded-xl overflow-hidden">
            {galleryImages.map((src, i) => (
              <div key={i} className="aspect-square overflow-hidden rounded-lg">
                <img
                  src={src}
                  alt=""
                  className="w-full h-full object-cover hover:scale-110 transition-transform duration-500"
                  loading="lazy"
                />
              </div>
            ))}
          </div>
        </FadeIn>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {templates.map(({ icon: Icon, title, desc }, i) => (
            <FadeIn key={title} delay={i * 50}>
              <div className="group bg-white/5 border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/50 transition-all duration-300 h-full">
                <Icon className="w-8 h-8 text-[#FFD700] mb-3" />
                <h3 className="text-white font-semibold text-sm md:text-base mb-1.5">{title}</h3>
                <p className="text-gray-400 text-xs md:text-sm leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
