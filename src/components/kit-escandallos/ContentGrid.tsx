import {
  UtensilsCrossed, Wine, CakeSlice, Truck, Coffee,
  BarChart3, Calculator, TrendingDown, ClipboardList, ChefHat, PartyPopper,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: UtensilsCrossed, title: 'Escandallo Estándar', desc: 'La plantilla más completa para platos a la carta. Introduce ingredientes, cantidades y precios de compra — las fórmulas calculan automáticamente la merma, el coste real por ración, el food cost % y el PVP sugerido según tu margen objetivo. Incluye zona para foto del plato terminado.' },
  { icon: ChefHat, title: 'Menú Degustación', desc: 'Diseñada para menús de 5 a 9 pases con escandallo individual por plato. La hoja resumen suma el coste total del menú completo, calcula el food cost global y sugiere el PVP por comensal. Perfecta para restaurantes gastronómicos y experiencias premium.' },
  { icon: ClipboardList, title: 'Menú del Día', desc: 'Estructura completa: primer plato, segundo, postre y extras (pan, bebida, café). Calcula automáticamente el coste total del menú y el PVP necesario para mantener tu margen. Incluye rotación semanal para planificar 5 menús diferentes con sus costes comparados.' },
  { icon: Wine, title: 'Cocktails y Bebidas', desc: 'Escandallo detallado de 4 cocktails con medidas exactas en cl/ml, coste por ingrediente y food cost unitario. Optimizada para barras con objetivo de food cost al 18-22%. Incluye cálculo de garnish, hielo y merma de destilados por evaporación y derrame.' },
  { icon: CakeSlice, title: 'Pastelería', desc: 'Plantilla especializada con mermas reales de pastelería: temperado de chocolate (12%), horneado de masas (8%), montaje de mousses. Incluye rendimiento por receta — cuántas raciones salen de cada elaboración. Con ejemplos de tarta, croissants y macarons listos para personalizar.' },
  { icon: PartyPopper, title: 'Catering', desc: 'La única plantilla que integra coste de materia prima + personal + logística + menaje en un solo presupuesto por persona. Define tu margen objetivo y obtén el precio por comensal al instante. Incluye checklist de evento y desglose para presentar al cliente.' },
  { icon: Coffee, title: 'Cafetería / Brunch', desc: 'Escandallos adaptados al formato cafetería con food cost objetivo del 25-30%. Incluye ejemplos reales: tostada de aguacate, açaí bowl, eggs benedict, carrot cake. Cada receta con coste real desglosado para que descubras qué platos te dan margen y cuáles te lo comen.' },
  { icon: Truck, title: 'Food Truck', desc: 'Plantilla pensada para street food: recetas rápidas con foco en velocidad de servicio y márgenes altos. Incluye smash burger, loaded fries y pulled pork con coste real por unidad. Calcula el punto de equilibrio diario: cuántas unidades necesitas vender para cubrir costes fijos.' },
  { icon: TrendingDown, title: 'Control de Mermas', desc: 'Sistema de registro semanal de mermas reales vs mermas estándar en 16 categorías de producto (carnes, pescados, frutas, lácteos…). Las celdas cambian de color automáticamente cuando la merma real supera el estándar. Incluye gráfico de evolución mensual para detectar tendencias.' },
  { icon: Calculator, title: 'Calculadora de PVP', desc: 'Introduce el coste de cualquier plato y obtén el PVP recomendado para 9 tipos de establecimiento: restaurante gastronómico, casual dining, fast casual, cafetería, food truck, catering, bar de copas, hotel y delivery. Cada uno con su rango de food cost objetivo del sector.' },
  { icon: BarChart3, title: 'Dashboard Mensual', desc: 'Panel de control con seguimiento de food cost durante 12 meses consecutivos. Registra compras, ventas y calcula el food cost real vs objetivo mes a mes. Incluye gráfico de evolución anual y alertas cuando el food cost supera tu límite. Tu cockpit financiero de cocina.' },
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
                <p className="text-gray-400 text-sm md:text-base leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
