import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Check } from 'lucide-react';
import { useLanguage } from '@/hooks/useLanguage';
import { Helmet } from 'react-helmet-async';

export default function ModernPricing() {
  const { getAppUrl, currentLanguage, t } = useLanguage();

  const plans = [
    {
      id: 'member',
      name: t('pricing.plans.member.name'),
      price: t('pricing.plans.member.price'),
      uses: t('pricing.plans.member.uses'),
      description: t('pricing.plans.member.description'),
      features: [
        t('pricing.plans.member.features.0'),
        t('pricing.plans.member.features.1'),
        t('pricing.plans.member.features.2'),
        t('pricing.plans.member.features.3')
      ],
      popular: false
    },
    {
      id: 'premium_pro',
      name: t('pricing.plans.premium_pro.name'),
      price: t('pricing.plans.premium_pro.price'),
      period: t('pricing.plans.premium_pro.period'),
      uses: t('pricing.plans.premium_pro.uses'),
      description: t('pricing.plans.premium_pro.description'),
      features: [
        t('pricing.plans.premium_pro.features.0'),
        t('pricing.plans.premium_pro.features.1'),
        t('pricing.plans.premium_pro.features.2'),
        t('pricing.plans.premium_pro.features.3'),
        t('pricing.plans.premium_pro.features.4')
      ],
      popular: false
    },
    {
      id: 'premium_plus',
      name: t('pricing.plans.premium_plus.name'),
      price: t('pricing.plans.premium_plus.price'),
      period: t('pricing.plans.premium_plus.period'),
      uses: t('pricing.plans.premium_plus.uses'),
      description: t('pricing.plans.premium_plus.description'),
      features: [
        t('pricing.plans.premium_plus.features.0'),
        t('pricing.plans.premium_plus.features.1'),
        t('pricing.plans.premium_plus.features.2'),
        t('pricing.plans.premium_plus.features.3'),
        t('pricing.plans.premium_plus.features.4')
      ],
      popular: true
    },
    {
      id: 'premium_max',
      name: t('pricing.plans.premium_max.name'),
      price: t('pricing.plans.premium_max.price'),
      period: t('pricing.plans.premium_max.period'),
      uses: t('pricing.plans.premium_max.uses'),
      description: t('pricing.plans.premium_max.description'),
      unlimitedBadge: t('pricing.unlimited_badge'),
      features: [
        t('pricing.plans.premium_max.features.0'),
        t('pricing.plans.premium_max.features.1'),
        t('pricing.plans.premium_max.features.2'),
        t('pricing.plans.premium_max.features.3'),
        t('pricing.plans.premium_max.features.4'),
        t('pricing.plans.premium_max.features.5'),
        t('pricing.plans.premium_max.features.6')
      ],
      popular: false
    },
    {
      id: 'premium_plus_annual',
      name: t('pricing.plans.premium_plus_annual.name'),
      price: t('pricing.plans.premium_plus_annual.price'),
      period: t('pricing.plans.premium_plus_annual.period'),
      uses: t('pricing.plans.premium_plus_annual.uses'),
      originalPrice: t('pricing.plans.premium_plus_annual.original_price'),
      discount: t('pricing.plans.premium_plus_annual.discount'),
      description: t('pricing.plans.premium_plus_annual.description'),
      features: [
        t('pricing.plans.premium_plus_annual.features.0'),
        t('pricing.plans.premium_plus_annual.features.1'),
        t('pricing.plans.premium_plus_annual.features.2'),
        t('pricing.plans.premium_plus_annual.features.3'),
        t('pricing.plans.premium_plus_annual.features.4'),
        t('pricing.plans.premium_plus_annual.features.5')
      ],
      popular: false,
      isAnnual: true
    }
  ];

  const handlePlanClick = () => {
    window.open(getAppUrl(currentLanguage) + '/pricing', '_blank');
  };

  const pricingSchema = {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "AI Chef Pro Subscription",
    "description": t('seo.description'),
    "brand": {
      "@type": "Brand",
      "name": "AI Chef Pro"
    },
    "offers": plans.map(plan => ({
      "@type": "Offer",
      "name": plan.name,
      "price": plan.price.replace(/[^0-9.]/g, ''),
      "priceCurrency": "EUR",
      "availability": "https://schema.org/InStock",
      "url": "https://aichef.pro"
    }))
  };

  return (
    <section id="pricing" className="container py-8 md:py-12 lg:py-24">
      <Helmet>
        <script type="application/ld+json">
          {JSON.stringify(pricingSchema)}
        </script>
      </Helmet>
      <div className="mx-auto flex max-w-[58rem] flex-col items-center justify-center gap-4 text-center">
        <h2 className="text-3xl font-bold leading-[1.1] sm:text-3xl md:text-5xl text-balance">
          {t('pricing.title')}
        </h2>
        <p className="max-w-[42rem] leading-normal text-muted-foreground sm:text-lg sm:leading-7 text-balance">
          {t('pricing.description')}
        </p>
      </div>

      <div className="grid w-full items-start gap-6 overflow-visible py-12 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5">
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
                className="popular-badge absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-3 py-1"
              >
                🔥 {t('pricing.most_popular')}
              </Badge>
            )}

            {plan.unlimitedBadge && !plan.popular && (
              <Badge 
                variant="default" 
                className="absolute -top-3 left-1/2 -translate-x-1/2 whitespace-nowrap px-3 py-1 shadow-lg"
                style={{ backgroundColor: 'hsl(270, 70%, 50%)', borderColor: 'hsl(270, 70%, 50%)' }}
              >
                ∞ {plan.unlimitedBadge}
              </Badge>
            )}
            
            {plan.discount && (
              <Badge 
                variant="default" 
                className="absolute -top-3 right-4 shadow-lg font-bold"
                style={{ backgroundColor: 'hsl(142, 70%, 40%)', borderColor: 'hsl(142, 70%, 40%)' }}
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
                {plan.uses && (
                  <div className="text-xs text-muted-foreground mt-1">
                    <span className="font-semibold uppercase tracking-wide">USOS: </span>
                    <span className="font-bold text-primary">{plan.uses}</span>
                  </div>
                )}
              </div>
              <CardDescription className="text-sm">{plan.description}</CardDescription>
            </CardHeader>
            
            <CardContent className="grid gap-4">
              <Button 
                onClick={handlePlanClick}
                variant="default"
                className={`w-full transition-all duration-300 ${
                  plan.popular 
                    ? 'btn-gold hover:shadow-gold-glow scale-105' 
                    : 'bg-accent text-accent-foreground hover:bg-accent-dark hover:shadow-lg hover:scale-105 font-semibold'
                }`}
              >
                {plan.price === t('pricing.plans.member.price') ? t('pricing.start_free') : t('pricing.select_plan')}
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
          {t('pricing.enterprise_question')}{" "}
          <a 
            href="#contacto" 
            className="font-medium text-primary hover:underline"
          >
            {t('pricing.contact_us')}
          </a>
        </p>
      </div>
    </section>
  );
}