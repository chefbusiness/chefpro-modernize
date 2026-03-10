import {
  ChefHat, Calculator, Cake, Wine, CalendarDays, Beaker,
  Megaphone, ShieldCheck, Briefcase, Users, Cpu, ClipboardList,
} from 'lucide-react';

const categories = [
  { icon: ChefHat, title: 'Cocina y Recetas', desc: 'Para chefs y cocineros: recetas creativas, técnicas, fusión y cocinas del mundo' },
  { icon: Calculator, title: 'Gestión y Costes', desc: 'Para gerentes y dueños: food cost, escandallos, rentabilidad y control de negocio' },
  { icon: Cake, title: 'Pastelería y Panadería', desc: 'Para pasteleros, panaderos y chocolateros: formulaciones, técnicas y creatividad' },
  { icon: Wine, title: 'Sala, Bar y Bebidas', desc: 'Para bartenders y sommeliers: coctelería, maridajes, carta de vinos y sala' },
  { icon: CalendarDays, title: 'Catering y Eventos', desc: 'Propuestas, presupuestos, logística y menús para bodas, corporativos y banquetes' },
  { icon: Beaker, title: 'Food Pairing', desc: 'Maridajes científicos, sustituciones de ingredientes y combinaciones inesperadas' },
  { icon: Megaphone, title: 'Marketing del Negocio', desc: 'RRSS, SEO local, reseñas, email marketing y posicionamiento de marca' },
  { icon: ShieldCheck, title: 'Alérgenos y Seguridad', desc: 'Gestión de alérgenos, etiquetado, protocolos APPCC y formación de equipo' },
  { icon: Briefcase, title: 'Gestión de Negocio', desc: 'Planes de negocio, franquicias, estrategia de precios y consultoría' },
  { icon: Users, title: 'Liderazgo y Equipos', desc: 'Liderazgo, feedback, bienestar y gestión de brigada' },
  { icon: Cpu, title: 'Prompt Engineering', desc: 'El framework para obtener respuestas perfectas de cualquier IA en hostelería' },
  { icon: ClipboardList, title: 'Plantillas Copy-Paste', desc: 'Listas para usar en segundos para cualquier perfil del sector' },
];

export default function CategoriesGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
            ¿Qué Encontrarás en el eBook?
          </h2>
          <p className="text-gray-400 text-lg">
            Más de 300 prompts organizados en 12 categorías para toda la hostelería
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {categories.map(({ icon: Icon, title, desc }) => (
            <div
              key={title}
              className="group bg-white/5 border border-white/10 rounded-xl p-5 hover:border-[#FFD700]/50 transition-all duration-300"
            >
              <Icon className="w-8 h-8 text-[#FFD700] mb-3" />
              <h3 className="text-white font-semibold text-sm md:text-base mb-1.5">{title}</h3>
              <p className="text-gray-400 text-xs md:text-sm leading-relaxed">{desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
