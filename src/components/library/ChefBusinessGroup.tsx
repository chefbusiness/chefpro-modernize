import { Bot, MapPin, Globe, MessageSquare, Users, CheckSquare } from 'lucide-react';

const brands = [
  {
    icon: Bot,
    name: 'AI Chef Pro',
    desc: 'IA para Chefs y profesionales de hostelería',
    href: 'https://aichef.pro',
    color: 'text-[#FFD700] bg-[#FFD700]/10',
  },
  {
    icon: MapPin,
    name: 'GastroLocal',
    desc: 'Más clientes con Google Maps',
    href: 'https://gastrolocal.pro',
    color: 'text-green-400 bg-green-400/10',
  },
  {
    icon: Globe,
    name: 'GastroSEO',
    desc: 'SEO para restaurantes',
    href: 'https://gastroseo.com',
    color: 'text-cyan-400 bg-cyan-400/10',
  },
  {
    icon: MessageSquare,
    name: 'ChefBusiness',
    desc: 'Consultoría para restaurantes',
    href: 'https://chefbusiness.co',
    color: 'text-amber-400 bg-amber-400/10',
    badge: 'Matriz',
  },
  {
    icon: Users,
    name: 'Hosply.pro',
    desc: 'Conectando proveedores con la hostelería',
    href: 'https://hosply.pro',
    color: 'text-pink-400 bg-pink-400/10',
  },
  {
    icon: CheckSquare,
    name: 'Timlup.pro',
    desc: 'Gestión de tareas recurrentes para hostelería y retail',
    href: 'https://timlup.pro',
    color: 'text-violet-400 bg-violet-400/10',
    badge: 'MVP',
  },
];

export default function ChefBusinessGroup() {
  return (
    <section className="py-16 px-4 border-t border-white/10">
      <div className="max-w-6xl mx-auto text-center">
        <p className="text-[#FFD700]/60 text-xs font-bold tracking-[0.25em] uppercase mb-3">
          Parte de
        </p>
        <h2 className="text-3xl md:text-4xl font-extrabold text-white mb-2 italic">
          ChefBusiness Group
        </h2>
        <p className="text-gray-400 mb-10">
          Soluciones digitales para la industria gastronómica
        </p>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
          {brands.map(({ icon: Icon, name, desc, href, color, badge }) => (
            <a
              key={name}
              href={href}
              target="_blank"
              rel="noopener noreferrer"
              className="group relative bg-white/5 border border-white/10 rounded-xl p-4 hover:border-[#FFD700]/30 transition-all duration-200 flex flex-col items-center text-center"
            >
              {badge && (
                <span className="absolute top-2 right-2 text-[10px] font-bold px-1.5 py-0.5 rounded bg-[#FFD700]/10 text-[#FFD700] border border-[#FFD700]/20">
                  {badge}
                </span>
              )}
              <div className={`w-12 h-12 rounded-xl ${color} flex items-center justify-center mb-3`}>
                <Icon className="w-6 h-6" />
              </div>
              <h3 className="text-white font-bold text-sm mb-1 group-hover:text-[#FFD700] transition-colors italic">
                {name}
              </h3>
              <p className="text-gray-500 text-xs leading-relaxed">{desc}</p>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
