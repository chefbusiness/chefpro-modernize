import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Star, ArrowRight } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import CounterStat from './CounterStat';
import { useState, useEffect } from 'react';

export default function ModernHero() {
  const { t, getAppUrl, currentLanguage } = useLanguage();
  
  // Get dynamic business types from translations
  const businessTypes = t('hero.business_types', { returnObjects: true }) as string[];
  
  const [currentWordIndex, setCurrentWordIndex] = useState(0);
  const [isAnimating, setIsAnimating] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setIsAnimating(true);
      setTimeout(() => {
        setCurrentWordIndex((prev) => (prev + 1) % businessTypes.length);
        setIsAnimating(false);
      }, 300); // Half of transition duration
    }, 3000); // Change word every 3 seconds

    return () => clearInterval(interval);
  }, [businessTypes.length]);

  const handleCTAClick = () => {
    window.open(getAppUrl(currentLanguage) + '/pricing', '_blank');
  };

  return (
    <section id="inicio" className="container flex max-w-[64rem] flex-col items-center gap-4 pb-8 pt-6 md:pb-12 md:pt-10 lg:py-32">
      <Badge variant="outline" className="px-4 py-1.5">
        {t('hero.badge')}
      </Badge>
      
      <h1 className="text-center text-3xl font-bold leading-tight tracking-tighter md:text-5xl lg:text-6xl lg:leading-[1.1] text-balance">
        {t('hero.title_prefix')}{" "}
        <span 
          className={`inline-block transition-all duration-300 dynamic-hero-text ${
            isAnimating ? 'opacity-0 scale-95' : 'opacity-100 scale-100'
          }`}
        >
          {businessTypes[currentWordIndex]}
        </span>
        {" "}{t('hero.title_suffix')}{" "}
        <span className="gradient-text">{t('hero.title_brand')}</span>
      </h1>
      
      <p className="max-w-[42rem] text-center text-lg text-accent-dark font-semibold sm:text-xl text-balance leading-7 mb-2">
        {t('hero.subtitle')}
      </p>
      
      <p className="max-w-[42rem] text-center text-base text-muted-foreground text-balance leading-6">
        {t('hero.description')}
      </p>

      {/* Counter Stats */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-6 my-6 sm:my-8 p-4 sm:p-6 bg-muted/30 rounded-xl border">
        <CounterStat end={55} suffix="+" label={t('stats.apps_label')} />
        <CounterStat end={25} suffix="+" label={t('stats.cookbooks_label')} />
        <CounterStat end={10} suffix="+" label={t('stats.tools_label')} />
        <CounterStat end={6} suffix="" label={t('stats.categories_label')} />
      </div>

      <div className="flex items-center gap-2 mb-4">
        <div className="flex">
          {Array.from({ length: 5 }).map((_, i) => (
            <Star key={i} className="h-4 w-4 fill-accent text-accent" />
          ))}
        </div>
        <span className="text-sm text-muted-foreground font-medium">
          {t('hero.rating')}
        </span>
      </div>

      <div className="flex flex-col sm:flex-row gap-3 sm:gap-4 animate-fade-up w-full sm:w-auto">
        <Button 
          size="lg" 
          onClick={handleCTAClick}
          className="btn-gold hover:shadow-gold-glow w-full sm:w-auto min-h-[3rem]"
        >
          {t('cta.primary')}
          <ArrowRight className="ml-2 h-4 w-4" />
        </Button>
      <Button 
        size="lg"
        onClick={() => window.open('https://blog.aichef.pro', '_blank')}
        className="btn-gold-outline w-full sm:w-auto min-h-[3rem]"
      >
          {t('hero.see_resources')}
        </Button>
      </div>

    </section>
  );
}