import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Armchair, GlassWater,
  Users, UserCheck, UtensilsCrossed, Utensils, Truck,
  Flame, Megaphone, Tablet, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: 'Qué es un Restaurante Peruano', desc: 'Cevichería, criollo, Nikkei, Chifa, Novoandino. El fenómeno de la cocina peruana en el mundo y en España.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado de la Cocina Peruana en España 2026', desc: 'Crecimiento +40% en 5 años, ciudades con mayor demanda, perfil del cliente y competencia actual.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio', desc: 'Cevichería pura, restaurante criollo, Nikkei fusion, pollería, chifa, casual peruano y dark kitchen.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 130K-300K€, food cost 28-32%, márgenes pisco sour 78%, break-even mes 8-14.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales en España', desc: 'Licencias, importación de productos peruanos (ají, pisco), registro sanitario, terraza.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC y Seguridad Alimentaria', desc: 'APPCC para ceviche (pescado crudo), cadena de frío, alérgenos, trazabilidad de importados.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales, metros para 80 plazas, barra de ceviche abierta, barra de piscos.' },
  { icon: Layout, num: '08', title: 'Diseño de Cocina Peruana', desc: 'Estación de ceviche, wok para chifa/Nikkei, parrilla para anticuchos, zona de salsas (ají amarillo, rocoto).' },
  { icon: Wrench, num: '09', title: 'Equipamiento Específico', desc: 'Mesa refrigerada ceviche, wok industrial, parrilla anticuchos, vitrina de piscos. Costes detallados.' },
  { icon: Armchair, num: '10', title: 'Diseño de Sala: Ambiente Peruano', desc: 'Interiorismo moderno con toques peruanos: textiles andinos, cerámica, madera, colores tierra, barra abierta.' },
  { icon: GlassWater, num: '11', title: 'Vajilla y Presentación', desc: 'Platos de piedra para ceviche, cuencos de cerámica, vasos de pisco, presentación tipo Lima gourmet.' },
  { icon: GlassWater, num: '12', title: 'Barra de Piscos y Coctelería', desc: 'Pisco sour, chilcano, capitán, maracuyá sour. 20-30 referencias de pisco, márgenes 75-80%.' },
  { icon: Users, num: '13', title: 'Brigada de Cocina (6-10 personas)', desc: 'Cevichero, wokero, parrillero, cocineros. Salarios España 2026, formación en cocina peruana.' },
  { icon: UserCheck, num: '14', title: 'Equipo de Sala (6-8 personas)', desc: 'Servicio con conocimiento de pisco, maridaje, storytelling de platos peruanos, upselling.' },
  { icon: UtensilsCrossed, num: '15', title: 'La Carta: Menú Engineering Peruano', desc: 'Ceviches, tiraditos, causas, lomo saltado, ají de gallina, anticuchos. Matrix de rentabilidad.' },
  { icon: Flame, num: '16', title: 'Proveedores: Productos Peruanos en España', desc: 'Importadores de ají amarillo, rocoto, maíz morado, pisco, chicha morada. Proveedores nacionales.' },
  { icon: Utensils, num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos: ceviche clásico, lomo saltado, causa limeña, ají de gallina, anticuchos.' },
  { icon: Truck, num: '18', title: 'Delivery y Take Away Peruano', desc: 'Ceviches no viajan bien, pero causas, lomos, arroces sí. Menú delivery específico, packaging.' },
  { icon: Megaphone, num: '19', title: 'Marketing y Posicionamiento', desc: 'Instagram, TikTok, Fiestas Patrias (28 julio), eventos Nikkei, influencers food, Google My Business.' },
  { icon: Tablet, num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas, delivery, contabilidad, turnos, carta digital con fotos de platos peruanos.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-peruano-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-peruano-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-peruano-sala.jpg',
  '/lovable-uploads/ai-gallery/guia-peruano-plato.jpg',
  '/lovable-uploads/ai-gallery/guia-peruano-barra.jpg',
  '/lovable-uploads/ai-gallery/guia-peruano-equipo.jpg',
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
              Todo lo que necesitas saber para montar tu restaurante peruano en España, escrito por un profesional con 29 años en hostelería.
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
