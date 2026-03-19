import { Check, Star } from 'lucide-react';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import PaymentBadges from './PaymentBadges';

import avatar1 from '@/assets/avatars/avatar-1.jpg';
import avatar2 from '@/assets/avatars/avatar-2.jpg';
import avatar3 from '@/assets/avatars/avatar-3.jpg';
import avatar4 from '@/assets/avatars/avatar-4.jpg';
import avatar5 from '@/assets/avatars/avatar-5.jpg';
import avatar6 from '@/assets/avatars/avatar-6.jpg';
import avatar7 from '@/assets/avatars/avatar-7.jpg';
import avatar8 from '@/assets/avatars/avatar-8.jpg';

const avatars = [avatar1, avatar2, avatar3, avatar4, avatar5, avatar6, avatar7, avatar8];
const stripeLink = import.meta.env.VITE_STRIPE_PAYMENT_LINK || '#comprar';

const checkItems = [
  'eBook PDF + Dashboard exclusivo con todos los prompts',
  'Más de 300 prompts para toda la hostelería y restauración',
  '8 herramientas gratuitas profesionales incluidas',
  'Compatible con ChatGPT, Claude, Perplexity, DeepSeek y más',
  'Actualizaciones gratuitas de por vida',
];

const heroImages = [
  '/lovable-uploads/ai-gallery/tataki-presa-iberica-chimichurri.jpeg',
  '/lovable-uploads/ai-gallery/tartaleta-de-yuzu-y-merengue.jpeg',
  '/lovable-uploads/ai-gallery/cocktail-green-margarita.jpeg',
  '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg',
  '/lovable-uploads/ai-gallery/croissant-bicolor-de-mantequilla-aichefpro.jpeg',
  '/lovable-uploads/ai-gallery/huevo-baja-temperatura-trufa.jpeg',
];

export default function HeroSection() {
  return (
    <section className="relative px-4 pt-8 pb-16 md:pt-12 md:pb-24 overflow-hidden">
      {/* Food image mosaic background */}
      <div className="absolute inset-0 opacity-[0.12]">
        <div className="grid grid-cols-3 md:grid-cols-6 h-full gap-1">
          {heroImages.map((src, i) => (
            <div key={i} className="overflow-hidden">
              <img
                src={src}
                alt=""
                className="w-full h-full object-cover scale-110"
                loading="eager"
              />
            </div>
          ))}
        </div>
      </div>
      {/* Gradient overlays */}
      <div className="absolute inset-0 bg-gradient-to-b from-[#0a0a0a] via-[#0a0a0a]/80 to-[#0a0a0a]" />
      <div className="absolute inset-0 bg-radial-gradient" style={{
        background: 'radial-gradient(ellipse 80% 60% at 50% -10%, rgba(255,215,0,0.1) 0%, transparent 70%)',
      }} />

      <div className="relative max-w-4xl mx-auto text-center z-10">
        {/* Avatars + Stars */}
        <div className="flex flex-col items-center gap-2 mb-6">
          <div className="flex -space-x-3 justify-center">
            {avatars.map((avatar, i) => (
              <Avatar
                key={i}
                className="border-2 border-[#0a0a0a] w-9 h-9 sm:w-10 sm:h-10 ring-2 ring-[#0a0a0a]"
              >
                <AvatarImage src={avatar} alt={`Professional ${i + 1}`} />
                <AvatarFallback className="bg-gray-800 text-xs text-gray-400">P{i + 1}</AvatarFallback>
              </Avatar>
            ))}
          </div>
          <div className="flex items-center gap-0.5">
            {Array.from({ length: 5 }).map((_, i) => (
              <Star
                key={i}
                className={`h-4 w-4 ${i < 4 ? 'fill-[#FFD700] text-[#FFD700]' : 'fill-[#FFD700]/40 text-[#FFD700]/40'}`}
              />
            ))}
          </div>
        </div>

        {/* Badge */}
        <span className="inline-block mb-6 px-4 py-1.5 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 text-[#FFD700] text-sm font-medium animate-fade-in">
          El recurso #1 de prompts para hostelería y restauración
        </span>

        {/* H1 */}
        <h1 className="text-3xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
          El Único{' '}
          <span className="text-[#FFD700]">eBook de Prompts</span>{' '}
          de IA para Hostelería que Realmente Necesitas
        </h1>

        {/* Subtitle */}
        <p className="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto mb-10 leading-relaxed">
          Más de 300 prompts de inteligencia artificial para chefs, gerentes, pasteleros, bartenders, chocolateros, catering y dueños de restaurante. Prompts listos para usar en ChatGPT, Claude, Gemini, Perplexity y AI Chef Pro. La guía definitiva de IA para hostelería y restauración.
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
        <div className="inline-block bg-white/5 border border-[#FFD700]/20 rounded-2xl p-6 md:p-8 backdrop-blur-sm">
          <div className="flex items-center justify-center gap-4 mb-3">
            <span className="text-2xl text-gray-500 line-through">€50</span>
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
          <PaymentBadges className="mt-4" />
        </div>
      </div>
    </section>
  );
}
