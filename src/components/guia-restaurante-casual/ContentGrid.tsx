import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Armchair, GlassWater,
  Users, UserCheck, UtensilsCrossed, Utensils, Truck,
  Sun, Megaphone, Tablet, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: 'Qué es un Restaurante Casual', desc: 'Definición, diferencias con fast casual y fine dining. Ticket medio 18-35€, ambiente y público objetivo.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado del Casual Dining en España 2026', desc: 'Datos del sector: 12.400M EUR, crecimiento +8% anual, ciudades con mayor demanda y tendencias.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio Casual', desc: 'Barrio premium, gastrobar, temático (brunch, bowls) y casual + delivery híbrido. Pros y contras.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 150K-350K€, food cost 28-32%, EBITDA 12-18%, break-even mes 8-14.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, registro sanitario, Hacienda, seguros, LOPD, terraza y alcohol.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC obligatorio, trazabilidad, alérgenos, control de temperaturas.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales, metros para 80 plazas, salida de humos, terraza y accesibilidad.' },
  { icon: Layout, num: '08', title: 'Diseño de Cocina Profesional', desc: 'Flujo lineal: recepción → preparación → cocción → emplatado → pase. 40-55 m².' },
  { icon: Wrench, num: '09', title: 'Equipamiento de Cocina', desc: 'Lista completa con costes: horno mixto, plancha, freidora, cámaras, tren de lavado. 30-60K€.' },
  { icon: Armchair, num: '10', title: 'Diseño de Sala para 80 Plazas', desc: 'Distribución mesas, iluminación regulable, acústica, interiorismo y terraza.' },
  { icon: GlassWater, num: '11', title: 'Mobiliario, Vajilla y Menaje', desc: 'Selección inteligente: porcelana reforzada, cristalería resistente, sin manteles. 3-6K€.' },
  { icon: GlassWater, num: '12', title: 'Carta de Bebidas y Coctelería', desc: 'Vinos, cervezas craft, cócteles signature, happy hour. Margen 65-80%.' },
  { icon: Users, num: '13', title: 'Brigada de Cocina (6-10 personas)', desc: 'Organigrama compacto, salarios España 2026, turnos y polivalencia.' },
  { icon: UserCheck, num: '14', title: 'Equipo de Sala (6-8 personas)', desc: 'Encargado, camareros, runner, barra. Servicio eficiente y upselling natural.' },
  { icon: UtensilsCrossed, num: '15', title: 'Menú Engineering y Carta', desc: 'Estructura 18-26 platos, matrix Stars/Plowhorses/Puzzles/Dogs y rotación de carta.' },
  { icon: Utensils, num: '16', title: 'Menú del Día y Ofertas', desc: 'Estructura, pricing 12-16€, food cost 30-35%, brunch, happy hour y noches temáticas.' },
  { icon: Truck, num: '17', title: 'Delivery y Take Away', desc: 'Plataformas vs delivery propio, packaging eco, menú delivery optimizado, zona de packaging.' },
  { icon: Sun, num: '18', title: 'Terraza: Licencias y Rentabilidad', desc: 'Licencia municipal, mobiliario, 20-40% facturación extra en temporada.' },
  { icon: Megaphone, num: '19', title: 'Marketing Digital y Redes Sociales', desc: 'Google My Business, Instagram, TikTok, TheFork, delivery, presupuesto 500-1.500€/mes.' },
  { icon: Tablet, num: '20', title: 'Tecnología para Casual Dining', desc: 'TPV, reservas, integrador delivery, contabilidad, RRHH, carta digital, WiFi.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-casual-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-casual-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-casual-sala.jpg',
  '/lovable-uploads/ai-gallery/guia-casual-plato.jpg',
  '/lovable-uploads/ai-gallery/guia-casual-terraza.jpg',
  '/lovable-uploads/ai-gallery/guia-casual-equipo.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">20</span> Capítulos + 8 Plantillas + 6 Checklists + 2 Documentos
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Todo lo que necesitas saber para montar tu restaurante casual en España, escrito por un profesional con 29 años en hostelería.
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
