import logo from '@/assets/logo-ai-chef-pro.svg';

// `lang` (tienda EN, 2026-10-03): 'en' lleva el logo a /en. Sin la prop (el ES) es lo de siempre.
export default function TopBar({ lang = 'es' }: { lang?: 'es' | 'en' }) {
  return (
    <header className="sticky top-0 z-50 bg-white border-b border-gray-200 shadow-sm">
      <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
        <a href={lang === 'en' ? 'https://aichef.pro/en' : 'https://aichef.pro'} className="flex items-center gap-2">
          <img src={logo} alt="AI Chef Pro" className="h-8" />
        </a>
        <span className="px-3 py-1 bg-amber-100 border border-amber-300 text-amber-800 text-xs font-bold rounded-full tracking-wider uppercase">
          Pro Prompts Library
        </span>
      </div>
    </header>
  );
}
