import {
  CalendarDays, Clock, Euro, UserPlus, Palmtree,
  Star, Users, Megaphone, Calculator,
} from 'lucide-react';
import FadeIn from '../ebook/FadeIn';

const templates = [
  { icon: CalendarDays, title: 'Cuadrante de Turnos', desc: 'Planificación semanal y mensual con las 4 alertas reales: descanso mínimo de 12h entre jornadas (art. 34.3 ET), descanso semanal, jornada diaria máxima y horas sobre lo contratado.' },
  { icon: Clock, title: 'Control de Horas Extra', desc: 'Registro de horas extra por empleado con cálculo automático de coste según el recargo de tu convenio (celda editable). Alerta al superar el tope legal de 80h/año.' },
  { icon: Euro, title: 'Coste Laboral Mensual', desc: 'Ratio coste laboral/ventas con semáforo por tipo de negocio (fast casual, casual, fine dining, catering...). Previsión de plantilla por servicio y comparativa mensual.' },
  { icon: UserPlus, title: 'Onboarding Nuevo Empleado', desc: '50 tareas organizadas en cinco bloques: documentación legal, formación APPCC, prevención de riesgos, uniforme, formación de puesto, sistemas y accesos. Cada una con su plazo en días desde el alta.' },
  { icon: Palmtree, title: 'Planificación Vacaciones', desc: 'Calendario anual por semanas con saldo real de vacaciones. Solicitudes, aprobaciones, cobertura mínima por puesto y aviso en temporada alta.' },
  { icon: Star, title: 'Evaluación de Desempeño', desc: '10 competencias clave para hostelería con scoring 1-5. Histórico trimestral, objetivos por periodo y plan de desarrollo individual.' },
  { icon: Users, title: 'Directorio de Plantilla', desc: 'Base de datos completa: datos personales, puesto, convenio aplicable, vencimiento de contrato, carnets (manipulador, PRL) y aviso de menores de edad.' },
  { icon: Megaphone, title: 'BONUS: Briefing Cambio de Turno', desc: 'Traspaso entre turnos: incidencias, reservas VIP, tareas pendientes, stock bajo, ausencias y cambios de personal, ARQUEO DE CAJA con lectura Z y descuadre, y TEMPERATURAS al relevo (APPCC) con mínimo y máximo por equipo.' },
  { icon: Calculator, title: 'BONUS: Calculadora Plantilla Óptima', desc: 'Calcula cuántos empleados necesitas según covers por servicio, ratio empleado/cubierto, días de apertura y picos de demanda.' },
];

const galleryImages = [
  '/lovable-uploads/ai-gallery/tareas-gestion-personal-hero.jpg',
  '/lovable-uploads/ai-gallery/tareas-gestion-personal-turnos.jpg',
  '/lovable-uploads/ai-gallery/tareas-gestion-personal-cocina.jpg',
  '/lovable-uploads/ai-gallery/tareas-gestion-personal-equipo.jpg',
  '/lovable-uploads/ai-gallery/tareas-gestion-personal-oficina.jpg',
  '/lovable-uploads/ai-gallery/tareas-gestion-personal-servicio.jpg',
];

export default function ContentGrid() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-6xl mx-auto">
        <FadeIn>
          <div className="text-center mb-12">
            <h2 className="text-2xl md:text-4xl font-bold text-white mb-3">
              <span className="text-[#FFD700]">9</span> Plantillas de Gestion de Personal
            </h2>
            <p className="text-gray-400 text-lg max-w-3xl mx-auto">
              Cada plantilla incluye formulas automaticas y esta disenada para la realidad de la hosteleria. Solo ajusta a tu negocio y empieza a planificar.
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
