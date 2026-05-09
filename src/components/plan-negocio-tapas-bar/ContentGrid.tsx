import {
  FileText, FileSpreadsheet, TrendingUp, BarChart3,
  Users, ShieldCheck, Wrench, ListChecks, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Resumen ejecutivo, concepto, análisis de mercado, DAFO, marketing, operaciones, RRHH, financiero, legal y conclusiones. Listo para banco o inversores.' },
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (6 hojas)', desc: 'P&L previsional a 3 años, inversión inicial, punto de equilibrio, escenarios, cuadro de personal e instrucciones. Todas las celdas editables.' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: 'Modelo realista: 34 clientes al día con ticket medio €18, margen de seguridad 25 % y sensibilidad a horas pico de barra y comedor.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes y ticket medio. Útil para presentar a banco e inversores.' },
  { icon: Users, title: 'Cuadro de Personal y Costes', desc: 'Salarios brutos por puesto: jefe de cocina, cocineros, camareros de barra y de sala, con Seguridad Social al 33,4 % y 14 pagas.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución SL, licencia clasificada (no inocua, por potencia de cocina), salida de humos, equipamiento, RRHH, marketing pre-apertura y primeros 90 días.' },
  { icon: Wrench, title: 'Equipamiento Específico Tapas Bar', desc: 'Plancha, freidora, grifos de cerveza, vitrina de tapas, salamandra, expositor de raciones y vinoteca, con marcas de referencia y precios orientativos.' },
  { icon: ListChecks, title: 'Ratios de Referencia Tapas Bar', desc: 'Food cost tapas 28-32 %, márgenes bebidas 22-28 %, margen bruto >68 %, ticket medio 15-22 EUR y rotación por turno.' },
  { icon: Banknote, title: 'Plan de Financiación', desc: 'ICO, ENISA, préstamo bancario, inversores privados, business angels y subvenciones autonómicas con orden recomendado de gestión.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-tapas-bar-barra.jpg',
  '/lovable-uploads/ai-gallery/plan-tapas-bar-raciones.jpg',
  '/lovable-uploads/ai-gallery/plan-tapas-bar-terraza.jpg',
  '/lovable-uploads/ai-gallery/plan-tapas-bar-cerveza.jpg',
  '/lovable-uploads/ai-gallery/plan-tapas-bar-cocina.jpg',
  '/lovable-uploads/ai-gallery/plan-tapas-bar-vermut.jpg',
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
              9 secciones profesionales con datos reales del mercado español para construir la viabilidad financiera de tu tapas bar y presentarla a banco o inversores.
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
