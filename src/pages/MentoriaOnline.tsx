import { useTranslation } from 'react-i18next';
import { useLanguage } from '@/hooks/useLanguage';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, Clock, Users, Star, ArrowRight, BookOpen, Target, Zap, TrendingUp, Search, Lightbulb, Timer, ChevronDown, ChevronRight } from 'lucide-react';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";

const MentoriaOnline = () => {
  const { t } = useTranslation();
  const { currentLanguage } = useLanguage();

  const scrollToCalendly = () => {
    const calendlySection = document.getElementById('calendly-section');
    if (calendlySection) {
      calendlySection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  // Solo usar traducciones si no es español
  const getText = (spanishText: string, translationKey: string) => {
    if (currentLanguage === 'es') {
      return spanishText;
    }
    return t(translationKey);
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead 
        title={currentLanguage === 'es' ? "Mentoría Online Personalizada AI Chef Pro - Maximiza tu potencial" : t('pages.mentoria.seo.title')}
        description={currentLanguage === 'es' ? "Sesiones estratégicas 1:1 con expertos en gastronomía e IA para acelerar resultados en tu negocio. Planes desde €150. Reserva ahora." : t('pages.mentoria.seo.description')}
        keywords={currentLanguage === 'es' ? "mentoría chef, consultoría ai chef pro, asesoramiento gastronómico, inteligencia artificial restaurantes" : t('pages.mentoria.seo.keywords')}
      />
      <ModernHeader />
      
      <main>
        {/* Hero Section */}
        <section className="relative overflow-hidden bg-gradient-to-br from-primary/10 via-background to-secondary/5 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-6xl lg:text-7xl mb-6">
                {getText("Mentoría AI Chef Pro", "pages.mentoria.hero.title")}
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
                {getText("Incorpora el uso de la Inteligencia Artificial Profesional a tu día a día. Te Ofrecemos planes de Asesoramiento y Entrenamiento a medida.", "pages.mentoria.hero.subtitle")}
              </p>
            </div>
          </div>
        </section>

        {/* Second Hero Section */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center max-w-6xl mx-auto">
              <div>
                <h2 className="text-3xl font-bold text-foreground mb-6">
                  {getText("Mentoría Online Personalizada AI Chef Pro", "nav.mentoria_online")}
                </h2>
                <h3 className="text-2xl font-semibold text-primary mb-4">
                  {getText("Maximiza el potencial de AI Chef Pro con asesoría especializada", "pages.mentoria.benefits.subtitle")}
                </h3>
                <p className="text-lg text-muted-foreground mb-8">
                  {getText("Sesiones estratégicas 1:1 con expertos en gastronomía e IA para acelerar resultados en tu negocio", "pages.mentoria.features.subtitle")}
                </p>
                <Button size="lg" onClick={scrollToCalendly} className="bg-primary text-primary-foreground hover:bg-primary/90">
                  {getText("Reserva tu Mentoría Ahora", "pages.mentoria.hero.cta")}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </div>
              <div className="relative">
                <img 
                  src="https://blog.aichef.pro/wp-content/uploads/2025/03/Untitled-design.jpeg" 
                  alt="Consultoría AI Chef Pro" 
                  className="rounded-lg shadow-xl w-full"
                />
              </div>
            </div>
          </div>
        </section>

        {/* Benefits Section */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("¿Por qué necesitas una consultoría personalizada?", "pages.mentoria.benefits.title")}
              </h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <TrendingUp className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{getText("Resultados acelerados", "pages.mentoria.benefits.items.accelerated.title")}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {getText("Reduce meses de prueba y error a una sola sesión estratégica. ROI inmediato en tu inversión en AI Chef Pro.", "pages.mentoria.benefits.items.accelerated.description")}
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Search className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{getText("Estrategia a medida", "Estrategia a medida")}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {getText("Recibe un plan personalizado para tu tipo específico de negocio gastronómico, adaptado a tus objetivos particulares.", "Recibe un plan personalizado para tu tipo específico de negocio gastronómico, adaptado a tus objetivos particulares.")}
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Lightbulb className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{getText("Técnicas avanzadas", "Técnicas avanzadas")}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {getText("Accede a metodologías y prompts exclusivos no documentados que solo los usuarios expertos conocen.", "Accede a metodologías y prompts exclusivos no documentados que solo los usuarios expertos conocen.")}
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Timer className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{getText("Ahorro de tiempo", "Ahorro de tiempo")}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {getText("Elimina la curva de aprendizaje y comienza a implementar soluciones efectivas desde el primer día.", "Elimina la curva de aprendizaje y comienza a implementar soluciones efectivas desde el primer día.")}
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Pricing Plans Section - CONTENIDO ORIGINAL RESTAURADO */}
        <section className="py-20 bg-muted/50" id="calendly-section">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("Nuestros Planes de Consultoría y Mentoría Online", "Nuestros Planes de Consultoría y Mentoría Online")}
              </h2>
              <p className="text-xl text-muted-foreground max-w-4xl mx-auto">
                {getText("Selección el plan, agenda la mentoría y prepárate para en una o varias sesiones dominar el potencial de la inteligencia artificial aplicado a la gestión de restaurantes y el mundo de la gastronomía y la hostelería en general.", "Selección el plan, agenda la mentoría y prepárate para en una o varias sesiones dominar el potencial de la inteligencia artificial aplicado a la gestión de restaurantes y el mundo de la gastronomía y la hostelería en general.")}
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
              {/* Plan Express - CONTENIDO ORIGINAL */}
              <Card className="relative border-2 border-muted hover:border-primary/50 transition-colors">
                <CardHeader className="text-center">
                  <CardTitle className="text-2xl font-bold">Sesión Express</CardTitle>
                  <div className="mt-4 mb-4">
                    <span className="text-4xl font-bold">€150</span>
                  </div>
                  <CardDescription className="text-lg font-semibold">
                    2 horas
                  </CardDescription>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Diagnóstico rápido de necesidades</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Configuración inicial personalizada</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Enfoque en 1-2 herramientas clave</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Soluciones de implementación inmediata</span>
                    </li>
                  </ul>
                  <p className="text-sm text-muted-foreground">
                    <strong>Ideal para:</strong> Usuarios nuevos o con necesidades específicas puntuales
                  </p>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/john-guerrero-chefbusiness/mentoria-sesion-express-ai-chef-pro" target="_blank" rel="noopener noreferrer">
                      Reservar ahora
                    </a>
                  </Button>
                </CardContent>
              </Card>

              {/* Plan Estándar - CONTENIDO ORIGINAL */}
              <Card className="relative border-2 border-primary popular-plan">
                <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                  <Badge className="popular-badge">
                    Más popular
                  </Badge>
                </div>
                <CardHeader className="text-center pt-6">
                  <CardTitle className="text-2xl font-bold">Sesión Estándar</CardTitle>
                  <div className="mt-4 mb-2">
                    <span className="text-4xl font-bold">€275</span>
                  </div>
                  <CardDescription className="text-lg font-semibold">
                    3 horas
                  </CardDescription>
                  <Badge variant="secondary" className="bg-green-100 text-green-800 mt-2">
                    Ahorra un 8%
                  </Badge>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Análisis completo de necesidades</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Configuración avanzada del perfil</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Estrategia para 3-4 herramientas clave</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Plan de implementación a 30 días</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Material complementario exclusivo</span>
                    </li>
                  </ul>
                  <p className="text-sm text-muted-foreground">
                    <strong>Ideal para:</strong> Restaurantes, pastelerías y negocios establecidos
                  </p>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/john-guerrero-chefbusiness/mentoria-sesion-estandar-ai-chef-pro" target="_blank" rel="noopener noreferrer">
                      Reservar ahora
                    </a>
                  </Button>
                </CardContent>
              </Card>

              {/* Plan Intensiva - CONTENIDO ORIGINAL */}
              <Card className="relative border-2 border-muted hover:border-primary/50 transition-colors">
                <CardHeader className="text-center">
                  <CardTitle className="text-2xl font-bold">Sesión Intensiva</CardTitle>
                  <div className="mt-4 mb-2">
                    <span className="text-4xl font-bold">€360</span>
                  </div>
                  <CardDescription className="text-lg font-semibold">
                    4 horas
                  </CardDescription>
                  <Badge variant="secondary" className="bg-green-100 text-green-800 mt-2">
                    Ahorra un 20%
                  </Badge>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Plan estratégico de integración total</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Formación avanzada en todas las herramientas</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Optimización de prompts personalizados</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Seguimiento a 7 días incluido</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>Acceso a recursos premium exclusivos</span>
                    </li>
                  </ul>
                  <p className="text-sm text-muted-foreground">
                    <strong>Ideal para:</strong> Grupos de restauración, empresas de catering y negocios medianos
                  </p>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/john-guerrero-chefbusiness/mentoria-sesion-intensiva-ai-chef-pro" target="_blank" rel="noopener noreferrer">
                      Reservar ahora
                    </a>
                  </Button>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Specialized Mentoring Section - CONTENIDO ORIGINAL */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("Mentoría Especializada por Perfil Profesional o Consultoría por Concepto de Negocio", "Mentoría Especializada por Perfil Profesional o Consultoría por Concepto de Negocio")}
              </h2>
              <p className="text-lg text-muted-foreground max-w-6xl mx-auto">
                {getText("Todas nuestras sesiones de 1 hora, 2 o 3 horas se adaptan a tu perfil específico dentro de la industria gastronómica y/o a tu concepto de negocio. Nuestras mentorías de entrenamiento y capacitación estarán configuradas y enfocadas en tu realidad para que puedas aprovechar al máximo el uso de esta suite de herramientas impulsadas con inteligencia artificial son útiles para dueños de restaurantes, chefs ejecutivos / corporativos, managers o directores de restaurantes, líderes de equipos en general en la hostelería y la industria de la restauración.", "Todas nuestras sesiones de 1 hora, 2 o 3 horas se adaptan a tu perfil específico dentro de la industria gastronómica y/o a tu concepto de negocio. Nuestras mentorías de entrenamiento y capacitación estarán configuradas y enfocadas en tu realidad para que puedas aprovechar al máximo el uso de esta suite de herramientas impulsadas con inteligencia artificial son útiles para dueños de restaurantes, chefs ejecutivos / corporativos, managers o directores de restaurantes, líderes de equipos en general en la hostelería y la industria de la restauración.")}
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow text-center">
                <CardHeader>
                  <div className="mx-auto mb-4">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Restaurnte.jpeg" 
                      alt="Restaurantes" 
                      className="w-16 h-16 mx-auto rounded-lg"
                    />
                  </div>
                  <CardTitle className="text-xl">Restaurantes</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    Optimización de carta, gestión de costes, creatividad diferencial y experiencia del comensal
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow text-center">
                <CardHeader>
                  <div className="mx-auto mb-4">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Catering.jpeg" 
                      alt="Catering" 
                      className="w-16 h-16 mx-auto rounded-lg"
                    />
                  </div>
                  <CardTitle className="text-xl">Empresas de Catering</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    Gestión de eventos, escalabilidad, optimización logística y maximización de márgenes
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow text-center">
                <CardHeader>
                  <div className="mx-auto mb-4">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Pastelerias.jpeg" 
                      alt="Pastelería" 
                      className="w-16 h-16 mx-auto rounded-lg"
                    />
                  </div>
                  <CardTitle className="text-xl">Pastelerías/Panaderías</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    Creatividad, optimización de formulaciones, reducción de mermas y diferenciación
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow text-center">
                <CardHeader>
                  <div className="mx-auto mb-4">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Food-truck.jpeg" 
                      alt="Food Truck" 
                      className="w-16 h-16 mx-auto rounded-lg"
                    />
                  </div>
                  <CardTitle className="text-xl">Food Trucks, Dark Kitchens y Conceptos Emergentes</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    Eficiencia en espacios reducidos, optimización de carta y estrategias de crecimiento
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Testimonials Section - CONTENIDO ORIGINAL RESTAURADO */}
        <section className="py-20 bg-muted/50">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("Lo que dicen nuestros clientes", "Lo que dicen nuestros clientes")}
              </h2>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    {[1,2,3,4,5].map((star) => (
                      <Star key={star} className="h-5 w-5 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <blockquote className="text-muted-foreground mb-4">
                    "En solo dos horas reorganizamos completamente nuestro approach a la cocina creativa. Estamos creando platos innovadores con la mitad del esfuerzo y doble impacto en el cliente."
                  </blockquote>
                  <div className="flex items-center space-x-3">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/Testimonios-ai-chef-pro-Testimonios-ai-chef-pro-Martin.png" 
                      alt="Chef Martín"
                      className="w-10 h-10 rounded-full"
                    />
                    <div>
                      <p className="font-semibold text-sm">Chef Martín Rodríguez</p>
                      <p className="text-xs text-muted-foreground">Restaurante Fusión, Valencia</p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    {[1,2,3,4,5].map((star) => (
                      <Star key={star} className="h-5 w-5 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <blockquote className="text-muted-foreground mb-4">
                    "Reducimos nuestras mermas del 14% al 5% en menos de un mes aplicando las estrategias de la consultoría. El ROI fue instantáneo, literalmente pagamos la sesión con lo que ahorramos la primera semana."
                  </blockquote>
                  <div className="flex items-center space-x-3">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/Testimonios-ai-chef-pro-Testimonios-ai-chef-pro-Laura.png" 
                      alt="Laura García"
                      className="w-10 h-10 rounded-full"
                    />
                    <div>
                      <p className="font-semibold text-sm">Laura García</p>
                      <p className="text-xs text-muted-foreground">Directora de Operaciones, Grupo Gastronómico BCN</p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    {[1,2,3,4,5].map((star) => (
                      <Star key={star} className="h-5 w-5 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <blockquote className="text-muted-foreground mb-4">
                    "Conseguimos desarrollar una línea completa de 12 postres de autor para nuestro catálogo de verano en tiempo récord. La consultoría nos enseñó a exprimir al máximo las herramientas creativas de AI Chef Pro."
                  </blockquote>
                  <div className="flex items-center space-x-3">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/Testimonios-ai-chef-pro-Testimonios-ai-chef-pro-Carlos.png" 
                      alt="Carlos Ruiz"
                      className="w-10 h-10 rounded-full"
                    />
                    <div>
                      <p className="font-semibold text-sm">Carlos Ruiz</p>
                      <p className="text-xs text-muted-foreground">Maestro Pastelero, Sweet Dreams Madrid</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Process Section - CONTENIDO ORIGINAL */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("¿Cómo funciona el proceso?", "¿Cómo funciona el proceso?")}
              </h2>
            </div>
            
            <div className="max-w-4xl mx-auto">
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <div className="text-center">
                  <div className="w-12 h-12 bg-primary rounded-full flex items-center justify-center text-white font-bold text-xl mx-auto mb-4">
                    1
                  </div>
                  <h3 className="text-xl font-semibold mb-4">Reserva tu sesión</h3>
                  <p className="text-muted-foreground">
                    Selecciona el plan que mejor se adapte a tus necesidades y reserva tu espacio en nuestro calendario. Nuestra recomendación es que inicialmente contrates una hora. Si son necesarias más sesiones de 2 o 3 horas lo podremos valorar juntos y así podrás aprovechar mejor el tiempo y el conocimiento que podrás adquirir
                  </p>
                </div>
                <div className="text-center">
                  <div className="w-12 h-12 bg-primary rounded-full flex items-center justify-center text-white font-bold text-xl mx-auto mb-4">
                    2
                  </div>
                  <h3 className="text-xl font-semibold mb-4">Completa el cuestionario previo</h3>
                  <p className="text-muted-foreground">
                    Recibirás un formulario para completar 48h antes de la sesión para que podamos prepararnos específicamente para tus necesidades.
                  </p>
                </div>
                <div className="text-center">
                  <div className="w-12 h-12 bg-primary rounded-full flex items-center justify-center text-white font-bold text-xl mx-auto mb-4">
                    3
                  </div>
                  <h3 className="text-xl font-semibold mb-4">Sesión personalizada</h3>
                  <p className="text-muted-foreground">
                    Conectamos por videoconferencia para la sesión de consultoría, donde desarrollaremos estrategias específicas para tu negocio.
                  </p>
                </div>
                <div className="text-center">
                  <div className="w-12 h-12 bg-primary rounded-full flex items-center justify-center text-white font-bold text-xl mx-auto mb-4">
                    4
                  </div>
                  <h3 className="text-xl font-semibold mb-4">Implementación y seguimiento</h3>
                  <p className="text-muted-foreground">
                    Recibirás un plan de acción detallado y recursos complementarios. Incluimos seguimiento para asegurar resultados.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* FAQ Section - CONTENIDO ORIGINAL RESTAURADO */}
        <section className="py-20 bg-muted/50">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("Preguntas Frecuentes", "Preguntas Frecuentes")}
              </h2>
            </div>
            
            <div className="max-w-3xl mx-auto">
              <Accordion type="single" collapsible className="space-y-4">
                <AccordionItem value="item-1" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Necesito tener una suscripción activa a AI Chef Pro?
                  </AccordionTrigger>
                  <AccordionContent>
                    Sí, necesitas tener una cuenta activa en AI Chef Pro para poder aprovechar al máximo la consultoría. Recomendamos al menos el plan Pro para acceder a la mayoría de las funcionalidades que trabajaremos durante la sesión.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-2" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Qué plataforma se usa para las consultorías?
                  </AccordionTrigger>
                  <AccordionContent>
                    Utilizamos Google Meet para las sesiones de consultoría, lo que nos permite compartir pantalla, grabar la sesión (si lo deseas) y tener una comunicación fluida. Recibirás un enlace personalizado tras confirmar tu reserva.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-3" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Cómo me preparo para la sesión?
                  </AccordionTrigger>
                  <AccordionContent>
                    Te enviaremos un cuestionario completo 48 horas antes de la sesión. Para aprovechar al máximo, te recomendamos tener claros tus objetivos, acceso a tu cuenta de AI Chef Pro, y cualquier dato relevante de tu negocio (menús actuales, información sobre costes, etc.).
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-4" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Cuál es la política de cancelación?
                  </AccordionTrigger>
                  <AccordionContent>
                    Puedes reprogramar tu sesión hasta 24 horas antes sin coste adicional. Las cancelaciones con menos de 24 horas de antelación están sujetas a un cargo del 50%. Si necesitas cancelar, contáctanos cuanto antes para buscar la mejor solución.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-5" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Ofrecen garantía de satisfacción?
                  </AccordionTrigger>
                  <AccordionContent>
                    Sí, ofrecemos una garantía de satisfacción completa. Si al finalizar los primeros 30 minutos de la sesión consideras que no estás recibiendo el valor esperado, te reembolsaremos el 100% del importe.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-6" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Puedo solicitar una consultoría para un tema muy específico?
                  </AccordionTrigger>
                  <AccordionContent>
                    Absolutamente. En el formulario previo podrás detallar exactamente qué aspectos específicos quieres trabajar, ya sea una herramienta concreta de AI Chef Pro o un desafío particular de tu negocio.
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </div>
          </div>
        </section>

        {/* Final CTA Section - CONTENIDO ORIGINAL */}
        <section className="py-20 bg-gradient-to-r from-primary/10 to-secondary/10">
          <div className="container mx-auto px-4 text-center">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {getText("Reserva tu Mentoría Online Ahora", "Reserva tu Mentoría Online Ahora")}
              </h2>
              <p className="text-xl text-muted-foreground mb-8">
                {getText("Selecciona el tipo de sesión que prefieres y encuentra el momento perfecto para potenciar tu negocio con AI Chef Pro. Aprovecha la inteligencia artificial en tu día a día al máximo.", "Selecciona el tipo de sesión que prefieres y encuentra el momento perfecto para potenciar tu negocio con AI Chef Pro. Aprovecha la inteligencia artificial en tu día a día al máximo.")}
              </p>
              <Button size="lg" onClick={scrollToCalendly} className="bg-primary text-primary-foreground hover:bg-primary/90 mr-4">
                {getText("Reserva tu Mentoría Ahora", "Reserva tu Mentoría Ahora")}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
            </div>
          </div>
        </section>

        {/* Free 15min Session - CONTENIDO ORIGINAL */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto text-center">
              <h2 className="text-3xl font-bold text-foreground mb-6">
                {getText("¿No estás seguro de qué paquete elegir?", "¿No estás seguro de qué paquete elegir?")}
              </h2>
              <p className="text-lg text-muted-foreground mb-8">
                {getText("Agenda una micro-sesión gratuita de 15 minutos para discutir tus necesidades y determinar cuál es la mejor opción para tu negocio.", "Agenda una micro-sesión gratuita de 15 minutos para discutir tus necesidades y determinar cuál es la mejor opción para tu negocio.")}
              </p>
              <Card className="max-w-md mx-auto border-primary/20 shadow-lg">
                <CardHeader className="text-center">
                  <Badge variant="secondary" className="mb-2 bg-green-100 text-green-800">GRATIS</Badge>
                  <CardTitle className="text-xl">Micro-Sesión Gratuita</CardTitle>
                  <CardDescription>15 minutos para conocernos</CardDescription>
                </CardHeader>
                <CardContent>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/johnito9/micro-sesion-gratis-ai-chef-pro-15min" target="_blank" rel="noopener noreferrer">
                      Agendar micro-sesión gratuita
                    </a>
                  </Button>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>
      </main>
      
      <ModernFooter />
    </div>
  );
};

export default MentoriaOnline;