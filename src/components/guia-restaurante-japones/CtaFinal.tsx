import { Check } from 'lucide-react';
import PaymentBadges from '../ebook/PaymentBadges';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_GUIA_RESTAURANTE_JAPONES || '#comprar';

const items = [
  'Guía completa PDF + DOCX (20 capítulos, 60+ páginas)',
  '8 plantillas Excel con fórmulas',
  '6 checklists de apertura completos',
  'Business Plan modelo para bancos',
  'Manual de operaciones japonés',
  'Escandallos de 15 recetas base japonesas',
];

export default function CtaFinal() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.06]">
        <img src="/lovable-uploads/ai-gallery/guia-restaurante-japones-sala.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/90" />
      <div className="absolute inset-0" style={{ background: 'radial-gradient(ellipse 80% 60% at 50% 50%, rgba(255,215,0,0.06) 0%, transparent 70%)' }} />
      <div className="relative max-w-3xl mx-auto text-center z-10">
        <h2 className="text-2xl md:text-4xl font-bold text-white mb-4">No Abras Tu Restaurante a Ciegas</h2>
        <p className="text-gray-400 text-lg mb-10 max-w-2xl mx-auto">Todo lo que necesitas por menos de lo que cuesta un omakase para dos.</p>
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
            <span className="text-xl text-gray-500 line-through">180 EUR</span>
            <span className="text-4xl md:text-5xl font-extrabold text-[#FFD700]">65 EUR</span>
          </div>
          <a href={stripeLink} className="inline-block w-full md:w-auto px-10 py-4 bg-[#FFD700] text-black font-bold text-lg rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02] active:scale-[0.98]">
            SÍ, QUIERO LA GUÍA — 65 EUR
          </a>
          <PaymentBadges className="mt-5" />
        </div>
      </div>
    </section>
  );
}
