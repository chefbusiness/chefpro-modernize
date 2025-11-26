import { useTranslation } from 'react-i18next';
import { Helmet } from 'react-helmet-async';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, Clock, Users, Star, ArrowRight, BookOpen, Target, Zap, TrendingUp, Search, Lightbulb, Timer, ChevronDown, ChevronRight } from 'lucide-react';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { useLanguage } from '@/hooks/useLanguage';

const MentoriaOnline = () => {
  const { t } = useTranslation();
  const { currentLanguage } = useLanguage();

  const scrollToCalendly = () => {
    const calendlySection = document.getElementById('calendly-section');
    if (calendlySection) {
      calendlySection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://aichef.pro"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": t('mentoriaOnline.hero.title'),
        "item": "https://aichef.pro/mentoria-online"
      }
    ]
  };

  const serviceSchema = {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": t('mentoriaOnline.hero.title'),
    "description": t('mentoriaOnline.seo.description'),
    "provider": {
      "@type": "Organization",
      "name": "AI Chef Pro",
      "url": "https://aichef.pro"
    },
    "serviceType": "Professional Mentoring",
    "areaServed": {
      "@type": "Place",
      "name": "Worldwide"
    },
    "offers": [
      {
        "@type": "Offer",
        "name": currentLanguage === 'es' ? 'Sesión Express' : t('mentoriaOnline.sections.pricing.express.title'),
        "price": "150",
        "priceCurrency": "EUR"
      },
      {
        "@type": "Offer",
        "name": currentLanguage === 'es' ? 'Sesión Estándar' : t('mentoriaOnline.sections.pricing.standard.title'),
        "price": "275",
        "priceCurrency": "EUR"
      },
      {
        "@type": "Offer",
        "name": currentLanguage === 'es' ? 'Sesión Intensiva' : t('mentoriaOnline.sections.pricing.intensive.title'),
        "price": "360",
        "priceCurrency": "EUR"
      }
    ]
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead 
        title={t('pages.mentoria_online.seo_title')}
        description={t('pages.mentoria_online.seo_description')}
        keywords={t('pages.mentoria_online.seo_keywords')}
      />
      <Helmet>
        <script type="application/ld+json">
          {JSON.stringify(breadcrumbSchema)}
        </script>
        <script type="application/ld+json">
          {JSON.stringify(serviceSchema)}
        </script>
      </Helmet>
      <ModernHeader />
      
      <main>
        {/* Hero Section */}
        <section className="relative overflow-hidden bg-gradient-to-br from-primary/10 via-background to-secondary/5 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-6xl lg:text-7xl mb-6">
                {t('mentoriaOnline.hero.title')}
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
                {t('mentoriaOnline.hero.subtitle')}
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
                  {currentLanguage === 'es' ? 'Mentoría Online Personalizada AI Chef Pro' : t('mentoriaOnline.hero.title')}
                </h2>
                <h3 className="text-2xl font-semibold text-primary mb-4">
                  {currentLanguage === 'es' ? 'Maximiza el potencial de AI Chef Pro con asesoría especializada' : t('mentoriaOnline.hero.subtitle')}
                </h3>
                <p className="text-lg text-muted-foreground mb-8">
                  {currentLanguage === 'es' ? 'Sesiones estratégicas 1:1 con expertos en gastronomía e IA para acelerar resultados en tu negocio' : t('mentoriaOnline.sections.description')}
                </p>
                <Button size="lg" onClick={scrollToCalendly} className="bg-primary text-primary-foreground hover:bg-primary/90">
                  {currentLanguage === 'es' ? 'Reserva tu Mentoría Ahora' : t('mentoriaOnline.sections.cta_button')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </div>
              <div className="relative">
                <img 
                  src="https://blog.aichef.pro/wp-content/uploads/2025/03/Untitled-design.jpeg" 
                  alt={t('alt_texts.mentoria_hero')}
                  className="rounded-lg shadow-xl w-full"
                  loading="lazy"
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
                {currentLanguage === 'es' ? '¿Por qué necesitas una consultoría personalizada?' : t('mentoriaOnline.sections.benefits.title')}
              </h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <TrendingUp className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Resultados acelerados' : t('mentoriaOnline.sections.benefits.accelerated_results.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Reduce meses de prueba y error a una sola sesión estratégica. ROI inmediato en tu inversión en AI Chef Pro.' 
                      : t('mentoriaOnline.sections.benefits.accelerated_results.description')
                    }
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Search className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Estrategia a medida' : t('mentoriaOnline.sections.benefits.custom_strategy.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Recibe un plan personalizado para tu tipo específico de negocio gastronómico, adaptado a tus objetivos particulares.' 
                      : t('mentoriaOnline.sections.benefits.custom_strategy.description')
                    }
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Lightbulb className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Técnicas avanzadas' : t('mentoriaOnline.sections.benefits.advanced_techniques.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Accede a metodologías y prompts exclusivos no documentados que solo los usuarios expertos conocen.' 
                      : t('mentoriaOnline.sections.benefits.advanced_techniques.description')
                    }
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Timer className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Ahorro de tiempo' : t('mentoriaOnline.sections.benefits.time_saving.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Elimina la curva de aprendizaje y comienza a implementar soluciones efectivas desde el primer día.' 
                      : t('mentoriaOnline.sections.benefits.time_saving.description')
                    }
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Pricing Plans Section */}
        <section className="py-20 bg-muted/30" id="calendly-section">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {currentLanguage === 'es' ? 'Nuestros Planes de Consultoría y Mentoría Online' : t('mentoriaOnline.sections.pricing.title')}
              </h2>
              <p className="text-lg text-muted-foreground max-w-4xl mx-auto">
                {currentLanguage === 'es' 
                  ? 'Selección el plan, agenda la mentoría y prepárate para en una o varias sesiones dominar el potencial de la inteligencia artificial aplicado a la gestión de restaurantes y el mundo de la gastronomía y la hostelería en general.' 
                  : t('mentoriaOnline.sections.pricing.subtitle')
                }
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
              {/* Plan Express */}
              <Card className="hover-card relative transition-all duration-300 hover:scale-[1.02]">
                <CardHeader className="text-center">
                  <CardTitle className="text-2xl font-bold">
                    {currentLanguage === 'es' ? 'Sesión Express' : t('mentoriaOnline.sections.pricing.express.title')}
                  </CardTitle>
                  <div className="text-4xl font-bold text-primary">
                    {currentLanguage === 'es' ? '€150' : t('mentoriaOnline.sections.pricing.express.price')}
                  </div>
                  <div className="text-lg text-muted-foreground">
                    {currentLanguage === 'es' ? '2 horas' : t('mentoriaOnline.sections.pricing.express.duration')}
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-3">
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Diagnóstico rápido de necesidades' : t('mentoriaOnline.sections.pricing.express.features.0')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Configuración inicial personalizada' : t('mentoriaOnline.sections.pricing.express.features.1')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Enfoque en 1-2 herramientas clave' : t('mentoriaOnline.sections.pricing.express.features.2')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Soluciones de implementación inmediata' : t('mentoriaOnline.sections.pricing.express.features.3')}</span>
                    </li>
                  </ul>
                  <div className="pt-4">
                    <p className="text-sm text-muted-foreground mb-4">
                      <strong>{currentLanguage === 'es' ? 'Ideal para:' : t('mentoriaOnline.sections.pricing.ideal_for')}</strong> {currentLanguage === 'es' ? 'Usuarios nuevos o con necesidades específicas puntuales' : t('mentoriaOnline.sections.pricing.express.ideal')}
                    </p>
                    <Button 
                      className="w-full bg-accent text-accent-foreground hover:bg-accent-dark hover:shadow-lg hover:scale-105 font-semibold transition-all duration-300" 
                      onClick={() => window.open('https://calendly.com/john-guerrero-chefbusiness/mentoria-sesion-express-ai-chef-pro', '_blank')}
                    >
                      {currentLanguage === 'es' ? 'Reservar ahora' : t('mentoriaOnline.sections.pricing.express.button')}
                    </Button>
                  </div>
                </CardContent>
              </Card>

              {/* Plan Estándar - Most Popular */}
              <Card className="hover-card relative popular-plan scale-105 ring-2 ring-accent/20 transition-all duration-300">
                <Badge className="popular-badge absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-3 py-1">
                  {currentLanguage === 'es' ? '🔥 Más popular' : t('mentoriaOnline.sections.pricing.standard.badge')}
                </Badge>
                <CardHeader className="text-center pt-8">
                  <CardTitle className="text-2xl font-bold">
                    {currentLanguage === 'es' ? 'Sesión Estándar' : t('mentoriaOnline.sections.pricing.standard.title')}
                  </CardTitle>
                  <div className="text-4xl font-bold text-primary">
                    {currentLanguage === 'es' ? '€275' : t('mentoriaOnline.sections.pricing.standard.price')}
                  </div>
                  <div className="text-lg text-muted-foreground">
                    {currentLanguage === 'es' ? '3 horas' : t('mentoriaOnline.sections.pricing.standard.duration')}
                  </div>
                  <Badge variant="default" className="mx-auto bg-green-600 text-white border-green-600 shadow-lg font-bold">
                    {currentLanguage === 'es' ? 'Ahorra un 8%' : t('mentoriaOnline.sections.pricing.standard.save')}
                  </Badge>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-3">
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-accent mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Análisis completo de necesidades' : t('mentoriaOnline.sections.pricing.standard.features.0')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-accent mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Configuración avanzada del perfil' : t('mentoriaOnline.sections.pricing.standard.features.1')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-accent mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Estrategia para 3-4 herramientas clave' : t('mentoriaOnline.sections.pricing.standard.features.2')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-accent mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Plan de implementación a 30 días' : t('mentoriaOnline.sections.pricing.standard.features.3')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-accent mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Material complementario exclusivo' : t('mentoriaOnline.sections.pricing.standard.features.4')}</span>
                    </li>
                  </ul>
                  <div className="pt-4">
                    <p className="text-sm text-muted-foreground mb-4">
                      <strong>{currentLanguage === 'es' ? 'Ideal para:' : t('mentoriaOnline.sections.pricing.ideal_for')}</strong> {currentLanguage === 'es' ? 'Restaurantes, pastelerías y negocios establecidos' : t('mentoriaOnline.sections.pricing.standard.ideal')}
                    </p>
                    <Button 
                      className="w-full btn-gold hover:shadow-gold-glow scale-105 font-semibold transition-all duration-300" 
                      onClick={() => window.open('https://calendly.com/john-guerrero-chefbusiness/mentoria-sesion-estandar-ai-chef-pro', '_blank')}
                    >
                      {currentLanguage === 'es' ? 'Reservar ahora' : t('mentoriaOnline.sections.pricing.standard.button')}
                    </Button>
                  </div>
                </CardContent>
              </Card>

              {/* Plan Intensiva */}
              <Card className="hover-card relative transition-all duration-300 hover:scale-[1.02]">
                <CardHeader className="text-center">
                  <CardTitle className="text-2xl font-bold">
                    {currentLanguage === 'es' ? 'Sesión Intensiva' : t('mentoriaOnline.sections.pricing.intensive.title')}
                  </CardTitle>
                  <div className="text-4xl font-bold text-primary">
                    {currentLanguage === 'es' ? '€360' : t('mentoriaOnline.sections.pricing.intensive.price')}
                  </div>
                  <div className="text-lg text-muted-foreground">
                    {currentLanguage === 'es' ? '4 horas' : t('mentoriaOnline.sections.pricing.intensive.duration')}
                  </div>
                  <Badge variant="default" className="mx-auto bg-blue-600 text-white border-blue-600 shadow-lg font-bold">
                    {currentLanguage === 'es' ? 'Ahorra un 20%' : t('mentoriaOnline.sections.pricing.intensive.save')}
                  </Badge>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-3">
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Plan estratégico de integración total' : t('mentoriaOnline.sections.pricing.intensive.features.0')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Formación avanzada en todas las herramientas' : t('mentoriaOnline.sections.pricing.intensive.features.1')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Optimización de prompts personalizados' : t('mentoriaOnline.sections.pricing.intensive.features.2')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Seguimiento a 7 días incluido' : t('mentoriaOnline.sections.pricing.intensive.features.3')}</span>
                    </li>
                    <li className="flex items-start gap-3">
                      <CheckCircle className="h-5 w-5 text-primary mt-0.5 flex-shrink-0" />
                      <span>{currentLanguage === 'es' ? 'Acceso a recursos premium exclusivos' : t('mentoriaOnline.sections.pricing.intensive.features.4')}</span>
                    </li>
                  </ul>
                  <div className="pt-4">
                    <p className="text-sm text-muted-foreground mb-4">
                      <strong>{currentLanguage === 'es' ? 'Ideal para:' : t('mentoriaOnline.sections.pricing.ideal_for')}</strong> {currentLanguage === 'es' ? 'Grupos de restauración, empresas de catering y negocios medianos' : t('mentoriaOnline.sections.pricing.intensive.ideal')}
                    </p>
                    <Button 
                      className="w-full bg-accent text-accent-foreground hover:bg-accent-dark hover:shadow-lg hover:scale-105 font-semibold transition-all duration-300" 
                      onClick={() => window.open('https://calendly.com/john-guerrero-chefbusiness/mentoria-sesion-intensiva-ai-chef-pro', '_blank')}
                    >
                      {currentLanguage === 'es' ? 'Reservar ahora' : t('mentoriaOnline.sections.pricing.intensive.button')}
                    </Button>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Specialization Section */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {currentLanguage === 'es' ? 'Mentoría Especializada por Perfil Profesional o Consultoría por Concepto de Negocio' : t('mentoriaOnline.sections.specialization.title')}
              </h2>
              <p className="text-lg text-muted-foreground max-w-4xl mx-auto">
                {currentLanguage === 'es' 
                  ? 'Todas nuestras sesiones de 1 hora, 2 o 3 horas se adaptan a tu perfil específico dentro de la industria gastronómica y/o a tu concepto de negocio. Nuestras mentorías de entrenamiento y capacitación estarán configuradas y enfocadas en tu realidad para que puedas aprovechar al máximo el uso de esta suite de herramientas impulsadas con inteligencia artificial son útiles para dueños de restaurantes, chefs ejecutivos / corporativos, managers o directores de restaurantes, líderes de equipos en general en la hostelería y la industria de la restauración.' 
                  : t('mentoriaOnline.sections.specialization.subtitle')
                }
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <img 
                    src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Restaurnte.jpeg" 
                    alt={currentLanguage === 'es' ? 'Restaurantes' : t('mentoriaOnline.sections.specialization.restaurants.title')} 
                    className="w-16 h-16 mx-auto mb-4 rounded-lg"
                  />
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Restaurantes' : t('mentoriaOnline.sections.specialization.restaurants.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Optimización de carta, gestión de costes, creatividad diferencial y experiencia del comensal' 
                      : t('mentoriaOnline.sections.specialization.restaurants.description')
                    }
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <img 
                    src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Catering.jpeg" 
                    alt={currentLanguage === 'es' ? 'Catering' : t('mentoriaOnline.sections.specialization.catering.title')} 
                    className="w-16 h-16 mx-auto mb-4 rounded-lg"
                  />
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Empresas de Catering' : t('mentoriaOnline.sections.specialization.catering.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Gestión de eventos, escalabilidad, optimización logística y maximización de márgenes' 
                      : t('mentoriaOnline.sections.specialization.catering.description')
                    }
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <img 
                    src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Pastelerias.jpeg" 
                    alt={currentLanguage === 'es' ? 'Pastelería' : t('mentoriaOnline.sections.specialization.bakery.title')} 
                    className="w-16 h-16 mx-auto mb-4 rounded-lg"
                  />
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Pastelerías/Panaderías' : t('mentoriaOnline.sections.specialization.bakery.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Creatividad, optimización de formulaciones, reducción de mermas y diferenciación' 
                      : t('mentoriaOnline.sections.specialization.bakery.description')
                    }
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <img 
                    src="https://blog.aichef.pro/wp-content/uploads/2025/03/icon-industries-ai-chef-pro-Food-truck.jpeg" 
                    alt={currentLanguage === 'es' ? 'Food Truck' : t('mentoriaOnline.sections.specialization.food_truck.title')} 
                    className="w-16 h-16 mx-auto mb-4 rounded-lg"
                  />
                  <CardTitle className="text-xl">
                    {currentLanguage === 'es' ? 'Food Trucks, Dark Kitchens y Conceptos Emergentes' : t('mentoriaOnline.sections.specialization.food_truck.title')}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Eficiencia en espacios reducidos, optimización de carta y estrategias de crecimiento' 
                      : t('mentoriaOnline.sections.specialization.food_truck.description')
                    }
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Testimonials Section */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {currentLanguage === 'es' ? 'Lo que dicen nuestros clientes' : t('mentoriaOnline.sections.testimonials.title')}
              </h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex mb-4">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <p className="text-muted-foreground mb-4 italic">
                    {currentLanguage === 'es' 
                      ? '"En solo dos horas reorganizamos completamente nuestro approach a la cocina creativa. Estamos creando platos innovadores con la mitad del esfuerzo y doble impacto en el cliente."'
                      : t('mentoriaOnline.sections.testimonials.testimonial1.quote')
                    }
                  </p>
                  <div className="flex items-center gap-3">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/Testimonios-ai-chef-pro-Testimonios-ai-chef-pro-Martin.png" 
                      alt={currentLanguage === 'es' ? 'Chef Martín' : t('mentoriaOnline.sections.testimonials.testimonial1.name')} 
                      className="w-12 h-12 rounded-full"
                    />
                    <div>
                      <p className="font-semibold text-foreground">
                        {currentLanguage === 'es' ? 'Chef Martín Rodríguez' : t('mentoriaOnline.sections.testimonials.testimonial1.name')}
                      </p>
                      <p className="text-sm text-muted-foreground">
                        {currentLanguage === 'es' ? 'Restaurante Fusión, Valencia' : t('mentoriaOnline.sections.testimonials.testimonial1.position')}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex mb-4">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <p className="text-muted-foreground mb-4 italic">
                    {currentLanguage === 'es' 
                      ? '"Reducimos nuestras mermas del 14% al 5% en menos de un mes aplicando las estrategias de la consultoría. El ROI fue instantáneo, literalmente pagamos la sesión con lo que ahorramos la primera semana."'
                      : t('mentoriaOnline.sections.testimonials.testimonial2.quote')
                    }
                  </p>
                  <div className="flex items-center gap-3">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/Testimonios-ai-chef-pro-Testimonios-ai-chef-pro-Laura.png" 
                      alt={currentLanguage === 'es' ? 'Laura García' : t('mentoriaOnline.sections.testimonials.testimonial2.name')} 
                      className="w-12 h-12 rounded-full"
                    />
                    <div>
                      <p className="font-semibold text-foreground">
                        {currentLanguage === 'es' ? 'Laura García' : t('mentoriaOnline.sections.testimonials.testimonial2.name')}
                      </p>
                      <p className="text-sm text-muted-foreground">
                        {currentLanguage === 'es' ? 'Directora de Operaciones, Grupo Gastronómico BCN' : t('mentoriaOnline.sections.testimonials.testimonial2.position')}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex mb-4">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <p className="text-muted-foreground mb-4 italic">
                    {currentLanguage === 'es' 
                      ? '"Conseguimos desarrollar una línea completa de 12 postres de autor para nuestro catálogo de verano en tiempo récord. La consultoría nos enseñó a exprimir al máximo las herramientas creativas de AI Chef Pro."'
                      : t('mentoriaOnline.sections.testimonials.testimonial3.quote')
                    }
                  </p>
                  <div className="flex items-center gap-3">
                    <img 
                      src="https://blog.aichef.pro/wp-content/uploads/2025/03/Testimonios-ai-chef-pro-Testimonios-ai-chef-pro-Carlos.png" 
                      alt={currentLanguage === 'es' ? 'Carlos Ruiz' : t('mentoriaOnline.sections.testimonials.testimonial3.name')} 
                      className="w-12 h-12 rounded-full"
                    />
                    <div>
                      <p className="font-semibold text-foreground">
                        {currentLanguage === 'es' ? 'Carlos Ruiz' : t('mentoriaOnline.sections.testimonials.testimonial3.name')}
                      </p>
                      <p className="text-sm text-muted-foreground">
                        {currentLanguage === 'es' ? 'Maestro Pastelero, Sweet Dreams Madrid' : t('mentoriaOnline.sections.testimonials.testimonial3.position')}
                      </p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Process Section */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {currentLanguage === 'es' ? '¿Cómo funciona el proceso?' : t('mentoriaOnline.sections.process.title')}
              </h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-primary">1</span>
                </div>
                <h3 className="text-xl font-semibold mb-3">
                  {currentLanguage === 'es' ? 'Reserva tu sesión' : t('mentoriaOnline.sections.process.step1.title')}
                </h3>
                <p className="text-muted-foreground">
                  {currentLanguage === 'es' 
                    ? 'Selecciona el plan que mejor se adapte a tus necesidades y reserva tu espacio en nuestro calendario. Nuestra recomendación es que inicialmente contrates una hora. Si son necesarias más sesiones de 2 o 3 horas lo podremos valorar juntos y así podrás aprovechar mejor el tiempo y el conocimiento que podrás adquirir'
                    : t('mentoriaOnline.sections.process.step1.description')
                  }
                </p>
              </div>

              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-primary">2</span>
                </div>
                <h3 className="text-xl font-semibold mb-3">
                  {currentLanguage === 'es' ? 'Completa el cuestionario previo' : t('mentoriaOnline.sections.process.step2.title')}
                </h3>
                <p className="text-muted-foreground">
                  {currentLanguage === 'es' 
                    ? 'Recibirás un formulario para completar 48h antes de la sesión para que podamos prepararnos específicamente para tus necesidades.'
                    : t('mentoriaOnline.sections.process.step2.description')
                  }
                </p>
              </div>

              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-primary">3</span>
                </div>
                <h3 className="text-xl font-semibold mb-3">
                  {currentLanguage === 'es' ? 'Sesión personalizada' : t('mentoriaOnline.sections.process.step3.title')}
                </h3>
                <p className="text-muted-foreground">
                  {currentLanguage === 'es' 
                    ? 'Conectamos por videoconferencia para la sesión de consultoría, donde desarrollaremos estrategias específicas para tu negocio.'
                    : t('mentoriaOnline.sections.process.step3.description')
                  }
                </p>
              </div>

              <div className="text-center">
                <div className="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
                  <span className="text-2xl font-bold text-primary">4</span>
                </div>
                <h3 className="text-xl font-semibold mb-3">
                  {currentLanguage === 'es' ? 'Implementación y seguimiento' : t('mentoriaOnline.sections.process.step4.title')}
                </h3>
                <p className="text-muted-foreground">
                  {currentLanguage === 'es' 
                    ? 'Recibirás un plan de acción detallado y recursos complementarios. Incluimos seguimiento para asegurar resultados.'
                    : t('mentoriaOnline.sections.process.step4.description')
                  }
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* FAQ Section */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {currentLanguage === 'es' ? 'Preguntas Frecuentes' : t('mentoriaOnline.sections.faq.title')}
              </h2>
            </div>
            <div className="max-w-4xl mx-auto">
              <Accordion type="single" collapsible className="w-full space-y-4">
                <AccordionItem value="item-1" className="border border-border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    {currentLanguage === 'es' ? '¿Necesito tener una suscripción activa a AI Chef Pro?' : t('mentoriaOnline.sections.faq.questions.question1.question')}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Sí, necesitas tener una cuenta activa en AI Chef Pro para poder aprovechar al máximo la consultoría. Recomendamos al menos el plan Pro para acceder a la mayoría de las funcionalidades que trabajaremos durante la sesión.'
                      : t('mentoriaOnline.sections.faq.questions.question1.answer')
                    }
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-2" className="border border-border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    {currentLanguage === 'es' ? '¿Qué plataforma se usa para las consultorías?' : t('mentoriaOnline.sections.faq.questions.question2.question')}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Utilizamos Google Meet para las sesiones de consultoría, lo que nos permite compartir pantalla, grabar la sesión (si lo deseas) y tener una comunicación fluida. Recibirás un enlace personalizado tras confirmar tu reserva.'
                      : t('mentoriaOnline.sections.faq.questions.question2.answer')
                    }
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-3" className="border border-border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    {currentLanguage === 'es' ? '¿Cómo me preparo para la sesión?' : t('mentoriaOnline.sections.faq.questions.question3.question')}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Te enviaremos un cuestionario completo 48 horas antes de la sesión. Para aprovechar al máximo, te recomendamos tener claros tus objetivos, acceso a tu cuenta de AI Chef Pro, y cualquier dato relevante de tu negocio (menús actuales, información sobre costes, etc.).'
                      : t('mentoriaOnline.sections.faq.questions.question3.answer')
                    }
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-4" className="border border-border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    {currentLanguage === 'es' ? '¿Cuál es la política de cancelación?' : t('mentoriaOnline.sections.faq.questions.question4.question')}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Puedes reprogramar tu sesión hasta 24 horas antes sin coste adicional. Las cancelaciones con menos de 24 horas de antelación están sujetas a un cargo del 50%. Si necesitas cancelar, contáctanos cuanto antes para buscar la mejor solución.'
                      : t('mentoriaOnline.sections.faq.questions.question4.answer')
                    }
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-5" className="border border-border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    {currentLanguage === 'es' ? '¿Ofrecen garantía de satisfacción?' : t('mentoriaOnline.sections.faq.questions.question5.question')}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Sí, ofrecemos una garantía de satisfacción completa. Si al finalizar los primeros 30 minutos de la sesión consideras que no estás recibiendo el valor esperado, te reembolsaremos el 100% del importe.'
                      : t('mentoriaOnline.sections.faq.questions.question5.answer')
                    }
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-6" className="border border-border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    {currentLanguage === 'es' ? '¿Puedo solicitar una consultoría para un tema muy específico?' : t('mentoriaOnline.sections.faq.questions.question6.question')}
                  </AccordionTrigger>
                  <AccordionContent className="text-muted-foreground">
                    {currentLanguage === 'es' 
                      ? 'Absolutamente. En el formulario previo podrás detallar exactamente qué aspectos específicos quieres trabajar, ya sea una herramienta concreta de AI Chef Pro o un desafío particular de tu negocio.'
                      : t('mentoriaOnline.sections.faq.questions.question6.answer')
                    }
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </div>
          </div>
        </section>

        {/* Final CTA Section */}
        <section className="py-20 bg-gradient-to-r from-primary to-primary/80">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto text-center text-primary-foreground">
              <h2 className="text-3xl font-bold mb-4">
                {currentLanguage === 'es' ? 'Reserva tu Mentoría Online Ahora' : t('mentoriaOnline.sections.final_cta.title')}
              </h2>
              <p className="text-lg mb-8 opacity-90">
                {currentLanguage === 'es' 
                  ? 'Selecciona el tipo de sesión que prefieres y encuentra el momento perfecto para potenciar tu negocio con AI Chef Pro. Aprovecha la inteligencia artificial en tu día a día al máximo.' 
                  : t('mentoriaOnline.sections.final_cta.description')
                }
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <Button 
                  size="lg" 
                  onClick={scrollToCalendly}
                  variant="secondary"
                  className="bg-white text-primary hover:bg-white/90"
                >
                  {currentLanguage === 'es' ? 'Ver Planes de Mentoría' : t('mentoriaOnline.sections.final_cta.button')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </div>
            </div>
          </div>
        </section>

        {/* Free Consultation CTA */}
        <section className="py-16 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center max-w-2xl mx-auto">
              <h2 className="text-2xl font-bold text-foreground mb-4">
                {currentLanguage === 'es' ? '¿No estás seguro de qué paquete elegir?' : t('mentoriaOnline.sections.free_consultation.title')}
              </h2>
              <p className="text-muted-foreground mb-6">
                {currentLanguage === 'es' 
                  ? 'Agenda una micro-sesión gratuita de 15 minutos para discutir tus necesidades y determinar cuál es la mejor opción para tu negocio.' 
                  : t('mentoriaOnline.sections.free_consultation.description')
                }
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button 
                  variant="outline" 
                  onClick={() => window.open('https://calendly.com/john-guerrero-chefbusiness/micro-sesion-gratuita-15-min', '_blank')}
                >
                  {currentLanguage === 'es' ? 'Agendar micro-sesión gratuita' : t('mentoriaOnline.sections.free_consultation.button1')}
                </Button>
                <Button 
                  variant="outline" 
                  onClick={() => window.open('/contacto', '_blank')}
                >
                  {currentLanguage === 'es' ? 'Contactar ahora' : t('mentoriaOnline.sections.free_consultation.button2')}
                </Button>
              </div>
            </div>
          </div>
        </section>
      </main>

      <ModernFooter />
    </div>
  );
};

export default MentoriaOnline;