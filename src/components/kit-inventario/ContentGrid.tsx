import {
  Package, Users, ShoppingCart, ClipboardCheck, Trash2,
  RotateCcw, BarChart3, Clock, Calculator,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: Package, title: 'Inventario de Stock Diario', desc: 'Control de stock por zona (cocina, barra, almacen) con par levels, alertas de reposicion automaticas y valoracion de stock. Semaforo rojo/amarillo/verde.' },
  { icon: Users, title: 'Fichas de Proveedores', desc: 'Directorio completo, comparativa de precios entre 5 proveedores por producto, evaluacion de calidad/precio/entrega y condiciones comerciales.' },
  { icon: ShoppingCart, title: 'Pedidos de Compra', desc: 'Generacion automatica de pedidos desde niveles de stock. Dropdown de proveedores, subtotales con IVA y formato imprimible para enviar.' },
  { icon: ClipboardCheck, title: 'Recepcion de Mercancias', desc: 'Checklist de verificacion: cantidad, calidad, temperatura, caducidad. Registro de incidencias y discrepancias vs pedido original.' },
  { icon: Trash2, title: 'Control de Mermas', desc: 'Registro diario por categoria (caducidad, preparacion, devolucion). Coste automatico, dashboard mensual y plan de accion. Objetivo: <3%.' },
  { icon: RotateCcw, title: 'FIFO y Caducidades', desc: 'Control de rotacion First In First Out con alertas por colores: rojo (caduca manana), amarillo (3 dias), verde (OK). Mapa de almacen incluido.' },
  { icon: BarChart3, title: 'Analisis de Costes de Compras', desc: 'Coste por categoria, evolucion mensual, top 20 productos, alertas de variacion de precios (>5%) y dashboard de KPIs: food cost %, coste por cubierto.' },
  { icon: Clock, title: 'BONUS: Inventario Rapido Mensual', desc: 'Conteo simplificado de una pagina para inventario mensual completo. Auto-calcula valoracion y variaciones vs mes anterior.' },
  { icon: Calculator, title: 'BONUS: Calculadora Punto de Pedido', desc: 'Calcula cuando pedir cada ingrediente segun consumo diario, tiempo de entrega y stock de seguridad. Simulador de demanda variable.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/inventario-hero.jpg',
  '/lovable-uploads/ai-gallery/inventario-almacen.jpg',
  '/lovable-uploads/ai-gallery/inventario-recepcion.jpg',
  '/lovable-uploads/ai-gallery/inventario-proveedores.jpg',
  '/lovable-uploads/ai-gallery/inventario-cocina.jpg',
  '/lovable-uploads/ai-gallery/inventario-analisis.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">9</span> Plantillas de Control de Inventario
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla incluye formulas automaticas y esta disenada para la realidad de la hosteleria. Solo ajusta a tu negocio y empieza a controlar.
            </p>
          </div>
        </FadeIn>
        <FadeIn>
          <div className="grid grid-cols-3 md:grid-cols-6 gap-2 mb-12 rounded-xl overflow-hidden">
            {galleryImages.map((src, i) => (
              <div key={i} className="aspect-square overflow-hidden rounded-lg">
                <img src={src} alt="" className="w-full h-full object-cover hover:scale-110 transition-transform duration-500" loading="lazy" />
              </div>
            ))}
          </div>
        </FadeIn>
        <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
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
