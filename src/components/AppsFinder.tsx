import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { personas, getRecommendedApps } from '@/data/personas';
import { useLanguage } from '@/hooks/useLanguage';

export default function AppsFinder() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleAppClick = (appSlug: string) => {
    window.open(`${getAppUrl(currentLanguage)}/${appSlug}`, '_blank');
  };

  return (
    <section id="filtro-apps" className="container py-16 bg-muted/20">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          Encuentra tu <span className="gradient-text">App Perfecta</span>
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          Selecciona tu perfil y descubre las herramientas que mejor se adaptan a tus necesidades
        </p>
      </div>

      <Tabs defaultValue="chef-ejecutivo" className="w-full">
        <TabsList className="grid w-full grid-cols-2 md:grid-cols-3 lg:grid-cols-6 mb-8">
          {personas.map((persona) => (
            <TabsTrigger key={persona.id} value={persona.id} className="text-xs md:text-sm">
              <span className="mr-1">{persona.emoji}</span>
              <span className="hidden sm:inline">{persona.name.split(' ').slice(-1)}</span>
              <span className="sm:hidden">{persona.emoji}</span>
            </TabsTrigger>
          ))}
        </TabsList>

        {personas.map((persona) => {
          const recommendedApps = getRecommendedApps(persona.id);
          
          return (
            <TabsContent key={persona.id} value={persona.id}>
              <div className="text-center mb-8">
                <h3 className="text-xl font-semibold mb-2">
                  {persona.emoji} {persona.name}
                </h3>
                <p className="text-muted-foreground">{persona.description}</p>
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {recommendedApps.map((app) => {
                  if (!app) return null;
                  const IconComponent = app.icon;
                  
                  return (
                    <Card key={app.id} className="group hover:shadow-lg transition-all duration-300">
                      <CardHeader>
                        <div className="flex items-center justify-between mb-2">
                          <IconComponent className="h-6 w-6 text-accent" />
                        </div>
                        <CardTitle className="text-lg">{app.name}</CardTitle>
                        <CardDescription>{app.description}</CardDescription>
                      </CardHeader>
                      <CardContent>
                        <div className="bg-muted/50 p-3 rounded text-sm">
                          <p className="text-muted-foreground mb-1">Preview:</p>
                          <p className="font-medium text-sm">"{app.preview}"</p>
                        </div>
                      </CardContent>
                      <CardFooter>
                        <Button 
                          variant="outline" 
                          className="w-full group-hover:bg-accent group-hover:text-accent-foreground transition-colors"
                          onClick={() => handleAppClick(app.slug)}
                        >
                          Probar Ahora
                        </Button>
                      </CardFooter>
                    </Card>
                  );
                })}
              </div>
            </TabsContent>
          );
        })}
      </Tabs>
    </section>
  );
}