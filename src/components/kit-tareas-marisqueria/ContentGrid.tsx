import {
  DoorOpen, Droplets, ShieldCheck, Snowflake,
  Briefcase, Users, ClipboardList, CalendarDays, FileSpreadsheet,
  Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre Marisquería', desc: 'Vivero, expositor de hielo, cámaras, mise en place de salsas, montaje de sala con cubertería de marisco y cierre con arqueo, lavado de filtros y temperaturas.' },
  { icon: Droplets, title: 'Vivero, Lonjas y Pescado Fresco', desc: 'Control diario del vivero (temperatura del agua, oxígeno disuelto, salinidad, pH, densidad), compras en lonja e indicadores de frescura por pieza y especie.' },
  { icon: ShieldCheck, title: 'Trazabilidad y APPCC Marisco', desc: 'Registro de lotes, etiquetado UE 1379/2013, zona FAO, método de captura, alérgenos de crustáceos y moluscos y puntos críticos HACCP de la cadena del frío.' },
  { icon: Snowflake, title: 'Expositor y Barra de Mariscos', desc: 'Montaje del expositor de hielo, rotación FIFO, mantenimiento durante el servicio, apertura segura de ostras, navajas y almejas y reposición sin romper la cadena.' },
  { icon: Briefcase, title: 'Tareas del Manager', desc: 'Pedidos en lonja, gestión de proveedores, food cost por especie, revenue diario, RRHH, administración y reporting semanal de mermas y rotación.' },
  { icon: Users, title: 'Perfiles: Mariscador y Equipo', desc: 'Tareas claras por perfil: jefe de cocina/mariscador, partida de pescados, partida de mariscos, maître y camarero. Roles y responsabilidades sin solapes.' },
  { icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Limpieza profunda del vivero, inventarios, afilado de cuchillería de pescado, auditoría APPCC, evaluación de proveedores y formación del equipo.' },
  { icon: CalendarDays, title: 'Eventos y Temporadas', desc: 'Temporadas de pesca de España (percebes, gamba roja, centollo, bogavante), Navidad, Nochevieja, San Valentín y vedas oficiales por especie.' },
  { icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco con la estructura del kit para que crees checklists a medida de tu marisquería (gallega, mediterránea, restaurante de pescado, gastrobar de mariscos).' },
  { icon: Megaphone, title: 'BONUS: Briefing de Servicio', desc: 'Briefing pre-servicio de 5 minutos: capturas del día, alérgenos activos, reservas VIP, maridajes recomendados y avisos para barra y sala.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: 'Año completo con temporadas de pesca por mes, eventos, mantenimientos del vivero, formación del equipo y cierres por vacaciones.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-marisqueria-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-marisqueria-vivero.jpg',
  '/lovable-uploads/ai-gallery/tareas-marisqueria-expositor.jpg',
  '/lovable-uploads/ai-gallery/tareas-marisqueria-mariscos.jpg',
  '/lovable-uploads/ai-gallery/tareas-marisqueria-equipo.jpg',
  '/lovable-uploads/ai-gallery/tareas-marisqueria-emplatado.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Checklists Operativos para Marisquería
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada checklist viene pre-rellenado con las tareas reales de una marisquería profesional con vivero, expositor de hielo y trazabilidad APPCC. Solo ajusta a tu carta, imprime y empieza a operar con estándar profesional.
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
