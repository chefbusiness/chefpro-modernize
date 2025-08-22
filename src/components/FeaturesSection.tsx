import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Brain, Utensils, HeartHandshake } from 'lucide-react';

const FeaturesSection = () => {
  const features = [
    {
      icon: Brain,
      title: 'Modelo de Asistente Culinario AI',
      description: 'Recomendaciones personalizadas de recetas y técnicas adaptadas a tus preferencias culinarias. Más de 20 recetarios.'
    },
    {
      icon: Utensils,
      title: 'Food Pairing y Sustituciones de Ingredientes',
      description: 'Encuentra alternativas ideales para ingredientes que necesitas reemplazar en tus recetas.'
    },
    {
      icon: HeartHandshake,
      title: 'Coaching para Chefs',
      description: 'Apoyo psicológico y motivacional para mejorar el rendimiento y bienestar en la cocina.'
    }
  ];

  return (
    <section id="herramientas" className="py-20 bg-muted/30">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16 animate-fade-in-up">
          <h2 className="text-3xl md:text-4xl font-bold text-chef-dark mb-6">
            Herramientas Culinarias Avanzadas
          </h2>
          <p className="text-lg text-chef-gray max-w-3xl mx-auto leading-relaxed">
            Completa suite de herramientas y aplicaciones de inteligencia artificial para chefs y cocineros que quieran acelerar y optimizar su trabajo diario en la cocina profesional y explotar su creatividad.
          </p>
        </div>

        {/* Main Feature Image */}
        <div className="mb-16 animate-scale-in">
          <div className="chef-card overflow-hidden max-w-4xl mx-auto">
            <img 
              src="https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=612,h=415,fit=crop/AVLbeJ7l3JfrlNJr/ai-chef-pro---basic-apps-dWxb1bDVBVI55E7q.png"
              alt="Captura de modelos de IA entrenados para chefs y cocineros"
              className="w-full h-auto rounded-xl"
            />
          </div>
        </div>

        {/* Features Grid */}
        <div className="grid md:grid-cols-3 gap-8 animate-fade-in-up">
          {features.map((feature, index) => (
            <Card key={index} className="chef-card border-0 hover:shadow-elegant transition-all duration-300 hover:-translate-y-2">
              <CardHeader className="text-center pb-4">
                <div className="mx-auto w-16 h-16 bg-gradient-cta rounded-full flex items-center justify-center mb-4">
                  <feature.icon className="h-8 w-8 text-chef-dark" />
                </div>
                <CardTitle className="text-xl font-bold text-chef-dark">
                  {feature.title}
                </CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-chef-gray text-center leading-relaxed">
                  {feature.description}
                </CardDescription>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* LLM Models Section */}
        <div className="mt-20">
          <div className="text-center mb-12">
            <h3 className="text-2xl font-bold text-chef-dark mb-4">
              Tecnología LLM Avanzada
            </h3>
            <p className="text-chef-gray">
              Modelos de lenguaje especializados para el sector gastronómico
            </p>
          </div>
          
          <div className="grid grid-cols-2 md:grid-cols-5 gap-6 animate-scale-in">
            {[1, 2, 3, 4, 5].map((num) => (
              <div key={num} className="chef-card overflow-hidden">
                <img 
                  src={`https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=223,h=133,fit=crop/AVLbeJ7l3JfrlNJr/llm-${num}-${
                    num === 1 ? 'ALpok1ga1EfzpLrj' : 
                    num === 2 ? 'Yan98lK48Rc9D9ae' :
                    num === 3 ? 'dWxbkzgNN0treDe0' :
                    num === 4 ? 'A854KvXJ93I5kvw8' :
                    'A0xVJaXEGXFge8VZ'
                  }.png`}
                  alt={`Modelo LLM ${num} - AI Chef Pro`}
                  className="w-full h-24 object-cover rounded-lg hover:scale-105 transition-transform duration-300"
                />
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;