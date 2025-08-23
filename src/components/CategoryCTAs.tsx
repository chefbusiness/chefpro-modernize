import { Button } from '@/components/ui/button';
import { ChefHat, Globe, Calculator, Camera } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';

export default function CategoryCTAs() {
  const { getAppUrl, currentLanguage, t } = useLanguage();

  const ctaButtons = [
    {
      id: 'creativity',
      icon: ChefHat,
      title: t('category_ctas.creativity.title'),
      description: t('category_ctas.creativity.description'),
      path: '/cocina-creativa',
      color: 'from-orange-500 to-red-600'
    },
    {
      id: 'world',
      icon: Globe,
      title: t('category_ctas.world.title'),
      description: t('category_ctas.world.description'),
      path: '/recetarios',
      color: 'from-blue-500 to-cyan-600'
    },
    {
      id: 'business',
      icon: Calculator,
      title: t('category_ctas.business.title'),
      description: t('category_ctas.business.description'),
      path: '/herramientas',
      color: 'from-green-500 to-emerald-600'
    },
    {
      id: 'marketing',
      icon: Camera,
      title: t('category_ctas.marketing.title'),
      description: t('category_ctas.marketing.description'),
      path: '/contenidos',
      color: 'from-purple-500 to-pink-600'
    }
  ];

  const handleCTAClick = (path: string) => {
    window.open(`${getAppUrl(currentLanguage)}${path}`, '_blank');
  };

  return (
    <section id="category-ctas" className="container py-16">
      <div className="text-center mb-12">
        <h2 className="text-3xl font-bold tracking-tight md:text-4xl">
          {t('category_ctas.title_start')} <span className="gradient-text">{t('category_ctas.title_highlight')}</span> {t('category_ctas.title_end')}
        </h2>
        <p className="mt-4 text-lg text-muted-foreground max-w-2xl mx-auto">
          {t('category_ctas.description')}
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        {ctaButtons.map((cta) => {
          const IconComponent = cta.icon;
          
          return (
            <div key={cta.title} className="group relative">
              <div className={`absolute inset-0 bg-gradient-to-r ${cta.color} rounded-lg blur opacity-25 group-hover:opacity-40 transition-opacity duration-300`} />
              <div className="relative bg-background border border-border/50 rounded-lg p-4 sm:p-6 group-hover:border-accent/50 transition-all duration-300 active:scale-95">
                <div className="text-center space-y-3 sm:space-y-4">
                  <div className="mx-auto w-10 h-10 sm:w-12 sm:h-12 bg-accent/10 rounded-lg flex items-center justify-center group-hover:bg-accent/20 transition-colors">
                    <IconComponent className="h-5 w-5 sm:h-6 sm:w-6 text-accent" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-base sm:text-lg mb-2 leading-tight">{cta.title}</h3>
                    <p className="text-xs sm:text-sm text-muted-foreground mb-3 sm:mb-4 leading-relaxed">{cta.description}</p>
                  </div>
                  <Button 
                    className="w-full btn-gold group-hover:shadow-lg text-sm py-2 h-auto min-h-[2.5rem]"
                    onClick={() => handleCTAClick(cta.path)}
                  >
                    {t('category_ctas.cta_button')}
                  </Button>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </section>
  );
}