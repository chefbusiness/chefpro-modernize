import {
  FileSpreadsheet, Coins, TrendingUp, BarChart3,
  Users, ShieldCheck, Wrench, ListChecks, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años con estacionalidad navideña, inversión inicial, punto de equilibrio, escenarios, cuadro de personal panadero e instrucciones. Todas las celdas editables.' },
  { icon: Coins, title: 'Inversión Inicial Detallada', desc: 'Local, horno profesional de pisos, amasadora 40-80 kg, cámara de fermentación controlada, expositor refrigerado, mobiliario y fondo de maniobra (~88K EUR de referencia).' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: 'Cálculo por kilos de pan diarios y unidades de bollería con ticket medio €4,50, margen de seguridad e interpretación de resultados con sensibilidad al mix de producción.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes de producción y mix barra/bollería/cafetería para presentar a banco e inversores.' },
  { icon: Users, title: 'Cuadro de Personal Panadero', desc: 'Maestro panadero, oficial, ayudante de obrador y dependiente con salarios brutos, Seguridad Social al 33,4 %, 14 pagas, turno madrugada y plus de nocturnidad.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, RGSEAA obrador (Registro General Sanitario), licencias municipales, equipamiento (proyecto técnico, salida de humos), RRHH y primeros 90 días.' },
  { icon: Wrench, title: 'Equipamiento Específico Panadería', desc: 'Horno de pisos rotativo (Salva, Eurofours), amasadora 40-80 kg, cámara de fermentación controlada y expositor refrigerado, con marcas de referencia y precios.' },
  { icon: ListChecks, title: 'Ratios de Referencia Panadería', desc: 'Coste materia prima 22-28 %, personal <38 %, merma 3-5 %, margen bruto pan >70 % y bollería >75 %. Datos del sector panadero español 2026.' },
  { icon: Banknote, title: 'Plan de Financiación', desc: 'Opciones reales: ICO, ENISA, préstamo bancario, leasing de equipamiento (horno, amasadora), inversores privados y subvenciones autonómicas para obrador.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-panaderia-horno.jpg',
  '/lovable-uploads/ai-gallery/plan-panaderia-obrador.jpg',
  '/lovable-uploads/ai-gallery/plan-panaderia-pan.jpg',
  '/lovable-uploads/ai-gallery/plan-panaderia-bolleria.jpg',
  '/lovable-uploads/ai-gallery/plan-panaderia-masa.jpg',
  '/lovable-uploads/ai-gallery/plan-panaderia-tienda.jpg',
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
              9 secciones profesionales con datos reales del mercado panadero español para construir la viabilidad financiera de tu panadería u obrador y presentarla a banco o inversores.
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
