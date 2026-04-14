import {
  Building2, TrendingUp, Briefcase, Calculator, Scale,
  ShieldCheck, MapPin, Layout, Wrench, Armchair, GlassWater,
  Users, UserCheck, UtensilsCrossed, Utensils, Truck,
  Flame, Megaphone, Tablet, Sparkles,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const chapters = [
  { icon: Building2, num: '01', title: 'Qué es la Cocina Nikkei', desc: 'Fusión peruano-japonesa nacida en Perú (siglo XIX). Referentes: Nobu, Maido, Osaka, Pakta. Identidad y técnica.' },
  { icon: TrendingUp, num: '02', title: 'El Mercado Nikkei en España 2026', desc: 'Tendencia premium alcista, ciudades clave, omakase nikkei con lista de espera, público foodie 30-50.' },
  { icon: Briefcase, num: '03', title: 'Modelos de Negocio Nikkei', desc: 'Barra de tiraditos, cevichería nikkei, robata nikkei, omakase premium, casual premium, dark kitchen nikkei.' },
  { icon: Calculator, num: '04', title: 'Estudio de Viabilidad y Plan Financiero', desc: 'Inversión 280K-520K€, food cost 32-34%, márgenes pisco/sake 75-85%, break-even mes 10-16.' },
  { icon: Scale, num: '05', title: 'Requisitos Legales + Normativa Anisakis', desc: 'Licencias, RD 1420/2006 congelación preventiva -20°C/24h para tiraditos, importación peruana, registro sanitario.' },
  { icon: ShieldCheck, num: '06', title: 'APPCC Pescado Crudo + Leche de Tigre', desc: 'PCC específicos: anisakis tiraditos, cadena de frío leches de tigre, shari, alérgenos, ají.' },
  { icon: MapPin, num: '07', title: 'Ubicación y Local', desc: 'Zonas premium urbanas, metros para 60 plazas, barra tiraditos visible, proximidad mercados pescado.' },
  { icon: Layout, num: '08', title: 'Diseño de Cocina Nikkei', desc: 'Barra tiraditos, cold station leche de tigre, robata/josper, wok chaufa, hot kitchen anticuchos.' },
  { icon: Wrench, num: '09', title: 'Equipamiento Específico Nikkei', desc: 'Vitrina sashimi, robata/josper, wok station, licuadoras leches de tigre, yanagiba, molcajete, teppanyaki.' },
  { icon: Armchair, num: '10', title: 'Diseño de Sala: Estética Nikkei', desc: 'Fusión: madera japonesa minimalista + textiles peruanos, cerámica Chulucanas, iluminación cálida, barra tiraditos protagonista.' },
  { icon: GlassWater, num: '11', title: 'Vajilla y Presentación', desc: 'Cerámica japonesa artesanal + cerámica peruana Chulucanas. Asimetría, pizarras, presentación de autor.' },
  { icon: GlassWater, num: '12', title: 'Barra de Pisco, Sake y Coctelería Nikkei', desc: 'Pisco puro/acholado, sakes Junmai/Ginjo, 40 refs, pisco sours, chilcanos, maridaje tiraditos. Márgenes 75-85%.' },
  { icon: Users, num: '13', title: 'Brigada de Cocina (14-18 personas)', desc: 'Chef ejecutivo, itamae nikkei, parrillero robata, cold station leches de tigre, hot kitchen chaufa/anticuchos, pastelería.' },
  { icon: UserCheck, num: '14', title: 'Equipo de Sala (6-9 personas)', desc: 'Servicio cálido, sommelier pisco/sake, storytelling nikkei, upselling de maridajes.' },
  { icon: UtensilsCrossed, num: '15', title: 'La Carta: Menú Engineering Nikkei', desc: 'Tiraditos, ceviches nikkei, causas, makis acevichados, tatakis, anticuchos, chaufa, postres. Matrix de rentabilidad.' },
  { icon: Flame, num: '16', title: 'Proveedores: Productos Peruanos y Japoneses en España', desc: 'Inkawasi, Latin Products (ají amarillo/limo/rocoto), pescado sashimi-grade Mercamadrid, arroz Koshihikari, nori, pisco, sake.' },
  { icon: Utensils, num: '17', title: 'Recetas Base y Escandallos', desc: 'Fichas técnicas de 15 platos nikkei: tiradito clásico, ceviche nikkei, causa, maki acevichado, tataki atún, anticucho, chaufa mariscos.' },
  { icon: Truck, num: '18', title: 'Delivery y Take Away Nikkei', desc: 'Sushi/tiradito boxes, ceviche en frío, bowls, chaufa. Packaging premium que preserve temperatura y textura.' },
  { icon: Megaphone, num: '19', title: 'Marketing y Calendario Cultural', desc: 'Instagram, TikTok, Día del Pisco Sour, Fiestas Patrias Perú (28 julio), eventos cata pisco/sake, colaboraciones con chefs nikkei.' },
  { icon: Tablet, num: '20', title: 'Tecnología y Operaciones', desc: 'TPV, reservas con depósito para omakase, delivery, contabilidad, turnos, carta digital.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-hero.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-cocina.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-sala.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-plato.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-barra.jpg',
  '/lovable-uploads/ai-gallery/guia-restaurante-nikkei-equipo.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">20</span> Capítulos + 9 Plantillas + 6 Checklists + 2 Documentos
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Todo lo que necesitas saber para montar tu restaurante nikkei en España, escrito por un profesional con 29 años en hostelería.
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
