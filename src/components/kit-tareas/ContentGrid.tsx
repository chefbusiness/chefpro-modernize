import {
  DoorOpen, ChefHat, ClipboardList, Users, CalendarDays,
  PartyPopper, FileEdit, Megaphone, Calendar, Building2, Wallet,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre', desc: '6 checklists: apertura cocina, sala, barra + cierre cocina, sala, barra. Cada tarea con responsable, cuándo y firma. 111 tareas ya escritas solo en este fichero.' },
  { icon: ChefHat, title: 'Partidas de Cocina', desc: 'Tareas antes, durante y después del servicio para partida de calientes, fríos y mise en place general. Control de tiempos y calidad.' },
  { icon: ClipboardList, title: 'Tareas del Manager', desc: 'Checklist diario, semanal por bloques (DÍA 1-5 + fin de semana, para que el bloque no se pierda si cierras los lunes) y mensual. Plus handover de cambio de turno.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists personalizados para: jefe de cocina, sous chef, jefe de sala, camarero y barman. Las responsabilidades diarias de cada puesto.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Limpieza profunda semanal por zona, revisión FIFO de cámaras y almacén, mantenimiento mensual de equipos y seguridad.' },
  { icon: PartyPopper, title: 'Eventos y Festivos', desc: 'Checklist pre-evento (48h→día), San Valentín, Navidad/Nochevieja, apertura y cierre de temporada de terraza.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas maestras ya estructuradas —por franja horaria, por área y por perfil— con las secciones y la zona o el responsable puestos: tú solo escribes tus tareas en las celdas verdes.' },
  { icon: Building2, title: 'Apertura y Cierre de Negocio', desc: 'Checklist del local completo (no solo cocina): luces, alarma, TPV, terraza. Responsable y hora límite precargados para cada tarea.' },
  { icon: Wallet, title: 'Arqueo y Registro de Caja', desc: 'Apertura y cierre de caja con recuento por denominaciones, fondo de caja y descuadre automático frente al Z del TPV. Incluye registro mensual con descuadre por fórmula.' },
  { icon: Megaphone, title: 'BONUS: Briefing Servicio', desc: 'Plantilla de briefing pre-servicio: reservas, platos del día, 86s, alérgenos, equipo del turno. Imprime y pega en el pase.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '22 fechas clave de hostelería con tareas asociadas y antelación recomendada, más 5 huecos para las tuyas.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-restaurante-apertura.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-manager.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-sala.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-limpieza.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-eventos.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-perfiles.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">9</span> Plantillas de Tareas Operativas + 2 Bonus (11 ficheros)
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla incluye ya escritas las tareas más habituales de un restaurante casual. Ajusta a tu local, imprime y delega.
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
