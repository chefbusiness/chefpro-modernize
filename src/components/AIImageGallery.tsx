import { useState, useEffect, useCallback } from 'react';
import { ChevronLeft, ChevronRight, Sparkles } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import useEmblaCarousel from 'embla-carousel-react';
import { useLanguage } from '@/hooks/useLanguage';

type AIModel = 'nano_banana' | 'seedream' | 'ideogram';

interface GalleryImage {
  id: number;
  src: string;
  model: AIModel;
}

const AIImageGallery = () => {
  const { t } = useLanguage();
  const [selectedIndex, setSelectedIndex] = useState(0);
  const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true, duration: 30 });

  const images: GalleryImage[] = [
    { id: 1, src: '/lovable-uploads/ai-gallery/torrija-caramelizada-con-helado.jpeg', model: 'nano_banana' },
    { id: 2, src: '/lovable-uploads/ai-gallery/innovacion-diseno-restaurantes-3.jpeg', model: 'nano_banana' },
    { id: 3, src: '/lovable-uploads/ai-gallery/tataki-presa-iberica-chimichurri.jpeg', model: 'nano_banana' },
    { id: 4, src: '/lovable-uploads/ai-gallery/gambas-al-ajillo.jpeg', model: 'nano_banana' },
    { id: 5, src: '/lovable-uploads/ai-gallery/ostra-aire-gintonic.jpeg', model: 'nano_banana' },
    { id: 6, src: '/lovable-uploads/ai-gallery/cochinillo-asado.jpeg', model: 'seedream' },
    { id: 7, src: '/lovable-uploads/ai-gallery/canelon-aguacate-cangrejo.jpeg', model: 'seedream' },
    { id: 8, src: '/lovable-uploads/ai-gallery/huevo-baja-temperatura-trufa.jpeg', model: 'seedream' },
    { id: 9, src: '/lovable-uploads/ai-gallery/croqueta-jamon.jpeg', model: 'seedream' },
    { id: 10, src: '/lovable-uploads/ai-gallery/falso-risotto-semillas-plancton.jpeg', model: 'seedream' },
    { id: 11, src: '/lovable-uploads/ai-gallery/innovacion-diseno-restaurantes-2.jpeg', model: 'ideogram' },
    { id: 12, src: '/lovable-uploads/ai-gallery/carpaccio-gambas.jpeg', model: 'ideogram' },
    { id: 13, src: '/lovable-uploads/ai-gallery/gazpacho-clasico.jpeg', model: 'ideogram' },
    { id: 14, src: '/lovable-uploads/ai-gallery/aceitunas-liquidas.jpeg', model: 'ideogram' },
    { id: 15, src: '/lovable-uploads/ai-gallery/cocktail-gin-game.jpeg', model: 'nano_banana' },
    { id: 16, src: '/lovable-uploads/ai-gallery/cocktail-green-margarita.jpeg', model: 'seedream' },
    { id: 17, src: '/lovable-uploads/ai-gallery/cocktail-super-fashion.jpeg', model: 'ideogram' },
    { id: 18, src: '/lovable-uploads/ai-gallery/cocktail-tepache-pina-asada.jpeg', model: 'nano_banana' },
    { id: 19, src: '/lovable-uploads/ai-gallery/cocktail-garibaldi-fermentado.jpeg', model: 'seedream' },
  ];

  const scrollPrev = useCallback(() => {
    if (emblaApi) emblaApi.scrollPrev();
  }, [emblaApi]);

  const scrollNext = useCallback(() => {
    if (emblaApi) emblaApi.scrollNext();
  }, [emblaApi]);

  const onSelect = useCallback(() => {
    if (!emblaApi) return;
    setSelectedIndex(emblaApi.selectedScrollSnap());
  }, [emblaApi]);

  useEffect(() => {
    if (!emblaApi) return;
    onSelect();
    emblaApi.on('select', onSelect);
    emblaApi.on('reInit', onSelect);
  }, [emblaApi, onSelect]);

  // Auto-play
  useEffect(() => {
    if (!emblaApi) return;
    const autoplay = setInterval(() => {
      emblaApi.scrollNext();
    }, 5000);
    return () => clearInterval(autoplay);
  }, [emblaApi]);

  const getModelBadge = (model: AIModel) => {
    const badges = {
      nano_banana: { label: t('ai_gallery.models.nano_banana'), variant: 'default' as const, className: 'bg-amber-500/20 text-amber-400 border-amber-500/30' },
      seedream: { label: t('ai_gallery.models.seedream'), variant: 'default' as const, className: 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30' },
      ideogram: { label: t('ai_gallery.models.ideogram'), variant: 'default' as const, className: 'bg-purple-500/20 text-purple-400 border-purple-500/30' },
    };
    return badges[model];
  };

  const currentImage = images[selectedIndex];

  return (
    <section className="relative py-24 overflow-hidden bg-gradient-to-b from-slate-900 via-slate-800 to-slate-900">
      <div className="container px-4 mx-auto">
        {/* Header */}
        <div className="max-w-3xl mx-auto text-center mb-16 animate-fade-in">
          <Badge variant="outline" className="mb-4 text-amber-400 border-amber-500/30 bg-amber-500/10">
            <Sparkles className="w-3 h-3 mr-1" />
            {t('ai_gallery.badge')}
          </Badge>
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-white">
            {t('ai_gallery.title')}
          </h2>
          <p className="text-lg text-slate-300 mb-8">
            {t('ai_gallery.description')}
          </p>

          {/* Model Badges */}
          <div className="flex flex-wrap justify-center gap-3 mb-8">
            {(['nano_banana', 'seedream', 'ideogram'] as AIModel[]).map((model) => {
              const badge = getModelBadge(model);
              return (
                <Badge key={model} variant={badge.variant} className={badge.className}>
                  {badge.label}
                </Badge>
              );
            })}
          </div>
        </div>

        {/* Carousel */}
        <div className="relative max-w-6xl mx-auto">
          <div className="overflow-hidden" ref={emblaRef}>
            <div className="flex">
              {images.map((image) => (
                <div key={image.id} className="flex-[0_0_100%] min-w-0 px-4">
                  <div className="relative group">
                    <div className="relative aspect-[2/3] md:aspect-[16/10] rounded-2xl overflow-hidden bg-slate-800/50 backdrop-blur-sm border border-slate-700/50">
                      <img
                        src={image.src}
                        alt={t(`ai_gallery.images.image_${image.id}.title`)}
                        className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/20 to-transparent" />
                      
                      {/* Content Overlay */}
                      <div className="absolute bottom-0 left-0 right-0 p-4 md:p-8 text-white">
                        <div className="mb-2 md:mb-3">
                          <Badge variant="outline" className={`${getModelBadge(image.model).className} text-xs md:text-sm`}>
                            {t('ai_gallery.generated_with')} {getModelBadge(image.model).label}
                          </Badge>
                        </div>
                        <h3 className="text-xl md:text-2xl lg:text-3xl font-bold mb-2">
                          {t(`ai_gallery.images.image_${image.id}.title`)}
                        </h3>
                        <p className="text-slate-300 text-xs md:text-sm lg:text-base">
                          {t(`ai_gallery.images.image_${image.id}.description`)}
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Navigation Arrows */}
          <Button
            variant="outline"
            size="icon"
            onClick={scrollPrev}
            className="absolute left-2 md:left-4 top-1/2 -translate-y-1/2 z-10 bg-slate-900/90 backdrop-blur-sm border-slate-700 hover:bg-slate-800 text-white h-10 w-10 md:h-12 md:w-12 rounded-full shadow-xl"
          >
            <ChevronLeft className="h-5 w-5 md:h-6 md:w-6" />
          </Button>
          <Button
            variant="outline"
            size="icon"
            onClick={scrollNext}
            className="absolute right-2 md:right-4 top-1/2 -translate-y-1/2 z-10 bg-slate-900/90 backdrop-blur-sm border-slate-700 hover:bg-slate-800 text-white h-10 w-10 md:h-12 md:w-12 rounded-full shadow-xl"
          >
            <ChevronRight className="h-5 w-5 md:h-6 md:w-6" />
          </Button>

          {/* Dot Indicators */}
          <div className="flex justify-center gap-2 mt-8">
            {images.map((_, index) => (
              <button
                key={index}
                onClick={() => emblaApi?.scrollTo(index)}
                className={`h-2 rounded-full transition-all duration-300 ${
                  index === selectedIndex
                    ? 'w-8 bg-amber-400'
                    : 'w-2 bg-slate-600 hover:bg-slate-500'
                }`}
                aria-label={`Go to slide ${index + 1}`}
              />
            ))}
          </div>

          {/* Counter */}
          <p className="text-center text-slate-400 text-sm mt-4">
            {t('ai_gallery.counter', { current: selectedIndex + 1, total: images.length })}
          </p>
        </div>

        {/* CTA */}
        <div className="text-center mt-12 animate-fade-in">
          <Button size="lg" className="bg-amber-500 hover:bg-amber-600 text-slate-900 font-semibold px-8">
            <Sparkles className="w-5 h-5 mr-2" />
            {t('ai_gallery.cta')}
          </Button>
        </div>
      </div>
    </section>
  );
};

export default AIImageGallery;
