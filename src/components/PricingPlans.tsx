import { useTranslation } from 'react-i18next';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { useLanguage } from '@/hooks/useLanguage';

const APP_URL_MAP: Record<string, string> = {
  es: 'https://app.aichef.pro',
  en: 'https://app.aichef.pro',
  fr: 'https://app.aichef.pro',
  de: 'https://app.aichef.pro',
  it: 'https://app.aichef.pro',
  pt: 'https://app.aichef.pro',
  nl: 'https://app.aichef.pro',
};

interface PricingPlansProps {
  toolKey: string;
}

export default function PricingPlans({ toolKey }: PricingPlansProps) {
  const { t } = useTranslation();
  const { currentLanguage } = useLanguage();

  const pricing = t(`${toolKey}.pricing`, { returnObjects: true }) as any;
  const plans = pricing?.plans as Array<{ name: string; price: string; uses: string; highlight: boolean }> | undefined;
  const primaryBtn = t(`${toolKey}.cta_section.primary`);
  const secondaryBtn = t(`${toolKey}.cta_section.secondary`);

  if (!pricing || !plans || !plans.length) return null;

  const appUrl = APP_URL_MAP[currentLanguage] ?? APP_URL_MAP.es;

  return (
    <section className="py-20 bg-gradient-to-b from-muted/20 to-muted/50">
      <div className="container mx-auto px-4 text-center">
        <h2 className="text-3xl font-bold text-foreground mb-4">{pricing.title}</h2>
        <p className="text-lg text-muted-foreground mb-12 max-w-2xl mx-auto">{pricing.subtitle}</p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto mb-10">
          {plans.map((plan, i) => (
            <Card
              key={i}
              className={`text-center relative ${
                plan.highlight
                  ? 'ring-2 ring-amber-400 shadow-2xl scale-105 bg-gradient-to-b from-amber-50 to-white'
                  : 'shadow-md bg-card'
              }`}
            >
              {plan.highlight && (
                <Badge className="absolute -top-3 left-1/2 -translate-x-1/2 bg-amber-400 text-amber-950 border-0">
                  ⭐ Popular
                </Badge>
              )}
              <CardHeader className="pt-6">
                <CardTitle className={`text-lg ${plan.highlight ? 'text-amber-900' : ''}`}>
                  {plan.name}
                </CardTitle>
                <div className={`text-3xl font-bold ${plan.highlight ? 'text-amber-600' : 'text-primary'}`}>
                  {plan.price}
                </div>
                <div className="text-sm text-muted-foreground">{plan.uses}</div>
              </CardHeader>
              <CardContent>
                <Button
                  className={`w-full ${plan.highlight ? 'btn-gold' : ''}`}
                  variant={plan.highlight ? 'default' : 'outline'}
                  onClick={() => window.open(`${appUrl}/pricing`, '_blank')}
                >
                  {plan.highlight ? primaryBtn : secondaryBtn}
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
