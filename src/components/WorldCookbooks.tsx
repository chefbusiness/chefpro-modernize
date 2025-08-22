import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { worldCookbooks } from '@/data/apps';
import { useState } from 'react';

export default function WorldCookbooks() {
  const [selectedCuisine, setSelectedCuisine] = useState<string | null>(null);

  return (
    <section id="recetarios" className="container py-16 bg-muted/20">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          <span className="gradient-text">Recetarios Mundiales</span>
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          25 cocinas del mundo con recetas auténticas y técnicas tradicionales
        </p>
      </div>

      <div className="space-y-8">
        {/* Europa */}
        <div>
          <h3 className="text-2xl font-semibold mb-4 flex items-center gap-2">
            🌍 <span className="gradient-text">Europa</span>
            <Badge variant="secondary">10 Cocinas</Badge>
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {worldCookbooks.europa.map((cuisine) => (
              <Card 
                key={cuisine.name}
                className="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:border-accent/50"
                onClick={() => setSelectedCuisine(selectedCuisine === cuisine.name ? null : cuisine.name)}
              >
                <CardHeader className="pb-2">
                  <CardTitle className="text-center text-lg flex flex-col items-center gap-1">
                    <span className="text-2xl">{cuisine.flag}</span>
                    <span className="text-sm">{cuisine.name}</span>
                  </CardTitle>
                </CardHeader>
                {selectedCuisine === cuisine.name && (
                  <CardContent className="pt-0">
                    <CardDescription className="text-xs">
                      {cuisine.preview}
                    </CardDescription>
                  </CardContent>
                )}
              </Card>
            ))}
          </div>
        </div>

        {/* Latinoamérica */}
        <div>
          <h3 className="text-2xl font-semibold mb-4 flex items-center gap-2">
            🌎 <span className="gradient-text">Latinoamérica</span>
            <Badge variant="secondary">11 Cocinas</Badge>
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
            {worldCookbooks.latinoamerica.map((cuisine) => (
              <Card 
                key={cuisine.name}
                className="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:border-accent/50"
                onClick={() => setSelectedCuisine(selectedCuisine === cuisine.name ? null : cuisine.name)}
              >
                <CardHeader className="pb-2">
                  <CardTitle className="text-center text-lg flex flex-col items-center gap-1">
                    <span className="text-2xl">{cuisine.flag}</span>
                    <span className="text-sm">{cuisine.name}</span>
                  </CardTitle>
                </CardHeader>
                {selectedCuisine === cuisine.name && (
                  <CardContent className="pt-0">
                    <CardDescription className="text-xs">
                      {cuisine.preview}
                    </CardDescription>
                  </CardContent>
                )}
              </Card>
            ))}
          </div>
        </div>

        {/* Asia */}
        <div>
          <h3 className="text-2xl font-semibold mb-4 flex items-center gap-2">
            🌏 <span className="gradient-text">Asia</span>
            <Badge variant="secondary">4 Cocinas</Badge>
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {worldCookbooks.asia.map((cuisine) => (
              <Card 
                key={cuisine.name}
                className="group cursor-pointer hover:shadow-lg transition-all duration-300 hover:border-accent/50"
                onClick={() => setSelectedCuisine(selectedCuisine === cuisine.name ? null : cuisine.name)}
              >
                <CardHeader className="pb-2">
                  <CardTitle className="text-center text-lg flex flex-col items-center gap-1">
                    <span className="text-2xl">{cuisine.flag}</span>
                    <span className="text-sm">{cuisine.name}</span>
                  </CardTitle>
                </CardHeader>
                {selectedCuisine === cuisine.name && (
                  <CardContent className="pt-0">
                    <CardDescription className="text-xs">
                      {cuisine.preview}
                    </CardDescription>
                  </CardContent>
                )}
              </Card>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}