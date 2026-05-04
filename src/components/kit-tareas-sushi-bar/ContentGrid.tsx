import {
  DoorOpen, Sparkles, ShieldCheck, Refrigerator,
  Briefcase, Users, ClipboardList, CalendarDays, FileSpreadsheet,
  Megaphone, Calendar,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: DoorOpen, title: 'Apertura y Cierre Sushi', desc: 'Checklists de barra sushi, cocina caliente y sala: temperaturas de neta case, arroz cocido del día, pescado expuesto, cierre completo y arqueo.' },
  { icon: Sparkles, title: 'Arroz Sushi y Corte de Pescado', desc: 'Protocolo de arroz: lavado, cocción, sazonado con sushi-zu, control de pH (≤4.6) y tiempos de descarte. Técnicas de corte: yanagiba, sashimi, nigiri y maki.' },
  { icon: ShieldCheck, title: 'Seguridad Anisakis y APPCC', desc: 'Registro de congelación a -20 ºC durante 7 días por lote (RD 1420/2006), control de temperaturas, alérgenos y trazabilidad completa de pescado y proveedores.' },
  { icon: Refrigerator, title: 'Barra Sushi y Vitrina Neta Case', desc: 'Mise en place de la vitrina refrigerada (2-4 ºC), rotación FIFO por lotes, exposición máxima de 2 horas, organización de la estación itamae y limpieza por turno.' },
  { icon: Briefcase, title: 'Tareas del Manager', desc: 'Pedidos a lonja, control de stock de pescado, gestión del equipo, reservas (incluido omakase), revenue diario, comparativa de proveedores y reporting.' },
  { icon: Users, title: 'Perfiles: Itamae y Equipo', desc: 'Tareas claras por perfil: itamae, ayudante de sushi, cocina caliente, sala y servicio, delivery. Roles y responsabilidades sin solapes.' },
  { icon: ClipboardList, title: 'Semanales y Mensuales', desc: 'Cuchillería japonesa (afilado yanagiba, deba), limpieza profunda de neta case, stock de productos secos, formación del equipo y revisión de proveedores.' },
  { icon: CalendarDays, title: 'Eventos y Temporadas', desc: 'Calendario de temporadas de pescado en España (atún rojo, bonito, salmón salvaje), omakases especiales, Nochevieja, San Valentín y festivos asiáticos.' },
  { icon: FileSpreadsheet, title: 'Plantilla Personalizable', desc: 'Plantilla en blanco con la estructura del kit para que crees checklists a medida del concepto exacto de tu sushi bar (omakase, kaiten, takeaway, fusión nikkei).' },
  { icon: Megaphone, title: 'BONUS: Briefing de Servicio', desc: 'Briefing pre-servicio de 5 minutos: pescado del día, alérgenos críticos, VIPs, omakase, stock disponible y avisos para itamae y sala.' },
  { icon: Calendar, title: 'BONUS: Calendario Anual', desc: 'Año completo con temporadas de pescado, festivos asiáticos, mantenimientos de equipos, formación del equipo y cierres por vacaciones.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-chef-privado-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-servicio.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-transporte.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-emplatado.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-cliente.jpg',
  '/lovable-uploads/ai-gallery/tareas-chef-privado-cocina.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">11</span> Checklists Operativos para Sushi Bar
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada checklist viene pre-rellenado con las tareas reales de un sushi bar profesional. Solo ajusta a tu carta, imprime y empieza a operar con estándar Sanidad.
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
