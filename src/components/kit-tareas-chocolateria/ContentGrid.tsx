import {
  CakeSlice, Beaker, ClipboardList, Users, CalendarDays,
  Gift, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: CakeSlice, title: 'Apertura y Cierre', desc: 'Checklists completos: vitrina, mostrador, caja, obrador, limpieza de equipos de templado y cierre administrativo. ~35 tareas pre-rellenadas.' },
  { icon: Beaker, title: 'Partidas de Producción', desc: 'Templado de chocolate, moldeado de bombones y tabletas, envasado, control de temperaturas, etiquetado y registro de lotes.' },
  { icon: ClipboardList, title: 'Tareas del Manager', desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus control de food cost y mermas de producción.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists para: maestro chocolatero/obrador, dependiente de tienda y encargado de turno. Cada puesto sabe qué hacer.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Deep clean de obrador, mantenimiento de temperadora, inventario semanal por categoría (coberturas, rellenos, packaging, moldes).' },
  { icon: Gift, title: 'Eventos y Temporada', desc: 'Navidad, San Valentín, Pascua, Día de la Madre. Producción especial, packaging gift, catálogo estacional.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por zona, por turno y por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Diario', desc: 'Plantilla de briefing diario: producción del día, pedidos especiales, stock packaging, equipo del turno, promociones activas.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '15 fechas clave para chocolaterías con preparación especial y antelación recomendada.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-chocolateria-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-chocolateria-vitrina.jpg',
  '/lovable-uploads/ai-gallery/tareas-chocolateria-obrador.jpg',
  '/lovable-uploads/ai-gallery/tareas-chocolateria-produccion.jpg',
  '/lovable-uploads/ai-gallery/tareas-chocolateria-servicio.jpg',
  '/lovable-uploads/ai-gallery/tareas-chocolateria-equipo.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">9</span> Plantillas de Tareas Operativas
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla viene pre-rellenada con las tareas reales de una chocolatería artesanal. Solo ajusta, imprime y delega.
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
