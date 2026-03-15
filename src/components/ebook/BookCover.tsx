import PaymentBadges from './PaymentBadges';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK || '#comprar';

export default function BookCover() {
  return (
    <section className="py-16 md:py-24 px-4 relative overflow-hidden">
      {/* Ambient glow */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-[#FFD700]/[0.05] rounded-full blur-[120px] pointer-events-none" />

      <div className="max-w-5xl mx-auto flex flex-col items-center relative z-10">
        {/* 3D Mockup Bundle Image */}
        <img
          src="/ebook-mockup-bundle.png"
          alt="Gastro Pro Prompts — eBook, tablet y móvil con 300+ prompts de IA para hostelería y restauración"
          className="w-full mx-auto"
        />

        {/* CTA below mockup */}
        <div className="mt-10 text-center">
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
