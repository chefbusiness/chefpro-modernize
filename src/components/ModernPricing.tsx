import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Check } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

export default function ModernPricing() {
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
      price: '10€',
      period: '/mes',
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
      price: '15€',
      period: '/mes',
      description: 'Para uso frecuente y mayor creatividad',
      features: [
        'Todas las funciones Pro',
        'Coaching para Chefs',
        'Análisis nutricional avanzado',
        'Personalización completa',
        'Integraciones avanzadas'
      ],
      popular: false
    },
    {
      name: 'Premium Pro',
      price: '25€',
      period: '/mes',
      description: 'Para chefs en roles de liderazgo',
      features: [
        'Todas las funciones Premium',
        'Gestión de equipo',
        'Analíticas avanzadas',
        'API access',
        'Consultoría mensual'
      ],
      popular: false
    },
    {
      name: 'Premium Plus',
      price: '50€',
      period: '/mes',
      description: 'Uso ilimitado para chefs ejecutivos',
      features: [
        'Acceso ilimitado completo',
        'Soporte 24/7',
        'Consultoría personalizada',
        'Desarrollo de características customizadas',
        'Integración enterprise'
      ],
      popular: false
    },
    {
      name: 'Premium Plus Anual',
      price: '500€',
      period: '/año',
      originalPrice: '600€',
      discount: 'Ahorra 100€',
      description: 'Ideal para Chefs Ejecutivos y Directivos en Dirección Gastronómica',
      features: [
        'Todas las 55+ herramientas incluidas',
        'Uso ilimitado durante todo el año',
        'Acceso a todas las cocinas del mundo',
        'Herramientas avanzadas de negocio',
        'Soporte premium 24/7',
        'Consultoría mensual personalizada'
      ],
      popular: true,
      isAnnual: true
    }
  ];

  const handlePlanClick = () => {
    window.open(getAppUrl(currentLanguage) + '/pricing', '_blank');
  };

  return (
    <section id="pricing" className="container py-8 md:py-12 lg:py-24">
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
          Planes y Precios
        </h2>
        <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7 text-balance">
          Planes adaptados a diferentes etapas de tu carrera como chef. 
          Cada plan está diseñado para apoyar tu crecimiento profesional 
          y adaptarse a tus necesidades cambiantes.
        </p>
      </div>

      <div className="grid w-full items-start gap-6 overflow-visible py-12 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6">
        {plans.map((plan, index) => (
          <Card 
            key={index} 
            className={`hover-card relative transition-all duration-300 ${
              plan.popular 
                ? 'popular-plan scale-105 ring-2 ring-accent/20' 
                : 'hover:scale-[1.02]'
            }`}
          >
            {plan.popular && (
              <Badge 
                variant="default" 
                className="popular-badge absolute -top-3 left-1/2 -translate-x-1/2"
              >
                🔥 Más Popular
              </Badge>
            )}
            
            {plan.discount && (
              <Badge 
                variant="default" 
                className="absolute -top-3 right-4 bg-green-600 text-white border-green-600 shadow-lg font-bold"
              >
                {plan.discount}
              </Badge>
            )}
            
            <CardHeader className="text-center pb-2">
              <CardTitle className="text-lg font-medium">{plan.name}</CardTitle>
              <div className="flex flex-col items-center gap-1">
                {plan.originalPrice && (
                  <span className="text-sm text-muted-foreground line-through">
                    {plan.originalPrice}
                  </span>
                )}
                <div className="flex items-baseline justify-center gap-1">
                  <span className="text-3xl font-bold">{plan.price}</span>
                  {plan.period && (
                    <span className="text-muted-foreground">{plan.period}</span>
                  )}
                </div>
              </div>
              <CardDescription className="text-sm">{plan.description}</CardDescription>
            </CardHeader>
            
            <CardContent className="grid gap-4">
              <Button 
                onClick={handlePlanClick}
                variant={plan.popular ? "default" : "secondary"}
                className={`w-full ${
                  plan.popular 
                    ? 'btn-gold hover:shadow-gold-glow' 
                    : 'bg-primary text-primary-foreground hover:bg-primary/90'
                }`}
              >
                {plan.price === 'Gratis' ? 'Empezar Gratis' : 'Seleccionar Plan'}
              </Button>
              
              <ul className="grid gap-2 text-sm">
                {plan.features.map((feature, featureIndex) => (
                  <li key={featureIndex} className="flex items-center gap-2">
                    <Check className={`h-4 w-4 ${plan.popular ? 'text-accent' : 'text-primary'}`} />
                    <span className="text-xs leading-5">{feature}</span>
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        ))}
      </div>

      <div className="text-center">
        <p className="text-muted-foreground text-sm">
          ¿Necesitas un plan enterprise?{" "}
          <a 
            href="#contacto" 
            className="font-medium text-primary hover:underline"
          >
            Contáctanos para una solución personalizada
          </a>
        </p>
      </div>
    </section>
  );
}