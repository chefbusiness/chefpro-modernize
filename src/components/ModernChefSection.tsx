import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { ExternalLink } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

export default function ModernChefSection() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  const handleDiegoLink = () => {
    window.open('https://diegoschatten.com/', '_blank');
  };

  return (
    <section className="border-t bg-muted/20">
      <div className="container py-8 md:py-12 lg:py-24">
        <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
          <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
            Recetas instantáneas. Mayor Productividad.{" "}
            <span className="gradient-text">Inspiración sin fin.</span>
          </h2>
          
          <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7">
            Chef{" "}
            <button 
              onClick={handleDiegoLink}
              className="font-semibold text-foreground hover:text-accent inline-flex items-center gap-1 underline underline-offset-4"
            >
              Diego Schattenhofer
              <ExternalLink className="h-4 w-4" />
            </button>
            {" "}y su equipo usando AI Chef Pro
          </p>

          <Button 
            onClick={handleCTAClick}
            size="lg"
            className="bg-primary text-primary-foreground hover:bg-primary/90 mt-4"
          >
            Prueba AI Chef Pro
          </Button>
        </div>

        {/* Images Grid */}
        <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3 mt-12">
          <Card className="hover-card overflow-hidden">
            <CardContent className="p-0">
              <img 
                src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=400,h=564,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-AE0ozo9ZB9TyR5p7.jpg"
                alt="Chef Diego Schattenhofer usando AI Chef Pro - Taste 1973"
                className="w-full h-64 object-cover"
              />
            </CardContent>
          </Card>
          
          <Card className="hover-card overflow-hidden">
            <CardContent className="p-0">
              <img 
                src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=194,h=276,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-2-AE0ozo9Z1Bi9KX9r.jpg"
                alt="Equipo Taste 1973 con AI Chef Pro"
                className="w-full h-64 object-cover"
              />
            </CardContent>
          </Card>
          
          <Card className="hover-card overflow-hidden">
            <CardContent className="p-0">
              <img 
                src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=194,h=276,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-3-A1awjw67oetpZEvK.jpg"
                alt="Innovación culinaria con AI Chef Pro"
                className="w-full h-64 object-cover"
              />
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}