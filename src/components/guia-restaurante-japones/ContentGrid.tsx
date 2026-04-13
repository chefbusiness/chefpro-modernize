import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Armchair, GlassWater,
  Users, UserCheck, UtensilsCrossed, Utensils, Truck,
  Flame, Megaphone, Tablet, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: 'Qué es un Restaurante Japonés', desc: 'Sushi-ya, ramen-ya, izakaya, omakase, robatayaki. El universo de la cocina japonesa premium en España.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado Japonés en España 2026', desc: 'Crecimiento +35% en 5 años, ciudades con mayor demanda, omakase con listas de espera, público foodie.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio', desc: 'Sushi-ya, ramen-ya, izakaya, omakase premium, robatayaki, mixto y dark kitchen japonesa.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 250K-500K€, food cost 30-35%, márgenes sake/whisky 75-85%, break-even mes 10-16.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales + Normativa Anisakis', desc: 'Licencias, RD 1420/2006 congelación preventiva -20°C/24h, importación, registro sanitario.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC para Pescado Crudo y Shari', desc: 'APPCC con PCC específicos: anisakis, temperatura arroz sushi, caldos ramen, alérgenos.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas ideales, metros para 60 plazas, barra sushi, proximidad a mercados de pescado fresco.' },
  { icon: Layout, num: '08', title: 'Diseño de Cocina Japonesa', desc: 'Barra de sushi, estación shari, ramen station, robata binchotan, teppanyaki, zona tempura.' },
  { icon: Wrench, num: '09', title: 'Equipamiento Específico Japonés', desc: 'Suihanki, vitrina sashimi, ramen cooker, robata, teppanyaki, cuchillos yanagiba/deba/usuba. Costes.' },
  { icon: Armchair, num: '10', title: 'Diseño de Sala: Estética Japonesa', desc: 'Wabi-sabi, ma, shibui. Madera natural, lámparas washi, jardín zen, bambú, minimalismo.' },
  { icon: GlassWater, num: '11', title: 'Vajilla y Presentación', desc: 'Cerámica japonesa artesanal, asimetría wabi-sabi, platos de pizarra, presentación tipo kaiseki.' },
  { icon: GlassWater, num: '12', title: 'Barra de Sake y Whisky Japonés', desc: 'Junmai, Ginjo, Daiginjo, Nigori + whisky Yamazaki/Hibiki. 30-50 refs, márgenes 75-85%.' },
  { icon: Users, num: '13', title: 'Brigada de Cocina (8-12 personas)', desc: 'Itamae, sushi chef, ramen cook, robata cook, tempura cook. Salarios España 2026.' },
  { icon: UserCheck, num: '14', title: 'Equipo de Sala (5-8 personas)', desc: 'Servicio con protocolo japonés, sommelier de sake, storytelling, upselling de whisky japonés.' },
  { icon: UtensilsCrossed, num: '15', title: 'La Carta: Menú Engineering Japonés', desc: 'Sashimi, nigiri, maki, ramen, yakitori, tempura, katsu. Matrix de rentabilidad.' },
  { icon: Flame, num: '16', title: 'Proveedores: Productos Japoneses en España', desc: 'Distribuidores de pescado sashimi-grade, arroz Koshihikari, algas nori, sake, whisky japonés.' },
  { icon: Utensils, num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos: sashimi moriawase, ramen tonkotsu, tempura, yakitori, katsu.' },
  { icon: Truck, num: '18', title: 'Delivery y Take Away Japonés', desc: 'Sushi boxes, bowls, katsudon, gyoza. Ramen especial. Packaging premium japonés.' },
  { icon: Megaphone, num: '19', title: 'Marketing y Calendario Cultural', desc: 'Instagram, TikTok, Hanami (marzo), Día del Sushi (18 junio), eventos de cata de sake.' },
  { icon: Tablet, num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas con depósito para omakase, delivery, contabilidad, turnos, carta de sakes.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-restaurante-japones-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-japones-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-japones-sala.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-japones-plato.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-japones-barra.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-japones-equipo.jpg',
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
              Todo lo que necesitas saber para montar tu restaurante japonés en España, escrito por un profesional con 29 años en hostelería.
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
