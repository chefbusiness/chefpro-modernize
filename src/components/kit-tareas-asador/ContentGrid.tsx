import {
  DoorOpen, Flame, Beef, Fish,
  Briefcase, Users, ClipboardList, CalendarDays, FileSpreadsheet,
  Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre Asador', desc: 'Checklists de encendido del Josper, parrilla abierta, cocina caliente y sala: brasas, carne expuesta, control de temperaturas, cierre completo y arqueo.' },
  { icon: Flame, title: 'Horno Josper y Brasas', desc: 'Protocolo Josper completo: encendido, precalentamiento, zonas de calor, tipos de carbón (encina, quebracho), regulación de compuertas y mantenimiento por turno.' },
  { icon: Beef, title: 'Maduración y Despiece de Carne', desc: 'Fichas dry-age y wet-age, control de piezas por peso y fecha, temperaturas de cámara (≤4 ºC), cálculo de mermas reales y temperaturas internas por punto de cocción.' },
  { icon: Fish, title: 'Parrilla Pescados y Verduras', desc: 'Técnicas para pescados (lubina, rodaballo, dorada) y verduras de temporada (espárragos, alcachofas, calçots) con tiempos por pieza y zonas de la parrilla.' },
  { icon: Briefcase, title: 'Tareas del Manager', desc: 'Pedidos de carne, control de stock de carbón, gestión del equipo, reservas para grupos grandes, revenue diario, comparativa de proveedores y reporting.' },
  { icon: Users, title: 'Perfiles: Parrillero y Equipo', desc: 'Tareas claras por perfil: parrillero/asador, ayudante de parrilla, cocina caliente, sala y servicio. Roles y responsabilidades sin solapes.' },
  { icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Limpieza profunda del Josper, cuchillería de trinchado y deshuesado, control de stock de carbón y carne, formación del equipo y revisión de proveedores.' },
  { icon: CalendarDays, title: 'Eventos y Temporadas', desc: 'Calçotada, chuletón para grupos, Nochevieja, San Valentín, temporadas de caza (octubre-febrero) y carnes de temporada con piezas especiales.' },
  { icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco con la estructura del kit para que crees checklists a medida del concepto exacto de tu asador (steakhouse, parrilla argentina, gastrobar con Josper).' },
  { icon: Megaphone, title: 'BONUS: Briefing de Servicio', desc: 'Briefing pre-servicio de 5 minutos: carnes del día, piezas especiales (chuletón maduro, tomahawk), grupos, stock de carbón y avisos para parrilla y sala.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: 'Año completo con temporadas de carne y caza, festivos, mantenimientos del Josper, formación del equipo y cierres por vacaciones.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-asador-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-asador-parrilla.jpg',
  '/lovable-uploads/ai-gallery/tareas-asador-josper.jpg',
  '/lovable-uploads/ai-gallery/tareas-asador-maduracion.jpg',
  '/lovable-uploads/ai-gallery/tareas-asador-equipo.jpg',
  '/lovable-uploads/ai-gallery/tareas-asador-emplatado.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Checklists Operativos para Asador
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada checklist viene pre-rellenado con las tareas reales de un asador profesional con horno Josper. Solo ajusta a tu carta, imprime y empieza a operar con estándar profesional.
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
