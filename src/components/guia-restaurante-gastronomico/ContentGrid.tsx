import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Armchair, Wine, GlassWater,
  Users, UserCheck, UtensilsCrossed, Leaf, Star, Sun,
  Globe, Megaphone, Tablet, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: 'Qué es un Restaurante Gastronómico', desc: 'Definición, categorías (fine dining, casual fine, tasting menu) y diferencias con la restauración convencional.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado de la Alta Cocina en España 2026', desc: 'Datos del sector, ticket medio, tendencias de gasto y ciudades con mayor demanda gastronómica.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio', desc: 'Menú degustación, carta premium, omakase, chef's table. Pros, contras y márgenes de cada formato.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 500K-900K€, P&L mensual, food cost 25-28%, break-even y proyecciones a 3 años.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, registro sanitario, Hacienda, seguros, LOPD, normativa de terraza y alcohol.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC obligatorio, trazabilidad premium, alérgenos, control de temperaturas y auditorías.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas prime, metros mínimos para 65 plazas, accesibilidad, aparcamiento y entorno competitivo.' },
  { icon: Layout, num: '08', title: 'Diseño de Cocina Profesional', desc: 'Flujo de trabajo fine dining: recepción, mise en place, partidas, pase y emplatado de precisión.' },
  { icon: Wrench, num: '09', title: 'Equipamiento de Cocina', desc: 'Lista completa con costes: hornos Rational, Thermomix, abatidores, Pacojet, Roner, plancha Josper.' },
  { icon: Armchair, num: '10', title: 'Diseño de Sala para 65 Plazas', desc: 'Distribución, iluminación, acústica, mobiliario premium, interiorismo y experiencia del comensal.' },
  { icon: GlassWater, num: '11', title: 'Vajilla, Cristalería y Cubertería Premium', desc: 'Selección de marcas (Riedel, Zwiesel, RAK), inversión por cubierto y reposición anual.' },
  { icon: Wine, num: '12', title: 'Bodega y Servicio de Vinos', desc: 'Diseño de carta de vinos, maridajes, almacenamiento, sommelier y márgenes por copa/botella.' },
  { icon: Users, num: '13', title: 'Brigada de Cocina (12-17 personas)', desc: 'Organigrama, perfiles, salarios España 2026, turnos, formación continua y retención de talento.' },
  { icon: UserCheck, num: '14', title: 'Equipo de Sala (9-12 personas)', desc: 'Maître, sumiller, jefes de rango, runners. Salarios, formación en protocolo y gestión de turnos.' },
  { icon: UtensilsCrossed, num: '15', title: 'Menú Engineering para Fine Dining', desc: 'Diseño de carta, food cost por plato, matrix Stars/Plowhorses/Puzzles/Dogs y pricing psicológico.' },
  { icon: Leaf, num: '16', title: 'Proveedores Km0 y Producto de Temporada', desc: 'Red de proveedores locales, lonjas, huertos propios, temporalidad y trazabilidad del producto.' },
  { icon: Star, num: '17', title: 'Cómo Aspirar a Estrella Michelin', desc: 'Criterios de evaluación, qué buscan los inspectores, timeline realista y casos de éxito en España.' },
  { icon: Sun, num: '18', title: 'Cómo Aspirar a Sol Repsol', desc: 'Diferencias con Michelin, proceso de evaluación, requisitos y estrategia de posicionamiento.' },
  { icon: Globe, num: '19', title: "The World's 50 Best", desc: 'Cómo funciona el ranking, votantes, categorías y qué hacer para entrar en el radar internacional.' },
  { icon: Megaphone, num: '20', title: 'Marketing, PR y Lanzamiento', desc: 'Estrategia pre-apertura, prensa gastronómica, influencers food, redes sociales y evento inaugural.' },
  { icon: Tablet, num: '21', title: 'Tecnología para Fine Dining', desc: 'TPV, reservas (TheFork, Resy), CRM de comensales, gestión de alérgenos y digitalización discreta.' },
  { icon: Sparkles, num: '22', title: 'Tendencias 2025-2026', desc: 'Sostenibilidad, fermentación, cocina vegetal, experiencias inmersivas, IA aplicada y nuevos formatos.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-gastro-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-gastro-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-gastro-sala.jpg',
  '/lovable-uploads/ai-gallery/guia-gastro-plato.jpg',
  '/lovable-uploads/ai-gallery/guia-gastro-bodega.jpg',
  '/lovable-uploads/ai-gallery/guia-gastro-equipo.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">22</span> Capítulos + 10 Plantillas + 8 Checklists + 2 Documentos
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Todo lo que necesitas saber para montar tu restaurante gastronómico en España, escrito por un profesional con 29 años en alta hostelería.
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
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {chapters.map(({ icon: Icon, num, title, desc }, i) => (
            <FadeIn key={title} delay={i * 40}>
              <div className="group bg-white/5 border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/50 transition-all duration-300 h-full">
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-[#FFD700] text-xs font-bold opacity-50">{num}</span>
                  <Icon className="w-6 h-6 text-[#FFD700]" />
                </div>
                <h3 className="text-white font-semibold text-sm mb-1.5">{title}</h3>
                <p className="text-gray-400 text-xs leading-relaxed">{desc}</p>
              </div>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
