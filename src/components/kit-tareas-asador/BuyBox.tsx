import PaymentBadges from '../ebook/PaymentBadges';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_TAREAS_ASADOR || '#comprar';

export default function BuyBox() {
  return (
    <section id="comprar" className="py-16 md:py-24 px-4 relative overflow-hidden">
      <div className="absolute inset-0 opacity-[0.06]">
        <img src="/lovable-uploads/ai-gallery/tareas-asador-emplatado.jpg" alt="" className="w-full h-full object-cover" loading="lazy" />
      </div>
      <div className="absolute inset-0 bg-[#0a0a0a]/90" />
      <div className="relative max-w-lg mx-auto z-10">
        <div className="bg-white/5 border-2 border-[#FFD700]/50 rounded-2xl p-8 md:p-10 text-center backdrop-blur-sm">
          <div className="flex items-center justify-center gap-4 mb-3">
            <span className="text-2xl text-gray-500 line-through">€69</span>
            <span className="text-5xl md:text-6xl font-extrabold text-[#FFD700]">€14</span>
            <span className="px-3 py-1 rounded-full bg-[#FFD700]/20 text-[#FFD700] text-sm font-bold">-80%</span>
          </div>
          <p className="text-gray-400 text-sm mb-6">Precio especial de lanzamiento — 80% de descuento</p>
          <a href={stripeLink} className="inline-block w-full px-8 py-4 bg-[#FFD700] text-black font-bold text-lg rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02] active:scale-[0.98]">
            SÍ, QUIERO EL KIT DE TAREAS ASADOR — €14
          </a>
          <PaymentBadges className="mt-5" />
        </div>
      </div>
    </section>
  );
}
