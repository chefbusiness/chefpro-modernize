import {
  Sunrise, ConciergeBell, ClipboardList, UtensilsCrossed,
  PartyPopper, Megaphone, Calendar, Bed, Building2, Waves,
  Sun, Wrench, BarChart3, Sparkles, Users,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: Sunrise, title: 'Buffet Desayuno', desc: 'Apertura y cierre del buffet: cocina, montaje, reposición, show cooking, mermas. ~40 tareas.' },
  { icon: UtensilsCrossed, title: 'Buffet Almuerzo / Cena', desc: 'Montaje de estaciones, show cooking, reposición, temperaturas APPCC. Diferencias almuerzo vs. cena.' },
  { icon: ClipboardList, title: 'Restaurante À la Carte', desc: 'Apertura: reservas, montaje, briefing. Cierre: caja, reposición, feedback. 2 checklists.' },
  { icon: ConciergeBell, title: 'Outlets: Pool · Lobby · Snack', desc: 'Pool bar, lobby bar/lounge y snack bar/grab & go. Cada outlet con su checklist específico.' },
  { icon: ConciergeBell, title: 'Room Service + Minibar', desc: 'Room service completo (pedido→entrega→recogida) + minibar (reposición, PMS, caducidades).' },
  { icon: PartyPopper, title: 'Banquetes y Eventos', desc: 'Bodas, convenciones, galas. BEO, montaje sala, audiovisuales, timing pases, desmontaje.' },
  { icon: Building2, title: 'Recepción — 3 Turnos', desc: 'Mañana, tarde, noche/auditoría nocturna + protocolo check-in/check-out paso a paso. 4 checklists.' },
  { icon: Users, title: 'Guest Services', desc: 'Conserjería (transfers, excursiones) + Guest Experience (VIPs, reviews, CRM, fidelización).' },
  { icon: Bed, title: 'Housekeeping', desc: 'Checkout, estancia, turndown, deep cleaning semanal y control de lencería. 5 checklists.' },
  { icon: Building2, title: 'Áreas Públicas', desc: 'Lobby, pasillos y ascensores, baños públicos, parking. 4 checklists de limpieza y control.' },
  { icon: Waves, title: 'Piscina', desc: 'Apertura/cierre diario, mantenimiento semanal (filtros, químicos) y servicio de toallas.' },
  { icon: Sun, title: 'Terraza', desc: 'Montaje de temporada + servicio diario: mobiliario, parasoles, limpieza, carta.' },
  { icon: Wrench, title: 'Mantenimiento', desc: 'Ronda diaria, semanal, mensual + HVAC, fontanería y electricidad. 6 checklists técnicos.' },
  { icon: BarChart3, title: 'Administración', desc: 'Revenue management, reservas, contabilidad cierre día, RRHH operativo. 4 checklists.' },
  { icon: Sparkles, title: 'Spa / Wellness', desc: 'Apertura/cierre, cabinas entre tratamientos, vestuarios. 4 checklists.' },
  { icon: Megaphone, title: 'BONUS: Briefing Diario F&B', desc: 'Plantilla de reunión diaria: ocupación, VIPs, menú del día, equipo, incidencias.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: '20 fechas clave para F&B hotelero: temporadas, festividades, congresos.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-hotel-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-hotel-buffet.jpg',
  '/lovable-uploads/ai-gallery/tareas-hotel-roomservice.jpg',
  '/lovable-uploads/ai-gallery/tareas-hotel-cocina.jpg',
  '/lovable-uploads/ai-gallery/tareas-hotel-banquete.jpg',
  '/lovable-uploads/ai-gallery/tareas-hotel-equipo.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">46</span> Checklists en <span className="text-[#FFD700]">15</span> Plantillas — 11 Departamentos
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla viene pre-rellenada con las tareas reales de un hotel profesional. Solo ajusta, imprime y delega.
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
