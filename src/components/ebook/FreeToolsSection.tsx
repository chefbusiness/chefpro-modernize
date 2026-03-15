import {
  Calculator, ShieldAlert, Calendar, TrendingUp, FileText,
  Smartphone, Users, Sparkles, ArrowRight,
} from 'lucide-react';
import FadeIn from './FadeIn';

const tools = [
  { icon: Calculator, title: 'Calculadora Food Cost', desc: 'Calcula el coste real de cada plato al céntimo', href: '/calculadora-food-cost-restaurante', color: 'text-green-400' },
  { icon: ShieldAlert, title: 'Detector Alérgenos', desc: 'Identifica alérgenos automáticamente en tus recetas', href: '/detector-alergenos-restaurante', color: 'text-red-400' },
  { icon: Calendar, title: 'Calendario Contenidos', desc: 'Plan de contenido mensual para redes sociales', href: '/calendario-contenidos-restaurante', color: 'text-purple-400' },
  { icon: TrendingUp, title: 'Simulador Rentabilidad', desc: 'Proyecta ingresos, costes y beneficio neto', href: '/simulador-rentabilidad-restaurante', color: 'text-yellow-400' },
  { icon: FileText, title: 'Generador Textos Carta', desc: 'Descripciones irresistibles para tu menú', href: '/generador-textos-carta-restaurante', color: 'text-blue-400' },
  { icon: Smartphone, title: 'Test Digitalización', desc: 'Evalúa el nivel digital de tu restaurante', href: '/test-digitalizacion-restaurante', color: 'text-teal-400' },
  { icon: Users, title: 'Calculadora Brigada', desc: 'Personal óptimo según tu volumen de servicio', href: '/calculadora-brigada-restaurante', color: 'text-orange-400' },
  { icon: Sparkles, title: 'Generador Menú Degustación', desc: 'Crea menús degustación con IA en segundos', href: '/generador-menu-degustacion', color: 'text-indigo-400' },
];

export default function FreeToolsSection() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-4">
            <span className="inline-block mb-4 px-3 py-1 rounded-full bg-green-500/10 border border-green-500/30 text-green-400 text-xs font-bold tracking-wider uppercase">
              Bonus extra incluido
            </span>
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              8 Herramientas Profesionales <span className="text-[#FFD700]">Gratuitas</span>
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Con tu compra accedes también a nuestras herramientas profesionales para hostelería. Úsalas directamente desde tu dashboard o desde aquí.
            </p>
          </div>
        </FadeIn>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-10">
          {tools.map(({ icon: Icon, title, desc, href, color }, i) => (
            <FadeIn key={title} delay={i * 60}>
              <a
                href={href}
                className="group bg-white/5 border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/40 transition-all duration-300 block h-full"
              >
                <Icon className={`w-7 h-7 ${color} mb-3`} />
                <h3 className="text-white font-semibold text-sm mb-1.5 group-hover:text-[#FFD700] transition-colors">
                  {title}
                </h3>
                <p className="text-gray-500 text-xs leading-relaxed mb-3">{desc}</p>
                <span className="text-[#FFD700] text-xs font-medium flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                  Usar gratis <ArrowRight className="w-3 h-3" />
                </span>
              </a>
            </FadeIn>
          ))}
        </div>
      </div>
    </section>
  );
}
