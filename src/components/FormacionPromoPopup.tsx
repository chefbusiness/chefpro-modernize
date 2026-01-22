import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { GraduationCap, Building2, ChefHat, Hotel } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { useLanguage } from '@/hooks/useLanguage';

const STORAGE_KEY_DISMISSED = 'formacion-promo-dismissed';
const STORAGE_KEY_NEVER_SHOW = 'formacion-promo-never-show';
const STORAGE_KEY_VISITED = 'has-visited-formacion';
const DISMISS_DURATION_DAYS = 7;
const POPUP_DELAY_MS = 10000; // 10 seconds

const FormacionPromoPopup = () => {
  const [isVisible, setIsVisible] = useState(false);
  const [neverShowAgain, setNeverShowAgain] = useState(false);
  const { currentLanguage } = useLanguage();
  const navigate = useNavigate();

  useEffect(() => {
    // Only show for Spanish users
    if (currentLanguage !== 'es') return;

    // Check if user opted out permanently
    const neverShow = localStorage.getItem(STORAGE_KEY_NEVER_SHOW);
    if (neverShow === 'true') return;

    // Check if user already visited the formacion page
    const hasVisited = localStorage.getItem(STORAGE_KEY_VISITED);
    if (hasVisited === 'true') return;

    // Check if dismissed recently (within 7 days)
    const dismissedTimestamp = localStorage.getItem(STORAGE_KEY_DISMISSED);
    if (dismissedTimestamp) {
      const dismissedDate = parseInt(dismissedTimestamp, 10);
      const daysSinceDismissed = (Date.now() - dismissedDate) / (1000 * 60 * 60 * 24);
      if (daysSinceDismissed < DISMISS_DURATION_DAYS) return;
    }

    // Show popup after delay
    const timer = setTimeout(() => {
      setIsVisible(true);
    }, POPUP_DELAY_MS);

    return () => clearTimeout(timer);
  }, [currentLanguage]);

  const handleDismiss = () => {
    if (neverShowAgain) {
      localStorage.setItem(STORAGE_KEY_NEVER_SHOW, 'true');
    } else {
      localStorage.setItem(STORAGE_KEY_DISMISSED, Date.now().toString());
    }
    setIsVisible(false);
  };

  const handleCTAClick = () => {
    // Mark as visited so we don't show again
    localStorage.setItem(STORAGE_KEY_VISITED, 'true');
    setIsVisible(false);
    navigate('/formacion-presencial');
  };

  // Don't render for non-Spanish users
  if (currentLanguage !== 'es') return null;

  return (
    <Dialog open={isVisible} onOpenChange={(open) => !open && handleDismiss()}>
      <DialogContent className="sm:max-w-md border-0 bg-gradient-to-br from-amber-50 via-orange-50 to-amber-100 p-0 overflow-hidden">
        {/* Decorative top bar */}
        <div className="h-2 bg-gradient-to-r from-amber-500 via-orange-500 to-amber-600" />
        
        <div className="p-6 pt-4">
          <DialogHeader className="text-center space-y-4">
            {/* Icon cluster */}
            <div className="flex justify-center gap-2 mb-2">
              <div className="p-2 bg-amber-100 rounded-full">
                <Building2 className="h-5 w-5 text-amber-600" />
              </div>
              <div className="p-3 bg-gradient-to-br from-amber-500 to-orange-500 rounded-full shadow-lg">
                <GraduationCap className="h-7 w-7 text-white" />
              </div>
              <div className="p-2 bg-amber-100 rounded-full">
                <Hotel className="h-5 w-5 text-amber-600" />
              </div>
            </div>

            <DialogTitle className="text-xl sm:text-2xl font-bold bg-gradient-to-r from-amber-700 to-orange-600 bg-clip-text text-transparent">
              IA Gastronómica para tu Organización
            </DialogTitle>
            
            <p className="text-sm text-amber-700 font-medium">
              Formación presencial e in-house en España
            </p>
          </DialogHeader>

          <div className="mt-6 space-y-4">
            {/* Segmentation question */}
            <div className="bg-white/60 backdrop-blur-sm rounded-xl p-4 border border-amber-200/50">
              <p className="text-sm sm:text-base text-foreground text-center leading-relaxed">
                <span className="font-semibold text-amber-800">¿Diriges una escuela de cocina, grupo de restauración, hotel o centro gastronómico?</span>
              </p>
            </div>

            {/* Value proposition */}
            <p className="text-center text-sm text-muted-foreground">
              Llevo la revolución de la IA directamente a tu equipo con{' '}
              <span className="font-semibold text-amber-700">programas personalizados desde 990€</span>
            </p>

            {/* Audience badges */}
            <div className="flex flex-wrap justify-center gap-2">
              {['Escuelas', 'Restaurantes', 'Hoteles', 'Catering'].map((badge) => (
                <span 
                  key={badge}
                  className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-amber-100 text-amber-700 border border-amber-200"
                >
                  <ChefHat className="h-3 w-3 mr-1" />
                  {badge}
                </span>
              ))}
            </div>

            {/* CTA Buttons */}
            <div className="space-y-3 pt-2">
              <Button 
                onClick={handleCTAClick}
                className="w-full bg-gradient-to-r from-amber-500 to-orange-500 hover:from-amber-600 hover:to-orange-600 text-white font-semibold py-5 text-base shadow-lg hover:shadow-xl transition-all"
              >
                <GraduationCap className="mr-2 h-5 w-5" />
                Descubrir Servicios de Formación
              </Button>
              
              <button
                onClick={handleDismiss}
                className="w-full text-sm text-muted-foreground hover:text-foreground transition-colors py-2"
              >
                Ahora no, gracias
              </button>
            </div>

            {/* Never show again checkbox */}
            <div className="flex items-center justify-center gap-2 pt-2">
              <Checkbox 
                id="never-show" 
                checked={neverShowAgain}
                onCheckedChange={(checked) => setNeverShowAgain(checked === true)}
                className="border-amber-300 data-[state=checked]:bg-amber-500 data-[state=checked]:border-amber-500"
              />
              <label 
                htmlFor="never-show" 
                className="text-xs text-muted-foreground cursor-pointer"
              >
                No volver a mostrar
              </label>
            </div>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default FormacionPromoPopup;
