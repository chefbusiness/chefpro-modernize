import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Check } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

const PricingSection = () => {
  const { getAppUrl, currentLanguage } = useLanguage();

  const plans = [
    {
      name: 'Miembro',
      price: 'Gratis',
      description: 'Para explorar funcionalidades básicas',
      features: [
        'Acceso básico a herramientas',
        'Recetas básicas',
        'Soporte por email',
        'Funcionalidades limitadas'
      ],
      popular: false
    },
    {
      name: 'Pro',
      price: '10€/mes',
      description: 'Ideal para chefs individuales',
      features: [
        'Todas las funciones básicas',
        'Generador de recetas avanzado',
        'Food Pairing AI',
        'Soporte prioritario',
        'Más de 20 recetarios'
      ],
      popular: false
    },
    {
      name: 'Premium',
      price: '15€/mes',
      description: 'Para uso frecuente y mayor creatividad',
      features: [
        'Todas las funciones Pro',
        'Coaching para Chefs',
        'Análisis nutricional avanzado',
        'Personalización completa',
        'Integraciones avanzadas'
      ],
      popular: true
    },
    {
      name: 'Premium Pro',
      price: '25€/mes',
      description: 'Para chefs en roles de liderazgo',
      features: [
        'Todas las funciones Premium',
        'Gestión de equipo',
        'Análticas avanzadas',
        'API access',
        'Consultoría mensual'
      ],
      popular: false
    },
    {
      name: 'Premium Plus',
      price: '50€/mes',
      description: 'Uso ilimitado para chefs ejecutivos',
      features: [
        'Acceso ilimitado completo',
        'Soporte 24/7',
        'Consultoría personalizada',
        'Desarrollo de características customizadas',
        'Integración enterprise'
      ],
      popular: false
    }
  ];

  const handlePlanClick = () => {
    window.open(getAppUrl(currentLanguage) + '/pricing', '_blank');
  };

  return (
    <section id="precios" className="py-20 bg-muted/20">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16 animate-fade-in-up">
          <h2 className="text-3xl md:text-4xl font-bold text-chef-dark mb-6">
            Planes y Precios
          </h2>
          <p className="text-lg text-chef-gray max-w-3xl mx-auto">
            Planes adaptados a diferentes etapas de tu carrera como chef. Cada plan está diseñado para apoyar tu crecimiento profesional y adaptarse a tus necesidades cambiantes.
          </p>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6 animate-scale-in">
          {plans.map((plan, index) => (
            <Card 
              key={index} 
              className={`chef-card border-2 relative hover:shadow-elegant transition-all duration-300 hover:-translate-y-2 ${
                plan.popular 
                  ? 'border-chef-gold shadow-glow' 
                  : 'border-border hover:border-chef-gold/30'
              }`}
            >
              {plan.popular && (
                <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                  <span className="bg-chef-gold text-chef-dark px-4 py-1 rounded-full text-sm font-bold">
                    Más Popular
                  </span>
                </div>
              )}
              
              <CardHeader className="text-center pb-4">
                <CardTitle className="text-xl font-bold text-chef-dark">
                  {plan.name}
                </CardTitle>
                <div className="mt-4">
                  <span className="text-3xl font-bold text-chef-dark">
                    {plan.price}
                  </span>
                </div>
                <CardDescription className="text-chef-gray mt-2">
                  {plan.description}
                </CardDescription>
              </CardHeader>
              
              <CardContent className="space-y-4">
                <ul className="space-y-3">
                  {plan.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-start gap-2">
                      <Check className="h-5 w-5 text-chef-gold mt-0.5 flex-shrink-0" />
                      <span className="text-sm text-chef-gray">{feature}</span>
                    </li>
                  ))}
                </ul>
                
                <Button 
                  onClick={handlePlanClick}
                  className={`w-full mt-6 ${
                    plan.popular 
                      ? 'chef-cta-button' 
                      : 'bg-secondary text-secondary-foreground hover:bg-secondary/80'
                  }`}
                >
                  {plan.price === 'Gratis' ? 'Empezar Gratis' : 'Seleccionar Plan'}
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>

        <div className="text-center mt-12">
          <p className="text-chef-gray">
            ¿Necesitas un plan enterprise? {' '}
            <a 
              href="#contacto" 
              className="text-chef-gold hover:underline font-medium"
            >
              Contáctanos para una solución personalizada
            </a>
          </p>
        </div>
      </div>
    </section>
  );
};

export default PricingSection;