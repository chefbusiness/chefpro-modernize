import {
  Calculator, ShieldAlert, Calendar, TrendingUp, FileText,
  Smartphone, Users, Sparkles, ArrowRight,
} from 'lucide-react';

const tools = [
  { icon: Calculator, title: 'Calculadora Food Cost', desc: 'Calcula el coste real de cada plato', href: '/calculadora-food-cost-restaurante', color: 'bg-green-500/20 text-green-400' },
  { icon: ShieldAlert, title: 'Detector Alérgenos', desc: 'Identifica alérgenos en tus recetas', href: '/detector-alergenos-restaurante', color: 'bg-red-500/20 text-red-400' },
  { icon: Calendar, title: 'Calendario Contenidos', desc: 'Plan mensual para redes sociales', href: '/calendario-contenidos-restaurante', color: 'bg-purple-500/20 text-purple-400' },
  { icon: TrendingUp, title: 'Simulador Rentabilidad', desc: 'Proyecta ingresos y beneficio neto', href: '/simulador-rentabilidad-restaurante', color: 'bg-yellow-500/20 text-yellow-400' },
  { icon: FileText, title: 'Generador Textos Carta', desc: 'Descripciones irresistibles para tu menú', href: '/generador-textos-carta-restaurante', color: 'bg-blue-500/20 text-blue-400' },
  { icon: Smartphone, title: 'Test Digitalización', desc: 'Evalúa el nivel digital de tu restaurante', href: '/test-digitalizacion-restaurante', color: 'bg-teal-500/20 text-teal-400' },
  { icon: Users, title: 'Calculadora Brigada', desc: 'Personal óptimo según tu servicio', href: '/calculadora-brigada-restaurante', color: 'bg-orange-500/20 text-orange-400' },
  { icon: Sparkles, title: 'Menú Degustación', desc: 'Crea menús degustación con IA', href: '/generador-menu-degustacion', color: 'bg-indigo-500/20 text-indigo-400' },
];

export default function FreeToolsGrid() {
  return (
    <section className="py-10 px-4">
      <div className="max-w-5xl mx-auto">
        <div className="flex flex-col sm:flex-row sm:items-center gap-3 mb-6">
          <h2 className="text-2xl font-bold text-white">Herramientas Gratuitas</h2>
          <span className="px-3 py-1 bg-green-500/10 text-green-400 text-sm rounded-full w-fit border border-green-500/20">
            8 herramientas incluidas
          </span>
        </div>
        <p className="text-gray-400 mb-6 max-w-2xl">
          Como comprador del eBook, tienes acceso directo a todas nuestras herramientas profesionales para hostelería.
        </p>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          {tools.map(({ icon: Icon, title, desc, href, color }) => (
            <a
              key={title}
              href={href}
              target="_blank"
              rel="noopener noreferrer"
              className="group bg-white/5 border border-white/10 rounded-xl p-4 hover:border-[#FFD700]/40 transition-all duration-200"
            >
              <div className={`w-10 h-10 rounded-lg ${color.split(' ')[0]} flex items-center justify-center mb-3`}>
                <Icon className={`w-5 h-5 ${color.split(' ')[1]}`} />
              </div>
              <h3 className="text-white font-semibold text-sm mb-1 group-hover:text-[#FFD700] transition-colors">
                {title}
              </h3>
              <p className="text-gray-500 text-xs leading-relaxed mb-2">{desc}</p>
              <span className="text-[#FFD700] text-xs font-medium inline-flex items-center gap-1">
                Abrir <ArrowRight className="w-3 h-3 group-hover:translate-x-0.5 transition-transform" />
              </span>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
