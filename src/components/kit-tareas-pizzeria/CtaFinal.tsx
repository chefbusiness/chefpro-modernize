import { Check } from 'lucide-react';
import PaymentBadges from '../ebook/PaymentBadges';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_TAREAS_PIZZERIA || '#comprar';

const items = [
  'Checklists de apertura y cierre: horno, línea, sala, barra',
  'Tareas del pizzero: fermentación, estirado, cocción 60-90s',
  'Control de horno: temperatura 400-450 °C, limpieza, leña',
  'Checklist diario, semanal y mensual del manager',
  'Tareas por perfil: pizzero, cocinero línea, encargado, repartidor',
  'Delivery y take-away: packaging, riders, tiempos',
  'BONUS: Briefing de Servicio (€7)',
  'BONUS: Calendario Anual de Tareas (€9)',
];

export default function CtaFinal() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.06]">
        <img src="/lovable-uploads/ai-gallery/tareas-pizzeria-hero.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/90" />
      <div className="absolute inset-0" style={{
        background: 'radial-gradient(ellipse 80% 60% at 50% 50%, rgba(255,215,0,0.06) 0%, transparent 70%)',
      }} />

      <div className="relative max-w-3xl mx-auto text-center z-10">
        <h2 className="text-2xl md:text-4xl font-bold text-white mb-4">
          Deja de Repetir las Mismas Instrucciones Cada Día
        </h2>
        <p className="text-gray-400 text-lg mb-10 max-w-2xl mx-auto">
          9 checklists operativos para pizzería por menos de lo que cuesta una hora de consultoría.
        </p>

        <div className="bg-white/5 border border-[#FFD700]/20 rounded-2xl p-8 md:p-10 backdrop-blur-sm">
          <div className="flex flex-col items-start gap-3 mb-8 max-w-md mx-auto">
            {items.map((item) => (
              <div key={item} className="flex items-start gap-3">
                <Check className="w-5 h-5 text-[#FFD700] flex-shrink-0 mt-0.5" />
                <span className="text-gray-200 text-left">{item}</span>
              </div>
            ))}
          </div>

          <div className="flex items-center justify-center gap-4 mb-4">
            <span className="text-xl text-gray-500 line-through">€39</span>
            <span className="text-4xl md:text-5xl font-extrabold text-[#FFD700]">€12</span>
          </div>

          <a
            href={stripeLink}
            className="inline-block w-full md:w-auto px-10 py-4 bg-[#FFD700] text-black font-bold text-lg rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02] active:scale-[0.98]"
          >
            SÍ, QUIERO EL KIT DE TAREAS — €12
          </a>
          <PaymentBadges className="mt-5" />
        </div>
      </div>
    </section>
  );
}
