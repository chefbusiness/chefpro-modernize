import {
  FileSpreadsheet, Coins, TrendingUp, BarChart3,
  Users, ShieldCheck, Wrench, ListChecks, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años, inversión inicial, punto de equilibrio, escenarios, cuadro de personal e instrucciones. Todas las celdas editables con fórmulas.' },
  { icon: Coins, title: 'Inversión Inicial Detallada', desc: 'Local, máquina de café, horno, vitrina refrigerada, mobiliario, terraza y fondo de maniobra desglosados (~94K EUR de referencia).' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: '53 clientes al día con ticket medio €9,50. Cálculo de margen de seguridad e interpretación de resultados con sensibilidad a horas pico.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes de clientes y ticket medio. Útil para presentar a banco e inversores.' },
  { icon: Users, title: 'Cuadro de Personal y Costes', desc: 'Baristas, ayudante de cocina y camareros con salarios brutos, Seguridad Social al 33,4 %, 14 pagas y coste real por puesto.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, licencia de actividad inocua, RGSEAA, terraza, equipamiento, RRHH, marketing pre-apertura y primeros 90 días.' },
  { icon: Wrench, title: 'Equipamiento Específico Cafetería', desc: 'Máquina espresso 2 grupos, molinillo profesional, horno de convección, vitrina refrigerada para bollería y mobiliario, con marcas de referencia y precios.' },
  { icon: ListChecks, title: 'Ratios de Referencia Cafetería', desc: 'Food cost café 25-30 %, ticket medio €8-12, margen bruto >65 %, rotación por franja horaria (mañana / mediodía / tarde) y datos del sector.' },
  { icon: Banknote, title: 'Plan de Financiación', desc: 'Opciones reales: ICO, ENISA, préstamo bancario, inversores privados, business angels y subvenciones autonómicas con orden recomendado de gestión.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-cafeteria-interior.jpg',
  '/lovable-uploads/ai-gallery/plan-cafeteria-latte.jpg',
  '/lovable-uploads/ai-gallery/plan-cafeteria-brunch.jpg',
  '/lovable-uploads/ai-gallery/plan-cafeteria-barra.jpg',
  '/lovable-uploads/ai-gallery/plan-cafeteria-bolleria.jpg',
  '/lovable-uploads/ai-gallery/plan-cafeteria-terraza.jpg',
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
              9 secciones profesionales con datos reales del mercado español para construir la viabilidad financiera de tu cafetería o brunch y presentarla a banco o inversores.
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
