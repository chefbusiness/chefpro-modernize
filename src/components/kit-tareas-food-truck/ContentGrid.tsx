import {
  Truck, Wrench, ShieldCheck, MapPin,
  Users, UserCog, ClipboardList, PartyPopper, FileSpreadsheet,
  Calendar, CalendarDays,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: Truck, title: 'Setup y Teardown', desc: 'Montaje y desmontaje completos: generador, gas, agua, cocina, vitrina, puesto de servicio, caja y cierre del vehículo. Llegar, montar, vender y recoger sin huecos.' },
  { icon: Wrench, title: 'Operaciones Móviles y Vehículo', desc: 'Vehículo, generador, gestión de energía, gas, agua potable, aguas grises y residuos. Lo que mantiene el truck operativo todo el día sin sustos eléctricos ni sanitarios.' },
  { icon: ShieldCheck, title: 'APPCC Seguridad Alimentaria Móvil', desc: 'Temperaturas, cadena de frío durante transporte, manipulación en espacios reducidos, alérgenos y documentación sanitaria que exige el control oficial a una cocina móvil.' },
  { icon: MapPin, title: 'Permisos, Eventos y Localizaciones', desc: 'Licencias municipales, seguros de responsabilidad civil, certificados de manipulador, briefing pre-evento y tipos de evento (festivales, bodas, mercados, corporativos).' },
  { icon: Users, title: 'Tareas del Manager', desc: 'Planificación de rutas y eventos, stock, food cost, pricing por evento, RRSS, reservas privadas y reporting semanal con KPIs operativos del truck.' },
  { icon: UserCog, title: 'Tareas por Perfil', desc: 'Tareas claras por perfil: chef de food truck, ayudante de cocina, cajero/servicio y conductor/técnico. Roles y responsabilidades sin solapes ni huecos.' },
  { icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Limpieza profunda del truck, mantenimiento del generador, ITV y revisiones del vehículo, auditoría APPCC móvil y revisión de permisos vigentes por localización.' },
  { icon: PartyPopper, title: 'Eventos y Temporadas', desc: 'Temporada alta y baja, festivales de música, bodas, eventos corporativos, mercados gastronómicos y rutas urbanas. Stock y carta dinámicos todo el año.' },
  { icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu food truck (tacos, hamburguesas, fusión, dulce, café, etc.).' },
  { icon: Calendar, title: 'BONUS: Briefing Pre-Evento', desc: 'Briefing pre-evento de 5 minutos: tipo de evento, logística de localización, menú y stock necesario, asignación de equipo y avisos clave para el día.' },
  { icon: CalendarDays, title: 'BONUS: Calendario Anual', desc: 'Año completo con eventos por mes, menú sugerido por temporada, mantenimiento del vehículo y generador, y acciones de marketing por estación.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-bar-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-barra.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-cocteleria.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-equipo.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-stock.jpg',
  '/lovable-uploads/ai-gallery/tareas-bar-terraza.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Checklists Operativos para Food Truck
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada checklist viene pre-rellenado con las tareas reales de un food truck profesional con setup y teardown, operaciones móviles, APPCC móvil, permisos y gestión de eventos. Solo ajusta a tu carta y ruta, imprime y empieza a operar con estándar profesional.
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
