import { useRef, useState } from 'react';
import { UtensilsCrossed } from 'lucide-react';
import PaymentBadges from './PaymentBadges';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK || '#comprar';

export default function BookCover() {
  const bookRef = useRef<HTMLDivElement>(null);
  const [rotation, setRotation] = useState({ x: 0, y: -15 });

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!bookRef.current) return;
    const rect = bookRef.current.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const rotateY = ((e.clientX - centerX) / rect.width) * 25;
    const rotateX = -((e.clientY - centerY) / rect.height) * 12;
    setRotation({ x: rotateX, y: rotateY });
  };

  const handleMouseLeave = () => {
    setRotation({ x: 0, y: -15 });
  };

  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      {/* Ambient glow behind book */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-[#FFD700]/[0.07] rounded-full blur-[120px] pointer-events-none" />

      <div className="max-w-lg mx-auto flex flex-col items-center relative z-10">
        {/* 3D Interactive Book */}
        <div
          ref={bookRef}
          className="relative cursor-pointer"
          style={{ perspective: '1800px' }}
          onMouseMove={handleMouseMove}
          onMouseLeave={handleMouseLeave}
        >
          <div
            className="relative transition-transform duration-300 ease-out"
            style={{
              transform: `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`,
              transformStyle: 'preserve-3d',
            }}
          >
            {/* === BOOK STRUCTURE === */}
            <div className="relative w-72 sm:w-80 md:w-96" style={{ transformStyle: 'preserve-3d' }}>

              {/* FRONT COVER */}
              <div
                className="relative rounded-r-xl rounded-l-sm overflow-hidden"
                style={{ transformStyle: 'preserve-3d' }}
              >
                {/* Full food image background */}
                <div className="absolute inset-0">
                  <img
                    src="/lovable-uploads/ai-gallery/ostra-aire-gintonic.jpeg"
                    alt=""
                    className="w-full h-full object-cover"
                  />
                  <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-black/50 to-black/80" />
                </div>

                {/* Content */}
                <div className="relative z-10 flex flex-col items-center justify-center min-h-[420px] sm:min-h-[480px] md:min-h-[560px] p-8 md:p-10">
                  {/* Top gold accent line */}
                  <div className="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-r from-transparent via-[#FFD700] to-transparent" />

                  {/* Large background icon */}
                  <div className="absolute inset-0 flex items-center justify-center opacity-[0.06] pointer-events-none">
                    <UtensilsCrossed className="w-64 h-64 text-[#FFD700]" />
                  </div>

                  {/* Icon */}
                  <div className="w-16 h-16 md:w-20 md:h-20 rounded-full bg-[#FFD700]/20 border border-[#FFD700]/30 flex items-center justify-center mb-6 backdrop-blur-sm">
                    <UtensilsCrossed className="w-8 h-8 md:w-10 md:h-10 text-[#FFD700]" />
                  </div>

                  <p className="text-[#FFD700] text-xs md:text-sm font-bold tracking-[0.25em] uppercase mb-3">
                    Pro Prompts
                  </p>
                  <h3 className="text-white text-xl md:text-2xl font-extrabold text-center mb-2 leading-tight">
                    Hostelería y<br />Restauración
                  </h3>
                  <div className="w-16 h-px bg-gradient-to-r from-transparent via-[#FFD700] to-transparent my-4" />
                  <p className="text-gray-300 text-sm text-center font-medium">
                    300+ Prompts profesionales
                  </p>
                  <p className="text-gray-500 text-xs text-center mt-1">
                    AI Chef Pro · 2026
                  </p>

                  {/* Bottom gold accent line */}
                  <div className="absolute bottom-0 left-0 right-0 h-1.5 bg-gradient-to-r from-transparent via-[#FFD700] to-transparent" />
                </div>

                {/* Glossy reflection overlay */}
                <div
                  className="absolute inset-0 pointer-events-none"
                  style={{
                    background: 'linear-gradient(135deg, rgba(255,255,255,0.12) 0%, transparent 40%, transparent 60%, rgba(255,255,255,0.05) 100%)',
                  }}
                />

                {/* Gold border frame */}
                <div className="absolute inset-0 border-2 border-[#FFD700]/20 rounded-r-xl rounded-l-sm pointer-events-none" />
                <div className="absolute inset-2 border border-[#FFD700]/10 rounded-r-lg pointer-events-none" />
              </div>

              {/* SPINE (left edge) — visible 3D side */}
              <div
                className="absolute top-0 left-0 h-full"
                style={{
                  width: '28px',
                  transform: 'translateX(-14px) rotateY(-90deg)',
                  transformOrigin: 'right center',
                  background: 'linear-gradient(to right, #B8860B, #DAA520, #FFD700, #DAA520, #B8860B)',
                  borderRadius: '2px 0 0 2px',
                }}
              >
                {/* Spine text */}
                <div className="absolute inset-0 flex items-center justify-center">
                  <p
                    className="text-black/70 text-[8px] font-bold tracking-[0.15em] uppercase whitespace-nowrap"
                    style={{ writingMode: 'vertical-rl', transform: 'rotate(180deg)' }}
                  >
                    PRO PROMPTS · AI CHEF PRO
                  </p>
                </div>
                {/* Spine texture lines */}
                <div className="absolute top-4 left-1/2 -translate-x-1/2 w-[60%] h-px bg-black/20" />
                <div className="absolute bottom-4 left-1/2 -translate-x-1/2 w-[60%] h-px bg-black/20" />
              </div>

              {/* PAGES (visible edge on the right when rotated) */}
              <div
                className="absolute top-[3px] right-0 bottom-[3px]"
                style={{
                  width: '20px',
                  transform: 'translateX(10px) rotateY(90deg)',
                  transformOrigin: 'left center',
                  background: 'repeating-linear-gradient(to bottom, #f5f0e8 0px, #f5f0e8 1px, #e8e0d0 1px, #e8e0d0 2px)',
                  borderRadius: '0 2px 2px 0',
                  boxShadow: 'inset -3px 0 6px rgba(0,0,0,0.15)',
                }}
              />

              {/* BACK COVER (behind) */}
              <div
                className="absolute inset-0 bg-gray-900 rounded-r-xl rounded-l-sm"
                style={{
                  transform: 'translateZ(-28px)',
                  boxShadow: '0 0 20px rgba(0,0,0,0.5)',
                }}
              />
            </div>
          </div>

          {/* Shadow on surface */}
          <div
            className="absolute -bottom-6 left-1/2 -translate-x-1/2 w-[75%] h-8 rounded-full"
            style={{
              background: 'radial-gradient(ellipse, rgba(0,0,0,0.5) 0%, rgba(0,0,0,0.2) 50%, transparent 80%)',
              filter: 'blur(8px)',
            }}
          />
        </div>

        {/* CTA below book */}
        <div className="mt-12 text-center">
          <a
            href={stripeLink}
            className="inline-block px-8 py-3.5 border-2 border-[#FFD700] text-[#FFD700] font-bold rounded-xl hover:bg-[#FFD700] hover:text-black transition-all duration-300"
          >
            COMPRAR AHORA — €9
          </a>
          <PaymentBadges className="mt-3" />
        </div>
      </div>
    </section>
  );
}
