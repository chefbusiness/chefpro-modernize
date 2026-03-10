import { Check } from 'lucide-react';

const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK || '#comprar';

const checkItems = [
  'Acceso instantáneo al eBook completo',
  'Más de 300 prompts para toda la hostelería y restauración',
  'Compatible con ChatGPT, Claude, Perplexity, DeepSeek y más',
  'Actualizaciones gratuitas de por vida',
];

export default function HeroSection() {
  return (
    <section className="relative px-4 pt-24 pb-16 md:pt-32 md:pb-24">
      <div className="max-w-4xl mx-auto text-center">
        {/* Badge */}
        <span className="inline-block mb-6 px-4 py-1.5 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-sm font-medium">
          🌍 El recurso #1 de prompts para el mundo de la hostelería y la restauración
        </span>

        {/* H1 */}
        <h1 className="text-3xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
          El Único{' '}
          <span className="text-[#FFD700]">eBook de Prompts</span>{' '}
          de IA para Hostelería que Realmente Necesitas
        </h1>

        {/* Subtitle */}
        <p className="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto mb-10 leading-relaxed">
          Para chefs, gerentes, pasteleros, bartenders, chocolateros, dueños de restaurante y todos los profesionales del sector. Desbloquea el potencial real de la IA en tu negocio.
        </p>

        {/* Checklist */}
        <div className="flex flex-col items-center gap-3 mb-10">
          {checkItems.map((item) => (
            <div key={item} className="flex items-center gap-3 text-gray-200">
              <Check className="w-5 h-5 text-[#FFD700] flex-shrink-0" />
              <span>{item}</span>
            </div>
          ))}
        </div>

        {/* Price Box */}
        <div className="inline-block bg-white/5 border border-white/10 rounded-2xl p-6 md:p-8 backdrop-blur-sm">
          <div className="flex items-center justify-center gap-4 mb-3">
            <span className="text-2xl text-gray-500 line-through">€97</span>
            <span className="text-5xl md:text-6xl font-extrabold text-[#FFD700]">€9</span>
            <span className="px-3 py-1 rounded-full bg-[#FFD700]/20 text-[#FFD700] text-sm font-bold">
              -90%
            </span>
          </div>
          <p className="text-sm text-gray-400 mb-5">
            Precio especial de lanzamiento. Sube pronto
          </p>
          <a
            href={stripeLink}
            className="inline-block w-full md:w-auto px-10 py-4 bg-[#FFD700] text-black font-bold text-lg rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02] active:scale-[0.98]"
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
