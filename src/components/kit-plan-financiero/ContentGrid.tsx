import {
  TrendingUp, Target, Wallet, Building2, BarChart3,
  PieChart, FileText, Shuffle, ClipboardList,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: TrendingUp, title: 'Plan Financiero Previsional (3 Años)', desc: 'Proyección de ingresos y gastos a 3 años con desglose mensual. Líneas de ingreso (comedor, barra, delivery, eventos), costes variables/fijos, EBITDA y gráficos automáticos.' },
  { icon: TrendingUp, title: 'Plan Financiero Previsional (5 Años)', desc: 'Misma estructura que el plan a 3 años pero con proyección a 5 años. Ideal para presentaciones a bancos, inversores o franquicias que requieren horizontes más largos.' },
  { icon: Target, title: 'Calculadora Punto de Equilibrio', desc: 'Calcula comensales/día mínimos, umbral de facturación y el ticket medio necesario para los cubiertos que preveas, con gráfico de ingresos vs costes. Break-even operativo y de caja, y 3 escenarios: pesimista, realista y optimista.' },
  { icon: Wallet, title: 'Cash Flow Forecast (12 Meses)', desc: 'Flujo de caja mensual con desfase cobros/pagos, IVA trimestral y estacionalidad. Alerta automática en rojo cuando el saldo cae por debajo del umbral de seguridad.' },
  { icon: Building2, title: 'Presupuesto de Inversión / CAPEX', desc: 'Desglose por partida: obra, equipamiento cocina, mobiliario sala, tecnología, licencias. Presupuesto vs real con % desviación. Totales con y sin IVA.' },
  { icon: BarChart3, title: 'P&L Mensual Real vs Presupuesto', desc: 'Cada mes compara real vs presupuesto con desviación % y semáforo (verde <5%, amarillo 5-10%, rojo >10%). Food cost, labor cost y prime cost automáticos.' },
  { icon: PieChart, title: 'Dashboard de Ratios Financieros', desc: 'Calcula food cost %, labor cost %, prime cost %, GOP, RevPASH, coste por cubierto. Compara contra benchmarks del sector hostelero español.' },
  { icon: FileText, title: 'Informe de Viabilidad para Bancos', desc: 'Formato profesional listo para presentar: resumen ejecutivo, proyecciones, TIR, VAN, payback period. Diseñado para lo que los bancos realmente piden.' },
  { icon: Shuffle, title: 'BONUS: Simulador de Escenarios', desc: 'Modifica ticket medio, cubiertos/día, food cost y ve impacto instantáneo en rentabilidad. 3 escenarios con comparativa visual lado a lado.' },
  { icon: ClipboardList, title: 'BONUS: Checklist Pre-Apertura Financiero', desc: '54 ítems agrupados en 7 fases: constitución, financiación, licencias, proveedores, seguros, tesorería y obligaciones laborales. Con estado, responsable y fecha límite.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-financiero-hero.jpg',
  '/lovable-uploads/ai-gallery/plan-financiero-oficina.jpg',
  '/lovable-uploads/ai-gallery/plan-financiero-reunion.jpg',
  '/lovable-uploads/ai-gallery/plan-financiero-graficos.jpg',
  '/lovable-uploads/ai-gallery/plan-financiero-restaurante.jpg',
  '/lovable-uploads/ai-gallery/plan-financiero-analisis.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">10</span> Plantillas de Plan Financiero
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Las 10 plantillas son coherentes entre sí: mismas categorías de ingreso/gasto, mismos ratios y la misma base sin IVA (salvo la tesorería, que va con IVA porque es caja). Benchmarks reales del sector hostelero español.
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
          {templates.map(({ icon: Icon, title, desc }, i) => (
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
