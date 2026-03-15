import { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Sparkles } from 'lucide-react';
import { Checkbox } from '@/components/ui/checkbox';
import {
  Dialog,
  DialogContent,
} from '@/components/ui/dialog';
import { useLanguage } from '@/hooks/useLanguage';

const STORAGE_KEY_DISMISSED = 'ebook-promo-dismissed';
const STORAGE_KEY_NEVER_SHOW = 'ebook-promo-never-show';
const DISMISS_DURATION_HOURS = 24;
const POPUP_DELAY_MS = 12000;

const EbookPromoPopup = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [neverShowAgain, setNeverShowAgain] = useState(false);
  const { currentLanguage } = useLanguage();
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    // Only show for Spanish users
    if (currentLanguage !== 'es') return;

    // Don't show on ebook-related pages
    if (location.pathname.includes('pro-prompts')) return;

    // Check if user opted out permanently
    if (localStorage.getItem(STORAGE_KEY_NEVER_SHOW) === 'true') return;

    // Check if dismissed recently
    const dismissedTimestamp = localStorage.getItem(STORAGE_KEY_DISMISSED);
    if (dismissedTimestamp) {
      const hoursSince = (Date.now() - parseInt(dismissedTimestamp, 10)) / (1000 * 60 * 60);
      if (hoursSince < DISMISS_DURATION_HOURS) return;
    }

    const timer = setTimeout(() => setIsVisible(true), POPUP_DELAY_MS);
    return () => clearTimeout(timer);
  }, [currentLanguage, location.pathname]);

  const handleDismiss = () => {
    if (neverShowAgain) {
      localStorage.setItem(STORAGE_KEY_NEVER_SHOW, 'true');
    } else {
      localStorage.setItem(STORAGE_KEY_DISMISSED, Date.now().toString());
    }
    setIsVisible(false);
  };

  const handleCTAClick = () => {
    localStorage.setItem(STORAGE_KEY_NEVER_SHOW, 'true');
    setIsVisible(false);
    navigate('/pro-prompts-ebook');
  };

  if (currentLanguage !== 'es') return null;

  return (
    <Dialog open={isVisible} onOpenChange={(open) => !open && handleDismiss()}>
      <DialogContent className="sm:max-w-md border-0 bg-[#0a0a0a] p-0 overflow-hidden shadow-2xl shadow-[#FFD700]/10">
        {/* Mockup Image */}
        <div className="px-4 pt-6">
          <img
            src="/ebook-mockup-bundle.png"
            alt="Gastro Pro Prompts — eBook de IA para hostelería"
            className="w-full"
          />
        </div>

        <div className="px-6 pb-6 pt-2 text-center">
          {/* Badge */}
          <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-[#FFD700]/10 border border-[#FFD700]/30 mb-3">
            <Sparkles className="h-3.5 w-3.5 text-[#FFD700]" />
            <span className="text-[#FFD700] text-xs font-bold tracking-wider uppercase">Nuevo</span>
          </div>

          <h3 className="text-white text-xl font-bold mb-2">
            Gastro Pro Prompts
          </h3>
          <p className="text-gray-400 text-sm mb-1">
            300+ prompts de IA profesionales para hostelería y restauración
          </p>
          <p className="text-gray-500 text-xs mb-5">
            Compatible con ChatGPT, Claude, Perplexity, Gemini y más
          </p>

          {/* Price */}
          <div className="flex items-center justify-center gap-3 mb-5">
            <span className="text-gray-500 line-through text-lg">€50</span>
            <span className="text-[#FFD700] text-3xl font-extrabold">€9</span>
            <span className="px-2 py-0.5 rounded-full bg-[#FFD700]/20 text-[#FFD700] text-xs font-bold">-82%</span>
          </div>

          {/* CTA */}
          <button
            onClick={handleCTAClick}
            className="w-full py-3.5 bg-[#FFD700] text-black font-bold text-base rounded-xl hover:bg-[#FFD700]/90 transition-all active:scale-[0.98]"
          >
            VER EL EBOOK — €9
          </button>

          <button
            onClick={handleDismiss}
            className="w-full text-sm text-gray-500 hover:text-gray-300 transition-colors py-3 mt-1"
          >
            Ahora no, gracias
          </button>

          {/* Never show again */}
          <div className="flex items-center justify-center gap-2 pt-1">
            <Checkbox
              id="never-show-ebook"
              checked={neverShowAgain}
              onCheckedChange={(checked) => setNeverShowAgain(checked === true)}
              className="border-gray-600 data-[state=checked]:bg-[#FFD700] data-[state=checked]:border-[#FFD700] data-[state=checked]:text-black"
            />
            <label htmlFor="never-show-ebook" className="text-xs text-gray-600 cursor-pointer">
              No volver a mostrar
            </label>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default EbookPromoPopup;
