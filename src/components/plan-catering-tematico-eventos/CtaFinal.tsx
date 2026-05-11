import { Check } from 'lucide-react';
import PaymentBadges from '../ebook/PaymentBadges';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_PLAN_CATERING_TEMATICO || '#comprar';

const items = [
  'Plan de Negocio DOCX 60+ pp. + Plan Financiero Excel 6 hojas',
  'Calculadora Pricing multi-concepto + Plantilla 96 proveedores · 12 cocinas del mundo',
  'Catálogo equipamiento multi-cocina (cuchillería japonesa, horno leña, tandoor, smoker, wok)',
  '12 conceptos pre-empaquetados + Carta 12 menús temáticos cocinas del mundo',
  'Manual técnico APPCC multi-concepto + Modelos contrato B2C + B2B corporate (con MSA)',
  'Guía especialización progresiva — escalar de 1 a 6+ conceptos en portafolio',
  'Checklist apertura 6 fases + anexo regulación 17 CCAA catering itinerante',
  'Acceso de por vida + 30 días garantía devolución',
];

export default function CtaFinal() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.06]">
        <img src="/lovable-uploads/ai-gallery/plan-catering-tematico-eventos-hero.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/90" />
      <div className="absolute inset-0" style={{ background: 'radial-gradient(ellipse 80% 60% at 50% 50%, rgba(255,215,0,0.06) 0%, transparent 70%)' }} />
      <div className="relative max-w-3xl mx-auto text-center z-10">
        <h2 className="text-2xl md:text-4xl font-bold text-white mb-4">Es Hora de Lanzar tu <span className="text-[#FFD700]">Catering Temático Multi-concepto</span></h2>
        <p className="text-gray-400 text-lg mb-10 max-w-2xl mx-auto">No dejes pasar esta oportunidad. Únete a sushi masters, taqueros, pizzaiolos, asadores argentinos, chefs ceviche y tandoor masters que ya montaron o escalaron su catering temático multi-concepto con un plan adaptado al mercado español premium.</p>
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
            <span className="text-xl text-gray-500 line-through">€165</span>
            <span className="text-4xl md:text-5xl font-extrabold text-[#FFD700]">€45</span>
          </div>
          <a href={stripeLink} className="inline-block w-full md:w-auto px-10 py-4 bg-[#FFD700] text-black font-bold text-lg rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02] active:scale-[0.98]">
            SÍ, QUIERO EL PLAN — €45
          </a>
          <PaymentBadges className="mt-5" />
        </div>
      </div>
    </section>
  );
}
