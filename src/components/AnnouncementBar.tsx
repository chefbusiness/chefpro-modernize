import { useState } from 'react';
import { Sparkles, X } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

const AnnouncementBar = () => {
  const { t, currentLanguage } = useLanguage();
  const [visible, setVisible] = useState(() => {
    // Este initializer corre DURANTE el render, también en el pase SSR de los
    // islands de marketing (client:load desde 2026-08-01), donde no hay
    // localStorage. En servidor se pinta visible —es contenido, y así entra en
    // el HTML— y el cliente la oculta al hidratar si el usuario ya la cerró.
    if (typeof localStorage === 'undefined') return true;
    return localStorage.getItem('announcement-dismissed') !== 'true';
  });

  const dismiss = () => {
    setVisible(false);
    localStorage.setItem('announcement-dismissed', 'true');
  };

  if (!visible) return null;

  // Gemelo de la barra de astro-site/src/components/Header.astro: MISMO destino
  // por idioma y mismo copy (announcement_bar.* de los locales). Si tocas uno,
  // toca el otro. Desde 8B.6 el inglés tiene blog propio al que enviar el clic;
  // los demás idiomas siguen cayendo en el post ES porque no hay alternativa.
  const href =
    currentLanguage === 'es'
      ? '/pro-prompts-ebook'
      : currentLanguage === 'en'
        ? '/en/blog/best-ai-tools-for-chefs-2026'
        : '/blog/30-hacks-con-inteligencia-artificial-de-ai-chef-pro-para-mejorar-la-eficiencia-en-tu-cocina';

  return (
    <div className="bg-chef-dark text-background text-center text-xs sm:text-sm py-2 px-10 relative">
      <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-2 hover:text-accent transition-colors"
      >
        <Sparkles className="h-3.5 w-3.5 text-accent flex-shrink-0" />
        <span className="hidden sm:inline">{t('announcement_bar.text')}</span>
        <span className="sm:hidden">{t('announcement_bar.text_short')}</span>
        <span className="font-semibold text-accent whitespace-nowrap">
          {t('announcement_bar.cta')} →
        </span>
      </a>
      <button
        onClick={dismiss}
        className="absolute right-2 top-1/2 -translate-y-1/2 text-background/60 hover:text-background transition-colors p-1"
        aria-label="Close"
      >
        <X className="h-3.5 w-3.5" />
      </button>
    </div>
  );
};

export default AnnouncementBar;
