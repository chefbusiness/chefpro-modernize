import {
  DoorOpen, Sandwich, ChefHat, Beer,
  Briefcase, Users, ClipboardList, CalendarDays, FileSpreadsheet,
  Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre Tapas Bar', desc: 'Barra, cocina, sala y terraza: vitrina de tapas, grifos de cerveza, mise en place, montaje de pizarra del día y cierre con arqueo de caja, limpiezas y temperaturas.' },
  { icon: Sandwich, title: 'Barra de Tapas y Pinchos', desc: 'Vitrina de tapas frías, montaje de pinchos, rotación FIFO, tapas del día, pizarra, control de mermas y reposición durante el servicio sin huecos en barra.' },
  { icon: ChefHat, title: 'Cocina de Raciones y Platos', desc: 'Plancha, freidora, cazuelas, guisos, emplatado y timing de servicio. Estándares de cocción, mise en place y cambios de turno con pase ordenado.' },
  { icon: Beer, title: 'Bebidas: Cerveza, Vino y Vermut', desc: 'Grifos de cerveza (presión, CO2, temperatura, purga, líneas), vinos por copa, vermut con sifón, coctelería ligera, inventario de barra y control de mermas.' },
  { icon: Briefcase, title: 'Tareas del Manager', desc: 'Revenue diario, food cost, compras, gestión de proveedores, RRHH, marketing, reservas, terraza y reporting semanal con KPIs operativos del local.' },
  { icon: Users, title: 'Tareas por Perfil', desc: 'Tareas claras por perfil: jefe de cocina, cocinero de raciones, camarero de barra, camarero de sala/terraza y encargado. Roles y responsabilidades sin solapes.' },
  { icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Limpieza profunda de líneas de cerveza, inventarios, auditoría APPCC, evaluación de proveedores y rotación/evaluación de carta de tapas y raciones.' },
  { icon: CalendarDays, title: 'Eventos y Temporadas', desc: 'Tapas estacionales (gazpacho en verano, guisos en invierno, setas en otoño), Navidad, rutas de tapas, partidos de fútbol y after-work.' },
  { icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco con la estructura del kit para crear checklists a medida de tu tapas bar (clásico, moderno, gastrobar, tapas de barrio o terraza).' },
  { icon: Megaphone, title: 'BONUS: Briefing de Servicio', desc: 'Briefing pre-servicio de 5 minutos: tapas del día, bebidas destacadas, alérgenos activos, reservas, estado de terraza y avisos para barra y sala.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: 'Año completo con tapas por temporada, eventos gastronómicos, rutas de tapas, mantenimientos del local, formación del equipo y cierres por vacaciones.' },
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
              <span className="text-[#FFD700]">11</span> Checklists Operativos para Tapas Bar
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada checklist viene pre-rellenado con las tareas reales de un tapas bar o gastrobar profesional con barra de pinchos, cocina de raciones, cerveza de grifo y terraza. Solo ajusta a tu carta, imprime y empieza a operar con estándar profesional.
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
