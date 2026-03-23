import {
  ChefHat, Beaker, FlaskConical, Users, CalendarDays,
  Wine, Sparkles, Camera, FileEdit, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: ChefHat, title: 'Apertura y Cierre', desc: 'Checklists completos: cocina, pass, sala, bodega, mise en place degustacion, cierre administrativo. ~40 tareas pre-rellenadas para fine dining.' },
  { icon: Beaker, title: 'Mise en Place Degustacion', desc: 'Checklist de preparacion de cada pase del menu degustacion: bases, salsas, guarniciones, pre-emplatado, temperaturas y timing de servicio.' },
  { icon: FlaskConical, title: 'I+D y Desarrollo de Menu', desc: 'Fichas tecnicas de nuevos platos, pruebas de concepto, evaluacion sensorial, costes I+D, registro fotografico y evolucion de la carta.' },
  { icon: Users, title: 'Tareas por Brigada Creativa', desc: 'Checklists para: chef ejecutivo, sous-chef, jefe de partida, commis, chef pastelero creativo y stagiaire. Cada puesto sabe que hacer.' },
  { icon: CalendarDays, title: 'Semanales y Mensuales', desc: 'Deep clean de cocina, revision de maquinaria, inventario semanal (premium, fresco, seco), reunion creativa, actualizacion de carta.' },
  { icon: Wine, title: 'Sumiller y Maridajes', desc: 'Gestion de bodega, carta de vinos, maridajes por pase, servicio de sumilleria, catas para equipo, temperaturas de servicio.' },
  { icon: Sparkles, title: 'Chef\'s Table y Eventos', desc: 'Chef\'s table, cenas maridaje, showcookings, prensa y criticos, pop-ups y colaboraciones entre chefs.' },
  { icon: Camera, title: 'Fotografia y Storytelling', desc: 'Sesion de fotos de platos, contenido para RRSS, storytelling del menu, documentacion de procesos creativos.' },
  { icon: FileEdit, title: 'Plantilla Personalizable', desc: '3 plantillas en blanco (por partida, por turno y por perfil) para crear tus propias listas de tareas.' },
  { icon: Megaphone, title: 'BONUS: Briefing Diario de Servicio', desc: 'La reunion de 5 minutos antes de abrir: menu del dia, alergias confirmadas, VIPs, cambios de carta, timing de pases.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual de Eventos y Carta', desc: '15+ fechas clave: cambios estacionales de carta, eventos gastronomicos, guias, premios, temporadas de producto.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-emplatado.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-id.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-sumiller.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-chefstable.jpg',
  '/lovable-uploads/ai-gallery/tareas-restaurante-creativo-cocina.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Plantillas de Tareas Operativas
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla viene pre-rellenada con las tareas reales de un restaurante creativo o de autor. Solo ajusta, imprime y delega.
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
