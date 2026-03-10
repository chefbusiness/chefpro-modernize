import { ChefHat } from 'lucide-react';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK || '#comprar';

export default function BookCover() {
  return (
    <section className="py-16 md:py-24 px-4">
      <div className="max-w-lg mx-auto flex flex-col items-center">
        {/* 3D Book with CSS */}
        <div className="relative" style={{ perspective: '1200px' }}>
          <div
            className="relative w-64 md:w-80 rounded-xl overflow-hidden shadow-2xl"
            style={{
              transform: 'rotateY(-8deg)',
              transformStyle: 'preserve-3d',
            }}
          >
            {/* Spine */}
            <div className="absolute left-0 top-0 bottom-0 w-3 bg-[#FFD700] z-10 rounded-l-xl" />

            {/* Cover */}
            <div className="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 border border-white/10 p-8 md:p-10 flex flex-col items-center justify-center min-h-[380px] md:min-h-[460px]">
              <div className="w-16 h-16 rounded-full bg-[#FFD700]/20 flex items-center justify-center mb-6">
                <ChefHat className="w-8 h-8 text-[#FFD700]" />
              </div>
              <p className="text-[#FFD700] text-xs font-bold tracking-[0.2em] uppercase mb-2">
                Pro Prompts
              </p>
              <h3 className="text-white text-xl md:text-2xl font-bold text-center mb-2">
                Hostelería y Restauración
              </h3>
              <div className="w-12 h-px bg-[#FFD700]/60 my-3" />
              <p className="text-gray-400 text-sm text-center">
                300+ Prompts para toda la hostelería
              </p>
            </div>
          </div>

          {/* Shadow */}
          <div className="absolute -bottom-4 left-1/2 -translate-x-1/2 w-[85%] h-6 bg-black/40 blur-xl rounded-full" />
        </div>

        {/* CTA below book */}
        <div className="mt-12 text-center">
          <a
            href={stripeLink}
            className="inline-block px-8 py-3.5 border-2 border-[#FFD700] text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700] hover:text-black transition-all"
          >
            COMPRAR AHORA — €9
          </a>
          <p className="text-xs text-gray-500 mt-3">
            Pago 100% seguro. Acceso inmediato por email
          </p>
        </div>
      </div>
    </section>
  );
}
