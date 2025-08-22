import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { appCategories } from '@/data/apps';

export default function AppsCategories() {
  const scrollToSection = (categoryId: string) => {
    const sectionMap: { [key: string]: string } = {
      creativity: 'showcase-creatividad',
      worldCookbooks: 'recetarios',
      knowledge: 'gastro-conocimiento',
      business: 'herramientas-business',
      concepts: 'conceptos-negocio',
      marketing: 'marketing-contenido'
    };
    
    const targetId = sectionMap[categoryId] || categoryId;
    const element = document.getElementById(targetId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="categorias-apps" className="container py-16">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          Explora Nuestras <span className="gradient-text">6 Categorías</span> de Apps
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          Cada categoría está diseñada para potenciar un aspecto específico de tu trabajo culinario
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {appCategories.map((category) => {
          const IconComponent = category.icon;
          return (
            <Card 
              key={category.id}
              className="group hover:shadow-lg transition-all duration-300 cursor-pointer hover:scale-105 border-border/50 hover:border-accent/50"
              onClick={() => scrollToSection(category.id)}
            >
              <CardHeader>
                <div className="flex items-center justify-between mb-2">
                  <IconComponent className="h-8 w-8 text-accent group-hover:text-accent-dark transition-colors" />
                  <Badge variant="secondary" className="bg-accent/10 text-accent-dark font-semibold">
                    {category.count} Apps
                  </Badge>
                </div>
                <CardTitle className="text-xl group-hover:text-accent transition-colors">
                  {category.name}
                </CardTitle>
                <CardDescription className="text-base">
                  {category.description}
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-1">
                  {category.apps.slice(0, 4).map((app) => (
                    <Badge key={app.id} variant="outline" className="text-xs">
                      {app.name}
                    </Badge>
                  ))}
                  {category.apps.length > 4 && (
                    <Badge variant="outline" className="text-xs text-muted-foreground">
                      +{category.apps.length - 4} más
                    </Badge>
                  )}
                  {category.id === 'worldCookbooks' && (
                    <>
                      <Badge variant="outline" className="text-xs">Europa (10)</Badge>
                      <Badge variant="outline" className="text-xs">Latinoamérica (11)</Badge>
                      <Badge variant="outline" className="text-xs">Asia (4)</Badge>
                    </>
                  )}
                </div>
              </CardContent>
            </Card>
          );
        })}
      </div>
    </section>
  );
}