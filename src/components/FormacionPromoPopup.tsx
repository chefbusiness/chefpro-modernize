import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { GraduationCap, ChefHat, Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Checkbox } from '@/components/ui/checkbox';
import { Badge } from '@/components/ui/badge';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { useLanguage } from '@/hooks/useLanguage';
import formacionInhouse from '@/assets/formacion-inhouse.jpg';

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
      <DialogContent className="sm:max-w-lg border border-border/50 bg-gradient-to-br from-background via-background to-muted/30 p-0 overflow-hidden shadow-2xl">
        {/* Hero Image */}
        <div className="relative h-36 sm:h-44 overflow-hidden">
          <img 
            src={formacionInhouse} 
            alt="Formación In-House AI Chef Pro" 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/70 via-black/30 to-transparent" />
          
          {/* New Badge */}
          <Badge className="absolute top-3 left-3 bg-emerald-500 hover:bg-emerald-500 text-white border-0 shadow-lg">
            <Sparkles className="h-3 w-3 mr-1" />
            Nuevo
          </Badge>
          
          {/* Title overlay on image */}
          <div className="absolute bottom-3 left-4 right-4">
            <h3 className="text-white text-lg sm:text-xl font-bold drop-shadow-lg">
              Formaciones Presenciales
            </h3>
            <p className="text-white/90 text-sm">
              IA Gastronómica para tu organización
            </p>
          </div>
        </div>
        
        <div className="p-5 pt-4">
          <DialogHeader className="text-center space-y-3">
            {/* Attention message */}
            <div className="bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800 rounded-lg p-3">
              <p className="text-sm text-emerald-800 dark:text-emerald-200 font-medium leading-relaxed">
                <Sparkles className="inline h-4 w-4 mr-1.5 text-emerald-600" />
                Por fin, lo que durante más de un año nos habéis pedido...
                <span className="font-bold block mt-1">¡Ya está aquí!</span>
              </p>
            </div>

            <DialogTitle className="text-lg sm:text-xl font-bold text-foreground sr-only">
              Formaciones Presenciales en España
            </DialogTitle>
          </DialogHeader>

          <div className="mt-4 space-y-4">
            {/* Segmentation question */}
            <div className="bg-muted/50 backdrop-blur-sm rounded-xl p-4 border border-border/50">
              <p className="text-sm sm:text-base text-foreground text-center leading-relaxed">
                <span className="font-semibold">¿Diriges una escuela de cocina, grupo de restauración, hotel o centro gastronómico?</span>
              </p>
            </div>

            {/* Value proposition */}
            <p className="text-center text-sm text-muted-foreground">
              Llevo la revolución de la IA directamente a tu equipo con{' '}
              <span className="font-semibold text-foreground">programas personalizados desde 990€</span>
            </p>

            {/* Audience badges */}
            <div className="flex flex-wrap justify-center gap-2">
              {['Escuelas', 'Restaurantes', 'Hoteles', 'Catering'].map((badge) => (
                <span 
                  key={badge}
                  className="inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium bg-muted text-muted-foreground border border-border"
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
                className="w-full bg-slate-900 hover:bg-slate-800 dark:bg-slate-100 dark:hover:bg-slate-200 dark:text-slate-900 text-white font-semibold py-5 text-base shadow-lg hover:shadow-xl transition-all"
              >
                <GraduationCap className="mr-2 h-5 w-5" />
                Descubrir Formaciones
              </Button>
              
              <button
                onClick={handleDismiss}
                className="w-full text-sm text-muted-foreground hover:text-foreground transition-colors py-2"
              >
                Ahora no, gracias
              </button>
            </div>

            {/* Never show again checkbox */}
            <div className="flex items-center justify-center gap-2 pt-1">
              <Checkbox 
                id="never-show" 
                checked={neverShowAgain}
                onCheckedChange={(checked) => setNeverShowAgain(checked === true)}
                className="border-muted-foreground/30 data-[state=checked]:bg-emerald-600 data-[state=checked]:border-emerald-600"
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
