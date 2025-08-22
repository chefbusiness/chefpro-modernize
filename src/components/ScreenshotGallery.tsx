import { useState } from 'react';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ChevronLeft, ChevronRight } from 'lucide-react';

const screenshots = [
  {
    id: 1,
    title: 'Catering AI+',
    description: 'Modelo de conocimiento impulsado por inteligencia artificial para chefs, cocineros y emprendedores en el negocio de catering',
    image: '/lovable-uploads/975877a4-27f4-4215-9f8a-63882f278540.png',
    category: 'Conceptos de Negocio'
  },
  {
    id: 2,
    title: 'Food Pairing AI',
    description: 'Descubre maridajes científicos y combinaciones innovadoras basadas en perfiles aromáticos',
    image: '/lovable-uploads/c01838d8-9dd4-430c-a4d8-98359573a299.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 3,
    title: 'Pastelería Creativa',
    description: 'Genera recetas de pastelería de alta calidad con presentaciones profesionales estilo Michelin',
    image: '/lovable-uploads/f2d20b90-077c-4486-a944-1c6c7fdc570e.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 4,
    title: 'Platos de Autor',
    description: 'Crea platos contemporáneos únicos con ingredientes de temporada y técnicas innovadoras',
    image: '/lovable-uploads/5863854b-f30c-47d7-89f0-6124f57cfacf.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 5,
    title: 'Cocina Creativa',
    description: 'Generador de recetas de cocina creativa de calidad profesional con historias de fondo',
    image: '/lovable-uploads/12abdf30-3381-42de-a8f1-2abe9342145f.png',
    category: 'Creatividad Culinaria'
  }
];

export default function ScreenshotGallery() {
  const [currentIndex, setCurrentIndex] = useState(0);

  const nextSlide = () => {
    setCurrentIndex((prev) => (prev + 1) % screenshots.length);
  };

  const prevSlide = () => {
    setCurrentIndex((prev) => (prev - 1 + screenshots.length) % screenshots.length);
  };

  const currentScreenshot = screenshots[currentIndex];

  return (
    <section className="container mx-auto px-4 py-8 md:py-12">
      <div className="text-center mb-8">
        <Badge variant="outline" className="mb-4">
          55+ Apps Especializadas en Acción
        </Badge>
        <h2 className="text-2xl md:text-3xl lg:text-4xl font-bold mb-4">
          Descubre el Poder de AI Chef Pro
        </h2>
        <p className="text-muted-foreground max-w-2xl mx-auto">
          Explora capturas reales de nuestras aplicaciones especializadas para profesionales gastronómicos
        </p>
      </div>

      <div className="max-w-6xl mx-auto">
        {/* Screenshot Display */}
        <div className="relative rounded-xl overflow-hidden shadow-2xl hover:shadow-3xl transition-shadow duration-300 bg-white">
          <img
            src={currentScreenshot.image}
            alt={currentScreenshot.title}
            className="w-full h-auto object-contain"
            onError={(e) => {
              // Fallback to placeholder if image fails to load
              const target = e.target as HTMLImageElement;
              target.src = `data:image/svg+xml;base64,${btoa(`
                <svg width="800" height="500" xmlns="http://www.w3.org/2000/svg">
                  <rect width="100%" height="100%" fill="#f3f4f6"/>
                  <text x="50%" y="50%" text-anchor="middle" font-family="Arial" font-size="24" fill="#6b7280">
                    ${currentScreenshot.title}
                  </text>
                </svg>
              `)}`;
            }}
          />
        </div>

        {/* App Info Below Image */}
        <div className="text-center mt-6 space-y-3">
          <Badge variant="secondary">
            {currentScreenshot.category}
          </Badge>
          <h3 className="text-2xl font-bold">
            {currentScreenshot.title}
          </h3>
          <p className="text-muted-foreground max-w-2xl mx-auto">
            {currentScreenshot.description}
          </p>
        </div>

        {/* Navigation Controls */}
        <div className="flex items-center justify-between mt-6">
          <Button
            variant="outline"
            size="sm"
            onClick={prevSlide}
            className="flex items-center gap-2"
          >
            <ChevronLeft className="w-4 h-4" />
            Anterior
          </Button>

          {/* Dots Indicator */}
          <div className="flex space-x-2">
            {screenshots.map((_, index) => (
              <button
                key={index}
                onClick={() => setCurrentIndex(index)}
                className={`w-3 h-3 rounded-full transition-colors ${
                  index === currentIndex ? 'bg-primary' : 'bg-muted-foreground/30'
                }`}
              />
            ))}
          </div>

          <Button
            variant="outline"
            size="sm"
            onClick={nextSlide}
            className="flex items-center gap-2"
          >
            Siguiente
            <ChevronRight className="w-4 h-4" />
          </Button>
        </div>

        {/* App Counter */}
        <div className="text-center mt-8">
          <p className="text-muted-foreground">
            {currentIndex + 1} de {screenshots.length} aplicaciones mostradas
          </p>
          <Button 
            size="lg" 
            className="btn-gold mt-4"
            onClick={() => window.open('https://app.aichef.pro', '_blank')}
          >
            Explorar Todas las Apps
          </Button>
        </div>
      </div>
    </section>
  );
}