const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK_APPCC || '#comprar';

export default function StickyBar() {
  return (
    <div className="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-gray-900/95 backdrop-blur-md border-t border-white/10 px-4 py-3">
      <div className="flex items-center justify-between gap-3">
        <div>
          <p className="text-white text-sm font-bold">PACK APPCC — €14</p>
        </div>
        <a
          href={stripeLink}
          className="px-6 py-2.5 bg-[#FFD700] text-black font-bold text-sm rounded-lg whitespace-nowrap hover:bg-[#FFD700]/90 transition-all"
        >
          COMPRAR AHORA
        </a>
      </div>
    </div>
  );
}
