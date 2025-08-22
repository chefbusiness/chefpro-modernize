import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Star, ArrowRight } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import CounterStat from './CounterStat';

export default function ModernHero() {
  const { t, getAppUrl, currentLanguage } = useLanguage();

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage) + '/pricing', '_blank');
  };

  return (
    <section id="inicio" className="container flex max-w-[64rem] flex-col items-center gap-4 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
      <Badge variant="outline" className="px-4 py-1.5">
        Nuevo: Inteligencia Artificial para Chefs
      </Badge>
      
      <h1 className="text-center text-3xl font-bold leading-tight tracking-tighter md:text-5xl lg:text-6xl lg:leading-[1.1] text-balance">
        {t.hero.title.split(' ').slice(0, -3).join(' ')}{" "}
        <span className="gradient-text">AI Chef Pro</span>
      </h1>
      
      <p className="max-w-[42rem] text-center text-lg text-accent-dark font-semibold sm:text-xl text-balance leading-7 mb-2">
        {t.hero.subtitle}
      </p>
      
      <p className="max-w-[42rem] text-center text-base text-muted-foreground text-balance leading-6">
        {t.hero.description}
      </p>

      {/* Counter Stats */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-6 my-6 sm:my-8 p-4 sm:p-6 bg-muted/30 rounded-xl border">
        <CounterStat end={55} suffix="+" label="Apps Especializadas" />
        <CounterStat end={25} suffix="+" label="Recetarios Regionales" />
        <CounterStat end={10} suffix="+" label="Herramientas de Negocio" />
        <CounterStat end={6} suffix="" label="Categorías Profesionales" />
      </div>

      <div className="flex items-center gap-2 mb-4">
        <div className="flex">
          {Array.from({ length: 5 }).map((_, i) => (
            <Star key={i} className="h-4 w-4 fill-accent text-accent" />
          ))}
        </div>
        <span className="text-sm text-muted-foreground font-medium">
          {t.hero.rating}
        </span>
      </div>

      <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 animate-fade-up w-full sm:w-auto">
        <Button 
          size="lg" 
          onClick={handleCTAClick}
          className="btn-gold hover:shadow-gold-glow w-full sm:w-auto min-h-[3rem]"
        >
          {t.cta.primary}
          <ArrowRight className="ml-2 h-4 w-4" />
        </Button>
        <Button 
          variant="outline" 
          size="lg"
          onClick={() => window.open('https://blog.aichef.pro', '_blank')}
          className="btn-gold-outline w-full sm:w-auto min-h-[3rem]"
        >
          Ver Recursos
        </Button>
      </div>

    </section>
  );
}