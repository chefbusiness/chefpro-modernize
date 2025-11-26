import { 
  Carousel, 
  CarouselContent, 
  CarouselItem, 
  CarouselNext, 
  CarouselPrevious 
} from '@/components/ui/carousel';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Dialog, DialogContent, DialogTrigger } from '@/components/ui/dialog';
import { Star, ZoomIn } from 'lucide-react';
import { featuredApps } from '@/data/featured';
import { useLanguage } from '@/hooks/useLanguage';

export default function FeaturedApps() {
  const { getAppUrl, currentLanguage, t } = useLanguage();

  const handleAppClick = (appSlug: string) => {
    window.open(`${getAppUrl(currentLanguage)}/${appSlug}`, '_blank');
  };

  return (
    <section id="destacadas" className="container py-16 bg-muted/20">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          <span className="gradient-text">{t('featured.title_main')}</span> {t('featured.title_sub')}
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          {t('featured.description')}
        </p>
      </div>

      <Carousel className="w-full max-w-5xl mx-auto">
        <CarouselContent className="-ml-2 md:-ml-4">
          {featuredApps.map((app) => (
            <CarouselItem key={app.id} className="pl-2 md:pl-4 sm:basis-1/2 lg:basis-1/3">
              <Card className="category-card-marketing group h-full hover:shadow-lg transition-all duration-300 border-border/50 hover:border-accent/50">
                <CardHeader className="p-4 sm:p-6">
                  <div className="relative mb-4 group/image">
                    <Dialog>
                      <DialogTrigger asChild>
                        <div className="relative cursor-pointer">
                          <img 
                            src={app.image} 
                            alt={`${app.name} screenshot`}
                            className="w-full h-32 sm:h-40 object-cover rounded-lg transition-all duration-300 group-hover/image:scale-105"
                            loading="lazy"
                          />
                          <div className="absolute inset-0 bg-black/30 opacity-0 group-hover/image:opacity-100 transition-opacity duration-300 rounded-lg flex items-center justify-center">
                            <ZoomIn className="h-8 w-8 text-white" />
                          </div>
                        </div>
                      </DialogTrigger>
                      <DialogContent className="max-w-4xl w-[95vw] h-[95vh] p-4">
                        <div className="relative w-full h-full flex flex-col">
                          <div className="mb-4">
                             <h3 className="text-xl font-bold">{t(`featured.apps.${app.id.replace(/-/g, '_')}.name`)}</h3>
                             <p className="text-muted-foreground">{t(`featured.apps.${app.id.replace(/-/g, '_')}.description`)}</p>
                          </div>
                          <div className="flex-1 flex items-center justify-center">
                            <img 
                              src={app.image} 
                              alt={`${app.name} screenshot`}
                              className="max-w-full max-h-full object-contain rounded-lg shadow-lg"
                            />
                          </div>
                        </div>
                      </DialogContent>
                    </Dialog>
                    <div className="absolute top-2 right-2">
                      <div className="flex items-center gap-1 bg-background/90 backdrop-blur-sm px-2 py-1 rounded-full">
                        <Star className="h-3 w-3 fill-accent text-accent" />
                        <span className="text-xs font-medium">{t('featured.badge')}</span>
                      </div>
                    </div>
                  </div>
                  <CardTitle className="text-base sm:text-lg group-hover:text-accent transition-colors leading-tight">
                    {t(`featured.apps.${app.id.replace(/-/g, '_')}.name`)}
                  </CardTitle>
                  <CardDescription className="text-sm leading-relaxed">{t(`featured.apps.${app.id.replace(/-/g, '_')}.description`)}</CardDescription>
                </CardHeader>
                <CardContent className="p-4 sm:p-6 pt-0">
                  <blockquote className="border-l-4 border-accent/30 pl-3 sm:pl-4 italic text-sm">
                    <p className="mb-2 text-xs sm:text-sm leading-relaxed">"{t(`featured.apps.${app.id.replace(/-/g, '_')}.testimonial.text`)}"</p>
                    <footer className="text-muted-foreground">
                      <strong className="text-xs sm:text-sm">{t(`featured.apps.${app.id.replace(/-/g, '_')}.testimonial.author`)}</strong>
                      <br />
                      <span className="text-xs">{t(`featured.apps.${app.id.replace(/-/g, '_')}.testimonial.role`)}</span>
                    </footer>
                  </blockquote>
                </CardContent>
                <CardFooter className="p-4 sm:p-6 pt-0">
                  <Button 
                    className="w-full btn-gold group-hover:shadow-lg text-sm py-2 h-auto min-h-[2.5rem]"
                    onClick={() => handleAppClick(app.slug)}
                  >
                    {t(`featured.apps.${app.id.replace(/-/g, '_')}.cta`)}
                  </Button>
                </CardFooter>
              </Card>
            </CarouselItem>
          ))}
        </CarouselContent>
        <CarouselPrevious className="border-accent text-accent hover:bg-accent hover:text-accent-foreground" />
        <CarouselNext className="border-accent text-accent hover:bg-accent hover:text-accent-foreground" />
      </Carousel>
    </section>
  );
}