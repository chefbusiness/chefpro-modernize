import { useTranslation } from 'react-i18next';
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

  const scrollToCalendly = () => {
    const calendlySection = document.getElementById('calendly-section');
    if (calendlySection) {
      calendlySection.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-background">
      <SEOHead 
        title={t('pages.mentoria.seo.title')}
        description={t('pages.mentoria.seo.description')}
        keywords={t('pages.mentoria.seo.keywords')}
      />
      <ModernHeader />
      
      <main>
        {/* Hero Section */}
        <section className="relative overflow-hidden bg-gradient-to-br from-primary/10 via-background to-secondary/5 py-20 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="mx-auto max-w-4xl text-center">
              <Badge variant="secondary" className="mb-6 text-lg px-6 py-2">
                {t('pages.mentoria.hero.badge')}
              </Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-6xl lg:text-7xl mb-6">
                {t('pages.mentoria.hero.title')}
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
                {t('pages.mentoria.hero.subtitle')}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" onClick={scrollToCalendly} className="bg-primary text-primary-foreground hover:bg-primary/90">
                  {t('pages.mentoria.hero.cta')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </div>
              <p className="text-sm text-muted-foreground mt-4">
                ⭐ {t('pages.mentoria.hero.rating')}
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
                  {t('nav.mentoria_online')}
                </h2>
                <h3 className="text-2xl font-semibold text-primary mb-4">
                  {t('pages.mentoria.benefits.subtitle')}
                </h3>
                <p className="text-lg text-muted-foreground mb-8">
                  {t('pages.mentoria.features.subtitle')}
                </p>
                <Button size="lg" onClick={scrollToCalendly} className="bg-primary text-primary-foreground hover:bg-primary/90">
                  {t('pages.mentoria.hero.cta')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </div>
              <div className="relative">
                <img 
                  src="https://blog.aichef.pro/wp-content/uploads/2025/03/Untitled-design.jpeg" 
                  alt={t('pages.mentoria.hero.title')}
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
                {t('pages.mentoria.benefits.title')}
              </h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-6xl mx-auto">
              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <TrendingUp className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{t('pages.mentoria.benefits.items.accelerated.title')}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.benefits.items.accelerated.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Target className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{t('pages.mentoria.benefits.items.goals.title')}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.benefits.items.goals.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <Users className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{t('pages.mentoria.benefits.items.personalized.title')}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.benefits.items.personalized.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                    <BookOpen className="h-8 w-8 text-primary" />
                  </div>
                  <CardTitle className="text-xl">{t('pages.mentoria.benefits.items.network.title')}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.benefits.items.network.description')}
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Pricing Plans Section */}
        <section className="py-20 bg-muted/50" id="calendly-section">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('pricing.title')}
              </h2>
              <p className="text-xl text-muted-foreground">
                {t('pricing.description')}
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
              {/* Plan Express */}
              <Card className="relative border-2 border-muted hover:border-primary/50 transition-colors">
                <CardHeader className="text-center">
                  <CardTitle className="text-2xl font-bold">Express</CardTitle>
                  <CardDescription className="text-lg">
                    {t('pricing.plans.express.subtitle')}
                  </CardDescription>
                  <div className="mt-4">
                    <span className="text-4xl font-bold">€150</span>
                    <span className="text-muted-foreground ml-2">/sesión</span>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.express.features.0')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.express.features.1')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.express.features.2')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.express.features.3')}</span>
                    </li>
                  </ul>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/johnito9/mentoria-express-ai-chef-pro-150" target="_blank" rel="noopener noreferrer">
                      {t('pricing.plans.express.cta')}
                    </a>
                  </Button>
                </CardContent>
              </Card>

              {/* Plan Estándar */}
              <Card className="relative border-2 border-primary popular-plan">
                <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                  <Badge className="popular-badge">
                    {t('pricing.popular')}
                  </Badge>
                </div>
                <CardHeader className="text-center pt-6">
                  <CardTitle className="text-2xl font-bold">Estándar</CardTitle>
                  <CardDescription className="text-lg">
                    {t('pricing.plans.standard.subtitle')}
                  </CardDescription>
                  <div className="mt-4">
                    <span className="text-4xl font-bold">€275</span>
                    <span className="text-muted-foreground ml-2">/sesión</span>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.standard.features.0')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.standard.features.1')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.standard.features.2')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.standard.features.3')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.standard.features.4')}</span>
                    </li>
                  </ul>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/johnito9/mentoria-estandar-ai-chef-pro-275" target="_blank" rel="noopener noreferrer">
                      {t('pricing.plans.standard.cta')}
                    </a>
                  </Button>
                </CardContent>
              </Card>

              {/* Plan Intensiva */}
              <Card className="relative border-2 border-muted hover:border-primary/50 transition-colors">
                <CardHeader className="text-center">
                  <CardTitle className="text-2xl font-bold">Intensiva</CardTitle>
                  <CardDescription className="text-lg">
                    {t('pricing.plans.intensive.subtitle')}
                  </CardDescription>
                  <div className="mt-4">
                    <span className="text-4xl font-bold">€360</span>
                    <span className="text-muted-foreground ml-2">/sesión</span>
                  </div>
                </CardHeader>
                <CardContent className="space-y-4">
                  <ul className="space-y-2">
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.intensive.features.0')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.intensive.features.1')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.intensive.features.2')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.intensive.features.3')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.intensive.features.4')}</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-5 w-5 text-green-500 mr-2" />
                      <span>{t('pricing.plans.intensive.features.5')}</span>
                    </li>
                  </ul>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/johnito9/mentoria-intensiva-ai-chef-pro-360" target="_blank" rel="noopener noreferrer">
                      {t('pricing.plans.intensive.cta')}
                    </a>
                  </Button>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Specialized Mentoring Section */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('pages.mentoria.features.title')}
              </h2>
              <p className="text-xl text-muted-foreground">
                {t('pages.mentoria.features.subtitle')}
              </p>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                      <Zap className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{t('pages.mentoria.features.items.ai_integration.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.features.items.ai_integration.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                      <BookOpen className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{t('pages.mentoria.features.items.practical_sessions.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.features.items.practical_sessions.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                      <TrendingUp className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{t('pages.mentoria.features.items.business_strategy.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.features.items.business_strategy.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                      <Search className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{t('pages.mentoria.features.items.marketing_digital.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.features.items.marketing_digital.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                      <Target className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{t('pages.mentoria.features.items.menu_optimization.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.features.items.menu_optimization.description')}
                  </p>
                </CardContent>
              </Card>

              <Card className="border-none shadow-lg hover:shadow-xl transition-shadow">
                <CardHeader>
                  <div className="flex items-center space-x-3">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                      <Timer className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-xl">{t('pages.mentoria.features.items.cost_management.title')}</CardTitle>
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">
                    {t('pages.mentoria.features.items.cost_management.description')}
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* Testimonials Section */}
        <section className="py-20 bg-muted/50">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('pages.mentoria.testimonials.title')}
              </h2>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
              <Card className="border-none shadow-lg">
                <CardContent className="p-6">
                  <div className="flex items-center mb-4">
                    {[1,2,3,4,5].map((star) => (
                      <Star key={star} className="h-5 w-5 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <blockquote className="text-muted-foreground mb-4">
                    "{t('pages.mentoria.testimonials.items.testimonial_1.quote')}"
                  </blockquote>
                  <div className="flex items-center space-x-3">
                    <div className="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center">
                      <span className="text-sm font-semibold text-primary">CM</span>
                    </div>
                    <div>
                      <p className="font-semibold text-sm">{t('pages.mentoria.testimonials.items.testimonial_1.name')}</p>
                      <p className="text-xs text-muted-foreground">{t('pages.mentoria.testimonials.items.testimonial_1.role')}</p>
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
                    "{t('pages.mentoria.testimonials.items.testimonial_2.quote')}"
                  </blockquote>
                  <div className="flex items-center space-x-3">
                    <div className="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center">
                      <span className="text-sm font-semibold text-primary">AR</span>
                    </div>
                    <div>
                      <p className="font-semibold text-sm">{t('pages.mentoria.testimonials.items.testimonial_2.name')}</p>
                      <p className="text-xs text-muted-foreground">{t('pages.mentoria.testimonials.items.testimonial_2.role')}</p>
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
                    "{t('pages.mentoria.testimonials.items.testimonial_3.quote')}"
                  </blockquote>
                  <div className="flex items-center space-x-3">
                    <div className="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center">
                      <span className="text-sm font-semibold text-primary">DF</span>
                    </div>
                    <div>
                      <p className="font-semibold text-sm">{t('pages.mentoria.testimonials.items.testimonial_3.name')}</p>
                      <p className="text-xs text-muted-foreground">{t('pages.mentoria.testimonials.items.testimonial_3.role')}</p>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>

        {/* FAQ Section */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('faq.title')}
              </h2>
            </div>
            
            <div className="max-w-3xl mx-auto">
              <Accordion type="single" collapsible className="space-y-4">
                <AccordionItem value="item-1" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Qué incluye exactamente cada sesión de mentoría?
                  </AccordionTrigger>
                  <AccordionContent>
                    Cada sesión incluye una consulta personalizada donde analizamos tus objetivos específicos, revisamos tu uso actual de AI Chef Pro, identificamos oportunidades de mejora y creamos un plan de acción concreto. También recibes materiales de apoyo y seguimiento por email.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-2" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Necesito tener experiencia previa con IA para aprovechar la mentoría?
                  </AccordionTrigger>
                  <AccordionContent>
                    No es necesario. Nuestras mentorías están diseñadas para todos los niveles, desde principiantes hasta usuarios avanzados. Adaptamos el contenido a tu nivel actual y te guiamos paso a paso.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-3" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Cuál es la diferencia entre los planes Express, Estándar e Intensiva?
                  </AccordionTrigger>
                  <AccordionContent>
                    El plan Express (90 min) se enfoca en consultas específicas y resolución rápida de dudas. El Estándar (120 min) incluye análisis más profundo y estrategias personalizadas. El Intensiva (180 min) es la opción más completa con análisis exhaustivo, plan de implementación detallado y seguimiento extendido.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-4" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Las sesiones son virtuales o presenciales?
                  </AccordionTrigger>
                  <AccordionContent>
                    Todas las sesiones son virtuales a través de videollamada, lo que te permite acceder desde cualquier lugar del mundo. Esto también nos permite grabar la sesión (con tu consentimiento) para que puedas revisarla después.
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="item-5" className="border rounded-lg px-6">
                  <AccordionTrigger className="text-left">
                    ¿Puedo agendar múltiples sesiones?
                  </AccordionTrigger>
                  <AccordionContent>
                    Sí, puedes agendar tantas sesiones como necesites. Muchos de nuestros mentores trabajan con planes mensuales o trimestrales para obtener mejores resultados a largo plazo.
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </div>
          </div>
        </section>

        {/* Final CTA Section */}
        <section className="py-20 bg-gradient-to-r from-primary/10 to-secondary/10">
          <div className="container mx-auto px-4 text-center">
            <div className="max-w-3xl mx-auto">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('pages.mentoria.cta.title')}
              </h2>
              <p className="text-xl text-muted-foreground mb-8">
                {t('pages.mentoria.cta.subtitle')}
              </p>
              <Button size="lg" onClick={scrollToCalendly} className="bg-primary text-primary-foreground hover:bg-primary/90 mr-4">
                {t('pages.mentoria.cta.button')}
                <ArrowRight className="ml-2 h-5 w-5" />
              </Button>
              <p className="text-sm text-muted-foreground mt-4">
                📅 {t('pages.mentoria.cta.availability')}
              </p>
            </div>
          </div>
        </section>

        {/* Free 15min Session */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto text-center">
              <h2 className="text-3xl font-bold text-foreground mb-6">
                ¿No estás seguro? ¡Comienza con una Micro-Sesión GRATUITA!
              </h2>
              <p className="text-lg text-muted-foreground mb-8">
                15 minutos gratis para conocernos y ver si podemos ayudarte a maximizar tu potencial con AI Chef Pro
              </p>
              <Card className="max-w-md mx-auto border-primary/20 shadow-lg">
                <CardHeader className="text-center">
                  <Badge variant="secondary" className="mb-2 bg-green-100 text-green-800">GRATIS</Badge>
                  <CardTitle className="text-xl">Micro-Sesión Gratuita</CardTitle>
                  <CardDescription>15 minutos para conocernos</CardDescription>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2 text-sm text-left mb-6">
                    <li className="flex items-center">
                      <CheckCircle className="h-4 w-4 text-green-500 mr-2" />
                      <span>Evaluación rápida de tu situación</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-4 w-4 text-green-500 mr-2" />
                      <span>Recomendaciones iniciales</span>
                    </li>
                    <li className="flex items-center">
                      <CheckCircle className="h-4 w-4 text-green-500 mr-2" />
                      <span>Sin compromiso</span>
                    </li>
                  </ul>
                  <Button className="w-full btn-gold text-black hover:bg-yellow-400" asChild>
                    <a href="https://calendly.com/johnito9/micro-sesion-gratis-ai-chef-pro-15min" target="_blank" rel="noopener noreferrer">
                      Reservar Gratis
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