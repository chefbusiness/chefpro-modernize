import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { businessTools } from '@/data/apps';
import { useLanguage } from '@/hooks/useLanguage';

export default function BusinessToolsShowcase() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleAppClick = (appSlug: string) => {
    window.open(`${getAppUrl(currentLanguage)}/${appSlug}`, '_blank');
  };

  return (
    <section id="herramientas-business" className="container py-16">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          <span className="gradient-text">Herramientas Business</span>
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          6 aplicaciones esenciales para optimizar tu operación diaria
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {businessTools.map((tool) => {
          const IconComponent = tool.icon;
          
          return (
            <Card key={tool.id} className="group hover:shadow-lg transition-all duration-300 border-border/50 hover:border-accent/50">
              <CardHeader>
                <div className="flex items-center justify-between">
                  <IconComponent className="h-8 w-8 text-accent group-hover:text-accent-dark transition-colors" />
                </div>
                <CardTitle className="text-lg group-hover:text-accent transition-colors">{tool.name}</CardTitle>
                <CardDescription>{tool.description}</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="bg-muted/50 p-3 rounded text-sm">
                  <p className="text-muted-foreground mb-1">Caso de uso:</p>
                  <p className="font-medium">"{tool.preview}"</p>
                </div>
              </CardContent>
              <CardFooter>
                <Button 
                  variant="outline" 
                  className="w-full group-hover:bg-accent group-hover:text-accent-foreground transition-colors"
                  onClick={() => handleAppClick(tool.slug)}
                >
                  Usar Herramienta
                </Button>
              </CardFooter>
            </Card>
          );
        })}
      </div>
    </section>
  );
}