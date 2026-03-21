import {
  DoorOpen, Croissant, ClipboardList, Users, CalendarDays,
  PartyPopper, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre', desc: '6 checklists: apertura y cierre de obrador, horno, vitrina y despacho. Cada tarea con responsable, hora límite y firma. ~45 tareas pre-rellenadas.' },
  { icon: Croissant, title: 'Partidas de Producción', desc: 'Masas y fermentación (croissant, brioche, pan), cremas y rellenos (pastelera, ganache, mousse), decoración y montaje de vitrina.' },
  { icon: ClipboardList, title: 'Tareas del Manager', desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus handover de cambio de turno con traspaso de información.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists personalizados para: jefe pastelero, pastelero oficial, ayudante de pastelería y dependiente de vitrina.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de hornos, amasadora y laminadora.' },
  { icon: PartyPopper, title: 'Eventos y Festivos', desc: 'Navidad (roscón, turrones), San Valentín (bombones, tartas corazón), Semana Santa (torrijas, monas), Día de la Madre y más.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por franja horaria, por zona, por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Servicio', desc: 'Plantilla de briefing diario: producción del día, encargos especiales, alérgenos, equipo del turno. Imprime y pega en obrador.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '17 fechas clave de pastelería con producción especial y antelación recomendada. Añade tus fechas locales.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-pasteleria-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-pasteleria-horno.jpg',
  '/lovable-uploads/ai-gallery/tareas-pasteleria-masas.jpg',
  '/lovable-uploads/ai-gallery/tareas-pasteleria-decoracion.jpg',
  '/lovable-uploads/ai-gallery/tareas-pasteleria-vitrina.jpg',
  '/lovable-uploads/ai-gallery/tareas-pasteleria-equipo.jpg',
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
              Cada plantilla viene pre-rellenada con las tareas reales de una pastelería / obrador. Solo ajusta, imprime y delega.
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
