import { ArrowRight } from 'lucide-react';
import FadeIn from './FadeIn';

export default function TryPlatformBanner() {
  return (
    <section className="py-16 md:py-24 px-4">
      <FadeIn>
        <div className="max-w-4xl mx-auto text-center">
          <p className="text-gray-400 text-sm tracking-[0.2em] uppercase mb-4">
            ¿Aún no conoces la plataforma?
          </p>

          <h2 className="text-3xl md:text-5xl lg:text-6xl font-extrabold text-white mb-3 leading-tight">
            Prueba AI Chef Pro{' '}
            <span className="text-[#FFD700]">Gratis</span>
          </h2>

          <p className="text-gray-400 text-lg md:text-xl max-w-2xl mx-auto mb-4">
            La suite de IA más completa para hostelería y restauración.
            Disponible en 7 idiomas.
          </p>

          {/* Language pills */}
          <div className="flex flex-wrap justify-center gap-2 mb-10">
            {['Español', 'English', 'Français', 'Deutsch', 'Italiano', 'Português', 'Nederlands'].map((lang) => (
              <span
                key={lang}
                className="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-gray-400 text-xs font-medium"
              >
                {lang}
              </span>
            ))}
          </div>

          <a
            href="https://aichef.pro"
            className="inline-flex items-center gap-2 px-8 py-4 rounded-xl border-2 border-[#FFD700] text-[#FFD700] font-bold text-lg hover:bg-[#FFD700] hover:text-black transition-all hover:scale-[1.02] active:scale-[0.98]"
          >
            Descubre AI Chef Pro
            <ArrowRight className="w-5 h-5" />
          </a>
        </div>
      </FadeIn>
    </section>
  );
}
