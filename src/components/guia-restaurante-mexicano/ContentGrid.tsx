import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Armchair, GlassWater,
  Users, UserCheck, UtensilsCrossed, Utensils, Truck,
  Flame, Megaphone, Tablet, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: 'Qué es un Restaurante Mexicano en España', desc: 'Diferencia entre mexicano auténtico, tex-mex y fusion. Posicionamiento, público objetivo y ticket medio 18-30€.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado de la Cocina Mexicana en España 2026', desc: 'Datos del sector, crecimiento de la demanda, ciudades con mayor oportunidad y competencia actual.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio', desc: 'Taquería gourmet, cantina mexicana, casual mexicano, cocina de autor mexicana y dark kitchen de tacos.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 120K-280K€, food cost 28-33%, márgenes en bebidas (tequila/mezcal 75-80%), break-even.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, registro sanitario, importación de productos mexicanos, licencia de alcohol, terraza.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'Plan APPCC adaptado: chiles secos, masa de maíz, importación, trazabilidad de productos mexicanos.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales en España, metros para 80 plazas, barra de tequilas, cocina abierta y terraza.' },
  { icon: Layout, num: '08', title: 'Diseño de Cocina Mexicana', desc: 'Plancha/comal, estación de tacos, zona de salsas, parrilla, freidora para totopos. Flujo específico.' },
  { icon: Wrench, num: '09', title: 'Equipamiento Específico', desc: 'Comal, tortillera, molcajete industrial, parrilla, ahumador, máquina de margaritas. Costes detallados.' },
  { icon: Armchair, num: '10', title: 'Diseño de Sala: Ambiente Mexicano', desc: 'Interiorismo auténtico: colores vivos, azulejos Talavera, plantas, luces de verbena, arte mexicano.' },
  { icon: GlassWater, num: '11', title: 'Vajilla, Menaje y Presentación', desc: 'Platos de barro, cazuelas, vasos de vidrio soplado, cestitas para totopos. Autenticidad en cada detalle.' },
  { icon: GlassWater, num: '12', title: 'Barra de Tequilas y Mezcales', desc: 'Selección de 30-50 referencias, coctelería mexicana (margarita, paloma, michelada), márgenes 75-80%.' },
  { icon: Users, num: '13', title: 'Brigada de Cocina (6-10 personas)', desc: 'Taquero, parrillero, salsero, cocineros polivalentes. Salarios España 2026 y formación en cocina mexicana.' },
  { icon: UserCheck, num: '14', title: 'Equipo de Sala (6-8 personas)', desc: 'Servicio cercano y festivo, conocimiento de tequilas/mezcales, upselling de margaritas y guacamole.' },
  { icon: UtensilsCrossed, num: '15', title: 'La Carta: Menú Engineering Mexicano', desc: 'Tacos, burritos, enchiladas, quesadillas, ceviches, guacamole. Matrix de rentabilidad por plato.' },
  { icon: Flame, num: '16', title: 'Proveedores: Productos Mexicanos en España', desc: 'Importadores de chiles, masa de maíz, tortillas, salsas, tequila, mezcal. Proveedores nacionales y directos.' },
  { icon: Utensils, num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos clave: tacos al pastor, carnitas, guacamole, mole, churros. Food cost real.' },
  { icon: Truck, num: '18', title: 'Delivery y Take Away Mexicano', desc: 'Tacos y burritos viajan bien. Packaging específico, menú delivery optimizado, plataformas vs propio.' },
  { icon: Megaphone, num: '19', title: 'Marketing y Posicionamiento', desc: 'Instagram, TikTok, influencers food, eventos temáticos (Día de Muertos, Cinco de Mayo), Google My Business.' },
  { icon: Tablet, num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas, delivery, contabilidad, turnos, carta digital con fotos de platos mexicanos.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-mexicano-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-mexicano-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-mexicano-sala.jpg',
  '/lovable-uploads/ai-gallery/guia-mexicano-plato.jpg',
  '/lovable-uploads/ai-gallery/guia-mexicano-barra.jpg',
  '/lovable-uploads/ai-gallery/guia-mexicano-equipo.jpg',
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
              Todo lo que necesitas saber para montar tu restaurante mexicano en España, escrito por un profesional con 29 años en hostelería.
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
