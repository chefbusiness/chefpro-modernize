import {
  Sunrise, Wheat, Flame, Store,
  Users, UserCog, ClipboardList, Gift, FileSpreadsheet,
  Calendar, CalendarDays,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: Sunrise, title: 'Apertura y Cierre (Turno Madrugada)', desc: 'Apertura del obrador desde las 03:00, encendido y precalentamiento de hornos, masas del día, división y formado, primera hornada, apertura de tienda y cierre con limpieza profunda.' },
  { icon: Wheat, title: 'Masas Madre y Fermentación', desc: 'Refresco de masa madre natural, pre-fermentos como poolish y biga, control de temperatura, hidratación y tiempos. Protocolos para recuperar masas que pierden fuerza.' },
  { icon: Flame, title: 'Hornos y Cocción', desc: 'Horno de piso (solera refractaria), rotativo y de convección con vapor. Temperaturas, tiempos, grenado, carga óptima y uso del vapor para cada tipo de pan y bollería.' },
  { icon: Store, title: 'Expositor y Venta', desc: 'Montaje del expositor, rotación de producto, etiquetado obligatorio, atención al cliente, gestión de cola en horas punta y reposición a lo largo del día.' },
  { icon: Users, title: 'Tareas del Manager', desc: 'Planificación de producción semanal, stock de harinas y materias primas, food cost, pricing por línea, gestión de proveedores y reporting con KPIs del obrador.' },
  { icon: UserCog, title: 'Tareas por Perfil', desc: 'Maestro panadero, oficial de obrador, ayudante de panadería y dependiente de tienda. Roles claros sin solapes ni huecos en producción ni en línea de venta.' },
  { icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Limpieza profunda de hornos, revisión de harinas y materias primas, calibración de básculas y termómetros, auditoría APPCC y mantenimiento preventivo del obrador.' },
  { icon: Gift, title: 'Eventos y Temporadas', desc: 'Navidad, Reyes, Semana Santa, San Juan y otras campañas con panes especiales y bollería de temporada. Producción estacional planificada con margen y stock controlado.' },
  { icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu panadería u obrador (panes especiales, sin gluten, ecológicos, bollería, salados…).' },
  { icon: Calendar, title: 'BONUS: Briefing Producción Diaria', desc: 'Briefing de producción del día: cantidades por línea, masas activas, hornadas planificadas, equipo asignado y avisos clave para arrancar la jornada sin sorpresas.' },
  { icon: CalendarDays, title: 'BONUS: Calendario Anual', desc: 'Año completo con producción por mes, panes de temporada, mantenimiento programado de hornos y maquinaria, y acciones de marketing por estación.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/use-case-panadero-hero.jpg',
  '/lovable-uploads/ai-gallery/use-case-panadero-fermentacion.jpg',
  '/lovable-uploads/ai-gallery/use-case-panadero-masa.jpg',
  '/lovable-uploads/ai-gallery/use-case-panadero-horneado.jpg',
  '/lovable-uploads/ai-gallery/use-case-panadero-panes.jpg',
  '/lovable-uploads/ai-gallery/use-case-panadero-team.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Checklists Operativos para Panadería
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada checklist viene pre-rellenado con las tareas reales de un obrador profesional con turno madrugada, masas madre y pre-fermentos, hornos de piso y rotativo, expositor y venta. Solo ajusta a tu surtido de panes, imprime y empieza a producir con estándar artesano.
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
