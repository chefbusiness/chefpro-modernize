import { Button } from '@/components/ui/button';
import { Card, CardContent } from '@/components/ui/card';
import { useLanguage } from '@/hooks/useLanguage';

export default function ModernAbout() {
  const { getAppUrl, currentLanguage } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage), '_blank');
  };

  return (
    <section className="container py-8 md:py-12 lg:py-24">
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
          Sobre AI Chef Pro
        </h2>
        <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7 text-balance">
          <strong>AI Chef Pro</strong> es tu <strong>asistente culinario ideal</strong>, 
          ofreciendo herramientas innovadoras para <strong>chefs</strong> y <strong>cocineros</strong> que 
          buscan mejorar su <strong>eficiencia</strong> y <strong>creatividad</strong> apoyados 
          en el potencial que ofrece hoy la <strong>inteligencia artificial</strong>.
        </p>
      </div>

      <div className="mx-auto grid justify-center gap-4 sm:grid-cols-2 md:max-w-[64rem] md:grid-cols-3 mt-12">
        <Card className="hover-card">
          <CardContent className="flex flex-col items-center space-y-2 p-6">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <div className="h-6 w-6 rounded bg-accent" />
            </div>
            <h3 className="text-xl font-bold">Nuestra Misión</h3>
            <p className="text-sm text-muted-foreground text-center">
              Facilitar el uso de la <strong>inteligencia artificial generativa</strong> a 
              todos los profesionales de la <strong>cocina</strong>, la <strong>restauración</strong> y 
              la <strong>hostelería</strong> en general.
            </p>
          </CardContent>
        </Card>

        <Card className="hover-card">
          <CardContent className="flex flex-col items-center space-y-2 p-6">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <div className="h-6 w-6 rounded bg-accent" />
            </div>
            <h3 className="text-xl font-bold">Expande tu Creatividad</h3>
            <p className="text-sm text-muted-foreground text-center">
              Usa herramientas de última generación para potenciar e impulsar tu 
              capacidad de gestión, creatividad y liderazgo en el mundo gastronómico de hoy.
            </p>
          </CardContent>
        </Card>

        <Card className="hover-card">
          <CardContent className="flex flex-col items-center space-y-2 p-6">
            <div className="h-12 w-12 rounded-full bg-primary/10 flex items-center justify-center">
              <div className="h-6 w-6 rounded bg-accent" />
            </div>
            <h3 className="text-xl font-bold">Chef Diego Schattenhofer</h3>
            <p className="text-sm text-muted-foreground text-center">
              Desarrollado por el reconocido chef{" "}
              <a 
                href="https://diegoschatten.com/" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-accent hover:underline font-medium"
              >
                Diego Schattenhofer
              </a>{" "}
              y su equipo profesional.
            </p>
          </CardContent>
        </Card>
      </div>

      <div className="flex justify-center mt-12">
        <Button 
          onClick={handleCTAClick}
          size="lg"
          className="bg-primary text-primary-foreground hover:bg-primary/90"
        >
          PRUEBALO GRATIS AHORA
        </Button>
      </div>
    </section>
  );
}