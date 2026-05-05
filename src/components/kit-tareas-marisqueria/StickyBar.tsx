const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_TAREAS_MARISQUERIA || '#comprar';

export default function StickyBar() {
  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-gray-900/95 backdrop-blur-md border-t border-white/10 px-3 py-3">
      <div className="flex items-center justify-between gap-2 max-w-screen-sm mx-auto">
        <p className="text-white text-xs font-bold truncate">KIT TAREAS MARISQUERÍA — €14</p>
        <a href={stripeLink} className="flex-shrink-0 px-5 py-2.5 bg-[#FFD700] text-black font-bold text-sm rounded-lg hover:bg-[#FFD700]/90 transition-all">
          COMPRAR
        </a>
      </div>
    </div>
  );
}
