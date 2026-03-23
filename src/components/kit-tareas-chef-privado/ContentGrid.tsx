import {
  UserCheck, ShoppingCart, Briefcase, ShieldCheck, UtensilsCrossed,
  Heart, FileSpreadsheet, Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: UserCheck, title: 'Ficha de Cliente', desc: 'Datos completos, alergias (14 alérgenos UE), intolerancias, preferencias culinarias, dieta, equipamiento de la cocina del cliente. Una ficha por cliente.' },
  { icon: ShoppingCart, title: 'Menú y Compras', desc: 'Planificación de menú por servicio, lista de compras con cantidades, control de coste por comensal y margen bruto del servicio.' },
  { icon: Briefcase, title: 'Equipo y Transporte', desc: 'Checklist de cuchillos, sartenes, transporte frío, mini-despensa portátil, textiles y verificación del vehículo. Nada se queda en casa.' },
  { icon: ShieldCheck, title: 'APPCC Móvil', desc: 'Control de temperaturas, gestión de alérgenos, higiene en cocina ajena, trazabilidad, etiquetado de meal prep. Cumplimiento legal.' },
  { icon: UtensilsCrossed, title: 'Servicio Completo', desc: 'Pre-servicio (montaje, mise en place), durante (timing por pases, emplatado) y post-servicio (limpieza total, recogida de equipo).' },
  { icon: Heart, title: 'Seguimiento y Fidelización', desc: 'Post-servicio 24h, solicitud de reseñas, historial de servicios por cliente, fechas especiales, programa de recurrencia.' },
  { icon: FileSpreadsheet, title: 'Administración', desc: 'Facturación por servicio, control de gastos, obligaciones fiscales del autónomo (303, 130, 390), seguros y carnets.' },
  { icon: Megaphone, title: 'BONUS: Briefing Pre-Servicio', desc: 'Hoja de ruta para cada servicio: cliente, alergias, menú, equipo, verificación final. Tu checklist de vuelo antes de despegar.' },
  { icon: Calendar, title: 'BONUS: Calendario de Demanda', desc: '12 meses con picos de demanda, tipos de servicio estacionales y estrategia de marketing por temporada.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-chef-privado-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-servicio.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-transporte.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-emplatado.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-cliente.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-cocina.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">9</span> Plantillas de Gestión Profesional
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla viene pre-rellenada con las tareas reales de un chef privado profesional. Solo ajusta, imprime y organiza tu negocio.
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
