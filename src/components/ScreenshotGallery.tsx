import { useState, useEffect } from 'react';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { ChevronLeft, ChevronRight, Play, Pause } from 'lucide-react';

const screenshots = [
  {
    id: 1,
    title: 'Cocina Creativa',
    description: 'Generador de recetas de cocina creativa de calidad profesional con historias de fondo',
    image: '/lovable-uploads/12abdf30-3381-42de-a8f1-2abe9342145f.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 2,
    title: 'Platos de Autor',
    description: 'Crea platos contemporáneos únicos con ingredientes de temporada y técnicas innovadoras',
    image: '/lovable-uploads/5863854b-f30c-47d7-89f0-6124f57cfacf.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 3,
    title: 'Catering AI+',
    description: 'Modelo de conocimiento impulsado por inteligencia artificial para chefs, cocineros y emprendedores en el negocio de catering',
    image: '/lovable-uploads/975877a4-27f4-4215-9f8a-63882f278540.png',
    category: 'Conceptos de Negocio'
  },
  {
    id: 4,
    title: 'Food Pairing AI',
    description: 'Descubre maridajes científicos y combinaciones innovadoras basadas en perfiles aromáticos',
    image: '/lovable-uploads/c01838d8-9dd4-430c-a4d8-98359573a299.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 5,
    title: 'Pastelería Creativa',
    description: 'Genera recetas de pastelería de alta calidad con presentaciones profesionales estilo Michelin',
    image: '/lovable-uploads/f2d20b90-077c-4486-a944-1c6c7fdc570e.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 6,
    title: 'Sosa Ingredients Agent',
    description: 'Asistente IA especializado en ingredientes de vanguardia Sosa para cocina profesional y técnicas innovadoras',
    image: '/lovable-uploads/ed9e5325-4d1f-44fb-9643-e01fa3de208c.png',
    category: 'Proveedores Gastro'
  },
  {
    id: 7,
    title: 'Casual Restaurants AI+',
    description: 'Experto en restaurantes familiares, bistrós, mesones y gastrobares. Asesoramiento completo para propietarios y personal',
    image: '/lovable-uploads/4a01fa26-97e9-40ce-9cf6-d17c71b10abd.png',
    category: 'Conceptos de Negocio'
  },
  {
    id: 8,
    title: 'MenuDish Local SEO',
    description: 'Genera contenido SEO optimizado para cada plato de tu carta y potencia la visibilidad local de tu restaurante',
    image: '/lovable-uploads/6cfe3941-1762-441d-b87b-5bd37a8a3667.png',
    category: 'Marketing & Contenido'
  },
  {
    id: 9,
    title: 'Cocina Peruana',
    description: 'Generador especializado en recetas auténticas de la rica gastronomía peruana con historias culturales e ingredientes precisos',
    image: '/lovable-uploads/a1eb6b5e-e0c6-47e2-88d5-7a8247807000.png',
    category: 'Recetarios Mundiales'
  },
  {
    id: 10,
    title: 'Cocina Francesa',
    description: 'Maestro en la tradición culinaria francesa, desde clásicos bistró hasta alta cocina con técnicas profesionales',
    image: '/lovable-uploads/26949727-8432-41b4-8f59-8cc40151efa4.png',
    category: 'Recetarios Mundiales'
  },
  {
    id: 11,
    title: 'Fermentus Con AI+',
    description: 'Asistente experto en fermentación creativa y conservas de autor. Domina koji, kombuchas, misos y técnicas innovadoras',
    image: '/lovable-uploads/64a2d776-3e86-49cc-bdc7-9df927d3624a.png',
    category: 'Creatividad Culinaria'
  },
  {
    id: 12,
    title: 'Cocina India Recetario',
    description: 'Explora la rica gastronomía india con recetas auténticas como samosas, curries y chutneys tradicionales',
    image: '/lovable-uploads/c7595f12-a770-4c58-939f-69a9c3c8a1f8.png',
    category: 'Recetarios Mundiales'
  }
];

export default function ScreenshotGallery() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isAutoRotating, setIsAutoRotating] = useState(true);
  const [isTransitioning, setIsTransitioning] = useState(false);

  const nextSlide = () => {
    if (isTransitioning) return;
    setIsTransitioning(true);
    setCurrentIndex((prev) => (prev + 1) % screenshots.length);
    setTimeout(() => setIsTransitioning(false), 300);
  };

  const prevSlide = () => {
    if (isTransitioning) return;
    setIsAutoRotating(false);
    setIsTransitioning(true);
    setCurrentIndex((prev) => (prev - 1 + screenshots.length) % screenshots.length);
    setTimeout(() => setIsTransitioning(false), 300);
  };

  const goToSlide = (index: number) => {
    if (isTransitioning || index === currentIndex) return;
    setIsAutoRotating(false);
    setIsTransitioning(true);
    setCurrentIndex(index);
    setTimeout(() => setIsTransitioning(false), 300);
  };

  const toggleAutoRotation = () => {
    setIsAutoRotating(!isAutoRotating);
  };

  // Auto-rotation effect
  useEffect(() => {
    if (!isAutoRotating) return;
    
    const interval = setInterval(() => {
      nextSlide();
    }, 4000); // Change image every 4 seconds

    return () => clearInterval(interval);
  }, [isAutoRotating, currentIndex]);

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
            className={`w-full h-auto object-contain transition-opacity duration-300 ${
              isTransitioning ? 'opacity-50' : 'opacity-100'
            }`}
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
          {/* Auto-rotation indicator */}
          {isAutoRotating && (
            <div className="absolute top-4 right-4">
              <div className="flex items-center gap-2 bg-black/20 backdrop-blur-sm rounded-full px-3 py-1">
                <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                <span className="text-white text-xs font-medium">Auto</span>
              </div>
            </div>
          )}
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
            disabled={isTransitioning}
          >
            <ChevronLeft className="w-4 h-4" />
            Anterior
          </Button>

          {/* Center Controls: Dots + Play/Pause */}
          <div className="flex items-center space-x-4">
            {/* Auto-rotation toggle */}
            <Button
              variant="ghost"
              size="sm"
              onClick={toggleAutoRotation}
              className="flex items-center gap-2"
            >
              {isAutoRotating ? (
                <Pause className="w-4 h-4" />
              ) : (
                <Play className="w-4 h-4" />
              )}
            </Button>

            {/* Dots Indicator */}
            <div className="flex space-x-2">
              {screenshots.map((_, index) => (
                <button
                  key={index}
                  onClick={() => goToSlide(index)}
                  disabled={isTransitioning}
                  className={`w-3 h-3 rounded-full transition-all duration-300 hover:scale-110 ${
                    index === currentIndex 
                      ? 'bg-primary scale-110' 
                      : 'bg-muted-foreground/30 hover:bg-muted-foreground/50'
                  }`}
                />
              ))}
            </div>
          </div>

          <Button
            variant="outline"
            size="sm"
            onClick={nextSlide}
            className="flex items-center gap-2"
            disabled={isTransitioning}
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