import {
  FileText, FileSpreadsheet, TrendingUp, BarChart3,
  Users, ShieldCheck, Wrench, ListChecks, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileText, title: 'Plan de Negocio DOCX (10 secciones)', desc: 'Documento profesional completo con análisis de mercado, modelo de negocio, plan operativo de food truck, marketing y proyecciones financieras a 3 años.' },
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (9 hojas)', desc: 'Supuestos, inversión inicial, P&L previsional a 3 años, punto de equilibrio, escenarios, cuadro de personal, tesorería mes a mes, plan de financiación e instrucciones. Las celdas verdes son las que se teclean; el resto se recalcula solo y va protegido, sin contraseña, para que no se rompa una fórmula sin querer.' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: '41 clientes al día con ticket medio de 12 € sin IVA para cubrir todos los costes, y 38 para cubrir además la cuota del préstamo. Margen de contribución, días de operación y una tabla de sensibilidad de 20 combinaciones de ticket y coste variable.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes ubicaciones, días de operación y ticket medio para presentar a banco e inversores.' },
  { icon: Users, title: 'Cuadro Personal (4 puestos, 1,6 jornadas)', desc: 'Equipo reducido de food truck con salarios brutos, Seguridad Social al 33 %, 14 pagas y coste real por puesto: propietario/a a jornada completa, ayudante de cocina y servicio al 45 %, refuerzo de festivales al 10 % y suplencias de vacaciones al 6 %. El libro avisa en rojo si un sueldo baja del SMI en proporción a su jornada.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Alta autónomo o SL, licencias municipales de venta ambulante, registro sanitario de tu comunidad autónoma y autorización sanitaria del vehículo, ITV si lo modificas, seguros y primeros 90 días.' },
  { icon: Wrench, title: 'Equipamiento Cocina Móvil', desc: 'Plancha, freidora, generador eléctrico, depósitos de agua limpia y residual, extracción de humos con filtros y normativa técnica del vehículo adaptado.' },
  { icon: ListChecks, title: 'Ratios de Referencia Food Truck', desc: 'Los rangos del sector (food cost de comida 28-33 %, de bebida 22-28 %, packaging 3-5 %, personal 25-32 %, margen bruto > 62 %) al lado de lo que sale en TU plan: 27,1 % de coste de mercancía, 64,1 % de margen bruto y 31,2 % de personal. El retorno de la inversión no se promete: lo calcula la hoja de tesorería con tu propio flujo de caja.' },
  { icon: Banknote, title: 'Plan de Financiación', desc: 'Hoja propia: recursos propios, préstamo bancario, línea ICO, préstamo participativo ENISA, business angels y subvenciones autonómicas o locales, con el cuadro de amortización del préstamo año a año, la cobertura del servicio de la deuda (DSCR) y el aviso de si el dinero que aportas no llega a lo que hace falta.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/plan-food-truck-exterior.jpg',
  '/lovable-uploads/ai-gallery/plan-food-truck-cocinando.jpg',
  '/lovable-uploads/ai-gallery/plan-food-truck-plato.jpg',
  '/lovable-uploads/ai-gallery/plan-food-truck-mercado.jpg',
  '/lovable-uploads/ai-gallery/plan-food-truck-cola.jpg',
  '/lovable-uploads/ai-gallery/plan-food-truck-setup.jpg',
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
              9 secciones profesionales con datos reales del sector street food en España para montar tu food truck con cabeza y bajo riesgo.
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
