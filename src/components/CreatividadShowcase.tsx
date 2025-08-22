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

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {creativityApps.map((app) => {
          const IconComponent = app.icon;
          
          return (
            <Card key={app.id} className="group cursor-pointer hover:scale-105 transition-transform duration-300 border-border/50 hover:border-accent/50">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <IconComponent className="h-8 w-8 text-accent group-hover:text-accent-dark transition-colors" />
                </div>
                <CardTitle className="text-lg group-hover:text-accent transition-colors">{app.name}</CardTitle>
                <CardDescription>{app.description}</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="bg-muted/50 p-3 rounded text-sm">
                  <p className="text-muted-foreground mb-1">Preview:</p>
                  <p className="font-medium">"{app.preview}"</p>
                </div>
              </CardContent>
              <CardFooter>
                <Button 
                  variant="outline" 
                  className="w-full group-hover:bg-accent group-hover:text-accent-foreground transition-colors"
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