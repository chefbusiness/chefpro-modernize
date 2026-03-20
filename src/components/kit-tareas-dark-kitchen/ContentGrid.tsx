import {
  DoorOpen, Warehouse, ClipboardList, Users, CalendarDays,
  PartyPopper, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre', desc: '6 checklists: apertura y cierre de estaciones de produccion, zona de empaquetado, expedicion y zona de riders. Cada tarea con responsable, hora limite y firma. ~80 tareas pre-rellenadas.' },
  { icon: Warehouse, title: 'Estaciones de Produccion', desc: 'Encendido de equipos por estacion, mise en place multi-marca, control de temperaturas, reposicion de envases y packaging diferenciado por marca virtual.' },
  { icon: ClipboardList, title: 'Tareas del Manager', desc: 'Checklist diario, semanal (lun-vie con foco por dia) y mensual. Plus handover de cambio de turno con traspaso de informacion entre turnos.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists personalizados para: cocinero multi-marca, empaquetador/expedidor, gestor de plataformas y encargado/a de operaciones.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Limpieza profunda semanal por zona, revision FIFO de camaras, mantenimiento mensual de equipos, calibracion de balanzas y revision de packaging.' },
  { icon: PartyPopper, title: 'Eventos y Festivos', desc: 'Checklist pre-evento (48h y dia), picos de demanda (viernes/sabado noche), festivos con menu limitado, gestion de saturacion de plataformas.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por franja horaria, por area, por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Servicio', desc: 'Plantilla de briefing pre-turno: marcas activas, promociones por plataforma, platos agotados, equipo del turno. Imprime y pega en cocina.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '17 fechas clave de hosteleria con tareas asociadas y antelacion recomendada. Anade tus fechas locales.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-dk-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-dk-produccion.jpg',
  '/lovable-uploads/ai-gallery/tareas-dk-empaquetado.jpg',
  '/lovable-uploads/ai-gallery/tareas-dk-expedicion.jpg',
  '/lovable-uploads/ai-gallery/tareas-dk-tablets.jpg',
  '/lovable-uploads/ai-gallery/tareas-dk-equipo.jpg',
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
              Cada plantilla viene pre-rellenada con las tareas reales de una dark kitchen multi-marca. Solo ajusta, imprime y delega.
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
