import { useState, useEffect, useRef } from 'react';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ChevronLeft, ChevronRight, Play, Pause } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

export default function ScreenshotGallery() {
  const { t, getAppUrl, currentLanguage } = useLanguage();
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAutoRotating, setIsAutoRotating] = useState(true);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  const screenshots = [
    {
      id: 1,
      titleKey: 'cocina_creativa',
      descKey: 'cocina_creativa',
      image: '/lovable-uploads/12abdf30-3381-42de-a8f1-2abe9342145f.png',
      categoryKey: 'creatividad'
    },
    {
      id: 2,
      titleKey: 'platos_autor',
      descKey: 'platos_autor',
      image: '/lovable-uploads/5863854b-f30c-47d7-89f0-6124f57cfacf.png',
      categoryKey: 'creatividad'
    },
    {
      id: 3,
      titleKey: 'catering_ai',
      descKey: 'catering_ai',
      image: '/lovable-uploads/975877a4-27f4-4215-9f8a-63882f278540.png',
      categoryKey: 'conceptos'
    },
    {
      id: 4,
      titleKey: 'food_pairing',
      descKey: 'food_pairing',
      image: '/lovable-uploads/c01838d8-9dd4-430c-a4d8-98359573a299.png',
      categoryKey: 'creatividad'
    },
    {
      id: 5,
      titleKey: 'pasteleria_creativa',
      descKey: 'pasteleria_creativa',
      image: '/lovable-uploads/f2d20b90-077c-4486-a944-1c6c7fdc570e.png',
      categoryKey: 'creatividad'
    },
    {
      id: 6,
      titleKey: 'sosa_ingredients',
      descKey: 'sosa_ingredients',
      image: '/lovable-uploads/ed9e5325-4d1f-44fb-9643-e01fa3de208c.png',
      categoryKey: 'proveedores'
    },
    {
      id: 7,
      titleKey: 'casual_restaurants',
      descKey: 'casual_restaurants',
      image: '/lovable-uploads/4a01fa26-97e9-40ce-9cf6-d17c71b10abd.png',
      categoryKey: 'conceptos'
    },
    {
      id: 8,
      titleKey: 'menu_local_seo',
      descKey: 'menu_local_seo',
      image: '/lovable-uploads/6cfe3941-1762-441d-b87b-5bd37a8a3667.png',
      categoryKey: 'marketing'
    },
    {
      id: 9,
      titleKey: 'cocina_peruana',
      descKey: 'cocina_peruana',
      image: '/lovable-uploads/a1eb6b5e-e0c6-47e2-88d5-7a8247807000.png',
      categoryKey: 'recetarios'
    },
    {
      id: 10,
      titleKey: 'cocina_francesa',
      descKey: 'cocina_francesa',
      image: '/lovable-uploads/26949727-8432-41b4-8f59-8cc40151efa4.png',
      categoryKey: 'recetarios'
    },
    {
      id: 11,
      titleKey: 'fermentus',
      descKey: 'fermentus',
      image: '/lovable-uploads/64a2d776-3e86-49cc-bdc7-9df927d3624a.png',
      categoryKey: 'creatividad'
    },
    {
      id: 12,
      titleKey: 'cocina_india',
      descKey: 'cocina_india',
      image: '/lovable-uploads/c7595f12-a770-4c58-939f-69a9c3c8a1f8.png',
      categoryKey: 'recetarios'
    }
  ];

  const nextSlide = () => {
    if (isTransitioning) return;
    setIsTransitioning(true);
    setCurrentIndex((prev) => (prev + 1) % screenshots.length);
    setTimeout(() => setIsTransitioning(false), 300);
  };

  const prevSlide = () => {
    if (isTransitioning) return;
    setIsAutoRotating(false);
    setIsTransitioning(true);
    setCurrentIndex((prev) => (prev - 1 + screenshots.length) % screenshots.length);
    setTimeout(() => setIsTransitioning(false), 300);
  };

  const goToSlide = (index: number) => {
    if (isTransitioning || index === currentIndex) return;
    setIsAutoRotating(false);
    setIsTransitioning(true);
    setCurrentIndex(index);
    setTimeout(() => setIsTransitioning(false), 300);
  };

  const toggleAutoRotation = () => {
    setIsAutoRotating(!isAutoRotating);
  };

  // Auto-rotation effect
  useEffect(() => {
    // Clear existing interval
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }

    if (!isAutoRotating) return;
    
    intervalRef.current = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % screenshots.length);
    }, 4000);

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [isAutoRotating, screenshots.length]);

  const currentScreenshot = screenshots[currentIndex];

  return (
    <section className="container mx-auto px-4 py-8 md:py-12">
      <div className="text-center mb-8">
        <Badge variant="outline" className="mb-4">
          {t('gallery.badge')}
        </Badge>
        <h2 className="text-2xl md:text-3xl lg:text-4xl font-bold mb-4">
          {t('gallery.title')}
        </h2>
        <p className="text-muted-foreground max-w-2xl mx-auto">
          {t('gallery.description')}
        </p>
      </div>

      <div className="max-w-6xl mx-auto">
        {/* Screenshot Display */}
        <div className="relative rounded-xl overflow-hidden shadow-2xl hover:shadow-3xl transition-shadow duration-300 bg-white">
          <img
            src={currentScreenshot.image}
            alt={t(`screenshots.${currentScreenshot.titleKey}.title`)}
            className={`w-full h-auto object-contain transition-opacity duration-300 ${
              isTransitioning ? 'opacity-50' : 'opacity-100'
            }`}
            onError={(e) => {
              // Fallback to placeholder if image fails to load
              const target = e.target as HTMLImageElement;
              target.src = `data:image/svg+xml;base64,${btoa(`
                <svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">
                  <rect width="100%" height="100%" fill="#f3f4f6"/>
                  <text x="50%" y="50%" text-anchor="middle" font-family="Arial" font-size="24" fill="#6b7280">
                    ${t(`screenshots.${currentScreenshot.titleKey}.title`)}
                  </text>
                </svg>
              `)}`;
            }}
          />
          {/* Auto-rotation indicator */}
          {isAutoRotating && (
            <div className="absolute top-4 right-4">
              <div className="flex items-center gap-2 bg-black/20 backdrop-blur-sm rounded-full px-3 py-1">
                <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                <span className="text-white text-xs font-medium">Auto</span>
              </div>
            </div>
          )}
        </div>

        {/* App Info Below Image */}
        <div className="text-center mt-6 space-y-3">
          <Badge variant="secondary">
            {t(`categories_labels.${currentScreenshot.categoryKey}`)}
          </Badge>
          <h3 className="text-2xl font-bold">
            {t(`screenshots.${currentScreenshot.titleKey}.title`)}
          </h3>
          <p className="text-muted-foreground max-w-2xl mx-auto">
            {t(`screenshots.${currentScreenshot.descKey}.description`)}
          </p>
        </div>

        {/* Navigation Controls */}
        <div className="flex flex-col md:flex-row items-center justify-center md:justify-between mt-6 gap-4">
          {/* Mobile: Top row with Previous/Next buttons */}
          <div className="flex items-center justify-between w-full md:w-auto md:contents">
            <Button
              variant="outline"
              size="sm"
              onClick={prevSlide}
              className="flex items-center gap-2"
              disabled={isTransitioning}
            >
              <ChevronLeft className="w-4 h-4" />
              <span className="hidden sm:inline">{t('gallery.previous')}</span>
            </Button>

            <Button
              variant="outline"
              size="sm"
              onClick={nextSlide}
              className="flex items-center gap-2 md:order-3"
              disabled={isTransitioning}
            >
              <span className="hidden sm:inline">{t('gallery.next')}</span>
              <ChevronRight className="w-4 h-4" />
            </Button>
          </div>

          {/* Center Controls: Dots + Play/Pause */}
          <div className="flex items-center space-x-4 md:order-2">
            {/* Auto-rotation toggle */}
            <Button
              variant="ghost"
              size="sm"
              onClick={toggleAutoRotation}
              className="flex items-center gap-2"
            >
              {isAutoRotating ? (
                <Pause className="w-4 h-4" />
              ) : (
                <Play className="w-4 h-4" />
              )}
            </Button>

            {/* Dots Indicator */}
            <div className="flex flex-wrap justify-center space-x-1 md:space-x-2 max-w-[70vw] md:max-w-none">
              {screenshots.map((_, index) => (
                <button
                  key={index}
                  onClick={() => goToSlide(index)}
                  disabled={isTransitioning}
                  className={`w-2 h-2 md:w-3 md:h-3 rounded-full transition-all duration-300 hover:scale-110 ${
                    index === currentIndex 
                      ? 'bg-primary scale-110' 
                      : 'bg-muted-foreground/30 hover:bg-muted-foreground/50'
                  }`}
                />
              ))}
            </div>
          </div>
        </div>

        {/* App Counter */}
        <div className="text-center mt-8">
          <p className="text-muted-foreground">
            {t('gallery.counter', { 
              current: currentIndex + 1, 
              total: screenshots.length 
            })}
          </p>
          <Button 
            size="lg" 
            className="btn-gold mt-4"
            onClick={() => window.open(getAppUrl(currentLanguage), '_blank')}
          >
            {t('gallery.explore_all')}
          </Button>
        </div>
      </div>
    </section>
  );
}