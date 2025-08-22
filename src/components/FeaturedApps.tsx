import { 
  Carousel, 
  CarouselContent, 
  CarouselItem, 
  CarouselNext, 
  CarouselPrevious 
} from '@/components/ui/carousel';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Star } from 'lucide-react';
import { featuredApps } from '@/data/featured';
import { useLanguage } from '@/hooks/useLanguage';

export default function FeaturedApps() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleAppClick = (appSlug: string) => {
    window.open(`${getAppUrl(currentLanguage)}/${appSlug}`, '_blank');
  };

  return (
    <section id="destacadas" className="container py-16 bg-muted/20">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          <span className="gradient-text">Apps Destacadas</span> de la Semana
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          Descubre las aplicaciones que están revolucionando la industria gastronómica
        </p>
      </div>

      <Carousel className="w-full max-w-5xl mx-auto">
        <CarouselContent>
          {featuredApps.map((app) => (
            <CarouselItem key={app.id} className="md:basis-1/2 lg:basis-1/3">
              <Card className="group h-full hover:shadow-lg transition-all duration-300 border-border/50 hover:border-accent/50">
                <CardHeader>
                  <div className="relative mb-4">
                    <img 
                      src={app.image} 
                      alt={`${app.name} screenshot`}
                      className="w-full h-40 object-cover rounded-lg"
                      loading="lazy"
                    />
                    <div className="absolute top-2 right-2">
                      <div className="flex items-center gap-1 bg-background/90 backdrop-blur-sm px-2 py-1 rounded-full">
                        <Star className="h-3 w-3 fill-accent text-accent" />
                        <span className="text-xs font-medium">Destacada</span>
                      </div>
                    </div>
                  </div>
                  <CardTitle className="text-lg group-hover:text-accent transition-colors">
                    {app.name}
                  </CardTitle>
                  <CardDescription>{app.description}</CardDescription>
                </CardHeader>
                <CardContent>
                  <blockquote className="border-l-4 border-accent/30 pl-4 italic text-sm">
                    <p className="mb-2">"{app.testimonial.text}"</p>
                    <footer className="text-muted-foreground">
                      <strong>{app.testimonial.author}</strong>
                      <br />
                      <span className="text-xs">{app.testimonial.role}</span>
                    </footer>
                  </blockquote>
                </CardContent>
                <CardFooter>
                  <Button 
                    className="w-full btn-gold group-hover:shadow-lg"
                    onClick={() => handleAppClick(app.slug)}
                  >
                    {app.ctaText}
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