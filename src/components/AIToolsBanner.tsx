import { ArrowRight, Wrench } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { useLanguage } from '@/hooks/useLanguage';
import { useTranslation } from 'react-i18next';

const AI_TOOLS_SLUGS: Record<string, string> = {
  es: 'herramientas-ia-para-restaurantes',
  en: 'en/ai-tools-for-restaurants',
  fr: 'fr/outils-ia-restaurant',
  de: 'de/ki-tools-restaurant',
  it: 'it/strumenti-ia-ristorante',
  pt: 'pt/ferramentas-ia-restaurante',
  nl: 'nl/ai-tools-restaurant',
};

export default function AIToolsBanner() {
  const { currentLanguage } = useLanguage();
  const { t } = useTranslation();
  const href = `/${AI_TOOLS_SLUGS[currentLanguage] || AI_TOOLS_SLUGS.es}`;

  return (
    <section className="py-12 bg-gradient-to-r from-amber-50 to-primary/5 border-y border-primary/10">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row items-center justify-between gap-6 max-w-5xl mx-auto">
          <div className="flex items-start gap-4">
            <div className="w-12 h-12 bg-primary/10 rounded-xl flex items-center justify-center flex-shrink-0">
              <Wrench className="h-6 w-6 text-primary" />
            </div>
            <div>
              <h2 className="text-xl font-bold text-foreground">
                {t('nav.herramientas_ia')}
              </h2>
              <p className="text-muted-foreground text-sm mt-1 max-w-xl">
                {t('landingRestaurantes.hero.subtitle')}
              </p>
            </div>
          </div>
          <Button
            asChild
            className="btn-gold flex-shrink-0"
            size="lg"
          >
            <a href={href}>
              {t('landingRestaurantes.hero.cta_primary')}
              <ArrowRight className="ml-2 h-5 w-5" />
            </a>
          </Button>
        </div>
      </div>
    </section>
  );
}
