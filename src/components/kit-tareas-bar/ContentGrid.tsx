import {
  DoorOpen, Wine, ClipboardList, Users, CalendarDays,
  PartyPopper, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre', desc: 'Checklists completos: mise en place de barra, cristalería, máquina de café, terraza, cierre administrativo y limpieza. ~55 tareas pre-rellenadas.' },
  { icon: Wine, title: 'Partidas de Barra', desc: 'Coctelería clásica (spirits, batches, jarabes), cerveza de grifo (CO₂, temperatura, purga), vinos por copa y bodega.' },
  { icon: ClipboardList, title: 'Tareas del Manager', desc: 'Checklist diario, semanal (lun-vie con foco por día) y mensual. Plus briefing con equipo y control de ambiente.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists para: head bartender, bartender, barback/auxiliar y camarero de sala/terraza.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Limpieza profunda de grifos, mantenimiento de espresso, inventario semanal por categoría (spirits, cerveza, vino, mixers).' },
  { icon: PartyPopper, title: 'Eventos y Festivos', desc: 'Nochevieja, Halloween, St. Patrick, after-work semanal, noches de cócteles especiales, catas y maridajes.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por franja horaria, por zona, por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Servicio', desc: 'Plantilla de briefing diario: cóctel del día, reservas, VIPs, promociones activas, equipo del turno.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '17 fechas clave para bares con preparación especial y antelación recomendada.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-cristaleria.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
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
              Cada plantilla viene pre-rellenada con las tareas reales de un bar de cocktails. Solo ajusta, imprime y delega.
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
