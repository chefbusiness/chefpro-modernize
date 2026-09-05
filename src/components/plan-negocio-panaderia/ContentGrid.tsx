import {
  FileSpreadsheet, Coins, TrendingUp, BarChart3,
  Users, ShieldCheck, Wrench, ListChecks, Banknote,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const categories = [
  { icon: FileSpreadsheet, title: 'Plan Financiero Excel (9 hojas)', desc: 'Supuestos, inversión inicial, P&L previsional a 3 años con estacionalidad navideña, punto de equilibrio, escenarios, personal con cobertura de horas, tesorería 12 meses con liquidación de IVA, plan de financiación con DSCR e instrucciones. Las celdas verdes son las que se teclean y las 733 fórmulas se recalculan solas.' },
  { icon: Coins, title: 'Inversión Inicial Detallada', desc: 'Local, horno profesional de pisos o rotativo, amasadora espiral 25-50 kg, divisora y boleadora, cámara de fermentación controlada, vitrina expositor, mobiliario y fondo de maniobra: 101.600 € de CAPEX más 43.615 € de colchón de caja, 145.215 € en total.' },
  { icon: TrendingUp, title: 'Punto de Equilibrio (Break-Even)', desc: 'Cálculo en transacciones diarias con ticket medio de 5,50 € sin IVA: 162 al día para cubrir costes y 155 en términos de caja, con holgura sobre el equilibrio año a año y tabla de sensibilidad al ticket y al coste variable.' },
  { icon: BarChart3, title: 'Escenarios Financieros', desc: 'Tres escenarios — pesimista, realista y optimista — con diferentes volúmenes de producción y mix barra/bollería/cafetería para presentar a banco e inversores.' },
  { icon: Users, title: 'Cuadro de Personal Panadero', desc: 'Seis puestos —maestro panadero, oficial, ayudante de obrador, dependienta, extra de fin de semana y suplencias de vacaciones y descansos— con salarios brutos, Seguridad Social al 33 %, 14 pagas, turno de madrugada y comprobación de que las horas contratadas cubren el horario declarado.' },
  { icon: ShieldCheck, title: 'Checklist Apertura (6 fases)', desc: 'Constitución de la SL, local y licencias (registro sanitario de tu Comunidad Autónoma, licencia clasificada), equipamiento (proyecto técnico, salida de humos), personal, marketing y primeros 90 días.' },
  { icon: Wrench, title: 'Equipamiento Específico Panadería', desc: 'Horno de pisos o rotativo, amasadora espiral 25-50 kg, divisora y boleadora, cámara de fermentación controlada, laminadora y vitrina expositor, cada uno con su importe orientativo en la hoja de inversión.' },
  { icon: ListChecks, title: 'Ratios de Referencia Panadería', desc: 'Coste de mercancía 25-30 % en pan y 32-38 % en bollería, personal 35-42 %, alquiler 10-14 %, merma de pan 5-10 % y margen bruto objetivo por encima del 62 %. Los mismos rangos contra los que el libro se audita a sí mismo.' },
  { icon: Banknote, title: 'Plan de Financiación', desc: 'Hoja «Financiación» con origen de fondos —recursos propios, préstamo bancario, línea ICO, ENISA, business angels y subvenciones autonómicas—, comprobación de que lo aportado cubre lo que hace falta, cuadro de amortización francés con carencia y DSCR año a año.' },
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
