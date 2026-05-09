import {
  FileSpreadsheet, Coins, TrendingUp, BarChart3,
  Users, ShieldCheck, Globe, FileText, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años, inversión inicial, punto de equilibrio, escenarios, personal e instrucciones. Todas las celdas editables con fórmulas.' },
  { icon: Coins, title: 'Inversión Inicial Detallada', desc: 'Local, cocina, sala, marketing, legal y fondo de maniobra desglosados (~133K EUR de referencia para bar-restaurante medio en España).' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: 'Cuántos cubiertos al día necesitas para cubrir costes fijos, margen de contribución e interpretación de resultados con sensibilidad a ticket medio.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes ocupaciones y ticket medio para presentar a banco o inversores.' },
  { icon: Users, title: 'Cuadro de Personal y Costes', desc: 'Salarios brutos por puesto, Seguridad Social al 33,4 %, 14 pagas y coste real por jefe de cocina, jefe de sala, cocineros, camareros y ayudantes.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, licencias hostelería, obra y acondicionamiento, RRHH, marketing pre-apertura y primeros 90 días de operación.' },
  { icon: Globe, title: 'Análisis de Mercado España 2026', desc: '81K+ restaurantes activos, ticket medio por comunidad, inversión media por tipo de local y tasa de cierre en los 3 primeros años.' },
  { icon: FileText, title: 'Instrucciones y Ratios de Referencia', desc: 'Food cost 28-32 %, personal inferior a 35 %, alquiler inferior a 10 % y datos sectoriales para comparar con tu proyecto y detectar desviaciones.' },
  { icon: Banknote, title: 'Plan de Financiación', desc: 'Opciones reales: ICO, ENISA, préstamo bancario, inversores privados, business angels y subvenciones autonómicas con orden recomendado de gestión.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-bar-restaurante-interior.jpg',
  '/lovable-uploads/ai-gallery/plan-bar-restaurante-cocina.jpg',
  '/lovable-uploads/ai-gallery/plan-bar-restaurante-plato.jpg',
  '/lovable-uploads/ai-gallery/plan-bar-restaurante-barra.jpg',
  '/lovable-uploads/ai-gallery/plan-bar-restaurante-equipo.jpg',
  '/lovable-uploads/ai-gallery/plan-bar-restaurante-terraza.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              Qué Incluye el <span className="text-[#FFD700]">Plan de Negocio</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              9 secciones profesionales con datos reales del mercado español para construir la viabilidad financiera de tu bar-restaurante y presentarla a banco o inversores.
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
          {categories.map(({ icon: Icon, title, desc }, i) => (
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
