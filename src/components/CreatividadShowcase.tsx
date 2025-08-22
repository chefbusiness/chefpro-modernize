import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { creativityApps } from '@/data/apps';
import { useLanguage } from '@/hooks/useLanguage';

export default function CreatividadShowcase() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleAppClick = (appSlug: string) => {
    window.open(`${getAppUrl(currentLanguage)}/${appSlug}`, '_blank');
  };

  return (
    <section id="showcase-creatividad" className="container py-16">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          <span className="gradient-text">Creatividad Culinaria</span> Showcase
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          8 aplicaciones especializadas para llevarte más allá de lo convencional
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6">
        {creativityApps.map((app) => {
          const IconComponent = app.icon;
          
          return (
            <Card key={app.id} className="group cursor-pointer hover:scale-[1.02] active:scale-[0.98] transition-transform duration-300 border-border/50 hover:border-accent/50">
              <CardHeader className="p-4 sm:p-6">
                <div className="flex items-center justify-between mb-2">
                  <IconComponent className="h-6 w-6 sm:h-8 sm:w-8 text-accent group-hover:text-accent-dark transition-colors" />
                </div>
                <CardTitle className="text-base sm:text-lg group-hover:text-accent transition-colors leading-tight">{app.name}</CardTitle>
                <CardDescription className="text-sm leading-relaxed">{app.description}</CardDescription>
              </CardHeader>
              <CardContent className="p-4 sm:p-6 pt-0">
                <div className="bg-muted/50 p-3 rounded text-sm">
                  <p className="text-muted-foreground mb-1 text-xs">Preview:</p>
                  <p className="font-medium text-xs sm:text-sm leading-relaxed">"{app.preview}"</p>
                </div>
              </CardContent>
              <CardFooter className="p-4 sm:p-6 pt-0">
                <Button 
                  variant="outline" 
                  className="w-full group-hover:bg-accent group-hover:text-accent-foreground transition-colors text-sm py-2 h-auto min-h-[2.5rem]"
                  onClick={() => handleAppClick(app.slug)}
                >
                  Explorar App
                </Button>
              </CardFooter>
            </Card>
          );
        })}
      </div>
    </section>
  );
}