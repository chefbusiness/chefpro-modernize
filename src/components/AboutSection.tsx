import { Button } from '@/components/ui/button';
import { useLanguage } from '@/hooks/useLanguage';
import chefDiegoImage from '@/assets/chef-diego.jpg';

const AboutSection = () => {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  return (
    <section id="sobre" className="py-20 bg-background">
      <div className="container mx-auto px-4">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Content */}
          <div className="space-y-8 animate-fade-in-up">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold text-chef-dark mb-6">
                Sobre AI Chef Pro
              </h2>
              <p className="text-lg text-chef-gray leading-relaxed">
                <strong>AI Chef Pro</strong> es tu <strong>asistente culinario ideal</strong>, ofreciendo herramientas innovadoras para <strong>chefs</strong> y <strong>cocineros</strong> que buscan mejorar su <strong>eficiencia</strong> y <strong>creatividad</strong> apoyados en el potencial que ofrece hoy la <strong>inteligencia artificial</strong>.
              </p>
            </div>

            <div>
              <h3 className="text-2xl font-bold text-chef-dark mb-4">Nuestra Misión</h3>
              <p className="text-lg text-chef-gray leading-relaxed">
                La Misión de <strong>AI Chef Pro</strong> es facilitar el uso de la <strong>inteligencia artificial generativa</strong> a todos los profesionales de la <strong>cocina</strong>, la <strong>restauración</strong> y la <strong>hostelería</strong> en general.
              </p>
            </div>

            <div>
              <h3 className="text-2xl font-bold text-chef-dark mb-4">Expande tu Creatividad</h3>
              <p className="text-lg text-chef-gray leading-relaxed">
                Usa herramientas de última generación para potenciar e impulsar tu capacidad de gestión, creatividad y liderazgo en el mundo gastronómico de hoy.
              </p>
            </div>

            <Button 
              onClick={handleCTAClick}
              className="chef-cta-button text-lg px-8 py-4 hover:scale-105 transform transition-all duration-300"
            >
              PRUEBALO GRATIS AHORA
            </Button>
          </div>

          {/* Images */}
          <div className="grid grid-cols-2 gap-6 animate-scale-in">
            <div className="space-y-6">
              <div className="chef-card overflow-hidden">
                <img 
                  src={chefDiegoImage}
                  alt="Chef Diego Schattenhofer - AI Chef Pro"
                  className="w-full h-64 object-cover rounded-lg"
                />
              </div>
              <div className="chef-card overflow-hidden">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=328,h=227,fit=crop/AVLbeJ7l3JfrlNJr/equipo-YrDNv8pRppcZyG5y.png"
                  alt="Equipo AI Chef Pro"
                  className="w-full h-48 object-cover rounded-lg"
                />
              </div>
            </div>
            <div className="pt-12">
              <div className="chef-card overflow-hidden mb-6">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=400,h=480,fit=crop/AVLbeJ7l3JfrlNJr/equipo-YrDNv8pRppcZyG5y.png"
                  alt="Equipo AI Chef Pro trabajando"
                  className="w-full h-80 object-cover rounded-lg"
                />
              </div>
              <div className="chef-card overflow-hidden">
                <img 
                  src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=263,h=344,fit=crop/AVLbeJ7l3JfrlNJr/captura-de-pantalla-2024-08-29-a-las-11.58.02-AoPG8GrzGrFKWpoL.png"
                  alt="ID Alérgenos - AI Chef Pro"
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

export default AboutSection;