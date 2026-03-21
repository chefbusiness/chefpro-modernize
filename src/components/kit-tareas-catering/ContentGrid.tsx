import {
  ChefHat, Truck, ClipboardList, Users, Tent,
  PartyPopper, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: ChefHat, title: 'Producción Off-Site', desc: 'Mise en place en cocina central: elaboraciones D-1, cocciones día D, emplatado previo, empaquetado en GN y contenedores isotérmicos. ~30 tareas pre-rellenadas.' },
  { icon: Truck, title: 'Transporte y Logística', desc: 'Carga, cadena de frío, monitorización de temperatura, descarga en venue. Cumple normativa APPCC de transporte.' },
  { icon: ClipboardList, title: 'Tareas del Event Manager', desc: 'Coordinación semana previa, día del evento (pre-servicio, durante, post) y retrospectiva con equipo.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Checklists para: chef de evento, maître, camarero/runner, barman. Cada rol sabe qué hacer antes, durante y después.' },
  { icon: Tent, title: 'Montaje y Desmontaje', desc: 'Cocina temporal, sala, buffet/estaciones, check pre-apertura. Desmontaje: sala, cocina, carga y salida.' },
  { icon: PartyPopper, title: 'Tipos de Evento', desc: 'Bodas, corporativos, cocktail/standing, eventos outdoor. Checklists específicos para cada formato.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por fase, por zona, por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Pre-Evento', desc: 'Plantilla de briefing 30 min antes de puertas: evento, menú, alérgenos, equipo, VIPs y protocolo.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '20 fechas clave para catering: bodas, corporativos, Navidad, comuniones. Con antelación recomendada.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-catering-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-catering-montaje.jpg',
  '/lovable-uploads/ai-gallery/tareas-catering-servicio.jpg',
  '/lovable-uploads/ai-gallery/tareas-catering-cocina.jpg',
  '/lovable-uploads/ai-gallery/tareas-catering-transporte.jpg',
  '/lovable-uploads/ai-gallery/tareas-catering-equipo.jpg',
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
              Cada plantilla viene pre-rellenada con las tareas reales de una empresa de catering profesional. Solo ajusta, imprime y delega.
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
