import { Button } from '@/components/ui/button';
import { ExternalLink } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

const ChefDiegoSection = () => {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  const handleDiegoLink = () => {
    window.open('https://diegoschatten.com/', '_blank');
  };

  return (
    <section className="py-20 bg-gradient-hero text-white">
      <div className="container mx-auto px-4 text-center">
        <div className="max-w-4xl mx-auto space-y-8 animate-fade-in-up">
          {/* Main Heading */}
          <h2 className="text-3xl md:text-5xl font-bold leading-tight">
            Recetas instantáneas. Mayor Productividad.{' '}
            <span className="chef-gradient-text">Inspiración sin fin.</span>
          </h2>
          
          {/* Subheading */}
          <div className="space-y-4">
            <p className="text-xl md:text-2xl text-gray-200">
              Chef{' '}
              <button 
                onClick={handleDiegoLink}
                className="font-bold text-chef-gold hover:underline inline-flex items-center gap-1 transition-colors"
              >
                Diego Schattenhofer
                <ExternalLink className="h-4 w-4" />
              </button>
              {' '}y su equipo usando{' '}
              <strong>AI Chef Pro</strong>
            </p>
          </div>

          {/* CTA */}
          <div className="pt-4">
            <Button
              onClick={handleCTAClick}
              size="lg"
              className="chef-cta-button text-lg px-8 py-4 hover:scale-105 transform transition-all duration-300"
            >
              Prueba AI Chef Pro
            </Button>
          </div>

          {/* Images Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16 animate-scale-in">
            <div className="space-y-6">
              <div className="chef-card overflow-hidden bg-white/10 backdrop-blur-sm border-white/20">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=400,h=564,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-AE0ozo9ZB9TyR5p7.jpg"
                  alt="Chef Diego Schattenhofer usando AI Chef Pro - Taste 1973"
                  className="w-full h-80 object-cover rounded-lg"
                />
              </div>
            </div>
            
            <div className="space-y-6">
              <div className="chef-card overflow-hidden bg-white/10 backdrop-blur-sm border-white/20">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=194,h=276,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-2-AE0ozo9Z1Bi9KX9r.jpg"
                  alt="Equipo Taste 1973 con AI Chef Pro"
                  className="w-full h-64 object-cover rounded-lg"
                />
              </div>
              <div className="chef-card overflow-hidden bg-white/10 backdrop-blur-sm border-white/20">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=158,h=144,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-2-AE0ozo9Z1Bi9KX9r.jpg"
                  alt="Tecnología AI Chef Pro en cocina"
                  className="w-full h-32 object-cover rounded-lg"
                />
              </div>
            </div>
            
            <div className="space-y-6">
              <div className="chef-card overflow-hidden bg-white/10 backdrop-blur-sm border-white/20">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=194,h=276,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-3-A1awjw67oetpZEvK.jpg"
                  alt="Innovación culinaria con AI Chef Pro"
                  className="w-full h-64 object-cover rounded-lg"
                />
              </div>
              <div className="chef-card overflow-hidden bg-white/10 backdrop-blur-sm border-white/20">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=158,h=144,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---taste-1973-3-A1awjw67oetpZEvK.jpg"
                  alt="Resultados profesionales AI Chef Pro"
                  className="w-full h-32 object-cover rounded-lg"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ChefDiegoSection;