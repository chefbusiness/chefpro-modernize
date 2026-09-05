import {
  FileText, FileSpreadsheet, TrendingUp, BarChart3,
  Users, ShieldCheck, Wrench, ListChecks, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Resumen ejecutivo, concepto, análisis de mercado, DAFO, marketing, operaciones, RRHH, financiero, legal y conclusiones. Listo para banco o inversores.' },
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (9 hojas)', desc: 'Supuestos, inversión inicial, P&L previsional a 3 años, punto de equilibrio, escenarios, cuadro de personal, tesorería mes a mes y plan de financiación, más instrucciones. 742 fórmulas: cambias una celda verde y el libro entero se recalcula.' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: 'Modelo realista: 50 clientes al día para cubrir costes —47 si sólo cuentas la caja y la cuota del préstamo— con ticket medio de 18 € sin IVA, un 19,6 % de holgura sobre los 56 previstos y tabla de sensibilidad por ticket medio y coste variable.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes y ticket medio. Útil para presentar a banco e inversores.' },
  { icon: Users, title: 'Cuadro de Personal y Costes', desc: 'Salarios brutos de los 7 puestos —propietario/encargado de sala, jefe de cocina, camarero de barra, camarero de sala y terraza, ayudante de cocina, extra de fin de semana y suplencias—, con Seguridad Social al 33 %, 14 pagas, semáforo que avisa si un sueldo baja del salario mínimo en proporción a su jornada y contador de horas contratadas frente a las necesarias.' },
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
