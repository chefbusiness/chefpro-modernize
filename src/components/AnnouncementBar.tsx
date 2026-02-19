import { useState } from 'react';
import { Sparkles, X } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

const AnnouncementBar = () => {
  const { t } = useLanguage();
  const [visible, setVisible] = useState(() => {
    return localStorage.getItem('announcement-dismissed') !== 'true';
  });

  const dismiss = () => {
    setVisible(false);
    localStorage.setItem('announcement-dismissed', 'true');
  };

  if (!visible) return null;

  return (
    <div className="bg-chef-dark text-background text-center text-xs sm:text-sm py-2 px-10 relative">
      <a
        href="https://blog.aichef.pro/30-hacks-con-inteligencia-artificial-de-ai-chef-pro-para-mejorar-la-eficiencia-en-tu-cocina/"
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
