import {
  DoorOpen, Coffee, ClipboardList, Users, CalendarDays,
  PartyPopper, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre', desc: '6 checklists: apertura y cierre de barra, sala y terraza/cocina. Cada tarea con responsable, hora límite y firma. ~80 tareas pre-rellenadas.' },
  { icon: Coffee, title: 'Tareas del Barista', desc: 'Calibración de molinillo, purga de grupo, limpieza de vaporizador, latte art del día, stock de leches vegetales, control de temperatura de tazas.' },
  { icon: ClipboardList, title: 'Tareas del Manager', desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists personalizados para: barista jefe, barista, encargado de sala, camarero y responsable de cocina/obrador.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de equipos (cafetera, horno, vitrina).' },
  { icon: PartyPopper, title: 'Eventos y Festivos', desc: 'Checklist pre-evento (48h→día), brunch especial de festivos, pop-ups de temporada, apertura y cierre de terraza.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por franja horaria, por área, por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Servicio', desc: 'Plantilla de briefing pre-servicio: reservas, platos del día, alérgenos, equipo del turno. Imprime y pega en barra.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '17 fechas clave de hostelería con tareas asociadas y antelación recomendada. Añade tus fechas locales.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/appcc-control-temperaturas.jpeg',
  '/lovable-uploads/ai-gallery/appcc-limpieza-cocina.jpeg',
  '/lovable-uploads/ai-gallery/appcc-recepcion-mercancias.jpeg',
  '/lovable-uploads/ai-gallery/appcc-alergenos-carta.jpeg',
  '/lovable-uploads/ai-gallery/appcc-inspector-sanidad.jpeg',
  '/lovable-uploads/ai-gallery/appcc-registro-plantilla.jpeg',
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
              Cada plantilla viene pre-rellenada con las tareas reales de una cafetería / brunch. Solo ajusta, imprime y delega.
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
