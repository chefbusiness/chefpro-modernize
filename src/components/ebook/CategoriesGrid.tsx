import {
  ChefHat, Calculator, Cake, Wine, CalendarDays, Beaker,
  Megaphone, ShieldCheck, Briefcase, Users, Cpu, ClipboardList,
} from 'lucide-react';
import FadeIn from './FadeIn';

const categories = [
  { icon: ChefHat, title: 'Cocina y Recetas', desc: 'Más de 40 prompts para chefs y cocineros: genera recetas creativas con ingredientes disponibles, adapta platos a temporada, explora técnicas de alta cocina y fusión de cocinas del mundo. Incluye prompts para emplatado y presentación profesional.' },
  { icon: Calculator, title: 'Gestión y Costes', desc: 'Prompts esenciales para gerentes y dueños: calcula food cost en segundos, genera escandallos automáticos, analiza rentabilidad por plato y optimiza compras con proveedores. Convierte la IA en tu controller financiero de cocina.' },
  { icon: Cake, title: 'Pastelería y Panadería', desc: 'Sección dedicada a pasteleros, panaderos y chocolateros: formulaciones con porcentajes de panadero, técnicas de fermentación, combinaciones de sabores y adaptación de recetas para intolerancias. Crea cartas de temporada en minutos.' },
  { icon: Wine, title: 'Sala, Bar y Bebidas', desc: 'Para bartenders y sommeliers: crea cocktails de autor, diseña maridajes por plato, genera descripciones de vinos para la carta y optimiza el servicio de sala. Incluye prompts de mixología molecular y tendencias de bebidas.' },
  { icon: CalendarDays, title: 'Catering y Eventos', desc: 'Genera propuestas personalizadas, presupuestos detallados por comensal, planifica logística y diseña menús para bodas, corporativos y banquetes. Cada prompt pensado para impresionar al cliente y cerrar el evento.' },
  { icon: Beaker, title: 'Food Pairing', desc: 'Descubre combinaciones de ingredientes basadas en ciencia: maridajes por compuestos aromáticos, sustituciones inteligentes cuando falta un ingrediente y combinaciones inesperadas que sorprenden al comensal. La creatividad con base científica.' },
  { icon: Megaphone, title: 'Marketing del Negocio', desc: 'Prompts para generar contenido para RRSS, optimizar tu SEO local en Google, responder reseñas de forma profesional, crear campañas de email marketing y posicionar tu marca. Tu community manager con IA integrado.' },
  { icon: ShieldCheck, title: 'Alérgenos y Seguridad', desc: 'Genera fichas técnicas de alérgenos completas, etiquetado conforme a normativa, protocolos APPCC actualizados y planes de formación para tu equipo. Cumple la legislación sin pasar horas con la documentación.' },
  { icon: Briefcase, title: 'Gestión de Negocio', desc: 'Desde planes de negocio para nuevos conceptos hasta estrategias de precios y análisis de viabilidad de franquicias. Incluye prompts de consultoría que te ayudan a tomar decisiones estratégicas con datos, no con intuición.' },
  { icon: Users, title: 'Liderazgo y Equipos', desc: 'Prompts para mejorar tu liderazgo en cocina: evaluaciones de rendimiento, planes de formación, protocolos de onboarding para nuevas incorporaciones y técnicas de comunicación con brigada. Gestiona personas, no solo platos.' },
  { icon: Cpu, title: 'Prompt Engineering', desc: 'El capítulo que multiplica el valor de todos los demás: aprende el framework CRAFT para escribir prompts perfectos en hostelería. Entiende cómo piensa la IA y obtén respuestas 10x mejores en cualquier herramienta.' },
  { icon: ClipboardList, title: 'Plantillas Copy-Paste', desc: 'Prompts listos para copiar, pegar y usar en segundos — sin necesidad de adaptación. Organizados por perfil: chef, gerente, pastelero, bartender, catering y dueño de restaurante. La forma más rápida de empezar.' },
];

const foodStrip = [
  '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-garibaldi-fermentado.jpeg',
  '/lovable-uploads/ai-gallery/milhojas-vertical-de-vainilla-con-frambuesas-aichefpro-2.jpeg',
  '/lovable-uploads/ai-gallery/carpaccio-gambas.jpeg',
  '/lovable-uploads/ai-gallery/torrija-caramelizada-con-helado.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-tepache-pina-asada.jpeg',
];

export default function CategoriesGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              ¿Qué Encontrarás en el <span className="text-[#FFD700]">eBook</span>?
            </h2>
            <p className="text-gray-400 text-lg">
              Más de 300 prompts organizados en 12 categorías para toda la hostelería
            </p>
          </div>
        </FadeIn>

        {/* Food image strip */}
        <FadeIn>
          <div className="grid grid-cols-3 md:grid-cols-6 gap-2 mb-12 rounded-xl overflow-hidden">
            {foodStrip.map((src, i) => (
              <div key={i} className="aspect-square overflow-hidden rounded-lg">
                <img
                  src={src}
                  alt=""
                  className="w-full h-full object-cover hover:scale-110 transition-transform duration-500"
                  loading="lazy"
                />
              </div>
            ))}
          </div>
        </FadeIn>

        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
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
