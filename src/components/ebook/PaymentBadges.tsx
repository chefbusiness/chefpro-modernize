export default function PaymentBadges({ className = '' }: { className?: string }) {
  return (
    <div className={`flex flex-col items-center gap-2 ${className}`}>
      <img
        src="/powered-by-stripe.png"
        alt="Powered by Stripe — Visa, Mastercard, Maestro, Google Pay, Apple Pay"
        className="w-full max-w-[260px] bg-white rounded-lg px-3 py-1.5"
      />
    </div>
  );
}
