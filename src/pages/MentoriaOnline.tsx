import { useTranslation } from 'react-i18next';
import ModernHeader from '@/components/ModernHeader';
import ModernFooter from '@/components/ModernFooter';
import SEOHead from '@/components/SEOHead';
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle, Clock, Users, Star, ArrowRight, BookOpen, Target, Zap } from 'lucide-react';

const MentoriaOnline = () => {
  const { t } = useTranslation();

  const handleCTAClick = () => {
    window.open('https://app.aichef.pro/mentoria-online', '_blank');
  };

  const benefits = [
    { icon: BookOpen, key: 'personalized' },
    { icon: Target, key: 'goals' },
    { icon: Zap, key: 'accelerated' },
    { icon: Users, key: 'network' }
  ];

  const features = [
    { icon: CheckCircle, key: 'ai_integration' },
    { icon: CheckCircle, key: 'practical_sessions' },
    { icon: CheckCircle, key: 'business_strategy' },
    { icon: CheckCircle, key: 'marketing_digital' },
    { icon: CheckCircle, key: 'menu_optimization' },
    { icon: CheckCircle, key: 'cost_management' }
  ];

  const testimonials = [
    { key: 'testimonial_1' },
    { key: 'testimonial_2' },
    { key: 'testimonial_3' }
  ];

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
              <Badge variant="secondary" className="mb-6">
                {t('pages.mentoria.hero.badge')}
              </Badge>
              <h1 className="text-4xl font-bold tracking-tight text-foreground sm:text-6xl lg:text-7xl mb-6">
                {t('pages.mentoria.hero.title')}
              </h1>
              <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
                {t('pages.mentoria.hero.subtitle')}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
                <Button size="lg" onClick={handleCTAClick} className="bg-primary text-primary-foreground hover:bg-primary/90">
                  {t('pages.mentoria.hero.cta')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <div className="flex items-center gap-2 text-sm text-muted-foreground">
                  <div className="flex">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                    ))}
                  </div>
                  <span>{t('pages.mentoria.hero.rating')}</span>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Benefits Section */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('pages.mentoria.benefits.title')}
              </h2>
              <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
                {t('pages.mentoria.benefits.subtitle')}
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
              {benefits.map((benefit) => (
                <Card key={benefit.key} className="text-center border-none shadow-lg hover:shadow-xl transition-shadow">
                  <CardHeader>
                    <div className="mx-auto w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mb-4">
                      <benefit.icon className="h-8 w-8 text-primary" />
                    </div>
                    <CardTitle className="text-xl">
                      {t(`pages.mentoria.benefits.items.${benefit.key}.title`)}
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-muted-foreground">
                      {t(`pages.mentoria.benefits.items.${benefit.key}.description`)}
                    </p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* What's Included Section */}
        <section className="py-20">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto">
              <div className="text-center mb-16">
                <h2 className="text-3xl font-bold text-foreground mb-4">
                  {t('pages.mentoria.features.title')}
                </h2>
                <p className="text-lg text-muted-foreground">
                  {t('pages.mentoria.features.subtitle')}
                </p>
              </div>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {features.map((feature) => (
                  <div key={feature.key} className="flex items-start gap-4 p-6 rounded-lg bg-muted/30">
                    <feature.icon className="h-6 w-6 text-primary mt-1 flex-shrink-0" />
                    <div>
                      <h3 className="font-semibold text-foreground mb-2">
                        {t(`pages.mentoria.features.items.${feature.key}.title`)}
                      </h3>
                      <p className="text-muted-foreground">
                        {t(`pages.mentoria.features.items.${feature.key}.description`)}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Testimonials Section */}
        <section className="py-20 bg-muted/30">
          <div className="container mx-auto px-4">
            <div className="text-center mb-16">
              <h2 className="text-3xl font-bold text-foreground mb-4">
                {t('pages.mentoria.testimonials.title')}
              </h2>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
              {testimonials.map((testimonial) => (
                <Card key={testimonial.key} className="border-none shadow-lg">
                  <CardContent className="p-6">
                    <div className="flex mb-4">
                      {[...Array(5)].map((_, i) => (
                        <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                      ))}
                    </div>
                    <p className="text-muted-foreground mb-4 italic">
                      "{t(`pages.mentoria.testimonials.items.${testimonial.key}.quote`)}"
                    </p>
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center">
                        <span className="text-primary font-semibold">
                          {t(`pages.mentoria.testimonials.items.${testimonial.key}.name`).charAt(0)}
                        </span>
                      </div>
                      <div>
                        <p className="font-semibold text-foreground">
                          {t(`pages.mentoria.testimonials.items.${testimonial.key}.name`)}
                        </p>
                        <p className="text-sm text-muted-foreground">
                          {t(`pages.mentoria.testimonials.items.${testimonial.key}.role`)}
                        </p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="py-20 bg-gradient-to-r from-primary to-primary/80">
          <div className="container mx-auto px-4">
            <div className="max-w-4xl mx-auto text-center text-primary-foreground">
              <h2 className="text-3xl font-bold mb-4">
                {t('pages.mentoria.cta.title')}
              </h2>
              <p className="text-lg mb-8 opacity-90">
                {t('pages.mentoria.cta.subtitle')}
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <Button 
                  size="lg" 
                  onClick={handleCTAClick}
                  variant="secondary"
                  className="bg-white text-primary hover:bg-white/90"
                >
                  {t('pages.mentoria.cta.button')}
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
                <div className="flex items-center gap-2 text-sm opacity-75">
                  <Clock className="h-4 w-4" />
                  <span>{t('pages.mentoria.cta.availability')}</span>
                </div>
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