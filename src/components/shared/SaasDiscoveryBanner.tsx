import { ArrowRight, Sparkles } from 'lucide-react';

/**
 * Compact top banner for digital product pages.
 * Helps visitors understand that aichef.pro is a SaaS platform,
 * not just downloadable products.
 *
 * `lang` (2026-09-24, tienda internacional): 'en' para los dashboards de la tienda EN. Sin la
 * prop (los 50 dashboards ES) los textos y enlaces son exactamente los de antes. Los textos EN
 * son los mismos del banner de la plantilla de landing (astro-site/src/i18n/tienda/en.json).
 */
const COPY = {
  es: {
    home: '/',
    pre: 'Estos productos digitales complementan ',
    post: ' — el SaaS de IA para hostelería con +55 aplicaciones',
    postMobile: ' — SaaS de IA para hostelería',
    cta: 'Descubrir',
  },
  en: {
    home: '/en',
    pre: 'These digital products pair with ',
    post: ' — the AI platform for hospitality with 55+ tools',
    postMobile: ' — AI platform for hospitality',
    cta: 'Explore',
  },
} as const;

export default function SaasDiscoveryBanner({ lang = 'es' }: { lang?: 'es' | 'en' }) {
  const t = COPY[lang === 'en' ? 'en' : 'es'];
  return (
    <div className="bg-gradient-to-r from-[#FFD700]/10 via-[#FFD700]/5 to-[#FFD700]/10 border-b border-[#FFD700]/20">
      <div className="max-w-6xl mx-auto px-4 py-2.5 flex items-center justify-center gap-2 sm:gap-3 text-center">
        <Sparkles className="h-3.5 w-3.5 text-[#FFD700] flex-shrink-0 hidden sm:block" />
        <p className="text-xs sm:text-sm text-gray-300">
          <span className="hidden sm:inline">{t.pre}</span>
          <a
            href={t.home}
            className="font-semibold text-[#FFD700] hover:text-[#FFD700]/80 transition-colors"
          >
            AI Chef Pro
          </a>
          <span className="hidden sm:inline">{t.post}</span>
          <span className="sm:hidden">{t.postMobile}</span>
        </p>
        <a
          href={t.home}
          className="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-[#FFD700]/15 border border-[#FFD700]/30 text-[#FFD700] text-xs font-semibold hover:bg-[#FFD700]/25 transition-colors whitespace-nowrap flex-shrink-0"
        >
          {t.cta}
          <ArrowRight className="h-3 w-3" />
        </a>
      </div>
    </div>
  );
}
