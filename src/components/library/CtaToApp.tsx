import { ArrowRight } from 'lucide-react';

// `lang` (tienda EN, 2026-10-03): textos en inglés, nombres de agente de la plataforma EN
// (scripts/productos-digitales/pro-prompts-ebook-en/agentes_en.json) y home /en. Sin la prop (el ES)
// es lo de siempre.
const COPY = {
  es: {
    heading: '¿Quieres usar estos prompts con los 75+ agentes IA de AI Chef Pro?',
    text: 'La suite completa para toda la hostelería: chefs, gerentes, pasteleros, bartenders y dueños de negocio. Food Pairing AI, Mermas GenCal, Catering AI+ y mucho más.',
    href: 'https://aichef.pro',
    cta: 'Descubrir AI Chef Pro',
  },
  en: {
    heading: 'Want to use these prompts with the 70+ AI agents in AI Chef Pro?',
    text: 'The complete suite for all of hospitality: chefs, managers, pastry chefs, bartenders and business owners. Food Pairing AI, Waste GenCal, Catering AI+ and much more.',
    href: 'https://aichef.pro/en',
    cta: 'Discover AI Chef Pro',
  },
} as const;

export default function CtaToApp({ lang = 'es' }: { lang?: 'es' | 'en' }) {
  const t = COPY[lang === 'en' ? 'en' : 'es'];
  return (
    <section className="py-16 px-4">
      <div className="max-w-3xl mx-auto text-center bg-gradient-to-br from-white/5 to-white/[0.02] border border-white/10 rounded-2xl p-8 md:p-12">
        <h2 className="text-2xl md:text-3xl font-bold text-white mb-3">
          {t.heading}
        </h2>
        <p className="text-gray-400 leading-relaxed mb-6 max-w-xl mx-auto">
          {t.text}
        </p>
        <a
          href={t.href}
          className="inline-flex items-center gap-2 px-8 py-3.5 bg-[#FFD700] text-black font-bold rounded-xl hover:bg-[#FFD700]/90 transition-all hover:scale-[1.02]"
        >
          {t.cta}
          <ArrowRight className="w-5 h-5" />
        </a>
      </div>
    </section>
  );
}
